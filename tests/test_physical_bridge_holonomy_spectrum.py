"""R19: full relative character spectrum and actual-parent consistency controls."""
import importlib.util
from pathlib import Path

import pytest
import sympy as sp

SOURCE = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/holonomy_spectrum.py'
SPEC = importlib.util.spec_from_file_location('physical_bridge_holonomy_spectrum', SOURCE)
hs = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(hs)


def test_actual_presentation_asphericity_hypotheses_and_power_mutants():
    import snappy
    Q = snappy.Manifold('m202')
    pi = Q.fundamental_group()
    assert list(pi.generators()) == ['a', 'b'] and list(pi.relators()) == [hs.RELATOR]
    h = hs.relator_hypotheses(hs.RELATOR)
    assert h['nonproper_power'] and h['proper_periods'] == []
    assert hs.relator_hypotheses('abABabAB')['proper_periods'] == [4]
    assert not hs.relator_hypotheses('abBA')['cyclically_reduced']
    assert not hs.relator_hypotheses('')['nonproper_power']


def test_three_fox_calculations_and_full_character_identity():
    r = hs.identities()
    x, y = hs.X, hs.Y
    expected = x*x*y+x*x+x*y*y+x*y+x+y*y+y
    assert sp.expand(r['polynomial']-expected) == 0
    assert r['pinned_match'] and r['second_method'] and r['nilpotent'] and r['factorization']
    assert r['unitary_locus'] and r['inversion'] and r['missing_term_fails']
    assert hs.fox_row('abAB') == sp.Matrix([[1-y, x-1]])
    assert hs.triangular_row('abAB') == sp.Matrix([[1-y, x-1]])


def test_trivial_holonomy_retains_four_one_all_degrees():
    r = hs.cochains(1, 1)
    assert r['base_betti'] == [1, 2, 1, 0]
    assert r['relative_T'] == [0, 4, 1, 0] and r['relative_E_dual'] == [0, 1, 4, 0]
    assert r['polynomial'] == '7' and r['euler'] == -3


@pytest.mark.parametrize('x,y', [(-1, 1), (1, -1), (-1, -1)])
def test_every_nontrivial_order_two_character_removes_extra_pair(x, y):
    r = hs.cochains(x, y)
    assert r['base_betti'] == [0, 0, 0, 0]
    assert r['relative_T'] == [0, 3, 0, 0] and r['relative_E_dual'] == [0, 0, 3, 0]
    assert r['differential_ranks'] == [1, 1, 0] and r['exact_sequence_matches']


def test_exact_order_three_and_four_grids_are_controls_not_a_census():
    rows = hs.character_controls()
    assert len(rows) == 31
    for n in (2, 3, 4):
        group = [r for r in rows if r['grid_n'] == n]
        assert len(group) == n*n and sum(r['trivial'] for r in group) == 1
        assert all(r['exact_sequence_matches'] and r['euler'] == -3 for r in group)
    three = [r for r in rows if r['grid_n'] == 3 and not r['trivial']]
    assert len(three) == 8 and all(r['relative_T'] == [0, 3, 0, 0] for r in three)


def test_nontrivial_exceptional_unitary_roots_do_not_remove_the_pair():
    for sign in (-1, 1):
        z = (-3+sign*sp.I*sp.sqrt(7))/4
        r = hs.cochains(z, z)
        assert not r['trivial'] and r['exceptional'] and r['polynomial'] == '0'
        assert r['base_betti'] == [0, 1, 1, 0]
        assert r['relative_T'] == [0, 4, 1, 0] and r['relative_E_dual'] == [0, 1, 4, 0]


def test_source_component_count_and_zero_arc_control():
    for k in range(4):
        r, t = hs.cochains(-1, 1, k), hs.cochains(1, 1, k)
        assert r['relative_T'] == [0, k, 0, 0]
        assert t['relative_T'] == ([0, k+1, 1, 0] if k else [1, 2, 1, 0])
        assert r['exact_sequence_matches'] and t['exact_sequence_matches']
    r = hs.cochains(-1, 1, 3, [1, sp.I, -1])
    assert r['relative_T'] == [0, 3, 0, 0]


def test_nonunitary_inexact_and_invalid_topology_inputs_rejected():
    for x, y, k in [(2, 1, 3), (0, 1, 3), (-1., 1, 3), (-1, 1, -1), (-1, 1, 1.5)]:
        with pytest.raises(ValueError):
            hs.cochains(x, y, k)
    with pytest.raises(ValueError):
        hs.cochains(-1, 1, 3, [1, 1, 2])


def test_unitary_flat_covariant_homotopies_and_curvature_mutant():
    r = hs.covariant_controls()
    assert len(r['rows']) == 8
    assert all(v['homotopy'] and v['weighted_conjugacy'] and v['flat_square'] for v in r['rows'])
    assert r['curved_square_nonzero'] and r['unitary_gauge_norm'] == 1
    assert r['strong_plus'] == 'relative_T' and r['strong_minus'] == 'relative_E'


def test_actual_e6_weights_parent_period_and_normalization():
    r = hs.parent_controls()
    assert r['root_count'] == 72 and r['fundamental_weight_count'] == 27 and r['r15_match']
    assert r['adjoint_charge_dimensions'] == {'-1': 16, '0': 46, '1': 16}
    assert r['cocharacter_denominator'] == 3 and r['pi_u_parent_order'] == 6 and r['pi_u_adjoint_order'] == 2
    assert r['fundamental_u_charges'] == {'-2/3': 10, '1/3': 16, '4/3': 1}
    assert r['fundamental_psi_charges'] == {'-2': 10, '1': 16, '4': 1}
    assert not r['parent_connection_and_sources_selected']


def test_anomaly_is_net_chirality_not_the_extra_pair():
    r = hs.parent_controls()
    expected = dict(Tr_u=48, Tr_u3=48, Spin10_squared_u=6, mixed_matrix_matches=True)
    assert r['anomaly_four_one'] == r['anomaly_three_zero'] == expected
    assert r['anomaly_vectorlike_pair'] == dict(Tr_u=0, Tr_u3=0, Spin10_squared_u=0, mixed_matrix_matches=True)
    assert r['spinor_vector_trace_ratio_two'] and r['pure_spin10_cubic'] == 0
    assert r['b864_spinor_charge_one'] == dict(tr=16, tr3=16, so10sq=2)


def test_full_27_cancels_its_own_anomaly_not_a_preexisting_one():
    r = hs.parent_controls()
    a = r['anomaly_full_27']
    assert a['Tr_u'] == a['Tr_u3'] == 0 and a['mixed_matrix'] == sp.zeros(5)
    assert r['b864_parent_psi'] == dict(tr=0, tr3=0, so10sq=0)
    assert r['anomaly_three_zero']['Tr_u3']+a['Tr_u3'] != 0


def test_cusp_periods_price_the_flat_connection_not_the_gauge_zero_mode():
    import snappy
    pi = snappy.Manifold('m202').fundamental_group()
    exponents = [[w.count(c)-w.count(c.upper()) for c in ('a', 'b')]
                 for pair in pi.peripheral_curves() for w in pair]
    assert sp.Matrix(exponents).rank() == 2
    r = hs.cusp_norm_controls()
    assert r['constant_gauge_zero_form'].is_finite is not False
    assert sp.simplify(r['constant_gauge_zero_form']-sp.exp(-2*sp.Symbol('S', real=True))/2) == 0
    assert r['nonzero_period_one_form'] == sp.oo
