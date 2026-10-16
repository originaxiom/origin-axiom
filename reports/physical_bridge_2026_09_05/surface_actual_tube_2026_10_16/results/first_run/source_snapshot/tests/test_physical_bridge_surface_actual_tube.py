"""LIVE actual tube audit. No old particle/count/domain assertions."""
import json,os,subprocess,sys
from pathlib import Path
import pytest
ROOT=Path(__file__).resolve().parents[1]
HERE=ROOT/'reports/physical_bridge_2026_09_05/surface_actual_tube_2026_10_16'
@pytest.fixture(scope='module')
def cert():
    out=[]
    for name in ('probe','reference'):
        p=subprocess.run([sys.executable,'-B',str(HERE/(name+'.py'))],cwd=ROOT,
            env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),capture_output=True,text=True,timeout=1800)
        assert p.returncode==0,p.stderr+p.stdout
        out.append(json.loads(p.stdout))
    return out
def test_both_complete_actual_tube_calculations(cert):
    assert cert[0]==cert[1] and cert[0]['all_passed'] and all(cert[0]['checks'].values())
def test_actual_tube_contact_and_flat_opposition(cert):
    c=cert[0]['checks']
    for k in ('actual radius gradient and nonzero horizontal tilt','unit normal and complex partner orthogonal',
        'both modular radius transitions exact','actual CR tangent projection and positive rank two',
        'CR tangent annihilates radius and characteristic form','strict actual contact Levi coefficient',
        'actual tangent bracket has nonzero characteristic component','actual normal CR bracket spans all four ambient directions',
        'flat product control loses strict horizontal contact','actual angle derivative includes horizontal connection',
        'angular pair fails adapted compact gauge condition'):assert c[k],k
def test_actual_real_green_plane_not_vertical_or_hand_selection(cert):
    c=cert[0]['checks']
    for k in ('frozen actual real action complete record','all actual source Clifford relations',
        'old vertical minus sign is actual source projector','adapted actual projector Hermitian idempotent half rank',
        'adapted projector preserves true R and Majorana reality','both actual normal Green forms zero',
        'both CR tangential principal symbols preserved','complementary plane also zero flux not hand selection',
        'unchanged vertical plane fails actual tube Green control','adapted plane approaches vertical at fixed angle'):assert c[k],k
def test_moving_plane_keeps_actual_full_connection(cert):
    c=cert[0]['checks']
    for i in range(4):
        assert c['actual Kahler connection parallel J '+str(i)]
        assert c['full moving plane covariant derivative '+str(i)]
    assert c['constant plane shortcut loses extrinsic derivative']
def test_compact_gauge_constraint_not_complex_matter_exclusion(cert):
    c=cert[0]['checks']
    for k in ('compact matrix CR jet norm forces both real derivatives','complex nonconstant CR scalar is not excluded',
        'complex matrix CR jet without compact reality survives',
        'restricted conormal gauge jets have zero boundary cocycle pullback',
        'unrestricted angular cocycle density remains a nonzero control'):assert c[k],k
def test_finite_tube_does_not_claim_uniform_cusp_cut(cert):
    assert cert[0]['checks']['fixed tube cannot fit uniformly along cusp cycle']
