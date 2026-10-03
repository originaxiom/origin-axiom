#!/usr/bin/env python3
"""B1527 post-run check X2 (written after X1's first four manifolds were read; disclosed in FINDINGS).

Why. X1 reads its type-one points at a = 1e-5 with the sealed polish_point at 60 digits, polished to |F| < 1e-48. On every
index row there I = 0 and every identity holds, but on X1's first four manifolds 18 of 576 rows miss the sealed margin bar
(largest dropped singular value < 1e-40): the largest dropped reaches 4e-39. The rank decisions themselves are clear (the
smallest kept singular value is at least 5e-17), but the bar was sealed and a reading below it is not claimed. The likely
reason is the conditioning near rho_hyp. At a = 1e-5 the type-one Jacobian's smallest kept singular value is about 1e-8 of
its largest, so a residual of 1e-49 leaves the point about 1e-41 (relative) from the representation variety, and the
cohomology's kernels amplify that. If so, the dropped singular values fall with the working precision, while the kept ones
(set by psi(l), about 1e-5) stay.

What X2 does. For every manifold and every type-one point X1 polished (and X1c's new ones):
  1. it rebuilds X1's float64 point from the banked frame as X1 did, with X1's own functions: the pinned solve, then the
     type-one system at a = 1e-5. An X1c point starts from X1c's banked 60-digit solution;
  2. it polishes at mp.dps = 100 to |F| < 1e-88 (post_run_x1.polish_gn, unchanged);
  3. at 100 digits it recomputes every index row the 60-digit reading computed there, with the same characters, lambdas
     and modules and route W on the same rows; cusp_lib's and wang_lib's own thresholds are used (1e-30 relative);
  4. it compares with the 60-digit rows. I, every dimension (a0, h1, t0, r1, n, h1(Delta)) of V and V*, and route W's
     readings must agree row by row. It also reads the margins against the sealed bar, and the eigenvalues of rho(l);
  5. it reads the Jacobian nullities at 100 digits, of the type-one system (family_lib's) and of the b-free system (the
     same equations with b an unknown, written here with Ballas' slice at b != 0). X1 read them in float64 at a = 1e-5,
     where the frame's soft singular value (about 1e-8 of the top; it scales with a) is not separable from float64's
     floor on the longer words (about 1e-12 there), so X1's reading does not test P7. At 100 digits the null singular
     values sit near 1e-90 and the soft one stays near 1e-8.
Writes x2_<name>.json and x2.json; prints one line per manifold.
Usage: python3 post_run_x2.py --all | --some SIGN WORD ... (four at a time) | SIGN WORD | --totals (x2.json from the files)"""
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
import post_run_x1 as X1  # noqa: E402  (sets run.A_SCAN = 1e-5; its polish_gn is used unchanged)
import run as R  # noqa: E402
import scan_lib as S  # noqa: E402

DPS = 100
TOL = 88          # polish to |F| < 10^-TOL
DIMS = ("a0", "h1", "t0", "r1", "n", "h1(Delta)")
WKEYS = ("I", "h1(V)", "h1(V*)", "a0", "b0", "t0", "s0")


def flt(x):
    return float(str(x).replace(" ", ""))


def slice_ab(X, Y, a, b):
    """Ballas' slice at any (a, b), SL-normalised: |det|^(-1/4) exp(X N_a + Y N_b) (family_lib.slice_matrix is b = 0)"""
    N = mp.matrix(4, 4)
    N[0, 1], N[1, 1], N[1, 3] = X, a * X, X
    N[0, 2], N[2, 2], N[2, 3] = Y, b * Y, Y
    return mp.expm(N) * mp.exp(-(a * X + b * Y) / 4)


def residual_b_free(U, a, G, img):
    """family_lib.residual with b as the 53rd unknown"""
    mats, (Xl, Yl, Xt, Yt) = FL.unpack(U)
    b = U[52]
    inv = {g: mp.inverse(mats[g]) for g in mats}
    out = []
    for g in "ab":
        Rm = mats["t"] * mats[g] - FL._word(mats, img[g], inv) * mats["t"]
        out += [Rm[i, j] for i in range(4) for j in range(4)]
    for w, (X, Y) in ((G.cusp[0], (Xl, Yl)), (G.cusp[1], (Xt, Yt))):
        Rm = FL._word(mats, w, inv) - slice_ab(X, Y, a, b)
        out += [Rm[i, j] for i in range(4) for j in range(4)]
    out += [mp.det(mats["a"]) - 1, mp.det(mats["b"]) - 1]
    return mp.matrix(out)


def jacobian_cs(fun, U):
    """complex-step Jacobian at the ambient precision (every map is analytic in the real unknowns)"""
    h = mp.mpf(10) ** (-(mp.mp.dps - 5))
    cols = []
    for k in range(U.rows):
        v = mp.matrix([mp.mpc(x) for x in U])
        v[k] += 1j * h
        cols.append([mp.im(x) / h for x in fun(v)])
    J = mp.matrix(len(cols[0]), U.rows)
    for k in range(U.rows):
        for i in range(len(cols[0])):
            J[i, k] = cols[k][i]
    return J


def nullity(J):
    """singular values relative to the largest; null: below 1e-60 (the polish leaves about 1e-88); the soft one is the
    smallest kept"""
    sv = sorted([abs(x) for x in mp.svd_r(J, compute_uv=False)], reverse=True)
    top = sv[0]
    rel = [x / top for x in sv]
    null = [x for x in rel if x < mp.mpf(10) ** -60]
    kept = [x for x in rel if x >= mp.mpf(10) ** -60]
    return {"nullity": len(null), "largest null / top": mp.nstr(max(null), 3) if null else None,
            "smallest kept / top": mp.nstr(min(kept), 3), "next kept / top": mp.nstr(sorted(kept)[1], 3) if len(kept) > 1 else None,
            "gap": mp.nstr(min(kept) / max(null), 3) if null else None}


def rebuild(P, frame_deg):
    """X1's float64 type-one point at the banked frame: the pinned solve, then the b = 0 system (X1's own functions)"""
    rec = P.solve(np.radians(frame_deg))
    u1, f1, _ = X1.gauss_newton(lambda v: S.residual(v, X1.A, rec["W"], False).real,
                                lambda v: S.jacobian(v, X1.A, rec["W"], False), rec["u"][:52], 0.3 * rec["threshold"])
    return u1, float(f1), rec["threshold"], bool(rec["converged"])


def same_row(r60, r100):
    diffs = []
    if r60["I"] != r100["I"]:
        diffs.append("I")
    for side in ("V", "V*"):
        for k in DIMS:
            if r60[side].get(k) != r100[side].get(k):
                diffs.append(f"{side}.{k}")
    if ("W" in r60) != ("W" in r100):
        diffs.append("W present")
    elif "W" in r60:
        for k in WKEYS:
            if r60["W"][k] != r100["W"][k]:
                diffs.append(f"W.{k}")
    return diffs


def run_one(sign, word):
    t0 = time.time()
    name = R.name_of(sign, word)
    x1 = json.loads((HERE / ("x1_" + name + ".json")).read_text(encoding="utf-8"))
    mp.mp.dps = DPS
    lambdas = [mp.mpf(1), mp.mpf("1.7"), mp.expj(mp.mpf("0.9"))]   # run.P_LAMBDAS, rebuilt at 100 digits
    G, img = FL.word_group(sign, word)
    chars, _ = R.characters(img)
    chosen = [chars[0]] + [c for c in chars[1:]][:4]
    P = X1.Pinned(sign, word)
    out = {"manifold": sign + word, "a": X1.A, "dps": DPS, "points": []}
    work = [("X1", e) for e in x1["points"]]
    x1c_path = HERE / ("x1c_" + name + ".json")
    if x1c_path.exists():
        work += [("X1c", e) for e in json.loads(x1c_path.read_text(encoding="utf-8"))["new points"]]
    for source, entry in work:
        if source == "X1c":
            entry = {"frame alpha0": entry["alpha"], "point": {"index rows": entry["index rows"],
                                                               "psi(l) = a X_l": entry["psi(l) = a X_l"]},
                     "u60": entry["point (60 digits)"]}
        if not entry.get("point"):
            out["points"].append({"frame alpha0": entry["frame alpha0"], "source": source, "skipped": "not polished there"})
            continue
        mp.mp.dps = DPS
        if source == "X1":
            u1, f1, thr, conv = rebuild(P, entry["frame alpha0"])
            mp.mp.dps = DPS
            U = mp.matrix([mp.mpf(x) for x in u1])
        else:
            U = mp.matrix([mp.mpf(x) for x in entry["u60"]])
            f1, thr, conv = None, None, True
        tp = time.time()
        Up, fp, itp, _ = X1.polish_gn(U, mp.mpf(X1.A), G, img, tol=mp.mpf(10) ** -TOL, maxit=40)
        mats, (Xl, Yl, Xt, Yt) = FL.unpack(Up)
        mod = L.Module(mats)
        ev = FL.eig_sorted(mod.word("abAB"))
        pt = {"frame alpha0": entry["frame alpha0"], "source": source, "rebuilt float64 |F|": f1,
              "rebuilt converged": conv if f1 is None else bool(conv and f1 < thr),
              "polished |F| (100 digits)": mp.nstr(fp, 3), "polish iterations": itp, "polish seconds": round(time.time() - tp),
              "X_l": mp.nstr(Xl, 15), "psi(l) = a X_l": mp.nstr(mp.mpf(X1.A) * Xl, 10),
              "60-digit psi(l)": entry["point"]["psi(l) = a X_l"],
              "rho(l) eigenvalues": [mp.nstr(e, 15) for e in ev],
              "min |eigenvalue - 1|": mp.nstr(min(abs(e - 1) for e in ev), 4)}
        tn = time.time()
        aa = mp.mpf(X1.A)
        pt["nullity, type one (100 digits)"] = nullity(FL.jacobian(Up, aa, G, img))
        Ub = mp.matrix([x for x in Up] + [mp.mpf(0)])
        pt["nullity, b free (100 digits)"] = nullity(jacobian_cs(lambda v: residual_b_free(v, aa, G, img), Ub))
        pt["b-free residual at the point"] = mp.nstr(mp.norm(residual_b_free(Ub, aa, G, img)), 3)
        if "nullity, type one" in entry["point"]:
            pt["X1's float64 nullities"] = [entry["point"]["nullity, type one"]["nullity"],
                                            entry["point"]["nullity, b free"]["nullity"]]
        pt["nullity seconds"] = round(time.time() - tn)
        rows, k = [], 0
        x1rows = entry["point"]["index rows"]          # the 60-digit rows (X1's or X1c's)
        for u_ in chosen:
            for lam in lambdas:
                nu = R.nu_of(u_, lam)
                for wedge in (False, True):
                    m = R.twisted(mats, nu, wedge)
                    with_w = (u_ == chars[0]) and (lam == 1 or lam == mp.mpf("1.7"))
                    rec = R.index_both(G, img, m, with_w)
                    row = {"u": [str(u_[0]), str(u_[1])], "lambda": mp.nstr(lam, 6), "module": "L2" if wedge else "4", **rec}
                    ref = x1rows[k]
                    assert (ref["u"], ref["lambda"], ref["module"]) == (row["u"], row["lambda"], row["module"]), (ref, row)
                    row["differs from 60 digits in"] = same_row(ref, row)
                    row["60-digit margins"] = ref["margins"]
                    rows.append(row)
                    k += 1
        assert k == len(x1rows)
        pt["index rows"] = rows
        out["points"].append(pt)
    # the summary
    allrows = [r for p in out["points"] for r in p.get("index rows", [])]
    out["summary"] = {
        "points": sum(1 for p in out["points"] if "index rows" in p),
        "rows": len(allrows),
        "route W rows": sum(1 for r in allrows if "W" in r),
        "rows with I != 0": sum(1 for r in allrows if r["I"] != 0),
        "rows differing from 60 digits": sum(1 for r in allrows if r["differs from 60 digits in"]),
        "rows failing an identity": sum(1 for r in allrows if not all(r["checks"].values())),
        "rows with a non-acyclic cusp": sum(1 for r in allrows if r["V"]["t0"] or r["V*"]["t0"] or r["V"]["h1(Delta)"]),
        "rows with a0 or b0 != 0": sum(1 for r in allrows if r["V"]["a0"] or r["V*"]["a0"]),
        "rows meeting the sealed margin bar (kept > 1e-20, dropped < 1e-40)":
            sum(1 for r in allrows if flt(r["margins"]["smallest kept"]) > 1e-20
                and flt(r["margins"]["largest dropped"]) < 1e-40),
        "60-digit rows meeting it": sum(1 for r in allrows if flt(r["60-digit margins"]["smallest kept"]) > 1e-20
                                        and flt(r["60-digit margins"]["largest dropped"]) < 1e-40),
        "points with nullities 4 and 5 (100 digits)": sum(1 for p in out["points"] if "index rows" in p
                                                          and p["nullity, type one (100 digits)"]["nullity"] == 4
                                                          and p["nullity, b free (100 digits)"]["nullity"] == 5),
        "largest dropped (100 digits)": mp.nstr(max((flt(r["margins"]["largest dropped"]) for r in allrows), default=0), 3),
        "smallest kept (100 digits)": mp.nstr(min((flt(r["margins"]["smallest kept"]) for r in allrows), default=1), 3),
        "largest polished |F|": max((p["polished |F| (100 digits)"] for p in out["points"] if "index rows" in p),
                                    key=flt, default=None),
        "smallest min |eigenvalue - 1|": min((p["min |eigenvalue - 1|"] for p in out["points"] if "index rows" in p),
                                             key=flt, default=None)}
    out["seconds"] = round(time.time() - t0)
    (HERE / ("x2_" + name + ".json")).write_text(json.dumps(out, indent=1, default=str))
    s = out["summary"]
    print(f"{sign}{word}: {out['seconds']} s; points {s['points']}; rows {s['rows']}; I != 0: {s['rows with I != 0']}; "
          f"differ from 60 digits: {s['rows differing from 60 digits']}; margin bar met "
          f"{s['rows meeting the sealed margin bar (kept > 1e-20, dropped < 1e-40)']}/{s['rows']} "
          f"(at 60 digits: {s['60-digit rows meeting it']}); dropped <= {s['largest dropped (100 digits)']}, "
          f"kept >= {s['smallest kept (100 digits)']}; nullities 4 and 5 at {s['points with nullities 4 and 5 (100 digits)']}"
          f"/{s['points']} points", flush=True)
    return name


def totals():
    """x2.json: the per-manifold summaries and their totals, read from every x2_<name>.json"""
    rows, tot = {}, {}
    for sign, word in R.MANIFOLDS:
        p = HERE / ("x2_" + R.name_of(sign, word) + ".json")
        if not p.exists():
            rows[sign + word] = "missing"
            continue
        s = json.loads(p.read_text(encoding="utf-8"))["summary"]
        rows[sign + word] = s
        for k, v in s.items():
            if isinstance(v, int):
                tot[k] = tot.get(k, 0) + v
    (HERE / "x2.json").write_text(json.dumps({"manifolds": rows, "totals": tot}, indent=1))
    print(json.dumps(tot, indent=1))


def main():
    args = sys.argv[1:]
    if args == ["--totals"]:
        totals()
        return
    if args == ["--all"]:
        jobs = list(R.MANIFOLDS)
    elif args and args[0] == "--some":
        jobs = list(zip(args[1::2], args[2::2]))
    else:
        jobs = list(zip(args[0::2], args[1::2]))
        for sign, word in jobs:
            run_one(sign, word)
        return
    from multiprocessing import Pool
    with Pool(4) as pool:
        pool.starmap(run_one, jobs)
    totals()


if __name__ == "__main__":
    main()
