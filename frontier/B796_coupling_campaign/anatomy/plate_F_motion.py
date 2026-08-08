r"""PLATE F — THE MOUTH IN MOTION.

The cusp of m004 (the figure-eight knot complement) is an infinite funnel.
A Maass form living in it has the Fourier expansion

    f(z, t) = sum_mu  a_mu * t * K_{ir}(2 pi |mu| t) * exp(2 pi i <mu, z>)

on the cusp torus C/Lambda, Lambda = Z + Z*tau, tau = 2 sqrt(-3).
As the height t rises the K-Bessel factor collapses exponentially: the
object's voice fades into its own infinity.

This plate takes ONE certified eigenvalue -- the INHERITED (parent /
Bianchi) one, r = 7.072004186674375, lambda = 1 + r^2 = 51.013243216 --
reconstructs its Fourier coefficients from the Hejhal collocation system,
and draws Re f on the cusp torus at six rising heights, each panel
individually normalised so the pattern survives the amplitude collapse.
Underneath: the measured max|f|(t) over 25 heights on a log axis.

Every number is computed. Nothing is drawn by hand.
Gate 5-Q. Visualization only; no claim.
"""
import json
import os
import sys
import time

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.colors import LinearSegmentedColormap  # noqa: E402
from matplotlib.gridspec import GridSpec  # noqa: E402

ROOT = '/Users/dri/oa-audit-seat/origin-axiom'
B792 = f'{ROOT}/frontier/B792_maass_m004_eigenvalues'
OUT = f'{ROOT}/frontier/B796_coupling_campaign/anatomy'
sys.path.insert(0, B792)
from hejhal_m004 import (K_table, Lattice, System, bessel_nodes,  # noqa: E402
                         build_moves, find_cusp_lattice)

plt.rcParams['font.family'] = 'DejaVu Sans'
BG = '#0d0f14'
INK = '#e8e4dc'
AMB = '#e8a15c'
BLU = '#4a90c4'
RED = '#d64545'
MUT = '#9aa3b2'
GRID = '#3a4150'

WAVE = LinearSegmentedColormap.from_list(
    'wave', ['#1b3a6b', '#2f6fa8', '#7fb2d6', '#f2ede3',
             '#e8a15c', '#c9532f', '#6b1d12'])

T0 = time.time()


def log(msg):
    print(f'[{time.time() - T0:6.1f}s] {msg}', flush=True)


# ---------------------------------------------------------------- data
# the eigenvalue, read from the certified artifact (never typed in blind)
R_WANT = 7.072004186674375
rec = None
for fn in ('eigenvalues_final.json', 'scanD_refined.json',
           'scanE_refined.json'):
    p = f'{B792}/{fn}'
    if not os.path.exists(p):
        continue
    for e in json.load(open(p))['eigenvalues']:
        if abs(e['r'] - R_WANT) < 1e-6:
            rec = dict(e)
            rec['_src'] = fn
if rec is None:
    raise SystemExit('eigenvalue r = 7.072004187 not found in artifacts')
R = rec['r']
LAM = rec['lambda']
log(f"eigenvalue r = {R!r}  lambda = {LAM!r}  type = {rec['type']!r} "
    f"mult = {rec['multiplicity']}  (from {rec['_src']})")

log('building the Hejhal system ...')
tau, _, _, _ = find_cusp_lattice()
lat = Lattice(tau)
moves = build_moves()
S = System(lat, moves, 0.75, 10.1)
TAU = abs(tau)
log(f'  tau = {tau!r}   |tau| = {TAU!r}   {len(S.mus)} Fourier modes, '
    f'{len(S.zs)} collocation points')


def eigvec(r):
    """Fourier coefficients a_mu of the form at spectral parameter r."""
    KT = K_table(S.args, S.ts, S.wts, [r], [])
    KT = KT.reshape(len(S.norms), len(S.heights))
    V = ((S.Y * KT[S.nrm_idx, 0])[None, :] * S.P0
         - (S.tstar[:, None] * KT[S.nrm_idx, 1:].T) * S.P1)
    cn = np.linalg.norm(V, axis=0)
    cn[cn == 0] = 1
    _, sv, Vh = np.linalg.svd(V / cn[None, :])
    return Vh[-1].conj() / cn, sv


a, sv = eigvec(R)
log(f'  sigma_min = {sv[-1]:.3e}   next singular value = {sv[-2]:.4f}   '
    f'(gap {sv[-2] / sv[-1]:.2e}: the null space is 1-dimensional)')

# FIXED, REPRODUCIBLE NORMALISATION so the printed amplitudes mean something:
#   ||a||_2 = 1, and the global phase pinned so that the form is REAL-valued,
#   i.e. a_{-mu} = conj(a_mu).  The SVD returns the null vector only up to an
#   arbitrary global phase; without pinning it, Re f is an arbitrary rotation
#   of the true eigenfunction.
a = a / np.linalg.norm(a)
key = {(round(m.real, 9), round(m.imag, 9)): j for j, m in enumerate(S.mus)}
NEG = np.array([key[(round(-m.real, 9), round(-m.imag, 9))] for m in S.mus])
phi = -0.5 * np.angle(np.sum(a * a[NEG]))
a = a * np.exp(1j * phi)
kmax = int(np.argmax(np.abs(a)))
if a[kmax].real < 0:
    a = -a
sym_resid = np.abs(a[NEG] - np.conj(a)).max() / np.abs(a).max()
log(f'  reality phase phi = {phi!r};  conjugate-symmetry residual '
    f'|a_-mu - conj(a_mu)|/max|a| = {sym_resid:.3e}  (f is real to this level)')

ABSMU = np.abs(S.mus)
nz = ABSMU > 1e-12
live = np.abs(a) > 1e-8 * np.abs(a).max()
MU0 = ABSMU[live & nz].min()          # slowest-decaying harmonic actually used
T_TURN = R / (2 * np.pi * MU0)        # K_{ir}(x) turning point x = r
log(f'  live harmonics: {int(live.sum())}/{len(a)};  '
    f'slowest |mu| = {MU0!r};  turning height t* = {T_TURN!r}')


# ---------------------------------------------------------------- field
def field(t, nx=220, ny=320):
    """Re f(., t) on one period of the cusp torus, plus max|f|."""
    xs = np.linspace(-0.5, 0.5, nx)
    ys = np.linspace(-TAU / 2, TAU / 2, ny)
    xmin = (2 * np.pi * ABSMU[nz] * t).min()
    ts_, wts_ = bessel_nodes(R + 1, xmin)
    Kv = K_table(2 * np.pi * ABSMU * t, ts_, wts_, [R], [])[:, 0]
    c = a * t * Kv
    keep = np.abs(c) > 0
    c = c[keep]
    mu = S.mus[keep]
    Ex = np.exp(2j * np.pi * np.outer(mu.real, xs))      # (m, nx)
    Ey = np.exp(2j * np.pi * np.outer(mu.imag, ys))      # (m, ny)
    F = Ey.T @ (c[:, None] * Ex)                          # (ny, nx)
    return xs, ys, F


PANEL_T = [0.85, 1.0, 1.2, 1.45, 1.75, 2.1]
panels = []
ref = None
for t in PANEL_T:
    xs, ys, F = field(t)
    re = F.real
    amp = np.abs(F).max()
    imag_frac = np.abs(F.imag).max() / max(amp, 1e-300)
    if ref is None:
        ref = re
    # how much the PATTERN itself has changed: normalised inner product
    rho = float(np.sum(re * ref)
                / (np.linalg.norm(re) * np.linalg.norm(ref)))
    panels.append((t, xs, ys, re, amp, rho))
    log(f'  panel t = {t:.2f}   max|f| = {amp:.6e}   '
        f'imag/|f| = {imag_frac:.2e}   shape rho vs t=0.85 = {rho:.6f}')

# ---------------------------------------------------------------- decay
TS = np.linspace(0.8, 3.0, 25)
AMPS = np.empty(len(TS))
for i, t in enumerate(TS):
    _, _, F = field(t, nx=160, ny=220)
    AMPS[i] = np.abs(F).max()
log(f'  decay curve: max|f| from {AMPS[0]:.4e} down to {AMPS[-1]:.4e} '
    f'({AMPS[0] / AMPS[-1]:.3e}x over t in [0.8, 3.0])')

# exact leading-harmonic prediction: the |mu| = MU0 shell alone.
shell = live & (np.abs(ABSMU - MU0) < 1e-9)
xs0 = np.linspace(-0.5, 0.5, 240)
ys0 = np.linspace(-TAU / 2, TAU / 2, 340)
Ex0 = np.exp(2j * np.pi * np.outer(S.mus[shell].real, xs0))
Ey0 = np.exp(2j * np.pi * np.outer(S.mus[shell].imag, ys0))
A0 = np.abs(Ey0.T @ (a[shell][:, None] * Ex0)).max()
TSF = np.linspace(0.8, 3.0, 200)
tsb, wtsb = bessel_nodes(R + 1, 2 * np.pi * MU0 * TSF.min())
K0 = K_table(2 * np.pi * MU0 * TSF, tsb, wtsb, [R], [])[:, 0]
LEAD = A0 * TSF * K0
log(f'  leading shell |mu| = {MU0:.6f} carries {int(shell.sum())} '
    f'harmonics, torus amplitude A0 = {A0:.6e}')

# how well the measured maximum is explained by that single shell
LEAD_AT = np.interp(TS, TSF, LEAD)
dev = np.abs(AMPS / LEAD_AT - 1.0)
sel = TS >= 1.5
log(f'  measured/predicted: max relative deviation for t >= 1.5 is '
    f'{dev[sel].max():.3e}; over all 25 heights {dev.max():.3e}')

# local log-slope of the exact leading curve at the right edge (not a fit)
sl_local = float(np.gradient(np.log(LEAD), TSF)[-1])
DROP = float(AMPS[0] / AMPS[-1])
log(f'  local log-slope of the exact curve at t = 3: {sl_local:.4f}; '
    f'asymptote -2*pi*|mu| = {-2 * np.pi * MU0:.4f}; total drop {DROP:.4e}x')

# ---------------------------------------------------------------- draw
fig = plt.figure(figsize=(13.8, 15.2), facecolor=BG)
gs = GridSpec(2, 6, figure=fig, height_ratios=[8.0, 3.15],
              left=0.056, right=0.986, top=0.882, bottom=0.122,
              wspace=0.07, hspace=0.19)

for i, (t, xs, ys, re, amp, rho) in enumerate(panels):
    ax = fig.add_subplot(gs[0, i])
    v = np.percentile(np.abs(re), 99.4)
    ax.imshow(re, origin='lower', cmap=WAVE, vmin=-v, vmax=v,
              extent=[xs[0], xs[-1], ys[0], ys[-1]],
              interpolation='bilinear', aspect='equal', rasterized=True)
    ax.set_facecolor(BG)
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_color(GRID)
    ax.set_title(f'height  t = {t:.2f}', color=AMB, fontsize=12.5, pad=7)
    ax.text(0.5, -0.022, f'max|f| = {amp:.2e}', transform=ax.transAxes,
            color=INK, fontsize=9.9, ha='center', va='top',
            family='DejaVu Sans Mono')
    ax.text(0.5, -0.049,
            'reference panel' if i == 0
            else f'pattern unchanged: 1−ρ = {1 - rho:.1e}',
            transform=ax.transAxes, color=MUT, fontsize=8.3,
            ha='center', va='top')
    if i == 0:
        ax.text(-0.115, 0.5, 'one period of the cusp torus'
                f'   —   1  ×  {TAU:.4f}',
                transform=ax.transAxes, color='#6e7789', fontsize=8.6,
                rotation=90, ha='center', va='center')

axd = fig.add_subplot(gs[1, :])
axd.semilogy(TSF, LEAD, color=BLU, lw=3.4, ls='-', alpha=0.95, zorder=2,
             solid_capstyle='round',
             label=(f'PREDICTED, not fitted:  A₀·t·K_{{ir}}(2π·{MU0:.4f}·t)'
                    '  — the single slowest harmonic alone'))
axd.plot(TS, AMPS, 'o', ms=6.2, color=AMB, mec=BG, mew=0.9, zorder=4,
         label='MEASURED  max|f| over the whole cusp torus  (25 heights)')
for t, _, _, _, amp, _ in panels:
    axd.plot([t], [amp], marker='s', ms=11.0, mfc='none', mec=INK, mew=1.3,
             zorder=5)
axd.plot([], [], marker='s', ms=11.0, mfc='none', mec=INK, mew=1.3, ls='none',
         label='the six panels above')
axd.axvline(T_TURN, color=RED, lw=1.0, ls=':', zorder=1)
axd.annotate(f'turning height  t* = r/(2π|μ|) = {T_TURN:.4f}\n'
             'left: the harmonic still oscillates\n'
             'right: pure exponential decay',
             xy=(T_TURN + 0.045, AMPS.min() * 28),
             color=RED, fontsize=9.0, va='center')
axd.annotate('measured and predicted agree to '
             f'{100 * dev[sel].max():.2f} %  for t ≥ 1.5\n'
             f'log-slope at t = 3 :  {sl_local:.3f}   →   '
             f'asymptote −2π|μ| = {-2 * np.pi * MU0:.3f}',
             xy=(2.15, AMPS.min() * 5.5), color=INK, fontsize=9.4,
             ha='center', va='top')
axd.set_xlim(0.78, 3.02)
axd.set_ylim(AMPS.min() / 4.5, AMPS.max() * 55)
axd.set_facecolor(BG)
axd.set_xlabel('height  t  in the cusp        (t → ∞ is the funnel’s open '
               'end — the manifold’s only infinity)',
               color=MUT, fontsize=10.5, labelpad=7)
axd.set_ylabel('max |f|   (log scale)', color=MUT, fontsize=10.5)
axd.tick_params(colors='#5a6272', labelsize=8.6, which='both')
axd.grid(True, which='major', color=GRID, lw=0.5, alpha=0.55)
axd.grid(True, which='minor', color=GRID, lw=0.35, alpha=0.28)
for s in axd.spines.values():
    s.set_color(GRID)
axd.legend(frameon=False, fontsize=9.4, labelcolor='#c8cfda',
           loc='upper right', handletextpad=0.9, borderpad=0.2)

fig.suptitle('PLATE F — THE MOUTH IN MOTION', color=INK, fontsize=20,
             y=0.982, ha='center')
fig.text(0.5, 0.9545,
         'the same standing wave, photographed six times as you climb out of '
         'the cusp: the shape holds, the loudness collapses',
         color=INK, fontsize=13.2, ha='center')
fig.text(0.5, 0.9265,
         f'm004 (figure-eight knot complement)  ·  the INHERITED mode  '
         f'r = {R:.9f},  λ = 1 + r² = {LAM:.9f}  ·  '
         f'cusp torus ℂ/(ℤ+ℤτ), τ = 2√−3 = {TAU:.7f}i',
         color=MUT, fontsize=10.2, ha='center')
fig.text(0.5, 0.9055,
         f'{len(S.mus)} Fourier harmonics from {len(S.zs)} collocation '
         f'points at Y = 0.75  ·  σ_min = {sv[-1]:.2e} against next singular '
         f'value {sv[-2]:.3f}  ·  coefficients fixed by ‖a‖₂ = 1 and '
         'a₋μ = conj(aμ)',
         color='#6e7789', fontsize=9.0, ha='center')

fig.text(0.5, 0.021,
         'each panel is the SAME solution of Δf = λf, seen at a different '
         'height inside the manifold’s one infinite funnel; each is '
         're-brightened on its own so the pattern stays visible.\n'
         'the true loudness is printed under each: over a climb of 2.2 units '
         f'the wave becomes about {DROP:,.0f}× quieter, along a curve that is '
         'not fitted to the data but predicted outright by its slowest '
         'harmonic.\n'
         'this is the object’s voice falling away into its own infinity — '
         'and the reason a cusped manifold has a discrete spectrum at all.',
         color=MUT, fontsize=9.8, ha='center', va='bottom', linespacing=1.55)

path = f'{OUT}/plate_F_motion.png'
fig.savefig(path, dpi=145, facecolor=BG)
plt.close(fig)
log(f'saved {path}  ({os.path.getsize(path) / 1024:.0f} KB)')

# ------------------------------------------------- animation frames
for i, (t, xs, ys, re, amp, rho) in enumerate(panels):
    f2 = plt.figure(figsize=(3.0, 9.4), facecolor=BG)
    ax = f2.add_axes([0.06, 0.075, 0.88, 0.845])
    v = np.percentile(np.abs(re), 99.4)
    ax.imshow(re, origin='lower', cmap=WAVE, vmin=-v, vmax=v,
              extent=[xs[0], xs[-1], ys[0], ys[-1]],
              interpolation='bilinear', aspect='equal', rasterized=True)
    ax.set_facecolor(BG)
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_color(GRID)
    ax.set_title(f't = {t:.2f}', color=AMB, fontsize=13, pad=8)
    f2.text(0.5, 0.032, f'max|f| = {amp:.2e}', color=INK, fontsize=10,
            ha='center', family='DejaVu Sans Mono')
    fp = f'{OUT}/plate_F_frame_{i}.png'
    f2.savefig(fp, dpi=145, facecolor=BG)
    plt.close(f2)
    log(f'  frame {i}: {fp}  ({os.path.getsize(fp) / 1024:.0f} KB)')

# ------------------------------------------------- machine-readable log
json.dump({
    'plate': 'F — THE MOUTH IN MOTION',
    'manifold': 'm004',
    'eigenvalue': {'r': R, 'lambda': LAM, 'type': rec['type'],
                   'multiplicity': rec['multiplicity'],
                   'source_file': rec['_src']},
    'system': {'Y': 0.75, 'rmax': 10.1, 'n_modes': len(S.mus),
               'n_points': int(len(S.zs)), 'tau_imag': TAU,
               'sigma_min': float(sv[-1]), 'sigma_next': float(sv[-2])},
    'normalisation': ('a / ||a||_2; global phase pinned by a_{-mu} = '
                      'conj(a_mu) so f is real-valued'),
    'conj_symmetry_residual': float(sym_resid),
    'panels': [{'t': t, 'max_abs_f': float(amp), 'shape_rho_vs_t0': rho}
               for t, _, _, _, amp, rho in panels],
    'decay': {'t': TS.tolist(), 'max_abs_f': AMPS.tolist()},
    'leading_shell': {'abs_mu': float(MU0), 'n_harmonics': int(shell.sum()),
                      'A0': float(A0), 'turning_height': float(T_TURN)},
    'measured_vs_predicted_max_rel_dev_t_ge_1p5': float(dev[sel].max()),
    'measured_vs_predicted_max_rel_dev_all': float(dev.max()),
    'log_slope_of_exact_curve_at_t3': sl_local,
    'bessel_asymptote_rate': float(-2 * np.pi * MU0),
    'total_drop_0p8_to_3p0': DROP,
}, open(f'{OUT}/plate_F_data.json', 'w'), indent=1)
log('DONE')
