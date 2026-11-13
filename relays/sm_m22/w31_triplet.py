# M22: for each flux m, which icosahedral triplet (3 or 3') carries W31's 3-piece. The pair (C5^m, S5); the moves'
# lifts U_L, U_R solve U A U^-1 = A', U B U^-1 = B'; the 3-piece is an eigenspace of the lift of (L R^-1 L)^2;
# on it, U_L normalised to order 5 has trace phi = (1+sqrt5)/2 (one class) or 1 - phi (the other).
import numpy as np, itertools
z = np.exp(2j*np.pi/5); phi = (1+5**.5)/2
C = np.diag([z**k for k in range(5)]); S = np.roll(np.eye(5), 1, axis=0)
def lift(A, B, A2, B2):
    # solve U A = A2 U, U B = B2 U  (vec form, column-major)
    I = np.eye(5)
    M = np.vstack([np.kron(A.T, I) - np.kron(I, A2), np.kron(B.T, I) - np.kron(I, B2)])
    _, s, vh = np.linalg.svd(M); u = vh[-1].conj().reshape(5, 5).T
    return u / np.linalg.det(u) ** (1/5)
for m in (1, 2, 3, 4):
    A = np.linalg.matrix_power(C, m); B = S
    UL = lift(A, B, A, B @ A)           # L: (A, B) -> (A, B A)
    UR = lift(A, B, A @ B, B)           # R: (A, B) -> (A B, B)
    W = UL @ np.linalg.inv(UR) @ UL; W2 = W @ W
    ev, V = np.linalg.eig(W2)
    # group eigenvalues (up to phase the reflection has two eigenvalues)
    vals = np.round(ev, 6); groups = {}
    for i, e in enumerate(ev):
        key = next((k for k in groups if abs(k - e) < 1e-6), e); groups.setdefault(key, []).append(i)
    three = next(ix for ix in groups.values() if len(ix) == 3)
    P = V[:, three]; Q = np.linalg.pinv(P)
    L3 = Q @ UL @ P
    # check invariance, normalise to det 1 and order 5
    assert np.allclose(UL @ P, P @ L3, atol=1e-8)
    L3 = L3 / np.linalg.det(L3) ** (1/3)
    best = None
    for j in range(3):
        Lj = L3 * np.exp(2j*np.pi*j/3)
        if np.allclose(np.linalg.matrix_power(Lj, 5), np.eye(3), atol=1e-6): best = Lj
    tr = np.trace(best)
    sq = m in (1, 4)
    print("flux m=%d (%s mod 5): tr(L) on the 3-piece = %.6f%+.6fj  -> %s" % (m, "square" if sq else "non-square", tr.real, tr.imag,
          "phi" if abs(tr - phi) < 1e-6 else "1-phi" if abs(tr - (1 - phi)) < 1e-6 else "?"))
