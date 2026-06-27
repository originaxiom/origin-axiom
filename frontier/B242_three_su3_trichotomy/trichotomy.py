"""B242 -- the THREE SU(3)'s of the figure-eight: a trichotomy on three faces, with the genuine relations.
Firewall-clean (quantum topology / character-variety / rep-theory; physics framing stays firewalled, H37).
Nothing to CLAIMS.md.

THE THREE SU(3)'s (one per face of the four-faces dictionary):
  (1) CLASSICAL geometry  -- the SL(3,C) character variety of 4_1 [B71]: Fix(T_1^2) = 3 components, dim 2
      (V0 geometric=Sym^2, W1/W2 Dehn-filling). The space of SL(3,C) flat connections.
  (2) QUANTUM            -- the level-rank gauge dual SU(3)_2 [B238]: a Chern-Simons gauge group at level 2,
      dual to SU(2)_3 (shared kappa=k+N=5); knot fundamental invariant -2/phi, bundle WRT -1/phi.
  (3) SCFT (flavor)      -- the Gang-Yonekura SU(3) [B241, arXiv:1803.04009]: a global FLAVOR symmetry of the
      3d N=2 theory T[K], universal across all hyperbolic twist knots, from the A_1 (SU(2)) 6d theory.

They are DISTINCT (different type AND specificity): a variety vs a number vs a symmetry; all-level vs level-2 vs
level-free; golden-specific vs golden-specific vs twist-universal.

THE NEW RESULT (this file): the relation (1)<->(2) edge is the level-rank duality SU(2)_3 <-> SU(3)_2, and at the
golden root q=e^{i pi/5} (the shared kappa=5) it acts on the fundamental KNOT invariant as COMPLEX CONJUGATION:
  level-rank sends a=q^N -> a=q^{kappa-N}; at kappa=5, q^{5-N} = q^5 q^{-N} = -q^{-N}, so a^2 -> q^{-2N} = conj(q^{2N}).
Therefore SU(2)_3 (a=q^2) and SU(3)_2 (a=q^3) coincide EXACTLY iff the invariant is real iff the knot is
AMPHICHEIRAL (P(a)=P(a^{-1})). The figure-eight (amphicheiral) -> SU(2)_3 = SU(3)_2 = -2/phi exactly; chiral
knots -> the two are complex conjugates. This UNIFIES the amphichirality theme (B240/B241) with the level-rank
theme (B238): amphichirality IS the condition for the level-rank coincidence to be exact.

The SU(N)_k fundamental invariant = HOMFLY P(a=q^N, z=q-q^{-1}); HOMFLY polynomials from SnapPy/Sage, mapped to
(a,z) via the calibration L=-i*a, M=i*z (validated: trefoil 2a^2-a^4+a^2 z^2; fig-8 a^2+a^-2-1-z^2). Run:
python trichotomy.py (pyenv).
"""
import cmath

import numpy as np

PHI = (1 + 5 ** 0.5) / 2
Q = cmath.exp(1j * np.pi / 5)            # the golden root; SU(2)_3: a=q^2, SU(3)_2: a=q^3 (shared kappa=5)

# HOMFLY P(a,z) (Sage-verified, mapped to (a,z)); amphicheiral <=> symmetric under a -> 1/a.
HOMFLY = {
    "4_1 (amph)":  lambda a, z: a ** 2 - z ** 2 + a ** -2 - 1,
    "6_3 (amph)":  lambda a, z: -a ** 2 * z ** 2 + z ** 4 - a ** 2 + 3 * z ** 2 - z ** 2 / a ** 2 - a ** -2 + 3,
    "8_9 (amph)":  lambda a, z: (a ** 2 * z ** 4 - z ** 6 + 3 * a ** 2 * z ** 2 - 5 * z ** 4 + 2 * a ** 2
                                 - 8 * z ** 2 + z ** 4 / a ** 2 + 3 * z ** 2 / a ** 2 + 2 / a ** 2 - 3),
    "3_1 (chiral)": lambda a, z: -a ** 4 + a ** 2 * z ** 2 + 2 * a ** 2,
    "5_2 (chiral)": lambda a, z: z ** 2 / a ** 2 + 1 / a ** 2 + z ** 2 / a ** 4 + 1 / a ** 4 - 1 / a ** 6,
}


def su_nk_fundamental(P, N, q=Q):
    """the SU(N)_k fundamental quantum invariant of the knot = HOMFLY at a=q^N, z=q-q^{-1} (kappa=k+N=5)."""
    return P(q ** N, q - 1 / q)


def levelrank_pair(P):
    """(SU(2)_3 value, SU(3)_2 value) -- the level-rank dual pair at the golden root."""
    return su_nk_fundamental(P, 2), su_nk_fundamental(P, 3)


def is_amphicheiral(P, tol=1e-9):
    """real fundamental invariant <=> P(a)=P(1/a) <=> the level-rank pair coincides exactly."""
    s2, s3 = levelrank_pair(P)
    return abs(s2.imag) < tol and abs(s3.imag) < tol


if __name__ == "__main__":
    print("=== the (1)<->(2) edge: level-rank SU(2)_3 <-> SU(3)_2 on the fundamental knot invariant (golden root) ===")
    for nm, P in HOMFLY.items():
        s2, s3 = levelrank_pair(P)
        exact = abs(s2 - s3) < 1e-9
        conj = abs(s2 - s3.conjugate()) < 1e-9
        rel = "EQUAL (exact level-rank coincidence)" if exact else ("complex conjugates" if conj else "?")
        print(f"  {nm:13s}: SU(2)_3={s2:+.5f}  SU(3)_2={s3:+.5f}  -> {rel}")

    # the figure-eight: both = -2/phi, matching B240's J_2 (and B238's bundle -1/phi, same golden field)
    s2, s3 = levelrank_pair(HOMFLY["4_1 (amph)"])
    assert abs(s2 - (-2 / PHI)) < 1e-9 and abs(s3 - (-2 / PHI)) < 1e-9
    print(f"\n  4_1: SU(2)_3 = SU(3)_2 = -2/phi = {-2/PHI:+.5f}  (= B240 J_2; B238 bundle WRT = -1/phi, same field)")

    # the mechanism: exact coincidence  <=>  amphicheiral (real)  <=>  P(a)=P(1/a)
    print("\n=== the mechanism: level-rank duality = complex conjugation at kappa=5 ===")
    for nm, P in HOMFLY.items():
        s2, s3 = levelrank_pair(P)
        amph = is_amphicheiral(P)
        exact = abs(s2 - s3) < 1e-9
        assert amph == exact                        # exact level-rank coincidence  <=>  amphicheiral
        print(f"  {nm:13s}: amphicheiral={amph}  <=>  exact level-rank coincidence={exact}")
    # and the chiral ones are genuine complex-conjugate pairs (not equal)
    for nm in ("3_1 (chiral)", "5_2 (chiral)"):
        s2, s3 = levelrank_pair(HOMFLY[nm])
        assert abs(s2 - s3) > 1e-6 and abs(s2 - s3.conjugate()) < 1e-9

    print("\nTRICHOTOMY: (1) SL(3,C) char variety [B71, classical] -- (2) SU(3)_2 [B238, quantum] -- "
          "(3) GY flavor SU(3) [B241, SCFT].")
    print("  (1)<->(2): quantization (the WRT invariant quantizes the char variety; volume conj at k->inf).")
    print("  (2)<->SU(2)_3: level-rank duality = complex conjugation; EXACT iff amphicheiral (this file).")
    print("  (3): distinct from both -- flavor vs gauge/geometry, twist-universal vs golden (B241).")
    print("ALL CHECKS PASS")
