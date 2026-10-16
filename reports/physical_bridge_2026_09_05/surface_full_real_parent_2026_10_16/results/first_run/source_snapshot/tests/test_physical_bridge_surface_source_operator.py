"""Live source-component census; partial operator results never imply full action admission."""
import json,os,subprocess,sys
from pathlib import Path
import pytest
ROOT=Path(__file__).resolve().parents[1]
HERE=ROOT/'reports/physical_bridge_2026_09_05/surface_source_operator_2026_10_16'
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
    assert cert[0]==cert[1] and cert[0]['all_passed'] and all(cert[0]['checks'].values())
def test_actual_time_reality_and_signed_product_not_absolute_value(cert):
    c=cert[0]['checks']
    for k in ('actual normalized full MW Nambu frame','actual induced Nambu time and reality',
        'graded signed time is canonical positive contour','ordinary naive contour has a real signed mismatch',
        'graded one form fermion product reverses ordinary sign','Grassmann overlap vanishes',
        'graded internal differential has its induced sign'):
        assert c[k],k
def test_diagonal_phase_solver_has_two_sided_controls(cert):
    c=cert[0]['checks']
    assert c['phase solver recovers planted all direction map']
    assert c['phase solver rejects magnitude changing planted defect']
def test_every_source_dictionary_is_retained_and_correctly_graded(cert):
    rows=cert[0]['records']['source_census']
    assert len(rows)==8 and len({(r['graded'],r['scalar_bar_sign'],r['scalar_phase']) for r in rows})==8
    for row in rows:
        if row['source_boson_and_fermion_join']:
            assert row['positive_time_in_declared_contour'] and row['scalar_bar_sign']==1
            assert row['chiral_phase_map'] and row['full_printed_match'] and row['printed_witness'] is None
        if not row['chiral_phase_map']:assert row['phase_witness'] is not None
        if row['chiral_phase_map'] and not row['full_printed_match']:assert row['printed_witness'] is not None
def test_actual_full_T_current_and_both_domains(cert):
    c=cert[0]['checks']
    for k in ('actual eta full conjugate projector rank4','actual T Weyl and full reality',
        'actual epsilon minus T is common scalar','all active BPS tangents have same T scalar',
        'actual U2 degree and R transition commute','printed w1 T not a kinetic isometry',
        'canonical w2 T identity','finite positive congruence preserves kernel not masses'):
        assert c[k],k
    for ep in (-1,1):
        assert c['actual T paired plane preserved '+str(ep)] and c['actual transported Green current '+str(ep)]
