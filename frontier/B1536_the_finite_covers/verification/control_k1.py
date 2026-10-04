#!/usr/bin/env python3
"""B1536 control K1 (banked identity, on banked data only): the levels M_n (n = 2, 3, 4) read AS BASES, at every lambda = 1
member, on every finite abelian cover cut out by a subgroup B of the cusp-trivial characters -- sm:B1532's sealed population --
by route N (and route R for n = 2, 3).  The census histogram of counts must equal sm:B1532's banked one, level by level (it does
not depend on how the characters are labelled, so the two benches' different presentations do not matter).

    python3 control_k1.py [--levels 2 3 4 6] [--route-r-levels 2 3] [--cap 6 4] [--record [--out k1.json]]

--cap n m reads only the subgroups B of order <= m on level n (and the banked histogram restricted the same way); two-class
members (M6) are read at the interior class and at a generic class, as sm:B1532's census reads them (not at special classes).
Route R reads the one-class members only; its histogram is compared with the banked one at those members (class "c1").
On M2 and M3 every member has one class; on M6 the first run compared it with the whole histogram (disclosed in
PREREGISTRATION section 6; k1_m6_check.py re-reads that run's recorded histograms)."""
import gzip
import itertools
import json
import sys
import time
import warnings
from collections import Counter
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

B1532V = ROOT / "frontier" / "B1532_three_from_the_cusps" / "verification"


def _b1532_read_out():
    """sm:B1532's read_out.py, loaded by its path under its own module name. This arc has a read_out.py too: in a process
    that has already imported it (identity.py does, through read_out_selftest.py), a bare 'import read_out' returns this
    arc's module from the cache, and K1 failed there (PREREGISTRATION_ADDENDUM.md)."""
    import importlib.util
    name = "b1532_read_out"
    if name not in sys.modules:
        spec = importlib.util.spec_from_file_location(name, B1532V / "read_out.py")
        mod = importlib.util.module_from_spec(spec)
        sys.modules[name] = mod
        spec.loader.exec_module(mod)
    return sys.modules[name]


def banked_hist(levels, tmp, cap=None):
    """sm:B1532's census histogram (route T's terms), keys (n, class, W, L2); with cap, only the subgroups of order <= cap[n]
    and only the classes c1, int and gen (the special classes are not read by this control)"""
    RO = _b1532_read_out()
    path = tmp / "terms_T.jsonl"
    if not path.exists():
        with gzip.open(B1532V / "terms_T.jsonl.gz", "rb") as src, open(path, "wb") as dst:
            dst.write(src.read())
    Rt = RO.Route("T", RO.load(path))
    cap = cap or {}
    subs = {n: [B for B in RO.subgroups(sorted(Rt.chars[n])) if n not in cap or len(B) <= cap[n]] for n in Rt.levels}
    hist, shaped = Rt.census(subs)
    return Counter({k: v for k, v in hist.items() if k[0] in levels and k[1] in ("c1", "int", "gen")}), \
        {n: len(subs[n]) for n in levels}, {n: len(Rt.members[n]) for n in levels}


def closure(gens):
    zero = (Fr(0), Fr(0))
    S, todo = {zero}, [zero]
    while todo:
        x = todo.pop()
        for g in gens:
            y = ((x[0] + g[0]) % 1, (x[1] + g[1]) % 1)
            if y not in S:
                S.add(y)
                todo.append(y)
    return frozenset(S)


def all_subgroups(elems):
    cyc = {}
    for g in elems:
        cyc.setdefault(closure([g]), g)
    out = set(cyc)
    for g1, g2 in itertools.combinations(list(cyc.values()), 2):
        out.add(closure([g1, g2]))
    return sorted(out, key=lambda s: (len(s), sorted(s)))


def abelian_cover(B):
    """the right action of Gamma_n on A = image of g -> (chi(g))_{chi in B}: x^g = x + psi(g); chi(a) = u_a, chi(b) = u_b,
    chi(t) = 0 (lambda = 1)"""
    Bl = sorted(B)
    psi = {"a": tuple(c[0] for c in Bl), "b": tuple(c[1] for c in Bl), "t": tuple(Fr(0) for _ in Bl)}
    zero = tuple(Fr(0) for _ in Bl)
    pts, idx, todo = [zero], {zero: 0}, [zero]
    while todo:
        x = todo.pop()
        for g in "abt":
            for s in (1, -1):
                y = tuple((xi + s * gi) % 1 for xi, gi in zip(x, psi[g]))
                if y not in idx:
                    idx[y] = len(pts)
                    pts.append(y)
                    todo.append(y)
    perms = {g: [idx[tuple((xi + gi) % 1 for xi, gi in zip(x, psi[g]))] for x in pts] for g in "abt"}
    return perms


def main():
    args = sys.argv[1:]

    def ints_after(flag, default):
        if flag not in args:
            return default
        out = []
        for x in args[args.index(flag) + 1:]:
            if x.startswith("--"):
                break
            out.append(int(x))
        return out
    levels = [n for n in ints_after("--levels", [2, 3, 4]) if n in (2, 3, 4, 5, 6)]
    rr = ints_after("--route-r-levels", [2, 3])
    capl = ints_after("--cap", [])                       # pairs: level, max order of B
    cap = {capl[i]: capl[i + 1] for i in range(0, len(capl), 2)}
    tmp = Path("/tmp") / "b1536_k1"
    tmp.mkdir(exist_ok=True)
    t0 = time.time()
    banked, nsub_b, nmem_b = banked_hist(levels, tmp, cap)
    out = {"levels": levels, "route R levels": rr, "per level": {}}
    pN = gf.primes_1_mod(120, N.P_BOUND, 1)[0]
    pR = gf.primes_1_mod(120, 1 << 31, 1)[0]
    FN, FR = gf.GF(pN, 120), gf.GF(pR, 120)
    for n in levels:
        st = CL.state("+" + "LR" * n)
        chars = [tuple(Fr(x) for x in u) for u in st["fibre characters"]]
        subs = [B for B in all_subgroups(chars) if n not in cap or len(B) <= cap[n]]
        BN, BR = N.Base(st, FN), N.Base(st, FR)
        hN, hR, bad = Counter(), Counter(), []
        for u in chars:
            chiN, chiR = BN.character(u, Fr(0)), BR.character(u, Fr(0))
            # the base class, each route by its own elimination
            pa1 = N.perm_arrays(BN.G, {"a": [0], "b": [0], "t": [0]})
            VetaN = N.tensor(BN, N.small_four(BN, chiN, 5), pa1)
            classes = N.base_classes(BN, VetaN)            # {"c1": z} or {"int": z, "gen": z}
            for B in subs:
                perms = abelian_cover(B)
                assert CL.check_cover(BN.G, perms)
                pa = N.perm_arrays(BN.G, perms)
                d = len(perms["a"])
                for cname, z in classes.items():
                    cz = {g: z[gi * 4:(gi + 1) * 4] for gi, g in enumerate(BN.gens)}
                    rN = N.reading(BN, pa, chiN, {g: [cz[g]] * d for g in BN.gens})
                    hN[(n, cname, rN["I(W)"], rN["I(L2W)"])] += 1
                    if not rN["all"]:
                        bad.append(("N", n, [str(x) for x in u], len(B), cname))
                if n in rr and len(classes) == 1:
                    VetaR = {g: BR.rho[g] * pow(int(chiR[g]), 5, pR) % pR for g in BR.gens}
                    c0R = R.base_cocycle(BR.G, VetaR, pR)
                    cov = R.PCover(BR.G, perms)
                    cv = R.cocycle_on_words(BR.G, VetaR, c0R, cov.sword, pR)
                    rR = R.reading(cov, BR.rho, chiR, cv, pR)
                    hR[(n, "c1", rR["I(W)"], rR["I(L2W)"])] += 1
                    if not rR["all"]:
                        bad.append(("R", n, [str(x) for x in u], len(B)))
                    if (rR["I(W)"], rR["I(L2W)"]) != (rN["I(W)"], rN["I(L2W)"]):  # one-class: rN is c1's
                        bad.append(("N != R", n, [str(x) for x in u], len(B)))
        bk = Counter({k: v for k, v in banked.items() if k[0] == n})
        rec = {"members": len(chars), "banked members": nmem_b[n], "subgroups": len(subs), "banked subgroups": nsub_b[n],
               "subgroup order cap": cap.get(n),
               "route N histogram": {str(k[1:]): v for k, v in sorted(hN.items())},
               "banked histogram": {str(k[1:]): v for k, v in sorted(bk.items())},
               "route N = banked": hN == bk, "failures": bad}
        if n in rr:
            rec["route R histogram"] = {str(k[1:]): v for k, v in sorted(hR.items())}
            # route R reads the one-class members only, so it is compared with the banked histogram at their class "c1"
            rec["route R = banked"] = hR == Counter({k: v for k, v in bk.items() if k[1] == "c1"})
        out["per level"][str(n)] = rec
        print(n, json.dumps({k: v for k, v in rec.items() if "histogram" not in k}), f"{time.time() - t0:.0f}s", flush=True)
    out["holds"] = all(r["route N = banked"] and r.get("route R = banked", True) and not r["failures"]
                       for r in out["per level"].values())
    out["primes"] = {"route N": pN, "route R": pR}
    out["seconds"] = round(time.time() - t0)
    print(json.dumps({"holds": out["holds"], "seconds": out["seconds"]}))
    if "--record" in sys.argv:
        name = args[args.index("--out") + 1] if "--out" in args else "k1.json"
        (HERE / name).write_text(json.dumps(out, indent=1) + "\n")
    return out


if __name__ == "__main__":
    main()
