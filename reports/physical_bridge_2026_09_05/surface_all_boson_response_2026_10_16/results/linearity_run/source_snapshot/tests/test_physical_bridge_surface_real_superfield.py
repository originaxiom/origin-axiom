"""Actual real F-action and all boundary slots, not a full physical-model seal."""
import json,os,subprocess,sys
from pathlib import Path
import pytest
ROOT=Path(__file__).resolve().parents[1]
HERE=ROOT/'reports/physical_bridge_2026_09_05/surface_real_superfield_2026_10_16'
@pytest.fixture(scope='module')
def cert():
    rows=[]
    for name in ('probe','reference'):
        p=subprocess.run([sys.executable,'-B',str(HERE/(name+'.py'))],cwd=ROOT,
            env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),capture_output=True,text=True,timeout=1200)
        assert p.returncode==0,p.stderr+p.stdout
        rows.append(json.loads(p.stdout))
    return rows
def test_complete_direct_and_component_records_agree(cert):
    assert cert[0]==cert[1] and cert[0]['all_passed'] and all(cert[0]['checks'].values())
def test_full_reduction_fermions_auxiliary_and_end(cert):
    for k in ('whole superfield two derivative reduction','six cubic permutations retained',
        'nonzero full transgression not dropped','all actual fermion auxiliary F components',
        'auxiliary integration by parts keeps boundary','auxiliary primitive nonzero control',
        'trace derivative representation diagnostic','trace variation representation diagnostic',
        'wrong transgression sign remains detected','wrong variation surface sign remains detected',
        'untraced commutator not erased'):
        assert cert[0]['checks'][k],k
def test_actual_adjoint_and_two_sided_odd_instruments(cert):
    for k in ('actual whole superfield conjugate F extraction','actual real F action involution',
        'wrong anti Berezin sign rejected','dagger exact anti multiplicative and involutive',
        'theta odd matrix anticommutes','commuting fermion instrument fails F term',
        'actual graded trace cyclicity'):
        assert cert[0]['checks'][k],k
def test_whole_boundary_not_just_lowest_bosons(cert):
    for k in ('whole superfield first variation with surface','variation surface cannot be dropped',
        'whole tangential chiral Dirichlet cancels F surface',
        'lowest boson Dirichlet alone fails boundary multiplet',
        'boundary auxiliary and fermion terms both retained',
        'tangential gauge derivative violates cutoff law'):
        assert cert[0]['checks'][k],k
def test_gauge_covariance_and_actual_inverse_metric(cert):
    c=cert[0]['checks']
    assert c['all small gauge curvature jets covariant']
    assert c['real parent holomorphic trace gauge invariant']
    assert c['omitted gauge connection derivative detected']
    assert all(c['actual auxiliary Gaussian '+str(j)] for j in range(3))
    assert c['auxiliary inverse metric not copied']
