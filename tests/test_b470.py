"""B470 — locks: the RF0 gate, the tower word laws, and P-QB at p = 61."""
import os
import sys
from itertools import product

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "frontier", "B470_reflection_campaign"))
sys.path.insert(0, os.path.join(HERE, "..", "frontier", "B465_monodromy_intake"))
sys.path.insert(0, os.path.join(HERE, "..", "frontier", "B467_family_residue_wall"))


def _tower_words(n, A, B):
    s = {0: "b", 1: "a"}
    for k in range(2, n + 1):
        s[k] = s[k - 1] + s[k - 2]
    return {k: "".join(A if c == "a" else B for c in s[k]) for k in s}


def test_letter_tower_imbalance_is_fibonacci():
    W = _tower_words(10, "R", "L")
    F = {0: 1, 1: 1}
    for k in range(2, 11):
        F[k] = F[k - 1] + F[k - 2]
    for n in range(4, 11):
        w = W[n]
        assert w.count('L') - w.count('R') == -(w.count('R') - w.count('L'))
        assert abs(w.count('L') - w.count('R')) == F[n - 2] or abs(w.count('L') - w.count('R')) == F[n - 3]


def test_body_words_balanced_and_mirror():
    from hierarchy_verify import revswap, cyc_eq
    W = _tower_words(8, "RL", "RRLL")
    for n in range(2, 9):
        w = W[n]
        assert w.count('R') == w.count('L')
        assert cyc_eq(w, revswap(w))


def test_pqb_exact_p61():
    from exact_engine import build, matmul, find_root_of_unity
    from det_check import detmod
    p = 61
    z15 = find_root_of_unity(p, 15)
    omega = pow(z15, 5, p)
    z, i4, W1, W2, Par = build(p, c=1)
    D = [[pow(z, (j * (j - 1) // 2) % 15, p) if i == j else 0 for j in range(15)]
         for i in range(15)]
    Dinv = [[pow(D[j][j], p - 2, p) if i == j else 0 for j in range(15)] for i in range(15)]
    Wr = matmul(W1, Dinv, p)
    for alpha in (("R", "L"), ("RL", "RRLL")):
        W = _tower_words(6, *alpha)
        for n in range(2, 7):
            w = W[n]
            M = [[1 if i == j else 0 for j in range(15)] for i in range(15)]
            for ch in w:
                M = matmul(M, Wr if ch == 'R' else D, p)
            M = matmul(Par, M, p)
            pred = (-(pow(omega, (w.count('L') - w.count('R')) % 3, p))) % p
            assert detmod(M, p) == pred


def test_rf0_gate_fig8():
    import snappy
    M = snappy.Manifold("b++RL")
    assert abs(float(M.volume()) - 2.029883213) < 1e-8
    assert abs(float(M.chern_simons())) < 1e-10
