# -*- coding: utf-8 -*-
from core import *

EMPTYMINI = lambda msg: '<div class="em">' + HEART + '<div>' + msg + '</div></div>'

body = ('<div class="app">' + nav('Clients') + '<main class="mn">' + header() +
 hero(hero_svg('Clients.dc.html'),
      'ลูกค้าทั้งหมด <b class="cn" style="--v:{{nAll}}"></b> คน', '{{heroSub}}',
      '<button class="bt" onClick="{{heroGo}}">{{heroBtn}}</button>') + WARN +
 '<h2>ระดับสมาชิก · แตะการ์ดเพื่อกรองรายชื่อ</h2><div class="row" style="gap:20px;margin-bottom:26px">'
 '<sc-for list="{{cards}}" as="t" hint-placeholder-count="5"><button class="tc {{t.cls}} {{t.on}}" onClick="{{t.pick}}"><div class="ti"></div><div class="tn">{{t.name}}</div><div class="ts">{{t.sub}}</div><em><b class="cn" style="--v:{{t.n}}"></b> คน</em></button></sc-for></div>'
 '<sc-if value="{{noAny}}" hint-placeholder-val="{{false}}"><div class="empty">' + HEART +
 '<h2>ยังไม่มีข้อมูลลูกค้า</h2><p>เพิ่มลูกค้าเพื่อเก็บเบอร์โทร โน้ต และประวัติการใช้บริการ จากนั้นสมัครสมาชิกให้ลูกค้าที่ต้องการสะสมแต้มได้</p></div></sc-if>'
 '<sc-if value="{{hasAny}}" hint-placeholder-val="{{true}}"><div id="list" class="row"><input class="si" placeholder="ค้นหาชื่อหรือเบอร์โทร" aria-label="ค้นหาลูกค้า" value="{{q}}" onInput="{{onQ}}">'
 '<div class="sg"><sc-for list="{{segs}}" as="s" hint-placeholder-count="3"><button class="{{s.on}}" onClick="{{s.pick}}">{{s.name}}</button></sc-for></div>'
 '<button class="bt o" style="margin-left:auto" onClick="{{tierSet}}">ตั้งค่าระดับสมาชิก</button></div>'
 '<div class="lay"><div class="c l1"><div class="sx"><div class="r h"><div>ลูกค้า</div><div>เบอร์ติดต่อ</div><div>สถานะ</div><div>ล่าสุด</div><div>ครั้ง</div><div>ยอดสะสม</div></div>'
 '<sc-for list="{{rows}}" as="r" hint-placeholder-count="4"><div class="r {{r.on}}"><div class="ph"><i>{{r.ini}}</i><button class="nb" onClick="{{r.pick}}">{{r.name}}</button></div><div>{{r.phone}}</div><div><span class="sb2 {{r.bc}}"><i></i>{{r.badge}}</span></div><div>{{r.last}}</div><div>{{r.visits}}</div><div>{{r.spend}}</div></div></sc-for></div>'
 '<sc-if value="{{noRows}}" hint-placeholder-val="{{false}}">' + EMPTYMINI('ไม่พบลูกค้าที่ตรงกับตัวกรอง<br><button class="bt o" style="margin-top:12px" onClick="{{clear}}">ล้างตัวกรอง</button>') + '</sc-if></div>'
 '<div class="c l2"><sc-if value="{{noSel}}" hint-placeholder-val="{{false}}">' + EMPTYMINI('เลือกลูกค้าจากรายชื่อเพื่อดูโปรไฟล์') + '</sc-if>'
 '<sc-if value="{{hasSel}}" hint-placeholder-val="{{true}}"><div class="row" style="margin:0"><div class="av2" style="width:64px;height:64px;font-size:24px;font-weight:700;background:#FFDFFF">{{sel.ini}}</div>'
 '<div><h2 style="margin:0">{{sel.name}} <small style="font-weight:400;color:#6B6D7A">{{sel.nick}}</small></h2><span class="mb {{sel.bc}}">{{sel.badge}}</span></div></div>'
 '<div class="tabs"><sc-for list="{{tabs}}" as="t" hint-placeholder-count="5"><button class="{{t.on}}" onClick="{{t.pick}}">{{t.name}}</button></sc-for></div>'
 '<sc-if value="{{t0}}"><div class="tp"><sc-for list="{{sel.kv}}" as="x"><div class="kv"><span>{{x.k}}</span><b>{{x.v}}</b></div></sc-for>'
 '<div class="row" style="margin:14px 0 0"><button class="bt o" onClick="{{sel.edit}}">แก้ไขข้อมูล</button><button class="bt d" onClick="{{sel.del}}">{{sel.delTxt}}</button></div></div></sc-if>'
 '<sc-if value="{{t1}}"><div class="tp"><sc-if value="{{sel.isMem}}"><div class="kv"><span>เริ่มเป็นสมาชิก</span><b>{{sel.since}}</b></div><div class="kv"><span>คะแนนสะสม</span><b>{{sel.pts}} แต้ม</b></div>'
 '<div class="kv"><span>ส่วนลดบริการ</span><b>{{sel.discTxt}}</b></div><div style="margin:12px 0 4px">{{sel.nextTxt}}</div><div class="bar"><i style="width:{{sel.pct}}%"></i></div>'
 '<h2 style="margin:16px 0 4px">สิทธิประโยชน์</h2><sc-for list="{{sel.bens}}" as="b"><div class="ap">✦ {{b.t}}</div></sc-for>'
 '<div class="row" style="margin:12px 0 0"><sc-if value="{{sel.hasNext}}"><button class="bt" onClick="{{sel.up}}">อัปเกรดเป็น {{sel.nextName}}</button></sc-if><button class="bt d" onClick="{{sel.leave}}">{{sel.leaveTxt}}</button></div></sc-if>'
 '<sc-if value="{{sel.isNon}}"><div class="em"><span class="mb np">Non-member</span><p>ยังไม่ได้เป็นสมาชิก สมัครเพื่อสะสมแต้มและรับส่วนลดตามระดับ</p><button class="bt" onClick="{{sel.join}}">สมัครสมาชิก Pearl</button></div></sc-if></div></sc-if>'
 '<sc-if value="{{t2}}"><div class="tp"><sc-if value="{{sel.hasNotes}}"><div class="row"><sc-for list="{{sel.notes}}" as="n"><span class="ch nt">{{n.t}}<button aria-label="ลบโน้ต" onClick="{{n.rm}}">×</button></span></sc-for></div></sc-if>'
 '<sc-if value="{{sel.noNotes}}">' + EMPTYMINI('ยังไม่มีโน้ต เพิ่มสีที่ชอบหรือข้อควรระวังด้านล่าง') + '</sc-if>'
 '<div class="ni"><input placeholder="เพิ่มโน้ตใหม่ เช่น สีที่ชอบ" aria-label="โน้ตใหม่" value="{{nin}}" onInput="{{onNin}}"><button class="bt" onClick="{{addNote}}">บันทึก</button></div></div></sc-if>'
 '<sc-if value="{{t3}}"><div class="tp"><sc-if value="{{sel.hasV}}"><div class="tl"><sc-for list="{{sel.vs}}" as="v"><div><small>{{v.k}}</small><b>{{v.v}}</b></div></sc-for></div><h2>บริการที่ใช้บ่อย</h2>'
 '<sc-for list="{{sel.top}}" as="t"><div class="ap"><div style="display:flex;justify-content:space-between"><span>{{t.n}}</span><b>{{t.c}}</b></div><div class="bar" style="margin-top:6px"><i style="width:{{t.w}}%"></i></div></div></sc-for></sc-if>'
 '<sc-if value="{{sel.noV}}">' + EMPTYMINI('ยังไม่เคยใช้บริการ ข้อมูลสรุปจะแสดงเมื่อมีนัดที่เสร็จสิ้น') + '</sc-if></div></sc-if>'
 '<sc-if value="{{t4}}"><div class="tp"><sc-for list="{{sel.hist}}" as="h"><div class="hi2"><button onClick="{{h.toggle}}"><span><b>{{h.date}}</b> · {{h.items}}</span><span><span class="ch {{h.pc}}">{{h.pay}}</span> {{h.ar}}</span></button>'
 '<sc-if value="{{h.isOpen}}"><div class="dd">ช่าง {{h.staff}} · {{h.dur}} · {{h.price}}{{h.more}}</div></sc-if></div></sc-for>'
 '<sc-if value="{{sel.noH}}">' + EMPTYMINI('ยังไม่มีประวัติบริการ') + '</sc-if></div></sc-if>'
 '</sc-if></div></div></sc-if>' + MODAL + '</main></div>')

js = r"""
const TB=['ข้อมูลพื้นฐาน','สถานะสมาชิก','โน้ต','สรุปการใช้บริการ','ประวัติบริการ'];
const mkCust=()=>({_k:'cust',name:'',nick:'',phone:'',bd:'',line:'',tier:''});
class Component extends Base{
boot(){const u=uiGet();if(u.open==='cust'){uiSet({open:''});this.setState({form:mkCust(),fe:''})}}
renderVals(){
const d=load(),S=Object.assign({f:'all',q:'',sel:null,tab:0,nin:'',op:null,form:null,fe:'',cdel:false,cl:false,to:''},this.state),set=o=>this.setState(o);
const T=TODAY(),toast=m=>this.toast(m);
const st=c=>cStats(d,c);
const inF=c=>S.f==='all'||(S.f==='np'&&!c.tier)||(S.f==='mem'&&!!c.tier)||S.f===c.tier;
const q=S.q.trim();
const rows=d.customers.filter(c=>inF(c)&&(!q||c.name.includes(q)||(c.nick||'').includes(q)||(c.phone||'').includes(q))).map(c=>{const s=st(c);return{name:c.name,phone:c.phone||'—',badge:c.tier||'Non-member',bc:c.tier?TCL[c.tier]:'np',last:s.last?thS(s.last):'—',visits:s.visits,spend:fm(s.spend),ini:c.name.replace('คุณ','').charAt(0)||'ล',on:S.sel===c.id?'on':'',pick:()=>set({sel:c.id,tab:0,op:null,nin:'',cdel:false,cl:false})}});
const cnt=t=>d.customers.filter(c=>c.tier===t).length,nNon=d.customers.filter(c=>!c.tier).length;
const cards=[['np','Non-member','ลูกค้าทั่วไป',nNon,'np']].concat(d.tiers.map(t=>[t.n,t.n,t.disc?'สมาชิก · ลด '+t.disc+'%':'สมาชิก',cnt(t.n),TCL[t.n]])).map(([k,n,s,v,cl])=>({name:n,sub:s,n:v,cls:'t'+cl,on:S.f===k?'on':'',pick:()=>set({f:S.f===k?'all':k})}));
const segs=[['all','ทั้งหมด'],['np','Non-member'],['mem','Membership']].map(([k,n])=>({name:n,on:(k==='mem'?(S.f==='mem'||!!TCL[S.f]):S.f===k)?'on':'',pick:()=>set({f:k})}));
const tabs=TB.map((n,i)=>({name:n,on:S.tab===i?'on':'',pick:()=>set({tab:i,op:null})}));
const c=getC(d,S.sel);let sel={};
if(c){const s=st(c),ti=tierO(d,c),nx=nextTier(d,c),pts=Math.floor(s.spend/10),ns=c.notes||[];
const top={};s.list.forEach(a=>a.items.forEach(i=>{top[i.name]=(top[i.name]||0)+1}));const tl=Object.entries(top).sort((a,b)=>b[1]-a[1]).slice(0,5),mx=Math.max(1,...tl.map(x=>x[1]));
const hist=d.appts.filter(a=>a.cust===c.id).sort((a,b)=>(b.date+b.time).localeCompare(a.date+a.time));
const pct=ti&&nx?Math.round((s.spend-ti.min)/Math.max(1,nx.min-ti.min)*100):100;
sel={name:c.name,nick:c.nick?'('+c.nick+')':'',badge:c.tier||'Non-member',bc:c.tier?TCL[c.tier]:'np',ini:c.name.replace('คุณ','').charAt(0)||'ล',
kv:[{k:'เบอร์โทรศัพท์',v:c.phone||'—'},{k:'วันเกิด',v:thD(c.bd)},{k:'วันที่ลงทะเบียน',v:thD(c.created)},{k:'Line ID',v:c.line||'—'}],
edit:()=>set({form:{_k:'cust',id:c.id,name:c.name,nick:c.nick||'',phone:c.phone||'',bd:c.bd||'',line:c.line||'',tier:c.tier||''},fe:''}),
delTxt:S.cdel?'กดอีกครั้งเพื่อยืนยันลบ':'ลบลูกค้า',
del:()=>{if(hist.length)return toast('ลบไม่ได้ เพราะลูกค้ามีประวัตินัดหมายอยู่');if(!S.cdel)return set({cdel:true});M(x=>{x.customers=x.customers.filter(z=>z.id!==c.id)});set({sel:null,cdel:false});toast('ลบลูกค้าแล้ว')},
isMem:!!c.tier,isNon:!c.tier,since:thD(c.since),pts:nn(pts),discTxt:ti&&ti.disc?ti.disc+'%':'ไม่มี',pct:Math.min(100,Math.max(4,pct)),nextTxt:nx?'อีก '+fm(Math.max(0,nx.min-s.spend))+' สู่ '+nx.n:'ระดับสูงสุดแล้ว',hasNext:!!nx,nextName:nx?nx.n:'',
bens:ti?[{t:'สะสม 1 แต้มทุกการใช้จ่าย ฿10'}].concat(ti.disc?[{t:'ส่วนลดบริการ '+ti.disc+'% (ใช้กับนัดหมายใหม่)'}]:[]):[],
join:()=>{M(x=>{const z=getC(x,c.id);z.tier=x.tiers[0].n;z.since=T});toast('สมัครสมาชิก '+d.tiers[0].n+' เรียบร้อย')},
up:()=>{M(x=>{getC(x,c.id).tier=nx.n});toast('อัปเกรดเป็น '+nx.n+' แล้ว')},
leaveTxt:S.cl?'กดอีกครั้งเพื่อยืนยันยกเลิก':'ยกเลิกสมาชิก',leave:()=>{if(!S.cl)return set({cl:true});M(x=>{const z=getC(x,c.id);z.tier='';z.since=''});set({cl:false});toast('ยกเลิกสมาชิกแล้ว')},
notes:ns.map((x,i)=>({t:x,rm:()=>{M(y=>{getC(y,c.id).notes=ns.filter((_,j)=>j!==i)});toast('ลบโน้ตแล้ว')}})),hasNotes:ns.length>0,noNotes:ns.length===0,
vs:[{k:'จำนวนครั้ง',v:s.visits+' ครั้ง'},{k:'ยอดสะสม',v:fm(s.spend)},{k:'เฉลี่ยต่อครั้ง',v:fm(s.visits?s.spend/s.visits:0)},{k:'ล่าสุด',v:s.last?thD(s.last):'—'}],
top:tl.map(x=>({n:x[0],c:x[1]+' ครั้ง',w:Math.round(x[1]/mx*100)})),hasV:s.visits>0,noV:s.visits===0,
hist:hist.map((a,i)=>{const z=stOf(a);return{date:thD(a.date),items:a.items.map(x=>x.name).join(' + '),staff:sName(d,a.staff),price:fm(net(a)),dur:dur(a)?dur(a)+' นาที':'ไม่ระบุเวลา',more:a.disc?' · ส่วนลดสมาชิก '+a.disc+'%':'',pay:z[0],pc:z[1],isOpen:S.op===i,ar:S.op===i?'▲':'▼',toggle:()=>set({op:S.op===i?null:i})}}),noH:hist.length===0}}
const F=S.form,k=F&&F._k;let mo={};
const CSP=[{k:'name',label:'ชื่อลูกค้า',full:1,ph:'เช่น คุณสุดา มั่นคง'},{k:'nick',label:'ชื่อเล่น (ไม่บังคับ)'},{k:'phone',label:'เบอร์โทร (ไม่บังคับ)',type:'tel',ph:'08x-xxx-xxxx'},{k:'bd',label:'วันเกิด (ไม่บังคับ)',type:'date'},{k:'line',label:'Line ID (ไม่บังคับ)'},{k:'tier',label:'สถานะสมาชิก',opts:[['','ยังไม่เป็นสมาชิก (Non-member)']].concat(d.tiers.map(t=>[t.n,'สมาชิก '+t.n]))}];
if(k==='shop')mo=shopMo(this,F,S);
if(k==='cust')mo={title:F.id?'แก้ไขข้อมูลลูกค้า':'เพิ่มลูกค้า',spec:CSP,saveTxt:F.id?'บันทึกการแก้ไข':'เพิ่มลูกค้า',save:()=>{const name=(F.name||'').trim(),phone=(F.phone||'').trim();
if(!name)return set({fe:'กรุณากรอกชื่อลูกค้า'});const dup=phone&&d.customers.find(z=>z.phone===phone&&z.id!==F.id);if(dup)return set({fe:'เบอร์นี้มีในระบบแล้ว (ลูกค้า: '+dup.name+')'});
let nid=F.id;M(x=>{if(F.id){const z=getC(x,F.id);z.name=name;z.nick=(F.nick||'').trim();z.phone=phone;z.bd=F.bd||'';z.line=(F.line||'').trim();if(F.tier&&!z.tier)z.since=T;if(!F.tier)z.since='';z.tier=F.tier||''}else{nid=x.seq++;x.customers.push({id:nid,name,nick:(F.nick||'').trim(),phone,bd:F.bd||'',line:(F.line||'').trim(),tier:F.tier||'',since:F.tier?T:'',created:T,notes:[]})}});
set({form:null,fe:'',sel:nid,tab:0,f:'all',q:''});toast(F.id?'บันทึกการแก้ไขแล้ว':'เพิ่มลูกค้าแล้ว')}};
if(k==='tiers'){const sp=[];d.tiers.forEach((t,i)=>{if(i>0)sp.push({k:'min'+i,label:t.n+' · ยอดสะสมขั้นต่ำ (บาท)',type:'number'});sp.push({k:'disc'+i,label:t.n+' · ส่วนลดบริการ (%)',type:'number'})});
mo={title:'ตั้งค่าระดับสมาชิก',hint:'กำหนดตามนโยบายของร้าน ส่วนลดใช้กับนัดหมายที่สร้างหลังจากนี้',spec:sp,save:()=>{const t=d.tiers.map((z,i)=>({n:z.n,min:i?+F['min'+i]:0,disc:+F['disc'+i]||0}));
for(let i=0;i<t.length;i++){if(isNaN(t[i].min)||t[i].min<0||t[i].disc<0||t[i].disc>100)return set({fe:'กรุณากรอกตัวเลขให้ถูกต้อง (ส่วนลด 0–100%)'});if(i&&t[i].min<=t[i-1].min)return set({fe:'ยอดสะสมของระดับสูงต้องมากกว่าระดับก่อนหน้า'})}
M(x=>{x.tiers=t});set({form:null,fe:''});toast('บันทึกระดับสมาชิกแล้ว')}}}
const n=d.customers.length,nm=n-nNon;
return{today:thL(T),noStore:!OKS,openShop:()=>openShopForm(this),nAll:n,
heroSub:n?'สมาชิก '+nm+' · Non-member '+nNon:'เริ่มต้นด้วยการเพิ่มลูกค้าคนแรกของร้าน',heroBtn:n?'+ เพิ่มลูกค้า':'เพิ่มลูกค้าคนแรก',heroGo:()=>set({form:mkCust(),fe:''}),
add:()=>set({form:mkCust(),fe:''}),tierSet:()=>{const F2={_k:'tiers'};d.tiers.forEach((t,i)=>{F2['min'+i]=t.min;F2['disc'+i]=t.disc});set({form:F2,fe:''})},
q:S.q,onQ:e=>set({q:e.target.value}),nin:S.nin,onNin:e=>set({nin:e.target.value}),
addNote:()=>{const v=S.nin.trim();if(!v||!c)return;M(x=>{const z=getC(x,c.id);z.notes=(z.notes||[]).concat(v)});set({nin:''});toast('บันทึกโน้ตแล้ว')},
clear:()=>set({f:'all',q:''}),rows,cards,segs,tabs,sel,hasAny:n>0,noAny:n===0,noRows:n>0&&rows.length===0,hasSel:!!c,noSel:!c,t0:S.tab===0,t1:S.tab===1,t2:S.tab===2,t3:S.tab===3,t4:S.tab===4,fm:modalOf(this,S,mo),toast:S.to,toastText:S.to}}}
"""

html = page('Solva – ลูกค้า', helmet_css('Clients.dc.html')+'.mb{height:auto;gap:0}', body, js)
html = html.replace('class="hi"', 'class="hi2"')
write('Clients.dc.html', html)
