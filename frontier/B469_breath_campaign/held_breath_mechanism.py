#!/usr/bin/env python3
"""Mechanism probe for the held-breath divisibility law:
 (1) exact minpoly of the sqrt-7 component across m=3,6,9,12,15 — same point or family?
 (2) is that character finite-order (root-of-unity eigenvalues)? trace z, is z=2cos(pi q)?
 (3) same for sqrt41 across m=5,10,15."""
import sympy as sp
x, z = sp.symbols('x z')
def components(m):
    t = {0: x, 1: z}
    for k in range(2, m + 2):
        t[k] = sp.expand(x * t[k-1] - t[k-2])
    eqs = [sp.expand(t[m] - x), sp.expand(t[m+1] - z), sp.expand(2*x**2 + z**2 - x*x*z)]
    G = sp.groebner(eqs, x, z, order='lex')
    elim = [g for g in G.exprs if g.free_symbols <= {z}]
    poly = sp.gcd(*elim) if len(elim) > 1 else elim[0]
    return [sp.expand(f) for f, _ in sp.factor_list(poly)[1]]

print("=== sqrt-7 components (3|m): exact z-minpoly ===")
for m in (3, 6, 9, 12, 15):
    comps = components(m)
    for f in comps:
        d = sp.Poly(f, z).degree()
        if d == 2 and sp.discriminant(f, z) == -7:
            print(f"  m={m}: {f}   roots {sp.solve(f,z)}", flush=True)

print("=== sqrt41 components (5|m) ===")
for m in (5, 10, 15):
    comps = components(m)
    for f in comps:
        d = sp.Poly(f, z).degree()
        disc = sp.discriminant(f, z)
        if disc == 16400:  # sqrt41 quartic
            print(f"  m={m}: {f}", flush=True)

# finite-order test: for the m=3 sqrt-7 point, get the full (x,y=x,z) triple and
# check if the group element has root-of-unity eigenvalues (finite order)
print("=== finite-order test on m=3 held breath ===")
m = 3
t = {0: x, 1: z}
for k in range(2, m + 2): t[k] = sp.expand(x * t[k-1] - t[k-2])
eqs = [sp.expand(t[m] - x), sp.expand(t[m+1] - z), sp.expand(2*x**2 + z**2 - x*x*z)]
sols = sp.solve(eqs, [x, z], dict=True)
for s in sols:
    xv, zv = s[x], s[z]
    if zv == 0: continue
    print(f"  (tr a, tr b, tr ab) = ({xv}, {xv}, {zv})  |disc check|", flush=True)
    # a finite-order element has trace 2cos(pi*rational); test tr a = xv
    print(f"    tr a = {sp.nsimplify(xv)}; is real 2cos? {sp.im(xv)==0 and abs(sp.re(xv))<=2}", flush=True)
    print(f"    N(z) = {sp.simplify(zv*sp.conjugate(zv))}", flush=True)
print("MECHANISM PROBE DONE", flush=True)
