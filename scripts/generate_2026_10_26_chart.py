from pathlib import Path
import os

import matplotlib.pyplot as plt
from matplotlib import font_manager


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "2026-10-26-chart.png"


def load_fonts():
    font_dir = Path(os.environ.get("SATOSHI_DIR", ""))
    medium = font_dir / "Satoshi-Medium.ttf"
    bold = font_dir / "Satoshi-Bold.ttf"
    if medium.exists() and bold.exists():
        font_manager.fontManager.addfont(medium)
        font_manager.fontManager.addfont(bold)
        return font_manager.FontProperties(fname=medium), font_manager.FontProperties(fname=bold)
    return font_manager.FontProperties(family="DejaVu Sans"), font_manager.FontProperties(
        family="DejaVu Sans", weight="bold"
    )


def main():
    regular, bold = load_fonts()
    labels = ["Mon\n19 Oct", "Tue\n20 Oct", "Wed\n21 Oct", "Thu\n22 Oct", "Fri\n23 Oct"]
    sp500 = [100.0, 100.3, 100.9, 99.6, 99.1]
    nasdaq = [100.0, 100.0, 101.0, 98.4, 98.2]

    fig, ax = plt.subplots(figsize=(12, 6.75), dpi=100)
    fig.patch.set_facecolor("#FFFFFF")
    ax.set_facecolor("#FFFFFF")
    ax.plot(labels, sp500, color="#6D90B9", linewidth=3.5, marker="o", markersize=7, label="S&P 500")
    ax.plot(labels, nasdaq, color="#94ACCB", linewidth=3.5, marker="o", markersize=7, label="Nasdaq Composite")
    ax.axhline(100, color="#BBC7DC", linewidth=1)
    ax.set_ylim(97.6, 101.5)
    ax.set_yticks([98, 99, 100, 101])
    ax.set_yticklabels(["98", "99", "100", "101"], color="#5A697C", fontsize=12, fontproperties=regular)
    ax.tick_params(axis="x", colors="#1C2531", labelsize=12, length=0, pad=12)
    ax.tick_params(axis="y", length=0)
    ax.grid(axis="y", color="#BBC7DC", linewidth=0.8)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_visible(False)
    legend = ax.legend(loc="lower left", frameon=False, ncol=2, bbox_to_anchor=(0, 1.02))
    for text in legend.get_texts():
        text.set_color("#1C2531")
        text.set_fontproperties(regular)
        text.set_fontsize(13)
    fig.text(0.08, 0.94, "A late-week slide erased the Nasdaq's early gain", fontsize=24, fontproperties=bold, color="#1C2531")
    fig.text(0.08, 0.885, "Indexed to 100 at the 19 October close; latest completed US session was Friday", fontsize=15, fontproperties=regular, color="#5A697C")
    fig.text(0.08, 0.035, "Source: Yahoo Finance chart data for ^GSPC and ^IXIC, accessed 26 October 2026", fontsize=10, fontproperties=regular, color="#5A697C")
    plt.subplots_adjust(left=0.09, right=0.96, top=0.75, bottom=0.18)
    fig.savefig(OUTPUT, facecolor="#FFFFFF")


if __name__ == "__main__":
    main()
