"""R20 independent assertions for exact word actions and parent lift costs."""
import importlib.util
from pathlib import Path

import sympy as sp

PATH = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/holonomy_equivariance_word_control.py'
SPEC = importlib.util.spec_from_file_location('physical_bridge_holonomy_word_control', PATH)
wc = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(wc)


def test_actual_free_automorphisms_inverses_and_relator_not_just_h1():
    r = wc.word_actions()
    assert r['outer_class_lower_bound'] == 12 and len(r['actions']) == 12
    assert all(v['two_sided_free_inverse'] and v['relator_preserved'] for v in r['generators'])
    assert all(v['relator_preserved'] for v in r['actions'])
    assert not wc.preserves_relator(('a', 'a'))
    assert wc.compose_words(wc.R, ('a', 'a')) != wc.ID


def test_word_h1_group_is_dihedral_and_its_c3_is_normal():
    A = [sp.Matrix(r['h1_matrix']) for r in wc.word_actions()['actions']]
    r = sp.Matrix([[0, -1], [1, 1]])
    s = sp.Matrix([[1, 1], [0, -1]])
    assert r**6 == s**2 == sp.eye(2) and s*r*s == r.inv()
    C3 = {wc.he.key_matrix(r**k) for k in (0, 2, 4)}
    assert all(wc.he.key_matrix(g*r**2*g.inv()) in C3 for g in A)
    assert len({wc.he.key_matrix(g) for g in A}) == 12


def test_numerical_upper_count_and_peripheral_control_match_exact_words():
    g = wc.control_geometry()
    assert not g['verified'] and g['lower_equals_upper']
    assert g['canonical_symmetry_upper_bound'] == 12 and g['m004_symmetry_count'] == 8
    assert len(g['numerical_peripheral_control']['isometries']) == 12
    assert g['canonical_orientations_all_positive']
    assert [r['fixed_points'] for r in g['canonical_c3_cusps']] == [[3, 3], [3, 3]]


def test_all_continuous_c3_characters_enumerated_with_fixed_point_controls():
    a = wc.algebra()
    assert {tuple(r['h']) for r in a['c3_fixed']} == {(0, 0), (sp.Rational(1, 3), sp.Rational(2, 3)), (sp.Rational(2, 3), sp.Rational(1, 3))}
    assert len(wc.he.fixed_characters(-sp.eye(2))) == 4
    assert a['c6_fixed'] == a['full_group_fixed'] == [[0, 0]]


def test_actual_pair_free_kernels_and_trivial_control_all_degrees():
    for r in wc.algebra()['c3_fixed']:
        c = r['cohomology']
        plus = [0, 4, 1, 0] if c['trivial'] else [0, 3, 0, 0]
        assert c['relative_T'] == plus and c['relative_E_dual'] == plus[::-1]
        assert not c['exceptional'] and c['euler'] == -3


def test_nontrivial_pair_stabilizers_and_old_order_two_choice():
    a = wc.algebra()
    pair = [r for r in a['c3_fixed'] if not r['cohomology']['trivial']]
    assert len(pair) == 2
    assert all(len(r['orbit']) == 2 and r['stabilizer_orders'] == {1: 1, 2: 3, 3: 2} for r in pair)
    assert not a['old_order_two']['c3_invariant'] and len(a['old_order_two']['orbit']) == 3
    assert all(a['polynomial_invariance'])


def test_parent_fixed_locus_is_central_not_pair_free():
    a = wc.algebra()
    assert {tuple(r['h']) for r in a['simply_connected_c3_fixed']} == {(0, 0), (1, 2), (2, 1)}
    assert all(r['invariant_parent'] and r['adjoint_h'] == [0, 0] for r in a['simply_connected_c3_fixed'])
    assert a['parent']['coroot_period'] == 3 and a['parent']['adjoint_period'] == 1


def test_all_nine_parent_lifts_checked_and_period_one_mutant_detected():
    A = sp.Matrix(wc.algebra()['c3_matrix'])
    for r in wc.algebra()['c3_fixed']:
        lifts = r['parent_lifts']
        assert len(lifts) == 9 and all(v['invariant_adjoint'] for v in lifts)
        assert sum(v['invariant_parent'] for v in lifts) == (3 if r['cohomology']['trivial'] else 0)
        if not r['cohomology']['trivial']:
            assert wc.he.invariant(A, r['h'], 1) and not wc.he.invariant(A, r['h'], 3)
            assert all(v['central_defect_mod_three'] != [0, 0] for v in lifts)


def test_adjoint_descends_but_fundamental_27_does_not():
    a = wc.algebra()
    assert a['parent']['central_root_phases'] == [0]
    assert a['parent']['central_fundamental_phases'] == [sp.Rational(1, 3)]
    assert not a['physical_selection'] and not a['orbifold_projection_performed']
