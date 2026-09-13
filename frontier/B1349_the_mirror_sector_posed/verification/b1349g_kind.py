"""The KIND gate, first step: do the readings lie in B1011 C6's BANKED theta-even value set?

Addendum 2 closed by saying "what now gates the row is kind-correctness, not arithmetic."
This asks the first kind question there is: does the quantity even land in the value set the
corpus has already banked for this sector, whose declared KIND (KIND_TABLE) is amplitude-part,
bounds [-1,1], field Q(sqrt5)?

B1011 C6, verbatim: "The theta-even value set, exact:
  {0, +-1/4, +-1/(4phi), +-1/2, +-1/(2phi), +-phi/4, +-phi/2, +-1}"

CAUTION ON WHAT IS BEING COMPARED (E72: one name, two quantities). C6's set is a CENSUS over
group elements of Re(zeta^-1 u-bar M u); the values here are over the 15 metallic words R^m L^m
with the charge-conjugation weld. The quantities are NOT asserted to be identical. What is tested
is CONTAINMENT -- whether each computed reading is an element of the banked set, and of its
declared field. That is what the kind question needs, and it needs no identification.
"""
import math
from fractions import Fraction

PHI = (1 + 5 ** 0.5) / 2
C6 = {0.0}
for v in (0.25, 1 / (4 * PHI), 0.5, 1 / (2 * PHI), PHI / 4, PHI / 2, 1.0):
    C6.add(v); C6.add(-v)
C6 = sorted(C6)

def in_C6(x, tol=1e-12):
    return any(abs(x - c) < tol for c in C6)

# --- CONTROL first: the criterion must reject values near the set but not in it ---
assert in_C6(1 / (2 * PHI)) and in_C6(-1 / (2 * PHI)) and in_C6(0.5) and in_C6(1.0) and in_C6(0.0)
assert not in_C6(0.31), "must reject 0.31 (near 1/(2phi) = 0.309 but not equal)"
assert not in_C6(0.3), "must reject 0.3"
assert not in_C6(1 / (2 * PHI) + 1e-9), "the tolerance must be tight enough to separate"
print("  [PASS] containment test is two-sided: accepts the banked values, rejects near-misses")
print(f"  B1011 C6's banked theta-even set ({len(C6)} values):")
print("   ", [f"{c:+.9f}" for c in C6])

EAR_INDEP = {"-1/(2phi)": -1 / (2 * PHI), "0": 0.0, "1/2": 0.5, "1": 1.0}
EAR_DEP = {"phi^2/(2sqrt2)": PHI ** 2 / (2 * 2 ** 0.5), "1/(phi.2sqrt2)": 1 / (PHI * 2 * 2 ** 0.5),
           "sqrt5/(2sqrt2)": 5 ** 0.5 / (2 * 2 ** 0.5), "1/(2sqrt2)": 1 / (2 * 2 ** 0.5)}

print()
print("=" * 78)
print("BRANCH A -- the ear-INDEPENDENT forced values (gcd(m,15) > 1)")
print("=" * 78)
okA = True
for n, v in EAR_INDEP.items():
    hit = in_C6(v); okA &= hit
    print(f"  {n:>16s} = {v:+.9f}   in C6's banked set ? {hit}")
print(f"\n  ALL FOUR IN THE BANKED SET: {okA}")
assert okA, "branch A must land in the banked set"

print()
print("=" * 78)
print("BRANCH B -- the ear-DEPENDENT extremes (gcd(m,15) = 1)")
print("=" * 78)
anyB = False
for n, v in EAR_DEP.items():
    hit = in_C6(v); anyB |= hit
    near = min(C6, key=lambda c: abs(c - v))
    print(f"  {n:>16s} = {v:+.9f}   in C6's banked set ? {hit}"
          f"   (nearest banked value {near:+.9f}, off by {abs(v - near):.4f})")
print(f"\n  ANY IN THE BANKED SET: {anyB}")
assert not anyB, "branch B must fall outside the banked set"

print()
print("=" * 78)
print("WHY, structurally -- and it is the field, not an accident")
print("=" * 78)
print("  KIND_TABLE declares the mirror row's field as Q(sqrt5).")
print("  Branch A's four values lie in Q(sqrt5).                           -> KIND-ELIGIBLE")
print("  Branch B's values each carry 1/sqrt2 and generate Q(sqrt2,sqrt5).")
print("  sqrt2 is not in Q(zeta_60) (conductor 8 does not divide 60), so a fortiori not in")
print("  Q(sqrt5) -- branch B's readings CANNOT be elements of a set declared over Q(sqrt5).")
print()
print("  => BRANCH B IS EXCLUDED ON KIND, not merely short on the R11 ledger.")
print("     Its values are not of the mirror row's declared kind, in the strict sense that they")
print("     do not lie in the row's field. This is INDEPENDENT of the 2 - 2 = 0 tie.")
print("  => BRANCH A IS KIND-ELIGIBLE, which is NOT the same as kind-correct: eligibility means")
print("     the value could belong to the row. Whether the row is the right physical observable")
print("     is the question B856 lost on its own sector, and nothing here touches it.")
