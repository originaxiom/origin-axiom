"""Locks for B380 — the Galois covariance laws (all from the banked exact tables)."""

import json
import os
from fractions import Fraction as Fr
from math import gcd

TABLES = json.load(open(os.path.join(os.path.dirname(__file__), "..",
                                     "frontier", "B367_value_map", "step0_tables.json")))
ORD = {1: 20, 2: 12, 3: 6, 4: 20}
Z = (Fr(0),) * 4


def load(pair):
    t = {}
    for k, v in TABLES[f"{pair[0]},{pair[1]}"].items():
        a, b = (int(x) for x in k.split(","))
        t[(a, b)] = tuple(Fr(x) for x in v)
    return t, ORD[pair[0]], ORD[pair[1]]


def act(c, v):
    s5 = 1 if c % 5 in (1, 4) else -1
    s3 = 1 if c % 3 == 1 else -1
    return (v[0], s5 * v[1], s3 * v[2], s5 * s3 * v[3])


def test_sigma31_all_tables():
    for pair in ((1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)):
        t, o1, o2 = load(pair)
        assert all(t.get((31 * a % o1, 31 * b % o2), Z) == t.get((a, b), Z)
                   for a in range(o1) for b in range(o2))


def test_mirror_is_tau3():
    t, o1, o2 = load((1, 2))
    assert all(t.get((a, (-b) % 12), Z) == act(11, t.get((a, b), Z))
               for a in range(20) for b in range(12))


def test_23_stabilized_by_sqrt5_fixing_halfgroup():
    t, o1, o2 = load((2, 3))
    stab = [c for c in range(60) if gcd(c, 60) == 1 and c % 5 in (1, 4)
            and all(t.get((c * a % o1, c * b % o2), Z) == act(c, t.get((a, b), Z))
                    for a in range(o1) for b in range(o2))]
    assert stab == [1, 11, 19, 29, 31, 41, 49, 59]


def test_f4_reciprocal_duality_and_equal_norm():
    t, _, _ = load((1, 2))
    rows = (1, 5, 9, 11, 15, 19)
    c1 = [t.get((a, 1), Z)[3] for a in rows]
    c5 = [t.get((a, 5), Z)[3] for a in rows]
    ratios = sorted(set(Fr(x, y) for x, y in zip(c1, c5)))
    assert ratios == [Fr(-4), Fr(-3, 2), Fr(-2, 3), Fr(-1, 4)]
    n1 = sum(x * x for x in c1)
    n5 = sum(x * x for x in c5)
    assert n1 == n5 == Fr(49, 115200)
    assert sum(x * y for x, y in zip(c1, c5)) == Fr(-13, 57600)
