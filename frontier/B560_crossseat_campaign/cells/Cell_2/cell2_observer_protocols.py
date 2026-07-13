#!/usr/bin/env python3
"""Cell 2 — exact observer-flow closure and protocol dependence.

The finite word is used only to discover candidate return words. Every
derivation step is then certified without a finite-prefix assumption by:

1. exact return-word boundary identities;
2. exact morphism intertwining;
3. primitivity of the return substitution;
4. prolongability on the initial return word.

These conditions prove that the candidate return substitution generates the
complete derived sequence of the source fixed point.
"""

from __future__ import annotations

from collections import Counter, deque
import itertools
import json

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


SEED_SYSTEMS = {
    "S_A": ((0,1,2,3),(3,2,0,3),(3,),(0,1,2,0,3)),
    "S_B": ((0,1,2),(0,1,0,3,2,0),(0,1),(0,1,2,0)),
    "S_a": ((0,1,2,2,3),(0,2,3),(0,1,2,3),(0,2)),
    "S_b": ((0,1,2,3),(2,0,3),(0,3),(2,0,1,0,3)),
    "S_aA": ((0,1,2,3,2,1),(4,2,3,2,3),(0,1),(4,2,3),(0,1,2,3)),
    "S_Bab": ((0,1,2,1,3),(3,),(1,0,3),(0,1,2,1,0,3)),
    "S_bABab": (
        (0,1,0,1,2,3,1,0,1,2,3,1,4,1,0,1,2,3,1),
        (0,1,3,1,4,1),
        (0,1,0,1,2,3,1,4,1,0,1,2,3,1,4,1),
        (0,1,0,1,2,3,1,0,1,2,3,1,4,1,0,1,2,3,1,4,1,0,1,2,3,1),
        (0,1,0,1,2,3,1,4,1,0,1,2,3,1),
    ),
}

X = sp.symbols("x")
P1 = X**4 - 2*X**3 - 5*X**2 - 4*X - 1
P2 = X**4 - 14*X**3 + 7*X**2 - 6*X + 1


def relabel_codes(codes, permutation):
    size = len(codes)
    inverse = [0] * size
    for old, new in enumerate(permutation):
        inverse[new] = old
    return tuple(
        tuple(permutation[symbol] for symbol in codes[inverse[new_domain]])
        for new_domain in range(size)
    )


def canonical_with_permutation(codes):
    return min(
        (
            relabel_codes(codes, permutation),
            permutation,
        )
        for permutation in itertools.permutations(range(len(codes)))
    )


def canonical_codes(codes):
    return canonical_with_permutation(codes)[0]


def incidence(codes):
    size = len(codes)
    return sp.Matrix([
        [
            sum(symbol == row for symbol in codes[column])
            for column in range(size)
        ]
        for row in range(size)
    ])


def apply_codes(codes, word):
    output = []
    for symbol in word:
        output.extend(codes[symbol])
    return tuple(output)


def fixed_prefix(codes, minimum_length=140000):
    assert codes[0][0] == 0
    word = (0,)
    while len(word) < minimum_length:
        word = apply_codes(codes, word)
    return word


def occurrences(word, factor, maximum_start=None):
    size = len(factor)
    bound = len(word) - size + 1
    if maximum_start is not None:
        bound = min(bound, maximum_start)
    return [
        start
        for start in range(bound)
        if word[start:start + size] == factor
    ]


def primitive(matrix):
    size = matrix.rows
    accumulated = sp.zeros(size)
    power = sp.eye(size)
    for _ in range(size * size):
        power = power * matrix
        accumulated += power
        if all(
            accumulated[row, column] > 0
            for row in range(size)
            for column in range(size)
        ):
            return True
    return False


def q_type(codes):
    polynomial = sp.factor(incidence(codes).charpoly(X).as_expr())
    if sp.expand(polynomial - P1) == 0:
        return 1
    if sp.expand(polynomial - X * P1) == 0:
        return 1
    if sp.expand(polynomial - P2) == 0:
        return 2
    if sp.expand(polynomial - X * P2) == 0:
        return 2
    raise AssertionError(f"Unexpected polynomial: {polynomial}")


def exact_prefix_derivation(codes, prefix_length):
    codes = canonical_codes(codes)
    source_matrix = incidence(codes)
    assert codes[0][0] == 0
    assert primitive(source_matrix)

    fixed = fixed_prefix(codes)
    prefix = fixed[:prefix_length]
    positions = occurrences(fixed, prefix, maximum_start=100000)

    return_words = []
    return_index = {}
    for start, end in zip(positions, positions[1:]):
        return_word = fixed[start:end]
        if return_word not in return_index:
            return_index[return_word] = len(return_words)
            return_words.append(return_word)

    raw_codes = []
    exact_identities = []

    for return_word in return_words:
        image = apply_codes(codes, return_word)
        augmented = image + prefix
        boundaries = [
            start
            for start in occurrences(augmented, prefix)
            if start <= len(image)
        ]

        assert boundaries[0] == 0
        assert boundaries[-1] == len(image)

        parsed = []
        for start, end in zip(boundaries, boundaries[1:]):
            piece = image[start:end]
            assert piece in return_index
            parsed.append(return_index[piece])

        parsed = tuple(parsed)
        raw_codes.append(parsed)

        decoded = tuple(
            symbol
            for return_symbol in parsed
            for symbol in return_words[return_symbol]
        )
        assert image == decoded
        exact_identities.append(True)

    raw_codes = tuple(raw_codes)
    target_matrix = incidence(raw_codes)

    proper_return_words = all(
        occurrences(return_word + prefix, prefix)
        == [0, len(return_word)]
        for return_word in return_words
    )
    target_primitive = primitive(target_matrix)
    target_prolongable = raw_codes[0][0] == 0

    assert proper_return_words
    assert target_primitive
    assert target_prolongable
    assert all(exact_identities)

    canonical, permutation = canonical_with_permutation(raw_codes)

    proof = {
        "prefix_length": prefix_length,
        "prefix": list(prefix),
        "return_words": [list(word) for word in return_words],
        "raw_codes": [list(image) for image in raw_codes],
        "canonical_codes": [list(image) for image in canonical],
        "return_word_count": len(return_words),
        "source_primitive": True,
        "source_prolongable": True,
        "proper_return_words": True,
        "exact_intertwining_identities": True,
        "target_primitive": True,
        "target_prolongable": True,
        "completeness_argument": (
            "The primitive prolongable return substitution has a fixed point y. "
            "The coding Theta satisfies source(Theta(i))=Theta(target(i)) exactly, "
            "so Theta(y) is the unique source fixed point beginning in 0. Proper "
            "return-word boundaries then imply the return-word list is complete."
        ),
        "exact_step_certified": True,
    }
    return canonical, proof


def build_protocol(prefix_length):
    code_to_name = {}
    nodes = {}
    queue = deque()

    for name, codes in SEED_SYSTEMS.items():
        canonical = canonical_codes(codes)
        if canonical not in code_to_name:
            code_to_name[canonical] = name
            nodes[name] = canonical
            queue.append(name)

    edges = {}
    proofs = {}
    new_index = 0

    while queue:
        source = queue.popleft()
        target_codes, proof = exact_prefix_derivation(
            nodes[source],
            prefix_length,
        )

        if target_codes not in code_to_name:
            target = f"K{prefix_length}_N{new_index}"
            new_index += 1
            code_to_name[target_codes] = target
            nodes[target] = target_codes
            queue.append(target)
        else:
            target = code_to_name[target_codes]

        edges[source] = target
        proofs[source] = proof

    return nodes, edges, proofs


def canonical_cycle(cycle):
    minimum_index = min(
        range(len(cycle)),
        key=lambda index: cycle[index],
    )
    return cycle[minimum_index:] + cycle[:minimum_index]


def graph_summary(nodes, edges):
    fixed_points = sorted(
        node for node, target in edges.items()
        if node == target
    )

    cycles = []
    globally_seen = set()

    for start in sorted(nodes):
        if start in globally_seen:
            continue

        path = []
        path_index = {}
        current = start

        while (
            current not in path_index
            and current not in globally_seen
        ):
            path_index[current] = len(path)
            path.append(current)
            current = edges[current]

        if current in path_index:
            cycle = path[path_index[current]:]
            cycles.append(canonical_cycle(cycle))

        globally_seen.update(path)

    cycles.sort(key=lambda cycle: (len(cycle), cycle))
    nontrivial = [cycle for cycle in cycles if len(cycle) > 1]

    return {
        "node_count": len(nodes),
        "fixed_points": fixed_points,
        "fixed_point_count": len(fixed_points),
        "cycles": cycles,
        "nontrivial_cycles": nontrivial,
        "nontrivial_cycle_lengths": [
            len(cycle) for cycle in nontrivial
        ],
        "nontrivial_cycle_q_types": [
            [q_type(nodes[node]) for node in cycle]
            for cycle in nontrivial
        ],
        "alphabet_size_counts": dict(
            sorted(Counter(len(codes) for codes in nodes.values()).items())
        ),
    }


def orbit_record(start, edges):
    path = []
    positions = {}
    current = start

    while current not in positions:
        positions[current] = len(path)
        path.append(current)
        current = edges[current]

    return {
        "path": path,
        "cycle_entry": current,
        "preperiod": positions[current],
        "cycle_length": len(path) - positions[current],
    }


def smith_diagonal(matrix):
    smith = smith_normal_form(matrix, domain=ZZ)
    return [
        abs(int(smith[index, index]))
        for index in range(min(smith.shape))
    ]


def invariant_collision(protocol_one_nodes, protocol_one_edges):
    matrix_sa = incidence(protocol_one_nodes["S_a"])
    matrix_sb = incidence(protocol_one_nodes["S_B"])

    conjugator = sp.Matrix([
        [0, -5, -3, -5],
        [0, -3, -2, -3],
        [-5, -3, 0, 0],
        [-3, -2, 0, 0],
    ])

    assert matrix_sa * conjugator == conjugator * matrix_sb
    assert int(conjugator.det()) == -1

    packet_sa = {
        "alphabet_size": 4,
        "q": q_type(protocol_one_nodes["S_a"]),
        "charpoly": str(sp.factor(matrix_sa.charpoly(X).as_expr())),
        "smith_I_minus_A": smith_diagonal(sp.eye(4) - matrix_sa),
        "determinant": int(matrix_sa.det()),
        "mod2_conjugate_via_integral_conjugator": True,
        "GLZ_conjugate": True,
    }
    packet_sb = {
        "alphabet_size": 4,
        "q": q_type(protocol_one_nodes["S_B"]),
        "charpoly": str(sp.factor(matrix_sb.charpoly(X).as_expr())),
        "smith_I_minus_A": smith_diagonal(sp.eye(4) - matrix_sb),
        "determinant": int(matrix_sb.det()),
        "mod2_conjugate_via_integral_conjugator": True,
        "GLZ_conjugate": True,
    }

    assert packet_sa == packet_sb
    assert protocol_one_edges["S_a"] != protocol_one_edges["S_B"]

    return {
        "first_node": "S_a",
        "second_node": "S_B",
        "common_packet": packet_sa,
        "integral_conjugator": [[int(value) for value in row] for row in conjugator.tolist()],
        "conjugator_determinant": -1,
        "first_target": protocol_one_edges["S_a"],
        "second_target": protocol_one_edges["S_B"],
        "conclusion": (
            "The proposed incidence/arithmetic invariant packet does not "
            "determine the observer-flow target."
        ),
    }


def run_all():
    protocols = {}
    rows = []

    for prefix_length in range(1, 13):
        nodes, edges, proofs = build_protocol(prefix_length)
        summary = graph_summary(nodes, edges)
        sigma_orbit = orbit_record("S_a", edges)

        protocols[str(prefix_length)] = {
            "nodes": {
                name: [list(image) for image in codes]
                for name, codes in sorted(nodes.items())
            },
            "edges": dict(sorted(edges.items())),
            "proofs": proofs,
            "summary": summary,
            "sigma_orbit": sigma_orbit,
        }

        rows.append({
            "prefix_length": prefix_length,
            "node_count": summary["node_count"],
            "fixed_point_count": summary["fixed_point_count"],
            "nontrivial_cycle_lengths":
                summary["nontrivial_cycle_lengths"],
            "nontrivial_cycle_q_types":
                summary["nontrivial_cycle_q_types"],
            "sigma_preperiod": sigma_orbit["preperiod"],
            "sigma_cycle_length": sigma_orbit["cycle_length"],
            "all_steps_exactly_certified": all(
                proof["exact_step_certified"]
                for proof in proofs.values()
            ),
        })

    protocol_one = protocols["1"]
    protocol_two = protocols["2"]
    protocol_three = protocols["3"]

    assert protocol_one["summary"]["node_count"] == 12
    assert protocol_one["summary"]["fixed_point_count"] == 3
    assert protocol_one["summary"]["nontrivial_cycle_lengths"] == [2]
    assert protocol_one["summary"]["nontrivial_cycle_q_types"] == [[2, 2]]

    assert protocol_two["summary"]["node_count"] == 12
    assert protocol_two["summary"]["fixed_point_count"] == 2
    assert protocol_two["summary"]["nontrivial_cycle_lengths"] == [2, 2]
    assert protocol_two["sigma_orbit"]["cycle_length"] == 2

    assert protocol_three["summary"]["node_count"] == 11
    assert protocol_three["summary"]["nontrivial_cycle_lengths"] == [2, 2]
    assert protocol_three["sigma_orbit"]["cycle_length"] == 2

    collision = invariant_collision(
        {
            name: tuple(tuple(image) for image in codes)
            for name, codes in protocol_one["nodes"].items()
        },
        protocol_one["edges"],
    )

    return {
        "protocol_definition": (
            "For each node, derive the fixed sequence with respect to its "
            "prefix of length k, canonicalize the exact return substitution, "
            "and iterate to closure from the seven B535 seed systems."
        ),
        "protocols": protocols,
        "protocol_summary_rows": rows,
        "invariant_packet_collision": collision,
        "classification": {
            "prefix_length_1_closure":
                "PROVED_EXACTLY_12_NODES",
            "prefix_length_1_three_fixed_points":
                "PROVED_EXACTLY",
            "prefix_length_1_unique_q2_two_cycle":
                "PROVED_EXACTLY_WITHIN_PROTOCOL",
            "intrinsic_12_node_graph":
                "REFUTED_BY_PREFIX_LENGTH_2_AND_3",
            "intrinsic_sigma_self_fixed_point":
                "REFUTED_BY_PREFIX_LENGTH_2",
            "intrinsic_unique_double_clock":
                "REFUTED_BY_ALTERNATIVE_PREFIX_PROTOCOLS",
            "incidence_arithmetic_packet_predicts_target":
                "REFUTED_BY_GLZ_CONJUGATE_COLLISION",
            "observer_flow_status":
                "CONDITIONED_ON_OBSERVATION_PROTOCOL",
        },
    }


if __name__ == "__main__":
    print(json.dumps(run_all(), indent=2))
