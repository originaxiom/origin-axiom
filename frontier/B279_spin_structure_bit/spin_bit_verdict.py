"""B279 verdict (pyenv-safe; heavy SnapPy inputs in spin_structure_bit_snappy.py).

The amphicheiral involution tau of the figure-eight complement FIXES (does not swap) its two spin structures.
Topology result, FIREWALLED -- the physics reading (Chat-2: fix => tau gaugeable-with-fermions => non-chiral
gravitational vacuum) stays in speculations/ and rests on an UNVERIFIED parity-anomaly link. Nothing to CLAIMS.md.
"""
# checkable inputs (sage-python spin_structure_bit_snappy.py):
N_SPIN_STRUCTURES = 2            # H_1(4_1)=Z => H^1(;Z/2)=Z/2
SYMMETRY = "D4"                  # full symmetry group of the complement, order 8
IS_AMBIENT = True               # hyperbolic => Mostow + Gordon-Lueke: isometries extend to (S^3, 4_1)
HOMOLOGICAL_ACTION_TRIVIAL = True  # every cusp map is +-1 (identity mod 2) => tau* = id on H^1(;Z/2)

# the bit (proof in FINDINGS.md): the S^3-bounding spin structure sigma_0 is canonical and ambient-symmetry-
# invariant (S^3 has a UNIQUE spin structure), so tau(sigma_0)=sigma_0; and since tau*=id on H^1(;Z/2)=Z/2 the
# action is all-or-nothing => BOTH fixed.
BIT = "FIX"
PHYSICS_LINK_VERIFIED = False   # the fix->gaugeable-with-fermions step (parity anomaly / eta) is Chat-2's, unchecked


def verdict():
    return (N_SPIN_STRUCTURES == 2 and IS_AMBIENT and HOMOLOGICAL_ACTION_TRIVIAL and BIT == "FIX")


if __name__ == "__main__":
    print(f"4_1 spin structures: {N_SPIN_STRUCTURES} | symmetry {SYMMETRY} ambient={IS_AMBIENT}")
    print(f"tau action on the 2 spin structures: {BIT}")
    print(f"physics interpretation verified? {PHYSICS_LINK_VERIFIED} (firewalled)")
    print("verdict:", verdict())
