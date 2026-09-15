#!/usr/bin/env python3
"""ITEM 5b --- J(m004) = 1, exactly. Riley's pair. This one stands."""
import cmath
c=cmath.exp(1j*cmath.pi/3)
A=[[1,1],[0,1]]; B=[[1,0],[c,1]]
mul=lambda X,Y: [[sum(X[i][k]*Y[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def inv(X):
    d=X[0][0]*X[1][1]-X[0][1]*X[1][0]
    return [[X[1][1]/d,-X[0][1]/d],[-X[1][0]/d,X[0][0]/d]]
C=mul(mul(A,B),mul(inv(A),inv(B))); k=C[0][0]+C[1][1]
print(f"  A parabolic: tr^2 A - 4 = {A[0][0]+A[1][1]}^2 - 4 = 0")
print(f"  tr[A,B] - 2 = {k-2:.12f}  = c^2 = e^(2 i pi/3) = omega")
print(f"  |tr[A,B] - 2| = {abs(k-2):.15f}")
print(f"  => J(A,B) = 0 + 1 = 1  EXACTLY")
print("  Callahan Cor 2.4: m004 is the UNIQUE orientable hyperbolic 3-manifold with J=1.")
