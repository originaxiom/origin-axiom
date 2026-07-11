#!/usr/bin/env sage-python
"""B528 — compute the DGG gauge group of T[4_1] from SnapPy's Neumann-Zagier datum.
SL(2): gauge = U(1)^{N-c}, integer NZ data => abelian CS-matter. The 'N-1' pattern = cusp Cartan K-1."""
import snappy
from sage.all import ZZ
M = snappy.Manifold('4_1')
N, c = M.num_tetrahedra(), M.num_cusps()
ge = M.gluing_equations()
print("figure-eight: N =", N, "tetrahedra, c =", c, "cusp(s)")
print("SL(2) DGG gauge group = U(1)^(N-c) = U(1)^%d (ABELIAN)" % (N - c))
print("gluing/NZ data all integers:", all(x in ZZ for row in ge for x in row),
      "-> abelian CS-matter (nonabelian gauge is not integer-NZ-encodable)")
print("cusp Cartan rank K-1 (abelian flavor):", {K: K - 1 for K in (2, 3, 4, 5)})
