#!/usr/bin/env python3
"""B1527 post-run check X1 (written after the seal, while the sealed run was still running; disclosed in FINDINGS).

Why. The sealed type-one scan (run.py S1) seeds Levenberg-Marquardt from the hyperbolic point in 72 frames 5 degrees apart, with
an 80-iteration budget. At fixed a the type-one frame is pinned only at order a (the soft singular value of the type-one
system), so a seed more than about 0.2 degrees off a type-one frame does not reach it within the budget (found by probing m004 at
offsets from Ballas' axis, after the seal: 0.33 degrees needs 125 iterations, 1 degree 303, 2.5 degrees more than 400). The sealed
scan therefore finds a type-one family only when a grid seed falls within about 0.2 degrees of it.

What X1 does instead. It pins the frame explicitly and reads b as a function of it:
  1. the b-free system plus two equations, Im(e^{-i alpha0} z_l) = 0 and Re(e^{-i alpha0} z_l) = R0 (z_l = X_l + i Y_l): l at
     angle alpha0 with length R0 = |z_l| of the hyperbolic point. At fixed a this cuts the generalized-cusp surface to points
     (the gauge aside). Solved by Gauss-Newton (least squares, SVD cut 1e-13, step halving), seeded from the hyperbolic point in
     the frame alpha0;
  2. b(alpha0) on alpha0 = 0, 5, ..., 355 degrees, at a = 1e-5. (A first form used the sealed a = 0.002; it worked on m004,
     but on the long words the pinned Jacobian's condition number is about 1e9 (top singular value 3e7 on -LLLLRLLLRR), and
     float64 Gauss-Newton converged from the hyperbolic seed only for a <= 3e-5. At a = 1e-5 the deformation is still genuine,
     psi(l) ~ 1e-5, far above the 60-digit polish's noise);
  3. each zero of b (a sign change between neighbours with |b/a| < 10, not a pole) refined by bisection to a bracket of
     1e-10 rad (float64's noise on b is about |b/a| = 1e-6 on the long words), accepted at |b/a| < 1e-4 (b/a varies by O(1)
     across 5 degrees; a pole would leave |b/a| large);
  4. at each zero, the type-one system (b = 0) solved from that point, then passed to the sealed run's own polish_point
     (60 digits; eigenvalues of rho(l), the nearest lattice slope, the Jacobian nullities, the index rows in both routes),
     with its polisher replaced by polish_gn (Gauss-Newton with an SVD pseudo-inverse): the sealed Levenberg-Marquardt
     polisher stalled near |F| = 1e-11 on the long words, while Gauss-Newton converges quadratically (to 1e-54 in five steps
     on -LLLLRLLLRR).
It reads the sealed predictions' criteria on these points (the frames, the coset, Part A, the nullities), the weight-3 law
b/a = -tan(3 (alpha0 - alpha_1)) on the converged frames, and the sign changes of psi_a + psi_b, 3 psi_a - psi_b and
3 psi_b - psi_a at l (the eigenvalue-one crossings).
Usage: python3 post_run_x1.py --all  (four at a time; writes x1_<name>.json and x1.json)  or  python3 post_run_x1.py SIGN WORD"""
import json
import sys
import time
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import numpy as np  # noqa: E402

import family_lib as FL  # noqa: E402
import run as R  # noqa: E402
import scan_lib as S  # noqa: E402

A = 1e-5            # X1's slice scale (see the docstring: the long words' conditioning); the sealed scan used 0.002
R.A_SCAN = A        # so that the sealed polish_point polishes and reads at X1's a
GRID_DEG = [5 * k for k in range(72)]


def residual_pinned(u, W, alpha0, R0):
    F = S.residual(u, A, W, True)
    Xl, Yl = u[48], u[49]
    c, s = np.cos(alpha0), np.sin(alpha0)
    return np.concatenate([F, [-s * Xl + c * Yl, c * Xl + s * Yl - R0]])


def jacobian_pinned(u, W, alpha0, R0):
    cols = []
    for k in range(len(u)):
        v = np.array(u, dtype=complex)
        v[k] += 1j * S.H_STEP
        cols.append(residual_pinned(v, W, alpha0, R0).imag / S.H_STEP)
    return np.array(cols).T


def gauss_newton(fun, jac, u0, tol, maxit=60):
    u = np.array(np.real(u0), dtype=float)
    F = fun(u).real
    f = np.linalg.norm(F)
    for it in range(maxit):
        if f < tol:
            return u, f, it
        d = np.linalg.lstsq(jac(u), -F, rcond=1e-13)[0]
        step = 1.0
        while step > 1e-8:
            un = u + step * d
            Fn = fun(un).real
            fn = np.linalg.norm(Fn)
            if np.isfinite(fn) and fn < f:
                u, F, f = un, Fn, fn
                break
            step /= 2
        else:
            return u, f, it
    return u, f, maxit


def polish_gn(u0, a, G, img, tol=None, maxit=40, lam0=None):
    """X1's 60-digit polish: Gauss-Newton with the SVD pseudo-inverse (singular values below 1e-40 of the largest cut: the
    gauge). It replaces family_lib.solve_type_one (Levenberg-Marquardt), which stalled near 1e-11 on the long words; same
    signature and return, so the sealed polish_point reads the polished point unchanged."""
    import mpmath as mp
    tol = tol or mp.mpf(10) ** (-(mp.mp.dps - 12))
    U = mp.matrix([mp.re(x) for x in u0])
    hist = []
    for it in range(maxit):
        F = FL.residual(U, a, G, img)
        f = mp.norm(F)
        hist.append(f)
        if f < tol:
            return U, f, it, hist
        J = FL.jacobian(U, a, G, img)
        Ur, Sv, Vr = mp.svd_r(J, full_matrices=False)
        smax = max(Sv[i] for i in range(len(Sv)))
        rhs = Ur.T * mp.matrix([mp.re(x) for x in F])
        step = mp.matrix(U.rows, 1)
        for i in range(len(Sv)):
            if Sv[i] > mp.mpf(10) ** -40 * smax:
                c = rhs[i] / Sv[i]
                for k in range(U.rows):
                    step[k] += c * Vr[i, k]
        U = U - step
    F = FL.residual(U, a, G, img)
    return U, mp.norm(F), maxit, hist


R.FL.solve_type_one = polish_gn      # the sealed polish_point now polishes by Gauss-Newton (disclosed in FINDINGS)


class Pinned:
    def __init__(self, sign, word):
        self.sign, self.word, self.cache = sign, word, {}
        G, img, W, u0, orient = S.hyperbolic_seed(sign, word, 0.0, self.cache)
        self.z0 = S.frame_reading(u0, False)["zl"]
        self.R0 = abs(self.z0)
        self.orient = orient

    def solve(self, alpha0):
        th = alpha0 - np.angle(self.z0)
        G, img, W, u0, orient = S.hyperbolic_seed(self.sign, self.word, th, self.cache)
        floor = float(np.linalg.norm(S.residual(u0, 0.0, W, False).real))
        thresh = max(R.CONVERGED_FLOOR, R.CONVERGED_FACTOR * floor)
        u, f, it = gauss_newton(lambda v: residual_pinned(v, W, alpha0, self.R0),
                                lambda v: jacobian_pinned(v, W, alpha0, self.R0),
                                np.concatenate([u0, [0.0]]), 0.3 * thresh)
        r = S.frame_reading(u, True)
        return {"alpha0": float(np.degrees(alpha0)), "converged": bool(f < thresh), "|F|": float(f), "iterations": it,
                "b": r["b"], "zl": [r["zl"].real, r["zl"].imag], "threshold": thresh,
                "psi_a(l)": A * r["zl"].real, "psi_b(l)": r["b"] * r["zl"].imag, "u": u, "W": W}


def bisect(P, lo, hi, blo, bhi, steps=60):
    """a zero of b between frames lo and hi (radians) where b changes sign"""
    rec = None
    for _ in range(steps):
        mid = 0.5 * (lo + hi)
        rec = P.solve(mid)
        if not rec["converged"]:
            return None
        if abs(rec["b"]) < 1e-8 * A:
            return rec
        if np.sign(rec["b"]) == np.sign(blo):
            lo, blo = mid, rec["b"]
        else:
            hi, bhi = mid, rec["b"]
        if hi - lo < 1e-10:          # the zero located to float64's noise on b (|b/a| about 1e-6 on the long words)
            return rec
    return rec


def run_one(sign, word):
    t0 = time.time()
    P = Pinned(sign, word)
    grid = [P.solve(np.radians(d)) for d in GRID_DEG]
    out = {"manifold": sign + word, "a": A, "R0": P.R0, "orient": P.orient,
           "grid": [{k: v for k, v in g.items() if k not in ("u", "W")} for g in grid]}
    conv = [g for g in grid if g["converged"]]
    # the weight-3 law: b/a = -tan(3 (alpha0 - alpha1)) with alpha1 fitted
    zeros, poles = [], []
    for i in range(len(grid)):
        g, h = grid[i], grid[(i + 1) % len(grid)]
        if not (g["converged"] and h["converged"]):
            continue
        if np.sign(g["b"]) != np.sign(h["b"]):
            (zeros if abs(g["b"]) < 10 * A and abs(h["b"]) < 10 * A else poles).append((g, h))
    roots = []
    for g, h in zeros:
        lo = np.radians(g["alpha0"])
        hi = np.radians(h["alpha0"]) if h["alpha0"] > g["alpha0"] else np.radians(h["alpha0"] + 360)
        rec = bisect(P, lo, hi, g["b"], h["b"])
        if rec is not None and rec["converged"] and abs(rec["b"]) < 1e-4 * A:   # a zero of b, not a pole
            roots.append(rec)
    out["zeros bracketed"] = len(zeros)
    out["sign changes through a pole"] = len(poles)
    out["type-one frames"] = [float(r["alpha0"] % 360) for r in roots]
    if roots:
        a1 = np.radians(roots[0]["alpha0"])
        dev = [abs(g["b"] / A + np.tan(3 * (np.radians(g["alpha0"]) - a1))) for g in conv
               if abs(np.cos(3 * (np.radians(g["alpha0"]) - a1))) > 0.3]
        out["weight-3 law: max |b/a + tan(3 (alpha0 - alpha_1))| (|cos| > 0.3)"] = float(max(dev)) if dev else None
    # eigenvalue-one crossings on the converged grid (adjacent, both |b| < 50 a)
    cross = []
    for i in range(len(grid)):
        g, h = grid[i], grid[(i + 1) % len(grid)]
        if not (g["converged"] and h["converged"]) or abs(g["b"]) > 50 * A or abs(h["b"]) > 50 * A:
            continue
        for name, f in (("psi_a + psi_b", lambda x: x["psi_a(l)"] + x["psi_b(l)"]),
                        ("3 psi_a - psi_b", lambda x: 3 * x["psi_a(l)"] - x["psi_b(l)"]),
                        ("3 psi_b - psi_a", lambda x: 3 * x["psi_b(l)"] - x["psi_a(l)"])):
            if np.sign(f(g)) != np.sign(f(h)):
                cross.append({"between": [g["alpha0"], h["alpha0"]], "g": name})
    out["eigenvalue-one crossings"] = cross
    # the type-one points: the b = 0 system from each root, then the sealed polish
    G, img = FL.word_group(sign, word)
    chars, _ = R.characters(img)
    pts = []
    for r in roots:
        u1, f1, it1 = gauss_newton(lambda v: S.residual(v, A, r["W"], False).real,
                                   lambda v: S.jacobian(v, A, r["W"], False), r["u"][:52], 0.3 * r["threshold"])
        rr = S.frame_reading(u1, False)
        alpha = float(np.degrees(np.angle(rr["zl"])) % 360)
        beta = S.line_angle_from_l(1j, rr["zl"], P.orient)
        entry = {"frame alpha0": r["alpha0"] % 360, "type-one |F|": float(f1), "alpha": alpha, "beta": beta,
                 "converged": bool(f1 < r["threshold"])}
        if f1 < r["threshold"]:
            rep = {"u": [float(x) for x in u1], "alpha": alpha, "beta": beta, "threshold": r["threshold"]}
            entry["point"] = R.polish_point(sign, word, rep, chars)
        pts.append(entry)
    out["points"] = pts
    out["seconds"] = round(time.time() - t0)
    (HERE / ("x1_" + R.name_of(sign, word) + ".json")).write_text(json.dumps(out, indent=1, default=str))
    print(f"{sign}{word}: {out['seconds']} s; converged {len(conv)}/72; type-one frames {len(roots)}; "
          f"poles {len(poles)}", flush=True)
    return R.name_of(sign, word)


def main():
    args = sys.argv[1:]
    if args == ["--all"]:
        from multiprocessing import Pool
        with Pool(4) as pool:
            pool.starmap(run_one, R.MANIFOLDS)
    else:
        for sign, word in zip(args[0::2], args[1::2]):
            run_one(sign, word)


if __name__ == "__main__":
    main()
