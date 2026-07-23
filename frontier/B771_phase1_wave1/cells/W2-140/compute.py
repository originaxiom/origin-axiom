"""W2-140 (B157) -- the metallic exponent law k in [A,B] = s*mu^k across the (m,o,n) grid,
read via the A-polynomial-slope route (the matrix identity on the order(mu)=infinity stratum;
raw 25-var Groebner is WALLED and is NOT attempted).

Question (LEAD_REGISTER #5 / PREREG_WAVE2 W2-140): is there a closed-form exponent law across
the (m,o,n) grid?  Banked state: k=4-m(o-3) (B154) was REFUTED by bronze (B157); B198/B199
sharpened the grid + refuted every k(o,m), k(A^m-spectrum) and gcd rule, leaving "no law".

NEW IDEA TESTED HERE (stated before computing -- in-cell prereg):
the B199 refuters kill laws in (o,m) and in A^m alone, but leave open laws in the invariant pair
    eff = projective order of the boundary spectrum  (order of the eigenvalue-RATIO group of A)
    g   = gcd(m, eff)
    e   = eff/g = projective order of A^m.
On the banked table the exponent looks single-valued on (e,g).  Two candidate closed forms fit
every banked point:
    C1:  k = floor((7-e)/g)
    C2:  k = 7-e   if g==1,   4-g   if g>=2      (piecewise)
Both must be tested on NEW off-grid cells computed IN-CELL (never cited):
    P1: (m=1,o=6,n=4)  eff=6 g=1 e=6  -> C1: 1   C2: 1
    P2: (m=2,o=6,n=3)  eff=6 g=2 e=3  -> C1: 2   C2: 2
    P3: (m=3,o=8,n=4)  eff=4 g=1 e=4  -> C1: 3   C2: 3
    P4: (m=2,o=8,n=4,exps[0,1,3,4]) eff=8 g=2 e=4 -> C1: floor(3/2)=1  C2: 4-2=2   <- DISCRIMINATES
    P5: (m=1,o=8,n=4,exps[0,1,3,4]) eff=8 g=1 e=8 -> both predict -1 => NO clean k / empty
All banked-table cells are RE-COMPUTED in-cell (discriminating facts never cited), each at 2
independent RNG-stream pairs, with conditioning/irreducibility/non-central-longitude gates.

House method: pyenv python3, numerics >=2 seeds with conditioning; exact word-identity and
spectral-collision checks in sympy.  Standalone character-variety math; no physics; nothing to
CLAIMS.md.  Re-runnable end-to-end:  python3 compute.py            (uses cached results/*.json)
                                     python3 compute.py --fresh    (recompute everything)
Heavy cells (SL5 o5) can be pre-run in parallel:  python3 compute.py --only m1_o5_n5
"""
import os, sys, json, time, argparse
from math import gcd
from collections import Counter

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
sys.path.insert(0, os.path.join(REPO, "frontier", "B198_metallic_exponent_CAS"))
from gauge_newton import make_A, newton_t, newton_bt, irred, exponent  # noqa: E402

RESULTS = os.path.join(HERE, "results")
os.makedirs(RESULTS, exist_ok=True)


# ---------------------------------------------------------------- invariants
def eff_of(o, exps):
    """Projective order of the spectrum diag(z^e): order of the eigenvalue-ratio group."""
    ds = [abs(a - b) for i, a in enumerate(exps) for b in exps[i + 1:]]
    gg = o
    for d in ds:
        gg = gcd(gg, d % o)
    return o // gg if gg else o


def invariants(m, o, exps):
    eff = eff_of(o, exps)
    g = gcd(m, eff)
    e = eff // g
    return eff, g, e


# ---------------------------------------------------------------- exact checks (sympy)
def exact_checks():
    import sympy as sp
    out = {}
    # (a) free-group word identity phi_m([A,B]) = A^m [A,B] A^-m  for m=1..4
    def reduce_word(w):
        out_ = []
        for s in w:
            if out_ and out_[-1][0] == s[0] and out_[-1][1] == -s[1]:
                out_.pop()
            else:
                out_.append(s)
        return tuple(out_)
    def inv(w):
        return tuple((c, -p) for c, p in reversed(w))
    def phi_m(w, m):
        # sigma_R^m then sigma_L^m composed:  phi_m: A -> A (A^m B)^m, B -> A^m B  (B157 form)
        A = tuple([("A", 1)])
        B = tuple([("B", 1)])
        Am = tuple([("A", 1)]) * m
        AmB = reduce_word(Am + B)
        img = {"A": reduce_word(A + AmB * m), "B": AmB}
        res = []
        for c, p in w:
            res += list(img[c] if p == 1 else inv(img[c]))
        return reduce_word(tuple(res))
    ok = True
    for m in (1, 2, 3, 4):
        A = (("A", 1),); B = (("B", 1),)
        comm = reduce_word(A + B + inv(A) + inv(B))
        lhs = phi_m(comm, m)
        Am = A * m
        rhs = reduce_word(Am + comm + inv(Am))
        if lhs != rhs:
            ok = False
    out["word_identity_phi_m_commutator_m1..4"] = ok
    # (b) the A^m-spectrum collision (B199 refuter 2, recomputed exactly):
    #     A(o=4,{1,i,-i})^2 == A(o=6,{1,z6,z6^5})^3 == diag(1,-1,-1)
    i_ = sp.I
    z6 = sp.exp(2 * sp.pi * sp.I / 6)
    A4 = sp.diag(1, i_, -i_)
    A6 = sp.diag(1, z6, z6 ** 5)
    coll = sp.simplify(A4 ** 2 - A6 ** 3) == sp.zeros(3)
    tgt = sp.simplify(A4 ** 2 - sp.diag(1, -1, -1)) == sp.zeros(3)
    out["Am_spectrum_collision_A4sq_eq_A6cube_eq_diag(1,-1,-1)"] = bool(coll and tgt)
    # (c) invariants of the collision pair DIFFER in g:  (m=2,eff=4): g=2 ; (m=3,eff=6): g=3
    out["collision_separated_by_g"] = (gcd(2, 4), gcd(3, 6)) == (2, 3)
    return out


# ---------------------------------------------------------------- numeric cell engine
def mu_order(mu, tol=1e-6, maxd=90):
    ev = np.linalg.eigvals(mu)
    off = float(np.max(np.abs(np.abs(ev) - 1.0)))
    order = next((d for d in range(1, maxd + 1) if np.max(np.abs(ev ** d - 1)) < tol), None)
    return order, off


def run_cell(m, o, n, exps, seeds=300, rng_seeds=(0, 1), want_geo=8,
             relresid=1e-10, errtol=1e-6, kmax=16):
    """One grid cell: gauge-fixed Newton sweep; k read as the A-poly slope (matrix identity)
    on the order(mu)=infinity (loxodromic/geometric) stratum only.  Detailed records kept."""
    A = make_A(o, exps)[0]
    Ai = np.linalg.inv(A)
    gfix = list(range(n - 1))
    geo, fin = Counter(), Counter()
    fin_orders = set()
    n_irred = 0
    n_lox = 0
    lox_errs = []          # best-k err for every loxodromic irreducible rep (sublocus diagnostics)
    sample = None
    t0 = time.time()
    for rs in rng_seeds:
        rng = np.random.default_rng(rs)
        for _ in range(seeds):
            if m == 1:
                Aa, Aii, Ai2 = make_A(o, exps)
                t, r = newton_t(Aa, Aii, Ai2, n, gfix, rng)
                B = None if t is None else Ai2 @ t @ Aa @ np.linalg.inv(t)
            else:
                x, r = newton_bt(A, m, n, gfix, rng)
                B, t = (None, None) if x is None else (x[:n * n].reshape(n, n), x[n * n:].reshape(n, n))
            if t is None or r > relresid or abs(np.linalg.det(t)) < 1e-3 or np.linalg.cond(t) > 1e6:
                continue
            mu = np.linalg.matrix_power(Ai, m) @ t
            if np.max(np.abs(mu - t)) < 1e-6:      # o|m degenerate: mu=t, not a metallic cusp
                continue
            if irred(A, B, n) != n * n:
                continue
            comm = A @ B @ Ai @ np.linalg.inv(B)
            offc = np.max(np.abs(comm - np.trace(comm) / n * np.eye(n)))
            if offc < 1e-4:                        # central longitude: excluded
                continue
            n_irred += 1
            s_, k_, err = exponent(A, B, t, m, kmax=kmax)
            order, off = mu_order(mu)
            if order is None:
                n_lox += 1
                lox_errs.append(float(err))
                if err < errtol and k_ >= 1:
                    # best-fit margin: second-best j must be far
                    muI = np.linalg.inv(mu)
                    second = 9e9
                    for j in range(0, kmax + 1):
                        if j == k_:
                            continue
                        mj = np.linalg.matrix_power(mu, j)
                        second = min(second,
                                     min(np.max(np.abs(comm - mj)), np.max(np.abs(comm + mj))))
                    if second > 1e-2:
                        geo[(s_, k_)] += 1
                        if sample is None:
                            sample = {"mu_abs": [round(float(a), 4)
                                                 for a in np.abs(np.linalg.eigvals(mu))],
                                      "err": float(err), "second": float(second),
                                      "cond_t": float(np.linalg.cond(t))}
            else:
                if err < errtol:
                    fin[(s_, k_)] += 1
                    fin_orders.add(int(order))
        if sum(geo.values()) >= want_geo:
            break
    eff, g, e = invariants(m, o, exps)
    dom = max(geo.items(), key=lambda kv: kv[1])[0] if geo else None
    kvals = sorted({k for (_, k) in geo})
    return {
        "m": m, "o": o, "n": n, "exps": list(exps),
        "eff": eff, "g": g, "e": e,
        "rng_seeds": list(rng_seeds), "seeds_per_stream": seeds,
        "n_irred": n_irred, "n_lox": n_lox,
        "geo": {f"{s},{k}": c for (s, k), c in geo.items()},
        "geo_unique": len(kvals) == 1,   # uniqueness of k (sign may split, e.g. o=8: B199 s+-)
        "k_values": kvals,
        "signs": sorted({s for (s, _) in geo}),
        "k": (dom[1] if dom else None), "s": (dom[0] if dom else None),
        "clean_geo_reps": int(sum(geo.values())),
        "lox_err_median": (float(np.median(lox_errs)) if lox_errs else None),
        "fin": {f"{s},{k}": c for (s, k), c in fin.items()},
        "fin_orders": sorted(fin_orders),
        "sample": sample,
        "secs": round(time.time() - t0, 1),
    }


def cell_cached(cid, *args, fresh=False, **kw):
    p = os.path.join(RESULTS, cid + ".json")
    if not fresh and os.path.exists(p):
        with open(p) as f:
            return json.load(f)
    res = run_cell(*args, **kw)
    res["id"] = cid
    with open(p, "w") as f:
        json.dump(res, f, indent=1)
    return res


# ---------------------------------------------------------------- the cell list
# (id, m, o, n, exps, kw) -- two disjoint RNG streams inside each run; every banked value
# is RE-computed here (never cited).  New off-grid prediction cells marked NEW.
CELLS = [
    # re-computed banked table (A-poly-slope reading on the loxodromic stratum)
    ("m1_o3_n3", 1, 3, 3, [0, 1, 2], {}),
    ("m1_o4_n3", 1, 4, 3, [0, 1, 3], {}),
    ("m2_o3_n3", 2, 3, 3, [0, 1, 2], {}),
    ("m2_o4_n3", 2, 4, 3, [0, 1, 3], {}),
    ("m3_o4_n3", 3, 4, 3, [0, 1, 3], {}),
    ("m3_o6_n3", 3, 6, 3, [0, 1, 5], {}),
    ("m1_o3_n4", 1, 3, 4, [0, 0, 1, 2], {}),
    ("m1_o8_n4", 1, 8, 4, [1, 3, 5, 7], {}),
    ("m2_o8_n4", 2, 8, 4, [1, 3, 5, 7], {"seeds": 150, "want_geo": 6}),
    ("m1_o5_n5", 1, 5, 5, [0, 1, 2, 3, 4], {"seeds": 350, "want_geo": 4}),   # heavy
    # NEW off-grid prediction cells (predictions in the header, fixed before computing)
    ("m1_o6_n4", 1, 6, 4, [0, 0, 1, 5], {"seeds": 350}),                     # P1 -> 1
    ("m2_o6_n3", 2, 6, 3, [0, 1, 5], {"seeds": 350}),                        # P2 -> 2
    ("m3_o8_n4", 3, 8, 4, [1, 3, 5, 7], {"seeds": 150, "want_geo": 6}),      # P3 -> 3
    ("m2_o8e8_n4", 2, 8, 4, [0, 1, 3, 4], {"seeds": 150, "want_geo": 6}),    # P4 C1:1 C2:2
    ("m1_o8e8_n4", 1, 8, 4, [0, 1, 3, 4], {"seeds": 300}),                   # P5 -> none
    # rank-independence backup for P1's class at another spectrum
    ("m1_o6b_n4", 1, 6, 4, [0, 1, 2, 3], {"seeds": 300}),                    # eff=6 g=1 e=6 -> 1
    # C1-vs-C6 discriminators added mid-cell (predictions fixed before their computation):
    # C6 := k=(8-e-g)/g when a positive integer, ELSE rigid sublocus empty
    ("m2_o10_n4", 2, 10, 4, [0, 1, 3, 6], {"seeds": 150, "want_geo": 6}),    # (e,g)=(5,2) C1:1 C6:EMPTY
    ("m3_o9_n3", 3, 9, 3, [0, 1, 8], {"seeds": 350}),                        # (e,g)=(3,3) C1:1 C6:EMPTY
]
SECOND_STREAMS = {"default": (7, 11), "m1_o5_n5": (7,)}


# ---------------------------------------------------------------- probe merge
def probe_points():
    """Merge the k-constrained-Newton probe results (probe_k.py; logs under results/) into
    grid points.  A probe-ESTABLISHED point needs hits on >=2 RNG streams, or >=5 hits on one
    stream plus a zero control at a neighbouring k (the hits are independent random starts
    converging onto the constrained variety; each is a verified rep at resid<1e-12).
    A probe-EMPTY record is a bounded negative (absence of hits, not proof)."""
    p = os.path.join(RESULTS, "probe_points.json")
    if not os.path.exists(p):
        return [], []
    with open(p) as f:
        recs = json.load(f)
    groups = {}
    for r in recs:
        key = (r["m"], r["o"], r["n"], tuple(r["exps"]))
        groups.setdefault(key, []).append(r)
    est, empty = [], []
    for (m, o, n, exps), rs in groups.items():
        hitks = {}
        for r in rs:
            if r["hits"] > 0:
                hitks.setdefault((r["s"], r["k"]), []).append(r)
        eff, g, e = invariants(m, o, list(exps))
        base = {"id": "probe_m%d_o%d_n%d" % (m, o, n), "m": m, "o": o, "n": n,
                "exps": list(exps), "eff": eff, "g": g, "e": e}
        if hitks:
            if len({k for (_, k) in hitks}) == 1:
                (s, k), rr = next(iter(hitks.items()))
                streams = {x["rng"] for x in rr}
                tot = sum(x["hits"] for x in rr)
                controls0 = any(x["hits"] == 0 and abs(x["k"] - k) == 1 for x in rs)
                if len(streams) >= 2 or (tot >= 5 and controls0):
                    est.append({**base, "k": k, "s": s, "hits": tot,
                                "streams": sorted(streams), "established": True})
                else:
                    est.append({**base, "k": k, "s": s, "hits": tot,
                                "streams": sorted(streams), "established": False})
        else:
            tried = sorted({r["k"] for r in rs})
            tot = sum(r["of"] for r in rs)
            empty.append({**base, "k_tried": tried, "total_seeds": tot})
    return est, empty


# ---------------------------------------------------------------- law analysis
def law_analysis(rows):
    pts = [r for r in rows if r["k"] is not None and r["geo_unique"] and r["clean_geo_reps"] >= 2]
    est, probe_empty = probe_points()
    swept = {(r["m"], r["o"], r["n"]) for r in pts}
    for r in est:
        if r["established"] and (r["m"], r["o"], r["n"]) not in swept:
            r["clean_geo_reps"] = r["hits"]
            r["n_lox"] = r["hits"]
            pts.append(r)
    have = {(r["m"], r["o"], r["n"]) for r in rows} | {(p["m"], p["o"], p["n"]) for p in pts}
    rows = rows + [dict(r, **{"k": None, "n_lox": 999,           # probe-only bounded negative
                              "id": r["id"] + "_probeempty"}) for r in probe_empty
                   if (r["m"], r["o"], r["n"]) not in have]
    report_probe = {"probe_established": est, "probe_empty": probe_empty}
    weak = [r for r in rows if r["k"] is not None and not (r["geo_unique"] and r["clean_geo_reps"] >= 2)]
    empty = [r for r in rows if r["k"] is None]
    report = {"points": [], "weak": [], "empty": [r["id"] for r in empty]}
    report.update(report_probe)
    for r in pts:
        report["points"].append({k: r[k] for k in ("id", "m", "o", "n", "eff", "g", "e", "k", "s",
                                                   "clean_geo_reps", "n_lox")})
    for r in weak:
        report["weak"].append({k: r[k] for k in ("id", "m", "o", "n", "eff", "g", "e", "k",
                                                 "clean_geo_reps", "geo")})
    # single-valuedness of k on (e,g) vs on other invariant pairs
    def classes(keyf):
        d = {}
        for r in pts:
            d.setdefault(keyf(r), set()).add(r["k"])
        return d
    eg = classes(lambda r: (r["e"], r["g"]))
    report["k_single_valued_on_(e,g)"] = all(len(v) == 1 for v in eg.values())
    report["(e,g)_classes"] = {str(k): sorted(v) for k, v in sorted(eg.items())}
    om = classes(lambda r: (r["o"], r["m"]))
    report["k_single_valued_on_(o,m)"] = all(len(v) == 1 for v in om.values())
    # candidate closed forms
    def C1(r):
        return (7 - r["e"]) // r["g"]
    def C2(r):
        return 7 - r["e"] if r["g"] == 1 else 4 - r["g"]
    def C3(r):
        return 4 - r["m"] * (r["o"] - 3)          # the banked partial law (B154)
    def C4(r):
        return 7 - r["o"]
    def C5(r):
        return 7 - r["eff"]
    def C6(r):
        # k = (8-e-g)/g when a positive integer, else the rigid sublocus is EMPTY (None)
        num = 8 - r["e"] - r["g"]
        return num // r["g"] if (num > 0 and num % r["g"] == 0) else None
    def C7(r):
        # the post-(3,2)-hit refinement: k = floor((8-e-g)/g), empty when < 1
        v = (8 - r["e"] - r["g"]) // r["g"]
        return v if v >= 1 else None
    cands = {"C1 floor((7-e)/g)": C1, "C2 piecewise(7-e | 4-g)": C2,
             "C3 4-m(o-3) [banked partial]": C3, "C4 7-o": C4, "C5 7-eff": C5,
             "C6 (8-e-g)/g-integrality": C6, "C7 floor((8-e-g)/g)": C7}
    report["candidates"] = {}
    # sublocus-empty cells: >=50 loxodromic irreducible reps swept, ZERO clean exponent --
    # excluding any (m,o,n) where the k-constrained probe DID establish the sublocus
    # (random sweeps can miss a thin sublocus: the m2_o6_n3 lesson)
    haveval = {(p["m"], p["o"], p["n"]) for p in pts}
    subempty = [r for r in rows if r["k"] is None and r["n_lox"] >= 50
                and (r["m"], r["o"], r["n"]) not in haveval]
    report["sublocus_empty_cells"] = [
        {k: r[k] for k in ("id", "m", "o", "n", "eff", "g", "e", "n_lox")} for r in subempty]
    for name, f in cands.items():
        fails = [(r["id"], r["k"], f(r)) for r in pts if f(r) != r["k"]]
        # existence scoring: a law claiming k>=1 at a sublocus-empty cell fails existence there
        exist_fails = [(r["id"], f(r)) for r in subempty
                       if (f(r) is not None and f(r) >= 1)]
        report["candidates"][name] = {"fits_all_values": not fails, "value_failures": fails,
                                      "existence_failures": exist_fails}
    # brute-force affine search over 1-2 feature integer forms (overfit audit)
    feats = {"m": lambda r: r["m"], "o": lambda r: r["o"], "n": lambda r: r["n"],
             "eff": lambda r: r["eff"], "g": lambda r: r["g"], "e": lambda r: r["e"],
             "gcd(m,o)": lambda r: gcd(r["m"], r["o"])}
    fits = []
    names = list(feats)
    for i, f1 in enumerate(names):
        for c1 in range(-4, 5):
            for c0 in range(-8, 9):
                if all(c0 + c1 * feats[f1](r) == r["k"] for r in pts):
                    fits.append(f"{c0} + {c1}*{f1}")
        for f2 in names[i + 1:]:
            for c1 in range(-4, 5):
                for c2 in range(-4, 5):
                    for c0 in range(-8, 9):
                        if all(c0 + c1 * feats[f1](r) + c2 * feats[f2](r) == r["k"] for r in pts):
                            fits.append(f"{c0} + {c1}*{f1} + {c2}*{f2}")
    report["affine_fits_1_2_features"] = fits
    return report


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fresh", action="store_true")
    ap.add_argument("--only", default=None, help="run just this cell id (for parallel pre-runs)")
    args = ap.parse_args()

    if args.only:
        spec = next(c for c in CELLS if c[0] == args.only)
        cid, m, o, n, exps, kw = spec
        r1 = cell_cached(cid, m, o, n, exps, fresh=args.fresh, rng_seeds=(0, 1), **kw)
        ss = SECOND_STREAMS.get(cid, SECOND_STREAMS["default"])
        r2 = cell_cached(cid + "_v", m, o, n, exps, fresh=args.fresh, rng_seeds=ss, **kw)
        print(json.dumps({"run1": r1, "run2": r2}, indent=1))
        return

    print("=" * 78)
    print("W2-140 / B157: the metallic exponent law via the A-polynomial-slope route")
    print("=" * 78)

    print("\n[0] exact checks (sympy):")
    for k, v in exact_checks().items():
        print("   %-58s %s" % (k, "PASS" if v else "FAIL"))

    print("\n[1] the grid (each cell: 2 independent RNG-stream pairs; k = A-poly slope on the")
    print("    order(mu)=inf stratum; gates: full-relation 1e-10, irreducible Burnside=n^2,")
    print("    cond(t)<1e6, non-central longitude, non-degenerate mu!=t, margin>1e-2):")
    rows = []
    for cid, m, o, n, exps, kw in CELLS:
        r1 = cell_cached(cid, m, o, n, exps, fresh=args.fresh, rng_seeds=(0, 1), **kw)
        ss = SECOND_STREAMS.get(cid, SECOND_STREAMS["default"])
        r2 = cell_cached(cid + "_v", m, o, n, exps, fresh=args.fresh, rng_seeds=ss, **kw)
        agree = (r1["k"] == r2["k"])   # k must agree; the sign may split (o=8: B199 s+-)
        merged = dict(r1)
        merged["clean_geo_reps"] = r1["clean_geo_reps"] + r2["clean_geo_reps"]
        merged["geo_unique"] = r1["geo_unique"] and r2["geo_unique"] and agree
        merged["verified_2streams"] = agree
        rows.append(merged)
        kstr = ("k=%d s=%+d" % (r1["k"], r1["s"])) if r1["k"] is not None else "EMPTY/no-geo"
        print("  %-12s m=%d o=%d n=%d eff=%d g=%d e=%d : %-14s reps=%d+%d lox=%d %s  [%s]" % (
            cid, m, o, n, merged["eff"], merged["g"], merged["e"], kstr,
            r1["clean_geo_reps"], r2["clean_geo_reps"], r1["n_lox"] + r2["n_lox"],
            ("geo=%s" % r1["geo"]) if not r1["geo_unique"] else "",
            "2-stream AGREE" if agree else "STREAMS DISAGREE"))

    print("\n[2] law analysis:")
    rep = law_analysis(rows)
    print(json.dumps({k: v for k, v in rep.items() if k != "points"}, indent=1))
    print("\n  committed points (unique k, >=2 clean reps, 2-stream verified):")
    for p in rep["points"]:
        print("   ", p)

    with open(os.path.join(HERE, "law_report.json"), "w") as f:
        json.dump(rep, f, indent=1)

    # verdict material
    print("\n[3] VERDICT MATERIAL:")
    for name, c in rep["candidates"].items():
        print("  %-32s fits_values=%s  value_fails=%s  existence_fails=%s" %
              (name, c["fits_all_values"], c["value_failures"], c["existence_failures"]))
    print("  k single-valued on (e,g):", rep["k_single_valued_on_(e,g)"])
    print("  affine 1-2 feature fits:", rep["affine_fits_1_2_features"] or "NONE")
    anyfits = any(c["fits_all_values"] and not c["existence_failures"]
                  for c in rep["candidates"].values()) or rep["affine_fits_1_2_features"]
    print("\n  => %s" % (
        "a closed form matching all computed points EXISTS (RESOLVED-A material)" if anyfits
        else "NO closed form matches all computed points at the swept size; the table is "
             "banked; k is single-valued on (e,g) but the g=1 row (4,3,2,4) admits no "
             "closed form tried, and existence is (m,n)-dependent beyond (e,g) "
             "(RESOLVED-B material)"))


if __name__ == "__main__":
    main()
