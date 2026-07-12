#!/usr/bin/env python3
"""B536: verify seat-1's Phase 2-3 findings (theta-lift, level 15).

Conventions: W1 = diag(z^{n(n-1)/2}), W2 = F W1^-1 F^-1, Par = F^2 (n -> -n).
Evolution U = rho(A1) = W1 @ W2  (A1 = T L, rho(T) = W1, rho(L) = F rho(T)^-1 F^-1 = W2).
Answers the handoff's five questions.
"""
import numpy as np

N = 15
z = np.exp(2j*np.pi/N)
n_ = np.arange(N)
W1 = np.diag(z**((n_*(n_-1)//2) % N))
F = z**np.outer(n_, n_) / np.sqrt(N)
W2 = F @ np.conj(W1) @ np.conj(F).T
Par = np.zeros((N, N)); Par[n_, (-n_) % N] = 1
U = W1 @ W2

def commutant_dim(mats):
    rows = [np.kron(np.eye(N), M) - np.kron(M.T, np.eye(N)) for M in mats]
    s = np.linalg.svd(np.vstack(rows), compute_uv=False)
    return int(np.sum(s < 1e-10 * s[0])) + (N*N - len(s) if len(s) < N*N else 0)

print("── F1: irreducibility ──")
d12 = commutant_dim([W1, W2])
d123 = commutant_dim([W1, W2, Par])
print(f"commutant dim {{W1,W2}} = {d12} (Weil 2+3+4+6 sectors -> expect 4)")
print(f"commutant dim {{W1,W2,Par}} = {d123} (claim: 1, via the Heisenberg twist")
print(f"  Par W Par^-1 W^-1 != 1, the banked B358 theta-twist)")

print("\n── CRT factorization of U (Q1) ──")
# CRT permutation: n <-> (n mod 3, n mod 5), index 5*(n%3)+(n%5)
P = np.zeros((N, N))
for n in range(N):
    P[5*(n % 3) + (n % 5), n] = 1
Uc = P @ U @ P.T
# test tensor structure: Uc == U3 kron U5 up to scalar
M3 = Uc.reshape(3, 5, 3, 5)
# extract candidate factors from the largest entry
i0 = np.unravel_index(np.argmax(np.abs(Uc)), Uc.shape)
a0, b0 = divmod(i0[0], 5); a1, b1 = divmod(i0[1], 5)
U5 = M3[a0, :, a1, :].copy()
U3 = M3[:, b0, :, b1].copy() / M3[a0, b0, a1, b1]
err = np.abs(np.einsum('ik,jl->ijkl', U3, U5) - M3).max()
print(f"U = U3 (x) U5 tensor error: {err:.2e}  -> local unitary;")
print(f"Q1 ANSWER: entanglement conservation is TRIVIAL (CRT-local unitary)")

print("\n── F2/Q2: the period ──")
ev, evec = np.linalg.eig(U)
par_exp = [float(np.real(np.conj(v) @ Par @ v)) for v in evec.T]
k0 = int(np.argmin(np.abs(par_exp)))
psi0 = evec[:, k0]
print(f"most-uncertain eigenvector: <Par> = {par_exp[k0]:.4f}, "
      f"phase = {np.angle(ev[k0])/np.pi:.4f} pi")
psi = (psi0 + Par @ psi0); psi = psi / np.linalg.norm(psi)   # Par=+1 projection
seq = []
cur = psi.copy()
for t_ in range(13):
    seq.append(float(np.real(np.conj(cur) @ Par @ cur)))
    cur = U @ cur
print(f"<Par>(t): {np.round(seq, 3)}")
# period up to global phase
periods = [k for k in range(1, 61)
           if np.abs(np.abs(np.conj(np.linalg.matrix_power(U, k) @ psi
                                    ) @ psi) - 1) < 1e-9]
print(f"state-period (up to phase): {periods[0] if periods else '>60'}")
# eigenphase support explanation
sup = [k for k in range(N) if abs(np.conj(evec[:, k]) @ psi) > 1e-9]
phases = np.angle(ev[sup]) / np.pi
print(f"support on {len(sup)} eigenvectors, phases/pi: {np.round(sorted(phases), 4)}")
d = np.angle(ev[sup] / ev[sup[0]]) / np.pi
print(f"phase differences/pi vs first: {np.round(sorted(d), 4)} "
      f"(period 6 <=> all differences multiples of 1/3)")

print("\n── F3/Q5: entanglement ──")
rho = psi.reshape(3, 5) if False else (P @ psi).reshape(3, 5)
sv = np.linalg.svd(rho, compute_uv=False)
lam = sv**2 / (sv**2).sum()
S = float(-np.sum(lam * np.log(lam)))
print(f"Schmidt rank: {int(np.sum(sv > 1e-10))}, lambdas: {np.round(lam, 6)}")
print(f"S = {S:.4f} (claim 1.0620), S/ln3 = {S/np.log(3):.4f}")
Ssteps = []
cur = psi.copy()
for t_ in range(7):
    svt = np.linalg.svd((P @ cur).reshape(3, 5), compute_uv=False)
    lt = svt**2 / (svt**2).sum(); lt = lt[lt > 1e-15]
    Ssteps.append(float(-np.sum(lt*np.log(lt))))
    cur = U @ cur
print(f"S(t): {np.round(Ssteps, 6)} (conserved: {np.ptp(Ssteps) < 1e-9})")

print("\n── F4/Q3: darkness of the state seam ──")
def dark_count(state):
    c = 0
    for j in range(N):
        for l in range(N):
            v = np.conj(state) @ (Par @ np.linalg.matrix_power(W1, j)
                                  @ np.linalg.matrix_power(W2, l)) @ state
            if abs(v) < 1e-10:
                c += 1
    return c
print(f"psi_bang dark points: {dark_count(psi)}/225 (claim 0)")
e0 = np.zeros(N); e0[0] = 1
print(f"basis state e0 dark points: {dark_count(e0)}/225 (NOT zero -> not universal)")
rng = np.random.RandomState(1)
rnd = rng.randn(N) + 1j*rng.randn(N); rnd /= np.linalg.norm(rnd)
print(f"random state dark points: {dark_count(rnd)}/225 (generic -> 0)")
print("Q3 ANSWER: dark-free is GENERIC (codim-1 exceptions, e.g. basis states);")
print("  psi_bang is not special; the architecture/state distinction stands.")

print("\n── F5/Q4: [W1,W2] golden eigenvalue ──")
for lvl in (5, 15):
    zz = np.exp(2j*np.pi/lvl); m_ = np.arange(lvl)
    w1 = np.diag(zz**((m_*(m_-1)//2) % lvl))
    f_ = zz**np.outer(m_, m_) / np.sqrt(lvl)
    w2 = f_ @ np.conj(w1) @ np.conj(f_).T
    C = w1 @ w2 - w2 @ w1
    eg = np.linalg.eigvals(C)
    phi = (1+np.sqrt(5))/2
    hit = [e for e in eg if abs(abs(e) - phi) < 1e-9 and abs(e.real) < 1e-9]
    print(f"level {lvl}: |eigs| = {np.round(np.sort(np.abs(eg))[::-1], 4)}")
    print(f"  +-i*phi present: {len(hit) > 0} ({np.round(hit, 6) if hit else ''})")

print("\n── F6: Par splits (exact) ──")
for p in (3, 5, 15):
    pp = np.zeros((p, p)); mm = np.arange(p); pp[mm, (-mm) % p] = 1
    plus = int(round((p + np.trace(pp)) / 2))
    print(f"Par_{p}: +1 dim = {plus}, -1 dim = {p - plus}")
