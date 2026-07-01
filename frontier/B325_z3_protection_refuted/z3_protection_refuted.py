"""B325 -- Chat-2's 'symmetry obstruction' (Part 2 of its handoff) is REFUTED; the CRUX does NOT relocate to Level 4.
Run: python (pyenv). Verify-don't-trust on the load-bearing NEW claim of the Chat-2 handoff. (Part 1, the exact
omega-circulant, is confirmed and banked as B324 -- structure, not values, both seats agree.)

Chat-2 Part 2 claimed: the two light eigenvalues (1, omega^2) are 'Z/3-PROTECTED', the E6 cubic is Z/3-invariant, and
'a Z/3-invariant operator cannot lift a Z/3-protected degeneracy' -> the cubic cannot split the light masses -> the
hierarchy requires Z/3-BREAKING from the index-12 embedding (Level 4), the cubic is 'messenger not source', so the CRUX
relocates from Level 3 to Level 4. This is a representation-theory ERROR:

  (1) The generation Z/3 acts as the REGULAR representation = trivial (+) omega (+) omega^2 -- THREE DISTINCT 1-dim
      irreps. The two LIGHT eigenvectors are the omega-mode and the omega^2-mode: DIFFERENT irreps, not a single 2-dim
      irrep. Wigner protection ('a symmetric perturbation cannot lift a degeneracy') applies only WITHIN one irrep. Two
      distinct 1-dim irreps carry NO such protection.
  (2) By Schur, a Z/3-invariant (circulant) operator is diagonal on the irreps with ARBITRARY scalars -- so it CAN give
      the omega and omega^2 modes DIFFERENT eigenvalues. Demonstrated: a generic COMPLEX Z/3-invariant circulant has two
      DISTINCT light singular values (it SPLITS them). So a Z/3-invariant cubic mass matrix generically SPLITS the light
      masses.
  (3) The equal light magnitudes of OUR overlap matrix alpha*J + omega*P are ACCIDENTAL -- they come from the single
      perturbation being a UNIT (|omega|=1), not from Z/3-protection. A different Z/3-invariant circulant (the physical
      E6-cubic mass matrix) is NOT degenerate.
  (4) Chat-2 also conflates the SL(2) OVERLAP matrix tr(a_i b_j^-1) (degenerate) with the physical E6-CUBIC mass matrix
      (unknown, a different circulant). The overlap's accidental degeneracy does not transfer.

VERDICT: the light degeneracy is NOT Z/3-protected; a Z/3-invariant cubic CAN lift it. The CRUX does NOT relocate to
Level 4; it stays the Level-3 E6-cubic computation -- which is NOT obstructed from producing the hierarchy. (Do not
update OPEN_PROBLEMS to relocate the CRUX; Chat-2's Part-2 relocation was based on the error above.) The exact
omega-circulant (Part 1 / B324) stands as structure. FIREWALLED; nothing to CLAIMS.
"""
import numpy as np

_w = np.exp(2j * np.pi / 3)
_P = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)


def generic_z3_invariant_splits_light(tol=1e-6):
    """a generic COMPLEX circulant (Z/3-invariant) has two DISTINCT light singular values -> it splits them."""
    # a fixed, reproducible complex circulant (not the special alpha J + omega P)
    c0, c1, c2 = 1 + 0.5j, 2j, 3 - 1j
    C = c0 * np.eye(3) + c1 * _P + c2 * (_P @ _P)
    sv = sorted(np.linalg.svd(C, compute_uv=False))
    return abs(sv[0] - sv[1]) > tol                              # the two light singular values differ


def overlap_light_magnitudes():
    """our alpha J + omega P: the two light |eigenvalues| are equal (=1) -- ACCIDENTAL (|omega|=1)."""
    alpha = (5 - np.sqrt(3) * 1j) / 2
    M = alpha * np.ones((3, 3)) + _w * _P
    mags = sorted(abs(np.linalg.eigvals(M)))
    return [round(mags[0], 6), round(mags[1], 6)]


# --- the verdict facts ---
LIGHT_MODES_ARE_DIFFERENT_IRREPS = True     # omega, omega^2 -- distinct 1-dim irreps, no Wigner protection
Z3_INVARIANT_CAN_SPLIT_LIGHT = True         # generic complex circulant splits the light singular values
OVERLAP_DEGENERACY_IS_ACCIDENTAL = True     # equal magnitudes from |omega|=1, not Z/3-protection
OVERLAP_NOT_THE_PHYSICAL_MASS = True        # SL(2) trace overlap != the E6-cubic mass matrix
CHAT2_OBSTRUCTION_REFUTED = True
CRUX_STAYS_LEVEL3_NOT_RELOCATED = True       # the E6-cubic (Level 3) can lift the light masses
DERIVES_SM_VALUES = False


def verdict():
    return bool(
        generic_z3_invariant_splits_light() and overlap_light_magnitudes() == [1.0, 1.0]
        and LIGHT_MODES_ARE_DIFFERENT_IRREPS and Z3_INVARIANT_CAN_SPLIT_LIGHT
        and OVERLAP_DEGENERACY_IS_ACCIDENTAL and OVERLAP_NOT_THE_PHYSICAL_MASS
        and CHAT2_OBSTRUCTION_REFUTED and CRUX_STAYS_LEVEL3_NOT_RELOCATED and not DERIVES_SM_VALUES
    )


if __name__ == "__main__":
    print("light modes = omega, omega^2 irreps (DIFFERENT irreps -> no Wigner protection):", LIGHT_MODES_ARE_DIFFERENT_IRREPS)
    print("generic Z/3-invariant circulant SPLITS the light singular values:", generic_z3_invariant_splits_light())
    print("our alpha J + omega P light magnitudes:", overlap_light_magnitudes(), "-> equal, but ACCIDENTAL (|omega|=1)")
    print("VERDICT: Chat-2 Part 2 REFUTED; a Z/3-invariant cubic CAN split -> CRUX stays Level 3 (the E6 cubic).")
    print("verdict:", verdict())
