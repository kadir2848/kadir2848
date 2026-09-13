"""Generate original, local profile artwork. Requires Pillow and a Unicode TTF font.
Usage: python scripts/render_hero.py --font FONT.ttf
"""
from pathlib import Path
import argparse,math
from PIL import Image,ImageDraw,ImageFont
parser=argparse.ArgumentParser();parser.add_argument('--font',required=True);args=parser.parse_args()
out=Path(__file__).resolve().parents[1]/'assets';out.mkdir(exist_ok=True)
W,H=1280,420
fonts={n:ImageFont.truetype(args.font,n) for n in [13,15,17,19,23,52]}
for theme in ['dark','light']:
 c={'bg':'#0b121a','panel':'#111e27','grid':'#172831','text':'#edf4f8','muted':'#9eb2c0','accent':'#87dfc0','line':'#2a404c'} if theme=='dark' else {'bg':'#f3f8fa','panel':'#e7f0f3','grid':'#dce8ed','text':'#142b37','muted':'#48616e','accent':'#14694f','line':'#b4cdd7'}
 base=Image.new('RGB',(W,H),c['bg']);d=ImageDraw.Draw(base)
 for x in range(780,W,32):d.line((x,0,x,H),fill=c['grid'])
 for y in range(0,H,32):d.line((780,y,W,y),fill=c['grid'])
 d.line((52,58,1228,58),fill=c['line'],width=1)
 d.text((52,26),'KCG  /  ENGINEERING NOTES',font=fonts[15],fill=c['muted'])
 d.text((1002,26),'SYSTEMS · OPEN SOURCE',font=fonts[13],fill=c['muted'])
 d.text((52,86),'Kadir Can Girenitlioğlu',font=fonts[52],fill=c['text'])
 d.text((54,160),'Computer Engineering  /  Cybersecurity',font=fonts[23],fill=c['accent'])
 d.text((54,197),'Software Engineering  /  Open Source',font=fonts[23],fill=c['text'])
 d.text((54,244),'Exploring systems. Building with AI. Contributing with evidence.',font=fonts[17],fill=c['muted'])
 # Abstract signal reducer motif; no activity counts or live status claims.
 for i,y in enumerate([103,128,153,178,203]):
  d.line((990,y,1020,y),fill=c['line'],width=2);d.line((1020,y,1071,153),fill=c['line'],width=2)
 d.rounded_rectangle((1071,132,1113,174),radius=9,fill=c['panel'],outline=c['accent'],width=2)
 d.line((1113,153,1190,153),fill=c['accent'],width=2);d.ellipse((1190,148,1200,158),fill=c['accent'])
 d.text((1035,224),'SIGNAL > NOISE',font=fonts[15],fill=c['muted'])
 d.rounded_rectangle((52,307,1228,381),radius=9,fill=c['panel'],outline=c['line'])
 d.text((75,330),'event.route',font=fonts[17],fill=c['muted'])
 centers=[365,550,735,920,1110];labels=['EVENT','REDUCE','DEDUPE','GATE','DECISION']
 for i,(cx,label) in enumerate(zip(centers,labels)):
  d.text((cx-35,331),label,font=fonts[15],fill=c['text'])
  if i<4:d.line((cx+57,342,centers[i+1]-55,342),fill=c['line'],width=2)
 d.text((54,395),'ILLUSTRATIVE FLOW · INDEPENDENT PROJECTS',font=fonts[13],fill=c['muted'])
 base.save(out/f'hero-{theme}.png',optimize=True)
 frames=[]
 for frame in range(50):
  im=base.copy();dr=ImageDraw.Draw(im)
  progress=min(frame/36,1)*4;idx=min(int(progress),4)
  if frame<40:
   x=centers[idx] if idx==4 else centers[idx]+(centers[idx+1]-centers[idx])*(progress-idx)
   dr.ellipse((x-4,365,x+4,373),fill=c['accent'])
   dr.line((centers[idx]-34,362,centers[idx]+40,362),fill=c['accent'],width=2)
  frames.append(im.quantize(colors=96))
 frames[0].save(out/f'hero-{theme}.gif',save_all=True,append_images=frames[1:],duration=120,loop=0,optimize=True,disposal=1)
 print(theme,(out/f'hero-{theme}.gif').stat().st_size,'bytes')
