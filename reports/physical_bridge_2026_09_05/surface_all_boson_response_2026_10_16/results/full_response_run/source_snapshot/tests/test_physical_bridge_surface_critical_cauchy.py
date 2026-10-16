"""LIVE critical interacting fundamentals, source tangent and response bounds."""
import json,os,subprocess,sys
from pathlib import Path
import pytest
ROOT=Path(__file__).resolve().parents[1]
HERE=ROOT/'reports/physical_bridge_2026_09_05/surface_critical_cauchy_2026_10_16'
@pytest.fixture(scope='module')
def cert():
    data=[]
    for name in ('probe','reference'):
        p=subprocess.run([sys.executable,'-B',str(HERE/(name+'.py'))],cwd=ROOT,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),capture_output=True,text=True,timeout=1800)
        assert p.returncode==0,p.stderr+p.stdout;data.append(json.loads(p.stdout))
    return data
def test_complete_live_methods_and_parent_matrices(cert):
    assert cert[0]==cert[1] and cert[0]['all_passed'] and all(cert[0]['checks'].values())
    assert cert[0]['checks']['every saved matrix and metadata reconstructed exactly']
def test_complete_fundamental_and_green_forms(cert):
    for N in (1,2):
        for prefix in ('complete fundamental residual ','all four Green pairings and actual inverse ',
                       'log solution from independent reduction and determinant ','both full trace planes and Green nullness ',
                       'all L2 and nonL2 leading columns preserved '):assert cert[0]['checks'][prefix+str(N)]
def test_all_actual_sector_types_and_trace_completeness(cert):
    r=cert[0]['records'];assert r['coefficient_directions']==3968 and len(r['all_blocks'])==28
    assert {x['key'][2] for x in r['all_blocks']}=={-1,1}
    for k,v in cert[0]['checks'].items():
        if k.startswith(('actual entire coupled block ','both actual critical signs retained ','complete singleton fundamental ','singleton complete allowed ')):assert v,k
def test_field_dependence_log_and_two_sided_mutations(cert):
    for N in (1,2):
        for prefix in ('background dependent projector and derivative current ','log scale change only adds regular seed ',
                       'negative controls full backreaction Higgs leading only ','nonL2 and missing log controls fire '):assert cert[0]['checks'][prefix+str(N)]
def test_constructive_finite_momentum_majorants(cert):
    for k in ('rational column majorants for whole interval','exact Volterra integral bound not sampled grid',
              'majorant lowered below true vector fails','Neumann tail and all finite momentum small radius'):assert cert[0]['checks'][k]
    for N in (1,2):assert cert[0]['checks']['Volterra derivative identity full nonzero momentum '+str(N)]
    assert 'NOT numerical interval' in cert[0]['records']['volterra']['construction']
def test_full_actual_nonlinear_BPS_tangent_and_scope(cert):
    for k in ('same actual E8 triplet and source dictionary','full nonlinear angular BPS tangent not leading only',
              'full actual 48component nonlinear tangent radial residual','full source Majorana of BPS tangent',
              'all spin blocks reconstruct full actual BPS source'):assert cert[0]['checks'][k]
    r=cert[0]['records'];assert r['tangent']['matched_source_blocks']==8
    assert not r['scope']['full_curved_boundary_action'] and not r['scope']['full_physical_SM_three_gravity']
