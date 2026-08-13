"""A2's m = 5, dedicated run (parallel to the m=4 typing): the z-eliminant's
complete factorization with RAW POLYNOMIALS printed (the A8 exact-match test),
full-triple typing per factor, and the geometric component's degree — my last
blind number. Conventions as declared: phi_5^2 (abelianization trace 27, det 1),
the Markov surface, trivial dropped, elliptic-typed-out on the FULL TRIPLE.
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
m = 5
wa, wb = "a"*m + "b", "a"
sub = lambda word: "".join({"a": wa, "b": wb, "A": winv(wa), "B": winv(wb)}[ch] for ch in word)
w2a, w2b = sub(wa), sub(wb)

def wtrace(word):
    M = sp.eye(2)
    for ch in word: M = M * mats[ch]
    return sp.cancel(sp.together(sp.trace(M)))

print(f"[m5] building trace polynomials (word lengths {len(w2a)}, {len(w2b)}, {len(w2a+w2b)})...", flush=True)
eqs = [sp.numer(sp.together(wtrace(w2a) - x)),
       sp.numer(sp.together(wtrace(w2b) - y)),
       sp.numer(sp.together(wtrace(w2a + w2b) - z)),
       x**2 + y**2 + z**2 - x*y*z]
print(f"[m5] system degrees: {[sp.total_degree(e) for e in eqs]}; lex groebner...", flush=True)
G = groebner(eqs, x, y, z, order='lex')
print(f"[m5] basis size {len(G.exprs)}", flush=True)
uni = [g for g in G.exprs if g.free_symbols <= {z}][0]
facs = sp.factor_list(sp.Poly(uni, z))[1]
print(f"[m5] z-eliminant factors (deg, mult): {[(sp.degree(f), e) for f, e in facs]}", flush=True)
print("[m5] RAW FACTOR POLYNOMIALS (the discard log's substrate, per the amended protocol):", flush=True)
for f, e in facs:
    print(f"[m5]   deg {sp.degree(f)}: {sp.expand(f.as_expr() if hasattr(f,'as_expr') else f)}", flush=True)

others = [g for g in G.exprs if not (g.free_symbols <= {z})]
def etype(c):
    if abs(c.imag) > 1e-20: return "lox"
    if abs(c.real) < 2 - 1e-20: return "ELL"
    return "par/hyp"

print("[m5] full-triple typing per factor:", flush=True)
for f, _e in facs:
    d = sp.degree(f)
    if d == 0: continue
    P = sp.Poly(f, z)
    verdicts = []
    for k in range(d):
        zr = CRootOf(P, k) if d > 1 else list(sp.roots(P).keys())[0]
        try:
            sols = sp.solve([sp.expand(g.subs(z, zr)) for g in others], [x, y], dict=True)
        except Exception as ex:
            verdicts.append(f"root{k}: solve-failed {type(ex).__name__}")
            continue
        for s in sols:
            try:
                tx = complex(sp.N(s[x], 25)); ty = complex(sp.N(s[y], 25)); tz = complex(sp.N(zr, 25))
            except Exception:
                continue
            verdicts.append(f"root{k}: ({etype(tx)},{etype(ty)},{etype(tz)})")
            break
    geom = any("(lox,lox,lox)" in v_ for v_ in verdicts) and not any(",ELL" in v_ or "(ELL" in v_ and "lox" not in v_ for v_ in [])
    n_ell = sum(1 for v_ in verdicts if "ELL" in v_)
    print(f"[m5]   deg-{d} factor: {n_ell} root(s) with an elliptic coordinate; "
          f"sample: {verdicts[:3]}", flush=True)

print("[m5] THE NUMBER: the geometric z-factor degree(s) = the deg of factors whose", flush=True)
print("     typed roots carry NO elliptic coordinate. Read from the lines above.", flush=True)
print("==== m5 done ====", flush=True)
