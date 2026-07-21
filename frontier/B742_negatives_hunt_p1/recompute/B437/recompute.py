"""B739 Stage-B recompute -- target B437 (banked negative, ground=dead-probe).

BANKED KILL (Stage-A record): "'The golden return' as INHERITANCE: the child's Q(sqrt5)
abelian floor is numerator-forced (every knot at slope 5 gives Z/5 -> zeta_5 -> sqrt5),
not the parent's golden memory -- retracted by the trefoil control."

THE DISCRIMINATING FACT (the fact that, if true, kills the inheritance claim):
  Trefoil(5,1): Tr_{Q(zeta5)/Q(sqrt5)} tau = 1 - sqrt(5)/5 -- the SAME field Q(sqrt5)
  as the figure-eight child's 3 + sqrt(5)/5, from a parent with NO golden Alexander data
  (trefoil roots are primitive 6th roots of unity, not phi^{+-2}).
The arc's own script (abelian_book.py) computes ONLY the 4_1 trace; the trefoil control
is asserted in the FINDINGS CORRECTION but never computed there (fact_basis=asserted).
Here we RE-DERIVE it, plus both E19 directions:
  (i)  the trefoil trace genuinely involves sqrt5 (irrational -- else the control fails
       and the kill would NOT be discriminating);
  (ii) the field-landing is fully generic: for an ARBITRARY numerator (symbolic residue
       mod Phi_5, covering every knot's Alexander polynomial), the trace lies in
       Q(sqrt5) = Q(zeta5)^+ -- the "numerator-forced / every knot at slope 5" theorem;
  (iii) the VALUES differ (121 vs 1 total torsion; 3+sqrt5/5 vs 1-sqrt5/5), i.e. what
       survives as parent-specific is the value, exactly as the corrected FINDINGS says.

CONVENTIONS (from the original arc, abelian_book.py, re-declared; E1 notes marked *):
  - Surgery formula for slope (5,1): tau_j = Delta(zeta5^j)/(zeta5^j - 1)^2 (q=1, so both
    denominator factors are (zeta-1)); characters j=1..4 on H1 = Z/5.
  - H1(S^3_{5/1}(K)) = Z/5 for EVERY knot K (standard surgery homology, |H1| = |p| = 5):
    the character field Q(zeta5) is slope-forced. (Theorem, not recomputed.)
  - Trace to the real subfield = tau + sigma_4(tau), sigma_4: zeta -> zeta^4 (complex
    conjugation); basis identity w = zeta + zeta^4 = (-1+sqrt5)/2, zeta^2+zeta^3 = -1-w,
    sqrt5 > 0 (real embedding) -- all as in the arc's golden_trace().
  - Delta_{4_1}(t) = t^2 - 3t + 1 (the arc's declared representative).
  * Delta_{3_1}(t) = t^2 - t + 1: UNDECLARED in the arc (E1 choice) -- we take the same
    normalization class as the arc's 4_1 representative (monic quadratic, Delta(0)=1;
    Alexander polynomials are defined up to +-t^k). Its roots are the primitive 6th
    roots of unity, matching the FINDINGS' remark "the trefoil's are 6th roots of unity".
  * Genericity controls (supporting only, computed in-sandbox, not cited): Delta_{5_2} =
    2t^2 - 3t + 2, Delta_{6_1} = 2t^2 - 5t + 2 (standard tables), unknot Delta = 1.

Deterministic: exact sympy arithmetic mod Phi_5 + fixed numeric crosscheck (no clocks,
no randomness, no network).
"""
import cmath
import sympy as sp

t = sp.Symbol('t')
PHI5 = sp.Poly(sum(t**k for k in range(5)), t)           # Phi_5 = 1+t+t^2+t^3+t^4
SQRT5 = sp.sqrt(5)
W = (-1 + SQRT5) / 2                                     # zeta + zeta^4

INV_DEN = sp.invert(sp.Poly((t - 1)**2, t), PHI5)        # ((t-1)^2)^{-1} mod Phi_5


def trace_exact(Delta_expr):
    """Tr_{Q(zeta5)/Q(sqrt5)} of tau = Delta/(t-1)^2 mod Phi_5, exact.

    Returns (value, a, b) with value = a + b*sqrt5, a,b in Q.
    Follows the arc's golden_trace() step for step, generalized to any Delta.
    """
    tau = sp.rem(sp.expand(Delta_expr * INV_DEN.as_expr()), PHI5.as_expr(), t)
    s4 = sp.rem(sp.expand(tau.subs(t, t**4)), PHI5.as_expr(), t)
    half = sp.rem(sp.expand(tau + s4), PHI5.as_expr(), t)
    p = sp.Poly(half, t)
    h = p.all_coeffs()[::-1]
    h = list(h) + [sp.Integer(0)] * (4 - len(h))
    # Galois-invariant under sigma_4 in the power basis <=> h1 = 0 and h2 = h3:
    assert sp.simplify(h[1]) == 0 and sp.simplify(h[2] - h[3]) == 0, \
        "trace not sigma_4-invariant -- convention error"
    val = sp.simplify(h[0] + h[2] * (-1 - W))
    b = sp.simplify((val - val.subs(SQRT5, -SQRT5)) / (2 * SQRT5))
    a = sp.simplify(val - b * SQRT5)
    return val, a, b


def trace_numeric(Delta_expr):
    """Numeric crosscheck: tau(zeta) + tau(zeta^4) at zeta = e^{2 pi i/5}."""
    z = cmath.exp(2j * cmath.pi / 5)
    f = sp.lambdify(t, Delta_expr, "math")

    def tau(j):
        zj = z**j
        return complex(f(zj)) / (zj - 1)**2
    return tau(1) + tau(4)


def total_torsion(Delta_expr, p=5):
    """|Res(Phi_p, Delta)| = prod_j |Delta(zeta_p^j)| -- the arc's 'total'."""
    Phi = sum(t**k for k in range(p))
    return abs(int(sp.resultant(Phi, Delta_expr, t)))


def report(name, Delta_expr):
    val, a, b = trace_exact(Delta_expr)
    num = trace_numeric(Delta_expr)
    assert abs(float(val) - num.real) < 1e-12 and abs(num.imag) < 1e-12, \
        f"numeric crosscheck FAILED for {name}"
    tot = total_torsion(Delta_expr)
    print(f"{name}: Delta = {sp.expand(Delta_expr)}")
    print(f"  trace = {val} = ({a}) + ({b})*sqrt5   [numeric {float(val):.12f}, ok]")
    print(f"  in Q(sqrt5): yes (exact);  sqrt5-part nonzero: {b != 0}")
    print(f"  total torsion |Res(Phi_5, Delta)| = {tot}")
    return val, a, b, tot


print("=" * 72)
print("B739 Stage-B recompute of B437's discriminating fact (the trefoil control)")
print("=" * 72)

# -- Step 0: the field identity Q(zeta5)^+ = Q(sqrt5) (the 'zeta5 -> sqrt5' link) --
mp = sp.minimal_polynomial(2 * sp.cos(2 * sp.pi / 5), t)   # min poly of zeta+zeta^4
print(f"\n[0] min poly of zeta5 + zeta5^4 over Q: {mp}  (degree 2, disc "
      f"{sp.discriminant(mp, t)}) => Q(zeta5)^+ = Q(sqrt5).  w = (-1+sqrt5)/2: "
      f"{sp.simplify(mp.subs(t, W)) == 0}")
assert mp == t**2 + t - 1 and sp.simplify(mp.subs(t, W)) == 0

# -- Step 1: reconfirm the arc's own 4_1 computation (baseline) --
print("\n[1] BASELINE (the arc's own computation, re-derived):")
v41, a41, b41, tot41 = report("figure-eight 4_1(5,1)", t**2 - 3*t + 1)
assert sp.simplify(v41 - (3 + SQRT5/5)) == 0, "4_1 baseline mismatch"
assert tot41 == 121, "4_1 total (Lucas L_5^2) mismatch"

# -- Step 2: THE DISCRIMINATING FACT -- the trefoil control, computed (not cited) --
print("\n[2] THE TREFOIL CONTROL (the kill's discriminating fact, asserted-only in arc):")
v31, a31, b31, tot31 = report("trefoil 3_1(5,1)", t**2 - t + 1)
print(f"  banked assertion 'trace = 1 - sqrt5/5': "
      f"{sp.simplify(v31 - (1 - SQRT5/5)) == 0}")
assert sp.simplify(v31 - (1 - SQRT5/5)) == 0, "banked trefoil value REFUTED"
# E19 direction check: the control only kills if the trefoil trace GENUINELY needs sqrt5
assert b31 != 0, "trefoil trace rational -- control would NOT show the field is shared"
assert tot31 == 1, "trefoil total mismatch (FINDINGS: 'trefoil -> 1')"
# trefoil roots: primitive 6th roots of unity, NOT golden
r = sp.roots(t**2 - t + 1, t)
assert all(sp.simplify(x**6 - 1) == 0 and sp.simplify(x**2 - 1) != 0 for x in r)
print("  trefoil Delta roots are primitive 6th roots of unity (non-golden parent): True")

# -- Step 3: same field, different value (what kills inheritance, what survives) --
print("\n[3] SAME FIELD, DIFFERENT VALUE:")
print(f"  4_1 trace  = {v41}  (sqrt5-part {b41})")
print(f"  3_1 trace  = {v31}  (sqrt5-part {b31})")
print(f"  same field Q(sqrt5), both irrational: {b41 != 0 and b31 != 0}")
print(f"  values differ (parent-specific residue): {sp.simplify(v41 - v31) != 0}")
assert sp.simplify(v41 - v31) != 0

# -- Step 4: numerator-forced for EVERY knot (symbolic residue mod Phi_5) --
# Any Delta_K reduces mod Phi_5 to c0 + c1 t + c2 t^2 + c3 t^3, c_i in Q. Show the
# trace lands in Q(sqrt5) IDENTICALLY in (c0,c1,c2,c3): the field needs NO input
# from the parent at all -- it is a theorem about the integer 5.
c0, c1, c2, c3 = sp.symbols('c0 c1 c2 c3', rational=True)
vg, ag, bg = trace_exact(c0 + c1*t + c2*t**2 + c3*t**3)
print("\n[4] GENERIC NUMERATOR (every knot at slope 5), trace = a + b*sqrt5 with")
print(f"    a = {sp.nsimplify(sp.expand(ag))}")
print(f"    b = {sp.nsimplify(sp.expand(bg))}")
print("    -> lies in Q(sqrt5) for ALL (c0,c1,c2,c3): numerator-forced. QED")
# spot-checks of the general formula against steps 1-2:
assert sp.simplify(vg.subs({c0: 1, c1: -3, c2: 1, c3: 0}) - v41) == 0
assert sp.simplify(vg.subs({c0: 1, c1: -1, c2: 1, c3: 0}) - v31) == 0

# -- Step 5: supporting genericity table (in-sandbox, standard Delta tables) --
print("\n[5] SUPPORTING CONTROLS (same slope, other parents -- all land in Q(sqrt5)):")
for name, D in [("unknot(5,1) = L(5,1)", sp.Integer(1)),
                ("5_2(5,1)", 2*t**2 - 3*t + 2),
                ("6_1(5,1)", 2*t**2 - 5*t + 2)]:
    report(name, D)

print("\n" + "=" * 72)
print("VERDICT INPUT: trefoil(5,1) trace = 1 - sqrt(5)/5 in Q(sqrt5) -- RECOMPUTED,")
print("matches the banked kill record verbatim; the field Q(sqrt5) is proven")
print("numerator-forced for arbitrary Delta (step 4). The banked kill STANDS.")
print("=" * 72)
