#!/usr/bin/env python3
"""B1362 -- THE HIERARCHY IS A U(1)-BREAKING EFFECT AT ORDER ONE.

(1) A deck-symmetric complex symmetric 3x3 Yukawa (invariant under the cyclic permutation of the three generations) is a symmetric
    circulant circ(x, y, y): its eigenvalues are x + 2y, x - y, x - y (symbolic) -- a degenerate pair -- so the deck must be broken
    for any hierarchy.
(2) The hollow leading texture is robust: for M = M_0 + E with M_0 hollow symmetric (sigma_1 = sigma_2 + sigma_3, B1361) Weyl's
    inequality |sigma_i(M) - sigma_i(M_0)| <= ||E||_op gives  m_3 - m_2 - m_1 <= 3 ||E||_op, i.e. the U(1)^2-violating part of the
    mass matrix has operator norm at least (m_3 - m_2 - m_1)/3 in every charged sector.
(3) The bound is nearly attained: for a symmetric target M = U Sigma U^T (Takagi) the nearest hollow symmetric matrix is M minus its
    diagonal, so the minimal ||E|| over textures equals min_U max_i |(U Sigma U^T)_ii|; we minimise this numerically over unitaries
    for the data singular values and compare with the bound and with m_3/3.
"""
import numpy as np, sympy as sp

print("=" * 96)
print("(1) deck-symmetric Yukawa: symmetric circulant circ(x, y, y)")
print("=" * 96)
x, y = sp.symbols('x y')
C = sp.Matrix([[x, y, y], [y, x, y], [y, y, x]])
ev = C.eigenvals()
print(f"  eigenvalues of circ(x,y,y): {dict(ev)}  -> a degenerate pair x - y (multiplicity 2): {ev.get(x - y, 0) == 2}")
print("  hence two of the three masses coincide for any deck-symmetric symmetric texture: the deck must be broken by the vevs or the spurions.")

print("\n" + "=" * 96)
print("(2) Weyl's bound on the U(1)^2-violating part E = M - M_0, M_0 hollow symmetric")
print("=" * 96)
data = {"up": (1.3e-3, 0.63, 172.5), "down": (2.8e-3, 0.055, 2.86), "charged leptons": (0.000511, 0.1057, 1.777)}
for name, (m1, m2, m3) in data.items():
    bound = (m3 - m2 - m1) / 3
    print(f"  {name}: ||E||_op >= (m3 - m2 - m1)/3 = {bound:.4g} GeV = {bound/m3:.3f} m_3")

print("\n" + "=" * 96)
print("(3) the minimal violation for the data: min over unitaries U of max_i |(U Sigma U^T)_ii|, Sigma = diag(m1, m2, m3)")
print("=" * 96)
rng = np.random.default_rng(3)
def random_unitary(n):
    Z = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
    Q, R = np.linalg.qr(Z)
    return Q @ np.diag(np.diag(R) / np.abs(np.diag(R)))
def maxdiag(U, S):
    M = U @ np.diag(S) @ U.T
    return np.max(np.abs(np.diag(M)))
def unitary_from_params(p):
    # 9 real parameters -> Hermitian H -> U = expm(iH)
    H = np.zeros((3, 3), dtype=complex)
    k = 0
    for i in range(3):
        H[i, i] = p[k]; k += 1
    for i in range(3):
        for j in range(i + 1, 3):
            H[i, j] = p[k] + 1j * p[k + 1]; H[j, i] = np.conj(H[i, j]); k += 2
    w, V = np.linalg.eigh(H)
    return V @ np.diag(np.exp(1j * w)) @ V.conj().T
def minimise(S, restarts=60, iters=4000):
    best = np.inf
    for _ in range(restarts):
        p = rng.standard_normal(9) * 2
        f = maxdiag(unitary_from_params(p), S)
        step = 0.5
        for it in range(iters):
            q = p + rng.standard_normal(9) * step
            g = maxdiag(unitary_from_params(q), S)
            if g < f:
                p, f = q, g
            else:
                step *= 0.995
                if step < 1e-4:
                    step = 0.05
        best = min(best, f)
    return best
for name, (m1, m2, m3) in data.items():
    S = np.array([m1, m2, m3])
    val = minimise(S)
    print(f"  {name}: minimal max|M_ii| = {val:.5g} GeV = {val/m3:.4f} m_3  (Weyl bound {((m3 - m2 - m1)/3)/m3:.4f} m_3; the attained "
          f"minimum sits at m_3/3 up to the lighter masses)")
print("\n  so at least a third of the third-generation Yukawa must violate the apex U(1)s: the hierarchy is not a small correction to the hollow texture.")
print("\nDONE")
