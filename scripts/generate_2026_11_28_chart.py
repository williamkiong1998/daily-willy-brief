from pathlib import Path
import os
import urllib.request
import zipfile

import matplotlib.pyplot as plt
from matplotlib import font_manager


ROOT = Path(__file__).resolve().parents[1]
FONT_DIR = ROOT / ".fonts"
FONT_DIR.mkdir(exist_ok=True)


def install_satoshi():
    """Best-effort font install; chart remains portable without it."""
    try:
        archive = FONT_DIR / "satoshi.zip"
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

labels = ["Total approved\ninvestment", "Data centre +\ncloud computing"]
values = [350.4, 123.5]
colors = ["#94ACCB", "#6D90B9"]
bars = ax.barh(labels, values, color=colors, height=0.52)

ax.set_xlim(0, 390)
ax.set_xticks([0, 100, 200, 300])
ax.set_xticklabels(["RM0bn", "RM100bn", "RM200bn", "RM300bn"], color="#5A697C", fontsize=11)
ax.tick_params(axis="y", colors="#1C2531", labelsize=13, length=0)
ax.tick_params(axis="x", length=0)
ax.xaxis.grid(True, color="#BBC7DC", linewidth=0.8)
ax.set_axisbelow(True)
for side in ax.spines.values():
    side.set_visible(False)

for bar, value in zip(bars, values):
    ax.text(value + 8, bar.get_y() + bar.get_height() / 2, f"RM{value:.1f}bn",
            va="center", ha="left", color="#1C2531", fontsize=16, fontweight="bold")

ax.text(123.5, 1.37, "35.2% of all approved investment", ha="center", va="bottom",
        color="#42648A", fontsize=12, fontweight="bold")
ax.annotate("", xy=(123.5, 1.23), xytext=(123.5, 1.06),
            arrowprops={"arrowstyle": "-", "color": "#42648A", "lw": 1.2})

fig.text(0.08, 0.92, "Malaysia’s data-centre pipeline is now more than a third of approvals",
         color="#1C2531", fontsize=22, fontweight="bold")
fig.text(0.08, 0.86, "First nine months of 2026 — approved investments, not cash deployed",
         color="#5A697C", fontsize=12)
fig.text(0.08, 0.05, "Source: Malaysian Investment Development Authority (MIDA), 17 Nov 2026",
         color="#5A697C", fontsize=10)

plt.tight_layout(rect=[0.06, 0.1, 0.98, 0.8])
output = ROOT / "assets" / "2026-11-28-chart.png"
fig.savefig(output, dpi=100, facecolor="#FFFFFF")
print(output)
