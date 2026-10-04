"""Exact Laurent certificates and EACH cyclotomic-field root, not averaged roots."""
from functools import lru_cache
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "phase_component_matter_2026_10_04"))
import verify_matter as matter
sys.path.insert(0, str(HERE.parent / "common_hypercharge_gate_2026_09_27"))
import verify_common_line as old
from verify_global_seed import Rep, eye, kron, zero
from verify_relative_capacity import relative_h1
from flint import fmpq, fmpq_mat
import sympy as sp

t = matter.ex.t
OMEGA = (-1+sp.sqrt(3)*sp.I)/2
K = sp.QQ.algebraic_field(OMEGA)
Z = sp.Matrix([[0, -1], [1, -1]])


def inputs():
    return json.loads((HERE / "INPUTS.json").read_text())


def identity(n):
    return tuple(range(n)), (0,)*n, (0,)*n, (1,)*n


def multiply(a, b):
    p, v, phase, sign = a
    q, w, other, osign = b
    pi = matter.ex.invperm(p)
    return (tuple(p[q[i]] for i in range(len(p))),
            tuple(v[i]+w[pi[i]] for i in range(len(p))),
            tuple((phase[i]+other[pi[i]])%3 for i in range(len(p))),
            tuple(sign[i]*osign[pi[i]] for i in range(len(p))))


def inverse(a):
    p, v, phase, sign = a
    return (matter.ex.invperm(p), tuple(-v[p[i]] for i in range(len(p))),
            tuple(-phase[p[i]]%3 for i in range(len(p))), tuple(sign[p[i]] for i in range(len(p))))


def word(w, gens):
    result = identity(len(gens[0][0]))
    for x in w:
        result = multiply(result, gens[x-1] if x > 0 else inverse(gens[-x-1]))
    return result


def signed_data(seed, component, eta):
    gens = matter.coefficient_data(seed, component, "E")
    return [(p, v, a, tuple((-1)**e*x for x in s)) for (p,v,a,s), e in zip(gens, eta)]


def matrix(g):
    p, v, phase, sign = g
    result = sp.zeros(2*len(p))
    for j, i in enumerate(p):
        result[2*i:2*i+2, 2*j:2*j+2] = sign[i]*t**v[i]*(Z**phase[i])
    return result


def fox(w, which, gens):
    prefix = identity(len(gens[0][0]))
    result = sp.zeros(2*len(prefix[0]))
    for x in w:
        if x > 0:
            if x == which:
                result += matrix(prefix)
            prefix = multiply(prefix, gens[x-1])
        else:
            prefix = multiply(prefix, inverse(gens[-x-1]))
            if -x == which:
                result -= matrix(prefix)
    return result


@lru_cache(None)
def symbolic_complex(seed, component, eta, dual):
    gens = signed_data(seed, component, eta)
    if dual:
        gens = matter.actual_dual_data(gens)
    rels, mu, lam = matter.ex.cover(6)
    assert all(word(r, gens) == identity(5) for r in rels)
    assert word(mu, gens) == identity(5)
    longitude = matrix(word(lam, gens))
    assert not any(x.has(t) for x in longitude)
    assert 10-matter.ex.evaluate(longitude-sp.eye(10), 2).rank() == 6
    d0 = sp.Matrix.vstack(*(matrix(g)-sp.eye(10) for g in gens))
    d1 = sp.Matrix.vstack(*(sp.Matrix.hstack(*(fox(r, g, gens) for g in range(1, 8))) for r in rels))
    restriction = sp.Matrix.vstack(*(sp.Matrix.hstack(*(fox(w, g, gens) for g in range(1, 8))) for w in (mu, lam)))
    boundary = sp.Matrix.vstack(sp.zeros(10), longitude-sp.eye(10))
    assert all(sp.expand(x) == 0 for x in d1*d0)
    assert all(sp.expand(x) == 0 for x in restriction*d0-boundary)
    cone0 = sp.Matrix.vstack(d0, sp.eye(10))
    cone1 = sp.Matrix.vstack(sp.Matrix.hstack(d1, sp.zeros(d1.rows, 10)),
                             sp.Matrix.hstack(restriction, -boundary))
    assert cone1.shape == (80, 80)
    assert all(sp.expand(x) == 0 for x in cone1*cone0)
    numeric = Rep([matter.matrix(g, 2) for g in gens])
    assert all(matter.ex.evaluate(fox(w, g, gens), 2) == numeric.fox(w, g)
               for w in (*rels, mu, lam) for g in range(1, 8))
    return d0, cone1


def coords(expr):
    value = K.from_sympy(sp.sympify(expr))
    coefficients = value.to_sympy_list()
    assert len(coefficients) <= 2
    a = coefficients[-1] if coefficients else sp.Rational(0)
    b = coefficients[-2] if len(coefficients) == 2 else sp.Rational(0)
    assert K.from_sympy(a+b*OMEGA) == value
    return str(a), str(b)


def coord_matrix(ab):
    a, b = (fmpq(x) for x in ab)
    return fmpq_mat([[a, -b], [b, a-b]])


@lru_cache(None)
def split_factor(coefficients):
    polynomial = sp.Poly.from_list([sp.Rational(c) for c in coefficients], t, domain=sp.QQ)
    assert polynomial.is_irreducible and not polynomial.eval(0) == 0
    over_k = polynomial.set_domain(K)
    scalar, factors = over_k.factor_list()
    product = sp.Poly(scalar, t, domain=K)
    records = []
    for factor, multiplicity in factors:
        assert factor.is_irreducible
        monic = factor.monic()
        product *= factor**multiplicity
        records.append({"coefficients_ab": [coords(c) for c in monic.all_coeffs()],
                        "degree_over_K": monic.degree(), "multiplicity": multiplicity,
                        "polynomial": str(monic.as_expr()), "irreducible_over_K": True})
    assert product == over_k and sum(r["degree_over_K"]*r["multiplicity"] for r in records) == polynomial.degree()
    return records


@lru_cache(None)
def field_for_factor(coefficients_ab):
    assert coefficients_ab[0] == ("1", "0")
    k = len(coefficients_ab)-1
    polynomial = sp.Poly.from_list([sp.Rational(a)+sp.Rational(b)*OMEGA
                                   for a, b in coefficients_ab], t, domain=K)
    assert k >= 1 and polynomial.degree() == k and polynomial.is_irreducible
    companion = zero(2*k, 2*k)
    for i in range(k-1):
        companion[2*i+2, 2*i] = companion[2*i+3, 2*i+1] = 1
    for i in range(k):
        block = -coord_matrix(coefficients_ab[k-i])
        for r in range(2):
            for c in range(2):
                companion[2*i+r, 2*(k-1)+c] = block[r, c]
    omega = kron(eye(k), matter.Z)
    assert companion*omega == omega*companion
    assert omega**2+omega+eye(2*k) == zero(2*k, 2*k)
    value = zero(2*k, 2*k)
    for coefficient in coefficients_ab:
        value = value*companion+kron(eye(k), coord_matrix(coefficient))
    assert value == zero(2*k, 2*k) and companion.det() != 0
    basis = [companion**i*omega**j for i in range(k) for j in range(2)]
    trace = fmpq_mat([[sum((a*b)[i, i] for i in range(2*k)) for b in basis] for a in basis])
    assert trace.det() != 0
    assert companion.transpose()*trace == trace*companion
    assert omega.transpose()*trace == trace*omega
    return companion, omega, trace


def specialize(gens, value, omega):
    d = value.nrows()
    matrices = []
    for p, v, a, s in gens:
        matrix = zero(len(p)*d, len(p)*d)
        for j, i in enumerate(p):
            block = s[i]*(value**v[i])*(omega**a[i])
            for r in range(d):
                for c in range(d):
                    matrix[d*i+r, d*j+c] = block[r, c]
        matrices.append(matrix)
    return Rep(matrices)


@lru_cache(None)
def candidate_point(seed, component, eta, coefficients_ab):
    value, omega, trace = field_for_factor(coefficients_ab)
    degree = value.nrows()
    gens = signed_data(seed, component, eta)
    rep = specialize(gens, value, omega)
    literal_dual = specialize(matter.actual_dual_data(gens), value, omega)
    pairing = kron(eye(5), trace)
    assert rep.dual().mats == [pairing*a*pairing.inv() for a in literal_dual.mats]
    indexed, _ = matter.ex.indexed(rep, 6, degree)
    actual_dual, _ = matter.ex.cohom(literal_dual, 6, degree)
    assert actual_dual == indexed["dual"]
    relative = relative_h1(rep, 6, degree)
    relative_dual = relative_h1(literal_dual, 6, degree)
    assert indexed["I"] == relative["interior"]-relative_dual["interior"]
    return {"seed": seed, "component": component, "eta": eta,
            "coefficients_ab": coefficients_ab, "Q_field_degree": degree,
            "indexed": indexed, "n": relative["interior"], "n_dual": relative_dual["interior"],
            "relative": relative, "relative_dual": relative_dual,
            "each_irreducible_K_factor_not_an_average": True}


@lru_cache(None)
def certificate(seed, component, eta):
    candidates = set()
    out = {"seed": seed, "component": component, "eta": eta, "coefficients": {}}
    for name, dual in (("V", False), ("actual_dual", True)):
        d0, cone = symbolic_complex(seed, component, eta, dual)
        records = {}
        for label, matrix in (("global_d0", d0), ("relative_cone", cone)):
            print("MINOR_START", json.dumps({"seed": seed, "component": component, "eta": eta,
                                             "coefficient": name, "matrix": label}), flush=True)
            record, _ = matter.ex.selected_minor(matrix, inputs()["generic_control"])
            records[label] = record
            for factor in record["factors"]:
                coeff = tuple(factor["coefficients"])
                if coeff != ("1", "0"):
                    candidates.add(coeff)
        numerator = 74-records["relative_cone"]["rank"]-records["global_d0"]["rank"]
        assert numerator >= 0 and numerator % 2 == 0
        records["interior_upper_bound_off_candidate_roots"] = numerator//2
        out["coefficients"][name] = records
    out["candidate_factors_over_Q"] = sorted(candidates, key=lambda c: (len(c), c))
    return out


def absorption(seed, component):
    reduction = old.character_reduction()
    specification = old.inputs()["absorption"][seed]
    k, s = specification["k"], specification["diagonal_exponents"]
    for (p, v, a, _), chi in zip(matter.coefficient_data(seed, component, "E"), reduction["restricted_chi"]):
        assert [(v[p[i]]-k*chi-s[p[i]]+s[i])%5 for i in range(5)] == [0]*5
        phase = sp.diag(*(sp.Symbol("w")**x for x in a))
        conjugator = sp.diag(*(sp.Symbol("q")**x for x in s))
        assert phase*conjugator == conjugator*phase
    return {"seed": seed, "component": component, "M6_entrywise_residuals_zero": True,
            "new_phase_commutes_with_absorbing_diagonal": True, "k": k}


def field_controls():
    split = split_factor(("1", "1", "1"))
    assert len(split) == 2 and all(r["degree_over_K"] == 1 for r in split)
    ranks = []
    for row in split:
        value, omega, _ = field_for_factor(tuple(tuple(x) for x in row["coefficients_ab"]))
        ranks.append((value-omega).rank()//2)
    assert sorted(ranks) == [0, 1]
    irreducible = split_factor(("1", "0", "-2"))
    assert len(irreducible) == 1 and irreducible[0]["degree_over_K"] == 2
    value, omega, _ = field_for_factor(tuple(tuple(x) for x in irreducible[0]["coefficients_ab"]))
    assert value**2 == 2*eye(4) and value.nrows() == 4
    assert coord_matrix(coords(OMEGA)) == matter.Z
    assert coord_matrix(coords(1-2*OMEGA)) == eye(2)-2*matter.Z
    try:
        field_for_factor((("1", "0"), ("1", "0"), ("1", "0")))
    except AssertionError:
        rejected = True
    else:
        raise AssertionError("Reducible tensor was accepted as a field")
    return {"rational_factor_split_before_field_ranks": True,
            "two_roots_with_different_toy_ranks_distinguished": ranks,
            "irreducible_quadratic_has_Q_degree_four": True,
            "coordinate_embedding_and_trace_pairing_verified": True,
            "reducible_tensor_rejected_as_field": rejected}


def retained_points():
    rows = []
    for seed in inputs()["seeds"]:
        for component in inputs()["components"]:
            for parameter in (-1, 1, 2):
                coefficients = (("1", "0"), (str(-parameter), "0"))
                point = candidate_point(seed, component, (0,)*7, coefficients)
                oldpoint = matter.point(seed, component, parameter)["coefficients"]["E"]
                assert point["n"] == oldpoint["n"] and point["n_dual"] == oldpoint["n_dual"]
                rows.append(point)
    return rows


def run():
    print("FIELD_CONTROL", json.dumps(field_controls()), flush=True)
    reduction = old.character_reduction()
    print("LINE_REDUCTION", json.dumps({"all_marked_meridian_trivial_characters": reduction["character_count"],
          "inverse_fourth_power_images": reduction["fourth_power_count"],
          "quadratic_characters": reduction["quadratic_characters"], "parent": old.parent_center()}), flush=True)
    for row in retained_points():
        print("RETAINED", json.dumps(row), flush=True)
    complete, generic_zero, target_excluded, observed = True, True, True, []
    for seed in inputs()["seeds"]:
        for component in inputs()["components"]:
            print("ABSORPTION", json.dumps(absorption(seed, component)), flush=True)
            for eta in reduction["quadratic_characters"]:
                eta = tuple(eta)
                cert = certificate(seed, component, eta)
                print("CERTIFICATE", json.dumps(cert), flush=True)
                bounds = [x["interior_upper_bound_off_candidate_roots"] for x in cert["coefficients"].values()]
                generic_zero &= max(bounds) == 0
                target_excluded &= max(bounds) < 3
                for coefficients in cert["candidate_factors_over_Q"]:
                    for factor in split_factor(tuple(coefficients)):
                        if factor["degree_over_K"] > inputs()["maximum_K_factor_degree"]:
                            complete = False
                            print("UNANALYSED", json.dumps({"seed": seed, "component": component, "eta": eta,
                                  "Q_factor": coefficients, "K_factor": factor}), flush=True)
                            continue
                        point = candidate_point(seed, component, eta, tuple(tuple(x) for x in factor["coefficients_ab"]))
                        observed.append(point["indexed"]["I"])
                        print("ROOT", json.dumps({"Q_factor": coefficients, "K_factor": factor, "point": point}), flush=True)
    summary = {"all_nonzero_complex_parameters_and_reduced_lines_covered": complete,
               "generic_open_set_E_and_dual_interior_zero": generic_zero,
               "required_u_index_zero_for_all_meridian_trivial_lines": complete and generic_zero and all(x == 0 for x in observed),
               "joint_three_generation_linear_target_excluded_in_four_families": complete and target_excluded and all(abs(x) != 3 for x in observed),
               "candidate_indices": observed, "all_other_backgrounds_classified": False,
               "parameter_free_SM_derived": False, "full_physical_theory_derived": False}
    print("SUMMARY", json.dumps(summary), flush=True)
    print("PASS: exact identities and certificates; outcome and completeness are in SUMMARY")
    return summary


if __name__ == "__main__":
    run()
