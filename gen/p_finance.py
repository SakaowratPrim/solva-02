# -*- coding: utf-8 -*-
from core import *

FAB = '<button class="fab" aria-label="เพิ่มรายรับ" onClick="{{addIn}}"><svg width="32" height="32" viewBox="0 0 32 32" stroke="#FF9AFF" stroke-width="3" stroke-linecap="round"><path d="M16 5v22M5 16h22"></path></svg></button>'

body = ('<div class="app">' + nav('Finance') + '<main class="mn">' + header() +
 hero(hero_svg('Finance.dc.html'), 'กำไรสุทธิ{{moWord}} {{profitTxt}}', '{{heroSub}}', '<a class="bt" href="#report">ดูรายงาน</a>') + WARN +
 '<h1>การเงิน · {{moTxt}}</h1><div class="row"><div class="stp"><button aria-label="เดือนก่อนหน้า" onClick="{{prev}}">‹</button><b>{{moTxt}}</b><button aria-label="เดือนถัดไป" onClick="{{next}}">›</button></div>'
 '<button class="bt" style="margin-left:auto" onClick="{{addIn}}">+ รายรับ</button><button class="bt d" onClick="{{addOut}}">+ รายจ่าย</button></div>'
 '<div class="g"><div class="c lf"><div class="kl">รายได้รวม</div><div class="k">{{incTxt}}</div></div><div class="c lf"><div class="kl">ค่าใช้จ่ายรวม</div><div class="k">{{expTxt}}</div><div class="ye" style="text-align:center">{{pendTxt}}</div></div>'
 '<div class="c lf"><div class="kl">กำไรสุทธิ</div><div class="k">{{profitTxt}}</div><div class="gr" style="text-align:center">รายได้ − ค่าใช้จ่าย</div></div>'
 '<div class="c lf"><div class="kl">ค่าคอมมิชชัน</div><div class="k">{{comTxt}}</div><div class="mut" style="text-align:center;font-size:13px">{{comSub}}</div></div></div>'
 '<div id="report" class="c rs" style="margin-bottom:22px"><h2>รายได้รายเดือน (บาท)</h2><div class="mb"><sc-for list="{{chart}}" as="m" hint-placeholder-count="7"><div><b>{{m.v}}</b><i style="height:{{m.h}}px;animation-delay:{{m.dl}}ms"></i><span>{{m.l}}</span></div></sc-for></div>'
 '<sc-if value="{{noInc}}"><p class="mut" style="text-align:center;margin:8px 0 0">ยังไม่มีรายได้ในช่วง 7 เดือนนี้ กราฟจะแสดงเมื่อมีการรับชำระเงินหรือบันทึกรายรับ</p></sc-if></div>'
 '<div class="g2"><div class="c"><h2>ความคืบหน้าเทียบเป้าหมาย</h2><div class="dn"><svg width="300" height="300" viewBox="0 0 200 200"><defs><linearGradient id="gd"><stop offset="0" stop-color="#FF9AFF"></stop><stop offset="1" stop-color="#FFDFFF"></stop></linearGradient></defs><circle cx="100" cy="100" r="80" fill="none" stroke="#E6E6E6" stroke-width="30"></circle><circle cx="100" cy="100" r="80" fill="none" stroke="url(#gd)" stroke-width="30" stroke-dasharray="{{ring}} 503" style="animation:dr 1.3s ease-out"></circle></svg>'
 '<div class="ct"><div class="big">{{goalBig}}</div><div class="sm">{{goalSm}}</div></div></div><div style="text-align:center"><button class="bt o" onClick="{{openShop}}">{{goalBtn}}</button></div></div>'
 '<div class="c rt" style="overflow-x:auto"><h2>รายการล่าสุด</h2><sc-if value="{{hasTx}}"><table><tr><th>วันที่</th><th>รายละเอียด</th><th>หมวด</th><th>จำนวน</th><th>จ่ายโดย</th><th>สถานะ</th></tr>'
 '<sc-for list="{{txs}}" as="t" hint-placeholder-count="3"><tr><td data-label="วันที่">{{t.date}}</td><td data-label="รายละเอียด"><sc-if value="{{t.isTx}}"><button class="lk" onClick="{{t.pick}}">{{t.detail}}</button></sc-if><sc-if value="{{t.isAp}}"><a href="Schedule.dc.html" onClick="{{t.pick}}" style="color:inherit">{{t.detail}}</a></sc-if></td><td data-label="หมวด">{{t.cat}}</td><td data-label="จำนวน" class="{{t.cls}}"><b>{{t.amt}}</b></td><td data-label="จ่ายโดย">{{t.method}}</td><td data-label="สถานะ"><span class="ch {{t.sc}}">{{t.st}}</span></td></tr></sc-for></table></sc-if>'
 '<sc-if value="{{noTx}}"><div class="em"><h2>ยังไม่มีรายการเงินเข้า–ออก</h2><p>รายรับจากนัดหมายที่รับชำระแล้วจะแสดงที่นี่อัตโนมัติ ส่วนค่าใช้จ่ายเช่น ค่าเช่า ค่าวัสดุ ให้กด “+ รายจ่าย” เพื่อบันทึก</p><button class="bt" onClick="{{addOut}}">บันทึกรายจ่ายแรก</button></div></sc-if></div></div>'
 '<div class="g2"><div class="c"><h2>รายได้ตามช่าง</h2><sc-for list="{{byStaff}}" as="u"><div class="ut"><span>{{u.n}}</span><div class="bar"><i style="width:{{u.w}}%"></i></div><b>{{u.v}}</b></div></sc-for><sc-if value="{{noByStaff}}"><p class="mut" style="margin:0">ยังไม่มีรายได้จากนัดหมายในเดือนนี้</p></sc-if></div>'
 '<div class="c"><h2>บริการขายดี</h2><sc-for list="{{topSv}}" as="u"><div class="ut" style="grid-template-columns:130px 1fr 60px"><span>{{u.n}}</span><div class="bar"><i style="width:{{u.w}}%"></i></div><b>{{u.v}}</b></div></sc-for><sc-if value="{{noTopSv}}"><p class="mut" style="margin:0">ยังไม่มีบริการที่ชำระเงินแล้วในเดือนนี้</p></sc-if></div></div>'
 + FAB + MODAL + '</main></div>')

js = r"""
const mkTx=(type,T)=>({_k:'tx',type:type,amount:'',date:T,cat:'',detail:'',method:PAYM[0],status:'ok'});
const kf=n=>n>=1000?(Math.round(n/100)/10)+'k':String(Math.round(n));
class Component extends Base{
boot(){const u=uiGet();if(u.open==='out'||u.open==='in'){uiSet({open:''});this.setState({form:mkTx(u.open,TODAY()),fe:''})}}
renderVals(){
const d=load(),T=TODAY(),S=Object.assign({mo:0,form:null,fe:'',cdel:false,to:''},this.state),set=o=>this.setState(o),toast=m=>this.toast(m);
const k=mAdd(mkey(T),S.mo),[f,t]=mRange(k),dOf=a=>a.paidDate||a.date,inM=s=>s>=f&&s<=t;
const aps=d.appts.filter(a=>isRev(a)&&inM(dOf(a))),txIn=d.tx.filter(x=>x.type==='in'&&inM(x.date)),txOut=d.tx.filter(x=>x.type==='out'&&inM(x.date));
const inc=sum(aps,net)+sum(txIn,x=>x.amount),exp=sum(txOut.filter(x=>x.status==='ok'),x=>x.amount),pend=sum(txOut.filter(x=>x.status!=='ok'),x=>x.amount),profit=inc-exp;
const com=sum(aps,a=>commOf(a,getS(d,a.staff))),noRate=d.staff.filter(s=>s.rate==null||s.rate==='').length;
const months=[6,5,4,3,2,1,0].map(i=>mAdd(k,-i)),vals=months.map(m=>{const [a,b]=mRange(m);return revOf(d,a,b)}),mx=Math.max(1,...vals);
const chart=months.map((m,i)=>({v:vals[i]?kf(vals[i]):'0',h:vals[i]?Math.max(6,Math.round(vals[i]/mx*200)):3,dl:i*110,l:mShort(m)}));
const goal=d.shop.goal||0,pct=goal?Math.min(100,Math.round(inc/goal*100)):0;
const rows=aps.map(a=>({date:dOf(a),sort:dOf(a)+'b'+String(a.id).padStart(6,'0'),isTx:false,isAp:true,detail:cName(d,a.cust)+' · '+a.items.map(i=>i.name).join(' + '),cat:'รายรับ (บริการ)',amt:'+'+fm(net(a)),cls:'gr',method:a.method||'—',st:'สำเร็จ',sc:'s1',pick:()=>uiSet({sel:a.id,date:a.date})}))
.concat(d.tx.filter(x=>inM(x.date)).map(x=>({date:x.date,sort:x.date+'a'+String(x.id).padStart(6,'0'),isTx:true,isAp:false,detail:x.detail||x.cat||(x.type==='in'?'รายรับอื่น ๆ':'รายจ่าย'),cat:x.cat||(x.type==='in'?'รายรับ':'รายจ่าย'),amt:(x.type==='in'?'+':'−')+fm(x.amount),cls:x.type==='in'?'gr':'rd',method:x.method||'—',st:x.status==='ok'?'สำเร็จ':'รอชำระ',sc:x.status==='ok'?'s1':'s2',pick:()=>set({form:{_k:'tx',id:x.id,type:x.type,amount:x.amount,date:x.date,cat:x.cat||'',detail:x.detail||'',method:x.method||PAYM[0],status:x.status},fe:'',cdel:false})}))).sort((a,b)=>b.sort.localeCompare(a.sort)).slice(0,20).map(r=>Object.assign(r,{date:thS(r.date)}));
const bs={};aps.forEach(a=>{bs[a.staff]=(bs[a.staff]||0)+net(a)});const bl=Object.entries(bs).sort((a,b)=>b[1]-a[1]),bmx=Math.max(1,...bl.map(x=>x[1]));
const sv={};aps.forEach(a=>a.items.forEach(i=>{sv[i.name]=(sv[i.name]||0)+1}));const sl=Object.entries(sv).sort((a,b)=>b[1]-a[1]).slice(0,5),smx=Math.max(1,...sl.map(x=>x[1]));
const F=S.form,fk=F&&F._k;let mo={};
if(fk==='shop')mo=shopMo(this,F,S);
if(fk==='tx'){const isIn=F.type==='in';mo={title:(F.id?'แก้ไข':'บันทึก')+(isIn?'รายรับ':'รายจ่าย'),hint:isIn?'ใช้สำหรับรายรับที่ไม่ได้มาจากนัดหมาย เช่น ขายสินค้า (รายได้จากนัดหมายแสดงอัตโนมัติ)':'เช่น ค่าเช่า ค่าวัสดุ ค่าน้ำไฟ',
spec:[{k:'amount',label:'จำนวนเงิน (บาท)',type:'number',ph:'0'},{k:'date',label:'วันที่',type:'date'},{k:'cat',label:'หมวด',ph:isIn?'เช่น ขายสินค้า':'เช่น ค่าเช่า'},{k:'method',label:'จ่ายโดย',opts:PAYM.concat(['อื่น ๆ']).map(x=>[x,x])},{k:'detail',label:'รายละเอียด',full:1,ph:'เช่น สีเจลโทนนู้ด 6 ขวด'},{k:'status',label:'สถานะ',opts:[['ok','สำเร็จ'],['pend','รอชำระ']]}],saveTxt:F.id?'บันทึกการแก้ไข':'บันทึก',
save:()=>{const amount=F.amount===''||F.amount==null?NaN:+F.amount;if(isNaN(amount)||amount<=0)return set({fe:'กรุณากรอกจำนวนเงินมากกว่า 0'});if(!F.date)return set({fe:'กรุณาเลือกวันที่'});
M(x=>{const v={type:F.type,amount,date:F.date,cat:(F.cat||'').trim(),detail:(F.detail||'').trim(),method:F.method,status:F.status};if(F.id)Object.assign(x.tx.find(z=>z.id===F.id),v);else x.tx.push(Object.assign({id:x.seq++},v))});
set({form:null,fe:'',mo:F.date.slice(0,7)===mkey(T)?S.mo:S.mo});toast('บันทึก'+(isIn?'รายรับ':'รายจ่าย')+'แล้ว')},
del:F.id?(()=>{if(!S.cdel)return set({cdel:true});M(x=>{x.tx=x.tx.filter(z=>z.id!==F.id)});set({form:null,cdel:false});toast('ลบรายการแล้ว')}):null,delTxt:'ลบรายการ'}}
const empty=!d.appts.length&&!d.tx.length;
return{today:thL(T),noStore:!OKS,openShop:()=>{const sp=this;set({form:{_k:'shop',name:d.shop.name,phone:d.shop.phone,goal:d.shop.goal||'',cap:d.shop.cap||5},fe:''})},
moTxt:mTxt(k),moWord:S.mo===0?'เดือนนี้':'',prev:()=>set({mo:S.mo-1}),next:()=>{if(S.mo<0)set({mo:S.mo+1})},
profitTxt:fm(profit),incTxt:fm(inc),expTxt:fm(exp),pendTxt:pend?'รอจ่ายอีก '+fm(pend):'',comTxt:fm(com),comSub:noRate&&d.staff.length?'มีพนักงาน '+noRate+' คนที่ยังไม่ตั้งอัตราคอม':(d.staff.length?'จากงานที่ชำระเงินแล้ว':'ยังไม่มีพนักงาน'),
heroSub:empty?'ยังไม่มีข้อมูลการเงิน เริ่มจากรับชำระนัดหมายหรือบันทึกรายรับ–รายจ่าย':goal?'ทำได้ '+pct+'% ของเป้าหมาย '+fm(goal):'ตั้งเป้าหมายรายได้เพื่อดูความคืบหน้า',
addIn:()=>set({form:mkTx('in',T),fe:'',cdel:false}),addOut:()=>set({form:mkTx('out',T),fe:'',cdel:false}),
chart,noInc:Math.max(...vals)===0,ring:Math.round(pct/100*503),goalBig:goal?pct+'%':'—',goalSm:goal?'ของเป้าหมาย '+fm(goal):'ยังไม่ได้ตั้งเป้าหมาย',goalBtn:goal?'แก้ไขเป้าหมาย':'ตั้งเป้าหมายรายได้',
txs:rows,hasTx:rows.length>0,noTx:rows.length===0,
byStaff:bl.map(x=>({n:sName(d,+x[0]),w:Math.round(x[1]/bmx*100),v:fm(x[1])})),noByStaff:bl.length===0,topSv:sl.map(x=>({n:x[0],w:Math.round(x[1]/smx*100),v:x[1]+' ครั้ง'})),noTopSv:sl.length===0,
fm:modalOf(this,S,mo),toast:S.to,toastText:S.to}}}
"""

html = page('Solva – การเงิน', helmet_css('Main.dc.html') + '.tb2 .lk{border:0;background:none;font:inherit;cursor:pointer;color:inherit;text-align:left;padding:0;text-decoration:underline dotted}.rt .lk{border:0;background:none;font:inherit;cursor:pointer;color:inherit;text-align:left;padding:0;text-decoration:underline dotted}', body, js)
write('Finance.dc.html', html)
