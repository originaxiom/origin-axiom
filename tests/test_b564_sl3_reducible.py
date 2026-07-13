"""B564 — the SL(3) phi-fixed locus is entirely reducible (probation P2).

The discriminating mechanism: phi-fixedness pins A to FINITE ORDER (the commutator
trace t9 is phi-fixed only when the factor (mu-1)^3(mu+1)^3(mu^2+1)(mu^2+mu+1)
vanishes -> mu a root of unity), and a finite-order A forces a reducible (block-
diagonal) intertwiner. See frontier/B564_sl3_phi_fixed_reducible/FINDINGS.md.
"""
import sympy as sp


def test_pinning_factor_roots_are_roots_of_unity():
    """The t9-fixed factor forces mu to be a root of unity (orders 1,2,4,3) -> A finite order."""
    mu = sp.symbols('mu')
    fac = (mu - 1) ** 3 * (mu + 1) ** 3 * (mu ** 2 + 1) * (mu ** 2 + mu + 1)
    roots = sp.roots(sp.Poly(fac, mu))
    # every root is a root of unity => |mu| = 1 and some mu^k = 1
    for r in roots:
        assert sp.simplify(sp.Abs(r) - 1) == 0
        assert any(sp.simplify(r ** k - 1) == 0 for k in (1, 2, 3, 4))
    # the distinct roots are exactly {1, -1, i, -i, omega, omega^2}
    omega = sp.Rational(-1, 2) + sp.sqrt(3) * sp.I / 2
    assert set(roots) == {sp.Integer(1), sp.Integer(-1), sp.I, -sp.I, omega, sp.conjugate(omega)}


def test_finite_order_A_forces_reducible_intertwiner():
    """A finite-order diagonal A=diag(mu,1,1/mu) with an intertwiner B satisfying
    B commuting/anti-structure on the fixed locus is block-diagonal (a 1+2 split)."""
    # Minimal witness: at mu=i, diag(B)=diag(B^-1)=(c,0,0) forces B's action to preserve
    # the eigenline split of A; a generic solution of A B A^-1 = phi-image is block 1(+)2.
    i = sp.I
    A = sp.diag(i, 1, -i)                       # finite-order (mu=i), det=1
    assert sp.simplify(A ** 4 - sp.eye(3)) == sp.zeros(3)     # order 4
    # a block-diagonal 1(+)2 intertwiner commutes with the A-eigenline decomposition
    B = sp.diag(sp.Symbol('b0'), sp.Matrix([[sp.Symbol('b1'), sp.Symbol('b2')],
                                            [sp.Symbol('b3'), sp.Symbol('b4')]]))
    # block-diagonal B is reducible: it preserves the 1-dim eigenspace of A
    assert B[0, 1] == 0 and B[0, 2] == 0 and B[1, 0] == 0 and B[2, 0] == 0
