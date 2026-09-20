"""R38 exact controls; no claim to certify a global physical reduction."""
import importlib.util
from pathlib import Path

import pytest
import sympy as sp

SPEC = importlib.util.spec_from_file_location(
    'physical_bridge_parent_vertex', Path(__file__).resolve().parents[1]/
    'reports/physical_bridge_2026_09_05/parent_vertex.py')
pv = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(pv)


def test_complete_E8_roots_by_two_constructions_and_lattice():
    e = pv.embedding_controls()
    assert e['e8_root_count'] == 240
    assert e['e8_gram_det'] == abs(e['e8_basis_det']) == 1
    assert e['roots_norm_two'] and e['reflection_complete'] and e['e8_roots_integral']


def test_actual_H_cocharacters_integral_saturated_and_faithful():
    e = pv.embedding_controls()
    assert e['cocharacter_rank'] == 6
    assert e['cocharacter_integral'] and e['saturation_index'] == 1
    assert e['central_direction'] == pv.root_data()['U']
    assert e['d5_metric_correct'] and e['d5_roots_preserved']


def test_entire_248_weight_multiset_including_extra_fields():
    e = pv.embedding_controls()
    assert e['total_dimension'] == 248 and e['full_weight_multiset_matches']
    assert e['all_restricted_weights_integral']
    assert e['charge_dimensions'] == {-4: 3, -3: 16, -2: 30, -1: 48, 0: 54,
                                       1: 48, 2: 30, 3: 16, 4: 3}


def test_fields_equal_the_old_H_weights_not_just_dimensions():
    e = pv.embedding_controls()
    assert e['same_actual_spinor'] and e['same_actual_vector'] and e['same_actual_Q']
    assert e['same_euclidean_spinor']
    assert e['wrong_spinor_same_dimension'] and e['wrong_spinor_different']


def test_parent_change_is_not_an_extension_of_original_E6():
    e = pv.embedding_controls()
    assert e['original_adjoint_charge_dims'] == {-1: 16, 0: 46, 1: 16}
    assert e['old_simple_image_norm'] == 8 and e['old_simple_image_not_root']


def test_central_rescaling_mutant_fails_the_global_lattice():
    assert not pv.embedding_controls()['central_division_mutant_integral']


def test_each_family_block_is_the_full_actual_27_roster():
    f = pv.family_controls()
    assert f['each_full_H_27'] and f['family_roots'] == 81
    assert f['family_zero_roots'] == 72
    assert sorted(f['family_blocks'].values()) == [27, 27, 27]


def test_all_family_triples_and_invariant_tensor():
    f = pv.family_controls()
    assert f['zero_sum_triples'] == 270 and f['internal_triples'] == 45
    assert f['family_assignment_multiplicities'] == [6] and f['all_distinct_families']
    assert f['family_invariant_dimension'] == 1 and f['epsilon_invariant']


def test_nonzero_E8_root_channel_is_a_positive_control():
    f = pv.family_controls()
    assert f['witness_charges'] == [-1, -1, 2]
    assert f['witness_all_roots'] and f['witness_nonzero_bracket_root'] and f['witness_actual_fields']
    assert sum(f['charged_root_witness'], sp.zeros(8, 1)) == sp.zeros(8, 1)


def test_full_SO3_tensor_spaces_and_fixed_vector_mutant():
    i = pv.internal_controls()
    assert i['invariant_dimensions'] == {'1': 0, '2': 1, '3': 1}
    assert i['delta_invariant'] and i['epsilon_invariant']
    assert i['fixed_vector_not_invariant']
    assert i['delta_not_alternating'] and i['epsilon_not_symmetric']


def test_Grassmann_instrument_has_nonzero_and_zero_controls():
    a, b = sp.symbols('a b')
    assert pv.grassmann_coefficients(sp.Matrix([[0, a], [b, 0]])) == {(0, 1): a-b}
    assert pv.grassmann_coefficients(sp.eye(2)) == {}
    with pytest.raises(ValueError):
        pv.grassmann_coefficients(sp.ones(2, 3))


def test_zero_form_bracket_and_all_ten_family_blocks_cancel():
    s = pv.statistics_controls()
    assert s['color_antisymmetric'] and s['zero_form_matrix_symmetric']
    assert s['zero_form_coefficients'] == 0
    assert s['family_matrix_antisymmetric']
    assert s['parent_family_zero_form_coefficients'] == [0]*10


def test_one_form_and_mixed_parent_vertices_survive():
    s = pv.statistics_controls()
    assert s['one_form_matrix_antisymmetric']
    assert s['one_form_coefficients'] > 0 and s['mixed_species_coefficients'] > 0


def test_actual_added_EFT_Yukawa_is_not_killed_by_parent_test():
    s = pv.statistics_controls()
    assert s['all_ten_Y_symmetric']
    assert len(s['added_EFT_coefficients']) == 10
    assert all(n > 0 for n in s['added_EFT_coefficients'])


def test_wedge_and_metric_contractions_discriminate_both_ways():
    c = pv.contraction_controls()
    assert c == dict(equal_dot=1, equal_wedge=0, orthogonal_dot=0, orthogonal_wedge=-1)
