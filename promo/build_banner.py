#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Poziomy banner 1200x630 (og-image / event) — Historia animacji. @2x -> banner.png"""
import os, subprocess, tempfile

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
OUT = os.path.dirname(os.path.abspath(__file__))
LINK = "futureshow.pl/historia-animacji"

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
 '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
 '<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&'
 'family=Space+Grotesk:wght@300;400;500;700&family=IBM+Plex+Mono:wght@400;500&'
 'display=swap" rel="stylesheet">')

HTML = f"""<!doctype html><html lang="pl"><head><meta charset="utf-8">{FONTS}<style>
:root{{--bg:#0f0e13;--card:#16151c;--ink:#f3efe6;--dim:#b5b0a4;--faint:#6f6b63;
  --acc:#ffb320;--line:#2a2833;
  --display:'Archivo Black','Arial Black',sans-serif;
  --body:'Space Grotesk','Helvetica Neue',sans-serif;
  --mono:'IBM Plex Mono','Courier New',monospace;}}
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:1200px;height:630px;}}
body{{background:var(--bg);color:var(--ink);font-family:var(--body);position:relative;
  overflow:hidden;-webkit-font-smoothing:antialiased;}}
/* filmstrip band (signature) */
.strip{{position:absolute;top:-30px;bottom:-30px;right:104px;width:172px;z-index:1;
  background:var(--card);border-left:1px solid var(--line);border-right:1px solid var(--line);}}
.strip::before{{content:"";position:absolute;left:16px;top:0;bottom:0;width:24px;
  background:repeating-linear-gradient(to bottom,var(--bg) 0 22px,transparent 22px 44px);}}
.strip::after{{content:"";position:absolute;right:16px;top:0;bottom:0;width:24px;
  background:repeating-linear-gradient(to bottom,var(--bg) 0 22px,transparent 22px 44px);}}
.frame{{position:absolute;left:52px;right:52px;height:3px;background:var(--acc);opacity:.5;}}
.wrap{{position:absolute;inset:0;z-index:2;display:flex;flex-direction:column;
  justify-content:center;padding:70px 76px;}}
.kicker{{font-family:var(--mono);font-size:21px;letter-spacing:.28em;text-transform:uppercase;
  color:var(--acc);}}
.ubar{{width:64px;height:3px;background:var(--acc);margin-top:18px;}}
h1{{font-family:var(--display);text-transform:uppercase;line-height:.92;font-size:96px;
  letter-spacing:-.01em;margin-top:20px;}}
.stroke{{color:transparent;-webkit-text-stroke:2.5px var(--ink);}}
.tag{{font-size:27px;line-height:1.4;color:var(--dim);max-width:640px;margin-top:24px;}}
.stats{{font-family:var(--mono);font-size:22px;color:var(--ink);margin-top:20px;
  letter-spacing:.02em;}}
.stats b{{color:var(--acc);font-weight:500;}}
.foot{{position:absolute;left:76px;bottom:44px;z-index:2;display:flex;gap:24px;
  align-items:center;font-family:var(--mono);font-size:20px;letter-spacing:.04em;}}
.foot .lnk{{color:var(--acc);}} .foot .br{{color:var(--faint);}}
</style></head><body>
<div class="strip"><div class="frame" style="top:150px"></div>
  <div class="frame" style="top:315px"></div><div class="frame" style="top:480px"></div></div>
<div class="wrap">
  <div class="kicker">Historia filmu animowanego · 1833 → dziś</div>
  <div class="ubar"></div>
  <h1>Historia<br><span class="stroke">Animacji</span></h1>
  <div class="tag">Cała światowa historia animacji — od zabawek optycznych po Pixara.</div>
  <div class="stats"><b>430</b> filmów · <b>231</b> twórców · <b>30</b> rozdziałów</div>
</div>
<div class="foot"><span class="lnk">{LINK}</span></div>
</body></html>"""

tmp = os.path.join(tempfile.gettempdir(), "ha_banner.html")
with open(tmp, "w", encoding="utf-8") as f:
    f.write(HTML)
out = os.path.join(OUT, "banner.png")
subprocess.run([CHROME, "--headless", f"--screenshot={out}",
                "--window-size=1200,630", "--force-device-scale-factor=2",
                "--hide-scrollbars", "--virtual-time-budget=3200", f"file://{tmp}"],
               check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print("✓ banner.png (1200×630 @2x) →", out)
