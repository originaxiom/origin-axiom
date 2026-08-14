r"""B940 — THE SEALED DIRAC RUN on (m004, spin structure rho_1).

Binding documents (read before editing):
  * ``PREREGISTRATION.md`` in this directory (sealed 2026-08-07, sha-256
    recorded by stage ``seal`` into ``results.json``).
  * ``../B933_spinor_hejhal_design/DESIGN.md`` sections 2 (operator +
    declared choices), 3 (spin structure), 4 (cusp modes), 5 (shape gates),
    6 (collocation), 7 (certification protocol), 8 (anchor substitution),
    10 (the two-outcome criterion).

This module REUSES the B933 probe's machinery by import (lattice, moves,
pullback with tracked SL(2,C) lifts, Iwasawa twist, the trapezoid Bessel
table, the collocation system).  It never writes into the B933 directory:
banked probe artifacts stay byte-faithful.

THE SEALED CRITERION (PREREGISTRATION.md, verbatim):

    In the window |lam| <= 4, the instrument produces >= 1 eigenvalue
    passing ALL of: two-Y bar |Dlam| < 10^-9 at 10-digit working
    precision; two seeds; P4 restart spread under the sealed bar; P3
    displaced-lam control finds nothing; gates G1, G2, G2b, assembly
    cross-check pass; the +- partner is present within the same bars
    (section 5a is a theorem -- enforceable).

Stages (each dumps ``results.json`` on completion; an interruption never
loses a completed stage)::

    python3 dirac_sealed.py seal      # seal integrity + declared choices
    python3 dirac_sealed.py gates     # G1, G2, G2b, assembly cross-check
    python3 dirac_sealed.py scan      # sigma_min over |lam| <= 4, two systems
    python3 dirac_sealed.py refine    # 4 instruments, V-crossing refinement
    python3 dirac_sealed.py p4        # perturbed restarts, spread bar
    python3 dirac_sealed.py p3        # displaced-lam control (must find nothing)
    python3 dirac_sealed.py verdict   # the sealed criterion, element by element
    python3 dirac_sealed.py all       # the whole battery in order
"""
import hashlib
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
PROBE_DIR = os.path.normpath(os.path.join(HERE, '..',
                                          'B933_spinor_hejhal_design'))
sys.path.insert(0, PROBE_DIR)
import probe  # noqa: E402  (the B933 machinery, imported not copied)

RESULTS = os.path.join(HERE, 'results.json')

# ----------------------------------------------------------------
# DECLARED CHOICES (WORKING_RULES rule 4).  Every one of these is fixed
# here, before the battery runs, and echoed into results.json.
# ----------------------------------------------------------------
WINDOW = 4.0            # the sealed window |lam| <= 4
SCAN_DL = 0.01          # DESIGN section 7: grid dlam = 0.01
SCAN_DL_2 = 0.02        # second-instrument dip-list cross-check grid
MARGIN = 32.0           # Bessel truncation margin: rel. tail ~ e^-32 = 1.3e-14
OVERSAMPLE = 0.75       # rows 2*npts ~ 1.5 * nmodes
# The trapezoid quadrature for K_{i lam -+ 1/2}.  The probe used h = 0.15,
# tol_exp = 45; measured against mpmath that holds ~1e-15 RELATIVE only out
# to x ~ 30 and degrades to 1.3e-4 at x = 80 (the Poisson error term
# ~ e^{-pi(2 pi/h - lam)/2} is fixed in absolute size while K(x) ~ e^{-x}
# shrinks).  Columns are normalised before the SVD, so the large-|mu|
# columns -- whose entries are ALL exponentially small -- would be the ones
# corrupted.  h = 0.08, tol_exp = 60 restores <= 3e-15 relative accuracy
# across the whole x-range the instrument actually uses.  Declared change.
BESSEL_H = 0.08
BESSEL_TOL_EXP = 60.0
GOLDEN_HALFWIDTH = 6e-3
GOLDEN_TOL = 1e-7
VFIT_D1 = 1e-6          # V-crossing offsets (d1, 2*d1); error is O(d1^2)
VFIT_ITERS = 2
BAR_TWO_Y = 1e-9        # the ONLY numeric bar sealed in the PREREGISTRATION;
BAR_SPREAD = 1e-9       # "the sealed bar" for the P4 spread reads as the same
DIP_FACTOR = 0.5        # dip = local min with sigma < 0.5 * median sigma
CERT_FACTOR = 0.1       # a certification candidate needs sigma < 0.1 * median

# the four instruments: (label, Y, sample seed, move word length, margin)
INSTRUMENTS = [
    ('S1', 0.75, 11, 5, MARGIN),   # primary
    ('S2', 0.62, 11, 5, MARGIN),   # two-Y axis   (seed and word set fixed)
    ('S3', 0.75, 23, 5, MARGIN),   # two-seed axis (Y and word set fixed)
    ('S4', 0.68, 7, 6, MARGIN),    # word-set axis (maxlen-6 moves)
]
TRUNCATION_LADDER = [21.0, 32.0, 40.0]   # margin sensitivity gate
P3_DISPLACED = [1.0, 1.5, 2.0, 2.5, 3.5, 3.7]
P4_PERTURBATIONS = [-5e-3, -3e-3, -1e-3, 1e-3, 3e-3, 5e-3]

VOL_M004 = 2.029883212819307


# ----------------------------------------------------------------
# results.json plumbing: merge-and-dump after EVERY stage
# ----------------------------------------------------------------

def load_results():
    if os.path.exists(RESULTS):
        with open(RESULTS) as f:
            return json.load(f)
    return {}


def save_results(d):
    with open(RESULTS, 'w') as f:
        json.dump(d, f, indent=1, default=float)
    print('[results] dumped results.json')   # relative: no machine paths


def stage_dump(key, payload):
    d = load_results()
    d.setdefault('stages_completed', [])
    if key not in d['stages_completed']:
        d['stages_completed'].append(key)
    d[key] = payload
    save_results(d)


# ----------------------------------------------------------------
# The sealed system: the B933 collocation system + an exposed row
# assembly (so the mpmath cross-check tests exactly what sigma uses)
# ----------------------------------------------------------------

def sealed_bessel_nodes(lmax, xmin, h=BESSEL_H, tol_exp=BESSEL_TOL_EXP):
    """Trapezoid nodes for K_{i lam - 1/2}; tighter than the probe's."""
    T0 = np.arccosh((np.pi * lmax / 2 + tol_exp) / xmin)
    Tmax = np.arccosh((np.pi * lmax / 2 + tol_exp + T0 / 2 + 1) / xmin)
    Q = int(np.ceil(Tmax / h)) + 1
    ts = h * np.arange(Q)
    wts = np.full(Q, h)
    wts[0] = h / 2
    return ts, wts


class SealedSystem(probe.SpinSystem):
    """B933 SpinSystem, sealed quadrature, raw row block exposed."""

    def __init__(self, lat, moves, Y, lmax, **kw):
        super().__init__(lat, moves, Y, lmax, **kw)
        # rebuild the Bessel table on the sealed (tighter) quadrature
        args = 2 * np.pi * np.outer(self.norms, self.heights)
        self.arg_shape = args.shape
        flat = args.ravel()
        self.x_min, self.x_max = float(flat.min()), float(flat.max())
        self.ts, self.wts = sealed_bessel_nodes(lmax, self.x_min)
        self.E = np.exp(-np.outer(flat, np.cosh(self.ts)))

    def rows(self, lam):
        """The 2*npts x nmodes block  psi_mu(x*_j) - conj(k_j) psi_mu(x_j)."""
        # two REAL mat-vecs against the (large) real table E: a single
        # complex mat-vec would promote E to complex128 and copy it on
        # every evaluation.  Bit-for-bit the same result.
        kc = probe.K_column(self.ts, self.wts, lam)
        K = (self.E @ np.ascontiguousarray(kc.real)
             + 1j * (self.E @ np.ascontiguousarray(kc.imag))
             ).reshape(self.arg_shape)
        K1Y = K[self.nrm_idx, 0]
        K1s = K[self.nrm_idx, 1:]
        Y32 = self.Y ** 1.5
        t32 = self.tstar ** 1.5
        c1x = Y32 * K1Y[None, :] * self.P0
        c2x = Y32 * (self.theta_fac * np.conj(K1Y))[None, :] * self.P0
        c1s = t32[:, None] * K1s.T * self.P1
        c2s = (t32[:, None] * (self.theta_fac[None, :] * np.conj(K1s.T))
               * self.P1)
        k = self.ks
        R1 = c1s - (k[:, 0, 0][:, None] * c1x + k[:, 0, 1][:, None] * c2x)
        R2 = c2s - (k[:, 1, 0][:, None] * c1x + k[:, 1, 1][:, None] * c2x)
        return np.vstack([R1, R2])

    def sigma(self, lam, nsv=3):
        V = self.rows(lam)
        cn = np.linalg.norm(V, axis=0)
        cn[cn == 0] = 1.0
        sv = np.linalg.svd(V / cn[None, :], compute_uv=False)
        return sv[-nsv:][::-1]


_CACHE = {}


def get_lattice_and_moves(maxlen):
    key = ('lm', maxlen)
    if key not in _CACHE:
        tau, w0, nfound, nbad = probe.find_cusp_lattice()
        lat = probe.SpinLattice(tau)
        _CACHE[key] = (lat, probe.build_spin_moves(maxlen=maxlen),
                       tau, w0, nfound, nbad)
    return _CACHE[key]


def build(label, Y, seed, maxlen, margin, lmax=WINDOW):
    key = (label, Y, seed, maxlen, margin, lmax)
    if key in _CACHE:
        return _CACHE[key]
    lat, moves = get_lattice_and_moves(maxlen)[:2]
    t0 = time.time()
    S = SealedSystem(lat, moves, Y, lmax, margin=margin,
                     oversample=OVERSAMPLE, seed=seed)
    S.label = label
    S.meta = {'label': label, 'Y': Y, 'seed': seed, 'move_maxlen': maxlen,
              'margin': margin, 'nmodes': int(len(S.mus)),
              'npts': int(len(S.zs)), 'rows': int(2 * len(S.zs)),
              'su2_dev_max': float(S.su2_dev_max),
              'bessel_nodes': int(len(S.ts)), 'bessel_h': BESSEL_H,
              'x_min': S.x_min, 'x_max': S.x_max,
              'build_seconds': time.time() - t0}
    print(f'[build] {label}: Y={Y} seed={seed} maxlen={maxlen} '
          f'margin={margin} -> {len(S.mus)} modes, {len(S.zs)} pts '
          f'({2*len(S.zs)} rows), su2_dev {S.su2_dev_max:.1e}, '
          f'{time.time()-t0:.1f}s', flush=True)
    _CACHE[key] = S
    return S


# ----------------------------------------------------------------
# The refinement: golden bracket, then V-crossing extrapolation.
#
# sigma_min(lam) near an eigenvalue is an EXACT V (measured: slope
# 2.6667, linear down to sigma ~ 4e-10 with no noise floor).  Locating
# the vertex directly is limited by how small sigma can be resolved;
# intersecting the two straight branches fitted at offsets +-d, +-2d is
# not, and its error scales as O(d^2) -- the structural analogue of the
# scalar protocol's quadratic-convergence certification.
# ----------------------------------------------------------------

def v_cross(S, centre, d1):
    d2 = 2.0 * d1
    xs = np.array([-d2, -d1, d1, d2])
    ss = np.array([S.sigma(centre + x, 1)[0] for x in xs])
    mL = (ss[1] - ss[0]) / (xs[1] - xs[0])
    bL = ss[1] - mL * xs[1]
    mR = (ss[3] - ss[2]) / (xs[3] - xs[2])
    bR = ss[3] - mR * xs[3]
    den = mR - mL
    if not np.isfinite(den) or abs(den) < 1e-12:
        return float('nan'), float(mL), float(mR), ss
    return centre + (bL - bR) / den, float(mL), float(mR), ss


def refine_lambda(S, lam_start, d1=VFIT_D1, halfwidth=GOLDEN_HALFWIDTH,
                  tol=GOLDEN_TOL):
    """golden bracket -> two V-crossing iterations.  Returns a record."""
    c, s_gold = probe.golden_min(lambda x: S.sigma(x, 1)[0],
                                 lam_start - halfwidth, lam_start + halfwidth,
                                 tol=tol)
    trail = [float(c)]
    slopes = (float('nan'), float('nan'))
    diverged = False
    guard = 20.0 * halfwidth       # a V-crossing may not leave the region
    for _ in range(VFIT_ITERS):
        c2, mL, mR, _ = v_cross(S, c, d1)
        slopes = (mL, mR)
        if not np.isfinite(c2) or abs(c2 - lam_start) > guard:
            diverged = True        # no V here: the extrapolation ran away
            break
        c = c2
        trail.append(float(c))
    sig = S.sigma(c, 3)
    return {'lam': float(c), 'golden_lam': trail[0],
            'golden_sigma': float(s_gold),
            'sigma1': float(sig[0]), 'sigma2': float(sig[1]),
            'sigma3': float(sig[2]),
            'slope_left': slopes[0], 'slope_right': slopes[1],
            'v_crossing_diverged': bool(diverged),
            'trail': trail, 'lam_start': float(lam_start)}


# ----------------------------------------------------------------
# STAGE seal
# ----------------------------------------------------------------

def stage_seal():
    print('=' * 72)
    print('STAGE seal: preregistration integrity + declared choices')
    print('=' * 72)
    prereg = os.path.join(HERE, 'PREREGISTRATION.md')
    with open(prereg, 'rb') as f:
        raw = f.read()
    h = hashlib.sha256(raw).hexdigest()
    design = os.path.join(PROBE_DIR, 'DESIGN.md')
    with open(design, 'rb') as f:
        hd = hashlib.sha256(f.read()).hexdigest()
    with open(os.path.join(PROBE_DIR, 'probe.py'), 'rb') as f:
        hp = hashlib.sha256(f.read()).hexdigest()
    criterion = (
        'In the window |lam| <= 4, the instrument produces >= 1 eigenvalue '
        'passing ALL of: two-Y bar |Dlam| < 10^-9 at 10-digit working '
        'precision; two seeds; P4 restart spread under the sealed bar; P3 '
        'displaced-lam control finds nothing; gates G1, G2, G2b, assembly '
        'cross-check pass; the +- partner is present within the same bars '
        '(DESIGN section 5a is a theorem -- enforceable).')
    payload = {
        'preregistration_sha256': h,
        'design_sha256': hd,
        'probe_sha256': hp,
        'sealed_criterion_verbatim': criterion,
        'kernel_excluded_from_seal': True,
        'declared_choices': {
            'operator': 'D = -i[ t(sig1 d_x + sig2 d_y + sig3 d_t) - sig3 ]',
            'coordinates': 'upper half-space (z,t), metric (|dz|^2+dt^2)/t^2',
            'frame': '(e1,e2,e3) = (t d_x, t d_y, t d_t)',
            'trivialisation': 'Iwasawa section s(z,t)=[[sqrt t, z/sqrt t],'
                              '[0, 1/sqrt t]]',
            'clifford': 'c(e_i) = sigma_i (Pauli), sigma1 sigma2 sigma3 = i I',
            'spin_structure': 'rho_1 = (A,B) Riley lift; meridian trace +2 '
                              '(periodic), longitude trace -2 (ANTIperiodic)',
            'mode_lattice': 'Lambda* + u2/2, u2 = i/(2 sqrt 3); no zero mode',
            'automorphy_twist': 'CONJUGATE Iwasawa factor conj(k), '
                                'k = s(x*)^-1 rho_1(g) s(x)  [gate G2b]',
            'window': WINDOW,
            'scan_grid': SCAN_DL,
            'scan_grid_second_instrument': SCAN_DL_2,
            'truncation_margin': MARGIN,
            'truncation_relative_tail': float(np.exp(-MARGIN)),
            'oversample': OVERSAMPLE,
            'bessel_quadrature': f'trapezoid step h = {BESSEL_H}, '
                                 f'tol_exp = {BESSEL_TOL_EXP} (TIGHTER than '
                                 f'the B933 probe\'s h = 0.15, tol_exp = 45: '
                                 f'the probe setting loses relative accuracy '
                                 f'above x ~ 35 and the collocation columns '
                                 f'are normalised, so exponentially small '
                                 f'columns would be corrupted)',
            'refinement': f'golden(tol={GOLDEN_TOL}) then {VFIT_ITERS} '
                          f'V-crossing iterations at offsets '
                          f'(+-{VFIT_D1}, +-{2*VFIT_D1})',
            'instruments': [
                {'label': a, 'Y': b, 'seed': c, 'move_maxlen': d,
                 'margin': e} for a, b, c, d, e in INSTRUMENTS],
            'bar_two_Y': BAR_TWO_Y,
            'bar_p4_spread': BAR_SPREAD,
            'bar_reading': 'the PREREGISTRATION seals exactly one numeric '
                           'bar (10^-9); "the sealed bar" for the P4 restart '
                           'spread is read as that same 10^-9. Declared here '
                           'before the battery runs.',
            'working_precision': 'IEEE-754 binary64 throughout the '
                                 'collocation/SVD path (~15.95 decimal '
                                 'digits), which exceeds the sealed '
                                 '"10-digit working precision" requirement; '
                                 'mpmath (dps 30-40) is used for the '
                                 'independent G1 and assembly cross-checks. '
                                 'The 25-digit rung needs the O5 driver port '
                                 'and is NOT attempted here.',
        },
    }
    for k, v in payload.items():
        if k != 'declared_choices':
            print(f'  {k}: {v}')
    stage_dump('seal', payload)


# ----------------------------------------------------------------
# STAGE gates: G1, G2, G2b, assembly cross-check, shape-gate wiring
# ----------------------------------------------------------------

def stage_gates():
    import mpmath as mp
    print('=' * 72)
    print('STAGE gates: G1 (operator identity), G2 (twists), G2b (frame), '
          'assembly')
    print('=' * 72)
    out = {}
    lat, moves, tau, w0, nfound, nbad = get_lattice_and_moves(5)

    # ---- lattice / mode wiring -------------------------------------
    print(f'\n[lattice] tau = {tau:.15f} (word {w0!r}, {nfound} parabolics, '
          f'{nbad} outside Z+Z tau)')
    assert nbad == 0
    out['tau'] = [tau.real, tau.imag]
    out['tau_vs_2sqrt_minus3'] = float(abs(tau - 2j * probe.SQ3))
    print(f'[lattice] |tau - 2 sqrt(-3)| = {out["tau_vs_2sqrt_minus3"]:.2e}')

    L = probe.wmat(probe.LONG_WORD)
    trL = complex(np.trace(L))
    assert abs(trL + 2) < 1e-9 and abs(L[1, 0]) < 1e-9
    vL = -L[0, 1]
    nvec = lat.Minv @ np.array([vL.real, vL.imag])
    assert np.max(np.abs(nvec - np.round(nvec))) < 1e-9
    assert int(round(nvec[1])) % 2 == 1, 'longitude must be ODD in tau'
    out['longitude_trace'] = [trL.real, trL.imag]
    out['longitude_lattice_coords'] = [float(nvec[0]), float(nvec[1])]
    print(f'[lattice] rho_1({probe.LONG_WORD}) trace = {trL.real:+.15f}, '
          f'lattice coords {nvec.round(9).tolist()} (odd in tau: spin '
          f'character -1)')

    mus = lat.modes_shifted(3.0)
    mumin = float(np.min(np.abs(mus)))
    assert abs(mumin - 1 / (4 * probe.SQ3)) < 1e-12
    out['mu_min'] = mumin
    out['mu_min_theory'] = 1 / (4 * probe.SQ3)
    out['no_zero_mode'] = bool(np.min(np.abs(mus)) > 0.1)
    print(f'[modes] |mu|_min = {mumin:.15f} = 1/(4 sqrt 3); no zero mode '
          f'=> no Eisenstein sector (Baer discreteness visible in the '
          f'instrument)')

    # ---- Bessel table vs mpmath, over the instrument's real x-range -
    mp.mp.dps = 50
    S0 = build(*INSTRUMENTS[0])
    S0b = build(*INSTRUMENTS[1])
    xlo = min(S0.x_min, S0b.x_min)
    xhi = max(S0.x_max, S0b.x_max)
    xtest = sorted({round(x, 6) for x in
                    list(np.geomspace(xlo, xhi, 12)) + [xlo, xhi]})
    ts, wts = sealed_bessel_nodes(WINDOW, xlo)
    tsp, wtsp = probe.bessel_nodes(WINDOW, xlo)   # the probe's setting
    maxrel, maxrel_probe = 0.0, 0.0
    for lam in (0.0, 0.7, 2.3, 2.974550580, 4.0):
        for x in xtest:
            ref = mp.besselk(mp.mpc(-0.5, lam), x)
            got = np.exp(-x * np.cosh(ts)) @ probe.K_column(ts, wts, lam)
            gotp = np.exp(-x * np.cosh(tsp)) @ probe.K_column(tsp, wtsp, lam)
            maxrel = max(maxrel, float(abs(mp.mpc(got) - ref) / abs(ref)))
            maxrel_probe = max(maxrel_probe,
                               float(abs(mp.mpc(gotp) - ref) / abs(ref)))
    out['bessel_x_range'] = [xlo, xhi]
    out['bessel_h'] = BESSEL_H
    out['bessel_nodes'] = int(len(ts))
    out['bessel_max_rel_err'] = float(maxrel)
    out['bessel_max_rel_err_probe_quadrature'] = float(maxrel_probe)
    print(f'\n[bessel] x-range actually used by the instrument: '
          f'[{xlo:.3f}, {xhi:.3f}]')
    print(f'[bessel] sealed quadrature h = {BESSEL_H} ({len(ts)} nodes): max '
          f'RELATIVE err vs mpmath = {maxrel:.2e}')
    print(f'[bessel] the probe quadrature h = 0.15 ({len(tsp)} nodes) on the '
          f'same range: {maxrel_probe:.2e}  <- why the step was tightened')
    assert maxrel < 1e-12

    # ---- G1: operator identity by mpmath finite differences --------
    print('\n[G1] D psi_mu = lam psi_mu by finite differences (mpmath dps 40, '
          'independent implementation):')
    mp.mp.dps = 40
    h = mp.mpf(10) ** -8

    def mode_mp(zx, zy, t, mu, lam):
        k2p = 2 * mp.pi * abs(mu)
        phv = mp.e ** (2j * mp.pi * (mu.real * zx + mu.imag * zy))
        th = mp.atan2(mu.imag, mu.real)
        K1 = mp.besselk(mp.mpc(-0.5, lam), k2p * t)
        K2 = mp.besselk(mp.mpc(0.5, lam), k2p * t)
        w = t ** mp.mpf(1.5)
        return (phv * w * K1, phv * w * (-1j) * mp.e ** (1j * th) * K2)

    rng = np.random.default_rng(17)
    g1 = []
    for lam in (1.234, -0.777, 2.974550580, 0.0):
        mu = complex(mus[rng.integers(len(mus))])
        zx = mp.mpf(str(rng.uniform(-0.4, 0.4)))
        zy = mp.mpf(str(rng.uniform(-0.4, 0.4)))
        t = mp.mpf(str(rng.uniform(0.6, 1.1)))
        f0 = mode_mp(zx, zy, t, mu, lam)
        dx = [(a - b) / (2 * h) for a, b in zip(
            mode_mp(zx + h, zy, t, mu, lam), mode_mp(zx - h, zy, t, mu, lam))]
        dy = [(a - b) / (2 * h) for a, b in zip(
            mode_mp(zx, zy + h, t, mu, lam), mode_mp(zx, zy - h, t, mu, lam))]
        dt = [(a - b) / (2 * h) for a, b in zip(
            mode_mp(zx, zy, t + h, mu, lam), mode_mp(zx, zy, t - h, mu, lam))]
        s1 = (dx[1], dx[0])
        s2 = (-1j * dy[1], 1j * dy[0])
        s3 = (dt[0], -dt[1])
        Dpsi = [-1j * (t * (s1[c] + s2[c] + s3[c])
                       - (f0[c] if c == 0 else -f0[c])) for c in range(2)]
        scale = max(abs(f0[0]), abs(f0[1]))
        den = abs(lam) * scale if lam != 0 else scale
        res = float(max(abs(Dpsi[c] - lam * f0[c]) for c in range(2)) / den)
        g1.append({'lam': lam, 'mu': [mu.real, mu.imag], 'rel_residual': res})
        print(f'   lam = {lam:+.9f}, mu = {mu:.5f}: rel residual {res:.2e}')
    g1max = max(r['rel_residual'] for r in g1)
    out['G1_fd'] = g1
    out['G1_max_rel_residual'] = g1max
    out['G1_pass'] = bool(g1max < 1e-10)
    assert out['G1_pass'], 'G1 FAILED'
    print(f'   G1 max = {g1max:.2e}  -> PASS (bar 1e-10)')

    # ---- G2: peripheral twists, cocycle, SU(2)-ness ----------------
    print('\n[G2] twists:')
    z0, t0 = complex(0.13, 0.44), 0.8
    kM = probe.twist(z0 + 1, t0, probe.wmat('a'), z0, t0)
    kL = probe.twist(z0 + vL, t0, L, z0, t0)
    dM = float(np.abs(kM - np.eye(2)).max())
    dL = float(np.abs(kL + np.eye(2)).max())
    print(f'   meridian twist - (+I) = {dM:.2e}; longitude twist - (-I) = '
          f'{dL:.2e}')
    assert dM < 1e-12 and dL < 1e-12
    out['G2_meridian_dev'] = dM
    out['G2_longitude_dev'] = dL

    rng = np.random.default_rng(23)
    maxco = 0.0
    for _ in range(40):
        w1 = ''.join(rng.choice(list('abAB'), size=rng.integers(1, 6)))
        w2 = ''.join(rng.choice(list('abAB'), size=rng.integers(1, 6)))
        g1m, g2m = probe.wmat(w1), probe.wmat(w2)
        z = complex(rng.uniform(-1, 1), rng.uniform(-1, 1))
        t = rng.uniform(0.4, 1.2)
        z2, t2 = probe.apply_m(g2m, z, t)
        z12, t12 = probe.apply_m(g1m @ g2m, z, t)
        ka = probe.twist(z12, t12, g1m @ g2m, z, t)
        kb = (probe.twist(z12, t12, g1m, z2, t2)
              @ probe.twist(z2, t2, g2m, z, t))
        maxco = max(maxco, float(np.abs(ka - kb).max()))
    out['G2_cocycle_max_dev'] = maxco
    assert maxco < 1e-10
    print(f'   cocycle k(g1 g2) = k(g1) k(g2), 40 random pairs: {maxco:.2e}')

    rng = np.random.default_rng(3)
    maxsu = 0.0
    for _ in range(60):
        z = complex(rng.uniform(-1, 1), rng.uniform(-2, 2))
        t = rng.uniform(0.4, 0.8)
        zs_, ts_, G, _ = probe.reduce_pt_spin(lat, moves, z, t)
        maxsu = max(maxsu, float(probe.su2_dev(
            probe.twist(zs_, ts_, G, z, t))))
    out['G2_su2_max_dev'] = maxsu
    assert maxsu < 1e-9
    out['G2_pass'] = True
    print(f'   SU(2) deviation over 60 tracked pullback twists: {maxsu:.2e}')

    # ---- G2b: the frame gate, WITH its discriminating control ------
    print('\n[G2b] frame gate  R_geom = Ad(conj k)  (and the control: the '
          'unconjugated twist must FAIL):')
    sig = [probe.SIG1, probe.SIG2, probe.SIG3]

    def frame_rot_geom(g, z, t, eps=1e-6):
        za, ta = probe.apply_m(g, z, t)
        R = np.zeros((3, 3))
        for j, (dz, dt_) in enumerate([(eps * t, 0), (1j * eps * t, 0),
                                       (0, eps * t)]):
            z1, t1 = probe.apply_m(g, z + dz, t + dt_)
            R[0, j] = (z1 - za).real / (eps * ta)
            R[1, j] = (z1 - za).imag / (eps * ta)
            R[2, j] = (t1 - ta) / (eps * ta)
        return R

    def frame_rot_ad(k):
        ki = np.linalg.inv(k)
        return np.array([[0.5 * np.trace(sig[i] @ k @ sig[j] @ ki).real
                          for j in range(3)] for i in range(3)])

    rng = np.random.default_rng(9)
    maxfr, maxfr_wrong = 0.0, 0.0
    for _ in range(12):
        w = ''.join(rng.choice(list('abAB'), size=rng.integers(2, 6)))
        g = probe.wmat(w)
        z = complex(rng.uniform(-1, 1), rng.uniform(-1, 1))
        t = rng.uniform(0.5, 1.0)
        z1, t1 = probe.apply_m(g, z, t)
        k = probe.twist(z1, t1, g, z, t)
        Rg = frame_rot_geom(g, z, t)
        maxfr = max(maxfr, float(np.abs(Rg - frame_rot_ad(np.conj(k))).max()))
        maxfr_wrong = max(maxfr_wrong,
                          float(np.abs(Rg - frame_rot_ad(k)).max()))
    out['G2b_max_dev_conjugate_twist'] = maxfr
    out['G2b_max_dev_unconjugated_control'] = maxfr_wrong
    out['G2b_pass'] = bool(maxfr < 1e-5 and maxfr_wrong > 1e-2)
    print(f'   |R_geom - Ad(conj k)| = {maxfr:.2e}  (bar 1e-5)')
    print(f'   |R_geom - Ad(k)|      = {maxfr_wrong:.2e}  (the control: the '
          f'gate is discriminating, not vacuous)')
    assert out['G2b_pass'], 'G2b FAILED'

    # ---- shape gate 5(a): J = sigma2 . conj anticommutes with D ----
    # (symbolic-level check on the Pauli algebra: J c(e_i) = -c(e_i) J
    #  for every i, and J^2 = -1.)
    print('\n[5a] shape gate: J = sigma2 o conj, JD = -DJ on the symbol:')
    s2 = probe.SIG2
    anti = max(float(np.abs(s2 @ np.conj(s) + s @ s2).max())
               for s in (probe.SIG1, probe.SIG2, probe.SIG3))
    # D = -i[ t sum sigma_k d_k - sigma_3 ]; J psi = sigma_2 conj(psi):
    #   J(-i X psi) = sigma_2 conj(-i X psi) = +i sigma_2 conj(X) conj(psi)
    #   and sigma_2 conj(sigma_k) = -sigma_k sigma_2, so J D = -D J.
    j2 = float(np.abs(s2 @ np.conj(s2) + np.eye(2)).max())
    out['shape_5a_anticommutator_max'] = anti
    out['shape_5a_J_squared_plus_I'] = j2
    out['shape_5a_pass'] = bool(anti < 1e-15 and j2 < 1e-15)
    print(f'   max |sigma_2 conj(sigma_k) + sigma_k sigma_2| = {anti:.2e}; '
          f'|J^2 + I| = {j2:.2e}  => spectrum is exactly +- symmetric and '
          f'ker D is even-dimensional')
    assert out['shape_5a_pass']

    # ---- assembly cross-check: dumb mpmath row rebuild -------------
    print('\n[assembly] independent mpmath rebuild of collocation rows vs '
          'the vectorised assembly:')
    mp.mp.dps = 30
    S = S0
    lam_a = 2.974550580
    V = S.rows(lam_a)
    rng = np.random.default_rng(101)
    npts = len(S.zs)
    devs = []
    for _ in range(24):
        j = int(rng.integers(npts))
        n = int(rng.integers(len(S.mus)))
        mu = complex(S.mus[n])
        kc = S.ks[j]

        def psi(zz, tt):
            k2p = 2 * mp.pi * abs(mu)
            ph = mp.e ** (2j * mp.pi * (mu.real * zz.real
                                        + mu.imag * zz.imag))
            th = mp.atan2(mu.imag, mu.real)
            w = mp.mpf(str(tt)) ** mp.mpf(1.5)
            K1 = mp.besselk(mp.mpc(-0.5, lam_a), k2p * tt)
            K2 = mp.besselk(mp.mpc(0.5, lam_a), k2p * tt)
            return (ph * w * K1, ph * w * (-1j) * mp.e ** (1j * th) * K2)

        pstar = psi(complex(S.zstar[j]), float(S.tstar[j]))
        pbase = psi(complex(S.zs[j]), float(S.Y))
        r1 = pstar[0] - (kc[0, 0] * pbase[0] + kc[0, 1] * pbase[1])
        r2 = pstar[1] - (kc[1, 0] * pbase[0] + kc[1, 1] * pbase[1])
        scale = max(abs(complex(pstar[0])), abs(complex(pstar[1])),
                    abs(complex(pbase[0])), abs(complex(pbase[1])))
        d = max(abs(complex(r1) - V[j, n]), abs(complex(r2) - V[npts + j, n]))
        devs.append(float(d / scale))
    amax = max(devs)
    out['assembly_max_rel_dev'] = amax
    out['assembly_samples'] = len(devs)
    out['assembly_pass'] = bool(amax < 1e-10)
    print(f'   24 random (point, mode) rows at lam = {lam_a}: max relative '
          f'deviation {amax:.2e}  (bar 1e-10)')
    assert out['assembly_pass'], 'assembly cross-check FAILED'

    out['all_gates_pass'] = bool(out['G1_pass'] and out['G2_pass']
                                 and out['G2b_pass'] and out['assembly_pass']
                                 and out['shape_5a_pass'])
    print(f'\n[gates] ALL GATES PASS = {out["all_gates_pass"]}')
    stage_dump('gates', out)


# ----------------------------------------------------------------
# STAGE scan
# ----------------------------------------------------------------

def _scan_one(S, dl):
    lam_vals = np.arange(-WINDOW, WINDOW + dl / 2, dl)
    sig = np.empty((len(lam_vals), 3))
    t0 = time.time()
    for i, lam in enumerate(lam_vals):
        sig[i] = S.sigma(lam)
        if i % 100 == 0:
            el = time.time() - t0
            print(f'   {S.label} {i}/{len(lam_vals)} {el:.0f}s '
                  f'eta {el/max(i,1)*(len(lam_vals)-i):.0f}s', flush=True)
    med = float(np.median(sig[:, 0]))
    dips = []
    for i in range(1, len(lam_vals) - 1):
        if (sig[i, 0] < sig[i - 1, 0] and sig[i, 0] < sig[i + 1, 0]
                and sig[i, 0] < DIP_FACTOR * med):
            dips.append({'lam': float(lam_vals[i]), 'sigma1': float(sig[i, 0]),
                         'sigma2': float(sig[i, 1]),
                         'sigma3': float(sig[i, 2])})
    return med, dips, lam_vals, sig, time.time() - t0


def stage_scan():
    print('=' * 72)
    print(f'STAGE scan: sigma_min over |lam| <= {WINDOW}')
    print('=' * 72)
    out = {}
    S1 = build(*INSTRUMENTS[0])
    med1, dips1, lv1, sg1, sec1 = _scan_one(S1, SCAN_DL)
    print(f'\n[scan] {S1.label}: median sigma_min = {med1:.4e}; '
          f'{len(dips1)} dips ({sec1:.0f}s)')
    for d in dips1:
        print(f'    lam = {d["lam"]:+.4f}  sigma = ({d["sigma1"]:.3e}, '
              f'{d["sigma2"]:.3e}, {d["sigma3"]:.3e})')
    out['S1'] = {'meta': S1.meta, 'dl': SCAN_DL, 'median_sigma': med1,
                 'dips': dips1, 'seconds': sec1}
    np.savez(os.path.join(HERE, 'scan_S1.npz'), lam=lv1, sig=sg1)
    stage_dump('scan', out)

    S2 = build(*INSTRUMENTS[1])
    med2, dips2, lv2, sg2, sec2 = _scan_one(S2, SCAN_DL_2)
    print(f'\n[scan] {S2.label}: median sigma_min = {med2:.4e}; '
          f'{len(dips2)} dips ({sec2:.0f}s)')
    for d in dips2:
        print(f'    lam = {d["lam"]:+.4f}  sigma = ({d["sigma1"]:.3e}, '
              f'{d["sigma2"]:.3e}, {d["sigma3"]:.3e})')
    out['S2'] = {'meta': S2.meta, 'dl': SCAN_DL_2, 'median_sigma': med2,
                 'dips': dips2, 'seconds': sec2}
    np.savez(os.path.join(HERE, 'scan_S2.npz'), lam=lv2, sig=sg2)

    # dip-list agreement (completeness cross-check between two instruments)
    l1 = sorted(d['lam'] for d in dips1)
    l2 = sorted(d['lam'] for d in dips2)
    matched = []
    for a in l1:
        b = min(l2, key=lambda q: abs(q - a)) if l2 else None
        matched.append({'S1': a, 'S2': b,
                        'sep': abs(b - a) if b is not None else None})
    same_count = (len(l1) == len(l2)
                  and all(m['sep'] is not None and m['sep'] <= SCAN_DL_2
                          for m in matched))
    out['dip_list_agreement'] = {'S1_dips': l1, 'S2_dips': l2,
                                 'matched': matched,
                                 'same_dip_list': bool(same_count)}
    print(f'\n[scan] dip lists agree across the two instruments: '
          f'{same_count}')

    # doubling observation (DESIGN 5c): sigma1 == sigma2 everywhere
    r = np.abs(sg1[:, 1] - sg1[:, 0]) / np.maximum(sg1[:, 0], 1e-300)
    out['doubling_sigma1_vs_sigma2'] = {
        'max_rel_gap_over_whole_scan': float(np.max(r)),
        'median_rel_gap': float(np.median(r)),
        'sigma3_over_sigma1_median': float(np.median(sg1[:, 2] / sg1[:, 0])),
        'note': 'DESIGN 5c: the ENTIRE singular spectrum is doubled at every '
                'lam (on and off eigenvalue); mechanism = obligation O1'}
    print(f'[scan] doubling sigma1 = sigma2: max relative gap over the whole '
          f'scan = {np.max(r):.2e}')
    stage_dump('scan', out)


# ----------------------------------------------------------------
# STAGE refine: the four instruments on every dip
# ----------------------------------------------------------------

def stage_refine():
    print('=' * 72)
    print('STAGE refine: V-crossing on four instruments')
    print('=' * 72)
    res = load_results()
    dips = [d['lam'] for d in res['scan']['S1']['dips']]
    print(f'[refine] dips from the S1 scan: {dips}')
    out = {'dips': dips, 'per_dip': []}

    systems = [build(*spec) for spec in INSTRUMENTS]
    for l0 in dips:
        is_kernel = abs(l0) < 1e-3
        rec = {'dip': l0, 'is_kernel_candidate': is_kernel, 'instruments': {}}
        print(f'\n[refine] dip {l0:+.4f}'
              + ('   (KERNEL CANDIDATE -- EXCLUDED from the seal)'
                 if is_kernel else ''))
        for S in systems:
            t0 = time.time()
            r = refine_lambda(S, l0)
            r['seconds'] = time.time() - t0
            rec['instruments'][S.label] = r
            print(f'    {S.label}: lam = {r["lam"]:+.13f}  sigma = '
                  f'({r["sigma1"]:.2e}, {r["sigma2"]:.2e}, {r["sigma3"]:.2e})'
                  f'  slopes ({r["slope_left"]:+.4f}, '
                  f'{r["slope_right"]:+.4f})  {r["seconds"]:.0f}s',
                  flush=True)
        lams = {k: v['lam'] for k, v in rec['instruments'].items()}
        rec['two_Y_dev'] = abs(lams['S1'] - lams['S2'])
        rec['two_seed_dev'] = abs(lams['S1'] - lams['S3'])
        rec['word_set_dev'] = abs(lams['S1'] - lams['S4'])
        rec['max_dev'] = max(rec['two_Y_dev'], rec['two_seed_dev'],
                             rec['word_set_dev'])
        rec['two_Y_pass'] = bool(rec['two_Y_dev'] < BAR_TWO_Y)
        rec['two_seed_pass'] = bool(rec['two_seed_dev'] < BAR_TWO_Y)
        rec['word_set_pass'] = bool(rec['word_set_dev'] < BAR_TWO_Y)
        med = res['scan']['S1']['median_sigma']
        rec['sigma_below_cert_factor'] = bool(
            rec['instruments']['S1']['sigma1'] < CERT_FACTOR * med)
        print(f'    two-Y |Dlam| = {rec["two_Y_dev"]:.2e}  '
              f'two-seed {rec["two_seed_dev"]:.2e}  '
              f'word-set {rec["word_set_dev"]:.2e}   (bar {BAR_TWO_Y:.0e})')
        out['per_dip'].append(rec)
        stage_dump('refine', out)

    # ---- +- partner enforcement (DESIGN 5a is a theorem) -----------
    pos = [r for r in out['per_dip']
           if not r['is_kernel_candidate'] and r['dip'] > 0]
    neg = [r for r in out['per_dip']
           if not r['is_kernel_candidate'] and r['dip'] < 0]
    pairs = []
    for p in pos:
        lp = p['instruments']['S1']['lam']
        best, dev = None, None
        for n in neg:
            ln = -n['instruments']['S1']['lam']
            if dev is None or abs(ln - lp) < dev:
                best, dev = n, abs(ln - lp)
        pairs.append({'lam_pos': lp,
                      'lam_neg_abs': (-best['instruments']['S1']['lam']
                                      if best else None),
                      'pair_dev': dev,
                      'pair_pass': bool(dev is not None and dev < BAR_TWO_Y)})
    out['pm_pairing'] = pairs
    print('\n[refine] +- partner enforcement (5a):')
    for p in pairs:
        print(f'    +{p["lam_pos"]:.13f}  vs  |{-p["lam_neg_abs"]:.13f}|  '
              f'dev {p["pair_dev"]:.2e}  pass {p["pair_pass"]}')

    # ---- truncation ladder ----------------------------------------
    print('\n[refine] truncation gate (margin ladder on S1):')
    lam_ref = None
    for r in out['per_dip']:
        if not r['is_kernel_candidate'] and r['dip'] > 0:
            lam_ref = r['instruments']['S1']['lam']
            break
    ladder = []
    if lam_ref is not None:
        for mg in TRUNCATION_LADDER:
            Sm = build(f'T{mg:g}', INSTRUMENTS[0][1], INSTRUMENTS[0][2],
                       INSTRUMENTS[0][3], mg)
            rr = refine_lambda(Sm, lam_ref)
            ladder.append({'margin': mg, 'nmodes': Sm.meta['nmodes'],
                           'lam': rr['lam'], 'dev_vs_sealed_margin':
                           abs(rr['lam'] - lam_ref)})
            print(f'    margin {mg:>5.1f} ({Sm.meta["nmodes"]:4d} modes): '
                  f'lam = {rr["lam"]:.13f}  dev {abs(rr["lam"]-lam_ref):.2e}')
    out['truncation_ladder'] = ladder
    out['truncation_max_dev'] = (max(x['dev_vs_sealed_margin']
                                     for x in ladder) if ladder else None)

    # ---- refinement convergence: O(d^2) in the V-fit offset --------
    print('\n[refine] V-fit convergence in the offset d (quadratic-'
          'convergence analogue of the scalar protocol):')
    conv = []
    if lam_ref is not None:
        S1 = systems[0]
        for d1 in (5e-7, 1e-6, 2e-6, 4e-6, 8e-6):
            c = lam_ref
            for _ in range(2):
                c, _, _, _ = v_cross(S1, c, d1)
            conv.append({'d1': d1, 'lam': float(c)})
        base = conv[0]['lam']
        for c in conv:
            c['dev_vs_smallest_d'] = abs(c['lam'] - base)
            print(f'    d1 = {c["d1"]:.1e}: lam = {c["lam"]:.13f}  '
                  f'dev {c["dev_vs_smallest_d"]:.2e}')
        ratios = []
        for i in range(1, len(conv) - 1):
            a, b = conv[i]['dev_vs_smallest_d'], conv[i + 1][
                'dev_vs_smallest_d']
            if a > 0:
                ratios.append(b / a)
        conv_ratio = ratios
        print(f'    successive dev ratios at doubling d (O(d^2) predicts 4): '
              f'{[round(x, 2) for x in conv_ratio]}')
        out['vfit_convergence'] = {'points': conv, 'doubling_ratios':
                                   conv_ratio, 'expected_ratio_for_d2': 4.0}
    stage_dump('refine', out)


# ----------------------------------------------------------------
# STAGE p4: perturbed restarts
# ----------------------------------------------------------------

def stage_p4():
    print('=' * 72)
    print('STAGE P4: perturbed restarts, spread against the sealed bar')
    print('=' * 72)
    res = load_results()
    targets = [r for r in res['refine']['per_dip']
               if not r['is_kernel_candidate']]
    out = {'bar': BAR_SPREAD, 'targets': []}
    for r in targets:
        lam0 = r['instruments']['S1']['lam']
        rec = {'dip': r['dip'], 'lam_reference': lam0, 'restarts': {}}
        print(f'\n[P4] target lam = {lam0:+.13f}')
        for spec in INSTRUMENTS[:2]:          # S1 and S2 (the two-Y pair)
            S = build(*spec)
            vals = []
            for dlt in P4_PERTURBATIONS:
                rr = refine_lambda(S, lam0 + dlt)
                vals.append({'perturbation': dlt, 'lam': rr['lam'],
                             'sigma1': rr['sigma1']})
                print(f'    {S.label} start {lam0+dlt:+.6f}: '
                      f'lam = {rr["lam"]:+.13f}', flush=True)
            arr = np.array([v['lam'] for v in vals])
            spread = float(arr.max() - arr.min())
            rec['restarts'][S.label] = {
                'values': vals, 'spread': spread,
                'spread_pass': bool(spread < BAR_SPREAD),
                'max_dev_from_reference': float(np.max(np.abs(arr - lam0)))}
            print(f'    {S.label} spread = {spread:.2e}  (bar '
                  f'{BAR_SPREAD:.0e})  pass '
                  f'{rec["restarts"][S.label]["spread_pass"]}')
        allv = []
        for k in rec['restarts']:
            allv += [v['lam'] for v in rec['restarts'][k]['values']]
        rec['joint_spread'] = float(max(allv) - min(allv))
        rec['joint_spread_pass'] = bool(rec['joint_spread'] < BAR_SPREAD)
        print(f'    joint (S1+S2, {len(allv)} restarts) spread = '
              f'{rec["joint_spread"]:.2e}  pass {rec["joint_spread_pass"]}')
        out['targets'].append(rec)
        stage_dump('p4', out)
    out['all_pass'] = bool(all(t['joint_spread_pass'] for t in out['targets']))
    stage_dump('p4', out)


# ----------------------------------------------------------------
# STAGE p3: the displaced-lambda control.  IT MUST FIND NOTHING.
# ----------------------------------------------------------------

def stage_p3():
    print('=' * 72)
    print('STAGE P3: displaced-lambda control -- MUST find nothing')
    print('=' * 72)
    res = load_results()
    med = res['scan']['S1']['median_sigma']
    known = [r['instruments']['S1']['lam'] for r in res['refine']['per_dip']]
    out = {'median_sigma': med, 'cert_factor': CERT_FACTOR,
           'known_eigenvalues': known, 'controls': []}
    S1, S2 = build(*INSTRUMENTS[0]), build(*INSTRUMENTS[1])
    for lam_d in P3_DISPLACED:
        sep = min(abs(lam_d - k) for k in known)
        r1 = refine_lambda(S1, lam_d)
        r2 = refine_lambda(S2, lam_d)
        two_y = abs(r1['lam'] - r2['lam'])
        deep = bool(min(r1['golden_sigma'], r1['sigma1'])
                    < CERT_FACTOR * med)
        # "found something" = a deep dip AND two-Y reproducibility
        found = bool(deep and two_y < BAR_TWO_Y)
        rec = {'lam_displaced': lam_d,
               'separation_from_nearest_eigenvalue': sep,
               'S1': r1, 'S2': r2, 'two_Y_dev': two_y,
               'golden_sigma_over_median': r1['golden_sigma'] / med,
               'deep_dip': deep, 'found_something': found}
        out['controls'].append(rec)
        print(f'  lam_d = {lam_d:+.3f} (sep {sep:.3f}): golden sigma = '
              f'{r1["golden_sigma"]:.3e} = {r1["golden_sigma"]/med:.2f} x '
              f'median; S1 -> {r1["lam"]:+.9f}, S2 -> {r2["lam"]:+.9f}, '
              f'two-Y |Dlam| = {two_y:.2e};  found something: {found}',
              flush=True)
        stage_dump('p3', out)
    out['control_finds_nothing'] = bool(
        not any(c['found_something'] for c in out['controls']))
    out['verdict'] = ('PASS -- the control found nothing'
                      if out['control_finds_nothing'] else
                      'FAILURE OF THE CELL -- the control found something')
    print(f'\n[P3] {out["verdict"]}')
    stage_dump('p3', out)


# ----------------------------------------------------------------
# STAGE verdict
# ----------------------------------------------------------------

def stage_verdict():
    print('=' * 72)
    print('STAGE verdict: the sealed criterion, element by element')
    print('=' * 72)
    res = load_results()
    g, sc, rf = res['gates'], res['scan'], res['refine']
    p4, p3 = res['p4'], res['p3']

    cands = []
    for r in rf['per_dip']:
        if r['is_kernel_candidate']:
            continue
        lam = r['instruments']['S1']['lam']
        p4rec = next((t for t in p4['targets']
                      if abs(t['lam_reference'] - lam) < 1e-6), None)
        pair = next((p for p in rf['pm_pairing']
                     if abs(abs(p['lam_pos']) - abs(lam)) < 1e-6
                     or abs(abs(p['lam_neg_abs']) - abs(lam)) < 1e-6), None)
        elements = {
            'two_Y_bar_1e-9': r['two_Y_pass'],
            'two_seeds': r['two_seed_pass'],
            'P4_restart_spread_under_sealed_bar': (
                p4rec['joint_spread_pass'] if p4rec else False),
            'P3_displaced_control_finds_nothing': p3['control_finds_nothing'],
            'G1': g['G1_pass'],
            'G2': g['G2_pass'],
            'G2b': g['G2b_pass'],
            'assembly_cross_check': g['assembly_pass'],
            'pm_partner_present_within_bars': (
                pair['pair_pass'] if pair else False),
        }
        cands.append({
            'lam': lam,
            'in_window': bool(abs(lam) <= WINDOW),
            'elements': elements,
            'passes_all': bool(all(elements.values()) and abs(lam) <= WINDOW),
            'two_Y_dev': r['two_Y_dev'], 'two_seed_dev': r['two_seed_dev'],
            'word_set_dev': r['word_set_dev'],
            'p4_joint_spread': p4rec['joint_spread'] if p4rec else None,
            'pair_dev': pair['pair_dev'] if pair else None,
            'per_instrument': {k: v['lam']
                               for k, v in r['instruments'].items()},
        })

    npass = sum(1 for c in cands if c['passes_all'])
    outcome = 'A' if npass >= 1 else 'B'
    lam1 = None
    if npass:
        lam1 = min((abs(c['lam']) for c in cands if c['passes_all']))

    # digits of agreement across the four instruments
    digits = None
    if lam1 is not None:
        best = min((c for c in cands if c['passes_all']),
                   key=lambda c: abs(c['lam']))
        spread = max(best['two_Y_dev'], best['two_seed_dev'],
                     best['word_set_dev'])
        digits = int(np.floor(-np.log10(spread / abs(lam1))))

    # Weyl screen inside the sealed window
    weyl_c = 2 * VOL_M004 / (6 * np.pi ** 2)
    n_states = 2 * sum(1 for c in cands if abs(c['lam']) <= WINDOW)  # 5c x2
    out = {
        'candidates': cands,
        'n_passing_all_elements': npass,
        'outcome': outcome,
        'lambda_1': lam1,
        'lambda_1_10_digits': (float(f'{lam1:.9e}') if lam1 else None),
        'instrument_agreement_digits': digits,
        'kernel_excluded': True,
        'kernel_record': next((r for r in rf['per_dip']
                               if r['is_kernel_candidate']), None),
        'weyl_screen': {
            'coefficient_2vol_over_6pi2': weyl_c,
            'expected_states_abs_lam_le_window': weyl_c * WINDOW ** 3,
            'found_states_with_5c_doubling': n_states,
            'plus_kernel_dim': 2,
            'note': 'leading term only; sub-leading cusp terms for the Dirac '
                    'operator are unknown. Screen, not a gate.'},
        'multiplicity_caution': sc.get('doubling_sigma1_vs_sigma2'),
    }
    print(f'\nCandidates in |lam| <= {WINDOW}: {len(cands)}; passing every '
          f'sealed element: {npass}')
    for c in cands:
        print(f'  lam = {c["lam"]:+.13f}  passes_all = {c["passes_all"]}')
        for k, v in c['elements'].items():
            print(f'      {k:<42s} {v}')
    print(f'\nOUTCOME {outcome}')
    if outcome == 'A':
        print(f'  lambda_1 = {lam1:.13f}  '
              f'({digits} digits of cross-instrument agreement)')
    stage_dump('verdict', out)


# ----------------------------------------------------------------
# STAGE qctl: post-verdict control -- did tightening the Bessel
# quadrature move the answer?  Touches no sealed element; it exists so
# the FINDINGS' "the fix did not move lambda_1" is reproducible rather
# than asserted.
# ----------------------------------------------------------------

def stage_qctl():
    print('=' * 72)
    print('STAGE qctl (post-verdict control): sealed quadrature h = '
          f'{BESSEL_H} vs the B933 probe quadrature h = 0.15')
    print('=' * 72)
    res = load_results()
    lam_ref = res['verdict']['lambda_1']
    lat, moves = get_lattice_and_moves(5)[:2]
    label, Y, seed, maxlen, margin = INSTRUMENTS[0]

    S_sealed = build(*INSTRUMENTS[0])
    r_sealed = refine_lambda(S_sealed, lam_ref)
    # the probe's own SpinSystem: probe.bessel_nodes, h = 0.15, tol_exp = 45
    S_probe = probe.SpinSystem(lat, moves, Y, WINDOW, margin=margin,
                               oversample=OVERSAMPLE, seed=seed)
    r_probe = refine_lambda(S_probe, lam_ref)
    dev = abs(r_sealed['lam'] - r_probe['lam'])
    out = {'instrument': label,
           'lam_sealed_quadrature': r_sealed['lam'],
           'lam_probe_quadrature': r_probe['lam'],
           'bessel_nodes_sealed': int(len(S_sealed.ts)),
           'bessel_nodes_probe': int(len(S_probe.ts)),
           'abs_difference': dev,
           'two_Y_bar_for_scale': BAR_TWO_Y,
           'conclusion': ('the large-x quadrature defect was LATENT: '
                          'tightening the step does not move lambda_1 at the '
                          'level the seal cares about'
                          if dev < 1e-11 else
                          'the quadrature change MOVED lambda_1 -- report')}
    print(f'  sealed  h={BESSEL_H} ({len(S_sealed.ts)} nodes): '
          f'{r_sealed["lam"]!r}')
    print(f'  probe   h=0.15 ({len(S_probe.ts)} nodes): {r_probe["lam"]!r}')
    print(f'  |difference| = {dev:.3e}   (sealed two-Y bar {BAR_TWO_Y:.0e})')
    print(f'  {out["conclusion"]}')
    stage_dump('quadrature_control', out)


STAGES = {'seal': stage_seal, 'gates': stage_gates, 'scan': stage_scan,
          'refine': stage_refine, 'p4': stage_p4, 'p3': stage_p3,
          'verdict': stage_verdict, 'qctl': stage_qctl}


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'all'
    if cmd == 'all':
        for name in ('seal', 'gates', 'scan', 'refine', 'p4', 'p3', 'verdict'):
            STAGES[name]()
    elif cmd in STAGES:
        STAGES[cmd]()
    else:
        print(f'unknown stage {cmd}; known: {sorted(STAGES)} or "all"')
        sys.exit(2)


if __name__ == '__main__':
    main()
