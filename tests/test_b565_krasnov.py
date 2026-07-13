"""
B565 H1(i) -- Krasnov EXPLICIT: Spin(9) on O^2=R^16, so(9) centralizer of the
complex structure J_R = right-multiplication by a unit imaginary octonion on
each O factor.

Reproduces (Krasnov, "SO(9) characterisation of the Standard Model gauge
group", arXiv:1912.11282):
  - Cl_9 realized as X(r,x) = [[r, L_x],[L_xbar,-r]]  (octonion left mult)
  - Theorem 1: centraliser of J_R = diag(R_i,R_i) in Spin(9) is G_SM = S(U(3)xU(2))
    i.e. so(9)-centralizer has Lie algebra su(3)+su(2)+u(1), dim 12, rank 4.
  - Cross-check (paper, Sec.1): centralizer of J_L = diag(L_i,L_i) is
    su(2)+su(4), dim 3+15=18.

Pure numpy linear algebra on 8x8 / 16x16 real matrices, octonions built from
scratch via Cayley-Dickson doubling (verified division/alternative algebra).
"""
import numpy as np
import pytest


# =====================================================================
# Octonions via Cayley-Dickson doubling from R
# =====================================================================
def conj(x):
    x = np.asarray(x, dtype=float)
    if len(x) == 1:
        return x.copy()
    n = len(x) // 2
    a, b = x[:n], x[n:]
    return np.concatenate([conj(a), -b])


def mult(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    if len(x) == 1:
        return x * y
    n = len(x) // 2
    a, c = x[:n], y[:n]
    b, d = x[n:], y[n:]
    real_part = mult(a, c) - mult(conj(d), b)
    imag_part = mult(d, a) + mult(b, conj(c))
    return np.concatenate([real_part, imag_part])


DIM = 8
E = [np.eye(DIM)[i] for i in range(DIM)]  # e0=1, e1..e7 imaginary units


def left_mult_matrix(u):
    return np.stack([mult(u, E[j]) for j in range(DIM)], axis=1)


def right_mult_matrix(u):
    return np.stack([mult(E[j], u) for j in range(DIM)], axis=1)


L = [left_mult_matrix(E[i]) for i in range(DIM)]

I8 = np.eye(8)
Z8 = np.zeros((8, 8))
I16 = np.eye(16)


def offdiag(A, B):
    return np.block([[Z8, A], [B, Z8]])


# Gamma_1..Gamma_8 <-> e0..e7 (octonion left mult), Gamma_9 = grading diag(I,-I)
Gamma = [offdiag(L[i], L[i].T) for i in range(8)]
Gamma.append(np.block([[I8, Z8], [Z8, -I8]]))

pairs = [(i, j) for i in range(9) for j in range(i + 1, 9)]
Gij = {p: 0.5 * (Gamma[p[0]] @ Gamma[p[1]] - Gamma[p[1]] @ Gamma[p[0]]) for p in pairs}


def bracket(A, B):
    return A @ B - B @ A


def centralizer_of(J, tol=1e-8):
    """dim + orthonormal 16x16 basis of {X in span(Gij) : [X,J]=0}."""
    comm_rows = [(Gij[p] @ J - J @ Gij[p]).flatten() for p in pairs]
    A = np.stack(comm_rows, axis=0).T  # 256 x 36
    U, S, Vt = np.linalg.svd(A)
    thresh = tol * max(A.shape) * (S[0] if len(S) else 1.0)
    rank = int(np.sum(S > thresh))
    nullity = A.shape[1] - rank
    null_coeffs = Vt[rank:, :]
    Cent = [sum(row[k] * Gij[pairs[k]] for k in range(36)) for row in null_coeffs]
    if Cent:
        Cflat = np.stack([X.flatten() for X in Cent], axis=0)
        Q, _ = np.linalg.qr(Cflat.T)
        Cent = [Q[:, k].reshape(16, 16) for k in range(nullity)]
    return nullity, Cent


def lie_algebra_data(basis):
    """Given an orthonormal closed matrix basis, return structure constants,
    ad matrices, center dim, derived-algebra dim, Killing eigenvalues, rank."""
    n = len(basis)
    basis = np.stack(basis, axis=0)
    F = np.zeros((n, n, n))
    for a in range(n):
        for b in range(n):
            Cab = bracket(basis[a], basis[b])
            F[a, b, :] = np.einsum('cij,ij->c', basis, Cab)
    ad = np.stack([F[a].T for a in range(n)], axis=0)  # ad[a][c,b] = F[a,b,c]

    # center: w s.t. sum_a w_a ad_a = 0
    Amat = ad.reshape(n, n * n).T
    _, S, Vt = np.linalg.svd(Amat)
    tol = 1e-8 * max(Amat.shape) * (S[0] if len(S) else 1.0)
    rank_map = int(np.sum(S > tol))
    dim_center = n - rank_map

    # derived algebra = image of bracket
    bracket_vectors = F.reshape(n * n, n)
    dim_derived = int(np.linalg.matrix_rank(bracket_vectors, tol=1e-8))

    # Killing form
    K = np.einsum('aij,bji->ab', ad, ad)
    K = 0.5 * (K + K.T)
    eigvals = np.sort(np.linalg.eigvalsh(K))

    # rank(g) = min nullity of ad_X over random X (regular element)
    rng = np.random.default_rng(0)
    min_nullity = n
    for _ in range(20):
        x = rng.normal(size=n)
        ad_X = np.einsum('a,acb->cb', x, ad)
        rk = np.linalg.matrix_rank(ad_X, tol=1e-8)
        min_nullity = min(min_nullity, n - rk)

    return dict(n=n, ad=ad, dim_center=dim_center, dim_derived=dim_derived,
                killing_eigs=eigvals, rank_g=min_nullity)


# =====================================================================
# Fixtures / shared computation
# =====================================================================
@pytest.fixture(scope="module")
def octonion_sanity():
    rng = np.random.default_rng(0)
    for _ in range(20):
        x = rng.normal(size=8)
        y = rng.normal(size=8)
        xy = mult(x, y)
        assert abs(np.dot(xy, xy) - np.dot(x, x) * np.dot(y, y)) < 1e-8
        assert np.allclose(mult(x, mult(x, y)), mult(mult(x, x), y), atol=1e-8)
    return True


@pytest.fixture(scope="module")
def clifford9():
    max_err = 0.0
    for i in range(9):
        for j in range(9):
            anti = Gamma[i] @ Gamma[j] + Gamma[j] @ Gamma[i]
            target = 2 * I16 if i == j else np.zeros((16, 16))
            max_err = max(max_err, np.max(np.abs(anti - target)))
    return max_err


@pytest.fixture(scope="module")
def so9_rank():
    M = np.stack([Gij[p].flatten() for p in pairs], axis=0)
    return np.linalg.matrix_rank(M, tol=1e-8)


# =====================================================================
# Tests
# =====================================================================
def test_octonion_algebra_valid(octonion_sanity):
    assert octonion_sanity is True


def test_clifford9_relations(clifford9):
    assert clifford9 < 1e-8


def test_so9_generators_linearly_independent(so9_rank):
    assert so9_rank == 36


def test_JR_centralizer_dimension_is_12():
    R1 = right_mult_matrix(E[1])
    JR = np.block([[R1, Z8], [Z8, R1]])
    assert np.max(np.abs(JR @ JR + I16)) < 1e-8   # JR^2 = -I
    dim, basis = centralizer_of(JR)
    assert dim == 12


def test_JR_centralizer_type_su3_su2_u1():
    R1 = right_mult_matrix(E[1])
    JR = np.block([[R1, Z8], [Z8, R1]])
    dim, basis = centralizer_of(JR)
    assert dim == 12
    data = lie_algebra_data(basis)
    assert data["dim_center"] == 1
    assert data["dim_derived"] == 11
    # Killing eigenvalues: 8 equal (su(3) block), 3 equal (su(2) block), 1 zero (center)
    eigs = data["killing_eigs"]
    n_zero = int(np.sum(np.abs(eigs) < 1e-6))
    assert n_zero == 1
    nonzero = np.sort(eigs[np.abs(eigs) > 1e-6])
    # cluster the 11 nonzero eigenvalues
    clusters = []
    cur = [nonzero[0]]
    for v in nonzero[1:]:
        if abs(v - cur[-1]) < 1e-4:
            cur.append(v)
        else:
            clusters.append(cur)
            cur = [v]
    clusters.append(cur)
    block_sizes = sorted(len(c) for c in clusters)
    assert block_sizes == [3, 8]   # su(2) (dim3) + su(3) (dim8)
    # rank-4 check: rank(g) = rank(u(1)) + rank(su(2)) + rank(su(3)) = 1+1+2 = 4
    assert data["rank_g"] == 4


def test_JL_centralizer_cross_check_su2_su4():
    """Independent validation of the whole pipeline against the literature:
    Krasnov (1912.11282) states the centralizer of J_L=diag(L_i,L_i) in
    Spin(9) is SU(2)xSU(4)/Z2, dim 3+15=18 -- this does NOT depend on the
    J_R tuning used for the SM-group result, so matching it here confirms
    the Gamma-matrix / octonion construction itself is correct."""
    L1 = left_mult_matrix(E[1])
    JL = np.block([[L1, Z8], [Z8, L1]])
    assert np.max(np.abs(JL @ JL + I16)) < 1e-8
    dim, basis = centralizer_of(JL)
    assert dim == 18


if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, "-v"]))
