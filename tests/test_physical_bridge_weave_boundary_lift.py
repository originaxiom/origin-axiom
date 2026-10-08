"""Full-angular admission; a kinetic positive is not a physical spectrum."""
import importlib.util
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/weave_boundary_lift_2026_10_09'
def load(name):
    sp=importlib.util.spec_from_file_location('test_boundary_lift_'+name,BASE/(name+'.py'))
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
p=load('probe');r=load('reference')
def check(*names):return all(p.run()['facts'][name] for name in names)
def test_actual_physical_principal_and_normal_map():
    assert check('principal_from_actual_mass_and_metric','normal_target_phase_and_reality_map')
def test_full_four_weyl_kinetic_packaging():
    assert check('full_symbol_hermitian_and_norm','four_weyl_packaging_matches_full_operator')
def test_actual_charged_extreme_not_removed():
    assert check('actual_cusp_extreme_drifts','drifts_agree_with_existing_end_blocks','charged_witness_not_a_deleted_exotic')
    assert p.run()['charged_witness_weights']==r.run()['charged_witness_weights']
def test_old_horizontal_trace_fails_angular_symbol():
    assert check('old_allowed_lambda_has_decaying_angular_symbol','old_reference_trace_keeps_the_witness')
    assert r.run()['predicates']['old_angular_intersection_is_nonzero']
def test_local_positive_projector_and_all_covectors():
    assert check('local_projector_hermitian_involution','all_covectors_operator_and_adjoint_complement')
def test_actual_adjoint_and_lorentz_flux():
    assert check('adjoint_green_pairing','lorentz_current_vanishes')
def test_spin_seam_and_bad_constant_control():
    assert check('spin_seam_descends','constant_mixing_fails_seam')
def test_conjugate_field_relation_not_extra_species():
    assert check('actual_conjugate_fields_compatible','scalar_phase_fails_reality')
def test_pointwise_gauge_covariance():
    assert check('arbitrary_gauge_action_commutes')
def test_new_law_does_not_inherit_old_count():
    assert check('new_trace_does_not_reuse_old_witness','new_sigma_mixes_angular_parity')
    for key in ('old_anomaly_transfers_to_new_boundary','interacting_boundary_completion',
                'stable_chiral_spectrum_derived','nonauthor_acceptance','physical_goal_achieved'):
        assert p.run()[key] is False
def test_separate_cauchy_space_verification():
    assert check('finite_full_symbol_rank_controls')
    assert r.run()['predicates']['independent_cauchy_spaces_are_complementary']
    assert p.run()['full_symbol_ranks']==r.run()['full_symbol_ranks']
def test_every_predicate_and_profile():
    for d,k in ((p.run(),'facts'),(r.run(),'predicates')):
        assert d[k] and all(d[k].values()) and d['predicates_passed']==len(d[k])
    assert p.run()['j0_reference_signs']==r.run()['j0_reference_signs']
