#!/usr/bin/env python3
"""V11 -- shared library: functions MIRRORED VERBATIM (or near-verbatim, deviations flagged inline)
from the banked B162/B163/B186 scripts in origin-axiom (read-only source repo). No banked file is
modified; this module is a fresh copy living in the v11 work directory.

Provenance of every function (banked source -> this file):
  fib_word, H_eig, band_measure_1d           <- B162 frontier/B162_kappa_sweep/kappa_sweep.py
  area_2d                                    <- B162 (same file)
  mst_max_edge (banked name: mst_max_edge),
  diam                                       <- B163 frontier/B163_kappa_sweep_resolved/kappa_resolved.py
  metallic_word, spectrum, box_dim,
  T, survival, escape_rate                   <- B186 frontier/B186_hyperbolicity_certification/trace_map_hyperbolicity.py

Trace-map / invariant convention (B186's, used throughout -- see DEVIATIONS.md for the
discrepancy against the task prompt's paraphrase T(x,y,z)=(z,x,xz-y), which is K001's DIFFERENT
(Markov, coefficient-1-xyz) normalization, not B162/B186's Suto/KKT one):
    T(x,y,z) = (2xy - z, x, y)            conserves   I = x^2+y^2+z^2-2xyz-1
    seed      = ((E-lambda)/2, E/2, 1)    lies on I=(lambda/2)^2 for all E  =>  kappa = 2 + lambda^2
    kappa>2 <=> lambda real (Hermitian, Damanik-Gorodetski proven Cantor)
    kappa=2 <=> lambda=0    (the full AC band, the unique positive-measure wall)
    kappa<2 <=> lambda = i*mu, mu=sqrt(2-kappa) real (non-Hermitian/PT, THIS CELL's regime)
"""
import numpy as np

# ----------------------------------------------------------------------------------------------
# B162 kappa_sweep.py -- direct finite-Fibonacci-chain diagonalization ("the eigenvalues ARE the
# spectrum"), and the 1D transfer-matrix band-measure (a literal trace/transfer-matrix escape
# criterion: |tr M(E)| <= 2 along the real axis).
# ----------------------------------------------------------------------------------------------

def fib_word(n):
    w = {1: "a", 2: "ab"}
    for j in range(3, n + 1):
        w[j] = w[j - 1] + w[j - 2]
    return w[n]


def H_eig(word, lam, periodic=False):
    L = len(word)
    V = np.array([lam if c == "a" else 0.0 for c in word], dtype=complex)
    H = np.zeros((L, L), dtype=complex)
    np.fill_diagonal(H, V)
    i = np.arange(L - 1)
    H[i, i + 1] = 1.0
    H[i + 1, i] = 1.0
    if periodic:
        H[0, L - 1] = 1.0
        H[L - 1, 0] = 1.0
    return np.linalg.eigvals(H)


def band_measure_1d(word, lm, NE=300000):
    """1D Lebesgue measure of {E real : |tr M(E)| <= 2}. Banked version assumes lm REAL
    (Es, a,b,c,d are float64 arrays). Kept byte-for-byte identical to B162 for calibration."""
    Es = np.linspace(-(2 + lm) - .05, (2 + lm) + .05, NE)
    a = np.ones(NE); b = np.zeros(NE); c = np.zeros(NE); d = np.ones(NE)
    with np.errstate(over='ignore', invalid='ignore'):
        for ch in word:
            V = lm * (1.0 if ch == 'a' else 0.0)
            na = (Es - V) * a - c; nb = (Es - V) * b - d
            a, b, c, d = na, nb, a.copy(), b.copy()
        return float(np.mean(np.abs(a + d) <= 2.0) * (Es[-1] - Es[0]))


def band_measure_1d_complex(word, lm, Es):
    """DEVIATION (flagged, additive-only): B162's band_measure_1d hardcodes real dtype arrays,
    so it cannot be called with complex lm (needed off-axis, kappa<2). This is the SAME
    transfer-matrix recursion (the trace/transfer-matrix escape criterion |tr M(E)|<=2),
    generalized to complex dtype so it can be evaluated ALONG THE REAL E-AXIS for complex lm --
    used only for the new readout "does the spectrum touch the real axis". Verified below
    (calibrate.py) to reproduce band_measure_1d exactly at real lm.
    Returns the boolean "bounded" mask over the supplied (real-valued) Es grid.
    """
    NE = len(Es)
    a = np.ones(NE, dtype=complex); b = np.zeros(NE, dtype=complex)
    c = np.zeros(NE, dtype=complex); d = np.ones(NE, dtype=complex)
    Esc = Es.astype(complex)
    with np.errstate(over='ignore', invalid='ignore'):
        for ch in word:
            V = lm * (1.0 if ch == 'a' else 0.0)
            na = (Esc - V) * a - c; nb = (Esc - V) * b - d
            a, b, c, d = na, nb, a.copy(), b.copy()
        tr = a + d
        return np.isfinite(tr) & (np.abs(tr) <= 2.0)


def area_2d(ev, eps):
    """2D-area proxy for a complex spectrum (grid-cell count x eps^2)."""
    lo_r, lo_i = ev.real.min() - 1e-6, ev.imag.min() - 1e-6
    cells = set(zip(np.floor((ev.real - lo_r) / eps).astype(int).tolist(),
                     np.floor((ev.imag - lo_i) / eps).astype(int).tolist()))
    return len(cells) * eps * eps


def nn95(A, B):
    A2 = np.c_[A.real, A.imag]; B2 = np.c_[B.real, B.imag]
    return np.percentile([np.min(np.sum((B2 - a) ** 2, axis=1)) ** 0.5 for a in A2], 95)


# ----------------------------------------------------------------------------------------------
# B163 kappa_resolved.py -- the largest-spectral-gap / Cantor indicator (MST max edge / diameter)
# ----------------------------------------------------------------------------------------------

def mst_max_edge(pts):
    """max edge of the Euclidean MST (Prim, O(N^2)) = the largest spectral gap."""
    P = np.c_[pts.real, pts.imag]; n = len(P)
    in_tree = np.zeros(n, bool); mind = np.full(n, np.inf); mind[0] = 0.0; edges = np.empty(n)
    for t in range(n):
        u = int(np.argmin(np.where(in_tree, np.inf, mind)))
        edges[t] = mind[u]; in_tree[u] = True
        d = np.sqrt(((P - P[u]) ** 2).sum(1)); upd = (~in_tree) & (d < mind); mind[upd] = d[upd]
    return float(edges[1:].max())


def diam(pts):
    return float(np.hypot(pts.real.max() - pts.real.min(), pts.imag.max() - pts.imag.min()))


def max_gap_over_diam(pts):
    return mst_max_edge(pts) / diam(pts)


# ----------------------------------------------------------------------------------------------
# B186 trace_map_hyperbolicity.py -- the trace-map escape criterion (T, survival, escape_rate),
# the metallic word/diagonalization spectrum, and box-counting dimension.
# ----------------------------------------------------------------------------------------------

def T(p):
    x, y, z = p
    return np.array([2 * x * y - z, x, y])


def survival(lmb, Egrid, Kmax=30, R=20.0):
    """Iterate T on the seed for every E in Egrid; return the per-iteration alive fraction f(K)."""
    P = np.array([[(Ev - lmb) / 2, Ev / 2, 1.0] for Ev in Egrid], dtype=complex)
    alive = np.ones(len(P), bool); f = []
    for _ in range(Kmax):
        nrm = np.linalg.norm(P, axis=1); alive &= np.isfinite(nrm) & (nrm < R)
        f.append(alive.mean())
        P[~alive] = 0.0                                  # freeze escaped (avoid overflow)
        P = np.array([T(p) for p in P])
    return np.array(f)


def escape_rate(f):
    """B186's exact estimator: linear fit of log f(K) vs K over the window 1e-3 < f < 0.5.
    NOTE (B451 correction, propagated here for honesty): this is the EARLY-WINDOW value of
    the estimator -- known to overshoot the true asymptotic escape rate at kappa>2 (0.509
    quoted vs 0.445+-0.006 true, ~14% high) because Kmax~30 / 400-point sampling does not
    reach the asymptotic decay regime. Kept verbatim for calibration; see robust_escape_rate
    below for the supplementary asymptotic-window cross-check used to guard Q3."""
    K = np.arange(len(f)); m = (f > 1e-3) & (f < 0.5)
    if m.sum() < 3: return 0.0
    return float(-np.polyfit(K[m], np.log(f[m]), 1)[0])


def metallic_word(n, m=1):
    sub = "a" * m + "b"; s = {-1: "b", 0: "a"}
    for k in range(1, n + 1):
        s[k] = "".join(sub if c == "a" else "a" for c in s[k - 1])
    return s[n]


def spectrum(word, lmb, periodic=True):
    L = len(word); V = np.array([lmb if c == "a" else 0.0 for c in word], dtype=complex)
    H = np.zeros((L, L), dtype=complex); np.fill_diagonal(H, V); i = np.arange(L - 1)
    H[i, i + 1] = 1; H[i + 1, i] = 1
    if periodic:
        H[0, L - 1] = 1; H[L - 1, 0] = 1
    return np.linalg.eigvals(H)


def box_dim(ev, scales=2.0 ** np.arange(-2, -8, -1)):
    P = np.c_[ev.real, ev.imag]; rng = np.ptp(P, axis=0); rng[rng == 0] = 1
    P = (P - P.min(0)) / rng
    Ns = [len({(int(a // s), int(b // s)) for a, b in P}) for s in scales]
    return float(np.polyfit(np.log(1 / scales), np.log(np.array(Ns, float)), 1)[0])


# ----------------------------------------------------------------------------------------------
# NEW (this cell, additive-only): a genuine 2D complex-E escape-criterion grid -- "the complex
# spectrum window" that item 2 of the task asks for. None of B162/B163/B186 built a full 2D
# (Re E, Im E) boundedness MASK; B186's survival() only ever ran on a 1D line (Hermitian
# calibration) or a coarse ad hoc 80x13 strip (off-axis gamma only). This reuses B186's EXACT
# T/seed/Kmax/R conventions, just scanned over a systematic grid capped <=400x400 (runtime guard).
# ----------------------------------------------------------------------------------------------

def spectrum_window(lmb, re_lo, re_hi, im_lo, im_hi, n_re=400, n_im=400, Kmax=30, R=20.0):
    """Return (ReE grid, ImE grid, bounded mask [n_im,n_re], survival-fraction-vs-K curve).
    Same seed/T/Kmax/R as B186.survival; extended from a line/strip to a full rectangle."""
    re = np.linspace(re_lo, re_hi, n_re)
    im = np.linspace(im_lo, im_hi, n_im)
    RE, IM = np.meshgrid(re, im)              # shape (n_im, n_re)
    Egrid = (RE + 1j * IM).ravel()
    P = np.array([(Egrid - lmb) / 2, Egrid / 2, np.ones_like(Egrid)]).T  # (N,3) complex
    alive = np.ones(len(P), bool); f = []
    for _ in range(Kmax):
        nrm = np.linalg.norm(P, axis=1)
        alive &= np.isfinite(nrm) & (nrm < R)
        f.append(alive.mean())
        P[~alive] = 0.0
        x, y, z = P[:, 0], P[:, 1], P[:, 2]
        P = np.column_stack([2 * x * y - z, x, y])
    bounded = alive.reshape(n_im, n_re)
    return re, im, bounded, np.array(f)


def robust_escape_rate(f, tail_frac=0.5):
    """Supplementary (NOT a banked number): asymptotic-window escape-rate estimator in the
    spirit of B451's fix to B186's early-window bias -- fit log f(K) vs K over the LATER half
    of the surviving/finite range (after 1e-3) instead of the full 1e-3<f<0.5 window, so a
    slowly-relaxing transient does not bias the slope. Used only to sanity-check Q3
    (monotonicity) against estimator bias; the primary reproduction uses escape_rate() as-is."""
    K = np.arange(len(f))
    m = (f > 1e-6) & (f < 0.5)
    if m.sum() < 4:
        return float('nan')
    idx = np.where(m)[0]
    cut = idx[int(len(idx) * (1 - tail_frac)):]
    if len(cut) < 3:
        cut = idx
    return float(-np.polyfit(K[cut], np.log(f[cut]), 1)[0])
