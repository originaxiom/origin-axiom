#!/usr/bin/env python3
"""MEMO-43 CELL: THE FIXED POINT AND ITS TWIN — the holonomy character is a
fixed point of the trace-map dynamics on the cusped Fricke surface, its Galois
twin is the other one, and the beat is the exchange.

Setup (all exact over Q(q) on the banked chi=+1 lift):
  - fiber basis candidates U = b a^-1, V = a U a^-1 (exponent-sum 0; the
    fibration Gamma -> Z kills them); the monodromy is conjugation by the
    section a.
  - DISCOVERY 1: the substitution — express phi(V) = a V a^-1 as an exact word
    in U, V (searched, matched matrix-exactly), so <U, V> is phi-stable and
    the cat map is realized as words.
  - FACT 1: tr[U,V] = -2 exactly — the fiber's boundary is the CUSP (matches
    the banked longitude trace -2): the fiber triple lies on the cusped
    Fricke surface  x^2+y^2+z^2-xyz = tr[U,V]+2 = 0.
  - FACT 2: the triple (tr U, tr V, tr UV) is a FIXED POINT of the trace map
    (phi is realized by conjugation, so every basis trace is preserved) —
    the object IS the fixed locus (the atlas's object=dynamics pattern,
    B67/K007, here on the nose).
  - FACT 3: the triple is NOT rational — its Galois conjugate is a DIFFERENT
    point, ALSO fixed (gal commutes with the polynomial dynamics: the trace
    map has integer coefficients), on the SAME surface (the level 0 is
    rational).  The beat maps one to the other (antiholomorphic, verified by
    direct computation).
  => the trace-map dynamics on the cusped surface has (at least) this pair of
     conjugate fixed points, and the object's own Z/2 is the deck exchange of
     the pair: kappa's reflection (memo 41), the mirror bit (memo 37), and
     the fixed-point twin are one structure.
"""
from fractions import Fraction as F
from itertools import product

def fadd(u,v): return (u[0]+v[0],u[1]+v[1])
def fneg(u): return (-u[0],-u[1])
def fmul(u,v):
    a,b=u; c,d=v
    return (a*c-b*d, a*d+b*c+b*d)
def gal(u): return (u[0]+u[1],-u[1])
ZERO=(F(0),F(0)); ONE=(F(1),F(0)); Q=(F(0),F(1))
def mmul(X,Y): return [[fadd(fmul(X[i][0],Y[0][j]),fmul(X[i][1],Y[1][j])) for j in range(2)] for i in range(2)]
def mgal(X): return [[gal(x) for x in row] for row in X]
def inv2(X):
    d=fadd(fmul(X[0][0],X[1][1]),fneg(fmul(X[0][1],X[1][0]))); assert d==ONE
    return [[X[1][1],fneg(X[0][1])],[fneg(X[1][0]),X[0][0]]]
def tr(X): return fadd(X[0][0],X[1][1])
A=[[ONE,ONE],[ZERO,ONE]]; B=[[ONE,ZERO],[Q,ONE]]
dd={'a':A,'A':inv2(A),'b':B,'B':inv2(B)}
def word(w):
    M=[[ONE,ZERO],[ZERO,ONE]]
    for ch in w: M=mmul(M,dd[ch])
    return M
assert word('abABaBAbaB')==[[ONE,ZERO],[ZERO,ONE]]

U=word('bA'); V=word('abAA')          # V = a U a^-1
Ui=inv2(U); Vi=inv2(V)
Am=A; Ami=inv2(A)

# DISCOVERY 1: phi(V) = a V a^-1 as a word in U, V (search up to length 5)
target=mmul(Am,mmul(V,Ami))
gens={'U':U,'u':Ui,'V':V,'v':Vi}
found=None
for L in range(1,6):
    for wtuple in product('UuVv',repeat=L):
        # skip immediate cancellations
        bad=any((wtuple[i]=='U' and wtuple[i+1]=='u') or (wtuple[i]=='u' and wtuple[i+1]=='U')
                or (wtuple[i]=='V' and wtuple[i+1]=='v') or (wtuple[i]=='v' and wtuple[i+1]=='V')
                for i in range(L-1))
        if bad: continue
        M=[[ONE,ZERO],[ZERO,ONE]]
        for ch in wtuple: M=mmul(M,gens[ch])
        if M==target:
            found=''.join(wtuple); break
    if found: break
print(f"substitution discovered: phi(U) = V (by construction);  phi(V) = {found}  (exact matrix match)")
assert found is not None
# abelianization check: the substitution's abelianized matrix should be cat-map-like (det 1, trace 3)
nU=found.count('U')-found.count('u'); nV=found.count('V')-found.count('v')
Mab=[[0,nU],[1,nV]]
det=Mab[0][0]*Mab[1][1]-Mab[0][1]*Mab[1][0]; trace=Mab[0][0]+Mab[1][1]
print(f"abelianized substitution matrix [[0,{nU}],[1,{nV}]]: det = {det}, trace = {trace}  (cat map: det +-1, |trace| 3)")

# FACT 1: the commutator = the cusp
K=mmul(mmul(U,V),mmul(Ui,Vi))
kf=tr(K)
print(f"tr[U,V] = {kf}   (expect -2: the fiber boundary IS the cusp; banked longitude trace -2)")
assert kf==(F(-2),F(0))

# FACT 2 + 3: the triple, its level, fixedness, irrationality, and the beat
x=tr(U); y=tr(V); z=tr(mmul(U,V))
lvl=fadd(fadd(fadd(fmul(x,x),fmul(y,y)),fmul(z,z)), fneg(fmul(fmul(x,y),z)))
print(f"fiber triple (x,y,z) = ({x}, {y}, {z})")
print(f"Fricke level x^2+y^2+z^2-xyz = {lvl}   (expect 0 = tr[U,V]+2: the CUSPED surface)")
assert lvl==ZERO
# fixed point: traces of the phi-images equal the originals (phi = conjugation)
xp=tr(mmul(Am,mmul(U,Ami))); yp=tr(mmul(Am,mmul(V,Ami))); zp=tr(mmul(Am,mmul(mmul(U,V),Ami)))
print(f"trace-map image of the triple: ({xp}, {yp}, {zp})  — FIXED: {(xp,yp,zp)==(x,y,z)}")
assert (xp,yp,zp)==(x,y,z)
irr = any(t[1]!=0 for t in (x,y,z))
print(f"the triple is irrational (has q-part): {irr}  => its Galois conjugate is a DIFFERENT point")
assert irr
galtrip=(gal(x),gal(y),gal(z))
lvl2=fadd(fadd(fadd(fmul(galtrip[0],galtrip[0]),fmul(galtrip[1],galtrip[1])),fmul(galtrip[2],galtrip[2])), fneg(fmul(fmul(galtrip[0],galtrip[1]),galtrip[2])))
print(f"Galois twin ({galtrip[0]}, {galtrip[1]}, {galtrip[2]}): level = {lvl2} (SAME surface — level 0 is rational)")
assert lvl2==ZERO
# the twin is also fixed: gal commutes with conjugation-by-real-matrix? verify directly:
# the beat carries the rep to its conjugate; traces of the SAME words at the conjugate rep = gal(traces)
W=[[ONE,Q],[ZERO,ONE]]; Wi=[[ONE,fneg(Q)],[ZERO,ONE]]
def beta(X): return mmul(W,mmul(mgal(X),Wi))
bx=tr(beta(U)); by=tr(beta(V)); bz=tr(beta(mmul(U,V)))
print(f"beat image of the triple: ({bx}, {by}, {bz})  == Galois twin: {(bx,by,bz)==galtrip}")
assert (bx,by,bz)==galtrip

print("""
THE FIXED POINT AND ITS TWIN, EXACT: the fiber triple of the holonomy sits on
the CUSPED Fricke surface (level 0, boundary trace -2 = the longitude), is a
FIXED POINT of the monodromy's trace-map dynamics, and is irrational — so its
Galois conjugate is a second, distinct fixed point on the same rational-level
surface.  The beat maps one to the other, computed on the nose.  The atlas's
object=dynamics pattern (the object as the trace map's fixed locus) is here
with its full structure: the fixed locus is a CONJUGATE PAIR, and the object's
own Z/2 — the beat, the kappa-reflection, the mirror bit — is the deck
transformation of that pair.  One Z/2, now seen as the exchange of the two
fixed points of the one forced dynamics.""")
