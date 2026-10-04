import os
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib import font_manager


OUTPUT = Path(__file__).resolve().parents[1] / "assets" / "2026-10-04-chart.png"

font_dir = Path(os.environ.get("SATOSHI_FONT_DIR", ""))
font_family = "DejaVu Sans"
if font_dir.is_dir():
    medium = font_dir / "Satoshi-Medium.otf"
    bold = font_dir / "Satoshi-Bold.otf"
    if medium.is_file() and bold.is_file():
        font_manager.fontManager.addfont(medium)
        font_manager.fontManager.addfont(bold)
        font_family = font_manager.FontProperties(fname=medium).get_name()

plt.rcParams.update({"font.family": font_family, "font.size": 14})
fig, ax = plt.subplots(figsize=(12, 6.75), dpi=100)
fig.patch.set_facecolor("#FFFFFF")
ax.set_facecolor("#FFFFFF")

commitment = 10_000
ax.barh(["Per planned FDE"], [commitment], height=0.38, color="#6D90B9")
ax.set_xlim(0, 12_000)
ax.set_xticks([0, 3_000, 6_000, 9_000, 12_000])
ax.set_xticklabels(["$0", "$3k", "$6k", "$9k", "$12k"], color="#5A697C")
ax.set_yticks([])
ax.grid(axis="x", color="#BBC7DC", linewidth=0.8)
ax.set_axisbelow(True)
ax.spines[["top", "right", "left", "bottom"]].set_visible(False)
ax.tick_params(axis="x", length=0)
ax.set_title("Anthropic’s FDE programme implies $10,000 per planned engineer", loc="left", color="#1C2531", fontsize=18, fontweight="bold", pad=22)
ax.text(0, 0.33, "$100m commitment ÷ 10,000 FDE target through 2027", color="#5A697C", fontsize=13)
ax.text(commitment + 180, 0, "$10,000", va="center", color="#42648A", fontsize=24, fontweight="bold")
fig.text(0.125, 0.04, "Source: Anthropic, 2 Oct 2026. Calculation: The Willy Brief.", color="#5A697C", fontsize=10)
plt.tight_layout(rect=(0.05, 0.08, 0.98, 0.93))
fig.savefig(OUTPUT, dpi=100, facecolor="#FFFFFF")
