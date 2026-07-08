#!/usr/bin/env python3
"""Extend the held-breath tower m=13..16 to test: 3|m <=> Q(sqrt-7) component;
5|m <=> Q(sqrt41) component. m=15 is the crux (should carry BOTH)."""
import sympy as sp
x, z = sp.symbols('x z')
def held(m):
    t = {0: x, 1: z}
    for k in range(2, m + 2):
        t[k] = sp.expand(x * t[k-1] - t[k-2])
    eqs = [sp.expand(t[m] - x), sp.expand(t[m+1] - z), sp.expand(2*x**2 + z**2 - x*x*z)]
    G = sp.groebner(eqs, x, z, order='lex')
    elim = [g for g in G.exprs if g.free_symbols <= {z}]
    if not elim: return "positive-dim"
    poly = sp.gcd(*elim) if len(elim) > 1 else elim[0]
    out = []
    for f, mult in sp.factor_list(poly)[1]:
        d = sp.Poly(f, z).degree()
        if d == 1: 
            if sp.solve(f,z)[0] != 0: out.append("z=nonzero-rational")
            continue
        disc = sp.discriminant(f, z); sf = 1
        for pr, e in sp.factorint(int(disc)).items():
            if e % 2: sf *= pr
        out.append(f"deg{d}~Q(sqrt{sf})")
    return out
for m in (13, 14, 15, 16):
    r = held(m)
    has7 = any('sqrt-7' in s for s in r) if isinstance(r, list) else False
    has41 = any('sqrt41' in s for s in r) if isinstance(r, list) else False
    print(f"m={m}: {r}  | 3|m={m%3==0} sqrt-7={has7}  5|m={m%5==0} sqrt41={has41}", flush=True)
print("EXT DONE", flush=True)
