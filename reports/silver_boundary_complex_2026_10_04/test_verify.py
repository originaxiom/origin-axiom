import importlib.util
from pathlib import Path

spec=importlib.util.spec_from_file_location('silver_boundary_complex',Path(__file__).with_name('verify.py'))
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_connecting_classes_and_two_cancellation_controls():
    c=m.controls()
    assert c['unmatched_boundary_H0']==[0,1,0,0]
    assert c['attached_A0']==c['global_H0_cancels']==[0,0,0,0]


def test_source_recovery_and_broken_map_rejection():
    c=m.controls()
    assert c['empty_boundary_recovers_source']==[1,0,0,0]
    assert c['broken_chain_map_rejected']


def test_cone_preserves_the_interior_degree_one_positive():
    rows=m.actual_members()
    assert len(rows)==4
    for row in rows:
        for a,sectors in row['amplitudes'].items():
            assert [r['H1_differences']['cone'] for r in sectors.values()]==([0,0] if a=='0' else [-1,-1])


def test_reversed_endpoints_change_degree_one_but_not_euler():
    for row in m.actual_members():
        for a,sectors in row['amplitudes'].items():
            expected=[0,0] if a=='0' else [0,-1]
            assert [r['H1_differences']['reversed'] for r in sectors.values()]==expected
            assert [r['E']['models']['cone']['odd_minus_even'] for r in sectors.values()]==expected
            for r in sectors.values():
                for side in ('E','dual'):
                    p=r[side]['models']
                    assert p['cone']['odd_minus_even']==p['reversed']['odd_minus_even']


def test_actual_degree_two_map_and_paired_dimensions():
    detected=False
    for row in m.actual_members():
        for sectors in row['amplitudes'].values():
            for r in sectors.values():
                for name in ('cone','reversed'):
                    assert r['E']['models'][name]['H']==r['dual']['models'][name]['H'][::-1]
                    assert r['E']['models'][name]['chain_identities']
                assert r['E']['restriction2_rank']==r['boundary_H0'][1]-r['global_H0'][1]
                detected |= r['E']['wrong_R2_sign_detected']
    assert detected


def test_degree_zero_and_three_are_not_silently_discarded():
    for row in m.actual_members():
        r=row['amplitudes']['1']['W']
        assert r['E']['models']['cone']['H']==[0,0,1,1]
        assert r['dual']['models']['cone']['H']==[1,1,0,0]
        e=row['amplitudes']['1']['wedge2W']
        assert e['E']['models']['cone']['H']==[0,0,1,0]
        assert e['dual']['models']['cone']['H']==[0,1,0,0]


def test_tilted_complement_control_in_both_sectors():
    assert m.actual_members()[0]['tilted_complement_control']=={'W':True,'wedge2W':True}
