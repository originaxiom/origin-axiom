#!/usr/bin/env python3
"""C2b: THE CORRECT HABIRO COMPARISON — the Ohtsuki/Taylor expansion at q = 1
approximates the root-of-unity evaluations p-adically, with valuations growing
with the truncation order: the coherence the naive tower (memo 39) lacked,
found where Habiro-ring theory says it lives.

The unified element of 4_1 (all cyclotomic coefficients 1):
    f(q) = sum_{k>=0} prod_{j=1}^{k} (1 - q^j)(1 - q^{-j})
        (h-adically convergent: term k has t-adic valuation 2k, t = q - 1;
         at q = zeta_n it truncates to the memo-39 evaluation I(zeta_n),
         since (2 - zeta^j - zeta^{-j}) = (1-zeta^j)(1-zeta^{-j}) and the
         j = n factor vanishes — identity checked exactly below).
STEP 1: the Taylor/Ohtsuki coefficients a_n at q = 1, EXACT integers,
    f = sum_n a_n t^n  (computed in Z[[t]] to order N_MAX; term-count gate
    2k > N_MAX shown, so the truncation is complete, not approximate).
STEP 2: for each p^r in {4, 8, 9, 27, 5, 25} and truncation N in {4, 6, 8, 10}:
    v(N, p^r) := v_pi( I(zeta_{p^r}) - sum_{n<N} a_n (zeta_{p^r} - 1)^n ),
    computed exactly via v_p(Norm) (unique prime above p, f = 1).
PREREGISTERED two-outcome: v(N, p^r) >= N for every cell of the table (the
Taylor truncation approximates the evaluation to pi-order at least its own
length — Habiro-ring coherence exhibited exactly), or not (banked honestly).
Either way the exact table is the deliverable; together with memo 39's
universal v = 2 law it gives C-AD3 both faces: raw evaluations do not cohere
with each other, but all of them cohere with the SINGLE Taylor germ at 1 —
the finite places all reading one analytic object.
"""
import sympy as sp

x = sp.symbols('x')
N_MAX = 12
K_MAX = N_MAX // 2 + 1   # term k has t-valuation 2k

# ---- STEP 1: exact Taylor coefficients in Z[[t]] via polynomial arithmetic in t
t = sp.symbols('t')
def series_trunc(p_, order):
    return sp.Poly(sp.expand(p_), t).as_expr() + sp.O(t**order) if False else sp.expand(sp.series(p_, t, 0, order).removeO())
# work with plain truncated polys: represent series as Poly in t mod t^N
def mulmod(a, b, order):
    return sp.expand(sp.Mul(a, b, evaluate=True))
def trunc(e, order):
    e = sp.expand(e)
    return sum(c*t**int(m[0]) for m, c in sp.Poly(e, t).terms() if m[0] < order)

qpow = {0: sp.Integer(1)}
def q_to(j, order):
    # (1+t)^j for j possibly negative, truncated
    if j >= 0:
        return trunc(sp.expand((1+t)**j), order)
    inv = trunc(sp.expand(sum((-t)**i for i in range(order))), order)  # 1/(1+t)
    e = sp.Integer(1)
    for _ in range(-j):
        e = trunc(sp.expand(e*inv), order)
    return e

f_series = sp.Integer(0)
prod = sp.Integer(1)
for k in range(K_MAX+1):
    if k > 0:
        fac = trunc(sp.expand((1 - q_to(k, N_MAX))*(1 - q_to(-k, N_MAX))), N_MAX)
        prod = trunc(sp.expand(prod*fac), N_MAX)
        if prod == 0: break
    f_series = trunc(sp.expand(f_series + prod), N_MAX)
coeffs = [int(f_series.coeff(t, n)) for n in range(N_MAX)]
print(f"Ohtsuki/Taylor coefficients of the unified 4_1 element at q=1 (t = q-1), to t^{N_MAX-1}:")
print("  ", coeffs)
print(f"(truncation complete: term k has t-valuation 2k; k <= {K_MAX} covers order {N_MAX})")

# ---- machinery from memo 39 (exact, Z[x]/Phi)
def I_at_level(n):
    Phi = sp.Poly(sp.cyclotomic_poly(n, x), x)
    tot = sp.Integer(0); prod = sp.Integer(1)
    for k in range(n):
        if k > 0:
            term = 2 - x**(k % n) - x**((-k) % n)
            prod = sp.rem(sp.Poly(sp.expand(prod*term), x), Phi).as_expr()
        tot = sp.expand(tot + prod)
    return sp.rem(sp.Poly(tot, x), Phi).as_expr()

def val_p_norm(expr, modn, p):
    Phi = sp.Poly(sp.cyclotomic_poly(modn, x), x)
    Pe = sp.Poly(sp.expand(expr), x)
    if Pe.is_zero: return 'INF'
    R = sp.Integer(sp.resultant(Phi.as_expr(), Pe.as_expr(), x))
    if R == 0: return 'INF'
    v = 0
    while R % p == 0:
        R //= p; v += 1
    return v

# identity check: (2 - zeta^j - zeta^-j) == (1-zeta^j)(1-zeta^-j) exactly (as Laurent identity)
zj = sp.symbols('zj')
assert sp.expand((1-zj)*(1-1/zj) - (2 - zj - 1/zj)) == 0
print("identity (1-q^j)(1-q^-j) = 2 - q^j - q^-j: exact — I(zeta) is f's evaluation")

# ---- STEP 2: the comparison table
print("\nv_pi( I(zeta_{p^r}) - Taylor_N(zeta - 1) ), exact:")
levels = [(2,4),(2,8),(3,9),(3,27),(5,5),(5,25)]
gate_ok = True
for p, n in levels:
    Phi = sp.Poly(sp.cyclotomic_poly(n, x), x)
    I = I_at_level(n)
    row = []
    for N in (4, 6, 8, 10):
        tay = sp.Integer(0)
        for k in range(N):
            tay = sp.rem(sp.Poly(sp.expand(tay + coeffs[k]*(x-1)**k), x), Phi).as_expr()
        dif = sp.expand(I - tay)
        v = val_p_norm(dif, n, p)
        row.append((N, v))
        if v != 'INF' and v < N: gate_ok = False
    print(f"  p^r = {n}: " + "  ".join(f"N={N}: v={v}" for N, v in row))
print(f"\npreregistered gate v(N, p^r) >= N everywhere: {gate_ok}")
assert gate_ok

print("""
C2b CLOSED: the Taylor/Ohtsuki germ at q = 1 approximates EVERY p-power
evaluation to pi-adic order at least the truncation length — the exact
Habiro-ring coherence, exhibited as a table.  Read with memo 39: the finite
places do not cohere with EACH OTHER (universal v = 2), but every one of them
coheres with the single analytic germ at 1 — one object, many shadows, which
is C-AD3's adelic picture made exact.  The corpus's banked Ohtsuki-tower
arithmetic (B1133's C_0..C_4) now has its finite-place counterpart: the
integer coefficient list above is the shared germ both towers read.
Placement/structure only; Gate 5 untouched.""")
