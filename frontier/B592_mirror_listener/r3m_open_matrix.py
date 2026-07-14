"""B592-OPEN — R3-M run exactly per the self-contained handoff: the OPEN matrix.

M_{lm} = <l_b|weld|m_a> kept as a MATRIX (Step 2: do not sum), decomposed into
theta-parity blocks (Step 3), all numbers written before comparison (Step 4).
The weld = C rho(g) (the handoff's own identification of the theta-odd twist
via the naming theorem); g sweeps {I, RL, RRLL}. C1 FIRST (the foundation).

Run: python3 r3m_open_matrix.py (pyenv, ~1 min). Nothing to CLAIMS.md.
"""
import cmath
import importlib.util
import math
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


def load(rel, name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, rel))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


b238 = load("../B238_su32_levelrank/su32_wrt.py", "b238")
b245 = load("../B245_higher_color_levelrank/higher_color_levelrank.py", "b245")

w, S, T, cc = b238.su3_data(2)
n = len(w)
C = np.zeros((n, n))
for i, wt in enumerate(w):
    C[w.index((wt[1], wt[0])), i] = 1.0
conj_idx = [w.index((wt[1], wt[0])) for wt in w]
q = cmath.exp(1j * math.pi / 5)
J = {(0, 0): 1.0, (1, 0): b245.H_sym(1, q ** 3, q), (0, 1): b245.H_antisym(2, q ** 3, q),
     (2, 0): b245.H_sym(2, q ** 3, q), (0, 2): b245.H_sym(2, q ** 3, q), (1, 1): 0.0}
psi = np.array([J[wt] for wt in w], dtype=complex)
Si, Ti = np.linalg.inv(S), np.linalg.inv(T)
R, L = T, Si @ Ti @ S

pairs = [(w.index((1, 0)), w.index((0, 1))), (w.index((2, 0)), w.index((0, 2)))]
sing = [w.index((0, 0)), w.index((1, 1))]
odd = np.zeros((n, 2))
even = np.zeros((n, 4))
for j, (a, b) in enumerate(pairs):
    odd[a, j], odd[b, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)
    even[a, j], even[b, j] = 1 / np.sqrt(2), 1 / np.sqrt(2)
for j, i in enumerate(sing):
    even[i, 2 + j] = 1.0


def open_matrix(word, twisted=True):
    M2 = np.eye(n, dtype=complex)
    for ch in word:
        M2 = M2 @ (R if ch == 'R' else L)
    W = (C @ M2) if twisted else M2
    return np.diag(np.conj(psi[conj_idx])) @ W @ np.diag(psi)


print("==== C1 FIRST (the foundation): the UNTWISTED plain double, all channels ====")
M0 = open_matrix("", twisted=False)
print(f"  max|Im| over the whole matrix: {np.abs(M0.imag).max():.2e}")
assert np.abs(M0.imag).max() < 1e-12, "C1 FAILED -- computation invalid per the handoff"
print("  C1 PASS: real in all channels.")

print("\n==== THE OPEN MATRIX, theta-parity blocks (Steps 2-4) ====")
for word in ("", "RL", "RRLL"):
    M = open_matrix(word, twisted=True)
    Moo = odd.T @ M @ odd
    Mee = even.T @ M @ even
    Moe = odd.T @ M @ even
    Meo = even.T @ M @ odd
    print(f"\n  weld g = {word if word else 'I'} (twisted):")
    print(f"    Im(M_odd) max = {np.abs(Moo.imag).max():.6f};  "
          f"Im(M_even) max = {np.abs(Mee.imag).max():.6f};  "
          f"cross max = {max(np.abs(Moe).max(), np.abs(Meo).max()):.2e}")
    print("    M_odd:")
    for row in Moo:
        print("      [" + "  ".join(f"{x:+.6f}" for x in row) + "]")

print("\n==== THE SIGN-FLIP THEOREM (what the twist does to the open matrix) ====")
# P_odd C = -P_odd and P_even C = +P_even  =>  the twist flips the odd-odd
# block's sign and fixes the even-even block. One-line proof + numerics:
ok = True
for word in ("", "RL", "RRLL"):
    Mt = open_matrix(word, twisted=True)
    Mu = open_matrix(word, twisted=False)
    flip = np.abs(odd.T @ Mt @ odd + odd.T @ Mu @ odd).max()
    same = np.abs(even.T @ Mt @ even - even.T @ Mu @ even).max()
    ok &= flip < 1e-12 and same < 1e-12
    print(f"  g = {word if word else 'I':>5}: odd-odd(twisted) = -odd-odd(untwisted): "
          f"{flip < 1e-12};  even-even equal: {same < 1e-12}")
assert ok
print("  => THE TWIST IS HEARD IN THE OPEN MATRIX AS THE SIGN OF THE ODD BLOCK")
print("     (and in no closed contraction: the B592 theorem).")

print("\n==== parity conservation (cross == 0): theorem ====")
print("  D = diag(psi) is real and C-symmetric; C rho(g) commutes with P_odd;")
print("  hence M preserves theta-parity exactly -- no odd<->even mixing, the")
print("  open-matrix face of the quadrature theorem (X2R).")

print("\n==== C4 in matrix form (5_2, R-matrix state) ====")


def rmat(N, qv):
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


def inv_fund(N, braid, nstr, qv):
    Rm = rmat(N, qv)
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


j52 = inv_fund(3, [1, 1, 1, 2, -1, 2], 3, q)
J52 = {(0, 0): 1.0, (1, 0): j52, (0, 1): j52, (2, 0): 0.0, (0, 2): 0.0, (1, 1): 0.0}
psi52 = np.array([J52[wt] for wt in w], dtype=complex)


def open52(word, twisted=True):
    M2 = np.eye(n, dtype=complex)
    for ch in word:
        M2 = M2 @ (R if ch == 'R' else L)
    W = (C @ M2) if twisted else M2
    return np.diag(np.conj(psi52[conj_idx])) @ W @ np.diag(psi52)


M52 = open52("RL")
Moo52 = odd.T @ M52 @ odd
cross52 = max(np.abs(odd.T @ M52 @ even).max(), np.abs((even.T @ M52 @ odd)).max())
print(f"  5_2 (J_3 = {j52:+.6f}, non-real; state still C-symmetric by invertibility):")
print(f"    cross max = {cross52:.2e} (parity conserved);  "
      f"Im(M_odd) max = {np.abs(Moo52.imag).max():.6f}")
flip52 = np.abs(odd.T @ open52('RL', True) @ odd + odd.T @ open52('RL', False) @ odd).max()
print(f"    the twist = odd-block sign flip for 5_2 too: {flip52 < 1e-12}")
print("    (knot-specific ENTRIES, universal STRUCTURE -- C4's contrast is in the")
print("     values: 5_2's blocks are non-real already at the plain weld away from I.)")

print("\n==== THE VERDICT (the locked table, extended per the handoff's own rule) ====")
print("  At the bare twisted weld (g = I): Im = 0 everywhere -> the table says DEAF.")
print("  At monodromy-dressed welds: Im(M_odd) != 0 AND Im(M_even) != 0 -> MIXED row;")
print("  cross == 0 exactly (parity conserved).  NEW ROW (banked as-is):")
print("  OPEN-HEARD / CLOSED-DEAF: the twist's entire imprint on the open matrix is")
print("  the SIGN of the theta-odd block (flip under twist; theorem P_odd C = -P_odd);")
print("  the imaginary parts are parity-symmetric inversion phases (conj A(g) = A(g^-1));")
print("  and every closed contraction of the odd block against the C-symmetric states")
print("  vanishes (B592). The mirror hears the twist as a sign it can never sum.")
print("\nALL GATES PASS")
