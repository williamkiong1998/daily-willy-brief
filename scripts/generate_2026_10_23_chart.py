from pathlib import Path
import os

import matplotlib.pyplot as plt
from matplotlib import font_manager


OUTPUT = Path(__file__).resolve().parents[1] / "assets" / "2026-10-23-chart.png"


def main():
    satoshi_dir = Path(os.environ.get("SATOSHI_DIR", "/nonexistent"))
    medium = satoshi_dir / "Satoshi-Medium.otf"
    bold = satoshi_dir / "Satoshi-Bold.otf"
    if medium.exists() and bold.exists():
        font_manager.fontManager.addfont(medium)
        font_manager.fontManager.addfont(bold)
        regular_font = font_manager.FontProperties(fname=medium)
        bold_font = font_manager.FontProperties(fname=bold)
    else:
        regular_font = font_manager.FontProperties(family="DejaVu Sans")
        bold_font = font_manager.FontProperties(family="DejaVu Sans", weight="bold")
    plt.rcParams.update({"font.family": regular_font.get_name()})
    fig, ax = plt.subplots(figsize=(12, 6.75), dpi=100)
    fig.patch.set_facecolor("#FFFFFF")
    ax.set_facecolor("#FFFFFF")

    labels = ["S&P 500", "Nasdaq\nComposite"]
    values = [-1.21, -2.60]
    bars = ax.bar(labels, values, color=["#94ACCB", "#6D90B9"], width=0.48)
    ax.axhline(0, color="#5A697C", linewidth=1.2)
    for bar, value in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, value - 0.13, f"{value:.2f}%",
                ha="center", va="top", color="#1C2531", fontsize=24, fontproperties=bold_font)

    ax.set_ylim(-3.2, 0.45)
    ax.set_yticks([-3, -2, -1, 0])
    ax.set_yticklabels(["-3%", "-2%", "-1%", "0%"], color="#5A697C", fontsize=12)
    ax.tick_params(axis="x", colors="#1C2531", labelsize=16, length=0)
    ax.tick_params(axis="y", length=0)
    ax.grid(axis="y", color="#BBC7DC", linewidth=0.8)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_visible(False)

    fig.text(0.08, 0.93, "AI doubts hit the tech-heavy index twice as hard", fontsize=28,
             fontproperties=bold_font, color="#1C2531")
    fig.text(0.08, 0.875, "US index moves on 22 October 2026", fontsize=15,
             fontproperties=regular_font, color="#5A697C")
    fig.text(0.08, 0.035, "Source: Reuters, via Yahoo Finance, 22 October 2026", fontsize=10,
             fontproperties=regular_font, color="#5A697C")
    plt.subplots_adjust(left=0.10, right=0.94, top=0.80, bottom=0.16)
    fig.savefig(OUTPUT, facecolor="#FFFFFF")


if __name__ == "__main__":
    main()
