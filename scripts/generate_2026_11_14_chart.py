"""Render the 14 November 2026 market-close comparison chart."""

from pathlib import Path
from urllib.request import urlretrieve
import zipfile

import matplotlib.pyplot as plt
from matplotlib import font_manager


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "2026-11-14-chart.png"
FONT_ZIP = Path("/tmp/satoshi-fontshare.zip")


def load_satoshi() -> tuple[font_manager.FontProperties, font_manager.FontProperties]:
    """Attempt the requested Fontshare family, then use a reliable sans fallback."""
    try:
        urlretrieve("https://api.fontshare.com/v2/fonts/download/satoshi", FONT_ZIP)
        with zipfile.ZipFile(FONT_ZIP) as archive:
            archive.extractall("/tmp/satoshi-fontshare")
        root = Path("/tmp/satoshi-fontshare")
        bold = next(root.rglob("Satoshi-Bold.ttf"))
        medium = next(root.rglob("Satoshi-Medium.ttf"))
        font_manager.fontManager.addfont(str(bold))
        font_manager.fontManager.addfont(str(medium))
        return (
            font_manager.FontProperties(fname=str(bold)),
            font_manager.FontProperties(fname=str(medium)),
        )
    except Exception:
        pass
    return (
        font_manager.FontProperties(family="DejaVu Sans", weight="bold"),
        font_manager.FontProperties(family="DejaVu Sans", weight="medium"),
    )


FONT_BOLD, FONT_MEDIUM = load_satoshi()

fig, ax = plt.subplots(figsize=(12, 6.75), dpi=100)
fig.patch.set_facecolor("#FFFFFF")
ax.set_facecolor("#FFFFFF")

labels = ["S&P 500", "Nasdaq Composite"]
changes = [-0.405, -0.906]
bars = ax.bar(labels, changes, width=0.52, color=["#94ACCB", "#6D90B9"])

ax.axhline(0, color="#BBC7DC", linewidth=1)
ax.yaxis.grid(True, color="#EBEFF4", linewidth=1)
ax.set_axisbelow(True)
ax.spines[["top", "right", "left", "bottom"]].set_visible(False)
ax.set_ylim(-1.15, 0.15)
ax.set_yticks([-1.0, -0.75, -0.5, -0.25, 0])
ax.set_yticklabels(["-1.00%", "-0.75%", "-0.50%", "-0.25%", "0%"], color="#5A697C", fontsize=12, fontproperties=FONT_MEDIUM)
ax.tick_params(axis="x", length=0, colors="#1C2531", labelsize=14, pad=12)
ax.tick_params(axis="y", length=0)

for bar, value in zip(bars, changes):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        value - 0.065,
        f"{value:.3f}%",
        ha="center",
        va="top",
        color="#1C2531",
        fontsize=18,
        fontproperties=FONT_BOLD,
    )

fig.text(0.08, 0.92, "Tech selling hit harder than the broad market", fontsize=25, fontproperties=FONT_BOLD, color="#1C2531")
fig.text(0.08, 0.865, "One-day change at the US close, Friday 13 November 2026", fontsize=13, fontproperties=FONT_MEDIUM, color="#5A697C")
fig.text(0.08, 0.055, "Source: Yahoo Finance chart data; Reuters via Free Malaysia Today", fontsize=10, fontproperties=FONT_MEDIUM, color="#5A697C")
plt.subplots_adjust(left=0.12, right=0.94, top=0.78, bottom=0.16)
fig.savefig(OUTPUT, facecolor="#FFFFFF")
