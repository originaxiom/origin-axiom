"""B570 AP2 -- the allowed-theater table: standalone lock (no external imports
beyond numpy). Self-contained reimplementation of the modular-data machinery
so this file can be dropped anywhere and run.

Convention (abelian (Z/N,q), N<=24): q(x) = r x^2/(2N) mod 1, x=0..N-1, with
r in range(2N), gcd(r,N)=1, and r even whenever N is odd (the standard
classification of nondegenerate Z-valued quadratic forms on a cyclic group).
S_ab = (1/sqrt(N)) exp(-2pi i r a b/N); T = diag(exp(2pi i(q(a) - c/24)));
c mod 8 fixed by Gauss-Milgram: sum_a theta_a = sqrt(N) exp(2pi i c/8).
A1 = T^2 S T (word-checked against T(ST^-1S^-1)).

Headline THEOREM (proved in closed form, see docstring of
test_abelian_Z_is_exactly_one_everywhere): Tr(rho(A1)) = 1 EXACTLY for every
consistent abelian modular theory. Verified here numerically to 1e-9 for all
243 (N,q) with N<=24; proved algebraically from the Gauss-Milgram identity
itself (not merely observed).
"""
import numpy as np
from math import gcd, sqrt

PHI = (1 + sqrt(5)) / 2


# ------------------------------------------------------------------ machinery
def gate_report(S, T, D):
    I = np.eye(D)
    C = S @ S
    out = {
        'unitary': np.linalg.norm(S @ S.conj().T - I),
        'symmetric': np.linalg.norm(S - S.T),
        'S4=I': np.linalg.norm(np.linalg.matrix_power(S, 4) - I),
        'C_involution': np.linalg.norm(C @ C - I),
        '(ST)^3=S^2': np.linalg.norm(np.linalg.matrix_power(S @ T, 3) - C),
    }
    Ncap = min(D, 6)
    verl_err = 0.0
    for a in range(Ncap):
        for b in range(Ncap):
            for c in range(Ncap):
                val = sum(S[a, x] * S[b, x] * np.conj(S[c, x]) / S[0, x] for x in range(D))
                verl_err = max(verl_err, abs(val - round(val.real)) + abs(val.imag))
    out['verlinde_int'] = verl_err
    return out


def gauss_milgram_c_mod8(theta, D, dims=None):
    if dims is None:
        dims = np.ones(D)
    dims = np.asarray(dims, dtype=float)
    Dtot = sqrt(np.sum(dims ** 2))
    G = np.sum(dims ** 2 * theta)
    mag_ok = abs(abs(G) - Dtot) < 1e-6
    phase = np.angle(G) % (2 * np.pi)
    c8 = (phase / (2 * np.pi)) * 8 % 8
    return c8, mag_ok


def genuine_T(h_list, c8):
    return np.diag([np.exp(2j * np.pi * (h - c8 / 24)) for h in h_list])


def evaluate_A1(S, T):
    w1 = T @ T @ S @ T
    w2 = T @ S @ np.linalg.inv(T) @ np.linalg.inv(S)
    return w1, np.linalg.norm(w1 - w2)


def matrix_order(M, bound=3000, tol=1e-6):
    D = M.shape[0]
    I = np.eye(D)
    P = np.eye(D)
    for k in range(1, bound + 1):
        P = P @ M
        if np.linalg.norm(P - I) < tol:
            return k
    return None


def sightedness(M, tol=1e-6):
    D = M.shape[0]
    c = np.trace(M) / D
    return 'BLIND' if np.linalg.norm(M - c * np.eye(D)) < tol else 'SIGHTED'


def abelian_theory(N, r):
    D = N
    h = [(r * x * x) / (2 * N) % 1 for x in range(D)]
    theta = np.array([np.exp(2j * np.pi * hh) for hh in h])
    S = np.array([[np.exp(-2j * np.pi * (r * a * b / N)) for b in range(D)]
                  for a in range(D)]) / sqrt(N)
    c8, mag_ok = gauss_milgram_c_mod8(theta, D)
    T = genuine_T(h, c8)
    gates = gate_report(S, T, D)
    gates_ok = all(v < 1e-6 for v in gates.values()) and mag_ok
    if not gates_ok:
        return {'gates_ok': False, 'gates': gates}
    w1, word_diff = evaluate_A1(S, T)
    return {'gates_ok': True, 'word_diff': word_diff, 'Z': np.trace(w1),
            'order': matrix_order(w1), 'sight': sightedness(w1)}


def enumerate_abelian(Nmax=24):
    out = []
    for N in range(1, Nmax + 1):
        for r in range(2 * N):
            if gcd(r, N) != 1:
                continue
            if N % 2 == 1 and r % 2 != 0:
                continue
            th = abelian_theory(N, r)
            th['N'], th['r'] = N, r
            out.append(th)
    return out


def fibonacci_data():
    D = 2
    Dn = sqrt(2 + PHI)
    S = np.array([[1, PHI], [PHI, -1]]) / Dn
    return S, [0, 2 / 5], 14 / 5, D


def ising_data():
    S = np.array([[1, sqrt(2), 1], [sqrt(2), 0, -sqrt(2)], [1, -sqrt(2), 1]]) / 2
    return S, [0, 1 / 16, 1 / 2], 1 / 2, 3


def su2k_data(k):
    D, m = k + 1, k + 2
    S = np.array([[sqrt(2 / m) * np.sin(np.pi * (i + 1) * (j + 1) / m) for j in range(D)]
                  for i in range(D)])
    h = [i * (i + 2) / (4 * m) for i in range(D)]
    return S, h, 3 * k / m, D


def run_named(S, h, c, D):
    theta = np.array([np.exp(2j * np.pi * hh) for hh in h])
    dims = (S[0, :] / S[0, 0]).real
    c8, mag_ok = gauss_milgram_c_mod8(theta, D, dims=dims)
    T = genuine_T(h, c % 8)  # exact known central charge (mod 8 representative)
    gates = gate_report(S, T, D)
    gates_ok = all(v < 1e-6 for v in gates.values()) and mag_ok
    assert gates_ok, gates
    w1, word_diff = evaluate_A1(S, T)
    return {'word_diff': word_diff, 'Z': np.trace(w1), 'order': matrix_order(w1),
            'sight': sightedness(w1)}


def run_doubled_fibonacci():
    S0, h0, c0, D0 = fibonacci_data()
    T0 = genuine_T(h0, c0 % 8)
    Tbar = np.conj(T0)
    S = np.kron(S0, np.conj(S0))
    T = np.kron(T0, Tbar)
    D = D0 * D0
    gates = gate_report(S, T, D)
    assert all(v < 1e-6 for v in gates.values())
    w1, word_diff = evaluate_A1(S, T)
    return {'word_diff': word_diff, 'Z': np.trace(w1), 'order': matrix_order(w1),
            'sight': sightedness(w1)}


def pisano_period(N):
    if N == 1:
        return 1
    a, b = 0, 1
    for i in range(1, 200 * N + 100):
        a, b = b, (a + b) % N
        if a == 0 and b == 1:
            return i
    return None


# ------------------------------------------------------------------------ tests
def test_abelian_gates_pass_all_N_le_24():
    for t in enumerate_abelian(24):
        assert t['gates_ok'], t.get('gates')


def test_abelian_Z_is_exactly_one_everywhere():
    """Tr(rho(A1)) = 1 for EVERY consistent abelian (Z/N,q), N<=24 (243 theories).
    Closed-form proof (elementary, not just numerics): Tr(T^2ST) = sum_a Ta^3 Saa;
    Ta^3 Saa = (1/sqrt N) e^{2pi i(q(a)-c/8)} using q(2a)=4q(a) [quadratic-form
    homogeneity, so 3q(a)-b(a,a) = 3q(a)-(q(2a)-2q(a)) = 5q(a)-4q(a) = q(a)];
    summing over a gives (1/sqrt N) e^{-2pi i c/8} * GaussSum, and GaussSum =
    sqrt(N) e^{2pi i c/8} BY DEFINITION of c mod 8 (Gauss-Milgram) -> ratio = 1
    identically, independent of N, r, and the sign convention."""
    for t in enumerate_abelian(24):
        assert abs(t['Z'] - 1.0) < 1e-8


def test_abelian_word_independence():
    for t in enumerate_abelian(24):
        assert t['word_diff'] < 1e-6


def test_abelian_only_trivial_N1_is_blind():
    for t in enumerate_abelian(24):
        assert t['sight'] == ('BLIND' if t['N'] == 1 else 'SIGHTED')


ORDER_TABLE = {
    1: 1, 2: 6, 3: 4, 4: 3, 5: 10, 6: 12, 7: 8, 8: 6, 9: 12, 10: 30,
    11: 5, 12: 12, 13: 14, 14: 24, 15: 20, 16: 12, 17: 18, 18: 12,
    19: 9, 20: 30, 21: 8, 22: 30, 23: 24, 24: 12,
}


def test_order_rho_A1_matches_table_and_is_q_independent():
    for N, expected in ORDER_TABLE.items():
        for r in range(2 * N):
            if gcd(r, N) != 1 or (N % 2 == 1 and r % 2 != 0):
                continue
            th = abelian_theory(N, r)
            assert th['order'] == expected, (N, r, th['order'], expected)


def test_pisano_period_relation_generic_and_exceptions():
    exceptions = {1: 1.0, 2: 2.0, 22: 1.0}
    for N in range(1, 25):
        piN = pisano_period(N)
        ratio = ORDER_TABLE[N] / piN
        expect = exceptions.get(N, 0.5)
        assert abs(ratio - expect) < 1e-9, (N, ratio, expect)


def test_named_theories():
    Sf, hf, cf, Df = fibonacci_data()
    fib = run_named(Sf, hf, cf, Df)
    assert abs(fib['Z'] - (-1 / PHI)) < 1e-8 and fib['order'] == 10 and fib['sight'] == 'SIGHTED'

    dfib = run_doubled_fibonacci()
    assert abs(dfib['Z'] - (2 - PHI)) < 1e-8 and dfib['order'] == 5 and dfib['sight'] == 'SIGHTED'

    Si, hi, ci, Di = ising_data()
    ising = run_named(Si, hi, ci, Di)
    assert abs(ising['Z']) < 1e-8 and ising['order'] == 3 and ising['sight'] == 'SIGHTED'

    expected_su2 = {1: (1.0, 6), 2: (0.0, 3), 3: (-1 / PHI, 15), 4: (0.0, 12)}
    for k, (Zexp, ordexp) in expected_su2.items():
        Sk, hk, ck, Dk = su2k_data(k)
        r = run_named(Sk, hk, ck, Dk)
        assert abs(r['Z'] - Zexp) < 1e-8 and r['order'] == ordexp and r['sight'] == 'SIGHTED'


def test_all_Z_real_and_small_finite_set():
    ab_Z = set(round(t['Z'].real, 6) for t in enumerate_abelian(24))
    assert ab_Z == {1.0}
    for t in enumerate_abelian(24):
        assert abs(t['Z'].imag) < 1e-8


if __name__ == '__main__':
    import pytest
    raise SystemExit(pytest.main([__file__, '-v']))
