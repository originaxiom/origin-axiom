#!/usr/bin/env python3
"""R07 post-unblinding diagnostic (written AFTER opening the arc's records).

The banked B955 scan example is N=6, x=(0,0,0,1,2,1), 'all 6-tuples' with root
evaluation m.c mod N — i.e. x = sum_i c_i omega_i^vee / N (fundamental-coweight
coordinates), which is an ADJOINT-torus parameterization. Compute exactly:
 - order of that x in adjoint E6 (smallest k with k x in P^vee),
 - order of that x in simply-connected E6 (smallest k with k x in Q^vee),
 - its centralizer type (must be A1+A2 + u1^3).
Exact rational arithmetic via sympy.
"""
from sympy import Matrix, Rational
import numpy as np
from e6_scan import C as Cnp, R, subsystem_type, rank_of_rootset

C = Matrix(Cnp.tolist())
c = Matrix([0, 0, 0, 1, 2, 1])
N = 6
# x in coweight basis: c/N. Coroot coordinates of x: C^{-1} c / N (C symmetric).
x_coroot = C.inv() * c / N
print("x in coroot basis:", [Rational(v) for v in x_coroot])

def order_in(latt_check, x):
    for k in range(1, 100):
        if latt_check(k * x):
            return k
    return None

is_int = lambda v: all(e == int(e) for e in v)
# adjoint: exp(2pi i x)=1 iff x in P^vee iff alpha_j(x) integer for all simple j,
# i.e. coweight coordinates integer -> k*c/N integer
ord_ad = order_in(lambda v: is_int(v), c / N)
# simply connected: x in Q^vee iff coroot coordinates integer
ord_sc = order_in(lambda v: is_int(v), x_coroot)
print(f"order of x in ADJOINT E6: {ord_ad}")
print(f"order of x in SIMPLY-CONNECTED E6: {ord_sc}")

# centralizer type via root evaluations m.c mod N
cv = np.array([0, 0, 0, 1, 2, 1], dtype=np.int64)
mask = (R @ cv) % N == 0
sub = [tuple(int(a) for a in r) for r in R[mask]]
srk = rank_of_rootset(sub)
print(f"contributing roots: {len(sub)}, semisimple type {subsystem_type(sub)}, "
      f"semisimple rank {srk}, centralizer = type + u1^{6-srk}, dim {6+len(sub)}")
