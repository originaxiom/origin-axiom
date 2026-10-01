import importlib.util
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/cone_orbit_control.py'
spec=importlib.util.spec_from_file_location('r73_control',p)
C=importlib.util.module_from_spec(spec)
spec.loader.exec_module(C)

def test_actual_compact_orbit_retains_radial_transport_and_boundary_data():
    assert all(C.old.orbit_controls()['checks'].values())

def test_finite_kinetic_tangent_normalizes_exact_leading_coefficient():
    out=C.tangent_controls()
    assert out['normalized_leading']==C.s.Rational(8,5)
    assert all(out['checks'].values())

def test_nonzero_interacting_residuals_transform_with_positive_metric():
    assert all(C.old.covariance_controls()['checks'].values())

def test_fermion_current_and_exact_Z_column_with_wrong_target_bite():
    out=C.operator_controls()
    assert out['form_dimension']==72 and all(out['checks'].values())

def test_spacetime_gauge_compensator_removes_false_scalar_kinetics():
    assert all(C.old.compensator_controls()['checks'].values())

def test_complete_separate_normalization_and_old_failure_custody():
    out=C.run()
    assert set(out['groups'])=={'orbit','tangent','covariance','operator','compensator'}
    assert out['all_checks_pass']
