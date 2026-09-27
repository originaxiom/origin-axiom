"""Exact centralizer certificates, full root characters and harmonic inputs."""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations, permutations, product
from pathlib import Path
import json
import sys
import sympy as sp
from flint import fmpq_mat

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "monomial_harmonic_background_2026_09_27"))
import verify_harmonic_background as hb
ex = hb.ex
from verify_global_seed import Rep, eye, kron, pullback, vs
from verify_topology import cover, data
from verify_finite_seed import compose
sys.path.insert(0, str(HERE.parent / "m6_parent_admission_2026_09_27"))
import verify_parent_admission as parent


def inputs():
    return json.loads((HERE / "INPUTS.json").read_text())


def up_monomials(gens):
    return [ex.word(w, gens) for w in data()["M6_generators_in_M2"]]


def dual_monomials(gens):
    return [(p, tuple(-v for v in weights), signs) for p, weights, signs in gens]


def permutation_group(gens):
    # The older finite-seed helper is deliberately fixed to SIX letters.
    # This is the actual FIVE-letter action, with its own identity.
    identity = tuple(range(len(gens[0])))
    seen, queue = {identity}, [identity]
    for a in queue:
        for b in gens:
            c = compose(a, b)
            if c not in seen:
                seen.add(c)
                queue.append(c)
    return seen


@lru_cache(None)
def coefficient_modules(number):
    mods = {k: up_monomials(v) for k, v in ex.modules(ex.inputs()["seeds"][number]).items()}
    for name in ("E", "wedge2E"):
        mods["dual_"+name] = dual_monomials(mods[name])
        numeric = ex.specialization(mods[name], fmpq_mat([[2]]))
        assert ex.specialization(mods["dual_"+name], fmpq_mat([[2]])).mats == numeric.dual().mats
    return mods


def invariants(rep, degree=1):
    d0 = vs(*(g-eye(rep.d) for g in rep.mats))
    dim = rep.d-d0.rank()
    assert dim % degree == 0
    return dim//degree


@lru_cache(None)
def diagonal_control(number):
    down, gram = hb.diagonal_representation(ex.inputs()["seeds"][number])
    up = pullback(down)
    assert invariants(up) == 0
    assert all(g.transpose()*hb.as_flint(gram)*g == hb.as_flint(gram) for g in up.mats)
    return {"H0": 0, "dimension": 4, "positive_parallel_metric": True}


@lru_cache(None)
def certificate(number):
    mods = coefficient_modules(number)
    candidates, records = set(), {}
    for name in inputs()["coefficients"]:
        gens = mods[name]
        dim = len(gens[0][0])
        assert all(ex.word(r, gens) == ex.identity(dim) for r in cover(6)[0])
        d0 = sp.Matrix.vstack(*(ex.matrix(g)-sp.eye(dim) for g in gens))
        record, _ = ex.selected_minor(d0, inputs()["generic_control"])
        assert record["rank"] == dim, (number, name, record["rank"], dim)
        records[name] = record
        for factor in record["factors"]:
            c = tuple(factor["coefficients"])
            if c != ("1", "0"):
                candidates.add(c)
    return {"seed": number, "diagonal": diagonal_control(number),
            "coefficients": records,
            "candidate_factors": sorted(candidates, key=lambda c: (len(c), c)),
            "generic_full_parent_dimension": 24}


@lru_cache(None)
def point(number, coefficients):
    value = ex.companion(coefficients)
    degree = value.nrows()
    mods = coefficient_modules(number)
    h0 = {name: invariants(ex.specialization(mods[name], value), degree)
          for name in inputs()["coefficients"]}
    assert h0["E"] == h0["dual_E"] and h0["wedge2E"] == h0["dual_wedge2E"]
    total = 24+h0["off"]+10*(h0["E"]+h0["dual_E"])+5*(h0["wedge2E"]+h0["dual_wedge2E"])
    return {"seed": number, "factor": list(coefficients), "field_degree": degree,
            "H0": h0, "full_parent_dimension": total}


def exterior_weights(n, k):
    return Counter(tuple(int(i in subset)-int(i+1 in subset) for i in range(n-1))
                   for subset in combinations(range(n), k))


def adjoint_weights(n):
    result = Counter({(0,)*(n-1): n-1})
    for i in range(n):
        for j in range(n):
            if i != j:
                v = [int(k == i)-int(k == j) for k in range(n)]
                result[tuple(v[k]-v[k+1] for k in range(n-1))] += 1
    return result


def d5_standard():
    e = [tuple(int(i == j) for j in range(5)) for i in range(5)]
    simple = [parent.sub(e[i], e[i+1]) for i in range(4)]+[parent.add(e[3], e[4])]
    roots = []
    for i, j in combinations(range(5), 2):
        for a, b in product((-1, 1), repeat=2):
            roots.append(tuple(a*e[i][k]+b*e[j][k] for k in range(5)))
    return e, simple, roots


def labels5(v, basis):
    return tuple(parent.ip(v, a) for a in basis)


@lru_cache(None)
def root_control():
    roots = parent.roots_twice()
    gauge, struct = parent.bases_twice()
    a3 = struct[1:]
    commuting = [r for r in roots if all(parent.ip(r, a) == 0 for a in a3)]
    grading = inputs()["positive_root_grading"]
    assert all(parent.ip(r, grading) != 0 for r in commuting)
    positive = [r for r in commuting if parent.ip(r, grading) > 0]
    sums = {parent.add(a, b) for a in positive for b in positive}
    simple = [r for r in positive if r not in sums]
    e, standard_simple, standard_roots = d5_standard()
    standard_cartan = [[parent.ip(a, b) for b in standard_simple] for a in standard_simple]
    order = next(p for p in permutations(simple)
                 if [[parent.ip(a, b)//4 for b in p] for a in p] == standard_cartan)
    assert len(simple) == 5 and len(commuting) == 40
    actual_root_labels = Counter(parent.dynkin(r, order) for r in commuting)
    expected_root_labels = Counter(labels5(r, standard_simple) for r in standard_roots)
    assert actual_root_labels == expected_root_labels
    assert all(g in commuting for g in gauge)
    assert sp.Matrix(standard_cartan).det() == 4

    z5, z3 = (0,)*5, (0,)*3
    actual = Counter((parent.dynkin(r, order), parent.dynkin(r, a3)) for r in roots)
    actual[(z5, z3)] += 8
    def fibre(a):
        return Counter({d: multiplicity for (d, b), multiplicity in actual.items() if b == a})
    spin, conjugate_spin, vector = fibre((1, 0, 0)), fibre((0, 0, 1)), fibre((0, 1, 0))
    expected_vector = Counter(labels5(v, standard_simple) for x in e for v in (x, tuple(-y for y in x)))
    spin_sets = []
    for parity in range(2):
        spin_sets.append(Counter(labels5(tuple(sp.Rational(v, 2) for v in signs), standard_simple)
                                 for signs in product((-1, 1), repeat=5)
                                 if signs.count(-1) % 2 == parity))
    assert vector == expected_vector and sum(vector.values()) == 10
    assert spin in spin_sets and conjugate_spin in spin_sets and spin != conjugate_spin
    assert conjugate_spin == parent.dual(spin)
    adj_d5 = actual_root_labels+Counter({z5: 5})
    one5, one3 = Counter({z5: 1}), Counter({z3: 1})
    four, four_dual, six, ad3 = exterior_weights(4, 1), exterior_weights(4, 3), exterior_weights(4, 2), adjoint_weights(4)
    expected = parent.tensor(adj_d5, one3)+parent.tensor(one5, ad3)
    expected += parent.tensor(spin, four)+parent.tensor(conjugate_spin, four_dual)+parent.tensor(vector, six)
    assert actual == expected and sum(actual.values()) == 248
    wrong = parent.tensor(adj_d5, one3)+parent.tensor(one5, ad3)
    wrong += parent.tensor(spin, four)+parent.tensor(spin, four_dual)+parent.tensor(vector, six)
    assert actual != wrong

    invariant = [r for r in commuting if sum((j+1)*v for j, v in enumerate(parent.dynkin(r, struct))) % 5 == 0]
    gauge_roots = [r for r in roots if all(parent.ip(r, a) == 0 for a in struct)]
    assert set(invariant) == set(gauge_roots) and len(invariant) == 20
    charges = Counter(sum(c*v for c, v in zip((4, 3, 2, 1), parent.dynkin(r, struct))) for r in commuting)
    assert charges == {0: 20, 4: 10, -4: 10}
    return {"commuting_root_count": len(commuting), "commuting_Cartan_dimension": 5,
            "D5_simple_roots_twice": list(order), "D5_Cartan": standard_cartan,
            "full_D5_root_labels_match": True, "full_248_branching_match": True,
            "spinor_weights_distinct_and_contragredient": True, "wrong_spinor_conjugation_rejected": True,
            "fifth_center_invariant_roots": len(invariant), "D5_extra_torus_root_charges": dict(charges)}


@lru_cache(None)
def finite_control(number):
    mods = coefficient_modules(number)
    gens = [g[0] for g in mods["E"]]
    group = permutation_group(gens)
    assert len(group) == 60
    chars = []
    for g in group:
        ch = sum(i == g[i] for i in range(5))-1
        square = compose(g, g)
        ch_square = sum(i == square[i] for i in range(5))-1
        chars.append((ch, (ch*ch-ch_square)//2, ch*ch-1))
    averages = [sp.Rational(sum(row[i] for row in chars), 60) for i in range(3)]
    inner = sp.Rational(sum(row[0]**2 for row in chars), 60)
    assert averages == [0, 0, 0] and inner == 1
    chi = inputs()["M2_chi5_exponents"]
    exponents = [sum((1 if x > 0 else -1)*chi[abs(x)-1] for x in w) % 5
                 for w in data()["M6_generators_in_M2"]]
    lifted_gens = list(zip(gens, exponents))
    identity = (tuple(range(5)), 0)
    seen, queue = {identity}, deque([identity])
    while queue:
        a, c = queue.popleft()
        for b, d in lifted_gens:
            item = (compose(a, b), (c+d) % 5)
            if item not in seen:
                seen.add(item)
                queue.append(item)
    assert len(seen) == 300 and all((g, k) in seen for g in group for k in range(5))
    spec = inputs()["absorption"][number]
    k, s = spec["k"], spec["diagonal_exponents"]
    assert k % 5 != 0
    for (p, v, _), c in zip(ex.modules(ex.inputs()["seeds"][number])["E"], chi):
        assert all((v[p[i]]-k*c-s[p[i]]+s[i]) % 5 == 0 for i in range(5))
    return {"seed": number, "M6_permutation_image_order": 60,
            "U_character_norm": str(inner), "invariants_U_wedgeU_adU": [int(x) for x in averages],
            "permutation_and_chi5_image_order": 300, "fifth_absorption_checked": True}


def wedge_matrix(a):
    pairs = list(combinations(range(a.nrows()), 2))
    return fmpq_mat([[a[i, k]*a[j, l]-a[i, l]*a[j, k] for k, l in pairs] for i, j in pairs])


def cohom_record(rep):
    a, _ = ex.indexed(rep, 6, 1)
    return {"ordinary": a, "n": a["V"][1]-a["V"][4],
            "n_dual": a["dual"][1]-a["dual"][4]}


@lru_cache(None)
def enhanced_matter(number):
    seed = ex.inputs()["seeds"][number]
    down, gram = hb.diagonal_representation(seed)
    u = pullback(down)
    trivial = Rep([eye(1) for _ in u.mats])
    wedge = Rep([wedge_matrix(g) for g in u.mats])
    end = Rep([kron(g, g.inv().transpose()) for g in u.mats])
    records = {"trivial": cohom_record(trivial), "U": cohom_record(u),
               "wedgeU": cohom_record(wedge), "EndU": cohom_record(end)}
    n = {name: record["n"] for name, record in records.items()}
    n_ad = n["EndU"]-n["trivial"]
    assert n_ad >= 0
    spectrum = {"45": n["trivial"], "1": n_ad, "16": n["U"],
                "16_dual": records["U"]["n_dual"], "10": n["wedgeU"]}
    total = 45*spectrum["45"]+spectrum["1"]+16*(spectrum["16"]+spectrum["16_dual"])+10*spectrum["10"]
    # Separate bookkeeping through the full original A4 x A4 branching.
    original = {name: cohom_record(ex.specialization(gens, fmpq_mat([[1]])))
                for name, gens in coefficient_modules(number).items()}
    diagonal = cohom_record(u)
    original_total = 24*n["trivial"]+diagonal["n"]+original["off"]["n"]
    original_total += 10*(original["E"]["n"]+original["dual_E"]["n"])
    original_total += 5*(original["wedge2E"]["n"]+original["dual_wedge2E"]["n"])
    assert total == original_total
    assert records["trivial"]["ordinary"]["V"][0] == 1
    assert records["EndU"]["ordinary"]["V"][0] == 1
    return {"seed": number, "coefficients": records, "conditional_D5_degree_one_spectrum": spectrum,
            "full_degree_one_dimension": total, "original_branching_total": original_total,
            "original_branching_coefficients": original}


@lru_cache(None)
def tangent_control(number):
    x = sp.symbols("x0:4", real=True)
    h = sp.diag(*x, -sum(x))
    p, q = sp.ones(5)/5, sp.eye(5)-sp.ones(5)/5
    assert p*p == p and q*q == q and p*q == sp.zeros(5)
    assert sp.simplify(p*h*p) == sp.zeros(5)
    pieces = [q*h*p, p*h*q, q*h*q]
    assert sp.simplify(sum(pieces, sp.zeros(5))-h) == sp.zeros(5)
    assert all(sp.simplify(sp.trace(a)) == 0 for a in pieces)
    norm = sp.trace(h*h)
    fractions = [sp.Rational(1, 5), sp.Rational(1, 5), sp.Rational(3, 5)]
    for a, weight in zip(pieces, fractions):
        assert sp.expand(sp.trace(a.T*a)-weight*norm) == 0
    assert all(sp.expand(sp.trace(a.T*b)) == 0 for a, b in combinations(pieces, 2))
    for permutation in ex.inputs()["seeds"][number]["permutations"]:
        matrix = sp.Matrix(5, 5, lambda i, j: int(i == permutation[j]))
        assert matrix*p == p*matrix and matrix*q == q*matrix
        transformed = matrix*h*matrix.T
        targets = [q*transformed*p, p*transformed*q, q*transformed*q]
        assert all(sp.simplify(matrix*a*matrix.T-b) == sp.zeros(5) for a, b in zip(pieces, targets))
    inherited = hb.one_seed(number)
    assert inherited["global_class_nonzero"]
    return {"seed": number, "norm_fractions_U_dualU_adU": [str(f) for f in fractions],
            "orthogonal_parallel_projection": True, "nonzero_actual_harmonic_class_rechecked": True,
            "individual_nonlinear_integrability_claimed": False}


def main():
    print("ROOTS", json.dumps(root_control()), flush=True)
    complete = True
    for number in inputs()["seeds"]:
        print("FINITE", json.dumps(finite_control(number)), flush=True)
        cert = certificate(number)
        print("CERTIFICATE", json.dumps(cert), flush=True)
        for factor in cert["candidate_factors"]:
            if len(factor)-1 > inputs()["max_factor_degree"]:
                print("UNANALYSED", json.dumps({"seed": number, "factor": factor}), flush=True)
                complete = False
            else:
                print("EXCEPTION", json.dumps(point(number, tuple(factor))), flush=True)
        print("MATTER", json.dumps(enhanced_matter(number)), flush=True)
        print("TANGENT", json.dumps(tangent_control(number)), flush=True)
    print("SCOPE", json.dumps({"all_nonzero_parameters_H0_classified": complete,
          "common_line": "trivial only", "global_group_form_classified": False,
          "physical_grade": "conditional on supplied model and authored analytic bridge",
          "chirality_repaired": False, "isolated_4d_EFT": False}), flush=True)
    print("PASS: exact full-parent controls and harmonic inputs; inspect all exceptional algebras")


if __name__ == "__main__":
    main()
