#!/usr/bin/env python3
"""B1527 -- THE CUSP DECIDES: the sealed run.  Written and committed with PREREGISTRATION.md before it was run on any word state
other than m004's banked Ballas axis (controls.py).

Ten manifolds (PREREGISTRATION section 5): +-LR (m004 and its sister), +-LLRLRR (swaprev-only), +-LLLRLRR (chiral),
+-LLLLRLLLRR and +-LLLLRLRRRLRR (the golden mirror-broken pair, traces 47 and 123).

Per manifold (python3 run.py SIGN WORD; or --all, four at a time):
  H  Part H at the hyperbolic point (theta = 0 frame): every torsion character nu|F of Gamma, with nu(t) = lambda over
     {lambda_c, 1, 1.7, e^{0.9 i}, -1} (lambda_c makes nu trivial on t', so on the cusp); the modules nu (x) rho and
     nu (x) Lambda^2 rho; route Fox (cusp_lib) on all, route W (wang_lib) at lambda_c and 1.7.
  S1 the type-one scan: 72 seeds (the hyperbolic point in the cusp frame rotated by 0, 5, ..., 355 degrees), Ballas' slice with
     b = 0 at a = 0.002, then a = 0.001 from each converged solution.
  S2 the b-free scan: the same 72 seeds, b free, a = 0.002.
  P  per cluster of type-one solutions (by the frame angle of l, 1 degree): the representative polished at 60 digits
     (family_lib); the eigenvalues of rho(l); the lattice slope nearest the unipotent line and its X-translation; the Jacobian
     nullities of both systems; the index (route Fox) for five characters (the trivial one and up to four others, the first
     in sorted order) x lambda in {1, 1.7, e^{0.9 i}} x both modules; route W for the trivial character at lambda = 1 and 1.7.
Writes run_<name>.json; read_out.py reads P1-P8 from them."""
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
import scan_lib as S  # noqa: E402
import wang_lib as WL  # noqa: E402

MANIFOLDS = [("+", "LR"), ("-", "LR"), ("+", "LLRLRR"), ("-", "LLRLRR"), ("+", "LLLRLRR"), ("-", "LLLRLRR"),
             ("+", "LLLLRLLLRR"), ("-", "LLLLRLLLRR"), ("+", "LLLLRLRRRLRR"), ("-", "LLLLRLRRRLRR")]
THETAS_DEG = [5 * k for k in range(72)]
A_SCAN, A_EXTRA = 0.002, 0.001
CONVERGED_FLOOR, CONVERGED_FACTOR = 1e-11, 100.0   # converged: |F| < max(1e-11, 100 x the seed's own float64 residual at a = 0)
CLUSTER_DEG = 1.0
EXTRA_LAMBDAS = [mp.mpf(1), mp.mpf("1.7"), mp.expj(mp.mpf("0.9")), mp.mpf(-1)]
P_LAMBDAS = [mp.mpf(1), mp.mpf("1.7"), mp.expj(mp.mpf("0.9"))]


def name_of(sign, word):
    return ("p" if sign == "+" else "m") + word


def characters(img):
    chars, D = FL.torsion_characters(img)
    return chars, D


def nu_of(u, lam):
    return {"a": mp.expjpi(2 * mp.mpf(u[0].numerator) / u[0].denominator),
            "b": mp.expjpi(2 * mp.mpf(u[1].numerator) / u[1].denominator), "t": lam}


def lambda_c(sign, u):
    nu = nu_of(u, 1)
    return mp.mpf(1) if sign == "+" else 1 / (nu["a"] * nu["b"])


def twisted(mats, nu, wedge=False):
    return {g: nu[g] * (L.wedge2(mats[g]) if wedge else mats[g]) for g in "abt"}


def index_both(G, img, mats, with_w):
    fox = L.class_index(G, L.Module(mats))
    rec = {"I": fox["I"], "V": fox["V"], "V*": fox["V*"], "checks": fox["checks"], "margins": fox["margins"],
           "relator residual": fox["relator residual"]}
    if with_w:
        w = WL.index_wang(img, G.cusp, mats)
        rec["W"] = {k: w[k] for k in ("I", "h1(V)", "h1(V*)", "a0", "b0", "t0", "s0", "margins")}
    return rec


# ================================================================================================ H: the hyperbolic point
def part_h(sign, word):
    mp.mp.dps = 60
    G, img = FL.word_group(sign, word)
    A2, B2, T2, sh = FL.hyperbolic_sl2(sign, word)
    M2 = FL.to_cusp_frame(A2, B2, T2, sign, 0)
    rho = FL.paraboloid_module(M2)
    mats = {g: rho.M[g] for g in "abt"}
    chars, D = characters(img)
    rows = []
    for u in chars:
        lc = lambda_c(sign, u)
        lams = [("lambda_c", lc)] + [(mp.nstr(x, 6), x) for x in EXTRA_LAMBDAS if abs(x - lc) > mp.mpf(10) ** -30]
        for lname, lam in lams:
            nu = nu_of(u, lam)
            for wedge in (False, True):
                m = twisted(mats, nu, wedge)
                with_w = lname == "lambda_c" or lname == "1.7"
                rec = index_both(G, img, m, with_w)
                rows.append({"u": [str(u[0]), str(u[1])], "lambda": lname, "module": "L2" if wedge else "4", **rec})
    return {"D": D, "snappy shape": [sh.real, sh.imag], "rho relator residual": mp.nstr(L.relator_residual(G, rho), 3),
            "rows": rows}


# ================================================================================================ S1, S2: the scans
def scans(sign, word):
    cache = {}
    t1, t2 = [], []
    for deg in THETAS_DEG:
        th = np.radians(deg)
        G, img, W, u0, orient = S.hyperbolic_seed(sign, word, th, cache)
        r0 = S.frame_reading(u0, False)
        alpha_seed = float(np.degrees(np.angle(r0["zl"])) % 360)
        floor = float(np.linalg.norm(S.residual(u0, 0.0, W, False).real))
        thresh = max(CONVERGED_FLOOR, CONVERGED_FACTOR * floor)
        # S1: type one
        u, f, it = S.solve(u0, A_SCAN, W, False, tol=0.3 * thresh)
        rec = {"theta": deg, "alpha seed": alpha_seed, "|F|": float(f), "iterations": it, "floor": floor, "threshold": thresh,
               "converged": bool(f < thresh)}
        if f < thresh:
            r = S.frame_reading(u, False)
            rec.update({"alpha": float(np.degrees(np.angle(r["zl"])) % 360), "zl": [r["zl"].real, r["zl"].imag],
                        "zt": [r["zt"].real, r["zt"].imag], "orient": orient,
                        "beta": S.line_angle_from_l(1j, r["zl"], orient), "u": [float(x) for x in u]})
            u2, f2, it2 = S.solve(u, A_EXTRA, W, False, tol=0.3 * thresh)
            rec["a=0.001"] = {"|F|": float(f2), "converged": bool(f2 < thresh)}
            if f2 < thresh:
                r2 = S.frame_reading(u2, False)
                rec["a=0.001"].update({"alpha": float(np.degrees(np.angle(r2["zl"])) % 360),
                                       "beta": S.line_angle_from_l(1j, r2["zl"], orient)})
        t1.append(rec)
        # S2: b free
        ub, fb, itb = S.solve(np.concatenate([u0, [0.0]]), A_SCAN, W, True, tol=0.3 * thresh)
        recb = {"theta": deg, "alpha seed": alpha_seed, "|F|": float(fb), "iterations": itb, "threshold": thresh,
                "converged": bool(fb < thresh)}
        if fb < thresh:
            r = S.frame_reading(ub, True)
            recb.update({"alpha": float(np.degrees(np.angle(r["zl"])) % 360), "b": r["b"],
                         "psi_a(l)": A_SCAN * r["zl"].real, "psi_b(l)": r["b"] * r["zl"].imag,
                         "zl": [r["zl"].real, r["zl"].imag]})
        t2.append(recb)
    return {"type one": t1, "b free": t2}


def circ_dist(x, y, period=360.0):
    d = abs(x - y) % period
    return min(d, period - d)


def clusters(t1):
    pts = [r for r in t1 if r["converged"]]
    out = []
    for r in sorted(pts, key=lambda r: r["alpha"]):
        for c in out:
            if circ_dist(c["alpha"], r["alpha"]) < CLUSTER_DEG:
                c["members"].append(r)
                break
        else:
            out.append({"alpha": r["alpha"], "members": [r]})
    for c in out:
        al = [m["alpha"] for m in c["members"]]
        ref = al[0]
        c["alpha"] = float((ref + np.mean([((x - ref + 180) % 360) - 180 for x in al])) % 360)
        c["rep"] = min(c["members"], key=lambda m: circ_dist(m["alpha"], c["alpha"]))
    return out


# ================================================================================================ P: the polished points
def nearest_lattice_slope(Xl, Yl, Xt, Yt, beta_dir):
    """the primitive slope p l + q t' (|p|, |q| <= 6) whose direction is nearest the unipotent line (the slice's Y axis)"""
    from math import gcd
    best = None
    for p in range(-6, 7):
        for q in range(0, 7):
            if (p, q) == (0, 0) or gcd(abs(p), q) != 1 or (q == 0 and p < 0):
                continue
            X, Y = p * Xl + q * Xt, p * Yl + q * Yt
            ang = abs(float(mp.atan2(abs(X), abs(Y))))           # angle from the Y axis
            if best is None or ang < best[0]:
                best = (ang, p, q, X)
    return {"slope (p, q)": [best[1], best[2]], "angle from the unipotent line (deg)": float(np.degrees(best[0])),
            "X-translation": mp.nstr(best[3], 3)}


def polish_point(sign, word, rep, chars):
    mp.mp.dps = 60
    G, img = FL.word_group(sign, word)
    W = S.Words(G, img)
    u = np.array(rep["u"])
    U = mp.matrix([mp.mpf(x) for x in u])
    t0 = time.time()
    Up, fp, itp, _ = FL.solve_type_one(U, mp.mpf(A_SCAN), G, img, tol=mp.mpf(10) ** -48, maxit=40)
    mats, XY = FL.unpack(Up)
    mod = L.Module(mats)
    Xl, Yl, Xt, Yt = XY
    ev = FL.eig_sorted(mod.word("abAB"))
    psi_l = mp.mpf(A_SCAN) * Xl
    out = {"alpha": rep["alpha"], "beta": rep["beta"], "polished |F|": mp.nstr(fp, 3), "polish iterations": itp,
           "polish seconds": round(time.time() - t0), "X_l": mp.nstr(Xl, 12), "Y_l": mp.nstr(Yl, 12), "X_t": mp.nstr(Xt, 12),
           "Y_t": mp.nstr(Yt, 12), "psi(l) = a X_l": mp.nstr(psi_l, 8),
           "rho(l) eigenvalues": [mp.nstr(e, 12) for e in ev],
           "min |eigenvalue - 1|": mp.nstr(min(abs(e - 1) for e in ev), 3),
           "unipotent line's nearest lattice slope": nearest_lattice_slope(Xl, Yl, Xt, Yt, None)}
    # Jacobian nullities (float64, at the scan's solution)
    J1 = S.jacobian(u, A_SCAN, W, False)
    s1 = np.linalg.svd(J1, compute_uv=False)
    ub, fb, _ = S.solve(np.concatenate([u, [0.0]]), A_SCAN, W, True, tol=0.3 * rep["threshold"])
    J2 = S.jacobian(ub, A_SCAN, W, True)
    s2 = np.linalg.svd(J2, compute_uv=False)

    def nul(s):
        """the nullity read at the largest ratio between consecutive singular values among the eight smallest"""
        tail = s[-8:]
        ratios = tail[:-1] / np.maximum(tail[1:], 1e-300)
        k = int(np.argmax(ratios))
        nullity = len(tail) - 1 - k
        return {"nullity": nullity, "gap ratio": float(ratios[k]), "largest null / top": float(tail[k + 1] / s[0]),
                "smallest kept / top": float(tail[k] / s[0]), "eight smallest / top": [float(x / s[0]) for x in tail]}
    out["nullity, type one"] = nul(s1)
    out["nullity, b free"] = nul(s2)
    out["b-free landing |F|"] = float(fb)
    # the index
    chosen = [chars[0]] + [c for c in chars[1:]][:4]
    rows = []
    for u_ in chosen:
        for lam in P_LAMBDAS:
            nu = nu_of(u_, lam)
            for wedge in (False, True):
                m = twisted(mats, nu, wedge)
                with_w = (u_ == chars[0]) and (lam == 1 or lam == mp.mpf("1.7"))
                rec = index_both(G, img, m, with_w)
                rows.append({"u": [str(u_[0]), str(u_[1])], "lambda": mp.nstr(lam, 6), "module": "L2" if wedge else "4", **rec})
    out["index rows"] = rows
    return out


def run_one(sign, word):
    name = name_of(sign, word)
    t0 = time.time()
    rec = {"manifold": sign + word}
    rec["H"] = part_h(sign, word)
    rec["seconds H"] = round(time.time() - t0)
    t1 = time.time()
    rec["scans"] = scans(sign, word)
    rec["seconds scans"] = round(time.time() - t1)
    cl = clusters(rec["scans"]["type one"])
    G, img = FL.word_group(sign, word)
    chars, _ = characters(img)
    t2 = time.time()
    rec["clusters"] = []
    for c in cl:
        entry = {"alpha": c["alpha"], "size": len(c["members"]),
                 "beta (a=0.002)": float(np.mean([m["beta"] for m in c["members"]])),
                 "beta (a=0.001)": [m["a=0.001"].get("beta") for m in c["members"] if m["a=0.001"]["converged"]][:1],
                 "point": polish_point(sign, word, c["rep"], chars)}
        rec["clusters"].append(entry)
    rec["seconds polish"] = round(time.time() - t2)
    rec["seconds"] = round(time.time() - t0)
    (HERE / ("run_" + name + ".json")).write_text(json.dumps(rec, indent=1, default=str))
    print(f"{sign}{word}: done in {rec['seconds']} s; clusters {len(cl)}", flush=True)
    return name


def main():
    args = sys.argv[1:]
    if args == ["--all"]:
        from multiprocessing import Pool
        with Pool(4) as pool:
            pool.starmap(run_one, MANIFOLDS)
    else:
        for sign, word in zip(args[0::2], args[1::2]):
            run_one(sign, word)


if __name__ == "__main__":
    main()
