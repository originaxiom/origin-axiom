#!/usr/bin/env python3
"""A3: THE BEAT ON THE CUSP LATTICE — Omega_cusp = diag(1,-1) exactly.

The beat's action has been banked on the fiber torus (FIRST_BEAT: H1(monodromy)
= [[2,1],[1,1]], trace 3, infinite order) and on holonomy/algebra/matter — but
never as an integer matrix on the CUSP torus's own H1(dM;Z) = Z<mu> + Z<lambda>.
Compute it exactly over Q(q), q^2 = q - 1:

    mu = A = [[1,1],[0,1]]            (meridian)
    lambda = b A B a a B A b          (the banked longitude word, trace -2 lift)
    beta(x) = W conj(x) W^-1,  W = [[1,q],[0,1]]  (the beat, memo 16/28)

Banked already: beta(mu) = +mu (memo 28, fact 2).  Here: beta(lambda) exactly.
No search: direct exact comparison against lambda^{+1}, lambda^{-1}, and their
negatives — the peripheral subgroup is Z^2 = <mu, lambda>, so these plus mu-
translates exhaust the candidates of matching trace; commutation and trace
checks close the identification.  PREREGISTERED: beta(lambda) = +lambda^{-1}
=> Omega_cusp = diag(1,-1): order 2, det -1, meridian fixed, longitude
reflected — one beat, two lattices, two different orders (2 vs infinity).
"""
from fractions import Fraction as F

def fadd(u,v): return (u[0]+v[0],u[1]+v[1])
def fneg(u): return (-u[0],-u[1])
def fmul(u,v):
    a,b=u; c,d=v
    return (a*c-b*d, a*d+b*c+b*d)     # q^2 = q-1
def gal(u): return (u[0]+u[1],-u[1])  # q -> 1-q = qbar (complex conjugation)
ZERO=(F(0),F(0)); ONE=(F(1),F(0)); Q=(F(0),F(1))

def mmul(X,Y):
    return [[fadd(fmul(X[i][0],Y[0][j]),fmul(X[i][1],Y[1][j])) for j in range(2)] for i in range(2)]
def mgal(X): return [[gal(x) for x in row] for row in X]
def mneg(X): return [[fneg(x) for x in row] for row in X]
def det(X): return fadd(fmul(X[0][0],X[1][1]),fneg(fmul(X[0][1],X[1][0])))
def inv(X):
    d=det(X); assert d==ONE, "det != 1"
    return [[X[1][1],fneg(X[0][1])],[fneg(X[1][0]),X[0][0]]]

A=[[ONE,ONE],[ZERO,ONE]]; B=[[ONE,ZERO],[Q,ONE]]
Ai=inv(A); Bi=inv(B)
d={'a':A,'A':Ai,'b':B,'B':Bi}
def word(w):
    M=[[ONE,ZERO],[ZERO,ONE]]
    for ch in w: M=mmul(M,d[ch])
    return M

# relator sanity (the chi=+1 lift)
R=word('a'+'bABa'+'B'+'AbaB')
assert R==[[ONE,ZERO],[ZERO,ONE]]
print("relator R(A,B) = +I: True (the chi=+1 lift)")

lam=word('bABaaBAb')
tr=fadd(lam[0][0],lam[1][1])
print(f"longitude lambda = bABaaBAb: trace = {tr}  (banked: -2 on this lift)")
assert tr==(F(-2),F(0))
comm = mmul(A,lam)==mmul(lam,A)
print("peripheral check: [mu, lambda] = 1:", comm); assert comm

W=[[ONE,Q],[ZERO,ONE]]; Wi=[[ONE,fneg(Q)],[ZERO,ONE]]
def beta(X): return mmul(W,mmul(mgal(X),Wi))

bmu=beta(A)
print("beta(mu) = +mu:", bmu==A); assert bmu==A

blam=beta(lam)
lami=inv(lam)
cands={'+lambda':lam,'-lambda':mneg(lam),'+lambda^-1':lami,'-lambda^-1':mneg(lami)}
hit=[k for k,V in cands.items() if blam==V]
print("beta(lambda) among {+-lambda^{+-1}}:", hit)
assert hit==['+lambda^-1']

print("\n=> Omega_cusp = [[1,0],[0,-1]] on H1(dM;Z) = Z<mu> (+) Z<lambda>:")
print("   meridian FIXED (sign +, the spin-selected lift's sign on the nose),")
print("   longitude REFLECTED (again sign +: chi(lambda)=+1, consistent with")
print("   lambda in the commutator subgroup - H1(M)=Z kills it).")
print("   order 2, det -1 - the beat is a REFLECTION of the cusp lattice,")
print("   against the fiber tick's [[2,1],[1,1]] (trace 3, INFINITE order):")
print("   ONE BEAT, TWO LATTICES, TWO ORDERS.  VII.1's mirror law (meridian")
print("   fixed, longitude inverted) is re-derived from the beat itself, with")
print("   the SL(2) signs exact - no sign anomaly anywhere on the cusp.")
