# -*- coding: utf-8 -*-
from core import *

EMPTYMINI = lambda msg: '<div class="em">' + HEART + '<div>' + msg + '</div></div>'
PERSON = '<svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="8" r="3.5"></circle><path d="M5 20c1-4 4-5.5 7-5.5s6 1.5 7 5.5"></path></svg>'

body = ('<div class="app">' + nav('Staff') + '<main class="mn">' + header() +
 hero(hero_svg('Staff.dc.html'),
      'ทีมของเรา <b class="cn" style="--v:{{nAll}}"></b> คน', '{{heroSub}}',
      '<button class="bt" onClick="{{add}}">{{heroBtn}}</button>') + WARN +
 '<sc-if value="{{noAny}}" hint-placeholder-val="{{false}}"><div class="empty">' + HEART +
 '<h2>ยังไม่มีพนักงาน</h2><p>เพิ่มพนักงานเพื่อรับนัดหมาย บันทึกเวลาเข้างาน และคำนวณค่าคอมมิชชันและทิปจากงานที่ทำจริง</p></div></sc-if>'
 '<sc-if value="{{hasAny}}" hint-placeholder-val="{{true}}"><div id="list" class="row"><input class="si" placeholder="ค้นหาชื่อพนักงาน" aria-label="ค้นหาพนักงาน" value="{{q}}" onInput="{{onQ}}">'
 '<div class="sg"><sc-for list="{{fil}}" as="f" hint-placeholder-count="4"><button class="{{f.on}}" onClick="{{f.pick}}">{{f.name}}</button></sc-for></div></div>'
 '<div class="lay"><div class="l1"><div class="sg2"><sc-for list="{{rows}}" as="s" hint-placeholder-count="3"><div class="c lf pf sc2 {{s.on}}"><div class="pa"><div>' + PERSON + '</div></div>'
 '<button class="ch nb" style="padding:6px 30px" onClick="{{s.pick}}">{{s.name}}</button><div class="sp">{{s.ski}}</div><span class="ch {{s.sb}}">{{s.sl}}</span><div class="ap" style="margin-top:12px">{{s.role}} · {{s.hrs}} ชม./เดือน</div></div></sc-for></div>'
 '<sc-if value="{{noRows}}" hint-placeholder-val="{{false}}">' + EMPTYMINI('ไม่มีพนักงานในสถานะนี้ตอนนี้<br><button class="bt o" style="margin-top:12px" onClick="{{clear}}">ดูทั้งหมด</button>') + '</sc-if></div>'
 '<div class="c l2"><sc-if value="{{noSel}}" hint-placeholder-val="{{false}}">' + EMPTYMINI('เลือกพนักงานเพื่อดูโปรไฟล์') + '</sc-if>'
 '<sc-if value="{{hasSel}}" hint-placeholder-val="{{true}}"><div class="row" style="margin:0"><div class="av2" style="width:64px;height:64px;background:#FFDFFF"><svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#2B2D3A" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="8" r="3.5"></circle><path d="M5 20c1-4 4-5.5 7-5.5s6 1.5 7 5.5"></path></svg></div>'
 '<div><h2 style="margin:0">{{sel.name}}</h2><div style="color:#6B6D7A">{{sel.role}} · อายุงาน {{sel.ten}}</div><span class="ch {{sel.sb}}">{{sel.sl}}</span></div></div>'
 '<div class="tl" style="grid-template-columns:repeat(3,1fr);margin-top:14px"><sc-for list="{{sel.sum}}" as="x"><div><small>{{x.k}}</small><b style="font-size:17px">{{x.v}}</b></div></sc-for></div>'
 '<div class="tabs"><sc-for list="{{tabs}}" as="t" hint-placeholder-count="6"><button class="{{t.on}}" onClick="{{t.pick}}">{{t.name}}</button></sc-for></div>'
 # 0 basic
 '<sc-if value="{{t0}}"><div class="tp"><sc-for list="{{sel.kv}}" as="x"><div class="kv"><span>{{x.k}}</span><b>{{x.v}}</b></div></sc-for>'
 '<div class="row" style="margin:14px 0 0"><button class="bt o" onClick="{{sel.edit}}">แก้ไขข้อมูล</button><button class="bt d" onClick="{{sel.del}}">{{sel.delTxt}}</button></div></div></sc-if>'
 # 1 hours
 '<sc-if value="{{t1}}"><div class="tp"><div class="mo"><button aria-label="เดือนก่อนหน้า" onClick="{{prev}}">‹</button><b>{{moTxt}}</b><button aria-label="เดือนถัดไป" onClick="{{next}}">›</button></div>'
 '<sc-if value="{{sel.hasHrs}}"><div class="wb"><sc-for list="{{sel.bars}}" as="b"><div><i style="height:{{b.h}}px"></i>{{b.l}}</div></sc-for></div></sc-if>'
 '<sc-if value="{{sel.noHrs}}">' + EMPTYMINI('ยังไม่มีเวลาเข้างานในเดือนนี้<br>บันทึกเวลาได้ที่แท็บ “การเข้างาน”') + '</sc-if>'
 '<div class="kv"><span>ชั่วโมงรวม</span><b>{{sel.hrs}}</b></div><div class="kv"><span>จำนวนวันทำงาน</span><b>{{sel.days}}</b></div><div class="kv"><span>เฉลี่ย</span><b>{{sel.avg}}</b></div><div class="kv"><span>เวลาทำงานตามตาราง</span><b>{{sel.sched}}</b></div></div></sc-if>'
 # 2 skills
 '<sc-if value="{{t2}}"><div class="tp"><sc-if value="{{sel.hasSk}}"><p style="margin:0 0 10px;color:#6B6D7A">แตะทักษะเพื่อสลับระหว่างหลักและรอง</p><div class="row"><sc-for list="{{sel.sk}}" as="k"><span class="rg2"><button class="ch {{k.cls}}" style="cursor:pointer;min-height:44px;font:inherit" onClick="{{k.pick}}">{{k.t}} · {{k.tag}}</button><button class="ch nt" style="cursor:pointer;min-height:44px;font:inherit" aria-label="ลบทักษะ" onClick="{{k.rm}}">×</button></span></sc-for></div></sc-if>'
 '<sc-if value="{{sel.noSk}}">' + EMPTYMINI('ยังไม่ได้ระบุความถนัด เพิ่มทักษะของพนักงานด้านล่าง') + '</sc-if>'
 '<div class="ni"><input list="svl" placeholder="เพิ่มทักษะ เช่น ต่อเล็บ" aria-label="ทักษะใหม่" value="{{skIn}}" onInput="{{onSk}}"><datalist id="svl"><sc-for list="{{svNames}}" as="o"><option value="{{o.v}}"></option></sc-for></datalist><button class="bt" onClick="{{addSk}}">เพิ่ม</button></div></div></sc-if>'
 # 3 attendance
 '<sc-if value="{{t3}}"><div class="tp"><div class="row" style="margin:0 0 10px"><button class="bt" onClick="{{sel.cin}}">เช็คอินตอนนี้</button><button class="bt o" onClick="{{sel.cout}}">เช็คเอาท์ตอนนี้</button><button class="bt d" onClick="{{sel.lv}}">ลาวันนี้</button><button class="bt d" onClick="{{sel.ab}}">ขาดวันนี้</button></div>'
 '<div class="mut" style="margin-bottom:10px">วันนี้: {{sel.todayTxt}}</div>'
 '<div class="sg" style="margin-bottom:10px"><sc-for list="{{sel.af}}" as="a"><button class="{{a.on}}" onClick="{{a.pick}}">{{a.name}}</button></sc-for></div>'
 '<sc-for list="{{sel.att}}" as="a"><div class="kv"><span><b style="color:#2B2D3A">{{a.date}}</b> · {{a.io}} · {{a.hrs}}</span><span><span class="ch {{a.sc}}">{{a.sl}}</span> <button class="ch nt" style="cursor:pointer;font:inherit" aria-label="ลบรายการ" onClick="{{a.rm}}">×</button></span></div></sc-for>'
 '<sc-if value="{{sel.noAtt}}">' + EMPTYMINI('ยังไม่มีบันทึกการเข้างาน กด “เช็คอินตอนนี้” เพื่อเริ่มบันทึก') + '</sc-if></div></sc-if>'
 # 4 commission
 '<sc-if value="{{t4}}"><div class="tp"><div class="mo"><button aria-label="เดือนก่อนหน้า" onClick="{{prev}}">‹</button><b>{{moTxt}}</b><button aria-label="เดือนถัดไป" onClick="{{next}}">›</button></div>'
 '<sc-if value="{{sel.noRate}}"><div class="em"><h2>ยังไม่ได้ตั้งค่าคอมมิชชัน</h2><p>กรอกอัตราค่าคอมมิชชันของพนักงานคนนี้ (เป็น % ของยอดบริการหลังหักส่วนลด) ตามนโยบายของร้าน</p>'
 '<div class="ni" style="justify-content:center"><input inputmode="decimal" style="max-width:140px;flex:none" placeholder="เช่น 20" aria-label="อัตราคอมมิชชัน (%)" value="{{rateIn}}" onInput="{{onRate}}"><button class="bt" onClick="{{saveRate}}">บันทึกอัตรา</button></div></div></sc-if>'
 '<sc-if value="{{sel.hasRate}}"><div class="tl"><sc-for list="{{sel.cs}}" as="x"><div><small>{{x.k}}</small><b>{{x.v}}</b></div></sc-for></div>'
 '<div class="row" style="margin:0 0 12px"><sc-if value="{{sel.hasPend}}"><button class="bt" onClick="{{sel.payAll}}">{{sel.payTxt}}</button></sc-if><button class="bt o" disabled="{{busy}}" onClick="{{sel.png}}">{{sel.pngTxt}}</button></div>'
 '<div class="mut" style="margin-bottom:6px">อัตราค่าคอมมิชชัน {{sel.rateTxt}}</div>'
 '<sc-for list="{{sel.hl}}" as="h"><div class="hi2"><button onClick="{{h.toggle}}"><span><b>{{h.date}}</b> · {{h.cust}} · {{h.svc}}</span><span><span class="ch {{h.pc}}">{{h.ps}}</span> {{h.ar}}</span></button><sc-if value="{{h.isOpen}}"><div class="dd">{{h.calc}}</div></sc-if></div></sc-for>'
 '<sc-if value="{{sel.noCom}}">' + EMPTYMINI('ยังไม่มีรายการที่ชำระเงินแล้วในเดือนนี้ ค่าคอมและทิปจะแสดงเมื่อรับชำระนัดหมาย') + '</sc-if></sc-if></div></sc-if>'
 # 5 history
 '<sc-if value="{{t5}}"><div class="tp"><sc-for list="{{sel.wh}}" as="h"><div class="hi2"><button onClick="{{h.toggle}}"><span><b>{{h.date}}</b> · {{h.cust}} · {{h.svc}}</span><span><span class="ch {{h.sc}}">{{h.st}}</span> {{h.ar}}</span></button><sc-if value="{{h.isOpen}}"><div class="dd">{{h.dur}} · {{h.price}} · ค่าคอม {{h.cm}}</div></sc-if></div></sc-for>'
 '<sc-if value="{{sel.noWh}}">' + EMPTYMINI('ยังไม่มีประวัติงาน') + '</sc-if></div></sc-if>'
 '</sc-if></div></div></sc-if>' + MODAL + '</main></div>')

js = png_js() + r"""
const TB=['ข้อมูลพื้นฐาน','ชั่วโมงทำงาน','ความถนัด','การเข้างาน','ค่าคอมฯ & ทิป','ประวัติงาน'],FL=[['all','ทั้งหมด'],['ontime','ตรงเวลา'],['late','มาสาย'],['leave','ลา']];
const mkStaff=()=>({_k:'staff',name:'',full:'',role:'ช่างเล็บ',phone:'',start:'',rate:'',ws:'09:00',we:'18:00'});
const hrsOf=r=>r&&r.type==='work'&&r.in&&r.out?Math.max(0,(tmin(r.out)-tmin(r.in))/60):0,h1=n=>(Math.round(n*10)/10)+' ชม.';
function billCom(d,s,k,L,tot,paid,pend){const rt=+s.rate,CP=['#CDEFD9','#1F7A4D'],CW=['#FBE8A6','#8A6500'],rg=mRange(k),last=k===mkey(TODAY())?TODAY():rg[1],a=pd(rg[0]),b=pd(last);
const rows=L.map(x=>[thS(x.date),x.cust+' · '+x.svc,fm(x.v),rt+'%',fm(x.cm),{t:x.p?'Paid':'Pending',chip:x.p?CP:CW}]);
return{w:760,shop:d.shop.name||'Solva',title:'รายงานค่าคอมมิชชันและทิป',info:[['พนักงาน',(s.full?s.full+' ('+s.name+')':s.name)],['ตำแหน่ง',s.role||'—'],['ช่วงรายงาน',a.getDate()+' – '+b.getDate()+' '+TH_M[b.getMonth()]+' '+(b.getFullYear()+543)],['วันที่จัดทำรายงาน',thD(TODAY())]],cols:[{w:.12,al:'l'},{w:.36,al:'l'},{w:.15,al:'r'},{w:.1,al:'r'},{w:.15,al:'r'},{w:.12,al:'c'}],head:['วันที่','รายการบริการ','มูลค่า','อัตรา','ค่าคอม','สถานะ'],rows,sum:[{k:'ค่าคอมมิชชันรวม',v:fm(tot[0])},{k:'ทิปรวม',v:fm(tot[1])},{k:'ยอดรวมค่าตอบแทนทั้งหมด',v:fm(tot[0]+tot[1]),big:1}],pay:[['จ่ายแล้ว (Paid)',fm(paid),CP],['รอจ่าย (Pending)',fm(pend),CW]],notes:['คิดจากงานที่ลูกค้าชำระเงินแล้วเท่านั้น','อัตราค่าคอมมิชชันของ'+s.name+' '+rt+'% ของยอดบริการหลังหักส่วนลด'],foot:['จัดทำโดยระบบ Solva']}}
class Component extends Base{
async share(spec,fn){this.setState({busy:true});try{await savePng(spec,fn);this.toast('บันทึกรูปเรียบร้อย ✓')}catch(e){this.toast(e&&e.code==='declined'?'ยกเลิกการบันทึก':e&&e.code==='unavailable'?'มุมมองนี้ยังบันทึกไฟล์ไม่ได้ ลองเปิดจากลิงก์ที่แชร์':'สร้างรูปไม่สำเร็จ กรุณาลองอีกครั้ง',2800)}this.setState({busy:false})}
boot(){const u=uiGet();if(u.open==='staff'){uiSet({open:''});this.setState({form:mkStaff(),fe:''})}}
renderVals(){
const d=load(),S=Object.assign({f:'all',q:'',sel:null,tab:0,mo:0,af:'all',op:null,skIn:'',rateIn:'',form:null,fe:'',cdel:false,busy:false,to:''},this.state),set=o=>this.setState(o);
const T=TODAY(),toast=m=>this.toast(m),k=mAdd(mkey(T),S.mo),inM=x=>mkey(x)===k;
const today=s=>attSt(s,attOf(d,s.id,T));
const monthH=s=>sum(d.att.filter(r=>r.staff===s.id&&inM(r.date)),hrsOf);
const q=S.q.trim();
const rows=d.staff.filter(s=>(S.f==='all'||today(s)===S.f)&&(!q||s.name.includes(q)||(s.full||'').includes(q))).map(s=>{const a=today(s),sk=(s.skills||[]).filter(x=>x.main).map(x=>x.n);return{name:s.name,role:s.role||'ช่างเล็บ',ski:sk.length?sk.join(' · '):'ยังไม่ระบุความถนัด',sb:a?ATL[a][1]:'nt',sl:a?ATL[a][0]:'ยังไม่เช็คอิน',hrs:Math.round(monthH(s)*10)/10,on:S.sel===s.id?'on':'',pick:()=>set({sel:s.id,tab:0,op:null,af:'all',cdel:false})}});
const fil=FL.map(([x,n])=>({name:n,on:S.f===x?'on':'',pick:()=>set({f:x})}));
const tabs=TB.map((n,i)=>({name:n,on:S.tab===i?'on':'',pick:()=>set({tab:i,op:null})}));
const s=getS(d,S.sel);let sel={};
if(s){const a=today(s),hasRate=s.rate!=null&&s.rate!=='',mine=d.appts.filter(x=>x.staff===s.id);
const recs=d.att.filter(r=>r.staff===s.id).sort((x,y)=>y.date.localeCompare(x.date));
const mrec=recs.filter(r=>inM(r.date)&&r.type==='work'&&r.out),totH=sum(mrec,hrsOf),dys=mrec.length,wk=[0,0,0,0,0];mrec.forEach(r=>{wk[Math.min(4,Math.floor((+r.date.slice(8)-1)/7))]+=hrsOf(r)});const mxw=Math.max(1,...wk);
const L=mine.filter(x=>isRev(x)&&inM(x.paidDate||x.date)).sort((x,y)=>(x.paidDate||x.date).localeCompare(y.paidDate||y.date)).map(x=>({id:x.id,date:x.paidDate||x.date,cust:cName(d,x.cust),svc:x.items.map(i=>i.name).join(' + '),v:net(x),cm:commOf(x,s),tip:x.tip||0,p:!!x.cp}));
const tC=sum(L,x=>x.cm),tT=sum(L,x=>x.tip),pdn=sum(L.filter(x=>x.p),x=>x.cm+x.tip),pend=sum(L.filter(x=>!x.p),x=>x.cm+x.tip);
const af=recs.filter(r=>S.af==='all'||attSt(s,r)===S.af),cnt=z=>recs.filter(r=>attSt(s,r)===z).length;
const skills=s.skills||[];
sel={name:s.name,role:s.role||'ช่างเล็บ',sb:a?ATL[a][1]:'nt',sl:a?ATL[a][0]:'ยังไม่เช็คอิน',ten:ten(s.start),
sum:[{k:'ชั่วโมง ('+mShort(k)+')',v:h1(totH)},{k:'ค่าคอมมิชชัน',v:hasRate?fm(tC):'ยังไม่ตั้งค่า'},{k:'ทิป',v:fm(tT)}],
kv:[{k:'ชื่อ-นามสกุล',v:s.full||'—'},{k:'ตำแหน่ง',v:s.role||'—'},{k:'เบอร์ติดต่อ',v:s.phone||'—'},{k:'วันที่เริ่มงาน',v:thD(s.start)},{k:'อายุงาน (คำนวณอัตโนมัติ)',v:ten(s.start)},{k:'อัตราค่าคอมมิชชัน',v:hasRate?s.rate+'%':'ยังไม่ได้ตั้งค่า'}],
edit:()=>set({form:{_k:'staff',id:s.id,name:s.name,full:s.full||'',role:s.role||'',phone:s.phone||'',start:s.start||'',rate:hasRate?s.rate:'',ws:s.ws||'09:00',we:s.we||'18:00'},fe:''}),
delTxt:S.cdel?'กดอีกครั้งเพื่อยืนยันลบ':'ลบพนักงาน',del:()=>{if(mine.length)return toast('ลบไม่ได้ เพราะพนักงานมีนัดหมายอยู่ในระบบ');if(!S.cdel)return set({cdel:true});M(x=>{x.staff=x.staff.filter(z=>z.id!==s.id);x.att=x.att.filter(z=>z.staff!==s.id)});set({sel:null,cdel:false});toast('ลบพนักงานแล้ว')},
hasHrs:dys>0,noHrs:dys===0,hrs:h1(totH),days:dys+' วัน',avg:dys?h1(totH/dys)+'/วัน':'—',sched:(s.ws||'09:00')+' – '+(s.we||'18:00'),
bars:wk.map((v,i)=>({h:Math.round(v/mxw*90)+6,l:'สป.'+(i+1)})),
sk:skills.map((x,i)=>({t:x.n,cls:x.main?'':'nt',tag:x.main?'หลัก':'รอง',pick:()=>{M(y=>{const z=getS(y,s.id).skills[i];z.main=!z.main});toast('ปรับทักษะเรียบร้อย')},rm:()=>{M(y=>{getS(y,s.id).skills.splice(i,1)});toast('ลบทักษะแล้ว')}})),hasSk:skills.length>0,noSk:skills.length===0,
cin:()=>{if(attOf(d,s.id,T))return toast('วันนี้มีบันทึกของ '+s.name+' แล้ว');M(y=>{y.att.push({id:y.seq++,staff:s.id,date:T,type:'work',in:NOWT(),out:''})});toast('เช็คอิน '+NOWT()+' น.')},
cout:()=>{const r=attOf(d,s.id,T);if(!r||r.type!=='work')return toast('ยังไม่ได้เช็คอินวันนี้');if(r.out)return toast('เช็คเอาท์ไปแล้ว');M(y=>{attOf(y,s.id,T).out=NOWT()});toast('เช็คเอาท์ '+NOWT()+' น.')},
lv:()=>{if(attOf(d,s.id,T))return toast('วันนี้มีบันทึกแล้ว ลบรายการก่อนหากต้องการเปลี่ยน');M(y=>{y.att.push({id:y.seq++,staff:s.id,date:T,type:'leave'})});toast('บันทึกวันลาแล้ว')},
ab:()=>{if(attOf(d,s.id,T))return toast('วันนี้มีบันทึกแล้ว ลบรายการก่อนหากต้องการเปลี่ยน');M(y=>{y.att.push({id:y.seq++,staff:s.id,date:T,type:'absent'})});toast('บันทึกขาดงานแล้ว')},
todayTxt:a?ATL[a][0]+(attOf(d,s.id,T).in?' · เข้า '+attOf(d,s.id,T).in+(attOf(d,s.id,T).out?' ออก '+attOf(d,s.id,T).out:' (ยังไม่เช็คเอาท์)'):''):'ยังไม่มีบันทึก (เวลาเข้างานตามตาราง '+(s.ws||'09:00')+' น.)',
af:FL.concat([['absent','ขาด']]).map(([x,n])=>({name:n+(x==='all'?'':' '+cnt(x)),on:S.af===x?'on':'',pick:()=>set({af:x})})),
att:af.slice(0,40).map(r=>{const z=attSt(s,r);return{date:thS(r.date),io:r.type==='work'?r.in+' – '+(r.out||'ยังไม่เช็คเอาท์'):'—',hrs:r.type==='work'?h1(hrsOf(r)):'—',sl:ATL[z][0],sc:ATL[z][1],rm:()=>{M(y=>{y.att=y.att.filter(w=>w.id!==r.id)});toast('ลบรายการแล้ว')}}}),noAtt:af.length===0,
hasRate:hasRate,noRate:!hasRate,rateTxt:hasRate?s.rate+'% ของยอดบริการหลังหักส่วนลด':'—',
cs:[{k:'ค่าคอมรวม',v:fm(tC)},{k:'ทิปรวม',v:fm(tT)},{k:'จ่ายแล้ว',v:fm(pdn)},{k:'รอจ่าย',v:fm(pend)}],hasPend:pend>0,payTxt:'จ่ายยอดค้าง '+fm(pend),
payAll:()=>{M(y=>{y.appts.forEach(z=>{if(L.some(l=>l.id===z.id))z.cp=true})});toast('บันทึกการจ่ายเรียบร้อย')},
hl:L.map((x,i)=>({date:thS(x.date),cust:x.cust,svc:x.svc,ps:x.p?'จ่ายแล้ว':'รอจ่าย',pc:x.p?'s1':'s2',calc:fm(x.v)+' × '+s.rate+'% = '+fm(x.cm)+' · ทิป '+fm(x.tip)+' → รวม '+fm(x.cm+x.tip),isOpen:S.op===i,ar:S.op===i?'▲':'▼',toggle:()=>set({op:S.op===i?null:i})})),noCom:L.length===0,
png:()=>{if(!L.length)return toast('ยังไม่มีรายการในเดือนนี้ให้สร้างรายงาน');this.share(billCom(d,s,k,L,[tC,tT],pdn,pend),'solva-commission-'+s.name+'-'+k+'.png')},pngTxt:S.busy?'กำลังสร้างรูป…':'Share as PNG',
wh:mine.slice().sort((x,y)=>(y.date+y.time).localeCompare(x.date+x.time)).map((x,i)=>{const z=stOf(x);return{date:thS(x.date),cust:cName(d,x.cust),svc:x.items.map(w=>w.name).join(' + '),st:z[0],sc:z[1],dur:dur(x)?dur(x)+' นาที':'ไม่ระบุเวลา',price:fm(net(x)),cm:hasRate?fm(commOf(x,s)):'ยังไม่ตั้งค่า',isOpen:S.op===i,ar:S.op===i?'▲':'▼',toggle:()=>set({op:S.op===i?null:i})}}),noWh:mine.length===0}}
const F=S.form,fk=F&&F._k;let mo={};
if(fk==='shop')mo=shopMo(this,F,S);
if(fk==='staff')mo={title:F.id?'แก้ไขข้อมูลพนักงาน':'เพิ่มพนักงาน',hint:F.id?'':'อัตราค่าคอมมิชชันตั้งทีหลังได้ที่แท็บ “ค่าคอมฯ & ทิป”',spec:[{k:'name',label:'ชื่อที่ใช้เรียก',ph:'เช่น พี่นุช'},{k:'full',label:'ชื่อ-นามสกุล (ไม่บังคับ)'},{k:'role',label:'ตำแหน่ง',ph:'เช่น ช่างเล็บ'},{k:'phone',label:'เบอร์ติดต่อ (ไม่บังคับ)',type:'tel'},{k:'start',label:'วันที่เริ่มงาน',type:'date'},{k:'rate',label:'ค่าคอมมิชชัน (%) ไม่บังคับ',type:'number',ph:'เช่น 20'},{k:'ws',label:'เวลาเริ่มงาน',type:'time'},{k:'we',label:'เวลาเลิกงาน',type:'time'}],saveTxt:F.id?'บันทึกการแก้ไข':'เพิ่มพนักงาน',
save:()=>{const name=(F.name||'').trim();if(!name)return set({fe:'กรุณากรอกชื่อพนักงาน'});const rate=F.rate===''||F.rate==null?null:+F.rate;if(rate!==null&&(isNaN(rate)||rate<0||rate>100))return set({fe:'ค่าคอมมิชชันต้องอยู่ระหว่าง 0–100%'});
if(d.staff.some(z=>z.name===name&&z.id!==F.id))return set({fe:'มีพนักงานชื่อนี้อยู่แล้ว ลองเพิ่มคำต่อท้ายให้ต่างกัน'});
let nid=F.id;M(x=>{const v={name,full:(F.full||'').trim(),role:(F.role||'').trim(),phone:(F.phone||'').trim(),start:F.start||'',rate,ws:F.ws||'09:00',we:F.we||'18:00'};if(F.id)Object.assign(getS(x,F.id),v);else{nid=x.seq++;x.staff.push(Object.assign({id:nid,skills:[],created:T},v))}});
set({form:null,fe:'',sel:nid,tab:0,f:'all',q:''});toast(F.id?'บันทึกการแก้ไขแล้ว':'เพิ่มพนักงานแล้ว')}};
const n=d.staff.length,po=d.staff.filter(z=>today(z)==='ontime').length,pl=d.staff.filter(z=>today(z)==='late').length,nc=d.staff.filter(z=>!attOf(d,z.id,T)).length;
return{today:thL(T),noStore:!OKS,openShop:()=>openShopForm(this),nAll:n,
heroSub:n?(po+pl+d.staff.filter(z=>['leave','absent'].includes(today(z))).length?'ตรงเวลา '+po+' · มาสาย '+pl+(nc?' · ยังไม่เช็คอิน '+nc:''):'วันนี้ยังไม่มีการบันทึกเวลาเข้างาน'):'เริ่มต้นด้วยการเพิ่มพนักงานคนแรกของร้าน',heroBtn:n?'+ เพิ่มพนักงาน':'เพิ่มพนักงานคนแรก',
add:()=>set({form:mkStaff(),fe:''}),q:S.q,onQ:e=>set({q:e.target.value}),clear:()=>set({f:'all',q:''}),rows,fil,tabs,sel,hasAny:n>0,noAny:n===0,noRows:n>0&&rows.length===0,hasSel:!!s,noSel:!s,
t0:S.tab===0,t1:S.tab===1,t2:S.tab===2,t3:S.tab===3,t4:S.tab===4,t5:S.tab===5,moTxt:mTxt(k),prev:()=>set({mo:S.mo-1,op:null}),next:()=>{if(S.mo<0)set({mo:S.mo+1,op:null})},
skIn:S.skIn,onSk:e=>set({skIn:e.target.value}),svNames:d.services.map(z=>({v:z.name})),
addSk:()=>{const v=S.skIn.trim();if(!v||!s)return;if((s.skills||[]).some(z=>z.n===v))return toast('มีทักษะนี้แล้ว');M(y=>{const z=getS(y,s.id);z.skills=(z.skills||[]).concat({n:v,main:true})});set({skIn:''});toast('เพิ่มทักษะแล้ว')},
rateIn:S.rateIn,onRate:e=>set({rateIn:e.target.value}),saveRate:()=>{const v=S.rateIn===''?NaN:+S.rateIn;if(isNaN(v)||v<0||v>100)return toast('กรุณากรอกอัตรา 0–100%');M(y=>{getS(y,s.id).rate=v});set({rateIn:''});toast('ตั้งค่าคอมมิชชัน '+v+'% แล้ว')},
busy:!!S.busy,fm:modalOf(this,S,mo),toast:S.to,toastText:S.to}}}
"""

html = page('Solva – พนักงาน', helmet_css('Staff.dc.html') + '.mb{height:auto;gap:0}', body, js)
html = html.replace('class="hi"', 'class="hi2"')
write('Staff.dc.html', html)
