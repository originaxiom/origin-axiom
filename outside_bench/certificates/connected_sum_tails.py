#!/usr/bin/env python3
"""THE OBJECT WITH c_eff(1/Phi) = 6 EXISTS, AND IT IS SIX FIGURE-EIGHTS -- on the colored
Jones side, computed here, no literature and no F_K required.

Memo 177 addendum 4 established, for the figure-eight, that the F_K block edge is the
RECIPROCAL of the colored Jones tail:  Phi_{4_1} = (q;q)_inf and the edge is 2 theta/(q;q)_inf
with c_eff = 1.  It proposed  c_edge(K) = c_eff(1/Phi_K)  as the mechanism, and observed that
tails are knot-by-knot, so the ceiling is too.  It then named connected sums as a route to 6
and, in the same section, recorded two arguments AGAINST that route.

This certificate settles the half of the question that can be settled offline.

  The normalised colored Jones is multiplicative under connected sum, so a connected sum of m
  figure-eights has J_n = J_n(4_1)^m.  Computing that from GM eq (166) and reading the stable
  head:

        tail( #^m 4_1 )  =  (q;q)_inf^m        for m = 1, 2, 3, 6, exactly,
                                               matched over the whole stable window,

  and the reciprocals have c_eff = m, measured on 30000 terms:

        m = 1 -> 0.999984      m = 2 -> 1.999966
        m = 3 -> 2.999940      m = 6 -> 5.999820.

  So on the colored Jones side the object with  c_eff(1/Phi) = 6  EXISTS, is explicit, and is
  the connected sum of six figure-eight knots.

WHAT IS STILL OPEN, AND THE HONEST PRIOR.  Whether Zhat sees it.  The mechanism
c_edge = c_eff(1/Phi_K) has exactly ONE data point (4_1), and memo 177 addendum 4 records two
computed arguments against the naive transfer: the product formula F_1 F_2 / U is not a formal
q-series (the cross term Xi(x)Xi(1/x) has coefficients that are sums of q-series with orders
unbounded below), and under a convolution rule the extreme edge of the connected sum would come
from a single endpoint term and reproduce Xi's own edge, leaving c_edge = 1.  The preregistered
cell therefore stands with prior OUTCOME B.

WHAT THIS IS NOT.  It is not a claim that c_eff = 6 is reachable for Zhat.  It is the
observation that the ONE ingredient that looked out of reach -- a tail whose reciprocal carries
six units of central charge -- is not out of reach at all, and costs nothing but a connected
sum.  That the multiplicity is six and the summand is the figure-eight is arithmetic:
c_eff(1/(q;q)_inf^m) = m, so any knot with tail (q;q)_inf would do.  Nothing here connects it to
c((E6)_1) = 6 beyond the number.

Gate 5: exact integer Laurent arithmetic in, one fit out.
"""
L=200
def J(n):
    total={0:1}; cur={0:1}
    for m in range(1,n):
        fac={n:1,-n:1}; fac[m]=fac.get(m,0)-1; fac[-m]=fac.get(-m,0)-1
        fac={k:v for k,v in fac.items() if v}
        nxt={}
        for e1,c1 in cur.items():
            for e2,c2 in fac.items(): nxt[e1+e2]=nxt.get(e1+e2,0)+c1*c2
        cur={k:v for k,v in nxt.items() if v}
        for k,v in cur.items(): total[k]=total.get(k,0)+v
    return {k:v for k,v in total.items() if v}
def head(d,N=24):
    lo=min(d); return [d.get(lo+i,0) for i in range(N)]
def prod(a,b):
    o={}
    for e1,c1 in a.items():
        for e2,c2 in b.items(): o[e1+e2]=o.get(e1+e2,0)+c1*c2
    return {k:v for k,v in o.items() if v}
qq=[0]*(L+1); qq[0]=1
for n in range(1,L+1):
    for i in range(L,n-1,-1): qq[i]-=qq[i-n]
def power(p,m):
    o=[0]*(L+1); o[0]=1
    for _ in range(m):
        n=[0]*(L+1)
        for i,x in enumerate(p):
            if x:
                for j,y in enumerate(o):
                    if y and i+j<=L: n[i+j]+=x*y
        o=n
    return o
print("tails of connected sums of figure-eights, from J_n(4_1)^m  (J is multiplicative)")
print("-"*74)
for m in (1,2,3,6):
    h1=None
    for n in (14,15):
        d=J(n)
        for _ in range(m-1): d=prod(d,J(n))
        if h1 is None: h1=head(d,26)
        else: h2=head(d,26)
    s=0
    while s<len(h1) and h1[s]==h2[s]: s+=1
    tgt=power(qq,m)[:s]
    ok = h2[:s]==tgt
    print(f"   m={m}:  stable window {s:>2}   head {h2[:min(s,12)]}")
    print(f"          (q;q)_inf^{m} {'':<{max(0,2-len(str(m)))}}  {tgt[:min(s,12)]}   MATCH: {ok}")
import math
def fit3(a,lo,hi):
    X=[];Y=[]
    for n in range(lo,hi+1):
        if n>1 and a[n]>0: X.append((math.sqrt(n),math.log(n),1.0)); Y.append(math.log(a[n]))
    mm=3; M=[[sum(X[i][p]*X[i][q] for i in range(len(X))) for q in range(mm)] for p in range(mm)]
    V=[sum(X[i][p]*Y[i] for i in range(len(X))) for p in range(mm)]
    for c in range(mm):
        piv=max(range(c,mm),key=lambda rr:abs(M[rr][c])); M[c],M[piv]=M[piv],M[c]; V[c],V[piv]=V[piv],V[c]
        for rr in range(mm):
            if rr==c: continue
            f=M[rr][c]/M[c][c]
            for cc in range(mm): M[rr][cc]-=f*M[c][cc]
            V[rr]-=f*V[c]
    s=[V[i]/M[i][i] for i in range(mm)]
    return 3*s[0]*s[0]/(2*math.pi**2)
BIG=30000
print("\n   c_eff of 1/(q;q)_inf^m, the reciprocal tails:")
qb=[0]*(BIG+1); qb[0]=1
for n in range(1,BIG+1):
    for i in range(BIG,n-1,-1): qb[i]-=qb[i-n]
for m in (1,2,3,6):
    inv=[0]*(BIG+1); inv[0]=1
    for _ in range(m):
        nw=[0]*(BIG+1)
        for i in range(BIG+1):
            if inv[i]:
                # multiply by 1/(q;q)_inf via partitions
                pass
        break
    # build 1/(q;q)^m directly: m colours of partitions
    inv=[0]*(BIG+1); inv[0]=1
    for col in range(m):
        for n in range(1,BIG+1):
            for i in range(n,BIG+1): inv[i]+=inv[i-n]
    print(f"      m={m}: c_eff = {fit3(inv,BIG//2,BIG):.6f}   (target {m})")
