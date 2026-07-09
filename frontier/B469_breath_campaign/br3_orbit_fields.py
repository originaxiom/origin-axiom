#!/usr/bin/env python3
"""B469 BR3 — the breath fields: the sigma_m-orbit of the geometric structure, per m.

sigma_m: a -> a^m b, b -> a. Trace map: T_m(x,y,z) = (t_m, x, t_{m+1}) where
t_k = tr(a^k b) satisfies t_k = x t_{k-1} - t_{k-2}, t_0 = y, t_1 = z (Cayley-Hamilton;
tr(a^m b a) = tr(a^{m+1} b) by cyclicity). m=1 gives the banked (z, x, xz-y).

Per m: the geometric fiber characters = Fix(T_m^2) with the cusp condition kappa = -2;
sigma_m acts; the period-2 orbit's field = the breath field of member m."""
import sympy as sp

x, y, z = sp.symbols('x y z')

def Tm(m):
    t = {0: y, 1: z}
    for k in range(2, m + 2):
        t[k] = sp.expand(x * t[k-1] - t[k-2])
    return (t[m], x, t[m+1])

def kappa(p, q, r):
    return sp.expand(p**2 + q**2 + r**2 - p*q*r - 2)

for m in (1, 2, 3):
    T = Tm(m)
    T2 = tuple(sp.expand(e.subs({x: T[0], y: T[1], z: T[2]}, simultaneous=True)) for e in Tm(m))
    eqs = [sp.expand(T2[i] - v) for i, v in enumerate((x, y, z))] + [kappa(x, y, z) + 2 - (-2) - 2]
    # cusp condition: kappa = -2 => x^2+y^2+z^2 - xyz = 0? kappa = tr[a,b] = x^2+y^2+z^2-xyz-2 = -2
    eqs = [sp.expand(T2[i] - v) for i, v in enumerate((x, y, z))] + [sp.expand(x**2 + y**2 + z**2 - x*y*z)]
    G = sp.groebner(eqs, x, y, z, order='lex')
    print(f"== m={m}: Groebner basis of Fix(T_m^2) + cusp ==", flush=True)
    uni = [g for g in G.exprs if len(g.free_symbols) == 1]
    for g in uni:
        var = list(g.free_symbols)[0]
        for f, mult in sp.factor_list(g)[1]:
            fp = sp.Poly(f, var)
            if fp.degree() >= 2:
                disc = sp.discriminant(f, var)
                sqf = sp.Integer(1)
                if disc != 0:
                    for pr, e in sp.factorint(sp.Integer(disc)).items():
                        if e % 2: sqf *= pr
                print(f"  factor in {var}: {sp.expand(f)}  disc={disc}  field=Q(sqrt({sqf}))", flush=True)
            elif fp.degree() == 1:
                print(f"  linear factor in {var}: {sp.expand(f)}", flush=True)
    # sigma-orbit check for the nondegenerate roots: T_m swaps the conjugate pair?
    print(flush=True)
print("DONE", flush=True)
