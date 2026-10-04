#!/usr/bin/env python3
"""The golden covers dossier, section 6: structure only (no twisted cohomology).

  Part 1  the traces of m004 and m003 (SnapPy's ManifoldHP holonomy, every word of length <= 4 in the generators and their
          inverses): each trace's minimal polynomial by PARI's algdep (degree <= 2).  All monic over Z with discriminant -3
          times a square means: trace field = invariant trace field = Q(sqrt -3), integral traces, so each group is derived from
          M_2(Q(sqrt -3)) (Maclachlan-Reid ch. 8) and, Q(sqrt -3) having class number 1, conjugate into PSL(2, O_3).
  Part 2  H_1(N; Z) of sm:B1536's 28 covers of degree <= 12 with n(1) >= 1 and n(rho) >= 1 at the trivial character (its banked
          post_run_rooms.json): Reidemeister-Schreier from the permutation action, abelianised, PARI's matsnf; checked against
          b1 = #cusps + n(1) (half-lives-half-dies) on every cover.

    python3 gc_structure.py      (a few seconds)"""
import importlib.util
import itertools
import math
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
B1536V = ROOT / "frontier" / "B1536_the_finite_covers" / "verification"


def _load(alias, path):
    if str(B1536V) not in sys.path:
        sys.path.append(str(B1536V))
    spec = importlib.util.spec_from_file_location(alias, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[alias] = mod
    spec.loader.exec_module(mod)
    return mod


def part1():
    import snappy
    from cypari import pari
    pari.set_real_precision(60)
    print("Part 1: the traces (words of length <= 4)")
    for name in ("m004", "m003"):
        G = snappy.ManifoldHP(name).fundamental_group()
        gens = G.generators()
        polys = set()
        for n in range(1, 5):
            for w in itertools.product(gens + [g.upper() for g in gens], repeat=n):
                m = G.SL2C("".join(w))
                t = m[0, 0] + m[1, 1]
                z = pari(str(t.real()).replace(" ", "")) + pari("I") * pari(str(t.imag()).replace(" ", ""))
                polys.add(pari.algdep(z, 2))
        monic = all(int(pari.pollead(q)) == 1 for q in polys)
        discs = sorted({int(pari.poldisc(q)) for q in polys if int(pari.poldegree(q)) == 2})
        sq3 = all(d < 0 and d % 3 == 0 and math.isqrt(-d // 3) ** 2 == -d // 3 for d in discs)
        print(f"  {name}: {len(polys)} minimal polynomials; all monic over Z: {monic}; quadratic discriminants {discs}: all "
              f"-3 x a square: {sq3}")


def part2():
    from cypari import pari
    POP = _load("b1536_population_gcs", B1536V / "population.py")
    CL = POP.CL
    rooms = json.loads((B1536V / "post_run_rooms.json").read_text())
    print("Part 2: H_1 of the covers with n(1) >= 1 and n(rho) >= 1 at the trivial character (sm:B1536, banked)")
    for st in ("m004", "m003"):
        want = {x["cover"]: (x["n(1)"], x["n(rho)"], x["cusps"]) for x in rooms[st]["trivial character supplies"]
                if x["n(1)"] >= 1 and x["n(rho)"] >= 1}
        S = CL.state(st)
        G = S["G"]
        covs = dict(POP.covers(S))
        for cid in sorted(want, key=lambda c: (int(c[1:].split(".")[0]), c)):
            perms = covs[cid]
            P = CL.with_inverses(perms)
            d = len(perms[G.gens[0]])
            seen, tree, queue = {0}, set(), [0]
            for x in queue:
                for g in G.gens:
                    y = P[g][x]
                    if y not in seen:
                        seen.add(y)
                        tree.add((x, g))
                        queue.append(y)
                    z = P["_inv"][g][x]
                    if z not in seen:
                        seen.add(z)
                        tree.add((z, g))
                        queue.append(z)
            edges = [(x, g) for x in range(d) for g in G.gens if (x, g) not in tree]
            col = {e: i for i, e in enumerate(edges)}
            rows = []
            for x0 in range(d):
                for r in G.rels:
                    v, x = [0] * len(edges), x0
                    for c in r:
                        g = c.lower()
                        if c.islower():
                            if (x, g) in col:
                                v[col[(x, g)]] += 1
                            x = P[g][x]
                        else:
                            y = P["_inv"][g][x]
                            if (y, g) in col:
                                v[col[(y, g)]] -= 1
                            x = y
                    assert x == x0
                    rows.append(v)
            snf = [int(z) for z in pari.matsnf(pari.matrix(len(rows), len(edges), [c for r in rows for c in r]).mattranspose())]
            free = len(edges) - sum(1 for z in snf if z != 0)
            tors = sorted(z for z in snf if z not in (0, 1))
            n1, nr, cus = want[cid]
            print(f"  {st} {cid}: H_1 = Z^{free}{''.join(f' + Z/{t}' for t in tors)}; cusps {cus}, n(1) {n1}, n(rho) {nr}; "
                  f"b1 = cusps + n(1): {free == cus + n1}")


if __name__ == "__main__":
    import warnings
    warnings.filterwarnings("ignore")
    part1()
    part2()
