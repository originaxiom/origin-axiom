import importlib.util
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05'


def load(name):
    spec=importlib.util.spec_from_file_location(name,BASE/(name+'.py'))
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module


C=load('mixing_selection');R=load('mixing_selection_control')


def test_generic_linear_source_not_exact_axis_even_at_large_quartic():
    out=C.scalar();assert all(out['checks'].values())
    assert out['axis_gradient']=='-J2'


def test_zero_source_phase_comparison_and_normalization_are_retained():
    checks=C.scalar()['checks']
    assert checks['zero_transverse_source_axis_possible']
    assert checks['zero_source_radius_comparison'] and checks['coordinate_ratio_invariant']


def test_relaxation_uses_full_nonorthogonal_gram_projection():
    out=C.projection();assert all(out['checks'].values())
    assert out['relaxed']=='w**2'


def test_obstructed_and_wrong_sign_and_sixth_order_opposite_controls():
    checks=C.projection()['checks']
    assert checks['obstruction_stays_positive']
    assert checks['wrong_sign_correction_rejected'] and checks['sixth_order_survives']


def test_curvature_and_profile_placement_change_frozen_mixing_quartic():
    assert all(C.profiles()['checks'].values())


def test_schur_and_no_trivial_fixed_vectors_do_not_certify_irreducible():
    out=C.schur();assert all(out['checks'].values())
    assert out['commutant_dimension']==1


def test_fixed_native_population():
    out=C.report();assert out['passed']==out['total']==33 and out['all_checks_pass']


def test_separate_rational_population():
    out=R.run();assert out['passed']==out['total']==413 and out['all_checks_pass']
    assert (out['scalar_predicates'],out['projection_predicates'],out['flag_predicates'])==(36,375,2)
