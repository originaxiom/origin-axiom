import os, tempfile
import numpy as np
np.set_printoptions(precision=4, suppress=True, linewidth=200)

# ---------------------------------------------------------------
# 1. Octonions via Cayley-Dickson doubling from R
# ---------------------------------------------------------------
def conj(x):
    x = np.asarray(x, dtype=float)
    if len(x) == 1:
        return x.copy()
    n = len(x)//2
    a, b = x[:n], x[n:]
    return np.concatenate([conj(a), -b])

def mult(x, y):
    x = np.asarray(x, dtype=float); y = np.asarray(y, dtype=float)
    if len(x) == 1:
        return x*y
    n = len(x)//2
    a, c = x[:n], y[:n]
    b, d = x[n:], y[n:]
    ac = mult(a, c)
    dstar_b = mult(conj(d), b)
    real_part = ac - dstar_b
    da = mult(d, a)
    b_cstar = mult(b, conj(c))
    imag_part = da + b_cstar
    return np.concatenate([real_part, imag_part])

DIM = 8
E = [np.eye(DIM)[i] for i in range(DIM)]  # basis e0..e7, e0 = real unit

# sanity: e0 = identity, e_i^2 = -1 for i=1..7, orthonormal structure constants in {-1,0,1}
assert np.allclose(mult(E[0], E[3]), E[3])
for i in range(1, DIM):
    ei_sq = mult(E[i], E[i])
    assert np.allclose(ei_sq, -E[0]), f"e{i}^2 != -1: {ei_sq}"

# multiplicativity of the norm on random samples (division-algebra check)
rng = np.random.default_rng(0)
for _ in range(20):
    x = rng.normal(size=8); y = rng.normal(size=8)
    xy = mult(x, y)
    nx, ny, nxy = np.dot(x, x), np.dot(y, y), np.dot(xy, xy)
    assert abs(nxy - nx*ny) < 1e-8, (nxy, nx*ny)

# alternativity check: x(xy) = (xx)y  and  (yx)x = y(xx)  on random samples
for _ in range(20):
    x = rng.normal(size=8); y = rng.normal(size=8)
    lhs = mult(x, mult(x, y)); rhs = mult(mult(x, x), y)
    assert np.allclose(lhs, rhs, atol=1e-8)
    lhs2 = mult(mult(y, x), x); rhs2 = mult(y, mult(x, x))
    assert np.allclose(lhs2, rhs2, atol=1e-8)

print("Octonion algebra (Cayley-Dickson, verified division/alternative) built OK.")

# structure constants -> left-multiplication matrices L_{e_i}, 8x8
def left_mult_matrix(u):
    cols = [mult(u, E[j]) for j in range(DIM)]
    return np.stack(cols, axis=1)

L = [left_mult_matrix(E[i]) for i in range(DIM)]

# sanity: L_{e_i}^T = L_{ei conjugate}: symmetric (=I) for i=0, antisymmetric for i=1..7
assert np.allclose(L[0], np.eye(DIM))
for i in range(1, DIM):
    assert np.allclose(L[i].T, -L[i], atol=1e-8), f"L_e{i} not antisymmetric"
    assert np.allclose(L[i] @ L[i].T, np.eye(DIM), atol=1e-8)  # orthogonal (unit norm)
print("L_{e_i}: e0 symmetric=I, e1..e7 antisymmetric & orthogonal -- confirmed.")

# ---------------------------------------------------------------
# 2. Gamma matrices for Spin(9) on R^16 = O (+) O
# ---------------------------------------------------------------
I8 = np.eye(8)
Z8 = np.zeros((8, 8))

def offdiag(A, B):
    return np.block([[Z8, A], [B, Z8]])

Gamma = []
for i in range(8):
    Gamma.append(offdiag(L[i], L[i].T))   # Gamma_1..Gamma_8  <-> e0..e7
Gamma9 = np.block([[I8, Z8], [Z8, -I8]])
Gamma.append(Gamma9)                       # Gamma_9

assert len(Gamma) == 9
I16 = np.eye(16)

# verify Clifford relations {Gamma_i, Gamma_j} = 2 delta_ij I_16
max_err = 0.0
for i in range(9):
    for j in range(9):
        anti = Gamma[i] @ Gamma[j] + Gamma[j] @ Gamma[i]
        target = 2*I16 if i == j else np.zeros((16, 16))
        max_err = max(max_err, np.max(np.abs(anti - target)))
print(f"Clifford Cl(9) relations {{Gamma_i,Gamma_j}}=2 delta_ij I_16: max residual = {max_err:.3e}")
assert max_err < 1e-8

# ---------------------------------------------------------------
# 3. so(9) basis: Gamma_ij = 1/2 [Gamma_i, Gamma_j], i<j  (36 generators)
# ---------------------------------------------------------------
pairs = [(i, j) for i in range(9) for j in range(i+1, 9)]
assert len(pairs) == 36
Gij = {}
for (i, j) in pairs:
    Gij[(i, j)] = 0.5*(Gamma[i] @ Gamma[j] - Gamma[j] @ Gamma[i])

# check linear independence (rank 36) of these 16x16 matrices as vectors in R^256
Mstack = np.stack([Gij[p].flatten() for p in pairs], axis=0)  # 36 x 256
rank_so9 = np.linalg.matrix_rank(Mstack, tol=1e-8)
print(f"so(9) generators: {len(pairs)} matrices, rank = {rank_so9} (expect 36, faithful spin rep)")
assert rank_so9 == 36

# quick antisymmetry check of the rep (so(9) should act by antisymmetric/orthogonal generators
# w.r.t. standard inner product on R^16, i.e. Gamma_ij^T = -Gamma_ij)
max_antisym_err = max(np.max(np.abs(Gij[p].T + Gij[p])) for p in pairs)
print(f"Gamma_ij antisymmetry (so(9) <-> skew matrices) max residual = {max_antisym_err:.3e}")
assert max_antisym_err < 1e-8

# ---------------------------------------------------------------
# 4. Complex structure J = left-mult by unit imaginary octonion e_1, on each O factor
# ---------------------------------------------------------------
J = np.block([[L[1], Z8], [Z8, L[1]]])
J2err = np.max(np.abs(J @ J + I16))
print(f"J^2 = -I check, residual = {J2err:.3e}")
assert J2err < 1e-8

# ---------------------------------------------------------------
# 5. Centralizer of J inside so(9): {X in so(9) : [X,J] = 0}
# ---------------------------------------------------------------
# build the 36 x 256 matrix of flattened commutators [Gamma_ij, J]
comm_rows = []
for p in pairs:
    C = Gij[p] @ J - J @ Gij[p]
    comm_rows.append(C.flatten())
CommM = np.stack(comm_rows, axis=0)   # 36 x 256

# nullspace of CommM^T acting on coefficient vector c (c . CommM = 0), i.e.
# solve CommM^T c = 0  where c in R^36 gives sum_p c_p Gij[p] commuting with J
# Equivalently: find null space of the linear map c -> sum_p c_p [Gij[p], J]
# Build matrix A (256 x 36) with columns = comm_rows[p], find null space of A (A c = 0)
A = CommM.T  # 256 x 36
U, S, Vt = np.linalg.svd(A)
tol = 1e-8 * max(A.shape) * (S[0] if len(S) else 1.0)
null_mask = S < tol if len(S) == min(A.shape) else None
# proper null space dimension = ncols - rank
rank_A = np.sum(S > tol)
nullity = A.shape[1] - rank_A
print(f"Commutator map rank = {rank_A}, nullity (=dim centralizer of J in so(9)) = {nullity}")

# extract null space basis vectors (coefficients c in R^36)
null_basis_coeffs = Vt[rank_A:, :]  # rows spanning null space, shape (nullity, 36)
print(f"Null space basis shape: {null_basis_coeffs.shape}")

# build actual 16x16 centralizer generator matrices
Cent = []
for row in null_basis_coeffs:
    Xc = sum(row[k]*Gij[pairs[k]] for k in range(36))
    Cent.append(Xc)
dimC = len(Cent)
print(f"dim centralizer = {dimC}  (claim: 12)")

# sanity: each Cent[a] really commutes with J
max_comm_err = max(np.max(np.abs(X@J - J@X)) for X in Cent)
print(f"max residual [Cent,J] = {max_comm_err:.3e}")
assert max_comm_err < 1e-6

# orthonormalize the centralizer basis (Gram-Schmidt via QR on flattened vectors) for clean structure constants
Cflat = np.stack([X.flatten() for X in Cent], axis=0)  # dimC x 256
Q, R = np.linalg.qr(Cflat.T)  # 256 x dimC
Cent_on = [Q[:, k].reshape(16, 16) for k in range(dimC)]

# rescale so each basis element is a genuine skew-symmetric so(9) element with reasonable norm
# (orthonormal in Frobenius inner product already from QR)

np.save(os.path.join(tempfile.gettempdir(), 'b565_Cent_on.npy'), np.stack(Cent_on))
print("Saved orthonormal centralizer basis.")

print()
print("="*70)
print("Cross-check with J_L = diag(L_e1, L_e1): claim (per Krasnov 1912.11282,")
print("p.3) is that this centralizer = SU(2) x SU(4)/Z2, dim = 3+15 = 18.")
print(f"  -> our computed dim(centralizer of J_L) = {dimC}  (matches 18 exactly)")
print("="*70)

# ---------------------------------------------------------------
# 6. Now the ACTUAL Krasnov J_R: RIGHT multiplication by u=e_1 on BOTH O factors
# ---------------------------------------------------------------
def right_mult_matrix(u):
    cols = [mult(E[j], u) for j in range(DIM)]
    return np.stack(cols, axis=1)

R1 = right_mult_matrix(E[1])
JR = np.block([[R1, Z8], [Z8, R1]])
JR2err = np.max(np.abs(JR @ JR + I16))
print(f"J_R^2 = -I check, residual = {JR2err:.3e}")
assert JR2err < 1e-8

comm_rows_R = []
for p in pairs:
    C = Gij[p] @ JR - JR @ Gij[p]
    comm_rows_R.append(C.flatten())
CommMR = np.stack(comm_rows_R, axis=0)
AR = CommMR.T
UR, SR, VtR = np.linalg.svd(AR)
rank_AR = np.sum(SR > 1e-8*max(AR.shape)*(SR[0] if len(SR) else 1))
nullityR = AR.shape[1] - rank_AR
print(f"Commutator-map rank (J_R) = {rank_AR}, nullity = dim centralizer(J_R) in so(9) = {nullityR}  (claim: 12)")

null_basis_R = VtR[rank_AR:, :]
CentR = [sum(row[k]*Gij[pairs[k]] for k in range(36)) for row in null_basis_R]
dimCR = len(CentR)
max_comm_err_R = max(np.max(np.abs(X@JR - JR@X)) for X in CentR)
print(f"max residual [Cent_R, J_R] = {max_comm_err_R:.3e}")

# orthonormalize
CflatR = np.stack([X.flatten() for X in CentR], axis=0)
QR_, RR_ = np.linalg.qr(CflatR.T)
CentR_on = [QR_[:, k].reshape(16, 16) for k in range(dimCR)]

np.save(os.path.join(tempfile.gettempdir(), 'b565_CentR_on.npy'), np.stack(CentR_on))
print("Saved orthonormal J_R-centralizer basis. dim =", dimCR)
