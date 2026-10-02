import importlib.util
from pathlib import Path

P=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/flat_vacuum.py'
SPEC=importlib.util.spec_from_file_location('r76_flat_vacuum',P)
C=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(C)


def test_actual_positive_metric_action_map_and_wrong_tension_control():
    out=C.metric_controls()
    assert all(out['checks'].values())
    assert out['checks']['nonzero_tension_control']


def test_target_curvature_sign_and_boundary_stationary_opposite_control():
    out=C.curvature_controls()
    assert all(out['checks'].values())
    assert out['interval_boundary']=='2*ddv'


def test_actual_cusp_splits_without_splitting_the_global_extension():
    out=C.peripheral_controls()
    assert all(out['checks'].values())
    assert len(out['peripheral_primitive'])==4


def test_compact_current_and_even_scaling_potential_from_actual_commutator():
    out=C.scaling_controls()
    assert all(out['checks'].values())
    assert out['checks']['source_projector']


def test_complete_fixed_control_population():
    out=C.run()
    assert out['all_checks_pass'] and out['passed']==out['total']==44
