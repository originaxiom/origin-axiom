"""B593 — Round 4: the second-order hearing law (locks).

A_eps(g) = A_0(g) - eps^2 (u' W(g) u) exactly, no O(eps) term; the closed
chiral amplitude = -2 eps^2 (u' M_odd u), complex at g = RL with the exact
golden-pentagonal value 1/(2 phi) + i sin(2pi/5)/sqrt5; R4-B null (8_17
fundamental state reverse-blind). See frontier/B593_round4_hearing/FINDINGS.md.
"""
import cmath
import importlib.util
import math
import os

import numpy as np

_ROOT = os.path.join(os.path.dirname(__file__), "..")


def _load(rel, name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(_ROOT, rel))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


b238 = _load("frontier/B238_su32_levelrank/su32_wrt.py", "b238m6")
b245 = _load("frontier/B245_higher_color_levelrank/higher_color_levelrank.py", "b245m6")

Q = cmath.exp(1j * math.pi / 5)
PHI = (1 + 5 ** 0.5) / 2


def _setup():
    w, S, T, c = b238.su3_data(2)
    n = len(w)
    C = np.zeros((n, n))
    for i, wt in enumerate(w):
        C[w.index((wt[1], wt[0])), i] = 1.0
    conj_idx = [w.index((wt[1], wt[0])) for wt in w]
    J = {(0, 0): 1.0, (1, 0): b245.H_sym(1, Q ** 3, Q),
         (0, 1): b245.H_antisym(2, Q ** 3, Q), (2, 0): b245.H_sym(2, Q ** 3, Q),
         (0, 2): b245.H_sym(2, Q ** 3, Q), (1, 1): 0.0}
    psi = np.array([J[wt] for wt in w], dtype=complex)
    Si, Ti = np.linalg.inv(S), np.linalg.inv(T)
    R, L = T, Si @ Ti @ S
    pairs = [(w.index((1, 0)), w.index((0, 1))), (w.index((2, 0)), w.index((0, 2)))]
    U = np.zeros((n, 2))
    for j, (a, b) in enumerate(pairs):
        U[a, j], U[b, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)
    return w, n, C, conj_idx, psi, R, L, U


def _weld(C, R, L, n, word, twisted):
    M = np.eye(n, dtype=complex)
    for ch in word:
        M = M @ (R if ch == 'R' else L)
    return (C @ M) if twisted else M


def _amp(psi, W, conj_idx, n):
    vec = W @ psi
    return sum(np.conj(psi[conj_idx[i]]) * vec[i] for i in range(n))


def test_hearing_law_exact():
    w, n, C, conj_idx, psi, R, L, U = _setup()
    for word in ("", "RL", "RRLL"):
        for twisted in (True, False):
            W = _weld(C, R, L, n, word, twisted)
            A0 = _amp(psi, W, conj_idx, n)
            for j in (0, 1):
                u = U[:, j].astype(complex)
                quad = np.conj(u) @ W @ u
                for eps in (0.05, 0.2):
                    Ae = _amp(psi + eps * u, W, conj_idx, n)
                    assert abs(Ae - (A0 - eps ** 2 * quad)) < 1e-12


def test_closed_chiral_amplitude_value():
    w, n, C, conj_idx, psi, R, L, U = _setup()
    Wt = _weld(C, R, L, n, "RL", True)
    u3 = U[:, 0].astype(complex)
    quad = np.conj(u3) @ Wt @ u3
    expected = 1 / (2 * PHI) + 1j * math.sin(2 * math.pi / 5) / math.sqrt(5)
    assert abs(quad - expected) < 1e-9                       # golden-pentagonal, Im != 0
    u6 = U[:, 1].astype(complex)
    assert abs(np.conj(u6) @ Wt @ u6 - np.conj(quad)) < 1e-9  # conjugate pair
    # the twisted-minus-untwisted closed amplitude at eps
    Wu = _weld(C, R, L, n, "RL", False)
    eps = 0.2
    d = (_amp(psi + eps * u3, Wt, conj_idx, n)
         - _amp(psi + eps * u3, Wu, conj_idx, n))
    assert abs(d - (-2 * eps ** 2 * quad)) < 1e-12
    assert abs(d.imag) > 1e-3                                # genuinely chiral (complex)


def _rmat(N, qv):
    d = N * N
    Rm = np.zeros((d, d), dtype=complex)
    for i in range(N):
        for j in range(N):
            row = i * N + j
            if i == j:
                Rm[row, row] = qv
            else:
                Rm[j * N + i, row] += 1.0
                if i < j:
                    Rm[row, row] += (qv - 1 / qv)
    return Rm / qv ** (1.0 / N)


def _inv(N, braid, nstr, qv):
    Rm = _rmat(N, qv)
    Ri = np.linalg.inv(Rm)
    M = np.eye(N ** nstr, dtype=complex)
    wr = 0
    for g in braid:
        k = abs(g) - 1
        M = M @ np.kron(np.kron(np.eye(N ** k), Rm if g > 0 else Ri),
                        np.eye(N ** (nstr - k - 2)))
        wr += 1 if g > 0 else -1
    mu1 = np.diag([qv ** (N - 1 - 2 * i) for i in range(N)])
    mu = mu1
    for _ in range(nstr - 1):
        mu = np.kron(mu, mu1)
    return np.trace(M @ mu) * qv ** (-(N - 1.0 / N) * wr) / np.trace(mu1)


def test_r4b_null_8_17():
    B = [1, 1, -2, 1, -2, 1, -2, -2]
    qm = cmath.exp(1j * (math.pi / 2 + 1e-7))
    assert abs(abs(_inv(2, B, 3, qm)) - 37) < 1e-3           # det gate: 8_17
    jf = _inv(3, B, 3, Q)
    jr = _inv(3, list(reversed(B)), 3, Q)
    assert abs(jf - jr) < 1e-12                              # reverse-blind (null)


def test_v2_braid_is_8_17_full_jones():
    def jones817(t):
        return (t**-4 - 3*t**-3 + 5*t**-2 - 6*t**-1 + 7 - 6*t + 5*t**2
                - 3*t**3 + t**4)
    B = [1, 1, -2, 1, -2, 1, -2, -2]
    for qv in (1.23 * cmath.exp(0.37j), 0.81 * cmath.exp(1.13j)):
        assert abs(_inv(2, B, 3, qv) - jones817(qv ** 2)) < 1e-8


def test_v3_negative_amphichiral_triangle():
    B = [1, 1, -2, 1, -2, 1, -2, -2]
    jf = _inv(3, B, 3, Q)
    jm = _inv(3, [-g for g in B], 3, Q)
    assert abs(jf.imag) < 1e-9                      # real (mirror = reverse + blindness)
    assert abs(jm - np.conj(jf)) < 1e-9


def test_v1_exact_symbolic_amplitude():
    import os as _os
    import pytest as _pytest
    if not _os.environ.get("OA_SLOW"):
        _pytest.skip("exact symbolic verification: set OA_SLOW=1")
    import sympy as sp
    import itertools
    weights = [(a, b) for a in range(3) for b in range(3 - a)]
    kap = 5
    Lvec = lambda w: sp.Matrix([w[0] + w[1] + 2, w[1] + 1, 0])
    ip = lambda u, v: (u.T * v)[0] - (sum(u) * sum(v)) / sp.Integer(3)
    perms = list(itertools.permutations(range(3)))
    sgn = lambda p: sp.Integer((-1) ** sum(p[i] > p[j] for i in range(3)
                                           for j in range(i + 1, 3)))
    n = len(weights)
    S = sp.zeros(n, n)
    for i, wl in enumerate(weights):
        Ll = Lvec(wl)
        for j, wm in enumerate(weights):
            Lm = Lvec(wm)
            S[i, j] = sum(sgn(p) * sp.exp(-2 * sp.pi * sp.I *
                          ip(sp.Matrix([Ll[p[0]], Ll[p[1]], Ll[p[2]]]), Lm) / kap)
                          for p in perms)
    S = S / sp.sqrt(sp.simplify(sum(S[0, j] * sp.conjugate(S[0, j])
                                    for j in range(n))))
    h = lambda wt: (sp.Rational(2, 3) * (wt[0]**2 + wt[0]*wt[1] + wt[1]**2)
                    / (2 * kap) + (wt[0] + wt[1]) / sp.Integer(kap))
    T = sp.diag(*[sp.exp(2 * sp.pi * sp.I * (h(wt) - sp.Rational(16, 5) / 24))
                  for wt in weights])
    rho = T * S.H * T.H * S
    idx = {wt: i for i, wt in enumerate(weights)}
    Cm = sp.zeros(n, n)
    for wt in weights:
        Cm[idx[(wt[1], wt[0])], idx[wt]] = 1
    u3 = sp.zeros(n, 1)
    u3[idx[(1, 0)], 0] = 1 / sp.sqrt(2)
    u3[idx[(0, 1)], 0] = -1 / sp.sqrt(2)
    quad = sp.simplify(sp.expand_complex((u3.H * Cm * rho * u3)[0]))
    phi = (1 + sp.sqrt(5)) / 2
    target = 1 / (2 * phi) + sp.I * sp.sin(2 * sp.pi / 5) / sp.sqrt(5)
    assert sp.simplify(sp.expand_complex(quad - target)) == 0
