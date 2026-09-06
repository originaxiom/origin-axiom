"""Direct, non-pullback verification of the R13 candidate; new seal."""
import importlib.util
from pathlib import Path

import numpy as np
import pytest

PATH = Path(__file__).resolve().parents[1] / "reports/physical_bridge_2026_09_05/harmonic_cusp_transport.py"
SPEC = importlib.util.spec_from_file_location("r13_harmonic_transport_test", PATH)
HT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(HT)


@pytest.fixture(scope="module")
def transport():
    return HT.run()


def test_primitive_transports_under_actual_generators_not_only_height_moves(transport):
    for row in transport["direct_generator_checks"]:
        assert row["samples_retained"] >= 25
        assert row["minimum_both_heights"] >= .55
        assert row["primitive_transport_max"] < 2e-9


def test_one_form_pullback_uses_the_jacobian_at_two_steps(transport):
    for row in transport["direct_generator_checks"]:
        assert len(row["one_form_pullback"]) == 2
        assert max(r["maximum"] for r in row["one_form_pullback"]) < 2e-6


def test_locally_harmonic_corruption_fails_global_transport(transport):
    nontranslation = [r for r in transport["direct_generator_checks"] if r["generator"] in "bB"]
    assert min(r["corrupted_transport_max"] for r in nontranslation) > 1e-4


def test_meridian_period_and_tangential_field_are_retained(transport):
    for row in transport["period_and_components"]:
        assert row["max_period_error"] < 1e-11
        assert row["tangential_orthonormal_rms"] >= row["height"]-1e-11
        assert row["normal_orthonormal_rms"] > 0


def test_analytic_one_form_matches_independent_potential_difference():
    basis, coef = HT.candidate()
    for point in (np.array([.12, .37, .8]), np.array([-.22, -.49, 1.1]), np.array([.31, .14, 1.5])):
        form = HT.one_form(basis, coef, np.array([point[0]+1j*point[1]]), np.array([point[2]]))[0]
        def value(p):
            return HT.potential(basis, coef, np.array([p[0]+1j*p[1]]), np.array([p[2]]))[0]
        step = 1e-6
        fd = np.array([(value(point+e)-value(point-e))/(2*step) for e in step*np.eye(3)])
        assert np.max(abs(form-fd)) < 1e-7
