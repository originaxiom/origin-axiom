"""Referee B1808, check 6: the real-multiplication classes (the rational part of H^2 where Lambda^2(A (x) I) has
eigenvalues phi^{+-4}) are (1,1) on the whole family, orthogonal to Lambda_A, of signature (1,1), and contain Kahler
classes on H x H; so the zero-FI D-term J.F = 0 holds for every invariant flux F with J in that plane -- the frame's
obstruction is that no Kahler class is A-INVARIANT (A cannot be an isometry), not the flux's D-term."""
import itertools, random
import sympy as sp, numpy as np
PAIRS = list(itertools.combinations(range(4), 2))
def ps(seq):
    s, a = 1, list(seq)
    for i in range(4):
        for j in range(i + 1, 4):
            if a[i] > a[j]: s = -s
            elif a[i] == a[j]: return 0
    return s
def wedge(F, G): return sum(F[p] * G[q] * ps(p + q) for p in PAIRS for q in PAIRS)
A = sp.Matrix([[1, 1], [1, 2]]); g = sp.Matrix(sp.BlockMatrix([[A[i, j] * sp.eye(2) for j in range(2)] for i in range(2)]))
C = sp.zeros(6, 6)
for a, (i, j) in enumerate(PAIRS):
    for b, (k, l) in enumerate(PAIRS):
        C[a, b] = g[i, k] * g[j, l] - g[i, l] * g[j, k]
T = C.T  # action on 2-form coefficient vectors
# rational RM lattice: kernel of (T^2 - 7T + I) (phi^4 + phi^-4 = 7)
RM = (T * T - 7 * T + sp.eye(6)).nullspace()
INV = (T - sp.eye(6)).nullspace()
print("rank RM (eigenvalues phi^{+-4}):", len(RM), "; rank Lambda_A:", len(INV))
vec = lambda v: {p: v[k] for k, p in enumerate(PAIRS)}
print("Q(RM, Lambda_A) all zero:", all(wedge(vec(r), vec(s)) == 0 for r in RM for s in INV))
Grm = sp.Matrix(len(RM), len(RM), lambda a, b: wedge(vec(RM[a]), vec(RM[b])))
print("Gram on RM:", Grm.tolist(), "eigen signs:", [int(sp.sign(e)) for e in Grm.evalf().eigenvals(multiple=True)])
phi = (1 + 5 ** 0.5) / 2
random.seed(3); ok = True; kahler = 0
for _ in range(20):
    z1 = complex(random.uniform(-2, 2), random.uniform(0.2, 3)); z2 = complex(random.uniform(-2, 2), random.uniform(0.2, 3))
    dzp = [1, z1, phi, phi * z1]; dzm = [1, z2, 1 - phi, (1 - phi) * z2]
    Om = {p: dzp[p[0]] * dzm[p[1]] - dzp[p[1]] * dzm[p[0]] for p in PAIRS}
    for r in RM:
        ok &= abs(wedge(vec([float(x) for x in r]), Om)) < 1e-9
    # Hermitian form of a positive RM class: J = combination with J^2 > 0
    P = np.array([dzp, dzm], dtype=complex); V = np.linalg.inv(np.vstack([P, P.conj()]))
    for cc in ((1, 0), (0, 1), (1, 1), (1, -1), (2, 1), (1, 2)):
        J = sum(c * np.array([float(x) for x in r]) for c, r in zip(cc, RM))
        if wedge(vec(J), vec(J)) <= 0: continue
        F = np.zeros((4, 4))
        for k, (i, j) in enumerate(PAIRS): F[i, j] = J[k]; F[j, i] = -J[k]
        h = -1j * (V.T @ F @ V)[0:2, 2:4]; h = (h + h.conj().T) / 2
        e = np.linalg.eigvalsh(h)
        kahler += int(all(e > 0) or all(e < 0))
print("RM classes (1,1) at 20 random points of H x H:", bool(ok), "; positive RM classes with definite Hermitian form:", kahler)
