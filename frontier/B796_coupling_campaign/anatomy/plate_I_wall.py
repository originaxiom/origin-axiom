r"""PLATE I — THE WALL.

The negative, rendered. m004's certified spectrum was run against the
18 banked PDG targets under a sealed pre-registration (c6954bfa); the
answer was a clean null at every level. This plate draws that null
instead of asserting it.

Everything here is recomputed from the branch's own artifacts:
  - the 17 certified eigenvalues (eigenvalues_final + scanD_refined,
    filtered by mode_count_certification.json, dr <= 1e-6)
  - frontier/B743_rung1_widened/pdg_targets.json (18 targets)
  - the prereg's OWN surrogate ensemble: numpy default_rng(31), 500
    Weyl-distributed spectra (density ~ r^2 over the observed window,
    same count). RNG(31) is consumed by the ensemble first in
    sm_comparison_tests.py, so the ensemble here is bit-identical, and
    the script ASSERTS that its recomputed per-target p_null reproduces
    the sealed run's published values in sm_comparison_results.json.

Gate 5-Q. Visualization of a banked negative; no claim.
"""
import json

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec

B792 = 'frontier/B792_maass_m004_eigenvalues'
OUT = 'frontier/B796_coupling_campaign/anatomy'

BG = '#0d0f14'
INK = '#e8e4dc'
AMBER = '#e8a15c'
BLUE = '#4a90c4'
RED = '#d64545'
MUTED = '#9aa3b2'
GRID = '#3a4150'
plt.rcParams['font.family'] = 'DejaVu Sans'

# ---------------------------------------------------------------- data
eigs = []
for fn in ('eigenvalues_final.json', 'scanD_refined.json'):
    with open(f'{B792}/{fn}') as f:
        eigs += [e['r'] for e in json.load(f)['eigenvalues']]
rs_all = sorted(set(round(r, 9) for r in eigs))

with open(f'{B792}/mode_count_certification.json') as f:
    cert = json.load(f)
cert_map = {round(row['r_banked'], 9): row['dr'] for row in cert['rows']}
rs = np.array([r for r in rs_all if cert_map.get(r, 1.0) <= 1e-6])
max_rel_dr = max(cert_map[r] / r for r in rs)
lams = 1 + rs * rs
assert len(rs) == 17, len(rs)

with open('frontier/B743_rung1_widened/pdg_targets.json') as f:
    targets = json.load(f)
assert len(targets) == 18, len(targets)

with open(f'{B792}/sm_comparison_results.json') as f:
    sealed = json.load(f)
assert sealed['clean_null'] is True
assert sealed['n_eigenvalues'] == 17

N_REAL = len(sealed['test1']) + len(sealed['test2'])          # 2 + 39 = 41
assert not any(c['gated'] for c in sealed['test1'] + sealed['test2'])


def tol_for(tg):
    return max(2 * tg['rel_unc'], 1e-8, 10 * max_rel_dr)


# ------------------------------------------- the prereg's own ensemble
NSURR = 500
RNG = np.random.default_rng(31)
r_lo, r_hi = rs[0], rs[-1]


def weyl_draw(n):
    u = RNG.uniform(r_lo ** 3, r_hi ** 3, n)
    return np.sort(u ** (1 / 3))


SURR = [weyl_draw(len(rs)) for _ in range(NSURR)]


def candidate_count(s):
    """total Test-1 + Test-2 candidates for one spectrum, all 18 targets."""
    sl = 1 + s * s
    off = ~np.eye(len(s), dtype=bool)
    rr = (s[:, None] / s[None, :])[off]
    ll = (sl[:, None] / sl[None, :])[off]
    n = 0
    for tg in targets:
        v = float(tg['value'])
        tau = tol_for(tg)
        for arr in (s, sl, rr, ll):
            n += int(np.count_nonzero(np.abs(arr / v - 1) < tau))
    return n


counts = np.array([candidate_count(s) for s in SURR])
n_obj = candidate_count(rs)
assert n_obj == N_REAL, (n_obj, N_REAL)   # our pipeline == the sealed run
pct = float((counts < n_obj).mean() * 100)

# ---- recompute the sealed per-target p_null and CHECK it reproduces ----
pub = {}
for c in sealed['test1']:
    pub.setdefault(c['target'], {})['t1'] = c['p_null']
for c in sealed['test2']:
    pub.setdefault(c['target'], {})['t2'] = c['p_null']

rows = []
for tg in targets:
    v = float(tg['value'])
    tau = tol_for(tg)
    h1 = h2 = 0
    for s in SURR:
        sl = 1 + s * s
        off = ~np.eye(len(s), dtype=bool)
        if np.any(np.abs(s / v - 1) < tau) or np.any(np.abs(sl / v - 1) < tau):
            h1 += 1
        rr = (s[:, None] / s[None, :])[off]
        ll = (sl[:, None] / sl[None, :])[off]
        if np.any(np.abs(rr / v - 1) < tau) or np.any(np.abs(ll / v - 1) < tau):
            h2 += 1
    p1, p2 = h1 / NSURR, h2 / NSURR
    if tg['name'] in pub:
        got = pub[tg['name']]
        if 't1' in got:
            assert abs(got['t1'] - p1) < 1e-12, (tg['name'], got['t1'], p1)
        if 't2' in got:
            assert abs(got['t2'] - p2) < 1e-12, (tg['name'], got['t2'], p2)
        rows.append((tg['name'], max(p1, p2),
                     sum(1 for c in sealed['test1'] + sealed['test2']
                         if c['target'] == tg['name'])))
rows.sort(key=lambda t: t[1])
print(f'ensemble reproduces the sealed run exactly; object count = {n_obj}, '
      f'surrogate median = {np.median(counts):.0f}, percentile = {pct:.1f}')

GATE = 0.02   # B743 Gate 3

# ------------------------------------------------------------- figure
fig = plt.figure(figsize=(15.0, 12.6), facecolor=BG)
gs = GridSpec(2, 2, figure=fig, height_ratios=[1.0, 0.72],
              hspace=0.30, wspace=0.20,
              left=0.062, right=0.968, top=0.855, bottom=0.115)

# ---- panel 1: the object is not special ----
ax = fig.add_subplot(gs[0, 0])
ax.set_facecolor(BG)
bins = np.arange(counts.min() - 0.5, counts.max() + 2.5, 2)
ax.hist(counts, bins=bins, color=BLUE, alpha=0.62, edgecolor=BG, linewidth=0.5)
ax.axvline(n_obj, color=AMBER, lw=2.4, zorder=6)
sfx = {1: 'st', 2: 'nd', 3: 'rd'}.get(
    round(pct) % 10 if round(pct) % 100 not in (11, 12, 13) else 0, 'th')
ax.annotate(f'the object\n{n_obj} near-hits\n{pct:.0f}{sfx} percentile',
            xy=(n_obj, ax.get_ylim()[1] * 0.86),
            xytext=(n_obj + 0.10 * (counts.max() - counts.min()),
                    ax.get_ylim()[1] * 0.86),
            color=AMBER, fontsize=10.2, va='center',
            arrowprops=dict(arrowstyle='-', color=AMBER, lw=0.9))
ax.axvline(np.median(counts), color=MUTED, lw=1.0, ls=(0, (4, 3)), zorder=5)
ax.text(np.median(counts) - 1.5, ax.get_ylim()[1] * 0.99,
        f'random median {np.median(counts):.0f}  ', color=MUTED, fontsize=8.8,
        va='top', ha='right')
ax.set_xlabel('near-hits on the 18 PDG targets  (direct + all pairwise ratios)',
              color=MUTED, fontsize=9.6)
ax.set_ylabel('how many random spectra', color=MUTED, fontsize=9.6)
ax.tick_params(colors='#5a6272', labelsize=8.5)
for s in ax.spines.values():
    s.set_color(GRID)
ax.set_title('1.  the object against 500 random spectra of its own shape',
             color=INK, fontsize=11.6, pad=9, loc='left')

# ---- panel 2: every candidate fails the gate ----
ax = fig.add_subplot(gs[0, 1])
ax.set_facecolor(BG)
ys = np.arange(len(rows))
names = [r[0] for r in rows]
ps = [r[1] for r in rows]
ns = [r[2] for r in rows]
ax.barh(ys, ps, height=0.56, color=AMBER, alpha=0.85, edgecolor='none')
for y, p, n in zip(ys, ps, ns):
    ax.text(p + 0.012, y, f'p = {p:.3f}   ({n} candidate{"s" if n > 1 else ""})',
            color=MUTED, fontsize=8.9, va='center')
ax.axvline(GATE, color=RED, lw=1.6, ls=(0, (5, 3)), zorder=6)
ax.text(GATE + 0.020, len(rows) - 1.30, 'GATE  p < 0.02\n(B743 Gate 3)',
        color=RED, fontsize=9.0, va='top')
ax.set_yticks(ys)
ax.set_yticklabels(names, color=INK, fontsize=9.6)
ax.set_xlim(0, 1.30)
ax.set_xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
ax.set_xlabel('probability a RANDOM spectrum also hits this target',
              color=MUTED, fontsize=9.6)
ax.tick_params(colors='#5a6272', labelsize=8.5)
for s in ax.spines.values():
    s.set_color(GRID)
ax.set_title('2.  the five targets that produced a near-hit — and why none counts',
             color=INK, fontsize=11.6, pad=9, loc='left')

# ---- panel 3: the ledger ----
ax = fig.add_subplot(gs[1, :])
ax.set_facecolor(BG)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xticks([])
ax.set_yticks([])
for s in ax.spines.values():
    s.set_color(GRID)

ax.text(0.018, 0.935, 'THE LEDGER OF NULLS', color=INK, fontsize=11.4,
        va='top', weight='bold')
LED = [
    ('TEST 1   direct match', 'r_n and λ_n vs 18 targets',
     '2 candidates', '0 gated'),
    ('TEST 2   ratios', 'all 272 r-ratios and 272 λ-ratios',
     '39 candidates', '0 gated'),
    ('TEST 3   algebraicity', 'PSLQ, 6 bases incl. ℚ(√5), 8 digits',
     '0 relations', 'null rate 0.00'),
]
y = 0.775
for a, b, c, d in LED:
    ax.text(0.030, y, a, color=INK, fontsize=10.0, va='center')
    ax.text(0.200, y, b, color=MUTED, fontsize=9.2, va='center')
    ax.text(0.462, y, c, color=AMBER, fontsize=10.0, va='center')
    ax.text(0.575, y, d, color=RED, fontsize=10.0, va='center', weight='bold')
    y -= 0.145
ax.plot([0.028, 0.672], [y + 0.062, y + 0.062], color=GRID, lw=0.8)
ax.text(0.030, y + 0.010,
        'VERDICT (sealed prereg c6954bfa):  no SM value is reachable from this '
        'spectral set at 8-digit\nprecision under the stated base-rate control.  '
        'n = 17 certified eigenvalues, r ≤ 9.84.\nA GENERIC-SPECTRUM null.',
        color=INK, fontsize=9.7, va='top', linespacing=1.5)

ax.plot([0.694, 0.694], [0.10, 0.93], color=GRID, lw=0.8)
ax.text(0.716, 0.935, 'THE STRUCTURAL WALL  (B727 self-audit)',
        color=INK, fontsize=9.9, va='top', weight='bold')
ax.text(0.716, 0.840,
        '•  ℚ(√−3) can reach no exceptional label but E₆ —\n'
        '   E₇ forces √2, E₈ forces √5, both real.\n'
        '   There was never a draw to win.\n\n'
        '•  4 of 13 hyperbolic knots surject onto 2T,\n'
        '   including the NON-arithmetic 7₂, 7₃, 8₁.\n\n'
        '•  the sister m003 carries the same field, and\n'
        '   is not even a knot in S³ (H₁ = ℤ/5 ⊕ ℤ).\n\n'
        'The recurrence is forced, not evidence.',
        color=MUTED, fontsize=9.1, va='top', linespacing=1.55)

ax.text(0.030, 0.070,
        'STILL OPEN, UNTESTED, IN BOTH DIRECTIONS:  deep precision (20+ digits) '
        'and deep algebraicity (50+ digits).\n8-digit PSLQ excludes only '
        'low-height relations.',
        color='#6f7889', fontsize=8.8, va='center', style='italic',
        linespacing=1.5)

fig.suptitle('PLATE I — THE WALL\nwhat the object does not contain, measured '
             'rather than assumed',
             color=INK, fontsize=17, y=0.965, ha='center')
fig.text(0.5, 0.045,
         'The programme asked whether the shape of this knot’s absence '
         'encodes the constants of physics. It ran the question as a sealed '
         'experiment and the answer came back no.\n'
         'Forty-one numerical coincidences turned up — and 500 spectra drawn at '
         'random produced just as many. Coincidence at this density is what any '
         'spectrum does; it is not a signal.\n'
         'This plate is the negative result, and in this repository the negative '
         'is the deliverable.',
         color=MUTED, fontsize=9.7, ha='center', linespacing=1.6)

fig.savefig(f'{OUT}/plate_I_wall.png', dpi=145, facecolor=BG)
plt.close(fig)
print('saved plate I')
