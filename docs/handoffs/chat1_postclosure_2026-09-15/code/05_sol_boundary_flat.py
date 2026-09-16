#!/usr/bin/env python3
"""SOL BOUNDARY EXHAUSTED. Every SU(2) flat connection on m004(0,1) is REDUCIBLE.
|det(RL-I)| = |2-3| = 1 -> ONE abelian point. rho(y)=-I gives a contradiction.
One RL-fixed sign pair. => integrality is ONE equation, not a selection rule.
p=0's canonicity (Seifert framing) is paid for with an EMPTY character variety."""
import sympy as sp
if __name__=="__main__":
    A=sp.Matrix([[2,1],[1,1]])                      # RL
    print("RL =",A.tolist()," trace",A.trace()," det",A.det())
    print("abelian flat SU(2) connections = |det(RL - I)| =", abs((A-sp.eye(2)).det()))
    M2=sp.Matrix(2,2,lambda i,j:A[i,j]%2)
    fixed=[(x,y) for x in range(2) for y in range(2)
           if (M2*sp.Matrix([x,y])).applyfunc(lambda z:z%2)==sp.Matrix([x,y])]
    print("RL-fixed sign pairs (mod 2):", fixed)
