#!/usr/bin/env python3
"""R037: exact restriction of m000 -> 2T quotients to the m004 cover.

All computations use only 2x2 matrices over F_3 and fixed presentations pinned
in source_snapshot.json.  No SnapPy or external algebra package is required.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from hashlib import sha256
from itertools import product
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
I = (1, 0, 0, 1)
Z = (2, 0, 0, 2)


def det(x):
    return (x[0] * x[3] - x[1] * x[2]) % 3


SL23 = [x for x in product(range(3), repeat=4) if det(x) == 1]


def mul(x, y):
    return (
        (x[0] * y[0] + x[1] * y[2]) % 3,
        (x[0] * y[1] + x[1] * y[3]) % 3,
        (x[2] * y[0] + x[3] * y[2]) % 3,
        (x[2] * y[1] + x[3] * y[3]) % 3,
    )


def inv(x):
    return (x[3] % 3, -x[1] % 3, -x[2] % 3, x[0] % 3)


def evaluate(word, assignment):
    answer = I
    for letter in word:
        value = assignment[letter.lower()]
        answer = mul(answer, value if letter.islower() else inv(value))
    return answer


def generated(generators):
    seen, todo = {I}, [I]
    while todo:
        current = todo.pop()
        for generator in generators:
            for step in (generator, inv(generator)):
                value = mul(current, step)
                if value not in seen:
                    seen.add(value)
                    todo.append(value)
    return seen


def commutator(x, y):
    return mul(mul(mul(x, y), inv(x)), inv(y))


def is_surjection(relators, assignment):
    return (all(evaluate(relator, assignment) == I for relator in relators)
            and len(generated(tuple(assignment.values()))) == 24)


def stable_hash(values):
    payload = json.dumps(sorted(values), separators=(",", ":"))
    return sha256(payload.encode()).hexdigest()


def build_automorphisms():
    """Exhaust Aut(SL(2,3)) from images of one generating pair."""

    seed = next((a, b) for a, b in product(SL23, repeat=2)
                if len(generated((a, b))) == 24)
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
    assert len(words) == 24

    automorphisms = []
    for left, right in product(SL23, repeat=2):
        if len(generated((left, right))) != 24:
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
                        for x in SL23 for y in SL23)):
            automorphisms.append(action)
    assert len(automorphisms) == 24
    return automorphisms


def orbit_key(row, automorphisms):
    return min(tuple(action[value] for value in row)
               for action in automorphisms)


def main():
    sources = json.loads((HERE / "source_snapshot.json").read_text())
    assert sources["schema"] == "oa-r037-a6-2t-restriction-sources-v1"
    assert sources["source_commit"] == "a5138424e5712d11aad69d75fc921e3dbccae7fb"
    assert {key: row["git_blob_sha1"] for key, row in sources["sources"].items()} == {
        "b1234_findings": "51ce96cc1f4a24440cfafce772a1707b126a7487",
        "b1234_code": "c5a1f23c4ba6005a0c5b16a08c2384de85c2ea1d",
        "b1234_results": "48a958ac50c81e29994859244a21ba942975ee56",
        "b1208_findings": "861ce76d732dc579bbc48e8c358c6d465ca5d2df",
        "identification_ledger": "859f1b85f0a49679937e9599f15a64f133afc3f6",
    }

    # Exact target-group invariants.  In particular, Q_ab=C3, so Q has no
    # quotient of order two and restriction to an index-two subgroup stays onto.
    assert len(SL23) == 24
    center = {x for x in SL23 if all(mul(x, y) == mul(y, x) for y in SL23)}
    derived = generated({commutator(x, y) for x in SL23 for y in SL23})
    assert center == {I, Z}
    assert len(derived) == 8 and len(SL23) // len(derived) == 3
    automorphisms = build_automorphisms()

    # G=m000.  Its unique nonzero mod-two character has w(a)=w(b)=1.
    # Reidemeister--Schreier for H=ker(w) gives u=ba^-1,v=a^2,w=ab.
    # Tietze conversion to the standard m004 presentation is
    # c=w^-1, d=wu^-1 and inversely u=d^-1c^-1,v=dc,w=c^-1.
    rel_g = ("aabbAB",)
    rel_h = ("vuwVU", "vwuW")
    rel_m = ("aaabABBAb",)
    central_characters = []
    for c_value, d_value in product(range(2), repeat=2):
        parity = sum(c_value if letter.lower() == "a" else d_value
                     for letter in rel_m[0]) % 2
        if parity == 0:
            central_characters.append((c_value, d_value))
    assert central_characters == [(0, 0), (0, 1)]
    surj_g = [(a, b) for a, b in product(SL23, repeat=2)
              if is_surjection(rel_g, {"a": a, "b": b})]
    surj_h = [(u, v, w) for u, v, w in product(SL23, repeat=3)
              if is_surjection(rel_h, {"u": u, "v": v, "w": w})]
    surj_m = [(c, d) for c, d in product(SL23, repeat=2)
              if is_surjection(rel_m, {"a": c, "b": d})]
    assert len(surj_g) == len(surj_h) == len(surj_m) == 48

    def restrict_h(row):
        a, b = row
        return (mul(b, inv(a)), mul(a, a), mul(a, b))

    def h_to_m(row):
        u, _v, w = row
        return (inv(w), mul(w, inv(u)))

    def m_to_h(row):
        c, d = row
        return (mul(inv(d), inv(c)), mul(d, c), inv(c))

    assert {h_to_m(row) for row in surj_h} == set(surj_m)
    assert all(m_to_h(h_to_m(row)) == row for row in surj_h)
    restricted = [h_to_m(restrict_h(row)) for row in surj_g]
    assert all(row in surj_m for row in restricted)

    fibres = defaultdict(list)
    for source, target in zip(surj_g, restricted):
        fibres[target].append(source)
    assert len(fibres) == 24
    assert Counter(map(len, fibres.values())) == {2: 24}

    # The two extensions are exactly the central orientation twists.
    def source_twist(row):
        return tuple(mul(Z, value) for value in row)

    assert all(set(rows) == {rows[0], source_twist(rows[0])}
               for rows in fibres.values())

    # Aut(Q) acts freely on surjections.  The cover has two quotient classes;
    # the restriction image is exactly one of them.
    orbits_g = defaultdict(list)
    orbits_m = defaultdict(list)
    for row in surj_g:
        orbits_g[orbit_key(row, automorphisms)].append(row)
    for row in surj_m:
        orbits_m[orbit_key(row, automorphisms)].append(row)
    assert sorted(map(len, orbits_g.values())) == [24, 24]
    assert sorted(map(len, orbits_m.values())) == [24, 24]
    image = set(restricted)
    complement = set(surj_m) - image
    assert len({orbit_key(row, automorphisms) for row in image}) == 1
    assert len({orbit_key(row, automorphisms) for row in complement}) == 1

    # The unique nonzero central H^1 twist on m004 exchanges the two orbits.
    # Its abelianization mod two kills c and detects d for rel_m.
    def cover_twist(row):
        c, d = row
        return (c, mul(Z, d))

    assert {cover_twist(row) for row in image} == complement
    for source_orbit in orbits_g.values():
        assert {h_to_m(restrict_h(row)) for row in source_orbit} == image

    assert stable_hash(surj_g) == "3336ac5610b96ab1d8887d940d46bc69f08a144a3b61e2476f16dcf4edd3bbf7"
    assert stable_hash(surj_m) == "3e1c2e18ae00a80ceb2e0f1b0afc609b6c4f77df1a52b7511997bf5a60792179"
    assert stable_hash(image) == "6294aad870d95283f8a2d5cb2daa42ae650c35a983e89816f71f81e14242f7de"

    print("PASS 2T has order 24, center C2, abelianization C3 and Aut order 24")
    print("PASS m000 and m004 each have 48 surjections = two Aut(2T) orbits")
    print("PASS every m000 surjection restricts surjectively to the orientation subgroup")
    print("RESULT restriction has 24 distinct images with fibre size two")
    print("RESULT exactly one of m004's two 2T quotient classes extends over m000")
    print("RESULT the nonextendable class is the unique central H^1 twist of the extendable class")
    print("SCOPE abstract finite quotient only; no ALE, physical E6, spin or chirality identification")


if __name__ == "__main__":
    main()
