"""B1299 (c): the subregular sl2 (weighted Dynkin (2,2,2,0,2,2), B1256's I-25 candidate) on B1296's E6: e6 decomposed by the
h-eigenvalue multiset; the 27 likewise; the outer involution at that point fixes sp(8) (principal-sl2 content V2 V6 V10 V14,
C4's exponents 1,3,5,7 -- cited) with complement 42; B1298's exact signs eps_S(k) = (-1)^(k/2+1) on each H^1(M; Sym^k) give
iota*; the mismatch set theta' != iota* on the eight tangent directions is computed.  DESIGN Q2: exactly one, the V10 of the 42."""
import os, sys, json, itertools
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "B1298_the_lift_fork", "verification"))
from e6_rational import *
from fractions import Fraction as Fr
def decompose(eigs):
    """multiset of integer h-eigenvalues of an sl2-rep -> highest weights (each V_{2m} has weights -2m..2m step 2)"""
    from collections import Counter
    c = Counter(eigs); hw = []
    for e in sorted(c, reverse=True):
        if e < 0: break
        n = c[e] - c.get(e + 2, 0)
        hw += [e] * n
    return sorted(hw, reverse=True)
def weighted(labels):
    def h(v): return sum(Fr(l) * dot(v, omega[k]) for k, l in enumerate(labels))
    return h
best = None
for perm in itertools.permutations(range(6)):
    labels = [(2, 2, 2, 0, 2, 2)[perm[k]] for k in range(6)]
    h = weighted(labels)
    e_adj = [int(h(r)) for r in roots] + [0] * 6
    e27 = [h(wv) for wv in W27]
    if any(x != int(x) for x in e27): continue
    hw = decompose(e_adj); hw27 = decompose([int(x) for x in e27])
    if hw == [16, 14, 10, 10, 8, 6, 4, 2] and hw27 == [12, 8, 4]:
        best = (labels, hw, hw27); break
labels, hw, hw27 = best
print("subregular labelling on B1296's simple roots (Bourbaki order):", labels)
print("e6 under the subregular sl2: V_k for k =", hw, " dims", [k + 1 for k in hw], " sum", sum(k + 1 for k in hw))
print("27 under it: V_k for k =", hw27, " dims", [k + 1 for k in hw27], " (B1256: 13 + 9 + 5)")
# the outer involution at this point fixes sp(8) = C4, whose principal sl2 has exponents 1,3,5,7 -> V2 V6 V10 V14 (dim 3+7+11+15 = 36)
sp8 = [2, 6, 10, 14]; rest = sorted(hw, reverse=True)
for k in sp8: rest.remove(k)
print("theta' fixed algebra sp(8): V_k, k =", sp8, " dim", sum(k + 1 for k in sp8), "; complement (the 42): V_k, k =", rest, " dim", sum(k + 1 for k in rest))
assert sum(k + 1 for k in sp8) == 36 and sum(k + 1 for k in rest) == 42
# the tangent space at the subregular point: one H^1(M; Sym^k) per summand (h^1 = 1 for even k, B1256/B1267/B1298)
eps_S = {k: (1 if (k // 2 + 1) % 2 == 0 else -1) for k in range(0, 24, 2)}      # B1298, exact
tangent = [(k, "sp(8)", +1) for k in sp8] + [(k, "42", -1) for k in rest]
mism = [(k, part) for k, part, th in tangent if eps_S[k] != th]
print("\ntangent directions (k, part, theta', iota*):")
for k, part, th in sorted(tangent): print(f"   V{k:<3d} {part:6s} theta' = {th:+d}   iota* = {eps_S[k]:+d}   {'MISMATCH' if eps_S[k] != th else ''}")
print("\nmismatch set theta' != iota*:", mism, " count", len(mism))
ok = (mism == [(10, "42")])
json.dump(dict(labels=labels, e6=hw, w27=hw27, sp8=sp8, rest=rest, mismatch=mism), open("b1299_subregular.json", "w"), indent=1)
print("Q2:", "PASS" if ok else "FAIL")
