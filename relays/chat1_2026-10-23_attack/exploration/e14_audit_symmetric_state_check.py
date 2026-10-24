#!/usr/bin/env python3
"""e14 (data-free; a non-authoring check, at the audit lane's request): the algebra of the lane's note
SYMMETRIC_STATE_REALIZATION_AND_MATTER_TRACE.md (audit/physical-bridge-2026-09-05 @ dff9478a9), equations (1)-(6), on
chat1's own code, with B1656's conventions copied from its verification script (main,
frontier/B1656_the_electrons_zero/verification/the_electrons_zero.py lines 33-34, 100-101, 130-139, 284):
  QI = diag(i, -i), QJ = EPS = [[0, 1], [-1, 0]], QK = QI QJ; ell_s(M) = sum_mn (EPS C_s)_mn M_mn (pair_mp);
  weighted_M(u) = sum_s u_s EDUAL_s with EDUAL the dual basis of ell (dual_basis); u_s = sqrt(2 pi L + c_s) R_s.
Checks (each a largest deviation over random draws, numpy, seed 14):
  C1  g^T EPS = EPS g^-1 for g = QI, QJ and random SU(2); hence M' = b g M g^T gives N' = b g N g^-1 for N = M EPS  (1)
  C2  the joint commutant of QI and QJ in M_2(C) is span(I) (dimension by SVD)                                     (2)
  C3  sum_s ell_s(M)^2 = 4 det M for random M; for rank one M = p q^T the sum vanishes                          (4)
  C4  ell_s(n EPS^-1) = (-2n, 0, 0, 0)                                                                        (5)
  C5  ell_s(weighted_M(u)) = u_s; EDUAL Hilbert-Schmidt orthogonal with squared norm 1/2; ||M||^2 = (1/2) sum |u_s|^2;
      dist(M, span EPS^-1)^2 = (1/2) sum_(i,j,k) |u_s|^2
  C6  (5a): for random rank-one M_raw = p q^T and random positive weights, dist/||M|| >= eta/sqrt(1 + eta^2), eta the
      least w_s/w_1 over nonzero imaginary channels; its smallest margin; the sharp case R = (1, i, 0, 0),
      w = (1, delta, 1, 1) at delta = 0.1, 0.5, 2 against delta/sqrt(1 + delta^2)
  C7  (6): P_M = M M^dag / tr(M M^dag) has P_(b g M g^T) = g P_M g^dag for random unitary g and complex b
  C8  the weak-centre step: conjugation by -I fixes every 2 x 2 matrix (End(C^2) is even under the centre)
    python3 -B e14_audit_symmetric_state_check.py     # writes e14_audit_symmetric_state_check_out.txt"""
import pathlib
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
rng = np.random.default_rng(14)
QI = np.array([[1j, 0], [0, -1j]]); QJ = np.array([[0, 1], [-1, 0]], dtype=complex); QK = QI @ QJ; EPS = QJ
UNITS = {"1": np.eye(2, dtype=complex), "i": QI, "j": QJ, "k": QK}
EC = {s: EPS @ C for s, C in UNITS.items()}


def ell(M):
    return np.array([np.sum(EC[s] * M) for s in UNITS])


def dual_basis():
    G = np.array([[np.sum(EC[t] * UNITS[s]) for s in UNITS] for t in UNITS])
    Gi = np.linalg.inv(G); keys = list(UNITS)
    return [sum(Gi[b, a] * UNITS[keys[b]] for b in range(4)) for a in range(4)]


ED = dual_basis()
def weighted_M(u):
    return sum(u[a] * ED[a] for a in range(4))


def rand_su2():
    z = rng.normal(size=4); z /= np.linalg.norm(z)
    return np.array([[z[0] + 1j * z[1], z[2] + 1j * z[3]], [-z[2] + 1j * z[3], z[0] - 1j * z[1]]])


def rand_u2():
    A = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)); Q, R = np.linalg.qr(A)
    return Q @ np.diag(np.diag(R) / np.abs(np.diag(R)))


def cm():
    return rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))


out = []
# C1
w1 = 0.0
for g in [QI, QJ] + [rand_su2() for _ in range(200)]:
    w1 = max(w1, float(np.max(np.abs(g.T @ EPS - EPS @ np.linalg.inv(g)))))
    M = cm(); b = complex(*rng.normal(size=2)); Mp = b * g @ M @ g.T
    w1 = max(w1, float(np.max(np.abs(Mp @ EPS - b * g @ (M @ EPS) @ np.linalg.inv(g)))))
out.append(f"C1 g^T EPS = EPS g^-1 and N' = b g N g^-1: largest deviation {w1:.2e}")
# C2
cols = []
for a in range(2):
    for c in range(2):
        E = np.zeros((2, 2), dtype=complex); E[a, c] = 1
        cols.append(np.concatenate([(g @ E - E @ g).ravel() for g in (QI, QJ)]))
A = np.array(cols).T                                   # 8 x 4: column = both commutators of one matrix unit
sv = np.linalg.svd(A, compute_uv=False)
null = int(np.sum(sv < 1e-12))
_, _, Vh = np.linalg.svd(A); v = Vh[-1].conj().reshape(2, 2); v = v / v[0, 0]
out.append(f"C2 joint commutant of QI and QJ: dimension {null}; its element normalised: {np.round(v, 12).tolist()}")
# C3
w3, w3r = 0.0, 0.0
for _ in range(1000):
    M = cm(); w3 = max(w3, float(abs(np.sum(ell(M) ** 2) - 4 * np.linalg.det(M)) / np.sum(np.abs(M) ** 2)))
    p, q = rng.normal(size=2) + 1j * rng.normal(size=2), rng.normal(size=2) + 1j * rng.normal(size=2)
    R = ell(np.outer(p, q)); w3r = max(w3r, float(abs(np.sum(R ** 2)) / np.sum(np.abs(R) ** 2)))
out.append(f"C3 sum ell_s^2 = 4 det M: largest relative deviation {w3:.2e}; rank-one |sum R_s^2|/sum|R_s|^2: largest {w3r:.2e}")
# C4
n = complex(*rng.normal(size=2))
out.append(f"C4 ell_s(n EPS^-1)/n = {np.round(ell(n * np.linalg.inv(EPS)) / n, 14).tolist()}")
# C5
w5a = max(float(np.max(np.abs(ell(weighted_M(u)) - u))) for u in (rng.normal(size=4) + 1j * rng.normal(size=4) for _ in range(200)))
gram = np.array([[np.sum(np.conj(ED[a]) * ED[b]) for b in range(4)] for a in range(4)])
w5b, w5c = 0.0, 0.0
C = np.linalg.inv(EPS) / np.linalg.norm(np.linalg.inv(EPS))
for _ in range(200):
    u = rng.normal(size=4) + 1j * rng.normal(size=4); M = weighted_M(u)
    w5b = max(w5b, abs(float(np.sum(np.abs(M) ** 2)) - 0.5 * float(np.sum(np.abs(u) ** 2))))
    d2 = float(np.sum(np.abs(M - np.sum(np.conj(C) * M) * C) ** 2))
    w5c = max(w5c, abs(d2 - 0.5 * float(np.sum(np.abs(u[1:]) ** 2))))
out.append(f"C5 ell(weighted_M(u)) = u: {w5a:.2e}; EDUAL's Hermitian Gram: {np.round(gram, 12).tolist()}; "
           f"||M||^2 = |u|^2/2: {w5b:.2e}; dist^2 = (|u_i|^2 + |u_j|^2 + |u_k|^2)/2: {w5c:.2e}")
# C6
margin, worst = np.inf, None
for _ in range(20000):
    p, q = rng.normal(size=2) + 1j * rng.normal(size=2), rng.normal(size=2) + 1j * rng.normal(size=2)
    R = ell(np.outer(p, q)); w = np.exp(rng.uniform(-3, 3, size=4)); u = w * R; M = weighted_M(u)
    nz = [a for a in (1, 2, 3) if abs(R[a]) > 1e-12]
    eta = min(w[a] / w[0] for a in nz)
    ratio = float(np.sqrt(0.5 * np.sum(np.abs(u[1:]) ** 2)) / np.linalg.norm(M))
    m = ratio - eta / np.sqrt(1 + eta ** 2)
    if m < margin:
        margin, worst = m, (ratio, float(eta))
sharp = []
for de in (0.1, 0.5, 2.0):
    u = np.array([1, 1j * de, 0, 0]); M = weighted_M(u)
    sharp.append([de, float(np.sqrt(0.5 * np.sum(np.abs(u[1:]) ** 2)) / np.linalg.norm(M)), de / np.sqrt(1 + de ** 2)])
out.append(f"C6 (5a) on 20 000 random rank-one residues and weights: smallest margin {margin:.3e} (ratio, eta there: "
           f"{worst[0]:.4f}, {worst[1]:.4f}); sharp case (delta, ratio, delta/sqrt(1+delta^2)): {np.round(sharp, 12).tolist()}")
# C7
w7 = 0.0
for _ in range(200):
    M = np.outer(rng.normal(size=2) + 1j * rng.normal(size=2), rng.normal(size=2) + 1j * rng.normal(size=2))
    g = rand_u2(); b = complex(*rng.normal(size=2))
    P = lambda X: X @ X.conj().T / np.trace(X @ X.conj().T)
    w7 = max(w7, float(np.max(np.abs(P(b * g @ M @ g.T) - g @ P(M) @ g.conj().T))))
out.append(f"C7 P_(b g M g^T) = g P_M g^dag (unitary g): largest deviation {w7:.2e}")
# C8
w8 = max(float(np.max(np.abs((-np.eye(2)) @ X @ np.linalg.inv(-np.eye(2)) - X))) for X in (cm() for _ in range(10)))
out.append(f"C8 conjugation by -I fixes End(C^2): largest deviation {w8:.2e}")
(HERE / "e14_audit_symmetric_state_check_out.txt").write_text("\n".join(out) + "\n")
print("written")
