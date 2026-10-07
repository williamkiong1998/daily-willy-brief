from pathlib import Path

import matplotlib.pyplot as plt


OUTPUT = Path(__file__).resolve().parents[1] / "assets" / "2026-10-08-chart.png"

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 14})
fig, ax = plt.subplots(figsize=(12, 6.75), dpi=100)
fig.patch.set_facecolor("#FFFFFF")
ax.set_facecolor("#FFFFFF")

labels = ["GPT-5.6 Instant", "GPT-6 Instant"]
values = [100, 56]
bars = ax.barh(labels, values, height=0.42, color=["#94ACCB", "#6D90B9"])
ax.invert_yaxis()
ax.set_xlim(0, 112)
ax.set_xticks([0, 25, 50, 75, 100])
ax.set_xticklabels(["0", "25", "50", "75", "100"], color="#5A697C")
ax.tick_params(axis="y", length=0, colors="#1C2531")
ax.tick_params(axis="x", length=0)
ax.grid(axis="x", color="#BBC7DC", linewidth=0.8)
ax.set_axisbelow(True)
ax.spines[["top", "right", "left", "bottom"]].set_visible(False)

for bar, label in zip(bars, ["Baseline", "44% sooner"]):
    ax.text(bar.get_width() + 2.2, bar.get_y() + bar.get_height() / 2, label,
            va="center", color="#42648A", fontsize=20, fontweight="bold")

ax.set_title("GPT-6 starts web-search answers 44% sooner on average", loc="left",
             color="#1C2531", fontsize=18, fontweight="bold", pad=22)
ax.set_xlabel("Relative time to begin answering (GPT-5.6 Instant = 100)", color="#5A697C", labelpad=14)
fig.text(0.125, 0.04,
         "Source: OpenAI, GPT-6 and Intelligent UI for everyone, 7 Oct 2026. Relative index calculated by The Willy Brief.",
         color="#5A697C", fontsize=10)
plt.tight_layout(rect=(0.05, 0.08, 0.98, 0.93))
fig.savefig(OUTPUT, dpi=100, facecolor="#FFFFFF")
