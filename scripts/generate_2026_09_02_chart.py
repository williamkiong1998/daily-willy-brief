import matplotlib.pyplot as plt

COLORS = {
    "ink": "#1C2531",
    "accent": "#6D90B9",
    "secondary": "#94ACCB",
    "muted": "#5A697C",
    "grid": "#BBC7DC",
}

plt.rcParams.update({"font.family": "DejaVu Sans"})
fig, ax = plt.subplots(figsize=(12, 6.75), dpi=100)
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

labels = ["January", "September"]
values = [2.6, 8.3]
bars = ax.bar(labels, values, width=0.48, color=[COLORS["secondary"], COLORS["accent"]])

ax.set_ylim(0, 10)
ax.set_yticks([0, 2, 4, 6, 8, 10])
ax.set_yticklabels(["0×", "2×", "4×", "6×", "8×", "10×"], color=COLORS["muted"], fontsize=12)
ax.grid(axis="y", color=COLORS["grid"], linewidth=0.8, alpha=0.7)
ax.set_axisbelow(True)
for spine in ax.spines.values():
    spine.set_visible(False)
ax.tick_params(axis="x", length=0, labelsize=14, colors=COLORS["ink"])
ax.tick_params(axis="y", length=0)

for bar, value in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width()/2, value + 0.23, f"{value:.1f}×",
            ha="center", va="bottom", fontsize=22, fontweight="bold", color=COLORS["ink"])

ax.set_title("Frontier firms widened their AI-usage gap", loc="left", pad=24,
             fontsize=25, fontweight="bold", color=COLORS["ink"])
ax.text(0, 1.02, "Output tokens per active user, relative to typical firms", transform=ax.transAxes,
        fontsize=13, color=COLORS["muted"])
fig.text(0.125, 0.055, "Source: OpenAI Enterprise Signals, published 1 September 2026", fontsize=10, color=COLORS["muted"])
plt.subplots_adjust(left=0.12, right=0.96, top=0.80, bottom=0.16)
plt.savefig("assets/2026-09-02-chart.png", dpi=100, facecolor="white")
