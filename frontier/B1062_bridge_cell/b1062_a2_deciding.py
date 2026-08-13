"""A2's deciding computation, independent derivation: the geometric trace-field
degrees for m = 4, 5. If the degree pattern 2, 4, 8, ... continues monotonically,
the arithmeticity control deflates to smallest-member-in-costume (Class IV); if
scattered, the control is vindicated. Method identical to blocks 3/3b: lex
Groebner, eliminant factorization, elliptic components excluded by typing.
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

def geometric_degrees(m):
    w2a, w2b = phi2_words(m)
    eqs = [sp.numer(sp.together(wtrace(w2a) - x)),
           sp.numer(sp.together(wtrace(w2b) - y)),
           sp.numer(sp.together(wtrace(w2a + w2b) - z)),
           x**2 + y**2 + z**2 - x*y*z]
    print(f"[A2 m={m}] degrees {[sp.total_degree(e) for e in eqs]}; groebner...", flush=True)
    G = groebner(eqs, x, y, z, order='lex')
    uni = [g for g in G.exprs if g.free_symbols <= {z}][0]
    facs = sp.factor_list(sp.Poly(uni, z))[1]
    print(f"[A2 m={m}] eliminant factors: {[(sp.degree(f), e) for f, e in facs]}", flush=True)
    # type each factor's roots: a factor is GEOMETRIC-CANDIDATE-bearing iff it has
    # a root whose (x,y,z) are all non-elliptic (checked numerically per root)
    others = [g for g in G.exprs if not (g.free_symbols <= {z})]
    def etype(c):
        if abs(c.imag) > 1e-20: return "lox"
        if abs(c.real) < 2 - 1e-20: return "ELL"
        return "par/hyp"
    results = []
    for f, _e in facs:
        d = sp.degree(f)
        if d == 0: continue
        P = sp.Poly(f, z)
        geom = False
        for k in range(d):
            zr = CRootOf(P, k) if d > 1 else sp.roots(P).popitem()[0]
            try:
                sols = sp.solve([sp.expand(g.subs(z, zr)) for g in others], [x, y], dict=True)
            except Exception:
                sols = []
            for s in sols:
                try:
                    tx = complex(sp.N(s[x], 25)); ty = complex(sp.N(s[y], 25)); tz = complex(sp.N(zr, 25))
                except Exception:
                    continue
                if etype(tx) != "ELL" and etype(ty) != "ELL" and \
                   (etype(tx) == "lox" or etype(ty) == "lox" or etype(tz) == "lox"):
                    geom = True
                    break
            if geom: break
        results.append((d, geom))
        print(f"[A2 m={m}]   factor deg {d}: geometric-candidate roots present: {geom}", flush=True)
    geo_degs = [d for d, g in results if g]
    print(f"[A2 m={m}] GEOMETRIC-COMPONENT DEGREES: {geo_degs}", flush=True)
    return geo_degs

for m in (4, 5):
    try:
        geometric_degrees(m)
    except Exception as e:
        print(f"[A2 m={m}] FAILED: {type(e).__name__}: {e}", flush=True)
print("==== A2 deciding computation done ====", flush=True)
