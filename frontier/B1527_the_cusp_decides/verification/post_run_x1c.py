#!/usr/bin/env python3
"""B1527 post-run check X1c (written after X1b was read; disclosed in FINDINGS).

Why. On -LLLLRLRRRLRR, float64 cannot tell a type-one point from the hyperbolic seed at a = 1e-5. X1b's controls, started 3
degrees off a frame, "converged" on 3 of 12 there. The one new point X1b passed to the 60-digit polish diverged (|F| = 6e210).
The float64 floor on this manifold (the hyperbolic seed's own residual at a = 0, about 1e-7, times 100 for the threshold) is
within a factor of a few of the residual that a = 1e-5 itself creates. X1's four points on this manifold are sound: their
60-digit polish converged (|F| < 1e-48).

What X1c does (its third form; the first two are below). It is X1's method with the decisive steps at 60 digits.
  1. X1's pinned system: the b-free equations (b the 53rd unknown) plus l's translation pinned at angle alpha and length R0.
     At 60 digits it is solved by Gauss-Newton: the SVD pseudo-inverse is cut at 1e-14 of the largest singular value (the
     gauge leaves exact nullity once the point moves, about 1e-17 of the top), with a step-halving line search, and |F| <
     1e-48 accepts. It is always warm-started: never from the hyperbolic seed, which is too far on this manifold (below).
  2. The bracket. At the six frames alpha_1 + 60 k (alpha_1 the mean of X1's frames mod 60), X1's own float64 pinned solve
     is run at alpha_k + d, d = -0.3, -0.2, ..., +0.3 degrees. The float64 solutions that converged are polished at 60 digits
     on the pinned system, and b(alpha) is read there. The nearest pair with opposite signs of b brackets the frame.
  3. The zero of b in the bracket is found by the Illinois method at 60 digits, to |b| < 1e-45. Each evaluation is
     warm-started from the nearer endpoint, rotated to the new alpha (both translations turned by the angle, and the four by
     four holonomy conjugated by the matching rotation of the (e2, e3) plane).
  4. At the zero, the type-one system (b = 0) is polished from that solution (X1's polish_gn), and the frame and beta are
     read from the polished point.
  5. Where X1 had the frame, X1c's frame is compared with X1's: these are the positive controls. Where X1 did not, X1c reads
     what polish_point reads (rho(l)'s eigenvalues; the index rows with the same characters, lambdas and modules, and route W
     on the same rows) and writes the 60-digit point for X2.
A second pass (--fine K ...) reruns the frames alpha_1 + 60 K whose bracket failed. It uses float64 offsets every 0.025
degrees in +-0.5, polishes at 60 digits only the nearest converged pair with opposite signs of b, and merges its result into
the same record ("fine run"). On -LLLLRLRRRLRR the first pass bracketed five frames;
at 300.95 degrees none of its seven float64 solves converged, because float64's convergence on this manifold is erratic (a probe
had converged at 300.95, 301.05 and 301.15 at slightly different angles).
X1's grid gaps away from the frames are not re-measured. Where b is not measured, "exactly six" on this manifold rests on two
things: X1's forty converged frames, which follow the weight-3 law, and the first-order theorem (Proposition Pi, steps 4-5).
Its earlier forms, disclosed:
  - The first solved the type-one system directly from the hyperbolic seed, with the pseudo-inverse cut at 1e-40. It stalled
    after one step at all eighteen seeds, the six frames and the twelve controls 3 degrees off. Far from a solution the
    type-one system's near-null directions (the curve, about 1e-21 of the top singular value 3e8) carry residual components,
    and the steps they produce are huge.
  - The second solved the pinned system from the hyperbolic seed, with the cut at 1e-40, and also read b at X1's sixteen
    gap frames more than 8 degrees from a pole. The gap job at 40 degrees made no progress in 40 steps. A diagnosis there
    found the step dominated by the gauge directions once the point moves (about 1e-17 of the top), and, with those cut,
    the line search still takes about 1/250 of the Newton step: the hyperbolic seed is outside the Newton basin of this
    ill-conditioned system (smallest genuine singular value about 4e-11 of the top). The bracket at the known frame
    240.95 degrees, a positive control, also failed. The run was stopped. Its partial log is in the seat's scratchpad, not
    kept as a result.
Writes x1c_<name>.json and prints one line per job.
Usage: python3 post_run_x1c.py SIGN WORD  (four processes)   or   python3 post_run_x1c.py SIGN WORD --fine K [K ...]"""
import json
import sys
import time
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import mpmath as mp  # noqa: E402
import numpy as np  # noqa: E402

import cusp_lib as L  # noqa: E402
import family_lib as FL  # noqa: E402
import post_run_x1 as X1  # noqa: E402  (a = 1e-5; polish_gn)
import run as R  # noqa: E402

DPS = 60
TOL = 48
B_TOL = 45
CUT = 14                                    # the pseudo-inverse keeps singular values above 10^-CUT of the largest
OFFSETS = [-0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3]
_CACHE = {}


def hyperbolic(sign, word):
    if (sign, word) not in _CACHE:
        _CACHE[(sign, word)] = FL.hyperbolic_sl2(sign, word)
    return _CACHE[(sign, word)]


def seed60(sign, word, theta):
    """the hyperbolic point in the cusp frame rotated by theta, packed as the type-one system's unknowns, at 60 digits
    (scan_lib.hyperbolic_seed's construction without the float64 rounding)"""
    G, img = FL.word_group(sign, word)
    A2, B2, T2, sh = hyperbolic(sign, word)
    mod = FL.paraboloid_module(FL.to_cusp_frame(A2, B2, T2, sign, theta))
    mats = {g: mp.matrix([[mp.re(mod.M[g][i, j]) for j in range(4)] for i in range(4)]) for g in "abt"}
    inv = {g: mp.inverse(mats[g]) for g in "abt"}
    Pl = FL._word(mats, G.cusp[0], inv)
    Pt = FL._word(mats, G.cusp[1], inv)
    XY = [mp.re(Pl[0, 1]), mp.re(Pl[0, 2]), mp.re(Pt[0, 1]), mp.re(Pt[0, 2])]
    U = FL.pack(L.Module(mats), XY)
    return G, img, mp.matrix([mp.re(x) for x in U])


def slice_ab(X, Y, a, b):
    N = mp.matrix(4, 4)
    N[0, 1], N[1, 1], N[1, 3] = X, a * X, X
    N[0, 2], N[2, 2], N[2, 3] = Y, b * Y, Y
    return mp.expm(N) * mp.exp(-(a * X + b * Y) / 4)


def residual_pinned(V, a, G, img, alpha, R0):
    """X1's pinned system at 60 digits: the b-free equations (b = V[52]) and l's translation at angle alpha, length R0"""
    mats, (Xl, Yl, Xt, Yt) = FL.unpack(V)
    b = V[52]
    inv = {g: mp.inverse(mats[g]) for g in mats}
    out = []
    for g in "ab":
        Rm = mats["t"] * mats[g] - FL._word(mats, img[g], inv) * mats["t"]
        out += [Rm[i, j] for i in range(4) for j in range(4)]
    for w, (X, Y) in ((G.cusp[0], (Xl, Yl)), (G.cusp[1], (Xt, Yt))):
        Rm = FL._word(mats, w, inv) - slice_ab(X, Y, a, b)
        out += [Rm[i, j] for i in range(4) for j in range(4)]
    out += [mp.det(mats["a"]) - 1, mp.det(mats["b"]) - 1]
    c, s = mp.cos(alpha), mp.sin(alpha)
    out += [-s * Xl + c * Yl, c * Xl + s * Yl - R0]
    return mp.matrix(out)


def jac_cs(fun, V):
    h = mp.mpf(10) ** (-(mp.mp.dps - 5))
    cols = []
    for k in range(V.rows):
        v = mp.matrix([mp.mpc(x) for x in V])
        v[k] += 1j * h
        cols.append([mp.im(x) / h for x in fun(v)])
    J = mp.matrix(len(cols[0]), V.rows)
    for k in range(V.rows):
        for i in range(len(cols[0])):
            J[i, k] = cols[k][i]
    return J


def gn(fun, V0, maxit=60):
    V = mp.matrix([mp.re(x) for x in V0])
    F = mp.matrix([mp.re(x) for x in fun(V)])
    f = mp.norm(F)
    for it in range(maxit):
        if f < mp.mpf(10) ** -TOL:
            return V, f, it, True
        J = jac_cs(fun, V)
        Ur, Sv, Vr = mp.svd_r(J, full_matrices=False)
        smax = max(Sv[i] for i in range(len(Sv)))
        rhs = Ur.T * F
        step = mp.matrix(V.rows, 1)
        for i in range(len(Sv)):
            if Sv[i] > mp.mpf(10) ** -CUT * smax:
                cf = rhs[i] / Sv[i]
                for k in range(V.rows):
                    step[k] += cf * Vr[i, k]
        t = mp.mpf(1)
        while t > mp.mpf(10) ** -12:
            Vn = V - t * step
            Fn = mp.matrix([mp.re(x) for x in fun(Vn)])
            fn = mp.norm(Fn)
            if fn < f:
                V, F, f = Vn, Fn, fn
                break
            t /= 2
        else:
            return V, f, it + 1, False
    return V, f, maxit, f < mp.mpf(10) ** -TOL


def rotate(V, delta_deg):
    """a pinned solution turned by delta in the cusp frame: both translations rotated, the holonomy conjugated by the matching
    rotation of the (e2, e3) plane (the image of diag(e^{i delta/2}, e^{-i delta/2}) under cusp_lib.hermitian_paraboloid)"""
    d = mp.radians(mp.mpf(delta_deg))
    R4 = L.hermitian_paraboloid(mp.matrix([[mp.expj(d / 2), 0], [0, mp.expj(-d / 2)]]))
    R4i = mp.inverse(R4)
    mats, (Xl, Yl, Xt, Yt) = FL.unpack(V)
    rot = {g: R4 * mats[g] * R4i for g in "abt"}
    zl = mp.expj(d) * mp.mpc(Xl, Yl)
    zt = mp.expj(d) * mp.mpc(Xt, Yt)
    U = FL.pack(L.Module(rot), [mp.re(zl), mp.im(zl), mp.re(zt), mp.im(zt)])
    return mp.matrix([mp.re(x) for x in U] + [V[52]])


class Problem:
    def __init__(self, sign, word):
        self.sign, self.word = sign, word
        mp.mp.dps = DPS
        self.G, self.img, U0 = seed60(sign, word, mp.mpf(0))
        _, (Xl, Yl, _, _) = FL.unpack(U0)
        self.z0 = mp.atan2(Yl, Xl)
        self.R0 = mp.sqrt(Xl ** 2 + Yl ** 2)
        self.a = mp.mpf(X1.A)
        self.P64 = X1.Pinned(sign, word)

    def solve(self, alpha_deg, warm):
        alpha = mp.radians(mp.mpf(alpha_deg))
        return gn(lambda v: residual_pinned(v, self.a, self.G, self.img, alpha, self.R0), warm)

    def float64_then_60(self, alpha_deg):
        """X1's float64 pinned solve at alpha, then the same system at 60 digits warm-started from it"""
        rec = self.P64.solve(np.radians(float(alpha_deg)))
        out = {"alpha": float(alpha_deg), "float64 converged": bool(rec["converged"]), "float64 |F|": rec["|F|"]}
        if not rec["converged"]:
            return out, None
        mp.mp.dps = DPS
        V, f, it, ok = self.solve(alpha_deg, mp.matrix([mp.mpf(float(x)) for x in rec["u"]]))
        out.update({"60-digit |F|": mp.nstr(f, 3), "60-digit iterations": it, "60-digit converged": ok})
        if ok:
            out["b/a"] = mp.nstr(V[52] / self.a, 12)
        return out, (V if ok else None)


def find_zero(P, center):
    """the zero of b near the frame `center` (degrees): a bracket from X1's float64 pinned solutions polished at 60 digits,
    then Illinois at 60 digits with rotated warm starts, to |b| < 10^-B_TOL"""
    log, pts = [], []
    for d in OFFSETS:
        rec, V = P.float64_then_60(center + d)
        log.append(rec)
        if V is not None:
            pts.append((mp.mpf(center + d), V))
    pair = None
    for (x0, V0), (x1, V1) in zip(pts, pts[1:]):
        if mp.sign(V0[52]) != mp.sign(V1[52]):
            if pair is None or abs(x1 - x0) < abs(pair[1][0] - pair[0][0]):
                pair = ((x0, V0), (x1, V1))
    if pair is None:
        return None, log
    (lo, Vlo), (hi, Vhi) = pair
    blo, bhi = Vlo[52], Vhi[52]
    side = 0
    V = None
    for _ in range(60):
        mid = (lo * bhi - hi * blo) / (bhi - blo)
        near_lo = abs(mid - lo) < abs(hi - mid)
        base, base_alpha = (Vlo, lo) if near_lo else (Vhi, hi)
        V, f, it, ok = P.solve(mid, rotate(base, mid - base_alpha))
        log.append({"alpha": mp.nstr(mid, 20), "b/a": mp.nstr(V[52] / P.a, 6), "|F|": mp.nstr(f, 3), "iterations": it,
                    "converged": ok})
        if not ok:
            return None, log
        bm = V[52]
        if abs(bm) < mp.mpf(10) ** -B_TOL:
            return V, log
        if mp.sign(bm) == mp.sign(blo):
            lo, blo, Vlo = mid, bm, V
            if side == -1:
                bhi /= 2
            side = -1
        else:
            hi, bhi, Vhi = mid, bm, V
            if side == 1:
                blo /= 2
            side = 1
        if hi - lo < mp.mpf(10) ** -40:
            return V, log
    return V, log


def find_zero_fine(P, center):
    """the second pass: X1's float64 pinned solve at center + d, d every 0.025 degrees in +-0.5; the nearest pair of converged
    ones with opposite signs of b is polished at 60 digits (only those two), then Illinois as in find_zero"""
    log, pts = [], []
    for i in range(41):
        d = round(-0.5 + 0.025 * i, 3)
        rec = P.P64.solve(np.radians(float(center + d)))
        log.append({"alpha": float(center + d), "float64 converged": bool(rec["converged"]), "float64 |F|": rec["|F|"],
                    "float64 b/a": rec["b"] / X1.A})
        if rec["converged"]:
            pts.append((center + d, rec))
    best = None
    for (x0, r0), (x1, r1) in zip(pts, pts[1:]):
        if np.sign(r0["b"]) != np.sign(r1["b"]) and (best is None or x1 - x0 < best[1][0] - best[0][0]):
            best = ((x0, r0), (x1, r1))
    if best is None:
        return None, log
    ends = []
    for x, r in best:
        mp.mp.dps = DPS
        V, f, it, ok = P.solve(x, mp.matrix([mp.mpf(float(v)) for v in r["u"]]))
        log.append({"alpha": x, "60-digit |F|": mp.nstr(f, 3), "60-digit iterations": it, "60-digit converged": ok,
                    "b/a": mp.nstr(V[52] / P.a, 12) if ok else None})
        if not ok:
            return None, log
        ends.append((mp.mpf(x), V))
    (lo, Vlo), (hi, Vhi) = ends
    if mp.sign(Vlo[52]) == mp.sign(Vhi[52]):
        return None, log
    blo, bhi = Vlo[52], Vhi[52]
    side = 0
    V = None
    for _ in range(60):
        mid = (lo * bhi - hi * blo) / (bhi - blo)
        near_lo = abs(mid - lo) < abs(hi - mid)
        base, base_alpha = (Vlo, lo) if near_lo else (Vhi, hi)
        V, f, it, ok = P.solve(mid, rotate(base, mid - base_alpha))
        log.append({"alpha": mp.nstr(mid, 20), "b/a": mp.nstr(V[52] / P.a, 6), "|F|": mp.nstr(f, 3), "iterations": it,
                    "converged": ok})
        if not ok:
            return None, log
        bm = V[52]
        if abs(bm) < mp.mpf(10) ** -B_TOL:
            return V, log
        if mp.sign(bm) == mp.sign(blo):
            lo, blo, Vlo = mid, bm, V
            if side == -1:
                bhi /= 2
            side = -1
        else:
            hi, bhi, Vhi = mid, bm, V
            if side == 1:
                blo /= 2
            side = 1
        if hi - lo < mp.mpf(10) ** -40:
            return V, log
    return V, log


def job(args):
    sign, word, kind, alpha_deg, x1_frames = args[:5]
    fine_pass = len(args) > 5 and args[5]
    mp.mp.dps = DPS
    t0 = time.time()
    P = Problem(sign, word)
    V, log = (find_zero_fine if fine_pass else find_zero)(P, alpha_deg)
    rec = {"kind": "frame", "predicted": alpha_deg % 360, "search": log}
    if V is None:
        rec.update({"found": False, "seconds": round(time.time() - t0)})
        print(json.dumps({k: v for k, v in rec.items() if k != "search"}), flush=True)
        return rec
    U = mp.matrix([V[i] for i in range(52)])
    Up, fp, itp, _ = X1.polish_gn(U, P.a, P.G, P.img, tol=mp.mpf(10) ** -TOL, maxit=40)
    mats, (Xl, Yl, Xt, Yt) = FL.unpack(Up)
    alpha = float(mp.degrees(mp.atan2(Yl, Xl)) % 360)
    zl = complex(float(Xl), float(Yl))
    orient = 1 if np.sign((complex(float(Xt), float(Yt)) / zl).imag) == np.sign(complex(hyperbolic(sign, word)[3]).imag) else -1
    rec.update({"found": True, "b at the zero": mp.nstr(V[52], 3), "type-one polished |F|": mp.nstr(fp, 3),
                "alpha": alpha, "beta": float(np.degrees(orient * np.angle(1j / zl)) % 180.0)})
    near = [x for x in x1_frames if R.circ_dist(alpha, x) < 0.01]
    rec["X1's frame"] = near[0] if near else None
    rec["|alpha - X1's frame| (deg)"] = R.circ_dist(alpha, near[0]) if near else None
    mod = L.Module(mats)
    ev = FL.eig_sorted(mod.word("abAB"))
    rec["rho(l) eigenvalues"] = [mp.nstr(e, 12) for e in ev]
    rec["min |eigenvalue - 1|"] = mp.nstr(min(abs(e - 1) for e in ev), 4)
    rec["psi(l) = a X_l"] = mp.nstr(P.a * Xl, 8)
    if not near and fp < mp.mpf(10) ** -TOL:
        chars, _ = R.characters(P.img)
        chosen = [chars[0]] + [c for c in chars[1:]][:4]
        rows = []
        for u_ in chosen:
            for lam in R.P_LAMBDAS:
                nu = R.nu_of(u_, lam)
                for wedge in (False, True):
                    m = R.twisted(mats, nu, wedge)
                    with_w = (u_ == chars[0]) and (lam == 1 or lam == mp.mpf("1.7"))
                    rows.append({"u": [str(u_[0]), str(u_[1])], "lambda": mp.nstr(lam, 6), "module": "L2" if wedge else "4",
                                 **R.index_both(P.G, P.img, m, with_w)})
        rec["index rows"] = rows
        rec["point (60 digits)"] = [mp.nstr(x, 70) for x in Up]
    rec["seconds"] = round(time.time() - t0)
    print(json.dumps({k: v for k, v in rec.items() if k not in ("search", "index rows", "point (60 digits)")}), flush=True)
    return rec


def fine(sign, word, ks):
    """the second pass: the frames alpha_1 + 60 k (k in ks) with float64 offsets every 0.025 degrees in +-0.5, merged into the
    first pass's record"""
    name = R.name_of(sign, word)
    path = HERE / ("x1c_" + name + ".json")
    out = json.loads(path.read_text(encoding="utf-8"))
    x1 = json.loads((HERE / ("x1_" + name + ".json")).read_text(encoding="utf-8"))
    recs = [job((sign, word, "frame", out["alpha_1"] + 60 * k, x1["type-one frames"], True)) for k in ks]
    out["fine run"] = {"frames": [out["alpha_1"] + 60 * k for k in ks], "offsets": "every 0.025 degrees in +-0.5", "records": recs}
    out["new points"] += [r for r in recs if "index rows" in r]
    out["frames found"] = (sum(1 for r in out["frames"] if r["found"])
                           + sum(1 for r in recs if r["found"]
                                 and not any(f["found"] and R.circ_dist(f["alpha"], r["alpha"]) < 0.01 for f in out["frames"])))
    path.write_text(json.dumps(out, indent=1, default=str))
    print(f"{sign}{word}: after the fine pass, frames found {out['frames found']}/6; new {len(out['new points'])}", flush=True)


def main():
    sign, word = sys.argv[1], sys.argv[2]
    if len(sys.argv) > 3 and sys.argv[3] == "--fine":
        fine(sign, word, [int(k) for k in sys.argv[4:]])
        return
    name = R.name_of(sign, word)
    x1 = json.loads((HERE / ("x1_" + name + ".json")).read_text(encoding="utf-8"))
    frames = x1["type-one frames"]
    a1 = float(np.mean([((f - frames[0] + 30) % 60) - 30 for f in frames]) + frames[0]) % 60
    jobs = [(sign, word, "frame", a1 + 60 * k, frames) for k in range(6)]
    from multiprocessing import Pool
    with Pool(4) as pool:
        fr = pool.map(job, jobs)
    out = {"manifold": sign + word, "a": X1.A, "dps": DPS, "alpha_1": a1, "frames": fr,
           "frames found": sum(1 for r in fr if r["found"]),
           "agree with X1": sum(1 for r in fr if r.get("X1's frame") is not None),
           "new points": [r for r in fr if "index rows" in r]}
    (HERE / ("x1c_" + name + ".json")).write_text(json.dumps(out, indent=1, default=str))
    print(f"{sign}{word}: frames found {out['frames found']}/6 (agreeing with X1: {out['agree with X1']}); new "
          f"{len(out['new points'])}", flush=True)


if __name__ == "__main__":
    main()
