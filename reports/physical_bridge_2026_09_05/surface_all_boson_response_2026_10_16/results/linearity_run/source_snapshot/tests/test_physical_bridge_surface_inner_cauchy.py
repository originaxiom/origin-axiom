"""LIVE punctured-interior response; no imported physical index or gap."""
import json,os,subprocess,sys
from pathlib import Path
import pytest
ROOT=Path(__file__).resolve().parents[1]
HERE=ROOT/'reports/physical_bridge_2026_09_05/surface_inner_cauchy_2026_10_16'
@pytest.fixture(scope='module')
def cert():
    data=[]
    for name in ('probe','reference'):
        p=subprocess.run([sys.executable,'-B',str(HERE/(name+'.py'))],cwd=ROOT,
            env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),capture_output=True,text=True,timeout=1800)
        assert p.returncode==0,p.stderr+p.stdout
        data.append(json.loads(p.stdout))
    return data
def test_complete_both_methods_and_same_source(cert):
    assert cert[0]==cert[1] and cert[0]['all_passed'] and all(cert[0]['checks'].values())
    for k in ('same complete source dictionary and all nine velocities','geometric polar frame is unitary and rotates actual normal',
        'polar monodromy and density retain both holonomy signs','actual polar connection canceled by density',
        'wrong polar sign and missing density are detected','angular lattices follow coefficient and spin monodromy',
        'full horizontal radial equation has correct source sign','normal matrices Hermitian square and anticommute'):assert cert[0]['checks'][k],k
def test_critical_transfer_retains_both_singular_signs(cert):
    c=cert[0]['checks']
    for sig in ('1','-1'):
        for label in ('critical supplied plane properties sign ','critical transfer graph equals derived response sign ',
            'critical finite response projector current and R sign ','critical full core compression sign ',
            'critical reality keeps conjugate Fourier sign ','zero momentum critical response without division sign '):assert c[label+sig],label+sig
    assert c['critical propagated data solve entire radial system']
def test_full_regular_response_and_uniform_complement(cert):
    c=cert[0]['checks']
    for sig in ('1','-1'):
        for label in ('regular graph derived from whole branch sign ','regular response projector current and R sign ',
            'all regular core compression sign ','regular reality keeps opposite m and xi sign ',
            'zero horizontal regular response is orthogonal core sign '):assert c[label+sig],label+sig
    for k in ('regular coefficients obey exact unit circle identity','uniform complement upper bound is Cauchy Schwarz identity',
        'all order first component Frobenius recurrence','all order second component Frobenius recurrence',
        'Bessel ratio Riccati identity and first crossing sign','Bessel both first order components not just scalar square',
        'independent regular branches and Riccati all declared numerical controls','regular indicial L2 borderline not discarded'):assert c[k],k
def test_reality_R_gauge_Lorentz_and_both_end_currents(cert):
    for k in ('actual Majorana reverses radial Fourier and R signs','normal response preserves source R and external Lorentz',
        'both oriented normal currents and all external generators kept','constant nonabelian gauge multiplicity not projected out'):assert cert[0]['checks'][k],k
def test_regular_massless_and_critical_modes_are_not_erased(cert):
    c=cert[0]['checks']
    for k in ('regular half integer modes recover every Cartesian source spinor',
        'constant spinor angular signs match regular radial equation','regular zero momentum boson has zero normal kinetic response',
        'critical physical half pole is retained and locally L2','zero full frequency has no invented spectral inverse'):assert c[k],k
    assert cert[0]['records']['recovery']['particle_count'] is False
def test_cutoff_scope_and_two_sided_mutations(cert):
    c=cert[0]['checks']
    for sig in ('1','-1'):assert c['critical cutoff difference and nonuniform norm sign '+sig]
    assert c['unchanged pointwise trace is not regular angular response']
    assert c['wrong regular graph sign fails core complement at zero horizontal']
