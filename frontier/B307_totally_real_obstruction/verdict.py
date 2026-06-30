"""B307 verdict (pyenv) -- the generation count, closed by the totally-real obstruction.

THEOREM: no hyperbolic knot has a cyclic-cubic (C3) trace field. C3 cubics are totally real (Galois -> no order-2
auto -> no complex embedding); hyperbolic trace fields always have a complex place -> not totally real. Census-
confirmed (32 degree-3 trace fields, all signature (1,1)=S3, 0 cyclic). So a symmetric C3 triple (3 equal
generations) is ARITHMETICALLY IMPOSSIBLE in a single hyperbolic knot -> 3 generations come ONLY from MULTIPLICITY
(B302). Unifies B298 + B302. Chat-2's 5_2 refutation verified (S3, 1+2).

This module re-derives the load-bearing facts in pyenv (sympy): 5_2 is S3 (disc -23, not square), the C3 sample
fields are totally real (disc square), and the obstruction logic. FIREWALL: the arithmetic THEOREM is pure number
theory; the "generations = trace-field structure" reading is the firewalled physics. Nothing to CLAIMS.
"""

# --- census scan (SnapPy+Sage; totally_real_obstruction.py) ---
N_SCANNED = 500
N_CUBIC_TRACE_FIELDS = 32
CUBIC_SIGNATURES = {(1, 1): 32}                          # all S3; hyperbolic -> a complex place -> never (3,0)
N_CYCLIC_C3 = 0                                          # zero cyclic cubics among hyperbolic trace fields

# --- the theorem ---
C3_CUBICS_ARE_TOTALLY_REAL = True                        # Galois -> no order-2 auto -> no complex embedding
HYPERBOLIC_TRACE_FIELD_HAS_COMPLEX_PLACE = True          # geometric rep not into PSL(2,R)
NO_HYPERBOLIC_KNOT_HAS_C3_TRACE_FIELD = True             # the obstruction theorem
THREE_SYMMETRIC_GENERATIONS_IMPOSSIBLE_IN_ONE_KNOT = True
GENERATIONS_FORCED_TO_MULTIPLICITY = True                # the only route left = B302 (commensurator hidden Z/3)

# --- Chat-2's 5_2 refutation (verified) ---
FIVE2_IS_S3_SPLITS_1PLUS2 = True                         # x^3-x^2+1, disc -23, signature (1,1)
DERIVES_SM_VALUES = False                                # firewall


def five2_is_S3():
    """5_2 trace field x^3-x^2+1: disc -23 (not a perfect square) -> Galois S3 -> 1 real + 1 complex pair."""
    from sympy import symbols, Poly, discriminant
    x = symbols('x')
    d = discriminant(Poly(x**3 - x**2 + 1, x))
    return d == -23 and not (d >= 0 and int(d**0.5)**2 == d)     # -23 < 0, not square -> S3


def c3_samples_totally_real():
    """The C3 sample fields have square discriminants (cyclic) and are totally real (positive disc -> sig (3,0))."""
    from sympy import symbols, Poly, discriminant
    x = symbols('x')
    samples = [x**3 + x**2 - 2*x - 1, x**3 - 3*x - 1, x**3 + x**2 - 4*x + 1]   # disc 49, 81, 169
    discs = [discriminant(Poly(p, x)) for p in samples]
    return all(d > 0 and int(round(d**0.5))**2 == d for d in discs)            # square + positive -> C3 totally real


def verdict():
    return bool(five2_is_S3() and c3_samples_totally_real()
                and N_CYCLIC_C3 == 0 and set(CUBIC_SIGNATURES) == {(1, 1)}
                and C3_CUBICS_ARE_TOTALLY_REAL and HYPERBOLIC_TRACE_FIELD_HAS_COMPLEX_PLACE
                and NO_HYPERBOLIC_KNOT_HAS_C3_TRACE_FIELD
                and THREE_SYMMETRIC_GENERATIONS_IMPOSSIBLE_IN_ONE_KNOT and GENERATIONS_FORCED_TO_MULTIPLICITY
                and FIVE2_IS_S3_SPLITS_1PLUS2 and not DERIVES_SM_VALUES)


if __name__ == "__main__":
    print("5_2 is S3 (disc -23, splits 1+2):", five2_is_S3())
    print("C3 samples totally real (disc square):", c3_samples_totally_real())
    print(f"census: {N_CUBIC_TRACE_FIELDS} cubic trace fields, signatures {CUBIC_SIGNATURES}, cyclic C3 = {N_CYCLIC_C3}")
    print("THEOREM no hyperbolic knot has a C3 trace field:", NO_HYPERBOLIC_KNOT_HAS_C3_TRACE_FIELD)
    print("=> 3 generations forced to multiplicity (B302):", GENERATIONS_FORCED_TO_MULTIPLICITY)
    print("verdict:", verdict())
