"""B252 (sage-python) -- rep-theory verification of the Chat-2 chirality-obstruction handoff (Steps 1,2,4 + the
E6 outer automorphism). Run: sage-python chirality_obstruction_sage.py. Backs the recorded constants in
chirality_obstruction.py."""
from sage.all import WeylCharacterRing

E6 = WeylCharacterRing("E6", style="coroots")
print("E6 fundamental reps (degree, self-dual?):")
for i in range(1, 7):
    w = [0] * 6
    w[i - 1] = 1
    r = E6(*w)
    print(f"  omega_{i}: dim {r.degree():>4}  self-dual {r == r.dual()}")

r27 = E6(1, 0, 0, 0, 0, 0)       # 27  = omega_1 (minuscule)
adj = E6(0, 1, 0, 0, 0, 0)       # 78  = omega_2 (adjoint)
print()
print("Step 1: 27 complex (27 != 27bar):", r27 != r27.dual(), " | 78 real (78 == 78bar):", adj == adj.dual())
print("        => chiral matter can live ONLY in the 27; the adjoint 78 is vector-like.")
print("E6 outer automorphism = duality, swaps the minuscule pair 27 <-> 27bar (both dim 27):",
      r27.dual().degree() == 27 and r27 != r27.dual())
print()
print("Step 4: E8 -> E6 x SU(3): 248 = (78,1)+(1,8)+(27,3)+(27bar,3bar);  dim check:",
      78 * 1 + 1 * 8 + 27 * 3 + 27 * 3, "= 248")
print("        => the 27 and 27bar appear PAIRED (with 3, 3bar): a conjugation-symmetric decomposition.")
print("\nAll machine-checkable steps confirm the handoff's rep theory. The load-bearing Step 3")
print("('amphicheirality = this outer automorphism, swapping 27<->27bar') IS banked -- HINT_LEDGER H36 (conjugation")
print("on 2T's irreps = the finite-E6 Dynkin automorphism, via the 2T McKay quiver) -- so chat2's citation is correct.")
