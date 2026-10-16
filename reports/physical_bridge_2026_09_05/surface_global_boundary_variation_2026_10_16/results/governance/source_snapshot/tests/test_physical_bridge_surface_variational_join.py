"""Live local action/fermion join, not global or independent analytic acceptance."""
import json,os,subprocess,sys
from pathlib import Path
import pytest
ROOT=Path(__file__).resolve().parents[1]
HERE=ROOT/'reports/physical_bridge_2026_09_05/surface_variational_join_2026_10_16'
@pytest.fixture(scope='module')
def cert():
    result=[]
    for name in ('probe','reference'):
        p=subprocess.run([sys.executable,'-B',str(HERE/(name+'.py'))],cwd=ROOT,
            env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),capture_output=True,text=True,timeout=1200)
        assert p.returncode==0,p.stderr+p.stdout
        result.append(json.loads(p.stdout))
    return result
def test_complete_live_records_agree(cert):
    assert cert[0]==cert[1] and cert[0]['all_passed'] and all(cert[0]['checks'].values())
def test_actual_full_Clifford_deformation_map(cert):
    c=cert[0]['checks']
    for key in ('phase instrument universal identity','phase instrument rejects one angle false zero',
        'phase instrument preserves derivative and half monodromy','radial instrument rejects one radius false zero',
        'radial instrument preserves restored halfpole derivative'):
        assert c[key],key
    for prefix,n in [('all ordered deformation coefficients ',16),('real norm polarization ',16),('tangent map Weyl and real ',4)]:
        rows=[v for k,v in c.items() if k.startswith(prefix)]
        assert len(rows)==n and all(rows)
    assert c['actual common real parameter rank4'] and c['parameter actually twist neutral'] and c['reversed BPS sign detected']
def test_actual_E8_BPS_tangent_has_interacting_domain(cert):
    c=cert[0]['checks']
    for key in ('actual E8 signed faithful root','actual selected root is antiperiodic',
        'all actual nonlinear BPS residuals','noncommuting background not abelianized',
        'actual amplitude tangent BPS and gauge fixing','amplitude is not a compact gauge orbit',
        'amplitude tangent finite L2','actual epsilon minus amplitude trace',
        'actual critical phases match source and conjugate','actual amplitude even term is old interacting dressing',
        'bare amplitude Yukawa genuinely nonzero','remaining root tangent is regular graph order'):
        assert c[key],key
def test_full_nonabelian_energy_not_scalar_surrogate(cert):
    c=cert[0]['checks']
    for key in ('full off shell nonabelian energy end identity','deleting curvature cross term detected',
        'deleting quartic detected','wrong full end sign detected','actual nonabelian root boundary current',
        'actual full root energy differentiated current','complete regulated energy and end cancel',
        'actual full energy leading divergence','singular first amplitude variations cancel'):
        assert c[key],key
def test_ramified_gauge_orbit_retains_Higgs_and_monodromy(cert):
    c=cert[0]['checks']
    for key in ('ramified gauge generator actual compact square','finite ramified gauge is unitary determinant one',
        'finite ramified gauge actual puncture equivariance','ramified gauge tends to identity',
        'gauge tangent changes Higgs as well as connection','gauge Higgs response bounded nonconstant',
        'gauge normal connection has genuine halfpole'):
        assert c[key],key
def test_source_action_map_is_tested_not_assumed(cert):
    c=cert[0]['checks']
    for key in ('literal source actual wedge and time weights','literal source kinetic normalized speeds',
        'literal dictionary w1 unequal not universal kill','literal dictionary w2 positive calibration',
        'actual G gaussian and eliminated source coefficient','literal Q2p residual weights calibrated'):
        assert c[key],key
    assert cert[0]['records']['literal_action_audit']['w1_residual_weights']==['1','1/4','1/4']
    assert cert[0]['records']['literal_action_audit']['w2_residual_weights']==['1','1','1']
