"""Generate the shared BharatCalc Open Graph card (1200x630 PNG).
Run: python scripts/make_og.py  -> writes og/default.png
Pure-PIL, no external services. Brand palette per CLAUDE.md.
"""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W, H = 1200, 630

INK = (13, 17, 23)        # ink-900  #0d1117
INK_SOFT = (24, 30, 40)   # subtle panel
LEAF = (22, 163, 74)      # leaf-600 #16a34a
SAFFRON = (234, 88, 12)   # saffron-600 #ea580c
WHITE = (255, 255, 255)
MUTED = (148, 163, 184)   # slate-400

FONTS = "C:/Windows/Fonts"
def font(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)

f_sub   = font("segoeui.ttf", 42)
f_tag   = font("segoeuib.ttf", 30)

CONTENT_W = W - 220  # left/right margin of 110

def fit_font(text, ttf, start, max_w):
    """Largest size <= start at which `text` fits within max_w."""
    size = start
    while size > 24:
        fnt = font(ttf, size)
        if ImageDraw.Draw(Image.new("RGB", (1, 1))).textlength(text, font=fnt) <= max_w:
            return fnt
        size -= 2
    return font(ttf, 24)

img = Image.new("RGB", (W, H), INK)
d = ImageDraw.Draw(img)

# top + bottom accent bars (leaf -> saffron gradient)
def hbar(y0, y1):
    for x in range(W):
        t = x / W
        r = int(LEAF[0] + (SAFFRON[0]-LEAF[0]) * t)
        g = int(LEAF[1] + (SAFFRON[1]-LEAF[1]) * t)
        b = int(LEAF[2] + (SAFFRON[2]-LEAF[2]) * t)
        d.line([(x, y0), (x, y1)], fill=(r, g, b))
hbar(0, 12)
hbar(H-12, H)

# faint corner glow panel
d.rounded_rectangle([60, 70, W-60, H-70], radius=28, outline=INK_SOFT, width=2)

# logo
logo_path = os.path.join(ROOT, "logo.png")
logo = Image.open(logo_path).convert("RGBA")
lw = 150
lh = int(logo.height * lw / logo.width)
logo = logo.resize((lw, lh), Image.LANCZOS)
img.paste(logo, (110, 110), logo)

# wordmark next to logo
d.text((110 + lw + 28, 110 + (lh-70)//2), "BharatCalc", font=font("segoeuib.ttf", 70), fill=WHITE)

# main headline (auto-fit so it never overflows)
line1, line2 = "Free Online Calculators", "for India"
f_title = fit_font(line1, "segoeuib.ttf", 104, CONTENT_W)
lh_title = f_title.size + 16
d.text((110, 268), line1, font=f_title, fill=WHITE)
d.text((110, 268 + lh_title), line2, font=f_title, fill=LEAF)

# tagline pill row near bottom
tags = ["Finance", "Tax", "Health", "Math"]
x = 110
y = H - 96
for i, t in enumerate(tags):
    tw = d.textlength(t, font=f_tag)
    pad = 22
    col = SAFFRON if i % 2 else LEAF
    d.rounded_rectangle([x, y, x + tw + pad*2, y + 56], radius=28, fill=col)
    d.text((x + pad, y + 12), t, font=f_tag, fill=WHITE)
    x += tw + pad*2 + 18

# domain bottom-right
dom = "bharatcalc.online"
dw = d.textlength(dom, font=f_sub)
d.text((W - 110 - dw, H - 86), dom, font=f_sub, fill=MUTED)

os.makedirs(os.path.join(ROOT, "og"), exist_ok=True)
out = os.path.join(ROOT, "og", "default.png")
img.save(out, "PNG", optimize=True)
print("wrote", out, img.size, str(os.path.getsize(out)//1024) + "KB")
