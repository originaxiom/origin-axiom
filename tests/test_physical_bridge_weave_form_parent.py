"""Live algebraic locks; not nonauthor/global PDE or full physics acceptance."""
from collections import Counter
import importlib.util
from pathlib import Path
import pytest
import sympy as s

PACKET = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/weave_form_parent_2026_10_08'


def load(name):
    spec = importlib.util.spec_from_file_location('form_parent_'+name, PACKET/(name+'.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope='module')
def native():
    return load('probe')


def test_native_and_separate_reference(native):
    a, b = native.run(), load('reference').run()
    assert all(a['facts'].values()) and all(b['predicates'].values())
    for key in ('cover_H1_character', 'cover_holomorphic_character', 'adjoint_Q8_multiplicities',
                'form_kernel_dimensions', 'parent_left_twisted_charges', 'gauge_dimensions',
                'weak_doublets_in_FORM_sector', 'bilinear_profile', 'zero_angular_form_squared_mass'):
        assert a[key] == b[key]


def test_cell_boundaries_and_deck_maps(native):
    _, _, d1, d2, ok, character = native.quaternion_complex()
    assert d1*d2 == s.zeros(4, 8) and ok
    assert [d1.rank(), d2.rank()] == [3, 7]
    assert character == [6, -2, 2, 2, 2, 2, 2, 2]


def test_holomorphic_family_not_counted_twice(native):
    k = native.run()['form_kernel_dimensions']
    assert k['W6_one_Hodge_type'] == 3
    assert k['adjoint_one_Hodge_type'] == 111 != 55+3*56


def test_all_generic_hypercharge_weights_retained(native):
    a, b = native.gauge_roster()
    assert [native.dimension(a), native.dimension(b), native.dimension(a+b)] == [55, 56, 111]
    assert all(v == 0 for v in native.charge_asymmetry(a+b).values())


def test_hermitian_conjugate_not_an_added_left_mirror(native):
    left = Counter({(3, 2, 1, 0): 1})
    right_conjugate = Counter({native.dual_key(k): v for k, v in left.items()})
    assert any(v for v in native.charge_asymmetry(left).values())
    # Only an INDEPENDENT LEFT mirror is added to the left roster here.
    assert all(v == 0 for v in native.charge_asymmetry(left+right_conjugate).values())


def test_complex_unpaired_fundamental_has_no_mass(native):
    generators = [s.diag(1, -1, 0), s.diag(0, 1, -1),
                  s.Matrix([[0, 1, 0], [0, 0, 0], [0, 0, 0]]),
                  s.Matrix([[0, 0, 0], [0, 0, 1], [0, 0, 0]])]
    assert native.invariant_bilinears(generators) == []


def test_adjoint_doublet_symmetric_mass_absent(native):
    _, ad, _ = native.sl3_adjoint()
    sl2 = [s.diag(1, -1), s.Matrix([[0, 1], [0, 0]]), s.Matrix([[0, 0], [1, 0]])]
    b3, b2 = native.invariant_bilinears(ad), native.invariant_bilinears(sl2)
    assert len(b3) == len(b2) == 1
    mass = s.kronecker_product(b3[0], b2[0])
    assert mass.rank() == 16 and mass.T == -mass
    assert mass+mass.T == s.zeros(16)


def test_two_doublets_have_full_rank_symmetric_mass(native):
    eps = s.Matrix([[0, 1], [-1, 0]])
    mass = s.kronecker_product(eps, eps)
    assert mass.T == mass and mass.rank() == 4
    gens = [s.kronecker_product(s.eye(2), a) for a in [s.diag(1, -1), s.Matrix([[0, 1], [0, 0]])]]
    assert native.invariant(mass, gens)


def test_arbitrary_family_pairing_is_not_gauge_invariant(native):
    _, ad, _ = native.sl3_adjoint()
    eps = s.Matrix([[0, 1], [-1, 0]])
    wrong = s.kronecker_product(s.diag(1, -1, *([0]*6)), eps)
    assert not native.invariant(wrong, [s.kronecker_product(a, s.eye(2)) for a in ad])


def test_full_parent_slots_not_discarded(native):
    rows = native.parent_slots()
    assert len(rows) == 4 and [x['qt'] for x in rows] == [2, 0, -1, -1]
    assert sum(abs(x['qt']) == 1 for x in rows) == 2


def test_wrong_twist_changes_kinetic_dictionary(native):
    assert [x['qt'] for x in native.parent_slots(0)] == [1, 1, -1, -1]
    assert [x['qt'] for x in native.parent_slots(-1)] == [0, 2, -1, -1]


def test_branch_pullback_and_form_radial_positive_control(native):
    result = native.run()
    assert result['facts']['square_root_pole_pulls_back_regular']
    assert result['facts']['form_radial_squared_mass_quarter']
    assert result['facts']['form_radial_not_ordinary_spin_massless']


def test_kinetics_and_gauge_interactions_not_removed(native):
    _, mats, gram = native.sl3_adjoint()
    assert any(a != s.zeros(8) for a in mats)
    assert all(gram[:n, :n].det() > 0 for n in range(1, 9))
    assert native.run()['weak_doublets_in_FORM_sector'] % 2 == 0


def test_no_full_physical_promotion(native):
    result = native.run()
    for k in ('complete_companion_spectrum_computed', 'full_curved_interacting_parent_certified',
              'global_physical_Fredholm_index_certified', 'generated_twist_or_action_selected',
              'physical_chiral_SM_derived', 'nonauthor_acceptance'):
        assert result[k] is False
