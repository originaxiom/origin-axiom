"""LIVE scoped action/Clifford/cutoff audit, NOT original named-map acceptance.

Original full-gate tests are retained in both immutable failure snapshots.
These locks preserve its exact negative as well as the actual positives.
"""
import importlib.util,json,os,subprocess,sys
from pathlib import Path
import pytest
ROOT=Path(__file__).resolve().parents[1]
HERE=ROOT/'reports/physical_bridge_2026_09_05/surface_full_real_parent_2026_10_16'
sp=importlib.util.spec_from_file_location('scope_lock',HERE/'scope_execute.py')
audit=importlib.util.module_from_spec(sp);sp.loader.exec_module(audit)
@pytest.fixture(scope='module')
def cert():
    rows=[]
    for name in ('probe','reference','clifford_diagnostic'):
        p=subprocess.run([sys.executable,'-B',str(HERE/(name+'.py'))],cwd=ROOT,
            env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),capture_output=True,text=True,timeout=1200)
        data=json.loads(p.stdout)
        if name=='clifford_diagnostic':assert p.returncode==0 and data['all_passed'],p.stderr
        else:assert p.returncode==1 and audit.scoped(data),p.stderr
        rows.append(data)
    return rows
def test_live_real_action_keeps_original_named_failure(cert):
    a,b,_=cert;assert a==b and a['all_passed'] is False
    assert len(a['checks'])==39 and sum(a['checks'].values())==38
    assert a['records']['source']['all_rejected_flavour_maps'][0]['reason']==['inconsistent edge',1,0,10,'1','-1']
def test_real_action_gaussians_covariances_and_retained_end(cert):
    c=cert[0]['checks']
    for k in ('actual full fermion action equals ordered components','actual full vector Yang Mills action',
        'actual vector D Gaussian half','actual D moment with retained boundary',
        'native fermion IBP keeps all currents','reference fermion IBP keeps all currents',
        'wrong gaugino sign changes bulk action','D commutator cannot be dropped',
        'actual complete normal potential twice residual action','normal quartic omission detected'):
        assert c[k],k
    assert all(c['actual external gauge covariance '+str(j)] and c['actual internal gauge covariance '+str(j)] for j in range(4))
    assert all(c['actual chiral auxiliary unit metric '+str(j)] for j in range(3))
def test_actual_clifford_module_and_oriented_obstruction(cert):
    d=cert[2];assert all(d['checks'].values())
    r=d['records'];assert r['actual_volume']=='1' and r['canonical_volume']=='-1'
    assert r['linear_fixed_orientation_intertwiner_obstructed']
    assert d['checks']['actual all81 Clifford relations'] and d['checks']['actual full Nambu reality on all coefficients']
def test_local_scalar_hatches_do_not_earn_old_global_bundle(cert):
    r=cert[2]['records'];maps=r['hatch_maps'];assert len(maps)==2
    assert len(maps)+len(r['hatch_rejections'])==96
    for m in maps:
        assert m['scalar_signs'][0]*m['scalar_signs'][1]==-1
        assert m['permutation']==[3,2,1,0]
        assert all(m[k] for k in ('complete_coefficients','unitary','C_compatible','R_compatible'))
        assert not m['same_U2_generators']
def test_actual_finite_cutoff_plane_and_exchanged_extremes(cert):
    d=cert[2];c=d['checks']
    for k in ('actual whole cutoff trace half rank and real','actual cutoff both real normal Green forms zero',
        'actual cutoff external and internal tangential action invariant'):assert c[k],k
    for m in d['records']['hatch_maps']:
        assert m['actual_whole_cutoff_image_epsilon']==[1]
        for q in m['paired_planes']:
            assert not q['preserved'] and q['mapped_to_opposite'] and q['target_Green_zero']
    assert c['credited universal normal end identity recovered']
    for j in (4,5):
        assert c['scalar reflection transports BOTH ends '+str(j)]
        assert c['scalar reflection keeps actual first variation '+str(j)]
        assert c['unchanged old end fails after scalar reflection '+str(j)]
