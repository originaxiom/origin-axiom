#!/usr/bin/env python3
"""B469 BR3 wave 2 (exact) — certify the T_m action on Fix(T_m^2) + cusp at
COMPONENT level by ideal membership (no numerics). For each irreducible factor
F(z) of the z-eliminant: does T_m map V(I+F) to V(I+G)? Test: reduce G(t_{m+1})
mod GB(I+F) == 0. Within a preserved component: T_m pointwise-fixed iff
T_m(x,y,z) === (x,y,z) mod the component ideal."""
import sympy as sp

x, y, z = sp.symbols('x y z')

def Tm_sym(m):
    t = {0: y, 1: z}
    for k in range(2, m + 2):
        t[k] = sp.expand(x * t[k-1] - t[k-2])
    return (t[m], x, t[m+1])

for m in (1, 2, 3):
    print(f"===== m = {m} =====", flush=True)
    T = Tm_sym(m)
    T2 = tuple(sp.expand(e.subs({x: T[0], y: T[1], z: T[2]}, simultaneous=True)) for e in Tm_sym(m))
    I = [sp.expand(T2[i] - v) for i, v in enumerate((x, y, z))] + [sp.expand(x**2 + y**2 + z**2 - x*y*z)]
    G = sp.groebner(I, x, y, z, order='lex')
    elim = [g for g in G.exprs if g.free_symbols <= {z}]
    assert elim, "no z-eliminant (not zero-dim in z?)"
    factors = [f for f, _ in sp.factor_list(sp.gcd(*elim) if len(elim) > 1 else elim[0])[1]]
    print(f"  z-eliminant factors: {[sp.expand(f) for f in factors]}", flush=True)
    comps = []
    for F in factors:
        GF = sp.groebner(list(G.exprs) + [F], x, y, z, order='lex')
        comps.append((F, GF))
    for F, GF in comps:
        img_z = T[2]  # z-coord of T_m(P) = t_{m+1}
        targets = [sp.expand(Gf) for Gf, _ in comps for Gf in [Gf]]
        hits = []
        for Gpoly, _ in comps:
            r = GF.reduce(sp.expand(Gpoly.subs(z, img_z) if False else sp.Poly(Gpoly, z).as_expr().subs(z, img_z)))[1]
            if r == 0: hits.append(sp.expand(Gpoly))
        fixed = all(GF.reduce(sp.expand(T[i] - v))[1] == 0 for i, v in enumerate((x, y, z)))
        deg = sp.Poly(F, z).degree()
        disc = sp.discriminant(F, z) if deg >= 2 else None
        print(f"  component F(z)={sp.expand(F)} (deg {deg}, disc {disc}): T_m maps into {hits}; pointwise-fixed={fixed}", flush=True)
print("BR3 WAVE2 EXACT DONE", flush=True)
