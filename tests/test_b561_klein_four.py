"""B561 addendum / probation P22 — the Klein-four -> SO(9) route also closes.

Seat-1 proposed: after B561 killed the Z/3 path, use the SECOND Z/2 (gamma =
Gal(Q(sqrt5)/Q), golden conjugation) to select an order-2 subalgebra of F4
(SO(9) via a (3,1) exponent split -> Pati-Salam -> SM).

Discriminating fact: gamma = (sqrt5 -> -sqrt5) FIXES Q(sqrt-3) pointwise, and the
theta-even H^1 (the F4 sector) lives over Q(sqrt-3) -- B370's Gram data is
tau = -2*sqrt(-3), no sqrt5. So gamma acts TRIVIALLY on the four exponent
directions; it acts on the QUANTUM/WRT face (colored Jones over Q(sqrt5), B314) --
the other end. Verdict: TOMBSTONE, F4 terminus. See frontier/B561_l50_crux/FINDINGS.md.
"""
import sympy as sp


def test_gamma_fixes_the_F4_sector_field():
    """gamma (sqrt5 -> -sqrt5) is the identity on Q(sqrt-3), where the F4 deformation lives."""
    s5, sm3 = sp.sqrt(5), sp.sqrt(-3)
    gamma = lambda e: e.subs(s5, -s5)
    assert gamma(sm3) == sm3                              # gamma fixes sqrt(-3)
    tau = -2 * sp.sqrt(3) * sp.I                          # B370 cusp/Gram datum
    assert sp.simplify(tau + 2 * sp.sqrt(-3)) == 0        # tau = -2 sqrt(-3) in Q(sqrt-3)
    assert sp.simplify(gamma(tau) - tau) == 0            # gamma acts TRIVIALLY on the F4 sector


def test_two_Z2s_act_on_different_fields():
    """theta lives on sqrt(-3) (E6/hyperbolic end), gamma on sqrt(5) (E8/quantum end):
    the Klein four's two generators act on DIFFERENT ends, not both on the F4 sector."""
    s5, sm3 = sp.sqrt(5), sp.sqrt(-3)
    theta = lambda e: e.subs(sm3, -sm3)                  # Gal(Q(sqrt-3)/Q)
    gamma = lambda e: e.subs(s5, -s5)                    # Gal(Q(sqrt5)/Q)
    assert theta(sm3) == -sm3 and theta(s5) == s5        # theta moves sqrt(-3), fixes sqrt5
    assert gamma(s5) == -s5 and gamma(sm3) == sm3        # gamma moves sqrt5, fixes sqrt(-3)
    # => on the F4 sector (over sqrt-3): theta is the E6->F4 fold; gamma is trivial.
