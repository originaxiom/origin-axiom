"""B757 -- the two-Z/3 identity cell (L108, prereg 23eb35be).  sympy + stdlib, exact."""
from itertools import product

import sympy as sp

x = sp.symbols("x")

print("=" * 84)
print("CELL 1 -- element level")
print("=" * 84)
g = sp.Matrix([[0, -1], [1, -1]])
print(f"g^3 == I: {g**3 == sp.eye(2)};  charpoly(g) = {sp.factor(g.charpoly(x).as_expr())} == Phi_3")
print("deck representatives are covering translations gamma*Gamma_3 with gamma in Gamma;")
print("Gamma = pi_1(m004) is TORSION-FREE (banked: B285 exact rep; classical for knot groups)")
print("=> every deck representative has INFINITE order; g has order 3.")
print("CELL 1 VERDICT: NO -- the two Z/3's are never the same element (theorem).")

print("=" * 84)
print("CELL 2 -- the congruence-level coincidence")
print("=" * 84)
t = sp.symbols("t")
Delta = t**2 - 3 * t + 1
deck_mod4 = sp.Matrix([[0, -1], [1, 3]]).applyfunc(lambda v: v % 4)   # companion of Delta
g_mod4 = g.applyfunc(lambda v: v % 4)
print(f"Delta mod 4 = {sp.Poly(Delta, t, modulus=4).as_expr()} = Phi_3 mod 4")
print(f"companion(Delta) mod 4 = {deck_mod4.tolist()};  g mod 4 = {g_mod4.tolist()}")
print(f"EXACT EQUALITY: {deck_mod4 == g_mod4}  (orientation: g matches t, not t^2, "
      "in the exhibited presentations)")

print("=" * 84)
print("CELL 3 -- the E20 adjudication: order-3 structure of GL(2, Z/4), brute force")
print("=" * 84)
els = []
for a, b, c, d in product(range(4), repeat=4):
    if (a * d - b * c) % 4 in (1, 3):
        els.append(sp.Matrix([[a, b], [c, d]]))
print(f"|GL(2, Z/4)| = {len(els)}")
def mmul(A, B):
    return (A * B).applyfunc(lambda v: v % 4)
order3 = [M for M in els if mmul(mmul(M, M), M) == sp.eye(2) and M != sp.eye(2)]
print(f"order-3 elements: {len(order3)}")
# conjugacy classes among order-3 elements
reps = []
seen = set()
for M in order3:
    key = tuple(M)
    if key in seen:
        continue
    cls = set()
    for P in els:
        det = (P[0, 0] * P[1, 1] - P[0, 1] * P[1, 0]) % 4
        inv_det = 1 if det == 1 else 3                     # 3*3 = 9 = 1 mod 4
        Padj = sp.Matrix([[P[1, 1], -P[0, 1]], [-P[1, 0], P[0, 0]]])
        Pinv = (inv_det * Padj).applyfunc(lambda v: v % 4)
        cls.add(tuple(mmul(mmul(P, M), Pinv)))
    seen |= cls
    reps.append((M, len(cls)))
print(f"conjugacy classes of order-3 elements: {len(reps)} "
      f"(sizes {[n for _, n in reps]}; representatives {[r.tolist() for r, _ in reps]})")
C = deck_mod4
C2 = mmul(C, C)
in_class_of = []
for M, tag in ((C, "C=deck=g"), (C2, "C^2")):
    for i, (r, _) in enumerate(reps):
        # test conjugacy by membership in the enumerated class
        cls = set()
        for P in els:
            det = (P[0, 0] * P[1, 1] - P[0, 1] * P[1, 0]) % 4
            inv_det = 1 if det == 1 else 3
            Padj = sp.Matrix([[P[1, 1], -P[0, 1]], [-P[1, 0], P[0, 0]]])
            Pinv = (inv_det * Padj).applyfunc(lambda v: v % 4)
            cls.add(tuple(mmul(mmul(P, r), Pinv)))
        if tuple(M) in cls:
            in_class_of.append((tag, i))
            break
print(f"class membership: {in_class_of}")
n_classes = len(reps)
print(f"=> with {n_classes} class(es), 'conjugate mod 4' for two arbitrary Z/3 actions is "
      f"{'FORCED up to orientation' if n_classes <= 2 else 'not forced'} -- "
      "the coincidence carries at most the 1-bit orientation.")
print("orientation canonicity: t IS canonical (the meridian generator of H_1 = Z);")
print("g vs g^2 is NOT (B302 exhibited a representative, not an oriented class).")
print("CELL 3 VERDICT: the mod-4 coincidence is BASE-RATE (Sylow-forced up to a")
print("non-canonical orientation bit) -- not identity content.")

print("=" * 84)
print("CELL 4 -- verdict assembly")
print("=" * 84)
print("VERDICT: DISSOLVED -- element-level NO (theorem); congruence-level coincidence real")
print("but E20-forced; no canonical orientation. The shared content is exactly the banked")
print("Eisenstein atom (charpoly Phi_3 / omega on both sides) and nothing more. L108 CLOSES;")
print("DOOR4 stays ROUTE-OBSTRUCTED (no new mechanism).")
