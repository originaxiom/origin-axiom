#!/usr/bin/env python3
"""MEMO-51 CELL: THE LONGITUDE IS THE LOCK — the boundary curve's action on the
carrier has multiplicative Jordan decomposition with semisimple part EXACTLY
the lock operator C_Psi.

Memo 50 upgraded C_Psi to a pi1- and beat-invariant grading (matter = +1).
This cell asks where in the group that grading operator LIVES.  Answer: it is
the semisimple part of the LONGITUDE — the boundary curve lambda = bABaaBAb
whose trace is -2 (the -unipotent conjugacy class).  Under the internal A1
bridge, -I acts on the 27 (weights {+-1,0}) as (-1)^wt = C_27, so the
longitude's image should be C times a unipotent; on the carrier the spinor
factor contributes the -I_2, completing C_Psi = (-I_2)(x)C_27.

PREREGISTERED (two-outcome; every claim an assert):
  FACT 0 (anchor): tr rho_2(lambda) = -2 exactly (the banked lift).
  FACT 1: C_27 commutes with the ENTIRE internal image (A27, B27 entrywise
    weight-parity check) — the 27-level analogue of memo 50's FACT B.
  FACT 2: rho_27(lambda) * C_27 is UNIPOTENT with nilpotency degree 2
    (the internal A1 sends parabolics to 2-step unipotents on the 27).
  FACT 3: on the carrier, C_Psi * rho_Psi(lambda) is UNIPOTENT with
    nilpotency degree 3 (two nontrivial 2-step factors, depth 2+2-1).
  FACT 4: therefore, by uniqueness of the multiplicative Jordan
    decomposition (C_Psi semisimple of order 2, commuting with the
    unipotent part — commutation asserted directly),
        rho_Psi(lambda) = C_Psi . U_lambda,   U_lambda unipotent:
    THE SEMISIMPLE PART OF THE LONGITUDE ON THE CARRIER IS THE LOCK.
    The matter grading is not an external comparison operator: it is the
    eigenvalue grading of the boundary curve itself.
  FACT 5 (measured, not preregistered to a value): the joint cusp-fixed
    space { v : rho_Psi(mu) v = v and rho_Psi(lambda) v = v } — computed by
    exact pair-field nullspace; asserted only to be nonzero and contained
    in the LOCKED sector (on the unlocked sector the longitude's semisimple
    eigenvalue is -1, so no fixed vectors can live there).

If any assert fails, the failing branch is the result: file, pin, correct.
"""
from fractions import Fraction as F
from collections import Counter
SCR=__import__('os').path.dirname(__import__('os').path.abspath(__file__))+""
src=open(SCR+"/twisted_double.py").read()
cut=src.index("# ---------------- stage 4")
exec(src[:cut])

LAM='bABaaBAb'

# ---- pair field scalars
Z=(F(0),F(0)); O=(F(1),F(0)); Qp=(F(0),F(1))

# ---- SL2 holonomy, FACT 0
A2=[[O,O],[Z,O]]; B2=[[O,Z],[Qp,O]]
def m2(X,Y): return [[fadd(fmul(X[i][0],Y[0][j]),fmul(X[i][1],Y[1][j])) for j in range(2)] for i in range(2)]
def inv2x2(X):
    d=fsub(fmul(X[0][0],X[1][1]),fmul(X[0][1],X[1][0])); assert d==O
    return [[X[1][1],fneg(X[0][1])],[fneg(X[1][0]),X[0][0]]]
d2={'a':A2,'A':inv2x2(A2),'b':B2,'B':inv2x2(B2)}
def word2(w):
    M=[[O,Z],[Z,O]]
    for ch in w: M=m2(M,d2[ch])
    return M
L2=word2(LAM)
trL=fadd(L2[0][0],L2[1][1])
print(f"FACT 0: tr rho_2(lambda) = {trL[0]} + {trL[1]} q")
assert trL==(F(-2),F(0))

# ---- internal bridge on the 27
r0=ROOTS[0]
E27p=toF(rho27_Q(evec(r0)))
F27p=toF(rho27_Q([-x for x in evec(tuple(-t for t in r0))]))
A27=nilexp(E27p,ONE);  A27i=nilexp(E27p,fneg(ONE))
B27=nilexp(F27p,QQ);   B27i=nilexp(F27p,fneg(QQ))
hA=[F(0)]*DIM
for k in range(N): hA[k]=F(r0[k])
Hint=rho27_Q(hA)
wt=[int(Hint[a][a]) for a in range(27)]
assert dict(Counter(wt))=={1:6,0:15,-1:6}
c27=[(1 if w%2==0 else -1) for w in wt]   # C_27 = (-1)^wt

# FACT 1: C_27 commutes with the whole internal image
def commutes_c27(M):
    return all(M[i][j]==Z or c27[i]==c27[j] for i in range(27) for j in range(27))
ok1=all(commutes_c27(M) for M in (A27,B27,A27i,B27i))
print(f"FACT 1: C_27 commutes with A27, B27 (and inverses): {ok1}")
assert ok1

def mmF(X,Y):
    n=len(X)
    out=[[Z]*n for _ in range(n)]
    for i in range(n):
        Xi=X[i]
        for k in range(n):
            x=Xi[k]
            if x==Z: continue
            Yk=Y[k]; Oi=out[i]
            for j in range(n):
                if Yk[j]!=Z: Oi[j]=fadd(Oi[j],fmul(x,Yk[j]))
    return out
def meye(n): return [[O if i==j else Z for j in range(n)] for i in range(n)]
d27={'a':A27,'A':A27i,'b':B27,'B':B27i}
def word27(w):
    M=meye(27)
    for ch in w: M=mmF(M,d27[ch])
    return M
L27=word27(LAM)

# FACT 2: C_27 * L27 unipotent of degree 2
CL=[[ (c27[i]*L27[i][j][0], c27[i]*L27[i][j][1]) for j in range(27)] for i in range(27)]
Nl=[[fsub(CL[i][j], O if i==j else Z) for j in range(27)] for i in range(27)]
Nl2=mmF(Nl,Nl)
nz1=any(x!=Z for row in Nl for x in row)
nz2=any(x!=Z for row in Nl2 for x in row)
print(f"FACT 2: (C_27 . rho_27(lambda) - I) != 0: {nz1}; squared = 0: {not nz2}")
assert nz1 and not nz2
print("  => rho_27(lambda) = C_27 . (2-step unipotent): the internal longitude is")
print("     the internal lock times a unipotent drift")

# ---- carrier
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
LPsi=kronF(L2,L27)
APsi=kronF(A2,A27)
cP=[-c27[a] for i in range(2) for a in range(27)]   # C_Psi = (-I_2)(x)C_27 = (-1)^(1+wt)
assert sum(1 for x in cP if x==1)==24

# commutation of C_Psi with rho_Psi(lambda) (needed for Jordan uniqueness)
okc=all(LPsi[i][j]==Z or cP[i]==cP[j] for i in range(54) for j in range(54))
print(f"FACT 3 pre: C_Psi commutes with rho_Psi(lambda): {okc}")
assert okc

# FACT 3: C_Psi * LPsi unipotent of degree 3
CLP=[[ (cP[i]*LPsi[i][j][0], cP[i]*LPsi[i][j][1]) for j in range(54)] for i in range(54)]
NL=[[fsub(CLP[i][j], O if i==j else Z) for j in range(54)] for i in range(54)]
NL2=mmF(NL,NL); NL3=mmF(NL2,NL)
z2=any(x!=Z for row in NL2 for x in row)
z3=any(x!=Z for row in NL3 for x in row)
print(f"FACT 3: (C_Psi . rho_Psi(lambda) - I)^2 != 0: {z2}; cubed = 0: {not z3}")
assert z2 and not z3
print("FACT 4: by uniqueness of the multiplicative Jordan decomposition,")
print("        rho_Psi(lambda) = C_Psi . U_lambda with U_lambda 3-step unipotent:")
print("        THE SEMISIMPLE PART OF THE LONGITUDE ON THE CARRIER IS THE LOCK.")

# FACT 5: joint cusp-fixed space, exact pair-field nullspace
def rankF(M):
    A=[row[:] for row in M]
    if not A: return 0
    rows=len(A); cols=len(A[0]); r=0
    for ccol in range(cols):
        p=next((i for i in range(r,rows) if A[i][ccol]!=Z),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        pv=finv(A[r][ccol]); A[r]=[fmul(pv,x) for x in A[r]]
        for i in range(rows):
            if i!=r and A[i][ccol]!=Z:
                fq=A[i][ccol]; A[i]=[fsub(x,fmul(fq,y)) for x,y in zip(A[i],A[r])]
        r+=1
    return r
NA=[[fsub(APsi[i][j], O if i==j else Z) for j in range(54)] for i in range(54)]
NLam=[[fsub(LPsi[i][j], O if i==j else Z) for j in range(54)] for i in range(54)]
stacked=NA+NLam
rk=rankF(stacked)
dfix=54-rk
print(f"FACT 5: joint cusp-fixed space dim {{v : mu v = v, lambda v = v}} = {dfix}")
assert dfix>0
# containment in the locked sector: on unlocked, lambda's ss eigenvalue is -1,
# so a fixed vector must vanish there.  Verify by rank: add the unlocked
# coordinate projections as equations and check the dimension is unchanged.
unlocked=[i for i in range(54) if cP[i]==-1]
proj=[[O if j==i else Z for j in range(54)] for i in unlocked]
rk2=rankF(stacked+proj)
print(f"        with 'vanishes on unlocked sector' imposed: dim = {54-rk2}")
assert 54-rk2==dfix
print("  => the whole cusp-fixed space of the carrier lives INSIDE matter")

print(f"""
THE LONGITUDE IS THE LOCK: the boundary curve acts on the carrier as
C_Psi . (3-step unipotent) — its semisimple part IS the lock operator whose
+1 sector is the 24 fermion-shaped slots (memo 46) and whose grading is the
clock-parity (memo 50).  The matter/non-matter distinction is not imposed on
the object: it is the eigenvalue grading of the boundary curve itself, with
the meridian supplying the clock and the longitude supplying the sign.  The
cusp's joint fixed space (dim {dfix}) lies entirely inside matter.  Structure
only; Gate 5 untouched.""")
