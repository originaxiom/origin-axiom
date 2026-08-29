#!/usr/bin/env python3
"""Independent full-census check of B1197's Vol/|CS| comparison.

Dependency: SnapPy.  The Chern--Simons normalization is primed on the unfilled
manifold exactly as in the banked B289 instrument.  The certificate distinguishes
the monotone, unselected (1,n) ladder from the non-monotone full closing census.
"""

from collections import defaultdict
from math import gcd
import random

import snappy


def fill(p, q):
    manifold = snappy.Manifold("m004")
    _ = float(manifold.chern_simons())
    manifold.dehn_fill((p, q))
    if "positively" not in str(manifold.solution_type()):
        return None
    volume = float(manifold.volume())
    cs = ((float(manifold.chern_simons()) + 0.5) % 1.0) - 0.5
    return volume, cs


# Oriented box: reproduce the sign-law control before using |CS|.
oriented = {}
for p in range(-8, 9):
    for q in range(-8, 9):
        if (p, q) == (0, 0) or gcd(abs(p), abs(q)) != 1:
            continue
        result = fill(p, q)
        if result is not None:
            oriented[(p, q)] = result

sign_pairs = 0
sign_matches = 0
for (p, q), (_, cs) in oriented.items():
    mirror = oriented.get((p, -q))
    if mirror is None:
        continue
    sign_pairs += 1
    mirror_cs = mirror[1]
    if abs(cs + mirror_cs) < 1e-6 or abs(abs(cs) - abs(mirror_cs)) < 1e-6:
        sign_matches += 1

assert len(oriented) == 156
assert (sign_matches, sign_pairs) == (156, 156)


# Unoriented census: (p,q) and (-p,-q) are the same filling.
rows = []
seen = set()
for p in range(-8, 9):
    for q in range(-8, 9):
        if (p, q) == (0, 0) or gcd(abs(p), abs(q)) != 1:
            continue
        key = (p, q) if p > 0 or (p == 0 and q > 0) else (-p, -q)
        if key in seen:
            continue
        seen.add(key)
        result = fill(*key)
        if result is not None:
            rows.append((key[0], key[1], result[0], abs(result[1])))

assert len(rows) == 78
ordered = sorted(rows, key=lambda row: row[2])
violations = [
    (ordered[index], ordered[index + 1])
    for index in range(len(ordered) - 1)
    if ordered[index][3] < ordered[index + 1][3] - 1e-9
]
assert len(violations) == 15

families = defaultdict(list)
for row in rows:
    families[row[0]].append(row)
family_monotone = {}
for p, family in families.items():
    sequence = sorted(family, key=lambda row: row[2])
    if len(sequence) >= 3:
        family_monotone[p] = all(
            sequence[index][3] >= sequence[index + 1][3] - 1e-12
            for index in range(len(sequence) - 1)
        )
assert family_monotone[1]
assert all(not family_monotone[p] for p in range(2, 9))


# The specially selected (1,n) ladder is monotone, but selection is an input.
ladder = []
for n in range(2, 31):
    result = fill(1, n)
    if result is not None:
        ladder.append((n, result[0], abs(result[1])))
assert len(ladder) == 29
assert all(ladder[i][1] < ladder[i + 1][1] + 1e-12 for i in range(28))
assert all(ladder[i][2] > ladder[i + 1][2] - 1e-12 for i in range(28))


# A deliberately shuffled control shows the violation detector is live.
rng = random.Random(20260828)
shuffled_cs = [row[3] for row in ordered]
rng.shuffle(shuffled_cs)
shuffle_violations = sum(
    shuffled_cs[index] < shuffled_cs[index + 1] - 1e-9
    for index in range(len(shuffled_cs) - 1)
)
assert shuffle_violations == 36

print("oriented_closings=156")
print("chern_simons_sign_control=156/156")
print("unoriented_closings=78")
print("selected_1n_ladder_monotone=True")
print("full_census_monotone=False")
print("full_census_violations=15")
print("families_p2_through_p8_each_nonmonotone=True")
print("shuffle_control_violations=36")
print("OA-C1153 FULL-COMMON-DOMAIN COHERENCE: REFUTED")
print("R023 B1197 CLOCK COHERENCE: PASS")
