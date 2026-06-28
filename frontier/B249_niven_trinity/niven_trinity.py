"""B249 -- Niven's theorem forces the figure-eight's dual McKay to be exactly E6+E8 (E7 geometrically excluded).

THE PUSH (from B248): the dual McKay E6+E8 is the figure-eight's hyperbolic<->spherical geometric transition. The
sharp question: sweeping the FULL orbifold tower (cone angle alpha=2pi/n, the meridian a rotation of order n), which
trace fields / McKay groups appear -- and is E7 really absent?

THE RESULT: at the Z/n orbifold the meridian trace is x = 2 cos(pi/n), and the rep's trace field is
    Q( x , sqrt( (5-x^2)(1-x^2) ) )      [from the char variety u^2 + (5-x^2) u + (5-x^2) = 0; disc = (5-x^2)(1-x^2)]
This is a CLEAN quadratic field (a single McKay group) iff x is rational. By NIVEN'S THEOREM, 2cos(pi/n) in Q only
for n in {1,2,3} (values -2,0,1) plus the cusp n=inf (x=2). Those are exactly:
    n=inf,1 (x=+-2): disc=-3 -> Q(sqrt-3)=Q(omega) -> 2T -> E6  (HYPERBOLIC, complete cusp)
    n=3     (x=1) : disc=0  -> Q              (EUCLIDEAN transition, degenerate)
    n=2     (x=0) : disc=5  -> Q(sqrt5)=Q(phi) -> 2I -> E8  (SPHERICAL, Z/2 orbifold; double cover L(5,2), det=5)
E7's field Q(sqrt2) would need x=sqrt2 (n=4), but sqrt2 is irrational (Niven), so the n=4 trace field is the MIXED
Q(sqrt2, sqrt-3) -- never the clean Q(sqrt2). So: the dual McKay E6+E8 AND the E7-exclusion are ONE arithmetic fact
(Niven on the orbifold deformation). E7 is not "excluded by three coincidences" (PAPER sec.5.2) but geometrically
impossible: no figure-eight orbifold has the rational meridian trace that a clean Q(sqrt2) would require.

OBJECT-SPECIFICITY: this needs the orbifold/knot structure (meridian, determinant, double branched cover = lens
space) -- among metallic bundles R^m L^m only m=1 (the figure-eight) is a knot complement in S^3. So the geometric
realization of the dual McKay is figure-eight-specific; the m>=2 bundles carry Q(sqrt(m^2+4)) in their monodromy but
have no knot structure to host the transition.

FIREWALL: E6/E7/E8 are McKay / Arnold-trinity labels, NOT physics gauge groups. The "geometric transition"
(negative -> zero -> positive curvature) is a structural rhyme, not a derived cosmology; no scale, no dynamics.
Nothing to CLAIMS.md.

Run: python niven_trinity.py (pyenv; sympy).
"""
import sympy as sp


def meridian_trace(n):
    """x = 2 cos(pi/n), the meridian trace at the Z/n orbifold (cone angle 2pi/n); n=oo -> 2 (complete cusp)."""
    if n == sp.oo:
        return sp.Integer(2)
    return sp.nsimplify(sp.simplify(2 * sp.cos(sp.pi / n)))


def discriminant(x):
    """disc of the char-variety quadratic u^2+(5-x^2)u+(5-x^2): (5-x^2)(1-x^2)."""
    return sp.simplify((5 - x ** 2) * (1 - x ** 2))


def trace_field_label(n):
    """returns (x, is_clean_quadratic, field-or-mixed label, McKay/geometry)."""
    x = meridian_trace(n)
    d = discriminant(x)
    clean = x.is_rational
    if clean:
        if sp.simplify(d) == 0:
            return x, True, "Q", "EUCLIDEAN (degenerate)"
        if sp.simplify(d - 5) == 0:
            return x, True, "Q(sqrt5)", "2I -> E8 (spherical)"
        if sp.simplify(d + 3) == 0:
            return x, True, "Q(sqrt-3)", "2T -> E6 (hyperbolic)"
        return x, True, f"Q(sqrt({d}))", "?"
    # mixed: x irrational
    return x, False, f"Q({x}, sqrt({d}))  [degree>2, MIXED]", "no clean McKay group"


def niven_rational_orbifolds():
    """the n for which 2cos(pi/n) is rational (Niven): {1,2,3} plus the cusp oo."""
    return [n for n in range(1, 200) if meridian_trace(n).is_rational] + [sp.oo]


if __name__ == "__main__":
    print("orbifold tower of 4_1 -- trace field by cone angle alpha = 2pi/n:")
    for n in [sp.oo, 1, 2, 3, 4, 5, 6, 8, 12]:
        x, clean, field, mck = trace_field_label(n)
        nm = "oo" if n == sp.oo else str(n)
        print(f"  n={nm:>3}  x={str(x):>14}  clean-quadratic={str(clean):>5}  {field:<22} {mck}")

    rat = niven_rational_orbifolds()
    print(f"\nNiven: rational-meridian-trace orbifolds = {[('oo' if r==sp.oo else r) for r in rat]}")
    assert set(r for r in rat if r != sp.oo) == {1, 2, 3}        # exactly n=1,2,3 (Niven)
    # the three clean fields are E6, Euclidean, E8 -- and E7 (sqrt2 at n=4) is mixed
    assert trace_field_label(2)[2] == "Q(sqrt5)"                  # E8
    assert trace_field_label(3)[2] == "Q"                         # Euclidean
    assert trace_field_label(sp.oo)[2] == "Q(sqrt-3)"            # E6
    assert not trace_field_label(4)[1]                            # n=4 (sqrt2 / E7) NOT clean
    print("\nForced trinity: E6 (hyperbolic, n=oo) | Euclidean (n=3) | E8 (spherical, n=2).")
    print("E7 (Q(sqrt2), n=4) is geometrically impossible: sqrt2 is never a rational 2cos(pi/n) (Niven).")
    print("=> dual McKay E6+E8 and the E7-exclusion are ONE arithmetic fact. ALL CHECKS PASS")
