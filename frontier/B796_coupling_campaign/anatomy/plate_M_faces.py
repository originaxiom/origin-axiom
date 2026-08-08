r"""PLATE M — THE THREE ANATOMIES.

The programme reasons about the object's "faces". The word is defined
THREE incompatible ways in the repo and never reconciled:

  2  faces  — being / hearing            (TERMINOLOGY.md, the two hands)
  3  faces  — being / hearing / meeting  (B730, closing at a Klein-four V4)
  11 faces  — the operational anatomy    (B738 kill_graph.json, the
                                          instrument actually wired up)

Panel 3's bars are COUNTED from kill_graph.json (741 entries), not
recalled. The collision band quotes LAW_MAP.md and B730 verbatim.

Gate 5-Q. Visualization only. This plate makes no mathematical claim;
it reports a vocabulary state.
"""
import collections
import json
import subprocess

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

BG = '#0d0f14'; INK = '#e8e4dc'; AMB = '#e8a15c'; BLU = '#5a9fd4'
RED = '#d64545'; MUT = '#9aa3b2'; DIM = '#6f7787'
OUT = 'frontier/B796_coupling_campaign/anatomy'
plt.rcParams['font.family'] = 'DejaVu Sans'


def from_main(path):
    return subprocess.run(['git', 'show', f'origin/main:{path}'],
                          capture_output=True, text=True, check=True).stdout


# ---- the counts, computed from the instrument's own data ----
kg = json.loads(from_main('frontier/B738_pathfinder_compiler/kill_graph.json'))
cnt = collections.Counter()
for e in kg:
    for f in e.get('faces_consulted') or []:
        cnt[f] += 1
cnt.pop('none', None)
faces = cnt.most_common()
N_ENTRIES = len(kg)
assert len(faces) == 11, f'expected 11 faces, got {len(faces)}'

fig = plt.figure(figsize=(17, 12.8), facecolor=BG)
gs = fig.add_gridspec(2, 3, height_ratios=[1.0, 0.66], hspace=0.26, wspace=0.26,
                      left=0.045, right=0.965, top=0.815, bottom=0.055)

fig.suptitle('PLATE M — THE THREE ANATOMIES', color=INK, fontsize=22, y=0.972)
fig.text(0.5, 0.935, 'the programme says "the object has faces". the word is defined '
         'three incompatible ways, and they were never reconciled.',
         color=MUT, fontsize=12, ha='center')

# column headings, placed by hand so nothing collides with the suptitle
COLX = (0.195, 0.505, 0.815)
for cx, big, small in [
        (COLX[0], 'TWO', 'TERMINOLOGY.md — "the two hands"'),
        (COLX[1], 'THREE', 'B730 — the forced faces close at a Klein-four V₄'),
        (COLX[2], 'ELEVEN', 'B738 kill_graph.json — the anatomy wired into the instrument')]:
    fig.text(cx, 0.878, big, color=AMB, fontsize=17, ha='center', fontweight='bold')
    fig.text(cx, 0.850, small, color=MUT, fontsize=9.5, ha='center')

# ================= 1. TWO =================
ax = fig.add_subplot(gs[0, 0], facecolor=BG)
ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis('off')
ax.set_aspect('equal')

for x, name, fld, sub, col in [(2.7, 'BEING', 'ℚ(√−3)', 'geometry · holonomy\nprime 3 · 2T · E₆', BLU),
                               (7.3, 'HEARING', 'ℚ(√5)', 'dynamics · monodromy\nprime 5 · 2I · E₈', AMB)]:
    ax.add_patch(plt.Circle((x, 5.55), 1.95, facecolor=col, alpha=0.16,
                            edgecolor=col, lw=2.0))
    ax.text(x, 6.35, name, color=INK, fontsize=14, ha='center', fontweight='bold')
    ax.text(x, 5.72, fld, color=col, fontsize=13, ha='center')
    ax.text(x, 4.85, sub, color=MUT, fontsize=8.8, ha='center')
ax.text(5, 5.55, '·', color=INK, fontsize=26, ha='center', va='center')
ax.text(5, 2.75, '"one hand cannot clap"\n= the generation no-go (B685)',
        color=DIM, fontsize=9.6, ha='center', style='italic')
ax.text(5, 1.45, 'the hands are ASYMMETRIC, not a mirror:\nφ(3) = 2 prime · φ(5) = 4 composite  (B691)',
        color=DIM, fontsize=8.8, ha='center')

# ================= 2. THREE =================
ax2 = fig.add_subplot(gs[0, 1], facecolor=BG)
ax2.set_xlim(0, 10); ax2.set_ylim(0, 10); ax2.axis('off')
ax2.set_aspect('equal')

nodes = {'1': (5.0, 8.35, MUT, ''),
         'being': (2.4, 5.75, BLU, 'ℚ(√−3)\ndisc −3'),
         'hearing': (7.6, 5.75, AMB, 'ℚ(√5)\ndisc 5'),
         'meeting': (5.0, 3.15, '#b06fd4', 'ℚ(√−15)\ndisc −15')}
for a, b in [('1', 'being'), ('1', 'hearing'), ('being', 'meeting'),
             ('hearing', 'meeting'), ('1', 'meeting')]:
    x0, y0 = nodes[a][:2]; x1, y1 = nodes[b][:2]
    ax2.plot([x0, x1], [y0, y1], color='#3a4150', lw=1.1, zorder=1)
for k, (x, y, col, lab) in nodes.items():
    ax2.add_patch(plt.Circle((x, y), 0.92, facecolor=col, alpha=0.20,
                             edgecolor=col, lw=1.8, zorder=2))
    ax2.text(x, y + 0.20, k, color=INK, fontsize=11, ha='center',
             fontweight='bold', zorder=3)
    ax2.text(x, y - 0.42, lab, color=col, fontsize=8.0, ha='center', zorder=3)
ax2.text(5.0, 5.75, 'being · hearing\n= meeting', color=INK, fontsize=10,
         ha='center', va='center')
ax2.text(5, 1.15, 'Gal(ℚ(√−3, √5)/ℚ) = C₂ × C₂\n"beyond being and hearing there is exactly\n'
         'ONE more forced face — the meeting."',
         color=DIM, fontsize=9.2, ha='center', style='italic')

# ================= 3. ELEVEN =================
ax3 = fig.add_subplot(gs[0, 2], facecolor=BG)
names = [f[0] for f in faces][::-1]
vals = [f[1] for f in faces][::-1]
cols = [BLU if n == 'being' else AMB if n == 'hearing'
        else '#b06fd4' if n == 'meeting' else '#4a5262' for n in names]
ax3.barh(range(len(names)), vals, color=cols, alpha=0.85, height=0.72)
for i, (n, v) in enumerate(zip(names, vals)):
    ax3.text(v + 6, i, str(v), color=MUT, fontsize=8.6, va='center')
ax3.set_yticks(range(len(names)))
ax3.set_yticklabels(names, color=INK, fontsize=9.2)
ax3.set_xlim(0, max(vals) * 1.20)
ax3.set_facecolor(BG)
ax3.tick_params(colors='#5a6272', labelsize=8)
for s in ax3.spines.values():
    s.set_color('#3a4150')
ax3.set_xlabel(f'times consulted across {N_ENTRIES} kill-graph entries '
               f'(counted from the file, not recalled)', color=DIM, fontsize=8.4)

# ================= THE COLLISION =================
axc = fig.add_subplot(gs[1, :], facecolor=BG)
axc.set_xlim(0, 10); axc.set_ylim(0, 10); axc.axis('off')
axc.add_patch(plt.Rectangle((0.06, 3.05), 9.88, 6.75, facecolor=RED, alpha=0.055,
                            edgecolor=RED, lw=1.4))
axc.text(5, 9.10, 'THE COLLISION — both of these are banked, on main, today',
         color=RED, fontsize=13.5, ha='center', fontweight='bold')

# the two claims, held well apart; citation above, quote below, no overlap
for x, cite, quote in [
        (2.30, 'docs/LAW_MAP.md : 170',
         '"THE OBJECT\'S EMITTANCE\n(heartbeat / voice) —\na real THIRD FACE,\nsame walls"   (B735)'),
        (7.70, 'B730_forced_faces_and_cosmos / FINDINGS.md',
         '"beyond being and hearing\nthere is exactly ONE more\nforced face —\nthe MEETING."')]:
    axc.text(x, 8.18, cite, color=MUT, fontsize=8.8, ha='center')
    axc.text(x, 6.85, quote, color=INK, fontsize=10.3, ha='center', va='center',
             style='italic', linespacing=1.5)

axc.add_patch(FancyArrowPatch((4.28, 7.15), (5.72, 7.15), arrowstyle='<|-|>',
                              mutation_scale=16, color=RED, lw=2.0))
axc.text(5.0, 6.42, 'two different faces claim\nthe same third slot', color=RED,
         fontsize=9.4, ha='center', va='center')

axc.text(5, 4.62, 'and the anatomy is mostly unattached:  B805 measures  567 of 733 arcs '
         '(77%) attach to NO face,  and 6 of the 11 faces carry NO proved arc',
         color=MUT, fontsize=10.4, ha='center')
axc.text(5, 3.62, 'FAMILY is never defined as a term anywhere in the repo — it carries two '
         'unmerged meanings (the metallic bundles; B855\'s two commensurability rows).\n'
         'and no document declares the shift to reading the object as relations at all: '
         'it is reconstructible only from four arcs over five days (B803, B805/6, B855, B856).',
         color=DIM, fontsize=9.3, ha='center', va='center', linespacing=1.6)

axc.text(5, 1.72, 'WHY IT MATTERS: 24 of the 32 lead-closures in the ledger were made before '
         'that shift, and 20 of 25 change when re-read relationally.\n'
         'a closure survives the re-read exactly when its scope sentence names no manifold.',
         color=AMB, fontsize=9.9, ha='center', va='center', linespacing=1.6)

fig.savefig(f'{OUT}/plate_M_faces.png', dpi=145, facecolor=BG)
print('saved plate_M_faces.png')
print('face counts used:', faces)
