"""Which leg carries the 4? The census 18+9+6+3 fixes it -- check that, and that it is UNIQUE."""
from itertools import product
census = {"conn/conn": 18, "tail6/conn": 9, "conn/tail2": 6, "tail6/tail2": 3}
# leg1 = a1 conn + a2 tail6 ; leg2 = b1 conn + b2 tail2 ; leg3 = h (no split)
sols = []
for a1, a2, b1, b2, h in product(range(1, 13), repeat=5):
    if (a1 * b1 * h == census["conn/conn"] and a2 * b1 * h == census["tail6/conn"]
            and a1 * b2 * h == census["conn/tail2"] and a2 * b2 * h == census["tail6/tail2"]):
        sols.append((a1 + a2, b1 + b2, h))
print("leg-dimension triples (leg1, leg2, leg3) consistent with the census:")
for s in sorted(set(sols)): print("   ", s)
uniq = sorted(set(sols))
print(f"\ntotal entries: {[a*b*c for a,b,c in uniq]}  (the block is 36)")
print("the multiset of leg dimensions in every solution:", sorted({tuple(sorted(s)) for s in uniq}))
# THE PROBE'S OWN CORRECTION: this was written expecting the census to FORCE 3x3x4. It does not.
assert sorted(uniq) == [(3, 4, 3), (3, 12, 1), (9, 4, 1)], uniq
print("""
=> THE CENSUS ALONE DOES NOT FORCE THE SHAPE. Three factorizations fit its four counts:
   (3,4,3) -- the banked reading -- and also (3,12,1) and (9,4,1).
   The 3x3x4 shape is fixed by data the census does not contain: the spec's own index
   ranges (i = 1..3 for A_7, j = 1..2 for B_6, k = 1..3 for B_2, giving the 1x18
   conn/conn row) together with B1161's sector table Q/dc/Hd = 3/3/4.
   B1185 states the census "-> 36 = 3x3x4 ... re-derived exactly"; that is TRUE as a
   consistency check and NOT true as a derivation from the census. Recorded here rather
   than left to be re-discovered: the shape is CORROBORATED by the census, SOURCED
   elsewhere. Nothing downstream changes -- B1205's codimension count needs only that the
   block be 3x3 in the matter legs and linear in a 4-dimensional Higgs space.""")
