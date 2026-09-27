from pathlib import Path

import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "2026-09-27-chart.png"

plt.rcParams.update({"font.family": "DejaVu Sans"})
fig, ax = plt.subplots(figsize=(12, 6.75), dpi=100, facecolor="#FFFFFF")
ax.set_facecolor("#FFFFFF")

labels = ["S&P 500", "Nasdaq\nComposite"]
values = [0.51, 0.48]
bars = ax.bar(labels, values, color=["#6D90B9", "#94ACCB"], width=0.52)

ax.set_title("Both major US indices rose on Friday — narrowly, but together",
             loc="left", fontsize=22, fontweight="bold", color="#1C2531", pad=22)
ax.text(0, 1.02, "Percentage change at the 25 September 2026 close", transform=ax.transAxes,
        fontsize=12, color="#5A697C")
ax.set_ylim(0, 0.7)
ax.set_yticks([0, 0.2, 0.4, 0.6])
ax.set_yticklabels(["0.0%", "0.2%", "0.4%", "0.6%"], color="#5A697C")
ax.grid(axis="y", color="#BBC7DC", linewidth=0.8)
ax.set_axisbelow(True)
ax.spines[["top", "right", "left"]].set_visible(False)
ax.spines["bottom"].set_color("#BBC7DC")
ax.tick_params(axis="x", colors="#1C2531", labelsize=14, length=0, pad=10)
ax.tick_params(axis="y", length=0)

for bar, value in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width() / 2, value + 0.025, f"+{value:.2f}%",
            ha="center", va="bottom", fontsize=16, fontweight="bold", color="#42648A")

fig.text(0.125, 0.035, "Source: Gate market data, 25 September 2026. Chart: The Willy Brief.",
         fontsize=10, color="#5A697C")
plt.tight_layout(rect=[0, 0.07, 1, 1])
fig.savefig(OUT, facecolor="#FFFFFF")
