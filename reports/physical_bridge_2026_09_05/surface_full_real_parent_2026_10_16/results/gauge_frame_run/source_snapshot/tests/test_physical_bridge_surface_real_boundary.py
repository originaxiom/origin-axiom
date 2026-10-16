"""Live full-parent matrices and local graph controls, not full physical acceptance."""
import json,os,subprocess,sys
from pathlib import Path
import pytest
ROOT=Path(__file__).resolve().parents[1]
HERE=ROOT/'reports/physical_bridge_2026_09_05/surface_real_boundary_2026_10_15'
@pytest.fixture(scope='module')
def cert():
    rows=[]
    for name in ('probe','reference'):
        p=subprocess.run([sys.executable,'-B',str(HERE/(name+'.py'))],cwd=ROOT,
            env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),capture_output=True,text=True,timeout=1200)
        assert p.returncode==0,p.stderr+p.stdout
        rows.append(json.loads(p.stdout))
    return rows
def test_whole_live_reality_certificate(cert):
    assert cert[0]==cert[1]
    assert all(r['all_passed'] and all(r['checks'].values()) for r in cert)
def test_actual_Majorana_Weyl_and_kinetic_map(cert):
    c=cert[0]['checks']
    assert c['full Majorana reality square one'] and c['Majorana preserves actual Weyl constraint']
    assert sum(k.startswith('Lorentz10 Clifford ') for k in c)==100
    assert sum(k.startswith('Majorana kinetic reality ') for k in c)==10
    assert c['wrong same R phase fails reality'] and c['single same-sign canonical block is not full reality']
def test_actual_source_slots_not_a_component_count(cert):
    r=cert[0]['records']
    assert [(v['field'],v['external_left_rank'],v['external_right_rank']) for v in r['actual_form_slots']]==[
        ('bar_eta',0,2),('psi_H',2,0),('psi_V',2,0),('bar_chi',0,2)]
    assert r['Weyl_tensor_sign']==-1
def test_entire_E8_reality_and_metric(cert):
    r=cert[0]['records'];c=cert[0]['checks']
    assert len(r['full_E8_roots'])==240 and len(r['tau_permutation'])==248
    assert r['coefficient_parities'].count(0)==136 and r['coefficient_parities'].count(1)==112
    assert c['full61504 signed compact conjugation bracket identities']
    assert c['full61504 actual Z2 bracket grading identities']
    assert sum(k.startswith('actual compact simple generator skew Hermitian ') for k in c)==24
    assert c['wrong plus Cartan conjugation rejected'] and c['naive identity coefficient metric rejected']
def test_paired_extremes_preserve_reality_without_independent_mirrors(cert):
    c=cert[0]['checks'];r=cert[0]['records']
    for eps in (-1,1):
        assert c['real paired trace law '+str(eps)] and c['actual parent current cancels '+str(eps)]
        assert c['same extreme in both R blocks fails reality '+str(eps)]
    assert [(x['allowed_Weyl_complex_rank'],x['independent_Rplus_complex_rank']) for x in r['critical_trace_laws']]==[(8,4),(8,4)]
def test_interacting_trace_is_dressed_not_deleted(cert):
    c=cert[0]['checks'];r=cert[0]['records']
    for prefix in ('actual critical normal solution ','actual full Higgs source ',
                   'actual dressed nonintegrable source cancels ','dressing keeps actual parent Weyl ',
                   'dressing commutes full Majorana '):
        assert sum(k.startswith(prefix) for k in c)==4
    assert sorted(x['correction_type'] for x in r['normal_dressing'])==['bounded_angular','bounded_angular','log','log']
    assert c['dressed residual r minus half log is square integrable'] and c['dressed Green lower terms vanish']
def test_bosonic_energy_gate_has_both_sides(cert):
    c=cert[0]['checks']
    assert c['actual radial integrals from the profile'] and c['critical trace finite positive L2']
    assert c['scalar supersymmetry partner gradient diverges']
    assert c['holomorphic Higgs and antiholomorphic normal connection leading equations']
    assert c['normal compact local Higgs moment zero'] and c['single root local Higgs moment nonzero']
    assert c['nonabelian charged interaction retained']
