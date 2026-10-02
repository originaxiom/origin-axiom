"""B1514 -- post-run checks (run after both sealed routes; not predictions).  Record: post_run_checks_run.txt.

(a) M5's double point (w = 7) carries one interior 10' (n(W1*) = 1, a vector-like partner of one of the two 10bar').  Does the 10'
    coupling, non-zero there (P4), survive on that interior class?  Both routes: B(f_int, f) for f in a basis of H^1(W1*) and f_int,
    and separately the self-coupling B(f_int, f_int), the only one among normalizable 10' zero modes (added after the first run of
    this script; disclosed in FINDINGS Section 7).
(b) Lemma 2's mechanism directly (route L): the image of H^1(V) in H^1(W1) has rank h^1(W1) at the first member of every group.
(c) The other order, W2 = [[L, delta V], [0, V]] with delta a class of Hom(V, L) = V_eta* (B1511's W2; banked I(W2) = -1, a chiral
    10').  The dual sub-wedge argument: W2* has V* as a sub, so the 10' classes of W2 live in V* and their wedge factors through
    H^2(Lambda^2 V*), which vanishes when Lambda^2 V is acyclic (duality).  Checked by both routes at one member of every group:
    the chiral 10' of W2 does not couple to any 5'_H of W2.
(d) Where P4's non-zero 10' couplings sit (from the two records)."""
import json
import sys
import time
from pathlib import Path

import numpy as np
import sympy as sp
from sympy.polys.matrices import DomainMatrix

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import law_lib as LT  # noqa: E402
import lift_route as LR  # noqa: E402
import census as CT  # noqa: E402

H, T = LT.H, LT.T
IA = LR.IA
RECORD = HERE / "post_run_checks_run.txt"


# ============================================================================================ W2, route T
def w2_T(mem):
    """W2 = [[L, delta V], [0, V]], delta a cocycle of V_eta* (row vector), route T"""
    G, dom = mem.G, mem.dom
    Ed = mem.Veta.dual()
    ds, _ = H.h1_basis(Ed)
    d = ds[0]
    mats = {}
    for g in G.gens:
        Lg = DomainMatrix([[mem.Lv[g]]], (1, 1), dom)
        top = Lg.hstack(d.v[g].transpose() * mem.V.rep.M[g])
        bot = DomainMatrix.zeros((4, 1), dom).hstack(mem.V.rep.M[g])
        mats[g] = top.vstack(bot)
    W2 = H.Module(G, mats)
    assert W2.check()
    return W2


def w2_L(mem):
    F = mem.F
    Ed = mem.Veta.dual()
    _, D0, D1 = IA.cohomology(Ed)
    d = IA.h1_basis(Ed, D0, D1)[0]
    dv = IA.values(F, d, 4)
    mats = {}
    for k in IA.GENS:
        Lg = mem.L.g[k][0]
        top = F.hstack([Lg, F.mul(F.T(dv[k]), mem.V.g[k][0])])
        bot = F.hstack([F.zeros(4, 1), mem.V.g[k][0]])
        mats[k] = F.vstack([top, bot])
    W2 = IA.Rep(F, mem.n, mats)
    assert W2.relators_hold()
    return W2


# ============================================================================================ (a) the interior 10' at w = 7
def interior_10_T(G, C, z, mem):
    ints = H.interior_classes(mem.W1d)
    hs, _ = H.h1_basis(mem.L2W)
    fs, _ = H.h1_basis(mem.W1d)
    form = H.form_wedge(5)
    dom = mem.dom
    vals, self_vals = [], []
    for (fint, _lift) in ints:
        for f in fs + [fint]:
            for h in hs:
                vals.append(H.triple(G, C, z, h, fint, f, form))
        self_vals.append([H.triple(G, C, z, h, fint, fint, form) != dom.zero for h in hs])
    return {"interior 10' classes": len(ints), "Higgs": len(hs),
            "coupling of the interior 10' (with itself and every 10') non-zero": any(v != dom.zero for v in vals),
            "self-coupling B(f_int, f_int) non-zero, per 5'_H": self_vals}


def interior_vectors_L(rep):
    """a basis of the interior subspace of H^1(rep), as cocycle columns"""
    F, d = rep.F, rep.d
    As = LR.basis(rep)
    I = F.eye(d)
    BP = F.vstack([F.sub(rep.g["t"][0], I), F.sub(rep.w(IA.ELL), I)])
    cols = [F.vstack([IA.values(F, a, d)["t"], LR.cocycle_on_word(rep, IA.values(F, a, d), IA.ELL)]) for a in As]
    M = F.hstack(cols + [BP])
    out = []
    for v in F.nullspace(M):
        coeffs = [F.tolist(v)[i][0] for i in range(len(As))]
        if all(F.zero_scalar(c) for c in coeffs):
            continue
        comb = None
        for cf, a in zip(coeffs, As):
            term = F.smul(cf, a)
            comb = term if comb is None else F.add(comb, term)
        out.append(comb)
    return out, As


def interior_10_L(mem):
    F = mem.F
    ints, As = interior_vectors_L(mem.W1d)
    Nw = IA.N_wedge(F)
    nonzero, self_nonzero = False, []
    for fi in ints[:1]:
        for f in As + [fi]:
            ok, vals, _ = LR.class_test(mem.L2Wd, mem.W1d, Nw, IA.values(F, fi, 5), IA.values(F, f, 5))
            assert ok, "the block checks of the lifting criterion failed"
            nonzero = nonzero or any(not F.zero_scalar(v) for v in vals)
        ok, vals, _ = LR.class_test(mem.L2Wd, mem.W1d, Nw, IA.values(F, fi, 5), IA.values(F, fi, 5))
        assert ok, "the block checks of the lifting criterion failed"
        self_nonzero.append(any(not F.zero_scalar(v) for v in vals))
    return {"interior 10' classes (spanning set)": len(ints), "coupling of the interior 10' non-zero": nonzero,
            "self-class [f_int ^ f_int] non-zero in H^2(Lambda^2 W1*)": self_nonzero}


# ============================================================================================ (b) Lemma 2's mechanism, route L
def lemma2_L(mem):
    F = mem.F
    Vb = LR.basis(mem.V)
    _, D0W, _ = IA.cohomology(mem.W1)
    pushed = []
    for a in Vb:
        av = IA.values(F, a, 4)
        pushed.append(F.vstack([F.vstack([av[k], F.zeros(1, 1)]) for k in IA.GENS]))
    rk = F.rank(F.hstack([D0W] + pushed)) - F.rank(D0W) if pushed else 0
    return {"h1(V)": len(Vb), "rank of H^1(V) -> H^1(W1)": rk, "h1(W1)": LR.h_data(mem.W1)["h1"],
            "isomorphism": rk == len(Vb) == LR.h_data(mem.W1)["h1"]}


# ============================================================================================ (c) W2's chiral 10'
def w2_coupling_T(G, C, z, mem):
    W2 = w2_T(mem)
    W2d = W2.dual()
    tens, nh, na = LT.coupling_tensor(G, C, z, W2.wedge2(), W2d, H.form_wedge(5))
    return {"h1(W2)": H.h1_basis(W2)[1], "h1(W2*)": na, "Higgs 5'_H of W2": nh, "the 10' coupling of W2 is zero": LT.all_zero(tens, mem.dom)}


def w2_coupling_L(mem):
    W2 = w2_L(mem)
    W2d = W2.dual()
    tab = LR.wedge_table(W2d.wedge2(), W2d)
    return {"h1(W2)": LR.h_data(W2)["h1"], "h1(W2*)": tab["dim H^1(slot)"], "the 10' coupling of W2 is zero": tab["zero"]}


def main():
    t0 = time.time()
    out = {"a": {}, "b": {}, "c": {}}
    pops = LT.populations()
    cache = {}
    for pop in pops:
        n = pop["level"]
        if n not in cache:
            G = H.FibredGroup(n)
            cache[n] = (G,) + G.fundamental()[:2]
        G, C, z = cache[n]
        orders = sorted({LT.reduce_char(ab, pop["N"])[1] for o in pop["orbits"].values() for ab in o}) + ([4] if "i" in pop["lam"] else [])
        (p, roots), = CT.primes_with_roots(pop["factor"], orders, 1, 2 ** 23 - 3 * 104729 - 17 * n)
        iota = T.gf_root_of_unity(p, 4) if "i" in pop["lam"] else None
        r = roots[0]
        field = T.Field("gf", p=p, r=r, iota=iota)
        rho = H.rho_mats(G, field)
        ab = next(iter(pop["orbits"].values()))[0]
        mT = LT.Member(G, field, rho, ab, pop["N"], LT.lam_value(field, pop["lam"]))
        F = IA.ModP(p, "post")
        (_, _), Nr = LR.reduce_char(ab, pop["N"])
        lamL = {"1": 1, "-1": p - 1, "i": iota, "-i": (p - iota) % p if iota else None}[pop["lam"]]
        mL = LR.Member(F, IA.mn_mats(F, r), n, ab, pop["N"], lamL, LR.root_of_unity(p, Nr))
        if n == 5 and pop["lam"] == "1":
            out["a"][pop["label"]] = {"route T": interior_10_T(G, C, z, mT), "route L": interior_10_L(mL), "p": p, "q": r}
        out["b"][pop["label"]] = lemma2_L(mL)
        out["c"][pop["label"]] = {"route T": w2_coupling_T(G, C, z, mT), "route L": w2_coupling_L(mL), "p": p, "q": r}
        print(f"[{time.time() - t0:7.1f}s] {pop['label']} done", flush=True)
    # (d) where the non-zero 10' couplings sit
    rT = json.loads((HERE / "census_run.txt").read_text(encoding="utf-8"))
    d = {}
    for blk in rT["A"]:
        for row in blk["rows"]:
            key = blk["population"]
            d.setdefault(key, set()).add((row["10' B"]["zero"], row["interior"]["W1*"], row["10' B"]["higgs"]))
    out["d"] = {k: [{"10' coupling zero": z_, "interior 10'": n_, "Higgs": h_} for (z_, n_, h_) in sorted(v)] for k, v in d.items()}
    out["summary"] = {
        "(a) the interior 10' at w = 7 couples (both routes)": [v["route T"]["coupling of the interior 10' (with itself and every 10') non-zero"]
                                                               and v["route L"]["coupling of the interior 10' non-zero"] for v in out["a"].values()],
        "(a) routes agree": all(v["route T"]["coupling of the interior 10' (with itself and every 10') non-zero"]
                                == v["route L"]["coupling of the interior 10' non-zero"] for v in out["a"].values()),
        "(a) the self-coupling B(f_int, f_int): route T, any 5'_H": [any(r) for v in out["a"].values()
                                                                     for r in v["route T"]["self-coupling B(f_int, f_int) non-zero, per 5'_H"]],
        "(a) the self-coupling: routes agree": all([any(r) for r in v["route T"]["self-coupling B(f_int, f_int) non-zero, per 5'_H"]]
                                                   == v["route L"]["self-class [f_int ^ f_int] non-zero in H^2(Lambda^2 W1*)"]
                                                   for v in out["a"].values()),
        "(b) H^1(V) -> H^1(W1) is an isomorphism at every group": all(v["isomorphism"] for v in out["b"].values()),
        "(c) W2's chiral 10' decouples at every group (both routes)": all(v["route T"]["the 10' coupling of W2 is zero"]
                                                                           and v["route L"]["the 10' coupling of W2 is zero"] for v in out["c"].values()),
        "(c) routes agree on W2": all(v["route T"]["the 10' coupling of W2 is zero"] == v["route L"]["the 10' coupling of W2 is zero"]
                                      and v["route T"]["h1(W2*)"] == v["route L"]["h1(W2*)"] for v in out["c"].values()),
    }
    out["seconds"] = round(time.time() - t0, 1)
    if "--record" in sys.argv:
        RECORD.write_text(json.dumps(out, indent=1, sort_keys=True, default=str) + "\n", encoding="utf-8")
    print(json.dumps(out["summary"], indent=1))
    return out


if __name__ == "__main__":
    main()
