"""All stated commuting completions, not selection of a favourable one."""
import importlib.util
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/surface_weak_completions_2026_10_14'
def mod(name):
    sp=importlib.util.spec_from_file_location('weak_family_'+name,BASE/(name+'.py'))
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
N,R=mod('probe'),mod('reference')
def test_both_whole_family_exact_methods():
    a,b=N.run(),R.run();assert a['all_passed'] and b['all_passed'] and a['records']==b['records']
def test_complete_family_not_all_normalizers():
    r=N.run()['records'];assert len(r['angle_labels'])==12 and len(r['classes'])==6
    assert all(sum(n for _,row in c['even'] for _,n in row)==136 and sum(n for _,row in c['odd'] for _,n in row)==112 for c in r['classes'])
def test_zero_phase_is_not_massless_in_canonical_parent():
    c=N.run()['checks'];assert c['full zero-phase Fourier square']
    assert c['noninteger unit comparator can erase projected mass']
    assert R.run()['checks']['massless zero-phase comparator']
def test_no_repaired_SM_axes_silently_imported():
    r=N.run()['records'];assert all(c['full_parallel_gauge_dimension']==15 and c['diagonal_Y_invariants']==0 for c in r['classes'])
