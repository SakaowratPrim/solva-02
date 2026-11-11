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
 '<button class="bt" data-tour="appt" style="margin-left:auto" onClick="{{add}}">+ สร้างนัดหมาย</button><button class="bt d" onClick="{{png}}">บันทึกบิลเป็น PNG</button>'+CAPMENU+'</div>'
 '<sc-if value="{{hasConf}}"><div class="wn">⚠ {{confTxt}}</div></sc-if>'
 '<sc-if value="{{hasUt}}"><div class="c rs" style="margin-bottom:22px;--i:2"><h2>การใช้เวลาของช่างวันนี้</h2><sc-for list="{{ut}}" as="u"><div class="ut"><span>{{u.n}}</span><div class="bar"><i style="width:{{u.w}}%"></i></div><b>{{u.p}}</b></div></sc-for>'
 '<div class="mut" style="font-size:13px">คิดจากเวลาของบริการที่ใช้ เทียบกับเวลาทำงานของช่างแต่ละคน</div></div></sc-if>'
 '<div id="list" class="g2"><div><div class="c wk"><sc-for list="{{week}}" as="w"><button class="{{w.cls}}" aria-label="{{w.aria}}" onClick="{{w.pick}}"><small>{{w.d}}</small><b>{{w.n}}</b><em>{{w.fl}}</em></button></sc-for></div>'
 '<sc-for list="{{groups}}" as="g" hint-placeholder-count="2"><div class="sxtg"><button class="sxtt" aria-label="ดูช่างว่างเวลา {{g.t}}" onClick="{{g.pickT}}">{{g.t}}</button><div class="sxtcs"><sc-for list="{{g.rows}}" as="a" hint-placeholder-count="1"><div class="sxaw"><i class="sxbar {{a.bc}}"></i><div class="sxac {{a.pc}} {{a.on}}" role="button" tabindex="0" onClick="{{a.pick}}" onKeyDown="{{a.key}}"><span class="sxfav">' + USR + '</span><span class="x"><b>{{a.staff}}</b><small>{{a.sv}}</small><small class="cu">ลูกค้า: {{a.cust}}</small></span><span class="sxr2"><span class="sxck2 {{a.ckc}}" role="img" aria-label="{{a.ckl}}"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="butt" stroke-linejoin="miter"><path d="M5 12.5L10 17.5L19 7"></path></svg></span><span class="ch {{a.sc}}">{{a.st}}</span></span></div></div></sc-for></div></div></sc-for>'
 '<sc-if value="{{noDay}}" hint-placeholder-val="{{false}}"><div class="c">' + EMPTYMINI('ไม่มีนัดหมายที่ตรงกับตัวกรองในวันนี้<br><button class="bt" style="margin-top:12px" onClick="{{add}}">สร้างนัดหมาย</button>') + '</div></sc-if></div>'
 '<div class="c tk"><div class="sxtabs"><span class="sxtb on">รายชื่อช่างประจำวัน</span><sc-if value="{{hasStaff}}"><select class="sxftsel" value="{{ft}}" onChange="{{onFt}}" aria-label="เลือกเวลา"><sc-for list="{{ftOpts}}" as="o"><option value="{{o.v}}">{{o.t}}</option></sc-for></select></sc-if></div>'
 '<sc-if value="{{hasStaff}}"><p class="mut" style="margin:8px 0 14px">{{ftSum}}</p><div class="sxfsg"><sc-for list="{{fstaff}}" as="m"><div class="sxfs {{m.cls}}"><span class="sxfav">' + USR + '</span><b>{{m.n}}</b><small>{{m.sk}}</small><sc-if value="{{m.hasBt}}"><button class="bt d" onClick="{{m.go}}">{{m.bt}}</button></sc-if><sc-if value="{{m.noBt}}"><span class="sxfl">{{m.fl}}</span></sc-if></div></sc-for></div><sc-if value="{{noStaff}}">' + EMPTYMINI('ยังไม่มีพนักงาน เพิ่มพนักงานที่เมนู “พนักงาน”') + '</sc-if></sc-if>'
 '</div></div>'
 '<sc-if value="{{isDet}}" hint-placeholder-val="{{false}}"><div class="ov" onClick="{{closeDet}}"><div class="md dt" onClick="{{stopP}}"><button class="dtx" aria-label="ปิด" onClick="{{closeDet}}">✕</button><div class="dta">'
 '<h1 style="font-size:30px;margin:0">{{sel.cust}}</h1><div style="color:#6B6D7A">{{sel.nick}}{{sel.timeTxt}} · ช่าง {{sel.staff}}</div><div style="font-weight:600;color:#6B6D7A;margin:6px 0">{{sel.memTxt}} · เลขที่บิล {{sel.no}}</div>'
 '<div style="border-top:2px solid #D9D9D9;margin:14px 0"></div><h2>โน้ตลูกค้า</h2><sc-if value="{{sel.hasNotes}}"><div class="row"><sc-for list="{{sel.notes}}" as="n"><span class="ch nt">{{n.t}}</span></sc-for></div></sc-if>'
 '<sc-if value="{{sel.noNotes}}"><p class="mut" style="margin:0 0 14px">ไม่มีโน้ต</p></sc-if>'
 '<sc-if value="{{sel.hasANote}}"><h2>หมายเหตุนัดหมาย</h2><p style="margin:0 0 14px">{{sel.aNote}}</p></sc-if>'
 '<h2>รายการวันนี้</h2><div class="rc h"><span>บริการ</span><span>ราคา</span></div><sc-for list="{{sel.items}}" as="i"><div class="rc"><span>{{i.n}}</span><span>{{i.p}}</span></div></sc-for>'
 '<div class="rc"><span>รวมก่อนหักส่วนลด</span><span>{{sel.sub}}</span></div><sc-if value="{{sel.hasDisc}}"><div class="rc"><span>ส่วนลด {{sel.memTxt}} {{sel.pct}}%</span><span>{{sel.disc}}</span></div></sc-if>'
 '<sc-if value="{{sel.hasTip}}"><div class="rc"><span>ทิป</span><span>{{sel.tip}}</span></div></sc-if></div><div class="dtb"><div class="tot"><span>ยอดสุทธิ</span><b>{{sel.net}}</b></div>'
 '<div class="kv"><span>วิธีชำระ</span><b>{{sel.method}}</b></div><div class="kv"><span>สถานะ</span><span class="ch {{sel.pc}}">{{sel.ps}}</span></div>'
 '<sc-if value="{{sel.payOpen}}"><div class="tl" style="grid-template-columns:1fr 1fr;margin-top:12px"><div><small>วิธีชำระเงิน</small><select class="sel2" style="background:#fff;width:100%" value="{{payM}}" onChange="{{onPayM}}"><sc-for list="{{payOpts}}" as="o"><option value="{{o.v}}">{{o.t}}</option></sc-for></select></div><div><small>ทิป (บาท)</small><input class="si" style="width:100%;max-width:none;min-width:0" inputmode="decimal" placeholder="0" value="{{payTip}}" onInput="{{onPayTip}}"></div></div>'
 '<div class="row" style="margin:0"><button class="bt" onClick="{{sel.payOk}}">ยืนยันรับชำระ {{sel.net}}</button><button class="bt d" onClick="{{sel.payNo}}">ยกเลิก</button></div></sc-if>'
 '<div class="row" style="margin:16px 0 0"><sc-for list="{{sel.acts}}" as="b"><button class="bt {{b.cls}}" onClick="{{b.go}}">{{b.t}}</button></sc-for>'
 '<sc-if value="{{sel.hasBill}}"><button class="bt o" disabled="{{busy}}" onClick="{{png}}">{{sel.pngTxt}}</button></sc-if><a class="bt o" href="Clients.dc.html">ดูโปรไฟล์ลูกค้า</a></div>'
 '<sc-if value="{{sel.noBill}}"><p class="mut" style="margin:10px 0 0">นัดนี้ไม่มีบิลให้บันทึก ({{sel.ps}})</p></sc-if></div></div></div></sc-if></sc-if>'
 + '<button class="fab" aria-label="สร้างนัดหมาย" onClick="{{add}}"><svg width="32" height="32" viewBox="0 0 32 32" stroke="#FF9AFF" stroke-width="3" stroke-linecap="round"><path d="M16 5v22M5 16h22"></path></svg></button>' + MODAL + '</main></div>')

css_extra = ('.mb{height:auto;gap:0}.wk button{border:0;background:none;font:inherit;padding:10px 8px;border-radius:30px;min-width:46px;cursor:pointer;text-align:center;color:inherit}.wk button.sl{background:#D9D9D9;padding:14px 8px 18px}.wk button.p b{background:#FFDFFF}.wk button em{display:block;font-style:normal;font-size:10px;font-weight:600}.wk button em:empty{display:none}.wk button.fu b{background:#FF9AFF;color:#2B2D3A}.wk button.fu em{color:#4A4C5A}'
             '.sr button.nb{font-size:15px}.sr small{display:block}'
 '.wk{margin-bottom:16px}.sxtg{display:grid;grid-template-columns:84px 1fr;gap:6px 12px;margin:0 0 6px}.sxtt{border:0;background:none;font:inherit;font-weight:600;font-size:18px;text-align:left;cursor:pointer;padding:10px 0;color:inherit;align-self:start}.sxtt:hover{color:#B3299E}.sxtcs{min-width:0}'
 '.sxaw{display:flex;gap:12px;margin:0 0 12px}.sxbar{flex:none;width:6px;border-radius:4px;background:#FF66D9}.sxbar.sxgr{background:#9A9CAA}'
 '.sxac{flex:1;min-width:0;display:flex;align-items:center;gap:16px;border:0;font:inherit;text-align:left;cursor:pointer;background:#fff;border-radius:22px;padding:18px 20px;box-shadow:0 6px 20px rgba(60,40,70,.08);color:inherit;position:relative}.sxac.sxpd,.sxac.sxcx{background:#E9E9E9;box-shadow:none}.sxac.on{outline:3px solid #FF9AFF}'
 '.sxfav{flex:none;width:68px;height:68px;border-radius:50%;background:#D9D9D9;display:grid;place-items:center}.sxfav svg{width:36px;height:36px}.sxac .x{flex:1;min-width:0}.sxac .x b{display:block;font-size:20px}.sxac .x small{display:block;font-size:14px;font-weight:600;margin-top:2px;overflow-wrap:anywhere}.sxac .x small.cu{margin-top:12px}'
 '.sxr2{align-self:stretch;display:flex;flex-direction:column;align-items:flex-end;justify-content:space-between;gap:8px}.sxck2{width:32px;height:32px;border-radius:50%;border:2px solid #2B2D3A;background:#fff;display:grid;place-items:center;font-size:18px;color:#fff;line-height:1}.sxck2 svg{display:none}.sxck2.sxy svg{display:block}.sxck2.sxy{background:#2B2D3A}'
 '.md.dt{width:min(520px,100%);padding:0;background:none;box-shadow:none;border-radius:0;position:relative;filter:drop-shadow(0 18px 36px rgba(60,40,70,.28))}.dta,.dtb{background:#fff;padding:26px 26px 18px}.dta{border-radius:28px 28px 0 0;-webkit-mask:radial-gradient(circle 16px at 0 100%,#0000 97%,#000),radial-gradient(circle 16px at 100% 100%,#0000 97%,#000);mask:radial-gradient(circle 16px at 0 100%,#0000 97%,#000),radial-gradient(circle 16px at 100% 100%,#0000 97%,#000);mask-composite:intersect;-webkit-mask-composite:source-in}.dtb{border-radius:0 0 28px 28px;position:relative;padding-top:22px;-webkit-mask:radial-gradient(circle 16px at 0 0,#0000 97%,#000),radial-gradient(circle 16px at 100% 0,#0000 97%,#000);mask:radial-gradient(circle 16px at 0 0,#0000 97%,#000),radial-gradient(circle 16px at 100% 0,#0000 97%,#000);mask-composite:intersect;-webkit-mask-composite:source-in}.dtb:before{content:"";position:absolute;left:24px;right:24px;top:0;border-top:2px dashed #D9D9D9}.dtx{position:absolute;top:14px;right:14px;z-index:2;min-height:36px;width:36px;padding:0;border-radius:50%;background:#F1F1F1;box-shadow:none;font-size:15px}.md.dt h1{padding-right:40px}.sxtabs{display:flex;align-items:center;gap:8px;flex-wrap:wrap}.sxtb{border:0;font:inherit;font-weight:600;border-radius:22px;padding:10px 18px;cursor:pointer;background:#F1F1F1;color:inherit}.sxtb.on{background:#FF9AFF}.sxftsel{margin-left:auto;border:0;background:none;font:inherit;font-size:20px;cursor:pointer;color:inherit}'
 '.sxfsg{display:grid;grid-template-columns:repeat(auto-fill,minmax(130px,1fr));gap:22px 12px;margin-top:6px}.sxfs{display:flex;flex-direction:column;align-items:center;text-align:center;gap:2px}.sxfs .sxfav{width:78px;height:78px;margin-bottom:8px;background:#B5B5B5}.sxfs.sxok .sxfav{box-shadow:0 0 0 5px #FFC9FF}.sxfs b{font-size:19px}.sxfs small{font-size:13px;font-weight:600}.sxfs .bt{margin-top:8px;min-height:40px;padding:0 16px;font-size:14px}.sxfs .sxfl{margin-top:6px;font-size:13px;font-weight:600;color:#1F7A4D}.sxfs.sxoff .sxfl{color:#6B6D7A}'
 '@media(max-width:820px){.sxtg{grid-template-columns:1fr}.sxtt{padding:4px 0}.sxac{padding:14px;gap:12px}.sxfav{width:56px;height:56px}.sxac .x b{font-size:17px}}')

js = png_js() + r"""
const ST_OPTS=[['all','ทุกสถานะ'],['booked','ยืนยันแล้ว'],['unpaid','รอชำระเงิน'],['done','เสร็จสิ้น'],['noshow','ไม่มาตามนัด'],['canceled','ยกเลิก']];
const stKey=a=>a.status==='done'?(a.paid?'done':'unpaid'):a.status;
const mkAppt=(date)=>({_k:'appt',cust:'',newName:'',newPhone:'',staff:'',date:date,time:'10:00',svs:[],note:''});
class Component extends Base{
async share(spec,fn){this.setState({busy:true});try{await savePng(spec,fn);this.toast('บันทึกรูปเรียบร้อย ✓')}catch(e){this.toast(e&&e.code==='declined'?'ยกเลิกการบันทึก':e&&e.code==='unavailable'?'มุมมองนี้ยังบันทึกไฟล์ไม่ได้ ลองเปิดจากลิงก์ที่แชร์':'สร้างรูปไม่สำเร็จ กรุณาลองอีกครั้ง',2800)}this.setState({busy:false})}
boot(){const u=uiGet(),o={};if(u.date){o.date=u.date;uiSet({date:''})}if(u.open==='appt'){uiSet({open:''});o.form=mkAppt(o.date||TODAY());o.fe=''}if(u.sel){o.sel=u.sel;o.rt='detail';uiSet({sel:0})}if(Object.keys(o).length)this.setState(o)}
renderVals(){
const d=load(),T=TODAY(),S=Object.assign({date:T,fs:'all',fst:'all',sel:null,form:null,fe:'',cdel:false,payOpen:false,payM:'',payTip:'',busy:false,to:'',rt:'free',ft:''},this.state),set=o=>this.setState(o),toast=m=>this.toast(m);
const goTk=()=>setTimeout(()=>{const e=document.querySelector('.tk');if(e&&innerWidth<=820)e.scrollIntoView({behavior:'smooth',block:'start'})},60);
const D=S.date,dayAll=d.appts.filter(a=>a.date===D).sort((a,b)=>a.time.localeCompare(b.time)||a.id-b.id);
const day=dayAll.filter(a=>(S.fs==='all'||String(a.staff)===S.fs)&&(S.fst==='all'||stKey(a)===S.fst));
const conf=dayAll.filter(a=>overlap(d,a).length>0);
const gm={};day.forEach(a=>{(gm[a.time]=gm[a.time]||[]).push(a)});
const groups=Object.keys(gm).sort().map(t=>({t:t.replace(':','.')+' น.',pickT:()=>set({ft:t}),rows:gm[t].map(a=>{const z=stOf(a);return{cust:cName(d,a.cust),pickT:null,key:e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();set({sel:a.id,payOpen:false,rt:'detail'})}},sub:'ช่าง '+sName(d,a.staff)+' · '+a.items.map(i=>i.name).join(' + ')+(overlap(d,a).length?' · ⚠ คิวซ้อน':''),st:z[0],sc:z[1],on:S.sel===a.id?'on':'',pick:()=>{set({sel:a.id,payOpen:false,rt:'detail'})},staff:sName(d,a.staff),sv:a.items.map(i=>i.name).join(', ')+(overlap(d,a).length?' · ⚠ คิวซ้อน':''),bc:a.status==='canceled'||a.status==='noshow'||(a.status==='done'&&a.paid)?'sxgr':'',pc:a.status==='canceled'||a.status==='noshow'?'sxcx':a.status==='done'&&a.paid?'sxpd':'',ckc:a.paid&&a.status==='done'?'sxy':'',ckm:a.paid&&a.status==='done'?'✓':'',ckl:a.paid&&a.status==='done'?'ชำระเงินแล้ว':'ยังไม่ชำระเงิน'}})}));
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
const hh0=d.shop.hours,okh=hh0&&hrsOk(d),lo=okh?tmin(hh0.open):540,hi=okh?tmin(hh0.close):1080,tstr=m=>p2(Math.floor(m/60))+':'+p2(m%60);
const slotSet=new Set();for(let m=lo;m<hi;m+=30)slotSet.add(tstr(m));dayAll.filter(x=>x.status!=='canceled').forEach(x=>slotSet.add(x.time));
const slots=[...slotSet].sort();let ft=S.ft&&slots.includes(S.ft)?S.ft:(a&&slots.includes(a.time)?a.time:(()=>{const f=dayAll.find(x=>x.status!=='canceled');if(f)return f.time;if(D===T){const nw=tmin(NOWT());const c=slots.find(x=>tmin(x)+30>nw);if(c)return c}return slots[0]||''})());
const ftm=ft?tmin(ft):0;
const fstaff=d.staff.map(z=>{const off=ftm<tmin(z.ws||'09:00')||ftm>=tmin(z.we||'18:00'),bz=off?null:dayAll.find(x=>x.staff===z.id&&x.status!=='canceled'&&x.status!=='noshow'&&tmin(x.time)<ftm+30&&ftm<tmin(x.time)+Math.max(dur(x),1)),mk=(z.skills||[]).filter(k=>k.main).map(k=>k.n);
return{n:z.name,sk:mk.length?mk.join(', '):(z.role||'ช่างเล็บ'),cls:bz?'':off?'sxoff':'sxok',hasBt:!!bz,noBt:!bz,bt:bz?'ติดคิว'+cName(d,bz.cust):'',go:bz?(()=>{set({sel:bz.id,payOpen:false,rt:'detail'})}):(()=>{}),fl:off?'นอกเวลางาน':'ว่าง'}});
const nFree=fstaff.filter(x=>x.cls==='sxok').length;
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
if(!F.cust)return set({fe:'กรุณาเลือกลูกค้า'});if(isNew&&!(F.newName||'').trim())return set({fe:'กรุณากรอกชื่อลูกค้าใหม่'});if(!F.staff)return set({fe:'กรุณาเลือกช่าง'});if(!F.date||!F.time)return set({fe:'กรุณาเลือกวันและเวลา'});if(!svs.length)return set({fe:'กรุณาเลือกบริการอย่างน้อย 1 อย่าง'});const hh=d.shop.hours;if(hh&&hrsOk(d)){const wd=pd(F.date).getDay();if(!hh.days.includes(wd))return set({fe:'ร้านปิดทำการวัน'+DAYN[wd]+' · วันทำการ: '+hoursTxt(d)});const st0=tmin(F.time),en0=st0+dur(tmp);if(st0<tmin(hh.open)||en0>tmin(hh.close))return set({fe:'อยู่นอกเวลาทำการ ('+hh.open+'–'+hh.close+')'+(st0>=tmin(hh.open)?' บริการนี้จะเสร็จเวลา '+p2(Math.floor(en0/60))+':'+p2(en0%60):' กรุณาเลือกเวลาในช่วงเปิดร้าน')})}
if(isFull(d,F.date,F.id||-1))return set({fe:(F.date===T?'คิววันนี้':'คิววันที่ '+thS(F.date))+'เต็มแล้ว ('+capOf(d)+' คิว) กรุณาเลือกวันหรือเวลาอื่น'});
let sid;M(x=>{let cid=+F.cust;if(isNew){cid=x.seq++;const ph=(F.newPhone||'').trim();x.customers.push({id:cid,name:F.newName.trim(),nick:'',phone:ph,bd:'',line:'',tier:'',since:'',created:TODAY(),notes:[]})}
const c=getC(x,cid),tr=tierO(x,c),v={cust:cid,staff:+F.staff,date:F.date,time:F.time,items:svs,note:(F.note||'').trim(),disc:tr?tr.disc:0,tier:tr?tr.n:''};
if(F.id){Object.assign(x.appts.find(w=>w.id===F.id),v);sid=F.id}else{const same=x.appts.filter(w=>w.date===F.date).map(w=>+(w.no||'').split('-')[2]||0),no='INV-'+F.date.replace(/-/g,'')+'-'+p2(Math.max(0,...same)+1).padStart(3,'0');sid=x.seq++;x.appts.push(Object.assign({id:sid,no,status:'booked',paid:false,method:'',tip:0,cp:false,created:TODAY()},v))}});
set({form:null,fe:'',date:F.date,sel:sid,rt:'detail',fs:'all',fst:'all'});toast(F.id?'บันทึกการแก้ไขแล้ว':'สร้างนัดหมายแล้ว')},
del:F.id?(()=>{if(!S.cdel)return set({cdel:true});M(x=>{x.appts=x.appts.filter(w=>w.id!==F.id)});set({form:null,cdel:false,sel:null});toast('ลบนัดหมายแล้ว')}):null,delTxt:'ลบนัดหมาย'}}
const nDay=dayAll.filter(x=>x.status!=='canceled').length,anyA=d.appts.length>0,m0=missing(d);
return{today:thL(T),noStore:!OKS,openShop:()=>openShopForm(this),
heroWho:D===T?'วันนี้':thS(D),nDay,heroSub:conf.length?'คิวซ้อน '+conf.length+' รายการ ควรตรวจสอบก่อนเริ่มงาน':anyA?(nDay?'ไม่มีคิวซ้อน':'ยังไม่มีนัดหมายในวันนี้'):'เริ่มต้นด้วยการสร้างนัดหมายแรก',heroBtn:conf.length?'ดูคิวซ้อน':anyA?'+ สร้างนัดหมาย':'สร้างนัดหมายแรก',heroGo:()=>{if(conf.length){set({fs:'all',fst:'all'});const e=document.getElementById('list');e&&e.scrollIntoView&&e.scrollIntoView({behavior:'smooth'})}else set({form:mkAppt(D),fe:''})},
add:()=>set({form:mkAppt(D),fe:'',cdel:false}),hasAny:anyA,noAny:!anyA,hasMiss:m0.length>0,miss:m0,
dateTxt:thL(D),dateShort:D===T?'วันนี้ · '+thS(D):thS(D)+' '+(pd(D).getFullYear()+543),prev:()=>set({date:iso(new Date(dt.getFullYear(),dt.getMonth(),dt.getDate()-1)),sel:null}),next:()=>set({date:iso(new Date(dt.getFullYear(),dt.getMonth(),dt.getDate()+1)),sel:null}),goToday:()=>set({date:T,sel:null}),
fs:S.fs,onFs:e=>set({fs:e.target.value}),fsOpts:[{v:'all',t:'ทุกพนักงาน'}].concat(d.staff.map(s=>({v:String(s.id),t:s.name}))),fst:S.fst,onFst:e=>set({fst:e.target.value}),fstOpts:ST_OPTS.map(o=>({v:o[0],t:o[1]})),
hasConf:conf.length>0,confTxt:'คิวซ้อน '+conf.length+' รายการ: '+conf.map(x=>sName(d,x.staff)+' '+x.time+' ('+cName(d,x.cust)+')').join(', '),
menuOpen:!!S.menu,toggleMenu:this.toggleMenu,openCap:()=>openCapForm(this),hasUt:ut.length>0&&dayAll.length>0,ut,week,groups,noDay:day.length===0,hasSel:!!a,noSel:!a,isDet:!!a&&!S.form,hasStaff:true,closeDet:()=>set({sel:null,payOpen:false}),stopP:e=>e.stopPropagation(),ft,onFt:e=>set({ft:e.target.value}),ftOpts:slots.map(x=>({v:x,t:x.replace(':','.')+' น.'})),fstaff,noStaff:d.staff.length===0,ftSum:ft?(d.staff.length?'เวลา '+ft.replace(':','.')+' น. · ช่างว่าง '+nFree+' จาก '+d.staff.length+' คน':''):'',sel,png,busy:!!S.busy,
payM:S.payM,onPayM:e=>set({payM:e.target.value}),payOpts:PAYM.map(x=>({v:x,t:x})),payTip:S.payTip,onPayTip:e=>set({payTip:e.target.value}),
fm:modalOf(this,S,mo),toast:S.to,toastText:S.to}}}
"""

html = page('Solva – ตารางนัด', helmet_css('Schedule.dc.html') + css_extra, body, js)
write('Schedule.dc.html', html)
