import pytest
import sympy as s
import verify as v


def test_cusp_threshold_and_inverse():
    assert v.cusp_map(s.Rational(3, 8)) == (s.Rational(7, 8), 0)
    assert v.cusp_map(s.Rational(1, 2)) == (0, 1)
    assert v.cusp_map(s.Rational(7, 8)) == (s.Rational(3, 8), 1)
    with pytest.raises(ValueError):
        v.cusp_map(1)


def test_spectral_control():
    t = s.ImmutableMatrix(s.diag(1, -1, s.I))
    assert v.exponents(t) == (0, s.Rational(1, 4), s.Rational(1, 2))
    with pytest.raises(ValueError):
        v.exponents(s.ImmutableMatrix([[2]]))


def test_symbolic_boolean_count_regression():
    assert v.high_count([s.Rational(j, 8) for j in (1, 3, 7)]) == 1
    assert v.high_count([s.Rational(j, 8) for j in (1, 5, 7)]) == 2
    assert v.high_count([s.Rational(1, 2)]) == 1
    assert v.high_count([]) == 0


def test_triplet_exponents_and_sign():
    _, t, _ = v.representations()['T']
    assert v.exponents(s.ImmutableMatrix(t)) == tuple(s.Rational(j, 8) for j in (1, 3, 7))
    assert v.exponents(s.ImmutableMatrix(-t)) == tuple(s.Rational(j, 8) for j in (3, 5, 7))


def test_central_mismatch_rejected():
    a, b, _ = v.representations()['T']
    with pytest.raises(ValueError):
        v.chi(1, a, b)


def test_record_and_nonzero_correction():
    result = v.run()
    assert result['all_passed']
    rows = [r for r in result['rows'] if 'high_count' in r]
    assert len(rows) == 10
    assert all(r['original_chi'] == '0' and r['shifted_chi'] != '0' for r in rows)
