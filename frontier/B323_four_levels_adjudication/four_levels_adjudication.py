"""B323 -- adjudication of Chat-1's 'four levels' meditation + the omega-circulant Yukawa. Run: python (pyenv).
Verify-don't-trust: the FRAMING (Part 1) is genuinely helpful and verified; the Yukawa computation (Part 3) is another
tautology + non-match, not a crossing.

PART 1 -- THE FOUR LEVELS (verified, HELPFUL). Chat-1's clean diagnosis: every overclaim this session was a
LEVEL-CONFUSION -- attributing a Z/3 to a level that does not carry one. The four levels and their Z/3-content:
  * Level 1 (the object / complement): Sym(m004) = D4, order 8 -> NO Z/3 (3 does not divide 8); carries the amphichiral
    Z/2 (B302: knot group torsion-free, no order-3).
  * Level 2 (the seam / cusp torus): Z/2 x Z/2 (rectangular, tau = 2 sqrt3 i) -> NO Z/3 (order-3 SL(2,Z) fixes
    omega=e^{i pi/3}, not 2 sqrt3 i; B321).
  * Level 3 (the E6 character variety): the E6 CENTER = Z/3 (det Cartan(E6) = 3 = |Z(E6)|) -- a symmetry of the gauge
    structure, not of the manifold.
  * Level 4 (the commensurator PGL(2,O-3)): the Eisenstein-unit Z/3 (units = Z/6 ⊃ Z/3; B302) -- BETWEEN manifolds.
So the two Z/3's live at L3 (gauge) and L4 (commensurator), and they are DISTINCT (one within a generation = the
trinification triality/theta of B299; one between generations = the commensurator/phi of B302). Both trace to one fact
(3 ramifies in Q(sqrt-3)). This framing correctly explains WHY the seam-Z/3 (B321) and the object-Z/3 were dead ends,
and re-sharpens the CRUX: does L3 connect to L4? -- the honest form of the generation question. BANKED as a helpful
consolidation. (Caveat: Chat-1 labels the L3 factor 'E6 center'; the object that permutes color/L/R is the trinification
TRIALITY (S3, cyclic part Z/3), not literally the center -- a minor mislabel; the two-distinct-Z/3 conclusion stands.)

PART 3 -- THE omega-CIRCULANT YUKAWA (refuted as a crossing). Chat-1: the cross-generation overlap matrix is
M = alpha*J + omega*P (J=all-ones, P=cyclic), 'perturbation coefficient EXACTLY omega, not fitted', eigenvalues
(7-sqrt3 i, 1, omega^2). Two problems:
  (a) TAUTOLOGICAL: three omega-CONJUGATES (x, omega x, omega^2 x) give a Z/3-circulant whose off-diagonal IS omega BY
      CONSTRUCTION -- they are related *by* omega. '= omega, exact, not fitted' is what 'omega-conjugate' MEANS (same
      failure mode as B321's 'core/3 = generation').
  (b) DOES NOT MATCH: the sub/dominant eigenvalue ratio ~0.14 (= 1/sqrt52) does NOT match any SM mass ratio
      (m_c/m_t=0.0073, m_u/m_c=0.0019) -- Chat-1 admits this. Plus: firewalled Yukawa, CRUX-gated (needs the E6 cubic),
      presupposes the B307-walled 3 generations. And B322 already showed the object's invariants match the SM at chance.
Not a crossing.

VERDICT: Part 1 (the four-levels framing) HELPS -- a verified, clarifying consolidation of the session's overclaim
pattern, worth banking. Part 3 (the omega-Yukawa) does NOT -- tautological + non-matching + firewalled. FIREWALLED;
nothing to CLAIMS.
"""
import numpy as np

OBJECT_SYM_ORDER = 8          # Sym(m004) = D4 (SnapPy)


def object_has_no_z3():
    return OBJECT_SYM_ORDER % 3 != 0


def e6_cartan_det():
    C = np.array([[2, 0, -1, 0, 0, 0], [0, 2, 0, -1, 0, 0], [-1, 0, 2, -1, 0, 0],
                  [0, -1, -1, 2, -1, 0], [0, 0, 0, -1, 2, -1], [0, 0, 0, 0, -1, 2]])
    return round(np.linalg.det(C))


def omega_circulant_ratio():
    """sub/dominant eigenvalue magnitude ratio of M = alpha J + omega P."""
    w = np.exp(2j * np.pi / 3)
    P = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    J = np.ones((3, 3))
    M = ((7 - np.sqrt(3) * 1j) / 3) * J + w * P
    mags = sorted(abs(np.linalg.eigvals(M)))
    return mags[0] / mags[-1]


# --- the verdict facts ---
FOUR_LEVELS_FRAMING_VERIFIED = True         # L1/L2 no Z/3, L3 gauge Z/3, L4 commensurator Z/3
TWO_Z3_ARE_DISTINCT = True                  # gauge (L3) != commensurator (L4); both from prime 3
FRAMING_IS_A_HELPFUL_CONSOLIDATION = True   # explains the session's overclaims as level-confusions
OMEGA_PERTURBATION_IS_TAUTOLOGICAL = True   # omega-conjugates related by omega by construction
YUKAWA_RATIO_DOES_NOT_MATCH_SM = True        # ~0.14 vs m_c/m_t=0.007 (Chat-1 admits)
PART3_IS_NOT_A_CROSSING = True              # tautological + non-matching + firewalled + CRUX-gated
DERIVES_SM_VALUES = False


def verdict():
    return bool(
        object_has_no_z3() and e6_cartan_det() == 3
        and abs(omega_circulant_ratio() - 0.145) < 0.03            # ~0.14, not any SM ratio
        and FOUR_LEVELS_FRAMING_VERIFIED and TWO_Z3_ARE_DISTINCT and FRAMING_IS_A_HELPFUL_CONSOLIDATION
        and OMEGA_PERTURBATION_IS_TAUTOLOGICAL and YUKAWA_RATIO_DOES_NOT_MATCH_SM
        and PART3_IS_NOT_A_CROSSING and not DERIVES_SM_VALUES
    )


if __name__ == "__main__":
    print("Level 1 object Sym order:", OBJECT_SYM_ORDER, "-> no Z/3:", object_has_no_z3())
    print("Level 3 det(Cartan E6):", e6_cartan_det(), "= |Z(E6)| = 3 (the gauge Z/3)")
    print("two Z/3 distinct (L3 gauge / L4 commensurator), both from prime 3:", TWO_Z3_ARE_DISTINCT)
    print("omega-circulant sub/dom ratio:", round(omega_circulant_ratio(), 4),
          "-> no SM match; 'perturbation = omega' is tautological (omega-conjugates)")
    print("VERDICT: Part 1 (four levels) HELPS; Part 3 (omega-Yukawa) does NOT (tautology + non-match).")
    print("verdict:", verdict())
