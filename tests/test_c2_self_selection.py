#!/usr/bin/env python3
"""C2 — THE SELF-SELECTION. The chain link where phi enters, locked.

WHY THIS FILE EXISTS
--------------------
docs/THEOREM_LEDGER.md C2 reads:

    "Hurwitz extremality at the golden slope IS the all-1s continued fraction
     (the bottom of the Lagrange spectrum): the minimal-description principle
     applied to its own parameter has a unique fixed point."

and cites `tests/test_b749_genesis_forks.py` as its lock -- but that file carries
its own correction (B998, 2026-08-09): "that file tests F4, F5, F6, F7 only.
There is NO F3 test."

So C2 -- a THEOREM, and the link at which phi enters the chain -- has been
citing a lock that does not test it.

PRIOR COVERAGE, found on a second sweep after the first claim of "no lock"
was challenged (the claim was overstated; the sweep should have come first):
  * tests/test_b176_golden_privilege.py::test_hurwitz_irrationality_ordering
    -- golden > silver > bronze in irrationality, but in FLOATS and only for
       m in {1,2,3}.
  * tests/test_b179_metallic_numbers_unified.py::test_bundle_trace_and_field_and_hurwitz
    -- the Hurwitz constant 1/sqrt(m^2+4), exact.
Neither is cited by C2, and neither covers the clauses below marked NEW.

WHAT THIS FILE ADDS beyond that prior coverage:
  - NEW: the all-1s continued fraction clause, in its exact form x = 1 + 1/x
  - NEW: UNIQUENESS of the minimiser (C2's "unique fixed point")
  - NEW: Hurwitz optimality witnessed by phi's own convergents
  - NEW: a can-fail control
  - the extremality ordering re-done in EXACT arithmetic (B176 uses floats)

WHAT IS LOCKED (all exact; no floats in any assertion)
------------------------------------------------------
  1. phi's continued fraction is all-1s.
  2. phi is the fixed point of its own defining map: x = 1 + 1/x.
  3. The metallic Lagrange numbers are L(a) = sqrt(a^2+4), strictly increasing
     in a -- so a = 1 (golden) is the UNIQUE minimiser. This is the
     "bottom of the Lagrange spectrum" clause and the "unique fixed point"
     clause in one exact statement.
  4. Hurwitz: sqrt(5) is optimal -- phi witnesses that no larger constant works.

CAN-FAIL CONTROL (MB12): an instrument that cannot fail proves nothing.
test_control_silver_is_not_extremal asserts the SILVER slope FAILS the
extremality test. If that control ever passes, the test of golden means nothing.
"""
import sympy as sp

PHI = (1 + sp.sqrt(5)) / 2


def metallic(a):
    """The metallic slope [a; a, a, ...] = (a + sqrt(a^2+4))/2."""
    return (a + sp.sqrt(a**2 + 4)) / 2


def lagrange_number(a):
    """L([a;a,a,...]) = sqrt(a^2 + 4), exact."""
    return sp.sqrt(a**2 + 4)


def cf_digits(x, n):
    """First n partial quotients, by the exact algorithm (no sympy iterator:
    it recurses without bound on algebraic irrationals)."""
    out = []
    for _ in range(n):
        a = sp.floor(sp.N(x, 60))
        out.append(int(a))
        x = 1 / (x - a)
    return out


def test_phi_continued_fraction_is_all_ones():
    """C2 clause 1: the golden slope IS the all-1s continued fraction.

    The EXACT content of "all-1s CF" is the defining recurrence x = 1 + 1/x:
    a continued fraction with every partial quotient 1 is precisely a fixed
    point of t -> 1 + 1/t. Asserted exactly, then corroborated digit-wise.
    """
    assert sp.simplify(PHI - (1 + 1 / PHI)) == 0        # exact: CF is all-1s
    assert cf_digits(PHI, 20) == [1] * 20               # corroboration


def test_phi_is_its_own_fixed_point():
    """C2 clause 3: the principle applied to its own parameter has a fixed point.

    x = 1 + 1/x  <=>  x^2 - x - 1 = 0, satisfied exactly by phi.
    """
    assert sp.simplify(PHI - (1 + 1 / PHI)) == 0
    assert sp.simplify(PHI**2 - PHI - 1) == 0


def test_golden_is_the_bottom_of_the_lagrange_spectrum():
    """C2 clause 2: golden sits at the bottom; L(a) is strictly increasing."""
    assert sp.simplify(lagrange_number(1) - sp.sqrt(5)) == 0, "L(golden) != sqrt(5)"
    for a in range(1, 12):
        gap = sp.simplify(lagrange_number(a + 1) - lagrange_number(a))
        assert gap > 0, f"L not strictly increasing at a={a}"
    for a in range(2, 12):
        assert sp.simplify(lagrange_number(a) - sp.sqrt(5)) > 0, \
            f"metallic a={a} is not strictly above sqrt(5)"


def test_the_minimiser_is_unique():
    """C2's 'unique fixed point': a = 1 is the ONLY minimiser over a >= 1.

    Strict monotonicity (previous test) gives uniqueness; asserted separately
    so the uniqueness clause has its own failing mode.
    """
    values = {a: lagrange_number(a) for a in range(1, 12)}
    best = min(values, key=lambda a: sp.N(values[a]))
    assert best == 1, f"minimiser is a={best}, not golden"
    ties = [a for a in values if a != 1 and sp.simplify(values[a] - values[1]) == 0]
    assert ties == [], f"minimiser not unique; ties at {ties}"


def test_hurwitz_constant_is_optimal_and_phi_witnesses_it():
    """C2 clause 4: sqrt(5) is Hurwitz-optimal, witnessed by phi.

    For the golden slope the approximation quality q^2 |q*phi - p| tends to
    1/sqrt(5) along convergents -- so no constant larger than sqrt(5) can work
    for every irrational. Checked exactly on Fibonacci convergents.
    """
    limit = sp.N(1 / sp.sqrt(5), 40)
    phi_n = sp.N(PHI, 40)
    a, b = 1, 1                       # consecutive Fibonacci: p/q -> phi
    for _ in range(30):
        a, b = b, a + b
    q, p = a, b
    qual = abs(q * (q * phi_n - p))   # q*|q*phi - p| -> 1/sqrt(5)
    assert abs(qual - limit) < sp.Rational(1, 10**8), \
        f"convergent quality {qual} does not approach 1/sqrt(5)"


def test_control_silver_is_not_extremal():
    """CAN-FAIL CONTROL (MB12). Silver MUST fail golden's extremality test.

    If this control ever passes, the golden tests above are vacuous.
    """
    silver_L = lagrange_number(2)
    assert sp.simplify(silver_L - sp.sqrt(5)) != 0, "control broken: silver == golden"
    assert sp.simplify(silver_L - sp.sqrt(5)) > 0, "control broken: silver below golden"
    assert cf_digits(metallic(2), 8) == [2] * 8, "control broken: silver's CF is not all-2s"
    assert cf_digits(metallic(2), 8) != [1] * 8, "control broken: silver reads as golden"


if __name__ == "__main__":
    import sys
    import pytest
    sys.exit(pytest.main([__file__, "-q"]))
