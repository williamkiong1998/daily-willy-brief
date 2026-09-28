from pathlib import Path
import matplotlib.pyplot as plt

OUTPUT = Path(__file__).resolve().parents[1] / "assets" / "2026-09-28-chart.png"

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 15})
fig, ax = plt.subplots(figsize=(12, 6.75), dpi=100)
fig.patch.set_facecolor("#FFFFFF")
ax.set_facecolor("#FFFFFF")

indices = ["S&P 500", "Nasdaq Composite"]
changes = [0.51, 0.48]
bars = ax.bar(indices, changes, color=["#6D90B9", "#94ACCB"], width=0.55)
ax.set_ylim(0, 0.70)
ax.set_ylabel("Daily change (%)", color="#5A697C")
ax.set_title("Friday's AI-led bounce lifted both headline indices", loc="left", fontsize=23, fontweight="bold", color="#1C2531", pad=18)
ax.grid(axis="y", color="#BBC7DC", linewidth=0.8)
ax.set_axisbelow(True)
for spine in ["top", "right", "left"]:
    ax.spines[spine].set_visible(False)
ax.spines["bottom"].set_color("#BBC7DC")
ax.tick_params(axis="x", colors="#1C2531", length=0)
ax.tick_params(axis="y", colors="#5A697C", length=0)
for bar, value, close in zip(bars, changes, ["7,743.41", "27,068.72"]):
    ax.text(bar.get_x() + bar.get_width() / 2, value + 0.025, f"+{value:.2f}%\n{close}", ha="center", va="bottom", color="#1C2531", fontweight="bold")
fig.text(0.125, 0.02, "Source: Portfolio Terminal, 25 Sep 2026 close. Chart: The Willy Brief.", color="#5A697C", fontsize=10)
plt.tight_layout(rect=(0, 0.06, 1, 1))
fig.savefig(OUTPUT, dpi=100, facecolor="#FFFFFF")
