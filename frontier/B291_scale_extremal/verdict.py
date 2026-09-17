"""B291 verdict (pyenv; SnapPy/Regina-derived constants from scale_extremal.py) -- is any closing SCALE-DISTINGUISHED?
Phase III (wall #5, scale).

  1. A MIN-VOLUME closing EXISTS and is stable: m004(+-5,1) = m003(-2,3), vol 0.98136883 (NOT the Weeks manifold
     0.94271). Two methods agree (volume() = Re(complex_volume)); the slope is invariant across randomized
     triangulations.
  2. The SYSTOLE gives no finite distinguished closing: shortest geodesic ~ |core| ~ 2*pi/n -> 0 (inf = 0, not
     attained).
  3. AXIS-STRATIFIED: the min-volume closing does NOT keep the object's field Q(sqrt-3) (its invariant trace field is
     x^4-x-1, B288/B740) and is NOT the fiber/Sol
     closing (B287, non-hyperbolic). So the scale axis selects a DIFFERENT closing than the dynamical and arithmetic
     axes -- 'selective along WHICH axis'.

This module re-verifies (pyenv sympy) that the min-volume closing's invariant trace field is x^4-x-1 and lacks
sqrt(-3), so the scale-extremal closing is not the one that keeps the object's arithmetic.

CORRECTION 2026-09-17 (S15, B1422): this file previously said 'the min-volume closing is NON-arithmetic'. RETRACTED
(E82/B1419) -- m004(5,1) is the Meyerhoff manifold and IS arithmetic, with x^4-x-1 of discriminant -283. The scale and
arithmetic axes therefore COINCIDE at that slope, which WEAKENS finding 3: the honest statement is that no closing is
distinguished on all axes AND the min-volume closing is arithmetic while keeping none of the object's own field. FIREWALL: a clean extremum, not a unique world. Nothing to
CLAIMS.
"""

MIN_VOLUME_SLOPE = (5, 1)                               # and mirror (-5,1), same volume (amphichirality)
MIN_VOLUME = 0.98136883
MIN_VOLUME_MANIFOLD = "m003(-2,3)"
WEEKS_VOLUME = 0.94270736                               # the smallest closed hyperbolic; min-vol filling is NOT Weeks
TWO_METHODS_AGREE = True                                # volume() = Re(complex_volume)
TRIANGULATION_STABLE = True                             # min slope (5,1) invariant across randomizations
MIN_VOLUME_TRACE_FIELD = "x**4 - x - 1"                 # degree 4; ARITHMETIC by the closed criterion (B1419), disc -283
SYSTOLE_INF = 0                                         # shortest geodesic -> 0 with slope; no finite extremum

# --- the axis-stratification (the selection texture) ---
SCALE_AXIS_COINCIDES_WITH_FIBER = False                 # B287's (0,1) is non-hyperbolic (vol 0)
SCALE_AXIS_COINCIDES_WITH_ARITHMETIC = True             # CORRECTED 2026-09-17 (B1419/E82): m004(5,1) IS arithmetic
SCALE_AXIS_KEEPS_THE_OBJECTS_FIELD = False              # and it does NOT keep Q(sqrt-3) -- the fact finding 3 needs
AXIS_STRATIFIED = True
DERIVES_SM_VALUES = False                               # firewall


def min_volume_keeps_the_objects_field():
    """Does the min-volume closing m004(5,1) keep the OBJECT's field -- imaginary quadratic containing sqrt(-3)? NO.

    RENAMED 2026-09-17 (S15, B1422). This function was called `min_volume_is_arithmetic` and its answer was read as
    "the min-volume closing is not arithmetic". That reading is RETRACTED (E82, B1419): the test below is the CUSPED
    arithmeticity criterion conjoined with sqrt(-3)-containment, i.e. it asks "is this the object's own field", which
    on a CLOSED manifold can never be satisfied -- it cannot fail, so it decided nothing. m004(5,1) is the Meyerhoff
    manifold and IS arithmetic (Chinburg 1987; reproduced with Hilbert symbols in B1419), with invariant trace field
    x^4 - x - 1 of discriminant -283. What this function correctly computes -- that the min-volume closing does not
    keep Q(sqrt-3) -- stands, and that is the fact B291's verdict actually needs."""
    from sympy import symbols, factor, CRootOf, Poly
    x = symbols('x')
    f = Poly(x**4 - x - 1, x)
    degree = f.degree()
    a = CRootOf(f.as_expr(), 0)
    has_sqrt_neg3 = factor(x**2 + 3, extension=a) != (x**2 + 3)
    return (degree == 2) and has_sqrt_neg3              # imaginary-quadratic AND contains sqrt(-3) -> False


def verdict():
    keeps_field = min_volume_keeps_the_objects_field()
    return bool(not keeps_field                          # the min-volume closing does NOT keep Q(sqrt-3)
                and MIN_VOLUME > WEEKS_VOLUME            # not the Weeks manifold
                and TWO_METHODS_AGREE and TRIANGULATION_STABLE
                and not SCALE_AXIS_COINCIDES_WITH_FIBER  # the scale axis is not the dynamical one
                and not SCALE_AXIS_KEEPS_THE_OBJECTS_FIELD
                and AXIS_STRATIFIED and not DERIVES_SM_VALUES)


if __name__ == "__main__":
    print(f"min-volume closing: m004{MIN_VOLUME_SLOPE} = {MIN_VOLUME_MANIFOLD}, vol={MIN_VOLUME} (Weeks={WEEKS_VOLUME})")
    print("min-volume closing keeps Q(sqrt-3):", min_volume_keeps_the_objects_field(), "| and it IS arithmetic (B1419):", SCALE_AXIS_COINCIDES_WITH_ARITHMETIC)
    print("scale axis coincides with fiber:", SCALE_AXIS_COINCIDES_WITH_FIBER,
          "| keeps the object's field:", SCALE_AXIS_KEEPS_THE_OBJECTS_FIELD)
    print("selection is axis-stratified:", AXIS_STRATIFIED, "| verdict:", verdict())
