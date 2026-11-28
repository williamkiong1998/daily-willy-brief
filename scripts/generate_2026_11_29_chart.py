from pathlib import Path
import urllib.request
import zipfile

import matplotlib.pyplot as plt
from matplotlib import font_manager


ROOT = Path(__file__).resolve().parents[1]
FONT_DIR = ROOT / ".fonts"
FONT_DIR.mkdir(exist_ok=True)


def install_satoshi():
    """Use Satoshi when Fontshare is reachable; keep a reliable fallback."""
    try:
        archive = FONT_DIR / "satoshi-2026-11-29.zip"
        urllib.request.urlretrieve(
            "https://api.fontshare.com/v2/fonts/download/satoshi", archive
        )
        with zipfile.ZipFile(archive) as bundle:
            bundle.extractall(FONT_DIR)
        for font in FONT_DIR.rglob("*.ttf"):
            font_manager.fontManager.addfont(str(font))
        return "Satoshi"
    except Exception:
        return "DejaVu Sans"


FONT = install_satoshi()
plt.rcParams.update({"font.family": FONT})

fig, ax = plt.subplots(figsize=(12, 6.75), dpi=100)
fig.patch.set_facecolor("#FFFFFF")
ax.set_facecolor("#FFFFFF")

labels = ["S&P 500", "Nasdaq Composite"]
daily = [1.6, 2.3]
weekly = [5.6, 6.7]
x = [0, 1]
width = 0.30

bars_daily = ax.bar([i - width / 2 for i in x], daily, width, color="#94ACCB", label="Friday")
bars_weekly = ax.bar([i + width / 2 for i in x], weekly, width, color="#6D90B9", label="Week")

ax.set_ylim(0, 8.1)
ax.set_xticks(x, labels, color="#1C2531", fontsize=14, fontweight="bold")
ax.set_yticks([0, 2, 4, 6, 8], ["0%", "2%", "4%", "6%", "8%"], color="#5A697C", fontsize=11)
ax.tick_params(axis="both", length=0)
ax.yaxis.grid(True, color="#BBC7DC", linewidth=0.8)
ax.set_axisbelow(True)
for spine in ax.spines.values():
    spine.set_visible(False)

for bars in (bars_daily, bars_weekly):
    for bar in bars:
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.18,
                f"{bar.get_height():.1f}%", ha="center", va="bottom",
                color="#1C2531", fontsize=13, fontweight="bold")

legend = ax.legend(loc="upper left", frameon=False, ncol=2, bbox_to_anchor=(0, 1.03))
for text in legend.get_texts():
    text.set_color("#5A697C")
    text.set_fontsize(11)

fig.text(0.08, 0.93, "Tech led both the Friday bounce and the Thanksgiving-week rebound",
         color="#1C2531", fontsize=21, fontweight="bold")
fig.text(0.08, 0.865, "Percentage change through the shortened US session on 27 November 2026",
         color="#5A697C", fontsize=12)
fig.text(0.08, 0.05, "Source: Associated Press market close, 27 Nov 2026",
         color="#5A697C", fontsize=10)

plt.tight_layout(rect=[0.06, 0.1, 0.98, 0.79])
output = ROOT / "assets" / "2026-11-29-chart.png"
fig.savefig(output, dpi=100, facecolor="#FFFFFF")
print(output)
