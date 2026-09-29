from pathlib import Path

import matplotlib.pyplot as plt


OUTPUT = Path(__file__).resolve().parents[1] / "assets" / "2026-09-29-chart.png"

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 14})
fig, ax = plt.subplots(figsize=(12, 6.75), dpi=100)
fig.patch.set_facecolor("#FFFFFF")
ax.set_facecolor("#FFFFFF")

layers = ["Model\ncapability", "Personal\nagent", "Business\nagent", "Developer\nAPI", "Coding\ntool"]
colors = ["#94ACCB", "#6D90B9", "#42648A", "#6D90B9", "#94ACCB"]
positions = list(range(len(layers)))

ax.barh(positions, [1] * len(layers), color=colors, height=0.58)
for y, layer in zip(positions, layers):
    ax.text(0.5, y, layer, ha="center", va="center", color="#FFFFFF", fontweight="bold", fontsize=14)

ax.set_xlim(0, 1)
ax.set_ylim(-0.8, len(layers) - 0.2)
ax.set_yticks([])
ax.set_xticks([])
ax.invert_yaxis()
for spine in ax.spines.values():
    spine.set_visible(False)
ax.set_title("An enterprise AI platform is a stack of five named surfaces", loc="left", fontsize=23, fontweight="bold", color="#1C2531", pad=18)
ax.text(0, -0.68, "Meta named these components as the initial scope of Meta Enterprise Platform—not proof of adoption or product-market fit.", color="#5A697C", fontsize=12)
fig.text(0.125, 0.02, "Source: Meta, 28 Sep 2026. Chart: The Willy Brief.", color="#5A697C", fontsize=10)
plt.tight_layout(rect=(0, 0.06, 1, 1))
fig.savefig(OUTPUT, dpi=100, facecolor="#FFFFFF")
