import importlib.util
from pathlib import Path

spec=importlib.util.spec_from_file_location('silver_tensor_structural',Path(__file__).with_name('structural.py'))
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_projector_and_two_sided_dimension_controls():
    c=m.controls()
    assert c['coefficient_projector_identity'] and c['coefficient_rank']==6
    assert c['equal_dimension_positive'] and c['unequal_invertible_reverse_escape']==2
    assert c['nonacyclic_unequal_dimension_positive']


def test_m136_inverse_boundary_maps_and_acyclic_summand():
    rows=[r for r in m.actual_members() if r['carrier']=='m136']
    assert len(rows)==2
    for row in rows:
        for v in row['amplitudes'].values():
            assert v['V_betti']==[0,0,0] and v['F_betti']==[2,4,2]
            assert v['maps']['rank']==v['maps']['reverse_rank']==4
            assert v['maps']['composition_defect']==v['maps']['dual_composition_defect']==0
            assert v['conditional_equal_dimension']==2
            assert v['conditional_paired_H1_difference']==0


def test_m136_all_subspaces_bound_but_split_dimension_control_survives():
    for row in m.actual_members():
        if row['carrier']=='m136':
            assert row['amplitudes']['0']['chosen_L_dimensions']==[2,2]
            assert row['amplitudes']['0']['reverse_escape_lower_bound']==0
            assert row['amplitudes']['1']['chosen_L_dimensions']==[1,3]
            assert row['amplitudes']['1']['reverse_escape_lower_bound']==2


def test_m135_is_not_falsely_killed_by_acyclic_argument():
    rows=[r for r in m.actual_members() if r['carrier']=='m135']
    assert len(rows)==2
    for row in rows:
        for v in row['amplitudes'].values():
            assert v['V_betti']==[1,2,1] and v['F_betti']==[3,6,3]
            assert v['maps']['kernel']==v['maps']['reverse_kernel']==2
            assert v['maps']['composition_defect']==v['maps']['dual_composition_defect']==2
            assert v['reverse_escape_lower_bound']==v['forward_escape_lower_bound']==0
            assert v['conditional_paired_H1_difference'] is None
