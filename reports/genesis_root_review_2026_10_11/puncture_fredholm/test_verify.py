import pytest
import sympy as s
import verify as v


def test_literal_coefficient():
    a, b = v.coefficient()
    assert a.shape == b.shape == (6, 6)
    assert a*b*a.inv()*b.inv() == -s.eye(6)
    assert a.det() == b.det() == 1


def test_all_rank_domains():
    for rank in range(7):
        for mixed in (False, True):
            data = v.boundary(v.projector(rank, mixed))
            assert data['plus_rank'] == rank
            assert data['full_rank'] == 6
            assert data['green_zero'] and data['grading_kept']


def test_non_projector_rejected():
    with pytest.raises(ValueError):
        v.boundary(2*s.eye(6))
    bad = s.eye(6)
    bad[0, 1] = 1
    with pytest.raises(ValueError):
        v.boundary(bad)


def test_wrong_size_and_rank_rejected():
    with pytest.raises(ValueError):
        v.boundary(s.eye(5))
    with pytest.raises(ValueError):
        v.projector(7)


def test_entire_finite_record():
    result = v.run()
    assert result['all_passed']
    assert len(result['profiles']) == 14
    assert {row['predicted_chiral_index'] for row in result['profiles']} == set(range(-3, 4))
