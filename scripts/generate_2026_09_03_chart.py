from pathlib import Path

import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
FONT_DIR = Path('/private/tmp/willy-brief-satoshi')

font_files = list(FONT_DIR.rglob('Satoshi-*.ttf')) if FONT_DIR.exists() else []
for path in font_files:
    fm.fontManager.addfont(str(path))

font_names = {Path(path).stem: fm.FontProperties(fname=str(path)).get_name() for path in font_files}
regular = font_names.get('Satoshi-Regular', 'DejaVu Sans')
bold = font_names.get('Satoshi-Bold', regular)

labels = ['SKILL.md files', 'distinct\ncontents', 'repositories']
values = [3_797_117, 1_877_981, 282_200]
colors = ['#6D90B9', '#94ACCB', '#5A697C']

fig, ax = plt.subplots(figsize=(12, 6.75), dpi=100, facecolor='#FFFFFF')
ax.set_facecolor('#FFFFFF')
bars = ax.bar(labels, values, color=colors, width=0.56)
ax.set_ylim(0, 4_450_000)
ax.set_yticks([0, 1_000_000, 2_000_000, 3_000_000, 4_000_000])
ax.set_yticklabels(['0', '1m', '2m', '3m', '4m'], fontname=regular, color='#5A697C', fontsize=11)
ax.grid(axis='y', color='#EBEFF4', linewidth=1.2)
ax.set_axisbelow(True)
for spine in ax.spines.values():
    spine.set_visible(False)
ax.tick_params(axis='x', length=0, labelsize=13, pad=12, colors='#1C2531')
ax.tick_params(axis='y', length=0)
for tick in ax.get_xticklabels():
    tick.set_fontname(bold)
for bar, value in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width() / 2, value + 105_000, f'{value / 1_000_000:.2f}m' if value >= 1_000_000 else f'{value / 1_000:.0f}k', ha='center', va='bottom', fontsize=17, fontname=bold, color='#1C2531')

fig.text(0.08, 0.93, 'Agent skills are spreading faster than the ecosystem can standardise them', fontsize=23, fontname=bold, color='#1C2531')
fig.text(0.08, 0.875, 'A July 2026 census of public GitHub repositories', fontsize=12, fontname=regular, color='#5A697C')
fig.text(0.08, 0.045, 'Source: GitSkills dataset, July 2026. Files are grouped by exact content hash.', fontsize=10, fontname=regular, color='#5A697C')
plt.subplots_adjust(left=0.10, right=0.95, top=0.80, bottom=0.18)
fig.savefig(ROOT / 'assets/2026-09-03-chart.png', dpi=100, facecolor='#FFFFFF')
