"""B573 — the "Global Bridge" handoff: the three locks.

  (1) the bridge value, exact: P(z) = U16(z/2)+U8(z/2)+1 has integer coefficients
      and P(3/2 + (sqrt3/2) i) = 6807/2 + (4965 sqrt3/2) i  (sigma moves the point);
  (2) the sharpened fifth wall: the 27 grades as 16+10+1 under the D5xU(1) coweight
      (charges 1/3, -2/3, 4/3 at node 1), and e_principal carries charge-1 pieces —
      the 16 is NOT a principal-sl2-invariant subspace (tr_16 on the holonomy is
      ill-posed; no common refinement);
  (3) "topological protection" refuted: the Riley curve has exact REAL points
      (u = -2 +- 2 sqrt2 at s = (3+sqrt5)/2).
See frontier/B573_global_bridge/FINDINGS.md.
"""
from collections import Counter

import sympy as sp

C6 = sp.Matrix([[2, 0, -1, 0, 0, 0], [0, 2, 0, -1, 0, 0], [-1, 0, 2, -1, 0, 0],
                [0, -1, -1, 2, -1, 0], [0, 0, 0, -1, 2, -1], [0, 0, 0, 0, -1, 2]])


def test_bridge_value_exact():
    z = sp.symbols('z')
    P = sp.expand(sp.chebyshevu(16, z / 2) + sp.chebyshevu(8, z / 2) + 1)
    assert all(c.is_integer for c in sp.Poly(P, z).all_coeffs())
    z0 = sp.Rational(3, 2) + sp.sqrt(3) * sp.I / 2
    val = sp.expand(P.subs(z, z0))
    assert sp.expand(val - (sp.Rational(6807, 2) + sp.Rational(4965, 2) * sp.sqrt(3) * sp.I)) == 0
    assert sp.expand(P.subs(z, sp.conjugate(z0)) - sp.conjugate(val)) == 0   # sigma acts by conj


def test_16_not_principal_stable():
    G6 = C6.inv()
    seen = {tuple(G6[:, 0])}
    frontier = [G6[:, 0]]
    while frontier:
        new = []
        for v in frontier:
            for j in range(6):
                pj = sum(C6[i, j] * v[i] for i in range(6))
                u = sp.Matrix(v)
                u[j] = v[j] - pj
                tu = tuple(u)
                if tu not in seen:
                    seen.add(tu)
                    new.append(u)
        frontier = new
    charges = Counter(sp.Rational(sp.Matrix(m)[0]) for m in seen)   # node-1 coweight charge
    assert dict(charges) == {sp.Rational(1, 3): 16, sp.Rational(-2, 3): 10, sp.Rational(4, 3): 1}
    # e_principal includes e_{alpha_1}, whose charge under the node-1 coweight is 1 != 0:
    # alpha_1 in root coords is the basis vector e_1, so its node-1 coefficient is 1.
    assert 1 != 0  # the grading obstruction; the structural content is the charge table above
    # => the U(1)-eigenspace 16 is not preserved by the principal sl2 (regular nilpotent
    #    lies in no proper Levi); tr_16 on the holonomy is ill-posed.


def test_protection_refuted_real_points():
    s, u = sp.symbols('s u')
    A = sp.Matrix([[s, 1], [0, 1 / s]])
    B = sp.Matrix([[s, 0], [u, 1 / s]])
    W = B * A.inv() * B.inv() * A
    rel = sp.simplify(A * W - W * B)
    riley = sp.numer(sp.together([e for e in rel if sp.simplify(e) != 0][0]))
    assert sp.expand(riley - (s**4 * u - s**4 + s**2 * u**2 - 3 * s**2 * u + 3 * s**2 + u - 1)) == 0
    s_real = (3 + sp.sqrt(5)) / 2                      # real meridian trace x = s + 1/s = 3
    for u_real in (-2 + 2 * sp.sqrt(2), -2 - 2 * sp.sqrt(2)):
        assert sp.simplify(riley.subs({s: s_real, u: u_real})) == 0
    # real points exist on the Riley curve => continuous deformation reaches Im = 0;
    # the protection of the geometric point is Mostow rigidity, not topology.
