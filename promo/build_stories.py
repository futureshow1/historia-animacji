#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HISTORIA ANIMACJI — plansze do Relacji FB/IG (Stories 1080x1920).
Estetyka 1:1 z portalem: ciepla czern #0f0e13, bursztyn #ffb320,
perforacja tasmy filmowej, skos -16 st., outline'owe numery klatek,
Archivo Black / Space Grotesk / IBM Plex Mono. Render: headless Chrome @2x.

Uruchom:  python3 build_stories.py   ->  story-1..10.png
"""
import os, subprocess, tempfile, html, sys

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
OUT = os.path.dirname(os.path.abspath(__file__))
LINK = "futureshow.pl/historia-animacji"
TOTAL = 10

# format: domyślnie story 1080x1920; "python3 build_stories.py square" -> 1080x1080 pod feed
SQ = 'square' in sys.argv
CANVAS_H = 1080 if SQ else 1920
PFX = 'square' if SQ else 'story'
SQ_CSS = ("html,body{height:1080px;}"
          ".stage{padding:84px 118px 92px;}"
          ".footer{bottom:40px;}"
          ".frow{padding:15px 2px;}"
          ".crow{padding:11px 2px;}"
          ".srow{padding:14px 2px;}"
          ".prow{padding:16px 4px;}")

CSS = r"""
:root{
  --bg:#0f0e13; --card:#16151c; --cardh:#1d1c25;
  --ink:#f3efe6; --dim:#b5b0a4; --faint:#6f6b63;
  --acc:#ffb320; --accd:#d18f0a; --line:#2a2833;
  --ondark:#17130a; --frag:#8a6d1f; --doc:#3d5a80;
  --display:'Archivo Black','Arial Black',sans-serif;
  --body:'Space Grotesk','Helvetica Neue',sans-serif;
  --mono:'IBM Plex Mono','Courier New',monospace;
}
*{margin:0;padding:0;box-sizing:border-box;}
html,body{width:1080px;height:1920px;}
body{background:var(--bg);color:var(--ink);font-family:var(--body);
  position:relative;overflow:hidden;-webkit-font-smoothing:antialiased;}
/* film-strip perforation (signature motif) */
.perf{position:absolute;top:0;bottom:0;right:56px;width:22px;z-index:1;
  background:repeating-linear-gradient(to bottom,transparent 0 10px,
  var(--line) 10px 26px,transparent 26px 36px);}
.perf.l{left:56px;right:auto;}
/* skewed amber splice (light-leak / film cut) */
.splice{position:absolute;right:196px;top:-60px;width:4px;height:1320px;
  background:var(--acc);opacity:.5;transform:skewX(-16deg);
  transform-origin:top;z-index:1;}
.stage{position:absolute;inset:0;z-index:2;display:flex;flex-direction:column;
  padding:128px 118px 150px;}
.grow{flex:1 1 auto;}

.kicker{font-family:var(--mono);font-size:25px;letter-spacing:.30em;
  text-transform:uppercase;color:var(--acc);}
.ubar{width:74px;height:4px;background:var(--acc);margin-top:22px;}
.display{font-family:var(--display);text-transform:uppercase;line-height:.92;
  font-size:128px;letter-spacing:-.01em;color:var(--ink);}
.stroke{color:transparent;-webkit-text-stroke:2.5px var(--ink);}
.statement{font-family:var(--body);font-weight:700;font-size:76px;
  line-height:1.08;letter-spacing:-.015em;color:var(--ink);}
.lede{font-weight:400;font-size:34px;line-height:1.5;color:var(--dim);}

.pill{display:inline-block;font-family:var(--mono);font-size:27px;
  letter-spacing:.03em;color:var(--ink);background:var(--card);
  border:1px solid var(--line);border-radius:8px;padding:15px 28px;}

/* stats */
.stat{display:flex;align-items:baseline;gap:34px;}
.bignum{font-family:var(--display);font-size:158px;color:var(--acc);line-height:1;}
.numlabel{font-family:var(--mono);font-size:31px;text-transform:uppercase;
  letter-spacing:.16em;color:var(--dim);}

/* film catalogue rows */
.frow{display:flex;align-items:center;gap:28px;padding:22px 2px;
  border-bottom:1px solid var(--line);}
.fidx{font-family:var(--display);font-size:38px;color:transparent;
  -webkit-text-stroke:1.5px var(--acc);flex:0 0 auto;width:74px;}
.fmeta{display:flex;flex-direction:column;gap:4px;}
.ftitle{font-weight:500;font-size:40px;color:var(--ink);line-height:1.1;}
.fdir{font-family:var(--mono);font-size:25px;color:var(--dim);letter-spacing:.02em;}
.fyear{margin-left:auto;font-family:var(--mono);font-size:32px;color:var(--acc);}
.badge{font-family:var(--mono);font-size:20px;color:var(--ondark);
  background:var(--acc);border-radius:4px;padding:3px 11px;margin-left:16px;
  letter-spacing:.06em;vertical-align:middle;}

/* source rows (canon) */
.srow{padding:20px 2px;border-bottom:1px solid var(--line);}
.sauth{font-weight:500;font-size:37px;color:var(--ink);}
.stitle{display:block;font-family:var(--mono);font-size:26px;color:var(--dim);
  margin-top:6px;letter-spacing:.01em;}

/* timeline */
.crow{display:flex;align-items:baseline;gap:34px;padding:19px 2px;
  border-bottom:1px solid var(--line);}
.tyear{font-family:var(--mono);font-size:34px;color:var(--acc);flex:0 0 auto;width:110px;}
.cname{font-weight:400;font-size:33px;color:var(--ink);}

/* feature play rows */
.prow{display:flex;align-items:center;gap:26px;padding:22px 4px;
  border-bottom:1px solid var(--line);}
.ptri{flex:0 0 auto;width:58px;height:58px;border-radius:50%;background:var(--acc);
  color:var(--ondark);display:flex;align-items:center;justify-content:center;
  font-size:26px;padding-left:4px;}
.ptitle{font-weight:500;font-size:42px;color:var(--ink);}
.pyear{margin-left:auto;font-family:var(--mono);font-size:30px;color:var(--acc);}
.ctapill{display:inline-block;font-family:var(--body);font-weight:700;font-size:40px;
  background:var(--acc);color:var(--ondark);border-radius:8px;padding:22px 44px;}

.linktext{font-family:var(--mono);font-size:29px;letter-spacing:.01em;
  color:var(--acc);line-height:1.4;max-width:940px;word-break:break-word;}
.brand{font-family:var(--mono);font-size:27px;letter-spacing:.06em;color:var(--faint);}

.footer{position:absolute;left:118px;right:118px;bottom:60px;display:flex;
  justify-content:space-between;font-family:var(--mono);font-size:23px;
  letter-spacing:.06em;color:var(--faint);z-index:3;}
"""

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
 '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
 '<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&'
 'family=Space+Grotesk:wght@300;400;500;700&family=IBM+Plex+Mono:wght@400;500&'
 'display=swap" rel="stylesheet">')


def esc(s):
    return html.escape(s)


def frow(idx, title, director, year, badge=None):
    b = f'<span class="badge">{badge}</span>' if badge else ''
    return (f'<div class="frow"><span class="fidx">{idx}</span>'
            f'<div class="fmeta"><div class="ftitle">{esc(title)}{b}</div>'
            f'<div class="fdir">{esc(director)}</div></div>'
            f'<span class="fyear">{year}</span></div>')


def frame(inner, page, splice=False, perf_left=False):
    sp = '<div class="splice"></div>' if splice else ''
    pf = '<div class="perf l"></div>' if perf_left else '<div class="perf"></div>'
    sq = f'<style>{SQ_CSS}</style>' if SQ else ''
    return (f'<!doctype html><html lang="pl"><head><meta charset="utf-8">{FONTS}'
            f'<style>{CSS}</style>{sq}</head><body>{pf}{sp}'
            f'<div class="stage">{inner}</div>'
            f'<div class="footer"><span>{page:02d} / {TOTAL}</span>'
            f'<span>historia animacji</span></div></body></html>')


def kick(text):
    return f'<div class="kicker">{text}</div><div class="ubar"></div>'


# ---------------------------------------------------------------------- slajdy
def s_cover():
    return (kick('Historia filmu animowanego · 1833 → dziś')
            + '<div class="grow"></div>'
            '<h1 class="display">Historia<br><span class="stroke">Animacji</span></h1>'
            '<div class="lede" style="margin-top:36px;max-width:840px">'
            'Światowa historia animacji w filmach z YouTube — od zabawek optycznych '
            'po pokolenie internetu. Kliknij kartę, aby obejrzeć.</div>'
            '<div style="margin-top:44px;display:flex;gap:16px;flex-wrap:wrap">'
            '<span class="pill">430 filmów</span><span class="pill">231 twórców</span>'
            '<span class="pill">30 rozdziałów</span></div>')

def s_hook():
    return (kick('Zacznijmy od zaskoczenia')
            + '<div class="grow"></div>'
            '<div class="statement" style="max-width:920px">'
            'Animacja jest starsza niż&nbsp;kino.</div>'
            '<div class="lede" style="margin-top:32px;max-width:840px">'
            'Fenakistiskop Josepha Plateau ożywił rysunek w 1833 roku — '
            '62 lata przed pierwszym seansem braci Lumière.</div>'
            '<div class="grow"></div>')

def s_stats():
    rows = [('430', 'filmów'), ('231', 'twórców'), ('30', 'rozdziałów')]
    body = ''.join(f'<div class="stat"><span class="bignum">{n}</span>'
                   f'<span class="numlabel">{l}</span></div>' for n, l in rows)
    return (kick('Cała historia w jednym miejscu')
            + '<div class="grow"></div>'
            f'<div style="display:flex;flex-direction:column;gap:34px">{body}</div>'
            '<div class="lede" style="margin-top:54px">Od 1833 do dziś. Filmy pełne, '
            'fragmenty i dokumenty — wszystkie oglądasz na miejscu.</div>'
            '<div class="grow"></div>')

def s_canon():
    src = [('Giannalberto Bendazzi', 'Animation: A World History'),
           ('Maureen Furniss', 'A New History of Animation'),
           ('Paweł Sitkiewicz', 'Polska szkoła animacji'),
           ('Marcin Giżycki', 'Nie tylko Disney')]
    rows = ''.join(f'<div class="srow"><span class="sauth">{esc(a)}</span>'
                   f'<span class="stitle">{esc(t)}</span></div>' for a, t in src)
    return (kick('Metoda')
            + '<div class="statement" style="font-size:60px;margin-top:24px">'
            'Ułożone według kanonu.</div>'
            f'<div style="margin-top:40px">{rows}</div>'
            '<div class="lede" style="margin-top:34px">Nie playlista z przypadku — '
            'układ 30 rozdziałów oparty na literaturze przedmiotu.</div>')

def s_pioneers():
    rows = (frow('01', 'Fenakistiskop', 'Joseph Plateau', '1833')
            + frow('02', 'Fantasmagorie', 'Émile Cohl', '1908')
            + frow('03', 'Gertie the Dinosaur', 'Winsor McCay', '1914')
            + frow('04', 'Prinz Achmed', 'Lotte Reiniger', '1926')
            + frow('05', 'Steamboat Willie', 'Disney / Ub Iwerks', '1928'))
    return (kick('Pionierzy')
            + '<div class="statement" style="font-size:58px;margin-top:22px">'
            'Zanim animacja miała dźwięk.</div>'
            f'<div style="margin-top:40px">{rows}</div>')

def s_masters():
    rows = (frow('01', 'Neighbours', 'Norman McLaren', '1952')
            + frow('02', 'Surogat', 'Dušan Vukotić', '1961')
            + frow('03', 'Jeżyk we mgle', 'Jurij Norstein', '1975')
            + frow('04', 'Możliwości dialogu', 'Jan Švankmajer', '1982')
            + frow('05', 'Luxo Jr.', 'John Lasseter / Pixar', '1986')
            + frow('06', 'Spirited Away', 'Hayao Miyazaki', '2001'))
    return (kick('Mistrzowie świata')
            + '<div class="statement" style="font-size:58px;margin-top:22px">'
            'Kanon w pięciu minutach.</div>'
            f'<div style="margin-top:36px">{rows}</div>')

def s_polska():
    rows = (frow('01', 'Zemsta operatora', 'Władysław Starewicz', '1912')
            + frow('02', 'Dom', 'Lenica / Borowczyk', '1958')
            + frow('03', 'Labirynt', 'Jan Lenica', '1962')
            + frow('04', 'Koń', 'Witold Giersz', '1967')
            + frow('05', 'Tango', 'Zbigniew Rybczyński', '1980', badge='Oscar')
            + frow('06', 'Katedra', 'Tomasz Bagiński', '2002', badge='nominacja'))
    return (kick('Polska w środku historii')
            + '<div class="statement" style="font-size:56px;margin-top:22px">'
            'Polska szkoła to światowa liga.</div>'
            f'<div style="margin-top:36px">{rows}</div>')

def s_timeline():
    tl = [('1833', 'Zabawki optyczne — prehistoria ruchu'),
          ('1908', 'Émile Cohl i pierwsi rysownicy'),
          ('1928', 'Disney i narodziny dźwięku'),
          ('1948', 'UPA — graficzna rewolucja'),
          ('1952', 'Norman McLaren i NFB'),
          ('1958', 'Polska szkoła animacji'),
          ('1975', 'Jurij Norstein'),
          ('1982', 'Jan Švankmajer'),
          ('1986', 'Pixar i narodziny CGI'),
          ('2005', 'Pokolenie internetu')]
    rows = ''.join(f'<div class="crow"><span class="tyear">{y}</span>'
                   f'<span class="cname">{esc(t)}</span></div>' for y, t in tl)
    return (kick('Kanon w 30 rozdziałach')
            + '<div class="statement" style="font-size:58px;margin-top:20px">'
            'Cała oś czasu.</div>'
            f'<div style="margin-top:34px">{rows}</div>')

def s_feature():
    rows = [('Gertie the Dinosaur', '1914'), ('Neighbours', '1952'),
            ('Tango', '1980'), ('Spirited Away', '2001')]
    pl = ''.join(f'<div class="prow"><span class="ptri">▶</span>'
                 f'<span class="ptitle">{esc(t)}</span>'
                 f'<span class="pyear">{y}</span></div>' for t, y in rows)
    return (kick('Jak to działa')
            + '<div class="statement" style="font-size:58px;margin-top:24px;max-width:900px">'
            'Klikasz kartę — oglądasz film.</div>'
            f'<div style="margin-top:42px">{pl}</div>'
            '<div style="margin-top:44px"><span class="ctapill">▶ 430 filmów na miejscu</span></div>'
            '<div class="lede" style="margin-top:32px">Każda karta to film osadzony '
            'z YouTube — bez instalacji, bez zbierania danych.</div>')

def s_cta():
    return (kick('Zacznij od 1833 roku')
            + '<div class="grow"></div>'
            '<h2 class="display" style="font-size:132px">Oglądaj.</h2>'
            '<div style="margin-top:44px"><span class="ctapill">▶ Otwórz portal</span></div>'
            f'<div class="linktext" style="margin-top:30px">{LINK}</div>'
            '<div class="brand" style="margin-top:24px">FutureShow · Jan Lubicz-Przyłuski</div>'
            '<div class="grow"></div>')

# (builder, splice, perf_left)  — splice retired: the perforation carries the film motif
SLIDES = [
    (s_cover,    False, False),
    (s_hook,     False, True),
    (s_stats,    False, False),
    (s_canon,    False, True),
    (s_pioneers, False, False),
    (s_masters,  False, False),
    (s_polska,   False, False),
    (s_timeline, False, True),
    (s_feature,  False, False),
    (s_cta,      False, False),
]


def render():
    for i, (builder, splice, pl) in enumerate(SLIDES, start=1):
        page = frame(builder(), i, splice=splice, perf_left=pl)
        tmp = os.path.join(tempfile.gettempdir(), f"ha_{PFX}_{i}.html")
        with open(tmp, "w", encoding="utf-8") as f:
            f.write(page)
        out = os.path.join(OUT, f"{PFX}-{i}.png")
        subprocess.run([CHROME, "--headless", f"--screenshot={out}",
                        f"--window-size=1080,{CANVAS_H}", "--force-device-scale-factor=2",
                        "--hide-scrollbars", "--virtual-time-budget=3200",
                        f"file://{tmp}"], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"  ✓ {PFX}-{i}.png")


if __name__ == "__main__":
    print(f"Renderuję Historia animacji — format {PFX} ({TOTAL} plansz)…")
    render()
    print("Gotowe →", OUT)
