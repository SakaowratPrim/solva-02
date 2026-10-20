# -*- coding: utf-8 -*-
from core import *

FAB = '<button class="fab" aria-label="บันทึกสต็อกเข้า–ออก" onClick="{{mv}}"><svg width="32" height="32" viewBox="0 0 32 32" stroke="#FF9AFF" stroke-width="3" stroke-linecap="round"><path d="M16 5v22M5 16h22"></path></svg></button>'

body = ('<div class="app">' + nav('Inventory') + '<main class="mn">' + header() +
 hero(hero_svg('Inventory.dc.html'), '{{heroT}} <b class="cn" style="--v:{{nLow}}"></b> รายการ', '{{heroSub}}', '<button class="bt" onClick="{{heroGo}}">{{heroBtn}}</button>') + WARN +
 '<h1>สต็อกสินค้า</h1><sc-if value="{{hasLow}}"><div class="wn">⚠ Low Stock: ใกล้หมด {{nWarn}} รายการ · หมด {{nOut}} รายการ ควรสั่งซื้อเพิ่ม</div></sc-if>'
 '<div class="g"><div class="c lf rs" style="--i:4"><div class="kl">ปกติ</div><div class="k"><b class="cn" style="--v:{{nOk}}"></b></div></div><div class="c lf rs" style="--i:5"><div class="kl">ใกล้หมด</div><div class="k"><b class="cn" style="--v:{{nWarn}}"></b></div></div><div class="c lf rs" style="--i:6"><div class="kl">หมด</div><div class="k"><b class="cn" style="--v:{{nOut}}"></b></div></div></div>'
 '<sc-if value="{{noAny}}" hint-placeholder-val="{{false}}"><div class="empty">' + HEART +
 '<h2>ยังไม่มีข้อมูลสินค้า</h2><p>เพิ่มสินค้าและวัสดุที่ใช้ในร้าน เช่น สีเจล ตะไบ น้ำยา พร้อมจำนวนคงเหลือและจำนวนขั้นต่ำ ระบบจะเตือนเมื่อใกล้หมด</p></div></sc-if>'
 '<sc-if value="{{hasAny}}" hint-placeholder-val="{{true}}"><div class="row"><select class="sel2" value="{{cat}}" onChange="{{onCat}}" aria-label="กรองหมวดหมู่"><sc-for list="{{catOpts}}" as="o"><option value="{{o.v}}">{{o.t}}</option></sc-for></select>'
 '<button class="bt" style="margin-left:auto" onClick="{{add}}">+ เพิ่มสินค้า</button><button class="bt d" onClick="{{mv}}">บันทึกสต็อกเข้า–ออก</button></div>'
 '<div class="g2"><div class="c rt" style="overflow-x:auto"><table><tr><th>สินค้า</th><th>SKU</th><th>หมวด</th><th>คงเหลือ</th><th>ขั้นต่ำ</th><th>สถานะ</th></tr>'
 '<sc-for list="{{rows}}" as="r" hint-placeholder-count="3"><tr><td data-label="สินค้า"><button class="lk" onClick="{{r.pick}}">{{r.name}}</button></td><td data-label="SKU">{{r.sku}}</td><td data-label="หมวด">{{r.cat}}</td><td data-label="คงเหลือ"><b>{{r.qty}}</b> {{r.unit}}<div class="mt {{r.sc}}"><i style="width:{{r.w}}%"></i></div></td><td data-label="ขั้นต่ำ">{{r.min}}</td><td data-label="สถานะ"><span class="ch {{r.sc}}">{{r.st}}</span></td></tr></sc-for></table>'
 '<sc-if value="{{noRows}}"><div class="em"><div>ไม่พบสินค้าในหมวดนี้</div></div></sc-if></div>'
 '<div class="c"><h2>ประวัติการเคลื่อนไหว</h2><sc-for list="{{hist}}" as="h"><div class="ap">{{h.t}}<br><small>{{h.by}}</small></div></sc-for>'
 '<sc-if value="{{noHist}}"><p class="mut" style="margin:0">ยังไม่มีการรับเข้าหรือเบิกออก กด “บันทึกสต็อกเข้า–ออก” เพื่อเริ่มบันทึก</p></sc-if></div></div></sc-if>'
 + FAB + MODAL + '</main></div>')

js = r"""
const mkProd=()=>({_k:'prod',name:'',sku:'',cat:'',unit:'ชิ้น',qty:'',min:''});
const mkMv=(pid)=>({_k:'mv',pid:pid?String(pid):'',type:'in',qty:'',by:'',note:''});
class Component extends Base{
boot(){const u=uiGet();if(u.open==='prod'){uiSet({open:''});this.setState({form:mkProd(),fe:''})}}
renderVals(){
const d=load(),T=TODAY(),S=Object.assign({cat:'all',low:false,form:null,fe:'',cdel:false,to:''},this.state),set=o=>this.setState(o),toast=m=>this.toast(m);
const P=d.products,cats=[...new Set(P.map(p=>p.cat).filter(Boolean))];
const nOk=P.filter(p=>stockSt(p)[0]==='ปกติ').length,nWarn=P.filter(p=>stockSt(p)[0]==='ใกล้หมด').length,nOut=P.filter(p=>stockSt(p)[0]==='หมด').length;
const list=P.filter(p=>(S.cat==='all'||p.cat===S.cat)&&(!S.low||stockSt(p)[0]!=='ปกติ'));
const rows=list.map(p=>{const z=stockSt(p);return{name:p.name,sku:p.sku||'—',cat:p.cat||'—',qty:p.qty,unit:p.unit||'',min:p.min,st:z[0],sc:z[1],w:p.qty<=0?0:p.min?Math.min(100,Math.round(p.qty/(p.min*2)*100)):100,pick:()=>set({form:{_k:'prod',id:p.id,name:p.name,sku:p.sku||'',cat:p.cat||'',unit:p.unit||'',min:p.min},fe:'',cdel:false})}});
const hist=d.stock.slice().sort((a,b)=>b.at.localeCompare(a.at)||b.id-a.id).slice(0,10).map(s=>{const p=P.find(x=>x.id===s.pid);return{t:thS(s.at.slice(0,10))+' '+s.at.slice(11)+' · '+(s.delta>0?'รับเข้า ':'เบิกออก ')+(p?p.name:'(สินค้าที่ถูกลบ)')+' '+Math.abs(s.delta)+' '+(p&&p.unit?p.unit:''),by:(s.by?'โดย '+s.by:'ไม่ระบุผู้ทำรายการ')+(s.note?' · '+s.note:'')}});
const F=S.form,fk=F&&F._k;let mo={};
if(fk==='shop')mo=shopMo(this,F,S);
if(fk==='prod'){const ed=!!F.id;mo={title:ed?'แก้ไขสินค้า':'เพิ่มสินค้า',hint:ed?'ปรับจำนวนคงเหลือได้ที่ปุ่ม “บันทึกสต็อกเข้า–ออก” เพื่อให้มีประวัติ':'จำนวนเริ่มต้นจะถูกบันทึกเป็นการรับเข้าครั้งแรก',
spec:[{k:'name',label:'ชื่อสินค้า',full:1,ph:'เช่น สีเจลโทนนู้ด'},{k:'sku',label:'รหัส SKU (ไม่บังคับ)'},{k:'cat',label:'หมวด (ไม่บังคับ)',ph:'เช่น สีเจล'},{k:'unit',label:'หน่วย',ph:'ขวด / แพ็ก / ชิ้น'}].concat(ed?[]:[{k:'qty',label:'จำนวนคงเหลือเริ่มต้น',type:'number',ph:'0'}],[{k:'min',label:'จำนวนขั้นต่ำที่ต้องเตือน',type:'number',ph:'เช่น 5'}]),saveTxt:ed?'บันทึกการแก้ไข':'เพิ่มสินค้า',
save:()=>{const name=(F.name||'').trim(),min=F.min===''||F.min==null?0:+F.min,qty=ed?0:(F.qty===''||F.qty==null?0:+F.qty);if(!name)return set({fe:'กรุณากรอกชื่อสินค้า'});if(isNaN(min)||min<0||isNaN(qty)||qty<0)return set({fe:'จำนวนต้องเป็นตัวเลข 0 ขึ้นไป'});if(P.some(p=>p.name===name&&p.id!==F.id))return set({fe:'มีสินค้าชื่อนี้อยู่แล้ว'});
M(x=>{const v={name,sku:(F.sku||'').trim(),cat:(F.cat||'').trim(),unit:(F.unit||'').trim(),min};if(ed)Object.assign(x.products.find(p=>p.id===F.id),v);else{const id=x.seq++;x.products.push(Object.assign({id,qty},v));if(qty>0)x.stock.push({id:x.seq++,pid:id,delta:qty,at:T+' '+NOWT(),by:'',note:'จำนวนเริ่มต้น'})}});set({form:null,fe:''});toast(ed?'บันทึกการแก้ไขแล้ว':'เพิ่มสินค้าแล้ว')},
del:ed?(()=>{if(!S.cdel)return set({cdel:true});M(x=>{x.products=x.products.filter(p=>p.id!==F.id);x.stock=x.stock.filter(s=>s.pid!==F.id)});set({form:null,cdel:false});toast('ลบสินค้าแล้ว')}):null,delTxt:'ลบสินค้า'}}
if(fk==='mv')mo={title:'บันทึกสต็อกเข้า–ออก',hint:P.length?'':'ต้องเพิ่มสินค้าก่อน',spec:[{k:'pid',label:'สินค้า',full:1,opts:[['','เลือกสินค้า…']].concat(P.map(p=>[String(p.id),p.name+' (คงเหลือ '+p.qty+' '+(p.unit||'')+')']))},{k:'type',label:'ประเภท',opts:[['in','รับเข้า'],['out','เบิกออก']]},{k:'qty',label:'จำนวน',type:'number',ph:'0'},{k:'by',label:'ผู้ทำรายการ',opts:[['','ไม่ระบุ']].concat(d.staff.map(s=>[s.name,s.name]))},{k:'note',label:'หมายเหตุ (ไม่บังคับ)'}],saveTxt:'บันทึก',
save:()=>{const q=F.qty===''||F.qty==null?NaN:+F.qty;if(!F.pid)return set({fe:'กรุณาเลือกสินค้า'});if(isNaN(q)||q<=0)return set({fe:'กรุณากรอกจำนวนมากกว่า 0'});const p=P.find(x=>x.id===+F.pid);if(F.type==='out'&&q>p.qty)return set({fe:'เบิกเกินจำนวนคงเหลือ (เหลือ '+p.qty+' '+(p.unit||'')+')'});
M(x=>{const z=x.products.find(w=>w.id===+F.pid),dl=F.type==='in'?q:-q;z.qty+=dl;x.stock.push({id:x.seq++,pid:z.id,delta:dl,at:T+' '+NOWT(),by:F.by||'',note:(F.note||'').trim()})});set({form:null,fe:''});toast((F.type==='in'?'รับเข้า ':'เบิกออก ')+p.name+' '+q+' แล้ว')}};
const n=P.length,nLow=nWarn+nOut;
return{today:thL(T),noStore:!OKS,openShop:()=>openShopForm(this),
heroT:n?'ต้องสั่งเพิ่ม':'สต็อกสินค้า',nLow,heroSub:n?(nLow?'ใกล้หมด '+nWarn+' · หมด '+nOut+' ควรสั่งซื้อก่อนของขาด':'สินค้าทุกรายการยังเพียงพอ'):'ยังไม่มีข้อมูลสินค้า เริ่มจากเพิ่มสินค้าชิ้นแรก',heroBtn:n?(nLow?(S.low?'ดูทั้งหมด':'ดูรายการที่ต้องสั่ง'):'+ เพิ่มสินค้า'):'เพิ่มสินค้า',heroGo:()=>{if(n&&nLow)set({low:!S.low,cat:'all'});else set({form:mkProd(),fe:''})},
add:()=>set({form:mkProd(),fe:'',cdel:false}),mv:()=>set({form:mkMv(),fe:'',cdel:false}),
nOk,nWarn,nOut,hasLow:nLow>0,cat:S.cat,onCat:e=>set({cat:e.target.value}),catOpts:[{v:'all',t:'ทุกหมวดหมู่'}].concat(cats.map(c=>({v:c,t:c}))),
rows,hasAny:n>0,noAny:n===0,noRows:n>0&&rows.length===0,hist,noHist:hist.length===0,fm:modalOf(this,S,mo),toast:S.to,toastText:S.to}}}
"""

html = page('Solva – สต็อก', helmet_css('Main.dc.html') + '.rt .lk{border:0;background:none;font:inherit;font-weight:600;cursor:pointer;color:inherit;text-align:left;padding:0;text-decoration:underline dotted}', body, js)
write('Inventory.dc.html', html)
