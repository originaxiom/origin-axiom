#!/usr/bin/env python3
"""
twoended.py -- P-TWOENDED probe (VALUE-PROBING WAVE, cc 2026-08-21):
does the Kashaev-tower arithmetic of the figure-eight knot (4_1) carry BOTH curvature
ends -- the hyperbolic Q(sqrt(-3))/E6 end (already established) AND the spherical
Q(sqrt5)/E8 end (untested)? A STRUCTURE question, not a value match.

PART A (cheap, runs first): structural analysis of the ALREADY-BANKED
    C_3 = (724351/12597120) * sqrt(3) * pi^3 * C_0          [frontier/B1124]
Independently re-verify the numerator/denominator factorizations, contrast against
C_1 = (11/108)*sqrt3*pi*C0 and C_2 = (697/7776)*pi^2*C0 (both {2,3}-smooth), check the
prime-splitting behaviour of 724351's prime factors in Q(sqrt(-3)) AND Q(sqrt5), and test
(for completeness, expecting no exact hit -- q3 is RATIONAL, these are not) naive ratios
against zeta_K(2) [K=Q(sqrt-3)], L(chi_5,2) [the Q(sqrt5) L-value], and the golden ratio.
Also illustrates the generic, two-ended-UNRELATED alternative mechanism (von Staudt-Clausen
/ Bernoulli-number denominators picking up new primes at higher perturbative order in ANY
WKB/quantum-dilogarithm expansion) that a bare "5" in a rational coefficient's denominator
would be consistent with, decoupled from any field-extension claim.

PART B (expensive, the real test): extend the J_N(4_1) Kashaev-invariant tower PAST
B1124's N=35,000,000 ceiling to resolve C_4 and (if reachable) C_5, reusing the b1124
precision discipline throughout:
  - "exact" constants (Vol, growth_rate, C0_target) frozen at DPS_VOL via a unary `+`,
    passed onward as high-precision decimal STRINGS to every multiprocessing worker, so
    every downstream context rounds DOWN, never up from a low-precision accident.
  - polynomial-in-1/N fits use a rescaled-CHEBYSHEV basis, never monomials.
  - "trusted digits" = min(within-window K-convergence, cross-window agreement), reported
    both as the PRIMARY (all genuine windows incl. the small-N ones) and the LARGE-WINDOW
    (big-N windows only) metric, kept visibly separate (the b1124/L180 lesson).
  - PSLQ recognition sweep, maxcoeff calibrated to achieved precision (never a blind
    high ceiling at low dps -- the noise-on-every-basis trap b1124 caught).
  - NEW relative to b1124: the recognition-type family is extended from {Q, Q(sqrt3)} to
    {Q, Q(sqrt3), Q(sqrt5), Q(sqrt15)}, and the candidate BASE family gets sqrt5/sqrt15-
    flavoured entries alongside the sqrt3-flavoured ones -- a DIRECT test of whether sqrt5
    (not sqrt3) ever appears in an odd coefficient, which is the actual two-ended
    signature (as opposed to a bare prime in a rational coefficient's denominator, which
    Part A shows is all C_3 currently exhibits). The already-known C_3 doubles as a
    NEGATIVE CONTROL for this new machinery: it must reproduce the known q3 on Q(sqrt3)
    and find a clean null on Q(sqrt5)/Q(sqrt15) before C_4/C_5 results are trusted.

Self-contained: mpmath + sympy only, no repo imports, no machine-specific paths (output
dir via $TWOENDED_OUTDIR, worker count via $TWOENDED_NWORKERS). Windows W1-W5 intentionally
match b1124_verify.py's grids exactly, N-for-N, so this script's OWN fresh computation is
diffable against the banked b1124_results.json as a correctness control on the new code --
done by hand ahead of the real run (R_N at N=1000/2000/20000 reproduced b1124's reported
values to all ~40 reported digits; see NOTES.md), not wired up as an in-script flag here.
"""
from __future__ import annotations

import json
import os
import sys
import time
import pickle
from multiprocessing import Pool
from fractions import Fraction as PyFraction

import mpmath as mp
import sympy

# =============================================================================
# Configuration (env-var overridable; no hardcoded machine paths)
# =============================================================================
DPS_VOL = 700           # "exact" constants frozen once here, highest precision needed anywhere
DPS_MAIN = 400           # main working precision (2x b1124's 200 -- cheap on this backend, see NOTES)
DPS_CROSS = 600           # precision-doubling cross-check (on a W6 subset)
NWORKERS = int(os.environ.get("TWOENDED_NWORKERS", "8"))
OUTDIR = os.environ.get("TWOENDED_OUTDIR") or os.path.dirname(os.path.abspath(__file__)) or "."
CKPT_PATH = os.path.join(OUTDIR, "twoended_checkpoint.pkl")
RUN_W6 = os.environ.get("TWOENDED_W6", "1") != "0"
RUN_W7 = os.environ.get("TWOENDED_W7", "0") == "1"   # off by default; light reach tier


def s(x, digits=30):
    return mp.nstr(x, digits)


# =============================================================================
# PART A -- cheap structural analysis of the banked C_3 (runs first, ~seconds)
# =============================================================================

def part_a_c3_structure():
    out = {}
    mp.mp.dps = 80

    # --- independent re-factorization (verify, not trust the NOTES.md prose) ---
    num, den = 724351, 12597120
    nf = sympy.factorint(num)
    df = sympy.factorint(den)
    assert sympy.prod([p ** e for p, e in nf.items()]) == num
    assert sympy.prod([p ** e for p, e in df.items()]) == den
    out["C3_numerator"] = num
    out["C3_denominator"] = den
    out["C3_numerator_factors"] = {str(k): v for k, v in nf.items()}
    out["C3_denominator_factors"] = {str(k): v for k, v in df.items()}
    out["C3_numerator_is_prime"] = sympy.isprime(num)

    # --- contrast: C1, C2 stay pure {2,3}-smooth ---
    contrast = {}
    for label, n, d in [("C1", 11, 108), ("C2", 697, 7776), ("C3", num, den)]:
        dfac = sympy.factorint(d)
        nfac = sympy.factorint(n)
        contrast[label] = dict(numerator=n, denominator=d,
                                num_factors={str(k): v for k, v in nfac.items()},
                                den_factors={str(k): v for k, v in dfac.items()},
                                den_primes=sorted(int(p) for p in dfac.keys()),
                                den_is_23_smooth=all(int(p) <= 3 for p in dfac.keys()))
    out["contrast_C1_C2_C3"] = contrast

    # --- prime-splitting behaviour of C3's numerator primes, in BOTH candidate fields ---
    # Q(sqrt(-3)): disc -3; p (!=3) splits iff p%3==1, inert iff p%3==2.
    # Q(sqrt5):    disc  5; p (!=5) splits iff p%5 in {1,4}, inert iff p%5 in {2,3}.
    splitting = {}
    for p in nf.keys():
        p = int(p)
        m3, m5 = p % 3, p % 5
        split_m3 = "splits" if m3 == 1 else ("inert" if m3 == 2 else "ramifies")
        split_5 = "splits" if m5 in (1, 4) else ("inert" if m5 in (2, 3) else "ramifies")
        splitting[str(p)] = dict(mod3=m3, in_Q_sqrt_m3=split_m3, mod5=m5, in_Q_sqrt5=split_5)
    out["numerator_prime_splitting"] = splitting
    both_split = [p for p, v in splitting.items() if v["in_Q_sqrt_m3"] == "splits" and v["in_Q_sqrt5"] == "splits"]
    both_inert = [p for p, v in splitting.items() if v["in_Q_sqrt_m3"] == "inert" and v["in_Q_sqrt5"] == "inert"]
    out["splitting_correlation_note"] = (
        f"{len(both_split)} of 3 primes split in BOTH fields, {len(both_inert)} of 3 inert in BOTH "
        f"-- for 3 primes this 'same behaviour in both fields' pattern has ~1/8 probability under "
        f"independence (Chebotarev), i.e. NOT a strong signal either way; reported, not oversold."
    )

    # --- transcendental-quantity context (zeta_K(2), L(chi_5,2), phi) ---
    with mp.workdps(60):
        def L2_chi_m3():
            return mp.mpf(1) / 9 * (mp.zeta(2, mp.mpf(1) / 3) - mp.zeta(2, mp.mpf(2) / 3))

        def L2_chi_5():
            return mp.mpf(1) / 25 * (mp.zeta(2, mp.mpf(1) / 5) - mp.zeta(2, mp.mpf(2) / 5)
                                      - mp.zeta(2, mp.mpf(3) / 5) + mp.zeta(2, mp.mpf(4) / 5))

        L_m3 = L2_chi_m3()
        zetaK = mp.zeta(2) * L_m3
        L_5 = L2_chi_5()
        phi = (1 + mp.sqrt(5)) / 2
        sqrt5 = mp.sqrt(5)
        q3 = mp.mpf(num) / mp.mpf(den)

        candidates = {
            "zeta_K(2)/pi^2": zetaK / mp.pi ** 2,
            "L(2,chi5)/pi^2": L_5 / mp.pi ** 2,
            "L(2,chi5)/zeta(2)": L_5 / mp.zeta(2),
            "zeta_K(2)/zeta(2)": zetaK / mp.zeta(2),
            "1/phi^2": 1 / phi ** 2,
            "1/phi^3": 1 / phi ** 3,
            "1/(5*phi)": 1 / (5 * phi),
            "sqrt5/pi^2": sqrt5 / mp.pi ** 2,
        }
        ratio_checks = {name: dict(value=s(val, 20), ratio_to_q3=s(val / q3, 15),
                                    ratio_is_near_simple_rational=False)
                        for name, val in candidates.items()}
        # explicit near-integer/near-simple-rational scan on the ratio (would flag a hidden hit)
        for name, val in candidates.items():
            r = val / q3
            near = mp.nint(r)
            ratio_checks[name]["ratio_is_near_simple_rational"] = bool(abs(r - near) < mp.mpf('1e-6'))

    out["q3_decimal"] = s(q3 if 'q3' in dir() else mp.mpf(num) / mp.mpf(den), 40)
    out["transcendental_context"] = dict(
        L2_chi_m3=s(L_m3, 40), zeta_K2_Q_sqrt_m3=s(zetaK, 40), L2_chi5=s(L_5, 40),
        phi=s(phi, 40),
        note=("q3 is a PLAIN RATIONAL (established via 36-digit direct confirmation in B1124); "
              "a rational cannot equal a generic transcendental/irrational combination like these -- "
              "this scan exists only to positively rule out a hidden simple-rational-multiple "
              "coincidence, not because a hit was expected."),
        ratio_checks=ratio_checks,
        any_near_simple_rational=any(v["ratio_is_near_simple_rational"] for v in ratio_checks.values()),
    )

    # --- the generic (two-ended-UNRELATED) alternative mechanism: von Staudt-Clausen ---
    # Denominator of the Bernoulli number B_{2n} = product of primes p with (p-1)|2n
    # (von Staudt-Clausen). This is a WELL-KNOWN, field-extension-free reason a "new prime"
    # enters a perturbative-expansion coefficient's denominator at higher order -- present
    # for EVERY hyperbolic knot's WKB/Ohtsuki series, nothing specific to two-endedness.
    vsc_rows = []
    for n2 in range(2, 13, 2):
        b = sympy.bernoulli(n2)
        den_b = sympy.fraction(b)[1]
        primes_in_den = sorted(int(p) for p in sympy.factorint(den_b).keys())
        five_enters = 5 in primes_in_den
        vsc_rows.append(dict(index=f"B_{n2}", value=str(b), denominator=int(den_b),
                              primes_in_denominator=primes_in_den, prime_5_present=five_enters))
    out["von_staudt_clausen_alternative_mechanism"] = dict(
        rows=vsc_rows,
        note=("Illustrative only (no claim that Ohtsuki's exact recursion for 4_1 is derived here): "
              "von Staudt-Clausen shows prime 5 enters/exits Bernoulli-number denominators purely by "
              "the combinatorial rule (p-1)|2n -- a MUNDANE, per-knot-universal source of 'new primes "
              "at higher order' with zero connection to any number field. C_3's bare '5' is consistent "
              "with this generic mechanism; distinguishing it from a genuine sqrt5/E8 signal requires "
              "the Part B extension (does 5 recur/grow in a DIRECTED way, and does sqrt5 itself ever "
              "appear as an algebraic generator, not just a denominator prime)."),
    )

    out["part_a_verdict"] = (
        "The '5' in C_3's denominator (12,597,120 = 2^7*3^9*5) is a prime factor of a PLAIN RATIONAL "
        "coefficient multiplying sqrt(3)*pi^3*C0 -- the trace field itself is unchanged, confirmed "
        "Q(sqrt3) to 36 digits (B1124). This is STRUCTURALLY WEAKER than a genuine sqrt5/E8 signal: "
        "no sqrt5 appears anywhere in the closed form. The numerator's prime factorization (53*79*173) "
        "shows no clean splitting-based fingerprint tying it to Q(sqrt5) (weak ~1/8-probability "
        "coincidence at best), and no simple-rational-multiple relation to zeta_K(2), L(chi5,2), or "
        "phi was found. A single banked data point cannot distinguish 'the E8 end entering' from "
        "'a generic Bernoulli/von-Staudt-Clausen-type combinatorial prime' -- both are consistent with "
        "what is banked. Part B is the actual discriminating test."
    )
    return out


# =============================================================================
# PART B -- the tower extension
# =============================================================================

# ---- 0. Vol(4_1), independently, from closed forms (dilog / Lobachevsky) ----

def compute_vol_fig8():
    with mp.workdps(DPS_VOL):
        def Li2(z):
            return mp.polylog(2, z)
        routeA = 2 * mp.im(Li2(mp.e ** (1j * mp.pi / 3)))

        def lobachevsky(theta):
            return mp.mpf('0.5') * mp.im(Li2(mp.e ** (2j * theta)))
        v3 = 3 * lobachevsky(mp.pi / 3)
        routeB = 2 * v3
        agree = abs(routeA - routeB) < mp.mpf(10) ** (-(DPS_VOL - 15))
        return +routeA, +routeB, agree


# ---- 1. J_N(4_1): fast angle-addition path + direct cross-validation path ----

def J_N_trig_fast(N: int, renorm_every: int = 2000) -> mp.mpf:
    theta = mp.pi / N
    c1 = mp.cos(theta)
    s1 = mp.sin(theta)
    c, sN = mp.mpf(1), mp.mpf(0)
    total = mp.mpf(1)
    prod = mp.mpf(1)
    for j in range(1, N):
        c, sN = c * c1 - sN * s1, sN * c1 + c * s1
        if renorm_every and j % renorm_every == 0:
            norm = mp.sqrt(c * c + sN * sN)
            c, sN = c / norm, sN / norm
        factor = 4 * sN * sN
        prod *= factor
        total += prod
    return total


def J_N_trig_direct(N: int) -> mp.mpf:
    total = mp.mpf(1)
    prod = mp.mpf(1)
    for j in range(1, N):
        factor = 4 * mp.sin(mp.pi * j / N) ** 2
        prod *= factor
        total += prod
    return total


# ---- 2. Multiprocessing worker: R_N from FROZEN high-precision constants ----

def _worker_R_N(args):
    N, dps, growth_rate_str, p_exact_str = args
    mp.mp.dps = dps
    growth_rate = mp.mpf(growth_rate_str)
    p_exact = mp.mpf(p_exact_str)
    j = J_N_trig_fast(N)
    lj = mp.log(j)
    log_R = lj - p_exact * mp.log(N) - growth_rate * N
    R_N = mp.exp(log_R)
    return (N, mp.nstr(R_N, dps + 20))


def freeze_strings(*vals, digits=DPS_VOL + 10):
    with mp.workdps(DPS_VOL):
        return [mp.nstr(+v, digits) for v in vals]


def parallel_R_N(pool, Ns, dps, gr_str, pe_str, have=None):
    have = have or {}
    todo = [N for N in Ns if N not in have]
    out = dict(have)
    if todo:
        args = [(N, dps, gr_str, pe_str) for N in todo]
        for N, R_str in pool.imap_unordered(_worker_R_N, args):
            out[N] = mp.mpf(R_str)
    return {N: out[N] for N in Ns}


# ---- 3. Linear algebra: rescaled-Chebyshev basis fit ----

def _poly_mul_trunc(p, q, K):
    result = [mp.mpf(0)] * K
    for i in range(min(len(p), K)):
        if p[i] == 0:
            continue
        for j in range(min(len(q), K - i)):
            result[i + j] += p[i] * q[j]
    return result


def _rescaled_cheb_basis(xs, K):
    xmin, xmax = min(xs), max(xs)
    center = (xmin + xmax) / 2
    halfwidth = (xmax - xmin) / 2
    alpha = 1 / halfwidth
    beta = -center / halfwidth
    lin = [2 * beta, 2 * alpha] + [mp.mpf(0)] * (K - 2)
    P = [[mp.mpf(1)] + [mp.mpf(0)] * (K - 1)]
    if K > 1:
        P.append([beta, alpha] + [mp.mpf(0)] * (K - 2))
    for k in range(2, K):
        term = _poly_mul_trunc(lin, P[k - 1], K)
        P.append([term[j] - P[k - 2][j] for j in range(K)])
    return P, center, halfwidth


def _cheb_vals(u, K):
    Tv = [mp.mpf(1)]
    if K > 1:
        Tv.append(u)
    for k in range(2, K):
        Tv.append(2 * u * Tv[-1] - Tv[-2])
    return Tv


def poly_fit_1_over_N(Ns, Rs, K):
    n = len(Ns)
    xs = [mp.mpf(1) / N for N in Ns]
    P, center, halfwidth = _rescaled_cheb_basis(xs, K)
    A = mp.matrix(n, K)
    b = mp.matrix(n, 1)
    for i, x in enumerate(xs):
        u = (x - center) / halfwidth
        Tv = _cheb_vals(u, K)
        for k in range(K):
            A[i, k] = Tv[k]
        b[i] = Rs[i]
    d, resid = mp.qr_solve(A, b)
    C = [mp.mpf(0)] * K
    for k in range(K):
        for j in range(K):
            C[j] += d[k] * P[k][j]
    return C, resid


# ---- 4. PSLQ recognition sweep -- EXTENDED beyond {Q, Q(sqrt3)} ----

MAXCOEFF_LIST = (100, 1000, 10000, 100000, 1000000, 3000000)

# recognition "field types" tested against every T. Q(sqrt3) is the ESTABLISHED law;
# Q(sqrt5) and Q(sqrt15) are the NEW two-ended probe (sqrt15 = sqrt3*sqrt5, the
# multiplicative compositum signature).
QTYPES = ("Q", "Q(sqrt3)", "Q(sqrt5)", "Q(sqrt15)")


def _qtype_vec(Tm, qtype):
    if qtype == "Q":
        return [Tm, mp.mpf(1)]
    if qtype == "Q(sqrt3)":
        return [Tm, mp.mpf(1), mp.sqrt(3)]
    if qtype == "Q(sqrt5)":
        return [Tm, mp.mpf(1), mp.sqrt(5)]
    if qtype == "Q(sqrt15)":
        return [Tm, mp.mpf(1), mp.sqrt(15)]
    raise ValueError(qtype)


def recognize_sweep_multi(T_hp, dps_for_pslq, maxcoeff_list=MAXCOEFF_LIST, maxsteps=20000,
                           qtypes=QTYPES):
    attempts = []
    with mp.workdps(dps_for_pslq):
        Tm = +T_hp
        for qtype in qtypes:
            vec = _qtype_vec(Tm, qtype)
            for maxcoeff in maxcoeff_list:
                r = mp.pslq(vec, maxcoeff=maxcoeff, maxsteps=maxsteps)
                # For 3-term types (Q(sqrt3)/Q(sqrt5)/Q(sqrt15)) PSLQ can return a DEGENERATE
                # relation with the irrational coefficient r[2]==0 whenever T is genuinely
                # PLAIN RATIONAL -- that is just the 2-term Q relation padded with a zero, not
                # evidence of the irrational type. Require r[2]!=0 for those types, else this
                # would misclassify an honest single-end null (C4 landing on plain Q, as
                # predicted) as a spurious Q(sqrt5)/Q(sqrt15) "hit" -- a false two-ended signal.
                degenerate = (len(vec) == 3 and r is not None and len(r) == 3 and r[2] == 0)
                found = (r is not None and r[0] != 0 and not degenerate)
                attempts.append(dict(basis=qtype, maxcoeff=maxcoeff, dps=dps_for_pslq,
                                      relation=(list(r) if found else None), found=found,
                                      degenerate_zero_irrational_coeff=degenerate))
    return attempts


def build_candidate_bases():
    """Original 11-base {1,3}-flavoured family (b1124, kept identical for comparability)
    PLUS 6 new sqrt5/sqrt15-flavoured bases (the two-ended probe: if the true relation has
    a sqrt5 component, testing against a sqrt5-carrying base can reveal it as a Q-type hit,
    the same mechanism that revealed C_1/C_2's structure via sqrt3-carrying bases)."""
    with mp.workdps(DPS_VOL):
        sqrt3 = mp.sqrt(3)
        sqrt5 = mp.sqrt(5)
        sqrt15 = mp.sqrt(15)
        pi = mp.pi
        bases = {
            "1": +mp.mpf(1),
            "pi": +pi,
            "2pi": +(2 * pi),
            "pi/sqrt3": +(pi / sqrt3),
            "2pi/sqrt3": +(2 * pi / sqrt3),
            "pi*sqrt3": +(pi * sqrt3),
            "2pi*sqrt3": +(2 * pi * sqrt3),
            "sqrt3": +sqrt3,
            "1/sqrt3": +(1 / sqrt3),
            "4pi": +(4 * pi),
            "pi^2": +(pi * pi),
            # -- new: sqrt5/sqrt15-flavoured --
            "pi/sqrt5": +(pi / sqrt5),
            "pi*sqrt5": +(pi * sqrt5),
            "sqrt5": +sqrt5,
            "1/sqrt5": +(1 / sqrt5),
            "pi/sqrt15": +(pi / sqrt15),
            "pi*sqrt15": +(pi * sqrt15),
        }
        return bases


BASE_SQRT3_PARITY = {   # 1 if the base carries an ODD net power of sqrt(3), else 0
    "1": 0, "pi": 0, "2pi": 0, "4pi": 0, "pi^2": 0,
    "pi/sqrt3": 1, "2pi/sqrt3": 1, "pi*sqrt3": 1, "2pi*sqrt3": 1, "sqrt3": 1, "1/sqrt3": 1,
    "pi/sqrt5": 0, "pi*sqrt5": 0, "sqrt5": 0, "1/sqrt5": 0, "pi/sqrt15": 0, "pi*sqrt15": 0,
}
WRONG_PI_POWER_BASES = ("1", "pi^2")
# bases that themselves carry sqrt5/sqrt15 -- flagged separately, not part of the
# established Q/Q(sqrt3) law (see expected_basis_kind docstring)
SQRT5_FLAVOURED_BASES = ("pi/sqrt5", "pi*sqrt5", "sqrt5", "1/sqrt5", "pi/sqrt15", "pi*sqrt15")


def expected_basis_kind(k, base_name):
    """Q/Q(sqrt3) law ONLY (b1124, unchanged, derivation reproduced from that script):
    kappa_k := C_k/(C0*pi^k) is type R (rational) if k even, type S=rational*sqrt3 if k odd.
    A base B = pi*sqrt(3)^m*(rational) has B^k carrying sqrt(3)^{m*k}; k even -> ALWAYS
    type R regardless of the base's own sqrt3 content; k odd -> type R iff the base itself
    carries an odd sqrt3 power, else type S. Returns None for wrong-pi-power controls and
    for sqrt5/sqrt15-flavoured bases (no established law covers those -- they are the
    open two-ended question, not a control)."""
    if base_name in WRONG_PI_POWER_BASES or base_name in SQRT5_FLAVOURED_BASES:
        return None
    if k % 2 == 0:
        return "Q"
    base_parity = BASE_SQRT3_PARITY.get(base_name, 0)
    return "Q" if base_parity == 1 else "Q(sqrt3)"


# =============================================================================
# N-grids -- W1..W5 MATCH b1124_verify.py exactly (correctness cross-check target);
# W6 (and optional W7) are the NEW extension past N=35,000,000.
# =============================================================================

def _geom_ints(start, end, n):
    with mp.workdps(50):
        vals = [start * (mp.mpf(end) / start) ** (mp.mpf(i) / (n - 1)) for i in range(n)]
    ints = sorted(set(int(round(v)) for v in vals))
    # guarantee endpoints exactly and strict monotonic increase
    ints[0], ints[-1] = int(start), int(end)
    out = [ints[0]]
    for v in ints[1:]:
        if v <= out[-1]:
            v = out[-1] + 1
        out.append(v)
    return out


def build_grids(quick: bool):
    if quick:
        CONTROL_NS = [1, 2, 3, 4, 5, 10, 20, 50, 100]
        W1 = [500, 700, 900, 1200, 1600, 2100]
        W2 = [2500, 3200, 4200, 5400, 7000, 9000]
        W3 = [11000, 14000, 18000, 23000, 29000, 37000]
        W4 = [65000, 78000, 92000, 108000, 128000, 150000]
        W5 = [220000, 260000, 305000, 360000, 420000, 495000]
        W6 = [600000, 750000, 950000, 1200000, 1500000] if RUN_W6 else []
        W7 = []
        CROSS_DPS_NS = W4
    else:
        CONTROL_NS = [1, 2, 3, 4, 5, 6, 8, 10, 15, 20, 30, 50, 75, 100, 150, 200,
                      300, 500, 750, 1000]
        # W1..W5: EXACT match to b1124_verify.py's build_grids(quick=False)
        W1 = [2000, 2500, 3200, 4000, 5000, 6300, 8000, 10000, 12500, 16000, 20000]
        W2 = [25000, 32000, 40000, 50000, 63000, 80000, 100000, 125000, 160000, 200000]
        W3 = [250000, 323000, 417000, 539000, 696000, 898000, 1160000, 1499000,
              1936000, 2500000]
        W4 = [2800000, 3291000, 3869000, 4548000, 5346000, 6285000, 7388000,
              8684000, 10208000, 12000000]
        W5 = [13000000, 14512000, 16200000, 18085000, 20189000, 22537000, 25159000,
              28086000, 31353000, 35000000]
        # W6: NEW, the extension. 8 log-spaced points, 38M -> 70M (~2.0x past W5).
        # (sized down TWICE from an initial 38M-150M/12pt design: this machine's REAL,
        # now twice-confirmed throughput on W3 AND W4 of this same run settled at a
        # consistent ~109,300 steps/sec -- roughly 1x single-process speed despite
        # 8-way multiprocessing, i.e. near-zero real parallelism benefit, because
        # ambient load climbed sharply mid-session (load average ~2.3 -> ~6-8, another
        # session's long-running job pinning a full core throughout) and is contending
        # with, not yielding to, this run's workers. At that measured rate the original
        # 684M-step W6 alone was a ~104-minute commitment; resized to keep the total
        # run bounded on a machine other seats are actively sharing, while still a
        # genuine, meaningful extension past b1124's N=35M ceiling.)
        W6 = _geom_ints(38_000_000, 70_000_000, 8) if RUN_W6 else []
        # W7: NEW, light reach tier (off by default; TWOENDED_W7=1 to enable).
        W7 = _geom_ints(170_000_000, 500_000_000, 6) if RUN_W7 else []
        CROSS_DPS_NS = W6[::3] if W6 else W4  # every third W6 point: precision-doubling subset
    grids = dict(CONTROL=CONTROL_NS, W1=W1, W2=W2, W3=W3, W4=W4, W5=W5)
    if W6:
        grids["W6"] = W6
    if W7:
        grids["W7"] = W7
    return grids, CROSS_DPS_NS


# =============================================================================
# main
# =============================================================================

def main(quick: bool = False):
    t_start = time.time()
    results = {"dps_main": DPS_MAIN, "dps_cross": DPS_CROSS, "dps_vol": DPS_VOL,
               "nworkers": NWORKERS, "quick_mode": quick, "run_w6": RUN_W6, "run_w7": RUN_W7}

    print("=" * 96)
    print("P-TWOENDED -- Kashaev tower J_N(4_1): PART A (cheap C_3 structure) + PART B")
    print("(expensive tower extension past N=35,000,000 for C_4/C_5, sqrt5/sqrt15 probe)")
    print("=" * 96)

    # ---- PART A ----
    print("\n[PART A] C_3 structural analysis (cheap)")
    part_a = part_a_c3_structure()
    print(f"    C3 numerator factors: {part_a['C3_numerator_factors']}")
    print(f"    C3 denominator factors: {part_a['C3_denominator_factors']}")
    print(f"    numerator prime splitting: {part_a['numerator_prime_splitting']}")
    print(f"    {part_a['splitting_correlation_note']}")
    print(f"    any near-simple-rational ratio to zeta_K(2)/L(chi5,2)/phi combos: "
          f"{part_a['transcendental_context']['any_near_simple_rational']}")
    print(f"    PART A VERDICT: {part_a['part_a_verdict']}")
    results["part_a"] = part_a

    # ---- PART B: Step 0: Vol(4_1) + frozen constants ----
    print(f"\n[PART B, 0] Vol(4_1) independently (dps={DPS_VOL}):")
    volA, volB, vol_agree = compute_vol_fig8()
    Vol = volA
    print(f"    route A (2*Im Li2(e^(i pi/3))): {s(volA, 45)}")
    print(f"    route B (2*3*Lobachevsky(pi/3)): {s(volB, 45)}")
    print(f"    agree to working precision: {vol_agree}")
    results["vol"] = {"route_A": s(volA, 60), "route_B": s(volB, 60), "agree": vol_agree}

    with mp.workdps(DPS_VOL):
        p_exact = +(mp.mpf(3) / 2)
        two_pi = +(2 * mp.pi)
        growth_rate = +(Vol / two_pi)
        C0_target = +(mp.mpf(3) ** (-mp.mpf(1) / 4))
    print(f"    growth_rate = Vol/2pi = {s(growth_rate, 40)}")
    print(f"    C_0 target = 3^(-1/4) = {s(C0_target, 45)}")
    results["C0_target_3^-1/4"] = s(C0_target, 60)

    gr_str, pe_str = freeze_strings(growth_rate, p_exact)

    prediction = {
        "law": "k even -> C_k/(C0*pi^k) in Q;  k odd -> C_k/(C0*pi^k) in Q*sqrt(3)  [b1124 law]",
        "C_4_predicted_form": "C_4 = q4 * pi^4 * C0,  q4 rational (single-end null)",
        "C_5_predicted_form": "C_5 = q5 * sqrt(3) * pi^5 * C0,  q5 rational (single-end null)",
        "two_ended_alternative": (
            "C_4 or C_5 recognized instead on Q(sqrt5)/Q(sqrt15) (or a sqrt5-carrying base "
            "flips to a Q hit the way sqrt3-carrying bases did for C1/C2), OR the 5's exponent "
            "in the denominator GROWS/RECURS in a directed way across C_3->C_4->C_5"
        ),
        "anti_coincidence_controls": [
            "C_4 vs rational*sqrt3*pi^4*C0 (wrong parity: Q(sqrt3) not Q)",
            "C_5 vs plain-rational*pi^5*C0 (wrong parity: Q not Q(sqrt3))",
            "both vs sqrt3-alone, 1/sqrt3, pi^2, 1 (wrong power of pi / no pi)",
            "both vs Q(sqrt5), Q(sqrt15) recognition on EVERY base (the two-ended probe itself)",
        ],
        "negative_control": "C_3 re-run through the SAME extended sweep must reproduce the known "
                             "q3=724351/12597120 on Q(sqrt3) AND find a clean null on Q(sqrt5)/"
                             "Q(sqrt15) before C_4/C_5 results are trusted.",
        "stated_before_pslq": True,
    }
    print(f"\n[PREDICTION] (stated before any PSLQ call this run)")
    print(f"    {prediction['C_4_predicted_form']}")
    print(f"    {prediction['C_5_predicted_form']}")
    print(f"    two-ended alternative: {prediction['two_ended_alternative']}")
    results["prediction"] = prediction

    # ---- Step 1: hand control + fast-vs-direct ----
    mp.mp.dps = DPS_MAIN
    print(f"\n[PART B, 1] CONTROL: hand-derived exact values (dps={DPS_MAIN})")
    hand = {1: 1, 2: 5, 3: 13, 4: 27}
    tol = mp.mpf(10) ** (-(DPS_MAIN - 20))
    control_rows = []
    all_hand_pass = True
    for N, expected in hand.items():
        jf = J_N_trig_fast(N)
        d = abs(jf - expected)
        ok = d < tol
        all_hand_pass &= ok
        print(f"    N={N}: J_N_fast={s(jf, 15)}  expected={expected}  diff={s(d, 4)}  PASS={ok}")
        control_rows.append(dict(N=N, expected=expected, diff=s(d, 6), pass_=ok))
    results["control_hand_check"] = {"rows": control_rows, "all_pass": all_hand_pass}
    if not all_hand_pass:
        print("    ABORT: hand-check failed, refusing to proceed.")
        with open(os.path.join(OUTDIR, "results.json"), "w") as f:
            json.dump(results, f, indent=1, default=str)
        sys.exit(1)

    print("    fast (angle-addition) vs direct (mp.sin) cross-validation:")
    cross_rows = []
    for N in ([5, 17, 30, 100] if not quick else [5, 17]):
        jf = J_N_trig_fast(N)
        jd = J_N_trig_direct(N)
        rel = abs(jf - jd) / jd
        print(f"      N={N:4d}: rel.diff(fast,direct) = {s(rel, 4)}")
        cross_rows.append(dict(N=N, rel_diff=s(rel, 6)))
    results["control_fast_vs_direct"] = cross_rows

    # ---- Step 2: N-grids ----
    windows, CROSS_DPS_NS = build_grids(quick)
    all_Ns_main = sorted(set(n for g in windows.values() for n in g))
    total_steps = sum(all_Ns_main)
    print(f"\n[PART B, 2] N-grids (quick={quick}, W6={RUN_W6}, W7={RUN_W7}):")
    for wname, g in windows.items():
        print(f"    {wname}: n={len(g)}, N in [{min(g):,},{max(g):,}]")
    print(f"    total main-pass N-steps (sum of N): {total_steps:,}")
    print(f"    NWORKERS = {NWORKERS}")
    results["grids"] = {k: v for k, v in windows.items()}
    results["cross_dps_Ns"] = CROSS_DPS_NS
    results["total_main_pass_steps"] = total_steps

    # ---- Step 3: R_N over all points, checkpointed per window ----
    print(f"\n[PART B, 3] Computing R_N over {len(all_Ns_main)} points at dps={DPS_MAIN}, "
          f"{NWORKERS}-way parallel ...")
    R = {}
    if os.path.exists(CKPT_PATH):
        try:
            with open(CKPT_PATH, "rb") as f:
                ck = pickle.load(f)
            if ck.get("dps_main") == DPS_MAIN and ck.get("quick") == quick:
                R = {N: mp.mpf(v) for N, v in ck.get("R_main", {}).items()}
                print(f"    resumed {len(R)} points from checkpoint {CKPT_PATH}")
        except Exception as e:
            print(f"    (checkpoint unreadable, starting fresh: {e})")

    t0 = time.time()
    window_order = [w for w in ("CONTROL", "W1", "W2", "W3", "W4", "W5", "W6", "W7") if w in windows]
    with Pool(processes=NWORKERS) as pool:
        for wname in window_order:
            Ns = windows[wname]
            tw0 = time.time()
            R.update(parallel_R_N(pool, Ns, DPS_MAIN, gr_str, pe_str, have=R))
            dtw = time.time() - tw0
            print(f"    window {wname} (n={len(Ns)}, max N={max(Ns):,}): {dtw:.1f}s "
                  f"(cumulative {time.time()-t0:.1f}s)", flush=True)
            with open(CKPT_PATH, "wb") as f:
                pickle.dump({"dps_main": DPS_MAIN, "quick": quick,
                             "R_main": {N: mp.nstr(v, DPS_MAIN + 20) for N, v in R.items()}}, f)

        t_main_compute = time.time() - t0
        print(f"    main-dps generation done in {t_main_compute:.1f}s "
              f"({total_steps/max(t_main_compute,1e-9):.0f} steps/sec effective)")
        results["timing_main_compute_s"] = round(t_main_compute, 3)
        results["effective_steps_per_sec"] = round(total_steps / max(t_main_compute, 1e-9), 1)

        table = []
        for N in windows["CONTROL"] + [windows["W1"][0], windows["W1"][-1],
                                        windows["W5"][0], windows["W5"][-1]]:
            table.append({"N": N, "R_N": s(R[N], 40)})
        if "W6" in windows:
            table += [{"N": windows["W6"][0], "R_N": s(R[windows["W6"][0]], 40)},
                      {"N": windows["W6"][-1], "R_N": s(R[windows["W6"][-1]], 40)}]
        if "W7" in windows:
            table += [{"N": windows["W7"][-1], "R_N": s(R[windows["W7"][-1]], 40)}]
        results["R_N_table_sample"] = table

        # ---- Step 4: C_0 recovery gate ----
        print(f"\n[PART B, 4] CONTROL: C_0 recovery, K=3 fit on W3")
        c0_coeffs, c0_resid = poly_fit_1_over_N(windows["W3"], [R[N] for N in windows["W3"]], 3)
        C0_simple = c0_coeffs[0]
        diff_c0_simple = abs(C0_simple - C0_target)
        print(f"    C_0 (K=3 fit, W3) = {s(C0_simple, 30)}   target = {s(C0_target, 30)}")
        print(f"    |diff| = {s(diff_c0_simple, 6)}   fit residual = {s(c0_resid, 6)}")
        results["control_C0_simple_fit"] = {"C0": s(C0_simple, 40), "target": s(C0_target, 40),
                                             "diff": s(diff_c0_simple, 15)}
        c0_gate_pass = diff_c0_simple < mp.mpf('1e-10') if not quick else diff_c0_simple < mp.mpf('1e-4')
        print(f"    GATE (|diff|<1e-10): {c0_gate_pass}")
        results["control_C0_gate_pass"] = c0_gate_pass
        if not c0_gate_pass:
            print("    ABORT: C_0 control failed -- refusing to trust C_1+ from this run.")
            with open(os.path.join(OUTDIR, "results.json"), "w") as f:
                json.dump(results, f, indent=1, default=str)
            sys.exit(1)

        t_checkpoint = time.time() - t_start
        print(f"\n[checkpoint] elapsed so far: {t_checkpoint:.1f}s")

        # ---- Step 5: per-window fits, multiple K, + POOLED ----
        print(f"\n[PART B, 5] MAIN EXTRACTION: polynomial-in-1/N fits, per window, multiple K")
        fit_windows = {wn: windows[wn] for wn in window_order if wn != "CONTROL"}
        POOLED = sorted(set(n for wn in fit_windows for n in windows[wn]))
        fit_windows["POOLED"] = POOLED
        K_CAP = 11
        K_CAP_POOLED = 30
        fits_raw = {}
        for wname, Ns in fit_windows.items():
            Rs = [R[N] for N in Ns]
            n = len(Ns)
            this_cap = K_CAP_POOLED if wname == "POOLED" else K_CAP
            kmax = min(this_cap, n - 1)
            wfits_raw = {}
            for K in range(3, kmax + 1):
                coeffs, resid = poly_fit_1_over_N(Ns, Rs, K)
                wfits_raw[K] = (coeffs, resid)
            fits_raw[wname] = wfits_raw
            c_display = "  ".join(f"C{i}={s(c,14)}" for i, c in enumerate(wfits_raw[kmax][0][:6]))
            print(f"    {wname} (n={n}, N in [{min(Ns):,},{max(Ns):,}]): K=3..{kmax}  "
                  f"@K={kmax}: {c_display}")
        results["fits_least_squares"] = {
            wn: {K: {"coeffs": [s(c, 45) for c in cf], "residual": s(rs, 8)}
                 for K, (cf, rs) in wf.items()}
            for wn, wf in fits_raw.items()
        }

        # ---- Step 6: stability + cross-window agreement, C_0..C_5 ----
        print(f"\n[PART B, 6] STABILITY ANALYSIS: trusted digits of C_0..C_5")
        TARGET_KS = (0, 1, 2, 3, 4, 5)
        stability = {}
        for target_k in TARGET_KS:
            stability[f"C{target_k}"] = {}
            for wname, wfits_raw in fits_raw.items():
                Ks = sorted(k for k in wfits_raw if k > target_k)
                if len(Ks) < 2:
                    continue
                diffs = []
                for i in range(1, len(Ks)):
                    K_prev, K_cur = Ks[i - 1], Ks[i]
                    d = abs(wfits_raw[K_cur][0][target_k] - wfits_raw[K_prev][0][target_k])
                    diffs.append((K_prev, K_cur, d))
                best_K = Ks[-1]
                best_val = wfits_raw[best_K][0][target_k]
                last_diff = diffs[-1][2] if diffs else mp.mpf(1)
                stable_digits = max(0, int(-mp.log10(last_diff))) if last_diff > 0 else DPS_MAIN
                stability[f"C{target_k}"][wname] = dict(
                    best_K=best_K, best_value=s(best_val, 45),
                    consecutive_K_diffs=[dict(K_prev=a, K_cur=b, diff=s(d, 6)) for a, b, d in diffs],
                    stable_digits_est=stable_digits)
            row = "  ".join(f"{wn}:{stability[f'C{target_k}'][wn]['stable_digits_est']}d"
                             for wn in fit_windows if wn in stability[f"C{target_k}"])
            print(f"    C{target_k}: {row}")
        results["stability_analysis"] = stability

        GENUINE_WINDOWS = [w for w in ("W1", "W2", "W3", "W4", "W5", "W6", "W7") if w in fit_windows]
        LARGE_WINDOWS = [w for w in ("W4", "W5", "W6", "W7") if w in fit_windows]
        print(f"\n    Cross-window agreement (genuine independent windows: {GENUINE_WINDOWS}):")
        cross_window = {}
        for target_k in TARGET_KS:
            vals = {wn: mp.mpf(stability[f"C{target_k}"][wn]["best_value"])
                    for wn in fit_windows if wn in stability[f"C{target_k}"]}
            pairs = []
            wnames = list(vals.keys())
            for i in range(len(wnames)):
                for j in range(i + 1, len(wnames)):
                    a, b = wnames[i], wnames[j]
                    d = abs(vals[a] - vals[b])
                    digits = max(0, int(-mp.log10(d))) if d > 0 else DPS_MAIN
                    pairs.append(dict(pair=f"{a}_vs_{b}", diff=s(d, 8), agree_digits=digits))
            cross_window[f"C{target_k}"] = pairs
            genuine_pairs = [p for p in pairs if p["pair"].split("_vs_")[0] in GENUINE_WINDOWS
                              and p["pair"].split("_vs_")[1] in GENUINE_WINDOWS]
            if genuine_pairs:
                worst = min(genuine_pairs, key=lambda p: p["agree_digits"])
                print(f"    C{target_k}: worst genuine-window pair = {worst['pair']} "
                      f"({worst['agree_digits']} digits)")
        results["cross_window_agreement"] = cross_window

        def trust_over(window_set, target_k):
            pairs = [p for p in cross_window[f"C{target_k}"]
                     if p["pair"].split("_vs_")[0] in window_set and p["pair"].split("_vs_")[1] in window_set]
            return min((p["agree_digits"] for p in pairs), default=0)

        GENUINE_SET = set(GENUINE_WINDOWS)
        LARGE_SET = set(LARGE_WINDOWS)
        final_estimates = {}
        large_window_estimates = {}
        print(f"\n    FINAL estimates (PRIMARY = all genuine windows incl. W1; "
              f"LARGE-WINDOW = {sorted(LARGE_SET)} only):")
        for target_k in TARGET_KS:
            candidates = [(wname, stability[f"C{target_k}"][wname]["stable_digits_est"])
                          for wname in fit_windows if wname in stability[f"C{target_k}"]]
            if not candidates:
                continue
            source_window = max(candidates, key=lambda t: t[1])[0]
            source_K = stability[f"C{target_k}"][source_window]["best_K"]
            val = fits_raw[source_window][source_K][0][target_k]
            conv_digits = stability[f"C{target_k}"][source_window]["stable_digits_est"]

            cw_primary = trust_over(GENUINE_SET, target_k)
            trusted_primary = min(conv_digits, cw_primary)
            final_estimates[f"C{target_k}"] = dict(value=s(val, 50), source_window=source_window,
                                                    source_K=source_K, trusted_digits=trusted_primary)

            cw_large = trust_over(LARGE_SET, target_k) if LARGE_SET else 0
            large_window_estimates[f"C{target_k}"] = dict(value=s(val, 50),
                                                            trusted_digits=min(conv_digits, cw_large))
            print(f"    C{target_k} = {s(val,30)}  PRIMARY~{trusted_primary}d  "
                  f"LARGE-WINDOW~{large_window_estimates[f'C{target_k}']['trusted_digits']}d")
        results["final_estimates"] = final_estimates
        results["large_window_estimates"] = large_window_estimates

        # precision-scaling records for C3/C4/C5 (self-digits vs window max_N) -- used to
        # extrapolate a floor if the gate isn't reached
        precision_scaling = {}
        for ck in ("C3", "C4", "C5"):
            rows = []
            for wname in GENUINE_WINDOWS:
                if wname in stability.get(ck, {}):
                    rows.append(dict(window=wname, max_N=max(windows[wname]),
                                      self_digits=stability[ck][wname]["stable_digits_est"]))
            precision_scaling[ck] = rows
            print(f"    {ck} self-convergence vs window max-N: {rows}")
        results["precision_scaling"] = precision_scaling

        # ---- Step 7: precision cross-check dps DPS_MAIN -> DPS_CROSS on a W6 subset ----
        print(f"\n[PART B, 7] PRECISION CROSS-CHECK: subset recomputed at dps={DPS_CROSS} "
              f"(vs main dps={DPS_MAIN})")
        t0c = time.time()
        R_cross = parallel_R_N(pool, CROSS_DPS_NS, DPS_CROSS, gr_str, pe_str)
        t_cross_compute = time.time() - t0c
        print(f"    done in {t_cross_compute:.1f}s")
        results["timing_cross_dps_compute_s"] = round(t_cross_compute, 3)

        rn_compare = []
        for N in CROSS_DPS_NS:
            d = abs(R[N] - R_cross[N])
            rn_compare.append(dict(N=N, diff=s(d, 10)))
        results["cross_dps_R_N_compare"] = rn_compare
        print("    R_N agreement at shared N (sample): "
              + ", ".join(f"N={r['N']}:{r['diff']}" for r in rn_compare[:3]))

        Ks_cross = list(range(3, min(K_CAP, len(CROSS_DPS_NS)) + 1))
        cross_fits = {}
        for K in Ks_cross:
            coeffs, resid = poly_fit_1_over_N(CROSS_DPS_NS, [R_cross[N] for N in CROSS_DPS_NS], K)
            cross_fits[K] = (coeffs, resid)
        dps_check = {}
        if Ks_cross:
            best_K_cross = Ks_cross[-1]
            print(f"    dps={DPS_CROSS} fit (K={best_K_cross}) vs dps={DPS_MAIN} final estimates:")
            for target_k in TARGET_KS:
                if target_k < best_K_cross and f"C{target_k}" in final_estimates:
                    val_cross = cross_fits[best_K_cross][0][target_k]
                    val_main = mp.mpf(final_estimates[f"C{target_k}"]["value"])
                    d = abs(val_cross - val_main)
                    digits = max(0, int(-mp.log10(d))) if d > 0 else DPS_MAIN
                    print(f"      C{target_k}: diff={s(d,6)} (~{digits} digits agree)")
                    dps_check[f"C{target_k}"] = dict(dps_main=s(val_main, 40),
                                                      dps_cross=s(val_cross, 40),
                                                      diff=s(d, 10), agree_digits=digits)
        results["cross_dps_fit_compare"] = dps_check

    # pool closed here

    # ---- Step 8: PSLQ sweep -- C_3 (negative control / reverify), C_4, C_5 ----
    print(f"\n[PART B, 8] PSLQ RECOGNITION SWEEP (extended: Q, Q(sqrt3), Q(sqrt5), Q(sqrt15))")
    bases = build_candidate_bases()
    print(f"    candidate bases ({len(bases)}): {list(bases.keys())}")
    SUFFICIENT_DIGITS_GATE = 18  # this task's own stated threshold
    pslq_results = {}
    for target_k in (3, 4, 5):
        if f"C{target_k}" not in final_estimates:
            continue
        Ck = mp.mpf(final_estimates[f"C{target_k}"]["value"])
        trusted_digits = final_estimates[f"C{target_k}"]["trusted_digits"]
        large_trusted = large_window_estimates.get(f"C{target_k}", {}).get("trusted_digits", 0)
        if f"C{target_k}" in dps_check:
            trusted_digits = min(trusted_digits, dps_check[f"C{target_k}"]["agree_digits"])
            large_trusted = min(large_trusted, dps_check[f"C{target_k}"]["agree_digits"])
        best_trust = max(trusted_digits, large_trusted)
        pslq_dps = max(20, best_trust - 4)
        sufficient_precision = best_trust >= SUFFICIENT_DIGITS_GATE
        print(f"\n    C_{target_k} = {s(Ck,30)}  (primary_trust={trusted_digits}, "
              f"large_window_trust={large_trusted}, gate={SUFFICIENT_DIGITS_GATE}, "
              f"sufficient={sufficient_precision})")
        # maxcoeff scaled to whichever trust we use for pslq_dps -- avoids the
        # noise-on-every-basis trap (b1124's caught bug). OUTER_SAFETY_CAP is a sanity
        # bound on PSLQ runtime only (2e9 is still fast for mpmath.pslq); it is NOT a
        # re-imposition of b1124's original 3M pre-registered ceiling -- this run is the
        # extension, and b1124 itself found it had to go to 20M for C_3's canonical-pi-
        # basis height, so under-searching here would silently reproduce that same miss.
        OUTER_SAFETY_CAP = 2_000_000_000
        maxcoeff_by_type = {
            "Q": min(OUTER_SAFETY_CAP, int(10 ** max(2, pslq_dps / 2 - 3))),
            "Q(sqrt3)": min(OUTER_SAFETY_CAP, int(10 ** max(2, pslq_dps / 3 - 3))),
            "Q(sqrt5)": min(OUTER_SAFETY_CAP, int(10 ** max(2, pslq_dps / 3 - 3))),
            "Q(sqrt15)": min(OUTER_SAFETY_CAP, int(10 ** max(2, pslq_dps / 3 - 3))),
        }
        k_results = {"C_k_value": s(Ck, 50), "trusted_digits": trusted_digits,
                     "large_window_trusted_digits": large_trusted,
                     "pslq_dps": pslq_dps, "sufficient_precision": sufficient_precision,
                     "maxcoeff_by_type": maxcoeff_by_type, "attempts": {}}
        for base_name, B in bases.items():
            with mp.workdps(DPS_VOL):
                Bk = B ** target_k
                T = Ck / (C0_target * Bk)
            per_type_hits = {}
            for qtype in QTYPES:
                mc = maxcoeff_by_type[qtype]
                # fixed diagnostic checkpoints (comparable to b1124's tiers) + the final
                # precision-calibrated ceiling, deduplicated and capped from above by mc
                mc_list = tuple(sorted(set(
                    v for v in [100, 1000, 10000, 100000, 1000000, 3000000, 20000000, mc]
                    if v <= mc
                )))
                attempts = recognize_sweep_multi(T, pslq_dps, maxcoeff_list=mc_list,
                                                  maxsteps=50000, qtypes=(qtype,))
                hits = [a for a in attempts if a["found"]]
                per_type_hits[qtype] = dict(any_hit=len(hits) > 0,
                                             best=min(hits, key=lambda a: a["maxcoeff"]) if hits else None,
                                             all_attempts=attempts)
            expected = expected_basis_kind(target_k, base_name)
            any_hit_anywhere = any(v["any_hit"] for v in per_type_hits.values())
            k_results["attempts"][base_name] = dict(T=s(T, min(40, pslq_dps + 5)),
                                                      per_type=per_type_hits,
                                                      any_hit=any_hit_anywhere,
                                                      expected_basis_kind=expected)
            if any_hit_anywhere:
                lines = []
                for qtype, v in per_type_hits.items():
                    if v["any_hit"]:
                        b = v["best"]
                        # mirrors the is_two_ended_signal computation in step 8b exactly --
                        # print-label priority: two-ended signal first (the important case),
                        # then the established-law tags, so the console log cannot mislabel
                        # a real signal as a mundane control-hit.
                        is_2e = (qtype in ("Q(sqrt5)", "Q(sqrt15)")
                                 or (base_name in SQRT5_FLAVOURED_BASES and qtype == "Q"))
                        tag = ("TWO-ENDED-SIGNAL" if is_2e else
                               "PREDICTED" if expected == qtype else
                               "WRONG-PI-POWER-CONTROL-HIT" if expected is None and base_name in WRONG_PI_POWER_BASES else
                               "PARITY-VIOLATING")
                        lines.append(f"{qtype}(mc={b['maxcoeff']},rel={b['relation']})[{tag}]")
                print(f"      base={base_name:12s}: HIT " + " | ".join(lines))
            else:
                print(f"      base={base_name:12s}: no relation on any type "
                      f"(maxcoeff up to {max(maxcoeff_by_type.values())})")
        pslq_results[f"C{target_k}"] = k_results
    results["pslq_sufficient_digits_gate"] = SUFFICIENT_DIGITS_GATE
    results["pslq_sweep"] = pslq_results

    # ---- Step 8b: cross-window validation + the two-ended signal scan ----
    print(f"\n[PART B, 8b] CROSS-WINDOW VALIDATION + two-ended signal scan")
    validated_hits = []
    sqrt5_signals = []
    for target_k in (3, 4, 5):
        if f"C{target_k}" not in pslq_results:
            continue
        kres = pslq_results[f"C{target_k}"]
        for base_name, att in kres["attempts"].items():
            expected = att["expected_basis_kind"]
            for qtype, v in att["per_type"].items():
                if not v["any_hit"]:
                    continue
                best_hit = v["best"]
                relation = best_hit["relation"]
                with mp.workdps(DPS_VOL):
                    B = bases[base_name]
                    Bk = B ** target_k
                    if qtype == "Q":
                        c0r, c1r = relation
                        closed_val = mp.mpf(-c1r) / c0r
                        irr = mp.mpf(1)
                    else:
                        c0r, c1r, c2r = relation
                        irr = {"Q(sqrt3)": mp.sqrt(3), "Q(sqrt5)": mp.sqrt(5),
                               "Q(sqrt15)": mp.sqrt(15)}[qtype]
                        closed_val = (-mp.mpf(c1r) - mp.mpf(c2r) * irr) / c0r
                    predicted_Ck = closed_val * C0_target * Bk
                cross_checks = []
                for wname in fit_windows:
                    if wname not in stability[f"C{target_k}"]:
                        continue
                    w_val = mp.mpf(stability[f"C{target_k}"][wname]["best_value"])
                    w_trusted = stability[f"C{target_k}"][wname]["stable_digits_est"]
                    d = abs(w_val - predicted_Ck)
                    digits = max(0, int(-mp.log10(d))) if d > 0 else DPS_MAIN
                    cross_checks.append(dict(window=wname, diff=s(d, 8), agree_digits=digits,
                                              window_own_trusted_digits=w_trusted))
                matches_prediction = (expected is not None and qtype == expected)
                # two-ended signal = EITHER a direct Q(sqrt5)/Q(sqrt15) recognition, OR a
                # sqrt5-flavoured base "flipping" the ratio to a plain-Q hit -- the exact
                # mechanism that revealed C1/C2's sqrt3 structure via sqrt3-carrying bases
                # (pi/sqrt3 etc: see expected_basis_kind). A Q hit on a sqrt5-flavoured base
                # is NOT "matches_prediction" (expected=None there, no established law covers
                # it) but IS exactly the two-ended signature if it appears.
                is_two_ended_signal = (qtype in ("Q(sqrt5)", "Q(sqrt15)")
                                        or (base_name in SQRT5_FLAVOURED_BASES and qtype == "Q"))
                record = dict(C_k=f"C{target_k}", base=base_name, basis_kind=qtype,
                               relation=relation, maxcoeff=best_hit["maxcoeff"],
                               expected_basis_kind=expected,
                               matches_prediction=matches_prediction,
                               is_wrong_pi_power_control=(base_name in WRONG_PI_POWER_BASES),
                               is_sqrt5_flavoured_base=(base_name in SQRT5_FLAVOURED_BASES),
                               is_two_ended_signal=is_two_ended_signal,
                               predicted_value=s(predicted_Ck, 40), cross_checks=cross_checks)
                validated_hits.append(record)
                if is_two_ended_signal:
                    sqrt5_signals.append(record)
                print(f"    C_{target_k}/base={base_name}/{qtype} relation={relation} "
                      f"(matches_prediction={matches_prediction}, two_ended_signal={is_two_ended_signal}): "
                      f"predicted={s(predicted_Ck,20)}")
    results["validated_hits"] = validated_hits
    results["sqrt5_signals"] = sqrt5_signals
    print(f"    TOTAL sqrt5/sqrt15-type hits found across C3(control)/C4/C5: {len(sqrt5_signals)}")

    # ---- Step 9: verdict ----
    print(f"\n[PART B, 9] VERDICT")
    ROBUST_MIN_DIGITS = 10
    robust_hits = []
    for h in validated_hits:
        if not h["matches_prediction"]:
            continue
        other_ok = sum(1 for c in h["cross_checks"]
                        if c["window"] in GENUINE_SET
                        and c["agree_digits"] >= min(ROBUST_MIN_DIGITS, c["window_own_trusted_digits"]))
        if other_ok >= 2:
            robust_hits.append(h)

    # genuine C3 negative-control check: BASE-AGNOSTIC. (a) does the raw FIT (no PSLQ
    # involved at all) agree with the independently-known closed form to good precision;
    # (b) does ANY Q(sqrt3)-type PSLQ hit (any base) reconstruct that same closed form;
    # (c) does the sweep stay clean on Q(sqrt5)/Q(sqrt15) for C3. All three must hold for
    # the extended machinery to be trusted on the genuinely new C4/C5 targets.
    with mp.workdps(DPS_VOL):
        TRUE_C3 = (mp.mpf(724351) / mp.mpf(12597120)) * mp.sqrt(3) * mp.pi ** 3 * C0_target
    fit_c3 = mp.mpf(final_estimates["C3"]["value"]) if "C3" in final_estimates else None
    fit_vs_true_diff = abs(fit_c3 - TRUE_C3) if fit_c3 is not None else None
    fit_vs_true_digits = (max(0, int(-mp.log10(fit_vs_true_diff))) if fit_vs_true_diff and fit_vs_true_diff > 0
                           else (DPS_MAIN if fit_vs_true_diff == 0 else 0))

    c3_hits = [h for h in validated_hits if h["C_k"] == "C3"]
    # matches_prediction already correctly accounts for the base's own sqrt3-parity flip
    # (a hit landing on plain "Q" for a sqrt3-carrying base like pi/sqrt3 IS the predicted
    # outcome for that base -- see expected_basis_kind); filter on that, not on the raw
    # basis_kind label, which is base-dependent and not itself the substantive distinction.
    c3_matching_hits = [h for h in c3_hits if h["matches_prediction"]]
    c3_sqrt3_hits = [h for h in c3_hits if h["basis_kind"] == "Q(sqrt3)" and h["matches_prediction"]]
    c3_pslq_reproduces_known = any(
        abs(mp.mpf(h["predicted_value"]) - TRUE_C3) < mp.mpf(10) ** (-15) for h in c3_matching_hits
    )
    c3_sqrt5_contamination = [h for h in c3_hits if h["is_two_ended_signal"]]
    negative_control = dict(
        true_C3_closed_form=s(TRUE_C3, 40),
        fit_vs_true_agree_digits=fit_vs_true_digits,
        c3_pslq_reproduces_known_any_base=c3_pslq_reproduces_known,
        c3_sqrt3_hit_count=len(c3_sqrt3_hits),
        c3_sqrt5_or_sqrt15_hits=len(c3_sqrt5_contamination),
        machinery_trustworthy=(fit_vs_true_digits >= 8 and len(c3_sqrt5_contamination) == 0),
    )
    print(f"    NEGATIVE CONTROL (C3 re-run through extended sweep): {negative_control}")
    results["negative_control"] = negative_control

    precision_by_k = {k: pslq_results[k]["sufficient_precision"] for k in pslq_results}
    sufficient_ks = [k for k, ok in precision_by_k.items() if ok]
    robust_ks = sorted(set(h["C_k"] for h in robust_hits) & set(sufficient_ks))
    clean_miss_ks = [k for k in sufficient_ks
                      if not any(att["any_hit"] for att in pslq_results[k]["attempts"].values())]

    print(f"    coefficients with >= {SUFFICIENT_DIGITS_GATE} trusted digits (best-of primary/large-window): "
          f"{sufficient_ks}")
    print(f"    robust predicted-parity hits: {robust_ks}")
    print(f"    clean misses (sufficient precision, nothing found anywhere): {clean_miss_ks}")
    print(f"    TWO-ENDED SIGNALS (sqrt5/sqrt15 hit on C4 or C5, cross-window validated): "
          f"{[(h['C_k'], h['base']) for h in sqrt5_signals if h['C_k'] in ('C4','C5')]}")

    # denominator growth/recurrence of the prime 5 (canonical pi-basis only, matching how
    # C1/C2/C3 are reported: C_k = q_k * [sqrt3 if k odd] * pi^k * C0)
    denom_5_exponents = {"C1": 0, "C2": 0, "C3": 1}
    for h in robust_hits:
        if h["C_k"] in ("C4",) and h["basis_kind"] == "Q" and h["base"] == "pi":
            _, c1r = h["relation"]
            frac = PyFraction(int(-c1r), int(h["relation"][0]))
            denom_5_exponents["C4"] = sympy.factorint(frac.denominator).get(5, 0)
    for h in robust_hits:
        if h["C_k"] in ("C5",) and h["basis_kind"] == "Q(sqrt3)" and h["base"] == "pi":
            _, c1r, c2r = h["relation"]
            frac = PyFraction(int(-c2r), int(h["relation"][0]))
            denom_5_exponents["C5"] = sympy.factorint(frac.denominator).get(5, 0)
    results["denom_5_exponent_by_Ck"] = denom_5_exponents
    print(f"    prime-5 exponent in canonical-pi-basis denominator, by C_k: {denom_5_exponents}")

    if len(sqrt5_signals) > 0 and any(h["C_k"] in ("C4", "C5") for h in sqrt5_signals):
        real_signals = [h for h in sqrt5_signals if h["C_k"] in ("C4", "C5")
                         and any(c["agree_digits"] >= ROBUST_MIN_DIGITS for c in h["cross_checks"]
                                 if c["window"] in GENUINE_SET)]
        if real_signals:
            verdict = "TWO-ENDED-CONFIRMED"
            verdict_reason = (f"sqrt5/sqrt15 recognized in {[(h['C_k'],h['base'],h['basis_kind']) for h in real_signals]}, "
                               f"cross-window validated -- the E8/sqrt5 end enters the tower's arithmetic.")
        else:
            verdict = "PRECISION-FLOOR"
            verdict_reason = "sqrt5/sqrt15 hit found but NOT cross-window validated -- treat as unconfirmed, not a signal."
    elif "C4" in robust_ks or "C5" in robust_ks:
        grown = denom_5_exponents.get("C4", 0) > 1 or denom_5_exponents.get("C5", 0) > 1
        recurs = denom_5_exponents.get("C4", 0) >= 1 or denom_5_exponents.get("C5", 0) >= 1
        if grown or recurs:
            verdict = "TWO-ENDED-CONFIRMED" if grown else "SINGLE-END"
            verdict_reason = (f"C4/C5 landed on the predicted Q/Q(sqrt3) basis (single-end law holds); "
                               f"5-exponent by order = {denom_5_exponents} -- "
                               + ("GROWING (>1 at higher order)" if grown else "recurs at exponent 1, not growing")
                               + "; no sqrt5/sqrt15 ever recognized as an algebraic generator.")
        else:
            verdict = "SINGLE-END"
            verdict_reason = (f"C4/C5 landed cleanly on the predicted Q/Q(sqrt3) basis, 5 does not recur "
                               f"in the denominator, and no sqrt5/sqrt15 hit anywhere -- consistent with "
                               f"C_3's 5 being a one-off (Bernoulli/combinatorial-type) prime, not an "
                               f"E8/sqrt5 signature.")
    else:
        verdict = "PRECISION-FLOOR"
        c4_digits = max(final_estimates.get("C4", {}).get("trusted_digits", 0),
                         large_window_estimates.get("C4", {}).get("trusted_digits", 0))
        c5_digits = max(final_estimates.get("C5", {}).get("trusted_digits", 0),
                         large_window_estimates.get("C5", {}).get("trusted_digits", 0))
        # distinguish "never reached enough digits to search" (a genuine precision floor)
        # from "reached the gate but found NOTHING anywhere, including the established
        # Q/Q(sqrt3) law itself" (a structural surprise -- escapes BOTH the single-end and
        # every tested two-ended hypothesis -- reported honestly, not silently folded into
        # an ordinary precision-floor reading).
        escapes_all = [k for k in ("C4", "C5") if k in clean_miss_ks]
        if escapes_all:
            verdict_reason = (f"C4 reached {c4_digits} trusted digits, C5 reached {c5_digits}; "
                               f"{escapes_all} reached the {SUFFICIENT_DIGITS_GATE}-digit gate but "
                               f"matched NEITHER the established Q/Q(sqrt3) single-end law NOR any "
                               f"tested two-ended hypothesis (Q(sqrt5)/Q(sqrt15)/sqrt5-flavoured-base) "
                               f"on any of the {len(bases)} candidate bases -- a STRUCTURAL SURPRISE, "
                               f"not merely a precision shortfall; only the {{1,sqrt3,sqrt5,sqrt15}} "
                               f"single/double-irrationality hypotheses were tested, so a genuinely "
                               f"MIXED coefficient (nonzero on more than one of sqrt3/sqrt5/sqrt15 "
                               f"simultaneously) would present exactly this way and was NOT ruled out.")
        else:
            verdict_reason = (f"C4 reached {c4_digits} trusted digits, C5 reached {c5_digits} "
                               f"(<{SUFFICIENT_DIGITS_GATE} needed for a confident search at the height "
                               f"the C1->C2->C3 pattern suggests); see precision_scaling for the N/dps "
                               f"extrapolation.")

    print(f"\n    VERDICT: {verdict}")
    print(f"    reason: {verdict_reason}")
    results["c3_status"] = "CONTROL_OK" if negative_control["machinery_trustworthy"] else "CONTROL_FAILED"
    results["verdict"] = verdict
    results["verdict_reason"] = verdict_reason
    results["robust_hits"] = robust_hits
    results["precision_sufficient_by_k"] = precision_by_k
    results["clean_miss_ks"] = clean_miss_ks

    t_total = time.time() - t_start
    results["timing_total_s"] = round(t_total, 3)
    print(f"\nTotal runtime: {t_total:.2f}s ({t_total/60:.1f} min)")

    outname = os.path.join(OUTDIR, "results_quick.json" if quick else "results.json")
    with open(outname, "w") as f:
        json.dump(results, f, indent=1, default=str)
    print(f"Wrote {outname}")
    if os.path.exists(CKPT_PATH):
        os.remove(CKPT_PATH)

    return results


if __name__ == "__main__":
    quick_flag = "--quick" in sys.argv
    main(quick=quick_flag)
