from pathlib import Path

import matplotlib.pyplot as plt


OUTPUT = Path(__file__).resolve().parents[1] / "assets" / "2026-10-09-chart.png"

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 14})
fig, ax = plt.subplots(figsize=(12, 6.75), dpi=100)
fig.patch.set_facecolor("#FFFFFF")
ax.set_facecolor("#FFFFFF")

labels = ["Nasdaq Composite", "Nvidia", "Broadcom", "Micron"]
values = [-1.3, -2.9, -4.3, -4.8]
bars = ax.barh(labels, values, height=0.5, color=["#94ACCB", "#6D90B9", "#6D90B9", "#6D90B9"])
ax.invert_yaxis()
ax.set_xlim(-5.6, 0.2)
ax.set_xticks([-5, -4, -3, -2, -1, 0])
ax.set_xticklabels(["-5%", "-4%", "-3%", "-2%", "-1%", "0%"], color="#5A697C")
ax.tick_params(axis="y", length=0, colors="#1C2531", labelsize=16)
ax.tick_params(axis="x", length=0)
ax.grid(axis="x", color="#BBC7DC", linewidth=0.8)
ax.set_axisbelow(True)
ax.spines[["top", "right", "left", "bottom"]].set_visible(False)

for bar, value in zip(bars, values):
    ax.text(value - 0.12, bar.get_y() + bar.get_height() / 2, f"{value:.1f}%",
            va="center", ha="right", color="#42648A", fontsize=20, fontweight="bold")

ax.set_title("AI-linked shares fell harder than the Nasdaq on Thursday", loc="left",
             color="#1C2531", fontsize=19, fontweight="bold", pad=22)
ax.set_xlabel("One-day price change, 8 October 2026", color="#5A697C", labelpad=14)
fig.text(0.125, 0.04,
         "Source: Associated Press, 8 Oct 2026. Past performance is not predictive.",
         color="#5A697C", fontsize=10)
plt.tight_layout(rect=(0.05, 0.08, 0.98, 0.93))
fig.savefig(OUTPUT, dpi=100, facecolor="#FFFFFF")
