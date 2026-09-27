#!/usr/bin/env python3
"""B1388, post-seal -- the anatomy of the cutoff dependence.  Not part of the sealed test (cutoff_test.py is).

Two counts agree at large height and can differ at a finite cut:
- the sealed one, the relative index -chi(d+M_T) with d+_{c,T} = {g_{c,T} > 0}, g = dF/dh on the cut;
- the signed number of zeros of the Higgs field omega = dF inside M_T.
Morse's boundary formula (for V = grad F on M_T, Ind V + Ind d_-V = chi(M_T) = 0, d_-V the tangential projection on the part of the
cut where V points inward) gives the second exactly:
    sum over the zeros of omega in M_T of their indices = sum_c Phi_c(T_c),
    Phi_c(T) = sum of the indices of the critical points of f = F(., T) at which g > 0.
The tangential projection of V to the cut is grad f (conformally), and it is non-zero where V is tangent to the cut, so no correction
term enters.  Phi_c changes only when a Higgs zero crosses height T.  chi(d+_{c,T}) changes when g has a critical point on its zero
level.  They agree when grad f points out of {g > 0} all along {g = 0}, as at large height (f = a(h) phi, g = a'(h) phi, a a' < 0).
So B1387's N = -sum_c chi(d+_c) is minus the signed number of Higgs zeros on the whole cusped manifold.

(a) THE ZEROS.  Every zero of dF at cusp-c height in [tau_emb(c), 20 tau_emb(c)], by damped Newton on (s, t, h) from a grid of seeds,
    at K_n = 14 and 20, with index sign det Hess F and the harmonicity check (at a zero, Delta_hyp F = h^2 tr Hess_Euclid F = 0).
    Each zero is pulled into the manifold and its height over the other Eisenstein cusp read, so the zeros are identified across
    charts.
(b) THE AXES.  dF/dh along the vertical line over each fixed point of the order-3 rotation R at cusp 0 (on it grad_x F = 0 by
    symmetry): its sign changes, i.e. the zeros on R's axes.
(c) THE JOINT EMBEDDING AND THE TOUCHING POINTS.  SnapPy's neighbourhoods of cusps 0 and 3 grown together (cusps 1 and 2 shrunk) until
    they touch: the joint height tau_joint; the touching points on cusp 0's torus (the cusp-3 height maximised at cusp-0 height
    tau_joint), and their offset from the zeros found in (a).
(d) MORSE'S BOUNDARY COUNT Phi_c(tau) against chi(d+_{c,tau}) over each cusp's range.
(e) THE SEALED RUN'S TRANSITION POINTS.  At each transition height bisected by cutoff_test.py, the critical points of g nearest the
    zero level and |grad_x F| there: a Higgs zero needs grad_x F = 0 as well.
Usage: python3 higgs_zeros.py"""
import math
import sys
import time
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
import numpy as np
from scipy.optimize import minimize
from scipy.special import k0, k1

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import cutoff_test as CT                        # the sealed test's functions (B1387's instrument as CT.HF, B1386's as CT.T)

HF, T = CT.HF, CT.T
SEALED_TRANSITIONS = {0: (0.0986149, 0.1052703, 0.1866807), 3: (0.0986262, 0.1052530, 0.1866900)}   # cutoff_test_run.txt


def _modes(S, x, c):
    mm, nn, kk = S.modes[c]
    cc = np.array([S.coefficient(x, c, j) for j in range(len(kk))])
    return mm.astype(float), nn.astype(float), kk, cc


def derivs(S, x, c, P):
    """F - A_c, grad F and Hess F in the coordinates (s, t, h) at the points P (N x 3): s, t lattice coordinates, h chart height.
    F = A_c + sum_j a_j(h) Re(c_j e^{2 pi i (m_j s + n_j t)}), a_j = 2 h K_1(2 pi k_j h)."""
    mm, nn, kk, cc = _modes(S, x, c)
    s, t, h = P[:, 0:1], P[:, 1:2], P[:, 2:3]
    a = 2 * np.pi * kk[None, :] * h
    A0 = 2 * h * k1(a)
    A1 = -4 * np.pi * kk[None, :] * h * k0(a)
    A2 = -4 * np.pi * kk[None, :] * (k0(a) - a * k1(a))
    E = cc[None, :] * np.exp(2j * np.pi * (s * mm[None, :] + t * nn[None, :]))
    iE, q = 2j * np.pi * E, -4 * np.pi ** 2 * E
    F = np.sum(A0 * E.real, axis=1)
    g = np.stack([np.sum(A0 * (iE * mm).real, 1), np.sum(A0 * (iE * nn).real, 1), np.sum(A1 * E.real, 1)], 1)
    H = np.empty((len(P), 3, 3))
    H[:, 0, 0] = np.sum(A0 * (q * mm * mm).real, 1)
    H[:, 0, 1] = H[:, 1, 0] = np.sum(A0 * (q * mm * nn).real, 1)
    H[:, 1, 1] = np.sum(A0 * (q * nn * nn).real, 1)
    H[:, 0, 2] = H[:, 2, 0] = np.sum(A1 * (iE * mm).real, 1)
    H[:, 1, 2] = H[:, 2, 1] = np.sum(A1 * (iE * nn).real, 1)
    H[:, 2, 2] = np.sum(A2 * E.real, 1)
    return F, g, H


def grad_scale(S, x, c, h):
    """a bound on the components of grad F at height(s) h: sum_j |c_j| (2 pi (|m_j| + |n_j|) |a_j| + |a_j'|)"""
    mm, nn, kk, cc = _modes(S, x, c)
    h = np.atleast_1d(h)[:, None]
    a = 2 * np.pi * kk[None, :] * h
    return np.sum(np.abs(cc)[None, :] * (2 * np.pi * (np.abs(mm) + np.abs(nn))[None, :] * 2 * h * k1(a)
                                         + 4 * np.pi * kk[None, :] * h * k0(a)), axis=1)


def zeros(S, x, c, tau_lo, tau_hi, ns=16, nh=24, iters=80):
    """the zeros of dF at cusp c with height tau in [tau_lo, tau_hi]: [((s, t, tau), index, Hessian eigenvalues, trace check)]"""
    sc = S.s[c]
    g1 = (np.arange(ns) + 0.5) / ns
    P = np.array([(a, b, h) for a in g1 for b in g1 for h in np.geomspace(tau_lo, tau_hi, nh) * sc])
    active = np.arange(len(P))
    for _ in range(iters):
        _, g, H = derivs(S, x, c, P[active])
        try:
            step = np.linalg.solve(H, g[:, :, None])[:, :, 0]
        except np.linalg.LinAlgError:
            step = np.array([np.linalg.lstsq(Hi, gi, rcond=None)[0] for Hi, gi in zip(H, g)])
        damp = np.maximum.reduce([np.abs(step[:, 0]) / 0.05, np.abs(step[:, 1]) / 0.05, np.abs(step[:, 2]) / (0.1 * P[active, 2]),
                                  np.ones(len(active))])
        step = step / damp[:, None]
        P[active] = P[active] - step
        P[active, 0:2] %= 1.0
        P[active, 2] = np.clip(P[active, 2], 0.5 * tau_lo * sc, 4 * tau_hi * sc)
        active = active[np.abs(step).max(axis=1) >= 1e-14]
        if not len(active):
            break
    F, g, H = derivs(S, x, c, P)
    conv = np.abs(g).max(axis=1) <= 1e-10 * grad_scale(S, x, c, P[:, 2])
    inr = (P[:, 2] >= tau_lo * sc) & (P[:, 2] <= tau_hi * sc)
    b1, b2 = S.C.lat[c]
    Li = np.linalg.inv(np.array([[b1.real, b2.real], [b1.imag, b2.imag]]))      # (x, y) -> (s, t)
    out = []
    for X, Hc in zip(P[conv & inr], H[conv & inr]):
        if any(np.abs((X[:2] - o[0][:2] + 0.5) % 1.0 - 0.5).max() < 1e-7 and abs(X[2] / sc - o[0][2]) < 1e-7 for o in out):
            continue
        Hxy = Li.T @ Hc[:2, :2] @ Li
        trace = (np.trace(Hxy) + Hc[2, 2]) / np.abs(np.linalg.eigvalsh(Hc)).max()
        out.append((np.array([X[0], X[1], X[2] / sc]), int(np.sign(np.linalg.det(Hc))), np.linalg.eigvalsh(Hc), trace))
    return sorted(out, key=lambda z: z[0][2])


def other_heights(S, c, X):
    """the point X = (s, t, tau) of cusp c's chart, pulled into the polyhedron: the largest normalised height over each cusp among the
    vertices of the tetrahedron containing it (a lower bound on the height in that cusp's region)"""
    b1, b2 = S.C.lat[c]
    i0 = next(i for i in range(S.P.ntet) for vv in HF.V if S.P.vclass[i][vv] == S.C.base[c])
    i, Ps, acc, _ = S.P.walk(i0, HF.act(S.C.A[c], (X[0] * b1 + X[1] * b2, X[2] * S.s[c])), S.v)
    out = {}
    for vv in HF.V:
        u = S.P.vclass[i][vv]
        cc = S.C.cusp_of_vertex[u]
        out[cc] = max(out.get(cc, 0.0), S.C.to_chart(cc, u, Ps)[1] / S.s[cc])
    return out


def joint_height(M):
    """SnapPy: cusps 1 and 2 shrunk, cusps 0 and 3 grown by equal displacements until they touch; tau_joint = 1/sqrt(2 V)"""
    CN = M.copy().cusp_neighborhood()
    for c in (1, 2):
        CN.set_displacement(-2.0, c)
    lo, hi = -3.0, 3.0
    for _ in range(60):
        d = 0.5 * (lo + hi)
        CN.set_displacement(d, 0)
        CN.set_displacement(d, 3)
        ok = CN.stopping_displacement(0) >= d - 1e-12 and CN.stopping_displacement(3) >= d - 1e-12
        lo, hi = (d, hi) if ok else (lo, d)
    CN.set_displacement(lo, 0)
    CN.set_displacement(lo, 3)
    V0, V3 = CN.volume(0), CN.volume(3)
    return 1 / math.sqrt(2 * V0), 1 / math.sqrt(2 * V3), V0, V3, CN.stopper(0), CN.stopper(3)


def touching_point(S, tj, guess):
    """the point of cusp 0's torus at height tj where the cusp-3 height is largest (Nelder-Mead from guess)"""
    f = lambda p: -other_heights(S, 0, (p[0] % 1, p[1] % 1, tj)).get(3, 0.0)
    r = minimize(f, list(guess), method="Nelder-Mead", options={"xatol": 1e-10, "fatol": 1e-13, "maxiter": 3000})
    return r.x[0] % 1, r.x[1] % 1, -r.fun


def axis_zeros(S, x, c, fixed, lo, hi, n=4000):
    """dF/dh along the vertical line over each fixed point of R at cusp c: the heights where it changes sign, and the largest
    |grad_x F| / scale on the line (zero by symmetry)"""
    taus = np.linspace(lo, hi, n)
    out = []
    for fp in fixed:
        P = np.array([(fp[0], fp[1], t * S.s[c]) for t in taus])
        _, g, _ = derivs(S, x, c, P)
        ch = [float(taus[j]) for j in np.where(np.diff(np.sign(g[:, 2])) != 0)[0]]
        out.append((fp, ch, float(np.max(np.abs(g[:, :2]).max(axis=1) / grad_scale(S, x, c, P[:, 2])))))
    return out


def f_terms(S, x, c, h, rel=1e-13):
    """the torus function f = F(., h) - A_c in B1386's term format (as CT.torus_terms does for g = dF/dh)"""
    mm, nn, kk = S.modes[c]
    coef = np.array([S.coefficient(x, c, j) for j in range(len(kk))]) * (h * k1(2 * np.pi * kk * h))
    keep = np.abs(coef) > rel * np.abs(coef).max()
    terms = []
    for z, m, n in zip(coef[keep], mm[keep], nn[keep]):
        terms += [(complex(z), (int(m), int(n))), (complex(np.conj(z)), (-int(m), -int(n)))]
    return terms


def phi(S, x, c, tau):
    """Morse's boundary count Phi_c(tau); completeness (the indices of all critical points of f sum to chi(T^2) = 0); and the smallest
    |g| at a critical point of f relative to max |g| (the distance from a Higgs zero on the cut)"""
    h = tau * S.s[c]
    ft, gt = f_terms(S, x, c, h), CT.torus_terms(S, x, c, h)
    for seeds in (64, 128):
        pts = T.critical_points(ft, seeds=seeds)
        total = sum(1 if k != "saddle" else -1 for _, _, k in pts)
        if total == 0:
            break
    gv = np.array([T.value_at(gt, p) for p, _, _ in pts])
    Phi = sum((1 if k != "saddle" else -1) for (p, _, k), v in zip(pts, gv) if v > 0)
    return Phi, total == 0, float(np.abs(gv).min() / np.abs(T.grid_values(gt, 96)).max())


def transition_points(S, x, c, tau, nshow=3):
    """the critical points of g nearest its zero level at height tau: [(s, t), g / max|critical value|, kind, |grad_x F| / max]"""
    h = tau * S.s[c]
    pts = T.critical_points(CT.torus_terms(S, x, c, h), seeds=128)
    top = max(abs(v) for _, v, _ in pts)
    g1 = np.arange(48) / 48
    _, grid, _ = derivs(S, x, c, np.array([(a, b, h) for a in g1 for b in g1]))
    gx = np.abs(grid[:, :2]).max()
    out = []
    for p, v, k in sorted(pts, key=lambda q: abs(q[1]))[:nshow]:
        _, gr, _ = derivs(S, x, c, np.array([[p[0], p[1], h]]))
        out.append(((float(p[0]), float(p[1])), v / top, k, float(np.abs(gr[0, :2]).max() / gx)))
    return out


if __name__ == "__main__":
    t0 = time.time()
    M = HF.member()
    tj0, tj3, V0, V3, st0, st3 = joint_height(M)
    print("B1388 post-seal: the anatomy of the cutoff dependence.", flush=True)
    print("=== (c) the joint embedding: cusps 0 and 3 grown together touch at volume %.5f, %.5f (9 sqrt3 = %.5f); tau_joint = %.7f, %.7f;"
          " each stopped by cusp %d, %d ===" % (V0, V3, 9 * math.sqrt(3), tj0, tj3, st0, st3), flush=True)
    for Kn in (14, 20):
        S, x, st = HF.solve(M, Kn, 0.10, 1, 1)
        emb = CT.embedded_heights(M, S)
        print("--- K_n %d (fit residual %.1e, test residual %.1e) ---" % (Kn, st["fit residual rms"], st["test residual rms"]), flush=True)
        print("=== (a) the zeros of omega = dF in each cusp's embedded range [tau_emb, 20 tau_emb] ===", flush=True)
        found = {}
        for c in range(4):
            te = emb[c]["tau_emb"]
            zs = zeros(S, x, c, te, 20 * te)
            found[c] = zs
            print("cusp %d, tau in [%.4f, %.4f]: %d zeros, index sum %+d" % (c, te, 20 * te, len(zs), sum(z[1] for z in zs)), flush=True)
            for X, ind, ev, tr in zs:
                oh = other_heights(S, c, X).get(3 - c if c in (0, 3) else -1)
                print("   tau %.7f (s, t) = (%.5f, %.5f) index %+d | trace check %.0e | height over the other Eisenstein cusp %s" % (
                    X[2], X[0], X[1], ind, tr, "%.7f" % oh if oh is not None else "(no vertex of it in this tetrahedron)"),
                    flush=True)
            if c == 2 and zs:
                # cusp 2's first shell is killed exactly by R's order-3 translation (B1386 S4); the solve returns it at ~1e-5, and far up
                # it outlives the leading sqrt3-shell (the same residue as cutoff_checks.py (c)).  Set it to its exact value, zero:
                mm, nn, kk = S.modes[2]
                first = [j for j in range(len(kk)) if abs(kk[j] - kk[0]) < 1e-6 * kk[0]]
                xz = x.copy()
                for j in first:
                    xz[S.first[2] + 2 * j] = xz[S.first[2] + 2 * j + 1] = 0.0
                zz = zeros(S, xz, 2, te, 20 * te)
                print("   with the killed first shell (residue |c| sqrt(covol) = %.0e) set to its exact value, zero: %d zeros" % (
                    max(abs(S.coefficient(x, 2, j)) for j in first) * S.s[2], len(zz)), flush=True)
        print("=== (b) the axes: dF/dh along the vertical lines over R's fixed points at cusp 0 ===", flush=True)
        fixed = [tuple(z[0][:2]) for z in found[0] if z[0][2] < 0.12]
        for fp, ch, gx in axis_zeros(S, x, 0, fixed, emb[0]["tau_emb"], 0.40):
            print("   over (%.5f, %.5f): sign changes of dF/dh at tau %s; |grad_x F|/scale on the line <= %.0e" % (
                fp[0], fp[1], ["%.5f" % t for t in ch], gx), flush=True)
        print("=== (c) the touching points against the zeros near tau_joint ===", flush=True)
        for X, ind, ev, tr in found[0]:
            if abs(X[2] - tj0) < 1e-3:
                ps, pt, h3 = touching_point(S, tj0, X[:2])
                _, g, _ = derivs(S, x, 0, np.array([[ps, pt, tj0 * S.s[0]]]))
                print("   touching point (%.6f, %.6f), cusp-3 height there %.7f; zero minus touching point (ds, dt, dtau) = (%.0e, %.0e, "
                      "%.0e); |dF| at the touching point / scale %.0e" % (ps, pt, h3, X[0] - ps, X[1] - pt, X[2] - tj0,
                                                                         np.abs(g[0]).max() / grad_scale(S, x, 0, tj0 * S.s[0])[0]),
                      flush=True)
        if Kn == 20:
            break
        print("=== (d) Morse's boundary count Phi_c(tau) against chi(d+_{c,tau}) ===", flush=True)
        for c in range(4):
            te = emb[c]["tau_emb"]
            rows = []
            for tau in np.geomspace(te, 20 * te, 60 if c in (0, 3) else 12):
                try:
                    rows.append((tau,) + phi(S, x, c, tau))
                except (ValueError, MemoryError):          # a field too close to one direction for isolated critical points
                    rows.append((tau, None, False, float("nan")))
            vals = sorted(set(r[1] for r in rows if r[1] is not None))
            print("cusp %d: Phi values %s over %d heights (complete %d); smallest |g| at a critical point of f / max |g| %.1e" % (
                c, vals, len(rows), sum(1 for r in rows if r[2]), np.nanmin([r[3] for r in rows])), flush=True)
            for (t1, p1, *_), (t2, p2, *_) in zip(rows, rows[1:]):
                if p1 is not None and p2 is not None and p1 != p2:
                    print("   Phi changes between tau %.5f and %.5f: %+d -> %+d" % (t1, t2, p1, p2), flush=True)
            if c in (0, 3):
                for tau in (0.095, 0.10, 0.12, 0.15, 0.183, 0.25):
                    print("   tau %.3f: Phi %+d, chi(d+) %+d" % (tau, phi(S, x, c, tau)[0], CT.chi_at(S, x, c, tau)[0]), flush=True)
        print("=== (e) the sealed run's transition points ===", flush=True)
        for c, taus in SEALED_TRANSITIONS.items():
            for tau in taus:
                print("cusp %d at tau %.7f: " % (c, tau) + "; ".join("(%.4f, %.4f) g/max %+.0e %s |grad_x F|/max %.3f" % (
                    p[0], p[1], v, k, gx) for p, v, k, gx in transition_points(S, x, c, tau)), flush=True)
    print("(%.0fs)" % (time.time() - t0), flush=True)
    print("DONE")
