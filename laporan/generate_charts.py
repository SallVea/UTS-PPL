from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

OUT = Path(__file__).parent / "img"
OUT.mkdir(exist_ok=True)

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
RED = "#c0392b"
GREEN = "#27ae60"
ORANGE = "#e67e22"
GREY = "#7f8c8d"
DARK = "#2c3e50"
LIGHT = "#ecf0f1"

def f(size, bold=False):
    return ImageFont.truetype(FONT_BOLD if bold else FONT, size)

def canvas(w, h):
    img = Image.new("RGB", (w*2, h*2), "white")
    return img, ImageDraw.Draw(img)

def save(img, name, w, h):
    img = img.resize((w, h), Image.LANCZOS)
    img.save(OUT / name, dpi=(160, 160))

def hbar(name, labels, values, colors, title, maxv=None):
    W, H = 1500, 760
    img, d = canvas(W, H)
    d.text((60*2, 35*2), title, font=f(40, True), fill=DARK)
    maxv = maxv or max(values)
    left, top = 470, 150
    bar_h, gap = 85, 55
    # grid
    for i in range(5):
        x = left + (W-560) * i / 4
        d.line([(x*2, top*2), (x*2, (top + 4*(bar_h+gap))*2)], fill="#d5dbdb", width=2)
        d.text((x*2-15, (top + 4*(bar_h+gap)+18)*2), f"{int(maxv*i/4)}", font=f(26), fill=GREY)
    for i, (lab, val, col) in enumerate(zip(labels, values, colors)):
        y = top + i*(bar_h+gap)
        d.text((60*2, (y+18)*2), lab, font=f(32), fill=DARK)
        bw = int((W-560) * val / maxv)
        d.rounded_rectangle([(left*2, y*2), ((left+bw)*2, (y+bar_h)*2)], radius=10, fill=col)
        d.text(((left+bw+18)*2, (y+15)*2), str(val), font=f(34, True), fill=col)
    save(img, name, W, H)

def stacked(name, rows, title):
    # rows: [(label, [(val,color,label),...]), ...]
    W, H = 1500, 560
    img, d = canvas(W, H)
    d.text((60*2, 30*2), title, font=f(40, True), fill=DARK)
    left, top = 260, 135
    bar_h, gap = 65, 55
    total = max(sum(v for v,_,_ in segs) for _, segs in rows)
    scale = (W-430)/total
    for i, (lab, segs) in enumerate(rows):
        y = top + i*(bar_h+gap)
        d.text((60*2, (y+12)*2), lab, font=f(32, True), fill=DARK)
        x = left
        for val, col, _ in segs:
            w = int(val*scale)
            if w:
                d.rectangle([(x*2, y*2), ((x+w)*2, (y+bar_h)*2)], fill=col)
                if val >= 2:
                    d.text(((x+w/2-10)*2, (y+16)*2), str(val), font=f(30, True), fill="white")
                x += w
    # legend
    leg = []
    for _, segs in rows:
        for _, col, lab in segs:
            if (col,lab) not in leg: leg.append((col,lab))
    lx, ly = 260, 460
    for col, lab in leg:
        d.rectangle([(lx*2, ly*2), ((lx+22)*2, (ly+22)*2)], fill=col)
        d.text(((lx+32)*2, (ly-4)*2), lab, font=f(28), fill=DARK)
        lx += 250
    save(img, name, W, H)

# 1. Status
hbar("status.png", ["FAILED", "PASSED", "BLOCKED"], [27,5,2], [RED,GREEN,ORANGE],
     "Status eksekusi Run 31 (34 test case)", maxv=30)

# 2. Priority stacked
stacked("priority-status.png", [
    ("P1", [(12,RED,"FAILED"), (1,GREEN,"PASSED")]),
    ("P2", [(15,RED,"FAILED"), (4,GREEN,"PASSED"), (2,ORANGE,"BLOCKED")]),
], "Hasil per priority (jumlah test case)")

# 3. Severity
hbar("severity.png", ["Critical", "Major", "Minor", "Trivial"], [2,10,16,4],
     ["#7b1e1e", RED, ORANGE, GREY], "Distribusi severity 32 issue", maxv=20)

# 4. Defect density
hbar("defect-density.png", ["Beranda & Katalog", "Login & Auth", "Keranjang", "Checkout & Pembayaran"],
     [171.4,50.0,80.0,81.8], ["#7b1e1e", ORANGE, RED, "#8e44ad"],
     "Defect density per area (bug / test case x 100%)", maxv=200)
