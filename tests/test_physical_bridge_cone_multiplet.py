import importlib.util
from pathlib import Path

path=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/cone_multiplet.py'
spec=importlib.util.spec_from_file_location('r70_cone_multiplet',path)
C=importlib.util.module_from_spec(spec)
spec.loader.exec_module(C)


def test_arbitrary_period_projection_and_similarity_annihilator():
    out=C.period_controls()
    assert out['period_norm']==12 and out['matrix_dimension']==4
    assert all(out['checks'].values())


def test_both_superfield_profiles_force_zero_neutral_trace():
    out=C.profile_controls()
    assert out['constraints'].rank()==4 and out['trace_dimension']==4
    assert out['checks']['one_profile_plus_reality_full_rank']
    assert out['required_maximal_dimension']==2


def test_self_adjoint_relative_control_does_not_prove_full_supersymmetry():
    out=C.profile_controls()['checks']
    assert out['relative_maximal_current'] and out['relative_passes_one_profile']
    assert out['relative_fails_reality'] and out['relative_fails_other_profile']


def test_actual_nonabelian_residuals_on_complex_neutral_profiles():
    out=C.boson_controls()['checks']
    assert out['full_radial_x'] and out['full_radial_y'] and out['full_tangential_zero']
    assert out['full_moment_unchanged'] and out['actual_residual_density']
    assert out['actual_kinetic_density'] and out['self_brackets_zero']


def test_finite_action_positive_outside_L4_and_bad_derivative_control():
    out=C.boson_controls()['checks']
    assert out['positive_H1_kinetic'] and out['positive_H1_action'] and out['positive_H1_apex']
    assert out['positive_outside_L4'] and out['bad_derivative_diverges']
    assert out['products_not_automatically_zero'] and out['complementary_source_retained']


def test_lines_pass_necessary_maps_without_selecting_one():
    out=C.profile_controls()
    assert out['tested_domains']==3
    assert out['checks']['all_line_profiles'] and out['checks']['all_line_current']
    assert out['checks']['all_line_reality'] and out['checks']['both_helicities_survive']


def test_affine_superpotential_boundary_not_just_homogeneous_line():
    out=C.boundary_controls()['checks']
    assert out['longitude_line_passes'] and out['helicity_background_term_survives']
    assert out['specified_counterterm_cancels'] and out['wrong_counterterm_sign_fails']
    assert out['boundary_two_form_unchanged'] and out['background_k_not_removed']


def test_all_frozen_two_sided_controls():
    result=C.run()
    assert set(result['groups'])=={'period','profile','boson','boundary'}
    assert len(result['checks'])==55
    assert result['all_checks_pass']
