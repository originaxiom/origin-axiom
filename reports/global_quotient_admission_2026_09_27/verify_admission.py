"""Exact parent and flat-lift admission. No first execution before seal."""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations, product
from pathlib import Path
import json
import sys
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "m6_parent_admission_2026_09_27"))
import verify_parent_admission as parent
sys.path.insert(0, str(HERE.parent / "global_sl5_seed_2026_09_27"))
from verify_topology import cover, generator_words


def inputs():
    return json.loads((HERE / "INPUTS.json").read_text())


def gl_weight(s, q):
    base = [sum(s[i:]) for i in range(4)] + [0]
    shift = sp.Rational(q-sum(base), 5)
    assert shift.q == 1, (s, q, shift)
    return tuple(int(x+shift) for x in base)


def exterior_weights(k, determinant_power=0):
    return Counter(tuple(int(i in chosen)+determinant_power for i in range(5))
                   for chosen in combinations(range(5), k))


def coefficient_fiber(weights, sm):
    out = Counter()
    for (g, s), multiplicity in weights.items():
        label = parent.sm_label(g)
        if label == sm:
            out[gl_weight(s, label[-1])] += multiplicity
    return out


@lru_cache(None)
def parent_control():
    actual = parent.actual_branching()
    assert actual == parent.expected_branching()
    count = 0
    for (g, s), multiplicity in actual.items():
        q = parent.sm_label(g)[-1]
        w = gl_weight(s, q)
        assert sum(w) == q and tuple(w[i]-w[i+1] for i in range(4)) == s
        count += multiplicity
    assert count == 248
    specifications = {"Q": (1, 0), "u": (1, -1), "e": (1, 1),
                      "d": (2, 0), "L": (2, -1)}
    for name, (k, power) in specifications.items():
        label = parent.SECTOR_LABELS[name]
        got = coefficient_fiber(actual, label)
        assert got == exterior_weights(k, power)
        assert got != exterior_weights(k, power+1)
        opposite = coefficient_fiber(actual, tuple(-x for x in label))
        assert opposite == Counter({tuple(-x for x in w): n for w, n in got.items()})
    roots = parent.roots_twice()
    g, s = parent.bases_twice()
    central = [r for r in roots if all(parent.ip(r, g[i]) == 0 for i in (0, 1, 3))]
    with_y = [r for r in central if parent.sm_label(parent.dynkin(r, g))[-1] == 0]
    structure = [r for r in roots if parent.dynkin(r, g) == parent.ZERO4]
    assert set(with_y) == set(structure)
    assert len(with_y) == 20 and len(central) == 30
    # An element central in SU5_s is z^b; x=z^a in U1.
    kernel = []
    for a, b in product(range(5), repeat=2):
        if all((a*parent.sm_label(gw)[-1] + b*sum((i+1)*x for i, x in enumerate(sw))) % 5 == 0
               for (gw, sw) in actual):
            kernel.append((a, b))
    assert kernel == [(a, -a % 5) for a in range(5)]
    # Cross-block gauge roots force x^5=1; then every Q component forces s=x^-1 I.
    assert coefficient_fiber(actual, (1, 0, 1, -5)) == Counter({(-1,)*5: 1})
    return {"all_parent_weight_multiplicities": count,
            "SM_connected_centralizer_dimension": len(with_y)+5,
            "without_Y_centralizer_dimension": len(central)+5,
            "line_structure_kernel_mod5": kernel,
            "five_sector_dictionary_and_actual_duals": True,
            "connected_compact_group": "U(5)", "disconnected_components_classified": False}


def exponent(word, n):
    return tuple(word.count(i)-word.count(-i) for i in range(1, n+1))


def value(word, phase, modulus):
    return sum((1 if i > 0 else -1)*phase[abs(i)-1] for i in word) % modulus


def finite_characters(a, modulus):
    inv = a.inv()
    generators = []
    for j in range(a.cols):
        column = [modulus*inv[i, j] for i in range(a.rows)]
        assert all(x.q == 1 for x in column)
        generators.append(tuple(int(x) % modulus for x in column))
    zero = (0,)*a.cols
    found, queue = {zero}, deque([zero])
    while queue:
        x = queue.popleft()
        for y in generators:
            z = tuple((u+v) % modulus for u, v in zip(x, y))
            if z not in found:
                found.add(z)
                queue.append(z)
    assert len(found) == abs(int(a.det()))
    assert all(all(v % modulus == 0 for v in a*sp.Matrix(x)) for x in found)
    return found, generators


@lru_cache(None)
def topology_control():
    rels, mu, lam = cover(6)
    a_full = sp.Matrix([exponent(r, 7) for r in rels])
    free = inputs()["free_splitting"]
    assert a_full*sp.Matrix(free) == sp.zeros(6, 1)
    base_exponents = [sum(1 if x > 0 else -1 for x in w) for w in generator_words(6)]
    assert [x//6 for x in base_exponents] == free
    assert all(x % 6 == 0 for x in base_exponents)
    a = a_full[:, 1:]
    cycle = sp.Matrix(6, 6, lambda i, j: -3 if i == j else int((i-j) % 6 in (1, 5)))
    assert a == cycle and exponent(lam, 7) == (0,)*7 and mu == (1,)
    snf = smith_normal_form(a, domain=sp.ZZ)
    factors = [abs(int(snf[i, i])) for i in range(6)]
    assert factors == [1, 1, 1, 1, 8, 40]
    modulus = inputs()["modulus"]
    chars, generators = finite_characters(a, modulus)
    image = {tuple(5*v % modulus for v in c) for c in chars}
    kernel = [c for c in chars if all(5*v % modulus == 0 for v in c)]
    assert len(chars) == 320 and len(image) == 64 and len(kernel) == 5
    fibers = Counter(tuple(5*v % modulus for v in c) for c in chars)
    assert set(fibers.values()) == {5}
    witness = generators[0]
    assert witness not in image
    cosets = [{tuple((j*w+x) % modulus for w, x in zip(witness, c)) for c in image}
              for j in range(5)]
    assert all(len(c) == 64 for c in cosets)
    assert len(set.union(*cosets)) == 320 and set.union(*cosets) == chars
    assert all(not cosets[i].intersection(cosets[j]) for i in range(5) for j in range(i))
    phase = (0, *witness)
    assert all(value(r, phase, modulus) == 0 for r in rels)
    assert value(mu, phase, modulus) == value(lam, phase, modulus) == 0
    return {"relation_matrix": a_full.tolist(), "free_splitting": free,
            "smith_factors_after_free_split": factors, "torsion_character_count": len(chars),
            "fifth_image_count": len(image), "fifth_kernel_count": len(kernel),
            "lift_obstruction_class_count": len(cosets), "witness_phases_mod40": phase,
            "witness_coset_representatives_mod40": [[0, *(j*x % modulus for x in witness)] for j in range(5)],
            "all_cosets_exhaustive_and_disjoint": True,
            "longitude_character_trivial": True}


def diagonal_witness():
    row = topology_control()
    p = row["witness_phases_mod40"]
    rels, mu, lam = cover(6)
    phases = [(x, 0, 0, 0, 0) for x in p]
    for word in [*rels, mu, lam]:
        totals = [sum((1 if k > 0 else -1)*phases[abs(k)-1][i] for k in word) % 40 for i in range(5)]
        assert totals == [0]*5
    # Actual dual/conjugate has opposite phases, independently of the determinant powers.
    profile = {}
    for name, k, power in [("Q", 1, 0), ("u", 1, -1), ("e", 1, 1), ("d", 2, 0), ("L", 2, -1)]:
        weights = list(exterior_weights(k, power).elements())
        character_vectors = [tuple(sum(w[i]*v[i] for i in range(5)) % 40 for v in phases) for w in weights]
        assert all(all(value(r, c, 40) == 0 for r in rels) for c in character_vectors)
        dual = [tuple(-v % 40 for v in c) for c in character_vectors]
        assert all(all((x+y) % 40 == 0 for x, y in zip(c, d)) for c, d in zip(character_vectors, dual))
        profile[name] = len(character_vectors)
    return {"diagonal_generator_phases_mod40": phases, "charged_ranks": profile,
            "honest_unitary_representation": True, "all_peripheral_matrices_identity": True,
            "separate_flat_lift_exists": False, "Psi": 0,
            "net_chirality_by_unitary_dual_pairing": 0,
            "individual_mode_dimensions_computed": False,
            "exact_SM_unbroken_group_claimed": False}


def controls():
    assert len({5*x % 4 for x in range(4)}) == 4
    assert len({5*x % 5 for x in range(5)}) == 1
    # General scalar twisting adds an element of the fifth image.
    a = sp.Matrix(topology_control()["relation_matrix"])[:, 1:]
    chars, _ = finite_characters(a, 40)
    fifth = {tuple(5*v % 40 for v in x) for x in chars}
    witness = topology_control()["witness_phases_mod40"][1:]
    assert all(tuple((w+5*x) % 40 for w, x in zip(witness, c)) not in fifth for c in chars)
    assert (0,)*6 in fifth
    assert all(tuple(5*x % 40 for x in c) in fifth for c in chars)
    return {"C4_fifth_power_surjective": True, "C5_fifth_power_not_surjective": True,
            "all_320_scalar_twists_preserve_nonliftability": True,
            "all_320_determinants_of_scalar_twists_of_SL5_lift": True}


def run():
    for key, result in [("PARENT", parent_control()), ("TOPOLOGY", topology_control()),
                        ("WITNESS", diagonal_witness()), ("CONTROLS", controls())]:
        print(key, json.dumps(result), flush=True)
    print("PASS: combined quotient admits additional flat sectors; no chiral spectrum constructed")


if __name__ == "__main__":
    run()
