#!/usr/bin/env python3
"""B469 BR3 wave 3 — the HELD-BREATH tower: Fix(T_m) directly (the sigma-FIXED
characters, not the period-2 breath). T_m(x,y,z) = (t_m, x, t_{m+1}) = (x,y,z) forces
x = y and t_m = x, t_{m+1} = z, on the cusp kappa = -2 (i.e. x^2+y^2+z^2-xyz = 0).
Cheap: one variable eliminated up front. Which m hold a breath, and in what field?"""
import sympy as sp
x, z = sp.symbols('x z')   # y = x on the fixed locus
def held(m):
    # t_0 = y = x, t_1 = z, t_k = x t_{k-1} - t_{k-2}
    t = {0: x, 1: z}
    for k in range(2, m + 2):
        t[k] = sp.expand(x * t[k-1] - t[k-2])
    eqs = [sp.expand(t[m] - x), sp.expand(t[m+1] - z),
           sp.expand(x**2 + x**2 + z**2 - x*x*z)]  # cusp with y=x
    G = sp.groebner(eqs, x, z, order='lex')
    elim = [g for g in G.exprs if g.free_symbols <= {z}]
    if not elim: return "positive-dim (no z-eliminant)"
    poly = sp.gcd(*elim) if len(elim) > 1 else elim[0]
    out = []
    for f, mult in sp.factor_list(poly)[1]:
        d = sp.Poly(f, z).degree()
        if d == 1:
            r = sp.solve(f, z)[0]
            out.append(f"z={r}(triv)" if r == 0 else f"z={r}")
        else:
            disc = sp.discriminant(f, z)
            sf = 1
            for pr, e in sp.factorint(int(disc)).items():
                if e % 2: sf *= pr
            out.append(f"deg{d}:disc{disc}~Q(sqrt{sf})")
    return out
for m in range(1, 13):
    print(f"m={m:2d}: {held(m)}", flush=True)
print("HELD BREATH TOWER DONE", flush=True)
