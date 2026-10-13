import pytest
import sympy as s
import verify as v


def test_all_exact_guards():
    result = v.run()
    assert result['all_passed'], [name for name, passed in result['checks'].items() if not passed]


def test_wrong_cusp_transport_rejected():
    a, _, _ = v.coefficient()
    with pytest.raises(ValueError):
        v.inverse_minus_identity(a)


def test_noncommuting_link_rejected():
    a, b, _ = v.coefficient()
    with pytest.raises(ValueError):
        v.complex_matrices(a, b)


def test_trivial_and_invariant_controls_survive():
    assert v.betti(s.eye(2), s.eye(2)) == (2, 4, 2)
    assert v.betti(s.diag(1, -1), s.diag(1, -1)) == (1, 2, 1)


def test_reversed_and_swapped_branches_remain_acyclic():
    a, _, t = v.coefficient()
    assert v.betti(t, a*t) == (0, 0, 0)
    assert v.betti((a*t).H, t.H) == (0, 0, 0)


def test_cover_cohomology_is_not_downstairs_cohomology():
    a, _, t = v.coefficient()
    assert v.betti(a*t, t) == (0, 0, 0)
    assert v.betti((a*t)**8, t**8) == (6, 12, 6)


def test_phase_detector_rejects_nonroot():
    with pytest.raises(ValueError):
        v.eighth_exponent(s.Integer(2))
