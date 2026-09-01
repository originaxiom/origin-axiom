"""R16 blind recomputation: Kashaev invariant asymptotics of 4_1.

Written BLIND (before reading arc verification scripts). Only inputs:
- the standard closed form <4_1>_N = sum_{k=0}^{N-1} prod_{j=1}^{k} |2 sin(pi j/N)|^2
- the banked rationals from the cell brief (used only at the DIFF stage at the end).

Method:
  J_N ~ e^{N V/(2 pi)} N^{3/2} (C0 + C1/N + C2/N^2 + ...),  V = Vol(4_1) = 6 Lambda(pi/3)
  Compute S(N) = J_N e^{-N V/(2 pi)} N^{-3/2} on a ladder of N, then solve the
  Vandermonde system in 1/N (full Richardson elimination) for c0..c_{m-1}.
  Stability estimated by comparing fits on two different node subsets.
"""
from mpmath import mp, mpf, mpc, pi, sin, exp, sqrt, polylog, matrix, lu_solve, nstr, log10, fabs

mp.dps = 620

def kashaev41(N):
    p = mpf(1)
    s = mpf(1)          # k = 0 term (empty product)
    piN = pi / N
    for j in range(1, N):
        t = 2 * sin(piN * j)
        p *= t * t
        s += p
    return s

# hyperbolic volume of 4_1: V = 2 Im Li2(e^{i pi/3})... use V = 3 Im Li2(e^{2 pi i /3})
V = 3 * polylog(2, exp(mpc(0, 2) * pi / 3)).imag
print("V (should be 2.02988321...):", nstr(V, 30))

Ns = [900, 1200, 1500, 1800, 2100, 2400, 2700, 3000, 3300, 3600, 3900, 4200]
Svals = {}
for N in Ns:
    J = kashaev41(N)
    S = J * exp(-N * V / (2 * pi)) / mpf(N) ** mpf('1.5')
    Svals[N] = S
    print(N, nstr(S, 25))

def fit(nodes, m):
    A = matrix(m, m)
    b = matrix(m, 1)
    for i, N in enumerate(nodes):
        x = mpf(1) / N
        for j in range(m):
            A[i, j] = x ** j
        b[i] = Svals[N]
    return lu_solve(A, b)

fitA = fit(Ns[:10], 10)          # N = 900..3600
fitB = fit(Ns[2:12], 10)         # N = 1500..4200
fitC = fit(Ns[1:11], 10)         # shifted subset

print("\ncoefficients (fit A | fit B | fit C), agreement -> honest digits:")
for k in range(6):
    print(f"c{k}: {nstr(fitA[k], 30)} | {nstr(fitB[k], 30)} | {nstr(fitC[k], 30)}")

# ---------------- DIFF vs banked rationals (from cell brief) ----------------
C0 = mpf(3) ** mpf('-0.25')
banked = [
    C0,
    mpf(11) / 108 * sqrt(mpf(3)) * pi * C0,
    mpf(697) / 7776 * pi ** 2 * C0,
    mpf(724351) / 12597120 * sqrt(mpf(3)) * pi ** 3 * C0,
    mpf(278392949) / 1813985280 * pi ** 4 * C0,
]
print("\nDIFF vs banked:")
for k in range(5):
    fa, fb = fitA[k], fitB[k]
    stab = fabs(fa - fb)
    dig_stab = int(-log10(stab / fabs(fa))) if stab > 0 else 99
    err = fabs(fa - banked[k]) / fabs(banked[k])
    dig_match = int(-log10(err)) if err > 0 else 99
    print(f"C{k}: fit={nstr(fa, 30)}")
    print(f"    banked={nstr(banked[k], 30)}")
    print(f"    stable digits ~{dig_stab}, matching digits vs banked ~{dig_match}")

# parity-law check: c_k / (C0 * pi^k) should be rational (even k) or sqrt(3)*rational (odd k)
print("\nparity-law ratios c_k/(C0 pi^k) [odd ones divided by sqrt(3)]:")
for k in range(1, 5):
    r = fitA[k] / (C0 * pi ** k)
    if k % 2 == 1:
        r = r / sqrt(mpf(3))
    print(f"k={k}: {nstr(r, 25)}")

# planted-negative control: perturb C1's rational 11/108 -> 12/108, show rejection scale
pert = mpf(12) / 108 * sqrt(mpf(3)) * pi * C0
print("\ncontrol: |fit c1 - (12/108)sqrt3 pi C0| / |c1| =", nstr(fabs(fitA[1] - pert) / fabs(fitA[1]), 5))
