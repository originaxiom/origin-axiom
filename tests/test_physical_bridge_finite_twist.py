"""R27 finite controls, not a numerical proof of the all-cover analytic theorem."""
import importlib.util
from pathlib import Path

import pytest
import sympy as sp

SPEC = importlib.util.spec_from_file_location('r27_test', Path(__file__).resolve().parents[1]/
                                            'reports/physical_bridge_2026_09_05/finite_twist.py')
m = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(m)


@pytest.mark.parametrize('power', range(1, 7))
def test_bochner_term_is_exactly_positive_for_nontrivial_control_modules(power):
    r = m.bochner(power)
    assert r['sl2_relations'] and r['e_adjoint_is_f'] and r['y_hermitian']
    for row in r['degrees']:
        assert row['hermitian'] and row['strictly_positive']
        assert row['rank'] == 3*(power+1)
        assert all(x > 0 for x in row['leading_minors'])


def test_trivial_geometric_representation_has_no_bochner_positive_bound():
    r = m.bochner(0)
    assert all(row['zero'] and not row['strictly_positive'] and row['rank'] == 0 for row in r['degrees'])
    with pytest.raises(ValueError):
        m.symmetric_lie(-1)


@pytest.mark.parametrize('degree', [1, 2, 3, 4, 6])
def test_actual_cellular_transfer_commutes_and_splits_pullback_in_characteristic_zero(degree):
    r = m.circle_transfer(degree)
    assert r['pullback_chain'] and r['trace_chain']
    assert r['trace_pullback'] == degree and r['projector'] and r['projector_rank'] == 1
    assert r['wrong_character_pullback_rejected']


def test_inverse_degree_argument_requires_the_coefficient_characteristic():
    r = m.lift_and_duality_controls()
    assert r['characteristic_three_degree_three_trace'] == 0
    assert 6*r['characteristic_thirteen_degree_six_invertible'] % 13 == 1
    with pytest.raises(ValueError):
        pow(3, -1, 3)


def test_restriction_to_a_changing_kernel_need_not_be_lower_semicontinuous():
    a, b = m.rank_jump()
    assert (a['parameter'], a['rank_j'], a['restriction_rank']) == (1, 0, 1)
    assert (b['parameter'], b['rank_j'], b['restriction_rank']) == (2, 1, 0)
    assert a['polynomial_map_rank'] == b['polynomial_map_rank'] == 1
    assert all(r['restriction_rank'] == r['stack_difference'] for r in (a, b))


def test_minus_identity_relator_is_invalid_for_an_odd_symmetric_power():
    r = m.lift_and_duality_controls()
    assert r['not_honest_sl2'] and r['psl_relator'] == m.mod(-sp.eye(2))
    assert r['odd_power_relator'] == m.mod(-sp.eye(4))
    assert r['even_power_relator'] == sp.eye(3)


def test_literal_dual_matrix_inequality_is_not_non_self_duality():
    r = m.lift_and_duality_controls()
    assert r['literal_dual_inequality'] and r['actual_self_duality']


def test_modular_rank_uses_the_actual_field_and_cross_checks_its_kernel():
    a = sp.Matrix([[1, 0], [0, 13]])
    assert a.rank() == 2 and m.rank(a) == 1
    assert m.kernel(a) == sp.Matrix([[0], [1]])
    assert m.rank(sp.zeros(0, 3)) == 0 and m.rank(sp.zeros(3, 0)) == 0


@pytest.fixture(scope='module')
def witness():
    return m.finite_field_witness()


def test_received_finite_field_positive_is_recomputed_with_both_cochain_maps(witness):
    a, b, pair = witness['V'], witness['dual'], witness['pair']
    assert all(a['checks'].values()) and all(b['checks'].values())
    assert a['two_constructions_agree'] and b['two_constructions_agree']
    assert (a['t0'], b['t0'], a['r1'], b['r1']) == (1, 1, 0, 2)
    assert (a['n'], b['n'], pair['index']) == (1, 0, 1)
    assert all(pair['identities'].values()) and pair['domain_equalities']
    assert a['restriction_stack_rank'] == a['r1'] and b['restriction_stack_rank'] == b['r1']


def test_domain_input_is_an_actual_irreducible_representation_and_unipotent_cusp(witness):
    assert witness['generated_algebra_dimension'] == 16
    c = witness['cusp']
    assert c['mu_nontrivial'] and c['nilpotent_square'] == sp.zeros(2)
    assert c['one_parameter'] and c['character_trivial'] and c['character_relators']
    assert witness['invalid_mutation'] is not None
    assert witness['base_pairing_invariant']


def test_non_self_duality_has_an_actual_obstruction_and_dual_character_map(witness):
    assert witness['intertwiner_dimension'] == 0
    t = witness['trace_obstruction']
    assert t and t['trace'] != t['dual_trace']
    assert witness['inverse_character_intertwines_dual']
    assert witness['inverse_character']['n'] == witness['dual']['n']
    assert witness['untwisted_pair']['index'] == 0


def test_one_boundary_image_is_isotropic_while_its_dual_image_is_not(witness):
    assert witness['cup_V']['rank'] == 0
    assert witness['cup_dual']['rank'] == 2 and witness['cup_dual']['symmetric']


def test_symmetric_power_respects_actual_matrix_multiplication(witness):
    a, b = [witness['rho2'][g] for g in witness['generators']]
    assert m.sym_power(m.mod(a*b), 3) == m.mod(m.sym_power(a, 3)*m.sym_power(b, 3))
    assert m.sym_power(m.inverse(a), 3) == m.inverse(m.sym_power(a, 3))
