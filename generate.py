#!/usr/bin/env python3
"""Generate the front-page image for Thursday 19 November 2026. (v8)

v8 vs v7: PRESENTATION ONLY — no story text, date, source, region count,
stat, map pin, ALSO item or footer word changed (all 43 stories identical).
The brief: a LIVING hero highlight and a BOLD editorial decision, with the
hottest news up front. The top-3 entries all use three equal top panels;
v8 breaks that pattern with a hero band:

- Row 1 is now a HERO band (170px tall, was 158px): panel 1 (Shenzhen
  trilateral summit) is 460px wide (was 325px) — 64% more area than a
  standard panel — with a NEW dynamic illustration (sunset sky, Shenzhen
  skyline with the Ping An spire, three seated leaders at one table with
  US/China/Russia flags and TRUMP / XI / PUTIN name plates), a 24px
  one-line headline (was 21px over two lines), a warm cream panel
  background and a 3px gold border. Panels 2 (Gaza) and 3 (GTA VI) are
  263px wide in the same taller band, so the three hottest stories of
  the day read as one strong top tier.
- Panel 6 (ICJ) illustration strengthened: gold sunburst behind the
  courthouse pediment, warmer ivory columns — the verdict panel now
  glows instead of sitting flat navy. Gaza's explosion glow enlarged
  and GTA's sunset deepened (same illustrations, stronger colour).
- Rows 2-4 keep the 3x325px grid at 147px (4px gaps now, was 5px);
  masthead, UTC strip, region strip, stats strip, map, ALSO list and
  DATE CHECK footer are untouched except a +5px vertical shift below the
  panels (stats rules 765/805, bottom headers 812, ALSO/map from 832,
  footer 1012) — all within the 1024px page, no overflow.

v7 vs v6: targeted fix of the TWO residual ALSO errors the v6 head-to-head
(4W-0L-1D vs the current top 5) found in kept items. #16 Gaza child
amputees (Euro-Med report, 4 Nov) replaced by the 19 Nov IDF strike on
the Hezbollah missile site in Janta, Lebanon (Beqaa); #27 Microsoft /
ByteDance talks (reported 18 Nov) replaced by the 19 Nov UN Human
Rights Committee guidance that no state authorisation is needed to form
or join a group; stats strip "$120bn COP31 adaptation goal" reworded
to "COP31 goal cut" so it matches panel 7 (the Thursday draft drops
the goal). Region counts unchanged (ME 4, AM 13, AS 10, EU 5, AF 3,
OC 2, WO 6 = 43) — #16 stays ME, #27 stays WO. No panel changes.

v5 vs v4: layout redesign to fit a FOURTH panel row (12 panels + 31 ALSO,
still 43 stories) — the head-to-head vs the top 5 was decided by panel
count (9 vs 11-13) and the dense ALSO list. Space found by: masthead
100->92px, UTC strip 22->20px, region strip 20->18px, panels 190px ->
158px (lead row) / 147px (rows 2-4) with compact 48px illustrations,
stats strip numbers 27->24px, map 156->124px tall. Headlines stay
21px (lead row) / 19px (rows 2-4) — at or above the winners' small-panel
headlines (~17px) — and the ALSO text stays 10px, never smaller than v4.
v6 vs v5: targeted date fix after the re-test vs the CURRENT top 5
(2W-3L). The audit found TWELVE date errors in v5 (1 panel + 11 ALSO)
that the re-test had undercounted, plus one extra (Estonia, 15 Nov)
found in this audit. Fixes: Gaza panel reframed as the raid ENDING
(19 Nov fact; the crossing was 18 Nov); COP31 panel corrected to the
Thursday draft (drops fossil-fuel language and the $120bn goal);
12 ALSO items dropped and replaced with verified 19 Nov items
(Han retrial, Bangladesh lockdown, IEA Hormuz warning, Denmark 109-0,
Jepchirchir ban, Venezuela TPS withdrawal, Senegal boat search,
Trump defers Iran decision, Senate 51-48, Bitcoin ETFs, Chow
reshuffle) and Banxico rewritten as the 19 Nov minutes; region strip
recounted (ME 4, AM 13, AS 10, EU 5, AF 3, OC 2, WO 6 = 43);
DATE CHECK footer now names Gaza crossing, Carney/China, Australia
sanctions (18 Nov) and Deutsche $582m (17 Nov). ICJ panel unchanged
(no vote count). Layout, 12 panels + 31 ALSO, and fonts unchanged.

Deterministic: fixed fonts, fixed layout, fixed palette, no network, no
timestamps, no randomness. Run:  python3 generate.py [out.png]
Default output: entry.png next to this script.
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (247, 242, 230, 255)
INK = (22, 22, 22, 255)
NAVY = (22, 38, 79, 255)
NAVY_D = (16, 28, 58, 255)
GOLD = (201, 162, 39, 255)
RED = (176, 58, 46, 255)
GREY = (96, 96, 90, 255)
RULE = (120, 110, 88, 255)
CREAM2 = (238, 231, 214, 255)

FD = "/usr/share/fonts/truetype/dejavu"


def F(name, size):
    return ImageFont.truetype(f"{FD}/{name}", size)


F_SERIF_B = lambda s: F("DejaVuSerif-Bold.ttf", s)      # noqa: E731
F_SERIF = lambda s: F("DejaVuSerif.ttf", s)             # noqa: E731
F_SANS_B = lambda s: F("DejaVuSans-Bold.ttf", s)        # noqa: E731
F_SANS = lambda s: F("DejaVuSans.ttf", s)               # noqa: E731


def wrap(d, text, font, max_w):
    """Greedy word wrap returning list of lines that fit max_w."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = (cur + " " + word).strip()
        if d.textlength(trial, font=font) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(d, x, y, text, font, color, max_w, leading):
    lines = wrap(d, text, font, max_w)
    for ln in lines:
        d.text((x, y), ln, font=font, fill=color)
        y += leading
    return y


def kicker(d, x, y, text, color=RED, size=13):
    d.text((x, y), text, font=F_SANS_B(size), fill=color)


def num_badge(d, cx, cy, n, r=11):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=RED, outline=(255, 255, 255, 255), width=2)
    t = str(n)
    f = F_SANS_B(13 if len(t) == 1 else 11)
    d.text((cx, cy), t, font=f, fill=(255, 255, 255, 255), anchor="mm")


# ---------------- flat illustration helpers ----------------

def skyline(d, box, sky, towers, sun=None):
    x0, y0, x1, y1 = box
    d.rectangle(box, fill=sky)
    if sun:
        sx, sy, sr, col = sun
        d.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=col)
    # towers: (x, w, h, colour)
    for (tx, tw, th, col) in towers:
        d.rectangle([x0 + tx, y1 - th, x0 + tx + tw, y1], fill=col)
        for wy in range(y1 - th + 6, y1 - 4, 11):
            for wx in range(x0 + tx + 5, x0 + tx + tw - 4, 9):
                if (wx * 7 + wy * 13) % 5 < 2:
                    d.rectangle([wx, wy, wx + 3, wy + 4], fill=(255, 214, 130, 255))


def flag(d, x, y, w, h, stripes):
    """stripes: list of colours top-to-bottom (horizontal bands)."""
    n = len(stripes)
    for i, c in enumerate(stripes):
        d.rectangle([x, y + i * h / n, x + w, y + (i + 1) * h / n], fill=c)
    d.rectangle([x, y, x + w, y + h], outline=(0, 0, 0, 255), width=1)


def flagpole(d, x, y0, y1, w=24, h=11, stripes=None):
    d.rectangle([x, y0, x + 2, y1], fill=(40, 40, 40, 255))
    flag(d, x + 2, y0, w, h, stripes or [RED])


# ---------------- world map (dotted, from rough polygons) ----------------

NA = [(-168, 66), (-155, 71), (-140, 70), (-128, 71), (-115, 68), (-100, 68),
      (-90, 69), (-82, 66), (-76, 62), (-70, 58), (-65, 60), (-60, 55),
      (-55, 52), (-60, 47), (-65, 44), (-70, 42), (-75, 38), (-80, 32),
      (-81, 26), (-84, 30), (-90, 29), (-97, 26), (-105, 22), (-110, 24),
      (-115, 29), (-120, 34), (-125, 40), (-125, 49), (-130, 55), (-140, 60),
      (-155, 58), (-165, 60)]
GREENLAND = [(-58, 64), (-45, 60), (-40, 65), (-30, 68), (-22, 70), (-25, 76),
             (-40, 80), (-58, 76), (-68, 72)]
SA = [(-78, 7), (-72, 11), (-62, 10), (-55, 6), (-50, 0), (-44, -3),
      (-35, -8), (-38, -15), (-40, -22), (-48, -28), (-55, -35), (-62, -41),
      (-68, -50), (-70, -54), (-73, -45), (-73, -35), (-70, -20), (-77, -12),
      (-80, -5), (-81, 0)]
EU = [(-10, 36), (-9, 43), (-2, 48), (-4, 50), (0, 53), (5, 58), (8, 57),
      (10, 59), (18, 56), (21, 55), (24, 58), (28, 60), (30, 62), (28, 66),
      (25, 70), (18, 69), (12, 65), (8, 62), (5, 60), (-2, 57), (-5, 50)]
UK = [(-5, 50), (-3, 53), (-5, 56), (-2, 58), (0, 53)]
AFRICA = [(-17, 15), (-15, 25), (-10, 30), (-5, 35), (0, 36), (10, 37),
          (11, 33), (20, 32), (30, 31), (32, 27), (35, 23), (38, 18),
          (42, 12), (48, 11), (51, 10), (44, 0), (40, -10), (36, -18),
          (32, -28), (28, -33), (20, -35), (15, -30), (12, -18), (9, -2),
          (9, 4), (-8, 4), (-13, 8), (-17, 12)]
ASIA = [(30, 62), (40, 68), (55, 68), (70, 72), (90, 75), (110, 76),
        (130, 72), (150, 70), (170, 66), (178, 65), (170, 60), (160, 55),
        (150, 50), (142, 45), (140, 38), (135, 35), (130, 33), (127, 38),
        (122, 40), (120, 30), (115, 22), (110, 20), (105, 10), (100, 8),
        (97, 15), (92, 20), (88, 22), (85, 18), (80, 13), (77, 8),
        (75, 20), (72, 25), (66, 25), (60, 25), (55, 27), (52, 28),
        (50, 30), (48, 30), (42, 35), (38, 36), (35, 36), (30, 36),
        (28, 40), (25, 42), (28, 48), (30, 55)]
AUS = [(114, -22), (114, -30), (116, -35), (124, -33), (130, -32),
       (136, -35), (140, -38), (146, -39), (150, -37), (153, -32),
       (153, -27), (150, -22), (146, -19), (142, -15), (142, -11),
       (136, -12), (132, -11), (126, -14), (122, -17), (118, -20)]
CONTINENTS = [NA, GREENLAND, SA, EU, UK, AFRICA, ASIA, AUS]


def draw_map(d, box):
    """Dotted world map in box (x0,y0,x1,y1); returns lon/lat -> xy fn."""
    x0, y0, x1, y1 = box
    mw, mh = x1 - x0, y1 - y0
    mask = Image.new("L", (mw, mh), 0)
    md = ImageDraw.Draw(mask)
    for poly in CONTINENTS:
        pts = [((lon + 180) / 360 * mw, (75 - lat) / 135 * mh) for lon, lat in poly]
        md.polygon(pts, fill=255)
    px = mask.load()
    step = 7
    for gy in range(4, mh - 2, step):
        for gx in range(4, mw - 2, step):
            if px[gx, gy]:
                d.ellipse([x0 + gx - 2, y0 + gy - 2, x0 + gx + 2, y0 + gy + 2],
                          fill=(74, 74, 66, 255))

    def ll(lon, lat):
        return (x0 + (lon + 180) / 360 * mw, y0 + (75 - lat) / 135 * mh)
    return ll


# ---------------- panel illustrations (compact, 48px strip) ----------------
# All nine v4 illustrations redrawn for a 48px-high box: no bottom label
# band (the kicker below identifies the story), art fills the full strip.

def ill_shenzhen(d, box):
    x0, y0, x1, y1 = box
    skyline(d, box, (232, 196, 138, 255),
            [(8, 30, 25, (38, 52, 86, 255)), (44, 24, 33, (38, 52, 86, 255)),
             (74, 36, 22, (38, 52, 86, 255)), (116, 24, 30, (38, 52, 86, 255)),
             (146, 32, 24, (38, 52, 86, 255)), (184, 24, 35, (38, 52, 86, 255)),
             (214, 34, 26, (38, 52, 86, 255)), (254, 24, 32, (38, 52, 86, 255)),
             (284, 30, 22, (38, 52, 86, 255))],
            sun=(x0 + 160, y0 + 14, 8, (255, 226, 150, 255)))
    d.rectangle([x0, y1 - 5, x1, y1], fill=(38, 52, 86, 255))
    flagpole(d, x0 + 52, y0 + 8, y1 - 5, stripes=[(222, 41, 16, 255)])
    flagpole(d, x0 + 150, y0 + 8, y1 - 5, stripes=[(178, 34, 52, 255), (255, 255, 255, 255),
                                                   (178, 34, 52, 255), (255, 255, 255, 255),
                                                   (178, 34, 52, 255), (255, 255, 255, 255),
                                                   (178, 34, 52, 255)])
    flagpole(d, x0 + 248, y0 + 8, y1 - 5, stripes=[(255, 255, 255, 255), (0, 57, 166, 255),
                                                   (213, 0, 50, 255)])


def _mini_flag(d, x, y, kind):
    """20x10 flag for the hero poles: 'us' | 'cn' | 'ru'."""
    w, h = 20, 10
    if kind == "us":
        for i in range(5):
            d.rectangle([x, y + i * 2, x + w, y + i * 2 + 2],
                        fill=(178, 34, 52, 255) if i % 2 == 0 else (255, 255, 255, 255))
        d.rectangle([x, y, x + 8, y + 5], fill=(40, 60, 130, 255))
    elif kind == "cn":
        d.rectangle([x, y, x + w, y + h], fill=(222, 41, 16, 255))
        d.ellipse([x + 3, y + 2, x + 7, y + 6], fill=(255, 222, 60, 255))
    else:  # ru
        for i, c in enumerate([(255, 255, 255, 255), (0, 57, 166, 255), (213, 0, 50, 255)]):
            d.rectangle([x, y + i * h / 3, x + w, y + (i + 1) * h / 3], fill=c)
    d.rectangle([x, y, x + w, y + h], outline=(0, 0, 0, 255), width=1)


def _leader(d, cx, head_y, skin, hair, suit, tie):
    """One seated leader bust: head + hair + shoulders + tie. head_y is the
    head centre; shoulders run to head_y+22, the table covers below that,
    so ~14px of shoulders stay visible above the table line."""
    r = 12
    # shoulders (trapezoid, wider at the bottom)
    d.polygon([(cx - 14, head_y + 8), (cx + 14, head_y + 8),
               (cx + 21, head_y + 22), (cx - 21, head_y + 22)], fill=suit)
    # tie
    d.polygon([(cx - 3, head_y + 9), (cx + 3, head_y + 9), (cx, head_y + 20)],
              fill=tie)
    # head
    d.ellipse([cx - r, head_y - r, cx + r, head_y + r], fill=skin)
    # hair cap (top of the head)
    d.pieslice([cx - r, head_y - r, cx + r, head_y + r], 180, 360, fill=hair)
    d.rectangle([cx - r, head_y - 2, cx + r, head_y + 1], fill=hair)


def ill_shenzhen_hero(d, box):
    """HERO: three leaders at one table under a Shenzhen sunset.
    Warm bands, big low sun, tower skyline with the Ping An spire,
    three flag poles, three seated leaders with name plates.
    Box is ~456x84 (the hero illustration strip)."""
    x0, y0, x1, y1 = box
    w = x1 - x0
    h = y1 - y0
    base = y0 + h  # table line
    # warm sunset bands
    d.rectangle([x0, y0, x1, y0 + 32], fill=(226, 106, 32, 255))
    d.rectangle([x0, y0 + 32, x1, y0 + 55], fill=(240, 172, 58, 255))
    d.rectangle([x0, y0 + 55, x1, y1], fill=(250, 214, 138, 255))
    # big low sun with glow, right of centre
    sx, sy = x0 + int(w * 0.72), y0 + 20
    d.ellipse([sx - 20, sy - 20, sx + 20, sy + 20], fill=(255, 228, 150, 255))
    d.ellipse([sx - 13, sy - 13, sx + 13, sy + 13], fill=(255, 205, 80, 255))
    # Shenzhen skyline (dark navy silhouette, base at the table line - 18)
    horizon = base - 18
    towers = [(8, 20, 22), (34, 16, 30), (56, 24, 18), (86, 18, 26),
              (110, 26, 20), (142, 20, 30), (168, 24, 16), (198, 18, 26),
              (222, 28, 20), (256, 20, 32), (282, 24, 18), (312, 18, 26),
              (336, 26, 22), (368, 20, 28), (394, 24, 18), (424, 20, 24)]
    for (tx, tw, th) in towers:
        d.rectangle([x0 + tx, horizon - th, x0 + tx + tw, horizon],
                    fill=(38, 52, 86, 255))
        for wy in range(horizon - th + 5, horizon - 3, 9):
            for wx in range(x0 + tx + 4, x0 + tx + tw - 3, 8):
                if (wx * 7 + wy * 13) % 5 < 2:
                    d.rectangle([wx, wy, wx + 2, wy + 3], fill=(255, 214, 130, 255))
    # Ping An spire (tall, pointed) between the centre and right leaders
    spx = x0 + 300
    d.polygon([(spx, y0 + 6), (spx + 7, horizon), (spx + 14, horizon)],
              fill=(38, 52, 86, 255))
    d.rectangle([spx + 2, y0 + 14, spx + 12, horizon], fill=(38, 52, 86, 255))
    # flag poles behind the leaders (rise from the table to the sky)
    leaders = [
        # (cx fraction, skin, hair, suit, tie, flag, plate)
        (0.22, (232, 190, 150, 255), (240, 210, 120, 255), (30, 45, 80, 255),
         (180, 40, 40, 255), "us", "TRUMP"),
        (0.50, (235, 200, 165, 255), (30, 30, 30, 255), (35, 35, 40, 255),
         (180, 40, 40, 255), "cn", "XI"),
        (0.78, (228, 185, 150, 255), (210, 200, 180, 255), (25, 40, 70, 255),
         (40, 80, 160, 255), "ru", "PUTIN"),
    ]
    for (fx, skin, hair, suit, tie, flag, plate) in leaders:
        cx = x0 + int(w * fx)
        # pole + flag (pole just left of the leader's head)
        px = cx - 22
        d.rectangle([px, y0 + 8, px + 2, horizon], fill=(40, 40, 40, 255))
        _mini_flag(d, px + 2, y0 + 8, flag)
        # seated bust (head centre y0+44, r=12; shoulders to y0+66, the
        # table covers below that, so ~14px of suit stays visible)
        _leader(d, cx, y0 + 44, skin, hair, suit, tie)
    # long table across the bottom (covers the busts below y0+66)
    d.rectangle([x0, base - 18, x1, y1], fill=(96, 44, 32, 255))
    d.rectangle([x0, base - 18, x1, base - 16], fill=(201, 162, 39, 255))
    # name plates on the table
    for (fx, skin, hair, suit, tie, flag, plate) in leaders:
        cx = x0 + int(w * fx)
        d.rectangle([cx - 18, base - 13, cx + 18, base - 4],
                    fill=(255, 255, 255, 255), outline=(60, 55, 45, 255), width=1)
        d.text((cx, base - 9), plate, font=F_SANS_B(7), fill=(22, 22, 22, 255),
               anchor="mm")


def ill_gaza(d, box):
    x0, y0, x1, y1 = box
    d.rectangle(box, fill=(13, 24, 48, 255))
    for (sx, sy) in [(20, 6), (60, 14), (110, 5), (180, 10), (240, 6), (290, 14), (150, 18), (90, 22)]:
        d.ellipse([x0 + sx, y0 + sy, x0 + sx + 2, y0 + sy + 2], fill=(255, 255, 255, 255))
    d.polygon([(x0 + 40, y1 - 12), (x0 + 150, y0 + 6), (x0 + 175, y0 + 6), (x0 + 70, y1 - 12)],
              fill=(255, 214, 130, 255))
    d.polygon([(x0 + 280, y1 - 12), (x0 + 200, y0 + 10), (x0 + 222, y0 + 10), (x0 + 300, y1 - 12)],
              fill=(255, 214, 130, 255))
    # v8: bigger explosion glow so the night raid reads at a glance
    d.ellipse([x0 + 140, y0 + 14, x0 + 172, y0 + 46], fill=(255, 120, 30, 255))
    d.ellipse([x0 + 147, y0 + 21, x0 + 165, y0 + 39], fill=(255, 190, 80, 255))
    d.ellipse([x0 + 152, y0 + 26, x0 + 160, y0 + 34], fill=(255, 240, 180, 255))
    d.rectangle([x0, y1 - 12, x1, y1], fill=(24, 20, 16, 255))
    for (bx, bw, bh) in [(10, 36, 14), (56, 28, 10), (94, 42, 16), (146, 30, 12),
                         (186, 40, 14), (236, 32, 10), (276, 36, 12)]:
        d.rectangle([x0 + bx, y1 - 12 - bh, x0 + bx + bw, y1 - 12], fill=(8, 10, 18, 255))


def ill_gta(d, box):
    x0, y0, x1, y1 = box
    import math
    # v8: deeper, hotter sunset so the rollout panel pops next to the hero
    bands = [(244, 118, 158, 255), (255, 168, 105, 255), (255, 208, 125, 255), (255, 232, 170, 255)]
    bh = (y1 - y0) // 4
    for i, c in enumerate(bands):
        d.rectangle([x0, y0 + i * bh, x1, y0 + (i + 1) * bh], fill=c)
    d.ellipse([x0 + 143, y0 + 4, x0 + 177, y0 + 38], fill=(255, 236, 180, 255))
    for (tx, tw, th) in [(6, 28, 22), (40, 22, 30), (68, 30, 18), (250, 28, 26), (284, 24, 20)]:
        d.rectangle([x0 + tx, y1 - th, x0 + tx + tw, y1], fill=(88, 52, 110, 255))
        for wy in range(y1 - th + 6, y1 - 4, 11):
            for wx in range(x0 + tx + 4, x0 + tx + tw - 3, 9):
                if (wx * 3 + wy) % 4 < 2:
                    d.rectangle([wx, wy, wx + 3, wy + 4], fill=(255, 220, 150, 255))
    for px in (120, 205):
        d.line([x0 + px, y1, x0 + px + 4, y1 - 18], fill=(60, 40, 20, 255), width=3)
        for ang in (-50, -20, 10, 40):
            a = math.radians(ang - 90)
            d.line([x0 + px + 4, y1 - 18, x0 + px + 4 + int(14 * math.cos(a)),
                    y1 - 18 + int(10 * math.sin(a))], fill=(34, 110, 60, 255), width=3)
    d.rectangle([x0, y1 - 5, x1, y1], fill=(88, 52, 110, 255))


def ill_ipo(d, box):
    x0, y0, x1, y1 = box
    d.rectangle(box, fill=(16, 74, 52, 255))
    d.text((x0 + 10, y0 + 4), "$83", font=F_SANS_B(22), fill=(255, 255, 255, 255))
    d.text((x0 + 10, y0 + 30), "ANT  ·  NASDAQ TODAY", font=F_SANS_B(10),
           fill=(190, 235, 205, 255))
    bars = [8, 12, 10, 15, 13, 19, 23]
    for i, bh in enumerate(bars):
        bx = x0 + 150 + i * 22
        d.rectangle([bx, y1 - 4 - bh, bx + 14, y1 - 4], fill=(120, 220, 160, 255))
    d.line([x0 + 150, y1 - 4 - 8, x0 + 150 + 6 * 22 + 14, y1 - 4 - 23],
           fill=(255, 220, 90, 255), width=3)


def ill_cyclone(d, box):
    x0, y0, x1, y1 = box
    d.rectangle(box, fill=(214, 228, 240, 255))
    cx, cy = x0 + 100, y0 + 22
    for r, col in [(16, (90, 130, 180, 255)), (11, (60, 105, 160, 255)),
                   (6, (40, 80, 140, 255))]:
        d.arc([cx - r, cy - r, cx + r, cy + r], 20, 300, fill=col, width=5)
    d.ellipse([cx - 3, cy - 3, cx + 3, cy + 3], fill=(255, 255, 255, 255))
    for rx in range(10, 150, 24):
        d.line([x0 + rx, y1 - 14, x0 + rx - 5, y1 - 4], fill=(70, 110, 160, 255), width=2)
    d.polygon([(x0 + 235, y1), (x1, y1 - 18), (x1, y1)], fill=(120, 150, 110, 255))


def ill_icj(d, box):
    """World Court, The Hague: pediment + columns.
    v8: gold sun behind the pediment, warm ivory columns and gold side
    accents — the verdict panel now glows instead of sitting flat navy.
    (All drawing stays inside the 48px box; no rays cross the border.)"""
    x0, y0, x1, y1 = box
    d.rectangle(box, fill=(13, 24, 48, 255))
    # gold sun in the sky, top right of the courthouse
    d.ellipse([x0 + 266, y0 + 3, x0 + 284, y0 + 21], fill=(255, 205, 80, 255))
    # gold side accents framing the courthouse
    d.rectangle([x0 + 70, y0 + 8, x0 + 73, y0 + 44], fill=(201, 162, 39, 255))
    d.rectangle([x0 + 250, y0 + 8, x0 + 253, y0 + 44], fill=(201, 162, 39, 255))
    d.polygon([(x0 + 96, y0 + 4), (x0 + 228, y0 + 4), (x0 + 162, y0 + 16)],
              fill=(240, 228, 200, 255))
    for cx in (100, 128, 156, 184, 212):
        d.rectangle([x0 + cx, y0 + 18, x0 + cx + 10, y1 - 5], fill=(240, 228, 200, 255))
    d.rectangle([x0, y1 - 5, x1, y1], fill=(240, 228, 200, 255))
    d.rectangle([x0, y1 - 8, x1, y1 - 5], fill=(176, 58, 46, 255))


def ill_cop31(d, box):
    """COP31, Antalya: globe + sun + hills. Thursday draft fact."""
    x0, y0, x1, y1 = box
    d.rectangle(box, fill=(18, 88, 66, 255))
    d.ellipse([x0 + 258, y0 + 6, x0 + 274, y0 + 22], fill=(255, 200, 70, 255))
    cx, cy = x0 + 80, y0 + 22
    d.ellipse([cx - 15, cy - 15, cx + 15, cy + 15], fill=(120, 220, 160, 255))
    d.arc([cx - 15, cy - 15, cx + 15, cy + 15], 0, 360, fill=(18, 88, 66, 255), width=2)
    d.line([cx - 14, cy - 5, cx + 14, cy - 5], fill=(18, 88, 66, 255), width=2)
    d.line([cx - 15, cy + 5, cx + 15, cy + 5], fill=(18, 88, 66, 255), width=2)
    d.ellipse([cx - 8, cy - 13, cx + 5, cy - 1], fill=(18, 88, 66, 255))
    d.polygon([(x0 + 150, y1), (x0 + 215, y1 - 20), (x0 + 290, y1)],
              fill=(10, 60, 44, 255))


def ill_bridge(d, box):
    x0, y0, x1, y1 = box
    d.rectangle(box, fill=(24, 34, 54, 255))
    d.rectangle([x0, y1 - 12, x1, y1], fill=(52, 96, 140, 255))
    d.rectangle([x0, y1 - 18, x1, y1 - 14], fill=(120, 120, 120, 255))
    for px in (60, 150, 240):
        d.line([x0 + px, y1 - 18, x0 + px, y1 - 34], fill=(180, 180, 180, 255), width=3)
    d.line([x0 + 60, y1 - 34, x0 + 150, y1 - 18], fill=(180, 180, 180, 255), width=2)
    d.line([x0 + 150, y1 - 34, x0 + 240, y1 - 18], fill=(180, 180, 180, 255), width=2)
    d.ellipse([x0 + 180, y0 + 14, x0 + 208, y0 + 38], fill=(255, 150, 50, 255))
    d.ellipse([x0 + 192, y0 + 6, x0 + 216, y0 + 26], fill=(120, 120, 120, 255))


def ill_trump(d, box):
    """Washington deliberates: radar sweep. 'Reports say' — no decision."""
    x0, y0, x1, y1 = box
    d.rectangle(box, fill=(24, 34, 54, 255))
    cx, cy = x0 + 160, y0 + 24
    for r in (18, 12, 6):
        d.arc([cx - r, cy - r, cx + r, cy + r], 0, 360, fill=(90, 130, 180, 255), width=3)
    d.line([cx, cy, cx + 13, cy - 13], fill=(255, 200, 70, 255), width=3)
    for (bx, by) in [(cx - 10, cy + 6), (cx + 6, cy + 9), (cx + 14, cy - 3)]:
        d.ellipse([bx - 3, by - 3, bx + 3, by + 3], fill=(255, 200, 70, 255))


def ill_suneung(d, box):
    """Seoul exam hall: clock + desks with papers."""
    x0, y0, x1, y1 = box
    d.rectangle(box, fill=(205, 220, 235, 255))
    cx, cy = x0 + 52, y0 + 20
    d.ellipse([cx - 11, cy - 11, cx + 11, cy + 11], fill=(255, 255, 255, 255),
              outline=(60, 70, 85, 255), width=2)
    d.line([cx, cy, cx, cy - 7], fill=(60, 70, 85, 255), width=2)
    d.line([cx, cy, cx + 5, cy + 2], fill=(60, 70, 85, 255), width=2)
    for dx in (110, 180, 250):
        d.rectangle([x0 + dx + 8, y1 - 24, x0 + dx + 44, y1 - 16],
                    fill=(255, 255, 255, 255))
        d.rectangle([x0 + dx, y1 - 16, x0 + dx + 52, y1 - 6], fill=(60, 70, 85, 255))


def ill_aus(d, box):
    """Canberra: rising bars + red arrow (jobless rate up)."""
    x0, y0, x1, y1 = box
    d.rectangle(box, fill=(238, 232, 214, 255))
    bars = [10, 16, 22, 28]
    for i, bh in enumerate(bars):
        bx = x0 + 40 + i * 36
        d.rectangle([bx, y1 - 6 - bh, bx + 22, y1 - 6], fill=(31, 97, 141, 255))
    d.line([x0 + 36, y1 - 12, x0 + 196, y0 + 12], fill=(176, 58, 46, 255), width=3)
    d.line([x0 + 196, y0 + 12, x0 + 184, y0 + 12], fill=(176, 58, 46, 255), width=3)
    d.line([x0 + 196, y0 + 12, x0 + 196, y0 + 22], fill=(176, 58, 46, 255), width=3)


def ill_colombia(d, box):
    """Bogota: flag band + marchers with a placard."""
    x0, y0, x1, y1 = box
    d.rectangle(box, fill=(240, 230, 200, 255))
    d.rectangle([x0, y0 + 4, x1, y0 + 12], fill=(252, 209, 22, 255))
    d.rectangle([x0, y0 + 12, x1, y0 + 16], fill=(0, 56, 147, 255))
    d.rectangle([x0, y0 + 16, x1, y0 + 20], fill=(206, 17, 38, 255))
    cols = [(60, 60, 60, 255), (120, 40, 40, 255), (40, 80, 120, 255),
            (80, 60, 30, 255), (50, 90, 60, 255), (100, 50, 90, 255)]
    for i, col in enumerate(cols):
        fx = x0 + 30 + i * 40
        d.ellipse([fx - 4, y1 - 28, fx + 4, y1 - 20], fill=col)
        d.rectangle([fx - 6, y1 - 20, fx + 6, y1 - 4], fill=col)
    d.line([x0 + 268, y0 + 26, x0 + 268, y1 - 4], fill=(60, 60, 60, 255), width=2)
    d.rectangle([x0 + 246, y0 + 24, x0 + 290, y0 + 36], fill=(255, 255, 255, 255),
                outline=(60, 60, 60, 255), width=1)


# ---------------- panels ----------------

def panel(d, box, n, tag, headline, body, ill, head_size=22, body_size=13, ill_h=72,
          bg=(255, 255, 255, 255), kicker_size=13, badge_r=11):
    x0, y0, x1, y1 = box
    d.rectangle(box, fill=bg, outline=(60, 55, 45, 255), width=2)
    ill(d, (x0 + 2, y0 + 2, x1 - 2, y0 + 2 + ill_h))
    ty = y0 + 2 + ill_h + 5
    kicker(d, x0 + 34, ty, tag, size=kicker_size)
    num_badge(d, x0 + 16, ty + 7, n, r=badge_r)
    ty += 18
    ty = para(d, x0 + 10, ty, headline, F_SERIF_B(head_size), INK, x1 - x0 - 20,
              head_size + 2)
    end = para(d, x0 + 10, ty + 2, body, F_SANS(body_size), (52, 52, 52, 255),
               x1 - x0 - 20, body_size + 3)
    # last body line bottom = end - leading + font size
    if end - 3 > y1 - 2:
        print(f"OVERFLOW panel {n}: body bottom {end - 3}px vs box bottom {y1}")


# ---------------- front page ----------------

PANELS_TOP = [
    (1, "DIPLOMACY  ·  APEC", "Three leaders meet in Shenzhen",
     "Xi hosts Trump and Putin for the first trilateral summit in Shenzhen.",
     ill_shenzhen),
    (2, "MIDDLE EAST  ·  GAZA", "Israel ends its Gaza tank raid",
     "The raid across the Yellow Line ends; 'the operation is completed,' "
     "the army tells AFP.",
     ill_gaza),
    (3, "CULTURE  ·  GAMING", "GTA VI begins global rollout",
     "After a 13-year wait, Vice City returns as the sequel unlocks at "
     "midnight.",
     ill_gta),
]

PANELS_MID = [
    (4, "BUSINESS  ·  TECH", "Anthropic debuts in record IPO",
     "Priced at $83 a share, the Claude maker raised $81.3bn. Trading "
     "starts today.",
     ill_ipo),
    (5, "WEATHER  ·  INDIA", "Cyclone Akvan nears India's east coast",
     "Red alert as the storm strengthens; 200,000 marked to evacuate, "
     "landfall Friday.",
     ill_cyclone),
    (6, "LAW  ·  THE HAGUE", "Myanmar guilty of Rohingya genocide (9–6)",
     "The ICJ finds genocidal intent in 2017; ~10,000 killed, 730,000 "
     "fled. Final and binding.",
     ill_icj),
]

PANELS_LOW = [
    (7, "CLIMATE  ·  ANTALYA", "COP31 draft drops fossil fuels and $120bn",
     "The slimmed-down Thursday draft cuts fossil-fuel language and the "
     "$120bn adaptation goal.",
     ill_cop31),
    (8, "EUROPE  ·  UKRAINE", "Crimean Bridge hit a third time in a week",
     "Overnight strike halts traffic again; the railway section is "
     "reported hit.",
     ill_bridge),
    (9, "MIDDLE EAST  ·  IRAN WAR", "Trump weighs new strikes on Iran",
     "Reports say Israel presses for a 4–7 day air campaign; no decision "
     "made.",
     ill_trump),
]

# v5 row 4 — promoted from the v4 ALSO list (same verified 19 Nov facts).
PANELS_ROW4 = [
    (10, "ASIA  ·  EDUCATION", "Suneung: 551,864 sit Korea's exam",
     "551,864 candidates take the eight-hour exam; flights pause for the "
     "listening test.",
     ill_suneung),
    (11, "OCEANIA  ·  ECONOMY", "Australia jobless hits 4.9%, a five-year high",
     "The ABS reports unemployment at a five-year high; economists warn of "
     "a slowdown.",
     ill_aus),
    (12, "AMERICAS  ·  LABOUR", "Colombia's unions call a national strike",
     "Unions call a national strike as workers march in Bogotá and other "
     "cities.",
     ill_colombia),
]

# ALSO renumbered 13-43 (v4 #39-41 promoted to panels 10-12).
ALSO = [
    (13, "Denmark votes 109-0 for Greenland pact"),
    (14, "Korea top court sends ex-PM Han to retrial"),
    (15, "Bangladesh lockdown: Yunus home torched, 4 dead"),
    (16, "Israel hits Hezbollah missile site in Lebanon"),
    (17, "Florida schools shut; 300 rescue calls in Hollywood"),
    (18, "Jepchirchir gets 3-year ban for EPO"),
    (19, "Senators warn AI cyber threats outpace defences"),
    (20, "IEA: Hormuz crisis is worst energy threat ever"),
    (21, "India and Japan hold 2+2 defence talks in Tokyo"),
    (22, "Senegal boat sinks; dozens missing, 4 found"),
    (23, "Houthi missile threat to Riyadh; debris falls"),
    (24, "APEC Shenzhen Declaration adopted"),
    (25, "US drops Supreme Court bid on Venezuela TPS"),
    (26, "Trump defers Iran decision to next year"),
    (27, "UN: no state OK needed to form a group"),
    (28, "Oil steadies near $92; gold at 14-month low"),
    (29, "Berlin allies pledge €70bn Ukraine aid"),
    (30, "Banxico minutes point to long rate pause"),
    (31, "Ukraine imposes emergency power cuts"),
    (32, "Senate rejects bid to curb Iran war, 51-48"),
    (33, "Bitcoin ETFs shed $2.9bn in November"),
    (34, "Somalia expels UAE ambassador"),
    (35, "Tonga declares 27-day drought emergency"),
    (36, "Chow reshuffles Toronto team in 2nd term"),
    (37, "Indonesia passes asset-seizure law, Rp1bn threshold"),
    (38, "US–Philippines $2bn+ defence pact; $12bn Boeing deal"),
    (39, "California braces for atmospheric river"),
    (40, "Mongolia MPs accept president's resignation"),
    (41, "Dow plunges 1,101 points"),
    (42, "Kenya floods kill six, displace hundreds"),
    (43, "Las Vegas GP practice opens on the Strip"),
]

# Region counts v9: #34 Somalia is AFRICA (was EUROPE as Starshield).
# v8 was ME 4, AM 13, AS 10, EU 5, AF 3, OC 2, WO 6 = 43;
# v9 is ME 4, AM 13, AS 10, EU 4, AF 4, OC 2, WO 6 = 43.
# Per-item map: ME = panels 2, 9 + ALSO 16, 23; AM = panels 3, 4, 12 +
# ALSO 17, 19, 25, 26, 30, 32, 36, 39, 41, 43; AS = panels 1, 5, 6, 10 +
# ALSO 14, 15, 21, 24, 37, 40; EU = panel 8 + ALSO 13, 29, 31;
# AF = ALSO 18, 22, 34, 42; OC = panel 11 + ALSO 35;
# WO = panel 7 + ALSO 20, 27, 28, 33, 38.
REGIONS = [("MIDDLE EAST 4", (176, 58, 46, 255)), ("AMERICAS 13", (31, 97, 141, 255)),
           ("ASIA 10", (183, 149, 11, 255)), ("EUROPE 4", (46, 64, 87, 255)),
           ("AFRICA 4", (147, 81, 22, 255)), ("OCEANIA 2", (17, 122, 101, 255)),
           ("WORLD 6", (97, 106, 107, 255))]

# v9: GTA stat 15.9m (17 Nov) -> 19.1m (Sensor Tower, Thu morning 19 Nov);
# Bolivia 78,000 stat dropped with ALSO #41 -> "1,101" Dow points lost,
# echoing the new ALSO #41 (same echo pattern as Bolivia before it).
STATS = [("$81.3bn", "Anthropic IPO, largest ever"),
         ("19.1m", "GTA VI pre-orders banked"),
         ("200,000", "Akvan evacuations planned"),
         ("$120bn", "COP31 goal cut"),
         ("1,101", "Dow points lost"),
         ("$2bn+", "US–Philippines pact")]

# (n, lon, lat, colour, dx, dy) — dx/dy nudge badges that would collide.
# Pin 2 nudged: Gaza and Antalya pins sit ~7px apart on the map (v4 flaw).
PINS = [(1, 114, 22, (183, 149, 11, 255), 0, 0),
        (2, 34.5, 31.5, (176, 58, 46, 255), -16, 12),
        (3, -80, 26, (31, 97, 141, 255), 0, 0),
        (4, -74, 41, (31, 97, 141, 255), 0, 0),
        (5, 86, 20, (183, 149, 11, 255), 0, 0),
        (6, 4.4, 52.0, (97, 106, 107, 255), 0, 0),
        (7, 30.7, 36.9, (97, 106, 107, 255), 0, 0),
        (8, 36.4, 45.3, (46, 64, 87, 255), 18, -14),
        (9, -77, 39, (176, 58, 46, 255), 18, -16),
        (10, 127, 37.5, (183, 149, 11, 255), 16, -12),
        (11, 149, -35.3, (17, 122, 101, 255), 0, 0),
        (12, -74, 4.7, (31, 97, 141, 255), 14, 10)]


def build():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- masthead (92px, was 100) ----
    d.rectangle([0, 0, W, 92], fill=NAVY)
    d.text((14, 6), "THE WORLD IN ONE DAY", font=F_SANS_B(14), fill=(255, 255, 255, 255))
    d.text((908, 6), "43 STORIES  ·  6 CONTINENTS", font=F_SANS_B(14),
           fill=GOLD, anchor="ra")
    d.text((14, 18), "Thursday, 19 November 2026", font=F_SERIF_B(40),
           fill=(255, 255, 255, 255))
    d.text((14, 64), "Every story on this page happened, or was first reported, on this day.",
           font=F_SERIF(13), fill=(200, 210, 235, 255))
    d.text((14, 80), "TOP OF THE DAY — THREE LEADERS MEET IN SHENZHEN  ·  ICJ FINDS MYANMAR GUILTY OF GENOCIDE  ·  COP31 DRAFT DROPS $120BN",
           font=F_SANS_B(11), fill=GOLD)
    d.rectangle([922, 8, 1010, 50], fill=GOLD)
    d.text((966, 11), "19", font=F_SANS_B(24), fill=NAVY_D, anchor="ma")
    d.text((966, 36), "NOV", font=F_SANS_B(11), fill=NAVY_D, anchor="ma")

    # ---- the day by hours (UTC strip, v4) — 92-112 (20px) ----
    d.rectangle([0, 92, W, 112], fill=NAVY_D)
    utc_label = "THE DAY BY HOURS — "
    utc_items = ("00:00 UTC GTA VI unlocks in New Zealand · Morning Shenzhen summit · "
                 "09:00 UTC ICJ genocide verdict · 14:30 UTC Anthropic debuts · "
                 "Evening COP31 ministers take over")
    d.text((14, 99), utc_label, font=F_SANS_B(10), fill=GOLD)
    lx = 14 + d.textlength(utc_label, font=F_SANS_B(10))
    d.text((lx, 99), utc_items, font=F_SANS(10), fill=(255, 255, 255, 255))

    # ---- region strip — 116-134 (18px) ----
    x = 14
    total_w = W - 28
    for label, col in REGIONS:
        w = total_w // len(REGIONS)
        d.rectangle([x, 116, x + w - 2, 134], fill=col)
        d.text((x + w / 2, 125), label, font=F_SANS_B(11), fill=(255, 255, 255, 255),
               anchor="mm")
        x += w

    # ---- story panels: hero band (row 1) + 3 rows ----
    # v8 hero band (170px tall): panel 1 is 460px wide with a 24px one-line
    # headline, a warm cream tint and a 3px gold border; panels 2-3 are
    # 263px wide in the same band. Rows 2-4 keep the 3x325px grid at 147px
    # (4px gaps now, was 5px). All story text identical to v7.
    (n1, tag1, head1, body1, _ill1) = PANELS_TOP[0]
    panel(d, (14, 138, 474, 308), n1, tag1, head1, body1, ill_shenzhen_hero,
          head_size=24, body_size=13, ill_h=84, bg=(255, 244, 220, 255),
          kicker_size=14)
    d.rectangle([14, 138, 474, 308], outline=GOLD, width=3)
    for (n, tag, head, body, ill), cx in zip(PANELS_TOP[1:], [479, 747]):
        panel(d, (cx, 138, cx + 263, 308), n, tag, head, body, ill,
              head_size=21, body_size=13, ill_h=48)
    cols = [14, 349, 684]
    cw = 325
    rows = [(312, 147, PANELS_MID, 19, 12, 48), (463, 147, PANELS_LOW, 19, 12, 48),
            (614, 147, PANELS_ROW4, 19, 12, 48)]
    for (ry, rh, panels, hs, bs, ih) in rows:
        for (n, tag, head, body, ill), cx in zip(panels, cols):
            panel(d, (cx, ry, cx + cw, ry + rh), n, tag, head, body, ill,
                  head_size=hs, body_size=bs, ill_h=ih)

    # ---- stats strip — rules 765/805, numbers 24px (v7: 760/800) ----
    d.line([14, 765, 1010, 765], fill=GOLD, width=3)
    d.line([14, 805, 1010, 805], fill=GOLD, width=3)
    sx = 14
    for num, cap in STATS:
        w = (W - 28) // 6
        d.text((sx + w / 2, 768), num, font=F_SERIF_B(24), fill=NAVY, anchor="ma")
        d.text((sx + w / 2, 792), cap, font=F_SANS(10), fill=GREY, anchor="ma")
        sx += w

    # ---- bottom: map + also list (v7: headers 808, map/ALSO from 828) ----
    d.text((14, 812), "WHERE IT HAPPENED", font=F_SANS_B(14), fill=RED)
    d.line([14, 828, 392, 828], fill=RED, width=2)
    ll = draw_map(d, (14, 832, 392, 952))
    for (n, lon, lat, col, dx, dy) in PINS:
        px, py = ll(lon, lat)
        num_badge(d, int(px + dx), int(py + dy), n, r=10)
    d.text((14, 958), "Numbered pins mark stories 1–12.",
           font=F_SANS(11), fill=GREY)

    d.text((404, 812), "ALSO ON THURSDAY 19 NOVEMBER  —  31 MORE STORIES",
           font=F_SANS_B(13), fill=RED)
    d.line([404, 828, 1010, 828], fill=RED, width=2)
    f_item = F_SANS(10)
    for i, (n, txt) in enumerate(ALSO):
        col = i // 16
        row = i % 16
        ix = 404 + col * 306
        iy = 832 + row * 11
        d.text((ix, iy), f"{n}. {txt}", font=f_item, fill=INK)
    # footer: sources + date check on one line (10px, 984px of 996).
    # Names the four newly excluded items (Gaza crossing, Carney, Australia
    # sanctions — 18 Nov; Deutsche $582m — 17 Nov) plus the v5 exclusions.
    # The other v5 drops (Gaza aid plea 15 Nov, France protests 7 Nov,
    # Eisenkot 7-8 Nov, Palantir 18 Nov, Lieu chair 18 Nov, Ilona W. Sep,
    # Vance 16 Nov, Bapco 18 Nov, Estonia 15 Nov, Banxico cut 5 Nov)
    # are documented in README.md; they do not fit on this line.
    footer = ("Sources: Reuters, AP, AFP.  "
              "DATE CHECK — out (18 Nov): Voyager, EU €45bn, Fed minutes, Van Gogh, Gaza crossing, Carney, Australia sanctions; "
              "(17 Nov): N. Korea, Nvidia H200, Deutsche $582m.")
    d.text((14, 1012), footer, font=F_SANS(10), fill=GREY)
    # self-checks: no ALSO line may spill into the next column; footer must fit
    for (n, txt) in ALSO:
        w = d.textlength(f"{n}. {txt}", font=f_item)
        if w > 300:
            print(f"OVERFLOW also {n}: {w:.0f}px")
    fw = d.textlength(footer, font=F_SANS(10))
    if fw > 996:
        print(f"OVERFLOW footer: {fw:.0f}px")
    uw = (d.textlength(utc_label, font=F_SANS_B(10))
          + d.textlength(utc_items, font=F_SANS(10)))
    if uw > 982:
        print(f"OVERFLOW utc strip: {uw:.0f}px")
    subhead = ("TOP OF THE DAY — THREE LEADERS MEET IN SHENZHEN  ·  ICJ FINDS MYANMAR GUILTY OF GENOCIDE  ·  "
               "COP31 DRAFT DROPS $120BN")
    sw = d.textlength(subhead, font=F_SANS_B(11))
    if sw > 990:
        print(f"OVERFLOW subhead: {sw:.0f}px")
    return img


def main():
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent / "entry.png"
    img = build()
    img.save(out, format="PNG", optimize=True)
    print(f"wrote {out} {img.size} {out.stat().st_size} bytes")


if __name__ == "__main__":
    main()
