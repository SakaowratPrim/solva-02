# -*- coding: utf-8 -*-
from core import *

body = ('<div class="app">' + nav('Services') + '<main class="mn">' + header() +
 hero(hero_svg('Main.dc.html'),
      'บริการทั้งหมด <b class="cn" style="--v:{{nSv}}"></b> รายการ', '{{heroSub}}',
      '<button class="bt" onClick="{{add}}">{{heroBtn}}</button>') + WARN +
 '<h1>บริการและราคา</h1>'
 '<sc-if value="{{hasAny}}" hint-placeholder-val="{{true}}"><div class="row"><input class="si" placeholder="ค้นหาบริการ" aria-label="ค้นหาบริการ" value="{{q}}" onInput="{{onQ}}">'
 '<select class="sel2" value="{{cat}}" onChange="{{onCat}}" aria-label="กรองหมวดหมู่"><sc-for list="{{catOpts}}" as="o"><option value="{{o.v}}">{{o.t}}</option></sc-for></select>'
 '</div>'
 '<div class="c rt" style="overflow-x:auto"><table><tr><th>บริการ</th><th>หมวด</th><th>ราคา</th><th>เวลา</th><th>ใช้ในนัดหมาย</th></tr>'
 '<sc-for list="{{rows}}" as="r" hint-placeholder-count="3"><tr><td><button class="nb2" onClick="{{r.pick}}">{{r.name}}</button></td><td>{{r.cat}}</td><td><b>{{r.price}}</b></td><td>{{r.dur}}</td><td>{{r.used}}</td></tr></sc-for></table>'
 '<sc-if value="{{noRows}}"><div class="em"><div>ไม่พบบริการที่ตรงกับตัวกรอง</div></div></sc-if></div></sc-if>'
 '<sc-if value="{{noAny}}" hint-placeholder-val="{{false}}"><div class="empty">' + HEART +
 '<h2>ยังไม่มีบริการ</h2><p>เพิ่มบริการที่ร้านให้ เช่น ทาสีเจล ต่อเล็บ พร้อมราคาและเวลาที่ใช้ เพื่อนำไปสร้างนัดหมายและบิลได้</p>'
 '</div></sc-if>'
 + MODAL + '</main></div>')

js = r"""
const SV_CATS=['เล็บมือ','เล็บเท้า','ต่อเล็บ','ทำสปา','ตกแต่งเล็บ','ถอด/ซ่อม'],SV_NAMES=['ทาสีเจล','ล้างเจล','ต่อเล็บ','เพ้นท์ลาย','ทำสปามือ','ทำสปาเท้า'];
const svSpec=(cats)=>[{k:'name',label:'ชื่อบริการ (เลือกด้านล่างหรือพิมพ์เองก็ได้)',full:1,ph:'เช่น ทาสีเจล',quick:SV_NAMES},{k:'cat',label:'หมวดหมู่ (ไม่บังคับ)',full:1,ph:'เลือกด้านล่างหรือพิมพ์หมวดของร้านเอง',quick:[...new Set(cats.concat(SV_CATS))]},{k:'price',label:'ราคา (บาท)',type:'number',ph:'0',quick:[200,300,500,800,1000]},{k:'dur',label:'เวลาที่ใช้ (นาที)',type:'number',ph:'ไม่บังคับ',unit:'นาที',quick:[30,45,60,90,120]}];
class Component extends Base{
boot(){const u=uiGet();if(u.open==='sv'){uiSet({open:''});this.setState({form:{_k:'sv',name:'',cat:'',price:'',dur:''},fe:''})}}
renderVals(){
const d=load(),S=Object.assign({q:'',cat:'all',form:null,fe:'',cdel:false,to:''},this.state),set=o=>this.setState(o);
const used=id=>d.appts.filter(a=>a.items.some(i=>i.sid===id)).length,q=S.q.trim();
const cats=[...new Set(d.services.map(s=>s.cat).filter(Boolean))];
const list=d.services.filter(s=>(S.cat==='all'||s.cat===S.cat)&&(!q||s.name.includes(q)));
const rows=list.map(s=>({name:s.name,cat:s.cat||'—',price:fm(s.price),dur:s.dur?s.dur+' นาที':'—',used:used(s.id)+' ครั้ง',pick:()=>set({form:{_k:'sv',id:s.id,name:s.name,cat:s.cat||'',price:s.price,dur:s.dur||''},fe:'',cdel:false})}));
const F=S.form,k=F&&F._k;let mo={};
if(k==='shop')mo=shopMo(this,F,S);
if(k==='sv')mo={title:F.id?'แก้ไขบริการ':'เพิ่มบริการ',hint:F.id?'การแก้ราคาไม่กระทบนัดหมายเดิมที่บันทึกไว้แล้ว':'',spec:svSpec(cats),saveTxt:F.id?'บันทึกการแก้ไข':'เพิ่มบริการ',
save:()=>{const name=(F.name||'').trim(),price=F.price===''||F.price==null?NaN:+F.price,dur=+F.dur||0;
if(!name)return set({fe:'กรุณากรอกชื่อบริการ'});if(isNaN(price)||price<0)return set({fe:'กรุณากรอกราคา (ตัวเลข 0 ขึ้นไป)'});
if(d.services.some(s=>s.name===name&&s.id!==F.id))return set({fe:'มีบริการชื่อนี้อยู่แล้ว'});
M(x=>{if(F.id){const s=x.services.find(z=>z.id===F.id);s.name=name;s.cat=(F.cat||'').trim();s.price=price;s.dur=dur}else x.services.push({id:x.seq++,name,cat:(F.cat||'').trim(),price,dur})});
set({form:null,fe:''});this.toast(F.id?'บันทึกการแก้ไขแล้ว':'เพิ่มบริการแล้ว')},
del:F.id?(()=>{if(!S.cdel)return set({cdel:true});M(x=>{x.services=x.services.filter(s=>s.id!==F.id)});set({form:null,cdel:false});this.toast('ลบบริการแล้ว')}):null,delTxt:'ลบบริการ'};
const n=d.services.length;
return{today:thL(TODAY()),noStore:!OKS,openShop:()=>openShopForm(this),nSv:n,
heroSub:n?'ตั้งราคาครั้งเดียว ใช้ได้ทั้งนัดหมายและบิล':'เริ่มต้นด้วยการเพิ่มบริการแรกของร้าน พร้อมราคา',heroBtn:n?'+ เพิ่มบริการ':'เพิ่มบริการ',
add:()=>set({form:{_k:'sv',name:'',cat:'',price:'',dur:''},fe:'',cdel:false}),
q:S.q,onQ:e=>set({q:e.target.value}),cat:S.cat,onCat:e=>set({cat:e.target.value}),catOpts:[{v:'all',t:'ทุกหมวดหมู่'}].concat(cats.map(c=>({v:c,t:c}))),
rows,hasAny:n>0,noAny:n===0,noRows:n>0&&rows.length===0,fm:modalOf(this,S,mo),toast:S.to,toastText:S.to}}}
"""

html = page('Solva – บริการ', helmet_css('Staff.dc.html') + '.nb2{border:0;background:none;font:inherit;font-weight:600;cursor:pointer;text-align:left;padding:0;color:inherit;text-decoration:underline dotted}', body, js)
write('Services.dc.html', html)
