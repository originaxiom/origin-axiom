"""LIVE full-source real Grassmann work and signed first-order variation."""
import json,os,subprocess,sys
from pathlib import Path
import pytest
ROOT=Path(__file__).resolve().parents[1]
HERE=ROOT/'reports/physical_bridge_2026_09_05/surface_real_fermion_work_2026_10_16'
@pytest.fixture(scope='module')
def cert():
    data=[]
    for name in ('probe','reference'):
        p=subprocess.run([sys.executable,'-B',str(HERE/(name+'.py'))],cwd=ROOT,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),capture_output=True,text=True,timeout=1800)
        assert p.returncode==0,p.stderr+p.stdout;data.append(json.loads(p.stdout))
    return data
def test_complete_live_methods_and_actual_source(cert):
    assert cert[0]==cert[1] and cert[0]['all_passed'] and all(cert[0]['checks'].values())
    for k in ('actual all nine velocities and full source reality','all16source components reconstructed',
              'complete248positive root basis not a small substitute','every actual E8 generator and parity acts faithfully',
              'complete compact conjugation and all gauge partners'):assert cert[0]['checks'][k]
def test_full_current_reality_and_external_action(cert):
    for k in ('complete3968actual Majorana metric and normal current','full interacting operator reality and Grassmann antisymmetry',
              'all j and momentum pair by actual coefficient covariance','both computational signs preserved and Lorentz exchanged'):assert cert[0]['checks'][k]
    for sig in (1,-1):
        for k in ('whole actual trace Green metric and reality ','induced trace reality constant for all x ',
                  'full real fixed frame all x ','single angular partner not mistaken for full real field ',
                  'all actual external velocities preserved on whole trace '):assert cert[0]['checks'][k+str(sig)]
def test_actual_on_shell_frame_and_work_not_rank_matching(cert):
    for k in ('entire actual on shell frame not leading asymptotic','full moving frame work equals true solution work',
              'full bulk density and both end identity','full work rank by exact inverse support not eigenvalues'):assert cert[0]['checks'][k]
    r=cert[0]['records']['frames']['1'];assert r['dimension']==1984 and r['actual_work_rank']>0 and r['witness']
def test_genuine_Grassmann_polynomial_and_dagger(cert):
    for sig in (1,-1):
        for k in ('actual real antisymmetric fermion work ','full exterior polynomial methods agree ',
                  'actual Grassmann dagger is Hermitian '):assert cert[0]['checks'][k+str(sig)]
    for k in ('commuting and trace only false negative controls','dagger without odd reversal rejected',
              'opposite real polynomial zero retained','known two generator real Grassmann control',
              'bare coefficient conjugation fails actual scalar reality'):assert cert[0]['checks'][k]
    assert cert[0]['records']['frames']['1']['polynomial'] and not cert[0]['records']['frames']['-1']['polynomial']
def test_signed_total_variation_and_Majorana_half_factor(cert):
    for k in ('signed bulk cancels boundary on shell not work erased','graded Majorana field variation and actual half factor',
              'wrong boundary sign and doubled Majorana factor fail'):assert cert[0]['checks'][k]
    assert cert[0]['records']['meaning']['signed_total_on_shell_variation']==0
def test_scope_is_not_complete_physical_boundary_theory(cert):
    r=cert[0]['records']['meaning'];assert r['nonzero_real_Grassmann_work_survives'] and r['not_unmatched_force']
    assert r['ranks_not_particles'] and not r['full_physical_SM_three_gravity']
