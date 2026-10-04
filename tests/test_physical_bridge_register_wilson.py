"""Live R90 exact observables and same-author independent arithmetic controls."""
from fractions import Fraction
import importlib.util
from pathlib import Path

import pytest

BASE = Path(__file__).resolve().parents[1] / 'reports' / 'physical_bridge_2026_09_05'


def load(name):
    spec = importlib.util.spec_from_file_location(name, BASE / (name + '.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


N = load('register_wilson')
R = load('register_wilson_reference')


def test_actual_root_roster_and_wrong_conjugation():
    ns = N.retained()
    assert ns['root_weights']() == ns['roster']()
    wrong = ns['BRANCHES'][:4] + (('5', '10'), ('bar5', 'bar10'))
    assert sum(ns['roster'](wrong).values()) == 248
    assert ns['roster'](wrong) != ns['root_weights']()


def test_haar_integrates_weights_not_inserted_multiplicities():
    assert N.weyl_density()[N.ZERO] == 120
    for a in N.LABELS:
        for b in N.LABELS:
            assert N.haar(N.char(a), N.char(b)) == int(a == b)


def test_formal_register_connected_to_haar_and_dual():
    c = N.sum_chars((1, N.char('10')), (1, N.char('bar5')))
    for probe, amplitude in (('10', 1), ('5', -1)):
        assert N.haar(c, N.probe(probe)) == amplitude
        assert N.haar(N.conjugate(c), N.probe(probe)) == -amplitude
        paired = N.sum_chars((2, c), (2, N.conjugate(c)))
        assert N.haar(paired, N.probe(probe)) == 0
        assert sum(paired.values()) == 60


def test_anomaly_free_is_not_duality_even():
    c = N.sum_chars((1, N.char('10')), (1, N.char('bar5')))
    block = (1, 1, 1, 1, -4)
    assert N.moment(c, block, 3) == 0
    assert N.moment(c, block, 5) == 240
    assert c != N.conjugate(c)


def test_full_cartan_symbolic_identity_and_anomalous_control():
    out = N.audit()
    for name in ('linear_trace_universal_zero', 'cubic_anomaly_universal_zero',
                 'quintic_universal_identity', 'quintic_universal_not_zero',
                 'anomalous_control_cubic', 'anomalous_control_not_zero'):
        assert out['checks'][name]


def test_exact_unitary_holonomy_and_its_reverse():
    c = N.sum_chars((1, N.char('10')), (1, N.char('bar5')))
    odd = N.sum_chars((1, c), (-1, N.conjugate(c)))
    block = (1, 1, 1, 1, -4)
    assert N.seventh(odd) == R.cyclic_odd(block) == (-4, -8, 2, -9, 1, -10)
    assert N.seventh(odd, tuple(-x for x in block)) == tuple(-x for x in N.seventh(odd))
    assert N.seventh(odd, (0,) * 5) == (0,) * 6


def test_no_silent_nontraceless_holonomy():
    with pytest.raises(ValueError):
        N.seventh(N.char('5'), (1, 1, 1, 1, 1))
    with pytest.raises(ValueError):
        N.moment(N.char('5'), (Fraction(1),) * 5, 3)
    with pytest.raises(ValueError):
        R.moments([1] * 5, 3)


def test_full_parent_even_does_not_erase_neutral_detector():
    actual = N.retained()['root_weights']()
    assert actual == N.conjugate(actual)
    assert sum(actual.values()) == 248
    assert N.audit()['checks']['odd_character_not_zero']


def test_reference_grid_and_moments_are_live_computations():
    native, reference = N.audit(), R.audit()
    assert native['passed'] == native['total']
    assert reference['passed'] == reference['total']
    assert native['total'] > 36
    assert reference['total'] > 81
    assert R.grid_gram() == [[int(i == j) for j in range(6)] for i in range(6)]


def test_parity_slots_and_source_scope_kept_separate():
    out = N.audit()
    for name in ('two_odd_slots_joint_even', 'fixed_probe_hears_linearly',
                 'both_scaled_quadratic', 'fixed_gauge_character_structure_variation_5'):
        assert out['checks'][name]
    assert not out['source_generated']
    assert not out['physical_chirality_derived']
    assert not out['quantum_measure_derived']
    assert not out['full_goal_achieved']
