"""Ground-truth e_n mod p via the escalator matrices.
M_0 = F = [[1,1],[1,0]];  T(M) = [[M, M],[M^2, M]];  M_n = T^n(F).
e_n = det(I - M_n).  Compute mod p with numpy int arithmetic (p small).
"""
import numpy as np

def matmod(A, B, p):
    return (A @ B) % p

def escalate(M, p):
    M2 = matmod(M, M, p)
    top = np.hstack([M, M])
    bot = np.hstack([M2, M])
    return np.vstack([top, bot]) % p

def det_mod(A, p):
    # Gaussian elimination mod p (p prime). Returns det mod p.
    A = A.copy().astype(np.int64) % p
    n = A.shape[0]
    det = 1
    for col in range(n):
        piv = -1
        for r in range(col, n):
            if A[r, col] % p != 0:
                piv = r; break
        if piv == -1:
            return 0
        if piv != col:
            A[[col, piv]] = A[[piv, col]]
            det = (-det) % p
        inv = pow(int(A[col, col]), p-2, p)
        det = (det * int(A[col, col])) % p
        # eliminate below (vectorized rank-1 update)
        if col+1 < n:
            factors = (A[col+1:, col] * inv) % p          # (n-col-1,)
            A[col+1:, col:] = (A[col+1:, col:] - np.outer(factors, A[col, col:])) % p
    return det % p

def e_n_sequence(p, Nmax):
    F = np.array([[1,1],[1,0]], dtype=np.int64)
    seq = []
    M = F % p
    for n in range(Nmax+1):
        N = M.shape[0]
        I = np.eye(N, dtype=np.int64)
        e = det_mod((I - M) % p, p)
        seq.append(int(e))
        if n < Nmax:
            M = escalate(M, p)
    return seq

if __name__ == "__main__":
    for p in (5, 7):
        seq = e_n_sequence(p, 9)
        print(f"p={p}: e_n mod {p} for n=0..9: {seq}")
    # sanity vs known integer charge tower |e_n| = 1,11,809,18845089,...
    known = [1, 11, 809, 18845089]
    for p in (5,7):
        seq = e_n_sequence(p, 3)
        ref = [ (-k)%p for k in known ]  # e_n are NEGATIVE: -1,-11,-809,...
        print(f"p={p}: computed {seq}  vs (-|e_n|)%p {ref}")
