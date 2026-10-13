"""Live based prerequisites with accepting/rejecting complete-roster controls."""
import importlib.util
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/based_transition_prerequisite_2026_10_13'
def mod(name):
    sp=importlib.util.spec_from_file_location('based_prerequisite_'+name,BASE/(name+'.py'))
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
N,R=mod('probe'),mod('reference')

def test_live_separate_matrix_root_records():
    a,b=N.run(),R.run()
    assert a['all_passed'] and b['all_passed'] and a['checks'] and b['checks']
    assert a['records']==b['records']

def test_based_words_not_homology_only():
    S={'a':'b','b':'BAb'}
    assert N.power(S,4)==N.inner('BabA')
    assert N.power(S,4)!={'a':'a','b':'b'}
    assert N.power(N.compose(S,{'a':'a','b':'ab'}),3)==N.power(S,2)

def test_rank_six_match_is_not_whole_adjoint_match():
    c=N.run()['checks'];r=N.run()['records']
    assert c['ordinary sign matches rank6 on this relation']
    assert c['canonical sign misses rank6 on this relation']
    assert r['full_E8_central_parities']==[136,112]
    assert r['conditional_spin_residual_ranks']==[544,448]
    assert c['no common scalar solves both parities']

def test_exact_square_root_free_normalization():
    c=R.run()['checks']
    assert c['exact unnormalized S square'] and c['exact unnormalized S fourth']
    assert c['actual BabA puncture transport']

def test_accepting_and_rejecting_scalars_and_matrix_control():
    c=R.run()['checks']
    assert c['scalar plus one retains even'] and c['scalar minus one retains odd']
    assert c['wrong scalar retains neither'] and c['matrix matching control retains everything']

def test_half_period_positive_retains_which_copy():
    c=N.run()['checks']
    assert all(c['quaternion half period '+str(p)] for p in [(1,0),(0,1),(1,1)])
    assert all(c['one fibre trivial Higgs parity '+str(p)] for p in [(1,0),(0,1),(1,1)])
    assert c['third period is not a quaternion sign twist']
    assert R.run()['checks']['zero line does not cancel nontrivial parities']
