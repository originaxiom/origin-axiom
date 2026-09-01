#!/usr/bin/env python3
"""R039: the m004 A4 quotient has exactly two 2T spin lifts.

This is an exhaustive calculation in SL(2,3) and its central quotient A4.
It proves a finite Spin(3)->SO(3) lift-torsor statement, not an identification
with tangent or four-dimensional Lorentz spin.
"""

from __future__ import annotations

from collections import defaultdict
from itertools import product
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
I = (1, 0, 0, 1)
Z = (2, 0, 0, 2)


def det(x):
    return (x[0] * x[3] - x[1] * x[2]) % 3


Q = tuple(x for x in product(range(3), repeat=4) if det(x) == 1)


def mul(x, y):
    return (
        (x[0] * y[0] + x[1] * y[2]) % 3,
        (x[0] * y[1] + x[1] * y[3]) % 3,
        (x[2] * y[0] + x[3] * y[2]) % 3,
        (x[2] * y[1] + x[3] * y[3]) % 3,
    )


def inv(x):
    return (x[3] % 3, -x[1] % 3, -x[2] % 3, x[0] % 3)


def generated(generators, identity, multiply, inverse):
    seen, todo = {identity}, [identity]
    while todo:
        current = todo.pop()
        for generator in generators:
            for step in (generator, inverse(generator)):
                value = multiply(current, step)
                if value not in seen:
                    seen.add(value)
                    todo.append(value)
    return seen


def evaluate(word, assignment, identity, multiply, inverse):
    answer = identity
    for letter in word:
        value = assignment[letter.lower()]
        answer = multiply(answer, value if letter.islower() else inverse(value))
    return answer


def q_surjections(relator):
    return tuple((a, b) for a, b in product(Q, repeat=2)
                 if evaluate(relator, {"a": a, "b": b}, I, mul, inv) == I
                 and len(generated((a, b), I, mul, inv)) == 24)


def canonical_coset(x):
    return min(x, mul(Z, x))


A4 = tuple(sorted({canonical_coset(x) for x in Q}))
A4_I = canonical_coset(I)


def a4_mul(x, y):
    return canonical_coset(mul(x, y))


def a4_inv(x):
    return canonical_coset(inv(x))


def a4_surjections(relator):
    return tuple((a, b) for a, b in product(A4, repeat=2)
                 if evaluate(relator, {"a": a, "b": b},
                             A4_I, a4_mul, a4_inv) == A4_I
                 and len(generated((a, b), A4_I, a4_mul, a4_inv)) == 12)


def build_automorphisms():
    seed = next((a, b) for a, b in product(Q, repeat=2)
                if len(generated((a, b), I, mul, inv)) == 24)
    letters = (seed[0], seed[1], inv(seed[0]), inv(seed[1]))
    words = {I: ()}
    todo = [I]
    while todo:
        current = todo.pop(0)
        for index, generator in enumerate(letters):
            value = mul(current, generator)
            if value not in words:
                words[value] = words[current] + (index,)
                todo.append(value)
    answer = []
    for left, right in product(Q, repeat=2):
        if len(generated((left, right), I, mul, inv)) != 24:
            continue
        images = (left, right, inv(left), inv(right))
        action = {}
        for element, word in words.items():
            value = I
            for index in word:
                value = mul(value, images[index])
            action[element] = value
        if (len(set(action.values())) == 24
                and all(action[mul(x, y)] == mul(action[x], action[y])
                        for x in Q for y in Q)):
            answer.append(action)
    assert len(answer) == 24
    return answer


def project(row):
    return tuple(canonical_coset(value) for value in row)


def restrict_q(row):
    a, b = row
    u, _v, w = mul(b, inv(a)), mul(a, a), mul(a, b)
    return (inv(w), mul(w, inv(u)))


def restrict_a4(row):
    a, b = row
    u, w = a4_mul(b, a4_inv(a)), a4_mul(a, b)
    return (a4_inv(w), a4_mul(w, a4_inv(u)))


def main():
    sources = json.loads((HERE / "source_snapshot.json").read_text())
    assert sources["schema"] == "oa-r039-a4-2t-lift-torsor-sources-v1"
    assert sources["source_commit"] == "f024f0f8c47ad13928c4feaeb0c255d84b301fed"
    assert {key: row["git_blob_sha1"] for key, row in sources["sources"].items()} == {
        "r037_certificate": "94c689bcd67c1a2c623a50298aa97da20c4a481a",
        "r037_memo": "7ea2a8e7589a978a4dc95e9e5f2383fbe2ff9c06",
        "r034_memo": "2369294edb50468d5b3bd40d6ea2e790bb0a629f",
        "b1141_findings": "c8c4f67f9705a16fdc5e6d675c4281d173f5a87e",
    }
    assert len(Q) == 24 and len(A4) == 12
    rel_g = "aabbAB"       # m000
    rel_m = "aaabABBAb"    # m004
    q_g, q_m = q_surjections(rel_g), q_surjections(rel_m)
    a_g, a_m = a4_surjections(rel_g), a4_surjections(rel_m)
    assert (len(q_g), len(q_m), len(a_g), len(a_m)) == (48, 48, 24, 24)

    # Every A4 map has exactly two 2T lifts, exchanged by the unique nonzero
    # central character.  No A4 quotient is missed.
    lifts_g, lifts_m = defaultdict(list), defaultdict(list)
    for row in q_g:
        lifts_g[project(row)].append(row)
    for row in q_m:
        lifts_m[project(row)].append(row)
    assert set(lifts_g) == set(a_g) and set(lifts_m) == set(a_m)
    assert {len(rows) for rows in lifts_g.values()} == {2}
    assert {len(rows) for rows in lifts_m.values()} == {2}

    # The A4 quotient passes through the orientation cover bijectively.
    restricted_a4 = {restrict_a4(row) for row in a_g}
    assert len(restricted_a4) == 24 and restricted_a4 == set(a_m)
    assert all(project(restrict_q(row)) == restrict_a4(project(row))
               for row in q_g)

    # The two parent 2T lifts restrict to the same cover lift because their
    # difference is the orientation character, which vanishes on the cover.
    restricted_q = {restrict_q(row) for row in q_g}
    assert len(restricted_q) == 24
    for rows in lifts_g.values():
        assert len({restrict_q(row) for row in rows}) == 1

    # Over each cover A4 map, exactly one 2T lift extends and the other is the
    # nonzero H^1(m004;C2) twist.
    for base, rows in lifts_m.items():
        assert len(set(rows) & restricted_q) == 1, base

    # Aut(2T) descends faithfully to all 24 automorphisms of A4, and the 24
    # A4 surjections form one quotient class on each manifold.
    aut_q = build_automorphisms()
    aut_a4 = []
    for action in aut_q:
        induced = {element: canonical_coset(action[element]) for element in A4}
        if induced not in aut_a4:
            aut_a4.append(induced)
    assert len(aut_a4) == 24
    orbit_g = {min(tuple(action[value] for value in row)
                   for action in aut_a4) for row in a_g}
    orbit_m = {min(tuple(action[value] for value in row)
                   for action in aut_a4) for row in a_m}
    assert len(orbit_g) == len(orbit_m) == 1

    print("PASS m000 and m004 each have one A4 quotient class: 24 surjections")
    print("PASS every A4 surjection has exactly two lifts through 2T=Spin(3) preimage")
    print("RESULT A4 restriction m000->m004 is bijective on all 24 maps")
    print("RESULT exactly one of each m004 map's two 2T lifts extends over m000")
    print("RESULT the parent H^1 bit restricts to zero; the cover's second lift is nonextendable")
    print("SCOPE finite Spin(3)->SO(3) representation torsor only; no tangent, 4d Lorentz or beat-chi identification")


if __name__ == "__main__":
    main()
