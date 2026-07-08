#!/usr/bin/env python3
"""B479 capstone: prime-m held breath = order-m torsion (tr a = cyclotomic trace)."""
import sympy as sp
x, z = sp.symbols('x z')
def held_xelim(m):
    t = {0: x, 1: z}
    for k in range(2, m + 2): t[k] = sp.expand(x * t[k-1] - t[k-2])
    eqs = [sp.expand(t[m]-x), sp.expand(t[m+1]-z), sp.expand(2*x**2+z**2-x*x*z)]
    Gx = sp.groebner(eqs, z, x, order="lex")
    return [g for g in Gx.exprs if g.free_symbols <= {x}][0]
for m in (7, 11, 13):
    cyc = sp.minimal_polynomial(2*sp.cos(2*sp.pi/m), x)
    facs = sp.factor_list(held_xelim(m))[1]
    ok = any(sp.Poly(f,x).degree()>1 and
             sp.simplify(sp.expand(f)/sp.LC(sp.Poly(f,x)) - sp.expand(cyc)/sp.LC(sp.Poly(cyc,x)))==0
             for f,_ in facs)
    print(f"m={m}: held breath = order-{m} torsion? {ok}")

