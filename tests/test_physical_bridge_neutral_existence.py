"""R51 exact finite locks; global analysis remains an authored argument."""
import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/neutral_existence.py'
SPEC = importlib.util.spec_from_file_location('r51_neutral_existence', PATH)
r = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(r)


def test_finite_energy_on_canonical_not_old_hyperbolic_end():
    assert all(r.energy_controls().values())


def test_anchored_hardy_identity_and_false_unanchored_control():
    assert all(r.hardy_controls().values())
    assert r.hardy_integrals((1,)) == (1, 0, 1)


@pytest.mark.parametrize('poly', [(0, 1), (1, -2, 3), (0, 0, 0, 1), (1, 2, 3, 4, 5)])
def test_exact_polynomial_integrals_obey_anchored_bound(poly):
    I, J, B = r.hardy_integrals(poly)
    assert I <= 2*B+4*J


def test_model_radial_correction_is_not_a_bounded_gauge_claim():
    assert all(r.model_controls().values())


def test_target_anchoring_needs_full_algebra_not_scalar_commutant():
    assert all(r.algebra_controls().values())


def test_actual_word_basis_controls_are_not_an_all_q_density_proof():
    values = r.word_controls()
    assert len(values) == 4 and all(values.values())


def test_trivial_holonomy_does_not_have_a_unique_positive_metric():
    s = r.s
    identity = s.eye(4)
    assert r.commutant_dimension((identity,)) == 16
    H1, H2 = identity, s.diag(2, s.Rational(1, 2), 1, 1)
    assert H1.det() == H2.det() == 1 and H1 != H2


def test_all_declared_finite_predicates():
    groups = r.controls()
    assert sum(map(len, groups.values())) == 29
    assert all(bool(v) for group in groups.values() for v in group.values())
