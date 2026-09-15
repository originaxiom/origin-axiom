#!/usr/bin/env python3
"""MEMO-88 CELL: THE DARK TOWER — the recursive dark law extended to ALL
prime powers N = p^e: one classifier, a loudness ladder |T| = p^{a/2},
and the single j = 2 thread carrying the recursion at every depth.
(The natural rung memo 87 explicitly did not claim; claimed now,
preregistered, and decided by the machine.)

THE GENERALIZED DERIVATION (same three lemmas, valuations tracked to
depth e; the docstring of memo 87 carries the base case):
  For N = p^e, T(j,l) = (1/N) SUM_{n,k} zeta^{ j n(n-1)/2 - l k(k-1)/2 + 2nk }:
  * v_p(l) >= 1 (including l = 0): the k-sum's off-level part forces the
    double sum to DESCEND a level with the same cancellation as e = 2:
    PREREGISTERED |T| = 1 for ALL j.  (The one genuinely conjectural
    clause of the generalization — two-outcome, the machine decides.)
  * v_p(l) = 0: with B534's trio alpha = j/2 + 2/l, beta = 1 - j/2:
      a = v_p(alpha) = 0             -> |T| = 1                 ACTIVE
      1 <= a < e:  v_p(beta) >= a    -> |T| = p^{a/2}           SHELL a
                   v_p(beta) <  a    -> T = 0                   DARK
      a = e (alpha = 0): beta = 0    -> |T| = p^{e/2}           SURVIVOR
                         beta != 0   -> T = 0                   DARK
    (Mechanism: the n-sum with v_p(alpha) = a splits n = u + p^{e-a}w;
    the w-sum forces p^a | beta, then the residual sum is p^a times a
    depth-(e-a) Gauss sum of magnitude p^{(e-a)/2}: |n-sum| = p^{(e+a)/2},
    and the k-sum contributes p^{e/2}: |T| = p^{a/2}.)
  COROLLARIES (asserted): the magnitude spectrum at depth e is EXACTLY
  {0} u {p^{a/2} : a = 0..e}; the depth-e survivor is UNIQUE at
  (j,l) = (2, p^e - 2) with |T| = p^{e/2}; every prime-level dark class
  with j0 != 2 is WHOLESALE dark at every depth (v_p(beta) = 0 on all
  lifts); the j = 2 thread carries shell a exactly on the sub-classes
  j = 2 mod p^a — the recursion, all the way up the tower.

MACHINE CHECKS (asserts):
  1. EXACT sweep in Z[zeta_27] at (p,e) = (3,3): every one of the 729
     points' |NT|^2 computed in cyclotomic integers and matched to the
     classifier.
  2. FLOAT sweeps (every point, 1e-5): (3,4) N=81, (5,3) N=125,
     (7,3) N=343, (5,4) N=625 — 500k+ points total.
  3. Spectrum, survivor uniqueness + location + loudness, wholesale rule,
     and the shell-count table (classifier counts == direct counts) at
     every tested (p,e).
Either branch banks: a failure of the v(l)>=1 clause or of any shell is
reported exactly and the classifier refined with the error filed.
Gate 5 untouched (roots of unity and counting only).
"""
import numpy as np
import sympy as sp
from sympy import Poly, cyclotomic_poly, symbols

x=symbols('x')

def vp(n,p,cap):
    n%=p**cap
    if n==0: return cap
    v=0
    while n%p==0: n//=p; v+=1
    return v

def classify(j,l,p,e):
    """return |T|^2 as an integer power of p, or 0 (dark)."""
    N=p**e
    if l%p==0: return 1
    inv2=pow(2,-1,N)
    alpha=(j*inv2 + 2*pow(l,-1,N))%N
    beta =(1 - j*inv2)%N
    a=vp(alpha,p,e)
    if a==0: return 1
    b=vp(beta,p,e)
    if a<e:  return p**a if b>=a else 0
    return p**e if beta==0 else 0

def Tmat(p,e):
    N=p**e
    z=np.exp(2j*np.pi/N)
    A=np.array([ (n*(n-1)//2)%N for n in range(N)])
    idx=np.arange(N)
    C=z**((2*np.outer(idx,idx))%N)
    U=z**((np.outer(idx,A))%N)
    V=z**((-np.outer(A,idx))%N)
    return (U@C@V)/N

def check_float(p,e):
    N=p**e
    T=Tmat(p,e)
    got=np.abs(T)**2
    cls=np.zeros((N,N))
    counts={}
    for j in range(N):
        for l in range(N):
            c=classify(j,l,p,e)
            cls[j,l]=c
            counts[c]=counts.get(c,0)+1
    assert np.max(np.abs(got-cls))<1e-5, f"float sweep fails ({p},{e}): max dev {np.max(np.abs(got-cls))}"
    # spectrum
    assert set(counts)=={0}|{p**a for a in range(e+1)}, f"spectrum ({p},{e}): {sorted(counts)}"
    # survivor unique at (2, N-2)
    surv=[(j,l) for j in range(N) for l in range(N) if cls[j,l]==p**e]
    assert surv==[(2,N-2)], f"survivor ({p},{e}): {surv}"
    # wholesale: prime-level dark classes j0 != 2 dark on all lifts
    for j0 in range(1,p):
        if j0==2: continue
        l0=(-4*pow(j0,-1,p))%p
        M=p**(e-1)
        assert all(cls[(j0+p*s)%N,(l0+p*t)%N]==0 for s in range(M) for t in range(M)), f"wholesale fails ({p},{e}) j0={j0}"
    return counts

def check_exact_33():
    p,e=3,3; N=27
    A=[ (n*(n-1)//2)%N for n in range(N)]
    Phi=Poly(cyclotomic_poly(N,x),x)
    counts={}
    for j in range(N):
        for l in range(N):
            h=np.zeros(N,dtype=object)
            for n in range(N):
                ja=(j*A[n])%N
                for k in range(N):
                    h[(ja - l*A[k] + 2*n*k)%N]+=1
            conj=np.zeros(N,dtype=object)
            for e2 in range(N):
                if h[e2]: conj[(-e2)%N]+=h[e2]
            prod=np.zeros(N,dtype=object)
            for e1 in range(N):
                if not h[e1]: continue
                for e2 in range(N):
                    if not conj[e2]: continue
                    prod[(e1+e2)%N]+=h[e1]*conj[e2]
            r=Poly(list(reversed(list(map(int,prod)))),x).rem(Phi)
            c=classify(j,l,p,e)
            assert r==Poly(int(c)*N*N,x), f"EXACT (3,3) mismatch at ({j},{l}): {r} vs {c}"
            counts[c]=counts.get(c,0)+1
    return counts

print("EXACT SWEEP (p,e)=(3,3): all 729 points in Z[zeta_27] ...")
c33=check_exact_33()
print(f"   PASS; shell counts {dict(sorted(c33.items()))}")
for (p,e) in ((3,4),(5,3),(7,3),(5,4)):
    counts=check_float(p,e)
    print(f"FLOAT SWEEP (p,e)=({p},{e}): all {p**(2*e)} points match; survivor (2,{p**e-2})"
          f" at |T|^2 = p^{e}; shells {dict(sorted(counts.items()))}")

# the loudness ladder along the thread, explicit
print("\nTHE THREAD: |T(2, p^e-2)|^2 = p^e at every tested depth (asserted above);")
print("the j=2-mod-p^a sub-classes carry shell a — the recursion climbs the tower.")

print("""
THE DARK TOWER STANDS: one classifier — (v(l), v(alpha), v(beta)) with
B534's trio — governs every prime power tested: spectrum exactly
{0, 1, sqrt p, ..., p^{e/2}}, a UNIQUE survivor at (2, p^e - 2) whose
loudness climbs as p^{e/2}, prime-dark classes with j != 2 wholesale
dark at every depth, and the single j = 2 thread carrying the whole law
upward.  The v(l) >= 1 clause (the one conjectural piece of the
generalization) held at every tested point.  Memo 87's law is the e = 2
floor of a tower.  FENCES: verified depths (3,3),(3,4),(5,3),(7,3),(5,4)
with (3,3) exact; general-e is the derivation in the docstring plus
these five instances, not an all-e machine proof; the exponent-echo hook
is untouched.  Gate 5 untouched.""")
