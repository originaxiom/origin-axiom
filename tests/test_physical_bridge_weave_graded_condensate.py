"""Locks on the matched-grading computation, not on the report's wording."""
import importlib.util
from pathlib import Path
import sympy as s

BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/weave_graded_condensate_2026_10_08'


def load(name):
    spec=importlib.util.spec_from_file_location('graded_'+name,BASE/(name+'.py'))
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


p=load('probe')
r=load('reference')


def facts(*names):
    data=p.run()['facts']
    return all(data[name] for name in names)


def test_full_root_system_and_regular_A2():
    rr=p.roots()
    assert len(rr)==240 and p.add(p.BETA,p.GAMMA)==p.V
    assert p.dot(p.BETA,p.GAMMA)==-4 and p.V in rr


def test_compact_triple_and_four_root_control():
    H,E,F=p.triple()
    assert p.comm(H,E)==2*E and p.comm(E,F)==H and E.conjugate().T==F
    assert facts('four_root_cross_brackets_zero','four_root_H_is_2v')


def test_actual_SO3_center_and_integral_cocharacter():
    assert all(p.dot(a,p.V)%4==0 for a in p.roots())
    assert facts('SO3_center_kernel_on_full_E8','all_condensate_roots_odd')


def test_peripheral_uses_old_SU6_element_and_area():
    assert facts('peripheral_is_actual_old_p','peripheral_area_limit')
    h=(-4,-4,-4,6,6,0,0,0)
    assert all((p.dot(a,h)-p.dot(a,p.V))%8==0 for a in p.roots())


def test_color_preservation_not_weak_preservation():
    assert facts('color_commutes')
    assert p.dot(p.BETA,p.V)==4


def test_same_action_stationary_nonflat_residuals():
    assert facts('Dbar_q_vanishes','curvature_moment_vanishes')
    H,E,F=p.triple()
    assert p.comm(E,F)!=s.zeros(3)


def test_wrong_backgrounds_do_not_pass():
    assert facts('flat_connection_control_fails','wrong_amplitude_control_fails')


def test_spin_cancellation_and_finite_norm():
    assert facts('spin_gauge_weights_cancel','trace_norm_positive_four_roots','finite_positive_end_norm')


def test_entire248_sl2_decomposition():
    w,j=p.weight_and_spins(p.roots())
    assert w=={-4:1,-2:56,0:134,2:56,4:1}
    assert j=={0:78,1:55,2:1}


def test_E6_identification_by_roots_not_dimension():
    rr,simple,c,arms=p.e6_data(p.roots())
    assert len(rr)==72 and len(simple)==6 and arms==[1,2,2]
    assert c.det()==3
    assert facts('E6_root_reflection_closure','E6_commutes_with_full_A2','E6_saturates_sl2_commutant')


def test_actual_complex_charged_branching():
    assert facts('A2_full_branching','charged_27_single_Weyl_orbit','conjugate_27_is_distinct')


def test_canonical_kinetic_metrics():
    assert facts('kinetic_rescalings_to_dt','density_shift_control_fails')
    c=p.normalized_coefficients()
    assert s.simplify(c['gauge']-c['wrong'])==c['u']/2


def test_gauge_and_W_Yukawa_coefficients_agree():
    c=p.normalized_coefficients()
    assert c['gauge_matter']==c['w_cubic']==1/s.sqrt(2)
    assert s.simplify(c['gauge']-c['spin'])==0


def test_complete_blocks_include_extreme_slots():
    assert [sum(b['channels'] for b in p.radial_blocks(j)) for j in range(3)]==[1,3,5]
    for j in range(3):
        for b in p.radial_blocks(j):
            assert p.zero(b['square']-(b['xi']**2+b['threshold'])*s.eye(b['channels']))
    assert facts('wrong_adjoint_control_fails','missing_Yukawa_control_fails')


def test_R_trace_pairing_and_independent_polynomial_metric():
    assert facts('R_trace_pairing_matches_old_Hessian')
    assert r.run()['predicates']['R_negative_weight_pairing']
    assert r.polynomial(2)[3]==[r.F(1),r.F(1,2),r.F(1)]


def test_full_and_R_threshold_counts_are_distinct():
    full,R=p.spectrum({0:78,1:55,2:1})
    assert full=={'1/4':133,'5/4':110,'9/4':3,'13/4':2}
    assert R=={'1/4':55,'5/4':55,'9/4':1,'13/4':1}
    assert sum(full.values())==248 and sum(R.values())==112


def test_gap_bounds_and_old_gapless_control():
    assert facts('positive_essential_threshold_not_zero','escaping_form_sequence_excess',
          'nonzero_angular_square_exact','uniform_angular_coefficient_bound',
          'confining_lower_bound_identity','old_odd_spectators_retained_as_control',
          'new_no_odd_spin0_spectators')


def test_actual_linear_dual_intertwiner():
    J=s.Matrix([[0,0,1],[0,-1,0],[1,0,0]])
    assert J.conjugate().T*J==s.eye(3)
    for T in p.triple():
        assert J*T==-T.T*J


def test_dual_map_descends_but_not_to_all_SU3():
    assert facts('dual_intertwines_spin_transitions','dual_intertwines_peripheral',
          'all_four_spin_choices_preserve_pair_map','outside_SO3_pairing_control_fails')
    assert r.run()['predicates']['dual_form_is_unitary_in_actual_metric']


def test_two_exact_algorithms_agree_without_physics_overclaim():
    a,b=p.run(),r.run()
    for key in ('root_profile','spectrum_profile','pairing_profile'):
        assert a[key]==b[key]
    assert all(a['facts'].values()) and all(b['predicates'].values())
    assert not any(a[k] for k in ('physical_chirality_achieved','global_zero_counts_computed',
                                  'genesis_selection_derived','physical_goal_achieved','nonauthor_acceptance'))
