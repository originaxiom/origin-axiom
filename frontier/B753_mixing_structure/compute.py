"""B753 -- the mixing-structure adjudication (prereg 406bd993).

Builds the explicit 2x2 theta-odd block of the twisted weld at g = RL from the
banked B238/B593 pipeline and decides chat-1's eigenvalue claim by computation.
Standard Hermitian inner product; canonical theta-odd basis {u3, u6}.
Deterministic; program-internal mathematics only (no SM values anywhere).
"""
import cmath
import importlib.util
import math
import os

import numpy as np

HERE = os.getcwd()


def load(rel, name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, rel))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


b238 = load("../B238_su32_levelrank/su32_wrt.py", "b238")

w, S, T, cc = b238.su3_data(2)
n = len(w)
C = np.zeros((n, n))
for i, wt in enumerate(w):
    C[w.index((wt[1], wt[0])), i] = 1.0
Si, Ti = np.linalg.inv(S), np.linalg.inv(T)
R, L = T, Si @ Ti @ S
PHI = (1 + math.sqrt(5)) / 2

pairs = [(w.index((1, 0)), w.index((0, 1))), (w.index((2, 0)), w.index((0, 2)))]
U = np.zeros((n, 2))
for j, (a, b) in enumerate(pairs):
    U[a, j], U[b, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)
U = U.astype(complex)

W_weld = C @ R @ L                                     # the twisted weld at g = RL

print("=" * 88)
print("CELL 1 -- the explicit 2x2 theta-odd block B_ij = u_i' W u_j (banked pipeline)")
print("=" * 88)
B = np.array([[np.conj(U[:, i]) @ W_weld @ U[:, j] for j in range(2)] for i in range(2)])
banked = 1 / (2 * PHI) + 1j * math.sin(2 * math.pi / 5) / math.sqrt(5)
print(f"B[0,0] = {B[0,0]:+.6f}   banked B593 element = {banked:+.6f}   "
      f"match: {abs(B[0,0]-banked) < 1e-12}")
print(f"B[1,1] = {B[1,1]:+.6f}   == conj(B[0,0]): {abs(B[1,1]-np.conj(B[0,0])) < 1e-12}")
print(f"B[0,1] = {B[0,1]:+.6f}   B[1,0] = {B[1,0]:+.6f}")
offdiag = max(abs(B[0, 1]), abs(B[1, 0]))
print(f"max |off-diagonal| = {offdiag:.3e}")

print("=" * 88)
print("CELL 2 -- chat-1's eigenvalue claim: are the block's eigenvalues e^{+-i 108deg}?")
print("=" * 88)
evals, evecs = np.linalg.eig(B)
target = cmath.exp(1j * math.radians(108))
print(f"eigenvalues of B: {evals[0]:+.6f}, {evals[1]:+.6f}")
print(f"|lambda_1| = {abs(evals[0]):.6f}, |lambda_2| = {abs(evals[1]):.6f}   (unit modulus? "
      f"{abs(abs(evals[0])-1) < 1e-9 and abs(abs(evals[1])-1) < 1e-9})")
print(f"e^(i 108deg) = {target:+.6f}; claimed real part cos(108deg) = {math.cos(math.radians(108)):+.6f}")
claim_holds = all(min(abs(ev - target), abs(ev - np.conj(target))) < 1e-6 for ev in evals)
print(f"CLAIM 'eigenvalues are e^(+-i 108deg)': {claim_holds}")
tr = B[0, 0] + B[1, 1]
print(f"trace(B) = {tr:+.6f}  (= 2*Re(banked element) = +1/phi = {1/PHI:+.6f}; chat-1 "
      f"asserted tr_odd = -1/phi = 2cos(108deg) = {2*math.cos(math.radians(108)):+.6f})")

print("=" * 88)
print("CELL 3 -- mixing is eigenvector-anchored: same spectrum, different mixing (demo)")
print("=" * 88)
H1 = np.diag([1.0, 2.0])
th = math.pi / 7
Q = np.array([[math.cos(th), -math.sin(th)], [math.sin(th), math.cos(th)]])
H2 = Q @ H1 @ Q.T
e1, e2 = np.linalg.eigvalsh(H1), np.linalg.eigvalsh(H2)
v2 = np.linalg.eigh(H2)[1]
print(f"H1, H2 spectra identical: {np.allclose(e1, e2)}")
print(f"H1 mixing vs e-basis: |<e1|v1>|^2 = 1.000000 (diagonal)")
print(f"H2 mixing vs e-basis: |<e1|v1>|^2 = {abs(v2[0,0])**2:.6f} = cos^2(pi/7) = "
      f"{math.cos(th)**2:.6f}")
print("=> identical eigenvalues, different mixing: mixing angles are what eigenvalues")
print("   DON'T determine; 'basis-independent eigenphase' is a category error as a mixing analogue.")

print("=" * 88)
print("CELL 4 -- the kind-correct object: the overlap matrix P_ij = |<u_i|w_j>|^2")
print("=" * 88)
normality = np.linalg.norm(B @ B.conj().T - B.conj().T @ B)
print(f"||[B, B^dag]|| = {normality:.3e}  (normal block <=> orthogonal eigenvectors)")
P = np.zeros((2, 2))
for j in range(2):
    wv = evecs[:, j] / np.linalg.norm(evecs[:, j])
    for i in range(2):
        ei = np.zeros(2, dtype=complex); ei[i] = 1
        P[i, j] = abs(np.vdot(ei, wv)) ** 2
print("P = |<u_i|w_j>|^2 =")
print(np.array2string(P, precision=6))
print(f"row sums = {P.sum(axis=1)}, col sums = {P.sum(axis=0)}")
print("(recorded as PROGRAM-INTERNAL numbers; no SM comparison -- the stopping rule + the pin)")

print("=" * 88)
print("CELL 5 -- the one-number pin: co-signed (ledger line in HINT_LEDGER)")
print("=" * 88)
print("ADJUDICATION COMPLETE")
