"""R67 boundary and radial controls; no independent analytic certificate."""
import importlib.util
from pathlib import Path

import sympy as s

PATH = Path(__file__).resolve().parents[1] / 'reports/physical_bridge_2026_09_05/cone_flux.py'
SPEC = importlib.util.spec_from_file_location('physical_bridge_cone_flux', PATH)
probe = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(probe)


def test_metric_and_covariant_boundary_identity():
    answer = probe.flux_controls()
    assert all(answer['checks'].values()), answer['checks']
    assert probe.geometry()[2] == s.diag(0, -1/probe.alpha, -probe.alpha)


def test_on_shell_bulk_cost_keeps_boundary_flux():
    answer = probe.flux_controls()
    assert probe.zero(answer['residual_density'].subs(answer['on_shell']))
    assert probe.zero((answer['expanded_density']+probe.dr(answer['boundary'])).subs(answer['on_shell']))
    assert not probe.zero(answer['boundary'])


def test_reference_subtraction_and_exact_comparator():
    answer = probe.limit_controls()
    assert all(answer['checks'].values()), answer['checks']
    assert not probe.zero(answer['exact_boundary']-answer['reference_boundary'])


def test_actual_radial_Jacobi_profile():
    answer = probe.jacobi_controls()
    assert all(answer['checks'].values()), answer['checks']
    assert answer['translation_equation'] == 0
    assert answer['formal_adjoint'] != s.zeros(4)


def test_kinetic_and_quartic_admission_are_different():
    answer = probe.jacobi_controls()
    assert answer['checks']['kinetic_leading']
    assert answer['checks']['quartic_leading']
    assert answer['checks']['L4_divergence']
    assert answer['checks']['apex_flux_vanishes']


def test_triangular_CS_variation_and_L2_countercontrol():
    answer = probe.boundary_controls()
    assert all(answer['checks'].values()), answer['checks']
    assert answer['triangular_boundary'] == 0
    assert answer['lower_boundary'] == -2


def test_wrong_boundary_sign_is_rejected_directly():
    answer = probe.flux_controls()
    assert not probe.zero(answer['residual_density']-answer['expanded_density']+probe.dr(answer['boundary']))
    assert answer['Ricci_density'] != 0


def test_all_four_groups():
    answer = probe.run()
    assert len(answer['groups']) == 4
    assert answer['checks']
    assert all(answer['checks'].values()), answer['checks']
    assert answer['all_checks_pass']
