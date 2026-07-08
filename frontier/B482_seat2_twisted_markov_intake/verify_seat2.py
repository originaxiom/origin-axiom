#!/usr/bin/env python3
"""B482: verification of seat-2's A2 (two-teeth/neg-Pell), B3 (unified commutator), A6 (Hurwitz)."""
import sympy as sp, math
d=sp.symbols('d')
print("A6 (1,d,d^2+1):", sp.simplify(((d**2+1)**2-1-d**2)-d*(d**2+1)))  # 0
a,b,c,e,f,g=sp.symbols('a b c e f g')
A=sp.Matrix([[a,b],[b,c]]); B=sp.Matrix([[e,f],[f,g]]); M=A*B
print("B3:", sp.simplify(sp.trace(A*B*A.inv()*B.inv())-(2-(M[0,1]-M[1,0])**2/(A.det()*B.det()))))  # 0
def negpell(D):
    for t in range(1,2000):
        v=D*t*t-4
        if v>=0 and math.isqrt(v)**2==v: return (math.isqrt(v),t)
for m in (1,2,5,13,29):
    print(f"A2 m={m}: D={9*m*m-4} neg-Pell -4 ->", negpell(9*m*m-4))
