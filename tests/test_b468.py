"""B468 — locks: the det decomposition (both-right-different-objects), the class
sizes, and (slow) the exact cross-table + continents."""
import os
import sys
from collections import Counter

import pytest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "frontier", "B468_z3_adjudication"))
sys.path.insert(0, os.path.join(HERE, "..", "frontier", "B465_monodromy_intake"))
sys.path.insert(0, os.path.join(HERE, "..", "frontier", "B467_family_residue_wall"))


def test_det_decomposition_exact():
    from exact_engine import build, matmul, find_root_of_unity
    from det_check import detmod
    p = 61
    z15 = find_root_of_unity(p, 15)
    omega = pow(z15, 5, p)
    z, i4, W1, W2, Par = build(p, c=1)
    N = 15
    D = [[pow(z, (j * (j - 1) // 2) % 15, p) if i == j else 0 for j in range(N)]
         for i in range(N)]
    Dinv = [[pow(D[j][j], p - 2, p) if i == j else 0 for j in range(N)] for i in range(N)]
    Wr = matmul(W1, Dinv, p)
    assert detmod(D, p) == omega                 # Chat-1 right for D alone
    assert detmod(Wr, p) == pow(omega, 2, p)     # the dropped conjugate factor
    assert detmod(W1, p) == 1 and detmod(W2, p) == 1
    assert detmod(Par, p) == p - 1               # -1


def test_class_sizes():
    cnt = Counter((j + 2 * l) % 3 for j in range(20) for l in range(12))
    assert dict(cnt) == {0: 80, 1: 80, 2: 80}


@pytest.mark.slow
def test_crosstable_uniform_dark_and_continents():
    import adjudicate as A
    pp = A.exact_tiers()
    table = Counter()
    for (x, y), z in pp.items():
        table[(A.TIER[z], (x + 2 * y) % 3)] += 1
    dark = sorted(table[('dark', c)] for c in range(3))
    assert dark == [22, 24, 24]                  # near-uniform — the 34/9/10 claim refuted
    assert sum(dark) == 70                       # the banked exact dark count
    sizes = A.part3_continents(pp)
    assert sorted(sizes) == [15] * 8             # Chat-2's continents confirmed
