"""Live cochain and actual-cusp controls, not a physical index certificate."""
import json,os,subprocess,sys
from pathlib import Path
import pytest
ROOT=Path(__file__).resolve().parents[1]
HERE=ROOT/'reports/physical_bridge_2026_09_05/surface_mode_transport_2026_10_15'
@pytest.fixture(scope='module')
def certificates():
    rows=[]
    for name in ('probe','reference'):
        p=subprocess.run([sys.executable,'-B',str(HERE/(name+'.py'))],cwd=ROOT,
            env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),capture_output=True,text=True,timeout=1200)
        assert p.returncode==0,p.stderr+p.stdout
        rows.append(json.loads(p.stdout))
    return rows
def test_whole_live_certificate_agrees(certificates):
    assert certificates[0]==certificates[1]
    assert all(v['all_passed'] and all(v['checks'].values()) for v in certificates)
def test_actual_inner_homotopies_not_raw_coefficient_action(certificates):
    c=certificates[0]['checks']
    assert sum(k.split(' ',1)[1].startswith('inner chain homotopy ') for k in c)==18
    assert sum('raw X inverse is not its H1 action' in k for k in c)==3
    assert sum('actual XZ homotopy' in k for k in c)==3
    assert sum('raw puncture sign is not cohomology transport' in k for k in c)==3
def test_hodge_and_spinor_lines_are_not_silently_identified(certificates):
    c=certificates[0]['checks'];r=certificates[0]['records']
    assert r['basic_Hodge_Hermitian']==[['-1','0'],['0','1']]
    assert c['Hodge positive is not the spinor plus coefficient line']
    assert c['wrong positive line is rejected']
    assert 'NOT asserted' in r['Hodge_to_spinor_identification']
def test_complete_kernel_phases_all_six_classes_both_extremes(certificates):
    r=certificates[0]['records'];rows=r['classes']
    assert [x['m'] for x in rows]==[1,3,5,7,9,11]
    assert [x['odd_zero_phase_alternative_domains'] for x in rows]==[[0,0],[17,17],[0,0],[0,0],[11,11],[0,0]]
    for x in rows:
        assert sum(x['even_gamma_plus'])==sum(x['even_gamma_minus'])==55
        assert sum(x['odd_gamma_plus'])==sum(x['odd_gamma_minus'])==56
        for name in ('odd_gamma_plus','odd_gamma_minus'):
            assert x['opposite_section_sign_control'][name]==[x[name][(j-6)%12] for j in range(12)]
    assert r['vertical_kernel_dimensions']['total_per_extreme']==166
def test_actual_profile_mixed_spin_and_R_terms_kept(certificates):
    r=certificates[0]['records'];c=certificates[0]['checks']
    assert r['conditional_radial_constants_N0']=={
        'even_gamma_minus':'1','even_gamma_plus':'1/2','odd_gamma_minus':'1/2','odd_gamma_plus':'1'}
    assert sum(k.startswith('dropping mixed spin changes the operator ') for k in c)==4
    assert c['integer six-unit separation proof endpoints'] and c['noninteger unit cancellation comparator']
def test_flat_label_nonpairing_is_not_assumed(certificates):
    r=certificates[0]['records'];c=certificates[0]['checks']
    assert r['flat_intertwiner_dimension']==9
    assert c['flat positive nonorthogonal metric witness']
    assert c['full specified moves reject that metric'] and c['canonical parent metric retained']
