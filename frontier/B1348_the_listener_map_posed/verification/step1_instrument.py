"""B1348 step 1 -- build the instrument from scratch and run the controls.

The spec fixes it: C^6 = SU(3) level-2 weight space, R = T, L = S^-1 T^-1 S with (S,T) the
Kac-Peterson matrices, |<R,L>| = 2880 = |2T x 2I|, and a conjugation weld theta grading
C^6 = C^2_odd (+) C^4_even. Nothing here is taken from B1011; it is rebuilt and then compared.
"""
import itertools, numpy as np

def su3_data(k):
    N, kap = 3, k + 3
    weights = [(a, b) for a in range(k + 1) for b in range(k + 1 - a)]
    Lvec = lambda w: np.array([w[0] + w[1] + 2.0, w[1] + 1.0, 0.0])
    ip = lambda u, v: float(np.dot(u, v) - u.sum() * v.sum() / 3.0)
    perms = list(itertools.permutations(range(3)))
    sgn = lambda p: (-1) ** sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3))
    n = len(weights)
    S = np.zeros((n, n), dtype=complex)
    for i, wl in enumerate(weights):
        Ll = Lvec(wl)
        for j, wm in enumerate(weights):
            Lm = Lvec(wm)
            tot = 0j
            for p in perms:
                tot += sgn(p) * np.exp(-2j * np.pi * ip(Ll[list(p)], Lm) / kap)
            S[i, j] = tot
    S *= -1j / (kap * np.sqrt(3.0))          # Kac-Peterson normalisation for SU(3)
    C2 = lambda w: (2.0/3.0)*(w[0]**2 + w[0]*w[1] + w[1]**2) + 2.0*(w[0] + w[1])
    cc = 8.0 * k / (k + 3.0)                  # central charge of SU(3)_k
    T = np.diag([np.exp(2j*np.pi*(C2(w)/(2*kap) - cc/24.0)) for w in weights])
    return weights, S, T

W, S, T = su3_data(2)
print("weights:", W)
n = len(W)
print("\n=== CONTROLS ===")
print("  S unitary        :", np.allclose(S @ S.conj().T, np.eye(n), atol=1e-10))
print("  S symmetric      :", np.allclose(S, S.T, atol=1e-10))
C = S @ S
print("  C = S^2 is a permutation (charge conjugation):",
      np.allclose(np.abs(C), (np.abs(C) > 0.5).astype(float), atol=1e-9))
perm = [int(np.argmax(np.abs(C[i]))) for i in range(n)]
print("  C permutation    :", [(W[i], W[perm[i]]) for i in range(n)])
print("  (ST)^3 = S^2     :", np.allclose((S@T)@(S@T)@(S@T), C, atol=1e-9))

R = T.copy()
Sinv = np.linalg.inv(S)
L = Sinv @ np.linalg.inv(T) @ S
print("\n  R = T, L = S^-1 T^-1 S built.")

# the group order, by closing the set of matrices up to phase-free comparison
def key(M, q=9):
    return tuple(np.round(M.flatten(), q).tolist())
seen, frontier = {key(np.eye(n))}, [np.eye(n, dtype=complex)]
gens = [R, L, np.linalg.inv(R), np.linalg.inv(L)]
while frontier and len(seen) < 20000:
    nxt = []
    for M in frontier:
        for g in gens:
            P = M @ g
            k_ = key(P)
            if k_ not in seen:
                seen.add(k_); nxt.append(P)
    frontier = nxt
print(f"  |<R,L>| = {len(seen)}   (B1011 C1 says 2880 = |2T x 2I|)   MATCH: {len(seen)==2880}")
np.save("/tmp/b1348_S.npy", S); np.save("/tmp/b1348_T.npy", T)
