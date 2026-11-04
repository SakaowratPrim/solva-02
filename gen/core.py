# -*- coding: utf-8 -*-
import re, os
LIVE = '/tmp/claude-0/-home-claude/9b09fc01-c23e-5d99-b82f-f46153f03eb3/scratchpad/live3/project/'
OUT = '/tmp/claude-0/-home-claude/9b09fc01-c23e-5d99-b82f-f46153f03eb3/scratchpad/out/project/'
os.makedirs(OUT, exist_ok=True)

def rd(f): return open(LIVE + f, encoding='utf-8').read()

def helmet_css(f):
    return re.search(r'<style>(.*?)</style></helmet>', rd(f), re.S).group(1)

def hero_svg(f):
    return re.search(r'<svg width="220" height="200".*?</svg>', rd(f), re.S).group(0)

FONT_LINK = '<link href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700&amp;family=Noto+Sans+Thai:wght@400;500;600;700&amp;family=Satisfy&amp;display=swap" rel="stylesheet">'

# ---------- CSS added on top of each page's original CSS (no .mb here: it clashes) ----------

RESP = r"""
.sb .lg{display:block;margin-bottom:8px}.lgi{display:block;width:64px;height:auto;margin:0 auto}
.hero>svg{flex:none;max-width:42%;height:auto}.dn svg{width:100%;height:auto}
@media(min-width:1700px){.app{max-width:1760px;margin:0 auto}}
@media(max-width:1100px){.mn{padding:24px 22px 120px 16px}.sb{margin-left:16px}.hero{padding:28px 32px}.hl{font-size:36px}.g2{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}
@media(max-width:820px){
.mn{padding:16px 16px calc(104px + env(safe-area-inset-bottom))}
.sb{bottom:calc(10px + env(safe-area-inset-bottom));left:10px;right:10px;border-radius:32px;height:64px;padding:4px 6px;align-items:center;gap:0}
.sb a{width:auto;flex:1;min-width:0;font-size:10px;padding:6px 0;gap:1px;border-radius:24px}.sb a svg{width:22px;height:22px}
.hd{margin-bottom:16px;gap:10px}.hd .hi0{font-size:20px}
.hero{flex-direction:row;align-items:center;gap:12px;padding:22px 20px;min-height:0;border-radius:28px;margin-bottom:18px}
.hero>svg{width:130px;max-width:38%;margin-right:-6px}.hero .tx{min-width:0;flex:1}
.hl{font-size:28px}.hs{font-size:14px;margin-bottom:14px}
.g{grid-template-columns:repeat(2,1fr);gap:12px}.g .c{padding:16px}.k{font-size:30px}.kl{font-size:14px}
.g2{grid-template-columns:1fr;gap:16px}.c{padding:18px;border-radius:24px}h1{font-size:20px}
.row{gap:10px}.row .bt{flex:1 1 140px}.si{max-width:none;min-width:0;flex:1 1 100%}
.hr:has(input){width:100%}.hr input{flex:1;width:auto;min-width:0}
.stp{width:100%;justify-content:space-between}.stp b{min-width:0;flex:1}
.dn{width:260px}.dn .big{font-size:34px}
.fab{right:14px;bottom:calc(88px + env(safe-area-inset-bottom));width:56px;height:56px}
.mb{height:200px;gap:8px}
.tk{overflow:hidden}.ov{padding:16px 12px}.md{padding:20px 18px;border-radius:24px}
.to{max-width:calc(100vw - 24px)}.sb .lg{display:none}
.ff input,.ff select,.ff textarea,.si,.hr input,.sel2{font-size:16px}
}
@media(min-width:700px) and (max-width:820px){.g2{grid-template-columns:1fr 1fr}}
@media(max-width:600px){
.hero{padding:20px 18px}.hero>svg{width:104px}.hl{font-size:24px}
.lgd{flex-wrap:wrap;gap:8px 14px}.tl{grid-template-columns:1fr 1fr}
.cal{gap:6px 0}.cal a.dy{width:36px;height:36px}.cal a.dy.f{width:40px;height:48px}
.wk{padding:10px 4px;gap:0}.wk button,.wk button.sl{min-width:0;flex:1;padding:8px 0}.wk button.sl{padding:12px 0 14px}.wk b{width:36px;height:36px}
.c.rt table,.c.rt tbody,.c.rt tr,.c.rt td{display:block;width:100%}
.c.rt tr:first-child{display:none}
.c.rt tr{padding:10px 0;border-top:1px solid #F0EEF1}.c.rt tr:hover td{background:none}
.c.rt td{border:0;padding:3px 0;display:flex;justify-content:space-between;align-items:center;gap:14px;text-align:right}
.c.rt td:before{content:attr(data-label);color:#6B6D7A;font-size:13px;text-align:left;flex:none}
.c.rt td:first-child{font-weight:600;font-size:16px}.c.rt td:first-child:before{display:none}
.bt{padding:0 18px}.hero .bt{min-height:44px}
.sx .r.h{display:none}.sx .r{grid-template-columns:1fr 1fr;min-width:0;gap:4px 12px;padding:12px 14px;font-size:14px}
.sx .r .ph{grid-column:1;font-size:16px;font-weight:600}.sx .r .bdg{grid-column:2;grid-row:1;justify-self:end}
.sx .r>div[data-label]:before{content:attr(data-label) ': ';color:#6B6D7A;font-size:13px}
.sg2{grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:56px 12px;margin-top:56px}.pf{margin-top:56px;padding-top:54px}.pf .pa{top:-48px;width:96px;height:96px}.pf .pa div{width:76px;height:76px}.pf .ch.nb{padding:6px 14px!important}
.trw{display:grid!important;grid-template-columns:repeat(2,1fr);gap:12px!important}.trw .tc{width:auto;min-width:0;height:108px}.trw .tc .tn{font-size:18px}.trw .tc em{right:8px;bottom:8px;padding:4px 14px}.trw .tc:hover{transform:translateY(-3px)}
}
@media(max-width:380px){
.mn{padding:14px 12px calc(100px + env(safe-area-inset-bottom))}
.hero>svg{width:84px}.hl{font-size:22px}.hs{font-size:13px}
.k{font-size:26px}.g{gap:10px}.g .c,.c{padding:14px}.sb a{font-size:9px}.sb{left:6px;right:6px}
.dn{width:230px}.tl b{font-size:19px}
}
"""
LOGO = open(__file__.rsplit('/',1)[0]+'/logo_uri.txt').read().strip()
CAPMENU = '<div class="mm3"><button class="mm3b" aria-label="ตัวเลือกเพิ่มเติม" aria-haspopup="menu" data-tour="cap" onClick="{{toggleMenu}}">···</button><sc-if value="{{menuOpen}}"><div class="mov" onClick="{{toggleMenu}}"></div><div class="mpop" role="menu"><button role="menuitem" data-tour="capitem" onClick="{{openCap}}">ตั้งค่าจำนวนคิวสูงสุด</button></div></sc-if></div>'
EXTRA_CSS = r"""
#tour-root{position:fixed;inset:0;z-index:60}.tr-b{position:absolute;inset:0}.tr-h{position:absolute;border-radius:16px;box-shadow:0 0 0 9999px rgba(43,45,58,.55),0 0 0 3px #FF9AFF;pointer-events:none;transition:all .25s}
.tr-c{position:absolute;background:#fff;border-radius:18px;padding:16px;box-shadow:0 12px 36px rgba(0,0,0,.28);color:#2B2D3A;box-sizing:border-box}.tr-c small{color:#6B6D7A}.tr-c h4{margin:4px 0 6px;font-size:17px}.tr-c p{margin:0 0 12px;font-size:14px;line-height:1.55;color:#4A4C5A}
.tr-r{display:flex;align-items:center;gap:8px}.tr-r span{flex:1}.tr-r button{min-height:40px;border:0;border-radius:20px;padding:0 16px;font:inherit;cursor:pointer;background:#FF9AFF;color:#2B2D3A;font-weight:600}.tr-r .tr-s{background:none;padding:0 4px;color:#6B6D7A;font-weight:400;text-decoration:underline}.tr-r .tr-p{background:#F3F3F3}
.hr .hlp{font-size:20px}

.obx{background:#fff;border:2px solid #FFDFFF;border-radius:28px;padding:20px 22px;margin-bottom:22px;box-shadow:0 10px 30px rgba(255,154,255,.18)}.obh{display:flex;justify-content:space-between;gap:6px 14px;flex-wrap:wrap;align-items:baseline}.obh small{color:#6B6D7A}
.obbar{height:10px;border-radius:5px;background:#EDEDED;margin:12px 0;overflow:hidden}.obbar i{display:block;height:100%;background:#FF9AFF;border-radius:5px;transition:width .6s}
.obs{display:flex;gap:6px;align-items:center;flex-wrap:wrap}.obs em{font-style:normal;display:inline-flex;align-items:center;gap:6px;min-height:32px;border-radius:16px;font-size:13px;color:#6B6D7A}.obs em u{text-decoration:none;width:28px;height:28px;border-radius:50%;display:grid;place-items:center;background:#EDEDED;font-weight:600;flex:none}.obs em.ok u{background:#CDEFD9;color:#1F7A4D}.obs em.cur{background:#FFDFFF;color:#2B2D3A;font-weight:600;padding-right:12px}.obs em.cur u{background:#FF9AFF}
.obt{font-size:19px;font-weight:600;margin:14px 0 2px}.obd{margin:0 0 12px;color:#4A4C5A}.obsub{display:grid;gap:6px;margin:0 0 14px}.obsub div{display:flex;gap:8px;align-items:center}.obsub u{text-decoration:none;width:24px;height:24px;border-radius:50%;display:grid;place-items:center;border:2px solid #D9D9D9;font-size:13px;flex:none}.obsub .ok u{background:#CDEFD9;border-color:#7BD3A0;color:#1F7A4D}
.oblk{position:fixed;inset:0;z-index:30;background:rgba(247,247,247,.82);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);display:grid;place-items:center;padding:24px}.obcard{background:#fff;border-radius:28px;padding:28px 26px;max-width:420px;text-align:center;box-shadow:0 18px 50px rgba(60,40,70,.18)}.obcard h2{margin:0 0 8px}.obcard p{margin:0 0 16px;color:#4A4C5A}
.sb{z-index:31}.sb a.lkd{opacity:.42;position:relative}.sb a.lkd:after{content:"🔒";position:absolute;top:2px;right:10px;font-size:10px}
.mm3{position:relative;display:inline-block}.mm3b{width:44px;height:44px;border:0;border-radius:50%;background:#F3F3F3;font:inherit;font-size:22px;font-weight:700;letter-spacing:1px;cursor:pointer;color:#4A4C5A;transition:.2s}.mm3b:hover{background:#FFDFFF}.mov{position:fixed;inset:0;z-index:40}.mpop{position:absolute;right:0;top:50px;z-index:41;background:#fff;border-radius:14px;box-shadow:0 10px 30px rgba(0,0,0,.15);padding:6px;min-width:210px}.mpop button{display:block;width:100%;min-height:44px;border:0;background:none;text-align:left;padding:0 14px;border-radius:10px;font:inherit;cursor:pointer}.mpop button:hover{background:#FFDFFF}
.lgd b{background:#FF9AFF!important}.lgd b.a{background:#FFDFFF!important}
.si{flex:1;min-width:200px;max-width:340px;height:44px;border:1px solid #D9D9D9;border-radius:22px;padding:0 18px;font-size:15px;background:#fff}
.sg{display:flex;gap:8px;flex-wrap:wrap}.sg button{min-height:44px;border:0;border-radius:22px;padding:0 20px;background:#fff;box-shadow:0 4px 14px rgba(0,0,0,.06);cursor:pointer;font-size:15px;transition:.2s}.sg button.on{background:#FF9AFF;font-weight:600}.sg button:hover{transform:translateY(-1px)}
.bt[disabled]{opacity:.65;cursor:wait}.bt[disabled]:before{content:"";display:inline-block;width:12px;height:12px;border:2px solid #2B2D3A;border-top-color:transparent;border-radius:50%;margin-right:8px;vertical-align:-2px;animation:spn .8s linear infinite}@keyframes spn{to{transform:rotate(360deg)}}
.kv{display:flex;justify-content:space-between;gap:12px;padding:11px 0;border-top:1px solid #F0EEF1}.kv span{color:#6B6D7A}
.tl{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;margin-bottom:14px}.tl div{background:#FFF3FF;border-radius:20px;padding:14px}.tl small{display:block;color:#6B6D7A}.tl b{font-size:22px}
.em{text-align:center;padding:30px 10px;color:#6B6D7A}.em h2{color:#2B2D3A;margin:10px 0 6px}.em p{margin:0 auto 14px;max-width:420px}
.to{position:fixed;left:50%;top:24px;bottom:auto;transform:translateX(-50%);background:#2B2D3A;color:#fff;border-radius:24px;padding:12px 24px;animation:tpin .3s;z-index:60;max-width:92vw;text-align:center}@keyframes tpin{from{opacity:0;transform:translateX(-50%) translateY(-10px)}}
.tp{animation:tpin2 .35s ease-out}@keyframes tpin2{from{opacity:0;transform:translateX(14px)}}
.hi2{border-top:1px solid #F0EEF1;padding:10px 0}.hi2>button{display:grid;grid-template-columns:1fr auto;gap:8px;width:100%;border:0;background:none;font:inherit;text-align:left;cursor:pointer;padding:4px 0;color:inherit}.hi2 .dd{background:#FFF3FF;border-radius:16px;padding:10px 14px;margin-top:8px;animation:tpin2 .3s}
.nt button{border:0;background:none;cursor:pointer;margin-left:6px;font-size:16px;color:#5E6070}
.ov{position:fixed;inset:0;background:rgba(43,34,48,.45);display:grid;place-items:start center;z-index:50;padding:48px 16px 16px;overflow:auto;animation:fi .2s}
.md{background:#fff;border-radius:28px;padding:24px;width:min(560px,100%);box-shadow:0 24px 60px rgba(60,40,70,.3)}.md h2{margin:0 0 6px;font-size:20px}.hn{margin:0 0 12px;color:#6B6D7A;font-size:14px}
.fg{display:grid;grid-template-columns:1fr 1fr;gap:12px}.ff{display:grid;gap:4px;font-size:13px;color:#6B6D7A;align-content:start}.ff.full{grid-column:1/-1}
.ff input,.ff select,.ff textarea{height:44px;border:1px solid #D9D9D9;border-radius:16px;padding:0 14px;font:inherit;font-size:15px;color:#2B2D3A;background:#fff;width:100%;min-width:0}.ff textarea{height:84px;padding:10px 14px;resize:vertical}
.ff .nx{background:#FFF3FF;border-radius:16px;padding:10px 14px;color:#2B2D3A;font-size:14px;line-height:1.6}.ff .nx.wr{background:#FBE8A6}
.chs.q{margin-top:8px}.chs{display:flex;flex-wrap:wrap;gap:8px}.chs button{min-height:40px;border:1.5px solid #D9D9D9;background:#fff;border-radius:20px;padding:0 14px;font:inherit;font-size:14px;cursor:pointer;transition:.2s}.chs button.on{background:#FFDFFF;border-color:#FF9AFF;font-weight:600}
.er{color:#B3261E;font-size:14px;min-height:20px;margin-top:10px}
.sel2{height:44px;border:1px solid #D9D9D9;border-radius:22px;padding:0 16px;font:inherit;font-size:15px;background:#FFDFFF;color:#2B2D3A;cursor:pointer}
.stp{display:flex;align-items:center;gap:10px}.stp button{width:44px;height:44px;border:0;border-radius:50%;background:#FFDFFF;cursor:pointer;font-size:18px}.stp b{min-width:130px;text-align:center}
.ck{display:flex;gap:12px;align-items:flex-start;padding:12px 0;border-top:1px solid #F0EEF1;text-decoration:none;color:inherit}.ck:first-of-type{border-top:0}.ck i{flex:none;width:28px;height:28px;border-radius:50%;border:2px solid #D9D9D9;display:grid;place-items:center;font-style:normal;font-size:15px}.ck.ok i{background:#CDEFD9;border-color:#7BD3A0;color:#1F7A4D}.ck small{display:block;color:#6B6D7A}
.empty{background:#fff;border-radius:28px;padding:34px 22px;text-align:center;box-shadow:0 10px 30px rgba(60,40,70,.08);color:#6B6D7A}.empty h2{color:#2B2D3A;margin:10px 0 6px;font-size:20px}.empty p{margin:0 auto 16px;max-width:460px}
.hi0{font-size:22px;font-weight:500}.em svg,.empty svg{margin:0 auto}.mut{color:#6B6D7A}.rg2{display:flex;gap:8px;flex-wrap:wrap}
table.tb2{width:100%;border-collapse:collapse}.tb2 button.lk{border:0;background:none;font:inherit;font-weight:600;cursor:pointer;color:inherit;text-align:left;padding:0;text-decoration:underline dotted}
@media(max-width:820px){.sb a{width:auto;flex:1;min-width:0;font-size:10px;padding:8px 0}.fg{grid-template-columns:1fr}.to{top:12px}}
"""

# ---------- navigation (7 items) ----------
ICONS = {
 'Main': '<path d="M4 11l8-7 8 7v9h-5v-6H9v6H4z"></path>',
 'Schedule': '<rect x="4" y="5" width="16" height="15" rx="3"></rect><path d="M4 10h16M9 3v4M15 3v4"></path>',
 'Clients': '<path d="M12 20s-8-5-8-11a4.5 4.5 0 0 1 8-2.5A4.5 4.5 0 0 1 20 9c0 6-8 11-8 11z"></path>',
 'Staff': '<circle cx="12" cy="8" r="3"></circle><circle cx="5" cy="10" r="2"></circle><circle cx="19" cy="10" r="2"></circle><path d="M6 20c0-4 3-6 6-6s6 2 6 6"></path>',
 'Services': '<path d="M12 3l1.8 4.7L18.5 9.5l-4.7 1.8L12 16l-1.8-4.7L5.5 9.5l4.7-1.8z"></path><path d="M18.5 15l.8 2 2 .8-2 .8-.8 2-.8-2-2-.8 2-.8z"></path>',
 'Finance': '<rect x="4" y="4" width="16" height="16" rx="3"></rect><path d="M9 16v-4M12 16V8M15 16v-6"></path>',
 'Inventory': '<path d="M4 20h16M5 20v-7h5v7M10 20V9h5v11M15 20v-5h4v5"></path>',
}
NAVL = [('Main','ภาพรวม'),('Schedule','ตารางนัด'),('Clients','ลูกค้า'),('Staff','พนักงาน'),('Services','บริการ'),('Finance','การเงิน'),('Inventory','สต็อก')]

def nav(active):
    h = '<nav class="sb"><a class="lg" href="Main.dc.html" aria-label="Solva"><img class="lgi" src="' + LOGO + '" alt="Solva" width="64" height="22"></a>'
    for k, t in NAVL:
        on = ' class="on {{lk.%s}}"' % k if k == active else ' class="{{lk.%s}}"' % k
        h += ('<a href="%s.dc.html"%s aria-label="%s"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
              'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">%s</svg>%s</a>') % (k, on, t, ICONS[k], t)
    return h + '</nav>'

AVATAR = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="3.5"></circle><path d="M5 20c1-4 4-5.5 7-5.5s6 1.5 7 5.5"></path></svg>'
BELL = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 17h12l-1.5-2v-4a4.5 4.5 0 0 0-9 0v4zM10 20h4"></path></svg>'
HEART = '<svg width="84" height="84" viewBox="0 0 100 100" aria-hidden="true"><g class="fl2"><path d="M50 84S16 64 16 40a17 17 0 0 1 34-6 17 17 0 0 1 34 6c0 24-34 44-34 44z" fill="#FFDFFF" stroke="#FF9AFF" stroke-width="4"></path></g></svg>'
HEART = HEART.replace('fl2', 'fl')

def header(extra=''):
    return ('<header class="hd"><div><div class="hi0">Welcome back</div><div class="sub">{{today}}</div></div>'
            '<div class="hr">' + extra + '<button class="av2 hlp" style="border:0;cursor:pointer;font:inherit;font-weight:700;font-size:20px" aria-label="ดูคำแนะนำการใช้งาน" title="ดูคำแนะนำการใช้งาน" onClick="{{tourStart}}">?</button><button class="av2" data-tour="shop" style="border:0;cursor:pointer" aria-label="ตั้งค่าร้าน" onClick="{{openShop}}">' + AVATAR + '</button></div></header>')

def hero(svg, title_html, sub_html, btn_html):
    return ('<section class="hero rs"><span class="bl" style="width:200px;height:200px;left:-40px;top:-60px"></span>'
            '<span class="bl" style="width:160px;height:160px;right:30%;bottom:-70px;opacity:.4"></span>'
            '<div class="tx"><div class="hl">' + title_html + '</div><div class="hs">' + sub_html + '</div>' + btn_html + '</div>' + svg + '</section>')

WARN0 = '<sc-if value="{{noStore}}" hint-placeholder-val="{{false}}"><div class="wn">⚠ มุมมองนี้บันทึกข้อมูลถาวรไม่ได้ ข้อมูลที่เพิ่มจะหายเมื่อปิดหน้า ลองเปิดจากลิงก์ที่แชร์ของ artifact</div></sc-if>'

GUIDE = '<sc-if value="{{g.on}}" hint-placeholder-val="{{false}}"><section class="obx" role="status" aria-label="ขั้นตอนเริ่มต้นใช้งาน"><div class="obh"><b>ตั้งค่าร้าน · ขั้นตอนที่ {{g.n}} จาก 5</b><small>{{g.nextTxt}}</small></div><div class="obbar"><i style="width:{{g.pct}}%"></i></div>' \
 '<div class="obs"><sc-for list="{{g.dots}}" as="x"><em class="{{x.c}}"><u>{{x.m}}</u>{{x.t}}</em></sc-for></div><h3 class="obt">{{g.t}}</h3><p class="obd">{{g.desc}}</p>' \
 '<sc-if value="{{g.hasSubs}}"><div class="obsub"><sc-for list="{{g.subs}}" as="y"><div class="{{y.c}}"><u>{{y.m}}</u>{{y.t}}</div></sc-for></div></sc-if><button class="bt" onClick="{{g.go}}">{{g.btn}}</button></section></sc-if>'
WARN = WARN0 + GUIDE

# generic modal form (fields are described by renderVals: fm = {open,title,hint,fields,err,saveTxt,save,close,stop,canDel,del,delTxt})
MODAL = (
'<sc-if value="{{fm.open}}" hint-placeholder-val="{{false}}"><div class="ov" onClick="{{fm.close}}"><div class="md" onClick="{{fm.stop}}">'
'<h2>{{fm.title}}</h2><sc-if value="{{fm.hasHint}}"><p class="hn">{{fm.hint}}</p></sc-if>'
'<div class="fg"><sc-for list="{{fm.fields}}" as="f" hint-placeholder-count="4"><div class="ff {{f.cls}}"><span>{{f.label}}</span>'
'<sc-if value="{{f.isIn}}"><input type="{{f.type}}" value="{{f.v}}" placeholder="{{f.ph}}" onInput="{{f.on}}"><sc-if value="{{f.hasQ}}"><div class="chs q"><sc-for list="{{f.qs}}" as="c"><button class="{{c.on}}" onClick="{{c.pick}}">{{c.t}}</button></sc-for></div></sc-if></sc-if>'
'<sc-if value="{{f.isSel}}"><select value="{{f.v}}" onChange="{{f.on}}"><sc-for list="{{f.opts}}" as="o"><option value="{{o.v}}">{{o.t}}</option></sc-for></select></sc-if>'
'<sc-if value="{{f.isTa}}"><textarea placeholder="{{f.ph}}" value="{{f.v}}" onInput="{{f.on}}"></textarea></sc-if>'
'<sc-if value="{{f.isChips}}"><div class="chs"><sc-for list="{{f.chips}}" as="c"><button class="{{c.on}}" onClick="{{c.pick}}">{{c.t}}</button></sc-for></div></sc-if>'
'<sc-if value="{{f.isNote}}"><div class="nx {{f.wr}}">{{f.v}}</div></sc-if>'
'</div></sc-for></div><div class="er">{{fm.err}}</div>'
'<div class="row" style="margin:10px 0 0"><button class="bt" onClick="{{fm.save}}">{{fm.saveTxt}}</button><button class="bt d" onClick="{{fm.close}}">ยกเลิก</button>'
'<sc-if value="{{fm.hasExtra}}"><button class="bt o" onClick="{{fm.extra}}">{{fm.extraTxt}}</button></sc-if>'
'<sc-if value="{{fm.canDel}}"><button class="bt o" style="margin-left:auto" onClick="{{fm.del}}">{{fm.delTxt}}</button></sc-if></div></div></div></sc-if>'
'<sc-if value="{{toast}}"><div class="to">{{toastText}}</div></sc-if>')

# ---------------------------------------------------------------- shared JS core
CORE_JS = r"""
const SK='solva_data_v1',UK='solva_ui_v1';
const TH_M=['ม.ค.','ก.พ.','มี.ค.','เม.ย.','พ.ค.','มิ.ย.','ก.ค.','ส.ค.','ก.ย.','ต.ค.','พ.ย.','ธ.ค.'],TH_F=['มกราคม','กุมภาพันธ์','มีนาคม','เมษายน','พฤษภาคม','มิถุนายน','กรกฎาคม','สิงหาคม','กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม'],TH_D=['อาทิตย์','จันทร์','อังคาร','พุธ','พฤหัสบดี','ศุกร์','เสาร์'],TH_S=['อา','จ','อ','พ','พฤ','ศ','ส'];
const TIER0=[{n:'Pearl',min:0,disc:0},{n:'Gold',min:10000,disc:5},{n:'Platinum',min:30000,disc:10},{n:'Diamond',min:60000,disc:15}],TCL={Pearl:'pe',Gold:'go',Platinum:'pl',Diamond:'di'},PAYM=['เงินสด','โอนเงิน / PromptPay','บัตรเครดิต/เดบิต'];
const EMPTY=()=>({v:1,seq:1,shop:{name:'',phone:'',goal:0,hours:null,setup:false},tiers:TIER0.map(t=>Object.assign({},t)),customers:[],staff:[],services:[],appts:[],att:[],tx:[],products:[],stock:[]});
let MEM=null,OKS=true;
try{localStorage.setItem('solva_probe','1');localStorage.removeItem('solva_probe')}catch(e){OKS=false}
function load(){if(OKS){try{const r=localStorage.getItem(SK);MEM=r?Object.assign(EMPTY(),JSON.parse(r)):EMPTY();return MEM}catch(e){OKS=false}}if(!MEM)MEM=EMPTY();return MEM}
function save(d){MEM=d;if(OKS){try{localStorage.setItem(SK,JSON.stringify(d))}catch(e){OKS=false}}try{if(window.BroadcastChannel){const b=new BroadcastChannel('solva');b.postMessage(1);b.close()}}catch(e){}}
const M=fn=>{const d=load(),r=fn(d);save(d);window.__lw=Date.now();return r};
function uiGet(){try{return JSON.parse(localStorage.getItem(UK)||'{}')}catch(e){return {}}}
function uiSet(o){try{localStorage.setItem(UK,JSON.stringify(Object.assign(uiGet(),o)))}catch(e){}}
const p2=n=>String(n).padStart(2,'0'),iso=x=>x.getFullYear()+'-'+p2(x.getMonth()+1)+'-'+p2(x.getDate()),pd=s=>{const a=s.split('-');return new Date(+a[0],+a[1]-1,+a[2])},TODAY=()=>iso(new Date()),NOWT=()=>{const x=new Date();return p2(x.getHours())+':'+p2(x.getMinutes())};
const thD=s=>{if(!s)return '—';const x=pd(s);return x.getDate()+' '+TH_M[x.getMonth()]+' '+(x.getFullYear()+543)},thS=s=>{const x=pd(s);return x.getDate()+' '+TH_M[x.getMonth()]},thL=s=>{const x=pd(s);return 'วัน'+TH_D[x.getDay()]+'ที่ '+x.getDate()+' '+TH_F[x.getMonth()]+' '+(x.getFullYear()+543)};
const mkey=s=>s.slice(0,7),mAdd=(k,n)=>{const a=k.split('-'),x=new Date(+a[0],+a[1]-1+n,1);return x.getFullYear()+'-'+p2(x.getMonth()+1)},mTxt=k=>{const a=k.split('-');return TH_F[+a[1]-1]+' '+(+a[0]+543)},mShort=k=>TH_M[+k.split('-')[1]-1],mDays=k=>{const a=k.split('-');return new Date(+a[0],+a[1],0).getDate()};
const fm=n=>(n<0?'−':'')+'฿'+Math.round(Math.abs(n)).toLocaleString('en-US'),nn=n=>Math.round(n).toLocaleString('en-US');
const sum=(a,f)=>a.reduce((s,x)=>s+f(x),0),tmin=t=>{const a=(t||'0:0').split(':');return +a[0]*60+ +a[1]};
const sub=a=>sum(a.items,i=>i.price),dsc=a=>Math.round(sub(a)*(a.disc||0)/100),net=a=>sub(a)-dsc(a),dur=a=>sum(a.items,i=>i.dur||0);
const getC=(d,id)=>d.customers.find(c=>c.id===id),getS=(d,id)=>d.staff.find(s=>s.id===id),cName=(d,id)=>{const c=getC(d,id);return c?c.name:'(ลูกค้าที่ถูกลบ)'},sName=(d,id)=>{const s=getS(d,id);return s?s.name:'(พนักงานที่ถูกลบ)'};
const isRev=a=>a.status==='done'&&a.paid,commOf=(a,st)=>st&&st.rate!=null&&st.rate!==''&&isRev(a)?Math.round(net(a)*st.rate/100):0;
const stOf=a=>a.status==='canceled'?['ยกเลิก','s3']:a.status==='noshow'?['ไม่มาตามนัด','s3']:a.status==='done'?(a.paid?['เสร็จสิ้น','s1']:['รอชำระเงิน','s2']):['ยืนยันแล้ว','s1'];
const cStats=(d,c)=>{const L=d.appts.filter(a=>a.cust===c.id&&a.status==='done'),P=L.filter(a=>a.paid),dates=L.map(a=>a.date).sort();return{visits:L.length,spend:sum(P,net),last:dates.length?dates[dates.length-1]:null,list:L}};
const tierO=(d,c)=>c&&c.tier?d.tiers.find(t=>t.n===c.tier):null;
const nextTier=(d,c)=>{const i=c.tier?d.tiers.findIndex(t=>t.n===c.tier):-1;return i>=0&&i<d.tiers.length-1?d.tiers[i+1]:null};
const capOf=d=>d.shop.cap||5,actN=(d,date,ex)=>d.appts.filter(a=>a.date===date&&a.status!=='canceled'&&a.id!==ex).length,isFull=(d,date,ex)=>actN(d,date,ex)>=capOf(d);
function capMo(self,F,S){return{title:'ตั้งค่าจำนวนคิวสูงสุด',hint:'จำนวนนัดหมายสูงสุดที่ร้านรับได้ต่อวัน (ไม่นับนัดที่ยกเลิก) เมื่อครบแล้ววันนั้นจะขึ้น “คิวเต็ม” และสร้างนัดเพิ่มไม่ได้',spec:[{k:'cap',label:'จำนวนคิวสูงสุดต่อวัน',type:'number',ph:'เช่น 8',quick:[5,8,10,12,15],unit:'คิว'}],saveTxt:'บันทึก',save:()=>{const n=Math.round(+F.cap);if(!(n>=1&&n<=200))return self.setState({fe:'กรุณากรอกจำนวนคิวเป็นเลข 1–200'});M(x=>{x.shop.cap=n});self.setState({form:null,fe:''});self.toast('บันทึกจำนวนคิวสูงสุดแล้ว: '+n+' คิวต่อวัน')}}}
const overlap=(d,a)=>{if(a.status==='canceled'||a.status==='noshow')return [];const s=tmin(a.time),e=s+Math.max(dur(a),1);return d.appts.filter(b=>b.id!==a.id&&b.staff===a.staff&&b.date===a.date&&b.status!=='canceled'&&b.status!=='noshow'&&tmin(b.time)<e&&s<tmin(b.time)+Math.max(dur(b),1))};
const attOf=(d,sid,date)=>d.att.find(x=>x.staff===sid&&x.date===date);
const attSt=(s,r)=>{if(!r)return null;if(r.type==='leave')return 'leave';if(r.type==='absent')return 'absent';return r.in&&tmin(r.in)>tmin(s.ws||'09:00')?'late':'ontime'};
const ATL={ontime:['ตรงเวลา','s1'],late:['มาสาย','s2'],leave:['ลา','nt'],absent:['ขาด','s3']};
const stockSt=p=>p.qty<=0?['หมด','s3']:p.qty<=p.min?['ใกล้หมด','s2']:['ปกติ','s1'];
const ten=s=>{if(!s)return '—';const a=pd(s),n=new Date();let m=(n.getFullYear()-a.getFullYear())*12+n.getMonth()-a.getMonth();if(n.getDate()<a.getDate())m--;if(m<0)return 'เพิ่งเริ่ม';const y=Math.floor(m/12);return (y?y+' ปี ':'')+(m%12)+' เดือน'};
const revOf=(d,from,to)=>sum(d.appts.filter(a=>isRev(a)&&(a.paidDate||a.date)>=from&&(a.paidDate||a.date)<=to),net)+sum(d.tx.filter(t=>t.type==='in'&&t.date>=from&&t.date<=to),t=>t.amount);
const mRange=k=>[k+'-01',k+'-'+p2(mDays(k))];
const missing=d=>{const m=[];if(!d.services.length)m.push({t:'เพิ่มบริการและราคา',h:'Services.dc.html'});if(!d.staff.length)m.push({t:'เพิ่มพนักงาน',h:'Staff.dc.html'});return m};

const STEPS=[
{t:'ตั้งชื่อร้าน',d:'ชื่อร้านจะแสดงบนบิลและรายงาน เริ่มจากตั้งชื่อร้านของคุณก่อน',page:'Main',open:'name1',btn:'ตั้งชื่อร้าน'},
{t:'เพิ่มบริการและกำหนดเวลาทำการ',d:'เพิ่มบริการที่ร้านให้พร้อมราคา และกำหนดวันเวลาเปิด–ปิดร้าน',page:'Services',open:'sv',btn:'เพิ่มบริการ'},
{t:'เพิ่มพนักงาน',d:'เพิ่มช่างหรือพนักงานที่ให้บริการ เพื่อรับนัดหมายและคำนวณค่าคอมมิชชัน',page:'Staff',open:'staff',btn:'เพิ่มพนักงานคนแรก'},
{t:'เพิ่มลูกค้า',d:'เพิ่มลูกค้าอย่างน้อย 1 คน เพื่อใช้สร้างนัดหมาย',page:'Clients',open:'cust',btn:'เพิ่มลูกค้าคนแรก'},
{t:'สร้างนัดหมายแรก',d:'เลือกลูกค้า ช่าง และบริการ ระบบจะคิดราคาให้อัตโนมัติ',page:'Schedule',open:'appt',btn:'สร้างนัดหมายแรก'}];
const NAVP=['Main','Schedule','Clients','Staff','Services','Finance','Inventory'];
const hrsOk=d=>{const h=d.shop.hours;return !!(h&&h.open&&h.close&&h.open<h.close&&(h.days||[]).length)};
const stepDone=d=>[!!d.shop.name,d.services.length>0&&hrsOk(d),d.staff.length>0,d.customers.length>0,d.appts.length>0];
const stepNow=d=>{if(d.shop.setup)return 5;const i=stepDone(d).indexOf(false);return i<0?5:i};
const pageAllowed=()=>true;
const goPage=(pg)=>{const a=document.createElement('a');a.href=pg+'.dc.html';document.body.appendChild(a);a.click();a.remove()};
const DAYN=['อาทิตย์','จันทร์','อังคาร','พุธ','พฤหัส','ศุกร์','เสาร์'];
const hoursTxt=d=>{const h=d.shop.hours;if(!hrsOk(d))return 'ยังไม่ได้ตั้ง';const ds=h.days.length===7?'ทุกวัน':h.days.map(x=>DAYN[x].replace('วัน','')).join(' ');return ds+' '+h.open+'–'+h.close};
function guideGo(self){const d=load(),n=stepNow(d);if(n>=5)return;const s=STEPS[n];let open=s.open;if(n===1&&d.services.length&&!hrsOk(d))open='hours';uiSet({open});if(PAGE===s.page&&self.boot)self.boot();else goPage(s.page)}
function guideVals(self){const d=load(),n=stepNow(d),on=n<5,s=STEPS[Math.min(n,4)],lk={};NAVP.forEach(p=>{lk[p]=pageAllowed(d,p)?'':'lkd'});
const subs=n===1?[{m:d.services.length?'✓':'○',c:d.services.length?'ok':'',t:'เพิ่มบริการอย่างน้อย 1 รายการ'+(d.services.length?' ('+d.services.length+')':'')},{m:hrsOk(d)?'✓':'○',c:hrsOk(d)?'ok':'',t:'กำหนดเวลาทำการ'+(hrsOk(d)?' · '+hoursTxt(d):'')}]:[];
const btn=n===1&&d.services.length&&!hrsOk(d)?'ตั้งเวลาทำการ':s.btn;
return{lk,tourStart:()=>tourStart(),g:{on,n:n+1,t:s.t,desc:s.d,pct:Math.round(n/5*100),nextTxt:n<4?'ถัดไป: '+STEPS[n+1].t:'ขั้นตอนสุดท้าย',subs,hasSubs:subs.length>0,btn,go:()=>guideGo(self),dots:STEPS.map((x,i)=>({m:i<n?'✓':String(i+1),c:i<n?'ok':i===n?'cur':'',t:i===n?x.t:''}))}}}
const TK='solva_tour_v1';
const TOUR=[
{p:'Main',s:'[data-tour=cap]',t:'ตั้งจำนวนคิวสูงสุดต่อวัน',d:'กดปุ่ม ··· ตรงนี้เพื่อเปิดเมนู แล้วตั้งว่าวันหนึ่งรับได้กี่คิว'},
{p:'Main',s:'[data-tour=capitem]',pre:'[data-tour=cap]',t:'เลือก “ตั้งค่าจำนวนคิวสูงสุด”',d:'กดเมนูนี้เพื่อกำหนดจำนวนคิวต่อวัน เมื่อคิวเต็ม ปฏิทินจะขึ้น “คิวเต็ม” และระบบจะไม่รับนัดเพิ่ม เปลี่ยนตัวเลขได้ทุกเมื่อ'},
{p:'Main',s:'[data-tour=shop]',t:'ตั้งค่าร้าน',d:'กดไอคอนนี้เพื่อแก้ชื่อร้าน เบอร์โทร และเป้าหมายรายได้ต่อเดือน รวมถึงสำรองข้อมูลเป็นไฟล์หรือรีเซ็ตข้อมูลเพื่อเริ่มใหม่'},
{p:'Schedule',s:'[data-tour=appt]',t:'สร้างและแก้นัดหมาย',d:'กดสร้างนัดหมายได้จากตรงนี้ ส่วนนัดที่มีอยู่ ให้กดที่รายการเพื่อเลื่อนเวลา เปลี่ยนช่าง รับชำระ หรือยกเลิกได้'},
{p:'Services',s:'[data-tour=hours]',t:'แก้เวลาทำการ',d:'เปลี่ยนวันและเวลาเปิด–ปิดร้านได้ตรงนี้ ระบบจะไม่รับนัดในวันหรือเวลาที่ร้านปิด ส่วนราคาและบริการแก้ได้โดยกดที่รายการบริการ'},
{p:'Staff',s:'[data-tour=staff]',t:'จัดการพนักงาน',d:'เพิ่มพนักงานใหม่ได้ที่นี่ กดชื่อพนักงานในรายการเพื่อแก้เวลาทำงาน ทักษะ และอัตราค่าคอมมิชชัน หรือเช็คอินเข้างาน'},
{p:'Clients',s:'[data-tour=tier]',t:'ตั้งค่าระดับสมาชิก',d:'กำหนดระดับสมาชิก ส่วนลด และเงื่อนไขการอัปเกรดได้ที่นี่ ส่วนข้อมูลและโน้ตของลูกค้าแต่ละคนแก้ได้จากหน้าโปรไฟล์'},
{p:'Finance',s:'[data-tour=goal]',t:'ตั้งเป้าหมายรายได้',d:'ตั้งหรือเปลี่ยนเป้าหมายรายได้ต่อเดือน กราฟวงกลมจะแสดงว่าทำได้ถึงเป้าแล้วกี่เปอร์เซ็นต์'},
{p:'Inventory',s:'[data-tour=stock]',t:'เพิ่มสินค้าและสต็อก',d:'เพิ่มสินค้าและกำหนดจุดสั่งซื้อซ้ำ เมื่อของใกล้หมดระบบจะแจ้งเตือน'}];
function tourGet(){try{return JSON.parse(localStorage.getItem(TK)||'null')}catch(e){return window.__tr||null}}
function tourSet(v){window.__tr=v;try{if(v==null)localStorage.removeItem(TK);else localStorage.setItem(TK,JSON.stringify(v))}catch(e){}}
function tourClose(){const r=document.getElementById('tour-root');if(r)r.remove();clearInterval(window.__tti);document.removeEventListener('keydown',window.__tkd||(()=>{}));window.addEventListener&&window.removeEventListener('resize',window.__trs||(()=>{}))}
function tourMenu(){const o=document.querySelector('.mov');if(o)o.click()}
function tourEnd(){tourMenu();tourClose();tourSet({done:1})}
function tourStart(){tourSet({i:0});const f=TOUR.findIndex(x=>x.p===PAGE);if(f===0)tourShow(0);else goPage('Main')}
function tourBoot(){const st=tourGet();if(!st||st.done||st.i==null)return;const k=st.i;if(!TOUR[k]||TOUR[k].p!==PAGE)return;setTimeout(()=>tourShow(k),700)}
function tourNext(i,dir){const j=i+dir;if(TOUR[i]&&TOUR[i].pre)tourMenu();tourClose();if(j>=TOUR.length){tourEnd();return}if(j<0)return;tourSet({i:j});if(TOUR[j].p===PAGE)tourShow(j);else goPage(TOUR[j].p)}
function tourShow(i,tries){tries=tries||0;const st=TOUR[i];if(!st){tourEnd();return}tourClose();
let el=document.querySelector(st.s);const vis=e=>{if(!e)return false;const r=e.getBoundingClientRect();return r.width>2&&r.height>2};
if(!vis(el)&&st.pre&&tries===0){const b=document.querySelector(st.pre);if(b&&!document.querySelector('.mov'))b.click()}
if(!vis(el)){if(tries<8){setTimeout(()=>tourShow(i,tries+1),250);return}if(i+1<TOUR.length&&TOUR[i+1].p===PAGE){tourSet({i:i+1});return tourShow(i+1)}return tourNext(i,1)}
const root=document.createElement('div');root.id='tour-root';
root.innerHTML='<div class="tr-b"></div><div class="tr-h"></div><div class="tr-c" role="dialog" aria-label="คำแนะนำการใช้งาน"><small></small><h4></h4><p></p><div class="tr-r"><button class="tr-s">ข้ามคำแนะนำ</button><span></span><button class="tr-p">ย้อนกลับ</button><button class="tr-n"></button></div></div>';
document.body.appendChild(root);
const h=root.querySelector('.tr-h'),c=root.querySelector('.tr-c');
c.querySelector('small').textContent='คำแนะนำ '+(i+1)+' จาก '+TOUR.length;c.querySelector('h4').textContent=st.t;c.querySelector('p').textContent=st.d;
const nb=c.querySelector('.tr-n');nb.textContent=i===TOUR.length-1?'เสร็จสิ้น':'ถัดไป';nb.onclick=()=>tourNext(i,1);
const pb=c.querySelector('.tr-p');if(i===0)pb.style.display='none';pb.onclick=()=>tourNext(i,-1);
c.querySelector('.tr-s').onclick=()=>tourEnd();
const place=()=>{const e=document.querySelector(st.s);if(!e)return;const r=e.getBoundingClientRect(),vw=innerWidth,vh=innerHeight,p=6;
h.style.cssText='left:'+(r.left-p)+'px;top:'+(r.top-p)+'px;width:'+(r.width+2*p)+'px;height:'+(r.height+2*p)+'px';
const cw=Math.min(320,vw-24);c.style.width=cw+'px';const ch=c.offsetHeight;let top=r.bottom+p+12;if(top+ch>vh-12)top=Math.max(12,r.top-p-12-ch);
let left=r.left+r.width/2-cw/2;left=Math.max(12,Math.min(left,vw-cw-12));c.style.top=top+'px';c.style.left=left+'px'};
try{el.scrollIntoView({block:'center',inline:'nearest'})}catch(e){}
setTimeout(()=>{place();nb.focus&&nb.focus({preventScroll:true})},120);
window.__trs=place;window.addEventListener('resize',place);window.addEventListener('scroll',place,true);
window.__tti=setInterval(()=>{if(!document.getElementById('tour-root'))clearInterval(window.__tti);else place()},400);
window.__tkd=e=>{if(e.key==='Escape')tourEnd()};document.addEventListener('keydown',window.__tkd)}
class Base extends DCLogic{
componentDidMount(){this._h=()=>this.setState({_t:Date.now()});window.addEventListener('storage',this._h);try{if(window.BroadcastChannel){this._bc=new BroadcastChannel('solva');this._bc.onmessage=this._h}}catch(e){}window.addEventListener('focus',this._h);this._sn=stepNow(load());this.boot&&this.boot();tourBoot()}
componentDidUpdate(){const d=load(),n=stepNow(d),p=this._sn;this._sn=n;if(p==null||n<=p)return;if(n>=5&&!d.shop.setup)M(x=>{x.shop.setup=true});if(Date.now()-(window.__lw||0)>2500)return;const done=STEPS[Math.min(n,5)-1],nx=n>=5?null:STEPS[n];this.toast('✓ ขั้นตอนที่ '+n+' เสร็จแล้ว: '+done.t+(nx?' · ไปต่อ: '+nx.t:' · ตั้งค่าร้านครบแล้ว!'),3200);setTimeout(()=>{if(nx){uiSet({open:nx.open});goPage(nx.page)}else{const t=tourGet();if(!t||(!t.done&&t.i==null))tourSet({i:0});goPage('Main')}},1500)}
componentWillUnmount(){window.removeEventListener('storage',this._h);window.removeEventListener('focus',this._h);try{this._bc&&this._bc.close()}catch(e){}}
toast(m,ms){this.setState({to:m});clearTimeout(this._tt);this._tt=setTimeout(()=>this.setState({to:''}),ms||2400)}
toggleMenu=()=>this.setState({menu:!this.state.menu});
fld(k){return e=>this.setState({form:Object.assign({},this.state.form,{[k]:e.target.value}),fe:''})}
chip(k,v){const f=this.state.form,a=f[k]||[];this.setState({form:Object.assign({},f,{[k]:a.includes(v)?a.filter(x=>x!==v):[...a,v]}),fe:''})}
}
// build the field list for the generic modal. spec: [{k,label,type,ph,opts,full,ta,note,chips,wr}]
function fieldsOf(self,spec,F){return spec.map(f=>{const v=f.note!=null?f.note:(F[f.k]==null?'':F[f.k]);return{label:f.label,cls:f.full?'full':'',isIn:!f.opts&&!f.ta&&!f.chips&&f.note==null,isSel:!!f.opts,isTa:!!f.ta,isChips:!!f.chips,isNote:f.note!=null,wr:f.wr?'wr':'',type:f.type||'text',ph:f.ph||'',v:v,on:self.fld(f.k),hasQ:!!(f.quick&&f.quick.length),qs:(f.quick||[]).map(q=>{const val=Array.isArray(q)?q[0]:q,t=Array.isArray(q)?q[1]:(f.unit?q+' '+f.unit:q);return{t:t,on:String(F[f.k]==null?'':F[f.k])===String(val)?'on':'',pick:()=>self.setState({form:Object.assign({},self.state.form,{[f.k]:val}),fe:''})}}),opts:(f.opts||[]).map(o=>({v:o[0],t:o[1]})),chips:(f.chips||[]).map(o=>({t:o[1],on:(F[f.k]||[]).includes(o[0])?'on':'',pick:()=>self.chip(f.k,o[0])}))}})}
function modalOf(self,S,o){const open=!!S.form;return{open:open,title:o.title||'',hint:o.hint||'',hasHint:!!o.hint,fields:open?fieldsOf(self,o.spec||[],S.form):[],err:S.fe||'',saveTxt:o.saveTxt||'บันทึก',save:o.save||(()=>{}),close:()=>self.setState({form:null,fe:'',cdel:false}),stop:e=>e.stopPropagation(),hasExtra:!!o.extra,extra:o.extra?o.extra.go:(()=>{}),extraTxt:o.extra?o.extra.t:'',canDel:!!o.del,del:o.del||(()=>{}),delTxt:S.cdel?'กดอีกครั้งเพื่อยืนยันลบ':(o.delTxt||'ลบ')}}
function openCapForm(self){const d=load();self.setState({menu:false,form:{_k:'cap',cap:capOf(d)},fe:''})}
function openShopForm(self){const d=load();self.setState({form:{_k:'shop',name:d.shop.name,phone:d.shop.phone,goal:d.shop.goal||''},fe:''})}
const SHOP_SPEC=[{k:'name',label:'ชื่อร้าน (แสดงบนบิลและรายงาน)',full:1,ph:'เช่น ร้านเล็บของฉัน'},{k:'phone',label:'เบอร์โทรร้าน',type:'tel'},{k:'goal',label:'เป้าหมายรายได้ต่อเดือน (บาท)',type:'number',ph:'ไม่บังคับ'}];
async function saveFile(name,blob){let dl=null;try{dl=window.claude&&await window.claude.use('downloads')}catch(e){}
if(dl)return dl.save({filename:name,data:blob});const u=URL.createObjectURL(blob),a=document.createElement('a');a.href=u;a.download=name;document.body.appendChild(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(u),4000)}
async function backup(self){try{await saveFile('solva-backup-'+TODAY()+'.json',new Blob([JSON.stringify(load())],{type:'application/json'}));self.toast('บันทึกไฟล์สำรองแล้ว')}catch(e){self.toast('บันทึกไฟล์สำรองไม่ได้ในมุมมองนี้')}}
function shopMo(self,F,S){return{title:'ตั้งค่าร้าน',hint:'ชื่อร้านใช้บนบิลและรายงาน · ปุ่ม “รีเซ็ตข้อมูลทั้งหมด” ล้างทุกอย่างเพื่อเริ่มใหม่ (กด 2 ครั้งเพื่อยืนยัน)',spec:SHOP_SPEC,save:()=>saveShop(self),extra:{t:'สำรองข้อมูลเป็นไฟล์',go:()=>backup(self)},delTxt:'รีเซ็ตข้อมูลทั้งหมด',del:()=>{if(!S.cdel)return self.setState({cdel:true});save(EMPTY());tourSet(null);uiSet({open:'',date:'',sel:0});self.setState({form:null,cdel:false,sel:null,fe:'',f:'all',q:''});self.toast('รีเซ็ตข้อมูลทั้งหมดแล้ว')}}}
function saveShop(self){const F=self.state.form;M(d=>{d.shop.name=(F.name||'').trim();d.shop.phone=(F.phone||'').trim();d.shop.goal=Math.max(0,+F.goal||0)});self.setState({form:null,fe:''});self.toast('บันทึกการตั้งค่าร้านแล้ว')}
"""

WRAP = '\n{const _r=Component.prototype.renderVals;Component.prototype.renderVals=function(){return Object.assign({},guideVals(this),_r.call(this))}}\n'

def page(title, css, body, js, extra_head=''):
    return ('<!doctype html><html lang="th"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><title>' + title + '</title><script src="./support.js"></script></head><body><x-dc><helmet>'
            + FONT_LINK + '<style>' + css + EXTRA_CSS + RESP + '</style></helmet>' + body + '</x-dc>'
            '<script type="text/x-dc" data-dc-script data-props=\'{"$preview":{"width":1280,"height":900}}\'>const PAGE="__PAGE__";' + CORE_JS + js + WRAP + '</script></body></html>')

def write(name, html):
    open(OUT + name, 'w', encoding='utf-8').write(html.replace('__PAGE__', name.split('.')[0]))
    print(name, len(html))

def png_js():
    s = rd('Schedule.dc.html')
    a = s.index("const FN=")
    b = s.index("const G=[")
    t = s[a:b]
    old = "async function savePng(spec,fn){const dl=window.claude&&await window.claude.use('downloads');if(!dl)throw {code:'unavailable'};const b=await mkPng(spec);return dl.save({filename:fn,data:b})}"
    assert old in t
    return t.replace(old, "async function savePng(spec,fn){const b=await mkPng(spec);return saveFile(fn,b)}")
