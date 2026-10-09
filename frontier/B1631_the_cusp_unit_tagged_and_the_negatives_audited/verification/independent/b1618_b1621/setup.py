import itertools
import numpy as np

w = np.exp(2j * np.pi / 3)


def perm_sign(p):
    s = 1
    p = list(p)
    for i in range(3):
        for j in range(i + 1, 3):
            if p[i] > p[j]:
                s = -s
    return s


def signed_perms_det1():
    out = []
    for p in itertools.permutations(range(3)):
        for s in itertools.product([1, -1], repeat=3):
            S = np.zeros((3, 3))
            for i in range(3):
                S[p[i], i] = s[i]
            if round(np.linalg.det(S)) == 1:
                out.append((S, perm_sign(p), p, s))
    return out


def build_G():
    G = []
    for S, sg, p, s in signed_perms_det1():
        for m in range(8):
            z = np.exp(2j * np.pi * m / 8)
            if abs(z ** 4 - sg) < 1e-9:
                G.append((z * S, z, S, sg))
    return G


def in_group(g, G, tol=1e-9):
    return any(np.allclose(g, h[0], atol=tol) for h in G)


def tensor_ops(g):
    """action of g on 3x3 matrix M for the three tensors"""
    return {
        'Dirac(Tbar x T)': lambda M: g.conj().T @ M @ g,
        'TxT': lambda M: g.T @ M @ g,
        'Sym2': lambda M: g.T @ M @ g,
    }


def op_matrix(f, basis):
    """matrix of linear map f in the given basis (list of 3x3), expressed in same basis
    via least squares; also returns residual to check closure"""
    B = np.array([b.flatten() for b in basis]).T  # 9 x n
    cols = []
    res = 0
    for b in basis:
        v = f(b).flatten()
        c, *_ = np.linalg.lstsq(B, v, rcond=None)
        res = max(res, np.linalg.norm(B @ c - v))
        cols.append(c)
    return np.array(cols).T, res


def E(i, j):
    M = np.zeros((3, 3), dtype=complex)
    M[i, j] = 1
    return M


full_basis = [E(i, j) for i in range(3) for j in range(3)]
sym_basis = [E(i, i) for i in range(3)] + [E(i, j) + E(j, i) for i in range(3) for j in range(i + 1, 3)]
diag_basis = [E(i, i) for i in range(3)]

a_in = np.diag([-1.0, 1.0, -1.0]).astype(complex)
b_in = np.diag([1.0, -1.0, -1.0]).astype(complex)
P = np.zeros((3, 3), dtype=complex)  # 3-cycle: e_i -> e_{i+1}
for i in range(3):
    P[(i + 1) % 3, i] = 1
U = 1j * P
