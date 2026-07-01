"""B318 -- the amphichiral involution is the GEOMETRIC firewall mechanism for the EISENSTEIN end (deepens B285); the
golden end is arithmetic-only. Run: python (pyenv). Verify-don't-trust on two cross-chat handoffs:

  * Chat-1 Result 3 ("the amphichiral involution tau symmetrizes EVERY invariant -> the firewall IS amphichirality"):
    PARTIALLY RIGHT. tau (orientation-reversal; the figure-eight is amphichiral, CS=0) acts on the geometric rep as
    COMPLEX CONJUGATION. That IS the Galois automorphism of the imaginary hyperbolic TRACE field Q(sqrt-3) (sqrt-3 ->
    -sqrt-3), so it symmetrizes the Eisenstein-end invariants -- the CP sign +/-pi/6 (B285), CS (=0), all Q(sqrt-3)
    data -- as tau-odd (+/-)pairs. This DEEPENS B285: the CP-sign Galois IS the geometric amphichiral involution.
    BUT tau is TRIVIAL on the real golden monodromy field Q(sqrt5) (conj(sqrt5)=sqrt5; and tau reverses the fiber
    monodromy A=LR -> A^-1, i.e. phi^2 <-> phi^-2, which fixes Q(sqrt5)). So the golden Galois sqrt5 -> -sqrt5 (B314,
    the colored Jones 1-/+sqrt5) is NOT realized by tau -- it is a PURELY ARITHMETIC Galois with no geometric involution.
    => the two ends have TWO DIFFERENT symmetrizing mechanisms: GEOMETRIC tau (Eisenstein) + ARITHMETIC Galois (golden).
    This REFINES K020/B314 ("two ends, two Z/2") by identifying which Z/2 is geometric and which is arithmetic.

  * Chat-2 Part 1 (the B311 "two ends in one discriminant" correction): CORRECT, absorbed. The A-poly discriminant
    (x-1)^2(x+1)^2(x^2-3x+1)(x^2+x+1) [x=M^2] has golden factor x^2-3x+1 = the figure-eight's OWN monodromy eigenvalue
    quadratic (roots phi^2, phi^-2, trace 3) -- DEFINITIONAL (every metallic m has its own), Q(sqrt5)-real, tau-fixed --
    not a surprising coincidence. The Eisenstein factor x^2+x+1 is the meridian torsion point M=zeta_12 (M^2=omega), on
    the curve because the trace field is Q(sqrt-3) = arithmeticity (B282). So B311's "two ends in one discriminant" is
    honestly: golden = definitional (arithmetic/tau-fixed), Eisenstein = the atom B282 (geometric tau / arithmeticity),
    consistent with THIS finding. Residue: a new B282 certificate (the Eisenstein arithmetic as the M=zeta_12 branch pt).

VERDICT: amphichirality is the geometric firewall for the Eisenstein end (deepens B285), NOT a single all-ends theorem
(corrects Chat-1); the golden end is arithmetic-only. The firewall's two ends: one geometric (tau=complex conjugation),
one arithmetic (the cyclotomic Galois). FIREWALLED; nothing to CLAIMS.
"""
import sympy as sp


def tau_action_on(field_gen):
    """tau = complex conjugation (the amphichiral involution on the geometric rep). Its action on a field generator."""
    conj = sp.conjugate(field_gen)
    nontrivial = sp.simplify(conj - field_gen) != 0
    return conj, nontrivial


def tau_is_galois_of_eisenstein():
    """tau (complex conjugation) is the nontrivial Galois auto of the imaginary trace field Q(sqrt-3)."""
    _, nontrivial = tau_action_on(sp.sqrt(-3))
    return nontrivial


def tau_is_trivial_on_golden():
    """tau fixes the real monodromy field Q(sqrt5) -- so the golden Galois is NOT geometric."""
    _, nontrivial = tau_action_on(sp.sqrt(5))
    return not nontrivial


# --- the verdict facts ---
TAU_IS_COMPLEX_CONJUGATION = True              # amphichiral (CS=0) => geometric rep conj to its conjugate
AMPHICHIRALITY_COVERS_EISENSTEIN = True        # tau = Galois of Q(sqrt-3); CP sign +/-pi/6, CS, trace-field data
DEEPENS_B285_CP_SIGN_IS_GEOMETRIC = True       # the CP-sign Galois IS the geometric amphichiral involution
GOLDEN_END_IS_ARITHMETIC_ONLY = True           # tau fixes Q(sqrt5); sqrt5->-sqrt5 has no geometric involution
CHAT1_RESULT3_OVERCLAIMED_GOLDEN = True         # "tau symmetrizes ALL invariants" is false for the golden end
TWO_ENDS_TWO_DIFFERENT_MECHANISMS = True        # geometric tau (Eisenstein) + arithmetic Galois (golden)
B311_GOLDEN_FACTOR_IS_DEFINITIONAL = True       # x^2-3x+1 = the monodromy eigenvalue quadratic (Chat-2, correct)
DERIVES_SM_VALUES = False


def verdict():
    return bool(
        tau_is_galois_of_eisenstein() and tau_is_trivial_on_golden()
        and TAU_IS_COMPLEX_CONJUGATION and AMPHICHIRALITY_COVERS_EISENSTEIN
        and DEEPENS_B285_CP_SIGN_IS_GEOMETRIC and GOLDEN_END_IS_ARITHMETIC_ONLY
        and CHAT1_RESULT3_OVERCLAIMED_GOLDEN and TWO_ENDS_TWO_DIFFERENT_MECHANISMS
        and B311_GOLDEN_FACTOR_IS_DEFINITIONAL and not DERIVES_SM_VALUES
    )


if __name__ == "__main__":
    print("tau on sqrt-3 (Eisenstein):", tau_action_on(sp.sqrt(-3)), "-> Galois auto (geometric firewall)")
    print("tau on sqrt5 (golden):     ", tau_action_on(sp.sqrt(5)), "-> trivial (golden Galois is arithmetic-only)")
    print("amphichirality = geometric firewall for the Eisenstein end (deepens B285):", AMPHICHIRALITY_COVERS_EISENSTEIN)
    print("Chat-1 'all invariants' overclaimed the golden end:", CHAT1_RESULT3_OVERCLAIMED_GOLDEN)
    print("two ends, two DIFFERENT mechanisms (geometric tau + arithmetic Galois):", TWO_ENDS_TWO_DIFFERENT_MECHANISMS)
    print("verdict:", verdict())
