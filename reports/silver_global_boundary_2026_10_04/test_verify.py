import importlib.util
from pathlib import Path

spec=importlib.util.spec_from_file_location('silver_global_boundary',Path(__file__).with_name('verify.py'))
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_opposite_controls_prevent_physical_projector_false_kill():
    result=m.controls()
    assert result['status']=='PASS'
    assert result['continuous_full_projector_with_compressed_jump']
    assert result['constant_rank_rotating_projector']
    assert result['two_term_Euler']==[0,0,0,0]


def test_all_four_global_complements_recover_interior_counts():
    rows=m.actual_members()
    assert len(rows)==4
    for row in rows:
        for t,result in row['amplitudes'].items():
            expected=0 if t=='0' else -1
            assert result['W']['difference']==result['wedge2W']['difference']==expected


def test_exterior_complement_jump_is_exact():
    for row in m.actual_members():
        split=row['amplitudes']['0']['wedge2W']['complement_dimensions'][0]
        for t in ('1','2','-1'):
            r=row['amplitudes'][t]['wedge2W']
            assert r['complement_dimensions'][0]==split-1
            assert r['split_projector_distance_one_witness']


def test_fundamental_uses_global_invariants_not_boundary_rank_jump():
    for row in m.actual_members():
        a,b=row['amplitudes']['0']['W'],row['amplitudes']['1']['W']
        assert a['complement_dimensions']==b['complement_dimensions']
        assert a['global_H0']==[1,1] and b['global_H0']==[0,1]


def test_group_cup_and_peripheral_transport():
    for row in m.actual_members():
        assert row['same_peripheral_matrices'] and row['nonzero_scaling_conjugacy']
        for result in row['amplitudes'].values():
            assert result['W']['group_log_cup_agrees'] and result['wedge2W']['group_log_cup_agrees']


def test_actual_nonunitary_gauge_and_metric_transport():
    assert m.actual_members()[0]['gauge_controls']==[True,True]
