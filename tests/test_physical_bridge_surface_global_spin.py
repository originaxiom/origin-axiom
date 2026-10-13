"""Live global-geometric controls, not a physical spectrum or full based lift."""
import importlib.util
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/surface_global_spin_2026_10_13'
def mod(name):
    sp=importlib.util.spec_from_file_location('global_spin_'+name,BASE/(name+'.py'))
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
N,R=mod('probe'),mod('reference')

def test_separate_records_and_live_controls():
    a,b=N.run(),R.run()
    assert a['all_passed'] and b['all_passed'] and a['checks'] and b['checks']
    assert a['records']==b['records']

def test_actual_coordinate_and_canonical_frame_map():
    c=N.run()['checks']
    assert c['S full coordinate coframe rotation']
    assert all(v for k,v in c.items() if k.startswith('canonical frame determinant '))

def test_full_variable_angle_operator_not_principal_only():
    c=N.run()['checks']
    assert all(c[f'actual Clifford transition {j}'] for j in range(4))
    assert c['whole ordinary differential covariance']
    assert c['whole canonical differential covariance']
    assert c['wrong R phase fails canonical covariance']
    assert c['omitted vertical rotation not a spin transition']

def test_connection_descent_does_not_flatten_R_line():
    c=N.run()['checks']
    assert c['actual Chern connection gauge law'] and c['nonflat R line still retained']
    assert c['T geometric transition trivial']

def test_central_loop_signs_and_actual_coefficient():
    c=N.run()['checks']
    assert c['spin central loop is not erased'] and c['R central loop is minus one']
    assert c['canonical central loop cancels'] and c['actual coefficient fourth power']
    assert c['ordinary full local6 loop is not cancelled']
    assert c['canonical full local6 loop cancels']
    assert c['fibre puncture centre retained']

def test_companions_and_independent_rotations_remain_live():
    c=N.run()['checks'];r=R.run()['checks']
    assert c['whole E8 companions retained'] and c['whole adjoint central action not scalar']
    assert all(r[f'rotation {j} full canonical covariance'] for j in range(6))
    assert r['rotation 0 wrong R phase rejected']
