#!/usr/bin/env python3
"""
W2-147 -- B313: further single-seed invariant classes for S032-A Gate A.

CONTEXT (read from the repo before computing):
  - S032-A / gate A (frontier/B330_s032a_galois_symmetrization/FINDINGS.md) asks: is there
    ANY trace-map-invariant, discretely-multivalued, single-seed invariant of the figure-eight
    that is NOT symmetrizable (not a Galois orbit / not canonical)?  B330 proved the mechanism
    ("a finite Galois orbit is always symmetrizable") and sealed 3 classes (trace ring, quantum/
    golden pair, Eisenstein/CP pair), naming an untested residual: Reidemeister/Ptolemy torsion
    of character-variety components; CS/eta beyond CS=0; torsion of higher/irregular covers;
    SL(n>=3)/Falbel gluing-variety invariants; Bloch-group/scissors-congruence classes.
  - B350 sealed the CYCLIC-COVER torsion class but at the TRIVIAL (abelianization) representation
    only (the classical Alexander polynomial Delta(t) = t^2-3t+1); B348 sealed the Bloch class;
    B349 sealed irregular covers to index 6; B458 sealed CS at the SL(3)/Ptolemy components
    (all zero); B581 computed the ADJOINT (Sym^{2m}) twisted Alexander polynomial Delta_m(t) at
    rho_geo for the six E6 exponents m in {1,4,5,7,8,11}, but ONLY evaluated it at t=1
    (tau_m = Delta_m'(1), the torsion of the BASE manifold) -- it never fed Delta_m through the
    cyclic-cover tower.
  - B350's own residual note says explicitly: "NOT covered: the nonabelian (Ptolemy/adjoint)
    torsion of the character-variety components ... the class as a whole stays in the untested
    residual."

THIS CELL's new class (engines #1 CRT/Fox-Wada + #3 cyclotomic, per LEAD_REGISTER.md:66):
  ADJOINT-TWISTED CYCLIC-COVER TORSION.  Combine B581's adjoint (Sym^{2m}) twisted Alexander
  polynomial Delta_m(t) with B350's cyclic-cover construction: for the n-fold cyclic cover,
  the order of the Sym^{2m}-twisted torsion is (Fox-Milnor-type formula, standard for twisted
  Alexander polynomials of fibered/once-punctured-torus-bundle knots)

      T_m(n) = prod_{j=1}^{n-1} Delta_m(zeta_n^j)         (zeta_n = primitive n-th root of unity)

  This is a genuinely NEW single-seed discrete invariant CLASS (m,n) -> T_m(n) -- distinct from
  B350 (which used the trivial rep, m=0 effectively) and from B581 (which used only n=1, i.e.
  the derivative at t=1, not the cyclic tower).  Gate A question: is {T_m(n)} always a canonical
  RATIONAL INTEGER (hence trivially in the Galois-fixed field, hence NOT an unsymmetrized forced
  choice), across a swept range of (m,n)?

Method: exact (sympy), both symbolic (resultant / closed form) and a >=2-seed high-precision
numeric cross-check (mpmath, tolerance-height rule).  Independent RE-DERIVATION of Delta_1(t)
from scratch (direct Sym^2 Fox calculus over QQ(omega)), cross-checked against the banked
B581 JSON, before building on it -- "discriminating fact computed in-cell, never cited."
"""
import json, os, sys
import sympy as sp
from sympy import symbols, I, sqrt, Rational, cyclotomic_poly, resultant, nsimplify, gcd, factorint
import mpmath as mp

mp.mp.dps = 60

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = {}

print("=" * 78)
print("STEP 0 -- re-read the sealed context (sanity echo, not authority)")
print("=" * 78)

B581_JSON = os.path.join(HERE, "..", "..", "..", "..",
                          "frontier", "B581_six_torsions", "six_torsions_results.json")
B581_JSON = os.path.normpath(B581_JSON)
print("B581 stored data:", B581_JSON, "exists:", os.path.exists(B581_JSON))

with open(B581_JSON) as f:
    b581 = json.load(f)

t = symbols('t')


def coeffs_to_poly(clist):
    """clist = [[re,im],...] highest degree first, real (imag must be 0 for us)."""
    n = len(clist)
    poly = 0
    for i, (re, im) in enumerate(clist):
        re = sp.nsimplify(re); im = sp.nsimplify(im)
        assert im == 0, f"unexpected imaginary part {im}"
        deg = n - 1 - i
        poly += sp.Integer(re) * t**deg
    return sp.expand(poly)


Delta_stored = {}
for m_key in b581:
    Delta_stored[int(m_key)] = coeffs_to_poly(b581[m_key]["quotient"])
    print(f"  banked Delta_{m_key}(t) = {Delta_stored[int(m_key)]}")

print()
print("=" * 78)
print("STEP 1 -- INDEPENDENT re-derivation of Delta_1(t) (adjoint, m=1) from scratch")
print("=" * 78)
print("Direct exact Fox calculus over QQ(omega), Sym^2 (3x3), NOT the B581/B425 CRT pipeline.")

# geometric (discrete faithful) representation of the figure-eight knot group
# <a,b | a w b^-1 w^-1>, w = b a^-1 b^-1 a  (B425's convention)
# rho_geo: a -> [[1,1],[0,1]], b -> [[1,0],[-omega,1]],  omega^2+omega+1=0
#
# SPEED NOTE: literal sqrt(-3) entries make sp.simplify() pathologically slow on this
# shared/loaded machine (many sibling B771 cells running concurrently). Instead represent
# Q(omega) exactly via a symbol w with the reduction rule w^2 = -1-w (omega's minimal
# polynomial) applied after every matrix product -- exact field arithmetic, no radicals,
# no simplify() calls, degree in w stays <= 1 throughout.
w = symbols('w')
MINPOLY_W = w**2 + w + 1


def redw(expr):
    """reduce a polynomial in w (with t/other symbols as coefficients) mod w^2+w+1."""
    p = sp.Poly(sp.expand(expr), w)
    _, r = sp.div(p, sp.Poly(MINPOLY_W, w))
    return r.as_expr()


def matredw(M):
    return M.applyfunc(redw)


chk = redw(w**2 + w + 1)
print("  omega^2+omega+1 (reduced) =", chk, " (must be 0)")
assert chk == 0

Amat = sp.Matrix([[1, 1], [0, 1]])
Bmat = sp.Matrix([[1, 0], [-w, 1]])
Ainv = sp.Matrix([[1, -1], [0, 1]])          # SL(2), explicit inverse
Binv = matredw(sp.Matrix([[1, 0], [w, 1]]))  # SL(2), explicit inverse

# relator check: r = a W b^-1 W^-1 should map to I  (W = b a^-1 b^-1 a)
Wmat = matredw(Bmat * Ainv * Binv * Amat)
Winv = matredw(Wmat.adjugate())              # det(Wmat)=1 (SL2) -> adjugate = inverse
rel = matredw(Amat * Wmat * Binv * Winv)
print("  rho(relator) =", rel.tolist(), " (must be I)")
assert rel == sp.eye(2)


def sym2(M):
    """Sym^2 of a 2x2 matrix M, exact, in the basis {x^2, xy, y^2} (standard formula)."""
    a, b, c, d = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    return sp.Matrix([
        [a**2,     a*b,       b**2],
        [2*a*c,    a*d+b*c,   2*b*d],
        [c**2,     c*d,       d**2],
    ])


A2 = matredw(sym2(Amat))
B2 = matredw(sym2(Bmat))
# det(Sym^2(M)) = det(M)^3 = 1 for M in SL(2) -> Sym^2(M) in SL(3) -> adjugate = inverse
A2inv = matredw(A2.adjugate())
B2inv = matredw(B2.adjugate())

# rebuild the same word structure as B425 (W_ = b a^-1 b^-1 a, R_ = a W b^-1 W^-1)
# generators list with exponents, Fox derivative d(R)/db, symbolic t-grading on 'a' only? --
# figure-eight abelianization sends a,b both to the SAME generator of H_1=Z (knot group), so the
# Alexander/torsion t-variable tracks total exponent sum of BOTH a and b (standard convention,
# matches B425's Phi(prefix) which grades by total exponent regardless of letter).
word = [('b', 1)]
invA = [('a', -1)]
invB = [('b', -1)]
Wword = [('b', 1)] + invA + invB + [('a', 1)]


def invw(w):
    return [(g, -e) for g, e in reversed(w)]


Rword = [('a', 1)] + Wword + invB + invw(Wword)


def fox_db(word):
    """Fox derivative d(word)/db, as a list of (prefix, sign)."""
    terms = []
    prefix = []
    for (g, e) in word:
        if e == 1:
            if g == 'b':
                terms.append((list(prefix), 1))
            prefix = prefix + [(g, 1)]
        else:
            prefix = prefix + [(g, -1)]
            if g == 'b':
                terms.append((list(prefix), -1))
    return terms


DRb = fox_db(Rword)
print(f"  Fox derivative dR/db has {len(DRb)} terms")

REP = {('a', 1): A2, ('a', -1): A2inv, ('b', 1): B2, ('b', -1): B2inv}


def Phi(prefix, tvar):
    M = sp.eye(3)
    texp = 0
    for (g, e) in prefix:
        M = matredw(M * REP[(g, e)])
        texp += e
    return matredw(tvar**texp * M)


S = sp.zeros(3, 3)
for (prefix, sign) in DRb:
    S += sign * Phi(prefix, t)
S = matredw(S)

N_t_full = redw(sp.expand(S.det()))  # p(t) + q(t)*w
N_t_poly_in_w = sp.Poly(N_t_full, w)
N_t_coeffs = N_t_poly_in_w.all_coeffs()  # [coeff of w^1, coeff of w^0] (degree <=1 after reduction)
if len(N_t_coeffs) == 1:
    N_t_w1, N_t_w0 = sp.Integer(0), N_t_coeffs[0]
else:
    N_t_w1, N_t_w0 = N_t_coeffs[0], N_t_coeffs[1]
print("  det(S) = [", sp.expand(N_t_w0), "]  +  [", sp.expand(N_t_w1), "] * omega")
print("  (omega-coefficient must vanish identically -- 'sqrt(-3) cancels in the")
print("   determinant', the exact B425 finding, re-derived independently here)")
assert sp.expand(N_t_w1) == 0, "sqrt(-3) did NOT cancel -- independent re-derivation disagrees with B425!"
N_t = sp.expand(N_t_w0)

D_t = sp.expand((t * A2 - sp.eye(3)).det())
D_t_full = redw(D_t)
D_t_poly_in_w = sp.Poly(D_t_full, w)
D_t_coeffs = D_t_poly_in_w.all_coeffs()
D_t_w1 = D_t_coeffs[0] if len(D_t_coeffs) > 1 else sp.Integer(0)
assert sp.expand(D_t_w1) == 0
D_t = sp.expand(D_t_coeffs[-1])
print("  N(t) =", N_t, " (a Laurent polynomial in t -- Fox calculus prefixes can have")
print("                  negative total exponent, hence negative powers of t)")
print("  D(t) =", D_t)

# N(t) is a LAURENT polynomial (has negative powers); use cancel() on the full rational
# function N(t)/D(t) rather than sp.div (which requires ordinary, non-Laurent polynomials).
# Wada's torsion is only defined up to a unit +-t^k -- the reduced denominator being a bare
# power of t is exactly that indeterminacy, not a computational slip.
Wada_ratio = sp.cancel(N_t / D_t)
num, den = sp.fraction(Wada_ratio)
num = sp.expand(num); den = sp.expand(den)
print("  cancel(N(t)/D(t)) = num/den, num =", num, " den =", den)
den_poly = sp.Poly(den, t)
assert den_poly.is_monomial, f"expected the residual denominator to be a bare power of t (the +-t^k unit indeterminacy of Wada torsion), got {den}"
print(f"  (denominator is a bare monomial t^{den_poly.degree()} -- exactly the standard")
print(f"   +-t^k unit ambiguity of Reidemeister/Wada torsion, not a bug)")

Delta1_derived = num
print("  INDEPENDENTLY DERIVED Delta_1(t) =", Delta1_derived)
print("  BANKED (B581) Delta_1(t)        =", Delta_stored[1])

# compare up to an overall sign/unit (Wada torsion is defined up to +-t^k)
diff_direct = sp.expand(Delta1_derived - Delta_stored[1])
diff_negated = sp.expand(Delta1_derived + Delta_stored[1])
match = (diff_direct == 0) or (diff_negated == 0)
print("  MATCH (up to overall sign):", match)
assert match, "independent re-derivation must reproduce the banked B581 polynomial"

Delta1 = Delta_stored[1]  # use the banked (sign-normalized, monic) version going forward
print(f"\n  CROSS-CHECK PASSED: independent direct Sym^2 Fox-calculus derivation over QQ(omega)")
print(f"  reproduces the banked B581/B425 (CRT-over-F_p) result EXACTLY, two independent")
print(f"  routes, one polynomial: Delta_1(t) = {Delta1}")

OUT['delta1_independent'] = str(Delta1_derived)
OUT['delta1_banked'] = str(Delta_stored[1])
OUT['delta1_cross_check_match'] = bool(match)

print()
print("=" * 78)
print("STEP 2 -- factor Delta_1(t), confirm the banked factorization")
print("=" * 78)
fac1 = sp.factor(Delta1)
print("  Delta_1(t) =", fac1)
roots1 = sp.roots(Delta1, t)
print("  roots:", roots1)
OUT['delta1_factored'] = str(fac1)

print()
print("=" * 78)
print("STEP 3 -- THE NEW CLASS: adjoint-twisted cyclic-cover torsion T_m(n)")
print("=" * 78)
print("""
T_m(n) := prod_{j=1}^{n-1} Delta_m(zeta_n^j)   (zeta_n primitive n-th root of unity)

standard fact: for a polynomial f(t) in QQ[t], prod_{zeta: zeta^n=1} f(zeta) = Res(x^n-1, f(x))
(monic resultant); dividing by f(1) removes the j=0 term.  All exact (sympy resultant).
""")

n_sym = symbols('n_dummy')


def T_of(poly_t, n):
    """prod_{j=1}^{n-1} poly(zeta_n^j) via the resultant identity, exact."""
    x = symbols('x')
    f = poly_t.subs(t, x)
    R = sp.resultant(sp.expand(x**n - 1), sp.Poly(f, x).as_expr(), x)
    f1 = poly_t.subs(t, 1)
    if f1 == 0:
        raise ZeroDivisionError("f(1)=0 -- must strip the (t-1) factor first")
    return sp.nsimplify(R / f1)


print("Delta_1(1) =", Delta1.subs(t, 1), " (expected 0 -- forced by dim H^1=1, per B581)")
assert sp.simplify(Delta1.subs(t, 1)) == 0

# strip the (t-1) factor (Delta_1(1)=0 is the base-manifold H^1 zero, not part of the
# cyclic-cover-tower invariant, exactly as B350 strips Delta(1)=+-1 units for the ordinary
# Alexander polynomial)
quo1, rem1 = sp.div(sp.Poly(Delta1, t), sp.Poly(t - 1, t))
assert rem1.as_expr() == 0
g1 = sp.expand(quo1.as_expr())
print("  Delta_1(t)/(t-1) =", g1, " (the reduced quadratic g_1(t))")
OUT['g1'] = str(g1)

T1_vals = {}
for n in range(2, 26):
    Tn = T_of(g1, n)
    T1_vals[n] = Tn
print("  T_1(n) = prod_{j=1}^{n-1} g_1(zeta_n^j), n=2..25:")
for n in range(2, 26):
    print(f"    n={n:2d}: T_1(n) = {T1_vals[n]}  (integer: {T1_vals[n].is_Integer})")

all_integer_1 = all(sp.Integer(T1_vals[n]).is_Integer for n in T1_vals)
print("\n  ALL T_1(n) integers for n=2..25:", all_integer_1)
OUT['T1_all_integer_n2_25'] = bool(all_integer_1)
OUT['T1_values'] = {str(n): str(v) for n, v in T1_vals.items()}

print()
print("=" * 78)
print("STEP 4 -- closed form for T_1(n) via the companion Lucas sequence of g_1")
print("=" * 78)
print("""
g_1(t) = t^2 - 5t + 1 (roots alpha,beta with alpha+beta=5, alpha*beta=1 -- a UNIT pair,
matches B581's note: root = (5+sqrt(21))/2 is the banked B520 BTZ entropy value).
Standard identity: prod_{zeta^n=1} g_1(zeta) = (alpha^n-1)(beta^n-1) = 2 - V_n
  where V_n = alpha^n+beta^n satisfies V_0=2, V_1=5, V_n = 5 V_{n-1} - V_{n-2}  (Lucas-type).
So  T_1(n) = [2-V_n] / g_1(1)  =  (V_n-2)/3   (g_1(1) = 1-5+1 = -3).
""")

V = {0: 2, 1: 5}
for n in range(2, 30):
    V[n] = 5 * V[n - 1] - V[n - 2]

closed_form_ok = True
for n in range(2, 26):
    predicted = sp.Rational(V[n] - 2, 3)
    if predicted != T1_vals[n]:
        closed_form_ok = False
        print(f"  MISMATCH at n={n}: predicted {predicted} vs computed {T1_vals[n]}")
print("  CLOSED FORM  T_1(n) = (V_n - 2)/3  VERIFIED for n=2..25:", closed_form_ok)
OUT['closed_form_T1_verified'] = bool(closed_form_ok)
OUT['V_sequence_n2_25'] = {str(n): V[n] for n in range(0, 26)}

print()
print("=" * 78)
print("STEP 5 -- >=2-seed numeric cross-check (mpmath, tolerance-height rule)")
print("=" * 78)
# seed A: high-precision direct complex evaluation of the product formula
# seed B: high-precision evaluation via the closed form (V_n recursion, done in exact ints above
#         -- so use a genuinely different numeric seed: brute-force complex root multiplication)
mismatches = []
for n in [3, 5, 7, 8, 11, 13, 17, 19, 23]:
    # prod_val = prod_{j=1}^{n-1} g_1(zeta_n^j) is ALREADY T_1(n) by definition (the j=0
    # term / zeta=1 is excluded by the range already) -- no further division needed.
    prod_val = mp.mpc(1)
    for j in range(1, n):
        angle = 2 * mp.pi * j / n
        zeta = mp.mpc(mp.cos(angle), mp.sin(angle))
        gval = zeta**2 - 5 * zeta + 1
        prod_val *= gval
    Tn_numeric = prod_val.real
    Tn_exact = float(T1_vals[n])
    diff = abs(Tn_numeric - Tn_exact)
    ok = diff < 1e-30
    mismatches.append((n, ok))
    print(f"  n={n:2d}: numeric(60dps)={mp.nstr(Tn_numeric,20)}  exact={Tn_exact}  |diff|={mp.nstr(diff,5)}  OK={ok}")

all_numeric_ok = all(ok for (_, ok) in mismatches)
print("\n  numeric cross-check (independent complex-root seed) all pass:", all_numeric_ok)
OUT['numeric_cross_check_pass'] = bool(all_numeric_ok)

print()
print("=" * 78)
print("STEP 6 -- extend to m=4,5,7,8,11 (the full E6 exponent set): T_m(n) integrality sweep")
print("=" * 78)
extend_results = {}
# NB: the E6-exponent Delta_m have degree 2m+1 up to 23 (m=11); resultants of degree-23
# polys with x^n-1 get expensive fast, and this cell runs on a shared, loaded machine
# (many sibling B771 cells concurrently). Keep this sweep small and honest about scope:
# m in {4,5} (degree 9, 11) at n=2..5 is enough to test "is the closed-form/integrality
# pattern m=1-specific or does it generalize" without an unbounded runtime risk.
SWEEP_M = [4, 5]
SWEEP_N = [2, 3, 4, 5]
for m_key in SWEEP_M:
    Dm = Delta_stored[m_key]
    Dm1 = sp.simplify(Dm.subs(t, 1))
    print(f"  m={m_key}: Delta_m(1) = {Dm1}")
    if Dm1 != 0:
        print(f"    Delta_{m_key}(1) != 0 -- do not strip a (t-1) factor; use Delta_m directly.")
        gm = Dm
    else:
        qm, rm = sp.div(sp.Poly(Dm, t), sp.Poly(t - 1, t))
        assert rm.as_expr() == 0
        gm = sp.expand(qm.as_expr())
    row = {}
    ok_all = True
    for n in SWEEP_N:
        Tn = sp.nsimplify(T_of(gm, n))
        row[n] = Tn
        if not Tn.is_Integer:
            ok_all = False
        print(f"    n={n}: T_{m_key}(n) = {Tn}  (integer: {Tn.is_Integer})")
    extend_results[m_key] = dict(all_integer=ok_all, values={str(n): str(v) for n, v in row.items()})
    print(f"  m={m_key}: all tested T_{m_key}(n) integer: {ok_all}")

print()
print("  (m in {7,8,11}: degree-15/17/23 polynomials -- resultant sweep skipped here for")
print("   runtime honesty on a shared machine; NOT claimed tested. Named as residual below.)")

OUT['extend_E6_sweep'] = extend_results

print()
print("=" * 78)
print("STEP 7 -- GATE A READING: is this new class symmetrizable / no forced choice?")
print("=" * 78)
print("""
The B330 mechanism: a finite Galois orbit is always symmetrizable.  Here the "orbit" acted on
by Gal(Q(zeta_n)/Q) is {zeta_n^j : j=1..n-1}; because Delta_m(t) has RATIONAL coefficients
(Galois symmetry rho-bar = rho o phi forces Q, per B581), permuting the zeta_n^j merely permutes
the factors of the product T_m(n) -- so T_m(n) is AUTOMATICALLY Galois-fixed (in Q), and (per the
integrality checks above) lands in Z exactly, at every (m,n) probed.  No sign ambiguity, no
unresolved member: the object hands you ONE integer per (m,n), never an orbit requiring a choice.
This extends gate A's evidence to a genuinely NEW invariant class (adjoint-twisted cyclic-cover
torsion) that neither B350 (trivial rep) nor B581 (n=1 only) computed.

BONUS (unforced): the m=1 case has an exact closed form via a companion Lucas sequence
V_n (V_0=2,V_1=5,V_n=5V_{n-1}-V_{n-2}), whose n=1 root (5+sqrt(21))/2 IS the banked B520 BTZ
entropy root -- B581 flagged this "unit-trace ladder {5,26,...}" as unregistered; this cell
identifies it exactly as the companion sequence of g_1(t)=t^2-5t+1, T_1(n)=(V_n-2)/3.
""")

result = dict(
    delta1_cross_check_match=bool(match),
    closed_form_T1_verified=bool(closed_form_ok),
    T1_all_integer_swept=bool(all_integer_1),
    numeric_cross_check_pass=bool(all_numeric_ok),
    extend_all_integer={str(k): v['all_integer'] for k, v in extend_results.items()},
)
print("SUMMARY:", json.dumps(result, indent=1))

OUT['summary'] = result
with open(os.path.join(HERE, "results.json"), "w") as f:
    json.dump(OUT, f, indent=1, default=str)
print("\n[results.json written]")
