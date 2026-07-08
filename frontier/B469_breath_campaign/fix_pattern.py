#!/usr/bin/env python3
"""For m=1..5: components of Fix(T_m^2)+cusp; which are sigma-fixed pointwise
(nontrivial Fix(T_m)) vs swapped. The m=3 sigma-fixed Q(sqrt-7) pair: first of a
pattern or isolated?"""
import sympy as sp
x, y, z = sp.symbols('x y z')
def Tm_sym(m):
    t = {0: y, 1: z}
    for k in range(2, m + 2):
        t[k] = sp.expand(x * t[k-1] - t[k-2])
    return (t[m], x, t[m+1])
for m in (1, 2, 3, 4, 5):
    T = Tm_sym(m)
    T2 = tuple(sp.expand(e.subs({x: T[0], y: T[1], z: T[2]}, simultaneous=True)) for e in Tm_sym(m))
    I = [sp.expand(T2[i] - v) for i, v in enumerate((x, y, z))] + [sp.expand(x**2 + y**2 + z**2 - x*y*z)]
    G = sp.groebner(I, x, y, z, order='lex')
    elim = [g for g in G.exprs if g.free_symbols <= {z}]
    factors = [f for f, _ in sp.factor_list(sp.gcd(*elim) if len(elim) > 1 else elim[0])[1]]
    out = []
    for F in factors:
        if sp.Poly(F, z).degree() == 1 and F == z: out.append("z:triv"); continue
        GF = sp.groebner(list(G.exprs) + [F], x, y, z, order='lex')
        fixed = all(GF.reduce(sp.expand(T[i] - v))[1] == 0 for i, v in enumerate((x, y, z)))
        deg = sp.Poly(F, z).degree()
        disc = sp.discriminant(F, z) if deg >= 2 else None
        out.append(f"deg{deg}(disc {disc}):{'SIGMA-FIXED' if fixed else 'swapped'}")
    print(f"m={m}: {out}", flush=True)
print("FIX PATTERN DONE", flush=True)
