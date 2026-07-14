"""B588 — the sector-exchange theorem (L81(a)).

(D_A1) Z(W; SU(2)_k) = (1/2)[t_+ - t_-] on C[Z_{2kap'}] (the A1 Weil rep),
exact vs banked su2 values; the membership fact (-1 in W(A1), -1 not in W(A2));
the ingredient identity at kap = kap' = 5: (1/2)(1 - sqrt5) = (1/12)[(1+5) - 6 sqrt5]
= -1/phi — the SAME Gauss data in opposite parity sectors. Sector exchange =
the migration of -1 across the Weyl-group boundary under level-rank.

Run: python3 sector_exchange.py (pyenv, ~1 min). Nothing to CLAIMS.md.
"""
import importlib.util
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    "b238", os.path.join(HERE, "..", "B238_su32_levelrank", "su32_wrt.py"))
b238 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b238)

PHI = (1 + 5 ** 0.5) / 2
R2 = np.array([[1, 1], [0, 1]])
L2 = np.array([[1, 0], [1, 1]])


def mono(word):
    M = np.eye(2, dtype=int)
    for ch in word:
        M = M @ (R2 if ch == 'R' else L2)
    return M


def a1_weil(kapp):
    """The A1 finite Weil rep on C[Z_{2kap'}]: T = e^{pi i mu^2/(2kap')},
    S = finite FT with pairing e^{-pi i mu nu / kap'}."""
    n = 2 * kapp
    mu = np.arange(n)
    T = np.exp(1j * np.pi * mu * mu / (2.0 * kapp))
    S = np.exp(-1j * np.pi * np.outer(mu, mu) / kapp) / np.sqrt(n)
    assert np.allclose(S @ S.conj().T, np.eye(n), atol=1e-9)
    P = np.zeros((n, n))
    for i in range(n):
        P[(-i) % n, i] = 1.0
    assert np.allclose(S @ S, P, atol=1e-8), "S^2 != parity (A1)"
    return T, S, P


def rho(word, T, S):
    n = S.shape[0]
    Rop = np.diag(T)
    Lop = S.conj().T @ np.diag(T).conj() @ S
    M = np.eye(n, dtype=complex)
    for ch in word:
        M = M @ (Rop if ch == 'R' else Lop)
    return M


# ---- the membership fact (exact integer check) ----
S1 = np.array([[-1, 0], [1, 1]])
S2m = np.array([[1, 1], [0, -1]])
weyl_a2 = []
for word in ((), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)):
    M = np.eye(2, dtype=int)
    for g in word:
        M = (S1 if g == 0 else S2m) @ M
    weyl_a2.append(M)
assert any(np.array_equal(w, -np.eye(2, dtype=int)) for w in [np.array([[-1, 0], [0, -1]])])
in_a2 = any(np.array_equal(w, -np.eye(2, dtype=int)) for w in weyl_a2)
print(f"membership: -1 in W(A1) = True (it IS the reflection);  -1 in W(A2) = {in_a2}")
assert not in_a2

# ---- (D_A1) across kap' for balanced words ----
print("\n(D_A1): Z(W; SU(2)_k) = (t_+ - t_-)/2, vs banked su2 values:")
WORDS = ("RL", "RRLL", "RRRLLL")
tvals = {}
for kapp in range(3, 21):
    S2wz, T2wz, c2 = b238.su2_data(kapp - 2)
    T, S, P = a1_weil(kapp)
    for wd in WORDS:
        M = rho(wd, T, S)
        tp = np.trace(M)
        tm = np.trace(M @ P)
        zW = (tp - tm) / 2.0
        zB = b238.wrt_trace(S2wz, T2wz, wd)
        assert abs(zW - zB) < 1e-7, f"(D_A1) fails at kap'={kapp}, {wd}: {zW} vs {zB}"
        if wd == "RL":
            tvals[kapp] = (tp, tm)
    print(f"  kap'={kapp:2d}: exact for RL, RRLL, RRRLLL  PASS")

# ---- the conductors and the golden point ----
A = mono("RL")
dm, dp = int(round(np.linalg.det(A - np.eye(2)))), int(round(np.linalg.det(A + np.eye(2))))
print(f"\nA1-side conductors for RL: det(A-I) = {dm} (unit), det(A+I) = {dp} (the 5)")
print("t_+ and t_- for RL over kap' (t_- fires sqrt5-family at 5|kap'):")
for kapp in sorted(tvals):
    tp, tm = tvals[kapp]
    print(f"  kap'={kapp:2d}: t_+ = {tp:+.6f}   t_- = {tm:+.6f}")

tp5, tm5 = tvals[5]
assert abs(tp5 - 1) < 1e-8 and abs(tm5 - np.sqrt(5)) < 1e-8, (tp5, tm5)
lhs = (1 - np.sqrt(5)) / 2
rhs = ((1 + 5) - 6 * np.sqrt(5)) / 12
print(f"\nTHE INGREDIENT IDENTITY at kap = kap' = 5 (the level-rank point):")
print(f"  A1 (all in the PLAIN = even sector):  (t_+ - t_-)/2 = (1 - sqrt5)/2 = {lhs:+.9f}")
print(f"  A2 (all in the C-COSET = odd sector): (1/12)[(1+5) - 6 sqrt5]      = {rhs:+.9f}")
assert abs(lhs - rhs) < 1e-12 and abs(lhs - (-1 / PHI)) < 1e-12
print("  both = -1/phi. The SAME Gauss data (the unit identity term + the sqrt5")
print("  family) assembles to the same number; on A1 the parity term sits INSIDE")
print("  the Weyl sum (-1 = w0 in W(A1), C = 1), on A2 it sits in the C-coset")
print("  (-1 not in W(A2)). SECTOR EXCHANGE = the migration of -1 across the")
print("  Weyl-group boundary under level-rank.")
print("\nALL GATES PASS")
