import importlib.util
from pathlib import Path

spec=importlib.util.spec_from_file_location('silver_zero_closure',Path(__file__).with_name('closure.py'))
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_degree_zero_control_can_close_and_fail():
    c=m.controls()
    assert c['full_invariant_positive'] and c['restricted_opposite_rank']==1


def test_m136_screened_parameters_do_not_form_a_closed_algebra():
    rows=[r for r in m.actual_members() if r['carrier']=='m136']
    assert len(rows)==2
    for r in rows:
        assert r['amplitudes']['1']['E x F -> F*']['rank']==1


def test_all_actual_product_obstructions_have_witnesses():
    rows=m.actual_members()
    assert len(rows)==4
    for r in rows:
        for a in r['amplitudes'].values():
            assert len(a)==6
            for x in a.values():
                assert (x['witness'] is None)==(x['rank']==0)
