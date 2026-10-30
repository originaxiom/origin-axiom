#!/usr/bin/env python3
"""T-NORM on FR-FIB's matter zero modes (P-525; P-510's pre-seal condition).  Data-free: no measured number is read.

THE MODES (the frame's own, read from its code):
  b1656_funcs.py (frontier/B1691_*/verification/correction/), lines 28-38 and 41-43:
    a field of charge q (6Y; SIXY line 22; cm_zero_line.SECTORS line 38) on the line w = p1 tau - p2 has the twist
    (a, b) = twist_of(q w) = (q p1, -2 q p2); its zero mode is the doublet
        F_x(z) = ( th[a,b](z; 2tau) / sqrt th1(z; tau),  e^{i pi b} th[a,b](z+tau; 2tau) / sqrt th1(z+tau; tau) ),
    the branch fixed as in bil(): F0 F1 = X0 X1 / (i e^{-i pi tau/2} e^{-i pi z} th1(z; tau)).
  The three generations are psi_p = C_p F_x with C_p in BLOCKS = [QJ, QI, QK] (line 21; the same F for all three),
  and the coupling reads (C_a F_x)^T eps S (C_b F_y) (coupling(), line 126).  B1642's residue_coupling.py lines 4-8
  (the SM seat's W21 zero mode, untwisted).

WHAT IS COMPUTED
  P0  my theta code against the frame's bil() and twist functions (the modes are the frame's, to machine precision)
  C+  positive controls: (i) int_P dA/|z| on a skewed cell against a polar reference (the puncture quadrature);
      (ii) magnetised-torus theta modes th[j/N,0](Nz; N tau) with metric exp(-2 pi N (Im z)^2/Im tau): Gram exactly
      sqrt(Im tau/(2N)) I_N on two different cells; (iii) the frame's |F|^2 by two independent quadratures
  C-  negative controls: (i) a non-orthogonal magnetised basis (predicted kappa/sqrt(1+kappa^2)); (ii) a rotated
      quaternion block (predicted off-diagonal sin(theta) on the cover); (iii) a flat-invariant NON-product metric
      on the generations (predicted Gram H |F|^2, cell-independent)
  S   structure: the doublet's monodromy (flat, unitary, Q8-type), the generations' characters, |F|^2 periodic
      (no Gaussian factor), the cross-integrands' characters
  G   the Gram matrix per (field, tau, line): (a) the invariant one, (1/4) of the integral over the 4-fold cover on
      which every character is trivial, with a generic offset (nodes not lattice translates); (b) the naive integral
      over two different fundamental cells (to show it is not an invariant)
  K   the dimension of the flat-invariant hermitian metrics on the three generations of one field
    OMP_NUM_THREADS=1 nice -n 10 python3 -I tnorm.py      # writes tnorm_results.json beside itself
"""
import json, math, os, sys, time, pathlib, itertools, importlib.util, contextlib, io
from fractions import Fraction as Fr
from multiprocessing import Pool
import numpy as np
from numpy.polynomial.legendre import leggauss
import mpmath as mp

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "frontier").is_dir() and (p / "GENESIS.md").is_file())
OUT = HERE / "tnorm_results.json"

QI = np.array([[1j, 0], [0, -1j]]); QJ = np.array([[0, 1], [-1, 0]], dtype=complex); QK = QI @ QJ
I2 = np.eye(2, dtype=complex)
BLOCKS = [("j", QJ), ("i", QI), ("k", QK)]                     # b1656_funcs.BLOCKS order
CHARGE = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6}            # 6Y (b1656_funcs.SIXY)
NK = 24


# ------------------------------------------------------------------ theta functions (my own implementation)
def th_char(a, b, z, T, nk=NK):
    """sum_n exp(i pi T (n+a)^2 + 2 pi i (n+a)(z+b))"""
    n = np.arange(-nk, nk + 1) + float(a); z = np.asarray(z, dtype=complex)[..., None]
    return np.sum(np.exp(1j * np.pi * T * n * n + 2j * np.pi * n * (z + float(b))), -1)


def th1(z, t, nk=NK):
    k = np.arange(-nk, nk + 1); h = k + 0.5; z = np.asarray(z, dtype=complex)[..., None]
    return -1j * np.sum((-1.0) ** k * np.exp(1j * np.pi * t * h * h + 1j * np.pi * (2 * k + 1) * z), -1)


def doublet_parts(z, a, b, tau, nk=NK):
    """X0, X1 (with the e^{i pi b}), th1(z), th1(z+tau), den = sqrt(th1(z) th1(z+tau)) on the frame's branch"""
    T = 2 * tau
    X0 = th_char(a, b, z, T, nk); X1 = np.exp(1j * np.pi * float(b)) * th_char(a, b, z + tau, T, nk)
    t1 = th1(z, tau, nk); t1s = th1(z + tau, tau, nk)
    den = 1j * np.exp(-1j * np.pi * tau / 2) * np.exp(-1j * np.pi * z) * t1
    return X0, X1, t1, t1s, den


def herm(z, a, b, tau, nk=NK):
    """P = F F^dagger: (|F0|^2, |F1|^2, conj(F0) F1), branch-free given the frame's convention"""
    X0, X1, t1, t1s, den = doublet_parts(z, a, b, tau, nk)
    n0 = np.abs(X0) ** 2 / np.abs(t1); n1 = np.abs(X1) ** 2 / np.abs(t1s)
    c01 = np.conj(X0) * X1 * t1 / (np.abs(t1) * den)
    return n0, n1, c01


def trace_with(M, n0, n1, c01):
    """tr(M P), P = [[n0, conj(c01)], [c01, n1]]  (P_mn = F_m conj(F_n)), i.e. F^dagger M F"""
    return M[0, 0] * n0 + M[0, 1] * c01 + M[1, 0] * np.conj(c01) + M[1, 1] * n1


def integrand(a, b, tau, mats):
    def f(z):
        n0, n1, c01 = herm(z, a, b, tau)
        return np.stack([trace_with(M, n0, n1, c01) for M in mats], -1)
    return f


# ------------------------------------------------------------------ quadrature on {x + t tau}, dA = Im tau dx dt
_GL = {}
def nodes01(n):
    if n not in _GL:
        x, w = leggauss(n); _GL[n] = (0.5 * (x + 1), 0.5 * w)
    return _GL[n]


def _cuts(a0, a1):
    return [a0] + [float(m) for m in range(math.floor(a0) + 1, math.ceil(a1)) if a0 + 1e-12 < m < a1 - 1e-12] + [a1]


def _islat(x, t): return abs(x - round(x)) < 1e-12 and abs(t - round(t)) < 1e-12


def quad(fun, x0, x1, t0, t1, tau, n):
    """split at the integer lines, then each piece into four quadrants; a quadrant whose outer corner is a lattice
    point (where the modes' 1/|z| sits) is integrated by the Duffy map (two triangles, Jacobian u), the others by
    tensor Gauss-Legendre"""
    u, w = nodes01(n); U, V = np.meshgrid(u, u, indexing="ij"); W = np.outer(w, w)
    tot = 0
    xs, ts = _cuts(x0, x1), _cuts(t0, t1)
    for xa, xb in zip(xs[:-1], xs[1:]):
        for ta, tb in zip(ts[:-1], ts[1:]):
            xm, tm = 0.5 * (xa + xb), 0.5 * (ta + tb)
            for cx in (xa, xb):
                for ct in (ta, tb):
                    A, B = xm - cx, tm - ct
                    if _islat(cx, ct):
                        J = abs(A * B) * U * W
                        for XX, TT in ((cx + A * U, ct + B * U * V), (cx + A * U * V, ct + B * U)):
                            tot = tot + np.einsum("ij,ijk->k", J, fun(XX + TT * tau))
                    else:
                        tot = tot + np.einsum("ij,ijk->k", abs(A * B) * W, fun(cx + A * U + (ct + B * V) * tau))
    return tot * tau.imag


def vangles(t):
    v = [0.5 + 0.5 * t, -0.5 + 0.5 * t, -0.5 - 0.5 * t, 0.5 - 0.5 * t]
    br = sorted(float(np.mod(np.angle(z), 2 * np.pi)) for z in v); return br + [br[0] + 2 * np.pi]


def rmax(th, t):
    d = np.exp(1j * th); y1 = d.imag / t.imag; x1 = d.real - y1 * t.real; return 0.5 / np.maximum(abs(x1), abs(y1))


def quad_polar(fun, tau, nth=48, nr=32):
    """an independent route on the cell centred at the puncture: polar about 0, r from 0 to the cell's boundary
    (r |F|^2 is bounded), theta split at the four vertex angles"""
    xg, wg = leggauss(nth); xr, wr = leggauss(nr); br = vangles(tau); tot = 0
    for a_, b_ in zip(br[:-1], br[1:]):
        th = 0.5 * (b_ - a_) * xg + 0.5 * (b_ + a_); wt = 0.5 * (b_ - a_) * wg
        R = rmax(th, tau)
        r = 0.5 * R[:, None] * (xr[None, :] + 1); wr2 = 0.5 * R[:, None] * wr[None, :]
        z = r * np.exp(1j * th)[:, None]
        tot = tot + np.einsum("ij,ijk->k", wt[:, None] * wr2 * r, fun(z))
    return tot


# ------------------------------------------------------------------ the frame's functions (for the plumbing check)
def frame_funcs():
    V = pathlib.Path(next(ROOT.glob("frontier/B1691_*/verification")))
    spec = importlib.util.spec_from_file_location("b1656_funcs_ro", V / "correction" / "b1656_funcs.py")
    B = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(B)
    return B


def twist(q, line):
    p1, p2 = line
    return (q * p1, -2 * q * p2)


# ------------------------------------------------------------------ structure: monodromy and characters
def structure(a, b, tau, rng, npts=24):
    """r = F1/F0 (single-valued); Phi(1) ~ QI means r(z+1) = -r(z); Phi(tau) ~ [[0,1],[s,0]] means r(z+tau) r(z) = s.
    |F0|^2, |F1|^2 periodic under 1 and swapped under tau (so |F|^2 is a function on the torus: flat, no Gaussian)."""
    zs = (rng.uniform(0.08, 0.92, npts) + rng.uniform(0.08, 0.92, npts) * tau)
    X0, X1, t1, t1s, den = doublet_parts(zs, a, b, tau)
    r = X1 * t1 / (X0 * den)
    X0a, X1a, t1a, _, dena = doublet_parts(zs + 1, a, b, tau); ra = X1a * t1a / (X0a * dena)
    X0b, X1b, t1b, _, denb = doublet_parts(zs + tau, a, b, tau); rb = X1b * t1b / (X0b * denb)
    s_vals = rb * r
    s = complex(np.mean(s_vals))
    n0, n1, c01 = herm(zs, a, b, tau); n0a, n1a, c01a = herm(zs + 1, a, b, tau); n0b, n1b, c01b = herm(zs + tau, a, b, tau)
    out = {"r(z+1)+r(z)": float(np.max(np.abs(ra + r) / np.abs(r))),
           "s = r(z+tau) r(z)": [round(s.real, 12), round(s.imag, 12)],
           "s spread": float(np.max(np.abs(s_vals - s))),
           "|F0|^2,|F1|^2 periodic under 1": float(max(np.max(np.abs(n0a / n0 - 1)), np.max(np.abs(n1a / n1 - 1)))),
           "|F0|^2<->|F1|^2 under tau": float(max(np.max(np.abs(n0b / n1 - 1)), np.max(np.abs(n1b / n0 - 1)))),
           "|F|^2 periodic (1 and tau)": float(max(np.max(np.abs((n0a + n1a) / (n0 + n1) - 1)), np.max(np.abs((n0b + n1b) / (n0 + n1) - 1))))}
    sr = round(s.real)
    Phi1 = QI; Phitau = np.array([[0, 1], [sr, 0]], dtype=complex)
    # characters: C Phi = chi Phi C  (C Phi C^-1 = chi Phi)
    chi = {}
    for nm, C in BLOCKS:
        c1 = C @ Phi1 @ np.linalg.inv(C); ct = C @ Phitau @ np.linalg.inv(C)
        chi[nm] = (int(round((np.trace(c1 @ np.linalg.inv(Phi1)) / 2).real)), int(round((np.trace(ct @ np.linalg.inv(Phitau)) / 2).real)))
        assert np.allclose(c1, chi[nm][0] * Phi1) and np.allclose(ct, chi[nm][1] * Phitau)
    out["characters (chi(1), chi(tau)) of C_p F"] = chi
    # the cross-integrands' characters, measured: g_pq(z+gamma) = chi_p chi_q(gamma) g_pq(z)
    worst = 0.0
    for (p, Cp), (q, Cq) in itertools.combinations(BLOCKS, 2):
        M = Cp.conj().T @ Cq
        g, ga, gb = trace_with(M, n0, n1, c01), trace_with(M, n0a, n1a, c01a), trace_with(M, n0b, n1b, c01b)
        pr = (chi[p][0] * chi[q][0], chi[p][1] * chi[q][1])
        assert pr != (1, 1)
        scale = np.abs(n0) + np.abs(n1)
        worst = max(worst, float(np.max(np.abs(ga - pr[0] * g) / scale)), float(np.max(np.abs(gb - pr[1] * g) / scale)))
    out["cross-integrand character residual"] = worst
    out["cross characters nontrivial"] = all((chi[p][0] * chi[q][0], chi[p][1] * chi[q][1]) != (1, 1) for (p, _), (q, _) in itertools.combinations(BLOCKS, 2))
    return out, Phi1, Phitau, chi


# ------------------------------------------------------------------ the Gram matrices for one (twist, tau)
OFF = (-0.37113, -0.42371)       # a generic offset for the cover's fundamental domain


def gram_from(vals):
    return np.array(vals).reshape(3, 3)


def gram_stats(G):
    d = np.real(np.diag(G))
    off = max(abs(G[p, q]) / math.sqrt(d[p] * d[q]) for p in range(3) for q in range(3) if p != q)
    return float(off), float(d.max() / d.min() - 1), d


def gram_job(args):
    key, a, b, tau = args
    t0 = time.time()
    mats = [Cp.conj().T @ Cq for _, Cp in BLOCKS for _, Cq in BLOCKS]
    f = integrand(a, b, tau, mats)
    res = {}
    for n in (20, 32):
        res["cover_n%d" % n] = quad(f, OFF[0], OFF[0] + 2, OFF[1], OFF[1] + 2, tau, n) / 4
    res["cell_P0"] = quad(f, -0.5, 0.5, -0.5, 0.5, tau, 32)               # centred at the puncture
    res["cell_Phalf"] = quad(f, 0.0, 1.0, 0.0, 1.0, tau, 32)              # centred at (1 + tau)/2
    res["cell_P0+1"] = quad(f, 0.5, 1.5, -0.5, 0.5, tau, 32)
    res["cell_P0+tau"] = quad(f, -0.5, 0.5, 0.5, 1.5, tau, 32)
    res["polar_P0"] = quad_polar(f, tau)
    out = {"key": key, "a": str(a), "b": str(b), "tau": [tau.real, tau.imag]}
    Gc = gram_from(res["cover_n32"]); off, spread, d = gram_stats(Gc)
    Gc20 = gram_from(res["cover_n20"])
    out["cover"] = {"max_offdiag": off, "max_diag_spread": spread, "norm_F2": float(d[0]),
                    "conv_n20_vs_n32_diag": float(abs(Gc20[0, 0] - Gc[0, 0]) / abs(Gc[0, 0])),
                    "conv_n20_vs_n32_offdiag": float(np.max(np.abs(Gc20 - Gc - np.diag(np.diag(Gc20 - Gc)))) / abs(Gc[0, 0]))}
    for nm in ("cell_P0", "cell_Phalf", "cell_P0+1", "cell_P0+tau", "polar_P0"):
        G = gram_from(res[nm]); o, s_, dd = gram_stats(G)
        out[nm] = {"max_offdiag": o, "max_diag_spread": s_, "norm_F2": float(dd[0]),
                   "offdiag_entries_normalised": {"%s%s" % (BLOCKS[p][0], BLOCKS[q][0]): [round(float((G[p, q] / dd[0]).real), 12), round(float((G[p, q] / dd[0]).imag), 12)]
                                                  for p, q in ((0, 1), (0, 2), (1, 2))}}
    out["norm_F2: cover vs P0 (Duffy) vs P0 (polar)"] = [float(d[0]), out["cell_P0"]["norm_F2"], out["polar_P0"]["norm_F2"]]
    out["norm route difference (Duffy vs polar)"] = abs(out["cell_P0"]["norm_F2"] / out["polar_P0"]["norm_F2"] - 1)
    out["seconds"] = round(time.time() - t0, 2)
    return out


# ------------------------------------------------------------------ controls
def control_singular():
    out = {}
    for tau in (1j, 0.3 + 1.2j, 0.45 + 2.6j):
        f = lambda z: (1 / np.abs(z))[..., None]
        val = quad(f, -0.5, 0.5, -0.5, 0.5, tau, 32)[0].real
        br = vangles(tau)
        mp.mp.dps = 30
        ref = mp.fsum(mp.quad(lambda th: 0.5 / max(abs(mp.cos(th) - mp.sin(th) / tau.imag * tau.real), abs(mp.sin(th) / tau.imag)), [a_, b_]) for a_, b_ in zip(br[:-1], br[1:]))
        out[str(tau)] = {"duffy": val, "polar_reference": float(ref), "rel_error": abs(val / float(ref) - 1)}
    out["exact at tau = i: 4 ln(1 + sqrt 2)"] = 4 * math.log(1 + math.sqrt(2))
    return out


def magnetised(N, tau, kappa=None):
    def f(z):
        h = np.exp(-2 * np.pi * N * z.imag ** 2 / tau.imag)
        ps = [th_char(Fr(j, N), 0, N * z, N * tau, nk=30) for j in range(N)]
        if kappa is not None: ps[1] = ps[1] + kappa * ps[0]
        return np.stack([np.conj(ps[j]) * ps[k] * h for j in range(N) for k in range(N)], -1)
    return f


def control_magnetised():
    out = {}
    for N in (2, 3, 5):
        for tau in (1j, 0.3 + 1.2j, 0.5 + 2.5j):
            exact = math.sqrt(tau.imag / (2 * N))
            row = {}
            for nm, box in (("cell centred at 0", (-0.5, 0.5, -0.5, 0.5)), ("cell with lattice corners", (0, 1, 0, 1)), ("generic cell", (0.137, 1.137, -0.291, 0.709))):
                G = quad(magnetised(N, tau), *box, tau, 32).reshape(N, N)
                d = np.real(np.diag(G))
                row[nm] = {"max_offdiag": float(max(abs(G[j, k]) / math.sqrt(d[j] * d[k]) for j in range(N) for k in range(N) if j != k)),
                           "max_diag_spread": float(d.max() / d.min() - 1), "max |G_jj/exact - 1|": float(np.max(np.abs(d / exact - 1)))}
            out["N=%d tau=%s" % (N, tau)] = row
    # negative control: a non-orthogonal basis psi_1 + kappa psi_0
    kappa = 0.3; tau = 0.3 + 1.2j; N = 3
    G = quad(magnetised(N, tau, kappa), -0.5, 0.5, -0.5, 0.5, tau, 32).reshape(N, N)
    d = np.real(np.diag(G))
    out["negative: psi_1 + 0.3 psi_0 (N = 3, tau = 0.3+1.2i)"] = {"offdiag_01": float(abs(G[0, 1]) / math.sqrt(d[0] * d[1])), "predicted": kappa / math.sqrt(1 + kappa ** 2),
                                                                   "diag_ratio_11/00": float(d[1] / d[0]), "predicted_ratio": 1 + kappa ** 2}
    return out


def control_frame_negative(a, b, tau, theta=0.3):
    """(ii) a rotated block in place of QI: C' = cos(th) QI + sin(th) QJ (a unit quaternion of mixed character);
    predicted on the cover: <QJ F, C' F> / |F|^2 = sin(th) * <QJ F, QJ F>/|F|^2 = sin(th) (the QI part averages out)."""
    Cp = math.cos(theta) * QI + math.sin(theta) * QJ
    blocks = [QJ, Cp, QK]
    mats = [A.conj().T @ Bm for A in blocks for Bm in blocks]
    f = integrand(a, b, tau, mats)
    G = gram_from(quad(f, OFF[0], OFF[0] + 2, OFF[1], OFF[1] + 2, tau, 32) / 4)
    d = np.real(np.diag(G))
    return {"theta": theta, "cover offdiag (QJ, C')": float(abs(G[0, 1]) / math.sqrt(d[0] * d[1])), "predicted": math.sin(theta),
            "cover offdiag (C', QK)": float(abs(G[1, 2]) / math.sqrt(d[1] * d[2])), "predicted (C',QK)": math.sin(theta)}


def invariant_metrics(Phi1, Phitau, chi):
    """K: the real dimension of the hermitian 6x6 forms X on (+)_p V (x) L_chi_p with rho^dagger X rho = X, rho = blockdiag(chi_p Phi)
    (the flat structure alone); then with the generations' characters also imposed as a symmetry on the multiplicity index
    alone (blockdiag(chi_p(g) I2)); then the cover typing (a metric K on V with Phi^dagger K Phi = K)."""
    def dim_inv(gens, n):
        # unknown X hermitian n x n: real parametrisation by n^2 reals
        basis = []
        for i in range(n):
            E = np.zeros((n, n), dtype=complex); E[i, i] = 1; basis.append(E)
        for i in range(n):
            for j in range(i + 1, n):
                E = np.zeros((n, n), dtype=complex); E[i, j] = E[j, i] = 1; basis.append(E)
                E = np.zeros((n, n), dtype=complex); E[i, j] = 1j; E[j, i] = -1j; basis.append(E)
        rows = []
        for g in gens:
            cols = [g.conj().T @ E @ g - E for E in basis]
            rows.append(np.array([np.concatenate([c.real.ravel(), c.imag.ravel()]) for c in cols]).T)
        A = np.vstack(rows); s = np.linalg.svd(A, compute_uv=False)
        return int(sum(s < 1e-10 * max(1, s.max()))) + max(0, len(basis) - len(s))
    rho = [np.kron(np.diag([chi[p][k] for p, _ in BLOCKS]).astype(complex), P) for k, P in ((0, Phi1), (1, Phitau))]
    d_flat = dim_inv(rho, 6)
    flav = [np.kron(np.diag([chi[p][k] for p, _ in BLOCKS]).astype(complex), I2) for k in (0, 1)]
    d_flav = dim_inv(rho + flav, 6)
    d_cover = dim_inv([Phi1, Phitau], 2)
    return {"flat structure alone (real dim)": d_flat, "plus the characters as a symmetry of the multiplicity index": d_flav,
            "cover typing: metric on V (2x2) invariant under the deck action Phi": d_cover}


def control_invariant_mixing(a, b, tau):
    """(iii) the flat-invariant cross pairing: X_pq = H_pq C_p C_q^-1 on the blocks.  Its integrand on the zero modes is
    H_pq |F|^2, a function on the torus, so every cell gives the same nonzero off-diagonal H_pq."""
    H = np.array([[1.0, 0.2, 0.0], [0.2, 1.0, 0.1j], [0.0, -0.1j, 1.0]])
    Cs = [C for _, C in BLOCKS]
    mats = [Cs[p].conj().T @ (H[p, q] * Cs[p] @ np.linalg.inv(Cs[q])) @ Cs[q] for p in range(3) for q in range(3)]
    f = integrand(a, b, tau, mats)
    out = {}
    for nm, box in (("cell_P0", (-0.5, 0.5, -0.5, 0.5)), ("cell_Phalf", (0, 1, 0, 1)), ("cover/4", (OFF[0], OFF[0] + 2, OFF[1], OFF[1] + 2))):
        G = gram_from(quad(f, *box, tau, 32)) / (4 if nm == "cover/4" else 1)
        out[nm] = {"G/|F|^2": [[[round(float(x.real), 10), round(float(x.imag), 10)] for x in row] for row in G / G[0, 0].real]}
    out["H"] = [[[x.real, x.imag] for x in row] for row in H.astype(complex)]
    # the invariance of the cross pairing, algebraically: Phi^dagger (C_p C_q^-1) Phi = chi_p chi_q (gamma) C_p C_q^-1
    return out


# ------------------------------------------------------------------ the sample
TAUS = [1j, 0.25 + 1.0j, 0.5 + 1.5j, 0.05 + 2.05j, 0.35 + 2.75j, 0.2 + 3.0j, 0.85 + 3.45j, 0.5 + 4.0j, 0.3 + 6.0j]
LINES = ([("zero", (Fr(0), Fr(0)))] + [("2/5,%d/10" % k, (Fr(2, 5), Fr(k, 10))) for k in range(10)]
         + [("ord4 %s,%s" % (p, q), (Fr(p), Fr(q))) for p, q in (("1/4", "0"), ("0", "1/4"), ("1/4", "1/4"), ("1/4", "1/2"), ("1/2", "1/4"), ("1/4", "3/4"))]
         + [("ord2 %s,%s" % (p, q), (Fr(p), Fr(q))) for p, q in (("1/2", "0"), ("0", "1/2"), ("1/2", "1/2"))]
         + [("ord3 1/3,0", (Fr(1, 3), Fr(0))), ("ord3 1/3,2/3", (Fr(1, 3), Fr(2, 3))), ("ord9 1/9,1/9", (Fr(1, 9), Fr(1, 9))),
            ("ord12 1/12,5/12", (Fr(1, 12), Fr(5, 12))), ("ord12 5/12,1/12", (Fr(5, 12), Fr(1, 12))), ("ord7 2/7,3/7", (Fr(2, 7), Fr(3, 7)))])


def main():
    t_start = time.time()
    R = {"what": "T-NORM on FR-FIB's matter zero modes (P-525); data-free", "NK": NK}
    rng = np.random.default_rng(525)
    # P0: plumbing against the frame's code
    B = frame_funcs()
    worst_bil = worst_tw = 0.0
    for _ in range(40):
        tau = complex(rng.uniform(0, 0.9), rng.uniform(1.0, 4.0))
        line = (Fr(int(rng.integers(0, 12)), 12), Fr(int(rng.integers(0, 12)), 12))
        for fld, q in CHARGE.items():
            x_mine = twist(q, line)
            w = B.line_w(line[0], line[1], tau); xf, _ = B.sector_twists(w, tau, q, 1)
            worst_tw = max(worst_tw, abs(float(x_mine[0]) - xf[0]), abs(float(x_mine[1]) - xf[1]))
        q1, q2 = rng.choice(list(CHARGE.values()), 2)
        x, y = twist(int(q1), line), twist(int(q2), line)
        z = complex(rng.uniform(0.05, 0.95), 0) + rng.uniform(0.05, 0.95) * tau
        Mf = B.bil((float(x[0]), float(x[1])), (float(y[0]), float(y[1])), np.array(z), tau)
        X0, X1, t1, t1s, den = doublet_parts(np.array(z), x[0], x[1], tau)
        Y0, Y1, _, _, _ = doublet_parts(np.array(z), y[0], y[1], tau)
        mine = np.array([[X0 * Y0 / t1, X0 * Y1 / den], [X1 * Y0 / den, X1 * Y1 / t1s]])
        worst_bil = max(worst_bil, float(np.max(np.abs(mine - np.array(Mf, dtype=complex))) / np.max(np.abs(mine))))
    # truncation of my series
    zt = np.array([0.3 + 1.7 * (0.5 + 3.4j), 0.9 + 2.6 * (0.2 + 1.1j)])
    trunc = max(float(np.max(np.abs(np.array(herm(zt, Fr(2, 5), Fr(-3, 5), 0.5 + 3.4j)) - np.array(herm(zt, Fr(2, 5), Fr(-3, 5), 0.5 + 3.4j, nk=60))))), 0.0)
    R["P0_plumbing"] = {"bil (holomorphic F_x F_y^T) vs the frame's b1656_funcs.bil, max rel": worst_bil,
                        "twist (q p1, -2 q p2) vs the frame's line_w/sector_twists, max abs": worst_tw,
                        "series truncation NK=24 vs 60 (abs, on herm at Im z up to 2.6 Im tau)": trunc}
    print("P0", R["P0_plumbing"], flush=True)
    R["C+_singular_quadrature"] = control_singular(); print("C+ singular", R["C+_singular_quadrature"], flush=True)
    R["C+-_magnetised"] = control_magnetised(); print("C+- magnetised done", flush=True)
    # S: structure at every (field, tau, line); K and the frame controls at a few
    jobs, struct, seen = [], {}, {}
    worst_s = {"r(z+1)+r(z)": 0, "s spread": 0, "|F0|^2,|F1|^2 periodic under 1": 0, "|F0|^2<->|F1|^2 under tau": 0, "|F|^2 periodic (1 and tau)": 0,
               "cross-integrand character residual": 0}
    s_values, chis = set(), set()
    for tau in TAUS:
        for lname, line in LINES:
            for fld, q in CHARGE.items():
                a, b = twist(q, line)
                cls = (a % 1, b % 1, tau)               # |F|^2 and the Gram depend on (a, b) mod 1 (up to constant phases)
                st, P1, Pt, chi = structure(a, b, tau, rng)
                for k_ in worst_s: worst_s[k_] = max(worst_s[k_], st[k_])
                s_values.add(tuple(st["s = r(z+tau) r(z)"])); chis.add(json.dumps(st["characters (chi(1), chi(tau)) of C_p F"], sort_keys=True))
                assert st["cross characters nontrivial"]
                if cls not in seen:
                    seen[cls] = len(jobs); jobs.append(("%s|%s|%s" % (fld, lname, tau), a, b, tau))
                struct.setdefault("%s|%s|%s" % (fld, lname, tau), seen[cls])
    R["S_structure_worst_over_all_configs"] = worst_s
    R["S_s_values_seen"] = sorted(s_values); R["S_character_tables_seen"] = sorted(chis)
    R["S_configs"] = len(struct); R["S_distinct_twist_classes"] = len(jobs)
    print("S", worst_s, R["S_s_values_seen"], R["S_character_tables_seen"], len(struct), len(jobs), flush=True)
    st, P1, Pt, chi = structure(Fr(2, 5), Fr(-1, 5), 0.35 + 2.75j, rng)
    R["K_invariant_metrics"] = invariant_metrics(P1, Pt, chi)
    R["K_intertwiner_invariance"] = float(max(np.max(np.abs(P.conj().T @ (Cp @ np.linalg.inv(Cq)) @ P - chi[p][k] * chi[q][k] * (Cp @ np.linalg.inv(Cq))))
                                             for (p, Cp), (q, Cq) in itertools.product(BLOCKS, BLOCKS) for k, P in ((0, P1), (1, Pt))))
    print("K", R["K_invariant_metrics"], R["K_intertwiner_invariance"], flush=True)
    R["C-_frame_rotated_block"] = {str(t): control_frame_negative(Fr(2, 5), Fr(-1, 5), t) for t in (1j, 0.35 + 2.75j)}
    R["C-_invariant_nonproduct_metric"] = {str(t): control_invariant_mixing(Fr(2, 5), Fr(-1, 5), t) for t in (1j, 0.35 + 2.75j)}
    print("C- frame done", flush=True)
    # G: the Gram matrices
    with Pool(int(os.environ.get("TN_WORKERS", "3"))) as Pl:
        res = Pl.map(gram_job, jobs, chunksize=1)
    R["G_results"] = res
    R["G_config_to_class"] = struct
    R["seconds"] = round(time.time() - t_start, 1)
    json.dump(R, open(OUT, "w"), indent=1, default=str)
    print("done", R["seconds"], "s;", len(res), "twist classes", flush=True)


if __name__ == "__main__":
    main()
