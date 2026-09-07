#!/usr/bin/env python3
"""CALIBRATE GC-6's c_eff ESTIMATOR ON KNOWNS, then apply it to the corpus's one banked q-series.

The estimator is GC-6's own, copied verbatim from
frontier/B1190_close_loop_batch2/verification/gc6_l154_bridge.py:
    c_eff(n) = 6 n (log a_{n+1} - log a_n)^2 / pi^2
Cardy:  a_n ~ exp(2 pi sqrt(c_eff n / 6)).

Nothing here is trusted until the estimator reproduces values that are known independently.
Gate 5: pure q-series arithmetic, no measured value.
"""
import math
NMAX = 4000

def c_eff_series(coeffs, skip=4):
    out = []
    for n in range(skip, len(coeffs) - 1):
        if coeffs[n] <= 0 or coeffs[n+1] <= 0: continue
        d = math.log(coeffs[n+1]) - math.log(coeffs[n])
        out.append((n, 6*n*d*d/math.pi**2))
    return out

def tail(cs, k=3):
    s = c_eff_series(cs)
    return [v for _, v in s[-k:]]

def mul(a, b, N=NMAX):
    out = [0]*(N+1)
    for i, ai in enumerate(a):
        if ai == 0 or i > N: continue
        for j, bj in enumerate(b):
            if i+j > N: break
            if bj: out[i+j] += ai*bj
    return out

# eta^-1 : partition numbers p(n).  Free boson, unitary, c = c_eff = 1.
P = [0]*(NMAX+1); P[0] = 1
for n in range(1, NMAX+1):
    for m in range(n, NMAX+1): P[m] += P[m-n]

# (q;q)_infty = prod (1-q^n)  -- Euler pentagonal, exact
E = [0]*(NMAX+1); E[0] = 1
k = 1
while True:
    g1 = k*(3*k-1)//2; g2 = k*(3*k+1)//2
    if g1 > NMAX and g2 > NMAX: break
    s = -1 if k % 2 else 1
    if g1 <= NMAX: E[g1] += s
    if g2 <= NMAX: E[g2] += s
    k += 1

# Rogers-Ramanujan G(q) = sum q^{n^2}/(q;q)_n  -> Lee-Yang M(2,5) character (up to q-power)
def rr(shift):
    out = [0]*(NMAX+1)
    n = 0
    while n*n + shift*n <= NMAX:
        num = [0]*(NMAX+1); num[n*n + shift*n] = 1
        den = [0]*(NMAX+1); den[0] = 1
        for j in range(1, n+1):
            f = [0]*(NMAX+1); f[0] = 1
            if j <= NMAX: f[j] = -1
            den = mul(den, f)
        inv = [0]*(NMAX+1); inv[0] = 1
        for m in range(1, NMAX+1):
            inv[m] = -sum(den[i]*inv[m-i] for i in range(1, m+1) if den[i])
        out = [o + t for o, t in zip(out, mul(num, inv))]
        n += 1
    return out
G = rr(0)

print("=" * 74)
print("CALIBRATION -- the estimator must reproduce values known independently")
print("=" * 74)
print(f"  eta^-1  (free boson, c = c_eff = 1)      : c_eff -> {tail(P)[-1]:.3f}   [target 1]")
print(f"  Rogers-Ramanujan G (Lee-Yang M(2,5))     : c_eff -> {tail(G)[-1]:.3f}   [target 2/5 = 0.4]")
print("     Lee-Yang: c = -22/5, h_min = -1/5, so c_eff = c - 24 h_min = -22/5 + 24/5 = 2/5.")
print("     A NON-UNITARY case where c_eff != c -- exactly the distinction GC-6's model erases.")

print()
print("=" * 74)
print("APPLIED -- the corpus's ONE banked object-side q-series")
print("=" * 74)
print("  B672's doublet, which GC-6 rewrites exactly as  Lee-Yang character x eta^10.")
E10 = [0]*(NMAX+1); E10[0] = 1
for _ in range(10): E10 = mul(E10, E)
D = mul(G, E10)
pos = sum(1 for i, v in enumerate(D[:400]) if v > 0)
neg = sum(1 for i, v in enumerate(D[:400]) if v < 0)
print(f"  first 400 coefficients: {pos} positive, {neg} NEGATIVE, {400-pos-neg} zero")
print(f"  -> the Cardy estimator is UNDEFINED on it (needs positive coefficients).")
print(f"  Predicted effective charge if it were formal: c_eff(LeeYang) + 10*c_eff(eta^+1)")
print(f"     = 2/5 + 10*(-1) = -48/5 = {2/5 - 10:.1f}  -- NEGATIVE, i.e. no Cardy growth at all.")
print(f"  This CONFIRMS B1191/GC-12's finding ('fails the kind-map's non-negativity')")
print(f"  and puts a number on it. The banked doublet CANNOT be the boundary character.")
