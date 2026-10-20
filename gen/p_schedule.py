# -*- coding: utf-8 -*-
from core import *

EMPTYMINI = lambda msg: '<div class="em">' + HEART + '<div>' + msg + '</div></div>'
USR = '<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#3A3C4A" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="8" r="3.5"></circle><path d="M5 20c1-4 4-5.5 7-5.5s6 1.5 7 5.5"></path></svg>'

body = ('<div class="app">' + nav('Schedule') + '<main class="mn">' + header() +
 hero(hero_svg('Schedule.dc.html'),
      '{{heroWho}} <b class="cn" style="--v:{{nDay}}"></b> นัดหมาย', '{{heroSub}}',
      '<button class="bt" onClick="{{heroGo}}">{{heroBtn}}</button>') + WARN +
 '<sc-if value="{{noAny}}" hint-placeholder-val="{{false}}"><div class="empty">' + HEART +
 '<h2>ยังไม่มีนัดหมาย</h2><p>สร้างนัดหมายแรกเพื่อจองคิวให้ลูกค้า ระบบจะคำนวณราคา ส่วนลดสมาชิก และออกบิลให้อัตโนมัติ</p>'
 '<sc-if value="{{hasMiss}}"><div style="text-align:left;max-width:420px;margin:0 auto 16px"><b style="color:#2B2D3A">ต้องตั้งค่าก่อนสร้างนัดหมาย</b><sc-for list="{{miss}}" as="m"><a class="ck" href="{{m.h}}"><i>!</i><span>{{m.t}}</span></a></sc-for></div></sc-if>'
 '</div></sc-if>'
 '<sc-if value="{{hasAny}}" hint-placeholder-val="{{true}}"><h1>ตารางนัดหมาย · {{dateTxt}}</h1>'
 '<div class="row"><div class="stp"><button aria-label="วันก่อนหน้า" onClick="{{prev}}">‹</button><b>{{dateShort}}</b><button aria-label="วันถัดไป" onClick="{{next}}">›</button></div><button class="bt o" onClick="{{goToday}}">วันนี้</button>'
 '<select class="sel2" value="{{fs}}" onChange="{{onFs}}" aria-label="กรองพนักงาน"><sc-for list="{{fsOpts}}" as="o"><option value="{{o.v}}">{{o.t}}</option></sc-for></select>'
 '<select class="sel2" value="{{fst}}" onChange="{{onFst}}" aria-label="กรองสถานะ"><sc-for list="{{fstOpts}}" as="o"><option value="{{o.v}}">{{o.t}}</option></sc-for></select>'
 '<button class="bt" style="margin-left:auto" onClick="{{add}}">+ สร้างนัดหมาย</button><button class="bt d" onClick="{{png}}">บันทึกบิลเป็น PNG</button>'+CAPMENU+'</div>'
 '<sc-if value="{{hasConf}}"><div class="wn">⚠ {{confTxt}}</div></sc-if>'
 '<sc-if value="{{hasUt}}"><div class="c rs" style="margin-bottom:22px;--i:2"><h2>การใช้เวลาของช่างวันนี้</h2><sc-for list="{{ut}}" as="u"><div class="ut"><span>{{u.n}}</span><div class="bar"><i style="width:{{u.w}}%"></i></div><b>{{u.p}}</b></div></sc-for>'
 '<div class="mut" style="font-size:13px">คิดจากเวลาของบริการที่ใช้ เทียบกับเวลาทำงานของช่างแต่ละคน</div></div></sc-if>'
 '<div id="list" class="g2"><div><div class="c wk"><sc-for list="{{week}}" as="w"><button class="{{w.cls}}" aria-label="{{w.aria}}" onClick="{{w.pick}}"><small>{{w.d}}</small><b>{{w.n}}</b><em>{{w.fl}}</em></button></sc-for></div>'
 '<sc-for list="{{groups}}" as="g" hint-placeholder-count="2"><div class="tm">{{g.t}}</div><sc-for list="{{g.rows}}" as="a" hint-placeholder-count="1"><div class="sr {{a.on}}"><div class="av rg">' + USR + '</div><div class="x"><button class="nb" onClick="{{a.pick}}">{{a.cust}}</button><small>{{a.sub}}</small></div><span class="ch {{a.sc}}">{{a.st}}</span></div></sc-for></sc-for>'
 '<sc-if value="{{noDay}}" hint-placeholder-val="{{false}}"><div class="c">' + EMPTYMINI('ไม่มีนัดหมายที่ตรงกับตัวกรองในวันนี้<br><button class="bt" style="margin-top:12px" onClick="{{add}}">สร้างนัดหมาย</button>') + '</div></sc-if></div>'
 '<div class="c tk"><sc-if value="{{noSel}}" hint-placeholder-val="{{false}}">' + EMPTYMINI('เลือกนัดหมายจากรายการเพื่อดูรายละเอียดและบิล') + '</sc-if>'
 '<sc-if value="{{hasSel}}" hint-placeholder-val="{{true}}"><h1 style="font-size:30px;margin:0">{{sel.cust}}</h1><div style="color:#6B6D7A">{{sel.nick}}{{sel.timeTxt}} · ช่าง {{sel.staff}}</div><div style="font-weight:600;color:#6B6D7A;margin:6px 0">{{sel.memTxt}} · เลขที่บิล {{sel.no}}</div>'
 '<div style="border-top:2px solid #D9D9D9;margin:14px 0"></div><h2>โน้ตลูกค้า</h2><sc-if value="{{sel.hasNotes}}"><div class="row"><sc-for list="{{sel.notes}}" as="n"><span class="ch nt">{{n.t}}</span></sc-for></div></sc-if>'
 '<sc-if value="{{sel.noNotes}}"><p class="mut" style="margin:0 0 14px">ไม่มีโน้ต</p></sc-if>'
 '<sc-if value="{{sel.hasANote}}"><h2>หมายเหตุนัดหมาย</h2><p style="margin:0 0 14px">{{sel.aNote}}</p></sc-if>'
 '<h2>รายการวันนี้</h2><div class="rc h"><span>บริการ</span><span>ราคา</span></div><sc-for list="{{sel.items}}" as="i"><div class="rc"><span>{{i.n}}</span><span>{{i.p}}</span></div></sc-for>'
 '<div class="rc"><span>รวมก่อนหักส่วนลด</span><span>{{sel.sub}}</span></div><sc-if value="{{sel.hasDisc}}"><div class="rc"><span>ส่วนลด {{sel.memTxt}} {{sel.pct}}%</span><span>{{sel.disc}}</span></div></sc-if>'
 '<sc-if value="{{sel.hasTip}}"><div class="rc"><span>ทิป</span><span>{{sel.tip}}</span></div></sc-if><div class="dv"></div><div class="tot"><span>ยอดสุทธิ</span><b>{{sel.net}}</b></div>'
 '<div class="kv"><span>วิธีชำระ</span><b>{{sel.method}}</b></div><div class="kv"><span>สถานะ</span><span class="ch {{sel.pc}}">{{sel.ps}}</span></div>'
 '<sc-if value="{{sel.payOpen}}"><div class="tl" style="grid-template-columns:1fr 1fr;margin-top:12px"><div><small>วิธีชำระเงิน</small><select class="sel2" style="background:#fff;width:100%" value="{{payM}}" onChange="{{onPayM}}"><sc-for list="{{payOpts}}" as="o"><option value="{{o.v}}">{{o.t}}</option></sc-for></select></div><div><small>ทิป (บาท)</small><input class="si" style="width:100%;max-width:none;min-width:0" inputmode="decimal" placeholder="0" value="{{payTip}}" onInput="{{onPayTip}}"></div></div>'
 '<div class="row" style="margin:0"><button class="bt" onClick="{{sel.payOk}}">ยืนยันรับชำระ {{sel.net}}</button><button class="bt d" onClick="{{sel.payNo}}">ยกเลิก</button></div></sc-if>'
 '<div class="row" style="margin:16px 0 0"><sc-for list="{{sel.acts}}" as="b"><button class="bt {{b.cls}}" onClick="{{b.go}}">{{b.t}}</button></sc-for>'
 '<sc-if value="{{sel.hasBill}}"><button class="bt o" disabled="{{busy}}" onClick="{{png}}">{{sel.pngTxt}}</button></sc-if><a class="bt o" href="Clients.dc.html">ดูโปรไฟล์ลูกค้า</a></div>'
 '<sc-if value="{{sel.noBill}}"><p class="mut" style="margin:10px 0 0">นัดนี้ไม่มีบิลให้บันทึก ({{sel.ps}})</p></sc-if></sc-if></div></div></sc-if>'
 + MODAL + '</main></div>')

css_extra = ('.mb{height:auto;gap:0}.wk button{border:0;background:none;font:inherit;padding:10px 8px;border-radius:30px;min-width:46px;cursor:pointer;text-align:center;color:inherit}.wk button.sl{background:#D9D9D9;padding:14px 8px 18px}.wk button.p b{background:#FFDFFF}.wk button em{display:block;font-style:normal;font-size:10px;font-weight:600}.wk button em:empty{display:none}.wk button.fu b{background:#FF9AFF;color:#2B2D3A}.wk button.fu em{color:#4A4C5A}'
             '.sr button.nb{font-size:15px}.sr small{display:block}')

js = png_js() + r"""
const ST_OPTS=[['all','ทุกสถานะ'],['booked','ยืนยันแล้ว'],['unpaid','รอชำระเงิน'],['done','เสร็จสิ้น'],['noshow','ไม่มาตามนัด'],['canceled','ยกเลิก']];
const stKey=a=>a.status==='done'?(a.paid?'done':'unpaid'):a.status;
const mkAppt=(date)=>({_k:'appt',cust:'',newName:'',newPhone:'',staff:'',date:date,time:'10:00',svs:[],note:''});
class Component extends Base{
async share(spec,fn){this.setState({busy:true});try{await savePng(spec,fn);this.toast('บันทึกรูปเรียบร้อย ✓')}catch(e){this.toast(e&&e.code==='declined'?'ยกเลิกการบันทึก':e&&e.code==='unavailable'?'มุมมองนี้ยังบันทึกไฟล์ไม่ได้ ลองเปิดจากลิงก์ที่แชร์':'สร้างรูปไม่สำเร็จ กรุณาลองอีกครั้ง',2800)}this.setState({busy:false})}
boot(){const u=uiGet(),o={};if(u.date){o.date=u.date;uiSet({date:''})}if(u.open==='appt'){uiSet({open:''});o.form=mkAppt(o.date||TODAY());o.fe=''}if(u.sel){o.sel=u.sel;uiSet({sel:0})}if(Object.keys(o).length)this.setState(o)}
renderVals(){
const d=load(),T=TODAY(),S=Object.assign({date:T,fs:'all',fst:'all',sel:null,form:null,fe:'',cdel:false,payOpen:false,payM:'',payTip:'',busy:false,to:''},this.state),set=o=>this.setState(o),toast=m=>this.toast(m);
const D=S.date,dayAll=d.appts.filter(a=>a.date===D).sort((a,b)=>a.time.localeCompare(b.time)||a.id-b.id);
const day=dayAll.filter(a=>(S.fs==='all'||String(a.staff)===S.fs)&&(S.fst==='all'||stKey(a)===S.fst));
const conf=dayAll.filter(a=>overlap(d,a).length>0);
const gm={};day.forEach(a=>{(gm[a.time]=gm[a.time]||[]).push(a)});
const groups=Object.keys(gm).sort().map(t=>({t:t.replace(':','.')+' น.',rows:gm[t].map(a=>{const z=stOf(a);return{cust:cName(d,a.cust),sub:'ช่าง '+sName(d,a.staff)+' · '+a.items.map(i=>i.name).join(' + ')+(overlap(d,a).length?' · ⚠ คิวซ้อน':''),st:z[0],sc:z[1],on:S.sel===a.id?'on':'',pick:()=>set({sel:a.id,payOpen:false})}})}));
const dt=pd(D),wkS=new Date(dt.getFullYear(),dt.getMonth(),dt.getDate()-dt.getDay());
const week=[0,1,2,3,4,5,6].map(i=>{const x=new Date(wkS.getFullYear(),wkS.getMonth(),wkS.getDate()+i),s=iso(x),n=d.appts.filter(a=>a.date===s&&a.status!=='canceled').length;return{d:TH_S[i],n:x.getDate(),fl:n>=capOf(d)?'คิวเต็ม':'',cls:(s===D?'sl':n?'p':'')+(n>=capOf(d)?' fu':''),aria:thL(s)+(n>=capOf(d)?' คิวเต็ม':' มี '+n+' นัดหมาย'),pick:()=>set({date:s,sel:null})}});
const ut=d.staff.map(s=>{const m=sum(dayAll.filter(a=>a.staff===s.id&&a.status!=='canceled'&&a.status!=='noshow'),a=>dur(a)),cap=Math.max(1,tmin(s.we||'18:00')-tmin(s.ws||'09:00')),p=Math.round(m/cap*100);return{n:s.name,w:Math.min(100,p),p:p+'%'}});
const a=d.appts.find(x=>x.id===S.sel);let sel={},png=()=>toast('เลือกนัดหมายจากรายการก่อน');
const billable=a=>a&&(a.status==='done'||a.status==='booked');
if(a){const sb=sub(a),ds=dsc(a),nt=net(a),z=stOf(a),c=getC(d,a.cust),mem=a.tier?'สมาชิก '+a.tier:'Non-member',date=thD(a.date)+' · '+a.time+' น.',bill=billable(a);
const spec={w:560,shop:d.shop.name||'Solva',title:'ใบเสร็จค่าบริการ',info:[['เลขที่บิล',a.no],['วันที่/เวลา',date],['ลูกค้า',cName(d,a.cust)+(c&&c.nick?' ('+c.nick+')':'')],['ระดับสมาชิก',mem],['พนักงานผู้ให้บริการ',sName(d,a.staff)]],cols:[{w:.72,al:'l'},{w:.28,al:'r'}],head:['รายการบริการ','ราคา'],rows:a.items.map(i=>[i.name,fm(i.price)]),
sum:[{k:'รวมก่อนหักส่วนลด',v:fm(sb)}].concat(a.disc?[{k:'ส่วนลดสมาชิก '+a.tier+' '+a.disc+'%',v:'−'+fm(ds)}]:[{k:'ส่วนลดสมาชิก',v:'—'}],a.tip?[{k:'ทิป',v:fm(a.tip)}]:[],[{k:'ยอดสุทธิที่ต้องชำระ',v:fm(nt+(a.tip||0)),big:1}]),
pay:[['วิธีชำระเงิน',a.method||'ยังไม่ระบุ'],['สถานะการชำระเงิน',a.paid?'ชำระแล้ว':'รอชำระ',a.paid?['#CDEFD9','#1F7A4D']:['#FBE8A6','#8A6500']]],notes:((c&&c.notes&&c.notes.length)?['โน้ตลูกค้า: '+c.notes.join(', ')]:[]).concat(a.note?['หมายเหตุ: '+a.note]:[]),foot:['ขอบคุณที่ใช้บริการ','จัดทำโดยระบบ Solva']};
png=()=>bill?this.share(spec,'solva-bill-'+a.no+'.png'):toast('นัดที่ยกเลิกหรือไม่มาตามนัดไม่มีบิลให้บันทึก');
const setSt=(s,m)=>()=>{if(a.status==='canceled'&&s!=='canceled'&&isFull(d,a.date,a.id))return toast('คิววันที่ '+thS(a.date)+' เต็มแล้ว ('+capOf(d)+' คิว) กู้คืนนัดนี้ไม่ได้');M(x=>{x.appts.find(w=>w.id===a.id).status=s});toast(m)};
const acts=[];
if(a.status==='booked'){acts.push({t:'เสร็จสิ้นงาน',cls:'',go:setSt('done','บันทึกว่างานเสร็จสิ้นแล้ว')});acts.push({t:'ไม่มาตามนัด',cls:'d',go:setSt('noshow','บันทึกว่าไม่มาตามนัดแล้ว')});acts.push({t:'ยกเลิกนัด',cls:'d',go:setSt('canceled','ยกเลิกนัดหมายแล้ว')})}
if(a.status==='done'&&!a.paid)acts.push({t:'รับชำระเงิน',cls:'',go:()=>set({payOpen:true,payM:S.payM||PAYM[0],payTip:''})});
if(a.status==='done'&&a.paid)acts.push({t:'ยกเลิกการรับชำระ',cls:'d',go:()=>{M(x=>{const w=x.appts.find(y=>y.id===a.id);w.paid=false;w.cp=false;w.paidDate='';w.tip=0});toast('ยกเลิกการรับชำระแล้ว')}});
if(a.status==='canceled'||a.status==='noshow')acts.push({t:'คืนเป็นยืนยันแล้ว',cls:'',go:setSt('booked','คืนสถานะเป็นยืนยันแล้ว')});
if(a.status==='done'&&!a.paid)acts.push({t:'ย้อนเป็นยืนยันแล้ว',cls:'d',go:setSt('booked','ย้อนสถานะแล้ว')});
acts.push({t:'แก้ไขนัด',cls:'o',go:()=>{if(a.paid)return toast('นัดที่รับชำระแล้วแก้ไขไม่ได้ กด “ยกเลิกการรับชำระ” ก่อน');set({form:{_k:'appt',id:a.id,cust:String(a.cust),newName:'',newPhone:'',staff:String(a.staff),date:a.date,time:a.time,svs:a.items.map(i=>i.sid),note:a.note||''},fe:'',cdel:false})}});
sel={cust:cName(d,a.cust),nick:c&&c.nick?'('+c.nick+') · ':'',staff:sName(d,a.staff),timeTxt:date,memTxt:mem,no:a.no,notes:((c&&c.notes)||[]).map(t=>({t})),hasNotes:!!(c&&c.notes&&c.notes.length),noNotes:!(c&&c.notes&&c.notes.length),hasANote:!!a.note,aNote:a.note||'',
items:a.items.map(i=>({n:i.name,p:fm(i.price)})),sub:fm(sb),hasDisc:ds>0,pct:a.disc||0,disc:'−'+fm(ds),hasTip:!!a.tip,tip:fm(a.tip||0),net:fm(nt),method:a.method||'ยังไม่ระบุ',ps:z[0],pc:z[1],
payOpen:S.payOpen&&a.status==='done'&&!a.paid,payOk:()=>{const tip=Math.max(0,+S.payTip||0);M(x=>{const w=x.appts.find(y=>y.id===a.id);w.paid=true;w.method=S.payM||PAYM[0];w.tip=tip;w.paidDate=TODAY();w.cp=false});set({payOpen:false});toast('รับชำระเงินเรียบร้อย '+fm(nt))},payNo:()=>set({payOpen:false}),
acts,hasBill:bill,noBill:!bill,pngTxt:S.busy?'กำลังสร้างรูป…':'Save as PNG'}}
const F=S.form,fk=F&&F._k;let mo={};
if(fk==='shop')mo=shopMo(this,F,S);if(fk==='cap')mo=capMo(this,F,S);
if(fk==='appt'){const miss=missing(d),isNew=F.cust==='__new',cu=isNew||!F.cust?null:getC(d,+F.cust),tr=cu?tierO(d,cu):null,svs=(F.svs||[]).map(id=>d.services.find(z=>z.id===id)||(F.id&&(d.appts.find(w=>w.id===F.id)||{items:[]}).items.find(i=>i.sid===id))).filter(Boolean).map(z=>({sid:z.id||z.sid,name:z.name,cat:z.cat||'',price:z.price,dur:z.dur||0}));
const tmp={id:F.id||-1,staff:+F.staff,date:F.date,time:F.time,items:svs,disc:tr?tr.disc:0,status:'booked'},ov=F.staff&&F.date&&F.time?overlap(d,tmp):[];
const sm=svs.length?'ยอดรวม '+fm(sub(tmp))+(tmp.disc?' · ส่วนลดสมาชิก '+tr.n+' '+tmp.disc+'% −'+fm(dsc(tmp)):'')+' · สุทธิ '+fm(net(tmp))+(dur(tmp)?' · ใช้เวลา '+dur(tmp)+' นาที':''):'เลือกบริการเพื่อดูยอดรวม';
const spec=[{k:'cust',label:'ลูกค้า',full:1,opts:[['','เลือกลูกค้า…']].concat(d.customers.map(c=>[String(c.id),c.name+(c.phone?' · '+c.phone:'')]),[['__new','+ ลูกค้าใหม่ (กรอกชื่อด้านล่าง)']])}];
if(isNew){spec.push({k:'newName',label:'ชื่อลูกค้าใหม่',ph:'เช่น คุณสุดา'},{k:'newPhone',label:'เบอร์โทร (ไม่บังคับ)',type:'tel'})}
spec.push({k:'staff',label:'ช่างที่ให้บริการ',opts:[['','เลือกพนักงาน…']].concat(d.staff.map(s=>[String(s.id),s.name]))},{k:'date',label:'วันที่',type:'date'},{k:'time',label:'เวลา',type:'time'},
{k:'svs',label:'บริการ (เลือกได้หลายอย่าง)',full:1,chips:d.services.map(z=>[z.id,z.name+' · '+fm(z.price)])},{k:'sm',label:'สรุป',full:1,note:sm+(ov.length?' ⚠ ช่างคนนี้มีนัดซ้อนเวลา '+ov.length+' รายการ (ยังบันทึกได้)':''),wr:ov.length>0},{k:'note',label:'หมายเหตุ (ไม่บังคับ)',full:1,ta:1,ph:'เช่น ต้องการห้องส่วนตัว'});
mo={title:F.id?'แก้ไขนัดหมาย':'สร้างนัดหมาย',hint:miss.length?'ต้อง'+miss.map(m=>m.t).join(' และ')+'ก่อน (เมนู “บริการ” และ “พนักงาน”)':'',spec,saveTxt:F.id?'บันทึกการแก้ไข':'สร้างนัดหมาย',
save:()=>{if(miss.length)return set({fe:'ยังสร้างนัดหมายไม่ได้: ต้อง'+miss.map(m=>m.t).join(' และ')+'ก่อน'});
if(!F.cust)return set({fe:'กรุณาเลือกลูกค้า'});if(isNew&&!(F.newName||'').trim())return set({fe:'กรุณากรอกชื่อลูกค้าใหม่'});if(!F.staff)return set({fe:'กรุณาเลือกช่าง'});if(!F.date||!F.time)return set({fe:'กรุณาเลือกวันและเวลา'});if(!svs.length)return set({fe:'กรุณาเลือกบริการอย่างน้อย 1 อย่าง'});if(isFull(d,F.date,F.id||-1))return set({fe:(F.date===T?'คิววันนี้':'คิววันที่ '+thS(F.date))+'เต็มแล้ว ('+capOf(d)+' คิว) กรุณาเลือกวันหรือเวลาอื่น'});
let sid;M(x=>{let cid=+F.cust;if(isNew){cid=x.seq++;const ph=(F.newPhone||'').trim();x.customers.push({id:cid,name:F.newName.trim(),nick:'',phone:ph,bd:'',line:'',tier:'',since:'',created:TODAY(),notes:[]})}
const c=getC(x,cid),tr=tierO(x,c),v={cust:cid,staff:+F.staff,date:F.date,time:F.time,items:svs,note:(F.note||'').trim(),disc:tr?tr.disc:0,tier:tr?tr.n:''};
if(F.id){Object.assign(x.appts.find(w=>w.id===F.id),v);sid=F.id}else{const same=x.appts.filter(w=>w.date===F.date).map(w=>+(w.no||'').split('-')[2]||0),no='INV-'+F.date.replace(/-/g,'')+'-'+p2(Math.max(0,...same)+1).padStart(3,'0');sid=x.seq++;x.appts.push(Object.assign({id:sid,no,status:'booked',paid:false,method:'',tip:0,cp:false,created:TODAY()},v))}});
set({form:null,fe:'',date:F.date,sel:sid,fs:'all',fst:'all'});toast(F.id?'บันทึกการแก้ไขแล้ว':'สร้างนัดหมายแล้ว')},
del:F.id?(()=>{if(!S.cdel)return set({cdel:true});M(x=>{x.appts=x.appts.filter(w=>w.id!==F.id)});set({form:null,cdel:false,sel:null});toast('ลบนัดหมายแล้ว')}):null,delTxt:'ลบนัดหมาย'}}
const nDay=dayAll.filter(x=>x.status!=='canceled').length,anyA=d.appts.length>0,m0=missing(d);
return{today:thL(T),noStore:!OKS,openShop:()=>openShopForm(this),
heroWho:D===T?'วันนี้':thS(D),nDay,heroSub:conf.length?'คิวซ้อน '+conf.length+' รายการ ควรตรวจสอบก่อนเริ่มงาน':anyA?(nDay?'ไม่มีคิวซ้อน':'ยังไม่มีนัดหมายในวันนี้'):'เริ่มต้นด้วยการสร้างนัดหมายแรก',heroBtn:conf.length?'ดูคิวซ้อน':anyA?'+ สร้างนัดหมาย':'สร้างนัดหมายแรก',heroGo:()=>{if(conf.length){set({fs:'all',fst:'all'});const e=document.getElementById('list');e&&e.scrollIntoView&&e.scrollIntoView({behavior:'smooth'})}else set({form:mkAppt(D),fe:''})},
add:()=>set({form:mkAppt(D),fe:'',cdel:false}),hasAny:anyA,noAny:!anyA,hasMiss:m0.length>0,miss:m0,
dateTxt:thL(D),dateShort:D===T?'วันนี้ · '+thS(D):thS(D)+' '+(pd(D).getFullYear()+543),prev:()=>set({date:iso(new Date(dt.getFullYear(),dt.getMonth(),dt.getDate()-1)),sel:null}),next:()=>set({date:iso(new Date(dt.getFullYear(),dt.getMonth(),dt.getDate()+1)),sel:null}),goToday:()=>set({date:T,sel:null}),
fs:S.fs,onFs:e=>set({fs:e.target.value}),fsOpts:[{v:'all',t:'ทุกพนักงาน'}].concat(d.staff.map(s=>({v:String(s.id),t:s.name}))),fst:S.fst,onFst:e=>set({fst:e.target.value}),fstOpts:ST_OPTS.map(o=>({v:o[0],t:o[1]})),
hasConf:conf.length>0,confTxt:'คิวซ้อน '+conf.length+' รายการ: '+conf.map(x=>sName(d,x.staff)+' '+x.time+' ('+cName(d,x.cust)+')').join(', '),
menuOpen:!!S.menu,toggleMenu:this.toggleMenu,openCap:()=>openCapForm(this),hasUt:ut.length>0&&dayAll.length>0,ut,week,groups,noDay:day.length===0,hasSel:!!a,noSel:!a,sel,png,busy:!!S.busy,
payM:S.payM,onPayM:e=>set({payM:e.target.value}),payOpts:PAYM.map(x=>({v:x,t:x})),payTip:S.payTip,onPayTip:e=>set({payTip:e.target.value}),
fm:modalOf(this,S,mo),toast:S.to,toastText:S.to}}}
"""

html = page('Solva – ตารางนัด', helmet_css('Schedule.dc.html') + css_extra, body, js)
write('Schedule.dc.html', html)
