"""B148 -- kappa/Fricke-Vogt identity + metallic monodromy = SL(2,Z) MCG action. Pure sympy (pyenv); no SnapPy/Sage."""
from frontier.B148_kappa_fricke_metallic.probe import (
    metallic_trace_fields,
    run_all,
    verify_fixed_slopes,
    verify_fricke_commutator,
    verify_kappa_4I_plus_2,
)


def test_fricke_commutator_identity():
    """tr(ABA^-1 B^-1) = x^2+y^2+z^2-xyz-2 exactly, from generic SL(2,C) matrices (det=1)."""
    assert verify_fricke_commutator() is True


def test_kappa_equals_4I_plus_2():
    """The exact convention: kappa = 4*I_FV + 2 under the half-trace substitution x=2X."""
    assert verify_kappa_4I_plus_2() is True


def test_fixed_slopes_are_roots_of_t2_plus_mt_minus_1():
    """Boundary fixed slopes of R^m L^m are the roots of t^2 + m t - 1 = 0."""
    assert verify_fixed_slopes() is True


def test_trace_fields_reduced_m1_m4_share_qsqrt5():
    """The eigenvalue/trace field is Q(sqrt(m^2+4)) reduced; m=1 and m=4 both give Q(sqrt5) (a false distinction if
    the unreduced discriminants 5 and 320 are read as different fields)."""
    fields = metallic_trace_fields()
    assert fields[0]["field_radicand"] == 5      # m=1
    assert fields[3]["field_radicand"] == 5      # m=4
    assert fields[1]["field_radicand"] == 2      # m=2 -> Q(sqrt2), NOT Q(sqrt32)
    assert all(row["trace"] == row["m"]**2 + 2 for row in fields)


def test_all_checks_pass():
    """The full independent re-derivation of the handoff's S1-S3 (16 symbolic checks)."""
    results, _ = run_all()
    failed = [k for k, v in results.items() if not v]
    assert failed == [], failed
