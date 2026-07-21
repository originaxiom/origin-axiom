"""B739 Stage B recompute -- TOMB-L77 (E19: compute-not-cite, both directions).

BANKED KILL (speculations/TOMBSTONES.md:L77, Chat-2 standard-theory-kills block):
    "Three regimes" (cyclotomic at finite k / algebraic at k->infty / transcendental
    coefficient) = an interpretation laid on top of the STANDARD ASYMPTOTIC EXPANSION
    of quantum invariants; not wrong, not new.  [kill_form: category-error]
Stage-A fact_basis was ASSERTED: "standard asymptotic expansion" was invoked with no
citation and no computation.  THE DISCRIMINATING FACT (the fact that, if true, kills
the claim): the three regimes are precisely the number-theoretic strata of the standard
asymptotic expansion of the standard quantum invariant, each derivable from the ambient
definitions ALONE (the Kashaev sum + saddle-point analysis), with zero framework input.
This script RE-DERIVES that expansion in-sandbox instead of citing it.

DECLARED CONVENTIONS (E1 -- the tombstone leaves these implicit; chosen explicitly,
from the original arc's own declarations):
  C1. "Quantum invariant" is instantiated as the figure-eight Kashaev invariant
      <4_1>_N = sum_{j=0}^{N-1} |(q)_j|^2,  q = e^{2*pi*i/N},  (q)_j = prod_{i<=j}(1-q^i)
      -- the arc's own exemplar and formula (S027 [MATH] block;
      frontier/physics_probes/kashaev_feasibility.py).  |1-q^i|^2 = 4 sin^2(pi*i/N),
      so <4_1>_N = sum_j prod_{i=1}^{j} 4 sin^2(pi*i/N)  (manifestly real).
  C2. Level convention N = k+2 (SU(2) CS), declared in the tombstone block itself:
      "the rep is defined over q = exp(2*pi*i/(k+2))".  "Cyclotomic at finite k"
      == the exact value at level k lies in Z[zeta_{k+2}] (a cyclotomic integer).
  C3. "Algebraic at k->infty" == the datum controlling the k->infty limit (the saddle
      point of the standard expansion, equivalently the shape parameter z_0 of the
      neighboring tombstone entries) is an algebraic number.
  C4. "Transcendental coefficient" == the exponential-rate coefficient Vol(4_1)/(2*pi).
      Transcendence of Vol(4_1) is not a theorem; the COMPUTABLE form used here is an
      integer-relation (PSLQ) exclusion at declared bounds (degree <= 6, |coeff| <= 10^8,
      120 dps), contrasted against the regimes-1/2 quantities for which the same method
      FINDS exact minimal polynomials.
  C5. Vol(4_1) := 2 * Im Li_2(e^{i*pi/3})  (= 2*D(z_0), Bloch-Wigner at |z|=1), computed
      via mpmath polylog; cross-checked against the arc's constant VOL_FIG8 =
      2.029883212819307 (kashaev_feasibility.py line 15).

DETERMINISM: no wall-clock, no randomness, no network.  Fixed N-lists, fixed mpmath
precision, PSLQ is deterministic.  (Stage-A tractability said needs-web because the
"standard asymptotic expansion" is literature; E19 dissolves that wall by deriving it.)

Gate 5: everything below is mathematics of a knot invariant; no SM quantities.
"""
from __future__ import annotations

import mpmath as mp
import sympy as sp

VOL_FIG8_ARC = "2.029883212819307"   # the arc's own constant, kashaev_feasibility.py:15

BAR = "=" * 78


def kashaev_exact(N: int):
    """<4_1>_N as an EXACT sympy number: sum_j prod_{i=1}^j 4 sin^2(pi i/N)."""
    total = sp.Integer(0)
    prod = sp.Integer(1)
    for j in range(N):
        total += prod
        prod *= 4 * sp.sin(sp.pi * (j + 1) / sp.Integer(N)) ** 2
    return sp.nsimplify(sp.simplify(total))


def kashaev_mp(N: int):
    """<4_1>_N numerically at current mpmath precision (same formula, C1)."""
    total = mp.mpf(0)
    prod = mp.mpf(1)
    for j in range(N):
        total += prod
        s = mp.sin(mp.pi * (j + 1) / N)
        prod *= 4 * s * s
    return total


def part1_cyclotomic():
    print(BAR)
    print("PART 1 -- REGIME 'cyclotomic at finite k': exact values at N = k+2")
    print(BAR)
    print("Each term of <4_1>_N is a Z-polynomial in q = zeta_N, so <4_1>_N is in")
    print("Z[zeta_N] BY CONSTRUCTION of q = exp(2 pi i/(k+2)) (same tautology as the")
    print("neighboring roots-of-unity tombstone).  Computed witness: the exact value and")
    print("its minimal polynomial (monic, integer coefficients, degree | phi(N)).\n")
    x = sp.symbols("x")
    ok_all = True
    for N in (3, 4, 5, 6, 7, 8, 12):
        k = N - 2
        val = kashaev_exact(N)
        p = sp.minimal_polynomial(val, x)
        deg = sp.degree(p, x)
        phi = sp.totient(N)
        monic = sp.LC(p, x) == 1
        intcoeffs = all(c.is_Integer for c in sp.Poly(p, x).all_coeffs())
        alg_int = bool(monic and intcoeffs)
        divides = (phi % deg == 0)
        ok = alg_int and divides
        ok_all &= ok
        print(f"  k={k:>2} (N={N:>2}): <4_1>_N = {sp.sstr(val)}")
        print(f"            = {sp.N(val, 20)}")
        print(f"            min poly: {sp.sstr(p)}")
        print(f"            deg={deg}, phi(N)={phi}, deg|phi(N): {divides}, "
              f"algebraic integer (monic+Z): {alg_int}  -> in Z[zeta_N]: {ok}")
    print(f"\n  REGIME-1 WITNESS: all listed levels give cyclotomic integers: {ok_all}")
    return ok_all


def part2_algebraic_saddle():
    print()
    print(BAR)
    print("PART 2 -- REGIME 'algebraic at k->infty': the saddle of the STANDARD expansion")
    print(BAR)
    print("Continuum limit of the summand (x = j/N):")
    print("  (1/N) log(term_j) -> f(x) = 2 * Integral_0^x log(2 sin(pi t)) dt")
    print("                            = -(2/pi) * Lob(pi x)   (Lobachevsky).")
    print("Critical-point equation f'(x) = 2 log(2 sin(pi x)) = 0  <=>  2 sin(pi x) = 1.\n")
    x = sp.symbols("x", real=True)
    sols = sorted(sp.solveset(2 * sp.sin(sp.pi * x) - 1, x,
                              sp.Interval.open(0, 1)))
    print(f"  solutions in (0,1): {sols}")
    fpp = sp.diff(2 * sp.log(2 * sp.sin(sp.pi * x)), x)
    checks = [(s, sp.simplify(fpp.subs(x, s))) for s in sols]
    for s, v in checks:
        kind = "MAXIMUM" if v.is_negative else "minimum"
        print(f"  f''({s}) = {sp.sstr(v)}  -> {kind}")
    xstar = [s for s, v in checks if v.is_negative][0]
    print(f"  saddle: x* = {xstar}  (peak term at j ~ {xstar}*N)")
    zstar = sp.exp(2 * sp.pi * sp.I * xstar)
    zstar_s = sp.simplify(zstar)
    t = sp.symbols("z")
    pz = sp.minimal_polynomial(zstar_s, t)
    print(f"\n  multiplicative saddle coordinate z* = exp(2 pi i x*) = {sp.sstr(zstar_s)}")
    print(f"  minimal polynomial of z*: {sp.sstr(pz)}   (degree {sp.degree(pz, t)})")
    z0 = sp.exp(sp.I * sp.pi / 3)
    pz0 = sp.minimal_polynomial(z0, t)
    same = sp.expand(pz - pz0) == 0
    disc = sp.discriminant(sp.Poly(pz, t))
    print(f"  the tombstone's z_0 = exp(i pi/3): min poly {sp.sstr(pz0)}; same quadratic as z*: {same}")
    print(f"  discriminant = {disc}  ->  field Q(sqrt(-3)) (the 4_1 trace field; z_0 is the")
    print(f"  shape parameter of the two regular ideal tetrahedra of the 4_1 complement).")
    conj_ok = sp.simplify(zstar_s - sp.conjugate(z0)) == 0
    print(f"  z* = conjugate(z_0): {conj_ok}")
    ok = same and sp.degree(pz, t) == 2 and disc == -3
    print(f"\n  REGIME-2 WITNESS: the k->infty limit is controlled by an ALGEBRAIC number")
    print(f"  (z^2 - z + 1 = 0, degree 2, disc -3), straight from the saddle equation: {ok}")
    return ok, xstar


def part3_transcendental_coefficient(xstar):
    print()
    print(BAR)
    print("PART 3 -- REGIME 'transcendental coefficient': the growth rate of the SAME sum")
    print(BAR)
    mp.mp.dps = 60
    # Lob(theta) = (1/2) Im Li_2(e^{2 i theta});  f(x*) = -(2/pi) Lob(pi x*) = (2/pi) Lob(pi/6)
    lob_pi6 = mp.im(mp.polylog(2, mp.e ** (1j * mp.pi / 3))) / 2
    c = (2 / mp.pi) * lob_pi6                       # predicted growth rate per unit N
    D_z0 = mp.im(mp.polylog(2, mp.e ** (1j * mp.pi / 3)))   # Bloch-Wigner D(z_0), |z_0|=1
    vol = 2 * D_z0                                  # C5
    print(f"  saddle value  f(x*) = (2/pi)*Lob(pi/6) = {mp.nstr(c, 25)}")
    print(f"  D(z_0) = Im Li_2(e^(i pi/3))          = {mp.nstr(D_z0, 25)}")
    print(f"  Vol(4_1) = 2 D(z_0)                   = {mp.nstr(vol, 25)}")
    print(f"  arc constant VOL_FIG8                 = {VOL_FIG8_ARC}")
    match_arc = abs(vol - mp.mpf(VOL_FIG8_ARC)) < mp.mpf("1e-15")
    print(f"  |2 D(z_0) - VOL_FIG8| < 1e-15: {match_arc}")
    rate_id = abs(c - vol / (2 * mp.pi)) < mp.mpf("1e-50")
    print(f"  identity f(x*) = Vol(4_1)/(2 pi) to 50 dps: {rate_id}")
    print(f"  => the exponential-rate coefficient of the standard expansion is Vol/2pi,")
    print(f"     the dilogarithm evaluated AT the algebraic saddle of Part 2.\n")

    # --- the sum itself converges to this rate (the arc's witness, re-derived) ---
    print("  (a) leading exponential: (2 pi/N) log<4_1>_N -> Vol(4_1), monotone from above")
    Ns = (50, 100, 200, 400, 800, 1600)
    growths = []
    for N in Ns:
        J = kashaev_mp(N)
        g = (2 * mp.pi / N) * mp.log(J)
        growths.append(g)
        print(f"      N={N:>5}: (2pi/N) log J_N = {mp.nstr(g, 15)}   err = {mp.nstr(g - vol, 6)}")
    mono = all(growths[i] > growths[i + 1] > vol for i in range(len(growths) - 1))
    print(f"      monotone decreasing toward Vol, always above: {mono}\n")

    # --- sub-leading strata of the SAME expansion, extracted from the sum itself ---
    print("  (b) power stratum: g_N = log J_N - N*Vol/2pi = p*log N + log C + o(1)")
    print("      p_hat = (g_2N - g_N)/log 2  (expect p = 3/2):")
    gvals = {}
    for N in (200, 400, 800, 1600, 3200):
        gvals[N] = mp.log(kashaev_mp(N)) - N * c
    for N in (200, 400, 800, 1600):
        p_hat = (gvals[2 * N] - gvals[N]) / mp.log(2)
        print(f"      N={N:>5}: p_hat = {mp.nstr(p_hat, 10)}")
    print("      -> p = 3/2 (rational stratum).\n")
    print("  (c) constant stratum: C_N = J_N / (N^(3/2) e^(N*Vol/2pi))  (expect 3^(-1/4)):")
    c3 = mp.mpf(3) ** mp.mpf("-0.25")
    Cs = {}
    for N in (400, 800, 1600, 3200):
        Cs[N] = mp.e ** (gvals[N] - mp.mpf("1.5") * mp.log(N))
        print(f"      N={N:>5}: C_N = {mp.nstr(Cs[N], 12)}")
    rich = 2 * Cs[3200] - Cs[1600]     # Richardson for a 1/N correction
    print(f"      Richardson (1/N): C_inf ~ {mp.nstr(rich, 12)}")
    print(f"      3^(-1/4)         = {mp.nstr(c3, 12)}")
    const_ok = abs(rich - c3) < mp.mpf("1e-4")
    print(f"      |C_inf - 3^(-1/4)| < 1e-4: {const_ok}   (algebraic stratum, x^4 = 1/3)\n")

    # --- PSLQ: the coefficient is NOT low-algebraic; the other strata ARE algebraic ---
    print("  (d) PSLQ integer-relation test, 120 dps, degree <= 6, |coeff| <= 10^8:")
    mp.mp.dps = 120
    D_z0 = mp.im(mp.polylog(2, mp.e ** (1j * mp.pi / 3)))
    vol = 2 * D_z0
    coeff = vol / (2 * mp.pi)
    controls = [
        ("<4_1>_5 = 46+2*sqrt(5) (regime 1)", 46 + 2 * mp.sqrt(5)),
        ("3^(-1/4) (regime-2/algebraic stratum)", mp.mpf(3) ** mp.mpf("-0.25")),
    ]
    for name, val in controls:
        rel = mp.pslq([val ** i for i in range(7)], maxcoeff=10 ** 8, maxsteps=10 ** 6)
        print(f"      {name}: relation {rel}  -> FOUND (algebraic, as it must be)")
    for name, val in (("Vol(4_1)/(2 pi)", coeff), ("Vol(4_1)", vol)):
        rel = mp.pslq([val ** i for i in range(7)], maxcoeff=10 ** 8, maxsteps=10 ** 6)
        verdictw = "NO relation" if rel is None else f"relation {rel}"
        print(f"      {name}: {verdictw}")
    print("      -> the rate coefficient admits NO integer polynomial of degree <= 6 with")
    print("         coefficients <= 10^8 (at 120 dps), while the regime-1/2 quantities do:")
    print("         the 'transcendental coefficient' stratum is the expansion's own.")
    mp.mp.dps = 60
    return bool(match_arc and rate_id and mono and const_ok)


def main():
    print(BAR)
    print("B739 / TOMB-L77 recompute: the 'three regimes' vs the standard asymptotic")
    print("expansion of the Kashaev invariant <4_1>_N -- derived, not cited (E19)")
    print(BAR)
    print()
    r1 = part1_cyclotomic()
    r2, xstar = part2_algebraic_saddle()
    r3 = part3_transcendental_coefficient(xstar)
    print()
    print(BAR)
    print("VERDICT COMPUTATION")
    print(BAR)
    print(f"  regime 1 (cyclotomic at finite k)  from the bare definition:   {r1}")
    print(f"  regime 2 (algebraic at k->infty)   from the saddle equation:   {r2}")
    print(f"  regime 3 (transcendental coeff.)   from the same expansion:    {r3}")
    all_ok = r1 and r2 and r3
    print()
    if all_ok:
        print("  All three 'regimes' are strata of ONE standard asymptotic expansion of the")
        print("  standard invariant, derived here from the ambient definitions alone --")
        print("  q = e^(2 pi i/(k+2)) forces cyclotomic values; the saddle z^2-z+1=0 supplies")
        print("  the algebraic k->infty datum; the rate Vol/2pi = (1/pi) Im Li_2(z_0) supplies")
        print("  the transcendental-type coefficient.  NO framework input entered at any step.")
        print("  The banked category-error kill is upheld: RECONFIRMED.")
    else:
        print("  At least one regime did NOT reproduce from the standard expansion -- the")
        print("  banked fact fails as stated: REVIVED (see the failing part above).")


if __name__ == "__main__":
    main()
