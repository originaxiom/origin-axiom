import numpy as np
np.set_printoptions(precision=4, suppress=True, linewidth=200)

CentR_on = np.load('/private/tmp/claude-501/-Users-dri-origin-axiom/06195d53-d92a-477a-b1cb-cccccca43ae9/scratchpad/CentR_on.npy')
n = CentR_on.shape[0]
print(f"Loaded centralizer basis: {n} matrices of shape {CentR_on.shape[1:]}")
assert n == 12

# --- verify Frobenius orthonormality
G = np.einsum('aij,bij->ab', CentR_on, CentR_on)
print("Gram matrix deviation from I:", np.max(np.abs(G - np.eye(n))))

# --- verify closure under bracket: [Y_a,Y_b] should lie entirely within span(CentR_on)
def bracket(A, B):
    return A @ B - B @ A

max_closure_residual = 0.0
F = np.zeros((n, n, n))  # structure constants f[a,b,c]:  [Y_a,Y_b] = sum_c f[a,b,c] Y_c
for a in range(n):
    for b in range(n):
        Cab = bracket(CentR_on[a], CentR_on[b])
        coeffs = np.einsum('cij,ij->c', CentR_on, Cab)   # projection (orthonormal basis)
        recon = np.einsum('c,cij->ij', coeffs, CentR_on)
        resid = np.max(np.abs(Cab - recon))
        max_closure_residual = max(max_closure_residual, resid)
        F[a, b, :] = coeffs

print(f"Max residual of [Y_a,Y_b] outside span(centralizer) (closure check): {max_closure_residual:.3e}")
assert max_closure_residual < 1e-6

# --- adjoint matrices ad_a (n x n):  (ad_a)[c,b] = f[a,b,c]
ad = np.zeros((n, n, n))
for a in range(n):
    ad[a] = F[a].T   # ad[a][c,b] = F[a,b,c]

# sanity: ad_a should be antisymmetric w.r.t. Killing-compatible pairing for compact algebra;
# more directly check ad_a acting on Y_b indeed reproduces bracket numerically for random combos
rng = np.random.default_rng(1)
for _ in range(5):
    v = rng.normal(size=n)
    X = np.einsum('a,aij->ij', v, CentR_on)
    w = rng.normal(size=n)
    Yv = np.einsum('a,aij->ij', w, CentR_on)
    lhs = bracket(X, Yv)
    # via structure constants: [X,Yv] coefficients = sum_a v_a * (ad_a @ w)
    coeff_pred = np.einsum('a,acb,b->c', v, ad, w)
    rhs = np.einsum('c,cij->ij', coeff_pred, CentR_on)
    assert np.max(np.abs(lhs - rhs)) < 1e-6
print("Structure-constant reconstruction of bracket verified on random samples.")

# --- 1) CENTER: w such that sum_a w_a ad_a = 0 (n x n zero matrix)
Amat = ad.reshape(n, n*n).T   # (n*n) x n ,  column a = flattened ad_a
U, S, Vt = np.linalg.svd(Amat)
tol = 1e-8 * max(Amat.shape) * (S[0] if len(S) else 1.0)
rank_center_map = np.sum(S > tol)
dim_center = n - rank_center_map
print(f"dim(center) = {dim_center}  (expect 1, the u(1) factor)")
center_dirs = Vt[rank_center_map:, :]   # rows spanning center coefficient space

# --- 2) DERIVED ALGEBRA dimension = rank of the bracket map (image of all [Y_a,Y_b])
bracket_vectors = F.reshape(n*n, n)   # each row = coeffs of [Y_a,Y_b]
rank_derived = np.linalg.matrix_rank(bracket_vectors, tol=1e-8)
print(f"dim([g,g]) (derived/semisimple part) = {rank_derived}  (expect 11 = 12-1)")

# --- 3) Killing form K(a,b) = trace(ad_a @ ad_b), rank & signature
K = np.einsum('aij,bji->ab', ad, ad)
K = 0.5*(K + K.T)
eigvals = np.linalg.eigvalsh(K)
print("Killing form eigenvalues:", np.round(eigvals, 6))
rank_K = np.sum(np.abs(eigvals) > 1e-6)
print(f"rank(Killing form) = {rank_K}  (expect 11; nullity 1 = center)")
print(f"Killing form negative semi-definite (compact type)? all eigs <=~0: {np.all(eigvals < 1e-6)}")

# --- 4) Decompose the 12-dim adjoint rep into invariant blocks via the COMMUTANT
#     of {ad_a}_{a=1..n} inside gl(n,R): solve C ad_a - ad_a C = 0 for all a.
# Build the linear system directly on the n*n entries of C using the standard basis
# matrices E_ij (avoids any vec-ordering ambiguity from kron tricks).
Ebasis = [np.zeros((n, n)) for _ in range(n*n)]
idx_map = []
k = 0
for i in range(n):
    for j in range(n):
        Ebasis[k][i, j] = 1.0
        idx_map.append((i, j))
        k += 1

rows = []
for a in range(n):
    for Eij in Ebasis:
        R = Eij @ ad[a] - ad[a] @ Eij
        rows.append(R.flatten())
BigM = np.stack(rows, axis=0)          # (n * n*n) x (n*n), row = residual for (a, basis E_ij), col = flattened residual index...
# We actually need: unknowns = coefficients of C in the E_ij basis (n*n unknowns),
# equations = flattened residual entries stacked over a (n * n*n equations).
# BigM as built has shape (n*n*n rows if we stacked per (a,Eij)) x (n*n flattened entries) -- fix via proper build:
BigM = None
cols = []
for Eij in Ebasis:
    col_entries = []
    for a in range(n):
        R = Eij @ ad[a] - ad[a] @ Eij
        col_entries.append(R.flatten())
    cols.append(np.concatenate(col_entries))
BigM = np.stack(cols, axis=1)   # (n * n*n) x (n*n):  BigM @ vec(C) = stacked residuals
Uc, Sc, Vtc = np.linalg.svd(BigM)
tolc = 1e-8 * max(BigM.shape) * (Sc[0] if len(Sc) else 1.0)
rank_comm_map = np.sum(Sc > tolc)
dim_commutant = BigM.shape[1] - rank_comm_map
print(f"dim(commutant of ad-representation) = {dim_commutant}  (expect 3: one scalar per invariant block)")

null_coeffs = Vtc[rank_comm_map:, :]   # each row: coefficients of C in E_ij basis
commutant_basis = []
for row in null_coeffs:
    C = np.zeros((n, n))
    for coeff, (i, j) in zip(row, idx_map):
        C[i, j] = coeff
    commutant_basis.append(C)
commutant_basis = np.stack(commutant_basis, axis=0)
print(f"Number of commutant basis matrices found: {commutant_basis.shape[0]}")

# The commutant of an algebra acting with invariant subspaces that are pairwise INEQUIVALENT
# irreducibles is spanned (up to change of basis) by projectors onto those blocks; extract block
# dims via simultaneous diagonalization: take a random combination of commutant matrices, find
# its eigenspaces (should be exactly the invariant block projectors' eigenspaces, real symmetric
# after symmetrizing w.r.t. Killing pairing -- since ad is not symmetric in general, use another route:
# find invariant subspaces directly via the null space structure / joint kernel of (ad_a - lambda) is
# awkward; instead diagonalize a SYMMETRIZED commutant element: since the algebra is compact,
# there's a basis where all ad_a are simultaneously block-skew-diagonal aligned with the invariant
# subspaces. We instead directly probe invariant-subspace dimensions using the RANK of projector
# candidates obtained from the commutant basis by symmetrizing (C + C^T)/2 and diagonalizing.
cand = commutant_basis[0]
cand_sym = 0.5*(cand + cand.T)
evals, evecs = np.linalg.eigh(cand_sym)
print("Eigenvalues of a symmetrized commutant element (block signature):", np.round(evals, 6))
# group eigenvalues into clusters
sorted_ev = np.sort(evals)
clusters = []
cur = [sorted_ev[0]]
for x in sorted_ev[1:]:
    if abs(x - cur[-1]) < 1e-4:
        cur.append(x)
    else:
        clusters.append(cur); cur=[x]
clusters.append(cur)
block_dims = sorted([len(c) for c in clusters])
print(f"Block sizes from symmetrized-commutant eigenvalue clustering: {block_dims}  (expect [1,3,8])")

# --- 5) RANK-4 CHECK: dim of centralizer of a GENERIC element = rank of g
rng2 = np.random.default_rng(7)
x = rng2.normal(size=n)
ad_X = np.einsum('a,acb->cb', x, ad)   # (ad_X)[c,b] = sum_a x_a ad[a,c,b]
rankX = np.linalg.matrix_rank(ad_X, tol=1e-8)
nullity_generic = n - rankX
print(f"Generic-element centralizer dimension (= rank of g) trial1 = {nullity_generic}")

# repeat a few times to make sure we hit a REGULAR (generic) element (min nullity over trials = rank)
nulls = []
for seed in range(30):
    r = np.random.default_rng(100+seed)
    x = r.normal(size=n)
    ad_X = np.einsum('a,acb->cb', x, ad)
    rk = np.linalg.matrix_rank(ad_X, tol=1e-8)
    nulls.append(n - rk)
print(f"Nullities over 30 random elements: min={min(nulls)}, values sample={sorted(set(nulls))}")
print(f"==> rank(g) = min nullity = {min(nulls)}  (claim/expect: 4 = rank u(1)[1] + su(2)[1] + su(3)[2])")
