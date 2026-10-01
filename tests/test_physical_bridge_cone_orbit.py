import importlib.util
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/cone_orbit.py'
spec=importlib.util.spec_from_file_location('r73_orbit',p)
C=importlib.util.module_from_spec(spec)
spec.loader.exec_module(C)

def test_actual_compact_orbit_retains_radial_transport_and_boundary_data():
    assert all(C.orbit_controls()['checks'].values())

def test_finite_kinetic_tangent_does_not_admit_its_straight_displacement():
    out=C.tangent_controls()
    assert C.zero(out['straight_increment'].diff(C.eps).subs(C.eps,0))
    assert all(out['checks'].values())

def test_nonzero_interacting_residuals_transform_with_positive_metric():
    assert all(C.covariance_controls()['checks'].values())

def test_fermion_current_transport_not_frozen_angular_Hermiticity():
    out=C.operator_controls()
    assert out['form_dimension']==72 and all(out['checks'].values())

def test_spacetime_gauge_compensator_removes_false_scalar_kinetics():
    assert all(C.compensator_controls()['checks'].values())

def test_complete_frozen_control_population():
    out=C.run()
    assert set(out['groups'])=={'orbit','tangent','covariance','operator','compensator'}
    assert out['all_checks_pass']
