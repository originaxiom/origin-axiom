"""LIVE all-angular source response, resonance and first-order boundary work."""
import json,os,subprocess,sys
from pathlib import Path
import pytest
ROOT=Path(__file__).resolve().parents[1]
HERE=ROOT/'reports/physical_bridge_2026_09_05/surface_all_angular_response_2026_10_16'
@pytest.fixture(scope='module')
def cert():
    out=[]
    for name in ('probe','reference'):
        p=subprocess.run([sys.executable,'-B',str(HERE/(name+'.py'))],cwd=ROOT,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),capture_output=True,text=True,timeout=1800)
        assert p.returncode==0,p.stderr+p.stdout;out.append(json.loads(p.stdout))
    return out
def test_complete_live_methods_and_actual_matrices(cert):
    assert cert[0]==cert[1] and cert[0]['all_passed'] and all(cert[0]['checks'].values())
    assert cert[0]['checks']['entire actual parent table matches reconstructed modules']
def test_all_angular_gap_regular_recurrences_and_resonance(cert):
    for k,v in cert[0]['checks'].items():
        if k.startswith(('all integer angular gap ','both recurrences ','all angular denominator ','injected regular resonance ')):assert v,k
    r=cert[0]['records'];assert len(r['all_noncritical'])==56 and r['compatible_resonant_entries']>0
    assert set(r['directions_per_angular_sign'].values())=={3968}
    assert cert[0]['checks']['zero angular gap control and actual term mutations fire']
def test_constructive_convergence_and_complete_L2_controls(cert):
    for k in ('exact L2 kernel bounds include borderline exponent','weighted continuous kernel bounds whole interval',
              'weighted quadratic maximum certificate','all order coefficient majorant ratio',
              'majorant convergence and exact generating function','known free Bessel first response recovered',
              'wrong free response normalization rejected'):assert cert[0]['checks'][k]
def test_untraced_work_and_correct_physical_parameter_variation(cert):
    assert cert[0]['checks']['physical background chain rule exact independent variables']
    for k,v in cert[0]['checks'].items():
        if k.startswith(('fixed physical momentum ','untraced differential boundary ')):assert v,k
    assert cert[0]['checks']['actual polarized first order Euler and weight']
    assert cert[0]['checks']['both endpoint orientation control']
def test_actual_nonzero_background_work_with_regular_partner(cert):
    for N in (1,2):
        for k in ('full actual boundary work and bulk density ','trace only and regular omission controls ',
                  'first order Hermitian work and inner limit '):assert cert[0]['checks'][k+str(N)]
        assert cert[0]['records']['boundary_work'][str(N)]['rank']==2
        assert cert[0]['records']['boundary_work'][str(N)]['trace']=='0'
def test_scope_remains_local_not_complete_physics(cert):
    r=cert[0]['records']['scope'];assert r['all_angular_local_response_with_same_n0_antecedent']
    assert not r['uniform_joint_high_frequency'] and not r['full_curved_common_boundary_action'] and not r['physical_SM_three_gravity']
