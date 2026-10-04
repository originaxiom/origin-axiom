import importlib.util
from pathlib import Path

spec=importlib.util.spec_from_file_location('silver_boundary_variation',Path(__file__).with_name('verify.py'))
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_boundary_pairing_is_not_flat_deformation_integrability():
    c=m.controls()
    assert c['sl2_Lagrangian_dimension']==3 and c['sl2_nonzero_bracket']
    assert c['sl2_zero_Hessian_at_origin'] and c['sl2_gauge_stabilizer_dimension']==1


def test_parameter_screen_has_both_outcomes():
    c=m.controls()
    assert c['common_line_all_parameters'] and c['distinct_line_constraint_rank']>0


def test_actual_cohomology_spaces_are_maximal_isotropic_in_charged_pairs():
    rows=m.actual_members()
    assert len(rows)==4
    for r in rows:
        for v in r['amplitudes'].values():
            for p in v['pairing'].values():
                assert p['isotropic'] and p['wrong_dual_space_rejected']
                assert 2*p['allowed_dimension']==p['symplectic_rank']==p['paired_H1_dimension']


def test_retained_and_excluded_parameters_have_complete_linear_certificates():
    for r in m.actual_members():
        for v in r['amplitudes'].values():
            assert set(v['parameters'])=={'E','E*','F','F*'}
            for p in v['parameters'].values():
                assert p['surviving']+p['constraint_rank']==p['full_H0']
                assert (p['excluded_witness'] is None)==(p['constraint_rank']==0)


def test_original_interior_positive_and_split_control_remain():
    for r in m.actual_members():
        assert r['amplitudes']['0']['interior_pair']==[0,0]
        assert r['amplitudes']['1']['interior_pair']==[-1,-1]


def test_constant_unbroken_gauge_factor_is_a_different_tensor_factor():
    assert m.controls()['gauge_structure_tensor_factors_commute']
