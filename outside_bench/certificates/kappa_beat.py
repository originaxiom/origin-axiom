#!/usr/bin/env python3
"""MEMO-41 CELL: WHERE THE TWO CONSERVED THINGS MEET — the beat reflects the
first integral, and every symmetric function of it is the field's own 3.

The atlas holds exactly ONE forced recurrence: the first integral
kappa = tr[a,b] (the Suto invariant, conserved by the trace map — K001/K007,
234 probes).  This lane's arc exhibited one conserved involution: the beat.
THE QUESTION OF THE DIVE: what does the beat do to kappa?

Computed exactly over Q(q), q^2 = q - 1, on the banked chi=+1 lift:
  1. kappa = tr[A,B] = tr(A B A^-1 B^-1), directly AND via the Fricke identity
     kappa = x^2 + y^2 + z^2 - xyz - 2 with (x,y,z) = (tr A, tr B, tr AB)
     — the two routes must agree (cross-check).
  2. the beat's action: beta(X) = W conj(X) W^-1 is antiholomorphic and
     trace-preserving up to Galois, so kappa(beta) = gal(kappa) — verified by
     direct matrix computation, not by the argument.
  3. the arithmetic of the meeting point:
       kappa + gal(kappa)  (the trace of the first integral)
       kappa * gal(kappa)  (the norm of the first integral)
       the minimal polynomial of kappa over Q and its discriminant.
PREREGISTERED (from the hand derivation, to be confirmed or refuted by the
run): kappa = 1 + q; trace = 3; norm = 3; minimal polynomial X^2 - 3X + 3
with discriminant -3 = d_K — i.e. THE BEAT REFLECTS THE FIRST INTEGRAL AND
EVERY BEAT-INVARIANT FUNCTION OF IT IS BUILT FROM THE FIELD'S OWN 3
(= |d_K| = the conductor of chi_-3 = the ramified prime).
"""
from fractions import Fraction as F

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
d={'a':A,'A':inv2(A),'b':B,'B':inv2(B)}
def word(w):
    M=[[ONE,ZERO],[ZERO,ONE]]
    for ch in w: M=mmul(M,d[ch])
    return M
assert word('abABaBAbaB')==[[ONE,ZERO],[ZERO,ONE]]   # the chi=+1 lift

# 1. kappa two ways
comm=word('abAB')
kappa=tr(comm)
x=tr(A); y=tr(B); z=tr(mmul(A,B))
fricke=fadd(fadd(fadd(fmul(x,x),fmul(y,y)),fmul(z,z)), fneg(fadd(fmul(fmul(x,y),z),(F(2),F(0)))))
print(f"kappa = tr[A,B] (direct)      = {kappa}   (as x + y*q)")
print(f"kappa via Fricke x^2+y^2+z^2-xyz-2 = {fricke}   with (x,y,z) = ({x},{y},{z})")
assert kappa==fricke
assert kappa==(F(1),F(1))
print("=> kappa = 1 + q  EXACTLY (preregistration confirmed)")

# 2. the beat's action on kappa — computed, not argued
W=[[ONE,Q],[ZERO,ONE]]; Wi=[[ONE,fneg(Q)],[ZERO,ONE]]
def beta(X): return mmul(W,mmul(mgal(X),Wi))
bA=beta(A); bB=beta(B)
comm_b=mmul(mmul(bA,bB),mmul(inv2(bA),inv2(bB)))
kb=tr(comm_b)
print(f"kappa(beta(a),beta(b)) = {kb}")
assert kb==gal(kappa) and kb!=kappa
print("=> THE BEAT REFLECTS THE FIRST INTEGRAL: kappa -> gal(kappa), not fixed")

# 3. the meeting point
trace_k=fadd(kappa,gal(kappa))
norm_k=fmul(kappa,gal(kappa))
print(f"kappa + gal(kappa) = {trace_k}   (the trace)")
print(f"kappa * gal(kappa) = {norm_k}   (the norm)")
assert trace_k==(F(3),F(0)) and norm_k==(F(3),F(0))
# minimal polynomial: X^2 - (tr)X + (norm) = X^2 - 3X + 3; discriminant 9 - 12 = -3
disc=9-12
print(f"minimal polynomial of kappa over Q: X^2 - 3X + 3;  discriminant = {disc} = d_K")
# and kappa is a unit times the ramified prime? N(kappa)=3 => (kappa) is THE prime above 3
print("N(kappa) = 3: the first integral GENERATES the ramified prime of Q(sqrt-3)")

# bonus exactness: the beat swaps the two Fricke surfaces through the trace triple
c_level=fadd(kappa,(F(2),F(0)))
print(f"Fricke level c = kappa + 2 = {c_level}; beat image = {gal(c_level)}  (Galois-conjugate surface)")

print("""
THE MEETING POINT, EXACT: the dynamics lane's one forced conservation (kappa,
the Suto first integral) and the structure lane's one conserved involution
(the beat) are not independent — the beat REFLECTS kappa into its Galois
conjugate, and the beat-invariant content of the first integral is exactly
  trace 3, norm 3, minimal polynomial X^2 - 3X + 3, discriminant -3:
every symmetric function of kappa is built from the field's own 3 — the
discriminant, the conductor of chi_-3, the ramified prime, which the ideal
(kappa) itself generates.  The two conserved things meet, and their meeting
point is the arithmetic of Q(sqrt-3) in its purest coin.""")
