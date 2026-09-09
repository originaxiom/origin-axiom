"""B1275 -- THE E8 FAMILY MECHANISM, VERIFIED ON MAIN -- and the one step that is not.

Owner: "lets integrate three generations derivation in main, verify whats remains
unverified."  The SM-derivation seat's B1269 derives three generations from E8 > E6 x A2.
This arc rebuilds E8 FROM SCRATCH on main and checks every structural claim, then states
exactly which step remains object-unverified.

VERIFIED HERE, from a from-scratch E8 (240 roots: +-e_i +- e_j, and (+-1/2)^8 with an even
number of minus signs):
  * an A2 subsystem exists (6 roots) and its centraliser in E8 is E6 (72 roots);
  * the remaining roots number 162 = 6 x 27;
  * they fall into SIX classes of EXACTLY 27, labelled by their A2 weight;
  * SUM RULE 1: two roots of the SAME class NEVER sum to a root -- 0 occurrences;
  * SUM RULE 2: roots of DIFFERENT classes sum to a root 270 times per ordered pair for
    exactly the 12 ordered pairs of distinct classes WITHIN an orbit of three (the branch's
    "e_i + e_j = -e_l, the third index"); the remaining values are 432 for the 6 class-
    conjugate pairs and 27 for the 12 cross-orbit pairs;
  * THE FAMILY STRUCTURE: the order-3 Weyl rotation s_a s_b of A2 (order verified = 3)
    cycles the six classes in exactly TWO ORBITS OF THREE -- (27,3) and (27bar,3bar).

So the branching 248 = 78 + 8 + (27,3) + (27bar,3bar) and the family structure are REAL and
STANDARD, and the seat's arithmetic reproduces exactly.  This is the classic E8 > E6 x SU(3)
family mechanism, and the corpus now has it verified rather than cited.

WHAT REMAINS UNVERIFIED -- and it is the whole object-specific step:
  THAT THE OBJECT'S OWN ORDER-3 ELEMENT IS THIS A2 ROTATION.
Everything above is a fact about E8; nothing in it mentions m004.  The seat's claim is that
"the founding ratio g" (B1268's icosian construction) supplies the order-3 element, which is
NOT checked here and would require that construction to be rebuilt on main.

AND THE CHAIN THIS EXPOSES.  The corpus now has THREE order-3 structures:
  L3   the trinification Z/3 grading of the 27  (B305; 85 distinct gradings, B1264)
  L4   the commensurator's Eisenstein unit Z/3  (B302/B323)
  A2   the family rotation verified here
B1264 established that L3 and L4 act by the SAME omega of Q(sqrt-3) -- not merely both of
order 3 -- but that L3 -> L4 is still not a map that ACTS (85 candidate gradings).  If the
A2 family rotation is that same omega, three generations become object-supplied.  THAT is
the sharp open question, and it is far more concrete than "derive three generations".

TWO FENCES CARRIED FROM THE SOURCE SEAT, NOT RELAXED:
  * its own arc says THE BIT -- choosing the matter triplet, omega vs omegabar -- is
    "supplied by a CLOSING, not by the object", the same mirror-odd Z/2 the corpus has
    carried since B582;
  * and it reports N = 0 and the Yukawa forced to ZERO on the triplet.
So even if the object-specific step lands, the mechanism buys the COUNT and not the VALUES.

CONTROLS (MB12, both directions):
  * E8 is built from its own definition and its 240 roots counted, not imported;
  * the A2 is FOUND by search (dot = -1 and the sum a root), not hard-coded;
  * the centraliser is computed and checked to be 72, so "E6" is verified not assumed;
  * the Weyl rotation's ORDER is computed to be 3 before its orbits are read;
  * SUM RULE 2's full value census is reported, so the branch's single number 270 is placed
    in context rather than confirmed selectively.
"""
import itertools
from collections import Counter
from fractions import Fraction as F


def e8_roots():
    roots = []
    for i in range(8):
        for j in range(i + 1, 8):
            for si in (1, -1):
                for sj in (1, -1):
                    v = [F(0)] * 8
                    v[i], v[j] = F(si), F(sj)
                    roots.append(tuple(v))
    for s in itertools.product((1, -1), repeat=8):
        if s.count(-1) % 2 == 0:
            roots.append(tuple(F(x, 2) for x in s))
    return roots


dot = lambda u, v: sum(x * y for x, y in zip(u, v))


def decompose():
    roots = e8_roots()
    R = set(roots)
    for a in roots:
        for b in roots:
            s = tuple(x + y for x, y in zip(a, b))
            if dot(a, b) == -1 and s in R:
                A2 = {a, b, s} | {tuple(-x for x in v) for v in (a, b, s)}
                if len(A2) == 6:
                    E6 = set(r for r in roots if all(dot(r, t) == 0 for t in A2))
                    rest = [r for r in roots if r not in A2 and r not in E6]
                    return roots, R, a, b, A2, E6, rest
    raise RuntimeError("no A2 found")


def selftest():
    print("B1275 -- the E8 family mechanism, verified on main (selftest)")
    roots, R, a, b, A2, E6, rest = decompose()
    print(f"  [ctl ] E8 roots built from definition: {len(roots)} (must be 240)")
    assert len(roots) == 240
    print(f"  [find] A2 found by search: {len(A2)} roots; centraliser E6: {len(E6)} (must be 72)")
    assert len(A2) == 6 and len(E6) == 72
    print(f"  [dec ] remaining: {len(rest)} = 6 x 27? {len(rest) == 162}")
    assert len(rest) == 162

    cls = lambda r: (dot(r, a), dot(r, b))
    byc = {}
    for r in rest:
        byc.setdefault(cls(r), []).append(r)
    print(f"  [cls ] classes: {len(byc)}, sizes {sorted({len(v) for v in byc.values()})}")
    assert len(byc) == 6 and {len(v) for v in byc.values()} == {27}

    same = sum(1 for k in byc for u in byc[k] for v in byc[k]
               if tuple(x + y for x, y in zip(u, v)) in R)
    print(f"  [SR1 ] same-class pairs summing to a root: {same} (branch: 0)")
    assert same == 0

    keys = sorted(byc)
    diff = {}
    for k1 in keys:
        for k2 in keys:
            if k1 != k2:
                diff[(k1, k2)] = sum(1 for u in byc[k1] for v in byc[k2]
                                     if tuple(x + y for x, y in zip(u, v)) in R)
    cen = Counter(diff.values())
    print(f"  [SR2 ] different-class ordered pairs, full census: {dict(cen)}")
    assert cen[270] == 12, "270 must hold for the 12 within-orbit ordered pairs"

    def refl(al):
        n = dot(al, al)
        return lambda v: tuple(x - 2 * dot(v, al) / n * y for x, y in zip(v, al))
    sa, sb = refl(a), refl(b)
    rot = lambda v: sa(sb(v))
    u, n = a, 0
    while True:
        u = rot(u); n += 1
        if u == a:
            break
    print(f"  [ctl ] order of the Weyl rotation s_a s_b: {n} (must be 3)")
    assert n == 3

    perm = {k: cls(rot(byc[k][0])) for k in keys}
    seen, orbits = set(), []
    for k in keys:
        if k in seen:
            continue
        o, x = [k], perm[k]
        while x != k:
            o.append(x); seen.add(x); x = perm[x]
        seen.add(k); orbits.append(o)
    print(f"  [FAM ] orbits of the order-3 rotation on the six classes: sizes "
          f"{sorted(len(o) for o in orbits)}  (branch: TWO ORBITS OF THREE)")
    assert sorted(len(o) for o in orbits) == [3, 3]

    print("\n  => the E8 > E6 x A2 family mechanism is VERIFIED on main, end to end.")
    print("     WHAT IS NOT: that the OBJECT'S own order-3 element is this A2 rotation.")
    print("     Everything above is a fact about E8; nothing in it mentions m004.")
    print("\nSELFTEST: PASS")


if __name__ == "__main__":
    selftest()
