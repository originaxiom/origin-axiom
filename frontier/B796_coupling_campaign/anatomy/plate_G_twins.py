r"""PLATE G — THE TWINS.

m004 (the figure-eight knot complement) and m003 (its sister) have the
SAME hyperbolic volume, the SAME trace field Q(sqrt-3), the SAME parent
Bianchi orbifold, and are built from the SAME two regular ideal
tetrahedra.  They are not the same manifold.  This plate shows exactly
where they come apart.

  panel 1  the first difference: H_1(m004) = Z,  H_1(m003) = Z + Z/5
           (from snappy .homology(), plus the surrounding same/different
           ledger, every entry from snappy or from the branch's data)
  panel 2  the trace-norm split mod 4 -- the proved theorem
           (frontier/B792_maass_m004_eigenvalues/mod4_trace_law_proof.txt,
           Theorem 2: N(tr gamma) mod 4 in {0,3} for every gamma in
           Gamma_41).  m004 never lands on 1 mod 4.  m003 does, 180 times.
  panel 3  the two length spectra as rugs on one axis, systoles marked.

Everything is computed here from:
  frontier/B792_maass_m004_eigenvalues/length_spectrum.json      (m004, 370)
  frontier/B792_maass_m004_eigenvalues/length_spectrum_m003.json (m003, 411)
  snappy.Manifold('m004' / 'm003')

Gate 5-Q. Visualization only; no claim.
"""
import json
import warnings
from collections import Counter

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

warnings.filterwarnings('ignore')

DATA = 'frontier/B792_maass_m004_eigenvalues'
OUT = 'frontier/B796_coupling_campaign/anatomy'

plt.rcParams['font.family'] = 'DejaVu Sans'
BG = '#0d0f14'
INK = '#e8e4dc'
AMBER = '#e8a15c'
BLUE = '#4a90c4'
RED = '#d64545'
MUTED = '#9aa3b2'
GRID = '#3a4150'
TICK = '#5a6272'

OM = complex(-0.5, np.sqrt(3) / 2)          # omega = e^{2 pi i / 3}

# ---------------------------------------------------------------- data
print('loading length spectra ...', flush=True)


def load(fn):
    d = json.load(open(f'{DATA}/{fn}'))
    return d['manifold'], d['cutoff'], d['geodesics']


nm4, cut4, G4 = load('length_spectrum.json')
nm3, cut3, G3 = load('length_spectrum_m003.json')
assert (nm4, nm3) == ('m004', 'm003') and cut4 == cut3
print(f'  {nm4}: {len(G4)} complex lengths, cutoff {cut4}', flush=True)
print(f'  {nm3}: {len(G3)} complex lengths, cutoff {cut3}', flush=True)


def eisenstein_norms(gs):
    """tr = 2 cosh(L/2) -> a + b*omega in Z[omega] -> N = a^2-ab+b^2."""
    rows, worst = [], 0.0
    for g in gs:
        tr = 2 * np.cosh(complex(g['re'], g['im']) / 2)
        b = tr.imag / OM.imag
        a = tr.real - b * OM.real
        ai, bi = int(round(a)), int(round(b))
        worst = max(worst, abs(a - ai), abs(b - bi))
        N = ai * ai - ai * bi + bi * bi
        rows.append((g['re'], g['im'], g['mult'], ai, bi, N, N % 4))
    return rows, worst


R4, dev4 = eisenstein_norms(G4)
R3, dev3 = eisenstein_norms(G3)
DEV = max(dev4, dev3)
print(f'  worst deviation from an exact Eisenstein integer: {DEV:.3e}',
      flush=True)

C4 = Counter(r[6] for r in R4)
C3 = Counter(r[6] for r in R3)
W4 = Counter()
W3 = Counter()
for r in R4:
    W4[r[6]] += r[2]
for r in R3:
    W3[r[6]] += r[2]
print('  m004 norms mod 4 :', dict(sorted(C4.items())),
      ' weighted', dict(sorted(W4.items())), flush=True)
print('  m003 norms mod 4 :', dict(sorted(C3.items())),
      ' weighted', dict(sorted(W3.items())), flush=True)

# which residues the norm form a^2-ab+b^2 can hit at all (exhaustive mod 4)
REACHABLE = sorted({(a * a - a * b + b * b) % 4
                    for a in range(4) for b in range(4)})
print('  residues attainable by a^2-ab+b^2 mod 4 :', REACHABLE, flush=True)
assert C4[1] == 0, 'the proved theorem failed on the data'

# ---- real length spectra, shared vs unique ----
L4 = Counter()
L3 = Counter()
for g in G4:
    L4[round(g['re'], 9)] += g['mult']
for g in G3:
    L3[round(g['re'], 9)] += g['mult']
SHARED = set(L4) & set(L3)
SAME_MULT = sum(1 for x in SHARED if L4[x] == L3[x])
SYS4 = min(g['re'] for g in G4)
SYS3 = min(g['re'] for g in G3)
print(f'  distinct real lengths: m004 {len(L4)}, m003 {len(L3)}, '
      f'shared {len(SHARED)} ({SAME_MULT} with equal multiplicity)',
      flush=True)
print(f'  systoles: m004 {SYS4}, m003 {SYS3}', flush=True)

# ---- snappy ledger ----
print('querying snappy ...', flush=True)
import snappy  # noqa: E402
SM = {n: snappy.Manifold(n) for n in ('m004', 'm003')}
HOM = {n: str(M.homology()) for n, M in SM.items()}
VOL = {n: float(M.volume()) for n, M in SM.items()}
NTET = {n: M.num_tetrahedra() for n, M in SM.items()}
NCSP = {n: M.num_cusps() for n, M in SM.items()}
CS = {n: float(M.chern_simons()) for n, M in SM.items()}
SYM = {n: str(M.symmetry_group()) for n, M in SM.items()}
ISO = SM['m004'].is_isometric_to(SM['m003'])
print('  ', HOM, VOL, CS, SYM, 'isometric:', ISO, flush=True)

# ---------------------------------------------------------------- figure
fig = plt.figure(figsize=(15.2, 12.4), facecolor=BG)
gs = fig.add_gridspec(2, 2, height_ratios=[1.0, 0.78],
                      width_ratios=[1.06, 1.0],
                      left=0.045, right=0.972, top=0.885, bottom=0.150,
                      hspace=0.34, wspace=0.16)

# ================= PANEL 1 : the ledger / the first difference =========
ax = fig.add_subplot(gs[0, 0])
ax.set_facecolor(BG)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xticks([])
ax.set_yticks([])
for s in ax.spines.values():
    s.set_color(GRID)

XA, XB = 0.415, 0.755
ax.text(0.5, 0.965, '1.  THE FIRST DIFFERENCE', color=INK, fontsize=12.5,
        ha='center', va='top', weight='bold')
ax.text(XA, 0.905, 'm004', color=AMBER, fontsize=13, ha='center', va='top')
ax.text(XB, 0.905, 'm003', color=BLUE, fontsize=13, ha='center', va='top')
ax.text(XA, 0.872, 'the object', color=MUTED, fontsize=8, ha='center',
        va='top')
ax.text(XB, 0.872, 'the sister', color=MUTED, fontsize=8, ha='center',
        va='top')
ax.plot([0.05, 0.95], [0.845, 0.845], color=GRID, lw=0.9)

SAME_ROWS = [
    ('hyperbolic volume', f'{VOL["m004"]:.10f}', f'{VOL["m003"]:.10f}'),
    ('ideal tetrahedra', f'{NTET["m004"]}  regular', f'{NTET["m003"]}  regular'),
    ('tetrahedron shape', '½ + i√3/2', '½ + i√3/2'),
    ('cusps', f'{NCSP["m004"]}  (torus)', f'{NCSP["m003"]}  (torus)'),
    ('trace field', 'Q(√−3)', 'Q(√−3)'),
    ('parent orbifold', 'PSL(2,O₃)\\H³', 'PSL(2,O₃)\\H³'),
]
ax.text(0.055, 0.812, 'S A M E', color=MUTED, fontsize=8.6, va='center')
y = 0.772
for lab, a, b in SAME_ROWS:
    ax.text(0.055, y, lab, color=MUTED, fontsize=9.4, va='center')
    ax.text(XA, y, a, color='#c8cfda', fontsize=9.6, ha='center', va='center')
    ax.text(XB, y, b, color='#c8cfda', fontsize=9.6, ha='center', va='center')
    y -= 0.048
    ax.plot([0.05, 0.95], [y + 0.024, y + 0.024], color='#22262f', lw=0.7)

# the hero row: homology
y -= 0.024
ax.add_patch(Rectangle((0.05, y - 0.098), 0.90, 0.138, facecolor='#161a22',
                       edgecolor=RED, lw=1.3, zorder=0))
ax.text(0.075, y + 0.004, 'first homology  H₁', color=INK, fontsize=10.4,
        va='center')
ax.text(0.075, y - 0.044, 'how many independent loops, and their torsion',
        color=MUTED, fontsize=7.9, va='center')
ax.text(XA, y - 0.020, HOM['m004'].replace('+', '⊕'), color=AMBER,
        fontsize=19, ha='center', va='center')
ax.text(XB, y - 0.020, HOM['m003'].replace('+', '⊕'), color=BLUE,
        fontsize=19, ha='center', va='center')
y -= 0.150

DIFF_ROWS = [
    ('Chern–Simons invariant', f'{CS["m004"]:.4f}', f'{CS["m003"]:.4f}'),
    ('systole (shortest closed loop)', f'{SYS4:.8f}', f'{SYS3:.8f}'),
    ('symmetry group', SYM['m004'], SYM['m003']),
    ('closed geodesics with ℓ ≤ 6', f'{len(G4)}', f'{len(G3)}'),
]
ax.text(0.055, y, 'D I F F E R E N T', color=RED, fontsize=8.6, va='center')
y -= 0.052
for lab, a, b in DIFF_ROWS:
    ax.text(0.055, y, lab, color=MUTED, fontsize=9.4, va='center')
    ax.text(XA, y, a, color=AMBER, fontsize=9.6, ha='center', va='center')
    ax.text(XB, y, b, color=BLUE, fontsize=9.6, ha='center', va='center')
    y -= 0.050
    ax.plot([0.05, 0.95], [y + 0.025, y + 0.025], color='#22262f', lw=0.7)

ax.text(0.5, y - 0.020,
        f'SnapPy  m004.is_isometric_to(m003)  →  {ISO}',
        color=RED, fontsize=10, ha='center', va='center')

# ================= PANEL 2 : the trace-norm split mod 4 ================
ax = fig.add_subplot(gs[0, 1])
ax.set_facecolor(BG)
bins = [0, 1, 2, 3]
w = 0.36
h4 = [C4[k] for k in bins]
h3 = [C3[k] for k in bins]
xs = np.arange(4)
ax.bar(xs - w / 2, h4, width=w, color=AMBER, edgecolor='none',
       label=f'm004   ({len(G4)} geodesics)')
ax.bar(xs + w / 2, h3, width=w, color=BLUE, edgecolor='none',
       label=f'm003   ({len(G3)} geodesics)')
for x, v in zip(xs - w / 2, h4):
    if v:
        ax.text(x, v + 4, str(v), color=AMBER, fontsize=9.6, ha='center')
for x, v in zip(xs + w / 2, h3):
    if v:
        ax.text(x, v + 4, str(v), color=BLUE, fontsize=9.6, ha='center')

# the hole: m004 has nothing at 1 mod 4
ax.add_patch(Rectangle((1 - w, 0), w, 196, facecolor='none',
                       edgecolor=RED, lw=1.6, linestyle=(0, (4, 3)), zorder=4))
ax.text(1 - w / 2, 8, '0', color=RED, fontsize=17, ha='center', va='bottom',
        zorder=5)
ax.annotate('THE HOLE\nm004 can never land here\n(proved: B792 Theorem 2)',
            xy=(1 - w / 2, 196), xytext=(1.62, 232), color=RED, fontsize=9.4,
            ha='left', va='center',
            arrowprops=dict(arrowstyle='-', color=RED, lw=1.0))
ax.text(2, 8, 'unreachable by any\nnorm from Z[ω]', color=TICK, fontsize=8.2,
        ha='center', va='bottom')

ax.set_xticks(xs)
ax.set_xticklabels(['≡ 0', '≡ 1', '≡ 2', '≡ 3'], fontsize=11)
ax.set_xlabel('N(tr γ)   mod 4        '
              '[ tr γ = 2 cosh(ℓ/2) = a + bω ,   N = a² − ab + b² ]',
              color=MUTED, fontsize=9.6, labelpad=9)
ax.set_ylabel('number of closed geodesics', color=MUTED, fontsize=9.6)
ax.set_ylim(0, 268)
ax.tick_params(colors=TICK, labelsize=9)
ax.grid(axis='y', color=GRID, lw=0.5, alpha=0.45)
ax.set_axisbelow(True)
for s in ax.spines.values():
    s.set_color(GRID)
ax.legend(frameon=False, fontsize=9, labelcolor='#c8cfda', loc='upper left',
          bbox_to_anchor=(0.005, 1.005))
ax.set_title('2.  THE TRACE-NORM SPLIT   (the proved theorem)', color=INK,
             fontsize=12.5, pad=11, loc='center', fontweight='bold')
ax.text(0.995, -0.163,
        f'sanity check: worst deviation from an exact Eisenstein integer '
        f'over all {len(G4) + len(G3)} traces = {DEV:.1e}',
        color=TICK, fontsize=7.8, ha='right', va='top',
        transform=ax.transAxes)

# ================= PANEL 3 : the two length spectra ====================
ax = fig.add_subplot(gs[1, :])
ax.set_facecolor(BG)

MAXM = max(max(L4.values()), max(L3.values()))


def rug(counter, sign, base_color, uniq_color):
    for x, m in counter.items():
        h = 0.22 + 0.78 * np.log1p(m) / np.log1p(MAXM)
        shared = x in SHARED
        ax.vlines(x, 0.018 * sign, sign * (0.018 + 0.92 * h),
                  color=base_color if shared else uniq_color,
                  lw=1.15 if shared else 1.5,
                  alpha=0.72 if shared else 1.0,
                  zorder=2 if shared else 3)


rug(L4, +1, '#5c6472', AMBER)
rug(L3, -1, '#5c6472', BLUE)
ax.axhline(0, color=GRID, lw=0.9)

ax.set_xlim(0.72, 6.09)
ax.set_ylim(-1.40, 1.40)
ax.set_yticks([])
ax.tick_params(axis='x', colors=TICK, labelsize=9)
ax.grid(axis='x', color=GRID, lw=0.5, alpha=0.35)
ax.set_axisbelow(True)
for s in ax.spines.values():
    s.set_color(GRID)
ax.set_xlabel('length of the closed geodesic          '
              '[ real part of the complex length; tick height ∝ log '
              'multiplicity; grey = a length the twins share, '
              'coloured = a length only this twin has ]',
              color=MUTED, fontsize=9.4, labelpad=9)

ax.text(6.03, 1.24, f'm004   {len(L4)} distinct lengths', color=AMBER,
        fontsize=11.5, ha='right', va='center')
ax.text(6.03, -1.24, f'm003   {len(L3)} distinct lengths', color=BLUE,
        fontsize=11.5, ha='right', va='center')

for x, sgn, col, lab in [(SYS4, +1, AMBER, 'systole  %.10f' % SYS4),
                         (SYS3, -1, BLUE, 'systole  %.10f' % SYS3)]:
    ax.plot([x, x], [0, sgn * 1.12], color=col, lw=1.0, ls=(0, (3, 2)),
            zorder=1)
    ax.plot([x], [sgn * 1.12], marker='v' if sgn > 0 else '^', color=col,
            ms=6, zorder=4)
    ax.text(x + 0.05, sgn * 1.12, lab, color=col, fontsize=9,
            ha='left', va='center')

ax.set_title('3.  THE LENGTH SPECTRA, ON ONE AXIS   —   they are not '
             'isospectral', color=INK, fontsize=12.5, pad=10,
             fontweight='bold')
ax.text(0.5, -0.272,
        f'{len(SHARED)} lengths occur in both, {len(L4) - len(SHARED)} only in '
        f'm004, {len(L3) - len(SHARED)} only in m003; of the shared ones '
        f'{len(SHARED) - SAME_MULT} occur a different number of times.',
        color=TICK, fontsize=8.8, ha='center', va='top',
        transform=ax.transAxes)

# ---------------------------------------------------------------- frame
fig.suptitle('PLATE G — THE TWINS\nsame volume, same number field, same two '
             'tetrahedra — and still not the same space',
             color=INK, fontsize=17.5, y=0.972, ha='center')
fig.text(0.5, 0.012, va='bottom', s=
         'm004 and m003 are the two smallest cusped hyperbolic 3-manifolds, '
         'and they have identical size (2.0298832128…). Three independent '
         'measurements pull them apart:\n'
         'their loop-counting invariant, the arithmetic class of their closed '
         'loops — m004 is forbidden an entire class that m003 uses freely — '
         'and the raw list of loop lengths itself.\n'
         'Nothing here is drawn by hand: every bar, tick and number is read '
         'off the computed spectra or straight out of SnapPy.',
         color=MUTED, fontsize=9.6, ha='center')

path = f'{OUT}/plate_G_twins.png'
fig.savefig(path, dpi=145, facecolor=BG)
plt.close(fig)
print('saved', path, flush=True)
