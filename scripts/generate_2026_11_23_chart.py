from pathlib import Path
from zipfile import ZipFile

import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
FONT_DIR = Path('/tmp/satoshi-2026-11-23')
ZIP = Path('/tmp/satoshi.zip')

if ZIP.exists() and not FONT_DIR.exists():
    with ZipFile(ZIP) as archive:
        archive.extractall(FONT_DIR)

fonts = list(FONT_DIR.rglob('Satoshi-Medium.ttf'))
font_bold = list(FONT_DIR.rglob('Satoshi-Bold.ttf'))
medium = fm.FontProperties(fname=str(fonts[0])) if fonts else fm.FontProperties(family='DejaVu Sans')
bold = fm.FontProperties(fname=str(font_bold[0])) if font_bold else fm.FontProperties(family='DejaVu Sans', weight='bold')

labels = ['Exports', 'Imports', 'Trade surplus']
values = [239.2, 197.4, 41.8]
colors = ['#6D90B9', '#94ACCB', '#5A697C']

fig, ax = plt.subplots(figsize=(12, 6.75), dpi=100)
fig.patch.set_facecolor('#FFFFFF')
ax.set_facecolor('#FFFFFF')
bars = ax.bar(labels, values, color=colors, width=0.56)
ax.set_ylim(0, 280)
ax.set_yticks(np.arange(0, 281, 70))
ax.set_yticklabels([f'RM {n}bn' for n in range(0, 281, 70)], fontproperties=medium, color='#5A697C', fontsize=12)
ax.tick_params(axis='x', length=0, pad=12)
for tick in ax.get_xticklabels():
    tick.set_fontproperties(bold)
    tick.set_color('#1C2531')
    tick.set_fontsize(14)
ax.grid(axis='y', color='#BBC7DC', linewidth=0.8)
ax.set_axisbelow(True)
for spine in ax.spines.values():
    spine.set_visible(False)
for bar, value in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width()/2, value + 8, f'RM {value:.1f}bn', ha='center', va='bottom', fontproperties=bold, fontsize=15, color='#1C2531')
fig.text(0.08, 0.94, 'Malaysia’s October exports cleared RM 200bn again', fontproperties=bold, fontsize=25, color='#1C2531')
fig.text(0.08, 0.885, 'Trade hit a record RM 436.6bn as E&E demand drove the strongest growth.', fontproperties=medium, fontsize=14, color='#5A697C')
fig.text(0.08, 0.035, 'Source: Department of Statistics Malaysia, October 2026 external trade statistics.', fontproperties=medium, fontsize=10, color='#5A697C')
plt.subplots_adjust(left=0.11, right=0.95, top=0.80, bottom=0.16)
fig.savefig(ROOT / 'assets/2026-11-23-chart.png', facecolor='#FFFFFF')
