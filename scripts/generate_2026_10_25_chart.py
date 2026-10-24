from pathlib import Path
import os
import matplotlib.pyplot as plt
from matplotlib import font_manager

OUTPUT = Path(__file__).resolve().parents[1] / "assets" / "2026-10-25-chart.png"

def fonts():
    satoshi_dir = Path(os.environ.get("SATOSHI_DIR", "/nonexistent"))
    medium, bold = satoshi_dir / "Satoshi-Medium.ttf", satoshi_dir / "Satoshi-Bold.ttf"
    if medium.exists() and bold.exists():
        font_manager.fontManager.addfont(medium); font_manager.fontManager.addfont(bold)
        return font_manager.FontProperties(fname=medium), font_manager.FontProperties(fname=bold)
    return font_manager.FontProperties(family="DejaVu Sans"), font_manager.FontProperties(family="DejaVu Sans", weight="bold")

def main():
    regular, bold = fonts()
    fig, ax = plt.subplots(figsize=(12, 6.75), dpi=100)
    fig.patch.set_facecolor("#FFFFFF"); ax.set_facecolor("#FFFFFF")
    labels, scores = ["Standard K3.1", "Risk-reduced K3.1 Pro"], [90.5, 81.0]
    bars = ax.bar(labels, scores, color=["#94ACCB", "#6D90B9"], width=0.52)
    for bar, score in zip(bars, scores):
        ax.text(bar.get_x() + bar.get_width() / 2, score + 1.4, f"{score:.1f}%", ha="center", va="bottom", color="#1C2531", fontsize=22, fontproperties=bold)
    ax.set_ylim(0, 100); ax.set_yticks(range(0, 101, 20))
    ax.set_yticklabels([f"{value}%" for value in range(0, 101, 20)], color="#5A697C", fontsize=12)
    ax.tick_params(axis="x", colors="#1C2531", labelsize=15, length=0, pad=12); ax.tick_params(axis="y", length=0)
    ax.grid(axis="y", color="#BBC7DC", linewidth=0.8); ax.set_axisbelow(True)
    for spine in ax.spines.values(): spine.set_visible(False)
    fig.text(0.08, 0.93, "Moonshot reports a 9.5-point cyber-capability trade-off", fontsize=24, fontproperties=bold, color="#1C2531")
    fig.text(0.08, 0.875, "Internal controlled-environment cyber benchmark; company-reported, not independently verified", fontsize=15, fontproperties=regular, color="#5A697C")
    fig.text(0.08, 0.035, "Source: Moonshot AI claims reported by Reuters via Free Malaysia Today, accessed 25 October 2026", fontsize=10, fontproperties=regular, color="#5A697C")
    plt.subplots_adjust(left=0.09, right=0.96, top=0.79, bottom=0.20)
    fig.savefig(OUTPUT, facecolor="#FFFFFF")

if __name__ == "__main__": main()
