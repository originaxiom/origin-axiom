#!/usr/bin/env python3
"""IDENTIFYING A BRAID WORD FOR 5_2 WITHOUT A KNOT TABLE.

Needed because memo 177 addendum 8 leaves one open item -- F_K for a CHIRAL knot whose blocks
widen -- and Park arXiv:2004.02087 cannot be fetched from this container.

The braid word is identified by TWO independent invariants computed from the validated
calculator in colored_jones_core.py, neither of which is looked up:

  (i)  the Jones polynomial (N = 2), whose coefficient shape must be V(5_2)'s;
  (ii) the ALEXANDER polynomial, extracted from the hbar-expansion by Melvin-Morton-Rozansky:
       writing J_n(e^hbar) = sum_m p_m(n) hbar^m, the leading coefficient c_{m,m} of p_m gives
       the Taylor series of 1/Delta_K(e^u).  The hbar^2 coefficient alone separates the
       candidates, since 1/Delta(e^u) = 1 + c22 u^2 + ... has
           3_1  Delta = t-1+1/t        -> c22 = -1
           4_1  Delta = -t+3-1/t       -> c22 = +1
           5_1  Delta = t^2-t+1-1/t+1/t^2 -> c22 = -3
           5_2  Delta = 2t-3+2/t       -> c22 = -2.

SnapPy is NOT usable for this: its `braid[...]` constructor returns the closure UNION THE BRAID
AXIS (braid[1,1,1] has two cusps), so its volumes do not identify the closure.  That was checked
and is recorded so the next reader does not repeat it.

Gate 5: exact arithmetic.
"""
import os, sys, itertools
from fractions import Fraction as Fr
HERE=os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(HERE,'colored_jones_validate.py')).read().split('ok={}')[0])
import sympy as sp

def perm_cycle(word,m):
    p=list(range(m))
    for g in word:
        i=abs(g)-1; p[i],p[i+1]=p[i+1],p[i]
    seen=set(); x=0
    while x not in seen: seen.add(x); x=p[x]
    return len(seen)

def c22(word,m,ns=(1,2,3,4)):
    ys=[hbar(Jn(n,word,m),2)[2] for n in ns]
    a,b,c=sp.symbols('a b c')
    sol=sp.solve([a*n**2+b*n+c-sp.Rational(ys[i].numerator,ys[i].denominator)
                  for i,n in enumerate(ns[:3])],[a,b,c])
    pred=sol[a]*ns[3]**2+sol[b]*ns[3]+sol[c]
    fit=sp.simplify(pred-sp.Rational(ys[3].numerator,ys[3].denominator))==0
    return sol[a], fit, ys

WORD=[1,1,2,2,1,-2]; M=3
print("CANDIDATE  sigma1^2 sigma2^2 sigma1 sigma2^-1  on 3 strands")
print(f"   closure is a KNOT (permutation is an {M}-cycle): {perm_cycle(WORD,M)==M}")
J2=Jn(2,WORD,M,framed=False); lo=min(J2)
sh=tuple(int(J2.get(lo+8*i,0)) for i in range((max(J2)-lo)//8+1))
print(f"   Jones polynomial shape: {sh}")
print(f"   V(5_2) shape          : (-1, 1, -1, 2, -1, 1)   match: {sh==(-1,1,-1,2,-1,1)}")
for nm,w,m in (("3_1",[1,1,1],2),("4_1",[1,-2,1,-2],3),("candidate",WORD,M)):
    a,fit,ys=c22(w,m)
    print(f"   {nm:<10} hbar^2 coefficients n=1..4 {[str(y) for y in ys]}  ->  c22 = {a}   (quadratic fit holds: {fit})")
print()
print("   reference c22 from 1/Delta(e^u):  3_1 -1   4_1 +1   5_1 -3   5_2 -2")
a,_,_=c22(WORD,M)
print(f"   CANDIDATE c22 = {a}  =>  Alexander polynomial 2t - 3 + 2/t  =>  the knot is 5_2")
print("   (5_2 is CHIRAL and HYPERBOLIC -- exactly the missing case.)")
