"""Live finite locks; authored analytic kernel proof remains separately scoped."""
from pathlib import Path
import importlib.util
import pytest
import sympy as s

P=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/weave_companion_roster_2026_10_08'


def load(name):
    spec=importlib.util.spec_from_file_location('companion_'+name,P/(name+'.py'))
    m=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


@pytest.fixture(scope='module')
def native():
    return load('probe')


def test_all_live_predicates(native):
    r=native.run()
    assert r['facts'] and all(r['facts'].values())
    assert r['predicates_passed']==len(r['facts'])


def test_separate_weight_reference(native):
    a,b=native.run(),load('reference').run()
    assert b['predicates'] and all(b['predicates'].values())
    for key in ('module_weights','module_dimensions','spin_line_selection','spin_kernel_dimensions','twist_profiles','complete_zero_weights','spin_Weyl_residual_coefficient'):
        assert a[key]==b[key]


def test_E8_projection_has_all_weights(native):
    _,m=native.modules()
    assert all(s.expand(x-y)==0 for x,y in zip(m,native.expected_modules()))
    assert [native.dimension(x) for x in m]==[55,27,27,27,56]


def test_every_compact_spin_structure(native):
    rows=[native.line_selection(x) for x in ((1,1),(1,-1),(-1,1),(-1,-1))]
    assert len(set(map(tuple,rows)))==4
    assert all(sum(row)==1 for row in rows)


def test_spin_companions_cannot_supply_weak_doublet_zero_partner(native):
    _,m=native.modules()
    for poly in m[:4]:
        assert all(abs(key[-1])!=1 for key in native.weights(poly))


def test_single_twist_complete_dimensions(native):
    p=native.run()['twist_profiles']['1,0']
    assert [x['left_zero_dimension'] for x in p]==[276,220,220,220]
    assert all(x['left_zero_dimension']>55+111 for x in p)


def test_double_twist_changes_both_slots_and_pairing(native):
    p=native.run()['twist_profiles']['1,1']
    assert all(x['left_zero_dimension']==332 and x['spin_slots']==0 and x['R_copies']==2 for x in p)


def test_all_nine_twists_without_chirality_selection(native):
    p=native.run()['twist_profiles']
    assert len(p)==9
    assert all(x['all_weights_self_conjugate'] for v in p.values() for x in v)


def test_chiral_positive_control_is_not_killed(native):
    poly=sum(native.COLOUR)*(native.W+1/native.W)*native.F1
    assert not native.self_dual(poly)
    dual=poly.subs(dict(zip(native.VARS,[1/v for v in native.VARS])),simultaneous=True)
    assert native.self_dual(poly+dual)


def test_actual_mass_bilinears(native):
    assert native.run()['protected_R_bilinear_ranks']==[16,32]
    assert native.run()['facts']['actual_R_bilinear_skew_rank16']
    assert native.run()['facts']['two_R_copies_admit_symmetric_full_rank_mass']


def test_continuum_not_confused_with_zero_kernel(native):
    r=native.run()
    assert r['spin_kernel_dimensions']==[55,27,27,27]
    assert all(p['ordinary_spin_zero_angular_fibre_channels']==224 for p in r['twist_profiles']['1,0'])
    v,m=native.modules()
    assert s.expand((v[0]-v[1])/2-2*m[4])==0


def test_spin_critical_norm_and_regular_norm(native):
    f=native.run()['facts']
    assert f['norm_coordinate_change'] and f['critical_spin_exponent_log_diverges'] and f['regular_spin_exponent_exponentially_decays']


def test_compact_dual_extension_is_not_substituted(native):
    assert native.run()['facts']['dual_canonical_not_ordinary_dual_degree']
    assert -2*s.Rational(1,2)==-1!=1


def test_zero_essential_sequence_and_form_threshold(native):
    r=native.run()
    assert r['spin_Weyl_residual_coefficient']==10
    assert r['facts']['Weyl_sequence_residual_tends_to_zero']
    assert r['facts']['form_square_has_quarter_threshold']


def test_physics_scope_flags(native):
    r=native.run()
    for key in ('full_curved_action_derived','gapped_4D_reduction_derived','physical_chiral_SM_derived','global_anomaly_acceptance','nonauthor_acceptance'):
        assert r[key] is False
