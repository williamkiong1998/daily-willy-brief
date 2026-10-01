from pathlib import Path

import matplotlib.pyplot as plt


OUTPUT = Path(__file__).resolve().parents[1] / "assets" / "2026-10-01-chart.png"

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 14})
fig, ax = plt.subplots(figsize=(12, 6.75), dpi=100)
fig.patch.set_facecolor("#FFFFFF")
ax.set_facecolor("#FFFFFF")

models = ["Sonnet 5", "Sonnet 5.5"]
scores = [10.3, 70.6]
bars = ax.bar(models, scores, color=["#94ACCB", "#6D90B9"], width=0.48)
ax.set_ylim(0, 82)
ax.set_ylabel("Terminal-Bench 4.0 score (%)", color="#5A697C", fontsize=12)
ax.set_title("The model improved; the work still needs context", loc="left", color="#1C2531", fontsize=22, fontweight="bold", pad=18)
ax.text(0, 76.5, "Anthropic reports a 60.3-point jump on an agentic coding benchmark.", color="#5A697C", fontsize=12)
ax.grid(axis="y", color="#BBC7DC", linewidth=0.8)
ax.set_axisbelow(True)
ax.spines[["top", "right", "left"]].set_visible(False)
ax.spines["bottom"].set_color("#BBC7DC")
ax.tick_params(axis="y", length=0, colors="#5A697C")
ax.tick_params(axis="x", length=0, colors="#1C2531", labelsize=14)
for bar, score in zip(bars, scores):
    ax.text(bar.get_x() + bar.get_width() / 2, score + 2, f"{score:.1f}%", ha="center", color="#42648A", fontsize=18, fontweight="bold")
fig.text(0.125, 0.02, "Source: Anthropic, Claude Sonnet 5.5, 28 Sep 2026. Chart: The Willy Brief.", color="#5A697C", fontsize=10)
plt.tight_layout(rect=(0.05, 0.06, 0.98, 0.92))
fig.savefig(OUTPUT, dpi=100, facecolor="#FFFFFF")
