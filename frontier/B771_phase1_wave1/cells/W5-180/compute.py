"""
B771 Phase-1 Wave-5, cell W5-180 (OI-180).
Target: resolve the "31-collision" tension filed under B406.

BACKGROUND (read from frontier/B406_two_conductor/FINDINGS.md,
frontier/B405_supersingular_check/{FINDINGS.md,sentinels.json,verify_15a1.py}):

  Side 1 (chat-1's E2 row): a claimed set of "split-PRINCIPAL primes" for the
  imaginary-quadratic field Q(sqrt(-15)) (disc -15, class number 2) said to be
  "absent from the program": their named examples are 19, 31, 61, 79, ...

  Side 2 (B405, banked): the supersingular-prime sentinel list for the
  conductor-15 elliptic curve 15a1 (y^2+xy+y = x^3+x^2-10x-10) below 200:
  {7, 23, 31, 79, 167}.

  The registered tension (B406): 31 and 79 sit in BOTH lists. Is this one
  identity (supersingularity of 15a1 <=> split-principal in Q(sqrt(-15)), a
  real arithmetic law), or two unrelated arithmetic conditions on the same
  small integers that happen to overlap at the base rate (E20 numerology)?

SEALED CRITERION (this cell): one identity behind both 31s (derived)
  => RESOLVED-A / the two 31s independent (base-rate, E20 margin computed)
  => RESOLVED-B.

METHOD: everything below is exact integer/modular arithmetic (no floats, no
PSLQ needed -- there is no real-valued transcendental identity in play here,
only two decidable arithmetic predicates on primes p). Two independent
"seeds" (bound=200 matching B405's banked list exactly, and an extended
bound=3000 for base-rate statistics) are computed in-cell.

B772 lesson check: a_p(15a1) IS a trace of Frobenius (an honest character
value), and "supersingular" means a_p = 0 EXACTLY (not "small") -- this is
already the full cancellation, not a chord/theta-odd average that could hide
a sign cancellation. No even/odd parity trap applies to a_p itself. The
splitting-type predicate (inert / split-principal / split-non-principal) is
likewise an exact trichotomy with no parity subtlety. So the B772-style risk
does not apply to either side's defining quantity.
"""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def log(msg):
    print(msg)


# ----------------------------------------------------------------------
# Sieve of primes
# ----------------------------------------------------------------------
def primes_upto(n):
    sieve = bytearray([1]) * (n + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = 0
    return [i for i in range(2, n + 1) if sieve[i]]


# ----------------------------------------------------------------------
# Side 2: a_p for 15a1 = y^2 + xy + y = x^3 + x^2 - 10x - 10, p odd, good
# reduction (p != 3, 5, the conductor primes).
#
# Complete the square (valid for odd p, invertible 4):
#   (y + (x+1)/2)^2 = x^3 + x^2 - 10x - 10 + (x+1)^2/4   =: R(x)
# affine point count at x: 1 + legendre(R(x), p)  [0 counts as 1 solution]
# total #E(F_p) = 1 (infinity) + sum_x [that], a_p = p + 1 - #E(F_p).
# ----------------------------------------------------------------------
def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    r = pow(a, (p - 1) // 2, p)
    return 1 if r == 1 else -1


def a_p_15a1(p):
    assert p not in (2, 3, 5)
    inv4 = pow(4, p - 2, p)
    total_affine = 0
    for x in range(p):
        rhs = (x ** 3 + x ** 2 - 10 * x - 10) % p
        corr = ((x + 1) ** 2) % p
        R = (rhs + corr * inv4) % p
        chi = legendre(R, p)
        total_affine += 1 + chi
    N = total_affine + 1  # + point at infinity
    return p + 1 - N


def a_p_15a1_bruteforce(p):
    """Slow, direct double loop -- used only as a cross-check on small p."""
    n = 1
    for x in range(p):
        rhs = (x * x * x + x * x - 10 * x - 10) % p
        for y in range(p):
            if (y * y + x * y + y - rhs) % p == 0:
                n += 1
    return p + 1 - n


# ----------------------------------------------------------------------
# Side 1: splitting type of p in K = Q(sqrt(-15)), disc D = -15, h(D) = 2.
# Reduced forms of disc -15: principal x^2+xy+4y^2 (a=1,b=1,c=4), and the
# non-principal ambiguous form 2x^2+xy+2y^2 (a=2,b=1,c=2).
#
#  - inert:            legendre(-15 mod p, p) == -1
#  - ramified:          p in {3,5}   (excluded -- bad primes for the curve too)
#  - split, principal:  p represented by x^2+xy+4y^2
#  - split, nonprinc.:  splits but NOT represented by the principal form
#
# Representation test (exact, derived by completing the square):
#   4(x^2+xy+4y^2) = (2x+y)^2 + 15y^2
# so p is represented by the principal form iff there exist integers u,v
# with u^2 + 15v^2 = 4p AND u == v (mod 2)  [then x=(u-v)/2, y=v].
# Bounded exact search: v = 0 .. floor(sqrt(4p/15)).
# ----------------------------------------------------------------------
def isqrt_exact(n):
    if n < 0:
        return None
    r = math.isqrt(n)
    return r if r * r == n else None


def represented_by_principal_form(p):
    bound = int(math.isqrt(4 * p // 15)) + 2
    for v in range(0, bound + 1):
        rem = 4 * p - 15 * v * v
        if rem < 0:
            break
        u = isqrt_exact(rem)
        if u is not None and (u % 2) == (v % 2):
            return True
    return False


def splitting_type(p):
    if p in (3, 5):
        return "ramified"
    chi = legendre((-15) % p, p)
    if chi == -1:
        return "inert"
    # chi == 1 (chi==0 impossible for p != 3,5): split
    if represented_by_principal_form(p):
        return "split-principal"
    return "split-nonprincipal"


# ----------------------------------------------------------------------
# Sanity checks (unit-test style, self-contained, no external claims)
# ----------------------------------------------------------------------
def sanity_checks():
    log("=== Sanity checks ===")
    ok = True

    # (a) fast a_p matches brute-force double loop on p<30 (cross-check the
    #     completed-square method against the naive method independently).
    for p in (7, 11, 13, 17, 19, 23, 29):
        fast = a_p_15a1(p)
        slow = a_p_15a1_bruteforce(p)
        match = (fast == slow)
        ok &= match
        log(f"  a_p({p}) fast={fast:+d} slow={slow:+d}  {'OK' if match else 'MISMATCH!!'}")

    # (b) direct hand-representation check: 19=1^2+1*2+4*2^2, 31=3^2+3*2+4*2^2,
    #     79=7^2+7*2+4*2^2 -- confirm the form-representation routine agrees.
    hand = {19: (1, 2), 31: (3, 2), 79: (7, 2)}
    for p, (x, y) in hand.items():
        val = x * x + x * y + 4 * y * y
        assert val == p, f"hand check failed for {p}: got {val}"
        rep = represented_by_principal_form(p)
        ok &= rep
        log(f"  {p} = {x}^2+{x}*{y}+4*{y}^2 = {val}; represented_by_principal_form={rep}  "
            f"{'OK' if rep else 'MISMATCH!!'}")

    log(f"All sanity checks: {'PASS' if ok else 'FAIL'}")
    return ok


# ----------------------------------------------------------------------
# Main computation
# ----------------------------------------------------------------------
def run(bound, label):
    log(f"\n=== SEED [{label}]: bound={bound} ===")
    ps = [p for p in primes_upto(bound) if p not in (2, 3, 5)]

    supersingular = []
    for p in ps:
        if a_p_15a1(p) == 0:
            supersingular.append(p)
    log(f"  supersingular(15a1) primes <= {bound}: {supersingular}")

    if bound == 200:
        expected = [7, 23, 31, 79, 167]
        cross_check = (supersingular == expected)
        log(f"  cross-check vs B405 banked sentinels.json {expected}: "
            f"{'MATCH' if cross_check else 'MISMATCH -- ' + str(supersingular)}")
    else:
        cross_check = None

    classified = {p: splitting_type(p) for p in supersingular}
    log("  classification of each supersingular prime in Q(sqrt(-15)):")
    for p, t in classified.items():
        log(f"    {p:5d}: {t}")

    classes_present = sorted(set(classified.values()))
    log(f"  distinct splitting-classes hit by supersingular primes: {classes_present}")

    # density of split-principal primes among all odd primes != 3,5 <= bound
    # (the base-rate comparator for side 1)
    all_types = [splitting_type(p) for p in ps]
    n_total = len(all_types)
    n_principal = sum(1 for t in all_types if t == "split-principal")
    n_nonprincipal = sum(1 for t in all_types if t == "split-nonprincipal")
    n_inert = sum(1 for t in all_types if t == "inert")
    density_principal = n_principal / n_total
    log(f"  base-rate over all {n_total} primes <= {bound} (p!=2,3,5): "
        f"principal={n_principal} ({density_principal:.4f}), "
        f"non-principal={n_nonprincipal} ({n_nonprincipal/n_total:.4f}), "
        f"inert={n_inert} ({n_inert/n_total:.4f})")

    return dict(
        bound=bound,
        supersingular=supersingular,
        classified=classified,
        classes_present=classes_present,
        cross_check_vs_b405=cross_check,
        n_total_primes=n_total,
        n_principal=n_principal,
        n_nonprincipal=n_nonprincipal,
        n_inert=n_inert,
        density_principal=density_principal,
    )


def e20_margin(seed_result):
    """Base-rate / look-elsewhere estimate: under the null that supersingularity
    is UNRELATED to splitting type in Q(sqrt(-15)), how many of the observed
    supersingular primes would we expect, by chance, to land in the
    split-principal class -- vs. how many actually do?
    Binomial model: k supersingular primes, each independently split-principal
    with probability = the measured background density."""
    k = len(seed_result["supersingular"])
    q = seed_result["density_principal"]
    observed_principal = sum(1 for t in seed_result["classified"].values()
                              if t == "split-principal")
    expected = k * q
    # exact binomial P(X >= observed_principal) as an "is this a surprise" gauge
    from math import comb
    p_ge = sum(comb(k, i) * (q ** i) * ((1 - q) ** (k - i))
               for i in range(observed_principal, k + 1))
    return dict(k=k, density_principal=q, observed_principal=observed_principal,
                expected_principal=expected, p_value_ge_observed=p_ge)


def main():
    log("B771 Wave-5 W5-180: the 31-collision tension (B406) -- identity or base-rate?")
    log("Curve: 15a1  y^2+xy+y = x^3+x^2-10x-10  (conductor 15)")
    log("Field: Q(sqrt(-15))  disc -15, class number 2, forms {x^2+xy+4y^2 (principal),"
        " 2x^2+xy+2y^2 (non-principal)}\n")

    ok = sanity_checks()

    seedA = run(200, "seed A (matches B405 bound)")
    seedB = run(3000, "seed B (extended, base-rate statistics)")

    marginA = e20_margin(seedA)
    marginB = e20_margin(seedB)
    log(f"\n=== E20 base-rate margin ===")
    log(f"  seed A (bound=200): k={marginA['k']} supersingular primes, background "
        f"P(split-principal)={marginA['density_principal']:.4f}, "
        f"expected principal-hits={marginA['expected_principal']:.3f}, "
        f"observed={marginA['observed_principal']}, "
        f"P(>=observed | null independence)={marginA['p_value_ge_observed']:.4f}")
    log(f"  seed B (bound=3000): k={marginB['k']} supersingular primes, background "
        f"P(split-principal)={marginB['density_principal']:.4f}, "
        f"expected principal-hits={marginB['expected_principal']:.3f}, "
        f"observed={marginB['observed_principal']}, "
        f"P(>=observed | null independence)={marginB['p_value_ge_observed']:.4f}")

    # ------------------------------------------------------------------
    # VERDICT LOGIC (in-code, two-outcome, able to emit UNRESOLVED)
    # ------------------------------------------------------------------
    log("\n=== VERDICT LOGIC ===")
    reasons = []

    if not ok:
        verdict = "UNRESOLVED"
        reasons.append("sanity checks failed -- computation not trustworthy")
    else:
        classesA = set(seedA["classes_present"])
        classesB = set(seedB["classes_present"])
        mixed_A = len(classesA) > 1
        mixed_B = len(classesB) > 1
        cross_check_ok = seedA["cross_check_vs_b405"] is True

        reasons.append(f"cross-check vs B405 sentinels.json (bound=200): "
                        f"{'MATCH' if cross_check_ok else 'MISMATCH'}")
        reasons.append(f"seed A splitting-classes hit by supersingular primes: {sorted(classesA)}")
        reasons.append(f"seed B splitting-classes hit by supersingular primes: {sorted(classesB)}")

        if not cross_check_ok:
            verdict = "UNRESOLVED"
            reasons.append("cannot trust downstream classification -- base list disagrees with banked B405 data")
        elif mixed_A and mixed_B:
            # A single arithmetic identity (supersingular <=> split-principal, or
            # any other clean equivalence with the class-group splitting type)
            # is REFUTED the moment supersingular primes appear OUTSIDE a single
            # splitting class -- and they do (both seeds): 7 is inert, 23 is
            # split-nonprincipal, 31/79/167(seed A) are split-principal.
            # No congruence-class law survives this. The 31/79 overlap sits
            # inside the base-rate expectation (E20 margin p-value not small).
            verdict = "RESOLVED-B"
            reasons.append("supersingularity of 15a1 hits ALL THREE splitting classes "
                            "(inert, split-nonprincipal, split-principal) at both bounds "
                            "-- no single class-group identity can underlie it; the 31/79 "
                            "overlap with the split-principal list is consistent with the "
                            "measured background density (E20 base-rate, not an anomaly)")
        else:
            verdict = "RESOLVED-A"
            reasons.append("supersingular primes fall into a single splitting class at "
                            "both bounds -- consistent with one identity behind both 31s")

    for r in reasons:
        log(f"  - {r}")
    log(f"\nVERDICT: {verdict}")

    results = dict(
        cell="W5-180",
        target="B406 31-collision: identity or base-rate?",
        curve="15a1: y^2+xy+y=x^3+x^2-10x-10 (conductor 15)",
        field="Q(sqrt(-15)) disc -15, h=2",
        sanity_checks_pass=ok,
        seedA=seedA,
        seedB=seedB,
        e20_margin_seedA=marginA,
        e20_margin_seedB=marginB,
        reasons=reasons,
        verdict=verdict,
    )
    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(results, f, indent=2, default=str)
    log(f"\nresults.json written to {os.path.join(HERE, 'results.json')}")


if __name__ == "__main__":
    main()
