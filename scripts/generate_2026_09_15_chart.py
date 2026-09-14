import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})

dates = ["Tue\nSep 8", "Thu\nSep 10", "Fri\nSep 11", "Mon\nSep 14"]
sp500 = [-0.6, -0.6, 0.9, -0.5]
nasdaq = [-0.3, -0.7, 1.0, -0.6]
x = np.arange(len(dates))
width = 0.34

fig, ax = plt.subplots(figsize=(12, 6.75), dpi=100)
fig.patch.set_facecolor("#FFFFFF")
ax.set_facecolor("#FFFFFF")

bars_sp = ax.bar(x - width / 2, sp500, width, label="S&P 500", color="#6D90B9")
bars_nq = ax.bar(x + width / 2, nasdaq, width, label="Nasdaq Composite", color="#94ACCB")

ax.axhline(0, color="#1C2531", linewidth=1)
ax.grid(axis="y", color="#BBC7DC", linewidth=0.8, alpha=0.75)
ax.set_axisbelow(True)
ax.spines[["top", "right", "left", "bottom"]].set_visible(False)
ax.set_xticks(x, dates, color="#1C2531")
ax.tick_params(axis="y", colors="#5A697C", length=0)
ax.tick_params(axis="x", length=0)
ax.set_ylim(-1.15, 1.35)
ax.set_yticks([-1, -0.5, 0, 0.5, 1])
ax.set_yticklabels(["-1.0%", "-0.5%", "0", "+0.5%", "+1.0%"])

for bars in (bars_sp, bars_nq):
    for bar in bars:
        val = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, val + (0.07 if val >= 0 else -0.11),
                f"{val:+.1f}%", ha="center", va="bottom" if val >= 0 else "top",
                color="#1C2531", fontsize=11, fontweight="bold")

ax.set_title("Friday's relief rally did not survive Monday's AI-and-oil reset",
             loc="left", fontsize=20, fontweight="bold", color="#1C2531", pad=22)
ax.legend(loc="upper right", frameon=False, labelcolor="#1C2531")
fig.text(0.125, 0.025, "Source: Associated Press market reports, 8–14 Sep 2026. Daily percentage change.",
         fontsize=10, color="#5A697C")
plt.tight_layout(rect=[0, 0.06, 1, 1])
plt.savefig("assets/2026-09-15-chart.png", facecolor="#FFFFFF", bbox_inches=None)
