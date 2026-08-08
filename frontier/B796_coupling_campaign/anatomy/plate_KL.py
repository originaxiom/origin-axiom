r"""PLATE K — THE CASCADE  and  PLATE L — THE WALL.

K: the symmetry-breaking chain, drawn from cc's banked B861/B862/B876
   results.json (menus, dimensions, registerability, the winner at each
   step, the forced global form). NOT from memory.
L: the being/hearing no-go (B736): two spectra, one ON the unit circle
   and one OFF it, disjoint => the only transport map is zero.

Gate 5-Q. Visualization only. K is CONDITIONAL on the cascade's own
premises and says nothing about values; L is a proved negative.
"""
import json

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, Circle

BG = '#0d0f14'; INK = '#e8e4dc'; AMB = '#e8a15c'; BLU = '#5a9fd4'
RED = '#d64545'; MUT = '#9aa3b2'
OUT = 'frontier/B796_coupling_campaign/anatomy'
plt.rcParams['font.family'] = 'DejaVu Sans'

C = json.load(open('/tmp/casc/B861_fused_cascade_results.json'))
G = json.load(open('/tmp/casc/B862_global_form_results.json'))

# ================= PLATE K =================
fig, ax = plt.subplots(figsize=(15, 11.5), facecolor=BG)
ax.set_facecolor(BG); ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis('off')

steps = [('step1_E6', 'E₆', 78, 9.05), ('step2_SO10', 'SO(10)×U(1)', 46, 6.55),
         ('step3_SU5', 'SU(5)×U(1)', 25, 4.05)]
ax.text(5, 9.72, 'PLATE K — THE CASCADE', color=INK, fontsize=21, ha='center')
ax.text(5, 9.40, 'how one big symmetry breaks, step by step, into the shape of the '
        'Standard Model', color=MUT, fontsize=11.5, ha='center')

y_win = {}
for key, name, dim, y in steps:
    s = C[key]
    ax.text(1.15, y, name, color=INK, fontsize=15, ha='right', va='center',
            fontweight='bold')
    ax.text(1.15, y - 0.30, f'dim {dim}', color=MUT, fontsize=9.5, ha='right',
            va='center')
    menu = s['menu']
    n = len(menu)
    for i, m in enumerate(menu):
        xx = 2.35 + i * 1.95
        win = (m['option'] == s['winner'])
        reg = m['registerable']
        col = AMB if win else (BLU if reg else '#4a5262')
        ax.add_patch(plt.Rectangle((xx - 0.87, y - 0.55), 1.74, 1.02,
                                   facecolor=col, alpha=0.20 if not win else 0.34,
                                   edgecolor=col, linewidth=2.0 if win else 0.9))
        ax.text(xx, y + 0.10, m['option'], color=INK if win else MUT,
                fontsize=10.5, ha='center', fontweight='bold' if win else 'normal')
        ax.text(xx, y - 0.24, f"dim {m['dim']}" +
                ('' if reg else '   ✕ not registerable'),
                color=AMB if win else ('#7d8798' if reg else RED),
                fontsize=8.6, ha='center')
        if win:
            y_win[key] = (xx, y - 0.55)
            ax.text(xx, y + 0.62, 'WINNER — largest surviving symmetry',
                    color=AMB, fontsize=8.4, ha='center')
    ax.text(9.55, y, f"{n} options\n{sum(1 for m in menu if m['registerable'])} registerable\nunique: "
            f"{'YES' if s.get('unique') else 'no'}", color=MUT, fontsize=8.4,
            ha='right', va='center')

for (k, _, _, y), (k2, _, _, y2) in zip(steps, steps[1:]):
    x0, ybot = y_win[k]
    ax.add_patch(FancyArrowPatch((x0, ybot - 0.05), (1.15, y2 + 0.42),
                                 arrowstyle='-|>', mutation_scale=15,
                                 color=AMB, lw=1.6, alpha=0.75,
                                 connectionstyle='arc3,rad=-0.18'))
x0, ybot = y_win['step3_SU5']
ax.add_patch(FancyArrowPatch((x0, ybot - 0.05), (3.4, 2.30),
                             arrowstyle='-|>', mutation_scale=15, color=AMB,
                             lw=1.6, alpha=0.75, connectionstyle='arc3,rad=-0.18'))
ax.add_patch(plt.Rectangle((2.05, 1.28), 5.9, 1.0, facecolor=AMB, alpha=0.14,
                           edgecolor=AMB, lw=2.2))
ax.text(5.0, 1.92, G['global_form'], color=INK, fontsize=15, ha='center',
        fontweight='bold')
ax.text(5.0, 1.55, f"the Standard Model's gauge group — and its GLOBAL FORM: "
        f"the ℤ{G['kernel_order']} quotient is forced, not chosen",
        color=AMB, fontsize=9.6, ha='center')

ax.text(5.0, 0.72, 'the rule at every step: among the options that can carry chiral '
        'matter ("registerable"), take the one with the LARGEST leftover symmetry.\n'
        'it lands on the Standard Model at every step, and the choice is unique each time.',
        color=MUT, fontsize=9.6, ha='center')
ax.text(5.0, 0.20, 'HONEST STATUS: conditional on the cascade\'s own premises — it says nothing '
        'about masses, couplings, generations, the Higgs, or spacetime.\n'
        'a control run (B869) checked the rule does NOT land on the SM from arbitrary '
        'starting groups, so the result is not vacuous.',
        color='#6f7787', fontsize=8.6, ha='center', style='italic')
fig.savefig(f'{OUT}/plate_K_cascade.png', dpi=145, facecolor=BG,
            bbox_inches='tight', pad_inches=0.35)
plt.close(fig)
print('saved plate_K_cascade.png')

# ================= PLATE L =================
fig, axes = plt.subplots(1, 2, figsize=(15, 7.6), facecolor=BG)
phi = (1 + np.sqrt(5)) / 2
om = complex(-0.5, np.sqrt(3) / 2)

axL = axes[0]; axL.set_facecolor(BG)
pts = [a + b * om for a in range(-6, 7) for b in range(-6, 7)]
axL.scatter([p.real for p in pts], [p.imag for p in pts], s=17, c=BLU)
for k in range(6):
    u = np.exp(2j * np.pi * k / 6)
    axL.scatter([u.real], [u.imag], s=95, facecolors='none', edgecolors=AMB, lw=1.8)
axL.set_aspect('equal'); axL.set_xlim(-4.2, 4.2); axL.set_ylim(-4.2, 4.2)
axL.set_title('BEING — ℚ(√−3), the object\'s own geometry\n'
              'a triangular lattice; its units (circled) sit ON the unit circle',
              color=INK, fontsize=11.5, pad=10)
axL.tick_params(colors='#5a6272', labelsize=7.5)
for s in axL.spines.values(): s.set_color('#3a4150')

axR = axes[1]; axR.set_facecolor(BG)
th = np.linspace(0, 2 * np.pi, 400)
axR.plot(np.cos(th), np.sin(th), color='#3a4150', lw=1.2)
for k in range(6):
    u = np.exp(2j * np.pi * k / 6)
    axR.scatter([u.real], [u.imag], s=120, color=BLU, zorder=5)
axR.scatter([phi**2, phi**-2], [0, 0], s=150, color=AMB, marker='D', zorder=5)
axR.annotate('φ² = 2.618…', xy=(phi**2, 0), xytext=(phi**2 + 0.12, 0.42),
             color=AMB, fontsize=10)
axR.annotate('φ⁻² = 0.382…', xy=(phi**-2, 0), xytext=(phi**-2 - 0.30, -0.62),
             color=AMB, fontsize=10)
axR.annotate('the object\'s own\neigenvalues (|z| = 1)', xy=(np.cos(2), np.sin(2)),
             xytext=(-2.6, 1.5), color=BLU, fontsize=10,
             arrowprops=dict(arrowstyle='-', color=BLU, lw=0.8))
axR.axvspan(1.0, phi**2, color=RED, alpha=0.07)
axR.text((1 + phi**2) / 2, -1.35, 'no shared eigenvalue\nanywhere', color=RED,
         fontsize=9.5, ha='center')
axR.set_aspect('equal'); axR.set_xlim(-1.9, 3.3); axR.set_ylim(-1.9, 1.9)
axR.set_title('HEARING — ℚ(√5), the object\'s dynamics\n'
              'its eigenvalues φ², φ⁻² lie OFF the circle, on the real axis',
              color=INK, fontsize=11.5, pad=10)
axR.tick_params(colors='#5a6272', labelsize=7.5)
for s in axR.spines.values(): s.set_color('#3a4150')

fig.suptitle('PLATE L — THE WALL\nwhy nothing can be carried from one face of the object '
             'to the other', color=INK, fontsize=17, y=0.99)
fig.text(0.5, 0.035,
         'the map that would transport a quantity between the two faces solves a Sylvester '
         'equation, and that equation has ONLY the zero solution\n'
         'when the two spectra share no eigenvalue. one side is on the unit circle, the other '
         'is off it: disjoint, so the transport map is exactly 0.\n'
         'this is a proved negative (B736) — a wall, not a bridge. it is why the object\'s '
         'geometry cannot hand its dynamics a number.',
         color=MUT, fontsize=9.4, ha='center')
fig.tight_layout(rect=[0.01, 0.115, 0.99, 0.90])
fig.savefig(f'{OUT}/plate_L_wall.png', dpi=145, facecolor=BG)
print('saved plate_L_wall.png')
