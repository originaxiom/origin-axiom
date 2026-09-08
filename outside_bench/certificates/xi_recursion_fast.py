#!/usr/bin/env python3
"""XI_k TO HIGH ORDER, and the resulting Zhat_0(S^3_{-1/2}(4_1)) series.

Same recursion (171)-(172) of Gukov-Manolescu arXiv:1904.06057v2 as xi_recursion.py,
but with the linear solve done in pure-integer Laurent arithmetic instead of sympy,
so it reaches k ~ 30 instead of k ~ 8.

Structure used:  writing PA,PB,PC,PD for the recursion's four coefficients after
clearing denominators, the X^{2m-1} coefficient of the recursion reads

   [A_0 + B_0 Q^{2m-1} + C_0 Q^{2(2m-1)} + D_0 Q^{3(2m-1)}] Xi_m  =  -(terms in Xi_{<m})

and (A_0,B_0,C_0,D_0) = (0, -Q, 1, 0), so the divisor is Q^{2m}(Q^{2m-2} - 1):
division by a binomial, exact by construction.

CONTROLS (both must fire or nothing is reported):
  C1  Xi_1..Xi_4 equal the four blocks printed in eq (11) / page 70.
  C2  Xi_k(1) = F(2k-1), the odd Fibonacci numbers, which the paper states
      independently in the h^0 line of its 2F_K expansion.
  C3  the assembled Zhat series reproduces all ten published coefficients of eq (13)
      and has no spurious term in q^0..q^16.

Gate 5: exact integer arithmetic.  No measured input.
"""
import sympy as sp, math, json, sys

X, Q = sp.symbols('X Q')
x, q = X**2, Q**2

alpha = -(q**2*x + 1)*(q**5*x**2 - 1) / (Q**5*(q*x + 1)*(q*x**2 - 1))
beta  = (q**5*x**2 - 1)*(q*x*( q*x*( q*( x*(q*x - 2) - 1 ) + x + 1 ) + q - x - 2 ) + 1) / (q**4*x**2*(q*x**2 - 1))
gamma = -(q**2*x + 1)*(q*x*( q*( q*x*( q*(q**2*x - 1)*(q**2*x + q - 1) - 1 ) - 2 ) + 1 ) + 1) / (Q**9*x**2*(q*x + 1))

P = x**4 - x**3 - x**2 - x + 1
assert sp.simplify(alpha.subs(Q,1) + 1) == 0
assert sp.simplify(beta.subs(Q,1) - P/x**2) == 0
assert sp.simplify(gamma.subs(Q,1) + P/x**2) == 0
print("   (172) transcription checked against the printed q=1 limits: ok")

D = Q**9*x**2*(q*x + 1)*(q*x**2 - 1)
polys = [sp.Poly(sp.expand(sp.cancel(c*D)), X) for c in (alpha, beta, gamma, sp.Integer(1))]

# --- Laurent polynomials in Q as dict {exp: int} -------------------------------------
def lmul(a, b):
    r = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            r[e1+e2] = r.get(e1+e2, 0) + c1*c2
    return {e: c for e, c in r.items() if c}
def ladd(a, b):
    r = dict(a)
    for e, c in b.items():
        r[e] = r.get(e, 0) + c
        if r[e] == 0: del r[e]
    return r
def lshift(a, s): return {e+s: c for e, c in a.items()}
def lneg(a): return {e: -c for e, c in a.items()}

def to_dict(expr):
    """coefficient (in Q) of a fixed X power -> Laurent dict"""
    p = sp.Poly(sp.expand(expr), Q)
    d = {}
    for (e,), c in p.terms():
        d[int(e)] = int(c)
    return {e: c for e, c in d.items() if c}

# PA..PD as lists over x-degree i, entries Laurent dicts
COEF = []
for p in polys:
    dx = int(sp.degree(p, X))
    assert dx % 2 == 0
    lst = []
    for i in range(dx//2 + 1):
        lst.append(to_dict(p.coeff_monomial(X**(2*i))))
    COEF.append(lst)
assert COEF[0][0] == {} and COEF[0][1] == {}
assert COEF[1][0] == {1: -1} and COEF[2][0] == {0: 1}
assert COEF[3][0] == {} and COEF[3][1] == {}
print("   divisor structure confirmed: (A0,B0,C0,D0) = (0, -Q, 1, 0)\n")

def divide_by_binomial(num, m):
    """exact division of Laurent dict num by Q^{2m} (Q^{2m-2} - 1)"""
    s = 2*m
    n = {e - s: c for e, c in num.items()}
    if m == 1:
        assert not n, "Xi_1 must be free"
        return None
    d = 2*m - 2
    # divide by (Q^d - 1):  work from the lowest exponent upward
    n = dict(n); out = {}
    while n:
        lo = min(n)
        c = n[lo]
        out[lo] = out.get(lo, 0) - c          # (Q^d-1)*(-c Q^lo) = -c Q^{lo+d} + c Q^lo
        n[lo] = n[lo] - c
        if n[lo] == 0: del n[lo]
        e2 = lo + d
        n[e2] = n.get(e2, 0) + c
        if n[e2] == 0: del n[e2]
    return {e: c for e, c in out.items() if c}

N = int(sys.argv[1]) if len(sys.argv) > 1 else 26
XI = {1: {0: 1}}
for m in range(2, N+1):
    acc = {}
    for j in range(4):
        for i, Pi in enumerate(COEF[j]):
            k = m - i
            if k < 1 or k >= m or not Pi: continue
            acc = ladd(acc, lmul(Pi, lshift(XI[k], j*(2*k-1))))
    XI[m] = divide_by_binomial(lneg(acc), m)

fib = [1, 1]
while len(fib) < 2*N: fib.append(fib[-1] + fib[-2])
PUB = {1: (0, [1]), 2: (0, [2]), 3: (-1, [1,3,1]), 4: (-2, [2,2,5,2,2])}

def block(k):
    d = XI[k]
    assert all(e % 2 == 0 for e in d), f"half-integer q power in Xi_{k}"
    lo, hi = min(d)//2, max(d)//2
    return lo, [d.get(2*e, 0) for e in range(lo, hi+1)]

print("XI_k FROM THE RECURSION")
print("="*78)
c1 = c2 = True
for k in range(1, min(N, 9)+1):
    lo, cs = block(k)
    s = sum(cs); f = fib[2*k-2]
    c2 &= (s == f)
    tag = ""
    if k in PUB:
        m = (lo, cs) == PUB[k]; c1 &= m
        tag = f"  [published: {'MATCH' if m else 'MISMATCH'}]"
    print(f"   Xi_{k}: q^{lo} .. q^{lo+len(cs)-1}  sum={s} (F({2*k-1})={f} {'ok' if s==f else 'BAD'}){tag}")
    if k <= 6: print(f"        {cs}")
for k in range(1, N+1):
    c2 &= (sum(block(k)[1]) == fib[2*k-2])
print(f"\n   C1 four published blocks : {'PASSED' if c1 else 'FAILED'}")
print(f"   C2 Fibonacci sums k<={N}  : {'PASSED' if c2 else 'FAILED'}")
if not (c1 and c2): raise SystemExit("controls failed -- generator void, nothing reported")

wid = [len(block(k)[1]) for k in range(1, N+1)]
print(f"   widths  : {wid[:12]}")
print(f"   (k-1)^2/4 floor*2+1: {[2*((k-1)**2//4)+1 for k in range(1,13)]}")

# ---- assemble Zhat_0(S^3_{-1/2}(4_1)) via Thm 1.2 / the derived placement ----------
print("\n" + "="*78)
print("Zhat_0(S^3_{-1/2}(4_1))")
print("="*78)
GIVEN = {0:1, 1:-1, 3:2, 6:-2, 9:1, 10:3, 11:1, 14:-1, 15:-3, 16:-1}
LIM = (2*N-1)*(N-1)          # last block's centre; safe horizon is a bit below
pred = {}
for k in range(1, N+1):
    C = (2*k-1)*(k-1); lo, cs = block(k)
    for i, c in enumerate(cs):
        e = lo + i
        pred[C+e] = pred.get(C+e, 0) + c
        pred[C+(2*k-1)+e] = pred.get(C+(2*k-1)+e, 0) - c
# safe horizon: below the lowest exponent any UNCOMPUTED block could reach
Kn = N+1
safe = (2*Kn-1)*(Kn-1) - ((Kn-1)**2//4) - 1
print(f"   blocks 1..{N} computed; series exact up to q^{safe}")
c3 = all(pred.get(e,0) == v for e,v in GIVEN.items()) and \
     all(pred.get(e,0) == 0 for e in range(17) if e not in GIVEN)
print(f"   C3 eq (13)'s ten coefficients, and no spurious term in q^0..q^16: "
      f"{'PASSED' if c3 else 'FAILED'}")

print("\n   THE BLOCK-4 PREDICTION (memo 175 addendum 2, made with no data behind it):")
print("     block 4 = [2,2,5,2,2] centred at 21 -> q^19..q^23, negated centred 28 -> q^26..q^30")
o1 = [pred.get(e,0) for e in range(19,24)]
o2 = [pred.get(e,0) for e in range(26,31)]
print(f"     q^19..q^23 = {o1}   {'CONFIRMED' if o1==[2,2,5,2,2] else 'REFUTED'}")
print(f"     q^26..q^30 = {o2}   {'CONFIRMED' if o2==[-2,-2,-5,-2,-2] else 'REFUTED'}")
gap = [e for e in range(17,19) if pred.get(e,0)]
print(f"     nothing at q^17, q^18 : {not gap}")

terms = " ".join(f"{v:+d}q^{e}" for e in range(0, min(safe,80)+1) if (v:=pred.get(e,0)))
print(f"\n   {terms}")

json.dump({str(e): pred.get(e,0) for e in range(0, safe+1)},
          open('/tmp/zhat41_series.json','w'))
print(f"\n   series written to /tmp/zhat41_series.json  (q^0 .. q^{safe})")
