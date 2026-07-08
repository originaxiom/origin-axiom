"""B474 — lock: the commutator-trace multiset on the torus + law 1 (fast part)."""
import os
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "frontier", "B474_tier_commutator_law"))


def test_commutator_trace_multiset():
    from cross_table import commutator_traces
    ctr = commutator_traces()
    assert dict(sorted(Counter(ctr.values()).items())) == {-5: 28, -1: 32, 3: 96, 15: 84}


def test_master_theorem_gcd_factorization():
    from math import gcd
    from collections import defaultdict
    sys.path.insert(0, os.path.join(HERE, "..", "frontier", "B468_z3_adjudication"))
    from cross_table import commutator_traces
    ctr = commutator_traces()
    m = defaultdict(set)
    for (x, y), t in ctr.items():
        m[(gcd(x, 20), gcd(y, 12))].add(t)
    assert all(len(v) == 1 for v in m.values())          # kappa_q factors
    assert len(m) == 36


def test_two_character_formula():
    from cross_table import commutator_traces
    def mm(A, B, m):
        return [[(A[0][0]*B[0][0]+A[0][1]*B[1][0]) % m, (A[0][0]*B[0][1]+A[0][1]*B[1][1]) % m],
                [(A[1][0]*B[0][0]+A[1][1]*B[1][0]) % m, (A[1][0]*B[0][1]+A[1][1]*B[1][1]) % m]]
    def inv2(M, m):
        d = (M[0][0]*M[1][1]-M[0][1]*M[1][0]) % m
        di = pow(d, -1, m)
        return [[(M[1][1]*di) % m, (-M[0][1]*di) % m], [(-M[1][0]*di) % m, (M[0][0]*di) % m]]
    def matpow(M, k, m):
        R = [[1, 0], [0, 1]]
        for _ in range(k):
            R = mm(R, M, m)
        return R
    A1 = [[2, 1], [1, 1]]
    A2 = [[5, 2], [2, 1]]
    ctr = commutator_traces()
    for j in range(20):
        for l in range(12):
            a = matpow(A1, j, 5)
            b = matpow(A2, l, 5)
            c = mm(mm(a, b, 5), mm(inv2(a, 5), inv2(b, 5), 5), 5)
            closure5 = (c == [[1, 0], [0, 1]])
            eps = 3 if (j * l) % 2 == 0 else -1
            chi5 = 5 if closure5 else 1
            assert ctr[(j, l)] == eps * chi5
