#!/usr/bin/env python3
"""BOTH OF GUKOV-JAGADALE's WORKED EXAMPLES, MEASURED DIRECTLY.

Owner instruction: "papers are old, dont rely on them, verify all."

[GJ] = Gukov, Jagadale, arXiv:2308.05360, compute c_eff for T[Sigma(2,3,5)] and T[Sigma(2,3,7)]
by mock modularity, via
    eq (33)  Zhat(Sigma(2,3,5);q) = q^{3/2} chi_0(q),   chi_0(q) = sum_n q^n     / (q^{n+1};q)_n
    eq (54)  Zhat(Sigma(2,3,7);q) = q^{-1/2} F_0(q),    F_0(q)   = sum_n q^{n^2} / (q^{n+1};q)_n
and print HALF-INDEX values c_eff = 6/5 and 8/7.

[HJNP] = Harichurn-Jagadale-Noshchenko-Passaro, arXiv:2508.10087, expect (their eq (9))
    c_eff = 24 ( m^2 / (4 s t p) - l ),
which at m = 1, l = 0 gives 1/5 for Sigma(2,3,5) and 1/7 for Sigma(2,3,7).

The two differ by exactly 1, the universal q^{-1/24} prefactor.  THIS FILE MEASURES THE BARE
SERIES and decides which convention the coefficient growth follows -- with the estimator
calibrated beforehand on eta^-1 and Rogers-Ramanujan to better than 0.01%.

Both mock theta series are built by TERM RECURSION rather than by dividing each term from
scratch (the naive route is O(L^3) and timed out):
    T_n = q^{p(n)}/(q^{n+1};q)_n ,
    T_{n+1}/T_n = q^{p(n+1)-p(n)} (1-q^{n+1}) / ((1-q^{2n+1})(1-q^{2n+2})).

CONTROL: the printed first terms of F_0 must match GM eq (175) / [GJ] eq (54),
    1 + q + q^3 + q^4 + q^5 + 2q^7 + q^8 + 2q^9 + q^10 + 2q^11 + q^12 + 3q^13.

Gate 5: exact integer series in, one fit out.
"""

import math
L=5000
def mulbin(a,j,sign):   # multiply by (1 - q^j)
    b=a[:]
    for i in range(L,j-1,-1): b[i]+=sign*a[i-j]
    return b
def divbin(a,j):        # divide by (1 - q^j)  ==  multiply by 1+q^j+q^{2j}+...
    b=a[:]
    for i in range(j,L+1): b[i]+=b[i-j]
    return b
def mock(p):
    out=[0]*(L+1)
    T=[0]*(L+1)
    if p(0)<=L: T[p(0)]=1
    n=0
    while True:
        if all(v==0 for v in T): break
        for i in range(L+1): out[i]+=T[i]
        d=p(n+1)-p(n)
        if d>L: break
        nt=[0]*(L+1)
        for i in range(L+1-d):
            if T[i]: nt[i+d]+=T[i]
        nt=mulbin(nt,n+1,-1)
        nt=divbin(nt,2*n+1); nt=divbin(nt,2*n+2)
        T=nt; n+=1
        if n>L: break
    return out
def fit3(a,lo,hi):
    X=[];Y=[]
    for n in range(lo,hi+1):
        if n>1 and a[n]>0: X.append((math.sqrt(n),math.log(n),1.0)); Y.append(math.log(a[n]))
    m=3; M=[[sum(X[i][p]*X[i][q] for i in range(len(X))) for q in range(m)] for p in range(m)]
    V=[sum(X[i][p]*Y[i] for i in range(len(X))) for p in range(m)]
    for c in range(m):
        piv=max(range(c,m),key=lambda rr:abs(M[rr][c])); M[c],M[piv]=M[piv],M[c]; V[c],V[piv]=V[piv],V[c]
        for rr in range(m):
            if rr==c: continue
            f=M[rr][c]/M[c][c]
            for cc in range(m): M[rr][cc]-=f*M[c][cc]
            V[rr]-=f*V[c]
    s=[V[i]/M[i][i] for i in range(m)]
    return 3*s[0]*s[0]/(2*math.pi**2), s[1]
c0=mock(lambda n:n)          # chi_0, order-5
f0=mock(lambda n:n*n)        # F_0,   order-7
print("control: chi_0 first terms", c0[:12], " (Gukov-Jagadale eq (33): sum q^n/(q^{n+1})_n)")
print("control: F_0   first terms", f0[:14], " (their eq (54); GM eq (175))")
for nm,s,tgt,lbl in (("chi_0  Sigma(2,3,5)",c0,0.2,"1/5"),("F_0    Sigma(2,3,7)",f0,1/7,"1/7")):
    c,B=fit3(s,L//2,L)
    print("   %-20s fitted c_eff = %.7f   target %s = %.7f   ratio %.5f   B=%+.4f"%(nm,c,lbl,tgt,c/tgt,B))
