"""Scrutiny: is the single algdim=9 'irreducible' at mu=i genuine, or the B564 rank-inflation trap?
Polish each mu=i solution to high precision, examine B in A's eigenbasis (off-block norm), the
algebra singular-value spectrum, and phi-fixedness of the commutator trace t9 (the trap: phi swaps
the two roots of the commutator so an 8-trace match fakes irreducibility while B is block-diagonal)."""
import numpy as np
from scipy.optimize import least_squares

A = np.diag(np.array([1, 1j, -1j], dtype=complex))

def R_of(g):
    gi = np.linalg.inv(g)
    return g @ A @ gi - A @ gi @ A @ g

def resid_real(x):
    g = (x[:9] + 1j * x[9:]).reshape(3, 3)
    try:
        M = R_of(g)
    except np.linalg.LinAlgError:
        return np.ones(18) * 1e3
    return np.concatenate([M.real.ravel(), M.imag.ravel()])

def algebra_svals(mats, n=3):
    basis = [np.eye(n, dtype=complex)]; frontier = [np.eye(n, dtype=complex)]
    for _ in range(8):
        nf = [M @ g for M in frontier for g in mats]
        cand = basis + nf
        flat = np.array([m.ravel() for m in cand])
        s = np.linalg.svd(flat, compute_uv=False)
        rank = int((s > 1e-7 * s[0]).sum())
        if rank == len(basis) or rank == n * n:
            flat = np.array([m.ravel() for m in cand])
            return np.linalg.svd(flat, compute_uv=False)
        basis = cand; frontier = nf
    return np.linalg.svd(np.array([m.ravel() for m in basis]), compute_uv=False)

def eig_basis_block(g):
    """B in A's eigenbasis; report the norm of off-block-diagonal parts vs full."""
    B = np.linalg.inv(g) @ A @ g
    w, V = np.linalg.eig(A)           # A already diagonal so V ~ I; use standard basis
    Be = np.linalg.inv(V) @ B @ V
    return B, Be

# collect flagged-irreducible solutions across many starts (2 seeds), high-precision polish
flagged = []
for seed in (20260724, 424242, 7):
    rng = np.random.default_rng(seed)
    for _ in range(400):
        x0 = rng.standard_normal(18)
        sol = least_squares(resid_real, x0, method="lm", max_nfev=2000, xtol=1e-15, ftol=1e-15, gtol=1e-15)
        if sol.cost > 1e-24:
            continue
        g = (sol.x[:9] + 1j * sol.x[9:]).reshape(3, 3)
        if abs(np.linalg.det(g)) < 1e-4:
            continue
        B = np.linalg.inv(g) @ A @ g
        s = algebra_svals([A, B])
        rank = int((s > 1e-7 * s[0]).sum())
        if rank == 9:
            # scrutinize: the smallest few SVs, and reducibility via invariant subspace
            flagged.append((g, s))

print(f"flagged algdim==9 (tol 1e-7) at mu=i: {len(flagged)}")
if not flagged:
    print("=> ZERO algdim-9 solutions under high-precision polish. The earlier single hit was under-polished noise.")
else:
    # examine the spectrum: is the 9th singular value a genuine O(1) or machine noise?
    for k, (g, s) in enumerate(flagged[:8]):
        B = np.linalg.inv(g) @ A @ g
        # tighter algebra rank thresholds
        r6 = int((s > 1e-6 * s[0]).sum()); r5 = int((s > 1e-5 * s[0]).sum())
        r4 = int((s > 1e-4 * s[0]).sum()); r3 = int((s > 1e-3 * s[0]).sum())
        # genuine invariant-subspace search: does A,B share an eigenvector (reducible)?
        def shares(M, N, tol):
            w, V = np.linalg.eig(M)
            best = 1.0
            for j in range(3):
                v = V[:, j]; Nv = N @ v
                proj = (v.conj() @ Nv) / (v.conj() @ v)
                best = min(best, np.linalg.norm(Nv - proj * v) / max(1e-15, np.linalg.norm(Nv)))
            return best
        s_ab = min(shares(A, B, 0), shares(B, A, 0))
        s_ab_dual = min(shares(A.conj().T, B.conj().T, 0), shares(B.conj().T, A.conj().T, 0))
        # commutator trace t9 phi-fixed? t9(A,B) vs t9(AB,A)
        def comm_tr(X, Y):
            return np.trace(X @ Y @ np.linalg.inv(X) @ np.linalg.inv(Y))
        t9 = comm_tr(A, B); t9p = comm_tr(A @ B, A)
        print(f"\n solution #{k}: det g={np.linalg.det(g):.3f}")
        print(f"   algebra SV spectrum (rel to max): {np.round(s/s[0], 10)}")
        print(f"   rank at tol 1e-7/1e-6/1e-5/1e-4/1e-3: 9/{r6}/{r5}/{r4}/{r3}")
        print(f"   min invariant-line residual (A,B) primal={s_ab:.2e} dual={s_ab_dual:.2e}  (small => reducible)")
        print(f"   t9=tr[A,B]={t9:.6f}  t9(phi)=tr[AB,A]={t9p:.6f}  |diff|={abs(t9-t9p):.2e}  (large => phi SWAPS roots => trap)")
