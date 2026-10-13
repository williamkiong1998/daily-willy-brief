from pathlib import Path

import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "2026-10-13-chart.png"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 14,
})

fig, ax = plt.subplots(figsize=(12, 6.75), dpi=100)
fig.patch.set_facecolor("#FFFFFF")
ax.set_facecolor("#FFFFFF")

labels = ["S&P 500", "Nasdaq Composite"]
changes = [-0.1, -0.4]
colors = ["#94ACCB", "#6D90B9"]
bars = ax.bar(labels, changes, color=colors, width=0.5)

ax.axhline(0, color="#BBC7DC", linewidth=1)
ax.yaxis.grid(True, color="#EBEFF4", linewidth=1)
ax.set_axisbelow(True)
ax.set_ylim(-0.55, 0.16)
ax.set_yticks([-0.5, -0.25, 0])
ax.set_yticklabels(["-0.5%", "-0.25%", "0%"], color="#5A697C")
ax.tick_params(axis="x", colors="#1C2531", labelsize=15, length=0)
ax.tick_params(axis="y", length=0)
for spine in ax.spines.values():
    spine.set_visible(False)

for bar, value in zip(bars, changes):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        value - 0.045,
        f"{value:.1f}%",
        ha="center",
        va="top",
        color="#1C2531",
        fontweight="bold",
        fontsize=20,
    )

fig.text(0.08, 0.92, "THE TECH WEIGHT SHOWED UP", fontsize=27, fontweight="bold", color="#1C2531")
fig.text(0.08, 0.865, "Monday's modest index move hid a sharper retreat in the Nasdaq.", fontsize=15, color="#42648A")
fig.text(0.08, 0.045, "Source: Associated Press, 12 Oct 2026. Percentage change for the session.", fontsize=10, color="#5A697C")
plt.subplots_adjust(left=0.11, right=0.94, top=0.77, bottom=0.18)
plt.savefig(OUTPUT, dpi=100, facecolor="#FFFFFF")
