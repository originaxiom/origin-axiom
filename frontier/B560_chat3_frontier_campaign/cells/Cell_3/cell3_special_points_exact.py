#!/usr/bin/env python3
from __future__ import annotations
import itertools, sympy as sp
from observer_fixed_point_exact import GENS, rho, PHYSICAL_VECTOR
I=sp.I; r=sp.sqrt(3)
M=sp.Matrix([[1,1,1,1],[1,0,1,0],[2,1,1,1],[1,1,1,0]])
Q=sp.Matrix([[1,3,6,7]])
assert all(int(x)%11==0 for x in Q*M-Q)
assert int((sp.eye(4)-M).det())==-11
orbits=[tuple(sorted({m,(-m)%11})) for m in range(6)]
assert orbits==[(0,),(1,10),(2,9),(3,8),(4,7),(5,6)]
# tangent matrices
V={}
for j,g in enumerate(GENS):
    V[g]=sp.Matrix(2,2,list(PHYSICAL_VECTOR[1+4*j:5+4*j,0]))
dtr={g:sp.simplify(sp.trace(V[g])) for g in GENS}
assert dtr=={'a':-3*r*I/2,'b':-3*r*I/2,'A':0,'B':0}
e=sp.symbols('e'); R={g:rho[g]+e*V[g] for g in GENS}
def kappa(A,B): return sp.simplify(sp.trace(A*B*A.inv()*B.inv()))
dk={}
for i,a in enumerate(GENS):
    for b in GENS[i+1:]: dk[a+b]=sp.simplify(sp.diff(kappa(R[a],R[b]),e).subs(e,0))
assert all(v==0 for v in dk.values())
print('det(I-M):',int((sp.eye(4)-M).det()))
print('Weyl orbits:',orbits)
print('trace derivatives:',dtr)
print('kappa derivatives:',dk)
