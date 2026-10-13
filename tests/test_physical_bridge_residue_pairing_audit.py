"""Actual bilinear/rank locks, not a physical mass or complete contour run."""
import importlib.util
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/residue_pairing_audit_2026_10_13'
def mod(name):
    sp=importlib.util.spec_from_file_location('residue_audit_'+name,BASE/(name+'.py'))
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
def test_actual_raw_matrix_and_opposing_tensor():
    r=mod('probe').run()
    assert r['all_passed'] and r['checks']['actual residue determinant zero polynomial']
    assert r['checks']['symmetric opposing tensor genuinely different']
    assert r['checks']['raw entry residues need not vanish']
def test_whole_complex_spectrum_not_a_sample_fit():
    r=mod('probe').run()['checks']
    assert r['whole complex Hermitian outer product']
    assert r['generic squared singular polynomial']
def test_separate_gaussian_records_agree():
    a,b=mod('probe').run(),mod('reference').run()
    assert a['records']==b['records'] and b['all_passed']
    assert b['checks']['symmetric opposing determinant twelve']
def test_quaternion_pairing_sign_is_not_erased():
    a,b=mod('probe').run()['checks'],mod('reference').run()['checks']
    assert a['actual quaternion epsilon skew'] and a['actual bilinear residue skew in every slot']
    assert all(b[f'actual coefficient transpose {p}{q}'] for p in range(3) for q in range(3))
