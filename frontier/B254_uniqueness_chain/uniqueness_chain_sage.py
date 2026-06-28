"""B254 (sage-python) -- the amphicheiral Z2 grading (E6 -> F4) and the conformal-embedding reality, backing the
recorded constants in uniqueness_chain.py. Run: sage-python uniqueness_chain_sage.py."""
from sage.all import WeylCharacterRing, branching_rule

E6 = WeylCharacterRing("E6", style="coroots")
F4 = WeylCharacterRing("F4", style="coroots")
br = branching_rule("E6", "F4", "symmetric")           # the Z2 folding = the amphicheiral involution (H36)

r27 = E6(1, 0, 0, 0, 0, 0)
adj = E6(0, 1, 0, 0, 0, 0)
print("E6 -> F4 (the amphicheiral Z2 fixed algebra, H36):")
print("  27 ->", r27.branch(F4, rule=br), "  (= 1 + 26: Z2-odd singlet + Z2-even 26)")
print("  78 ->", adj.branch(F4, rule=br), "  (= 26 + 52: Z2-odd 26 + Z2-even adjoint)")
print("  F4 dims: 1, 26 =", F4(0, 0, 0, 1).degree(), ", 52 =", F4(1, 0, 0, 0).degree())
print("\nThe cubic 27^3 (the symmetric invariant) inherits a Z2 selection rule from 27 = 26_+ + 1_-. This is")
print("rep theory; any 'Yukawa texture / fermion mass' reading is firewalled (NOT asserted here).")
