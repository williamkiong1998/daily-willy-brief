from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

ROOT = Path(__file__).resolve().parents[1]
font_dir = Path('/private/tmp/willy-brief-satoshi/Satoshi_Complete/Fonts/OTF')
title_font = FontProperties(fname=font_dir / 'Satoshi-Bold.otf')
body_font = FontProperties(fname=font_dir / 'Satoshi-Medium.otf')

labels = ['July', 'August']
values = [4.8, 5.4]
colors = ['#94ACCB', '#6D90B9']

fig, ax = plt.subplots(figsize=(12, 6.75), dpi=100)
fig.patch.set_facecolor('#FFFFFF')
ax.set_facecolor('#FFFFFF')
bars = ax.bar(labels, values, color=colors, width=0.52)

ax.set_ylim(0, 6.3)
ax.set_yticks([0, 2, 4, 6])
ax.set_yticklabels(['0%', '2%', '4%', '6%'], fontproperties=body_font, color='#5A697C', fontsize=13)
ax.grid(axis='y', color='#BBC7DC', linewidth=1, alpha=0.65)
ax.set_axisbelow(True)
for spine in ax.spines.values():
    spine.set_visible(False)
ax.tick_params(axis='x', length=0, pad=14)
ax.tick_params(axis='y', length=0, pad=10)
for label in ax.get_xticklabels():
    label.set_fontproperties(body_font)
    label.set_color('#1C2531')
    label.set_fontsize(16)

for bar, value in zip(bars, values):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        value + 0.14,
        f'{value:.1f}%',
        ha='center', va='bottom', color='#1C2531',
        fontproperties=title_font, fontsize=26,
    )

fig.text(0.08, 0.93, 'US wholesale inflation accelerated in August',
         fontproperties=title_font, fontsize=30, color='#1C2531')
fig.text(0.08, 0.875, 'Year-over-year change in producer prices',
         fontproperties=body_font, fontsize=15, color='#42648A')
fig.text(0.08, 0.045,
         'Source: Associated Press, citing the September 10 US wholesale-price report',
         fontproperties=body_font, fontsize=10, color='#5A697C')

plt.subplots_adjust(left=0.10, right=0.95, top=0.80, bottom=0.16)
fig.savefig(ROOT / 'assets/2026-09-11-chart.png', dpi=100, facecolor='#FFFFFF')
