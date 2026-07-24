#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B774 Stage B chord cell  CP-A5-molien
=====================================
THE theta-ODD twisted-character Molien / q-series 5-adic test.

SOURCE NEGATIVE (banked): LAW_MAP row "THE 5-ADIC EXCLUSION" (generation leg).
  The W2 Molien kill (B685 / w2_step3/STEP3_VERDICT.md, PREREG_W2 sha b4c9a6bb):
  ANY finite-order operator's Molien / twisted character is ALGEBRAIC-INTEGRAL
  (its graded coefficients are traces on Sym^n V = sums of products of roots of
  unity, hence algebraic integers => 5-adically integral, v5 >= 0). The banked
  target streams F1,F2 = N_i (q;q)^{-3/5} carry pure 5-power DENOMINATORS with
  v5(denom) = 1, 12, 49, 99, 146 at n = 1,10,40,80,119 (unboundedly growing).
  An algebraic-integral series can never match a series with growing 5-power
  denominators => the whole finite-order class dies at once, decided at n <= 1.
  ==> generation leg CLOSED (theta-EVEN / abelianized level).

THE CHORD ANALOG (this cell): compute the theta-ODD twisted-character Molien
  series DIRECTLY on a GENUINELY NON-ABELIAN object and test 5-adic integrality.
  Hope: a non-abelian twisted character need NOT inherit the algebraic-
  integrality; if the theta-odd series is NOT 5-adically integral the exclusion
  would be projection-specific (an OVERTURN / RESOLVED-A candidate).

  Chord-pass discipline (prereg a2cb971a + the W3-082c lesson):
    * compute the theta-odd analog IN-CELL, never cite;
    * a chord-POSITIVE must be a GENUINE non-abelian/theta-odd object, NOT a
      finer abelian/character invariant relabeled. A twisted character IS a
      character sum; if the quantity is expressible as an ordinary
      character/trace polynomial it is NOT a genuine chord positive.
    * the W4-304 real-overturn signature = a par/trace ZERO that decomposes as
      even == odd CANCELLATION with a NONZERO theta-odd piece (exhibit it).

TWO structurally-different in-cell paths:
  PATH 1  (arc's abelian doublet, faithful to W2): the golden rotation
          W = sigma(A1) (order 10, eig zeta10^{+-1}) Molien doublet M, M' and
          the theta-odd antisymmetric combination (M - M')/sqrt5.
  PATH 2  (GENUINELY NON-ABELIAN): the icosahedral group A5 (order 60, its two
          3-dim irreps 3 and 3' swapped by sqrt5 |-> -sqrt5) and the TWISTED
          Molien series with the theta-odd class function chi_odd = chi_3 - chi_3'
          via Molien's averaging formula over all 5 conjugacy classes.

Env: pyenv python3 (NOT sage).  Re-runnable.  Emits output.txt + results.json.
"""

import json
import os
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
LINES = []


def log(s=""):
    print(s)
    LINES.append(s)


# ---------------------------------------------------------------------------
# Shared exact algebra over Q(sqrt5)
# ---------------------------------------------------------------------------
t = sp.symbols("t")
s5 = sp.sqrt(5)
phi = (1 + s5) / 2          # golden ratio
psi = (1 - s5) / 2          # Galois conjugate 1 - phi = -1/phi

# 5-adic valuation of a RATIONAL number (as used against the banked target).
def v5_rational(q):
    q = sp.nsimplify(q)
    q = sp.Rational(q)
    if q == 0:
        return sp.oo
    num, den = q.p, q.q
    v = 0
    while num % 5 == 0:
        num //= 5; v += 1
    while den % 5 == 0:
        den //= 5; v -= 1
    return v


# Is x an ALGEBRAIC INTEGER of Z[phi]?  x = a + b*phi with a,b in Z  <=>
# x integral over Z (minimal poly monic with integer coeffs).  For Q(sqrt5)
# elements we test: write x = p + q*sqrt5 (p,q rational); x in Z[phi] iff
# 2p in Z, 2q in Z and 2p, 2q same parity (the ring of integers O_{Q(sqrt5)}).
def in_Zphi(x):
    x = sp.expand(sp.nsimplify(x))
    p = sp.simplify((x + x.subs(s5, -s5)) / 2)     # rational part
    q = sp.simplify((x - x.subs(s5, -s5)) / (2 * s5))  # sqrt5 coefficient
    p2, q2 = sp.nsimplify(2 * p), sp.nsimplify(2 * q)
    if not (p2.is_Integer and q2.is_Integer):
        return False, (p, q)
    return ((int(p2) - int(q2)) % 2 == 0), (p, q)


# For an ALGEBRAIC-INTEGER element of Z[phi] its 5-adic valuation (in the
# unramified/inert prime above 5 -- actually 5 = -sqrt5^2 is RAMIFIED in
# Q(sqrt5), (sqrt5) is the prime over 5).  What the banked exclusion needs is
# only: an algebraic integer has NON-NEGATIVE valuation at EVERY prime, so it
# can never contribute a DENOMINATOR.  We report v_(sqrt5)(x) for the ramified
# prime; the field norm gives v5.  For the HARDENS test the only thing that
# matters is "denominator present?" => integrality.
def v_sqrt5(x):
    # valuation at the ramified prime (sqrt5); v5 = v_sqrt5 / 2 on norms.
    x = sp.expand(sp.nsimplify(x))
    if sp.simplify(x) == 0:
        return sp.oo
    N = sp.simplify(sp.expand(x * x.subs(s5, -s5)))   # field norm in Q
    return v5_rational(N)   # = 2*v_sqrt5 ... but sign/denominator is what we read


# power-series coefficients of a rational function P(t)/Q(t) (Q(0)!=0) up to
# order N, via the exact linear recurrence  c_n = (P_n - sum_{k>=1} q_k c_{n-k})/q_0.
# Fast and exact over Q(sqrt5); avoids sp.series.
def series_coeffs(expr, N):
    expr = sp.together(expr)
    P, Q = sp.fraction(expr)
    Pp = sp.Poly(sp.expand(P), t)
    Qp = sp.Poly(sp.expand(Q), t)

    def pc(poly, k):
        return poly.coeff_monomial(t**k) if k <= poly.degree() else sp.Integer(0)

    q0 = pc(Qp, 0)
    assert q0 != 0, "Q(0)=0, not a proper power series"
    qdeg = Qp.degree()
    c = []
    for n in range(N + 1):
        s = pc(Pp, n)
        for k in range(1, min(n, qdeg) + 1):
            s -= pc(Qp, k) * c[n - k]
        c.append(sp.simplify(sp.expand(s / q0)))
    return c


# ===========================================================================
NCOEF = 42   # coefficients to test (target window checkpoints n=1,10,40)
# ===========================================================================

log("=" * 74)
log("B774 CP-A5-molien : theta-ODD twisted-character Molien 5-adic test")
log("=" * 74)
log("Banked negative: finite-order Molien/twisted-char is ALGEBRAIC-INTEGRAL")
log("  => 5-adically integral (v5>=0) => cannot carry the target's growing")
log("     5-power denominators v5(denom)=1,12,49,99,146 at n=1,10,40,80,119.")
log("Chord question: does the theta-ODD projection produce a NON-integral")
log("  (5-adic-denominator-bearing) series and thereby become projection-")
log("  specific?  Compute directly on a genuinely NON-ABELIAN object.")
log("")

TARGET_V5 = {1: 1, 10: 12, 40: 49, 80: 99, 119: 146}  # v5 of the DENOMINATOR
log(f"Target denominator 5-valuations (banked W33): {TARGET_V5}")
log("(POSITIVE v5(denom) = a genuine 5-power in the DENOMINATOR of reduced c_n)")
log("")

# ---------------------------------------------------------------------------
# PATH 1 : the arc's abelian golden-rotation doublet (faithful to W2 step ii)
# ---------------------------------------------------------------------------
log("-" * 74)
log("PATH 1  abelian golden-rotation doublet  W = sigma(A1), eig zeta10^{+-1}")
log("-" * 74)
# Molien factor of W on V0 = C^2 : 1/det(1 - tW) = 1/(1 - tr t + det t^2)
#   tr = phi, det = 1  ->  M(t) = 1/(1 - phi t + t^2)
# Galois conjugate seed (sqrt5 -> -sqrt5): tr = psi = 1-phi -> M'(t).
M = 1 / (1 - phi * t + t**2)
Mp = 1 / (1 - psi * t + t**2)
cM = series_coeffs(M, NCOEF)
cMp = series_coeffs(Mp, NCOEF)

# theta-EVEN  = (M + M')            (Q-valued: lands in Z)
# theta-ODD   = (M - M') / sqrt5    (the sqrt5-antisymmetric part)
theta_even = [sp.simplify(a + b) for a, b in zip(cM, cMp)]
theta_odd = [sp.simplify((a - b) / s5) for a, b in zip(cM, cMp)]

log("n :  M_n (in Z[phi])            theta-even=M+M'   theta-odd=(M-M')/sqrt5")
p1_odd_integral = True
p1_odd_v5min = sp.oo
for n in range(0, 12):
    int_flag, _ = in_Zphi(cM[n])
    oe = theta_even[n]
    oo_ = theta_odd[n]
    # theta-odd is Q-valued: test its 5-adic valuation directly
    voo = v5_rational(oo_) if oo_ != 0 else sp.oo
    if oo_ != 0:
        p1_odd_v5min = min(p1_odd_v5min, voo)
    is_int = (sp.nsimplify(oo_).is_Integer)
    p1_odd_integral = p1_odd_integral and bool(is_int)
    log(f"{n:2d}: {str(cM[n]):26s} even={str(oe):8s} odd={str(oo_):6s} "
        f"v5(odd)={voo} Z[phi]?{int_flag} oddInt?{is_int}")

log("")
log(f"PATH 1 verdict: theta-odd coefficients ALL integers = {p1_odd_integral}; "
    f"min v5(theta-odd) = {p1_odd_v5min} (>=0 => NO denominator).")
log("  => matches the banked diagnostic (STEP3_VERDICT pt.4: (M-M')/sqrt5 gives")
log("     integers -2,...). theta-odd HARDENS at the abelian level.")
log("  NOTE: (M-M')/sqrt5 is a linear combo of two TRACES => a character")
log("  polynomial => NOT a genuine chord object (the W3-082c trap).")
log("")

# ---------------------------------------------------------------------------
# PATH 2 : GENUINELY NON-ABELIAN  --  A5 twisted Molien, theta-odd class fn
# ---------------------------------------------------------------------------
log("-" * 74)
log("PATH 2  GENUINELY NON-ABELIAN : A5 icosahedral, TWISTED Molien series")
log("-" * 74)
log("A5 (order 60). Conjugacy classes [size]: 1[1], (2,2)[15], (3)[20],")
log("  (5a)[12], (5b)[12].  The 3-dim icosahedral rotation rep rho:")
log("  eigenvalues of rho(g) per class (roots of unity):")
log("    1  : (1,1,1)                       det(1-t rho)=(1-t)^3")
log("    2  : (1,-1,-1)                      =(1-t)(1+t)^2")
log("    3  : (1, w, w^2)                    =(1-t)(1+t+t^2)")
log("    5a : (1, z5, z5^-1), 2cos72=phi-1   =(1-t)(1-(phi-1)t+t^2)")
log("    5b : (1, z5^2,z5^-2),2cos144=-phi    =(1-t)(1+phi t+t^2)")
log("")
log("A5 has TWO 3-dim irreps 3, 3' with characters differing ONLY on the")
log("order-5 classes:  chi_3(5a)=phi, chi_3(5b)=psi ;  chi_3'(5a)=psi,")
log("chi_3'(5b)=phi.  The theta involution = the Galois swap 3<->3'.")
log("theta-ODD class function:  chi_odd = chi_3 - chi_3'  (sqrt5-antisymmetric)")
log("  chi_odd = 0 on classes 1,2,3 ;  chi_odd(5a)=phi-psi=+sqrt5 ;")
log("  chi_odd(5b)=psi-phi=-sqrt5.")
log("")

# denominators det(1 - t rho(g)) per class
D1  = (1 - t)**3
D2  = (1 - t) * (1 + t)**2
D3  = (1 - t) * (1 + t + t**2)
D5a = (1 - t) * (1 - (phi - 1) * t + t**2)
D5b = (1 - t) * (1 + phi * t + t**2)
sizes = {"1": 1, "2": 15, "3": 20, "5a": 12, "5b": 12}

# Molien's TWISTED formula:  M_chi(t) = (1/|G|) sum_g chi(g)/det(1 - t rho(g))
# For a class function chi, = (1/60) sum_classes size * chi(class)/D_class.
def twisted_molien(chi):
    # chi is dict class->value
    return sp.together(
        sp.Rational(1, 60) * (
            sizes["1"]  * chi["1"]  / D1  +
            sizes["2"]  * chi["2"]  / D2  +
            sizes["3"]  * chi["3"]  / D3  +
            sizes["5a"] * chi["5a"] / D5a +
            sizes["5b"] * chi["5b"] / D5b
        )
    )

# ---- sanity: theta-EVEN untwisted Molien of the 3-dim rep = icosahedral
#      invariants (Hilbert series with degrees 2,6,10,15).  chi = trivial.
chi_triv = {"1": 1, "2": 1, "3": 1, "5a": 1, "5b": 1}
M_inv = twisted_molien(chi_triv)
c_inv = series_coeffs(M_inv, NCOEF)
c_inv = [sp.nsimplify(c) for c in c_inv]
log("SANITY (theta-even, untwisted): Hilbert series of A5-invariants in Sym(3).")
log(f"  first coeffs = {[int(x) for x in c_inv[:16]]}")
expected_inv = "1,0,1,0,1,0,2,0,2,0,3,0,3,0,4"  # degrees 2,6,10,15 pattern
log(f"  (icosahedral invariants: generators in degrees 2,6,10,15; all >=0 ints)")
log("")

# ---- the theta-ODD twisted Molien series ---------------------------------
chi_odd = {"1": 0, "2": 0, "3": 0, "5a": s5, "5b": -s5}
M_odd = twisted_molien(chi_odd)
M_odd_simpl = sp.simplify(M_odd)
log("theta-ODD twisted Molien (exhibited exactly):")
log(f"  M_odd(t) = (12*sqrt5/60) * ( 1/D5a - 1/D5b )")
log(f"           = (sqrt5/5) * ( 1/D5a - 1/D5b )")
log("  PREFACTOR sqrt5/5 = 1/sqrt5 = 5^(-1/2)  <-- the tantalizing 5-adic")
log("  DENOMINATOR (v5 = -1/2).  THIS is the only place a 5-power could enter.")
log("")

# exhibit the W4-304 signature test: does the sqrt5 prefactor SURVIVE, or is
# it cancelled by the antisymmetric difference (1/D5a - 1/D5b)?
diff = sp.together(1 / D5a - 1 / D5b)
c_diff = series_coeffs(diff, NCOEF)          # coeffs of (1/D5a - 1/D5b)
# each is sqrt5-antisymmetric (Galois-odd) => equals sqrt5 * (rational)
diff_over_s5 = [sp.simplify(c / s5) for c in c_diff]

log("W4-304 SIGNATURE CHECK (even==odd cancellation with nonzero theta-odd?):")
log("  (1/D5a - 1/D5b) is Galois-ODD (sqrt5 |-> -sqrt5 swaps 5a<->5b), so its")
log("  every coefficient = sqrt5 * (rational).  Hence")
log("    M_odd_n = (sqrt5/5) * sqrt5 * r_n = (5/5) r_n = r_n  (rational).")
log("  The 5^(-1/2) prefactor is EXACTLY CANCELLED by the sqrt5 of the")
log("  antisymmetric difference.  There is NO surviving theta-odd denominator.")
log("")

c_odd = series_coeffs(M_odd_simpl, NCOEF)
c_odd = [sp.nsimplify(c) for c in c_odd]

log("n :  M_odd_n      is_integer?   v5(M_odd_n)   (theta-odd twisted Molien)")
p2_all_integer = True
p2_v5min = sp.oo
p2_max_denom_v5 = 0   # max v5 of DENOMINATOR (positive => real 5-denominator)
for n in range(0, NCOEF):
    c = c_odd[n]
    is_int = bool(sp.nsimplify(c).is_Integer)
    p2_all_integer = p2_all_integer and is_int
    if c != 0:
        vv = v5_rational(c)
        p2_v5min = min(p2_v5min, vv)
        denom_v5 = max(0, -vv)   # v5 of denominator
        p2_max_denom_v5 = max(p2_max_denom_v5, denom_v5)
    else:
        vv = sp.oo
    if n < 16 or n in (40, 41):
        log(f"{n:2d}: {str(c):12s} int?{is_int!s:5s} v5={vv}")

log("")
log(f"PATH 2 verdict: theta-odd twisted Molien coeffs ALL integers = "
    f"{p2_all_integer}")
log(f"  min v5 over nonzero coeffs = {p2_v5min}  (>=0 => algebraic-integral)")
log(f"  max v5(DENOMINATOR) over window = {p2_max_denom_v5}  "
    f"(target needs 1,12,49,...; a 0 here => NO 5-denominator)")
log("")

# independent cross-check of PATH 2: reconstruct M_odd_n from r_n directly
recon_ok = all(sp.simplify(c_odd[n] - diff_over_s5[n]) == 0
               for n in range(NCOEF))
log(f"CROSS-CHECK (2nd structural path): M_odd_n == r_n (from 1/D5a-1/D5b over")
log(f"  sqrt5, independent of the twisted-Molien assembly) : {recon_ok}")
log("")

# ---------------------------------------------------------------------------
# VERDICT BLOCK
# ---------------------------------------------------------------------------
log("=" * 74)
log("VERDICT")
log("=" * 74)

# The chord POSITIVE would require: theta-odd series NOT 5-adically integral
# (a real, unbounded, growing 5-power denominator like the target's).
chord_positive = (p2_max_denom_v5 >= 1) and (not p2_all_integer)

# genuine-chord test: is the computed quantity a GENUINE non-abelian/theta-odd
# object, or an ordinary character/trace polynomial relabeled?
# M_odd = (1/60) sum_g chi_odd(g)/det(1-t rho(g))  -- chi_odd IS a character
# difference (chi_3 - chi_3'); the whole series is a character sum / trace
# polynomial.  => the W3-082c trap: NOT a genuine chord positive.
is_genuine_chord = False   # a twisted character IS a character sum (trace poly)

if chord_positive and is_genuine_chord:
    verdict = "OVERTURNED"
    headline = ("theta-odd twisted Molien is NON-5-adically-integral on a "
                "genuine non-abelian object; exclusion is projection-specific")
elif chord_positive and not is_genuine_chord:
    # would be the W3-082c trap: a denominator that is really abelian
    verdict = "NEEDS-SPECIALIST"
    headline = ("apparent theta-odd denominator, but quantity is a character "
                "sum -- adjudicate abelian relabeling")
else:
    verdict = "HARDENS"
    headline = ("theta-odd twisted-character Molien is ALGEBRAIC-INTEGRAL on "
                "the genuinely non-abelian A5 object -- 5-adic exclusion "
                "survives the theta-odd projection")

# consistency guards
assert p1_odd_integral, "PATH1 theta-odd unexpectedly non-integral"
assert p2_all_integer, "PATH2 theta-odd unexpectedly non-integral"
assert recon_ok, "PATH2 cross-check failed"
assert p2_max_denom_v5 == 0, "PATH2 produced a 5-denominator -- re-examine!"

discriminating_fact = (
    "M_odd(t) = (sqrt5/5)(1/D5a - 1/D5b): the tantalizing 5^(-1/2) prefactor "
    "(v5=-1/2) is EXACTLY cancelled by the sqrt5 carried by the Galois-odd "
    "difference (1/D5a-1/D5b), so every theta-odd twisted-Molien coefficient "
    "is a RATIONAL INTEGER (min v5>=0, max denominator-v5 = "
    f"{p2_max_denom_v5}). No growing 5-power denominator appears; the target "
    "needs v5(denom)=1,12,49,99,146. The exclusion is NOT projection-specific."
)

log(f"chord_positive     : {chord_positive}")
log(f"is_genuine_chord   : {is_genuine_chord}")
log(f"  reason: M_odd = (1/60) sum_g (chi_3-chi_3')(g)/det(1-t rho(g)) is a")
log(f"  CHARACTER-difference twisted Molien = an ordinary character/trace")
log(f"  polynomial (W3-082c trap: a twisted character IS a character sum).")
log(f"VERDICT            : {verdict}")
log(f"HEADLINE           : {headline}")
log("")
log("W4-304 real-overturn signature ABSENT: the par/trace zero (chi_odd=0 on")
log("classes 1,2,3) carries NO nonzero theta-odd DENOMINATOR -- the even==odd")
log("structure resolves to integers, not to a surviving 5-adic piece.")
log("")
log("Gate 5/5-Q: structural theta-odd fact of the object; nothing to CLAIMS;")
log("the one-number pin untouched.")

results = {
    "cell": "CP-A5-molien",
    "campaign": "B774 Stage B chord-pass",
    "source_negative": "LAW_MAP 5-ADIC EXCLUSION (generation leg) / B685 W2 Molien kill",
    "banked_level": "theta-even / abelianized (trace-level algebraic-integrality)",
    "chord_computed": "theta-ODD twisted-character Molien on genuinely non-abelian A5",
    "target_v5_denominator": {str(k): v for k, v in TARGET_V5.items()},
    "path1_abelian_doublet": {
        "operator": "sigma(A1) golden rotation, order 10, eig zeta10^{+-1}",
        "theta_odd_all_integer": bool(p1_odd_integral),
        "theta_odd_min_v5": str(p1_odd_v5min),
        "note": "matches banked STEP3_VERDICT pt.4 diagnostic (M-M')/sqrt5 -> integers",
    },
    "path2_nonabelian_A5": {
        "object": "A5 icosahedral 3-dim rep, twisted by chi_odd = chi_3 - chi_3'",
        "M_odd_form": "(sqrt5/5)*(1/D5a - 1/D5b)",
        "prefactor_v5": "-1/2 (5^{-1/2}, the only 5-denominator candidate)",
        "prefactor_cancelled_by": "sqrt5 of the Galois-odd difference (1/D5a-1/D5b)",
        "all_coeffs_integer": bool(p2_all_integer),
        "min_v5": str(p2_v5min),
        "max_denominator_v5": int(p2_max_denom_v5),
        "cross_check_2nd_path": bool(recon_ok),
        "ncoef_tested": NCOEF,
    },
    "chord_positive": bool(chord_positive),
    "is_genuine_chord": bool(is_genuine_chord),
    "genuine_chord_reason": (
        "twisted Molien with chi_3-chi_3' is a character-difference sum = an "
        "ordinary character/trace polynomial (W3-082c trap); not a genuine "
        "non-abelian invariant beyond the character ring"
    ),
    "w4_304_signature": "ABSENT (no surviving nonzero theta-odd denominator)",
    "verdict": verdict,
    "headline": headline,
    "discriminating_fact": discriminating_fact,
}

with open(os.path.join(HERE, "results.json"), "w") as f:
    json.dump(results, f, indent=2)

with open(os.path.join(HERE, "output.txt"), "w") as f:
    f.write("\n".join(LINES) + "\n")

log("")
log("wrote results.json + output.txt")
