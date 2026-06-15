"""B153 CORRECTION (2026-06-15) -- n=5 non-semisimple: irreducible reps EXIST.

The earlier B153 claim "n=5 non-semisimple: 0/120, no irreducible reps (absent)" was an artifact of
random Newton drifting to the vacuous det t=0 stratum -- the SAME bug the campaign fixed at n=3 (by
pinning det t=1) but never back-applied to n=5. With det t=1 pinned, irreducible SL(5) bundle reps with
principal A-spectrum {1,1,1,-1,-1} DO exist for the non-semisimple Jordan types (abundantly for the two
[3]-block types). Two INDEPENDENT irreducibility certificates agree (Burnside span-rank = 25, and Schur
commutant dim = 1), with ~15-orders-of-magnitude SVD gaps and well-conditioned t (cond ~ 20).

The degeneration HEADLINE survives: degree=rank L=(-1)^{n-1}M^n is still NOT realized on any irreducible
rep at n=5 -- but the corrected reason is that the relation FAILS on the (existing) irreducibles
(best matrix-identity match ~2.5 over n=2..8), while the locus where it could be forced (A^2=I) is
reducible (dihedral, proven).  See FINDINGS.md.

Run:  python frontier/B153_degree_rank_degeneration/n5_nonss_irreducible.py
"""
from __future__ import annotations
import numpy as np

n = 5

def jblock(lam, k):
    M = lam * np.eye(k, dtype=complex)
    for i in range(k - 1):
        M[i, i + 1] = 1.0
    return M

def blockdiag(*bs):
    M = np.zeros((n, n), dtype=complex); r = 0
    for b in bs:
        k = b.shape[0]; M[r:r + k, r:r + k] = b; r += k
    return M

def star_res(A, t):
    return t @ np.linalg.inv(A @ A) @ t @ A - np.linalg.inv(A) @ t @ A @ t

def Bfrom(A, t):
    return np.linalg.inv(A @ A) @ t @ A @ np.linalg.inv(t)

def solve_t(A, rng, iters=600):
    """Newton on [vec(*); det t - 1]; det-pinned to avoid the vacuous det t=0 stratum."""
    t = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
    for _ in range(iters):
        g = np.concatenate([star_res(A, t).reshape(-1), [np.linalg.det(t) - 1.0]])
        if np.max(np.abs(g)) < 1e-13:
            break
        h = 1e-7; tf = t.reshape(-1); J = np.zeros((g.size, n * n), complex)
        for k in range(n * n):
            tp = tf.copy(); tp[k] += h
            gp = np.concatenate([star_res(A, tp.reshape(n, n)).reshape(-1),
                                 [np.linalg.det(tp.reshape(n, n)) - 1.0]])
            J[:, k] = (gp - g) / h
        st, *_ = np.linalg.lstsq(J, g, rcond=None); t = (tf - st).reshape(n, n)
    return t

def burnside_rank(A, B, rounds=7, tol=1e-6):
    gens = [A, B, np.linalg.inv(A), np.linalg.inv(B)]
    allm = [np.eye(n, dtype=complex)]; fr = [np.eye(n, dtype=complex)]
    for _ in range(rounds):
        fr = [g @ m for m in fr for g in gens]; allm += fr
    W = np.array([m.reshape(-1) for m in allm])
    W = W / np.maximum(np.linalg.norm(W, axis=1, keepdims=True), 1e-300)
    s = np.linalg.svd(W, compute_uv=False)
    return int(np.sum(s > tol * s[0])), s

def commutant_dim(A, B):
    """dim {X: XA=AX, XB=BX}. Schur: irreducible <=> 1 (only scalars)."""
    I5 = np.eye(n)
    def cm(M):
        return np.kron(M.T, I5) - np.kron(I5, M)
    s = np.linalg.svd(np.vstack([cm(A), cm(B)]), compute_uv=False)
    return int(np.sum(s < 1e-8 * s[0]))

def degree_rank_best_match(A, t):
    """min over n of || [A,B] - (-1)^(n-1) mu^n / det t ||  (matrix identity error)."""
    B = Bfrom(A, t); mu = np.linalg.inv(A) @ t
    comm = A @ B @ np.linalg.inv(A) @ np.linalg.inv(B); dt = np.linalg.det(t)
    return min(np.max(np.abs(comm - ((-1) ** (nn - 1)) * np.linalg.matrix_power(mu, nn) / dt))
               for nn in (2, 3, 4, 5, 6, 7, 8))

TYPES = {
    "[2,1]|[1,1]": blockdiag(jblock(1, 2), jblock(1, 1), jblock(-1, 1), jblock(-1, 1)),
    "[3]|[1,1]":   blockdiag(jblock(1, 3),               jblock(-1, 1), jblock(-1, 1)),
    "[1,1,1]|[2]": blockdiag(jblock(1, 1), jblock(1, 1), jblock(1, 1), jblock(-1, 2)),
    "[2,1]|[2]":   blockdiag(jblock(1, 2), jblock(1, 1),               jblock(-1, 2)),
    "[3]|[2]":     blockdiag(jblock(1, 3),                             jblock(-1, 2)),
}

def main(nseed=120):
    print("B153 n=5 non-semisimple: irreducible reps with principal spectrum {1,1,1,-1,-1}\n")
    total_irr = 0; best_dr = 1e9
    for name, A in TYPES.items():
        assert abs(np.linalg.det(A) - 1) < 1e-9 and not np.allclose(A @ A, np.eye(n))
        rng = np.random.default_rng(2026)
        nsol = nirr = 0
        for s in range(nseed):
            t = solve_t(A, rng)
            if np.max(np.abs(star_res(A, t))) > 1e-10 or abs(np.linalg.det(t) - 1) > 1e-9:
                continue
            if np.linalg.cond(t) > 1e4:
                continue
            nsol += 1; B = Bfrom(A, t)
            br, _ = burnside_rank(A, B)
            if br == n * n and commutant_dim(A, B) == 1:
                nirr += 1; total_irr += 1
                best_dr = min(best_dr, degree_rank_best_match(A, t))
        print(f"  {name:14s}: well-conditioned det-t=1 reps {nsol:3d}/{nseed}; "
              f"IRREDUCIBLE (Burnside=25 & commutant=1): {nirr}")
    print(f"\n  => irreducible non-ss reps EXIST at n=5 (total {total_irr}); "
          f"degree=rank best matrix match over all of them: {best_dr:.2f} (>> 0 => relation fails).")
    assert total_irr > 0, "expected irreducible non-ss reps at n=5"
    assert best_dr > 1.0, "degree=rank should fail on the non-ss irreducibles"
    print("  CORRECTED CLAIM verified: n=5 has irreducible reps, but degree=rank is not realized on them.")
    return total_irr, best_dr

if __name__ == "__main__":
    main()
