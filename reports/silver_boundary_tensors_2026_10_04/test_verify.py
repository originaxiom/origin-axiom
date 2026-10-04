import importlib.util
from pathlib import Path

spec=importlib.util.spec_from_file_location('silver_boundary_tensors',Path(__file__).with_name('verify.py'))
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_common_line_positive_and_distinct_line_negative():
    out=m.controls()
    assert out['common_line_all_six_channels_close']
    assert out['distinct_line_cup_rank']==10


def test_tensor_duality_and_exchange_controls():
    out=m.controls()
    assert out['wrong_dual_detected'] and out['wrong_exchange_sign_detected']


def test_all_four_coefficients_both_states_and_all_six_channels():
    rows=m.actual_members()
    assert len(rows)==4
    for row in rows:
        assert set(row['amplitudes'])=={'0','1'}
        for value in row['amplitudes'].values():
            assert len(value['channels'])==6
            assert all(r['equivariant'] for r in value['channels'].values())


def test_products_descend_and_preserve_graded_exchange():
    for row in m.actual_members():
        for value in row['amplitudes'].values():
            assert all(r['descends_to_cohomology'] and r['graded_exchange']
                       for r in value['channels'].values())


def test_every_nonzero_escape_has_an_exact_witness():
    for row in m.actual_members():
        for value in row['amplitudes'].values():
            for result in value['channels'].values():
                for name in ('degree_01','degree_10','degree_11'):
                    assert (result[name]['witness'] is None)==(result[name]['rank']==0)
                    assert result[name]['rank']>=0


def test_original_interior_positive_is_not_overwritten():
    for row in m.actual_members():
        assert row['amplitudes']['0']['interior_pair']==[0,0]
        assert row['amplitudes']['1']['interior_pair']==[-1,-1]
