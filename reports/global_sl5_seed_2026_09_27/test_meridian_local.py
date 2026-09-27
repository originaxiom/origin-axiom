import pytest
from flint import fmpq_mat

from verify_global_seed import (
    DEGREE, Rep, cohom, eye, indexed, kron, native_doublet, one_twist,
    parent, scalar_rep, transfer_pair, zero,
)
from verify_meridian_local import fixed_meridian_jacobian, off_block_rep, trace_comparators
from verify_topology import data


@pytest.mark.parametrize("which", ["rho", "line"])
def test_nontrivial_family_links_are_acyclic(which):
    rep = transfer_pair(native_doublet() if which == "rho" else scalar_rep(0))
    result = indexed(rep, 2)
    assert result["V"] == result["dual"] == (0, 0, 0, 0, 0)


def test_full_off_block_relative_jacobian_is_square_and_invertible():
    rep = off_block_rep()
    jac = fixed_meridian_jacobian(rep)
    assert rep.d//DEGREE == 14
    assert jac.nrows() == jac.ncols() == jac.rank() == 112
    assert jac.det() != 0
    assert (rep.mats[0]-eye(rep.d)).rank() == rep.d


def test_smaller_mixed_direction_is_not_falsely_removed():
    p = fmpq_mat(data()["regular_C3"])
    rep = Rep([kron(p**k, a) for a, k in zip(native_doublet().mats, data()["M2_to_C3"])])
    jac = fixed_meridian_jacobian(rep)
    raw = (jac.ncols()-jac.rank())//DEGREE
    gauge = (rep.d-(rep.mats[0]-eye(rep.d)).rank())//DEGREE-cohom(rep, 2)[0]
    assert raw == 2 and gauge == 1 and raw-gauge == 1


def test_off_block_character_matches_actual_parent():
    assert trace_comparators() == 7


def test_central_twists_have_same_actual_adjoint_action():
    base = parent(0)
    for q in range(1, 5):
        twisted = parent(q)
        for i in range(5):
            for j in range(5):
                eij = zero(5, 5)
                eij[i, j] = 1
                x = kron(eij, eye(4))
                for g in range(3):
                    assert base.mats[g]*x*base.invs[g] == twisted.mats[g]*x*twisted.invs[g]


def test_post_result_lock_of_joint_indices_and_H0_corrections():
    expected = [(0, 0), (0, 3), (1, 0), (-1, 0), (0, -3)]
    for q, pair in enumerate(expected):
        row = one_twist(q)
        assert (row["E"]["up"]["I"], row["wedge2E"]["up"]["I"]) == pair
    row = one_twist(1)["E"]["up"]
    assert row["V"][2]-row["V"][4] == 1 and row["I"] == 0
    row = one_twist(2)["wedge2E"]["up"]
    assert row["V"][2]-row["V"][4] == -3 and row["I"] == 0
