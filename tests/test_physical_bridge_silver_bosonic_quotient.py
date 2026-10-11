"""Real gauge/boundary zero-mode controls, not full Hamiltonian certification."""
import importlib.util
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/silver_bosonic_quotient_2026_10_11'
def load(name):
    spec=importlib.util.spec_from_file_location('bosonic_quotient_'+name,BASE/(name+'.py'))
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj);return obj
p=load('probe');r=load('reference')
def facts(*names):return all(p.run()['facts'][n] for n in names)
def refs(*names):return all(r.run()['predicates'][n] for n in names)
def test_actual_adjoint_and_full_nonabelian_jets():
    assert facts('actual_real_divergence_split','kappa_and_moment_Hermitian','generic_moment_Ward_with_full_jets','generic_gauge_fixing_Ward','full_zero_form_cross_terms_cancel','curvature_Ward_all_pairs','generic_residuals_not_assumed_zero','frozen_derivative_gauge_rejected')
    assert refs('formal_actual_adjoint','formal_cross_term_is_moment','cross_term_not_silently_dropped')
def test_harmonic_real_P_and_positive_form():
    assert facts('flat_harmonic_fixture_verified','compact_gauge_is_full_Hessian_null','flat_real_P_gauge_fixing','wrong_Higgs_potential_sign_rejected','positive_real_form_with_nonunitary_B','nonzero_gauge_first_and_second_jets')
    assert refs('harmonic_real_positive_P','formal_wrong_Higgs_sign_rejected')
def test_complex_gauge_cannot_delete_moment_modes():
    assert facts('complex_gauge_flat_but_not_moment_zero','imaginary_gauge_not_compact_slice')
    assert all(v for k,v in r.run()['predicates'].items() if k.endswith('complex_gauge_not_moment_null'))
def test_actual_source_flux_solution_and_opposing_compatibility():
    assert facts('source_flux_Fredholm_compatibility','wrong_flux_sign_rejected','real_inhomogeneous_boundary_solution','normal_gauge_jets_retained','frozen_normal_flux_cannot_solve_source')
    assert refs('boundary_linsolve_exists_with_kernel','boundary_mean_fixed_unique_solution','boundary_source_and_flux_exact','boundary_inconsistent_flux_rejected','boundary_wrong_flux_sign_rejected','boundary_normal_derivatives_not_frozen')
def test_integrated_slice_preserves_physical_harmonic_data():
    assert facts('slice_cancels_kappa_and_integrated_real_flux','imaginary_normal_primary_preserved','physical_harmonic_constant_not_removed','integrated_mixed_Green_form_zero','nonzero_projected_flux_Green_rejected','all_nonzero_covector_Dirichlet_symbol')
    assert refs('boundary_real_slice_preserves_harmonic_mean')
def test_real_quotient_and_kernel_dimensions_are_computed():
    assert all(c['real_physical_quotient']==2*c['harmonic_complex_dimension'] and c['endpoint_kernel']>0 for c in p.run()['finite_complex_controls'])
    assert all(c['real_quotient_rank']==2*c['complex_H1'] and c['real_kernel_before_gauge']-c['real_gauge_rank']==c['real_quotient_rank'] for c in r.run()['different_finite_controls'])
    assert all(v for k,v in p.run()['facts'].items() if k.startswith('toy_'))
    assert all(v for k,v in r.run()['predicates'].items() if k.startswith('block_'))
def test_scope_and_complete_nonvacuous_results():
    assert all(p.run()['facts'].values()) and all(r.run()['predicates'].values())
    assert p.run()['conditional_smooth_linear_quotient'] and p.run()['compact_real_gauge_only'] and r.run()['conditional_linear_quotient']
    assert p.run()['predicates_passed']==len(p.run()['facts']) and r.run()['predicates_passed']==len(r.run()['predicates'])
    for k in ('global_PDE_solved_numerically','silver_census_recomputed','nonlinear_moduli_integrated','complete_Hamiltonian_proved','nonauthor_review','boundary_selected','full_goal_achieved'):
        assert p.run()[k] is False
    for k in ('native_imported','global_silver_PDE_recomputed','physical_population_recomputed','full_multiplet_or_Hamiltonian','nonlinear_moduli','outside_review','generated_selection','full_goal_achieved'):
        assert r.run()[k] is False
