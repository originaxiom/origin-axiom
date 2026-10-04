"""TIER 2 (fragile). J = mult by i maps k=su(2) onto p=i.su(2); Cartan metric is Hermitian.
FRAGILITY: shape is fixed only for Ad(K)-invariant Hermitian metrics. Physical Strominger
solutions may break Ad(K) and reintroduce shape moduli -- CHECK against their actual metrics."""
import numpy as np
s=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.array([[1,0],[0,-1]],complex)]
k=[1j*x/2 for x in s]; p=[x/2 for x in s]; B=lambda X,Y:8*np.real(np.trace(X@Y))
print("J(k) in p:", all(any(np.allclose(1j*X,c*Y) for Y in p for c in(1,-1)) for X in k))
print("Hermitian:", all(np.isclose(-B(X,X),B(1j*X,1j*X)) for X in k))
