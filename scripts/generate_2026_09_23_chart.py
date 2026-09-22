from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "2026-09-23-chart.png"

labels = ["S&P 500\nMon", "Nasdaq\nMon", "S&P 500\nTue", "Nasdaq\nTue"]
changes = [1.5, 2.3, -0.001, 0.5]
colors = ["#94ACCB", "#6D90B9", "#BBC7DC", "#6D90B9"]

plt.rcParams.update({"font.family": "DejaVu Sans"})
fig, ax = plt.subplots(figsize=(12, 6.75), dpi=100, facecolor="#FFFFFF")
ax.set_facecolor("#FFFFFF")
bars = ax.bar(labels, changes, color=colors, width=0.56)
ax.axhline(0, color="#1C2531", linewidth=1)
ax.yaxis.grid(True, color="#EBEFF4", linewidth=1)
ax.xaxis.grid(False)
ax.set_axisbelow(True)
ax.set_ylim(-0.35, 2.75)
ax.set_yticks([0, 0.5, 1.0, 1.5, 2.0, 2.5])
ax.set_yticklabels(["0%", "0.5%", "1.0%", "1.5%", "2.0%", "2.5%"], color="#5A697C", fontsize=12)
ax.tick_params(axis="x", colors="#1C2531", labelsize=13, length=0)
ax.tick_params(axis="y", length=0)
for spine in ax.spines.values():
    spine.set_visible(False)
for bar, value in zip(bars, changes):
    label = "flat" if abs(value) < 0.01 else f"{value:.1f}%"
    y = value + 0.08 if value >= 0 else value - 0.11
    va = "bottom" if value >= 0 else "top"
    ax.text(bar.get_x() + bar.get_width() / 2, y, label,
            ha="center", va=va, color="#1C2531", fontsize=14, fontweight="bold")
fig.text(0.08, 0.92, "The Nasdaq kept climbing after Monday's broad relief rally", fontsize=23,
         fontweight="bold", color="#1C2531")
fig.text(0.08, 0.875, "US index moves on 21–22 September 2026", fontsize=13, color="#5A697C")
fig.text(0.08, 0.045, "Source: Associated Press market closes, 21 and 22 September 2026.", fontsize=10, color="#5A697C")
plt.subplots_adjust(left=0.12, right=0.94, top=0.8, bottom=0.16)
fig.savefig(OUT, dpi=100)
