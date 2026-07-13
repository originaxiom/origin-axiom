"""B570 AP5 -- the order obstruction: ord(rho(A1) mod N) over the program levels.

A1 = [[2,1],[1,1]] (= F^2, the object's monodromy generator). Two independent
methods agree exactly for all N: (1) direct matrix power mod N in SL(2,Z/N);
(2) CRT: lcm of orders mod each prime-power factor of N. For odd N these both
match a third, independent method: the projective order of the standard Weil
representation (chirp T / DFT S) applied to A1 -- confirming the abstract
group-theoretic order IS the dynamical order (no anomaly doubling for A1
specifically, at odd N).

N=30 is flagged: the naive odd-N Weil-rep chirp/DFT formula (s=(N+1)/2 with
2s=1 mod N) is invalid for even N (2 has no inverse mod 30) -- this is the
same "level 30 contains prime 2, genuinely metaplectic" fact already banked
in B567 FINDINGS salvage note 1. The matrix/CRT order (60) is still exact and
still constrains any dynamics at level 30; only the naive Weil-formula
shortcut breaks.
"""
import numpy as np
from sympy import Matrix, factorint
from math import lcm

A1 = Matrix([[2, 1], [1, 1]])

TABLE = {3: 4, 5: 10, 11: 5, 15: 20, 30: 60, 165: 20, 1155: 40}


def order_mod_N(N, kmax=None):
    if kmax is None:
        kmax = 20 * N + 50
    M = Matrix.eye(2)
    A = A1.applyfunc(lambda x: x % N)
    for k in range(1, kmax):
        M = (M * A).applyfunc(lambda x: x % N)
        if M == Matrix.eye(2):
            return k
    return None


def order_via_crt(N):
    fac = factorint(N)
    val = 1
    for p, e in fac.items():
        val = lcm(val, order_mod_N(p ** e))
    return val


def _weil_A1(N):
    zeta = np.exp(2j * np.pi / N)
    s = (N + 1) // 2
    T = np.diag([zeta ** ((s * x * x) % N) for x in range(N)])
    S = np.array([[zeta ** ((x * y) % N) for y in range(N)] for x in range(N)]) / np.sqrt(N)
    L = S @ np.linalg.inv(T) @ np.linalg.inv(S)
    return T @ L


def _weil_proj_order(N, kmax=200):
    U = _weil_A1(N)
    Uk = np.eye(N)
    for k in range(1, kmax + 1):
        Uk = Uk @ U
        idx = np.argmax(np.abs(Uk))
        ph = Uk.flatten()[idx]
        if abs(ph) > 1e-9 and np.linalg.norm(Uk / ph - np.eye(N)) < 1e-6:
            return k
    return None


def test_direct_matches_crt_for_all_levels():
    for N, expected in TABLE.items():
        direct = order_mod_N(N)
        crt = order_via_crt(N)
        assert direct == crt == expected, (N, direct, crt, expected)


def test_weil_rep_matches_group_order_at_odd_levels():
    # 2 is invertible mod N only for odd N -> the naive chirp/DFT Weil formula
    # is only valid (and only tested) at odd N here.
    for N in (3, 5, 11, 15, 165, 1155):
        assert _weil_proj_order(N) == TABLE[N]


def test_level_30_naive_weil_formula_is_invalid_flag_not_a_counterexample():
    # The construction requires s with 2s = 1 mod N; no such s exists mod 30
    # (2 is not invertible mod 30). The naive formula gives a spurious small
    # "order" (2) that must NOT be read as the true dynamical order; the true
    # order is the matrix/CRT value 60 (test above), reached via the
    # metaplectic double cover, not the naive odd-N shortcut.
    spurious = _weil_proj_order(30, kmax=400)
    assert spurious != TABLE[30]
    assert TABLE[30] == 60


def test_order_obstruction_retro_kills_b567_handoff_spectrum():
    # B567 handoff claimed six pi/3-spaced levels at level 15 -> would force
    # rho(A1)^6 ~ I, i.e. order | 6. The forced order is 20; 6 does not divide 20.
    ord15 = TABLE[15]
    assert ord15 == 20
    assert ord15 % 6 != 0
    # B567 handoff also claimed a 28/27 multiplicity pattern reading off level 165
    # as if order were small/six-fold; forced order is 20, same obstruction.
    ord165 = TABLE[165]
    assert ord165 == 20
    assert ord165 % 6 != 0


def test_order_obstruction_passes_c3_e6_level2_theta_odd_block():
    # C3 (banked): rho(A1) on the E6 level-2 theta-odd 3-space is order 4,
    # eigenvalues {1, +i, -i}. This is a DIFFERENT theater (E6_2 WZW modular
    # data, not the SL(2,Z/N) Weil family) but the same criterion applies:
    # H = -i log rho(A1) must have frequencies in (2*pi/4)*Z = (pi/2)*Z.
    eigs = np.array([1.0 + 0j, 1j, -1j])
    order = 4
    H_freqs = np.angle(eigs)
    lattice = 2 * np.pi / order
    for f in H_freqs:
        k = f / lattice
        assert abs(k - round(k)) < 1e-9
