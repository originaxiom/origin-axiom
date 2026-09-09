#!/usr/bin/env python3
"""INGEST AN EXTERNAL QUANTUM A-POLYNOMIAL AND SAY WHETHER IT ANNIHILATES F^+_{m(5_2)}.

Built while waiting for the primary-source data named in fetch/FETCH_REQUEST_CEFF.md
section B'' -- Garoufalidis-Sun [GS10] or Garoufalidis-Koutschan [GK13], the sources
Park's own footnote 12 names for eq (32)'s data.

WHY IT IS NOT JUST A PARSER.  Those authors write the operator in (M, L) notation and
need not share Park's conventions: an overall monomial is irrelevant to annihilation,
but q -> 1/q, x -> 1/x and a reversal of the yhat-degree all give a DIFFERENT operator
that is still "the" quantum A-polynomial of the same knot.  So this does not assume a
convention -- it SEARCHES the small standard space of them and reports which, if any,
annihilates Park's own printed blocks.

USAGE
    python3 ahat_ingest.py <file>
where <file> gives the five coefficients of yhat^i, in any of:
    a0: <expr>            (one per line, any order)
    {<a0>, <a1>, <a2>, <a3>, <a4>}          (a Mathematica-style list)
Accepted variable names: x or M for the meridian; q; and ^ or ** for powers.
Sqrt[q], q^(1/2) and q^{1/2} are all understood.

WHAT IT REPORTS
    for each convention tried, the coefficient of x^{n+1/2} in Ahat F^+ for n = 0..3,
    computed against Park's OWN f_0, f_1 (his closed forms) and f_2, f_3 (his Q(q)
    formulas).  A correct operator makes all four vanish.  Park's printed eq (32) makes
    the first three vanish and leaves q^13 f_0(q) at x^{7/2} -- memo 183's finding.

SELF-TEST (runs with no argument, and must pass before any external file is trusted):
    T1  the printed eq (32) reproduces memo 183's defect, in the identity convention.
    T2  no convention in the search space rescues it -- so a convention mismatch is
        NOT an alternative explanation for the defect.
    T3  eq (32) plus memo 183 addendum 2's c_3 term makes the x^{7/2} coefficient vanish,
        so the diagnostic can see a repair when there is one.

Gate 5: exact arithmetic.  No fitted constant.
"""
import sys, os, re
from fractions import Fraction as Fr
import sympy as sp

LQ = 240
x, Q = sp.symbols('x Q')          # q = Q^2 so half-integer powers of q stay polynomial
q = Q**2

# ---------- Park's own blocks: f_0, f_1 closed forms; f_2, f_3 his Q(q) formulas -------
def ladd(a, b, sc=1):
    r = dict(a)
    for e, c in b.items():
        r[e] = r.get(e, 0)+sc*c
        if r[e] == 0: del r[e]
    return r
def lmul(a, b, cap=LQ):
    r = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            e = e1+e2
            if e <= cap: r[e] = r.get(e, 0)+c1*c2
    return {e: c for e, c in r.items() if c}
def ldiv(num, den, cap=LQ):
    dl = min(den); dc = Fr(den[dl]); cur = dict(num); res = {}
    while cur:
        lo = min(cur)
        if lo-dl > cap: break
        k = Fr(cur[lo])/dc; res[lo-dl] = res.get(lo-dl, 0)+k
        for a_, b_ in den.items():
            t = lo-dl+a_; cur[t] = cur.get(t, 0)-Fr(b_)*k
            if cur[t] == 0: del cur[t]
    return {e: c for e, c in res.items() if c}
def poly(*t):
    d = {}
    for e, c in t: d[e] = d.get(e, 0)+c
    return {e: c for e, c in d.items() if c}
def f0ser():
    a = {}; j = 0
    while j*(j+1)//2 <= LQ+2: a[j*(j+1)//2] = a.get(j*(j+1)//2, 0)+(-1)**j; j += 1
    return {e-1: -c for e, c in a.items() if c}
def f1ser():
    a = {}; j = 0
    while j*(j+1)//2 <= LQ+2:
        b = j*(j+1)//2
        for t in range(j+1):
            if b+t <= LQ+2: a[b+t] = a.get(b+t, 0)+(-1)**j
        j += 1
    return {e-1: -c for e, c in a.items() if c}
F0, F1 = f0ser(), f1ser()
den2 = poly((1,-1),(3,1))
F2 = ladd(ldiv(lmul(poly((0,1),(1,1),(2,-1)), F0), den2),
          ldiv(lmul(poly((0,-1),(1,-2),(2,1)), F1), den2))
den3 = poly((2,1),(4,-1),(5,-1),(7,1))
F3 = ladd(ldiv(lmul(poly((0,-2),(1,-1),(2,-1),(3,2),(4,1),(5,-1)), F0), den3),
          ldiv(lmul(poly((0,2),(1,1),(2,3),(3,-1),(6,-1)), F1), den3))
FQ = {0: F0, 1: F1, 2: F2, 3: F3}

# ---------- the printed eq (32), for the self-test and as the comparison point ----------
A_PRINTED = [
  -q**9*x**7*(q**3*x+1)*(q**5*x**2-1)*(q**7*x**2-1),
  (Q**11*x**2*(q*x+1)*(q**3*x+1)*(q**7*x-1)
   *(q**9*x**6+q**8*x**6-q**8*x**4-3*q**7*x**5-q**7*x**4-q**6*x**5
     +2*q**6*x**4+2*q**6*x**3+q**5*x**4-q**5*x**2-q**4*x**3-q**3*x**4
     -q**3*x**3+q**3*x**2+2*q**2*x**3+2*q**2*x**2-q*x**2-2*q*x+1)),
  (-q**2*(q**2*x-1)*(q**2*x+1)*(q*x**2-1)*(q**7*x**2-1)
   *(q**12*x**6+q**11*x**5-2*q**10*x**5-3*q**9*x**4+2*q**8*x**4-q**8*x**3
     +2*q**7*x**3-q**6*x**4-4*q**6*x**3-q**5*x**3-3*q**5*x**2+q**4*x**3
     +2*q**4*x**2+q**3*x-q**2*x**2-2*q**2*x+1)),
  (Q*(q*x**2-1)*(q*x+1)*(q**3*x+1)
   *(q**16*x**6-2*q**13*x**5-q**13*x**4+q**11*x**4+2*q**10*x**4+2*q**10*x**3
     -q**9*x**4-q**8*x**3-q**8*x**2-q**7*x**3-q**7*x**2+2*q**6*x**3+2*q**6*x**2
     +q**5*x**2-q**3*x**2-3*q**3*x-q**2*x+q+1)),
  (q*x+1)*(q*x**2-1)*(q**3*x**2-1),
]

# ---------- parsing an external file ----------
def parse(text):
    t = text
    t = re.sub(r'\(\*.*?\*\)', ' ', t, flags=re.S)          # Mathematica comments
    t = t.replace('Sqrt[q]', '(q^(1/2))')
    t = re.sub(r'q\^\{([^}]*)\}', r'q^(\1)', t)             # q^{11/2}
    t = re.sub(r'x\^\{([^}]*)\}', r'x^(\1)', t)
    t = t.replace('^', '**')
    t = re.sub(r'\bM\b', 'x', t)                            # (M,L) notation
    labelled = re.findall(r'a\s*_?\s*([0-4])\s*[:=]\s*([^\n]+)', t)
    if len(labelled) >= 5:
        d = {int(i): e for i, e in labelled}
        return [d[i] for i in range(5)]
    m = re.search(r'\{(.*)\}', t, flags=re.S)
    if m:
        parts, depth, cur = [], 0, ''
        for ch in m.group(1):
            if ch in '([{': depth += 1
            if ch in ')]}': depth -= 1
            if ch == ',' and depth == 0: parts.append(cur); cur = ''
            else: cur += ch
        parts.append(cur)
        if len(parts) == 5: return parts
    raise SystemExit("could not parse five coefficients -- see the USAGE block")
def tosym(strs):
    out = []
    for s_ in strs:
        e = sp.sympify(s_.strip(), locals={'x': x, 'q': q, 'Q': Q})
        e = e.subs(sp.Symbol('q'), q)
        out.append(sp.expand(sp.together(e)))
    return out

# ---------- the diagnostic ----------
def coeffs_of(A):
    """A: list of five sympy expressions in x, Q -> {i: {x-degree: {Q-exp: int}}}"""
    out = []
    for a in A:
        a = sp.expand(sp.cancel(a))
        P = sp.Poly(a, x)
        d = {}
        for dx in range(P.degree()+1):
            c = sp.expand(P.coeff_monomial(x**dx))
            if c == 0: continue
            pc = sp.Poly(c, Q)
            dd = {}
            for (e,), co in pc.terms():
                co = sp.nsimplify(co)
                if co.q != 1: return None          # non-integer coefficient
                dd[int(e)] = int(co)
            if dd: d[dx] = dd
        out.append(d)
    return out
def q2Q(d): return {2*e: c for e, c in d.items()}
def defect(COEF, n, cap=2*LQ-60):
    row = {}
    for i in range(5):
        for dx, c in COEF[i].items():
            j = n-dx
            if j < 0 or j > 3: continue
            row[j] = ladd(row.get(j, {}), {e+2*i*j+i: v for e, v in c.items()})
    acc = {}
    for j, rj in row.items(): acc = ladd(acc, lmul(rj, q2Q(FQ[j]), cap))
    return {e: c for e, c in acc.items() if c and e <= cap}, (max(row) if row else -1)
def describe(d):
    if not d: return "0"
    tgt = {e+26: c for e, c in q2Q(F0).items() if e+26 <= max(d)}
    if all(d.get(e, 0) == v for e, v in tgt.items()) and all(e in tgt for e in d):
        return "q^13 * f_0(q)   <-- exactly memo 183's defect"
    lo = min(d)
    return "non-zero, lowest Q^%d, %d terms" % (lo, len(d))

CONVENTIONS = [
    ("identity",                       lambda A: A),
    ("q -> 1/q",                       lambda A: [sp.expand(sp.cancel(a.subs(Q, 1/Q))) for a in A]),
    ("x -> 1/x",                       lambda A: [sp.expand(sp.cancel(a.subs(x, 1/x))) for a in A]),
    ("yhat-degree reversed",           lambda A: A[::-1]),
    ("yhat reversed, q -> 1/q",        lambda A: [sp.expand(sp.cancel(a.subs(Q, 1/Q))) for a in A[::-1]]),
    ("yhat reversed, x -> 1/x",        lambda A: [sp.expand(sp.cancel(a.subs(x, 1/x))) for a in A[::-1]]),
    ("q -> 1/q and x -> 1/x",          lambda A: [sp.expand(sp.cancel(a.subs({Q: 1/Q, x: 1/x}))) for a in A]),
]
def clear_denoms(A):
    """an overall monomial in x and Q is irrelevant to annihilation; clear it"""
    out = []
    for a in A:
        a = sp.cancel(sp.together(a))
        n_, d_ = sp.fraction(a)
        out.append(sp.expand(n_/d_) if d_.free_symbols == set() else sp.expand(n_))
    lo_x = min([sp.Poly(a, x).monoms()[-1][0] for a in out if a != 0] or [0])
    out = [sp.expand(sp.cancel(a/x**lo_x)) for a in out]
    return out
def report(A, label):
    print("="*78); print(label); print("="*78)
    verdicts = {}
    for name, f in CONVENTIONS:
        try: B = clear_denoms(f([sp.sympify(a) for a in A]))
        except Exception as ex: print("   %-26s : could not normalise (%s)" % (name, ex)); continue
        C = coeffs_of(B)
        if C is None:
            print("   %-26s : non-integer coefficients after clearing" % name); continue
        rows = []
        allzero = True
        for n in range(4):
            d, need = defect(C, n)
            if need > 3: rows.append("x^{%d+1/2}: needs f_%d" % (n, need)); continue
            rows.append("x^{%d+1/2}: %s" % (n, describe(d)))
            if d: allzero = False
        verdicts[name] = allzero
        print("   %-26s : %s" % (name, "  |  ".join(rows)))
        if allzero: print("        >>> ANNIHILATES Park's blocks in this convention <<<")
    return verdicts

if __name__ == "__main__":
    if len(sys.argv) > 1:
        A = tosym(parse(open(sys.argv[1]).read()))
        v = report(A, "EXTERNAL OPERATOR: %s" % os.path.basename(sys.argv[1]))
        good = [k for k, ok in v.items() if ok]
        print("="*78)
        if good:
            print("VERDICT: this operator ANNIHILATES F^+_{m(5_2)}, in convention(s): %s" % good)
            print("   -> it differs from Park's printed eq (32), which does not.  The erratum")
            print("      of memo 183 is CONFIRMED against the primary source, and the repair")
            print("      is handed over rather than fitted.")
        else:
            print("VERDICT: this operator does NOT annihilate F^+_{m(5_2)} in any convention tried.")
            print("   -> if it is the same operator as eq (32), the defect is older and further")
            print("      upstream than Park.  If it differs, one of us has mis-transcribed and")
            print("      the printed coefficients above localise where.")
        raise SystemExit(0)
    # ---- self-test ----
    print("SELF-TEST (no file given).  These must pass before any external file is trusted.\n")
    v = report(A_PRINTED, "T1/T2  Park's printed eq (32)")
    d, _ = defect(coeffs_of(clear_denoms(A_PRINTED)), 3)
    t1 = describe(d).startswith("q^13")
    t2 = not any(v.values())
    rep = list(A_PRINTED); rep[1] = sp.expand(rep[1] - Q**25*x**3)
    v2 = report(rep, "T3  eq (32) + memo 183 addendum 2's c_3 = -q^{25/2} x^3 in a_1")
    d3, _ = defect(coeffs_of(clear_denoms(rep)), 3)
    t3 = (not d3)
    print("="*78)
    print("   T1 printed eq (32) reproduces memo 183's defect q^13 f_0 at x^{7/2} :",
          "PASSED" if t1 else "FAILED")
    print("   T2 no convention in the search space rescues it                     :",
          "PASSED" if t2 else "FAILED")
    print("   T3 the diagnostic sees a repair when there is one (x^{7/2} vanishes):",
          "PASSED" if t3 else "FAILED")
    if not (t1 and t2 and t3): raise SystemExit("SELF-TEST FAILED -- do not trust this ingester.")
    print("\nSELF-TEST PASSED.  Ready for the primary-source file.")
