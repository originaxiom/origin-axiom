"""C5 — executable lock for the conditional trace selector theorem.

Locks the *post-T1 algebra* of ``docs/TRACE_SELECTOR_THEOREM.md`` — everything
downstream of the named assumption T1. T1 itself ("the primitive projective
tangent return inherits the original arithmetic persistence filters") is a
chosen assumption and is NOT tested here; C5 stays `conditional`. What this
file locks is that, *given* T1's filter output (minimal positive integer
hyperbolic trace / tangent torsion-one), the algebra forces

    mu = 3  ->  I = 1/4  ->  (lambda/h)^2 = 1  ->  lambda/h = 1

and that the selected tangent quadratic is exactly the ``A`` sector
``t^2 - 3t + 1``. Previously C5 was the one ledger entry whose evidence
pointer was documentation only (audit 2026-07-01).
"""

import sympy as sp

from origin_axiom.algebra import A, F_FIB, char_poly, t


def test_tangent_trace_is_mu_equals_4I_plus_2():
    # On the primitive projective return family, I = c^2 - 1 and
    # mu(c) = 4c^2 - 2; hence mu = 4I + 2 identically.
    c, I = sp.symbols("c I", real=True)
    mu_of_c = 4 * c**2 - 2
    assert sp.expand(mu_of_c - (4 * (c**2 - 1) + 2)) == 0


def test_T1_filters_force_mu_equals_three():
    # Route 1 (minimal positive integer hyperbolic trace): the smallest
    # integer mu with |mu| > 2 and mu > 0 is 3.
    hyperbolic = [mu for mu in range(-10, 11) if abs(mu) > 2 and mu > 0]
    assert min(hyperbolic) == 3
    # Route 2 (tangent torsion-one closure): |det(M - Id)| = |2 - mu| = 1
    # on the positive hyperbolic branch gives mu = 3 uniquely.
    mu = sp.symbols("mu", integer=True)
    sols = sp.solve([sp.Abs(2 - mu) - 1], mu)
    torsion_one = {s[mu] if isinstance(s, dict) else s[0] for s in sols}
    assert torsion_one == {1, 3}
    assert {m for m in torsion_one if abs(m) > 2} == {3}


def test_mu_three_forces_I_one_quarter_and_lambda_over_h_one():
    I = sp.Rational(3 - 2, 4)
    assert I == sp.Rational(1, 4)
    # B25 Fibonacci-Hamiltonian normalization: I = (lambda/h)^2 / 4.
    lam_over_h_sq = 4 * I
    assert lam_over_h_sq == 1
    # positive coupling branch
    assert sp.sqrt(lam_over_h_sq) == 1


def test_selected_tangent_quadratic_is_the_A_sector():
    mu = 3
    q = t**2 - mu * t + 1
    assert sp.expand(q - char_poly(A)) == 0


def test_lucas_hierarchy_control_matches_the_documented_values():
    # Sec. 5 of the theorem doc: matching even powers F^n gives
    # char(F^n) = t^2 - L_n t + 1 and (lambda/h)^2 = L_n - 2, with first
    # values 1, 5, 16, 45, 121, 320. Verified from F itself, not hard-coded
    # Lucas numbers.
    documented = [1, 5, 16, 45, 121, 320]
    computed = []
    for k in range(1, 7):
        n = 2 * k
        Fn = F_FIB**n
        Ln = sp.trace(Fn)
        # char(F^n) = t^2 - L_n t + 1 (det F^n = 1 for even n)
        assert sp.expand(char_poly(Fn) - (t**2 - Ln * t + 1)) == 0
        computed.append(Ln - 2)
    assert computed == documented
    # The primitive first member is the lambda/h = 1 surface.
    assert computed[0] == 1


def test_lucas_hierarchy_equals_the_P8_torsion_orders():
    # Cross-link: L_{2k} - 2 = |det(F^{2k} - I)| = |det(A^k - I)|, the P8
    # mapping-torus torsion orders — the hierarchy is the torsion ladder.
    from origin_axiom.topology import torsion_order

    for k in range(1, 7):
        Ln = sp.trace(F_FIB ** (2 * k))
        assert Ln - 2 == torsion_order(k)
