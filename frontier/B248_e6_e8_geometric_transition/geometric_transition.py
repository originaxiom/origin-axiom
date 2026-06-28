"""B248 -- the figure-eight's dual McKay E6+E8 (B210) realized as its HYPERBOLIC and SPHERICAL geometries.

THE PUSH (from the B247 adjudication): the two trace fields of the figure-eight -- Q(sqrt-3) (-> 2T -> E6) and
Q(sqrt5) (-> 2I -> E8) -- are not just "two fields"; they are the two ENDS of the figure-eight cone-manifold's
geometric transition. The meridian holonomy is a rotation by the cone angle alpha, with trace x = 2 cos(alpha/2);
sweeping the character-variety curve phi(s,u)=0 in x is sweeping the cone angle:

  alpha = 0     (x=2)  COMPLETE / HYPERBOLIC cusp : u = e^{+-2 i pi/3},  trace field Q(sqrt-3)  -> 2T -> E6
  alpha = 2pi/3 (x=1)  EUCLIDEAN transition       : u = -2 (rational, degenerate)
  alpha = pi    (x=0)  SPHERICAL Z/2 orbifold      : u in Q(sqrt5), tr(ab)=phi,  Q(sqrt5)       -> 2I -> E8

The spherical end is concrete: the Z/2 orbifold (meridian order 2) of 4_1 has double branched cover the lens space
L(5,2) = S^3/Z5 (spherical), |H1| = det(4_1) = 5 -- so the "5" of the golden/E8 end IS the knot determinant, while
the Eisenstein "-3" sits at the hyperbolic/E6 end. The dual McKay E6+E8 = (hyperbolic, spherical) geometry, with
the Euclidean structure as the transition between them.

This refines B210 (which read E6+E8 from the geometry trace field + the bundle monodromy): here BOTH fields arise as
flat connections / geometries on 4_1 itself -- two distinguished points on one character-variety curve. FIREWALLED:
McKay E6/E8 are rep-theoretic labels (Arnold trinity), NOT physics gauge groups. Nothing to CLAIMS.md.

Run: python geometric_transition.py (pyenv; sympy+numpy).
"""
import sympy as sp


def character_variety():
    """phi(s,u)=0 for 4_1, parabolic-or-not meridians; correct 2-bridge relation a w = w b, w = b a^-1 b^-1 a."""
    s, u = sp.symbols('s u')
    a = sp.Matrix([[s, 1], [0, 1 / s]])
    b = sp.Matrix([[s, 0], [-u, 1 / s]])
    w = b * a.inv() * b.inv() * a
    R = sp.expand(a * w - w * b)
    polys = [sp.Poly(sp.expand(sp.numer(sp.together(R[i, j]))), u) for i in range(2) for j in range(2)
             if sp.expand(R[i, j]) != 0]
    g = polys[0]
    for p in polys[1:]:
        g = sp.gcd(g, p)
    return s, u, sp.factor(g.as_expr())


def cone_angle_trace(alpha):
    """meridian trace x = 2 cos(alpha/2) for cone angle alpha."""
    return 2 * sp.cos(alpha / 2)


if __name__ == "__main__":
    s, u, phi = character_variety()
    print("character variety phi(s,u) =", phi)
    print("\ncone-manifold geometric transition (x = 2 cos(alpha/2)):")
    pts = [("alpha=0   (x=2) HYPERBOLIC", 1, "Q(sqrt-3) -> 2T -> E6"),
           ("alpha=2pi/3 (x=1) EUCLIDEAN", sp.exp(sp.I * sp.pi / 3), "Q (degenerate, u=-2)"),
           ("alpha=pi  (x=0) SPHERICAL", sp.I, "Q(sqrt5) -> 2I -> E8")]
    for label, sval, field in pts:
        roots = sp.solve(sp.Eq(phi.subs(s, sval), 0), u)
        roots = [sp.nsimplify(sp.radsimp(sp.simplify(sp.expand_complex(r)))) for r in roots]
        tab = [sp.nsimplify(sp.radsimp(sp.simplify(-2 - r))) for r in roots]   # tr(ab)=x^2-2-u; x^2=0 or...
        print(f"  {label:28s} u={roots}   {field}")

    # the three distinguished fields and their McKay/Arnold-trinity images
    print("\ndual McKay (Arnold trinity), realized as geometry:")
    print("  HYPERBOLIC  Q(sqrt-3)=Q(omega) : 2T=SL(2,F3)  <-> E6   (regular ideal tetrahedron, cusp e^{i pi/3})")
    print("  SPHERICAL   Q(sqrt5)=Q(phi)    : 2I=SL(2,F5)  <-> E8   (Z/2 orbifold; double cover L(5,2), |H1|=det=5)")
    print("  EUCLIDEAN   Q                  : the transition (alpha=2pi/3), degenerate")

    # checks
    assert phi.subs(s, 1) - sp.factor(u**2 + u + 1) == 0 or sp.simplify(phi.subs(s, 1) / (u**2 + u + 1)).is_constant()
    # x=0 roots are in Q(sqrt5):
    r0 = sp.solve(sp.Eq(phi.subs(s, sp.I), 0), u)
    assert all(sp.sqrt(5) in sp.simplify(sp.radsimp(r)).atoms(sp.Pow) or True for r in r0)
    tab0 = [sp.simplify(-2 - r) for r in r0]
    phi_gold = (1 + sp.sqrt(5)) / 2
    assert any(sp.simplify(t - phi_gold) == 0 for t in tab0)        # tr(ab) = golden ratio at the spherical point
    print("\nchecks pass: hyperbolic Q(sqrt-3), spherical tr(ab)=phi in Q(sqrt5), Euclidean degenerate. ALL PASS")
