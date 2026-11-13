#!/usr/bin/env python3
"""The paired current pole on main, step 5 at the level of roots (P-749 (e)): which products of a charged-vector
component with a down component are not zero, in the module (16, 4) and in its conjugate.

MAIN'S OWN E8: the 240 roots as vectors of length^2 2 in eight coordinates: +-e_i +- e_j, and (+-1/2)^8 with an even
number of minus signs.  D5 on coordinates 1..5, A3 = D3 on 6..8.  Then (16, 4) is the half-integer roots with an even
number of minus signs in 1..5 (and so in 6..8), its conjugate those with an odd number; (10, 6) is +-e_i +- e_j, i <= 5 < j.
THE TWO Spin5: on coordinates (1, 2) and (3, 4); coordinate 5 is the direction neither rotates.  The principal grades
are m = 2 x1 + x2 and n = 2 x3 + x4: on the spinor (+-1/2, +-1/2) they are 3/2, 1/2, -1/2, -3/2, each once, so a pair
(m, n) names one weight of (4, 4); on the vector they are 2, 1, 0, -1, -2.
THE STATEMENT CHECKED (the lane's section 4 and 4a, read through the binding-minimum mask): with the vector on the
grade -2 plane, components a at (-3/2, -1/2) and b at (-1/2, -3/2), and the down pair u' at (-3/2, +3/2), v' at
(+3/2, -3/2), the product has exactly two components, "C b d_u and C a d_v", at grades (-2, 0) and (0, -2), the up
pair; and the same in the conjugate module.
WHAT IS USED AND NOT PROVED: in a simply-laced algebra [e_alpha, e_beta] = +-e_(alpha+beta) when alpha + beta is a root
and 0 otherwise, in a basis where every root vector has the same length.  So the size is common; what is computed is
WHICH sums are roots.
HOW IT COULD FAIL: a count of roots or of a module; a pair (m, n) naming two weights; a third non-zero product; the
conjugate module differing; the planted case, the two factors with the same A3 weight, must give no product."""
import itertools, json, pathlib
from fractions import Fraction as Fr
CHECKS = []
def check(name, ok, detail=""):
    CHECKS.append({"check": name, "holds": bool(ok), "detail": str(detail)[:300]}); print("%s  %s%s" % ("ok  " if ok else "FAIL", name, ("  [%s]" % str(detail)[:220]) if detail else ""))
h = Fr(1, 2)
roots = set()
for i, j in itertools.combinations(range(8), 2):
    for si, sj in itertools.product((1, -1), repeat=2):
        v = [Fr(0)] * 8; v[i] = Fr(si); v[j] = Fr(sj); roots.add(tuple(v))
for s in itertools.product((1, -1), repeat=8):
    if sum(1 for x in s if x < 0) % 2 == 0: roots.add(tuple(h * x for x in s))
check("240 roots, each of length^2 2", len(roots) == 240 and all(sum(x * x for x in r) == 2 for r in roots))
spin = [r for r in roots if r[0].denominator == 2]
m164 = [r for r in spin if sum(1 for x in r[:5] if x < 0) % 2 == 0]; bar = [r for r in spin if sum(1 for x in r[:5] if x < 0) % 2 == 1]
ten6 = [r for r in roots if r[0].denominator == 1 and sum(1 for x in r[:5] if x != 0) == 1 and sum(1 for x in r[5:] if x != 0) == 1]
check("(16, 4) and its conjugate have 64 roots each, (10, 6) has 60, and each is the other's negative where it should be", len(m164) == 64 == len(bar) and len(ten6) == 60 and {tuple(-x for x in r) for r in m164} == set(bar))
grade = lambda r: (2 * r[0] + r[1], 2 * r[2] + r[3])
a3 = lambda r: r[5:]
def run(module, name):
    by = {}
    for r in module: by.setdefault((grade(r), a3(r)), []).append(r)
    check("%s: a pair of grades and an A3 weight name exactly one root, and the grades are the 16 pairs of V(3/2) x V(3/2)" % name,
          all(len(v) == 1 for v in by.values()) and {g for g, _ in by} == {(Fr(p, 2), Fr(q, 2)) for p in (3, 1, -1, -3) for q in (3, 1, -1, -3)})
    z = {"a": (Fr(-3, 2), Fr(-1, 2)), "b": (Fr(-1, 2), Fr(-3, 2))}; d = {"u'": (Fr(-3, 2), Fr(3, 2)), "v'": (Fr(3, 2), Fr(-3, 2))}
    weights = sorted({a3(r) for r in module}); out = {}; same = 0
    for wz, wd in itertools.product(weights, repeat=2):
        for (zn, zg), (dn, dg) in itertools.product(z.items(), d.items()):
            s = tuple(x + y for x, y in zip(by[(zg, wz)][0], by[(dg, wd)][0]))
            if s in roots:
                if wz == wd: same += 1
                out.setdefault((zn, dn), set()).add((grade(s), s in ten6))
    pat = {k: sorted(v) for k, v in out.items()}
    check("%s: the non-zero products are exactly a with v' at grades (0, -2) and b with u' at (-2, 0), both in (10, 6), for every pair of different A3 weights" % name,
          pat == {("a", "v'"): [((Fr(0), Fr(-2)), True)], ("b", "u'"): [((Fr(-2), Fr(0)), True)]}, {"%s x %s" % k: [(str(g[0]), str(g[1]), t) for g, t in v] for k, v in pat.items()})
    n_pairs = sum(1 for wz, wd in itertools.product(weights, repeat=2) if wz != wd and tuple(x + y for x, y in zip(by[(z["a"], wz)][0], by[(d["v'"], wd)][0])) in roots)
    check("%s: and that for all 12 ordered pairs of different A3 weights; planted: with the same A3 weight no product is a root" % name, n_pairs == 12 and same == 0, "%d pairs; %d with equal weights" % (n_pairs, same))
    return pat
p1 = run(m164, "(16, 4)"); p2 = run(bar, "the conjugate module")
check("the two modules have the same pattern of non-zero products", p1 == p2)
if __name__ == "__main__":                              # the write only when run, never when a lock loads it
    json.dump({"checks": CHECKS, "failing": [c["check"] for c in CHECKS if not c["holds"]]}, open(pathlib.Path(__file__).with_suffix(".json"), "w"), indent=1)
    print("\n%d checks, %d failing" % (len(CHECKS), sum(1 for c in CHECKS if not c["holds"])))
