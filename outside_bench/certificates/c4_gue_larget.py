#!/usr/bin/env python3
"""C4 (HANDOFF to the banking seat's i9/64GB): LARGE-T GUE for zeta_K = zeta * L(chi_-3).

Discharges gue_bench.py's preregistered continuation ("re-run at much larger T,
thousands of zeros, before drawing any conclusion").  PREREGISTERED two-outcome:
with >= 3000 merged zeros, the unfolded nearest-neighbor spacings' KS distance
to the GUE Wigner surmise is SMALLER than to Poisson with p_GUE > 0.01 and
p_Poisson < 1e-6 (level repulsion confirmed at scale) — or not (the T=130 hint
was noise; banked negative).  GUE-genericity caveat stands regardless (B1142):
this certifies a universality class, never object-specificity.

Run:  python3 c4_gue_larget.py [T_MAX]      (default 3000; ~hours)
Checkpoints appended to c4_zeros_zeta.txt / c4_zeros_L.txt — safe to re-run,
it resumes past the largest stored zero.  Final block prints the KS table.
"""
import sys, os
from mpmath import mp, mpf, zetazero, zeta, gamma, pi, sqrt, log, exp, findroot, cos, sin, arg, mpc

mp.dps = 25
T_MAX = mpf(sys.argv[1]) if len(sys.argv) > 1 else mpf(3000)

def L_chi3(s):
    # L(s, chi_-3) = 3^{-s} (zeta(s,1/3) - zeta(s,2/3)), valid all s
    return 3**(-s) * (zeta(s, mpf(1)/3) - zeta(s, mpf(2)/3))

def completed_L_phase(t):
    # Hardy-style real rotation for L(1/2+it, chi_-3), conductor 3, odd character:
    # Lambda(s) = (3/pi)^{(s+1)/2} Gamma((s+1)/2) L(s);  Z(t) = e^{i theta(t)} L(1/2+it) real
    s = mpc(0.5, t)
    g = ((mpf(3)/pi)**((s+1)/2)) * gamma((s+1)/2)
    th = arg(g)
    return (exp(mpc(0, th)) * L_chi3(s)).real

def zeta_zeros(tmax, fname):
    zs = []
    if os.path.exists(fname):
        zs = [mpf(x) for x in open(fname).read().split()]
    n = len(zs) + 1
    while True:
        z = zetazero(n).imag
        if z > tmax: break
        zs.append(z); open(fname, 'a').write(str(z) + '\n'); n += 1
        if n % 200 == 0: print(f"  zeta zeros: {n} (t={float(z):.1f})", flush=True)
    return zs

def L_zeros(tmax, fname):
    zs = []
    t0 = mpf('0.05')
    if os.path.exists(fname):
        zs = [mpf(x) for x in open(fname).read().split()]
        if zs: t0 = zs[-1] + mpf('0.05')
    # adaptive scan: step = min(0.05, half local mean spacing of zeta_K)
    t = t0; f0 = completed_L_phase(t)
    while t < tmax:
        dens = (log(t * sqrt(mpf(3)) / (2*pi)) / pi) if t > 3 else mpf(1)
        step = min(mpf('0.05'), 1/(4*dens))
        t2 = t + step; f1 = completed_L_phase(t2)
        if f0 * f1 < 0:
            z = findroot(completed_L_phase, (t, t2), solver='bisect', tol=mpf(10)**(-18))
            zs.append(z); open(fname, 'a').write(str(z) + '\n')
            if len(zs) % 200 == 0: print(f"  L zeros: {len(zs)} (t={float(z):.1f})", flush=True)
        t, f0 = t2, f1
    return zs

print(f"C4: scanning to T = {T_MAX}")
zz = zeta_zeros(T_MAX, 'c4_zeros_zeta.txt')
zl = L_zeros(T_MAX, 'c4_zeros_L.txt')
print(f"zeta zeros: {len(zz)}   L(chi_-3) zeros: {len(zl)}   merged: {len(zz)+len(zl)}")

# GATE 1 (density): merged count vs the derived smooth law N(T) = (T/pi) log(T sqrt3/(2 pi e))
NT = (T_MAX/pi) * log(T_MAX * sqrt(mpf(3)) / (2*pi*exp(1)))
obs = len(zz) + len(zl)
print(f"density gate: observed {obs} vs smooth N(T) = {float(NT):.1f}  (|diff| should be O(log T))")

# unfold + KS
merged = sorted(zz + zl)
def Nsm(t): return (t/pi) * log(t * sqrt(mpf(3)) / (2*pi*exp(1)))
unf = [Nsm(t) for t in merged]
sp_ = [float(b - a) for a, b in zip(unf, unf[1:]) if b > a]
mean = sum(sp_)/len(sp_)
print(f"unfolded mean spacing = {mean:.6f} (gate: within 0.01 of 1)")
sp_ = sorted(s/mean for s in sp_)
import math
def cdf_gue(s): return 1 - math.exp(-4*s*s/math.pi)*(1 + 0)  # Wigner surmise CDF: 1 - e^{-4s^2/pi}...
# NOTE: GUE Wigner surmise: p(s) = (32/pi^2) s^2 e^{-4 s^2/pi};  CDF = erf-free closed form:
def cdf_gue(s):
    # integral: 1 - e^{-4s^2/pi} * ... use numeric integration for correctness
    from math import erf, sqrt as msqrt, exp as mexp, pi as mpi
    a = 4/mpi
    return erf(msqrt(a)*s) - (2*msqrt(a)*s/msqrt(mpi)) * mexp(-a*s*s)
def cdf_poisson(s): return 1 - math.exp(-s)
def ks(cdf):
    n = len(sp_); d = 0.0
    for i, s in enumerate(sp_):
        d = max(d, abs((i+1)/n - cdf(s)), abs(i/n - cdf(s)))
    lam = (math.sqrt(n) + 0.12 + 0.11/math.sqrt(n)) * d
    p = 2*sum((-1)**(k-1) * math.exp(-2*k*k*lam*lam) for k in range(1, 101))
    return d, max(min(p, 1.0), 0.0)
dg, pg = ks(cdf_gue); dp, pp = ks(cdf_poisson)
print(f"KS vs GUE Wigner surmise: D = {dg:.5f}  p = {pg:.3e}")
print(f"KS vs Poisson:            D = {dp:.5f}  p = {pp:.3e}")
verdict = "GUE-CONSISTENT, POISSON REJECTED" if (pg > 0.01 and pp < 1e-6 and dg < dp) else "PREREGISTERED GATE NOT MET — report honestly"
print("VERDICT (against the preregistered gate):", verdict)
