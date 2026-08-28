from pathlib import Path
from matplotlib import font_manager
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parents[1] / "assets" / "2026-08-28-chart.png"
FONT_DIR = Path("/private/tmp/willy-brief-satoshi/Satoshi_Complete/Fonts/WEB/fonts")
for name in ("Satoshi-Medium.ttf", "Satoshi-Bold.ttf"):
    path = FONT_DIR / name
    if path.exists():
        font_manager.fontManager.addfont(str(path))

medium = font_manager.FontProperties(fname=str(FONT_DIR / "Satoshi-Medium.ttf"))
bold = font_manager.FontProperties(fname=str(FONT_DIR / "Satoshi-Bold.ttf"))

plt.rcParams["font.family"] = medium.get_name()
fig, ax = plt.subplots(figsize=(12, 6.75), dpi=100)
fig.patch.set_facecolor("#FFFFFF")
ax.set_facecolor("#FFFFFF")
labels = ["Per employed\nperson", "Per hour\nworked"]
values = [4.9, 5.5]
bars = ax.bar(labels, values, color=["#6D90B9", "#94ACCB"], width=0.48)
ax.set_ylim(0, 7)
ax.set_yticks([0, 2, 4, 6])
ax.set_yticklabels(["0%", "2%", "4%", "6%"], color="#5A697C", fontproperties=medium, fontsize=12)
ax.grid(axis="y", color="#BBC7DC", linewidth=0.8)
ax.set_axisbelow(True)
for spine in ax.spines.values():
    spine.set_visible(False)
ax.tick_params(axis="x", length=0, pad=12, labelcolor="#1C2531", labelsize=14)
ax.tick_params(axis="y", length=0)
for bar, value in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width() / 2, value + 0.17, f"{value:.1f}%", ha="center", va="bottom", color="#1C2531", fontproperties=bold, fontsize=22)
fig.text(0.07, 0.91, "Malaysia's productivity grew faster per hour than per worker", color="#1C2531", fontproperties=bold, fontsize=24)
fig.text(0.07, 0.855, "Year-on-year change, Q2 2026", color="#5A697C", fontproperties=medium, fontsize=14)
fig.text(0.07, 0.045, "Source: DOSM, Labour Market Review Q2 2026", color="#5A697C", fontproperties=medium, fontsize=10)
plt.subplots_adjust(left=0.1, right=0.96, top=0.78, bottom=0.17)
fig.savefig(OUT, facecolor=fig.get_facecolor())
