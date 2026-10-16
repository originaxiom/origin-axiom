"""Live full real parent/operator gate, not a global SM/domain certificate."""
import json,os,subprocess,sys
from pathlib import Path
import pytest
ROOT=Path(__file__).resolve().parents[1]
HERE=ROOT/'reports/physical_bridge_2026_09_05/surface_full_real_parent_2026_10_16'
@pytest.fixture(scope='module')
def cert():
    rows=[]
    for name in ('probe','reference'):
        p=subprocess.run([sys.executable,'-B',str(HERE/(name+'.py'))],cwd=ROOT,
            env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),capture_output=True,text=True,timeout=1200)
        assert p.returncode==0,p.stderr+p.stdout
        rows.append(json.loads(p.stdout))
    return rows
def test_both_complete_live_actions_agree(cert):
    assert cert[0]==cert[1] and cert[0]['all_passed'] and all(cert[0]['checks'].values())
def test_real_WZ_action_and_actual_components(cert):
    c=cert[0]['checks']
    for k in ('full WZ vector reality and inverse','nonzero V squared retained V cubed zero',
        'all actual chirals satisfy barD','actual real K density',
        'actual full fermion action equals ordered components','native fermion IBP keeps all currents',
        'reference fermion IBP keeps all currents','wrong gaugino sign changes bulk action',
        'actual full vector Yang Mills action'):
        assert c[k],k
def test_actual_D_auxiliary_and_boundaries(cert):
    c=cert[0]['checks']
    for k in ('actual K D terms before IBP','actual D moment with retained boundary',
        'D commutator cannot be dropped','actual vector D Gaussian half'):
        assert c[k],k
    assert all(c['actual chiral auxiliary unit metric '+str(j)] for j in range(3))
def test_all_covariant_derivatives_and_full_positive_map(cert):
    c=cert[0]['checks']
    assert c['no higher fermion derivative or unpriced field']
    assert c['actual signed time weights positive'] and c['complete signed time metric']
    for j in range(4):
        assert c['actual external gauge covariance '+str(j)] and c['actual internal gauge covariance '+str(j)]
    assert c['full positive identity flavour Clifford map']
    assert c['actual map full MW C and time isometry'] and c['actual map U2 and R compatible']
    for ep in (-1,1):assert c['actual paired current plane preserved '+str(ep)]
def test_complete_same_normal_potential(cert):
    c=cert[0]['checks']
    for k in ('actual normal moment equals canonical curvature','actual normal F source equals canonical derivative',
        'actual complete normal potential twice residual action','normal quartic omission detected'):
        assert c[k],k
