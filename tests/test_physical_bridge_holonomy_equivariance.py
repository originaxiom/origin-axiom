"""R20: actual geometric action and global-parent symmetry controls."""
import importlib.util
from pathlib import Path

import pytest
import sympy as sp

PATH = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/holonomy_equivariance.py'
SPEC = importlib.util.spec_from_file_location('physical_bridge_holonomy_equivariance', PATH)
he = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(he)


def test_prior_explicit_word_map_preserves_relator_and_cubes_to_identity():
    r = he.word_map_control()
    assert r['relator_preserved'] and r['third_power'] == ['a', 'b']
    assert r['h1_matrix'] == [[0, 1], [-1, -1]]
    bad = he.word_map_control(('a', 'a'))
    assert not bad['relator_preserved'] and bad['third_power'] != ['a', 'b']


def test_complete_numerical_geometry_control_and_two_cusp_descent():
    g = he.numerical_control()['geometry']
    assert not g['verified'] and len(g['isometries']) == 12 and g['faithful_h1_action']
    assert g['c3_normal'] and g['m004_symmetry_count'] == 8
    assert sum(r['h1_order'] == 3 for r in g['isometries']) == 2
    B = g['peripheral_columns']
    for r in g['isometries']:
        iso = (r['cusp_images'], tuple(map(sp.Matrix, r['cusp_maps'])))
        assert he.h1_action(B, iso).tolist() == r['h1_matrix']
    broken = (g['isometries'][0]['cusp_images'], tuple(map(sp.Matrix, g['isometries'][0]['cusp_maps'])))
    broken[1][1][0, 0] += 1
    with pytest.raises(ValueError):
        he.h1_action(B, broken)


def test_cusp_composition_keeps_target_indices_and_round_trips():
    s = ((1, 0), (sp.Matrix([[1, 1], [0, 1]]), sp.Matrix([[1, 0], [1, 1]])))
    identity = ((0, 1), (sp.eye(2), sp.eye(2)))
    assert he.compose(he.inverse_iso(s), s) == identity
    assert he.compose(s, he.inverse_iso(s)) == identity
    assert he.compose(s, s)[1][0] == s[1][1]*s[1][0]


def test_finite_character_enumeration_has_both_positive_and_continuous_controls():
    assert he.fixed_characters(-sp.eye(2)) == [(0, 0), (0, sp.Rational(1, 2)), (sp.Rational(1, 2), 0), (sp.Rational(1, 2), sp.Rational(1, 2))]
    for A in (sp.eye(2), sp.Matrix([[2, 0], [0, 1]])):
        with pytest.raises(ValueError):
            he.fixed_characters(A)
    with pytest.raises(ValueError):
        he.fixed_characters(-sp.eye(2), 0)


def test_c3_fixes_exactly_trivial_and_the_two_cube_root_characters():
    r = he.numerical_control()['algebra']
    expected = {(0, 0), (sp.Rational(1, 3), sp.Rational(2, 3)), (sp.Rational(2, 3), sp.Rational(1, 3))}
    assert {tuple(v['h']) for v in r['c3_fixed']} == expected
    for v in r['c3_fixed']:
        c = v['cohomology']
        assert c['relative_T'] == ([0, 4, 1, 0] if c['trivial'] else [0, 3, 0, 0])
        assert not c['exceptional'] and c['euler'] == -3


def test_nontrivial_c3_characters_form_a_pair_with_six_element_stabilizers():
    rows = he.numerical_control()['algebra']['c3_fixed']
    for r in rows:
        n = 1 if r['cohomology']['trivial'] else 2
        assert len(r['orbit']) == n and r['stabilizer_size']*n == 12
        if n == 2:
            assert r['stabilizer_orders'] == {1: 1, 2: 3, 3: 2}


def test_sixfold_and_full_scalar_invariance_force_trivial_character():
    r = he.numerical_control()['algebra']
    assert r['c6_fixed'] == r['full_group_fixed'] == [[0, 0]]
    assert not r['old_order_two']['c3_invariant'] and len(r['old_order_two']['orbit']) == 3
    assert all(r['polynomial_invariance'])


def test_simply_connected_fixed_holonomies_are_central_and_adjoint_trivial():
    r = he.numerical_control()['algebra']
    assert {tuple(v['h']) for v in r['simply_connected_c3_fixed']} == {(0, 0), (1, 2), (2, 1)}
    assert all(v['invariant_parent'] and v['adjoint_h'] == [0, 0] for v in r['simply_connected_c3_fixed'])
    assert r['parent']['coroot_period'] == 3 and r['parent']['adjoint_period'] == 1
    assert r['parent']['central_root_phases'] == [0]
    assert r['parent']['central_fundamental_phases'] == [sp.Rational(1, 3)]


def test_every_scalar_lift_of_pair_free_character_has_central_obstruction():
    r = he.numerical_control()['algebra']
    for v in r['c3_fixed']:
        lifts = v['parent_lifts']
        assert len(lifts) == 9 and all(p['invariant_adjoint'] for p in lifts)
        assert sum(p['invariant_parent'] for p in lifts) == (3 if v['cohomology']['trivial'] else 0)
        if not v['cohomology']['trivial']:
            assert all(p['central_defect_mod_three'] != [0, 0] for p in lifts)
    assert not r['physical_selection'] and not r['orbifold_projection_performed']


def test_basis_conjugation_preserves_continuous_fixed_point_classification():
    A = sp.Matrix([[0, 1], [-1, -1]])
    U = sp.Matrix([[1, 2], [0, 1]])
    conjugate = U.inv()*A*U
    actual = set(he.fixed_characters(conjugate))
    expected = {he.mod_vector(U.T*sp.Matrix(h)) for h in he.fixed_characters(A)}
    assert actual == expected and len(actual) == 3
