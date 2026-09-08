#!/usr/bin/env python3
"""XI_k FROM THE PAPER'S OWN RECURSION -- an independent generator.

Gukov-Manolescu arXiv:1904.06057v2, section 9.3:
  (171)  alpha(x;q) F_K(x,q) + beta(x;q) F_K(xq,q) + gamma(x;q) F_K(xq^2,q) + F_K(xq^3,q) = 0
  (172)  alpha, beta, gamma explicit rational functions (transcribed verbatim below)

The paper uses this recursion + the h-bar initial conditions to build Table 8's P_k(x).
Here it is used differently: solved directly in the (x,q) series ansatz

      F_K(x,q) = sum_{k>=1} Xi_k(q) x^{k-1/2},      Xi_1 = 1   (normalisation)

which turns (171) into a triangular linear system for Xi_2, Xi_3, ....

CONTROL (preregistered, two-outcome): the paper prints Xi through x^{7/2} at line 4791 of
the extracted text / eq (11):
      Xi = x^{1/2} + 2x^{3/2} + (q^-1+3+q) x^{5/2} + (2q^-2+2q^-1+5+2q+2q^2) x^{7/2} + ...
If the recursion reproduces those four blocks exactly, the generator is trusted and its
Xi_5, Xi_6, Xi_7 are new data.  If it does not, the generator is void and nothing is
reported from it.

Second control: Xi_k(1) must equal the odd Fibonacci F(2k-1) = 1,2,5,13,34,89,233,
which the paper states independently in the h-bar^0 line of its 2F_K expansion (page 70).

Gate 5: exact rational arithmetic in Q[q,q^-1].  No measured input anywhere.
"""
import sympy as sp

X, Q = sp.symbols('X Q')
x = X**2
q = Q**2

# ---- (172), transcribed ------------------------------------------------------------
alpha_num = -(q**2*x + 1)*(q**5*x**2 - 1)
alpha_den = Q**5*(q*x + 1)*(q*x**2 - 1)

beta_inner = q*x*( q*x*( q*( x*(q*x - 2) - 1 ) + x + 1 ) + q - x - 2 ) + 1
beta_num = (q**5*x**2 - 1)*beta_inner
beta_den = q**4*x**2*(q*x**2 - 1)

gamma_inner = q*x*( q*( q*x*( q*(q**2*x - 1)*(q**2*x + q - 1) - 1 ) - 2 ) + 1 ) + 1
gamma_num = -(q**2*x + 1)*gamma_inner
gamma_den = Q**9*x**2*(q*x + 1)

# ---- sanity: the h-bar^0 (q=1) limits printed in (172) ------------------------------
P = x**4 - x**3 - x**2 - x + 1
chk = []
for nm, num, den, want in (("alpha", alpha_num, alpha_den, sp.Integer(-1)),
                           ("beta",  beta_num,  beta_den,  P/x**2),
                           ("gamma", gamma_num, gamma_den, -P/x**2)):
    got = sp.simplify((num/den).subs(Q, 1))
    ok = sp.simplify(got - want) == 0
    chk.append(ok)
    print(f"   (172) {nm} at q=1 matches the printed h^0 term: {ok}")
assert all(chk), "transcription of (172) is wrong -- stop"

# ---- clear denominators: D = Q^9 x^2 (qx+1)(qx^2-1) ---------------------------------
D = Q**9*x**2*(q*x + 1)*(q*x**2 - 1)
PA = sp.expand(sp.cancel(alpha_num*D/alpha_den))
PB = sp.expand(sp.cancel(beta_num *D/beta_den))
PC = sp.expand(sp.cancel(gamma_num*D/gamma_den))
PD = sp.expand(D)
for nm, p in (("A",PA),("B",PB),("C",PC),("D",PD)):
    assert sp.simplify(p - sp.expand(p)) == 0 and p.is_polynomial(X), nm
print("   denominators cleared; all four coefficients polynomial in x\n")

N = 9                                   # solve for Xi_1 .. Xi_N
f = [None] + [sp.Symbol(f'f{k}') for k in range(1, N+1)]
Fser = sum(f[k]*X**(2*k-1) for k in range(1, N+1))
E = sp.expand(PA*Fser
              + PB*Fser.subs(X, X*Q)
              + PC*Fser.subs(X, X*Q**2)
              + PD*Fser.subs(X, X*Q**3))
Epoly = sp.Poly(E, X)

sol = {f[1]: sp.Integer(1)}
for m in range(2, N+1):
    c = Epoly.coeff_monomial(X**(2*m-1))
    c = sp.expand(c.subs(sol))
    a = sp.expand(sp.diff(c, f[m]))
    b = sp.expand(c.subs(f[m], 0))
    val = sp.cancel(sp.simplify(-b/a))
    val = sp.cancel(sp.together(val))
    sol[f[m]] = sp.expand(sp.simplify(val))

def as_laurent(e):
    """return (min_exp_in_q, [coeffs]) of a Laurent polynomial in q = Q^2"""
    e = sp.cancel(sp.simplify(e))
    n, d = sp.fraction(sp.together(e))
    dp = sp.Poly(sp.expand(d), Q)
    assert len(dp.monoms()) == 1, f"denominator not a monomial: {d}"
    shift = int(sp.degree(dp, Q))
    lead = dp.coeffs()[0]
    np_ = sp.Poly(sp.expand(n)/lead, Q)
    deg = int(sp.degree(np_, Q))
    cs = [np_.coeff_monomial(Q**i) for i in range(deg+1)]
    lo = 0
    while lo < len(cs) and cs[lo] == 0: lo += 1
    hi = len(cs)
    while hi > lo and cs[hi-1] == 0: hi -= 1
    cs = cs[lo:hi]
    e0 = lo - shift
    assert e0 % 2 == 0 and all(c == 0 for i, c in enumerate(cs) if i % 2), f"half-integer q power in {e}"
    return int(e0//2), [int(c) for c in cs[::2]]

PUBLISHED = {1: (0, [1]), 2: (0, [2]), 3: (-1, [1,3,1]), 4: (-2, [2,2,5,2,2])}
FIB = [1,1]
while len(FIB) < 2*N+2: FIB.append(FIB[-1]+FIB[-2])

print("XI_k FROM THE RECURSION")
print("="*78)
control_ok = True
out = {}
for k in range(1, N+1):
    e0, cs = as_laurent(sol[f[k]])
    out[k] = (e0, cs)
    s = sum(cs)
    fib = FIB[2*k-2]
    line = f"   Xi_{k}: q^{e0:<3} {cs}"
    tag = f"   sum={s} (F({2*k-1})={fib} {'ok' if s==fib else 'MISMATCH'})"
    if k in PUBLISHED:
        m = (e0, cs) == PUBLISHED[k]
        control_ok &= m
        tag += f"   [published: {'MATCH' if m else 'MISMATCH'}]"
    else:
        tag += "   [NEW]"
    print(line + tag)
    control_ok &= (s == fib)

print("\n   CONTROL (four published blocks + all Fibonacci sums):",
      "PASSED" if control_ok else "FAILED -- generator void")
if not control_ok:
    raise SystemExit(1)

# ---- the actual test: block placement in Zhat_0(S^3_{-1/2}(4_1)) --------------------
print("\n" + "="*78)
print("BLOCK PLACEMENT TEST  --  eq (13), Zhat_0(S^3_{-1/2}(4_1))")
print("="*78)
GIVEN = {0:1, 1:-1, 3:2, 6:-2, 9:1, 10:3, 11:1, 14:-1, 15:-3, 16:-1}   # eq (13), published
pred = {}
for k in range(1, N+1):
    C = (2*k-1)*(k-1)
    e0, cs = out[k]
    for i, c in enumerate(cs):
        e = e0 + i
        pred[C+e]         = pred.get(C+e, 0) + c
        pred[C+(2*k-1)+e] = pred.get(C+(2*k-1)+e, 0) - c

allok = all(pred.get(e, 0) == v for e, v in GIVEN.items())
noextra = all(pred.get(e, 0) == 0 for e in range(0, 17) if e not in GIVEN)
print(f"   ten published coefficients reproduced : {allok}")
print(f"   no spurious terms in q^0..q^16         : {noextra}")

lim = (2*N-1)*(N-1)
print(f"\n   series through q^{lim} (blocks 1..{N} complete up to here):")
row = []
for e in range(0, lim+1):
    v = pred.get(e, 0)
    if v: row.append(f"{v:+d}q^{e}")
print("     " + " ".join(row))
print(f"\n   block 4 was PREDICTED at centre 21 (q^19..q^23) / negated 28 (q^26..q^30).")
b4 = {e: pred.get(e,0) for e in range(19,24)}
b4n = {e: pred.get(e,0) for e in range(26,31)}
print(f"   observed q^19..q^23: {[b4[e] for e in range(19,24)]}   (expect [2,2,5,2,2])")
print(f"   observed q^26..q^30: {[b4n[e] for e in range(26,31)]}  (expect [-2,-2,-5,-2,-2])")
