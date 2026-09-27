"""Exact all-parameter E5 interior-cohomology decision in two literal families."""
import json
from functools import lru_cache
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "monomial_exceptional_locus_2026_09_27"))
import verify_exceptional as ex
from verify_exceptional import (
    companion, evaluate, factor_metadata, identity, matrix, modules,
    selected_minor, specialization, t, word,
)
from verify_relative_capacity import relative_h1
from verify_global_seed import eye, pullback
from verify_topology import cover, data
from flint import fmpq_mat
import sympy as sp


def inputs():
    return json.loads((HERE / "INPUTS.json").read_text())


def pullback_monomials(gens):
    return [word(w, gens) for w in data()["M6_generators_in_M2"]]


def dual_monomials(gens):
    return [(p, tuple(-x for x in v), s) for p, v, s in gens]


def symbolic_complex(gens):
    rels, mu, lam = cover(6)
    assert len(gens) == 7 and all(word(r, gens) == identity(5) for r in rels)
    assert word(mu, gens) == identity(5)
    longitude = matrix(word(lam, gens))
    assert all(not x.has(t) for x in longitude)
    assert 5-evaluate(longitude-sp.eye(5), 2).rank() == 3
    d0 = sp.Matrix.vstack(*(matrix(g)-sp.eye(5) for g in gens))
    d1 = sp.Matrix.vstack(*(sp.Matrix.hstack(*(ex.fox(r, g, gens) for g in range(1, 8))) for r in rels))
    restriction = sp.Matrix.vstack(*(sp.Matrix.hstack(*(ex.fox(w, g, gens) for g in range(1, 8)))
                                    for w in (mu, lam)))
    boundary = sp.Matrix.vstack(sp.zeros(5), longitude-sp.eye(5))
    assert all(sp.expand(x) == 0 for x in d1*d0)
    assert all(sp.expand(x) == 0 for x in restriction*d0-boundary)
    cone0 = sp.Matrix.vstack(d0, sp.eye(5))
    cone1 = sp.Matrix.vstack(sp.Matrix.hstack(d1, sp.zeros(d1.rows, 5)),
                            sp.Matrix.hstack(restriction, -boundary))
    assert cone1.shape == (40, 40)
    assert all(sp.expand(x) == 0 for x in cone1*cone0)
    return d0, cone1


@lru_cache(None)
def certificate(number):
    inp = inputs()
    mods = modules(ex.inputs()["seeds"][number])
    up = pullback_monomials(mods["E"])
    dual = dual_monomials(up)
    numeric = pullback(specialization(mods["E"], fmpq_mat([[inp["generic_control"]]])))
    assert specialization(up, fmpq_mat([[2]])).mats == numeric.mats
    assert specialization(dual, fmpq_mat([[2]])).mats == numeric.dual().mats
    result = {"seed": number, "coefficients": {}, "candidate_factors": []}
    candidates = set()
    for name, gens in (("E", up), ("dual", dual)):
        d0, cone = symbolic_complex(gens)
        records = {}
        for label, a in (("global_d0", d0), ("relative_cone", cone)):
            record, _ = selected_minor(a, inp["generic_control"])
            assert record["rank"] == inp["expected_control_ranks"][label]
            records[label] = record
            for factor in record["factors"]:
                coeff = tuple(factor["coefficients"])
                if coeff != ("1", "0"):
                    candidates.add(coeff)
        # The theorem in PROOF.md, not pointwise extrapolation.
        bound = 35-records["relative_cone"]["rank"]-inp["known_boundary_dimension"]
        assert bound == 0 and records["global_d0"]["rank"] == 5
        records["interior_upper_bound_away_from_minor_roots"] = bound
        result["coefficients"][name] = records
    result["candidate_factors"] = [list(c) for c in sorted(candidates, key=lambda c: (len(c), c))]
    return result


@lru_cache(None)
def candidate_point(number, coefficients):
    value = companion(coefficients)
    degree = value.nrows()
    mods = modules(ex.inputs()["seeds"][number])
    rep = pullback(specialization(mods["E"], value))
    indexed, _ = ex.indexed(rep, 6, degree)
    rel = relative_h1(rep, 6, degree)
    rel_dual = relative_h1(rep.dual(), 6, degree)
    assert indexed["I"] == rel["interior"]-rel_dual["interior"]
    return {"factor": factor_metadata(coefficients), "indexed": indexed,
            "E_relative": rel, "dual_relative": rel_dual}


def main():
    complete, observed_indices = True, []
    for number in range(len(ex.inputs()["seeds"])):
        cert = certificate(number)
        print("CERTIFICATE", number, json.dumps(cert), flush=True)
        for coefficients in cert["candidate_factors"]:
            if len(coefficients)-1 > inputs()["max_factor_degree"]:
                complete = False
                print("UNANALYSED", number, json.dumps(factor_metadata(coefficients)), flush=True)
                continue
            point = candidate_point(number, tuple(coefficients))
            observed_indices.append(point["indexed"]["I"])
            print("ROOT", number, json.dumps(point), flush=True)
    print("SUMMARY", json.dumps({
        "all_nonzero_complex_parameters_covered": complete,
        "generic_open_set_interior_dimensions": [0, 0],
        "exceptional_indices": observed_indices,
        "zero_index_entire_family": complete and all(x == 0 for x in observed_indices),
        "physical_chirality_derived": False,
    }), flush=True)
    print("PASS: declared-family minor and exact-specialization audit; no wider no-go")


if __name__ == "__main__":
    main()
