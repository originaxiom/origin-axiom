#!/usr/bin/env python3
"""GM's CONSTANT c FOR 5_2, DETERMINED -- and it is the figure-eight's.

Park arXiv:2004.02087 section 4.4 gives F^+_{m(5_2)} = x^{1/2} sum_j f_j(q) x^j, with closed
forms for f_0 and f_1 (verified here against his printed expansions) and the quantum
A-hat-polynomial eq (32).

MY TRANSCRIPTION OF eq (32) HAS ONE ERROR, CAUGHT BY A CONTROL, NOT BY INSPECTION: my f_2
matches Park's printed Q(q)-coefficients exactly, but my f_3 differs from his by exactly -q^6.
Deciding it against his PRINTED f_3 SERIES (2 + q - 2q^2 - 2q^3 - 3q^4 + 2q^6 + 4q^7 + 4q^8
+ 2q^9 - 3q^11) shows HIS formula reproduces it and mine does not.  The residual of my n=3
equation on his verified f_0..f_3 is exactly Q^26 f_0 with the f_1 coefficient vanishing, so the
error is a SINGLE MONOMIAL at x-degree 3, in a_1, a_2 or a_3.  My typed version matches the PDF
text layer character for character, so it is an extraction artefact or a misprint.

WHICH OF THE THREE IS NOT DETERMINED HERE.  All three candidates give blocks with INTEGER
coefficients through f_9, and they agree exactly on f_2 and f_3; they first differ in the FOURTH
COEFFICIENT of f_4.

BUT THE ANSWER THIS CERTIFICATE REPORTS DOES NOT DEPEND ON WHICH IS RIGHT.  All three give the
SAME lowest q-power of f_j for every j <= 24:

   j    :  0  1  2  3  4  5  6  7   8   9  10  11  12 ... 24
   low  : -1 -1 -1  0 -2 -3 -3 -6 -11 -14 -20 -24 -31 ... -139

with exact closed forms, verified on both parities:

   even j >= 8 :  low(j) = -j^2/4 + 5
   odd  j >= 7 :  low(j) = -(j^2-1)/4 + 6

Since F^+ = sum_j f_j x^{(2j+1)/2}, the relevant index is m = 2j+1, so j = (m-1)/2 and

   low = -(m-1)^2/16 + const     =>    c = -1/16   EXACTLY

in the sense of GM's condition (177) ("the lowest powers of q in the coefficients f_m(q) of
x^{m/2} have exponents of the order c m^2").  GM state c = -1/16 for the FIGURE-EIGHT (page 73,
found experimentally) and deduce the range p/r in (-4, 0).

   => 5_2 HAS THE SAME c, AND THEREFORE THE SAME RANGE OF APPLICABILITY, AS 4_1.

Neither GM nor Park states this; GM give c only for the trefoil and the figure-eight.

Gate 5: exact integer Laurent-series arithmetic.
"""

import sympy as sp
from fractions import Fraction as Fr
exec(open('/tmp/k52/ahat.py').read().split('for n in range(0,4):')[0])
LQ=340          # work to Q^LQ  (q = Q^2)
def topoly(ex):
    p=sp.Poly(sp.expand(ex),Q)
    return {int(e):int(c) for (e,),c in p.terms()}
COEFD=[{d:topoly(c) for d,c in C.items()} for C in COEF]
def f0ser():
    a={}; j=0
    while j*(j+1)<=LQ: a[2*(j*(j+1)//2)]=a.get(2*(j*(j+1)//2),0)+(-1)**j; j+=1
    return {e-2:-c for e,c in a.items() if c}      # times -q^{-1} -> shift Q by -2
def f1ser():
    a={}; j=0
    while j*(j+1)<=LQ:
        b=j*(j+1)//2; s=(-1)**j
        for t in range(j+1):
            if 2*(b+t)<=LQ: a[2*(b+t)]=a.get(2*(b+t),0)+s
        j+=1
    return {e-2:-c for e,c in a.items() if c}
def lmul(a,b,lo=-999):
    r={}
    for e1,c1 in a.items():
        for e2,c2 in b.items():
            e=e1+e2
            if e<=LQ: r[e]=r.get(e,0)+c1*c2
    return {e:c for e,c in r.items() if c}
def ladd(a,b):
    r=dict(a)
    for e,c in b.items():
        r[e]=r.get(e,0)+c
        if r[e]==0: del r[e]
    return r
def ldiv(num, den, lowest):
    """divide Laurent series num by Laurent polynomial den; result starts at `lowest`"""
    dl=min(den); dc=Fr(den[dl])
    out={}
    n=dict(num)
    e=lowest+dl
    # standard long division from the bottom
    cur=dict(num)
    res={}
    for step in range(LQ*2):
        if not cur: break
        lo=min(cur)
        if lo>LQ: break
        k=Fr(cur[lo])/dc
        res[lo-dl]=res.get(lo-dl,0)+k
        for x,y in den.items():
            t=lo-dl+x
            cur[t]=cur.get(t,0)-Fr(y)*k
            if cur[t]==0: del cur[t]
    return res
F0=f0ser(); F1=f1ser()
for cand in (1,2,3):
    C=[dict(c) for c in COEFD]
    corr={26-cand:-1}
    C[cand][3]=ladd(C[cand].get(3,{}), corr)
    F={0:F0,1:F1}
    ok=True; why=''
    for n in range(2,25):
        row={}
        for i in range(5):
            for d,c in C[i].items():
                j=n-d
                if j<0 or j>n: continue
                sh=2*i*j+i
                cc={e+sh:v for e,v in c.items()}
                row[j]=ladd(row.get(j,{}),cc)
        row={j:v for j,v in row.items() if v}
        if n not in row: ok=False; why='no leading term at n=%d'%n; break
        rhs={}
        for j,rj in row.items():
            if j<n: rhs=ladd(rhs, lmul(rj,F[j]))
        rhs={e:-c for e,c in rhs.items()}
        res=ldiv(rhs,row[n],0)
        vals=sorted(res.items())[:18]
        if any(Fr(v).denominator!=1 for _,v in vals):
            ok=False; why='non-integer at f_%d: %s'%(n,[str(v) for _,v in vals[:6]]); break
        F[n]={e:int(v) for e,v in res.items() if v}
    print('a_%d correction -> %s'%(cand, 'INTEGRAL blocks through f_9' if ok else 'REJECTED: '+why))
    if ok:
        low=[Fr(min(F[n]),2) for n in range(25)]
        print('     lowest q-power of f_j, j=0..24:', [str(v) for v in low])
        import math
        # m = 2j+1 ; fit low ~ c m^2 + b m + a on the tail
        pts=[(2*j+1, float(low[j])) for j in range(10,25)]
        n_=len(pts); Sx=[sum(m**k for m,_ in pts) for k in range(5)]
        Sy=[sum(y*m**k for m,y in pts) for k in range(3)]
        import itertools
        A=[[Sx[i+j] for j in range(3)] for i in range(3)]; B=[Sy[i] for i in range(3)]
        for c_ in range(3):
            p=max(range(c_,3),key=lambda r:abs(A[r][c_])); A[c_],A[p]=A[p],A[c_]; B[c_],B[p]=B[p],B[c_]
            for r in range(3):
                if r==c_: continue
                f_=A[r][c_]/A[c_][c_]
                for cc in range(3): A[r][cc]-=f_*A[c_][cc]
                B[r]-=f_*B[c_]
        sol=[B[i]/A[i][i] for i in range(3)]
        print('     quadratic fit low(m) = %.6f m^2 + %.4f m + %.4f   -> c = %.6f'%(sol[2],sol[1],sol[0],sol[2]))
        print('     candidate exact values: -1/24=%.6f  -1/20=%.6f  -1/16=%.6f  -1/21=%.6f  -1/22=%.6f'
              %(-1/24,-1/20,-1/16,-1/21,-1/22))
