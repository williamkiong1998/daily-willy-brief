import matplotlib.pyplot as plt

COLORS = {
    "ink": "#1C2531",
    "accent": "#6D90B9",
    "secondary": "#94ACCB",
    "muted": "#5A697C",
    "border": "#BBC7DC",
}

labels = ["S&P 500", "Nasdaq", "Brent crude"]
values = [-0.4, -0.8, 2.9]
colors = [COLORS["secondary"], COLORS["secondary"], COLORS["accent"]]

fig, ax = plt.subplots(figsize=(12, 6.75), dpi=100)
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

bars = ax.bar(labels, values, color=colors, width=0.54)
ax.axhline(0, color=COLORS["border"], linewidth=1.2)
ax.yaxis.grid(True, color="#EBEFF4", linewidth=1)
ax.xaxis.grid(False)
ax.set_axisbelow(True)
ax.set_ylim(-1.35, 3.55)
ax.set_yticks([-1, 0, 1, 2, 3])
ax.set_yticklabels(["-1%", "0%", "1%", "2%", "3%"], color=COLORS["muted"], fontsize=12)
ax.tick_params(axis="x", colors=COLORS["ink"], labelsize=14, length=0, pad=12)
ax.tick_params(axis="y", length=0)
for spine in ax.spines.values():
    spine.set_visible(False)

for bar, value in zip(bars, values):
    y = value - 0.18 if value < 0 else value + 0.14
    va = "top" if value < 0 else "bottom"
    ax.text(bar.get_x() + bar.get_width() / 2, y, f"{value:+.1f}%", ha="center", va=va,
            color=COLORS["ink"], fontsize=18, fontweight="bold")

fig.text(0.08, 0.93, "Energy and yields put the squeeze on risk assets", fontsize=25,
         fontweight="bold", color=COLORS["ink"])
fig.text(0.08, 0.885, "Tuesday, 15 September 2026 — daily change", fontsize=13, color=COLORS["muted"])
fig.text(0.08, 0.045, "Source: Associated Press. S&P 500 and Nasdaq Composite closes; Brent settlement.",
         fontsize=10, color=COLORS["muted"])
plt.subplots_adjust(left=0.10, right=0.96, top=0.81, bottom=0.17)
plt.savefig("assets/2026-09-16-chart.png", dpi=100)
