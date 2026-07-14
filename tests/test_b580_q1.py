"""B580-Q1 — the level-1 (abelian) listener, reconstructed in-repo (L80(a)).

The Round-1 transcript banked Q1 with its artifacts uncommitted (agent
worktrees); this lock reconstructs the computation with the Q2-verifier's
lens-space control gate, as L80(a) required:

  * the E6 level-1 theater (3 primaries: 1, 27, 27b): S = the Z3 DFT,
    T from h = (0, 2/3, 2/3), c = 6 — modular gate (ST)^3 = S^2 verified;
  * the figure-eight gate at level 1: Z = tr rho(A1) = +1 (B569), and the
    vacuum column (1,1,1)/sqrt3 is the level-1 state;
  * THE STRUCTURAL UNHEARABILITY: the Dehn-filling covectors (row 0 of
    rho(g_{p,q})) over a full coprime slope sweep span EXACTLY the
    theta-even 2-plane — SVD rank 2, theta-odd projection < 1e-10;
  * THE LENS-SPACE CONTROL GATE: |Z(L(p,1))| from the modular rep equals
    the direct Z3 Gauss-sum magnitude, across a p-sweep.

See frontier/B580_chord_program/ROUND1_TRANSCRIPT.md (Q1, the hygiene list).
"""
import cmath
import math

import numpy as np

# Kac-Peterson convention: S_{lm} ~ e^{-2 pi i (l,m)} — the CONJUGATE Z3 DFT
S3 = np.array([[1, 1, 1],
               [1, cmath.exp(-2j * cmath.pi / 3), cmath.exp(2j * cmath.pi / 3)],
               [1, cmath.exp(2j * cmath.pi / 3), cmath.exp(-2j * cmath.pi / 3)]],
              dtype=complex) / math.sqrt(3)
HS = (0.0, 2 / 3, 2 / 3)
T3 = np.diag([cmath.exp(2j * cmath.pi * (h - 6 / 24)) for h in HS])

S2 = np.array([[0, -1], [1, 0]])
T2 = np.array([[1, 1], [0, 1]])


def sl2_word(g):
    """Decompose g in SL(2,Z) into a letter string over {S,T,t} (t = T^-1),
    verified exactly at the 2x2 level by the caller."""
    g = g.copy()
    word = []
    # reduce the bottom-left entry to 0 by T^k then S swaps
    while g[1, 0] != 0:
        if abs(g[0, 0]) >= abs(g[1, 0]):
            k = -(g[0, 0] // g[1, 0]) if g[1, 0] != 0 else 0
            # apply T^k on the LEFT: T^k g ; record so word = ... T^{-k}
            g = np.linalg.matrix_power(T2, int(k)).astype(int) @ g
            word.append(("T", -int(k)))
        g = S2.T @ g                      # S^{-1} g
        word.append(("S", 1))
    # now g is upper triangular with diag +-1
    if g[0, 0] == -1:
        g = (-np.eye(2, dtype=int)).astype(int) @ g
        word.append(("-", 1))             # -I = S^2
    k = int(g[0, 1] * g[0, 0]) if False else int(g[0, 1])
    word.append(("T", k))                 # remaining T^k: g = T^k after reductions
    return word


def rho_of(g, S, T):
    """rho(g) from the letter decomposition; verified against g at 2x2."""
    word = sl2_word(np.array(g, dtype=int))
    M2 = np.eye(2, dtype=int)
    M = np.eye(S.shape[0], dtype=complex)
    Ti = np.linalg.inv(T)
    for sym, k in word:
        if sym == "S":
            M2 = M2 @ S2
            M = M @ S
        elif sym == "-":
            M2 = M2 @ (-np.eye(2, dtype=int))
            M = M @ (S @ S)
        else:
            M2 = M2 @ np.linalg.matrix_power(T2, k)
            M = M @ (np.linalg.matrix_power(T, k) if k >= 0
                     else np.linalg.matrix_power(Ti, -k))
    assert np.array_equal(M2, np.array(g, dtype=int)), (g, M2)
    return M


def test_modular_gate_and_z_plus_one():
    ST3 = np.linalg.matrix_power(S3 @ T3, 3)
    S32 = S3 @ S3
    ratio = ST3[0, 0] / S32[0, 0]
    assert np.allclose(ST3, ratio * S32, atol=1e-9)      # (ST)^3 prop S^2
    assert abs(abs(ratio) - 1) < 1e-9
    A1 = np.array([[2, 1], [1, 1]])
    Z = np.trace(rho_of(A1, S3, T3))
    assert abs(Z - 1) < 1e-9                              # B569: Z = +1
    v = np.abs(S3[0, :])
    assert np.allclose(v, np.ones(3) / math.sqrt(3), atol=1e-12)


def test_filling_covectors_span_theta_even_only():
    covs = []
    for p in range(1, 21):
        for q in range(0, p):
            if math.gcd(p, q) != 1:
                continue
            # g with first COLUMN (p, q)
            # find (r, s): p*s - q*r = 1 via extended euclid
            r, s = _bezout(p, q)
            g = np.array([[p, r], [q, s]])
            assert int(round(np.linalg.det(g))) == 1
            covs.append(rho_of(g, S3, T3)[0, :])
    covs = np.array(covs)
    assert len(covs) >= 100
    sv = np.linalg.svd(covs, compute_uv=False)
    assert sv[1] / sv[0] > 1e-3 and sv[2] / sv[0] < 1e-10        # rank exactly 2
    odd = np.array([0, 1, -1]) / math.sqrt(2)                    # 27 <-> 27b antisym
    assert np.abs(covs @ odd).max() < 1e-10                      # unhearable


def _bezout(p, q):
    # returns (r, s) with p*s - q*r = 1
    if q == 0:
        return 0, 1
    g0, x0, y0 = _egcd(p, q)
    assert g0 == 1
    # p*x0 + q*y0 = 1  =>  s = x0, r = -y0
    return -y0, x0


def _egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = _egcd(b, a % b)
    return g, y, x - (a // b) * y


def test_lens_space_control_gate():
    # Z(L(p,1)) two ways, magnitudes: the surgery sandwich <0|rho(S T^p S)|0>
    # vs the direct Z3 Gauss sum (1/3) |sum_j e^{2 pi i p h_j}|
    for p in range(1, 13):
        g = S2 @ np.linalg.matrix_power(T2, p) @ S2
        za = rho_of(g, S3, T3)[0, 0]
        zb = sum(cmath.exp(2j * cmath.pi * p * h) for h in HS) / 3.0
        assert abs(abs(za) - abs(zb)) < 1e-9, (p, abs(za), abs(zb))


def test_knot_blindness_control():
    # CTRL: the covector machinery sees only the SL(2,Z) class, never a knot;
    # any two hyperbolic monodromy words give vacuum-uniform |row 0|
    for g in (np.array([[2, 1], [1, 1]]), np.array([[5, 2], [2, 1]])):
        row = np.abs(rho_of(g, S3, T3)[0, :])
        assert row.max() - row.min() < 1e-9
