#!/usr/bin/env python3
"""Geometric ID for s464 (m=3): (a) try the Ptolemy database for exact solutions;
(b) octic vs Q(sqrt-7): factor the octic over Q(sqrt-7); (c) fiber-subgroup traces
numerically via degree-0 words."""
import sympy as sp
z = sp.symbols('z')
oct_poly = z**8 - z**7 + 6*z**6 - 5*z**5 + 21*z**4 + 15*z**3 + 7*z**2 - 3*z + 3
print("octic factor over Q(sqrt(-7)):", sp.factor(oct_poly, extension=sp.sqrt(-7)), flush=True)
print("octic galois-reducibility over Q(i):", sp.factor(oct_poly, extension=sp.I), flush=True)
print("octic disc factored:", sp.factorint(sp.discriminant(oct_poly, z)), flush=True)

import snappy
M = snappy.Manifold('s464')
print("\ns464 ptolemy database try:", flush=True)
try:
    sols = M.ptolemy_variety(2, obstruction_class='all').retrieve_solutions(verbose=False)
    for i, per_class in enumerate(sols):
        for s in per_class.flatten(depth=2):
            try:
                nf = s.number_field()
                print(f"  class {i}: number field {nf}", flush=True)
            except Exception as e:
                print(f"  class {i}: sol ({type(s).__name__}) {e}", flush=True)
except Exception as e:
    print(f"  retrieve failed: {type(e).__name__}: {e}", flush=True)
