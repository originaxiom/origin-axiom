import importlib.util
from pathlib import Path

import pytest
import sympy as s

spec = importlib.util.spec_from_file_location('spin_swap_audit',Path(__file__).with_name('verify.py'))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_published_family_by_fox_calculus():
    assert m.wada_check()['checks']=='PASS'


def test_nonzero_spin_difference_with_zero_symmetry_residual():
    r=m.diagnostic_checks()
    assert r['normalized_symmetry_residual']=='0'
    assert r['spin_contrast']=='2*sqrt(3)'
    assert r['fixed_control_detects_unit'] and r['perturbed_partner_detected']


def test_coefficient_and_value_conjugation_are_not_conflated():
    f=m.t+s.I
    assert m.coefficient_conjugate(f)==m.t-s.I
    assert m.circle_conjugate(f)==1/m.t-s.I
    assert s.simplify(m.coefficient_conjugate(f)-m.circle_conjugate(f))!=0


def test_affine_criterion_and_all_origin_changes():
    r=m.affine_checks()
    assert r['checks']=='PASS'
    assert [x['affine_bijections'] for x in r['rows']]==[2,24,1344]
    assert r['rows'][0]['moving_origin_but_fixed_points']==0
    assert r['rows'][1]['moving_origin_but_fixed_points']>0


def test_nonunits_are_rejected_without_finite_exponent_cutoff():
    assert m.unit(-m.t**103)=={'sign':-1,'power':103}
    for bad in (2*m.t,m.t+1,(m.t+1)/(m.t-1)):
        with pytest.raises(AssertionError):
            m.unit(bad)


def test_pinned_branch_receipts_not_a_physics_verdict():
    r=m.branch_checks()
    assert r['kill_entries']==460 and r['face_only']==343
    assert sum(r['second_confirmed'].values())==84
    assert r['matching_character_counts']['s960']['1']==3
