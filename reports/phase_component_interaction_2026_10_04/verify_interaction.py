"""Exact logarithmic jets and ordinary continuation; no numerical differences."""
from functools import lru_cache
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "phase_component_matter_2026_10_04"))
import verify_matter as matter
sys.path.insert(0, str(HERE.parent / "monomial_harmonic_background_2026_09_27"))
import verify_harmonic_background as harmonic
from verify_parent_projection import projection_control
from verify_global_seed import Rep, eye, hs, kron, null_columns, submatrix, vs, zero
from flint import fmpq_mat


def inputs():
    return json.loads((HERE / "INPUTS.json").read_text())


def generator_jet(g, t):
    a = matter.matrix(g, t)
    _, v, _, _ = g
    diagonal = zero(a.nrows(), a.nrows())
    for i, exponent in enumerate(v):
        diagonal[2*i, 2*i] = diagonal[2*i+1, 2*i+1] = exponent
    return a, diagonal*a


def pair_product(a, b):
    return a[0]*b[0], a[1]*b[0]+a[0]*b[1]


def pair_inverse(a):
    inverse = a[0].inv()
    return inverse, -inverse*a[1]*inverse


def fox_jet(generators, w, g):
    d = generators[0][0].nrows()
    prefix, out = (eye(d), zero(d, d)), (zero(d, d), zero(d, d))
    for x in w:
        if x > 0:
            if x == g:
                out = out[0]+prefix[0], out[1]+prefix[1]
            prefix = pair_product(prefix, generators[x-1])
        else:
            prefix = pair_product(prefix, pair_inverse(generators[-x-1]))
            if -x == g:
                out = out[0]-prefix[0], out[1]-prefix[1]
    return out


def lift(a):
    return vs(hs(a[0], a[1]), hs(zero(a[0].nrows(), a[0].ncols()), a[0]))


def rank_increment(base, image):
    return hs(base, image).rank()-base.rank()


def sparse(column):
    return {str(i): str(column[i, 0]) for i in range(column.nrows()) if column[i, 0]}


def first_witness(j, dotj, cycles):
    left = null_columns(j.transpose())
    pairing = left.transpose()*dotj*cycles
    assert pairing.rank() == rank_increment(j, dotj*cycles)
    for i in range(pairing.nrows()):
        for k in range(pairing.ncols()):
            if pairing[i, k]:
                x = submatrix(cycles, 0, cycles.nrows(), k, k+1)
                ell = submatrix(left, 0, left.nrows(), i, i+1)
                assert j*x == zero(j.nrows(), 1)
                assert ell.transpose()*j == zero(1, j.ncols())
                assert (ell.transpose()*dotj*x)[0, 0] == pairing[i, k]
                return {"cycle_column": k, "cokernel_column": i,
                        "exact_pairing_not_a_physical_coupling": str(pairing[i, k]),
                        "cycle_sparse_over_Q": sparse(x), "cokernel_sparse_over_Q": sparse(ell)}
    return None


@lru_cache(None)
def continuation(seed, component, t, name="E", dual=False):
    gens = matter.coefficient_data(seed, component, name)
    if dual:
        gens = matter.actual_dual_data(gens)
    jets = [generator_jet(g, t) for g in gens]
    rep, lifted = Rep([a for a, _ in jets]), Rep([lift(a) for a in jets])
    d, ng = rep.d, len(jets)
    rels, mu, lam = matter.ex.cover(6)
    assert len(rels) == 6 and ng == 7
    for a in jets:
        inv = pair_inverse(a)
        assert pair_product(a, inv) == (eye(d), zero(d, d))
        assert lift(inv) == lift(a).inv()
    assert all(lifted.word(r) == eye(2*d) for r in rels)
    b, dotb = vs(*(a-eye(d) for a, _ in jets)), vs(*(da for _, da in jets))
    matrices = []
    derivatives = []
    for w in (*rels, mu, lam):
        blocks = [fox_jet(jets, w, g) for g in range(1, ng+1)]
        for g, (a, da) in enumerate(blocks, 1):
            assert a == rep.fox(w, g)
            assert lifted.fox(w, g) == lift((a, da))
        matrices.append(hs(*(a for a, _ in blocks)))
        derivatives.append(hs(*(da for _, da in blocks)))
    j, dotj = vs(*matrices[:6]), vs(*derivatives[:6])
    r, dotr = vs(*matrices[6:]), vs(*derivatives[6:])
    boundary = vs(rep.word(mu)-eye(d), rep.word(lam)-eye(d))
    assert all(lifted.word(w) == lift((rep.word(w), zero(d, d))) for w in (mu, lam))
    assert j*b == zero(j.nrows(), d) and dotj*b+j*dotb == zero(j.nrows(), d)
    assert r*b == boundary and dotr*b+r*dotb == zero(2*d, d)
    stacked, dotstacked = vs(j, r), vs(dotj, dotr)
    cycles = null_columns(stacked)
    boundary_invariants = null_columns(boundary)
    boundary_exact = b*boundary_invariants
    assert stacked*boundary_exact == zero(stacked.nrows(), boundary_exact.ncols())
    assert rank_increment(j, dotj*boundary_exact) == 0
    assert rank_increment(stacked, dotstacked*boundary_exact) == 0
    row = matter.point(seed, component, t)["coefficients"][name]
    ordinary = row["ordinary"]["dual" if dual else "V"]
    a0, a1, t0, _, r1 = ordinary
    n = a1-r1
    assert cycles.ncols()-boundary_exact.rank() == 2*n
    assert boundary_exact.rank() == 2*(t0-a0)
    ordinary_rank = rank_increment(j, dotj*cycles)
    fixed_rank = rank_increment(stacked, dotstacked*cycles)
    assert ordinary_rank % 2 == fixed_rank % 2 == 0
    assert 0 <= ordinary_rank <= fixed_rank <= 2*n
    witness = first_witness(j, dotj, cycles)
    assert (witness is None) == (ordinary_rank == 0)
    # Differentiate the literal actual dual against transpose-inverse, including phase.
    if name == "E":
        original = [generator_jet(g, t) for g in matter.coefficient_data(seed, component, name)]
        counterpart = [generator_jet(g, t) for g in matter.actual_dual_data(
            matter.coefficient_data(seed, component, name))]
        pairing = kron(eye(5), matter.TRACE)
        for a, c in zip(original, counterpart):
            inverse = pair_inverse(a)
            assert inverse[0].transpose() == pairing*c[0]*pairing.inv()
            assert inverse[1].transpose() == pairing*c[1]*pairing.inv()
    return {"seed": seed, "component": component, "t": t, "coefficient": name,
            "actual_dual": dual, "interior_input_dimension": n,
            "strict_cycles_dimension": cycles.ncols()//2,
            "boundary_connecting_dimension_removed": boundary_exact.rank()//2,
            "ordinary_H2_dimension": (j.nrows()-j.rank())//2,
            "ordinary_obstruction_rank": ordinary_rank//2,
            "fixed_peripheral_obstruction_rank": fixed_rank//2,
            "ordinary_witness": witness,
            "dual_number_fox_check": True, "boundary_connecting_obstruction_zero": True,
            "normalized_coupling_computed": False}


def complex_commutant(rep):
    d = rep.d
    field = kron(eye(d//2), matter.Z)
    equations = []
    for a in (*rep.mats, field):
        equation = zero(d*d, d*d)
        for i in range(d):
            for j in range(d):
                for k in range(d):
                    equation[d*i+j, d*k+j] += a[i, k]
                    equation[d*i+j, d*i+k] -= a[k, j]
        equations.append(equation)
    system = vs(*equations)
    for a in (eye(d), field):
        vector = fmpq_mat([[a[i, j]] for i in range(d) for j in range(d)])
        assert system*vector == zero(system.nrows(), 1)
    dimension = d*d-system.rank()
    assert dimension >= 2 and dimension % 2 == 0
    return dimension//2


@lru_cache(None)
def harmonic_transfer(seed, component):
    rep = matter.representation(seed, component, -1, "E")
    gens = matter.coefficient_data(seed, component, "E")
    diagonals = []
    cocycle = []
    for p, v, _, _ in gens:
        a = fmpq_mat([[int(i == p[k])-int(i == p[4]) for k in range(4)] for i in range(4)])
        diagonals.append(a)
        cocycle.extend(v[:4])
    for transport, diagonal in zip(rep.mats, diagonals):
        for k in range(4):
            h = zero(10, 10)
            h[2*k, 2*k] = h[2*k+1, 2*k+1] = 1
            h[8, 8] = h[9, 9] = -1
            expected = zero(10, 10)
            x = [diagonal[i, k] for i in range(4)]
            x += [-sum(x)]
            for i, value in enumerate(x):
                expected[2*i, 2*i] = expected[2*i+1, 2*i+1] = value
            assert transport*h*transport.inv() == expected
    diagonal_rep = Rep(diagonals)
    gram = fmpq_mat([[1+int(i == j) for j in range(4)] for i in range(4)])
    assert all(a.transpose()*gram*a == gram for a in diagonals)
    c = fmpq_mat([[x] for x in cocycle])
    b, j, r = harmonic.differential_matrices(diagonal_rep, 6)
    assert j*c == zero(j.nrows(), 1) and r*c == zero(r.nrows(), 1)
    assert b.rank() == 4 and hs(b, c).rank() == 5
    ordinary, _ = matter.ex.cohom(diagonal_rep, 6, 1)
    assert ordinary[0] == 0 and ordinary[1]-ordinary[4] == 1
    inherited = harmonic.one_seed(seed)
    assert inherited["covers"]["6"]["cocycle"] == str(c)
    assert inherited["covers"]["6"]["ordinary"] == ordinary
    count = complex_commutant(rep)
    charged = matter.point(seed, component, -1)["coefficients"]
    assert all(a["ordinary"]["V"][0] == a["ordinary"]["dual"][0] == 0
               for a in charged.values())
    return {"seed": seed, "component": component,
            "actual_diagonal_bundle_unchanged": True,
            "nonzero_interior_exponent_class": True, "finite_unitary_center": True,
            "complex_EndE_invariant_dimension": count,
            "structure_adjoint_H0": count-1,
            "full_parent_compact_gauge_Lie_dimension": 24+count-1,
            "complete_analytic_transfer": "authored conditional argument in PROOF.md",
            "isolated_EFT_claimed": False}


def instrument_controls():
    empty = zero(0, 1)
    z = zero(1, 1)
    one = eye(1)
    assert rank_increment(z, one) == 1
    assert rank_increment(empty, zero(0, 1)) == 0
    assert rank_increment(vs(empty, z), vs(zero(0, 1), one)) == 1
    assert rank_increment(z, z) == 0  # d(u)=u^2 jumps but its derivative at 0 is zero.
    a = (fmpq_mat([[2, 0], [0, 3]]), eye(2))
    correct = pair_inverse(a)
    assert pair_product(a, correct) == (eye(2), zero(2, 2))
    wrong = correct[0], -correct[1]
    assert pair_product(a, wrong)[1] != zero(2, 2)
    assert rank_increment(eye(2), eye(2)) == 0
    return {"nonzero_ordinary_obstruction_detected": True,
            "relative_only_is_not_bulk": True,
            "quadratic_jump_does_not_imply_first_derivative": True,
            "wrong_inverse_derivative_rejected": True,
            "surjective_differential_has_zero_obstruction": True}


def comparators():
    rows = []
    for seed in inputs()["seeds"]:
        for component in inputs()["components"]:
            for t, name in ((1, "E"), (-1, "wedge2E")):
                row = continuation(seed, component, t, name)
                assert row["interior_input_dimension"] == row["ordinary_obstruction_rank"] == 0
                rows.append(row)
        for dual in (False, True):
            row = continuation(seed, 0, 1, "E", dual)
            assert row["ordinary_obstruction_rank"] == 0, "old zero-cubic comparator disagrees"
            rows.append(row)
    return rows


def run():
    print("INSTRUMENT", json.dumps(instrument_controls()), flush=True)
    print("PARENT_PROJECTION", json.dumps({k: int(v) for k, v in projection_control().items()}), flush=True)
    for seed in inputs()["seeds"]:
        for component in inputs()["components"]:
            print("TRANSFER", json.dumps(harmonic_transfer(seed, component)), flush=True)
            for dual in (False, True):
                print("OBSTRUCTION", json.dumps(continuation(seed, component, -1, "E", dual)), flush=True)
    for row in comparators():
        print("COMPARATOR", json.dumps(row), flush=True)
    print("PASS: exact first order continuation and transfer controls; global proof remains authored")


if __name__ == "__main__":
    run()
