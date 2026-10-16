"""Live actual Noether/Weyl/curved connection map, not physical spectrum."""
import json,os,subprocess,sys
from pathlib import Path
import pytest
ROOT=Path(__file__).resolve().parents[1]
HERE=ROOT/'reports/physical_bridge_2026_09_05/surface_real_twist_2026_10_16'
@pytest.fixture(scope='module')
def cert():
    out=[]
    for name in ('probe','reference'):
        p=subprocess.run([sys.executable,'-B',str(HERE/(name+'.py'))],cwd=ROOT,
            env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),capture_output=True,text=True,timeout=1200)
        assert p.returncode==0,p.stderr+p.stdout
        out.append(json.loads(p.stdout))
    return out
def test_both_complete_actual_geometric_maps(cert):
    assert cert[0]==cert[1] and cert[0]['all_passed'] and all(cert[0]['checks'].values())
def test_actual_charge_and_all_action_coefficients(cert):
    c=cert[0]['checks']
    for k in ('actual scalar Noether charge is opposite old label','actual scalar charge Hermitian involution C odd',
        'actual scalar generator acts on both scalar vertices','same named flavours opposite Weyl unit phase map',
        'all six full scalar and derivative coefficients mapped','all external kinetic and gauge coefficients mapped',
        'actual physical isometry reality and true R map'):assert c[k],k
    assert cert[0]['records']['charges']['source_left_R']==['1','-1','-1','1']
    assert not cert[0]['records']['physical_map']['scalar_reflection']
def test_full_tensor_and_geometric_connection(cert):
    c=cert[0]['checks']
    assert cert[0]['records']['connections']['source']==cert[0]['records']['connections']['direct_tensor']
    for j in range(4):
        assert c['all actual tensor field connection entries '+str(j)]
        assert c['all actual opposite MW spin R connection entries '+str(j)]
    for k in ('whole contracted curved source expression agrees','actual scalar supersymmetry lambda connection parallel',
        'reversed and omitted R fail tensor and lambda comparisons','dropping full mixed term fails curved action comparison'):assert c[k],k
def test_global_chart_and_full_differential_law(cert):
    c=cert[0]['checks']
    for k in ('whole variable angle source tensor transition','full global chart intertwiner including MW and true R',
        'full variable angle curved differential covariance','wrong chart R inhomogeneous term rejected',
        'actual source central spin and R signs cancel','geometric S4 and ST central angle relations','source chart C reality'):assert c[k],k
    assert cert[0]['records']['charges']['geometric_weights']==[0,2,1,-3]
def test_real_cutoff_and_gauge_factor_without_old_count_transfer(cert):
    c=cert[0]['checks']
    for k in ('actual whole cutoff maps to opposite MW minus plane','both real normal physical Green forms vanish',
        'actual cutoff geometric charts glue','wrong unchanged old MW cutoff rejected','noncommuting gauge coefficient factor retained'):assert c[k],k
    assert cert[0]['records']['boundary']['epsilon']==-1 and cert[0]['records']['boundary']['same_scalar_coordinates']
