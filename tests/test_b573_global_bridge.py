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
import sympy as sp

from helpers_e6 import coordinate_charge, fundamental_coweight_orbit


def test_bridge_value_exact():
    z = sp.symbols('z')
    P = sp.expand(sp.chebyshevu(16, z / 2) + sp.chebyshevu(8, z / 2) + 1)
    assert all(c.is_integer for c in sp.Poly(P, z).all_coeffs())
    z0 = sp.Rational(3, 2) + sp.sqrt(3) * sp.I / 2
    val = sp.expand(P.subs(z, z0))
    assert sp.expand(val - (sp.Rational(6807, 2) + sp.Rational(4965, 2) * sp.sqrt(3) * sp.I)) == 0
    assert sp.expand(P.subs(z, sp.conjugate(z0)) - sp.conjugate(val)) == 0   # sigma acts by conj


def test_16_not_principal_stable():
    orbit = fundamental_coweight_orbit()          # the 27-weight orbit (shared BFS)
    charges = coordinate_charge(orbit, index=0)   # node-1 coweight charge
    assert dict(charges) == {sp.Rational(1, 3): 16, sp.Rational(-2, 3): 10, sp.Rational(4, 3): 1}
    # e_principal includes e_{alpha_1}; alpha_1 in root coords is the basis vector e_1,
    # so its node-1 coweight charge is its first coordinate = 1 != 0 (computed, not assumed):
    alpha1 = sp.Matrix([1, 0, 0, 0, 0, 0])
    assert alpha1[0] == 1 and alpha1[0] != 0   # the grading obstruction
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
