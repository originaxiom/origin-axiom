#!/usr/bin/env python3
"""R016: hostile reproduction of the corrected zeta_3 Habiro embedding.

Outside-bench memo 69 found a collapse at level 15.  Main B1158 attributed
that collapse to using the conjugate cube-root embedding and asserted that
the embedding compatible with the fixed abstract zeta_3 restores coherence.
This self-contained certificate performs the missing exact comparison.

The unified (Habiro) element of the figure-eight knot, EXACTLY the cyclotomic
form used in c2_habiro.py / c2b_ohtsuki_bridge.py (all cyclotomic
coefficients = 1, Habiro's own example for 4_1):
    F(q) = sum_{k>=0} prod_{j=1}^{k} (1 - q^j)(1 - q^{-j}).
At any root of unity zeta of order m, the j=m factor (1-zeta^m)=0 kills the
tail, so F(zeta) is the FINITE sum over k=0..m-1 (verified exactly in
c2_habiro.py / c2b_ohtsuki_bridge.py at several m; re-derived here as F_at_level).

PREREGISTERED FACTS (each backed by an assert below):
 1. Setup sanity: J_2 anchor and the Kashaev-bridge identity
    (1-q^j)(1-q^{-j}) = 2 - q^j - q^{-j} used by the banked certs still hold
    (re-verified, not re-derived from scratch, to certify we are using the
    SAME F(q) as c2_habiro.py/c2b_ohtsuki_bridge.py).
 2. THE GERM AT zeta_3: working in Q(zeta_3)[eps]/(eps^Nmax) with
    q = zeta_3 + eps (zeta_3 realized abstractly as the symbol x with
    x^2+x+1=0, i.e. Phi_3(x)), and q^{-1} built as a truncated geometric
    series, F(q) truncates: since q^3 = 1 + O(eps) only at eps=0 for the
    j-multiple-of-3 factors, each such factor has eps-valuation exactly 2,
    so term k has eps-valuation >= 2*floor(k/3); summing k = 0..K_BOUND with
    K_BOUND = 3*NMAX+3 already exceeds the needed floor(k/3) >= NMAX/2, and
    re-running with K_BOUND2 = K_BOUND+9 changes NONE of the NMAX extracted
    Taylor coefficients d_j (stabilization, asserted termwise).
 3. THE COMPARISON TABLE: for p in {5,7}, r in {1,2}, modn = 3*p^r, xi a
    primitive modn-th root (realized as the symbol w with Phi_modn(w)=0).
    The fixed abstract zeta_3 is embedded as w^e, where e is p^r or 2*p^r
    and e == 1 mod 3.  Its order is computed and asserted.  With
    Delta = xi-zeta_3, compute
    v_pi( F(xi) - sum_{j<N} d_j * Delta^j ), N = 1..NMAX, computed exactly via
    v_p(Norm) = v_p(Resultant(Phi_modn, .)).  The exact table must satisfy
    v(N)>=N and strict growth at all four declared levels.
 4. CONJUGATE-EMBEDDING CONTROL: at modn=15, deliberately substitute the
    other cube root w^5.  The memo-69 row [2,0,...,0] must reappear through
    Taylor order 11.  This separates a base-embedding mismatch from a
    truncation artifact.

The certificate proves the finite four-level statement only.  It does not
prove B1158's universal phrase "at every level"; that quantifier still needs
an all-level local/Habiro argument.
No measured physical constants enter anywhere (Gate 5 untouched — this is
pure exact algebra in Q and cyclotomic extensions of Q). CITED: the Habiro
cyclotomic form of the 4_1 unified WRT invariant is Habiro's own textbook
example (all cyclotomic coefficients = 1); everything else here is asserted.
"""
import sympy as sp

# ---------------------------------------------------------------------------
# FACT 1: sanity — same F(q) as the banked certs (Kashaev-bridge identity,
# and the classical-Jones anchor J_2, re-verified quickly, not re-derived).
# ---------------------------------------------------------------------------
q = sp.symbols('q')
zj = sp.symbols('zj')
assert sp.expand((1 - zj) * (1 - 1/zj) - (2 - zj - 1/zj)) == 0

def J_poly(N):
    tot = sp.Integer(0); prod = sp.Integer(1)
    for k in range(N):
        if k > 0:
            prod = sp.expand(prod * (q**N + q**(-N) - q**k - q**(-k)))
        tot = sp.expand(tot + prod)
    return sp.expand(tot)

J2 = J_poly(2)
assert sp.expand(J2 - (q**2 - q + 1 - 1/q + q**-2)) == 0
print("FACT 1 (sanity): (1-q^j)(1-q^-j) = 2-q^j-q^-j identity holds; J_2 == classical Jones of 4_1: True")

# ---------------------------------------------------------------------------
# FACT 2: the Taylor germ d_j of F(q) at q = zeta_3, exact in Q(zeta_3)[eps].
# zeta_3 realized as symbol x with Phi_3(x) = x^2+x+1 = 0.
# ---------------------------------------------------------------------------
x, eps = sp.symbols('x eps')
Phi3 = x**2 + x + 1
NMAX = 8                    # Taylor order requested ("around 8")
K_BOUND = 3*NMAX + 3        # 27 : term-count bound preregistered in the task
K_BOUND2 = K_BOUND + 9       # stabilization check bound

def trunc_eps(e, order):
    e = sp.expand(e)
    if not e.has(eps):
        return e
    p_ = sp.Poly(e, eps)
    return sp.expand(sum(c * eps**int(m[0]) for m, c in p_.terms() if m[0] < order))

def reduce_x(e):
    e = sp.expand(e)
    if not e.has(x):
        return e
    Px = sp.Poly(e, x)
    PPhi = sp.Poly(Phi3, x)
    return sp.rem(Px, PPhi).as_expr()

def reduce_all(e, order):
    return reduce_x(trunc_eps(e, order))

def taylor_germ(nmax, kbound):
    """Return [d_0,...,d_{nmax-1}], each an expr a+b*x (mod Phi3), the exact
    eps-Taylor coefficients of F(x+eps) truncated at eps^nmax, summing k=0..kbound."""
    inv_x = sp.expand(-1 - x)  # x^{-1} mod Phi3, since x^3=1 => x^{-1}=x^2=-1-x
    # 1/(x+eps) = inv_x / (1 + eps*inv_x) = inv_x * sum_i (-eps*inv_x)^i
    u = reduce_all(eps * inv_x, nmax)
    s = sp.Integer(0); term = sp.Integer(1)
    for _ in range(nmax):
        s = sp.expand(s + term)
        term = reduce_all(term * (-u), nmax)
    inv_q = reduce_all(inv_x * s, nmax)
    q_expr = x + eps
    qp = {0: sp.Integer(1)}
    qn = {0: sp.Integer(1)}
    for j in range(1, kbound + 1):
        qp[j] = reduce_all(qp[j - 1] * q_expr, nmax)
        qn[j] = reduce_all(qn[j - 1] * inv_q, nmax)
    tot = sp.Integer(0); prod = sp.Integer(1)
    for k in range(0, kbound + 1):
        if k > 0:
            factor = reduce_all((1 - qp[k]) * (1 - qn[k]), nmax)
            prod = reduce_all(prod * factor, nmax)
        tot = reduce_all(tot + prod, nmax)
    f_series = tot
    return [reduce_x(sp.expand(f_series).coeff(eps, j)) for j in range(nmax)]

d_coeffs = taylor_germ(NMAX, K_BOUND)
d_coeffs_check = taylor_germ(NMAX, K_BOUND2)
stable = all(sp.expand(d_coeffs[j] - d_coeffs_check[j]) == 0 for j in range(NMAX))
print(f"\nFACT 2: Taylor germ d_j of F at q=zeta_3 (x = zeta_3, Phi_3(x)=x^2+x+1=0), NMAX={NMAX}:")
for j, dj in enumerate(d_coeffs):
    a = dj.coeff(x, 0); b = dj.coeff(x, 1)
    print(f"  d_{j} = {a} + {b}*zeta_3   [raw: {dj}]")
print(f"stabilization K_BOUND={K_BOUND} -> K_BOUND2={K_BOUND2}: coefficients unchanged: {stable}")
assert stable

# ---------------------------------------------------------------------------
# FACT 3: the comparison table at modn = 3*p^r, p in {5,7}, r in {1,2}.
# xi realized as symbol w with Phi_modn(w)=0; zeta_3 embeds as w^{p^r}.
# ---------------------------------------------------------------------------
w = sp.symbols('w')

def Phi_poly(n):
    return sp.Poly(sp.cyclotomic_poly(n, w), w)

def F_at_level(modn):
    Phi = Phi_poly(modn)
    tot = sp.Integer(0); prod = sp.Integer(1)
    for k in range(modn):
        if k > 0:
            term = (1 - w**(k % modn)) * (1 - w**((-k) % modn))
            prod = sp.rem(sp.Poly(sp.expand(prod * term), w), Phi).as_expr()
        tot = sp.expand(tot + prod)
    return sp.rem(sp.Poly(tot, w), Phi).as_expr()

def val_p_norm(expr, modn, p):
    Phi = Phi_poly(modn)
    Pe = sp.Poly(sp.expand(expr), w)
    if Pe.is_zero:
        return 'INF'
    R = sp.Integer(sp.resultant(Phi.as_expr(), Pe.as_expr(), w))
    if R == 0:
        return 'INF'
    v = 0
    while R % p == 0:
        R //= p; v += 1
    return v

def order_of(expr, modn):
    """multiplicative order of expr mod Phi_modn, capped at modn (exact, by repeated squaring/mult)."""
    Phi = Phi_poly(modn)
    e = sp.rem(sp.Poly(sp.expand(expr), w), Phi).as_expr()
    cur = e
    for o in range(1, modn + 1):
        if sp.expand(cur - 1) == 0:
            return o
        cur = sp.rem(sp.Poly(sp.expand(cur * e), w), Phi).as_expr()
    return None

levels = [(p, r) for p in (5, 7) for r in (1, 2)]
print(f"\nFACT 3: comparison table v_p(Norm(F(xi) - sum_{{j<N}} d_j (xi-zeta_3)^j)), N=1..{NMAX}:")
all_rows = {}
for p, r in levels:
    modn = 3 * p**r
    Phi_modn = Phi_poly(modn)
    base_exp = p**r
    if base_exp % 3 != 1:
        base_exp *= 2
    x_embed = w**base_exp
    x_embed = sp.rem(sp.Poly(sp.expand(x_embed), w), Phi_modn).as_expr()
    ord_check = order_of(x_embed, modn)
    assert ord_check == 3, f"compatible zeta_3 embedding must have order 3, got {ord_check} at modn={modn}"

    d_w = [sp.rem(sp.Poly(sp.expand(dj.subs(x, x_embed)), w), Phi_modn).as_expr() for dj in d_coeffs]
    Delta = sp.rem(sp.Poly(sp.expand(w - x_embed), w), Phi_modn).as_expr()

    diffpow = {0: sp.Integer(1)}
    for j in range(1, NMAX):
        diffpow[j] = sp.rem(sp.Poly(sp.expand(diffpow[j - 1] * Delta), w), Phi_modn).as_expr()

    running = sp.Integer(0)
    S_by_N = {}
    for j in range(0, NMAX):
        running = sp.expand(running + d_w[j] * diffpow[j])
        running = sp.rem(sp.Poly(running, w), Phi_modn).as_expr()
        S_by_N[j + 1] = running

    F_w = F_at_level(modn)
    row = []
    for N in range(1, NMAX + 1):
        difN = sp.expand(F_w - S_by_N[N])
        v = val_p_norm(difN, modn, p)
        row.append(v)
    all_rows[(p, r)] = row
    print(f"  p={p}, r={r}, modn={modn} (phi={sp.totient(modn)}):  " +
          "  ".join(f"N={N}:v={v}" for N, v in zip(range(1, NMAX + 1), row)))

# ---------------------------------------------------------------------------
# Corrected-embedding gate: all four frozen rows must be coherent.
# ---------------------------------------------------------------------------
def is_numeric_row(row):
    return all(isinstance(v, int) for v in row)

numeric_rows = {k: r for k, r in all_rows.items() if is_numeric_row(r)}
assert len(numeric_rows) == len(levels), "expected every level to give a finite (non-INF) table row"

coherence_holds = all(
    all(v >= N for N, v in zip(range(1, NMAX + 1), row)) and row == sorted(row) and len(set(row)) == NMAX
    for row in numeric_rows.values()
)
print(f"\ncorrected-embedding gate: all 4 rows have v(N) >= N and strict growth: {coherence_holds}")
assert coherence_holds

print("\nFINITE CORRECTION: the compatible cube-root embedding restores coherence")
print("at levels 15, 75, 21 and 147 through Taylor order 8.")

# ---------------------------------------------------------------------------
# Conjugate-embedding control: deliberately use w^5 rather than the compatible
# w^10 at modn=15 and require memo 69's collapse through order 11.
# ---------------------------------------------------------------------------
NMAX_ROBUST = 11
K_BOUND_ROBUST = 3 * NMAX_ROBUST + 3
d_coeffs_robust = taylor_germ(NMAX_ROBUST, K_BOUND_ROBUST)

p, r = (5, 1)
modn = 3 * p**r
Phi_modn = Phi_poly(modn)
x_embed = sp.rem(sp.Poly(sp.expand(w**(p**r)), w), Phi_modn).as_expr()
d_w_robust = [sp.rem(sp.Poly(sp.expand(dj.subs(x, x_embed)), w), Phi_modn).as_expr() for dj in d_coeffs_robust]
Delta = sp.rem(sp.Poly(sp.expand(w - x_embed), w), Phi_modn).as_expr()
diffpow = {0: sp.Integer(1)}
for j in range(1, NMAX_ROBUST):
    diffpow[j] = sp.rem(sp.Poly(sp.expand(diffpow[j - 1] * Delta), w), Phi_modn).as_expr()
running = sp.Integer(0)
robust_row = []
F_w15 = F_at_level(modn)
for j in range(0, NMAX_ROBUST):
    running = sp.expand(running + d_w_robust[j] * diffpow[j])
    running = sp.rem(sp.Poly(running, w), Phi_modn).as_expr()
    difN = sp.expand(F_w15 - running)
    robust_row.append(val_p_norm(difN, modn, p))
print(f"\nconjugate-embedding control at modn=15 through N={NMAX_ROBUST}: {robust_row}")
robust_collapse = robust_row[0] == 2 and all(v == 0 for v in robust_row[1:])
print(f"memo-69 collapse reproduced under the conjugate embedding: {robust_collapse}")
assert robust_collapse

print("""
R016 PASS: B1158's corrected cube-root embedding restores the tested global
norm-valuation bound on all four frozen levels.  Memo 69's level-15 collapse
is also reproduced exactly under the conjugate embedding, so it is an
embedding artifact rather than a Taylor-truncation artifact.  The universal
all-level transport claim and normalized single-prime local valuation are
not proved by this finite certificate.  No physical quantity or
Standard-Model inference is involved.""")
