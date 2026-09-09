#!/usr/bin/env python3
"""C2 / C-AD3: THE HABIRO TOWER FOR 4_1 — the cyclotomic expansion verified
exactly, the Kashaev bridge verified exactly, and the p-adic congruence tower
exhibited with exact valuations: the finite-place shadow of the quantum
invariant, made explicit.

The Habiro/cyclotomic form of the (normalized) colored Jones of the figure-8
(all cyclotomic coefficients = 1 — Habiro's own example):
    J_N(q) = sum_{k=0}^{N-1} prod_{j=1}^{k} ( q^N + q^{-N} - q^j - q^{-j} ).
CHECKS (exact, in Z[q,q^-1] and Z[zeta]):
  1. N = 2 reproduces the classical Jones polynomial of 4_1:
     q^2 - q + 1 - q^{-1} + q^{-2}  (CITED anchor), and J_N(q) = J_N(1/q)
     manifestly; J_1 = 1.
  2. THE KASHAEV BRIDGE: at q = zeta_N (primitive N-th root), q^N = 1 and the
     j = N factor kills the tail, giving  J_N(zeta_N) = sum_k prod_j
     (2 - zeta^j - zeta^{-j}) = sum_k prod_j |1 - zeta^j|^2 = <4_1>_N —
     verified EXACTLY in Z[x]/Phi_N for N = 5, 7, 9.
  3. THE TOWER (the adelic cell's finite-place ladder): define the unified
     evaluation I(zeta) = sum_{k=0}^{ord-1} prod_{j=1}^{k}(2 - zeta^j -
     zeta^{-j}) in Z[zeta].  For p in {2,3,5} and r = 1,2 compare levels
     inside Z[zeta_{p^{r+1}}] (embedding zeta_{p^r} = zeta_{p^{r+1}}^p):
        v_r := pi-adic valuation of  I(zeta_{p^{r+1}}) - I(zeta_{p^r}),
     with pi = (1 - zeta_{p^{r+1}}) the unique prime above p; computed
     EXACTLY via v_p(|Norm|) = v_p(|Res(Phi_{p^{r+1}}, .)|)  (f = 1, so
     pi-valuation = p-valuation of the norm).
  PREREGISTERED two-outcome: the differences are nonzero with valuations
  v_r >= p^r - 1 growing along the tower (levels cohere p-adically — the
  congruence-tower structure C-AD3 names), banked as an exact table; or the
  tower fails to cohere — banked as the honest negative.
"""
import sympy as sp

q = sp.symbols('q')
x = sp.symbols('x')

def J_poly(N):
    tot = sp.Integer(0); prod = sp.Integer(1)
    for k in range(N):
        if k > 0:
            j = k
            prod = sp.expand(prod * (q**N + q**(-N) - q**j - q**(-j)))
        tot = sp.expand(tot + prod)
    return sp.expand(tot)

# 1. anchors
J1 = J_poly(1); J2 = J_poly(2)
print("J_1 =", J1)
print("J_2 =", sp.expand(J2))
assert J1 == 1
assert sp.expand(J2 - (q**2 - q + 1 - 1/q + q**-2)) == 0
J3 = J_poly(3)
assert sp.expand(J3 - J3.subs(q, 1/q)) == 0
print("J_2 = classical Jones of 4_1 (CITED anchor): True;  J_3(q) = J_3(1/q): True")

# 2. the Kashaev bridge, exactly in Z[x]/Phi_N
def to_cyclo(expr, n):
    """expr in q,q^-1 -> canonical rep in Z[x]/Phi_n(x)"""
    Phi = sp.cyclotomic_poly(n, x)
    e = sp.expand(expr)
    p_ = sp.Integer(0)
    for term, coeff in sp.Poly(sp.expand(e * q**(4*n*n)), q).all_terms() if False else []:
        pass
    # robust route: substitute q -> x with exponents reduced mod n
    e2 = sp.expand(e)
    out = sp.Integer(0)
    for mon, c in sp.Poly(sp.together(e2*q**(8*n)).simplify(), q).terms():
        exp_ = mon[0] - 8*n
        out += c * x**(exp_ % n)
    return sp.rem(sp.Poly(out, x), sp.Poly(Phi, x)).as_expr()

def kashaev_cyclo(n):
    Phi = sp.cyclotomic_poly(n, x)
    tot = sp.Integer(0); prod = sp.Integer(1)
    for k in range(n):
        if k > 0:
            term = 2 - x**(k % n) - x**((-k) % n)
            prod = sp.rem(sp.Poly(sp.expand(prod*term), x), sp.Poly(Phi, x)).as_expr()
        tot = sp.expand(tot + prod)
    return sp.rem(sp.Poly(tot, x), sp.Poly(Phi, x)).as_expr()

for n in (5, 7, 9):
    lhs = to_cyclo(J_poly(n), n)
    rhs = kashaev_cyclo(n)
    same = sp.expand(lhs - rhs) == 0
    print(f"Kashaev bridge at N = {n}: J_N(zeta_N) == <4_1>_N exactly in Z[zeta_{n}]: {same}")
    assert same

# 3. the p-adic tower
def I_at_level(n, modn):
    """I(zeta_n) written inside Z[x]/Phi_modn via zeta_n = x^(modn//n)"""
    Phi = sp.Poly(sp.cyclotomic_poly(modn, x), x)
    g = modn // n
    tot = sp.Integer(0); prod = sp.Integer(1)
    for k in range(n):
        if k > 0:
            term = 2 - x**((g*k) % modn) - x**((-g*k) % modn)
            prod = sp.rem(sp.Poly(sp.expand(prod*term), x), Phi).as_expr()
        tot = sp.expand(tot + prod)
    return sp.rem(sp.Poly(tot, x), Phi).as_expr()

def val_p_norm(expr, modn, p):
    Phi = sp.Poly(sp.cyclotomic_poly(modn, x), x)
    Pe = sp.Poly(sp.expand(expr), x)
    if Pe.is_zero: return None
    R = sp.resultant(Phi.as_expr(), Pe.as_expr(), x)
    R = sp.Integer(R)
    if R == 0: return None
    v = 0
    while R % p == 0:
        R //= p; v += 1
    return v

print("\nthe p-adic congruence tower (valuations of I(zeta_{p^{r+1}}) - I(zeta_{p^r}) at the prime above p):")
table = {}
for p in (2, 3, 5):
    for r in (1, 2):
        lo = p**r; hi = p**(r+1)
        if hi > 125: continue
        dif = sp.expand(I_at_level(hi, hi) - I_at_level(lo, hi))
        v = val_p_norm(dif, hi, p)
        table[(p, r)] = v
        print(f"  p={p}, level {lo} -> {hi}:  v_pi(difference) = {v}")
coherent = all(v is not None and v >= p**r - 1 for (p, r), v in table.items())
grow = all(table[(p,2)] > table[(p,1)] for p in (2,3) if (p,2) in table)
print(f"\npreregistered gates: all valuations >= p^r - 1: {coherent}; valuations grow with r: {grow}")
# PREREGISTERED SECOND BRANCH REALIZED — and the measured law is sharper than the gate:
univ2 = all(v == 2 for v in table.values())
print(f"MEASURED LAW: v_pi(difference) = 2 UNIVERSALLY (all p, all r): {univ2}")
assert univ2
# mechanism check: the first new-level factor pair (1-zeta)(1-zeta^{-1}) = 2 - zeta - zeta^{-1}
# itself has v_pi exactly 2 (it IS pi * pibar-associate); verify for each level
for p in (2,3,5):
    for r in (1,2):
        hi=p**(r+1)
        if hi>125: continue
        vfac = val_p_norm(2 - x - x**(hi-1), hi, p)
        print(f"  v_pi(2 - zeta - zeta^-1) at level {hi}: {vfac}  (the smallest new factor pair)")
        assert vfac == 2

print("""
C2 / C-AD3 CLOSED ON THE PREREGISTERED SECOND BRANCH, with the law exact:
the cyclotomic expansion of 4_1 is verified against its classical anchor and
the Kashaev bridge holds exactly in Z[zeta] at three levels — but the NAIVE
tower does NOT cohere: the difference of consecutive unified evaluations has
pi-adic valuation EXACTLY 2, universally (six cases, three primes), pinned to
the smallest new-level factor pair (1-zeta)(1-zeta^{-1}), whose valuation is
exactly 2.  In p-adic terms v_p = 2/phi(p^{r+1}) -> 0: raw evaluations do not
converge along the tower.  The finite-place shadow is exhibited and its
first-order structure is now an exact universal law; the CORRECT Habiro-ring
congruence (Taylor-at-zeta / Frobenius-twisted comparison) is the named
follow-up, with this table as its target data.  Placement/structure only;
Gate 5 untouched.""")
