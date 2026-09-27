"""All common flat lines: exact marked character reduction and Laurent cones."""
from collections import deque, Counter
from functools import lru_cache
from itertools import product, combinations
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "monomial_matter_locus_2026_09_27"))
import verify_matter_locus as ml
from verify_exceptional import (
    companion, factor_metadata, modules, selected_minor, specialization,
)
from verify_relative_capacity import relative_h1
from verify_topology import cover, data
from flint import fmpq_mat
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form


def inputs():
    return json.loads((HERE / "INPUTS.json").read_text())


def exponent_vector(word, ng):
    return tuple(word.count(j)-word.count(-j) for j in range(1, ng+1))


def character_value(word, weights, modulus):
    return sum((1 if x > 0 else -1)*weights[abs(x)-1] for x in word) % modulus


def finite_dual(a, modulus):
    """All x mod 1 with A x integral, from the inverse relation matrix."""
    inverse = a.inv()
    generators = []
    for column in range(a.cols):
        values = [modulus*inverse[row, column] for row in range(a.rows)]
        assert all(x.q == 1 for x in values)
        generators.append(tuple(int(x) % modulus for x in values))
    origin = (0,)*a.cols
    queue, found = deque([origin]), {origin}
    while queue:
        x = queue.popleft()
        for g in generators:
            y = tuple((xi+gi) % modulus for xi, gi in zip(x, g))
            if y not in found:
                found.add(y)
                queue.append(y)
    assert len(found) == abs(int(a.det()))
    assert all(all(v % modulus == 0 for v in a*sp.Matrix(x)) for x in found)
    return sorted(found), generators


@lru_cache(None)
def character_reduction():
    rels, mu, lam = cover(6)
    assert mu == (1,) and exponent_vector(lam, 7) == (0,)*7
    full = sp.Matrix([exponent_vector(r, 7) for r in rels])
    a = full[:, 1:]
    snf = smith_normal_form(a, domain=sp.ZZ)
    factors = [abs(int(snf[i, i])) for i in range(6)]
    assert factors == [1, 1, 1, 1, 8, 40]
    modulus = inputs()["torsion_modulus"]
    chars, generators = finite_dual(a, modulus)
    fourth = sorted({tuple(-4*v % modulus for v in x) for x in chars})
    quadratic = sorted(x for x in product(range(2), repeat=6)
                       if all(v % 2 == 0 for v in a*sp.Matrix(x)))
    fifth = sorted(x for x in product(range(5), repeat=6)
                   if all(v % 5 == 0 for v in a*sp.Matrix(x)))
    chi = tuple(character_value(w, inputs()["M2_chi5_exponents"], 5)
                for w in data()["M6_generators_in_M2"])
    assert chi[0] == 0 and len(quadratic) == 4 and len(fifth) == 5
    assert fifth == sorted({tuple(j*v % 5 for v in chi[1:]) for j in range(5)})
    decomposition = {}
    for eta in quadratic:
        for j in range(5):
            x = tuple((20*e+8*j*c) % modulus for e, c in zip(eta, chi[1:]))
            assert x not in decomposition
            decomposition[x] = {"quadratic": [0, *eta], "chi_power": j}
    assert fourth == sorted(decomposition) and len(fourth) == 20
    for x in chars:
        weights = (0, *x)
        assert all(character_value(r, weights, modulus) == 0 for r in rels)
        assert character_value(mu, weights, modulus) == character_value(lam, weights, modulus) == 0
    return {"relation_matrix_after_mu": a.tolist(), "smith_factors": factors,
            "longitude_exponents": exponent_vector(lam, 7),
            "character_generators_mod40": generators, "all_characters_mod40": chars,
            "character_count": len(chars), "fourth_power_count": len(fourth),
            "quadratic_characters": [[0, *e] for e in quadratic],
            "fifth_characters": fifth, "restricted_chi": chi,
            "fourth_power_decomposition": [{"character": x, **decomposition[x]} for x in fourth]}


def parent_center():
    center_weights = [(2, 1), (-2, -1), (1, -2), (-1, 2)]
    kernel = [(a, b) for a, b in product(range(5), repeat=2)
              if all((a*x+b*y) % 5 == 0 for x, y in center_weights)]
    assert kernel == [(a, -2*a % 5) for a in range(5)]
    h = inputs()["gauge_hypercharge_weights"]
    assert sum(h) == 0 and Counter(h[i]+h[j] for i, j in combinations(range(5), 2)) == {-4: 3, 1: 6, 6: 1}
    assert Counter(-x for x in h) == {2: 3, -3: 2}
    degrees = {"Q": 1, "u": 1, "e": 1, "d": 2, "lepton": 2}
    hidden = [(r, s) for r, s in product(range(5), repeat=2)
              if all((r*q+s*degrees[name]) % 5 == 0
                     for name, q in inputs()["sector_charges"].items())]
    assert hidden == [(r, -r % 5) for r in range(5)]
    return {"parent_center_kernel": kernel, "line_structure_kernel": hidden,
            "global_lift_scope": True, "nonliftable_bundles_classified": False}


def absorption(number):
    specification = inputs()["absorption"][number]
    k, s = specification["k"], specification["diagonal_exponents"]
    records = []
    gens = modules(ml.ex.inputs()["seeds"][number])["E"]
    for (p, v, _), c in zip(gens, inputs()["M2_chi5_exponents"]):
        residues = [(v[p[i]]-k*c-s[p[i]]+s[i]) % 5 for i in range(5)]
        assert residues == [0]*5
        records.append(residues)
    assert pow(k, -1, 5) in range(1, 5)
    return {"seed": number, **specification, "entrywise_residuals_mod5": records}


def twisted_gens(number, eta):
    gens = ml.pullback_monomials(modules(ml.ex.inputs()["seeds"][number])["E"])
    assert len(eta) == len(gens)
    return [(p, v, tuple((-1)**e*z for z in s)) for (p, v, s), e in zip(gens, eta)]


@lru_cache(None)
def certificate(number, eta):
    gens = twisted_gens(number, eta)
    dual = ml.dual_monomials(gens)
    control = inputs()["generic_control"]
    actual = specialization(gens, fmpq_mat([[control]]))
    assert specialization(dual, fmpq_mat([[control]])).mats == actual.dual().mats
    candidates, result = set(), {"seed": number, "eta": eta, "coefficients": {}}
    for name, coefficient in (("E_eta", gens), ("dual", dual)):
        d0, cone = ml.symbolic_complex(coefficient)
        records = {}
        for label, a in (("global_d0", d0), ("relative_cone", cone)):
            record, _ = selected_minor(a, control)
            records[label] = record
            for factor in record["factors"]:
                coeff = tuple(factor["coefficients"])
                if coeff != ("1", "0"):
                    candidates.add(coeff)
        bound = 35-records["relative_cone"]["rank"]-3+5-records["global_d0"]["rank"]
        assert bound >= 0
        records["interior_upper_bound_off_candidate_roots"] = bound
        result["coefficients"][name] = records
    result["candidate_factors"] = sorted(candidates, key=lambda c: (len(c), c))
    return result


@lru_cache(None)
def candidate_point(number, eta, coefficients):
    value = companion(coefficients)
    degree = value.nrows()
    rep = specialization(twisted_gens(number, eta), value)
    indexed, _ = ml.ex.indexed(rep, 6, degree)
    a, b = relative_h1(rep, 6, degree), relative_h1(rep.dual(), 6, degree)
    assert indexed["I"] == a["interior"]-b["interior"]
    return {"seed": number, "eta": eta, "factor": factor_metadata(coefficients),
            "indexed": indexed, "E_relative": a, "dual_relative": b}


def run():
    reduction = character_reduction()
    print("CHARACTERS", json.dumps(reduction, default=int), flush=True)
    print("PARENT", json.dumps(parent_center()), flush=True)
    complete, index_zero, target_excluded, observed = True, True, True, []
    for number in range(2):
        print("ABSORPTION", json.dumps(absorption(number)), flush=True)
        for e in reduction["quadratic_characters"]:
            eta = tuple(e)
            cert = certificate(number, eta)
            print("CERTIFICATE", json.dumps(cert), flush=True)
            bounds = [c["interior_upper_bound_off_candidate_roots"] for c in cert["coefficients"].values()]
            index_zero &= max(bounds) == 0
            target_excluded &= max(bounds) < 3
            for coefficients in cert["candidate_factors"]:
                if len(coefficients)-1 > inputs()["max_factor_degree"]:
                    complete = False
                    print("UNANALYSED", json.dumps({"seed": number, "eta": eta,
                          "factor": factor_metadata(coefficients)}), flush=True)
                    continue
                point = candidate_point(number, eta, tuple(coefficients))
                observed.append(point["indexed"]["I"])
                print("ROOT", json.dumps(point), flush=True)
    summary = {"all_nonzero_complex_parameters_covered": complete,
               "all_meridian_trivial_lines_reduced": reduction["character_count"],
               "required_u_index_zero_for_all_reduced_lines": complete and index_zero and all(x == 0 for x in observed),
               "joint_three_generation_ordinary_index_target_excluded": complete and target_excluded and all(abs(x) != 3 for x in observed),
               "exceptional_indices": observed, "physical_chirality_derived": False,
               "all_SL5_backgrounds_classified": False}
    print("SUMMARY", json.dumps(summary), flush=True)
    print("PASS: stated identities and exact certificates; outcome is the summary, not this marker")
    return summary


if __name__ == "__main__":
    run()
