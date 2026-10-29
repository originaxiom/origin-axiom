"""Zero-asymptotic-charge junction lattice of A^(N-1)BCC with (J,J) = -sum Q_i^2 + s*sum_{i<j} Q_iQ_j (z_i x z_j);
s = +-1 fixed by E8 (N=8) being even unimodular negative definite. Report det, signature; nesting is by restriction."""
import sympy as sp, json
def cross(z1, z2): return z1[0]*z2[1] - z2[0]*z1[1]
def lattice(N, s):
    zs = [(1, 0)] * (N - 1) + [(1, -1), (1, 1), (1, 1)]
    n = len(zs)
    G = sp.zeros(n, n)
    for i in range(n):
        G[i, i] = -2
        for j in range(i + 1, n):
            G[i, j] = G[j, i] = s * cross(zs[i], zs[j])
    # bilinear form: (J,J) = J^T (G/2) J  with diag -1 -> use G as 2x the form; then (J,J)=J^T G J /2
    Z = sp.Matrix([[z[0] for z in zs], [z[1] for z in zs]])
    ker = Z.nullspace()
    # integral basis of the kernel lattice via Smith/HNF: use sympy's 'nullspace' rational -> clear and saturate
    from sympy.matrices.normalforms import hermite_normal_form
    import itertools
    # integer kernel basis by LLL-free approach: columns of unimodular transform
    M = Z.T  # n x 2 ; find integer kernel of Z (2 x n)
    # use smith via sympy: Z * U = [H|0]
    from sympy import Matrix
    A = Z.copy(); U = sp.eye(n)
    # column operations to reduce Z to [h 0 ...]
    def colop(A, U):
        A = A.copy(); U = U.copy(); r = 0
        for row in range(2):
            while True:
                nz = [c for c in range(r, n) if A[row, c] != 0]
                if not nz: break
                piv = min(nz, key=lambda c: abs(A[row, c]))
                A.col_swap(r, piv); U.col_swap(r, piv)
                done = True
                for c in range(r + 1, n):
                    if A[row, c] != 0:
                        q = A[row, c] // A[row, r]
                        A[:, c] = A[:, c] - q * A[:, r]; U[:, c] = U[:, c] - q * U[:, r]
                        if A[row, c] != 0: done = False
                if done: break
            if any(A[row, c] != 0 for c in range(r, n)) or A[row, r] != 0: r += 1
        return A, U, r
    A2, U2, r = colop(A, U)
    K = U2[:, r:]
    assert (Z * K).is_zero_matrix
    Gram = (K.T * G * K) / 2   # (J,J) for basis junctions; off-diagonal = (J_a, J_b)
    Gram2 = K.T * G * K        # integer, = 2 x form
    import numpy as np
    ev = list(np.linalg.eigvalsh(np.array(Gram.tolist(), dtype=float)))
    pos = sum(1 for e in ev if e > 1e-9); neg = sum(1 for e in ev if e < -1e-9); zero = len(ev) - pos - neg
    return {"rank": K.shape[1], "det(-Gram)": int(sp.Matrix(-Gram).det()) if K.shape[1] else 1,
            "signature(+,-,0) of -Gram": (pos and neg, ) and (neg, pos, zero),
            "even": all((K[:, i].T * G * K[:, i])[0] % 4 == 0 for i in range(K.shape[1]))}
out = {}
for s in (1, -1):
    out[s] = {N: lattice(N, s) for N in range(1, 13)}
print(json.dumps(out, indent=0, default=str))
json.dump(out, open(__import__("pathlib").Path(__file__).with_name("junctions.json"), "w"), indent=1, default=str)
