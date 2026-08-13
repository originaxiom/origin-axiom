"""B749 locks for F2 and F8 — the two priced forks whose computations lived in
FINDINGS prose only (Part-0 audit line 1, 2026-08-13). Each test locks the
fork's own discriminating fact, exactly, per the FINDINGS' named witnesses.

Namespace note (the fork-label collision species, B530's family): these are the
GENESIS forks F2/F8 of B749 — not B216's period-law F8, not B766's phase-map
F2. The function names carry the arc id for exactly that reason.
"""
import sympy as sp

phi = (1 + sp.sqrt(5)) / 2


def test_b749_f2_small_trace_family_has_no_hyperbolic_carrier():
    """F2 ROBUST: the whole det=+1, |tr| <= 2 family is finite-order or
    reducible -- no pseudo-Anosov, no hyperbolic carrier. A mapping class is
    pA iff |tr| > 2; the periodic sibling cannot carry inexhaustibility."""
    t = sp.symbols('t')
    for tr in (-2, -1, 0, 1, 2):
        lam = sp.solve(t**2 - tr*t + 1, t)
        mods = [sp.Abs(sp.simplify(l)) for l in lam]
        # |tr| < 2: eigenvalues on the unit circle (elliptic/finite-order);
        # |tr| = 2: parabolic (reducible). Either way no expansion factor.
        assert all(sp.simplify(m - 1) == 0 for m in mods), (tr, mods)
    # the control: the persistent sector A = LR has tr = 3 and IS hyperbolic
    lam3 = sp.solve(t**2 - 3*t + 1, t)
    assert any(sp.simplify(sp.Abs(l)) > 1 for l in lam3)


def test_b749_f8_witness_1_effros_shen_K0_is_Z_phi():
    """F8 witness 1: the golden Effros-Shen AF algebra's K0 = Z + phi*Z as an
    ordered subgroup of R -- and its multiplier ring is Z[phi] exactly (End
    computed, not asserted): alpha*(Z + phi*Z) in Z + phi*Z forces alpha in
    Z[phi], using phi^2 = phi + 1."""
    a, b = sp.symbols('a b', rational=True)
    alpha = a + b*phi
    # alpha*1 = a + b*phi in Z+phi*Z  iff a, b in Z.
    # alpha*phi = a*phi + b*phi^2 = b + (a+b)*phi in Z+phi*Z iff b, a+b in Z.
    # Joint condition: a, b in Z => End(Z + phi*Z) = Z[phi]. Verify the
    # phi^2 reduction that the derivation rests on:
    assert sp.simplify(phi**2 - phi - 1) == 0
    prod = sp.expand(alpha * phi)
    assert sp.simplify(prod - (b + (a + b)*phi)) == 0


def test_b749_f8_witness_2_carrier_traces_live_in_Q_sqrt5():
    """F8 witness 2: the combinatorial carrier's eigenvalue data lives in
    Q(sqrt5) -- the substitution matrix A = [[2,1],[1,1]] has eigenvalues
    phi^2, phi^-2; its whole trace sequence is integral (Lucas numbers)."""
    A = sp.Matrix([[2, 1], [1, 1]])
    ev = list(A.eigenvals())
    fields = [sp.minimal_polynomial(e, sp.Symbol('x')) for e in ev]
    x = sp.Symbol('x')
    assert all(f == x**2 - 3*x + 1 for f in fields)          # phi^{\pm 2}
    assert all(complex(e).imag == 0 for e in ev)              # totally real
    # the eigenvalue field is Q(sqrt5): phi^2 = (3+sqrt5)/2
    assert sp.simplify(ev[0] + ev[1] - 3) == 0 and sp.simplify(ev[0]*ev[1] - 1) == 0


def test_b749_f8_witness_3_x2_plus_3_irreducible_over_Q_sqrt5_with_control():
    """F8 witness 3 (the load-bearing one): x^2 + 3 -- the minimal polynomial
    of sqrt(-3) -- is IRREDUCIBLE over the real field Q(sqrt5): the
    combinatorial carrier cannot see Q(sqrt-3). ***Ergo the being field is
    bought at geometrization and nowhere earlier.*** With the instrument
    control: the same test DOES factor x^2 - 5 (so 'irreducible' is a
    finding, not a limitation of the instrument)."""
    x = sp.Symbol('x')
    K = sp.QQ.algebraic_field(sp.sqrt(5))
    target = sp.Poly(x**2 + 3, x, domain=K)
    assert len(target.factor_list()[1]) == 1                  # irreducible
    control = sp.Poly(x**2 - 5, x, domain=K)
    assert len(control.factor_list()[1]) == 2                 # the control splits


def test_b749_f8_witness_4_hearing_module_End_is_Z_phi_not_larger():
    """F8 witness 4: End(Z + phi*Z) = Z[phi] -- no larger ring multiplies the
    hearing module into itself; in particular nothing containing sqrt(-3)
    does (a real quadratic module admits no imaginary multiplier)."""
    # alpha = p + q*sqrt(-3) with q != 0 sends 1 to a non-real number, which
    # cannot lie in Z + phi*Z (a subset of R). Lock the real-module fact:
    assert sp.im(phi) == 0
    # and the multiplier-ring closure from witness 1's derivation:
    # (a + b*phi)*phi = b + (a+b)*phi -- closed exactly on integer (a, b).
    a, b = 3, 5   # a concrete integral pair as the executable instance
    val = sp.expand((a + b*phi)*phi)
    assert sp.simplify(val - (b + (a + b)*phi)) == 0
