import os
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib import font_manager

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "2026-09-24-chart.png"

labels = ["S&P 500", "Nasdaq\nComposite"]
changes = [-0.74, -1.10]
colors = ["#94ACCB", "#6D90B9"]

for env_name in ("SATORI_BOLD", "SATORI_MEDIUM"):
    font_path = os.environ.get(env_name)
    if font_path and Path(font_path).is_file():
        font_manager.fontManager.addfont(font_path)
font_name = "Satoshi" if os.environ.get("SATORI_BOLD") else "DejaVu Sans"
plt.rcParams.update({"font.family": font_name})
fig, ax = plt.subplots(figsize=(12, 6.75), dpi=100, facecolor="#FFFFFF")
ax.set_facecolor("#FFFFFF")
bars = ax.bar(labels, changes, color=colors, width=0.52)
ax.axhline(0, color="#1C2531", linewidth=1)
ax.yaxis.grid(True, color="#EBEFF4", linewidth=1)
ax.xaxis.grid(False)
ax.set_axisbelow(True)
ax.set_ylim(-1.4, 0.2)
ax.set_yticks([0, -0.4, -0.8, -1.2])
ax.set_yticklabels(["0%", "-0.4%", "-0.8%", "-1.2%"], color="#5A697C", fontsize=12)
ax.tick_params(axis="x", colors="#1C2531", labelsize=15, length=0)
ax.tick_params(axis="y", length=0)
for spine in ax.spines.values():
    spine.set_visible(False)
for bar, value in zip(bars, changes):
    ax.text(bar.get_x() + bar.get_width() / 2, value - 0.08, f"{value:.2f}%",
            ha="center", va="top", color="#1C2531", fontsize=15, fontweight="bold")
fig.text(0.08, 0.92, "Hotter activity data reset the rate-sensitive trade", fontsize=23,
         fontweight="bold", color="#1C2531")
fig.text(0.08, 0.875, "US index moves at the 23 September 2026 close", fontsize=13, color="#5A697C")
fig.text(0.08, 0.045, "Source: Reuters preliminary market close, 23 September 2026.", fontsize=10, color="#5A697C")
plt.subplots_adjust(left=0.12, right=0.94, top=0.8, bottom=0.16)
fig.savefig(OUT, dpi=100)
