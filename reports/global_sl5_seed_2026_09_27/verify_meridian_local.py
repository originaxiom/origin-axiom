"""Post-result, separately sealed fixed-meridian local test."""
import json

from verify_global_seed import (
    DEGREE, Rep, blockdiag, cohom, eye, hs, indexed, kron, native_doublet,
    parent, scalar_rep, submatrix, transfer_pair, vs, zero,
)
from verify_topology import cover, data
from flint import fmpq_mat


def direct_sum(*reps):
    return Rep([blockdiag(*(r.mats[j] for r in reps)) for j in range(len(reps[0].mats))])


def off_block_rep():
    doublets = transfer_pair(native_doublet())
    lines = transfer_pair(scalar_rep(0))
    return direct_sum(doublets, doublets.dual(), lines, lines.dual(), lines)


def fixed_meridian_jacobian(rep):
    rels, _, _ = cover(2)
    return vs(*(hs(rep.fox(r, 2), rep.fox(r, 3)) for r in rels))


def field_trace(a):
    assert a.nrows() % DEGREE == 0
    out = zero(DEGREE, DEGREE)
    for i in range(a.nrows()//DEGREE):
        out += submatrix(a, DEGREE*i, DEGREE*(i+1), DEGREE*i, DEGREE*(i+1))
    return out


def rational_trace(a):
    return sum(a[i, i] for i in range(a.nrows()))


def trace_comparators():
    e, rho, off = parent(0), native_doublet(), off_block_rep()
    active = direct_sum(rho, scalar_rep(0))
    words = [(1,), (2,), (3,), (-1,), (1, 2), (2, 3, -2), (1, -2, 3)]
    for word in words:
        full, three = e.word(word), active.word(word)
        expected = rational_trace(field_trace(full)*field_trace(full.inv())
                                  -field_trace(three)*field_trace(three.inv())-2*eye(DEGREE))
        assert rational_trace(off.word(word)) == expected
    return len(words)


def main():
    pair_rho, pair_line = transfer_pair(native_doublet()), transfer_pair(scalar_rep(0))
    for rep in (pair_rho, pair_line):
        a = indexed(rep, 2)
        assert a["V"] == a["dual"] == (0, 0, 0, 0, 0)
    off = off_block_rep()
    assert off.d == 56
    assert cohom(off, 2) == (0, 0, 0, 0, 0)
    assert (off.mats[0]-eye(off.d)).rank() == off.d
    jac = fixed_meridian_jacobian(off)
    assert jac.nrows() == jac.ncols() == 112 and jac.rank() == 112
    determinant = jac.det()
    assert determinant != 0
    p = fmpq_mat(data()["regular_C3"])
    mixed = Rep([kron(p**k, a) for a, k in zip(native_doublet().mats, data()["M2_to_C3"])])
    jmix = fixed_meridian_jacobian(mixed)
    raw_kernel = (jmix.ncols()-jmix.rank())//DEGREE
    meridian_fixed = (mixed.d-(mixed.mats[0]-eye(mixed.d)).rank())//DEGREE
    global_fixed = cohom(mixed, 2)[0]
    assert raw_kernel == 2 and meridian_fixed-global_fixed == 1
    print(json.dumps({
        "off_block_rank_over_K": off.d//DEGREE,
        "paired_rho_data": indexed(pair_rho, 2), "paired_character_data": indexed(pair_line, 2),
        "off_block_fixed_meridian_jacobian_Q_shape": [112, 112],
        "off_block_fixed_meridian_jacobian_Q_rank": jac.rank(),
        "rational_determinant": str(determinant),
        "trace_comparator_words": trace_comparators(),
        "mixed_raw_kernel_over_K": raw_kernel,
        "mixed_residual_gauge_over_K": meridian_fixed-global_fixed,
        "mixed_meridian_relative_H1": raw_kernel-meridian_fixed+global_fixed,
        "scope": "Local fixed-meridian 3+1+1 splitting; not all relative components or physical domains",
    }, indent=2))
    print("PASS: off-block Jacobian invertible while the smaller-block mixed direction remains live")


if __name__ == "__main__":
    main()
