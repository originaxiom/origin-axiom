"""r4b_extraction.py — the algebraic hearing law, exact (chat-2, delivered
in-chat 2026-07-14 during their sandbox outage; dropped verbatim, path fixed).
Produces: L0 (blocks NOT dot-orthogonal), nilpotency orders (v4:5, v8:3),
L1 parity lemma ((v_m v0)^T v0 = 0 exactly), exact t-polynomial Im-coefficients
per word/slot (leading order t^2; witness -536481792000 at m=8/b2), and the
weld-only channel. Runtime ~14 min. For the R4 verdict map, the frozen 20-word
list was: a1,b1,a2,b2,a1b1,a2b2,a1b2,a2b1,a1a2,b1b2,a1b1a2b2,a2b2a1b1,
a1b2a2b1,a1b1A1B1,a1b2A1B2,a1a2b1b2,b1a2b2a1,a1b1a1,a1b1b2,a2b1b2 — extend
TESTW below to all of them for the full tables (item 4)."""
import os
import sys
from fractions import Fraction as Fr
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, '..', 'B575_bridge_obstruction',
                        'l51_obstruction.py')).read()
ns = {'__name__': 'l51mod'}; sys.argv = ['l51']
exec(compile(src, 'l51', 'exec'), ns)
K=ns['K']; mmul=ns['mmul']; madd=ns['madd']; mscale=ns['mscale']; meye=ns['meye']
bracket=ns['bracket']; mexp_nil=ns['mexp_nil']; nullspace=ns['nullspace']
A27=ns['A27']; B27=ns['B27']; A27i=ns['A27i']; B27i=ns['B27i']
e_pr=ns['e_pr']; f_pr=ns['f_pr']; h_pr=ns['h_pr']; BLOCKS=ns['BLOCKS']
K0=ns['K0']; K1=ns['K1']
kc=lambda x: K(x.a, -x.b)
def mconj(M): return [[kc(x) for x in r] for r in M]
def matvec(M,v): return [sum((M[i][j]*v[j] for j in range(27)
                        if not v[j].is_zero()),K0) for i in range(27)]
def dot(u,v): return sum((u[i]*v[i] for i in range(27)
                     if not(u[i].is_zero() or v[i].is_zero())),K0)
half=K(Fr(1,2))
Om=madd(madd(mmul(e_pr,f_pr),mmul(f_pr,e_pr)),mscale(half,mmul(h_pr,h_pr)))
v0=nullspace(Om)[0]
sym=all((Om[i][j]-Om[j][i]).is_zero() for i in range(27) for j in range(27))
print("L0 Omega dot-symmetric:", sym)                       # False
VM={m:BLOCKS[m][0] for m in (4,8)}
for m in (4,8):
    P=VM[m]; k=1
    while True:
        P=mmul(P,VM[m]); k+=1
        if all(all(x.is_zero() for x in r) for r in P): break
    print(f"ord(v_{m}) on 27:", k)                          # 5, 3
for m in (4,8):
    w1=matvec(VM[m],v0); c1=dot(w1,v0)
    print(f"L1 m={m}: (v_m v0)^T v0 =", "0" if c1.is_zero() else "NONZERO")
def build_letters(m,t):
    c=mexp_nil(mscale(K(t),VM[m])); ci=mexp_nil(mscale(K(-t),VM[m]))
    b2=mmul(mmul(c,mconj(B27)),ci); B2=mmul(mmul(c,mconj(B27i)),ci)
    return c,{'a':A27,'b':B27,'A':A27i,'B':B27i,'x':A27,'y':b2,'X':A27i,'Y':B2}
def wordmat(seq,LM):
    M=meye(27)
    for ch in seq: M=mmul(M,LM[ch])
    return M
TESTW=[('b2','y'),('a1b2','ay'),('a2b2','xy'),('a1b1a2b2','abxy'),
       ('a1b2A1B2','ayAY')]
def lagrange_coeffs(vals,pts):
    n=len(pts); coA=[Fr(0)]*n; coB=[Fr(0)]*n
    for i,(xi,vi) in enumerate(zip(pts,vals)):
        num=[Fr(1)]; den=Fr(1)
        for j,xj in enumerate(pts):
            if j==i: continue
            new=[Fr(0)]*(len(num)+1)
            for k in range(len(num)):
                new[k+1]+=num[k]; new[k]-=xj*num[k]
            num=new; den*=(xi-xj)
        for k in range(len(num)):
            coA[k]+=vi.a*num[k]/den; coB[k]+=vi.b*num[k]/den
    return coA,coB
for m,D in ((4,38),(8,22)):
    pts=[Fr(j) for j in range(D+1)]; cache={}
    for t in pts:
        c,LM=build_letters(m,t); cache[t]=(matvec(c,v0),LM)
    print(f"--- slot m={m} ---")
    for name,seq in TESTW:
        vals=[dot(cache[t][0],matvec(wordmat(seq,cache[t][1]),v0)) for t in pts]
        coA,coB=lagrange_coeffs(vals,pts)
        nz=[(k,coB[k]) for k in range(len(coB)) if coB[k]!=0]
        print(f"  {name}: Im orders {[k for k,_ in nz[:6]]}, "
              f"leading t^{nz[0][0]} coeff {nz[0][1]}" if nz else f"  {name}: Im=0")
for m in (4,8):
    c,LM=build_letters(m,Fr(1))
    val=dot(v0,matvec(wordmat('y',LM),v0))
    print(f"weld-only m={m} b2: {val.a} + ({val.b})·sqrt(-3)")
