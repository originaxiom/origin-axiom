"""B465 — locks: the 8-4-3 exact reproduction, the scalar law, the classical
shadow, and the mod-3 Galois split of the spectrum (p = 61 for speed)."""
import os
import sys
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "frontier", "B465_monodromy_intake"))

from exact_engine import (build, eig_mults, matmul, matpow, order_of,
                          find_root_of_unity, classical_shadow)

P = 61
N = 15


def _U_and_M1(p=P, c=1):
    _, _, W1, W2, Par = build(p, c=c)
    U = matmul(Par, W1, p)
    return U, matmul(U, W2, p), W2


def test_c1_the_843_exact():
    U, M1, _ = _U_and_M1()
    z60 = find_root_of_unity(P, 60)
    assert order_of(M1, P) == 60
    m = eig_mults(M1, P, z60)
    assert sorted(m.values(), reverse=True) == [4, 4, 4, 3]
    orders = {}
    for k, mult in m.items():
        orders[60 // gcd(k, 60)] = orders.get(60 // gcd(k, 60), 0) + mult
    assert orders == {60: 8, 15: 4, 30: 3}


def test_scalar_law_m4():
    _, M1, _ = _U_and_M1()
    M4 = matpow(M1, 4, P)
    s = M4[0][0]
    assert all(M4[i][j] % P == ((s if i == j else 0)) for i in range(N) for j in range(N))
    # spectrum is a mu_4 coset: eigenvalue k-labels differ by 15
    z60 = find_root_of_unity(P, 60)
    ks = sorted(eig_mults(M1, P, z60).keys())
    assert len(ks) == 4 and all((ks[i+1] - ks[i]) % 60 == 15 for i in range(3))


def test_classical_shadow():
    # tr(-A1 A2) = 0 mod 15 => order 4; A2^6 central => period 6 in l
    o, t = classical_shadow(1)
    assert (o, t) == (4, 0)
    o0, t0 = classical_shadow(0)
    assert (o0, t0) == (20, 12)
    for l in range(3):
        assert classical_shadow(l)[:2] == classical_shadow(l + 6)[:2]


def test_u_order_60_15_singletons():
    U, _, _ = _U_and_M1()
    z60 = find_root_of_unity(P, 60)
    assert order_of(U, P) == 60
    m = eig_mults(U, P, z60)
    assert len(m) == 15 and set(m.values()) == {1}


def test_galois_split_is_mod3_not_qr():
    z60 = find_root_of_unity(P, 60)
    specs = {}
    for c in [1, 2, 4, 7, 8, 11, 13, 14]:
        _, _, W1c, _, Parc = build(P, c=c)
        Uc = matmul(Parc, W1c, P)
        specs[c] = tuple(sorted(eig_mults(Uc, P, z60).items()))
    classes = {}
    for c, s in specs.items():
        classes.setdefault(s, []).append(c)
    parts = sorted(sorted(v) for v in classes.values())
    assert parts == [[1, 4, 7, 13], [2, 8, 11, 14]]   # mod-3 split, not QR {1,4}


def test_chat2_c_family_15_9_table_and_complementarity():
    """ADDENDUM: Chat-2's quadratic-form family — the 15/9 table splits by (c|5),
    and the full l=1 structure (mu4-coset + scalar law) persists iff (c|5)=+1."""
    import numpy as np
    sys.path.insert(0, os.path.join(HERE, "..", "frontier", "B465_monodromy_intake"))
    import c_family as CF
    for c in CF.CS:
        U = CF.U_c(c)
        assert np.max(np.abs(U @ U.conj().T - np.eye(15))) < 1e-12
        cnt = CF.spec(U)
        assert len(cnt) == CF.EXPECT[c]
        assert (c % 5 in CF.QR5) == (len(cnt) == 15)
        M4 = np.linalg.matrix_power(CF.M_c(c), 4)
        scal = np.max(np.abs(M4 - M4[0, 0] * np.eye(15))) < 1e-8
        assert scal == (c % 5 in CF.QR5)
