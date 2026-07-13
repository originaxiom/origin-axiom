#!/usr/bin/env python3
"""Cell 1 — universal Z/11 charge transport on the 12-node observer flow."""

from __future__ import annotations

import itertools
import json
from pathlib import Path

import numpy as np
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


SYSTEMS = {
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
ALPHA = "abcde"
P = 11


def relabel_codes(codes, permutation):
    size = len(codes)
    inverse = [0] * size
    for old, new in enumerate(permutation):
        inverse[new] = old
    return tuple(
        tuple(permutation[c] for c in codes[inverse[new_domain]])
        for new_domain in range(size)
    )


def canonical_with_permutation(codes):
    candidates = (
        (relabel_codes(codes, permutation), permutation)
        for permutation in itertools.permutations(range(len(codes)))
    )
    return min(candidates, key=lambda item: item[0])


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


def derive_prefix_with_parikh(codes, target_length=100000):
    """Return canonical derived codes and old-to-new return-word Parikh map."""
    size = len(codes)
    alphabet = ALPHA[:size]
    substitution = {
        alphabet[index]: "".join(alphabet[symbol] for symbol in codes[index])
        for index in range(size)
    }

    seed = next(
        (letter for letter in substitution if substitution[letter][0] == letter),
        None,
    )
    if seed is None:
        for letter in substitution:
            image = letter
            for _ in range(3):
                image = "".join(substitution[c] for c in image)
                if image[0] == letter:
                    seed = letter
                    break
            if seed is not None:
                break
    if seed is None:
        raise RuntimeError("No periodic seed found")

    word = seed
    while len(word) < target_length:
        word = "".join(substitution[c] for c in word)

    prefix_letter = word[0]
    positions = [
        index for index, letter in enumerate(word[:50000])
        if letter == prefix_letter
    ]

    return_index = {}
    return_words = []
    for start, end in zip(positions, positions[1:]):
        return_word = word[start:end]
        if return_word not in return_index:
            return_index[return_word] = len(return_words)
            return_words.append(return_word)

    def parse(image):
        boundaries = [
            index for index, letter in enumerate(image)
            if letter == prefix_letter
        ] + [len(image)]
        return tuple(
            return_index[image[start:end]]
            for start, end in zip(boundaries, boundaries[1:])
        )

    raw_codes = tuple(
        parse("".join(substitution[c] for c in return_word))
        for return_word in return_words
    )

    canonical, permutation = canonical_with_permutation(raw_codes)
    inverse = [0] * len(permutation)
    for old, new in enumerate(permutation):
        inverse[new] = old

    raw_parikh = sp.Matrix([
        [return_word.count(alphabet[row]) for return_word in return_words]
        for row in range(size)
    ])
    canonical_parikh = raw_parikh[:, inverse]
    return canonical, canonical_parikh


def left_nullspace_mod_p(matrix, prime=P):
    """Basis of row vectors x with x*matrix = 0 over F_p."""
    array = np.array(matrix.T.tolist(), dtype=int) % prime
    rows, columns = array.shape
    pivot_row = 0
    pivots = []

    for column in range(columns):
        pivot = next(
            (
                row for row in range(pivot_row, rows)
                if array[row, column] % prime
            ),
            None,
        )
        if pivot is None:
            continue
        array[[pivot_row, pivot]] = array[[pivot, pivot_row]]
        inverse = pow(int(array[pivot_row, column]), -1, prime)
        array[pivot_row] = (array[pivot_row] * inverse) % prime
        for row in range(rows):
            if row != pivot_row and array[row, column] % prime:
                array[row] = (
                    array[row]
                    - array[row, column] * array[pivot_row]
                ) % prime
        pivots.append(column)
        pivot_row += 1

    free = [column for column in range(columns) if column not in pivots]
    basis = []
    for free_column in free:
        vector = np.zeros(columns, dtype=int)
        vector[free_column] = 1
        for row, pivot_column in enumerate(pivots):
            vector[pivot_column] = (-array[row, free_column]) % prime
        basis.append(vector)
    return basis


def normalize(vector, prime=P):
    vector = np.array(vector, dtype=int) % prime
    last_nonzero = max(
        index for index, value in enumerate(vector)
        if value % prime
    )
    inverse = pow(int(vector[last_nonzero]), -1, prime)
    return (vector * inverse) % prime


def build_flow():
    canonical_to_name = {
        canonical_codes(codes): name
        for name, codes in SYSTEMS.items()
    }
    codes_by_name = {
        name: canonical_codes(codes)
        for name, codes in SYSTEMS.items()
    }

    flow = {}
    edge_parikh = {}
    frontier = []

    for name, codes in list(codes_by_name.items()):
        target_codes, parikh = derive_prefix_with_parikh(codes)
        if target_codes in canonical_to_name:
            target = canonical_to_name[target_codes]
        else:
            target = f"NEW_{len(frontier)}"
            canonical_to_name[target_codes] = target
            codes_by_name[target] = target_codes
            frontier.append((target, target_codes))
        flow[name] = target
        edge_parikh[name] = parikh

    while frontier:
        name, codes = frontier.pop()
        target_codes, parikh = derive_prefix_with_parikh(codes)
        if target_codes not in canonical_to_name:
            target = f"NEW_{len(canonical_to_name)}"
            canonical_to_name[target_codes] = target
            codes_by_name[target] = target_codes
            frontier.append((target, target_codes))
        flow[name] = canonical_to_name[target_codes]
        edge_parikh[name] = parikh

    return codes_by_name, flow, edge_parikh


def run_all():
    codes_by_name, flow, edge_parikh = build_flow()

    node_records = []
    charges = {}
    for name in sorted(codes_by_name):
        matrix = incidence(codes_by_name[name])
        smith = smith_normal_form(sp.eye(matrix.rows) - matrix, domain=ZZ)
        diagonal = [
            abs(int(smith[index, index]))
            for index in range(min(smith.shape))
        ]
        basis = left_nullspace_mod_p(matrix - sp.eye(matrix.rows))
        if len(basis) != 1:
            raise AssertionError(
                f"{name}: expected unique mod-11 charge, found {len(basis)}"
            )
        charge = normalize(basis[0])
        charges[name] = charge

        node_records.append({
            "node": name,
            "alphabet_size": matrix.rows,
            "det_I_minus_A": int((sp.eye(matrix.rows) - matrix).det()),
            "smith_diagonal": diagonal,
            "charge_dimension_mod_11": len(basis),
            "normalized_charge": charge.tolist(),
        })

    edge_records = []
    for source in sorted(flow):
        target = flow[source]
        source_matrix = incidence(codes_by_name[source])
        target_matrix = incidence(codes_by_name[target])
        parikh = edge_parikh[source]

        if source_matrix * parikh != parikh * target_matrix:
            raise AssertionError(f"{source}->{target}: intertwining failed")

        transported = (
            charges[source]
            @ (np.array(parikh.tolist(), dtype=int) % P)
        ) % P
        target_charge = charges[target]

        scalar = next(
            (
                value for value in range(1, P)
                if np.array_equal(
                    transported,
                    (value * target_charge) % P,
                )
            ),
            None,
        )
        if scalar is None:
            raise AssertionError(
                f"{source}->{target}: charge was not transported"
            )

        edge_records.append({
            "source": source,
            "target": target,
            "source_charge": charges[source].tolist(),
            "transported_charge": transported.tolist(),
            "target_charge": target_charge.tolist(),
            "edge_scalar_mod_11": scalar,
            "intertwining_verified": True,
        })

    two_cycle = [
        record for record in edge_records
        if (record["source"], record["target"])
        in {("NEW_2", "NEW_10"), ("NEW_10", "NEW_2")}
    ]
    if len(two_cycle) != 2:
        raise AssertionError("Expected the unique two-cycle")
    holonomy = 1
    for record in two_cycle:
        holonomy = (
            holonomy * record["edge_scalar_mod_11"]
        ) % P

    base_charge = [1, 3, 6, 7]
    base_matrix = incidence(codes_by_name["S_a"])
    assert np.array_equal(
        (
            np.array(base_charge, dtype=int)
            @ np.array(base_matrix.tolist(), dtype=int)
        ) % P,
        np.array(base_charge, dtype=int) % P,
    )

    return {
        "node_records": node_records,
        "edge_records": edge_records,
        "flow": flow,
        "base_charge_abAB": base_charge,
        "two_cycle_scalars": [
            record["edge_scalar_mod_11"] for record in two_cycle
        ],
        "two_cycle_holonomy_mod_11": holonomy,
        "classification": {
            "base_charge": "PROVED_EXACTLY",
            "universal_12_node_torsion": "COMPUTED_EXACTLY",
            "edge_transport": "COMPUTED_EXACTLY",
            "nontrivial_clock_charge_holonomy": (
                "REFUTED" if holonomy == 1 else "OBSERVED"
            ),
        },
    }


if __name__ == "__main__":
    print(json.dumps(run_all(), indent=2))
