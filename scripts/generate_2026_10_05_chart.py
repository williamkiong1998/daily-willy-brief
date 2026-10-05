import os
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib import font_manager


OUTPUT = Path(__file__).resolve().parents[1] / "assets" / "2026-10-05-chart.png"

font_dir = Path(os.environ.get("SATOSHI_FONT_DIR", ""))
font_family = "DejaVu Sans"
if font_dir.is_dir():
    medium = next(font_dir.rglob("Satoshi-Medium.otf"), None)
    bold = next(font_dir.rglob("Satoshi-Bold.otf"), None)
    if medium and bold:
        font_manager.fontManager.addfont(medium)
        font_manager.fontManager.addfont(bold)
        font_family = font_manager.FontProperties(fname=medium).get_name()

plt.rcParams.update({"font.family": font_family, "font.size": 14})
fig, ax = plt.subplots(figsize=(12, 6.75), dpi=100)
fig.patch.set_facecolor("#FFFFFF")
ax.set_facecolor("#FFFFFF")

total_parameters = 78.1
active_parameters = 3.46
bars = ax.barh(
    ["Total model weights", "Weights active per token"],
    [total_parameters, active_parameters],
    height=0.42,
    color=["#94ACCB", "#6D90B9"],
)
ax.set_xlim(0, 85)
ax.set_xticks([0, 20, 40, 60, 80])
ax.set_xticklabels(["0", "20B", "40B", "60B", "80B"], color="#5A697C")
ax.tick_params(axis="y", length=0, colors="#1C2531")
ax.tick_params(axis="x", length=0)
ax.grid(axis="x", color="#BBC7DC", linewidth=0.8)
ax.set_axisbelow(True)
ax.spines[["top", "right", "left", "bottom"]].set_visible(False)

for bar, label in zip(bars, ["78.1B", "3.46B"]):
    ax.text(
        bar.get_width() + 1.2,
        bar.get_y() + bar.get_height() / 2,
        label,
        va="center",
        color="#42648A",
        fontsize=20,
        fontweight="bold",
    )

ax.set_title(
    "Kolibri activates about 4% of its weights for each token",
    loc="left",
    color="#1C2531",
    fontsize=18,
    fontweight="bold",
    pad=22,
)
fig.text(
    0.125,
    0.04,
    "Source: Aleph Alpha Kolibri-1 model card, 3 Oct 2026. Calculation: The Willy Brief.",
    color="#5A697C",
    fontsize=10,
)
plt.tight_layout(rect=(0.05, 0.08, 0.98, 0.93))
fig.savefig(OUTPUT, dpi=100, facecolor="#FFFFFF")
