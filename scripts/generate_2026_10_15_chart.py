from pathlib import Path

import matplotlib.pyplot as plt


OUTPUT = Path(__file__).resolve().parents[1] / "assets" / "2026-10-15-chart.png"


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(12, 6.75), dpi=100)
    fig.patch.set_facecolor("#FFFFFF")
    ax.set_facecolor("#FFFFFF")

    labels = ["Aug\n2026", "Sep\n2026"]
    values = [3.4, 3.7]
    bars = ax.bar(labels, values, color=["#94ACCB", "#6D90B9"], width=0.52)
    ax.axhline(2.0, color="#5A697C", linewidth=1.4, linestyle=(0, (4, 4)))
    ax.text(1.35, 2.07, "2% reference", color="#5A697C", fontsize=12, ha="right")

    for bar, value in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, value + 0.08, f"{value:.1f}%",
                ha="center", va="bottom", color="#1C2531", fontsize=24, fontweight="bold")

    ax.set_ylim(0, 4.35)
    ax.set_yticks([0, 1, 2, 3, 4])
    ax.set_yticklabels(["0%", "1%", "2%", "3%", "4%"], color="#5A697C", fontsize=12)
    ax.tick_params(axis="x", colors="#1C2531", labelsize=14, length=0)
    ax.tick_params(axis="y", length=0)
    ax.grid(axis="y", color="#BBC7DC", linewidth=0.8)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_visible(False)

    fig.text(0.08, 0.93, "US inflation moved further from the finish line", fontsize=28,
             fontweight="bold", color="#1C2531")
    fig.text(0.08, 0.875, "Consumer price index, year-over-year change", fontsize=15, color="#5A697C")
    fig.text(0.08, 0.035, "Source: U.S. Bureau of Labor Statistics, September 2026 CPI release", fontsize=10,
             color="#5A697C")
    plt.subplots_adjust(left=0.10, right=0.94, top=0.80, bottom=0.16)
    fig.savefig(OUTPUT, facecolor="#FFFFFF")


if __name__ == "__main__":
    main()
