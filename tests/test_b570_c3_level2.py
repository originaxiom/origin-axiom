"""B570 Lane C, cell C3 — locks: the theta-odd sector is dynamically alive at level 2.

Full recomputation (W(E6) BFS + Kac-Peterson S + consistency gates + the monodromy),
~30-60 s. The decisive facts locked:
  - genuine rep gates: S unitary/symmetric, S^2 = the theta-flip permutation,
    (ST)^3 = S^2, Verlinde integrality (all 729);
  - h(27) = 13/21 at level 2 (and the other four weights);
  - rho(A1) block-diagonal in the theta-split; theta-ODD 3x3 block NON-SCALAR,
    order 4, eigenvalues {1, +i, -i}, det 1; theta-even eigenvalues {1,1,-1,-1,i,-i};
  - Z = +1 at level 2 (as at level 1).
See frontier/B570_allowed_plays/C3_RESULT.md.
"""
import importlib.util
import os

import numpy as np

_spec = importlib.util.spec_from_file_location(
    "c3mod", os.path.join(os.path.dirname(__file__), "..",
                          "frontier", "B570_allowed_plays", "c3_e6_level2_monodromy.py"))
c3 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(c3)


def _build():
    W, eps = c3.weyl_group()
    assert len(W) == 51840
    rho_w = c3.root_coords([1] * 6)
    shifted = [c3.root_coords(p) + rho_w for p in c3.PRIM]
    S = np.zeros((9, 9), dtype=complex)
    Wl = np.einsum('wij,lj->wli', W.astype(float), np.array(shifted))
    for a in range(9):
        for b in range(a, 9):
            ips = Wl[:, a, :] @ (c3.C @ shifted[b])
            S[a, b] = S[b, a] = np.sum(eps * np.exp(-2j * np.pi * ips / c3.KH))
    S /= np.sqrt((S @ S.conj().T)[0, 0].real)
    if S[0, 0].real < 0:
        S = -S
    hs = [float(c3.root_coords(p) @ (c3.C @ (c3.root_coords(p) + 2 * rho_w))) / (2 * c3.KH)
          for p in c3.PRIM]
    T = np.diag([np.exp(2j * np.pi * (h - (2 * 78 / c3.KH) / 24)) for h in hs])
    return S, T, hs


def test_c3_theta_odd_dynamical():
    S, T, hs = _build()
    # weights, exact
    from fractions import Fraction
    fr = [Fraction(h).limit_denominator(200) for h in hs]
    assert fr[1] == fr[2] == Fraction(13, 21)              # 27, 27bar
    assert fr[6] == Fraction(6, 7)                          # 78
    assert fr[5] == Fraction(9, 7)                          # 650
    assert fr[3] == fr[4] == Fraction(4, 3)                 # 351', 351'bar
    assert fr[7] == fr[8] == Fraction(25, 21)               # 351, 351bar
    # gates
    assert np.linalg.norm(S @ S.conj().T - np.eye(9)) < 1e-9
    assert np.linalg.norm(S - S.T) < 1e-9
    C2 = S @ S
    expect = np.zeros((9, 9))
    for i, p in enumerate(c3.PRIM):
        expect[c3.PRIM.index(c3.theta(p)), i] = 1
    assert np.allclose(C2, expect, atol=1e-9)               # S^2 = the theta flip
    assert np.linalg.norm(np.linalg.matrix_power(S @ T, 3) - C2) < 1e-9
    for a in range(9):
        for b in range(9):
            for cc in range(9):
                N = np.sum(S[a] * S[b] * S[cc].conj() / S[0])
                assert abs(N.imag) < 1e-9 and abs(N.real - round(N.real)) < 1e-9
                assert round(N.real) >= 0                    # Verlinde integrality
    # the monodromy, two words
    w1 = T @ T @ S @ T
    w2 = T @ S @ np.linalg.inv(T) @ np.linalg.inv(S)
    assert np.linalg.norm(w1 - w2) < 1e-9
    assert abs(np.trace(w1) - 1) < 1e-9                      # Z = +1 at level 2
    # the theta-odd block
    pairs = [(1, 2), (3, 4), (7, 8)]
    odd = np.zeros((9, 3))
    for j, (a, b) in enumerate(pairs):
        odd[a, j], odd[b, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)
    B = odd.T @ w1 @ odd
    assert np.linalg.norm(w1 @ expect - expect @ w1) < 1e-9  # [rho, C] = 0 (central)
    assert np.linalg.norm(B - B[0, 0] * np.eye(3)) > 1       # NON-SCALAR (the result)
    ev = sorted(np.linalg.eigvals(B), key=lambda z: (round(z.real, 6), round(z.imag, 6)))
    assert np.allclose(ev, [-1j, 1j, 1], atol=1e-8)          # {1, +i, -i}
    assert abs(np.linalg.det(B) - 1) < 1e-8                  # SU(3)
    assert np.linalg.norm(np.linalg.matrix_power(B, 4) - np.eye(3)) < 1e-8   # order 4
    assert np.linalg.norm(np.linalg.matrix_power(B, 2) - np.eye(3)) > 1
    # the theta-even block spectrum
    fixed = [0, 5, 6]
    even = np.zeros((9, 6))
    for j, f in enumerate(fixed):
        even[f, j] = 1
    for j, (a, b) in enumerate(pairs):
        even[a, 3 + j], even[b, 3 + j] = 1 / np.sqrt(2), 1 / np.sqrt(2)
    ev6 = sorted(np.linalg.eigvals(even.T @ w1 @ even),
                 key=lambda z: (round(z.real, 6), round(z.imag, 6)))
    assert np.allclose(ev6, [-1, -1, -1j, 1j, 1, 1], atol=1e-8)
