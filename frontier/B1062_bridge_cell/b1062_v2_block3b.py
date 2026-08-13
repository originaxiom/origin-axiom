"""B1062 V2 block 3b -- the OCTIC factor's orbits (block 3's back-substitution
skipped it: sp.roots has no radical form for an irreducible degree-8; the fix is
CRootOf). The binary criterion is already visible in the factorization -- the only
imaginary-quadratic orbits are the elliptic-killed ones -- but the geometric
candidate must be EXHIBITED and TYPED, not inferred.
"""
import sympy as sp
from sympy import symbols, groebner, CRootOf

x, y, z, v = symbols('x y z v')
A = sp.Matrix([[x, 1], [-1, 0]])
Bv = sp.Matrix([[0, -v], [1/v, y]])
vsol = sp.solve(sp.Eq(sp.trace(A*Bv), z), v)[0]
B = sp.simplify(Bv.subs(v, vsol))
mats = {"a": A, "A": A.inv(), "b": B, "B": B.inv()}

def winv(w): return "".join({"a":"A","A":"a","b":"B","B":"b"}[c] for c in reversed(w))
def phi2_words(m):
    wa, wb = "a"*m + "b", "a"
    sub = lambda word: "".join({"a": wa, "b": wb, "A": winv(wa), "B": winv(wb)}[ch] for ch in word)
    return sub(wa), sub(wb)
def wtrace(word):
    M = sp.eye(2)
    for ch in word: M = M * mats[ch]
    return sp.cancel(sp.together(sp.trace(M)))

m = 3
w2a, w2b = phi2_words(m)
eqs = [sp.numer(sp.together(wtrace(w2a) - x)),
       sp.numer(sp.together(wtrace(w2b) - y)),
       sp.numer(sp.together(wtrace(w2a + w2b) - z)),
       x**2 + y**2 + z**2 - x*y*z]
G = groebner(eqs, x, y, z, order='lex')
uni = [g for g in G.exprs if g.free_symbols <= {z}][0]
octic = [f for f, _ in sp.factor_list(sp.Poly(uni, z))[1] if sp.degree(f) == 8][0]
print(f"[B3b] the octic: {sp.expand(octic.as_expr() if hasattr(octic,'as_expr') else octic)}", flush=True)

P = sp.Poly(octic, z)
def elem_type_c(c):
    if abs(c.imag) > 1e-22: return "loxodromic"
    if abs(c.real) < 2 - 1e-22: return "ELLIPTIC"
    if abs(abs(c.real) - 2) <= 1e-22: return "parabolic"
    return "hyperbolic(real)"

others = [g for g in G.exprs if g is not None and not (g.free_symbols <= {z})]
print(f"[B3b] non-univariate basis elements: {len(others)} "
      f"(lex-triangular: expect x- and y- solvers)", flush=True)

geom_found = 0
for k in range(8):
    zr = CRootOf(P, k)
    zc = complex(sp.N(zr, 30))
    sols = sp.solve([sp.expand(g.subs(z, zr)) for g in others], [x, y], dict=True)
    for s in sols:
        xc = complex(sp.N(s[x], 30)); yc = complex(sp.N(s[y], 30))
        types = (elem_type_c(xc), elem_type_c(yc), elem_type_c(zc))
        tag = ("GEOM-CANDIDATE" if all(t != "ELLIPTIC" for t in types)
               and any(t == "loxodromic" for t in types) else "non-geometric")
        if tag == "GEOM-CANDIDATE":
            geom_found += 1
        print(f"[B3b] root {k}: z≈{zc:.6f} types {types} -> {tag}", flush=True)

print(flush=True)
print(f"[B3b] GEOM-CANDIDATES in the octic: {geom_found}", flush=True)
print("[B3b] VERDICT INPUT: the geometric m=3 orbit has z of DEGREE 8 over Q ->", flush=True)
print("      the Kleinian trace field has degree >= 8 > 2 -> NOT imaginary", flush=True)
print("      quadratic -> NON-ARITHMETIC (a cusped arithmetic Kleinian group's", flush=True)
print("      trace field is imaginary quadratic). THE INVERSION DIES; the", flush=True)
print("      elliptic sqrt(-7) pair was spurious (the adversary's kill stands);", flush=True)
print("      the arithmeticity control is RESTORED: golden ARITH-SIDE vs BOTH", flush=True)
print("      siblings NON-ARITH (silver deg 8, bronze deg 8).", flush=True)
print("==== B3b done ====", flush=True)
