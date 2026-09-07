"""R17 mathematical controls; no physical-kernel assertion from the tail bound."""
import importlib.util
from pathlib import Path
import math

import pytest
import sympy as sp

path = Path(__file__).resolve().parents[1]/"reports/physical_bridge_2026_09_05/cusp_tail.py"
spec = importlib.util.spec_from_file_location("cusp_tail_tests", path)
ct = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ct)


def test_metric_hodge_derivation_and_unitary_weights():
    row = ct.metric_derivation()
    assert row["residual"] == sp.zeros(8)
    assert row["unitary"] == [1]*8
    assert row["no_degree_shift_residual"] != sp.zeros(8)
    assert row["omitted_weight_norms"][0] != 1
    assert row["omitted_weight_norms"][1] == 1
    assert row["matrix"].diff(ct.ks)**2 == -sp.eye(8)


def test_full_operator_square_keeps_the_noncommuting_cross_term():
    row = ct.square_derivation()
    assert all(value == sp.zeros(8) for value in row["residual"].values())
    assert row["actual"][(0, 0, 2)] == -sp.eye(8)
    cross = row["missing_cross_witness"]
    assert cross[:4, 4:] == 2*sp.exp(ct.s)*ct.EPS[0]
    assert cross[4:, :4] == -2*sp.exp(ct.s)*ct.IOTA[0]
    assert cross != sp.zeros(8)


def test_closed_complex_algebra_and_clifford_perturbation():
    row = ct.algebra_controls()
    for key in ("d_squared", "delta_squared", "degree_d", "degree_delta"):
        assert row[key] == sp.zeros(4)
    assert row["cross_complement"] == sp.zeros(8)
    assert row["clifford_square"] == sp.zeros(8)
    a, b = sp.symbols("a b", real=True)
    assert sp.factor(row["perturbation_square"]) == (a-2*b)**2/2


def test_high_tail_inequality_has_a_positive_exact_factorization():
    row = ct.algebra_controls()
    t = sp.Symbol("t", nonnegative=True)
    assert row["high_tail_polynomial"] == 3*t*t/4+7*t+7
    # The unqualified estimate at |h'|=1 is false; the height restriction matters.
    assert (1-1)**2-3*1-2 < 1/4
    for q, b, c in ((0, 1, 0), (1, 0, 1), (1, -1, 0)):
        with pytest.raises(ValueError):
            ct.sufficient_height(q, b, c)


def test_actual_source_radial_data_including_charge_reversal_and_flux():
    rows = ct.radial_controls()
    assert len(rows) == 72
    assert max(row["derivative_error"] for row in rows) < 2e-12
    assert min(row["slope_margin"] for row in rows) >= -2e-12
    assert min(row["hprime_margin"] for row in rows) >= -2e-12
    assert min(row["hsecond_margin"] for row in rows) >= -2e-10
    assert all(row["bound"] >= row["simplified_bound"]*(1-2e-12) for row in rows)
    for s in (1., 3.):
        positive = ct.radial(s, .25, 2., -1.)
        negative = ct.radial(s, -.25, 2., -1.)
        assert all(float(p) == -float(n) for p, n in zip(positive, negative))


def test_unbounded_transverse_part_is_absorbed_not_assumed_small():
    rows = ct.complex_controls()
    assert max(row["nilpotent_norm"] for row in rows) < 1e-10
    assert all(row["complement_min"] >= -1e-10 for row in rows)
    assert all(row["complement_max"] > 0 for row in rows)
    assert rows[-1]["cross_nonzero"] > 100*rows[0]["cross_nonzero"]


def test_independent_integrated_energy_and_two_sided_cross_control():
    rows = ct.energy_controls()
    assert len(rows) == 12
    assert max(row["identity_error"] for row in rows) < 2e-11
    assert max(row["quadrature_change"] for row in rows) < 2e-11
    assert min(row["lower_margin"] for row in rows) >= 0
    assert min(row["simple_margin"] for row in rows) >= 0
    assert max(row["missing_cross_error"] for row in rows) > 1e-7
    assert all(abs(row["cross"]) > 1e-6 for row in rows)


def test_neutral_one_form_escapes_but_scalar_has_the_correct_threshold():
    row = ct.neutral_controls()
    assert row["profile_norm"] == sp.Rational(3, 8)
    assert row["profile_energy"] == sp.pi**2/2
    assert row["one_form_constant"] == 4*sp.pi**2/3
    for record in row["rows"]:
        assert abs(record["one_form"]/record["exact"]-1) < 2e-12
        assert abs(record["scalar"]-record["one_form"]-1) < 2e-12
    assert row["rows"][-1]["one_form"] < .06
    assert row["rows"][-1]["scalar"] > 1
    assert abs(row["rows"][0]["one_form"]/row["rows"][-1]["one_form"]-256) < 1e-9


def test_harmonic_corrector_derivatives_and_decaying_orthonormal_norm():
    row = ct.corrector_controls()
    assert row["derivative_residual"] == 0
    assert row["pde_residual"] == 0
    assert max(float(item["derivative_error"]) for item in row["modes"]) < 1e-45
    for k in (1, 2, 4):
        group = [float(item["orthonormal_gradient_bound"]) for item in row["modes"] if item["k"] == k]
        assert group[0] > group[1] > group[2] > 0
    # A constant Fourier mode has zero differential; a growing z^2 mode does not.
    z = sp.Symbol("z", positive=True)
    assert sp.diff(sp.Integer(1), z) == 0
    assert sp.simplify(z*sp.diff(z*z, z)) == 2*z*z
