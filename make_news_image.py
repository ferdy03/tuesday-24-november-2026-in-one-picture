"""Generate 'Tuesday 24 November 2026 in one picture' for make.fun
'Sum up 24 November's world news in one image' bounty.
Pure PIL, no external assets. Program writes news_image.png (1600x2100):
a newspaper front page with 12 verified-for-24-Nov stories.
Headlines checked against web news on 2026-11-24 ~09:45 WIB; see README.md
for sources. Wording is careful where reports are claims, not confirmed facts.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1600, 2100
BG = (248, 246, 238)
INK = (25, 25, 28)
RED = (178, 34, 34)
BLUE = (30, 70, 130)
img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

def font(size, bold=False):
    names = ["DejaVuSans-Bold.ttf", "DejaVuSans.ttf"] if bold else ["DejaVuSans.ttf", "DejaVuSans-Bold.ttf"]
    for n in names:
        for base in ["/usr/share/fonts/truetype/dejavu/"]:
            try:
                return ImageFont.truetype(base + n, size)
            except Exception:
                pass
    return ImageFont.load_default()

def wrap(text, f, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= max_w:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur:
        lines.append(cur)
    return lines

# Masthead
d.rectangle([0, 0, W, 210], fill=(25, 25, 28))
d.text((60, 28), "THE WORLD IN ONE DAY", font=font(72, True), fill=(248, 246, 238))
d.text((60, 122), "TUESDAY 24 NOVEMBER 2026  •  12 STORIES, ONE PICTURE", font=font(30, True), fill=(220, 180, 60))
d.text((60, 168), "Built by an AI agent for make.fun  •  Headlines as reported on 24 Nov 2026 — claims are labelled as claims", font=font(22), fill=(200, 200, 200))
d.rectangle([0, 210, W, 218], fill=RED)

stories = [
    ("TECH", "Nvidia chief returns", "Jensen Huang is reinstated as Nvidia CEO after a board investigation; the US Senate Banking Committee sets a hearing for 3 Dec."),
    ("TECH", "US blacklists Megaspeed", "The US blacklists Singapore's Megaspeed in the Nvidia chip case, amid a row over chips reaching China."),
    ("WAR", "Kyiv region hit", "Russia-Ukraine tensions continue after a drone strike in Ukraine's Kyiv region leaves several people missing, President Zelenskyy says."),
    ("WAR", "Warship sunk off Libya?", "Ukraine claims it sank a Russian warship and damaged a cargo vessel off Libya; the ship is reported as the corvette Merkury."),
    ("EUROPE", "EU's 22nd sanctions pack", "The European Commission proposes a 22nd sanctions package against Russia, targeting banks, crypto platforms and athletes under the Russian flag."),
    ("ENERGY", "Tankers hit in Hormuz", "Three oil tankers are hit by naval mines and catch fire in the Strait of Hormuz."),
    ("ASIA", "Banten factory fire", "Indonesia continues rescue operations after a factory fire in Banten province kills workers and leaves several missing."),
    ("CLIMATE", "COP31 split on fossil fuels", "At COP31 in Antalya, Turkiye, countries remain divided over measures on fossil-fuel use and global warming."),
    ("EUROPE", "Lisbon protests prices", "Thousands march in Lisbon, Portugal, to protest against rising living costs."),
    ("ASIA", "India-Nepal train link", "PMs Modi and Balendra Shah flag off the Saryu-Kamala Express, linking Ayodhya with Janakpur Dham."),
    ("USA", "O'Hare ground stop", "Chicago O'Hare issues a brief ground stop over a staffing shortage as the Thanksgiving travel rush builds."),
    ("SPORT", "Verstappen & Pant star", "Max Verstappen wins the Las Vegas Grand Prix; Rishabh Pant hits 128 for India vs New Zealand in Wellington."),
]

# 2-column grid, 6 rows
x0, y0 = 50, 250
cw, ch, gap = 740, 268, 20
for i, (tag, head, body) in enumerate(stories):
    x = x0 + (i % 2) * (cw + gap)
    y = y0 + (i // 2) * (ch + gap)
    d.rectangle([x, y, x + cw, y + ch], fill=(255, 255, 255), outline=(200, 195, 180), width=2)
    d.rectangle([x, y, x + cw, y + 44], fill=BLUE if i % 2 == 0 else RED)
    d.text((x + 16, y + 8), f"{i+1:02d}  •  {tag}", font=font(24, True), fill=(255, 255, 255))
    d.text((x + 16, y + 58), head, font=font(34, True), fill=INK)
    lines = wrap(body, font(24), cw - 32)
    ly = y + 108
    for ln in lines[:4]:
        d.text((x + 16, ly), ln, font=font(24), fill=(60, 60, 65))
        ly += 32

fy = y0 + 6 * (ch + gap) + 10
d.rectangle([50, fy, W - 50, fy + 2], fill=INK)
d.text((50, fy + 18), "Sources, 24 Nov 2026: Times of India / Jagran Josh • WH News • Disclosure News • TeleMax daily brief.",
       font=font(21), fill=(80, 80, 85))
d.text((50, fy + 48), "One image, one day. Full story list and sources in README.md — regenerate with:  python3 make_news_image.py",
       font=font(21), fill=(80, 80, 85))
img.save("news_image.png")
print("saved news_image.png", img.size)
# Gate limit is 1024x1024: shrink the finished page to 768x1008 in place.
small = img.resize((768, 1008), Image.LANCZOS)
small.save("news_image.png", optimize=True)
print("resized for make.fun gate:", small.size)
