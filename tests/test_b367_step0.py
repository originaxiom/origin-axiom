"""Locks for B367 step 0 — the exact six-pair s-matrices (banked step0_tables.json)."""

import json
import os
from fractions import Fraction as Fr

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B367_value_map")

K1 = [0, 1, 4, 5, 6, 9, 11, 14, 15, 16, 19]
K2 = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11]


def _load():
    data = json.load(open(os.path.join(HERE, "step0_tables.json")))
    out = {}
    for pair, tab in data.items():
        m1, m2 = pair.split(",")
        out[(int(m1), int(m2))] = {
            tuple(int(x) for x in k.split(",")): tuple(Fr(s) for s in v)
            for k, v in tab.items()}
    return out


TABLES = _load()
ORD = {1: 20, 2: 12, 3: 6, 4: 20}


def _s(tab, a, b):
    return tab.get((a, b), (0, 0, 0, Fr(0)))[3]


def test_flagship_and_addendum_entries_exact():
    t = TABLES[(1, 2)]
    assert t[(0, 4)] == (Fr(-1, 48), Fr(-1, 80), Fr(-1, 48), Fr(1, 48))
    for (i, j), v in {(0, 4): Fr(1, 48), (0, 7): Fr(-1, 48), (3, 1): Fr(1, 120),
                      (3, 5): Fr(-1, 480), (3, 8): Fr(-1, 160), (8, 3): Fr(-1, 160),
                      (8, 6): Fr(1, 120), (8, 10): Fr(-1, 480)}.items():
        assert _s(t, K1[i], K2[j]) == v


def test_sum_rules_all_pairs():
    for (m1, m2), tab in TABLES.items():
        for a in range(ORD[m1]):
            assert sum((_s(tab, a, b) for b in range(ORD[m2])), Fr(0)) == 0
        for b in range(ORD[m2]):
            assert sum((_s(tab, a, b) for a in range(ORD[m1])), Fr(0)) == 0


def test_rank_four_and_coxeter_odd():
    tab = TABLES[(1, 2)]
    M = [[_s(tab, a, b) for b in K2] for a in K1]
    r = 0
    for c in range(len(K2)):
        piv = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][c]
        M[r] = [v / pv for v in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [M[i][k] - f * M[r][k] for k in range(len(K2))]
        r += 1
    assert r == 4
    for a in K1:
        for b in K2:
            assert _s(tab, a, (12 - b) % 12) == -_s(tab, a, b)


def test_zeros_exact_and_value_sets():
    assert all(v[3] == 0 for v in TABLES[(1, 3)].values())
    assert all(v[3] == 0 for v in TABLES[(1, 4)].values())
    vs = lambda p: {v[3] for v in TABLES[p].values() if v[3] != 0}
    assert vs((2, 3)) == {Fr(1, 144), Fr(-1, 144), Fr(1, 288), Fr(-1, 288)}
    assert vs((2, 4)) == {Fr(s, d) for d in (120, 240, 480) for s in (1, -1)}
    assert vs((3, 4)) == {Fr(1, 48), Fr(-1, 48), Fr(1, 96), Fr(-1, 96)}


def test_exact_aggregates():
    agg = {p: sum((v[3] * v[3] for v in TABLES[p].values()), Fr(0)) for p in TABLES}
    assert agg[(1, 2)] == Fr(43, 7200)
    assert agg[(2, 3)] == Fr(1, 2304)
    assert agg[(2, 4)] == Fr(3, 3200)
    assert agg[(3, 4)] == Fr(1, 192)
    assert agg[(1, 3)] == 0 and agg[(1, 4)] == 0


def test_regenerate_smallest_pair_matches_banked():
    """OA_SLOW: rebuild pair (2,3) from scratch (exact engine) and compare."""
    if not os.environ.get("OA_SLOW"):
        import pytest
        pytest.skip("OA_SLOW not set")
    import sys
    sys.path.insert(0, HERE)
    from step0_exact_matrices import build_theta_W, matrix_order, pair_smatrix
    _, p2 = matrix_order(build_theta_W(2))
    _, p3 = matrix_order(build_theta_W(3))
    fresh = pair_smatrix(p2, p3)
    assert fresh == TABLES[(2, 3)]


def test_v3_verdict_outcome_B():
    """The pre-registered model fails on the true data; the graded diagnosis is stable."""
    import sys
    sys.path.insert(0, HERE)
    from v3_search import load_tables, records, solve_model
    tables = load_tables()
    train = [(1, 2), (2, 3), (2, 4), (3, 4)]
    assert solve_model(records(tables, train)) is None          # outcome B
    assert solve_model(records(tables, [(2, 4)])) is not None   # rank-1 pair factors
    assert solve_model(records(tables, [(2, 3)])) is not None
    assert solve_model(records(tables, [(1, 2)])) is None       # rank-4 pair fails
    assert solve_model(records(tables, [(3, 4)])) is None       # the law-breaker fails
