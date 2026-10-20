# -*- coding: utf-8 -*-
from core import *

HDR_EXTRA = ('<input placeholder="ค้นหาลูกค้า นัดหมาย สินค้า" aria-label="ค้นหา" value="{{q}}" onInput="{{onQ}}">'
             '<a class="ic" href="#notif" aria-label="แจ้งเตือน">' + BELL + '<sc-if value="{{hasN}}"><s>{{nN}}</s></sc-if></a>')

FAB = '<a class="fab" href="Schedule.dc.html" aria-label="สร้างนัดหมาย" onClick="{{goAppt}}"><svg width="32" height="32" viewBox="0 0 32 32" stroke="#FF9AFF" stroke-width="3" stroke-linecap="round"><path d="M16 5v22M5 16h22"></path></svg></a>'

body = ('<div class="app">' + nav('Main') + '<main class="mn">' + header(HDR_EXTRA) +
 hero(hero_svg('Main.dc.html'), 'วันนี้ร้านมี <b class="cn" style="--v:{{nQ}}"></b> คิว', '{{heroSub}}', '<a class="bt" href="{{heroHref}}" onClick="{{heroGo}}">{{heroBtn}}</a>') + WARN +
 '<sc-if value="{{hasQ}}"><div class="c rs" style="margin-bottom:22px"><h2>ผลการค้นหา “{{q}}”</h2><sc-for list="{{found}}" as="r"><a class="ap" href="{{r.h}}" onClick="{{r.go}}"><b>{{r.k}}</b> · {{r.t}}</a></sc-for><sc-if value="{{noFound}}"><p class="mut" style="margin:0">ไม่พบลูกค้า นัดหมาย หรือสินค้าที่ตรงกับคำค้น</p></sc-if></div></sc-if>'
 '<sc-if value="{{showSetup}}"><div class="c rs" style="margin-bottom:22px"><h2>เริ่มต้นใช้งาน · {{doneN}}/5 ขั้นตอน</h2><sc-for list="{{steps}}" as="s"><a class="ck {{s.cls}}" href="{{s.h}}" onClick="{{s.go}}"><i>{{s.mark}}</i><span><b>{{s.t}}</b><small>{{s.d}}</small></span></a></sc-for></div></sc-if>'
 '<div class="row rs" style="--i:1"><a class="bt" href="Schedule.dc.html" onClick="{{goAppt}}">+ เพิ่มนัดหมาย</a><a class="bt o" href="Clients.dc.html" onClick="{{goCust}}">+ เพิ่มลูกค้า</a><a class="bt d" href="Finance.dc.html" onClick="{{goOut}}">+ บันทึกรายจ่าย</a></div>'
 '<div class="g2"><div class="c rs" style="--i:2;position:relative"><div style="position:absolute;top:14px;right:14px;z-index:5">'+CAPMENU+'</div><div class="lgd"><span><b></b>คิวเต็ม</span><span><b class="a"></b>มีนัด</span></div><h2 style="text-align:center">{{moTxt}}</h2><div class="cal"><span>อา</span><span>จ</span><span>อ</span><span>พ</span><span>พฤ</span><span>ศ</span><span>ส</span>'
 '<sc-for list="{{days}}" as="c" hint-placeholder-count="35"><sc-if value="{{c.blank}}"><i></i></sc-if><sc-if value="{{c.real}}"><a class="dy {{c.cls}}" href="Schedule.dc.html" aria-label="{{c.aria}}" onClick="{{c.pick}}">{{c.n}}<sc-if value="{{c.full}}"><small>คิวเต็ม</small></sc-if></a></sc-if></sc-for></div></div>'
 '<div class="c rs" style="--i:3"><h2>รายได้วันนี้</h2><div class="dn"><svg width="300" height="300" viewBox="0 0 200 200"><defs><linearGradient id="gd"><stop offset="0" stop-color="#FF9AFF"></stop><stop offset="1" stop-color="#FFDFFF"></stop></linearGradient></defs><circle cx="100" cy="100" r="80" fill="none" stroke="#E6E6E6" stroke-width="30"></circle><circle cx="100" cy="100" r="80" fill="none" stroke="url(#gd)" stroke-width="30" stroke-dasharray="{{ring}} 503" style="animation:dr 1.3s ease-out"></circle></svg>'
 '<div class="ct"><div class="big">{{revTxt}}</div><div class="sm"><em>{{cmpTxt}}</em></div></div><sc-if value="{{hasL1}}"><span class="lb" style="right:-6px;top:14px">{{l1}}</span></sc-if><sc-if value="{{hasL2}}"><span class="lb" style="left:0;bottom:12px">{{l2}}</span></sc-if></div>'
 '<div class="mut" style="text-align:center;font-size:13px">วงกลมแสดงสัดส่วนของรายได้เดือนนี้ · เดือนนี้รวม {{monthRev}}</div></div></div>'
 '<h1>นัดหมายวันนี้</h1><div class="g"><div class="c lf rs" style="--i:4"><div class="kl">จองแล้ว</div><div class="k"><b class="cn" style="--v:{{nBooked}}"></b></div></div><div class="c lf rs" style="--i:5"><div class="kl">ยกเลิก</div><div class="k"><b class="cn" style="--v:{{nCanc}}"></b></div></div>'
 '<div class="c lf rs" style="--i:6"><div class="kl">เสร็จสิ้น</div><div class="k"><b class="cn" style="--v:{{nDone}}"></b></div></div><div class="c lf"><div class="kl">พนักงานเข้างาน</div><div class="k">{{presTxt}}</div></div></div>'
 '<div class="g2"><div class="c rs" style="--i:8"><h2>นัดหมายที่กำลังจะมาถึง</h2><sc-for list="{{up}}" as="u"><div class="ap"><sc-if value="{{u.next}}"><i class="pd"></i></sc-if><b>{{u.time}}</b> {{u.t}} <sc-if value="{{u.next}}"><span class="ch s2">ถัดไป</span></sc-if></div></sc-for>'
 '<sc-if value="{{noUp}}"><p class="mut" style="margin:0">ไม่มีนัดหมายที่รออยู่วันนี้ <a href="Schedule.dc.html" onClick="{{goAppt}}">สร้างนัดหมาย</a></p></sc-if></div>'
 '<div id="notif" class="c rs" style="--i:9"><h2>การแจ้งเตือน</h2><sc-for list="{{notes}}" as="n"><a class="ap {{n.cls}}" href="{{n.h}}">{{n.t}}</a></sc-for><sc-if value="{{noN}}"><p class="mut" style="margin:0">ยังไม่มีการแจ้งเตือน ระบบจะแจ้งเมื่อมีคิวใกล้ถึง ยอดค้างชำระ หรือสินค้าใกล้หมด</p></sc-if></div></div>'
 + FAB + MODAL + '</main></div>')

css_extra = ('.cal a.dy{font-style:normal;font-weight:600;width:40px;height:40px;margin:auto;display:grid;place-items:center;border-radius:50%;color:#4A4C5A;text-decoration:none;transition:transform .2s}.cal a.dy:hover{transform:scale(1.18)}'
 '.cal a.dy.f{background:#FF9AFF;color:#2B2D3A!important;-webkit-text-fill-color:#2B2D3A;border-radius:16px;width:48px;height:52px;display:flex;flex-direction:column;justify-content:center;align-items:center;line-height:1.1}.cal a.dy small{font-size:10px;font-weight:600;margin-top:2px;color:#2B2D3A}.cal a.dy.f.t{box-shadow:0 0 0 2px #2B2D3A}.cal a.dy.a{background:#FFDFFF}.cal a.dy.t{box-shadow:0 0 0 2px #2B2D3A;animation:pl 2s infinite}'
 'a.ap{display:block;color:inherit;text-decoration:none}a.ap.ye{color:#8A6500}a.ap.rd{color:#B3261E}a.ap:hover{background:#FFF8FF}a.ic{color:#2B2D3A;text-decoration:none}a.fab{text-decoration:none}.mn .mut a{color:#B3299E}')

js = r"""
class Component extends Base{
renderVals(){
const d=load(),T=TODAY(),S=Object.assign({q:'',form:null,fe:'',to:''},this.state),set=o=>this.setState(o);
const now=NOWT(),td=d.appts.filter(a=>a.date===T).sort((a,b)=>a.time.localeCompare(b.time)),act=td.filter(a=>a.status!=='canceled');
const booked=td.filter(a=>a.status==='booked'),nBooked=booked.length,nCanc=td.filter(a=>a.status==='canceled').length,nDone=td.filter(a=>a.status==='done').length;
const upl=booked.filter(a=>a.time>=now),up0=(upl.length?upl:booked).slice(0,5),nx=upl.length?upl[0]:null;
const step=(done,t,dsc,h,open,go)=>({cls:done?'ok':'',mark:done?'✓':'',t,d:dsc,h,go:go||(()=>{if(open)uiSet({open})})});
const steps=[step(d.services.length>0,'เพิ่มบริการและราคา','ตั้งชื่อบริการ ราคา และเวลาที่ใช้','Services.dc.html','sv'),step(d.staff.length>0,'เพิ่มพนักงาน','ชื่อ ตำแหน่ง และอัตราค่าคอมมิชชัน','Staff.dc.html','staff'),step(d.customers.length>0,'เพิ่มลูกค้า','เก็บเบอร์โทรและโน้ตของลูกค้า','Clients.dc.html','cust'),step(d.appts.length>0,'สร้างนัดหมายแรก','เลือกลูกค้า ช่าง และบริการ ระบบคิดราคาให้','Schedule.dc.html','appt'),
{cls:d.shop.name?'ok':'',mark:d.shop.name?'✓':'',t:'ตั้งชื่อร้าน',d:'ชื่อร้านจะแสดงบนบิลและรายงาน',h:'#',go:e=>{e&&e.preventDefault&&e.preventDefault();openShopForm(this)}}];
const doneN=steps.filter(s=>s.cls==='ok').length,firstTodo=steps.find(s=>s.cls!=='ok');
const yd=iso(new Date(new Date().getFullYear(),new Date().getMonth(),new Date().getDate()-1)),rev=revOf(d,T,T),yRev=revOf(d,yd,yd),[mf,mt]=mRange(mkey(T)),mRev=revOf(d,mf,mt);
const cm={};d.appts.filter(a=>isRev(a)&&(a.paidDate||a.date)===T).forEach(a=>a.items.forEach(i=>{const k=i.cat||'ไม่ระบุหมวด';cm[k]=(cm[k]||0)+i.price*(1-(a.disc||0)/100)}));const cl=Object.entries(cm).sort((a,b)=>b[1]-a[1]);
const cmp=!rev&&!yRev?'ยังไม่มีรายได้วันนี้':!yRev?'เมื่อวานยังไม่มีรายได้':(rev>=yRev?'↑ ':'↓ ')+Math.abs(Math.round((rev-yRev)/yRev*1000)/10)+'% เทียบเมื่อวาน';
const cnt={};d.appts.filter(a=>a.status!=='canceled').forEach(a=>{cnt[a.date]=(cnt[a.date]||0)+1});
const mk=mkey(T),a0=pd(mk+'-01'),days=[];for(let i=0;i<a0.getDay();i++)days.push({blank:true,real:false});
const cap=d.shop.cap||5;for(let i=1;i<=mDays(mk);i++){const s=mk+'-'+p2(i),n=cnt[s]||0;days.push({blank:false,real:true,n:i,full:n>=cap,cls:(n>=cap?'f':n>0?'a':'')+(s===T?' t':''),aria:thL(s)+(n>=cap?' คิวเต็ม':n?' มี '+n+' นัด':' ไม่มีนัด'),pick:()=>uiSet({date:s})})}
const notes=[];
if(nx){const m=tmin(nx.time)-tmin(now);if(m<=60)notes.push({t:'คิว'+cName(d,nx.cust)+' เริ่มในอีก '+m+' นาที',cls:'',h:'Schedule.dc.html'})}
const unpaid=d.appts.filter(a=>a.status==='done'&&!a.paid).length,cf=td.filter(a=>overlap(d,a).length>0).length,low=d.products.filter(p=>stockSt(p)[0]==='ใกล้หมด'),out=d.products.filter(p=>stockSt(p)[0]==='หมด');
if(cf)notes.push({t:'วันนี้มีคิวซ้อนเวลา '+cf+' รายการ',cls:'ye',h:'Schedule.dc.html'});
if(low.length)notes.push({t:'สินค้าใกล้หมด '+low.length+' รายการ: '+low.slice(0,3).map(p=>p.name+' (เหลือ '+p.qty+')').join(', '),cls:'ye',h:'Inventory.dc.html'});
if(out.length)notes.push({t:'สินค้าหมด '+out.length+' รายการ: '+out.slice(0,3).map(p=>p.name).join(', '),cls:'rd',h:'Inventory.dc.html'});
if(unpaid)notes.push({t:'รอชำระเงิน '+unpaid+' รายการ',cls:'rd',h:'Schedule.dc.html'});
const q=S.q.trim();let found=[];
if(q){d.customers.filter(c=>c.name.includes(q)||(c.nick||'').includes(q)||(c.phone||'').includes(q)).slice(0,4).forEach(c=>found.push({k:'ลูกค้า',t:c.name+(c.phone?' · '+c.phone:''),h:'Clients.dc.html',go:()=>{}}));
d.appts.filter(a=>cName(d,a.cust).includes(q)).sort((a,b)=>b.date.localeCompare(a.date)).slice(0,4).forEach(a=>found.push({k:'นัดหมาย',t:cName(d,a.cust)+' · '+thS(a.date)+' '+a.time+' น. · '+a.items.map(i=>i.name).join(' + '),h:'Schedule.dc.html',go:()=>uiSet({date:a.date,sel:a.id})}));
d.products.filter(p=>p.name.includes(q)||(p.sku||'').includes(q)).slice(0,4).forEach(p=>found.push({k:'สินค้า',t:p.name+' · คงเหลือ '+p.qty+' '+(p.unit||''),h:'Inventory.dc.html',go:()=>{}}))}
const pres=d.staff.filter(s=>{const r=attOf(d,s.id,T);return r&&r.type==='work'}).length;
const F=S.form,fk=F&&F._k;let mo={};
if(fk==='shop')mo=shopMo(this,F,S);if(fk==='cap')mo=capMo(this,F,S);
const setup=doneN<5;
return{today:thL(T),noStore:!OKS,openShop:()=>openShopForm(this),
nQ:act.length,capN:cap,menuOpen:!!S.menu,toggleMenu:this.toggleMenu,openCap:()=>openCapForm(this),heroSub:nx?'คิวถัดไป '+nx.time+' · '+cName(d,nx.cust)+' · '+nx.items.map(i=>i.name).join(' + '):act.length?'วันนี้ไม่มีคิวที่รออยู่แล้ว':(d.appts.length?'วันนี้ยังไม่มีนัดหมาย':'ยังไม่มีข้อมูล เริ่มตั้งค่าร้านได้จากขั้นตอนด้านล่าง'),
heroBtn:d.appts.length||!firstTodo?'ดูตารางนัด':'เริ่มตั้งค่าร้าน',heroHref:d.appts.length||!firstTodo?'Schedule.dc.html':firstTodo.h,heroGo:e=>{if(!d.appts.length&&firstTodo){if(firstTodo.h==='#'){e&&e.preventDefault&&e.preventDefault()}firstTodo.go(e)}},
q:S.q,onQ:e=>set({q:e.target.value}),hasQ:!!q,found,noFound:!!q&&found.length===0,hasN:notes.length>0,nN:notes.length,
showSetup:setup,doneN,steps,goAppt:()=>uiSet({open:'appt',date:T}),goCust:()=>uiSet({open:'cust'}),goOut:()=>uiSet({open:'out'}),
moTxt:mTxt(mk),days,ring:mRev?Math.round(Math.min(1,rev/mRev)*503):0,revTxt:fm(rev),cmpTxt:cmp,monthRev:fm(mRev),hasL1:cl.length>0,l1:cl.length?cl[0][0]+' '+fm(cl[0][1]):'',hasL2:cl.length>1,l2:cl.length>1?cl[1][0]+' '+fm(cl[1][1]):'',
nBooked,nCanc,nDone,presTxt:pres+'/'+d.staff.length,
up:up0.map((a,i)=>({time:a.time,t:cName(d,a.cust)+' · '+a.items.map(x=>x.name).join(' + '),next:!!nx&&i===0})),noUp:up0.length===0,notes,noN:notes.length===0,
fm:modalOf(this,S,mo),toast:S.to,toastText:S.to}}}
"""

html = page('Solva – ภาพรวม', helmet_css('Main.dc.html') + css_extra, body, js)
write('Main.dc.html', html)
