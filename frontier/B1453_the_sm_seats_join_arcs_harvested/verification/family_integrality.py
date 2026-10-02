#!/usr/bin/env python3
"""sm:B1390's side finding, with main's own code: which members of B1186's family of 112 have a non-integral trace
(hence are not arithmetic, hence not commensurable with m004).  tr(g^2) for words g of length <= 3 in the generators,
written as (m + n sqrt(-3))/2; an algebraic integer of Q(sqrt(-3)) has m, n integers of the same parity."""
import json, pathlib, itertools, math
import snappy
HERE = pathlib.Path(__file__).resolve().parent
def names():
    import glob
    p = glob.glob(str(HERE.parents[1] / "B1186_*" / "verification" / "family_census.json"))[0]; d = json.load(open(p))
    B = d["members_B"]; return [r["name"] if isinstance(r, dict) else r for r in B], [r["name"] if isinstance(r, dict) else r for r in d["members_A"]]
def witness(nm):
    M = snappy.ManifoldHP(nm); G = M.fundamental_group(); gens = G.generators(); s3 = math.sqrt(3.0)
    for L in (1, 2, 3):
        for w in itertools.product(gens, repeat=L):
            A = G.SL2C("".join(w)); t = complex((A * A).trace()); m, n = 2 * t.real, 2 * t.imag / s3
            if abs(m - round(m)) > 1e-9 or abs(n - round(n)) > 1e-9 or (round(m) - round(n)) % 2:
                return "".join(w), "tr(g^2) = (%s + %s sqrt(-3))/2" % (round(m, 6), round(n, 6))
    return None
if __name__ == "__main__":
    N, A = names(); bad = {}
    for nm in N:
        w = witness(nm)
        if w: bad[nm] = w
    print("members:", len(N), " with a non-integral trace among words of length <= 3:", len(bad))
    for k, v in bad.items(): print("   %-12s g = %-4s %s" % (k, v[0], v[1]))
    print("non-integral members among the regular-tetrahedral 77:", sorted(set(bad) & set(A)))
    json.dump(dict(members=len(N), regular=len(A), non_integral=bad), open(HERE / "family_integrality.json", "w"), indent=1)
