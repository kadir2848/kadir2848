"""Long Horizon: original, scriptless profile media.
Requires Python 3 and Playwright with Chromium. Run: python scripts/render_hero.py
The animation is an eight-second periodic loop; essential text never disappears.
"""
from pathlib import Path
import html
OUT=Path(__file__).resolve().parents[1]/'assets'
PHRASES=['Think from first principles.','Build with conviction.','Stay useful.','Play the long game.']
PALETTES={
'dark':dict(bg='#10151c',fg='#f0eee9',muted='#a7b0ba',accent='#d8b98a',line='#66788c',haze='#7a91b0'),
'light':dict(bg='#f5f3ee',fg='#1c2b3b',muted='#4e6072',accent='#81592e',line='#8c9fb0',haze='#b6c6d5')}
def text(x,y,s,size=24,fill='fg',family='sans',extra='',c=None):
 return f'<text x="{x}" y="{y}" fill="{c.get(fill,fill)}" font-size="{size}" font-family="{("Arial,Helvetica,sans-serif" if family=="sans" else "Georgia,serif")}" {extra}>{html.escape(s)}</text>'
def svg(theme,mobile=False,static=False):
 c=PALETTES[theme];w,h=(720,940) if mobile else (1440,760)
 glow=.30 if theme=='dark' else .12;gold=.21 if theme=='dark' else .07
 css='''@keyframes drift{0%,100%{transform:translate(0,0)}50%{transform:translate(8px,-7px)}}
@keyframes breath{0%,100%{opacity:.28}50%{opacity:.65}}
@keyframes thought{0%,100%{opacity:.18}50%{opacity:.9}}
@keyframes emphasis{0%,100%{opacity:0}12%,24%{opacity:1}38%,85%{opacity:0}}
.drift{animation:drift 8s ease-in-out infinite}.breath{animation:breath 8s ease-in-out infinite}.thought{animation:thought 8s ease-in-out infinite}.emphasis{animation:emphasis 8s ease-in-out infinite;opacity:0}
@media(prefers-reduced-motion:reduce){*{animation:none!important}.emphasis{opacity:0}}'''
 if static:css+='*{animation:none!important}.emphasis{opacity:0}'
 parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">Kadir Can Girenitlioğlu — Long Horizon</title><desc id="desc">'+html.escape(' '.join(PHRASES))+'</desc>',f'<style>{css}</style>',f'<defs><radialGradient id="haze"><stop stop-color="{c["haze"]}" stop-opacity="{glow}"/><stop offset="1" stop-color="{c["bg"]}" stop-opacity="0"/></radialGradient><radialGradient id="gold"><stop stop-color="{c["accent"]}" stop-opacity="{gold}"/><stop offset="1" stop-color="{c["bg"]}" stop-opacity="0"/></radialGradient></defs>',f'<rect width="{w}" height="{h}" fill="{c["bg"]}"/>']
 def t(*args,**kwargs):parts.append(text(*args,**kwargs,c=c))
 x=48 if mobile else 76
 if mobile:
  # Horizon beneath the typography: its own space, never under essential text.
  parts.append(f'<g class="drift"><ellipse cx="540" cy="785" rx="340" ry="155" fill="url(#haze)"/><path d="M90 856 Q390 630 778 792" fill="none" stroke="{c["line"]}" stroke-width="1.6" opacity=".5"/><path d="M90 868 Q390 642 778 804" fill="none" stroke="{c["line"]}" opacity=".12"/></g>')
  parts.append(f'<ellipse class="breath" cx="542" cy="758" rx="155" ry="30" fill="url(#gold)"/>')
  t(x,106,'KADIR CAN',56,extra='letter-spacing="1" font-weight="700"')
  t(x,170,'GIRENITLIOĞLU',57,extra='letter-spacing=".3" font-weight="700"')
  t(x,234,'Computer Engineering · Cybersecurity',37,fill='muted')
  t(x,274,'Software Engineering · Open Source',37,fill='muted')
  ys=[376,439,502,565]
  for i,y in enumerate(ys):
   t(x,y,PHRASES[i],39,fill=('accent' if static and i==3 else 'fg'),family='serif');t(x,y,PHRASES[i],39,fill='accent',family='serif',extra=f'class="emphasis" style="animation-delay:-{8-2*i}s"')
  t(x,654,'Curiosity. Discipline. Patience.',37,fill='muted')
  coords=[(460,751),(535,735),(613,723),(675,736)]
 else:
  parts.append(f'<g class="drift"><ellipse cx="1170" cy="420" rx="395" ry="305" fill="url(#haze)"/><path d="M736 581 Q1070 292 1470 514" fill="none" stroke="{c["line"]}" stroke-width="1.7" opacity=".52"/><path d="M736 593 Q1070 304 1470 526" fill="none" stroke="{c["line"]}" opacity=".12"/></g>')
  parts.append(f'<ellipse class="breath" cx="1150" cy="436" rx="230" ry="64" fill="url(#gold)"/>')
  t(x,116,'KADIR CAN',66,extra='letter-spacing="1.5" font-weight="700"')
  t(x,196,'GIRENITLIOĞLU',76,extra='letter-spacing=".3" font-weight="700"')
  t(x,256,'Computer Engineering · Cybersecurity',27,fill='muted')
  t(x,294,'Software Engineering · Open Source',27,fill='muted')
  for i,y in enumerate([398,460,522,584]):
   t(x,y,PHRASES[i],42,fill=('accent' if static and i==3 else 'fg'),family='serif');t(x,y,PHRASES[i],42,fill='accent',family='serif',extra=f'class="emphasis" style="animation-delay:-{8-2*i}s"')
  t(x,687,'Curiosity. Discipline. Patience.',25,fill='muted')
  coords=[(923,461),(1043,426),(1175,424),(1298,450)]
 for i,(cx,cy) in enumerate(coords):
  parts.append(f'<g class="thought" style="animation-delay:-{i*1.7}s"><circle cx="{cx}" cy="{cy}" r="3" fill="{c["accent"]}"/><circle cx="{cx}" cy="{cy}" r="9" fill="none" stroke="{c["accent"]}" stroke-width=".7" opacity=".35"/></g>')
 parts.append('</svg>');return '\n'.join(parts)
if __name__=='__main__':
 import tempfile
 from playwright.sync_api import sync_playwright
 OUT.mkdir(exist_ok=True)
 with sync_playwright() as p:
  browser=p.chromium.launch(headless=True)
  for theme in PALETTES:
   for mobile in [False,True]:
    stem='hero-'+('mobile-' if mobile else '')+theme
    (OUT/(stem+'.svg')).write_text(svg(theme,mobile))
    with tempfile.TemporaryDirectory() as folder:
     still=Path(folder)/'still.svg';still.write_text(svg(theme,mobile,True))
     page=browser.new_page(viewport={'width':720 if mobile else 1440,'height':940 if mobile else 760},device_scale_factor=1)
     page.goto(still.as_uri());page.screenshot(path=str(OUT/(stem+'.png')));page.close()
  browser.close()
 print('Rendered four original SVG animations and four intentional PNG stills.')
