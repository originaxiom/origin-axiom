#!/usr/bin/env python3
"""C1: THE WEYL COEFFICIENT, DERIVED — the cusp-spectrum counting law
N(T) = (T/pi) log(T sqrt(3)/(2 pi e)) is computed from the functional equation
of Lambda_K, not asserted, and validated against the zero census.

VI.3(a)'s named residue: B739/B1142 use the smooth law as an instrument; here
it is DERIVED: for K = Q(sqrt(-3)) (r1=0, r2=1, |d_K|=3),
    Lambda_K(s) = (sqrt(3)/(2 pi))^s Gamma(s) zeta_K(s),  Lambda_K(s)=Lambda_K(1-s)
(functional equation verified numerically to 1e-20 below), so by the argument
principle N(T) = theta_K(T)/pi + S(T) with
    theta_K(T) = Im[ log Gamma(1/2 + iT) ] + T log(sqrt(3)/(2 pi)),
and Stirling gives theta_K(T)/pi = (T/pi) log(T sqrt(3)/(2 pi e)) + c + O(1/T)
— the constant c is MEASURED below, not guessed; the data shows c = 0 (the
constant vanishes for this completed form, decaying ~ 1/T — unlike the
Riemann-zeta case, where the analogous constant is 7/8).  VALIDATION: the census of zeros to
T = 130 (recomputed in-run: 43 zeta + 65 L(chi_-3)) against the derived law at
checkpoints, with the remainder |S(T)| bounded as the argument principle
demands.  PREREGISTERED: |N_obs(T) - theta_K(T)/pi| < 2 for all checkpoints
(S(T) is O(log T) with small constant at these heights) — or the law fails.
"""
from mpmath import mp, mpf, mpc, gamma, loggamma, zeta, pi, sqrt, log, exp, arg, findroot, im

mp.dps = 30

def L_chi3(s):
    return 3**(-s) * (zeta(s, mpf(1)/3) - zeta(s, mpf(2)/3))
def zeta_K(s):
    return zeta(s) * L_chi3(s)
def Lambda_K(s):
    return (sqrt(mpf(3))/(2*pi))**s * gamma(s) * zeta_K(s)

# functional equation check (the completed form is right)
pts = [mpc(0.3, 2.1), mpc(0.7, 5.5), mpc(0.25, 11.0)]
errs = [abs(Lambda_K(s) - Lambda_K(1-s)) / abs(Lambda_K(s)) for s in pts]
print("functional equation Lambda_K(s) = Lambda_K(1-s), relative errors:", [float(e) for e in errs])
assert all(e < mpf(10)**(-18) for e in errs)

# theta_K and its Stirling form; extract the constant term symbolically-numerically
def theta_K(T):
    return im(loggamma(mpc(0.5, T))) + T*log(sqrt(mpf(3))/(2*pi))
def smooth(T):
    return (T/pi)*log(T*sqrt(mpf(3))/(2*pi*exp(1)))
# constant = lim (theta_K/pi - smooth); check it stabilizes (Stirling constant)
consts = [(T, float(theta_K(mpf(T))/pi - smooth(mpf(T)))) for T in (50, 100, 500, 2000, 10000)]
print("theta_K(T)/pi - (T/pi)log(T sqrt3/2 pi e) at increasing T:", consts)
c_inf = theta_K(mpf(100000))/pi - smooth(mpf(100000))
print(f"the Stirling constant  = {c_inf}  -> the constant term VANISHES (decays ~1/T; contrast Riemann 7/8)")
assert abs(c_inf) < mpf(10)**(-5)

# census to T = 130 (recomputed, not read from the banked file)
from mpmath import zetazero
zz = []
n = 1
while True:
    z = zetazero(n).imag
    if z > 130: break
    zz.append(z); n += 1
def hardyL(t):
    s = mpc(0.5, t)
    g = ((mpf(3)/pi)**((s+1)/2)) * gamma((s+1)/2)
    return (exp(mpc(0, arg(g))) * L_chi3(s)).real
zl = []
t = mpf('0.1'); f0 = hardyL(t)
while t < 130:
    t2 = t + mpf('0.05'); f1 = hardyL(t2)
    if f0*f1 < 0:
        zl.append(findroot(hardyL, (t, t2), solver='bisect', tol=mpf(10)**(-15)))
    t, f0 = t2, f1
print(f"census recomputed: {len(zz)} zeta zeros + {len(zl)} L(chi_-3) zeros = {len(zz)+len(zl)} (banked: 43+65=108)")
assert (len(zz), len(zl)) == (43, 65)

merged = sorted(zz + zl)
print("\ncheckpoint table: T | N_obs | theta_K(T)/pi | remainder S(T)")
ok = True
for T in (30, 50, 80, 100, 130):
    nobs = sum(1 for z in merged if z <= T)
    pred = theta_K(mpf(T))/pi
    S = nobs - pred
    print(f"  {T:5d} | {nobs:5d} | {float(pred):10.3f} | {float(S):+.3f}")
    ok = ok and abs(S) < 2
print("preregistered gate |S(T)| < 2 at all checkpoints:", ok)
assert ok

print("""
C1 CLOSED: the counting law is DERIVED — Lambda_K's verified functional
equation + the argument principle + Stirling give N(T) = (T/pi) log(T sqrt3/
(2 pi e)) + const + S(T), and the recomputed 108-zero census tracks it with
|S(T)| < 2 at every checkpoint.  B1142's density instrument (the 697x-sparse
falsification) now rests on a derived coefficient, not an asserted one.
Placement, not value; Gate 5 untouched.""")
