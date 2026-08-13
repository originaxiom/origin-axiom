"""A2's m = 5 via the FRICKE RECURSION (supersedes the matrix-product attempt,
which spent 78 CPU-minutes inside a symbolic 37-matrix product): word traces as
polynomials in (x, y, z) by the SL2 trace identities with memoization, then the
same lex-Groebner elimination. Raw factor polynomials printed (the A8 match);
full-triple typing NUMERIC per root (the solve-at-CRootOf failure species is
avoided: (x, y) recovered from the lex basis numerically, not symbolically).
"""
import sympy as sp
from sympy import symbols, groebner

x, y, z = symbols('x y z')

def winv(w): return "".join({"a":"A","A":"a","b":"B","B":"b"}[c] for c in reversed(w))

def cyc_reduce(w):
    # free reduction
    out = []
    for ch in w:
        if out and out[-1] != ch and out[-1].lower() == ch.lower():
            out.pop()
        else:
            out.append(ch)
    w = "".join(out)
    # cyclic reduction
    while len(w) >= 2 and w[0] != w[-1] and w[0].lower() == w[-1].lower():
        w = w[1:-1]
    return w

MEMO = {}
def tr(w):
    """trace of the word as a polynomial in x, y, z (SL2 Fricke identities)."""
    w = cyc_reduce(w)
    if w == "":
        return sp.Integer(2)
    # normalize over inverse and cyclic rotations for memo hits
    cands = []
    for rot in range(len(w)):
        r = w[rot:] + w[:rot]
        cands.append(r); cands.append(winv(r))
    key = min(cands)
    if key in MEMO:
        return MEMO[key]
    w = key
    if w == "a": val = x
    elif w == "b": val = y
    elif w in ("ab",): val = z
    elif len(w) == 1: val = {"A": x, "B": y}[w]
    else:
        # split: w = U V with U = first letter; tr(UV) = tr(U)tr(V) - tr(U^-1 V)
        U, V = w[0], w[1:]
        val = sp.expand(tr(U) * tr(V) - tr(winv(U) + V))
    MEMO[key] = val
    return val

m = 5
wa, wb = "a"*m + "b", "a"
sub = lambda word: "".join({"a": wa, "b": wb, "A": winv(wa), "B": winv(wb)}[ch] for ch in word)
w2a, w2b = sub(wa), sub(wb)
print(f"[m5F] words: |phi2(a)|={len(w2a)} |phi2(b)|={len(w2b)}", flush=True)

import time
t0 = time.time()
Ta = tr(w2a); print(f"[m5F] tr(phi2 a) built ({time.time()-t0:.0f}s, memo {len(MEMO)})", flush=True)
Tb = tr(w2b); Tab = tr(w2a + w2b)
print(f"[m5F] all three trace polynomials built ({time.time()-t0:.0f}s, memo {len(MEMO)})", flush=True)

eqs = [sp.expand(Ta - x), sp.expand(Tb - y), sp.expand(Tab - z),
       x**2 + y**2 + z**2 - x*y*z]
print(f"[m5F] system degrees: {[sp.total_degree(e) for e in eqs]}; lex groebner...", flush=True)
G = groebner(eqs, x, y, z, order='lex')
uni = [g for g in G.exprs if g.free_symbols <= {z}][0]
facs = sp.factor_list(sp.Poly(uni, z))[1]
print(f"[m5F] z-eliminant factors (deg, mult): {[(sp.degree(f), e) for f, e in facs]}", flush=True)
print("[m5F] RAW FACTOR POLYNOMIALS (the discard-match substrate):", flush=True)
for f, e in facs:
    print(f"[m5F]   deg {sp.degree(f)}: {sp.expand(f.as_expr() if hasattr(f,'as_expr') else f)}", flush=True)

# numeric typing: roots of each factor; (x, y) recovered numerically from the
# lex basis via nsolve-free polynomial evaluation (the basis is triangular).
others = [sp.Poly(g, x, y, z) for g in G.exprs if not (sp.sympify(g).free_symbols <= {z})]
import numpy as np
def etype(c):
    if abs(c.imag) > 1e-18: return "lox"
    if abs(c.real) < 2 - 1e-18: return "ELL"
    return "par/hyp"
for f, _e in facs:
    d = sp.degree(f)
    if d == 0: continue
    roots = sp.Poly(f, z).nroots(n=30, maxsteps=200)
    tags = []
    for zr in roots:
        zc = complex(zr)
        # solve the two triangular basis elements for x, y numerically
        subbed = [sp.Poly(o.as_expr().subs(z, zr), x, y) for o in others]
        try:
            sols = sp.solve([p.as_expr() for p in subbed], [x, y], dict=True)
        except Exception:
            sols = []
        got = None
        for s in sols:
            try:
                xc, yc = complex(sp.N(s[x], 25)), complex(sp.N(s[y], 25))
                got = (etype(xc), etype(yc), etype(zc))
                break
            except Exception:
                continue
        tags.append(got or ("solve-fail",))
    n_ell = sum(1 for t in tags if t and "ELL" in t)
    n_fail = sum(1 for t in tags if t == ("solve-fail",))
    print(f"[m5F] deg-{d} factor: roots typed {len(tags)}, with-elliptic {n_ell}, "
          f"solve-fails {n_fail}; sample {tags[:3]}", flush=True)
print("==== m5F done ====", flush=True)
