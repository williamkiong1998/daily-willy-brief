from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib import font_manager

dates = ["20 Oct", "21 Oct", "22 Oct", "23 Oct", "26 Oct"]
sp500 = [100.00, 100.58, 99.36, 98.85, 99.54]
nasdaq = [100.00, 101.05, 98.43, 98.22, 99.03]

font_dir = Path("/tmp/willy-brief-font/extracted/Satoshi_Complete/Fonts/WEB/fonts")
for filename in ("Satoshi-Regular.ttf", "Satoshi-Medium.ttf", "Satoshi-Bold.ttf"):
    font_manager.fontManager.addfont(font_dir / filename)
plt.rcParams["font.family"] = "Satoshi"
fig, ax = plt.subplots(figsize=(12, 6.75), dpi=100, facecolor="#FFFFFF")
ax.set_facecolor("#FFFFFF")

ax.plot(dates, sp500, color="#6D90B9", linewidth=3, marker="o", markersize=7, label="S&P 500")
ax.plot(dates, nasdaq, color="#94ACCB", linewidth=3, marker="o", markersize=7, label="Nasdaq Composite")

ax.set_title("Monday restored part of last week's AI-led slide", loc="left", fontsize=23, fontweight="bold", color="#1C2531", pad=22)
ax.text(0, 1.01, "Index level rebased to 100 at the 20 October close", transform=ax.transAxes, fontsize=12, color="#5A697C")
ax.set_ylim(97.7, 101.4)
ax.set_yticks([98, 99, 100, 101])
ax.set_yticklabels(["98", "99", "100", "101"], color="#5A697C", fontsize=11)
ax.tick_params(axis="x", colors="#5A697C", labelsize=11, length=0, pad=12)
ax.tick_params(axis="y", length=0, pad=8)
ax.grid(axis="y", color="#BBC7DC", linewidth=0.8)
ax.grid(axis="x", visible=False)
for spine in ax.spines.values():
    spine.set_visible(False)
ax.legend(frameon=False, loc="upper left", bbox_to_anchor=(0, 0.91), ncol=2, fontsize=12, labelcolor="#1C2531")
ax.text(0, -0.18, "Source: Yahoo Finance daily chart data, accessed 27 October 2026. Values rebased by The Willy Brief.", transform=ax.transAxes, fontsize=10, color="#5A697C")
fig.subplots_adjust(left=0.09, right=0.97, top=0.82, bottom=0.20)
fig.savefig(Path(__file__).resolve().parents[1] / "assets" / "2026-10-27-chart.png", facecolor="#FFFFFF")
