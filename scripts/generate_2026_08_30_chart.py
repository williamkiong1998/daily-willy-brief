from pathlib import Path

from matplotlib import font_manager
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parents[1] / "assets" / "2026-08-30-chart.png"
FONT_DIR = Path("/private/tmp/willy-brief-satoshi/Satoshi_Complete/Fonts/WEB/fonts")
for name in ("Satoshi-Medium.ttf", "Satoshi-Bold.ttf"):
    path = FONT_DIR / name
    if path.exists():
        font_manager.fontManager.addfont(str(path))
medium_path, bold_path = FONT_DIR / "Satoshi-Medium.ttf", FONT_DIR / "Satoshi-Bold.ttf"
medium = font_manager.FontProperties(fname=str(medium_path)) if medium_path.exists() else font_manager.FontProperties(family="DejaVu Sans")
bold = font_manager.FontProperties(fname=str(bold_path)) if bold_path.exists() else font_manager.FontProperties(family="DejaVu Sans", weight="bold")

fig, ax = plt.subplots(figsize=(12, 6.75), dpi=100)
fig.patch.set_facecolor("#FFFFFF")
ax.set_facecolor("#FFFFFF")
years, china, usa = [2020, 2021, 2022, 2023, 2024, 2025], [14, 16, 18, 20, 23, 25], [12, 12, 12, 12, 12, 12]
ax.plot(years, china, color="#6D90B9", linewidth=4, marker="o", markersize=8)
ax.plot(years, usa, color="#94ACCB", linewidth=2.5, marker="o", markersize=6)
ax.set_xlim(2019.8, 2025.25); ax.set_ylim(0, 30); ax.set_xticks(years); ax.set_yticks([0, 10, 20, 30])
ax.set_yticklabels(["0%", "10%", "20%", "30%"], color="#5A697C", fontproperties=medium, fontsize=12)
ax.set_xticklabels(years, color="#1C2531", fontproperties=medium, fontsize=12)
ax.grid(axis="y", color="#BBC7DC", linewidth=0.8); ax.set_axisbelow(True)
for spine in ax.spines.values(): spine.set_visible(False)
ax.tick_params(axis="both", length=0, pad=10)
ax.text(2025.08, 25, "China 25%", va="center", color="#42648A", fontproperties=bold, fontsize=16)
ax.text(2025.08, 12, "U.S. 12%", va="center", color="#5A697C", fontproperties=medium, fontsize=15)
fig.text(0.07, 0.91, "China added 11 points of global auto share in five years", color="#1C2531", fontproperties=bold, fontsize=24)
fig.text(0.07, 0.855, "Share of global vehicle market by automaker origin", color="#5A697C", fontproperties=medium, fontsize=14)
fig.text(0.07, 0.045, "Source: Center for Automotive Research analysis of GlobalData, via Axios", color="#5A697C", fontproperties=medium, fontsize=10)
plt.subplots_adjust(left=0.1, right=0.89, top=0.78, bottom=0.17)
fig.savefig(OUT, facecolor=fig.get_facecolor())
