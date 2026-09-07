#!/usr/bin/env python3
"""c_eff OF THE OBJECT'S OWN BOUNDARY SERIES -- computed, not modelled.

Sources, read on-bench from Gukov-Manolescu arXiv:1904.06057v2 (owner-supplied):
  Prop 4.8   Zhat_0(Sigma(b1,b2,b3)) = q^Delta (C - Psi~^{-(a1)-(a2)-(a3)+(a4)}_{b1b2b3})
             with Psi~^(a)_p = sum_{n>=0} psi^(a)_{2p}(n) q^{n^2/4p},  psi = +-1 on n = +-a mod 2p
  eq (12)    Zhat_0(-Sigma(2,3,7)) = -q^{-1/2}(1 + q + q^3 + q^4 + q^5 + 2q^7 + ...)
             = Ramanujan's order-7 mock theta F_0(q)
  eq (13)    Zhat_0(S^3_{-1/2}(4_1)), a HYPERBOLIC surgery -- "the first computations of
             Zhat_a(q) for hyperbolic manifolds in the literature"

Estimator is GC-6's own, calibrated in certificates/c_eff_calibration.py
(eta^-1 -> 0.975 vs 1; Rogers-Ramanujan -> 0.388 vs 2/5).
Gate 5: q-series arithmetic only.
"""
import math
from fractions import Fraction as Fr

def c_eff(a, skip=2):
    out=[]
    for n in range(skip, len(a)-1):
        if a[n] <= 0 or a[n+1] <= 0: continue
        d = math.log(a[n+1]) - math.log(a[n])
        out.append((n, 6*n*d*d/math.pi**2))
    return out

# ---------- Prop 4.8: Zhat_0(Sigma(2,3,7)) ----------
b1,b2,b3 = 2,3,7
p = b1*b2*b3
al = [p-b1*b2-b1*b3-b2*b3, p+b1*b2-b1*b3-b2*b3, p-b1*b2+b1*b3-b2*b3, p+b1*b2+b1*b3-b2*b3]
sgn = [-1,-1,-1,+1]
print(f"Prop 4.8 for Sigma(2,3,7): p = {p}, alpha = {al}, signs {sgn}")
NMAX = 400_000            # in units of q^{n^2/(4p)} -> collect by exponent numerator n^2
terms = {}                # exponent (Fraction) -> coefficient
for n in range(0, 4000):
    r = n % (2*p)
    for a, s in zip(al, sgn):
        if r == a % (2*p):   psi = +1
        elif r == (-a) % (2*p): psi = -1
        else: continue
        e = Fr(n*n, 4*p)
        terms[e] = terms.get(e, 0) - s*psi     # Zhat = q^D (C - Psi~), C=0
ex = sorted(e for e,c in terms.items() if c)
print(f"  nonzero terms: {len(ex)}   first exponents: {[str(e) for e in ex[:8]]}")
print(f"  coefficients : {[terms[e] for e in ex[:14]]}")
print(f"  max |coeff|  : {max(abs(terms[e]) for e in ex)}")
gaps = [float(ex[i+1]-ex[i]) for i in range(min(10,len(ex)-1))]
print(f"  exponent gaps: {[round(g,3) for g in gaps]}  -> QUADRATIC spacing (false theta)")
print("  => bounded coefficients + quadratically sparse exponents: NO Cardy growth, c_eff = 0.\n")

# ---------- eq (12): the MIRROR, = Ramanujan order-7 mock theta F_0(q) ----------
N = 3000
F0 = [0]*(N+1)
n = 0
while n*n <= N:
    # q^{n^2} / (q^{n+1};q)_n  -- expand 1/prod_{j=n+1}^{2n} (1-q^j)
    num = [0]*(N+1); num[n*n] = 1
    den = [0]*(N+1); den[0] = 1
    for j in range(n+1, 2*n+1):
        f=[0]*(N+1); f[0]=1
        if j<=N: f[j]=-1
        new=[0]*(N+1)
        for i,di in enumerate(den):
            if di:
                if i<=N: new[i]+=di
                if i+j<=N: new[i+j]-=di
        den=new
    inv=[0]*(N+1); inv[0]=1
    for m in range(1,N+1):
        inv[m] = -sum(den[i]*inv[m-i] for i in range(1,m+1) if den[i])
    for i in range(n*n, N+1):
        if inv[i-n*n]: F0[i]+=inv[i-n*n]
    n += 1
print("eq (12)  Zhat_0(-Sigma(2,3,7)) = Ramanujan order-7 mock theta F_0(q)")
print(f"  computed : {F0[:12]}")
print(f"  paper    : [1, 1, 0, 1, 1, 1, 0, 2, 1, 2, 1, 2]")
print(f"  MATCH    : {F0[:12] == [1,1,0,1,1,1,0,2,1,2,1,2]}")
ce = c_eff(F0)
if ce:
    print(f"  c_eff at n={ce[-1][0]}: {ce[-1][1]:.4f}   (n={ce[len(ce)//2][0]}: {ce[len(ce)//2][1]:.4f})")
print()
print("=" * 74)
print("THE COMPARISON THE SIGMA BRIDGE ACTUALLY NEEDS")
print("=" * 74)
print(f"  target  c((E6)_1) = 78/13 = 6")
if ce: print(f"  object-side c_eff (mock theta, N={N})      = {ce[-1][1]:.4f}")
print(f"  mirror  (false theta, Prop 4.8)            = 0 (bounded coefficients)")
