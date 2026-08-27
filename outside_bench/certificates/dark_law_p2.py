#!/usr/bin/env python3
"""MEMO-87 CELL: THE RECURSIVE DARK LAW PROVED — the named open step of
B566-S1 (the owner's H123, buried since 2026-07-14) paid: the N = p^2
dark-hyperbola law is derived by elementary degenerate Gauss sums, and
every banked count becomes a polynomial identity.

THE OBJECT (B534's pinned convention, banked): on (Z/N)^2,
    N * T(j,l) = SUM_{n,k mod N} zeta^E,
    E = j*n(n-1)/2 - l*k(k-1)/2 + 2nk,   zeta = e^{2 pi i / N}.
B534 PROVED the prime-level law (spectrum {0,1,sqrt p}; p-2 dark points on
j*l = -4; survivor (2,p-2)).  B566-S1 found the N = p^2 law EMPIRICALLY
(7 primes) and named the open step: "the symbolic proof (degenerate Gauss
sums at p^2)."  This cell supplies that proof and machine-checks every
piece.

THE PROOF (all steps elementary; p odd; 2 invertible mod p^2):
  LEMMA G1 (nondegenerate Gauss sum at p^2):  for p NOT | a:
    SUM_{x mod p^2} zeta^{a x^2} = p   EXACTLY (not just |.|):
    x = u + pv  =>  x^2 = u^2 + 2puv mod p^2; the v-sum gives
    p*[u = 0 mod p]; only u = 0 survives; total = p.
  LEMMA G2 (once-degenerate):  for a = p*a', p NOT | a':
    SUM_{x mod p^2} zeta^{p a' x^2} = p * g_p(a'),  |g_p| = sqrt p
    (the sum descends to the prime level with multiplicity p).
  LEMMA G3 (linear):  SUM_x zeta^{b x} = p^2*[p^2|b], and
    SUM_x zeta^{p b' x} = 0 for p NOT | b'.
  THE CASE ANALYSIS (complete the square twice, exactly as B534 at prime
  level, now tracking p-valuations):  write J = j/2, L = l/2 mod p^2.
  * v_p(l) = 0:  the k-sum is G1 (coefficient -L unit): = p * zeta^{Lc^2},
    c = 1/2 + n/L; the n-exponent becomes alpha*n^2 + beta*n + gamma with
    alpha = j/2 + 2/l, beta = 1 - j/2, gamma = l/8 (B534's trio, verbatim):
      - v_p(alpha) = 0:  G1 again  => |T| = 1                       ACTIVE
      - v_p(alpha) = 1:  n = u+pv splits; the v-sum forces p | beta:
          p NOT | beta  => T = 0                                    DARK
          p | beta      => p * (prime Gauss sum)  => |T| = sqrt p   DEEP
      - v_p(alpha) = 2:  pure linear (G3):
          beta != 0 mod p^2  => T = 0                               DARK
          beta  = 0 mod p^2  => |T| = p; forces (j,l) = (2, p^2-2) SURVIVOR
  * v_p(l) = 1:  the k-sum's v-part forces p | n; the whole double sum
    descends to a PRIME-level pair sum whose n1-sum is a delta:
    |T| = 1 for ALL j                                               ACTIVE
  * v_p(l) = 2 (l = 0):  k-sum = p^2*[n=0]  =>  T = 1               ACTIVE
  THE COUNTS (j <-> alpha is an affine bijection per unit l):
    |T|=1 : (p^2-p)^2 + (p-1)p^2 + p^2  =  p^2(p^2 - p + 1)
    DARK  : p^2(p-2) + (p-1)            =  (p-2)p^2 + (p-1)
    sqrt p: p(p-1)        SURVIVOR: 1
  — all four are POLYNOMIAL IDENTITIES (asserted symbolically below) and
  match B566-S1's banked table exactly.
  THE RECURSION (B566-S1's "9 of 10 wholesale"): a prime-level dark class
  (j0,l0) with j0 != 2 has beta unit on EVERY lift => ALL p^2 lifts dark
  (wholesale); the j0 = 2 class has p | beta on its lifts and recapitulates
  the {dark, sqrt p, survivor} split one level down — both read off the
  classifier, and verified in the sweeps.
MACHINE CHECKS (asserts):
  1. G1/G2 verified EXACTLY in Z[zeta_{p^2}] (reduction mod the cyclotomic
     polynomial) for p in {3,5,7}, all unit coefficients.
  2. FULL EXACT SWEEP at p in {3,5}: |N T|^2 computed in Z[zeta] for ALL
     (j,l), reduced mod Phi_{p^2} to a rational integer, compared to the
     classifier: EVERY point must match {0, p^4, p^5, p^6}.
  3. FLOAT SWEEP at p in {7,11,13}: all points vs the classifier (1e-6).
  4. The four count formulas as symbolic polynomial identities AND as
     exact counts at every tested p.
  5. The recursion statements verified at p = 11.
STATUS ON SUCCESS: the LIVE law of B566-S1 is upgraded to PROVED — the
derivation above is p-uniform and elementary; the machine checks pin every
lemma and the full classifier at five primes (two of them exactly).  The
exponent-echo HOOK (recursion depth vs e4) remains a hook — untouched.
Gate 5 untouched (roots of unity and counting only).
"""
import numpy as np
import sympy as sp
from sympy import Poly, cyclotomic_poly, symbols

x=symbols('x')

def exact_reduce(coeffs, N):
    """coeffs: integer array indexed by exponent mod N -> element of Z[zeta_N];
    return the sympy Poly remainder mod Phi_N(x) (equality test vehicle)."""
    P=Poly(list(reversed(list(map(int,coeffs)))), x) if any(coeffs) else Poly(0,x)
    return P.rem(Poly(cyclotomic_poly(N,x),x))

def conj_sq_exact(coeffs, N):
    """|z|^2 for z in Z[zeta_N] given exponent-coefficient vector: returns the
    reduced Poly of z * conj(z) (conj: exponent e -> -e mod N)."""
    conj=np.zeros(N,dtype=object)
    for e in range(N):
        if coeffs[e]: conj[(-e)%N]+=coeffs[e]
    prod=np.zeros(N,dtype=object)
    for e1 in range(N):
        c1=coeffs[e1]
        if not c1: continue
        for e2 in range(N):
            c2=conj[e2]
            if not c2: continue
            prod[(e1+e2)%N]+=c1*c2
    return exact_reduce(prod,N)

# ---- 1. the Gauss lemmas, exactly
for p in (3,5,7):
    N=p*p
    for a in range(1,N):
        if a%p==0: continue
        h=np.zeros(N,dtype=object)
        for xx in range(N): h[(a*xx*xx)%N]+=1
        h[0]-=p
        assert exact_reduce(h,N)==Poly(0,x), f"G1 fails p={p} a={a}"
    for ap in range(1,p):
        h=np.zeros(N,dtype=object)
        for xx in range(N): h[(p*ap*xx*xx)%N]+=1
        r=conj_sq_exact(h,N)
        assert r==Poly(p**3,x), f"G2 fails p={p} a'={ap}: {r}"
print("LEMMAS G1/G2: exact in Z[zeta_{p^2}] for p in {3,5,7}, all unit coefficients")

# ---- the classifier from the proof
def classify(j,l,p):
    N=p*p
    inv2=pow(2,-1,N)
    vl = 2 if l%N==0 else (1 if l%p==0 else 0)
    if vl>=1: return 1                      # |T| = 1  (cases B and C)
    alpha=(j*inv2 + 2*pow(l,-1,N))%N
    beta =(1 - j*inv2)%N
    va = 2 if alpha==0 else (1 if alpha%p==0 else 0)
    if va==0: return 1
    if va==1: return p if beta%p==0 else 0   # returns |T|^2 in {p} or 0
    return p*p if beta==0 else 0             # survivor |T|^2 = p^2, else dark
# encoding: return value = |T|^2 (1, p, p^2) or 0

# ---- 2. full exact sweep at p in {3,5}
for p in (3,5):
    N=p*p
    A=[ (n*(n-1)//2)%N for n in range(N)]
    counts={0:0,1:0,p:0,p*p:0}
    for j in range(N):
        for l in range(N):
            h=np.zeros(N,dtype=object)
            for n in range(N):
                ja=(j*A[n])%N
                for k in range(N):
                    h[(ja - l*A[k] + 2*n*k)%N]+=1
            r=conj_sq_exact(h,N)
            cls=classify(j,l,p)
            want=Poly(int(cls)*N*N,x)   # |N T|^2 = cls * N^2
            assert r==want, f"exact sweep mismatch p={p} (j,l)=({j},{l}): got {r}, classifier {cls}"
            counts[cls]+=1
    assert counts[0]==(p-2)*p*p+(p-1)
    assert counts[1]==p*p*(p*p-p+1)
    assert counts[p]==p*(p-1)
    assert counts[p*p]==1
    print(f"EXACT SWEEP p={p}: all {N*N} points match the classifier in Z[zeta]; counts exact")

# ---- 3. float sweep at p in {7,11,13}
for p in (7,11,13):
    N=p*p
    z=np.exp(2j*np.pi/N)
    A=np.array([ (n*(n-1)//2)%N for n in range(N)])
    nk=np.outer(np.arange(N),np.arange(N))
    C=z**((2*nk)%N)
    U=z**((np.outer(np.arange(N),A))%N)      # U[j,n]
    V=z**((-np.outer(A,np.arange(N)))%N)     # V[k,l]
    Tm=(U@C@V)/N
    counts={0:0,1:0,p:0,p*p:0}
    for j in range(N):
        for l in range(N):
            cls=classify(j,l,p)
            got=abs(Tm[j,l])**2
            assert abs(got-cls)<1e-5, f"float sweep p={p} ({j},{l}): {got} vs {cls}"
            counts[cls]+=1
    assert counts[0]==(p-2)*p*p+(p-1) and counts[1]==p*p*(p*p-p+1)
    assert counts[p]==p*(p-1) and counts[p*p]==1
    print(f"FLOAT SWEEP p={p}: all {N*N} points match; counts exact")

# ---- 4. the count formulas as polynomial identities
P=symbols('p')
assert sp.expand((P**2-P)**2 + (P-1)*P**2 + P**2 - P**2*(P**2-P+1))==0
assert sp.expand(P**2*(P-2)+(P-1) - ((P-2)*P**2+(P-1)))==0
tot=sp.expand(((P-2)*P**2+(P-1)) + P**2*(P**2-P+1) + P*(P-1) + 1 - P**4)
assert tot==0
print("COUNTS: the four formulas are polynomial identities summing to p^4")

# ---- 5. the recursion at p = 11 (from the classifier, spot-verified above)
p=11; N=p*p
hyper=[(j0,(-4*pow(j0,-1,p))%p) for j0 in range(1,p)]
wholesale=0; recap=None
for (j0,l0) in hyper:
    lifts=[classify(j0+p*s, l0+p*t, p) for s in range(p) for t in range(p)]
    if j0!=2:
        assert all(c==0 for c in lifts); wholesale+=1
    else:
        assert sorted(set(lifts))==[0,p,p*p]; recap=lifts
assert wholesale==p-2
print(f"RECURSION p=11: {wholesale} of {p-1} prime-dark classes wholesale dark;")
print("   the j=2 class recapitulates the {dark, sqrt p, survivor} split — as derived")

print("""
THE RECURSIVE DARK LAW IS PROVED.  The named open step of B566-S1
("degenerate Gauss sums at p^2") is paid: three elementary lemmas + the
double complete-the-square give the classifier
  v(l)>=1 -> ACTIVE(1);  v(l)=0: v(alpha)=0 -> ACTIVE(1);
  v(alpha)=1 -> DARK unless p|beta -> sqrt p;
  v(alpha)=2 -> DARK unless beta=0 -> SURVIVOR(p),
whose counts are polynomial identities matching the banked table, whose
spectrum is exactly {0, 1, sqrt p, p}, and whose wholesale/recapitulation
recursion is a two-line corollary.  Verified exactly in Z[zeta_{p^2}] at
p = 3, 5 (every point) and at p = 7, 11, 13 (every point, float), lemmas
exact at 3, 5, 7.  The owner's H123 (2026-07-14) moves from BURIED LIVE
LAW to PROVED.  The exponent-echo hook stays a hook.  Gate 5 untouched.""")
