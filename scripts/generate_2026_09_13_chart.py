from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib import font_manager

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "2026-09-13-chart.png"
FONT_DIR = Path("/tmp/willy-brief-font/unpacked/Satoshi_Complete/Fonts/WEB/fonts")

for filename in ("Satoshi-Medium.ttf", "Satoshi-Bold.ttf"):
    candidate = FONT_DIR / filename
    if candidate.exists():
        font_manager.fontManager.addfont(str(candidate))

plt.rcParams["font.family"] = "Satoshi"
fig, ax = plt.subplots(figsize=(12, 6.75), dpi=100)
fig.patch.set_facecolor("#FFFFFF")
ax.set_facecolor("#FFFFFF")
labels = ["S&P 500", "Nasdaq\nComposite"]
values = [-0.8, -0.7]
bars = ax.bar(labels, values, color=["#6D90B9", "#94ACCB"], width=0.46)
ax.axhline(0, color="#BBC7DC", linewidth=1)
ax.set_ylim(-1.15, 0.25)
ax.set_yticks([-1.0, -0.5, 0.0])
ax.set_yticklabels(["-1.0%", "-0.5%", "0%"], color="#5A697C", fontsize=13)
ax.grid(axis="y", color="#EBEFF4", linewidth=1)
ax.set_axisbelow(True)
for spine in ax.spines.values(): spine.set_visible(False)
ax.tick_params(axis="x", colors="#1C2531", labelsize=15, length=0, pad=12)
ax.tick_params(axis="y", length=0)
for bar, value in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width() / 2, value - 0.08, f"{value:.1f}%", ha="center", va="top", fontsize=20, fontweight="bold", color="#1C2531")
fig.text(0.08, 0.92, "Friday's rebound did not erase a week in the red", fontsize=26, fontweight="bold", color="#1C2531")
fig.text(0.08, 0.865, "Weekly change to Friday, 11 September 2026", fontsize=15, color="#5A697C")
fig.text(0.08, 0.045, "Source: Associated Press, Friday 11 September 2026 market recap.", fontsize=10, color="#5A697C")
plt.subplots_adjust(left=0.12, right=0.96, top=0.80, bottom=0.18)
fig.savefig(OUT, facecolor="#FFFFFF")
