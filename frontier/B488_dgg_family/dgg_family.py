#!/usr/bin/env sage-python
"""B488: metallic DGG laws T[A_m]=U(1)^{2m-1}, H1=(Z/m)^2+Z; twist-knot table."""
import snappy
for m in range(1,9):
    M=snappy.Manifold('b++'+'R'*m+'L'*m); M.simplify()
    print(f"m={m}: rank U(1)^{M.num_tetrahedra()-M.num_cusps()}, H1={M.homology()}")
