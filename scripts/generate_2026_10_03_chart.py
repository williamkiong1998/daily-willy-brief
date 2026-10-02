import os
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib import font_manager


OUTPUT = Path(__file__).resolve().parents[1] / "assets" / "2026-10-03-chart.png"

font_dir = Path(os.environ.get("SATOSHI_FONT_DIR", ""))
font_family = "DejaVu Sans"
if font_dir.is_dir():
    for font_path in (font_dir / "Satoshi-Medium.otf", font_dir / "Satoshi-Bold.otf"):
        if font_path.is_file():
            font_manager.fontManager.addfont(font_path)
    font_family = font_manager.FontProperties(fname=font_dir / "Satoshi-Medium.otf").get_name()

plt.rcParams.update({"font.family": font_family, "font.size": 14})
fig, ax = plt.subplots(figsize=(12, 6.75), dpi=100)
fig.patch.set_facecolor("#FFFFFF")
ax.set_facecolor("#FFFFFF")

labels = ["S&P 500", "Nasdaq Composite"]
values = [-0.3, 0.5]
bars = ax.bar(labels, values, color=["#94ACCB", "#6D90B9"], width=0.48)
ax.axhline(0, color="#BBC7DC", linewidth=1)
ax.set_ylim(-0.55, 0.75)
ax.set_ylabel("Weekly change (%)", color="#5A697C", fontsize=12)
ax.set_title("Tech carried the tape while the broad market slipped", loc="left", color="#1C2531", fontsize=22, fontweight="bold", pad=18)
ax.text(0.0, 0.63, "The Nasdaq gained 0.5% this week; the S&P 500 lost 0.3%.", color="#5A697C", fontsize=12)
ax.grid(axis="y", color="#BBC7DC", linewidth=0.8)
ax.set_axisbelow(True)
ax.spines[["top", "right", "left"]].set_visible(False)
ax.spines["bottom"].set_color("#BBC7DC")
ax.tick_params(axis="y", length=0, colors="#5A697C")
ax.tick_params(axis="x", length=0, colors="#1C2531", labelsize=14)
ax.set_yticks([-0.5, -0.25, 0, 0.25, 0.5, 0.75])
ax.set_yticklabels(["−0.5%", "−0.25%", "0%", "+0.25%", "+0.5%", "+0.75%"])
for bar, value in zip(bars, values):
    label = f"{value:+.1f}%"
    y = value + 0.07 if value >= 0 else value - 0.11
    ax.text(bar.get_x() + bar.get_width() / 2, y, label, ha="center", color="#42648A", fontsize=18, fontweight="bold")

fig.text(0.125, 0.02, "Source: Associated Press, US market close, 2 Oct 2026. Chart: The Willy Brief.", color="#5A697C", fontsize=10)
plt.tight_layout(rect=(0.05, 0.06, 0.98, 0.92))
fig.savefig(OUTPUT, dpi=100, facecolor="#FFFFFF")
