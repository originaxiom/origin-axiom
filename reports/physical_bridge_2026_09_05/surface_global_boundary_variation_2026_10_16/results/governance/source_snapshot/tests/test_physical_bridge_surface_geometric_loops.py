"""Geometric versus homology-only transport, retaining both extreme domains."""
import importlib.util
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/surface_geometric_loops_2026_10_14'
def mod(name):
    sp=importlib.util.spec_from_file_location('geom_test_'+name,BASE/(name+'.py'))
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
N,R=mod('probe'),mod('reference')
def test_actual_loop_and_two_arithmetic_methods():
    a,b=N.run(),R.run();assert a['all_passed'] and b['all_passed'] and a['records']==b['records']
def test_homology_is_not_a_based_frame_loop():
    c=N.run()['checks'];assert c['homology-only identity is rejected'] and c['SU6 alone does not match geometric frame']
    assert c['unpaired coefficient centre rejected'] and c['same homology different based lift']
    assert c['wrong original frame orientation rejected'] and c['positive frame inner puncture']
    assert R.run()['checks']['separate wrong frame orientation rejected']
def test_every_cusp_completion_and_both_A_eigenspaces_retained():
    r=N.run()['records'];assert len(r['classes'])==6
    for row in r['classes']:
        assert sum(n for _,rr in row['Z_even'] for _,n in rr)==136
        assert sum(n for _,rr in row['Z_odd'] for _,n in rr)==112
        assert [a for a,_ in row['Z_odd']]==['+i','-i']
        for (_,rr),(_,ii) in zip(row['Z_odd'],row['inverse_Z_odd']):
            assert dict(ii)=={r:dict(rr)[(-r)%12] for r in range(12)}
def test_complex_gluing_is_not_reality_selection():
    c=N.run()['checks'];assert c['both extreme complex planes preserved']
    assert c['normal reversal exchanges extremes'] and R.run()['checks']['Gaussian normal reversal exchanges extremes']
