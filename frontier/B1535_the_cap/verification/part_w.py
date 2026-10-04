#!/usr/bin/env python3
"""B1535 Part W -- Lemma W's census: the line has no interior class.  On every once-punctured-torus bundle with Anosov monodromy,
every finite-order character zeta has n(zeta) = 0.  Read on sm:B1529's 541 census rows (536 word states to length 12 and m004's
levels M2..M6) in two routes that share no code:

  - route X: sm:B1527's family_lib presentation <a, b, t | t g t^-1 = phi(g)> with its cusp <abAB, t'>, at every phi-fixed torsion
    character u of the fibre (denominator D) and every kappa = zeta(t') in mu_12; h^1 and r1 from the Fox Jacobian at 30 digits.
    It also reads Lemma W's mechanism: mu_u, the eigenvalue of phi* on H^1(F; u) = C^2 / C beta (u != 0), against the cusp
    transport tau_u (zeta(t) at kappa = 1): Lemma W holds iff mu_u = tau_u for every u != 0.
  - route S: SnapPy's own presentation of the bundle (b++w or b+-w, the naming family_lib.hyperbolic_sl2 uses) with SnapPy's
    peripheral curves, at every character of H_1 of order dividing 12 (from the abelianized relators); h^1, r1 the same way.
Both report n at every character and the margins (smallest kept and largest dropped singular values).  The order-dividing-12
characters are the same set in both routes, Hom(H_1, mu_12), so their counts must agree.

    python3 -u part_w.py [--workers N] --record   ->  part_w.json (summary) and part_w_rows.json (per row)"""
import json
import sys
import time
import warnings
from datetime import datetime, timezone
from fractions import Fraction
from itertools import product
from multiprocessing import Pool
from pathlib import Path

warnings.filterwarnings("ignore")
import mpmath as mp  # noqa: E402

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
B1529V = ROOT / "frontier" / "B1529_the_eigenvalue_one_locus" / "verification"
B1527V = ROOT / "frontier" / "B1527_the_cusp_decides" / "verification"
TOL = mp.mpf(10) ** -20
DPS = 30


def load_family():
    import importlib.util
    spec = importlib.util.spec_from_file_location("b1527_family_lib", B1527V / "family_lib.py")
    m = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(B1527V))
    spec.loader.exec_module(m)
    return m


def unit(fr):
    return mp.expjpi(2 * mp.mpf(fr.numerator) / fr.denominator)


# ============================================================================================ 1-dim Fox calculus
def wval(w, val):
    v = mp.mpc(1)
    for c in w:
        v = v * (val[c] if c.islower() else 1 / val[c.lower()])
    return v


def fox(w, g, val):
    """d w / d g at the character val (left cocycles: z(xy) = z(x) + x z(y))"""
    acc, pre = mp.mpc(0), mp.mpc(1)
    for c in w:
        if c.islower():
            if c == g:
                acc += pre
            pre = pre * val[c]
        else:
            pre = pre / val[c.lower()]
            if c.lower() == g:
                acc -= pre
    return acc


def svals(M):
    if not M or not M[0]:
        return []
    A = mp.matrix(M)
    return [abs(x) for x in mp.svd_c(A, compute_uv=False)]


def rank_of(M, marg):
    s = svals(M)
    r = sum(1 for x in s if x > TOL)
    kept = [x for x in s if x > TOL]
    drop = [x for x in s if x <= TOL]
    if kept:
        marg["kept"] = min(marg["kept"], min(kept)) if marg["kept"] is not None else min(kept)
    if drop:
        marg["dropped"] = max(marg["dropped"], max(drop)) if marg["dropped"] is not None else max(drop)
    return r


def nullspace(M, ncols):
    A = mp.matrix(M) if M else mp.matrix(0, ncols)
    if not M:
        return [[mp.mpc(1) if i == j else mp.mpc(0) for i in range(ncols)] for j in range(ncols)]
    U, S, V = mp.svd_c(A, full_matrices=True)
    r = sum(1 for i in range(min(A.rows, A.cols)) if abs(S[i]) > TOL)
    return [[mp.conj(V[i, j]) for j in range(ncols)] for i in range(r, ncols)]


def line_n(gens, rels, cusp, val, marg):
    """(h1, r1, n) of the character val on the presentation, with the cusp words"""
    J = [[fox(r, g, val) for g in gens] for r in rels]
    rk = rank_of(J, marg)
    trivial = all(abs(val[g] - 1) < TOL for g in gens)
    dimB = 0 if trivial else 1
    h1 = len(gens) - rk - dimB
    Z = nullspace(J, len(gens))
    R = [[sum(fox(w, g, val) * z[i] for i, g in enumerate(gens)) for w in cusp] for z in Z]
    BP = [[wval(w, val) - 1 for w in cusp]]
    rBP = rank_of(BP, marg)
    r1 = rank_of(R + BP, marg) - rBP
    return h1, r1, h1 - r1


# ============================================================================================ the two routes
def route_x(row, FL):
    sign, word = row["read as"][0], row["read as"][1:]
    G, img = FL.word_group(sign, word)
    chars, D = FL.torsion_characters(img)
    marg = {"kept": None, "dropped": None}
    out = {"chars": len(chars), "D": D, "n != 0": [], "mu != tau": [], "h1 pattern": {}, "order | 12": 0}
    for u in chars:
        ua, ub = unit(u[0]), unit(u[1])
        for k in range(12):
            kap = unit(Fraction(k, 12))
            tval = kap if sign == "+" else kap / (ua * ub)
            val = {"a": ua, "b": ub, "t": tval}
            h1, r1, n = line_n(G.gens, G.rels, G.cusp, val, marg)
            key = f"({h1}, {r1})"
            out["h1 pattern"][key] = out["h1 pattern"].get(key, 0) + 1
            if n != 0:
                out["n != 0"].append([str(u[0]), str(u[1]), k, h1, r1])
            if (u[0] * 12).denominator == 1 and (u[1] * 12).denominator == 1:
                out["order | 12"] += 1
        # the mechanism: mu_u against the transport tau_u (kappa = 1)
        if u != (0, 0):
            val = {"a": ua, "b": ub}
            Jf = [[fox(img[x], y, val) for y in "ab"] for x in "ab"]   # z(phi(x)) = sum_y J[x][y] z(y)
            mu = Jf[0][0] + Jf[1][1] - 1                                # J beta = beta, so the other eigenvalue is tr J - 1
            tau = mp.mpc(1) if sign == "+" else 1 / (ua * ub)
            if abs(mu - tau) > mp.mpf(10) ** -20:
                out["mu != tau"].append([str(u[0]), str(u[1]), mp.nstr(mu, 12), mp.nstr(tau, 12)])
    out["margins"] = {k: (mp.nstr(v, 6) if v is not None else None) for k, v in marg.items()}
    return out


def route_s(row):
    import snappy
    sign, word = row["read as"][0], row["read as"][1:]
    M = snappy.Manifold(("b++" if sign == "+" else "b+-") + word)
    G = M.fundamental_group()
    gens = list(G.generators())
    rels = list(G.relators())
    cusp = list(G.peripheral_curves()[0])
    E = [[r.count(g) - r.count(g.upper()) for g in gens] for r in rels]
    marg = {"kept": None, "dropped": None}
    out = {"snappy": M.name(), "homology": str(M.homology()), "order | 12": 0, "n != 0": [], "h1 pattern": {}}
    for x in product(range(12), repeat=len(gens)):
        if any(sum(e * xi for e, xi in zip(er, x)) % 12 for er in E):
            continue
        out["order | 12"] += 1
        val = {g: unit(Fraction(xi, 12)) for g, xi in zip(gens, x)}
        h1, r1, n = line_n(gens, rels, cusp, val, marg)
        key = f"({h1}, {r1})"
        out["h1 pattern"][key] = out["h1 pattern"].get(key, 0) + 1
        if n != 0:
            out["n != 0"].append([list(x), h1, r1])
    out["margins"] = {k: (mp.nstr(v, 6) if v is not None else None) for k, v in marg.items()}
    return out


def one(row):
    mp.mp.dps = DPS
    t0 = time.time()
    FL = load_family()
    rec = {"state": row["state"], "read as": row["read as"], "level": bool(row.get("level"))}
    rec["X"] = route_x(row, FL)
    rec["S"] = route_s(row)
    rec["agree on order | 12"] = rec["X"]["order | 12"] == rec["S"]["order | 12"]
    rec["seconds"] = round(time.time() - t0, 1)
    return rec


def rows():
    return json.loads((B1529V / "census_records.json").read_text())["records"]


def main():
    workers = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 2
    only = sys.argv[sys.argv.index("--only") + 1:] if "--only" in sys.argv else None
    R = [r for r in rows() if only is None or r["state"] in only]
    started = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    t0 = time.time()
    with Pool(workers) as pool:
        out = pool.map(one, R, chunksize=4)
    summ = {"started": started, "rows": len(out),
            "route X characters": sum(r["X"]["chars"] * 12 for r in out),
            "route S characters": sum(r["S"]["order | 12"] for r in out),
            "n != 0 (X)": sum(len(r["X"]["n != 0"]) for r in out),
            "n != 0 (S)": sum(len(r["S"]["n != 0"]) for r in out),
            "mu != tau": sum(len(r["X"]["mu != tau"]) for r in out),
            "order | 12 counts agree": all(r["agree on order | 12"] for r in out),
            "margins X": {"smallest kept": min((mp.mpf(r["X"]["margins"]["kept"]) for r in out if r["X"]["margins"]["kept"]),
                                               default=None),
                          "largest dropped": max((mp.mpf(r["X"]["margins"]["dropped"]) for r in out
                                                  if r["X"]["margins"]["dropped"]), default=None)},
            "margins S": {"smallest kept": min((mp.mpf(r["S"]["margins"]["kept"]) for r in out if r["S"]["margins"]["kept"]),
                                               default=None),
                          "largest dropped": max((mp.mpf(r["S"]["margins"]["dropped"]) for r in out
                                                  if r["S"]["margins"]["dropped"]), default=None)},
            "seconds": round(time.time() - t0)}
    summ = {k: (mp.nstr(v, 6) if isinstance(v, mp.mpf) else v) for k, v in summ.items()}
    for k in ("margins X", "margins S"):
        summ[k] = {a: (mp.nstr(b, 6) if b is not None else None) for a, b in summ[k].items()}
    summ["Lemma W holds"] = summ["n != 0 (X)"] == 0 and summ["n != 0 (S)"] == 0 and summ["mu != tau"] == 0 and \
        summ["order | 12 counts agree"]
    print(json.dumps(summ, indent=1))
    if "--record" in sys.argv:
        (HERE / "part_w.json").write_text(json.dumps(summ, indent=1) + "\n")
        (HERE / "part_w_rows.json").write_text(json.dumps(out, indent=1) + "\n")
    return summ, out


if __name__ == "__main__":
    main()
