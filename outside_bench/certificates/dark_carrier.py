#!/usr/bin/env python3
"""MEMO-57 CELL: THE FAMILY ESCALATOR — the object's internal clock walks the
family ladder (1 -> 16 -> 10, charge -3 per rung), the dark ledger extended to
the carrier, and the class content of what the cusp holds still.

Memo 56 found the bridge root carries family charge q(r0) = -3.  Since the
meridian's internal rungs are exactly E27 steps, the family classes CANNOT be
stable under the object's clock — each tick shifts family charge by -3.  This
cell computes the exact consequences on the 27 and on the carrier Psi.

PREREGISTERED (two-outcome; anchors and structural claims as asserts):
  FACT 1 (the escalator): every nonzero entry of E27 connects a wt(-1) basis
    state to a wt(+1) basis state whose family classes are EXACTLY
    (16 -> 10) or (1 -> 16)  (charge -3: 1 -> -2 and 4 -> 1; the other
    combinations are charge-forbidden).  Chain census by exact rank:
    rank(E27 from 16-bottoms) = 5, rank(E27 from the singlet-bottom) = 1
    => of the 6 internal doublets, FIVE are (16-bottom, 10-top) and ONE is
    (singlet-bottom, 16-top): the classic dark matter candidate is the
    BOTTOM of a chain whose top is SM-shaped.
  FACT 2 (the carrier's dark ledger): slot counts by class x lock on
    Psi = C^2 (x) 27: class sizes 32/20/2; locked (matter) slots per class
    = 12/10/2 (twice memo 56's odd-weight counts).  The singlet's two
    carrier slots are BOTH locked.
  FACT 3 (what the boundary holds, by class — measured): the 12-dim joint
    cusp-fixed space (memo 51) decomposed against the family classes:
    d_proj(c) = dim of its projection to class c, d_int(c) = dim of its
    intersection with class c — both by exact pair-field rank.  Preregister
    only the containment re-check (Fix inside the locked sector, dim 12);
    the class table is the measured outcome.
  FACT 4 (corollary, cited-banked + re-stated): in the E8 family channel
    (memo 53) every internal triple realizes all 6 family assignments, so
    combined with memo 56's typing the portal is FAMILY-DEMOCRATIC: each
    class role (the two 16s, the 10; the two 10s, the 1) visits every
    family.  No new computation claimed; the banked 45 x 6 count carries it.
"""
from fractions import Fraction as F
from collections import Counter
SCR=__import__('os').path.dirname(__import__('os').path.abspath(__file__))+""
src=open(SCR+"/twisted_double.py").read()
cut=src.index("# ---------------- stage 4")
exec(src[:cut])

# family classes (as in dark_ledger.py)
q3={a: int(3*ipr(weights[a], omega1)) for a in range(27)}
cnt=Counter(q3.values())
c16=next(v for v,m in cnt.items() if m==16); c10=next(v for v,m in cnt.items() if m==10)
c1 =next(v for v,m in cnt.items() if m==1)
cls={a:('16' if q3[a]==c16 else '10' if q3[a]==c10 else '1') for a in range(27)}

# bridge data
r0=ROOTS[0]
E27=rho27_Q(evec(r0))
hA=[F(0)]*DIM
for k in range(N): hA[k]=F(r0[k])
Hint=rho27_Q(hA)
wt=[int(Hint[a][a]) for a in range(27)]

# FACT 1: the escalator
pairs=Counter()
for t in range(27):
    for b in range(27):
        if E27[t][b]!=0:
            assert wt[b]==-1 and wt[t]==1
            pairs[(cls[b],cls[t])]+=1
            assert q3[t]==q3[b]-3
print("FACT 1: E27 support pairs by (bottom class -> top class):", dict(pairs))
assert set(pairs)<= {('16','10'),('1','16')}
def rankQ(M):
    A=[row[:] for row in M]
    if not A or not A[0]: return 0
    rows=len(A); cols=len(A[0]); r=0
    for c in range(cols):
        p=next((i for i in range(r,rows) if A[i][c]!=0),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        pv=A[r][c]; A[r]=[x/pv for x in A[r]]
        for i in range(rows):
            if i!=r and A[i][c]!=0:
                fq=A[i][c]; A[i]=[x-fq*y for x,y in zip(A[i],A[r])]
        r+=1
    return r
bots16=[b for b in range(27) if wt[b]==-1 and cls[b]=='16']
bots1 =[b for b in range(27) if wt[b]==-1 and cls[b]=='1']
r16=rankQ([[E27[t][b] for b in bots16] for t in range(27)])
r1 =rankQ([[E27[t][b] for b in bots1 ] for t in range(27)])
print(f"   chain census: rank from 16-bottoms = {r16} (expect 5), from singlet-bottom = {r1} (expect 1)")
assert r16==5 and r1==1
print("   => the clock walks the family ladder: 1 -> 16 -> 10, charge -3 per rung;")
print("      the singlet is the BOTTOM of a chain whose top is SM-shaped")

# FACT 2: the carrier's dark ledger
clsP=[cls[a] for i in range(2) for a in range(27)]
lockP=[(1 if (1+wt[a])%2==0 else -1) for i in range(2) for a in range(27)]
sizes=Counter(clsP)
locked=Counter(c for c,l in zip(clsP,lockP) if l==1)
print(f"FACT 2: carrier slots by class: {dict(sizes)}; locked (matter) per class: {dict(locked)}")
assert dict(sizes)=={'16':32,'10':20,'1':2} and dict(locked)=={'16':12,'10':10,'1':2}
print("   => BOTH of the singlet's carrier slots are in the locked matter sector")

# FACT 3: the cusp-fixed space by class (exact pair-field ranks; memo 51's system)
Z=(F(0),F(0)); O=(F(1),F(0)); Qp=(F(0),F(1))
E27p=toF(E27)
F27p=toF(rho27_Q([-x for x in evec(tuple(-t for t in r0))]))
A27=nilexp(E27p,ONE); A27i=nilexp(E27p,fneg(ONE))
B27=nilexp(F27p,QQ);  B27i=nilexp(F27p,fneg(QQ))
A2=[[O,O],[Z,O]]; B2=[[O,Z],[Qp,O]]
def m2(X,Y): return [[fadd(fmul(X[i][0],Y[0][j]),fmul(X[i][1],Y[1][j])) for j in range(2)] for i in range(2)]
def inv2x2(X):
    d=fsub(fmul(X[0][0],X[1][1]),fmul(X[0][1],X[1][0])); assert d==O
    return [[X[1][1],fneg(X[0][1])],[fneg(X[1][0]),X[0][0]]]
def mmF(X,Y):
    n=len(X)
    out=[[Z]*n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            x=X[i][k]
            if x==Z: continue
            for j in range(n):
                if Y[k][j]!=Z: out[i][j]=fadd(out[i][j],fmul(x,Y[k][j]))
    return out
def meye(n): return [[O if i==j else Z for j in range(n)] for i in range(n)]
def kronF(X,Y):
    nx=len(X); ny=len(Y)
    out=[[Z]*(nx*ny) for _ in range(nx*ny)]
    for i in range(nx):
        for j in range(nx):
            if X[i][j]==Z: continue
            for a in range(ny):
                for b in range(ny):
                    if Y[a][b]==Z: continue
                    out[i*ny+a][j*ny+b]=fmul(X[i][j],Y[a][b])
    return out
d2={'a':A2,'A':inv2x2(A2),'b':B2,'B':inv2x2(B2)}
d27={'a':A27,'A':A27i,'b':B27,'B':B27i}
def word2(w):
    M=[[O,Z],[Z,O]]
    for ch in w: M=m2(M,d2[ch])
    return M
def word27(w):
    M=meye(27)
    for ch in w: M=mmF(M,d27[ch])
    return M
LAM='bABaaBAb'
LPsi=kronF(word2(LAM),word27(LAM))
APsi=kronF(A2,A27)
NA=[[fsub(APsi[i][j], O if i==j else Z) for j in range(54)] for i in range(54)]
NL=[[fsub(LPsi[i][j], O if i==j else Z) for j in range(54)] for i in range(54)]
def rref(M):
    A=[row[:] for row in M]
    rows=len(A); cols=len(A[0]) if A else 0; r=0; piv=[]
    for c in range(cols):
        p=next((i for i in range(r,rows) if A[i][c]!=Z),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        pv=finv(A[r][c]); A[r]=[fmul(pv,x) for x in A[r]]
        for i in range(rows):
            if i!=r and A[i][c]!=Z:
                fq=A[i][c]; A[i]=[fsub(x,fmul(fq,y)) for x,y in zip(A[i],A[r])]
        piv.append(c); r+=1
    return A,piv,r
_,piv,rk=rref(NA+NL)
free=[c for c in range(54) if c not in piv]
Ared,pivl,_=rref(NA+NL)
basis=[]
for fc in free:
    v=[Z]*54; v[fc]=O
    for i,c in enumerate(pivl): v[c]=fneg(Ared[i][fc])
    basis.append(v)
assert len(basis)==54-rk
print(f"FACT 3: joint cusp-fixed space dim = {len(basis)} (expect 12)")
assert len(basis)==12
# containment in locked (re-check)
lockidx=[i for i in range(54) if lockP[i]==1]
assert all(all(v[i]==Z for i in range(54) if i not in lockidx) for v in basis)
# class decomposition
def rankF_rows(rows):
    if not rows: return 0
    _,_,r=rref(rows)
    return r
for c in ('16','10','1'):
    idx=[i for i in range(54) if clsP[i]==c]
    other=[i for i in range(54) if clsP[i]!=c]
    dproj=rankF_rows([[v[i] for i in idx] for v in basis])
    dint=len(basis)-rankF_rows([[v[i] for i in other] for v in basis])
    print(f"   class {c:>3}: d_proj = {dproj}, d_int = {dint}")

# FACT 4: corollary (banked memo 53: 45 internal triples x ALL 6 family assignments)
print("FACT 4 (corollary of banked memos 53+56): the E8 family channel realizes")
print("   every family assignment of every triple, so the portal is family-")
print("   democratic: the 10-role and the 1-role visit each family.")

print("""
THE FAMILY ESCALATOR: the object's internal clock does not respect the
family frame — each rung shifts family charge by -3, so the six internal
doublets straddle classes: five carry 16 -> 10 and one carries 1 -> 16.
The dark matter candidate (the singlet) is the bottom of a chain whose top
is SM-shaped, both its carrier slots are locked matter slots, and the class
content of the cusp-fixed space is tabulated above.  Kinematics only; the
D5 frame fence of memo 56 applies throughout; Gate 5 untouched.""")
