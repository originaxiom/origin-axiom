"""Locks for B746 -- the golden ledger's spot-checks (S1-S3; S4 is an absence,
grep-verifiable, recorded in the arc's spot_checks.txt)."""
import sympy as sp

t, x = sp.symbols("t x")
PHI = (1 + sp.sqrt(5)) / 2


def test_s1_seed_kappa_three_gives_disc_five_and_dilatation_phi_squared():
    assert sp.discriminant(t**2 - 3 * t + 1, t) == 5
    assert sp.simplify(sp.Rational(3, 2) + sp.sqrt(5) / 2 - PHI**2) == 0


def test_s2_b155_canonical_object_golden_times_phi6_glue_minus_fifteen():
    assert sp.expand((x**2 - 3 * x + 1) * (x**2 - x + 1)) == \
        x**4 - 4 * x**3 + 5 * x**2 - 4 * x + 1
    assert 5 * (-3) == -15


def test_s3_chord_and_tower_top_eigenvalues_are_golden_powers():
    assert sp.simplify(PHI**3 - (2 + sp.sqrt(5))) == 0          # chord top, SL(3)
    assert sp.simplify(PHI**8 - 7 * PHI**4 + 1) == 0            # phi^4 root of char(A^4)
