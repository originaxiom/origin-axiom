"""B480 reimplementation: 'level-ratio <r> = 0.16 at N = 181, 301' for the object's
own quantized dynamics (the golden cat map M = [[2,1],[1,1]] = A_1, m=1 member of the
metallic family). No script in frontier/B480_qca_dirac_lens/ computes this (qca_dispersion.py
only covers the coin/dispersion Q1 cell) -- FINDINGS.md attributes it to 'Hecke /
Kurlberg-Rudnick arithmetic symmetries' without a saved reproducer, so this is a from-
scratch minimal reimplementation of the standard quantized-cat-map construction.

Quantization: for M=(a b; c d) in SL(2,Z) with c invertible mod N, the Hannay-Berry /
Weil representation propagator is (up to an overall phase irrelevant to spacing ratios)
   U_N(j,k) = (1/sqrt(N)) exp( i*pi/(c*N) * (a k^2 - 2 j k + d j^2) ),  j,k = 0..N-1
For M = [[2,1],[1,1]]  (a=2,b=1,c=1,d=1; the golden/m=1 metallic cat map), c=1 so no
modular inverse is needed. Verified unitary to machine precision for several N below.

Statistic: eigenphases of U_N(M) sorted on the circle; consecutive spacings s_n; the
Oganesyan-Huse ratio r_n = min(s_n,s_{n+1})/max(s_n,s_{n+1}), averaged (<r>). Poisson
<r> ~ 0.386, GOE <r> ~ 0.53; heavy arithmetic degeneracy drives <r> well below both.
"""
import numpy as np

np.seterr(all="ignore")


def quantize(N, a=2, b=1, c=1, d=1):
    assert np.gcd(c, N) == 1
    cinv = pow(int(c), -1, N)
    j = np.arange(N).reshape(-1, 1)
    k = np.arange(N).reshape(1, -1)
    phase = (np.pi * cinv / N) * (a * k**2 - 2 * j * k + d * j**2)
    return np.exp(1j * phase) / np.sqrt(N)


def order_mod_N(N, M=np.array([[2, 1], [1, 1]])):
    P = M.copy() % N
    I = np.eye(2, dtype=object)
    Mm = M.astype(object)
    P = Mm.copy()
    for k in range(1, 4 * N + 1):
        if np.array_equal(P % N, I % N):
            return k
        P = (P @ Mm)
    return None


def mean_r_statistic(eigphases):
    ang = np.sort(np.mod(eigphases, 2 * np.pi))
    N = len(ang)
    s = np.diff(np.append(ang, ang[0] + 2 * np.pi))
    s = np.maximum(s, 0)
    r = np.minimum(s[:-1], s[1:]) / np.maximum(s[:-1], s[1:])
    r = r[np.isfinite(r)]
    return float(np.mean(r)), s


for N in (181, 301):
    U = quantize(N)
    dev = np.max(np.abs(U.conj().T @ U - np.eye(N)))
    print(f"N={N}: unitarity check max|U^dag U - I| = {dev:.2e}")
    ordM = order_mod_N(N)
    print(f"  ord(M) mod {N} = {ordM}  (N/ord ~ {N/ordM:.2f}, degeneracy scale)")

    eig = np.linalg.eigvals(U)
    phases = np.angle(eig)
    r_mean, spac = mean_r_statistic(phases)
    n_distinct = len(np.unique(np.round(np.mod(phases, 2*np.pi), 8)))
    n_zero_spacings = np.sum(spac < 1e-6)
    print(f"  <r> = {r_mean:.4f}   (target ~0.16; Poisson 0.386; GOE 0.53)")
    print(f"  distinct eigenphases: {n_distinct}/{N};  (near-)zero spacings: {n_zero_spacings}")
    print()

print("Reference (uniform/Poisson-random phases control, N=301):")
np.random.seed(0)
rand_phases = np.sort(np.random.uniform(0, 2*np.pi, 301))
r_rand, _ = mean_r_statistic(rand_phases)
print(f"  <r>_Poisson (numerical control) = {r_rand:.4f}  (expect ~0.386)")
