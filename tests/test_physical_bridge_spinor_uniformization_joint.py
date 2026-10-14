"""Live typed field/portal checks; no claim of a global physical Higgs map."""
import importlib.util
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/spinor_uniformization_joint_2026_10_14'
def mod(name):
    sp=importlib.util.spec_from_file_location('uniform_joint_'+name,BASE/(name+'.py'))
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
N,R=mod('probe'),mod('reference')

def test_both_actual_methods_with_typed_records():
    a,b=N.run(),R.run()
    assert a['all_passed'] and b['all_passed']
    assert all(a['records'][k]==v for k,v in b['records'].items())

def test_connection_preserving_identification_is_actually_tested():
    c=N.run()['checks']
    assert c['original spinor holomorphic residual zero']
    assert c['naive ordinary field same connection rejected']
    assert c['changed connection ordinary positive comparator']
    assert c['changed connection fails ORIGINAL moment']

def test_continuous_lift_not_read_from_finite_Q8():
    c=N.run()['checks']
    assert c['odd part includes a quartet'] and c['Q8 restriction still56 doublets']
    assert c['literal transformed lift has same full character']
    assert c['weight one comparator applies to THIS root']

def test_actual_interaction_positive_not_a_portal_kill():
    c=N.run()['checks']
    assert c['quartic interaction is present']
    assert c['standalone cubic not in original zero-r potential']
    assert c['background induced cubic positive route retained']
    assert c['commuting nilpotent two-field positive survives']

def test_ordinary_W75_local_math_replayed_without_parent_identification():
    r=N.run()['records']
    assert r['ordinary_W75_subset']=={'u2':True,'u3':True,'u4':True}
    assert N.run()['checks']['different spinors CAN produce ordinary K field']
