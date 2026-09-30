from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


OUTPUT = Path(__file__).resolve().parents[1] / "assets" / "2026-09-30-chart.png"

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 14})
fig, ax = plt.subplots(figsize=(12, 6.75), dpi=100)
fig.patch.set_facecolor("#FFFFFF")
ax.set_facecolor("#FFFFFF")

ax.set_axis_off()
ax.set_xlim(0, 12)
ax.set_ylim(0, 8)
fig.text(0.125, 0.92, "Yields and oil are the market's real constraint", fontsize=22, fontweight="bold", color="#1C2531")
fig.text(0.125, 0.865, "Tuesday's tape was mild. The operating inputs behind it were not.", fontsize=12, color="#5A697C")

cards = [
    (0.45, 4.0, "5.25%", "10-year Treasury yield", "#42648A"),
    (6.15, 4.0, "US$96.16", "Brent crude per barrel", "#6D90B9"),
    (0.45, 1.2, "−0.2%", "S&P 500 Tuesday change", "#94ACCB"),
    (6.15, 1.2, "−0.1%", "Nasdaq Tuesday change", "#94ACCB"),
]
for x, y, value, label, color in cards:
    ax.add_patch(FancyBboxPatch((x, y), 5.1, 2.05, boxstyle="round,pad=0.04,rounding_size=0.12", facecolor="#EBEFF4", edgecolor="#BBC7DC", linewidth=1))
    ax.text(x + 0.35, y + 1.22, value, color=color, fontsize=27, fontweight="bold", va="center")
    ax.text(x + 0.35, y + 0.55, label, color="#1C2531", fontsize=13, fontweight="bold", va="center")

fig.text(0.125, 0.02, "Source: Associated Press, 29 Sep 2026. Chart: The Willy Brief.", color="#5A697C", fontsize=10)
plt.tight_layout(rect=(0, 0.06, 1, 0.84))
fig.savefig(OUTPUT, dpi=100, facecolor="#FFFFFF")
