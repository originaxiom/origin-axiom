"""R32 exact module controls, not tests that certify the whole analytic proof."""
import importlib.util
import itertools
from pathlib import Path

import pytest
import sympy as sp

PATH = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/source_c3.py'
SPEC = importlib.util.spec_from_file_location('physical_bridge_source_c3', PATH)
sc = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(sc)


def test_actual_words_fixed_characters_and_fox_acyclicity():
    d = sc.actual_characters()
    assert d['A'] == sp.Matrix([[-1, -1], [1, 0]])
    assert d['A'].charpoly().as_expr() == sp.Symbol('lambda')**2+sp.Symbol('lambda')+1
    assert all(d['checks'].values())
    assert {tuple(r['h']) for r in d['rows']} == {(0, 0), (sp.Rational(1, 3), sp.Rational(2, 3)), (sp.Rational(2, 3), sp.Rational(1, 3))}
    for r in d['rows']:
        if any(r['h']):
            assert r['P'] == -2 and r['base'] == r['resolved'] == [0, 0, 0, 0]
            assert r['relative'] == [0, 3, 0, 0] and r['split'] == [3, 3, 0, 0]


def test_exact_fixed_fibre_trace_and_independent_integer_reduction():
    survivors = sc.zero_trace_triples()
    assert len(survivors) == 6
    for triple in itertools.product(range(3), repeat=3):
        n = [triple.count(a) for a in range(3)]
        rational_coefficients = (n[0]-n[2], n[1]-n[2])
        assert (triple in survivors) == (rational_coefficients == (0, 0))
    assert set(survivors) == set(itertools.permutations(range(3)))
    assert (0, 0, 0) not in survivors and sc.clean(3*sc.weight(0)) == 3


@pytest.mark.parametrize('phase,generator', itertools.product(range(3), (1, 2)))
def test_honest_projector_all_lifts_and_both_generators(phase, generator):
    U = sc.action([0, 1, 2], phase, generator)
    P = sc.projector(U)
    assert sc.matrix(U.H*U) == sp.eye(3)
    assert sc.matrix(P*P) == P == sc.matrix(P.H)
    assert P.rank() == 1 and sc.matrix(U*P) == P
    assert sum((sc.projector(sc.weight(a)*U) for a in range(3)), sp.zeros(3)) == sp.eye(3)


def test_basis_change_and_permutation_regular_module():
    U = sc.action([0, 1, 2])
    O = sp.Matrix([[sp.Rational(3, 5), -sp.Rational(4, 5), 0], [sp.Rational(4, 5), sp.Rational(3, 5), 0], [0, 0, 1]])
    assert O.T*O == sp.eye(3)
    assert sc.projector(sc.matrix(O*U*O.T)) == sc.matrix(O*sc.projector(U)*O.T)
    cycle = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    assert sc.projector(cycle) == sp.ones(3)/3
    assert cycle.charpoly().as_expr() == sp.Symbol('lambda')**3-1
    # Regular module does not imply equal masses in different irreducibles.
    H = sp.diag(1, 4, 9)
    assert H*U == U*H and len(H.eigenvals()) == 3


@pytest.mark.parametrize('phase,expected', [(0, [0, 2, 1]), (1, [0, 1, 0]), (2, [0, 1, 0])])
def test_trivial_line_cone_is_not_the_acyclic_case(phase, expected):
    d = sc.trivial_cone(phase)
    assert d['projected_betti'] == expected
    assert d['odd_minus_even'] == d['index_from_character'] == 1
    assert d['base_lefschetz'] == d['fixed_fibre_trace'] != 0


@pytest.mark.parametrize('t', [0, 1, 2, sp.Rational(1, 7)])
def test_equivariant_core_attachment_keeps_both_parities(t):
    for phase in range(3):
        r = sc.core_complex(t, phase)
        assert r['projected_betti'] == ([1, 1] if t == 0 else [0, 0])
        assert r['retained_even'] == r['retained_odd'] == 1
        assert r['commutes'] and r['positive_square'] and r['honest_projection_commutes']
        assert r['drop_core_commutes'] == (t == 0)


def test_tensor_factor_control_and_noncentral_qualification():
    for multiplicities in itertools.product(range(3), repeat=3):
        for phase in range(3):
            assert sc.tensor_invariants(multiplicities, phase) == sum(multiplicities)
    # Explicit tensor projectors, not only modular weight counting.
    for W in (sc.action([0, 0]), sc.action([1, 1]), sc.action([0, 1, 2])):
        assert sc.projector(sp.kronecker_product(sc.action([0, 1, 2]), W)).rank() == W.rows


@pytest.mark.parametrize('n', [1, 2, 5])
def test_projection_can_leave_unpaired_zero_modes_but_pairs_positive_modes(n):
    r = sc.reflection_circle(n)
    assert r['zero_betti'] == [1, 0]
    assert r['positive_even'] == r['positive_odd'] == 1
    assert r['positive_acyclic'] == [0, 0]
    assert r['intertwines'] and r['commutes'] and r['square']


def test_closed_fixed_circle_contributes_zero_but_an_arc_does_not():
    for phase in range(3):
        lam = sc.weight(phase)
        circle_trace = lam-lam  # one vertex and one edge, same fixed-fibre action
        arc_trace = 2*lam-lam  # two endpoints and the fixed edge
        assert sc.clean(circle_trace) == 0
        assert sc.clean(arc_trace-lam) == 0 and lam != 0


def test_reject_wrong_group_lift_noncomplex_and_nonequivariant_attachment():
    with pytest.raises(ValueError):
        sc.projector(sp.diag(1, -1), 3)
    with pytest.raises(ValueError):
        sc.projected_betti([sp.eye(3)], [sc.action([0, 1, 2]), sp.eye(3)])
    with pytest.raises(ValueError):
        sc.projected_betti([sp.eye(1), sp.eye(1)], [sp.eye(1)]*3)
    with pytest.raises(ValueError):
        sc.action([0, 1, 2], generator=0)
    with pytest.raises(ValueError):
        sc.weight(0.5)
    with pytest.raises(ValueError):
        sc.core_complex(0.1)
    with pytest.raises(ValueError):
        sc.tensor_invariants([1, -1, 1])
    with pytest.raises(ValueError):
        sc.reflection_circle(0)
