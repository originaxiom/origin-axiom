"""Live actual weighted-Hessian map, with explicit positive and negative guards."""
import json,os,subprocess,sys
from pathlib import Path
import pytest
ROOT=Path(__file__).resolve().parents[1]
HERE=ROOT/'reports/physical_bridge_2026_09_05/surface_weighted_hessian_2026_10_16'
@pytest.fixture(scope='module')
def cert():
    rows=[]
    for name in ('probe','reference'):
        p=subprocess.run([sys.executable,'-B',str(HERE/(name+'.py'))],cwd=ROOT,
            env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),capture_output=True,text=True,timeout=1200)
        assert p.returncode==0,p.stderr+p.stdout
        rows.append(json.loads(p.stdout))
    return rows
def test_both_complete_live_records_agree(cert):
    assert cert[0]==cert[1] and cert[0]['all_passed'] and all(cert[0]['checks'].values())
def test_actual_positive_source_map_required_not_only_classification(cert):
    c=cert[0]['checks']
    assert c['actual favourable chiral phase map REQUIRED']
    assert c['actual graded signed time REQUIRED']
    assert all(c['actual aligned source completion coefficient '+str(j)] for j in range(6))
    assert cert[0]['records']['source']['printed_conjugate_witness'] is not None
def test_all_ordered_derivatives_and_real_norms(cert):
    c=cert[0]['checks']
    assert c['parameter IS actual eta projector']
    for a in range(4):
        for b in range(4):
            assert c['actual completed source ordered derivative '+str((a,b))]
            assert c['actual q real kinetic polarization '+str((a,b))]
            assert c['actual output real polarization '+str((a,b))]
            assert c['full weighted quadratic norm '+str((a,b))]
    assert c['complex cross terms not silently zero']
def test_actual_weighted_hessian_is_BPS_scoped(cert):
    c=cert[0]['checks']
    assert c['nonzero BPS control all residuals vanish']
    assert c['actual BPS Hessian half second variation']
    assert c['nonBPS Hessian squared linearization false control']
    assert c['printed weight changes nonzero Hessian'] and c['canonical t1 recovered']
def test_nonlinear_weighted_action_keeps_curvature_quartic_and_end(cert):
    c=cert[0]['checks']
    for k in ('full weighted nonlinear energy end identity','weighted curvature omission detected',
        'weighted end omission detected','weighted quartic omission detected',
        'both weighted root ends retained','weighted root divergence and variation'):
        assert c[k],k
