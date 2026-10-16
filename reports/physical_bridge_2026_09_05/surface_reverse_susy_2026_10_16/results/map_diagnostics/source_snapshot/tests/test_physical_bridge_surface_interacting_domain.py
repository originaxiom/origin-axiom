"""Live interacting controls; the infinite-dimensional proof is separately authored."""
import json,os,subprocess,sys
from pathlib import Path
import pytest
ROOT=Path(__file__).resolve().parents[1]
HERE=ROOT/'reports/physical_bridge_2026_09_05/surface_interacting_domain_2026_10_15'
@pytest.fixture(scope='module')
def cert():
    rows=[]
    for name in ('probe','reference'):
        p=subprocess.run([sys.executable,'-B',str(HERE/(name+'.py'))],cwd=ROOT,
            env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),capture_output=True,text=True,timeout=1200)
        assert p.returncode==0,p.stderr+p.stdout
        rows.append(json.loads(p.stdout))
    return rows
def test_complete_live_records_agree(cert):
    assert cert[0]==cert[1] and cert[0]['checks'] and cert[0]['all_passed']
    assert all(cert[0]['checks'].values())
def test_small_perturbation_is_only_on_the_minimum(cert):
    c=cert[0]['checks']
    for key in ('actual small L3 norm','small coefficient tends zero','Holder L3 times L6 into L2',
        'critical halfpole is not minimal H1','proper closed range control','strict contraction range map',
        'bad noncontraction can collapse deficiency range'):
        assert c[key],key
def test_generic_complex_Higgs_dressing_and_full_reality(cert):
    c=cert[0]['checks']
    for prefix in ('generic complex source ','generic dressed cancellation ','generic dressed MW ',
                   'generic full real dressing '):
        rows=[v for k,v in c.items() if k.startswith(prefix)]
        assert len(rows)==8 and all(rows)
    assert c['all full-parent critical classes retained'] and c['dressed Green remainders vanish']
def test_full_critical_Green_count_not_sampled_six(cert):
    c=cert[0]['checks'];r=cert[0]['records']['domain']
    assert c['whole MW normal Green form nondegenerate']
    assert (r['regular_coefficients'],r['critical_coefficients'],r['complex_max_min_dimension'],r['deficiency_each'])==(136,112,1792,896)
    assert [q['full_complex_plane'] for q in r['laws']]==[896,896]
    for ep in (-1,1):assert c['paired maximal isotropic rank '+str(ep)] and c['paired plane real '+str(ep)]
def test_same_parent_nonabelian_backreaction(cert):
    c=cert[0]['checks']
    for key in ('actual odd112 root roster','actual compact signed SL2 root','explicit faithful root map',
        'nilpotent root has two compact real components','actual nonlinear holomorphic equation',
        'actual nonlinear moment balance','curvature is nonzero rather than normal commuting trick',
        'omitting backreaction fails moment','local added orthonormal connection bounded',
        'puncture holonomy unchanged to leading order','actual Higgs leading halfpole',
        'nonabelian curvature square logarithmic'):
        assert c[key],key
def test_action_identity_keeps_curvature_and_end(cert):
    c=cert[0]['checks']
    for key in ('off shell covariant boundary identity','dropping nonabelian curvature term fails',
        'actual regulated halfpole boundary cancellation','bare rough term genuinely divergent','wrong boundary sign rejected'):
        assert c[key],key
def test_actual_Fterm_boundary_variation_has_both_sides(cert):
    c=cert[0]['checks']
    for key in ('actual tangential Fterm critical pairing','actual charged dual Fterm coefficient nonzero',
        'normal Fterm wedge pulls back to zero','bounded tangential Fterm variation vanishes'):
        assert c[key],key
