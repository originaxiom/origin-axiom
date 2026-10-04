import pytest
import verify_boundary_continuation as b


@pytest.mark.parametrize("seed", [0, 1])
@pytest.mark.parametrize("component", [1, 2])
@pytest.mark.parametrize("dual", [False, True])
def test_explicit_ordinary_lift_and_irremovable_torus_period(seed, component, dual):
    row = b.escape(seed, component, dual)
    assert row["ordinary_lift_exists"] and row["torus_period_is_closed"]
    assert row["unavoidable_torus_quotient_complex_dimension"] == 1
    assert row["changing_ordinary_lift_cannot_remove_quotient"] and row["boundary_gauge_cannot_remove_quotient"]


@pytest.mark.parametrize("seed", [0, 1])
@pytest.mark.parametrize("component", [1, 2])
@pytest.mark.parametrize("dual", [False, True])
def test_actual_charged_cusp_channel_and_radial_controls(seed, component, dual):
    row = b.charged_cusp(seed, component, dual)
    assert row["global_H0"] == 0 and row["charged_boundary_H0"] == 3
    assert row["one_form_escaping_Rayleigh_constant"] == 12
    assert row["squared_Laplacian_residual_constant"] == 504
    assert not row["physical_end_law_changed"]


def test_solver_and_boundary_instruments_discriminate():
    assert all(b.controls().values())
