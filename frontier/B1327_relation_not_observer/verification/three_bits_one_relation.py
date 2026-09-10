"""Link 54 on the object: mirror = swap x arrow, so three named bits carry one relation."""
import snappy, warnings; warnings.filterwarnings("ignore")
from collections import Counter

M = snappy.Manifold("m004")
pats = Counter()
for iso in M.symmetry_group().isometries():
    A = iso.cusp_maps()[0]
    a, b, c, d = int(A[0, 0]), int(A[0, 1]), int(A[1, 0]), int(A[1, 1])
    pats[(a, d, a * d - b * c)] += 1          # (arrow s_m, swap s_l, mirror det); m004's maps are diagonal

for (sm, sl, det), n in sorted(pats.items()):
    print(f"arrow={sm:+d} swap={sl:+d} mirror={det:+d}  x{n}")
viol = [k for k in pats if k[2] != k[0] * k[1]]
assert not viol, viol
assert len(pats) == 4, len(pats)
assert sum(pats.values()) == 8, sum(pats.values())
print("\n4 of 8 sign triples realised; zero violations of mirror = arrow x swap.")
print("Three bits, one relation, two free -- and no act of selection in the statement.")
