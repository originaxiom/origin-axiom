#!/usr/bin/env python3
"""B1536 control K2 (positive control, banked data only): sm:B1534's silver squares m135 = -LLRR and m136 = +LLRR read AS BASES
at each of their 14 members, on the finite abelian cover of every subgroup H of the member's contributing characters C_nu, by
route N and route R.  Every banked count at a non-special class must be reproduced: the one class, the interior class, and the
generic class (sm:B1534's c_g1 and c_g2 are both generic, so they read the same; this control reads its own generic class).
It includes m135's generation-shaped (-1, -1) at the interior class: the instruments must find the one generation the frame
does carry.  The twisted four's supply n_N(nu^3 rho) is also reported on each cover.

    python3 control_k2.py [--record]   ->  k2.json"""
import json
import sys
import time
import warnings
from fractions import Fraction as Fr
from pathlib import Path

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))
import numpy as np  # noqa: E402
import cover_lib as CL  # noqa: E402
import gf  # noqa: E402
import route_n as N  # noqa: E402
import route_r as R  # noqa: E402

B1534V = ROOT / "frontier" / "B1534_the_silver_covers" / "verification"


def parse_char(lab):
    """'(w_a, w_b; k)' -> (w_a, w_b, k)"""
    a, rest = lab.strip("()").split(",", 1)
    b, k = rest.split(";")
    return Fr(a.strip()), Fr(b.strip()), Fr(k.strip())


def cover_of(H, sign):
    """the right action x^g = x + psi(g) on the image of psi(g) = (chi(g))_{chi in H}; chi(t) = k (+) or k - w_a - w_b (-)"""
    chis = [parse_char(h) for h in sorted(H)]
    val = {"a": tuple(c[0] for c in chis), "b": tuple(c[1] for c in chis),
           "t": tuple((c[2] if sign == "+" else c[2] - c[0] - c[1]) % 1 for c in chis)}
    zero = tuple(Fr(0) for _ in chis)
    pts, idx, todo = [zero], {zero: 0}, [zero]
    while todo:
        x = todo.pop()
        for g in "abt":
            for s in (1, -1):
                y = tuple((xi + s * gi) % 1 for xi, gi in zip(x, val[g]))
                if y not in idx:
                    idx[y] = len(pts)
                    pts.append(y)
                    todo.append(y)
    return {g: [idx[tuple((xi + gi) % 1 for xi, gi in zip(x, val[g]))] for x in pts] for g in "abt"}


def route_r_classes(G, VetaR, pR):
    """route R's own base classes (its own elimination): {'c1': z} or {'int': z, 'gen': z}"""
    gens = list(G.gens)
    e = 4
    z0 = R.base_cocycle(G, VetaR, pR)
    # the class space and the interior line, by route R's own linear algebra
    import rs_lib as RS
    inv = {g: RS.minv(VetaR[g], pR) for g in gens}
    rows = []
    for r in G.rels:
        rows.append(np.hstack([fox_small(VetaR, inv, r, g, pR) for g in gens]))
    Z = R.pnull(np.vstack(rows), pR, 3 * e)
    Bm = np.vstack([(VetaR[g] - np.eye(e, dtype=np.int64)) % pR for g in gens])
    reps, cur = [], Bm
    for z in Z:
        c2 = np.hstack([cur, z.reshape(-1, 1)])
        if R.prank(c2, pR) > R.prank(cur, pR):
            reps.append(z)
            cur = c2
    if len(reps) == 1:
        return {"c1": {g: reps[0][i * e:(i + 1) * e] for i, g in enumerate(gens)}}
    assert len(reps) == 2
    Rm = np.vstack([np.hstack([fox_small(VetaR, inv, w, g, pR) for g in gens]) for w in G.cusp])
    P1 = word_small(VetaR, inv, G.cusp[0], pR)
    P2 = word_small(VetaR, inv, G.cusp[1], pR)
    BP = np.vstack([(P1 - np.eye(e, dtype=np.int64)) % pR, (P2 - np.eye(e, dtype=np.int64)) % pR])
    A = np.hstack([RS.mmul(Rm, np.stack(reps, axis=1), pR), (-BP) % pR])
    K = R.pnull(A, pR, 2 + e)
    xs = [k[:2] for k in K if np.any(k[:2] % pR)]
    x = xs[0]
    cint = ((x[0] % pR) * reps[0] % pR + (x[1] % pR) * reps[1] % pR) % pR
    cb = reps[0] if (x[1] % pR) else reps[1]
    s = 5 * pow(11, -1, pR) % pR
    gen = (cb + s * cint % pR) % pR
    return {"int": {g: cint[i * e:(i + 1) * e] for i, g in enumerate(gens)},
            "gen": {g: gen[i * e:(i + 1) * e] for i, g in enumerate(gens)}}


def word_small(M, inv, w, p):
    import rs_lib as RS
    e = next(iter(M.values())).shape[0]
    X = np.eye(e, dtype=np.int64)
    for c in w:
        X = RS.mmul(X, M[c] if c.islower() else inv[c.lower()], p)
    return X


def fox_small(M, inv, w, g, p):
    import rs_lib as RS
    e = next(iter(M.values())).shape[0]
    K = np.zeros((e, e), dtype=np.int64)
    Pre = np.eye(e, dtype=np.int64)
    for c in w:
        h = c.lower()
        if c.islower():
            if h == g:
                K = (K + Pre) % p
            Pre = RS.mmul(Pre, M[h], p)
        else:
            Pre = RS.mmul(Pre, inv[h], p)
            if h == g:
                K = (K - Pre) % p
    return K


def main():
    t0 = time.time()
    banked = json.loads((B1534V / "terms.json").read_text())["states"]
    pN = gf.primes_1_mod(120, N.P_BOUND, 1)[0]
    pR = gf.primes_1_mod(120, 1 << 31, 1)[0]
    FN, FR = gf.GF(pN, 120), gf.GF(pR, 120)
    out = {"members": [], "primes": {"route N": pN, "route R": pR}}
    agree_all = True
    for key, name in (("-LLRR", "m135"), ("+LLRR", "m136")):
        st = CL.state(name)
        BN, BR = N.Base(st, FN), N.Base(st, FR)
        for mem in banked[key]["members"]:
            u = (Fr(mem["u"][0]), Fr(mem["u"][1]))
            kap = Fr(mem["kappa"])
            chiN, chiR = BN.character(u, kap), BR.character(u, kap)
            pa1 = N.perm_arrays(BN.G, {"a": [0], "b": [0], "t": [0]})
            clsN = N.base_classes(BN, N.tensor(BN, N.small_four(BN, chiN, 5), pa1))
            VetaR = {g: BR.rho[g] * pow(int(chiR[g]), 5, pR) % pR for g in BR.gens}
            clsR = route_r_classes(BR.G, VetaR, pR)
            rec = {"state": name, "u": mem["u"], "kappa": mem["kappa"], "rows": []}
            for bname, rows in mem["counts"].items():
                cname = {"the class": "c1", "c_int": "int", "c_g1": "gen", "c_g2": "gen"}.get(bname)
                if cname is None:
                    continue                      # special classes are not read by this control
                for row in rows:
                    perms = cover_of(row["H"], st["sign"])
                    assert CL.check_cover(BN.G, perms)
                    d = len(perms["a"])
                    pa = N.perm_arrays(BN.G, perms)
                    z = clsN[cname]
                    cz = {g: z[gi * 4:(gi + 1) * 4] for gi, g in enumerate(BN.gens)}
                    rN = N.reading(BN, pa, chiN, {g: [cz[g]] * d for g in BN.gens})
                    cov = R.PCover(BR.G, perms)
                    cv = R.cocycle_on_words(BR.G, VetaR, clsR[cname], cov.sword, pR)
                    rR = R.reading(cov, BR.rho, chiR, cv, pR)
                    cN, cR = [rN["I(W)"], rN["I(L2W)"]], [rR["I(W)"], rR["I(L2W)"]]
                    ok = cN == row["count"] == cR and rN["all"] and rR["all"]
                    agree_all = agree_all and ok
                    rec["rows"].append({"class": bname, "H order": row["order"], "banked": row["count"], "route N": cN,
                                        "route R": cR, "n((VL)*) N/R": [rN["n((VL)*)"], rR["n((VL)*)"]],
                                        "identities N/R": [rN["all"], rR["all"]], "ok": ok})
            out["members"].append(rec)
            print(name, mem["u"], mem["kappa"], "rows", len(rec["rows"]), "all ok", all(r["ok"] for r in rec["rows"]),
                  f"{time.time() - t0:.0f}s", flush=True)
    out["rows"] = sum(len(m["rows"]) for m in out["members"])
    out["generation-shaped rows reproduced"] = sum(1 for m in out["members"] for r in m["rows"]
                                                  if r["banked"][0] == r["banked"][1] != 0 and r["ok"])
    out["holds"] = agree_all
    out["seconds"] = round(time.time() - t0)
    print(json.dumps({k: v for k, v in out.items() if k != "members"}))
    if "--record" in sys.argv:
        (HERE / "k2.json").write_text(json.dumps(out, indent=1) + "\n")
    return out


if __name__ == "__main__":
    main()
