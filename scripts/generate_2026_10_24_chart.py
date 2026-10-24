from pathlib import Path
import os

import matplotlib.pyplot as plt
from matplotlib import font_manager


OUTPUT = Path(__file__).resolve().parents[1] / "assets" / "2026-10-24-chart.png"


def fonts():
    satoshi_dir = Path(os.environ.get("SATOSHI_DIR", "/nonexistent"))
    medium = satoshi_dir / "Satoshi-Medium.otf"
    bold = satoshi_dir / "Satoshi-Bold.otf"
    if medium.exists() and bold.exists():
        font_manager.fontManager.addfont(medium)
        font_manager.fontManager.addfont(bold)
        return font_manager.FontProperties(fname=medium), font_manager.FontProperties(fname=bold)
    return (font_manager.FontProperties(family="DejaVu Sans"),
            font_manager.FontProperties(family="DejaVu Sans", weight="bold"))


def main():
    regular, bold = fonts()
    fig, ax = plt.subplots(figsize=(12, 6.75), dpi=100)
    fig.patch.set_facecolor("#FFFFFF")
    ax.set_facecolor("#FFFFFF")
    labels = ["Chelsea v\nMan Utd", "Bournemouth v\nLeeds", "Brentford v\nNott'm Forest", "Coventry v\nSunderland"]
    ratings = [4, 3, 3, 2]
    bars = ax.bar(labels, ratings, color=["#6D90B9", "#94ACCB", "#94ACCB", "#94ACCB"], width=0.56)
    for bar, rating in zip(bars, ratings):
        ax.text(bar.get_x() + bar.get_width() / 2, rating + 0.10, f"{rating}/5", ha="center", va="bottom", color="#1C2531", fontsize=20, fontproperties=bold)
    ax.set_ylim(0, 5.1)
    ax.set_yticks(range(0, 6))
    ax.set_yticklabels([str(value) for value in range(0, 6)], color="#5A697C", fontsize=12)
    ax.tick_params(axis="x", colors="#1C2531", labelsize=15, length=0, pad=11)
    ax.tick_params(axis="y", length=0)
    ax.grid(axis="y", color="#BBC7DC", linewidth=0.8)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_visible(False)
    fig.text(0.08, 0.93, "Manchester United's next trip is the round's hardest listed test", fontsize=24, fontproperties=bold, color="#1C2531")
    fig.text(0.08, 0.875, "Fantasy Premier League fixture-difficulty ratings, 31 October 2026", fontsize=15, fontproperties=regular, color="#5A697C")
    fig.text(0.08, 0.035, "Source: Fantasy Premier League fixtures and team feed, accessed 24 October 2026", fontsize=10, fontproperties=regular, color="#5A697C")
    plt.subplots_adjust(left=0.09, right=0.96, top=0.79, bottom=0.20)
    fig.savefig(OUTPUT, facecolor="#FFFFFF")


if __name__ == "__main__":
    main()
