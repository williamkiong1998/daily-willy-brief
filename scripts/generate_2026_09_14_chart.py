import os
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.font_manager import FontProperties
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "2026-09-14-chart.png"
FONT_DIR = Path(os.environ.get("WILLY_BRIEF_FONT_DIR", ""))
medium_path = FONT_DIR / "Satoshi-Medium.otf"
bold_path = FONT_DIR / "Satoshi-Bold.otf"
if medium_path.exists():
    font_manager.fontManager.addfont(medium_path)
if bold_path.exists():
    font_manager.fontManager.addfont(bold_path)
medium = FontProperties(fname=medium_path) if medium_path.exists() else FontProperties(family="DejaVu Sans")
bold = FontProperties(fname=bold_path) if bold_path.exists() else FontProperties(family="DejaVu Sans", weight="bold")

days = ["Wed\n9 Sep", "Thu\n10 Sep", "Fri\n11 Sep"]
sp500 = [-0.5, -0.6, 0.9]
nasdaq = [-0.6, -0.7, 1.0]
x = np.arange(len(days))
width = 0.32

plt.rcParams.update({"font.family": medium.get_name(), "font.size": 12})
fig, ax = plt.subplots(figsize=(12, 6.75), dpi=100)
fig.patch.set_facecolor("#FFFFFF")
ax.set_facecolor("#FFFFFF")

bars1 = ax.bar(x - width / 2, sp500, width, label="S&P 500", color="#6D90B9")
bars2 = ax.bar(x + width / 2, nasdaq, width, label="Nasdaq Composite", color="#94ACCB")
ax.axhline(0, color="#5A697C", linewidth=1)
ax.yaxis.grid(True, color="#EBEFF4", linewidth=1)
ax.set_axisbelow(True)
for spine in ax.spines.values():
    spine.set_visible(False)
ax.set_xticks(x, days)
ax.set_ylabel("Daily change (%)", color="#5A697C")
ax.tick_params(colors="#5A697C")
ax.set_ylim(-1.05, 1.3)
ax.set_title("Friday erased the daily slide — not the week’s risk", loc="left", fontsize=22, fontproperties=bold, color="#1C2531", pad=22)
ax.legend(frameon=False, ncol=2, loc="upper left", bbox_to_anchor=(0, 1.01))

for bars in (bars1, bars2):
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height + (0.07 if height >= 0 else -0.12), f"{height:+.1f}%", ha="center", va="bottom" if height >= 0 else "top", color="#1C2531", fontsize=11, fontproperties=bold)

fig.text(0.08, 0.035, "Source: Associated Press market reports, 9–11 September 2026.", color="#5A697C", fontsize=10)
plt.tight_layout(rect=(0.04, 0.07, 0.98, 0.96))
fig.savefig(OUT, facecolor="#FFFFFF")
