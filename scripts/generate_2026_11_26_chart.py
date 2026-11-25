from pathlib import Path
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
FONT_DIR = ROOT / ".fonts"
for path in FONT_DIR.rglob("*.ttf"):
    fm.fontManager.addfont(str(path))

families = {font.name for font in fm.fontManager.ttflist}
font = "Satoshi" if "Satoshi" in families else "DejaVu Sans"

INK = "#1C2531"
ACCENT = "#6D90B9"
SECONDARY = "#94ACCB"
MUTED = "#5A697C"
BORDER = "#BBC7DC"

fig, ax = plt.subplots(figsize=(12, 6.75), dpi=100)
fig.patch.set_facecolor("#FFFFFF")
ax.set_facecolor("#FFFFFF")
ax.set_xlim(-0.25, 2.25)
ax.set_ylim(-0.7, 1.4)
ax.axis("off")

fig.text(0.07, 0.90, "GOOGLE'S AGENT ACCESS CLOCK HAS TWO HARD DEADLINES", fontsize=23,
         fontweight="bold", color=INK, fontname=font)
fig.text(0.07, 0.845, "MCP becomes the required path first; scaled usage starts charging later.", fontsize=12,
         color=MUTED, fontname=font)

xs = [0, 1, 2]
labels = ["24 NOV 2026", "1 FEB 2027", "1 APR 2027"]
titles = ["MCP + CLI GA", "MCP required", "Scaled tier billing"]
details = [
    "Workspace MCP servers and\nCLI begin rollout.",
    "Agentic tools must use\nMCP, not REST APIs.",
    "Higher usage above the free\nallowance becomes paid."
]

ax.plot(xs, [0, 0, 0], color=BORDER, linewidth=3, solid_capstyle="round")
for index, x in enumerate(xs):
    color = ACCENT if index < 2 else SECONDARY
    ax.scatter(x, 0, s=650, color=color, zorder=3, edgecolors="#FFFFFF", linewidths=3)
    ax.text(x, -0.32, labels[index], ha="center", va="top", fontsize=11,
            fontweight="bold", color=ACCENT, fontname=font)
    ax.text(x, 0.67, titles[index], ha="center", va="bottom", fontsize=15,
            fontweight="bold", color=INK, fontname=font)
    ax.text(x, 0.50, details[index], ha="center", va="top", fontsize=11,
            color=MUTED, fontname=font, linespacing=1.45)

fig.text(0.07, 0.075, "Source: Google Workspace Updates, 24 Nov 2026. Dates are announced rollout / enforcement milestones.",
         fontsize=10, color=MUTED, fontname=font)
plt.savefig(ROOT / "assets/2026-11-26-chart.png", dpi=100, facecolor="#FFFFFF", bbox_inches=None)
