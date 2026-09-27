import sympy as sp
from flint import fmpq_mat

from verify_exceptional import (
    algebra_dimension, bilinear_dimension, certificates, companion, evaluate,
    factor_metadata, identity, inputs, inverse, matrix, modules, mul,
    point_diagnostics, selected_minor, specialization, t, word,
)
from verify_global_seed import eye, wedge_over_field, kron
from verify_topology import cover


def test_signed_monomial_group_laws():
    a = ((1, 2, 0), (2, -1, 3), (-1, 1, -1))
    b = ((1, 0, 2), (0, 1, -2), (1, -1, 1))
    assert mul(a, inverse(a)) == identity(3)
    assert all(sp.expand(x) == 0 for x in matrix(mul(a, b))-matrix(a)*matrix(b))


def test_laurent_minor_clearing_and_synthetic_jump():
    a = sp.Matrix([[t**-2, 1], [1, t]])
    record, determinant = selected_minor(a, 2)
    assert record["rank"] == 2
    assert determinant == sp.Poly(t-t**2, t)
    assert evaluate(a, 1).rank() == 1


def test_companion_and_cyclotomic_controls():
    value = companion(["1", "1", "1"])
    assert value**3 == eye(2)
    assert factor_metadata(["1", "1", "1"])["root_order_if_cyclotomic"] == 3
    assert not factor_metadata(["1", "-3", "1"])["cyclotomic"]


def test_actual_wedge_not_rational_restriction_wedge():
    for seed in inputs()["seeds"]:
        mods = modules(seed)
        e = specialization(mods["E"], fmpq_mat([[2]]))
        w = specialization(mods["wedge2E"], fmpq_mat([[2]]))
        for a, b in zip(e.mats, w.mats):
            assert wedge_over_field(kron(a, eye(4))) == kron(b, eye(4))


def test_replays_both_known_rational_points():
    for seed in inputs()["seeds"]:
        result = point_diagnostics(modules(seed), fmpq_mat([[2]]))
        assert result["matrix_algebra_dimension"] == 25
        assert result["invariant_bilinear_dimension"] == 0
        assert result["fixed_meridian"] == {"J_rank": 32, "gauge_rank": 8, "relative_H1": 0}
        for coeff in result["coefficients"].values():
            assert coeff["M6"]["I"] == 0
            assert coeff["M6_interior"] == coeff["M6_dual_interior"] == 0


def test_number_field_finite_order_control():
    value = companion(["1", "1", "1"])
    for seed in inputs()["seeds"]:
        mods = modules(seed)
        result = point_diagnostics(mods, value)
        assert result["field_degree"] == 2
        # Conjugating the cubic root inverts all unit-modulus entries.
        # The dual is consequently Galois-conjugate, a forced-zero control.
        for coefficient in result["coefficients"].values():
            assert coefficient["M2"]["I"] == coefficient["M6"]["I"] == 0
