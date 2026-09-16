#!/usr/bin/env python3
"""Own count of SL(2,Z) and GL(2,Z) classes of primitive indefinite binary quadratic forms of discriminant D = m^2 + 4, m = 1..13
(B8148: the banked GL(2,Z) table (1,1,1,1,1,2,1,1,2,2,1) for m = 1..11 and 3/3 at m = 12; fc R42: 3 SL / 2 GL at m = 12).
Method: cycles of reduced forms under Gauss's reduction operator; proper (SL2) classes = cycles; GL2 classes = cycles modulo (a,b,c) -> (a,-b,c)."""
from math import gcd, isqrt
def reduced_forms(D):
    s=D**0.5; out=[]
    bmax=isqrt(D)
    for b in range(1, bmax+1):            # 0 < b < sqrt(D)  (b = isqrt(D) admissible when D is not a square)
        if b*b>=D: break
        if (D-b*b)%4: continue
        ac=(b*b-D)//4                     # a*c = (b^2 - D)/4 < 0
        for a in range(1, int(s)+2):
            for sa in (1,-1):
                A=sa*a
                if ac%A: continue
                C=ac//A
                if not (s-b < 2*abs(A) < s+b): continue
                if gcd(gcd(abs(A),b),abs(C))!=1: continue
                out.append((A,b,C))
    return sorted(set(out))
def rho(f,D):
    a,b,c=f; s=D**0.5
    # next form (c, b', a') with b' = -b mod 2c, sqrt(D)-2|c| < b' < sqrt(D)
    m=2*abs(c); b2=(-b)%m
    while b2<=s-m: b2+=m
    while b2>=s: b2-=m
    a2=(b2*b2-D)//(4*c)
    return (c,b2,a2)
def classes(D):
    R=reduced_forms(D); Rset=set(R); seen=set(); cycles=[]
    for f in R:
        if f in seen: continue
        cyc=[]; g=f
        while g not in seen:
            seen.add(g); cyc.append(g); g=rho(g,D); assert g in Rset, (D,f,g)
        cycles.append(frozenset(cyc))
    # GL2: identify a cycle with the cycle containing (a,-b,c)'s reduced representative: use (a,b,c) ~ (-a,b,-c)? The improper class of (a,b,c) is that of (a,-b,c) ~ (c,b,a) via (x,y)->(y,x): (c,b,a) is reduced iff (a,b,c) is.
    idx={}
    for i,cyc in enumerate(cycles):
        for f in cyc: idx[f]=i
    gl=set()
    for i,cyc in enumerate(cycles):
        f=next(iter(cyc)); j=idx[(f[2],f[1],f[0])]
        gl.add(frozenset({i,j}))
    return len(cycles), len(gl)
tab=[]
for m in range(1,14):
    D=m*m+4; sl,gl=classes(D); tab.append((m,D,sl,gl)); print(f'm={m:2d} D={D:4d}  SL(2,Z) classes {sl}  GL(2,Z) classes {gl}')
print('GL table m=1..11:', [t[3] for t in tab[:11]], ' banked (1,1,1,1,1,2,1,1,2,2,1)')
print('m=12:', tab[11])
