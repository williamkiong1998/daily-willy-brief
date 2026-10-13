from pathlib import Path

import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "2026-10-14-chart.png"

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 14})
fig, ax = plt.subplots(figsize=(12, 6.75), dpi=100)
fig.patch.set_facecolor("#FFFFFF")
ax.set_facecolor("#FFFFFF")

labels = ["Maia 200\n(indexed)", "Maia 300\n(expected)"]
values = [100, 140]
bars = ax.bar(labels, values, color=["#94ACCB", "#6D90B9"], width=0.52)
ax.set_ylim(0, 165)
ax.set_yticks([0, 50, 100, 150])
ax.set_yticklabels(["0", "50", "100", "150"], color="#5A697C")
ax.yaxis.grid(True, color="#EBEFF4", linewidth=1)
ax.set_axisbelow(True)
ax.tick_params(axis="x", colors="#1C2531", labelsize=15, length=0)
ax.tick_params(axis="y", length=0)
for spine in ax.spines.values():
    spine.set_visible(False)
for bar, value in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width() / 2, value + 5, f"{value}", ha="center", va="bottom", color="#1C2531", fontweight="bold", fontsize=20)

fig.text(0.08, 0.92, "MORE TOKENS, SAME POWER BUDGET", fontsize=27, fontweight="bold", color="#1C2531")
fig.text(0.08, 0.865, "Microsoft expects Maia 300 to process 40% more tokens per megawatt than Maia 200.", fontsize=15, color="#42648A")
fig.text(0.08, 0.045, "Source: Microsoft, 13 Oct 2026. Maia 200 indexed to 100; Maia 300 is company guidance.", fontsize=10, color="#5A697C")
plt.subplots_adjust(left=0.11, right=0.94, top=0.77, bottom=0.18)
plt.savefig(OUTPUT, dpi=100, facecolor="#FFFFFF")
