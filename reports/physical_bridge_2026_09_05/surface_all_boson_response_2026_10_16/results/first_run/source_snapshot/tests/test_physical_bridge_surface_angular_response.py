"""LIVE all-angle source boundary audit, no physical family/count assertion."""
import json,os,subprocess,sys
from pathlib import Path
import pytest
ROOT=Path(__file__).resolve().parents[1]
HERE=ROOT/'reports/physical_bridge_2026_09_05/surface_angular_response_2026_10_16'
@pytest.fixture(scope='module')
def cert():
    out=[]
    for name in ('probe','reference'):
        p=subprocess.run([sys.executable,'-B',str(HERE/(name+'.py'))],cwd=ROOT,
            env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),capture_output=True,text=True,timeout=1800)
        assert p.returncode==0,p.stderr+p.stdout
        out.append(json.loads(p.stdout))
    return out
def test_both_complete_actual_source_angular_calculations(cert):
    assert cert[0]==cert[1] and cert[0]['all_passed'] and all(cert[0]['checks'].values())
def test_actual_source_not_a_different_parent_or_deleted_conjugates(cert):
    c=cert[0]['checks']
    for k in ('actual complete source and method dictionary','all nine source Hermitian Clifford relations',
        'all actual source velocities Majorana even','actual adapted normal and all tangents orthonormal',
        'actual adapted whole trace still real and Green null','actual normal factorization keeps all scalar and tangential terms',
        'full frozen Hamiltonian Hermitian and exact square','normal current anticommutes full frozen Hamiltonian'):assert c[k],k
def test_characteristic_failure_is_bounded_and_controls_all_other_angles(cert):
    c=cert[0]['checks']
    for k in ('CR part exchanges old trace with invertible transverse square',
        'characteristic and actual scalar mass preserve old trace','both old planes retain equal signed characteristic multiplicities',
        'old compression keeps every angular and scalar term','principal old compression has correct two angular eigenbranches'):assert c[k],k
    rows=cert[0]['records']['angular']['finite_cauchy_controls']
    assert len(rows)==9
    for r in rows:
        wanted=4 if r['parameters'][:2]==[0,0] else 0
        assert r['old_intersections']==[wanted,wanted]
        assert r['spectral_union_rank']==16
def test_spectral_response_retains_reality_current_and_both_ends(cert):
    c=cert[0]['checks']
    for k in ('full Cauchy and spectral responses are exact orthogonal projectors',
        'spectral response complements complete interior Cauchy space','both spectral planes have true normal Green current zero',
        'all responses preserve external Lorentz generators','Fourier and charge reversal retain actual Majorana response',
        'fixed Fourier pointwise reality is not silently substituted','spectral response keeps full constant gauge multiplicity'):assert c[k],k
def test_same_frozen_exterior_and_zero_threshold_not_invented_action(cert):
    c=cert[0]['checks']
    for k in ('exterior and interior decaying solutions solve same equation','exterior squared norm response positive and normalized',
        'both oriented boundary spectral signs retained','interior norm identity retains boundary cross term',
        'zero threshold not divided or falsely gapped'):assert c[k],k
def test_local_charged_control_keeps_its_gauge_and_neutral_costs(cert):
    c=cert[0]['checks']
    for k in ('local complex bag is principal elliptic and Green null','unpaired complex bag fails actual pointwise reality',
        'existing conjugate charge pair local bag retains Majorana','paired charge conjugation flips axis without deleting fields',
        'charged local pair retains Lorentz and normal current','charged pair local principal complement for all covectors',
        'charge axis preserved but general gauge mixing detected'):assert c[k],k
