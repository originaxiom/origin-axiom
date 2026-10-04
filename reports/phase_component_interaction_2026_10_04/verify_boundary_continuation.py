"""Literal ordinary lift, unavoidable torus class and actual charged cusp controls."""
from functools import lru_cache
import json

import verify_interaction as original
from verify_global_seed import Rep, blockdiag, eye, hs, kron, null_columns, submatrix, vs, zero


def linear_solve(a, rhs):
    assert hs(a, rhs).rank() == a.rank()
    reduced, rank = hs(a, rhs).rref()
    result = zero(a.ncols(), rhs.ncols())
    for i in range(rank):
        pivot = next(j for j in range(a.ncols()) if reduced[i, j])
        for k in range(rhs.ncols()):
            result[pivot, k] = reduced[i, a.ncols()+k]
    assert a*result == rhs
    return result


def differentials(seed, component, dual):
    gens = original.matter.coefficient_data(seed, component, "E")
    if dual:
        gens = original.matter.actual_dual_data(gens)
    jets = [original.generator_jet(g, -1) for g in gens]
    rep = Rep([a for a, _ in jets])
    rels, mu, lam = original.matter.ex.cover(6)
    blocks = [[original.fox_jet(jets, w, g) for g in range(1, 8)] for w in (*rels, mu, lam)]
    j = vs(*(hs(*(a for a, _ in row)) for row in blocks[:6]))
    dotj = vs(*(hs(*(da for _, da in row)) for row in blocks[:6]))
    r = vs(*(hs(*(a for a, _ in row)) for row in blocks[6:]))
    dotr = vs(*(hs(*(da for _, da in row)) for row in blocks[6:]))
    b = vs(*(a-eye(rep.d) for a in rep.mats))
    return rep, (j, dotj, r, dotr, b), (mu, lam)


def torus_projector(rep, mu, lam):
    d = rep.d
    assert rep.word(mu) == eye(d)
    longitude = rep.word(lam)
    order = next(k for k in range(1, 61) if longitude**k == eye(d))
    projector = sum((longitude**k for k in range(order)), zero(d, d))/order
    gram = kron(eye(d//2), original.matter.GRAM)
    assert longitude.transpose()*gram*longitude == gram
    assert projector*projector == projector
    assert projector.transpose()*gram == gram*projector
    return blockdiag(projector, projector), order


@lru_cache(None)
def escape(seed, component, dual):
    rep, (j, dotj, r, dotr, b), (mu, lam) = differentials(seed, component, dual)
    base = original.continuation(seed, component, -1, "E", dual)
    assert base["ordinary_obstruction_rank"] == 0 and base["fixed_peripheral_obstruction_rank"] == 1
    stacked, dotstacked = vs(j, r), vs(dotj, dotr)
    cycles = null_columns(stacked)
    selected = None
    for k in range(cycles.ncols()):
        x = submatrix(cycles, 0, cycles.nrows(), k, k+1)
        if original.rank_increment(stacked, dotstacked*x):
            selected = k, x
            break
    assert selected is not None
    k, x = selected
    field = kron(eye(7*5), original.matter.Z)
    input_line = hs(x, field*x)
    assert stacked*input_line == zero(stacked.nrows(), 2)
    assert input_line.rank() == 2
    boundary0 = vs(rep.word(mu)-eye(rep.d), rep.word(lam)-eye(rep.d))
    boundary1 = hs(-(rep.word(lam)-eye(rep.d)), rep.word(mu)-eye(rep.d))
    boundary_exact = b*null_columns(boundary0)
    assert original.rank_increment(boundary_exact, input_line) == 2
    lift = linear_solve(j, -dotj*input_line)
    periods = r*lift+dotr*input_line
    assert boundary1*periods == zero(rep.d, 2)
    closed_corrections = null_columns(j)
    mutable_periods = hs(r*closed_corrections, boundary0)
    assert original.rank_increment(mutable_periods, periods) == 2
    projector, order = torus_projector(rep, mu, lam)
    harmonic_periods = projector*periods
    assert projector*boundary0 == zero(2*rep.d, rep.d)
    assert original.rank_increment(boundary0, periods-harmonic_periods) == 0
    assert original.rank_increment(projector*mutable_periods, harmonic_periods) == 2
    assert (projector*mutable_periods).rank() == 2*base["interior_input_dimension"]+4
    # Both corrections solve the same ordinary equation; their difference is closed.
    alternative = lift+submatrix(closed_corrections, 0, closed_corrections.nrows(), 0, 2)
    assert j*alternative == -dotj*input_line
    assert original.rank_increment(mutable_periods, r*alternative+dotr*input_line-periods) == 0
    return {"seed": seed, "component": component, "actual_dual": dual,
            "ordinary_lift_exists": True, "torus_period_is_closed": True,
            "unavoidable_torus_quotient_complex_dimension": 1,
            "longitude_order": order,
            "cycle_sparse_over_Q": original.sparse(x),
            "ordinary_correction_sparse_over_Q": original.sparse(submatrix(lift, 0, lift.nrows(), 0, 1)),
            "harmonic_period_sparse_over_Q": original.sparse(submatrix(harmonic_periods, 0, harmonic_periods.nrows(), 0, 1)),
            "changing_ordinary_lift_cannot_remove_quotient": True,
            "boundary_gauge_cannot_remove_quotient": True,
            "basis_numbers_are_not_flux_or_mass_predictions": True}


@lru_cache(None)
def charged_cusp(seed, component, dual):
    rep, _, (mu, lam) = differentials(seed, component, dual)
    boundary = vs(rep.word(mu)-eye(rep.d), rep.word(lam)-eye(rep.d))
    invariants = null_columns(boundary)
    assert invariants.ncols() == 6
    v = submatrix(invariants, 0, rep.d, 0, 1)
    assert rep.word(mu)*v == rep.word(lam)*v == v
    gram = kron(eye(5), original.matter.GRAM)
    norm = (v.transpose()*gram*v)[0, 0]
    assert norm > 0
    assert all(a.transpose()*gram*a == gram for a in rep.mats)
    global_d0 = vs(*(a-eye(rep.d) for a in rep.mats))
    assert global_d0.rank() == rep.d
    bump = original.harmonic.cusp_controls()
    assert bump["rayleigh_constant"] == 12 and bump["laplacian_norm_constant"] == 504
    return {"seed": seed, "component": component, "actual_dual": dual,
            "global_H0": 0, "charged_boundary_H0": 3,
            "parallel_cusp_vector_sparse_over_Q": original.sparse(v),
            "positive_reference_norm_squared_not_a_4d_kinetic_norm": str(norm),
            "one_form_escaping_Rayleigh_constant": int(bump["rayleigh_constant"]),
            "squared_Laplacian_residual_constant": int(bump["laplacian_norm_constant"]),
            "zero_charged_essential_threshold": "conditional authored Weyl sequence in BOUNDARY_PROOF.md",
            "physical_end_law_changed": False}


def controls():
    a = original.matter.fmpq_mat([[1, 0], [0, 0]])
    rhs = original.matter.fmpq_mat([[3], [0]])
    assert linear_solve(a, rhs) == original.matter.fmpq_mat([[3], [0]])
    impossible = original.matter.fmpq_mat([[3], [1]])
    assert hs(a, impossible).rank() > a.rank()
    assert original.rank_increment(eye(2), eye(2)) == 0
    assert original.rank_increment(zero(2, 0), eye(2)) == 2
    return {"consistent_solver_checks_actual_residual": True,
            "inconsistent_equation_rejected": True,
            "removable_and_unavoidable_periods_distinguished": True}


def run():
    print("INSTRUMENT", json.dumps(controls()), flush=True)
    for seed in original.inputs()["seeds"]:
        for component in original.inputs()["components"]:
            for dual in (False, True):
                print("ESCAPE", json.dumps(escape(seed, component, dual)), flush=True)
                print("CHARGED_CUSP", json.dumps(charged_cusp(seed, component, dual)), flush=True)
    print("PASS: explicit ordinary lifts with unavoidable charged torus class; no physical mass inferred")


if __name__ == "__main__":
    run()
