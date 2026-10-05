"""LIVE exact locks; no transcripts or external checkout required."""
from reports.physical_bridge_2026_09_05.apex_scope_2026_10_05 import probe, reference
import pytest
import sympy as s


def test_actual_cubic_mass_Hessians():
    n,nu,md,mt = probe.cubic_blocks()
    assert md == s.Matrix([[0,n,0,-nu],[-n,0,nu,0]])
    assert mt == (n*s.eye(3)).row_join(nu*s.eye(3))


def test_exact_exceptional_rank_and_rejection():
    g,gn = s.diag(1,0,0),s.diag(0,1,0)
    md,mt = probe.generation_blocks(g,gn)
    assert md.rank()==4 and mt.rank()==6
    # A component-dependent term is outside the shared-block hypothesis.
    changed = s.MutableDenseMatrix(mt); changed[6,6]=1
    assert changed.rank()==7 and changed.rank()!=3*(md.rank()//2)


def test_invalid_generation_blocks_rejected():
    with pytest.raises(ValueError):
        probe.generation_blocks(s.zeros(2,3),s.zeros(2,3))


def test_actual_compact_order_four_lifts_and_exterior_weights():
    rows = probe.torus()
    assert len(rows)==4
    assert {r['six'] for r in rows}==set(reference.six_phases())
    assert all(sum(r['six'])%4==0 for r in rows)
    assert all((3*s.Rational(r['central_defect'])).q==1 for r in rows)
    assert all((s.Rational(r['central_defect'])+4*s.Rational(r['central_shift']))%1==0 for r in rows)


def test_group_relations_and_Q8_nonabelian_population():
    assert len(probe.lines())==24
    assert len(reference.matrix_lines())==24
    for a,b in probe.lines():
        assert probe.qm(a,b)!=probe.qm(b,a)
        assert probe.qw(probe.phi(probe.phi(probe.phi('a')))+'A',a,b)==probe.ONE
        assert probe.qw(probe.phi(probe.phi(probe.phi('b')))+'B',a,b)==probe.ONE


def test_full_deck_census_matches_separate_representation():
    native,other = probe.deck_census(),reference.census()
    key = lambda r:(tuple(r['six']),tuple(r['a']),tuple(r['b']),tuple(r['char']))
    assert len(native)==len(other)==1152
    assert {key(r):r for r in native}=={key(r):r for r in other}
    assert all(r['witness'] and r['trace']!=r['deck_trace'] for r in native)


def test_lifted_operator_selection_and_nonremovable_sum():
    phases,w,p,op = probe.selection()
    assert w.det()==1 and w**4==s.eye(5)
    assert p==s.diag(1,1,1,0,0) and op==s.eye(5)-p
    assert phases=={'triplet_mass':0,'Higgs_mass':1,'up_Yukawa':0,'down_Yukawa':0,
        'neutrino_operator':0,'H_bar5_bilinear':2,'10_bar5_bar5':1,'10_10_10_bar5':3}
    assert p.rank()==3 and all(((-w)**k).rank()==5 for k in range(4))


def test_producers_pass_and_have_matching_exact_rank_cases():
    native,other = probe.run(),reference.run()
    assert native['checks'] and other['checks']
    assert all(native['checks'].values()) and all(other['checks'].values())
    assert native['rank_cases']==other['rank_cases']
    assert native['physical_goal_achieved'] is other['physical_goal_achieved'] is False
