from pathlib import Path

import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
FONT = ROOT / ".fonts/satoshi/Satoshi_Complete/Fonts/WEB/fonts/Satoshi-Variable.ttf"
if FONT.exists():
    fm.fontManager.addfont(str(FONT))
    plt.rcParams["font.family"] = fm.FontProperties(fname=str(FONT)).get_name()
else:
    plt.rcParams["font.family"] = "DejaVu Sans"

labels = ["S&P 500", "Nasdaq\nComposite"]
changes = [-2.02, -2.25]
colors = ["#94ACCB", "#6D90B9"]

fig, ax = plt.subplots(figsize=(12, 6.75), dpi=100)
fig.patch.set_facecolor("#FFFFFF")
ax.set_facecolor("#FFFFFF")
bars = ax.bar(labels, changes, color=colors, width=0.52)
ax.axhline(0, color="#BBC7DC", linewidth=1)
ax.grid(axis="y", color="#EBEFF4", linewidth=1)
ax.set_axisbelow(True)
ax.set_ylim(-2.8, 0.35)
ax.set_yticks([-2.5, -2.0, -1.5, -1.0, -0.5, 0])
ax.set_yticklabels([f"{tick:.1f}%" for tick in [-2.5, -2.0, -1.5, -1.0, -0.5, 0]], color="#5A697C")
ax.tick_params(axis="x", colors="#1C2531", labelsize=15, length=0, pad=12)
ax.tick_params(axis="y", labelsize=11, length=0)
for spine in ax.spines.values():
    spine.set_visible(False)
for bar, value in zip(bars, changes):
    ax.text(bar.get_x() + bar.get_width() / 2, value - 0.12, f"{value:.2f}%", ha="center", va="top", fontsize=18, fontweight="bold", color="#1C2531")
fig.text(0.08, 0.92, "Tech bore the sharper hit in Thursday’s US selloff", fontsize=25, fontweight="bold", color="#1C2531")
fig.text(0.08, 0.865, "Daily percentage change · latest available US close, 19 November 2026", fontsize=13, color="#5A697C")
fig.text(0.08, 0.045, "Source: Asian Development Bank Daily Market Watch, 20 Nov 2026; Bloomberg and CEIC data.", fontsize=10, color="#5A697C")
plt.subplots_adjust(left=0.09, right=0.96, top=0.80, bottom=0.18)
fig.savefig(ROOT / "assets/2026-11-21-chart.png", facecolor="#FFFFFF")
