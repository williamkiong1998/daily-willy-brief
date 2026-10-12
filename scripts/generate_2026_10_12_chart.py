from pathlib import Path

import matplotlib.pyplot as plt


OUTPUT = Path(__file__).resolve().parents[1] / "assets" / "2026-10-12-chart.png"

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 14})
fig, ax = plt.subplots(figsize=(12, 6.75), dpi=100)
fig.patch.set_facecolor("#FFFFFF")
ax.set_facecolor("#FFFFFF")

labels = ["Original", "10% synonym edits", "25% synonym edits"]
values = [92, 66, 17]
bars = ax.bar(labels, values, width=0.56, color=["#6D90B9", "#94ACCB", "#5A697C"])
ax.set_ylim(0, 100)
ax.set_yticks([0, 25, 50, 75, 100])
ax.set_yticklabels(["0%", "25%", "50%", "75%", "100%"], color="#5A697C")
ax.tick_params(axis="x", length=0, colors="#1C2531", labelsize=15)
ax.tick_params(axis="y", length=0)
ax.grid(axis="y", color="#BBC7DC", linewidth=0.8)
ax.set_axisbelow(True)
ax.spines[["top", "right", "left", "bottom"]].set_visible(False)

for bar, value in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width() / 2, value + 3, f"{value}%",
            va="bottom", ha="center", color="#42648A", fontsize=20, fontweight="bold")

ax.set_title("A little rewriting can erase most of a text watermark signal", loc="left",
             color="#1C2531", fontsize=19, fontweight="bold", pad=22)
ax.set_ylabel("Watermark detection rate", color="#5A697C", labelpad=12)
fig.text(0.125, 0.04,
         "Source: OpenAI textGrain evaluation, 5 Oct 2026. 400-token passages; 1% false-positive target.",
         color="#5A697C", fontsize=10)
plt.tight_layout(rect=(0.05, 0.08, 0.98, 0.93))
fig.savefig(OUTPUT, dpi=100, facecolor="#FFFFFF")
