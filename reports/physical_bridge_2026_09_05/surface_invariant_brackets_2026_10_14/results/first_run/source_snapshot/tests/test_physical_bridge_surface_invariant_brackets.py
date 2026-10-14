"""Live actual bracket certificate, not only assertions on stored stdout."""
import json,os,subprocess,sys
from pathlib import Path
import pytest

ROOT=Path(__file__).resolve().parents[1]
HERE=ROOT/'reports/physical_bridge_2026_09_05/surface_invariant_brackets_2026_10_14'
@pytest.fixture(scope='module')
def certificates():
    rows=[]
    for name in ('probe','reference'):
        p=subprocess.run([sys.executable,'-B',str(HERE/(name+'.py'))],cwd=ROOT,
             env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),capture_output=True,text=True,timeout=1200)
        assert p.returncode==0,p.stderr+p.stdout
        rows.append(json.loads(p.stdout))
    return rows

def test_complete_live_two_engine_records(certificates):
    assert certificates[0]==certificates[1]
    assert all(v['all_passed'] and all(v['checks'].values()) for v in certificates)

def test_actual_module_map_not_only_weights(certificates):
    c=certificates[0]['checks']
    assert sum(k.startswith('full module action ') for k in c)==45
    assert all(c[k] for k in c if k.startswith('full module action '))

def test_whole_invariant_brackets_and_jacobi(certificates):
    c=certificates[0]['checks'];r=certificates[0]['records']
    assert len(r['complete_bracket_tensor'])==225
    assert sum(k.startswith('invariant Jacobi ') for k in c)==455
    assert c['actual centre exactly weak Cartan'] and c['derived exactly colour plus mixed14']

def test_compact_killing_and_fake_form_control(certificates):
    c=certificates[0]['checks']
    assert c['intrinsic derived Killing nondegenerate']
    assert c['compact derived Killing negative definite'] and c['fake plus root form detected']
    assert sum(k.startswith('actual form invariant ') for k in c)==3375

def test_g2_actual_root_strings_not_dimension_matching(certificates):
    r=certificates[0]['records']
    assert r['Cartan']==[['2','-3'],['-1','2']]
    assert r['long_short_string']==[True,True,True,False]
    assert r['short_long_string']==[True,False]
    assert (r['rank'],r['derived_rank'],r['centre_dimension'])==(3,2,1)

def test_all_moves_and_wrong_symplectic_sign_control(certificates):
    c=certificates[0]['checks']
    assert c['wrong mixed sign fails move invariance']
    assert c['full wedge common fixed dimension one'] and c['all six weak corrections noncentral']
    assert sum(k.startswith('actual full move preserves ') for k in c)==5
