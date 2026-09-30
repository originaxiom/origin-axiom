"""R66 local equations and admission checks, not independent analytic review."""
import importlib.util
from pathlib import Path

import sympy as s

PATH = Path(__file__).resolve().parents[1] / 'reports/physical_bridge_2026_09_05/nilpotent_cone.py'
SPEC = importlib.util.spec_from_file_location('physical_bridge_nilpotent_cone', PATH)
probe = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(probe)


def test_actual_canonical_pair_and_grading():
    answer = probe.source_controls()
    assert all(answer['checks'].values()), answer['checks']
    assert (answer['meridian']-s.eye(4))**3 == s.zeros(4)
    assert (answer['meridian']-s.eye(4))**2 != s.zeros(4)


def test_both_equations_and_wrong_input_controls():
    answer = probe.equation_controls()
    assert all(answer['checks'].values()), answer['checks']
    assert all(x == s.zeros(4) for x in answer['curvature'].values())
    assert answer['cross_matrix'] != s.zeros(4)


def test_center_coordinates_and_invariance_residuals():
    answer = probe.center_controls()
    assert all(answer['checks'].values()), answer['checks']
    assert answer['vector_field'].jacobian([probe.u, probe.z]).subs({probe.u: 0, probe.z: 0}) == s.diag(0, 1)
    assert answer['graph2_residual'] != 0


def test_exact_comparator_and_failed_generic_truncation():
    answer = probe.comparator_controls()
    assert all(answer['checks'].values()), answer['checks']
    assert answer['scalar_residual'] != 0
    assert s.simplify(answer['scalar_residual'].subs(probe.beta**2, probe.alpha**3)) == 0


def test_full_peripheral_holonomy_and_singular_transport():
    answer = probe.holonomy_controls()
    assert all(answer['checks'].values()), answer['checks']
    assert (answer['meridian']-s.eye(4))**2 != s.zeros(4)
    assert s.simplify(answer['longitude'].det()) == 1


def test_L2_and_separate_graph_and_L4_failures():
    answer = probe.domain_controls()
    assert all(answer['checks'].values()), answer['checks']
    assert answer['differential_density'] != 0
    assert answer['adjoint_density'] != 0


def test_wrong_radial_sign_is_detected_directly():
    C = probe.fields()
    C[0] = -C[0]
    F, _ = probe.residuals(C, probe.metric())
    assert not probe.zero(F[0, 1])
    assert not probe.zero(F[0, 2])


def test_all_six_control_groups():
    answer = probe.run()
    assert len(answer['groups']) == 6
    assert answer['checks']
    assert all(answer['checks'].values()), answer['checks']
    assert answer['all_checks_pass']
