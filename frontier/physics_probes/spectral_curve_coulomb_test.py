"""Path B (re-examination of the j=1728 / Seiberg-Witten thread) -- CONFIRMS the V34 kill with new
explicit evidence: the m=2 (m136) spectral curve's j=1728 is an ISOLATED, symmetry-forced CM point,
NOT a Coulomb-branch deformation family.

Background (V32-V34, reconfirmed V37): the m=2 trace-map A-polynomial discriminant is the elliptic
curve y^2 = M^4 - 6 M^2 + 1 with j=1728 (CM by Z[i], tau=i). V34 killed the Seiberg-Witten
"identification" -- pure N=2 SU(2) SW theory is a FAMILY of curves over the Coulomb branch u with an
SW differential giving a(u), a_D(u), a prepotential; the m136 side is a SINGLE fixed curve with no u,
no SW differential, no prepotential. The match was ONE number (tau=i <=> j=1728), forced by the
silver mean (a=6 in kappa=P^2-6).

THE DECISIVE NEW COMPUTATION (this re-examination). Embed the curve in the 1-parameter family
y^2 = M^4 - a M^2 + 1 and compute the j-invariant explicitly via the binary-quartic invariants I, J:
   I(a) = a^2 + 12,   J(a) = 2 a (a-6)(a+6),   j(a) = 16 (a^2+12)^3 / ((a-2)^2 (a+2)^2).
Then:
   j = 1728  <=>  J = 0  <=>  a in {0, +-6}.
The silver mean FORCES a=6 (m136) => j=1728. And j VARIES with a (e.g. j(a=3)=148176/25 != 1728), so
`a` is the ONLY modulus and j=1728 is an ISOLATED point pinned by the single algebraic constraint J=0
-- there is no free Coulomb parameter, no SW-differential family, no prepotential. The `a`-deformation
is a quartic-coefficient deformation, NOT a deformation of the manifold m136 (which is the single point
a=6) and NOT a physical Coulomb branch.

VERDICT: CONFIRMS V34. The j=1728 CM curve is a real, isolated, exact NUMBER-THEORETIC fact about one
manifold, forced by the silver mean -- not 4D gauge-theory physics. No new evidence resurrects the
thread (the only "family", the a-deformation, has varying j but carries no SW structure and is
disconnected from m136's deformations). Computer-assisted, exact. Proven core P1-P16 untouched.
"""
import sympy as sp

a, M = sp.symbols("a M")


def quartic_invariants(coeffs):
    """Binary-quartic invariants (I,J) for f = p0 M^4 + p1 M^3 + p2 M^2 + p3 M + p4."""
    p0, p1, p2, p3, p4 = coeffs
    I = 12 * p0 * p4 - 3 * p1 * p3 + p2 ** 2
    J = 72 * p0 * p2 * p4 - 27 * p0 * p3 ** 2 - 27 * p1 ** 2 * p4 + 9 * p1 * p2 * p3 - 2 * p2 ** 3
    return sp.expand(I), sp.expand(J)


def j_of_a():
    """j-invariant of y^2 = M^4 - a M^2 + 1 as a function of a."""
    I, J = quartic_invariants((1, 0, -a, 0, 1))
    j = sp.simplify(1728 * 4 * I ** 3 / (4 * I ** 3 - J ** 2))
    return I, J, j


def main():
    I, J, j = j_of_a()
    print("Path B -- j=1728 / SW re-examination of the m=2 spectral curve\n")
    print("family y^2 = M^4 - a M^2 + 1:")
    print("  I(a) =", I)
    print("  J(a) =", sp.factor(J))
    print("  j(a) =", sp.factor(j))
    print("\n  j = 1728  <=>  J = 0  <=>  a in", sorted(sp.solve(sp.Eq(J, 0), a), key=lambda r: sp.re(r)))
    print("  silver mean fixes a=6 (m136) -> j=1728:", sp.simplify(j.subs(a, 6)) == 1728)
    print("  j varies with a (a is the only modulus):", sp.simplify(sp.diff(j, a)) != 0,
          " e.g. j(a=3) =", sp.nsimplify(j.subs(a, 3)))
    print("\n  => j=1728 is ISOLATED + symmetry-forced (a=6); no Coulomb branch, no SW differential.")
    print("     CONFIRMS V34: number theory, not 4D physics.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
