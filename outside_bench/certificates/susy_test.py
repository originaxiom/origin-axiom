#!/usr/bin/env python3
"""MEMO-71 CELL: THE SUSY QUESTION MADE FALSIFIABLE — does the carrier admit a
supercharge?  Three precise definitions, each decided exactly.  (D5 of the
MSSM-debt programme.)

A supermultiplet structure on Psi = C^2 (x) 27 needs an ODD operator Q (odd
with respect to a fermion grading) whose square is the available
"translation" — on the carrier the only banked translation-shaped operator
is the MERIDIAN rho_Psi(a) (the tick; the beat's own square, memo 46).
The natural fermion grading is the lock C_Psi (matter = its +1 sector,
named four independent ways).  Three equivariance choices, in decreasing
strength:

  DEFINITION A (pi1-equivariant supercharge): Q linear, Q C_Psi = -C_Psi Q,
    Q rho(g) = rho(g) Q for g in {a,b}, Q^2 = rho_Psi(a).
  DEFINITION B (gauge-equivariant supercharge): Q linear, Q commutes with
    the internal e6 action I_2 (x) rho27(x) for all 12 Chevalley
    generators, Q^2 = rho_Psi(a).
  DEFINITION C (the semilinear candidate): the record's one operator with
    square = meridian is the beat beta_Psi.  Is it a supercharge?

PREREGISTERED (each an exact computation or an arithmetic from in-run-derived
decompositions with the one CITED step labeled):
  FACT A: NO Definition-A supercharge exists — dim of the odd pi1-commutant
    is ZERO.  Route: an odd Q maps the locked sector to the unlocked sector
    equivariantly; as modules of the holonomy closure (= diagonal SL2,
    CITED-standard as in memo 48) the locked sector has content
    6 spin1 + 6 spin0 and the unlocked 15 spin1/2 (DERIVED in-run from the
    banked Jordan data, re-verified here); the contents are DISJOINT, so by
    Schur (CITED) every equivariant map between them is zero.  The
    arithmetic (content multisets, disjointness) is asserted.
  FACT B: NO Definition-B supercharge exists — computed WITHOUT Schur:
    (i) the 27's weight spaces are 1-dimensional and its weight graph under
    the 12 generators is CONNECTED (verified in-run), so any operator
    commuting with the Cartan and the generators is scalar on the 27;
    (ii) hence the e6-commutant on Psi is exactly {M (x) I_27 : M in gl2}
    (each 27x27 block of Q is an intertwiner 27->27 = scalar, from (i));
    (iii) (M (x) I)^2 = M^2 (x) I can never equal A_2 (x) A_27 because
    A_27 != I (off-diagonal entries exist — exhibited): assert.
  FACT C: the beat is NOT a supercharge: it is semilinear (not linear,
    banked memo 46 + the codex OA-C1090 correction), and it COMMUTES with
    the lock (memo 50 FACT D, re-verified here) — it is EVEN, not odd.
    The one square-root of the tick the object supplies is a mirror, not a
    supercharge.
VERDICT (two-outcome, landed negative in all three senses): the carrier's
kinematics does not support a supermultiplet structure under any natural
equivariance.  OWNER-DIRECTIVE NOTE: supersymmetry is NOT observed
structure, so this negative contradicts no observation — it aligns with
the empirical absence of superpartners; what it prices is the "M" in
MSSM: the object's NMSSM-shaped skeleton is a coupling structure, not a
supersymmetric one, as far as the carrier can say.  4d field-theoretic
SUSY with genuine spacetime translations lives behind Gates 2/3 and is
not touched by this cell.
"""
from fractions import Fraction as F
from collections import Counter
SCR=__import__('os').path.dirname(__import__('os').path.abspath(__file__))+""
src=open(SCR+"/twisted_double.py").read()
cut=src.index("# ---------------- stage 4")
exec(src[:cut])

r0=ROOTS[0]
hA=[F(0)]*DIM
for k in range(N): hA[k]=F(r0[k])
Hint=rho27_Q(hA)
wt=[int(Hint[a][a]) for a in range(27)]

# FACT A: closure-module contents of the two lock sectors (derived in-run)
lockP=[(i,a) for i in range(2) for a in range(27) if (1+wt[a])%2==0]
lockM=[(i,a) for i in range(2) for a in range(27) if (1+wt[a])%2!=0]
assert len(lockP)==24 and len(lockM)==30
def content(sector):
    wts=Counter()
    for (i,a) in sector:
        s_=1 if i==0 else -1
        wts[s_+wt[a]]+=1
    dec={}
    w=dict(wts)
    while any(v>0 for v in w.values()):
        top=max(k for k,v in w.items() if v>0); m=w[top]
        dec[F(top,2)]=dec.get(F(top,2),0)+m
        k=top
        while k>=-top:
            w[k]=w.get(k,0)-m; k-=2
    return dec
decP=content(lockP); decM=content(lockM)
print(f"FACT A: locked content {dict((str(k),v) for k,v in decP.items())}, unlocked {dict((str(k),v) for k,v in decM.items())}")
assert decP=={F(1):6, F(0):6} and decM=={F(1,2):15}
assert set(decP)&set(decM)==set()
print("   contents DISJOINT => (Schur, CITED; closure = diagonal SL2, CITED as memo 48)")
print("   every pi1-equivariant map locked <-> unlocked is ZERO:")
print("   dim(odd pi1-commutant) = 0 — NO Definition-A supercharge exists")

# FACT B: computed without Schur
gens=[]
for i in range(N):
    r=tuple(1 if k==i else 0 for k in range(N))
    gens.append(rho27_Q(evec(r)))
    gens.append(rho27_Q(evec(tuple(-x for x in r))))
# (i) weight graph connectivity (weights are distinct: verify)
Hs=[rho27_Q([F(1) if k==i else F(0) for k in range(DIM)]) for i in range(N)]
wt6=[tuple(Hs[i][a][a] for i in range(N)) for a in range(27)]
assert len(set(wt6))==27, "weights must be multiplicity-free"
adj={a:set() for a in range(27)}
for M in gens:
    for l in range(27):
        for c in range(27):
            if M[l][c]!=0: adj[c].add(l); adj[l].add(c)
seen={0}; stack=[0]
while stack:
    x=stack.pop()
    for y in adj[x]:
        if y not in seen: seen.add(y); stack.append(y)
print(f"FACT B(i): 27 weights multiplicity-free and weight graph connected: {len(seen)}/27")
assert len(seen)==27
print("   => any operator commuting with the Cartan and all 12 generators is a")
print("      SCALAR on the 27 (weight-diagonal by multiplicity-freeness, constant")
print("      along the connected generator graph) — commutant of the 27 = scalars,")
print("      PROVED in-run; hence the e6-commutant on Psi = {M (x) I : M in gl2}")
# (iii) meridian not of the form M^2 (x) I
E27=rho27_Q(evec(r0))
def matexp_nil(Mx):
    n=len(Mx)
    out=[[F(1) if i==j else F(0) for j in range(n)] for i in range(n)]
    term=[row[:] for row in out]; k=1
    while True:
        term=[[sum(term[i][l]*Mx[l][j] for l in range(n))/k for j in range(n)] for i in range(n)]
        if all(x==0 for row in term for x in row): break
        out=[[a+b for a,b in zip(r1,r2)] for r1,r2 in zip(out,term)]
        k+=1; assert k<40
    return out
A27q=matexp_nil(E27)
off=[(a,b) for a in range(27) for b in range(27) if a!=b and A27q[a][b]!=0]
print(f"FACT B(iii): A_27 has {len(off)} nonzero off-diagonal entries (e.g. {off[0]}) — A_27 != I,")
print("   so (M (x) I)^2 = M^2 (x) I can NEVER equal A_2 (x) A_27:")
print("   NO Definition-B supercharge exists")
assert off

# FACT C: the beat is even and semilinear (re-verify evenness)
Z=(F(0),F(0)); O=(F(1),F(0)); Qp=(F(0),F(1))
E27p=toF(E27)
U27=nilexp(E27p,QQ)
W2=[[O,Qp],[Z,O]]
cP=[(1 if (1+wt[a])%2==0 else -1) for i in range(2) for a in range(27)]
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
BtP=kronF(W2,U27)
even=all(BtP[i][j]==Z or cP[i]==cP[j] for i in range(54) for j in range(54))
print(f"FACT C: the beat commutes with the lock (is EVEN): {even}; and it is")
print("   Galois-SEMILINEAR (banked, memo 46 + OA-C1090): the object's one")
print("   square-root of the tick is a mirror, not a supercharge")
assert even

print("""
THE SUSY NO-GO (kinematic): no odd operator squaring to the meridian exists
on the carrier under pi1-equivariance (content-disjointness, Schur) or
gauge-equivariance (commutant = gl2 (x) I, proved in-run, cannot square to
the tick); and the record's own square-root of the tick — the beat — is
even and semilinear.  The "M" in MSSM is unsupported by the object's
kinematics: the NMSSM-shaped skeleton is a coupling structure, not a
supersymmetric one.  This contradicts no observation (superpartners are
not observed); 4d field SUSY with true translations is behind Gates 2/3
and untouched.  Gate 5 untouched."""
)
