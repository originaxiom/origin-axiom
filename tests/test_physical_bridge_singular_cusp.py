"""R14 direct equations and flux locks; no physical generation identification."""
import importlib.util
from pathlib import Path
import sys

import numpy as np
import pytest

PATH = Path(__file__).resolve().parents[1] / "reports/physical_bridge_2026_09_05/singular_cusp.py"
SPEC = importlib.util.spec_from_file_location("r14_singular_cusp", PATH)
SC = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = SC
SPEC.loader.exec_module(SC)


@pytest.fixture(scope="module")
def result():
    return SC.run()


def test_theta_kernel_is_periodic_and_matches_independent_library(result):
    assert result["torus"]["cutoff_error"] < 2e-11
    assert result["torus"]["mpmath_error"] < 2e-11
    for row in result["torus"]["periodicity"]:
        assert row["value_error"] < 2e-11 and row["gradient_error"] < 2e-11


def test_radial_zero_mode_and_local_geodesic_equations(result):
    rows = result["symbolic"]
    assert rows["zero_mode_ode_residual"] == "0"
    assert rows["local_geodesic_residual"] == "0"
    assert rows["missing_zero_mode_off_source_residual"] != "0"
    assert rows["flux_log_derivative"] == "2*pi*density"


def test_actual_off_source_pde_analytic_and_two_independent_steps(result):
    for row in result["pde"]:
        assert abs(row["analytic"]) < 2e-10
        assert len(row["finite"]) == 2
        assert max(abs(r["residual"]) for r in row["finite"]) < 3e-3


def test_three_fixed_points_and_two_rotation_orbits(result):
    assert result["fixed"]["fixed_points"] == [["0", "0"], ["1/3", "1/3"], ["2/3", "2/3"]]
    assert result["fixed"]["order6_permutation"] == [0, 2, 1]
    rows = result["fixed"]["symmetry"]
    assert rows[0]["potential_rotation_error"] < 2e-11
    assert rows[1]["potential_rotation_error"] < 2e-11
    assert rows[2]["potential_rotation_error"] > 1e-2


def test_charge_tubes_are_inward_not_empty_for_positive_density(result):
    rows = result["flux"][0]
    assert rows["upper_flux"] > 0
    assert all(t["flux"] < 0 and t["normal_component_at_z1_max"] < 0 for t in rows["tubes"])
    assert result["flux"][1]["upper_flux"] < 0
    assert all(t["flux"] > 0 for t in result["flux"][1]["tubes"])


def test_flux_balance_keeps_finite_radius_tubes_and_punctured_tori(result):
    for row in result["flux"]:
        assert abs(row["total_flux"]) < 2e-9
        assert max(abs(t["flux"]-t["expected"]) for t in row["tubes"]) < 2e-9
    assert abs(result["flux"][0]["without_tubes"]) > 1
    assert abs(result["flux"][1]["without_tubes"]) > 1


def test_balanced_sources_have_no_required_radial_zero_mode(result):
    field = SC.CuspField((-2., 1., 1.))
    assert field.total == 0
    assert field.radial(2.) == (0., 0., 0.)
    assert abs(result["flux"][2]["without_tubes"]) < 1e-12


def test_unspecified_homogeneous_mode_changes_flux_not_source_equation(result):
    rows = result["free_radial_flux_data"]
    assert rows[0]["normal_at_z1"] < 0 < rows[1]["normal_at_z1"] < rows[2]["normal_at_z1"]
    assert all(row["normal_at_z10"] > 0 for row in rows)
    for c in (-20., 0., 20.):
        _, d, dd = SC.CuspField(c=c).evaluate(.137+.193j, 1.7)
        assert abs(np.trace(dd)-d[2]/1.7) < 2e-10


def test_source_and_invalid_torus_are_not_silently_evaluated():
    with pytest.raises(ValueError, match="excluded source"):
        SC.green(0.)
    with pytest.raises(ValueError, match="upper-half-plane"):
        SC.green(.2+.1j, tau=.5-1j)
