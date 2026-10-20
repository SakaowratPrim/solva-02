# solva-02
Thesis prototype — **Solva**, a Thai-language salon management UI (dashboard, schedule, clients, staff, services, finance, inventory, login).

## Layout
- `out/project/` — the published pages (`*.dc.html`) and `canvas.json` (Design canvas artifact format).
- `gen/` — Python generator that writes those pages. `core.py` holds the shared store, helpers, modal and styles; `p_*.py` builds one page each.

## Rebuild
```
cd gen
for f in p_*.py; do python3 $f; done   # writes ../out/project/*.dc.html
```

## Notes
- Data is stored in the browser's `localStorage` (`solva_data_v1`), per browser — not shared across devices.
- Settings → "รีเซ็ตข้อมูลทั้งหมด" wipes all data (two-tap confirm).
- `Login.dc.html` is hand-written and not produced by the generator.

## Deploy (static site)
`docs/` is a ready-to-host static site (no build step): `index.html` redirects to `Login.dc.html`, and `support.js` is the page runtime.
- **GitHub Pages:** Settings → Pages → Source: *Deploy from a branch* → `main` / `/docs`.
- **Vercel / Netlify:** framework "Other", no build command, output/publish directory `docs`.
- Outside Claude, PNG and backup downloads use the browser's normal download.
- After regenerating pages (`gen/`), copy `out/project/*.dc.html` into `docs/` (keep `Login.dc.html` as is).
