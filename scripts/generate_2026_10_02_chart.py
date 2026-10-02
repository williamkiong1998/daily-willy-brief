from pathlib import Path

import matplotlib.pyplot as plt


OUTPUT = Path(__file__).resolve().parents[1] / "assets" / "2026-10-02-chart.png"

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 14})
fig, ax = plt.subplots(figsize=(12, 6.75), dpi=100)
fig.patch.set_facecolor("#FFFFFF")
ax.set_facecolor("#FFFFFF")
labels = ["Previous limit", "Gemini 4 Argon"]
values = [64_000, 1_000_000]
bars = ax.bar(labels, values, color=["#94ACCB", "#6D90B9"], width=0.48)
ax.set_ylim(0, 1_180_000)
ax.set_ylabel("Maximum output tokens", color="#5A697C", fontsize=12)
ax.set_title("A larger context window creates a larger review surface", loc="left", color="#1C2531", fontsize=22, fontweight="bold", pad=18)
ax.text(0, 1_095_000, "Google says Gemini 4 Argon raises the output limit from 64K to 1M tokens.", color="#5A697C", fontsize=12)
ax.grid(axis="y", color="#BBC7DC", linewidth=0.8)
ax.set_axisbelow(True)
ax.spines[["top", "right", "left"]].set_visible(False)
ax.spines["bottom"].set_color("#BBC7DC")
ax.tick_params(axis="y", length=0, colors="#5A697C")
ax.tick_params(axis="x", length=0, colors="#1C2531", labelsize=14)
ax.set_yticks([0, 250_000, 500_000, 750_000, 1_000_000])
ax.set_yticklabels(["0", "250K", "500K", "750K", "1M"])
for bar, value in zip(bars, values):
    label = "64K" if value == 64_000 else "1M"
    ax.text(bar.get_x() + bar.get_width() / 2, value + 40_000, label, ha="center", color="#42648A", fontsize=18, fontweight="bold")
ax.annotate("15.6×", xy=(1, 1_000_000), xytext=(0.52, 905_000), color="#42648A", fontsize=16, fontweight="bold", arrowprops={"arrowstyle": "-", "color": "#42648A"})
fig.text(0.125, 0.02, "Source: Google, Gemini 4 Argon, 30 Sep 2026. Chart: The Willy Brief.", color="#5A697C", fontsize=10)
plt.tight_layout(rect=(0.05, 0.06, 0.98, 0.92))
fig.savefig(OUTPUT, dpi=100, facecolor="#FFFFFF")
