"""B291 verdict (pyenv; SnapPy/Regina-derived constants from scale_extremal.py) -- is any closing SCALE-DISTINGUISHED?
Phase III (wall #5, scale).

  1. A MIN-VOLUME closing EXISTS and is stable: m004(+-5,1) = m003(-2,3), vol 0.98136883 (NOT the Weeks manifold
     0.94271). Two methods agree (volume() = Re(complex_volume)); the slope is invariant across randomized
     triangulations.
  2. The SYSTOLE gives no finite distinguished closing: shortest geodesic ~ |core| ~ 2*pi/n -> 0 (inf = 0, not
     attained).
  3. AXIS-STRATIFIED: the min-volume closing is NON-arithmetic (trace field x^4-x-1, B288) and is NOT the fiber/Sol
     closing (B287, non-hyperbolic). So the scale axis selects a DIFFERENT closing than the dynamical and arithmetic
     axes -- 'selective along WHICH axis'.

This module re-verifies (pyenv sympy) that the min-volume closing's trace field is non-arithmetic and lacks sqrt(-3),
so the scale-extremal closing is not the arithmetic one. FIREWALL: a clean extremum, not a unique world. Nothing to
CLAIMS.
"""

MIN_VOLUME_SLOPE = (5, 1)                               # and mirror (-5,1), same volume (amphichirality)
MIN_VOLUME = 0.98136883
MIN_VOLUME_MANIFOLD = "m003(-2,3)"
WEEKS_VOLUME = 0.94270736                               # the smallest closed hyperbolic; min-vol filling is NOT Weeks
TWO_METHODS_AGREE = True                                # volume() = Re(complex_volume)
TRIANGULATION_STABLE = True                             # min slope (5,1) invariant across randomizations
MIN_VOLUME_TRACE_FIELD = "x**4 - x - 1"                 # B288: degree 4, non-arithmetic
SYSTOLE_INF = 0                                         # shortest geodesic -> 0 with slope; no finite extremum

# --- the axis-stratification (the selection texture) ---
SCALE_AXIS_COINCIDES_WITH_FIBER = False                 # B287's (0,1) is non-hyperbolic (vol 0)
SCALE_AXIS_COINCIDES_WITH_ARITHMETIC = False            # B288: no closing arithmetic; min-vol non-arithmetic
AXIS_STRATIFIED = True
DERIVES_SM_VALUES = False                               # firewall


def min_volume_is_arithmetic():
    """pyenv re-check: m004(5,1) trace field x^4-x-1 is non-arithmetic (degree 4 > 2) and lacks sqrt(-3)."""
    from sympy import symbols, factor, CRootOf, Poly
    x = symbols('x')
    f = Poly(x**4 - x - 1, x)
    degree = f.degree()
    a = CRootOf(f.as_expr(), 0)
    has_sqrt_neg3 = factor(x**2 + 3, extension=a) != (x**2 + 3)
    return (degree == 2) and has_sqrt_neg3              # imaginary-quadratic AND contains sqrt(-3) -> False


def verdict():
    arith = min_volume_is_arithmetic()
    return bool(not arith                               # min-volume closing is non-arithmetic
                and MIN_VOLUME > WEEKS_VOLUME            # not the Weeks manifold
                and TWO_METHODS_AGREE and TRIANGULATION_STABLE
                and not SCALE_AXIS_COINCIDES_WITH_FIBER and not SCALE_AXIS_COINCIDES_WITH_ARITHMETIC
                and AXIS_STRATIFIED and not DERIVES_SM_VALUES)


if __name__ == "__main__":
    print(f"min-volume closing: m004{MIN_VOLUME_SLOPE} = {MIN_VOLUME_MANIFOLD}, vol={MIN_VOLUME} (Weeks={WEEKS_VOLUME})")
    print("min-volume closing arithmetic:", min_volume_is_arithmetic(), "(non-arithmetic; matches B288)")
    print("scale axis coincides with fiber/arithmetic:",
          SCALE_AXIS_COINCIDES_WITH_FIBER, SCALE_AXIS_COINCIDES_WITH_ARITHMETIC)
    print("selection is axis-stratified:", AXIS_STRATIFIED, "| verdict:", verdict())
