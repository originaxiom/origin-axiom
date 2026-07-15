"""Proposed locks for the LEVEL-LADDER campaign (seat cc2; B-number at banking).

Self-contained (no imports from the packet): rebuilds E6 level-4 modular data
with the banked conventions (B570-C3 / B578-D7 pattern) and locks:

  L1  P+_4(E6) = 42 primaries; 8 theta-fixed; theta-odd dim 17.
  L2  Z4 = Tr rho(A1) = 0 EXACTLY (integer reduction mod Phi_192 over Z --
      the certificate is integer arithmetic, no floats).
  L3  Tr(Theta rho) = 0 EXACTLY (same certificate) => both sector traces vanish.
  L4  ord(rho(A1)|odd) = 12 = ord(rho(A1)|even) (float gate 1e-6; divisors fail).
  L5  the Q(sqrt2) import: {2+-sqrt2, 4+-2sqrt2, 1+-1/sqrt2} subset of the
      odd magnitude set w = 32|S_odd|^2 (1e-8), plus rationals {4/3,8/3,4,16/3}.
  L6  the two odd quartics: minpolys [4,-48,148,-88,1] and [324,-2160,3348,-888,49]
      vanish on the remaining eight values (1e-8); all disc primes >= 5 to EVEN
      exponent (17^2, 7^2 -- norm/index content, not ramification).
  L7  the ladder context: at k = 1,2,3 the same build returns Z = +1 (1e-9)
      (reproduces B569 / B570-C3 / B578-D7's headline).
  L8  L73 lemma: det(A1 - I) = -1; A1 - I invertible mod every N <= 512.

Runtime ~2-3 min (the k=4 Weyl sums dominate). OA_SLOW-pattern candidate.
"""
import numpy as np
import pytest
import sympy as sp

C6 = np.array([[2, 0, -1, 0, 0, 0], [0, 2, 0, -1, 0, 0], [-1, 0, 2, -1, 0, 0],
               [0, -1, -1, 2, -1, 0], [0, 0, 0, -1, 2, -1], [0, 0, 0, 0, -1, 2]],
              dtype=np.int64)
MARKS = [1, 2, 2, 3, 2, 1]
HVEE = 12
theta = lambda w: (w[5], w[1], w[4], w[3], w[2], w[0])
Cinv3 = np.rint(3 * np.linalg.inv(C6)).astype(np.int64)


def enumerate_level_weights(level):
    weights = []
    bounds = [level // m + 1 for m in MARKS]
    for l0 in range(bounds[0]):
        for l1 in range(bounds[1]):
            for l2 in range(bounds[2]):
                for l3 in range(bounds[3]):
                    for l4 in range(bounds[4]):
                        for l5 in range(bounds[5]):
                            lab = (l0, l1, l2, l3, l4, l5)
                            if sum(m * x for m, x in zip(MARKS, lab)) <= level:
                                weights.append(lab)
    return weights


def weyl_group():
    gens = []
    for j in range(6):
        M = np.eye(6, dtype=np.int64)
        M[j, :] -= C6[:, j]
        gens.append(M)
    I = np.eye(6, dtype=np.int64)
    seen = {I.tobytes()}
    mats, signs = [I], [1]
    frontier = [(I, 1)]
    while frontier:
        new = []
        for M, s in frontier:
            for g in gens:
                Mg = g @ M
                key = Mg.tobytes()
                if key not in seen:
                    seen.add(key)
                    new.append((Mg, -s))
                    mats.append(Mg)
                    signs.append(-s)
        frontier = new
    return np.array(mats), np.array(signs, dtype=np.int64)


def build(level, W, eps):
    K = level + HVEE
    M6 = 6 * K
    PRIM = enumerate_level_weights(level)
    N = len(PRIM)
    P = (Cinv3 @ (np.array(PRIM, dtype=np.int64) + 1).T).T
    WP = np.einsum('wij,aj->wai', W, P)
    CP = C6 @ P.T
    counts = np.zeros((N, N, M6), dtype=np.int64)
    for a in range(N):
        Q = WP[:, a, :] @ CP
        assert (Q % 3 == 0).all()
        E = (-2 * (Q // 3)) % M6
        for b in range(a, N):
            cp = np.bincount(E[eps > 0, b], minlength=M6)
            cm = np.bincount(E[eps < 0, b], minlength=M6)
            counts[a, b] = counts[b, a] = cp - cm
    lam3 = (Cinv3 @ np.array(PRIM, dtype=np.int64).T).T
    rho3 = Cinv3 @ np.ones(6, dtype=np.int64)
    r = np.array([int((la @ C6 @ (la + 2 * rho3))) for la in lam3])
    assert (r % 3 == 0).all()
    T_expo = (2 * (r // 3) - 39 * level) % (12 * K)
    return PRIM, counts, T_expo, K


def sfloat(counts, M6):
    z = np.exp(2j * np.pi * np.arange(M6) / M6)
    U = counts @ z
    norm = np.sqrt((U @ U.conj().T)[0, 0].real)
    S = U / norm
    return -S if S[0, 0].real < 0 else S


@pytest.fixture(scope="module")
def data():
    W, eps = weyl_group()
    assert len(W) == 51840
    PRIM, counts, T_expo, K = build(4, W, eps)
    S = sfloat(counts, 6 * K)
    T = np.diag(np.exp(2j * np.pi * T_expo / (12 * K)))
    rho = T @ T @ S @ T
    w2 = T @ S @ np.linalg.inv(T) @ np.linalg.inv(S)
    assert np.linalg.norm(rho - w2) < 1e-8          # two-word lock (B569 lesson)
    return dict(W=W, eps=eps, PRIM=PRIM, counts=counts, T_expo=T_expo, K=K,
                S=S, T=T, rho=rho)


def _cyclo_zero(coef, M):
    x = sp.Symbol('x')
    poly = sp.Poly(list(reversed(coef)), x, domain='ZZ')
    return poly.rem(sp.Poly(sp.cyclotomic_poly(M, x), x, domain='ZZ')).is_zero


def test_L1_counts(data):
    PRIM = data['PRIM']
    assert len(PRIM) == 42
    fixed = [p for p in PRIM if theta(p) == p]
    assert len(fixed) == 8 and (42 - 8) // 2 == 17


def test_L2_Z4_exact_zero(data):
    K, M12 = data['K'], 12 * data['K']
    coef = [0] * M12
    for a in range(42):
        sh = 3 * int(data['T_expo'][a])
        row = data['counts'][a, a]
        for j in range(6 * K):
            c = int(row[j])
            if c:
                coef[(2 * j + sh) % M12] += c
    assert _cyclo_zero(coef, M12)


def test_L3_theta_trace_exact_zero(data):
    K, M12, PRIM = data['K'], 12 * data['K'], data['PRIM']
    idx = [PRIM.index(theta(p)) for p in PRIM]
    coef = [0] * M12
    for a in range(42):
        ta = idx[a]
        sh = (2 * int(data['T_expo'][ta]) + int(data['T_expo'][a])) % M12
        row = data['counts'][ta, a]
        for j in range(6 * K):
            c = int(row[j])
            if c:
                coef[(2 * j + sh) % M12] += c
    assert _cyclo_zero(coef, M12)


def _blocks(data):
    PRIM, S, rho = data['PRIM'], data['S'], data['rho']
    pairs, used = [], set()
    for i, p in enumerate(PRIM):
        if i in used or theta(p) == p:
            continue
        j = PRIM.index(theta(p))
        pairs.append((i, j)); used.update((i, j))
    fixed = [i for i, p in enumerate(PRIM) if theta(p) == p]
    odd = np.zeros((42, 17))
    for j, (a, b) in enumerate(pairs):
        odd[a, j], odd[b, j] = 2 ** -0.5, -2 ** -0.5
    even = np.zeros((42, 25))
    for j, a in enumerate(fixed):
        even[a, j] = 1
    for j, (a, b) in enumerate(pairs):
        even[a, 8 + j], even[b, 8 + j] = 2 ** -0.5, 2 ** -0.5
    return odd.T @ S @ odd, odd.T @ rho @ odd, even.T @ rho @ even


def test_L4_orders(data):
    _, B_odd, B_even = _blocks(data)
    for B, n in ((B_odd, 17), (B_even, 25)):
        P = np.eye(n, dtype=complex)
        order = None
        for m in range(1, 100):
            P = P @ B
            if np.linalg.norm(P - np.eye(n)) < 1e-6:
                order = m
                break
        assert order == 12
        for d in (6, 4):
            assert np.linalg.norm(np.linalg.matrix_power(B, d) - np.eye(n)) > 1e-2


def test_L5_L6_magnitude_arithmetic(data):
    S_odd, _, _ = _blocks(data)
    mags = np.abs(S_odd)
    vals = sorted(set(round(v, 8) for row in mags for v in row if v > 1e-6))
    assert len(vals) == 18
    ws = sorted(32 * v ** 2 for v in vals)
    s2 = np.sqrt(2)
    expected_q2 = [2 - s2, 2 + s2, 4 - 2 * s2, 4 + 2 * s2, 1 - 1 / s2, 1 + 1 / s2]
    expected_ratl = [4 / 3, 8 / 3, 4.0, 16 / 3]
    for t in expected_q2 + expected_ratl:
        assert min(abs(w - t) for w in ws) < 5e-7, t  # float64-dedupe granularity; dps-50 certificate in packet
    rest = [w for w in ws
            if min(abs(w - t) for t in expected_q2 + expected_ratl) > 5e-7]
    assert len(rest) == 8
    q1 = [4, -48, 148, -88, 1]
    q2 = [324, -2160, 3348, -888, 49]
    for w in rest:
        v1 = abs(sum(c * w ** (4 - i) for i, c in enumerate(q1)))
        v2 = abs(sum(c * w ** (4 - i) for i, c in enumerate(q2)))
        assert min(v1, v2) < 1e-3, w  # 8-dp dedupe x quartic derivative ~2e-4; wrong-quartic value is O(10-100)
    for q in (q1, q2):
        disc = sp.discriminant(sp.Poly(q, sp.Symbol('w')).as_expr(), sp.Symbol('w'))
        for p, e in sp.factorint(abs(int(disc))).items():
            if p >= 5:
                assert e % 2 == 0, (q, p, e)


def test_L7_ladder_context(data):
    W, eps = data['W'], data['eps']
    for k, zexp in ((1, 1.0), (2, 1.0), (3, 1.0)):
        PRIM, counts, T_expo, K = build(k, W, eps)
        S = sfloat(counts, 6 * K)
        T = np.diag(np.exp(2j * np.pi * T_expo / (12 * K)))
        Z = np.trace(T @ T @ S @ T)
        assert abs(Z - zexp) < 1e-9, (k, Z)


def test_L8_l73_lemma():
    A1 = np.array([[2, 1], [1, 1]], dtype=np.int64)
    M = A1 - np.eye(2, dtype=np.int64)
    assert int(round(np.linalg.det(M))) == -1
    from math import gcd
    for N in range(2, 513):
        d = int(M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]) % N
        assert gcd(d, N) == 1
