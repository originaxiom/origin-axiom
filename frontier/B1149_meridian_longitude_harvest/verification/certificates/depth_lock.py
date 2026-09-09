#!/usr/bin/env python3
"""MEMO-50 CELL: ODD STEPS ARE MATTER — the meridian's Jordan filtration on the
carrier, and the lock as clock-depth parity.

Memo 49 proved the meridian is EXACTLY 3-step nilpotent on Psi = C^2 (x) 27.
Memo 46 proved the lift-independent (locked) sector of Psi is exactly the 24
fermion-shaped slots.  This cell computes the meridian's full Jordan structure
and asks whether the two facts are one fact.

PREREGISTERED (two-outcome; every claim an assert):
  FACT A (the filtration): N = rho_Psi(a) - I has Jordan type
      6 J3 (+) 15 J2 (+) 6 J1
    equivalently rank N = 27, rank N^2 = 6, N^3 = 0; graded layer dims
    ker N : ker N^2/ker N : ker N^3/ker N^2 = 27 : 21 : 6.
    (Predicted mechanism: 27 under the bridge sl2 is 6 doublets + 15
    singlets, so A27 is 6 J2 + 15 J1; J2 (x) J2 = J3 (+) J1 and
    J2 (x) J1 = J2.)
  FACT B (the lock is pi1-covariant): C_Psi = diag((-1)^(1+wt)) commutes
    with BOTH generators rho_Psi(a) and rho_Psi(b) exactly (e and f shift
    the internal h-weight by 2, preserving parity; -I_2 is central).
  FACT C (the lock IS depth parity): N restricted to the locked (+1) sector
    (dim 24) has Jordan type 6 J3 (+) 6 J1 — ONLY ODD chain lengths;
    N restricted to the unlocked (-1) sector (dim 30) has type 15 J2 —
    ONLY EVEN chain lengths.  So the memo-46 lock bit equals the parity of
    the meridian-clock chain length: matter slots are exactly the slots
    whose internal time runs an odd number of steps, and full depth 3 is
    reached ONLY in the matter sector.
  FACT D (beat compatibility): the beat operator BtP = W (x) U27 commutes
    with C_Psi exactly (so the antiunitary beta_Psi = BtP o conj preserves
    both lock sectors), and beta_Psi preserves every filtration layer
    ker N^k (immediate from memo 46's beta rho(a) beta^-1 = rho(a), re-run
    here as a direct check on ker-layer stability via commutation).

If any assert fails, the failing branch is the result: file the error, pin
the mechanism, correct, rerun.
"""
import itertools
from fractions import Fraction as F
from collections import Counter
SCR=__import__('os').path.dirname(__import__('os').path.abspath(__file__))+""
src=open(SCR+"/twisted_double.py").read()
cut=src.index("# ---------------- stage 4")
exec(src[:cut])

# ---- rational carrier matrices (as in memo 49's trace_three.py)
r0=ROOTS[0]
E27=rho27_Q(evec(r0))
F27=rho27_Q([-x for x in evec(tuple(-t for t in r0))])
def matexp_nil_scaled(M,s):
    n=len(M)
    out=[[F(1) if i==j else F(0) for j in range(n)] for i in range(n)]
    term=[row[:] for row in out]
    k=1
    while True:
        term=[[sum(term[i][l]*M[l][j] for l in range(n))*s/k for j in range(n)] for i in range(n)]
        if all(x==0 for row in term for x in row): break
        out=[[a+b for a,b in zip(r1,r2)] for r1,r2 in zip(out,term)]
        k+=1
        assert k<40
    return out
A27q=matexp_nil_scaled(E27,F(1))
hA=[F(0)]*DIM
for k in range(N): hA[k]=F(r0[k])
Hint=rho27_Q(hA)
wt=[int(Hint[a][a]) for a in range(27)]
assert dict(Counter(wt))=={1:6,0:15,-1:6}

A2q=[[F(1),F(1)],[F(0),F(1)]]
def kronQ(X,Y):
    nx=len(X); ny=len(Y)
    out=[[F(0)]*(nx*ny) for _ in range(nx*ny)]
    for i in range(nx):
        for j in range(nx):
            if X[i][j]==0: continue
            for a in range(ny):
                for b in range(ny):
                    if Y[a][b]==0: continue
                    out[i*ny+a][j*ny+b]=X[i][j]*Y[a][b]
    return out
def mmQ(X,Y):
    n=len(X); m=len(Y[0])
    out=[[F(0)]*m for _ in range(n)]
    for i in range(n):
        for k in range(len(Y)):
            if X[i][k]==0: continue
            x=X[i][k]
            for j in range(m):
                if Y[k][j]!=0: out[i][j]+=x*Y[k][j]
    return out
def rankQ(M):
    A=[row[:] for row in M]
    if not A: return 0
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

APsi=kronQ(A2q,A27q)
Nm=[[APsi[i][j]-(F(1) if i==j else F(0)) for j in range(54)] for i in range(54)]
N2=mmQ(Nm,Nm); N3=mmQ(N2,Nm)
assert all(x==0 for row in N3 for x in row)
r1=rankQ(Nm); r2=rankQ(N2)
b_ge1=54-r1; b_ge2=r1-r2; b_ge3=r2
n3=b_ge3; n2=b_ge2-b_ge3; n1=b_ge1-b_ge2
print(f"FACT A: rank N = {r1}, rank N^2 = {r2}, N^3 = 0")
print(f"  Jordan type of the meridian on Psi: {n3} J3 (+) {n2} J2 (+) {n1} J1")
print(f"  graded layers ker N : ker N^2/ker N : Psi/ker N^2 = {54-r1} : {r1-r2} : {r2}")
assert (r1,r2)==(27,6) and (n3,n2,n1)==(6,15,6)

# FACT B: C_Psi commutes with the full pi1 image
c=[(1 if (1+wt[a])%2==0 else -1) for a in range(27)]
cP=[c[a] for i in range(2) for a in range(27)]   # (-1 from -I_2)*(−1)^wt = (−1)^(1+wt): spin factor is scalar
assert sum(1 for x in cP if x==1)==24
# exact pair-field check of commutation for BOTH generators:
Z=(F(0),F(0)); O=(F(1),F(0)); Qp=(F(0),F(1))
E27p=toF(E27); F27p=toF(F27)
A27f=nilexp(E27p,ONE); B27f=nilexp(F27p,QQ)
A2f=[[O,O],[Z,O]]; B2f=[[O,Z],[Qp,O]]
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
APsif=kronF(A2f,A27f); BPsif=kronF(B2f,B27f)
def commutes_diag(M):
    return all(M[i][j]==Z or cP[i]==cP[j] for i in range(54) for j in range(54))
okA=commutes_diag(APsif); okB=commutes_diag(BPsif)
print(f"FACT B: C_Psi commutes with rho_Psi(a): {okA}; with rho_Psi(b): {okB}")
assert okA and okB

# FACT C: restricted Jordan types on the two lock sectors
lockP=[i for i in range(54) if cP[i]==1]; lockM=[i for i in range(54) if cP[i]==-1]
assert len(lockP)==24 and len(lockM)==30
# N preserves each sector (Fact B over Q: same support), restrict:
def restrict(M,idx):
    return [[M[i][j] for j in idx] for i in idx]
NP=restrict(Nm,lockP); NM=restrict(Nm,lockM)
# safety: no leakage between sectors
assert all(Nm[i][j]==0 for i in lockP for j in lockM)
assert all(Nm[i][j]==0 for i in lockM for j in lockP)
NP2=mmQ(NP,NP); NM2=mmQ(NM,NM)
rp1=rankQ(NP); rp2=rankQ(NP2); rm1=rankQ(NM); rm2=rankQ(NM2)
p_ge1=24-rp1; p_ge2=rp1-rp2; p_ge3=rp2
pn3=p_ge3; pn2=p_ge2-p_ge3; pn1=p_ge1-p_ge2
m_ge1=30-rm1; m_ge2=rm1-rm2; m_ge3=rm2
mn3=m_ge3; mn2=m_ge2-m_ge3; mn1=m_ge1-m_ge2
print(f"FACT C: LOCKED sector (dim 24): {pn3} J3 (+) {pn2} J2 (+) {pn1} J1")
print(f"        UNLOCKED sector (dim 30): {mn3} J3 (+) {mn2} J2 (+) {mn1} J1")
assert (pn3,pn2,pn1)==(6,0,6) and (mn3,mn2,mn1)==(0,15,0)
print("  => the locked sector carries ONLY ODD chains (3,1); the unlocked ONLY")
print("     EVEN chains (2): the memo-46 lock bit IS the parity of the meridian")
print("     clock's chain length, and depth 3 is reached ONLY in matter.")

# FACT D: the beat respects both structures
W2f=[[O,Qp],[Z,O]]; U27f=nilexp(E27p,QQ)
BtP=kronF(W2f,U27f)
okC=commutes_diag(BtP)
print(f"FACT D: BtP = W (x) U27 commutes with C_Psi: {okC}  (C real diagonal =>")
print("        beta_Psi = BtP o conj preserves both lock sectors)")
assert okC
# filtration stability of the beat: beta rho(a) beta^-1 = rho(a) (memo 46) means
# beta maps ker N^k to ker (gal N)^k = ker N^k' where N' = rho(a)-I again; direct check:
def mgal(X): return [[(x[0]+x[1],-x[1]) for x in row] for row in X]
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
W2i=[[O,fneg(Qp)],[Z,O]]; U27i=nilexp(E27p,fneg(QQ))
BtPi=kronF(W2i,U27i)
lhs=mmF(BtP,mmF(mgal(APsif),BtPi))
okBeat = lhs==APsif
print(f"        beta_Psi rho(a) beta_Psi^-1 = rho(a) re-verified: {okBeat}")
print("        => every filtration layer ker N^k is beat-stable (dims 27/48/54)")
assert okBeat

print(f"""
ODD STEPS ARE MATTER: the meridian's clock on the carrier has Jordan type
6 J3 (+) 15 J2 (+) 6 J1 (graded 27:21:6); the lock commutes with the whole
pi1 image and with the beat; and the two lock sectors split the clock by
CHAIN-LENGTH PARITY — odd chains (3 and 1) are exactly the 24 fermion-shaped
locked slots, even chains (2) exactly the 30 unlocked ones.  Memo 46's lock
and memo 49's three steps are one fact: a slot is lift-independent precisely
when its internal time under the meridian is odd, and the full three steps
happen only in matter.  Structure only; Gate 5 untouched.""")
