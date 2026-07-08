#!/usr/bin/env python3
import sympy as sp
x, y, z = sp.symbols('x y z')
def Tm_sym(m):
    t = {0: y, 1: z}
    for k in range(2, m + 2):
        t[k] = sp.expand(x * t[k-1] - t[k-2])
    return (t[m], x, t[m+1])
m = 2
T = Tm_sym(m)
T2 = tuple(sp.expand(e.subs({x: T[0], y: T[1], z: T[2]}, simultaneous=True)) for e in Tm_sym(m))
I = [sp.expand(T2[i] - v) for i, v in enumerate((x, y, z))] + [sp.expand(x**2 + y**2 + z**2 - x*y*z)]
comp = sp.groebner(I + [z**4 + 16], x, y, z, order='lex')
fixed_ideal = sp.groebner(list(comp.exprs) + [sp.expand(T[i] - v) for i, v in enumerate((x, y, z))], x, y, z, order='lex')
print("Fix(T_2) on the z^4+16 component:", "EMPTY (free involution, two 2-cycles)" if fixed_ideal.exprs == [sp.Integer(1)] else fixed_ideal.exprs, flush=True)
# how many points does the component have? (degree of the ideal)
print("component GB:", [sp.expand(g) for g in comp.exprs], flush=True)
