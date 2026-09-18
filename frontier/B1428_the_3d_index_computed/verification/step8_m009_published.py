"""
Step 8.  A SECOND independently published series: m009.

SOURCE: GHRS, "The 3D-index and normal surfaces", Illinois J. Math. 60 (2016),
Section 11.5 "m009" (p.331-332), local text ghrs_normal_surfaces.txt l.1938-2000.
Verbatim:

  "I_even(2x mu + 2y lam) = sum_{k1,k2} q^{k1+k2} J_D(-y, 2k1-x, 2k2)
                                  J_D(y, k2+x, 2k1-x) J_D(-2y, k2, 2k1-x+y)"
  "I_even(0,0) = 1 - q - q^2 + 6q^3 + 9q^4 + 12q^5 - 5q^6 - 34q^7
                   - 79q^8 - 118q^9 - 118q^10 + ...".

m009 has non-peripheral Z/2Z homology, so GHRS split the index into an 'even'
and an 'odd' part; the 'even' part is exactly the sum over INTEGER edge weights
(0,k1,k2), i.e. exactly what my general driver computes.
"""
import sys
from tet_index import s_str, s_mul, s_add, s_shift, s_trunc, s_eq
from step7_fixed_gluing import J_mindeg, J_normalised, index_zero

X = int(sys.argv[1]) if len(sys.argv) > 1 else 30
CUT = X - 6

PUB = {0:1, 2:-1, 4:-1, 6:6, 8:9, 10:12, 12:-5, 14:-34, 16:-79, 18:-118, 20:-118}


def term(triples, Xmax):
    D = sum(J_mindeg(*t) for t in triples)
    if D > Xmax:
        return None, D
    budget = Xmax - D
    p = {0: 1}
    for t in triples:
        p = s_mul(p, J_normalised(*t, budget=budget), budget)
    return s_shift(p, D, Xmax), D


print("=" * 78)
print("STEP 8: m009 against GHRS Section 11.5")
print("=" * 78)

# ---- GHRS's own closed form, x=y=0, written out by hand from the paper
print("\n[A] GHRS closed form  sum_{k1,k2} q^{k1+k2} J(0,2k1,2k2) J(0,k2,2k1) J(0,k2,2k1):")
tot = {}
B = 40
kept = 0
outer = 0
for k1 in range(-B, B + 1):
    for k2 in range(-B, B + 1):
        triples = [(0, 2 * k1, 2 * k2), (0, k2, 2 * k1), (0, k2, 2 * k1)]
        D0 = 2 * (k1 + k2) + sum(J_mindeg(*t) for t in triples)
        if D0 > X:
            continue
        kept += 1
        outer = max(outer, abs(k1), abs(k2))
        budget = X - D0
        p = {0: 1}
        for t in triples:
            p = s_mul(p, J_normalised(*t, budget=budget), budget)
        tot = s_add(tot, s_shift(p, D0, X))
print(f"    {kept} lattice points, outermost |k|={outer} (box +-{B})")
print("    closed form :", s_str(tot, CUT))
ok1 = {k: v for k, v in s_trunc(tot, 20).items() if v} == {k: v for k, v in PUB.items() if v}
print(f"    matches the published I_even(0,0) through q^10: {ok1}")

# ---- my general snappy-driven driver
print("\n[B] my general driver on snappy's m009 (all three edge choices):")
sers = []
for z in range(3):
    s, npts, mx = index_zero("m009", X, zero_edge=z)
    sers.append(s)
    ok = {k: v for k, v in s_trunc(s, 20).items() if v} == {k: v for k, v in PUB.items() if v}
    print(f"    zero_edge={z} ({npts} pts): matches published: {ok}")
    print(f"       {s_str(s, CUT)}")
print(f"    all three agree with each other: {all(s_eq(sers[0], t, CUT) for t in sers)}")
print(f"    driver == GHRS closed form: {s_eq(sers[0], tot, CUT)}")
