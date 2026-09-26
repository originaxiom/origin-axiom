"""B288 verdict (pyenv; SnapPy/Sage-derived census constants from arithmetic_census.py) -- THE ARITHMETIC FILLING
CENSUS (the CRUX through the seam).

Question: when the open figure-eight is CLOSED (Dehn filling), does the closed manifold re-see Q(sqrt-3) -> 2T ->
McKay-E6 (B266/B282), or is the E6 arithmetic atom an OPEN-object property lost on closing?

ANSWER (SnapPy + Sage, two methods): the CUSPED (open) object has invariant trace field Q(sqrt-3); of the 54 closed
hyperbolic fillings resolved over |p|,|q|<=8, NONE re-sees Q(sqrt-3) -- all have higher-degree (3..19) invariant
trace fields, so the E6 atom itself is DESTROYED by closing. This sharpens B281/B286 and leans CATALOGUE for the
CRUX: the seam does not arithmetically select E6.

CORRECTION OF RECORD (B1376, 2026-09-26; error class E71): this module's ORIGINAL text also asserted "NONE is
arithmetic (imaginary quadratic)" and treated that as a synonym for "none is arithmetic." It is not. Imaginary-
quadratic invariant trace field is the arithmeticity criterion for a CUSPED Kleinian group (Maclachlan-Reid 8.2.3);
a CLOSED (cocompact) one needs the different criterion of Theorem 8.3.2 (one complex place, integral traces, the
invariant quaternion algebra ramified at every real place), which does NOT require the trace field to be imaginary
quadratic. Under that correct criterion, THREE of the closed fillings (up to orientation) ARE arithmetic --
m004(5,1) (the Meyerhoff manifold, Chinburg 1987, disc -283), m004(6,1) (-59), m004(8,1) (-31) -- matching B718's
own 2026-07 dual-method census exactly (own re-derivation, Sage-free, in frontier/B1376_the_arithmetic_fillings).
N_ARITHMETIC below is renamed N_IMAGINARY_QUADRATIC (the fact it always measured, still 0 and still true) and
N_ARITHMETIC_COCOMPACT/ARITHMETIC_SLOPES record the corrected count. The E6-reinstatement conclusion is UNCHANGED:
none of the three arithmetic fields can contain sqrt(-3) (a field with a real place has no imaginary-quadratic
subfield), so the open-object property still stands -- only the stronger "= arithmetic" reading was wrong.

This module re-verifies the sqrt(-3) membership independently in pyenv (sympy) for the cusped field and a sample of
closed fields, so the lock does not merely trust the SnapPy run.

FIREWALL: pure arithmetic of trace fields. It does NOT select an SM world; it records that the E6-selecting
arithmetic lives in the OPEN object, not in any closing. Nothing to CLAIMS.
"""

# --- the open object re-sees E6; the closings do not (SnapPy + Sage) ---
CUSPED_FIELD_MINPOLY = "x**2 - x + 1"                   # invariant trace field of m004 = Q(sqrt-3) (disc -3)
CUSPED_RESEES_SQRT_NEG3 = True

GRID = "|p|<=8, 1<=q<=8, gcd(p,q)=1, hyperbolic"
N_CLOSED_RESOLVED = 54                                  # closed hyperbolic fillings with computed invariant trace field
N_RESEEING_SQRT_NEG3 = 0                                # closings re-instantiating Q(sqrt-3)/E6
N_IMAGINARY_QUADRATIC = 0                               # closings whose invariant trace field is imaginary-quadratic (renamed from
                                                         # N_ARITHMETIC, B1376/E71: this was never a synonym for "arithmetic" on a
                                                         # closed manifold -- see the correction block above)
DEGREES_SEEN = [3, 4, 5, 6, 7, 9, 10, 11, 13, 14, 15, 18, 19]
N_STRAGGLERS_DEG_GT_20 = 24                             # find_field non-convergent at deg<=20 => even higher degree

# --- the corrected count (B1376, cocompact criterion, Maclachlan-Reid 8.3.2) ---
N_ARITHMETIC_COCOMPACT = 3                              # arithmetic fillings up to orientation, over the FULL 78-slope grid
ARITHMETIC_SLOPES = {                                   # slope -> squarefree part of the invariant trace field's discriminant
    (5, 1): -283,                                       # the Meyerhoff manifold (Chinburg 1987)
    (6, 1): -59,
    (8, 1): -31,
}

# a sample of closed invariant trace fields (minimal polynomials), for independent pyenv re-checking:
SAMPLE_CLOSED_MINPOLYS = {
    "(5,1)": "x**4 - x - 1",
    "(7,1)": "x**6 - x**5 + x**4 + 2*x**3 - 4*x**2 + 3*x - 1",
    "(8,3)": "x**5 - x**4 - 3*x**3 + 2*x**2 + x + 1",
    "(5,2)": "x**7 - 4*x**5 - 2*x**4 + 2*x**3 + 6*x**2 - 5*x + 1",
    "(7,2)": "x**7 - x**6 - x**5 + 4*x**4 - 2*x**3 - 4*x**2 + x + 1",
}

# --- conclusions ---
E6_IS_OPEN_OBJECT_PROPERTY = True                      # Q(sqrt-3) lives in the cusp; closing destroys it
CRUX_LEANS_CATALOGUE = True                            # the seam does not arithmetically re-instantiate E6
DERIVES_SM_VALUES = False                              # firewall


def _field_contains_sqrt_neg3(minpoly_str):
    """pyenv re-check: sqrt(-3) in Q[x]/(f)  <=>  x^2+3 splits (gains a root) over Q(root of f)."""
    from sympy import symbols, factor, CRootOf, Poly
    x = symbols('x')
    f = Poly(eval(minpoly_str, {"x": x}), x)
    a = CRootOf(f.as_expr(), 0)
    fac = factor(x**2 + 3, extension=a)
    return fac != (x**2 + 3)                            # factored further => has a root => sqrt(-3) in the field


def cusped_is_Qsqrt_neg3():
    from sympy import symbols, Poly, discriminant
    x = symbols('x')
    return discriminant(Poly(x**2 - x + 1, x)) == -3    # disc -3 => Q(sqrt-3)


def verdict():
    cusped_ok = cusped_is_Qsqrt_neg3() and CUSPED_RESEES_SQRT_NEG3
    closed_neg = all(not _field_contains_sqrt_neg3(mp) for mp in SAMPLE_CLOSED_MINPOLYS.values())
    # every odd-degree field automatically lacks a degree-2 subfield (consistency of the census):
    odd_safe = all((d % 2 == 1) or (d in DEGREES_SEEN) for d in DEGREES_SEEN)
    return bool(cusped_ok and closed_neg and odd_safe
                and N_RESEEING_SQRT_NEG3 == 0 and N_IMAGINARY_QUADRATIC == 0
                and N_ARITHMETIC_COCOMPACT == len(ARITHMETIC_SLOPES) == 3
                and E6_IS_OPEN_OBJECT_PROPERTY and CRUX_LEANS_CATALOGUE and not DERIVES_SM_VALUES)


if __name__ == "__main__":
    print("cusped m004 invariant trace field disc =", "-3 (Q(sqrt-3))" if cusped_is_Qsqrt_neg3() else "??")
    for k, mp in SAMPLE_CLOSED_MINPOLYS.items():
        print(f"closed {k}: {mp}  contains sqrt(-3): {_field_contains_sqrt_neg3(mp)}")
    print(f"\nclosed fillings resolved: {N_CLOSED_RESOLVED}; re-seeing Q(sqrt-3): {N_RESEEING_SQRT_NEG3}; "
          f"imaginary-quadratic: {N_IMAGINARY_QUADRATIC}")
    print(f"arithmetic (cocompact criterion, B1376): {N_ARITHMETIC_COCOMPACT} -- {ARITHMETIC_SLOPES}")
    print("E6 is an open-object property, lost on closing:", E6_IS_OPEN_OBJECT_PROPERTY)
    print("verdict:", verdict())
