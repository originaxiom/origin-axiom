"""Complete centre and selected overlap locks, with scope-changing controls."""
import importlib.util
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/weave_field_map_2026_10_14'
def mod(name):
    sp=importlib.util.spec_from_file_location('weave_field_map_'+name,BASE/(name+'.py'))
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
N,R=mod('probe'),mod('reference')

def test_live_exact_and_separate_records():
    a,b=N.run(),R.run()
    assert a['all_passed'] and b['all_passed'] and a['checks'] and b['checks']
    assert a['records']==b['records']

def test_current_weak_centre_is_whole_root_action():
    p,e,rr,hq,_=N.data();hw=e[3]-e[4]
    assert len(rr)==240 and all(int(r.dot(hq-hw))%2==0 for r in rr)
    assert N.run()['records']['original_joint_parities']==[[[0,0],136],[[1,1],112]]

def test_alternative_is_not_selected_to_close_the_goal():
    c=N.run()['checks'];r=N.run()['records']['alternative_joint_parities']
    assert c['alternative is an actual sl2 subalgebra']
    assert c['alternative centralizes literal quaternion holonomies']
    d={tuple(k):v for k,v in r}
    assert d[(0,1)]>0 and d[(1,0)]>0 and sum(d.values())==248

def test_full_field_necessary_condition_not_three_labels():
    d=N.run()['records']['uniform_rho_necessary_compatibility']
    assert d['Q'] and d['L']
    assert not any(d[k] for k in ['u^c','d^c','e^c','neutral_singlet'])
    assert N.run()['checks']['bare parity Higgs fails this weak-doublet coefficient test']

def test_W61_zero_is_exact_common_profile_not_omega_sample():
    c=N.run()['checks']
    rows=[v for k,v in c.items() if k.startswith('exact common-profile zero ')]
    assert len(rows)==12 and all(rows)
    assert c['non-skew polynomial control is nonzero']
    assert c['invariant bilinear nullity exactly one']

def test_W61_normalized_replay_and_noncommon_kinetic_control():
    c=N.run()['checks'];r=N.run()['records']
    assert c['unchanged upstream Q1 and normalized Q2 replay']
    assert r['normalized_Hermitian_diagonals']==[[1,1,-1],[-1,1,1],[1,-1,1]]
    assert c['supplied unequal kinetic Gram changes masses']

def test_no_flat_sign_fix_but_added_tensor_remains_an_alternative():
    c=N.run()['checks'];d=R.run()['checks']
    assert c['flat sign twist cannot change commutator']
    assert d['four flat twists keep odd puncture centre']
    assert c['quaternion tensor comparator has even centre']
    assert d['added tensor factor comparator changes centre']
