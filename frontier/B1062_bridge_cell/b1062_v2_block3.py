"""B1062 V2 block 3 -- the COMPLETE fixed-point variety for m = 3 (the adversary's
kill: block 1's solve returned only a non-geometric elliptic orbit; tr = -1 forces
order-3 elliptics, impossible for a faithful rep of a free group). Method: exact
elimination (Groebner, lex) -> univariate factorization -> back-substitution ->
TYPE every orbit (loxodromic = non-real trace required for geometricity candidates).
Also re-typing m = 1, 2's orbits for the record (their traces are non-real: pass).
"""
import sympy as sp
from sympy import symbols, groebner, QQ

x, y, z, v = symbols('x y z v')

A = sp.Matrix([[x, 1], [-1, 0]])
Bv = sp.Matrix([[0, -v], [1/v, y]])
vsol = sp.solve(sp.Eq(sp.trace(A*Bv), z), v)[0]
B = sp.simplify(Bv.subs(v, vsol))
Ai, Bi = A.inv(), B.inv()
mats = {"a": A, "A": Ai, "b": B, "B": Bi}

def winv(w):
    return "".join({"a":"A","A":"a","b":"B","B":"b"}[c] for c in reversed(w))

def phi2_words(m):
    wa, wb = "a"*m + "b", "a"
    def sub(word):
        return "".join({"a": wa, "b": wb, "A": winv(wa), "B": winv(wb)}[ch] for ch in word)
    return sub(wa), sub(wb)

def wtrace(word):
    M = sp.eye(2)
    for ch in word:
        M = M * mats[ch]
    return sp.cancel(sp.together(sp.trace(M)))

m = 3
w2a, w2b = phi2_words(m)
Ta, Tb, Tab = wtrace(w2a), wtrace(w2b), wtrace(w2a + w2b)
eqs = [sp.numer(sp.together(Ta - x)),
       sp.numer(sp.together(Tb - y)),
       sp.numer(sp.together(Tab - z)),
       x**2 + y**2 + z**2 - x*y*z]
print(f"[B3] m=3 system degrees: {[sp.total_degree(e) for e in eqs]}", flush=True)

print("[B3] computing lex Groebner basis (eliminating x, y)...", flush=True)
G = groebner(eqs, x, y, z, order='lex')
uni = [g for g in G.exprs if g.free_symbols <= {z}]
print(f"[B3] basis size {len(G.exprs)}; univariate-in-z elements: {len(uni)}", flush=True)
assert uni, "no univariate eliminant -- HALT"
fz = sp.factor_list(sp.Poly(uni[0], z))
print(f"[B3] eliminant factors (deg, mult): {[(sp.degree(f), e) for f, e in fz[1]]}", flush=True)

orbits = []
for f, _e in fz[1]:
    d = sp.degree(f)
    if d == 0:
        continue
    for zr in sp.roots(sp.Poly(f, z)) or {}:
        # back-substitute: solve remaining basis elements for x, y at z = zr
        sub = [sp.expand(g.subs(z, zr)) for g in G.exprs]
        sols = sp.solve([s for s in sub if s.free_symbols & {x, y}], [x, y], dict=True)
        for s in sols:
            orbits.append((s[x], s[y], zr, sp.degree(f)))
print(f"[B3] fixed points recovered: {len(orbits)}", flush=True)

def elem_type(tr):
    trn = sp.nsimplify(tr)
    c = complex(sp.N(trn, 30))
    if abs(c.imag) > 1e-25:
        return "loxodromic"
    if abs(c.real) < 2 - 1e-25:
        return "ELLIPTIC"
    if abs(abs(c.real) - 2) <= 1e-25:
        return "parabolic"
    return "hyperbolic(real)"

geoms = []
for (X, Y, Z, d) in orbits:
    types = (elem_type(X), elem_type(Y), elem_type(Z))
    tag = "GEOM-CANDIDATE" if all(t != "ELLIPTIC" for t in types) and \
          any(t == "loxodromic" for t in types) else "non-geometric"
    if X == 0 and Y == 0 and Z == 0:
        tag = "trivial"
    print(f"[B3]   deg-{d} orbit ({sp.nsimplify(X)}, {sp.nsimplify(Y)}, {sp.nsimplify(Z)}) "
          f"types {types} -> {tag}", flush=True)
    if tag == "GEOM-CANDIDATE":
        prim = X + 2*Y + 4*Z
        t = sp.symbols('t')
        mp = sp.minimal_polynomial(prim, t)
        geoms.append(((X, Y, Z), mp, sp.degree(mp)))

print(flush=True)
for (triple, mp, deg) in geoms:
    print(f"[B3] GEOM-CANDIDATE field degree {deg}; minpoly {sp.expand(mp)}", flush=True)
    # imaginary-quadratic test decides the leading criterion
    if deg == 2:
        disc = sp.discriminant(sp.Poly(mp, sp.symbols('t')))
        print(f"[B3]   degree 2, discriminant {disc} -> "
              f"{'IMAGINARY QUADRATIC: ARITH-SIDE' if disc < 0 else 'real: NON-ARITH'}",
              flush=True)
    else:
        print(f"[B3]   degree {deg} > 2 -> NON-ARITHMETIC (cusped arithmetic needs "
              f"imaginary quadratic)", flush=True)

print("==== B3 done: m=3's complete variety, typed ====", flush=True)
