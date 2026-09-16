from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "2026-09-17-chart.png"

labels = ["Dow", "S&P 500", "Nasdaq"]
changes = [-1.2, -0.4, -0.01]
colors = ["#94ACCB", "#6D90B9", "#5A697C"]

plt.rcParams.update({"font.family": "DejaVu Sans"})
fig, ax = plt.subplots(figsize=(12, 6.75), dpi=100, facecolor="#FFFFFF")
ax.set_facecolor("#FFFFFF")
bars = ax.bar(labels, changes, color=colors, width=0.56)
ax.axhline(0, color="#1C2531", linewidth=1)
ax.yaxis.grid(True, color="#EBEFF4", linewidth=1)
ax.xaxis.grid(False)
ax.set_axisbelow(True)
ax.set_ylim(-1.45, 0.2)
ax.set_yticks([-1.2, -0.8, -0.4, 0.0])
ax.set_yticklabels(["-1.2%", "-0.8%", "-0.4%", "0%"], color="#5A697C", fontsize=12)
ax.tick_params(axis="x", colors="#1C2531", labelsize=14, length=0)
ax.tick_params(axis="y", length=0)
for spine in ax.spines.values():
    spine.set_visible(False)
for bar, value in zip(bars, changes):
    ax.text(bar.get_x() + bar.get_width() / 2, value - 0.07, f"{value:.2g}%",
            ha="center", va="top", color="#1C2531", fontsize=15, fontweight="bold")
fig.text(0.08, 0.92, "Fed day hit the Dow harder than big-tech indices", fontsize=23,
         fontweight="bold", color="#1C2531")
fig.text(0.08, 0.875, "US index moves on 16 September 2026", fontsize=13, color="#5A697C")
fig.text(0.08, 0.045, "Source: Associated Press market close, 16 September 2026.", fontsize=10, color="#5A697C")
plt.subplots_adjust(left=0.12, right=0.94, top=0.8, bottom=0.16)
fig.savefig(OUT, dpi=100)
