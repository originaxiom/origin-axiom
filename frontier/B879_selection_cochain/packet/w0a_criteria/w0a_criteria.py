#!/usr/bin/env python3
"""
W0a THE SELECTION TABLE
Derivation Campaign, seat cc3, cell W0a.

Enumerate all PRIMITIVE cyclic words in {R,L} of length 2..12 up to cyclic
rotation. R = [[1,1],[0,1]], L = [[1,0],[1,1]]. For each hyperbolic
(mixed-letter, primitive) class compute: matrix product, trace, disc =
tr^2-4 (+ full prime factorization), conductor primality (is disc prime),
det(A-I) = 2-tr and its unit status (|2-tr|==1), amphichirality computed
HONESTLY from the word criterion (w cyclically equivalent to swap(reverse(w))),
and the Legendre/Kronecker character table (kappa|p) for p | disc, kappa=4..15.

Monochromatic words (all-R or all-L) are parabolic (trace 2, disc 0) and are
recorded separately, excluded from the hyperbolic analysis.

THE FALSIFIER: if any hyperbolic class other than RL/LR is simultaneously
amphichiral + unit-det(A-I) + prime-conductor, report it loudly. Also report
near-misses (exactly two of the three).

Exact integer arithmetic throughout. No floats anywhere in any verdict.
"""

import json
import itertools
import sys

MIN_LEN = 2
MAX_LEN = 12

# -------------------- exact integer matrix arithmetic --------------------

R = ((1, 1), (0, 1))
L = ((1, 0), (1, 1))
IDENTITY = ((1, 0), (0, 1))

SWAP_TABLE = str.maketrans('RL', 'LR')


def matmul(A, B):
    return (
        (A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]),
        (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]),
    )


def word_matrix(word):
    """Matrix product in left-to-right letter order: w1 w2 ... wn -> M(w1)*M(w2)*...*M(wn)."""
    M = IDENTITY
    for ch in word:
        M = matmul(M, R if ch == 'R' else L)
    return M


# -------------------- combinatorics: canonical necklace reps --------------------

def canonical(word):
    """Lexicographically minimal rotation. Python string compare is by
    codepoint; 'L' (76) < 'R' (82) so this already matches alphabetical
    L < R ordering with no custom comparator needed."""
    n = len(word)
    return min(word[i:] + word[:i] for i in range(n))


def minimal_period(word):
    """Smallest d | len(word) such that word is (word[:d]) repeated. A word
    is primitive (not a power of a shorter word) iff minimal_period == len."""
    n = len(word)
    for d in range(1, n + 1):
        if n % d == 0:
            if word[:d] * (n // d) == word:
                return d
    return n


# -------------------- exact integer number theory --------------------

def factorize(n):
    """Full prime factorization of a positive integer n (exact trial division).
    Returns dict prime -> exponent. n must be >= 1."""
    assert isinstance(n, int) and n >= 1
    factors = {}
    m = n
    d = 2
    while d * d <= m:
        while m % d == 0:
            factors[d] = factors.get(d, 0) + 1
            m //= d
        d += 1
    if m > 1:
        factors[m] = factors.get(m, 0) + 1
    return factors


def is_prime_exact(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def legendre_or_kronecker(kappa, p):
    """(kappa | p). For odd primes p this is the standard Legendre symbol,
    computed exactly via modular exponentiation (integer arithmetic only:
    Euler's criterion, pow(kappa, (p-1)//2, p) in {0,1,p-1}).
    For p == 2 (which can divide disc when tr is even) there is no standard
    Legendre symbol (2 is not odd); we use the standard supplementary-law
    definition of the quadratic character mod 8 (the Kronecker symbol
    (kappa|2)): 0 if kappa even, +1 if kappa = +-1 mod 8, -1 if kappa = +-3 mod 8.
    This is exact integer arithmetic (mod 8 residue check), no floats."""
    if p == 2:
        if kappa % 2 == 0:
            return 0
        r8 = kappa % 8
        if r8 in (1, 7):
            return 1
        else:  # r8 in (3,5)
            return -1
    else:
        r = kappa % p
        if r == 0:
            return 0
        val = pow(r, (p - 1) // 2, p)
        if val == 1:
            return 1
        elif val == p - 1:
            return -1
        else:
            raise AssertionError(f"Euler criterion gave unexpected value {val} for kappa={kappa} p={p}")


# -------------------- enumeration --------------------

def enumerate_necklaces(n):
    """All distinct necklace canonical reps of length n over {R,L}."""
    seen = set()
    for tup in itertools.product('RL', repeat=n):
        w = ''.join(tup)
        c = canonical(w)
        seen.add(c)
    return seen


def build_table():
    hyperbolic = []
    parabolic = []
    counts_per_length = {}
    excluded_periodic_mixed_per_length = {}

    for n in range(MIN_LEN, MAX_LEN + 1):
        necklaces = enumerate_necklaces(n)
        n_hyper = 0
        n_para = 0
        n_excluded_periodic = 0

        for w in sorted(necklaces):
            is_mono = (len(set(w)) == 1)
            period = minimal_period(w)
            is_primitive = (period == n)

            if is_mono:
                # parabolic: R^n or L^n. Always non-primitive for n>=2
                # (period 1 < n), recorded separately and excluded from the
                # hyperbolic (mixed-letter) analysis.
                letter = w[0]
                M = word_matrix(w)
                tr = M[0][0] + M[1][1]
                disc = tr * tr - 4
                det_AminusI = 2 - tr
                parabolic.append({
                    "word": w,
                    "length": n,
                    "letter": letter,
                    "primitive_by_definition": is_primitive,  # always False for n>=2
                    "matrix": [list(M[0]), list(M[1])],
                    "trace": tr,
                    "disc": disc,
                    "det_A_minus_I": det_AminusI,
                    "unit_det": (abs(det_AminusI) == 1),
                    "excluded_from_hyperbolic_analysis": True,
                    "class": "parabolic",
                })
                n_para += 1
                continue

            if not is_primitive:
                # mixed-letter but periodic (e.g. RLRL = (RL)^2): excluded,
                # not a primitive word. Tallied only, not recorded in detail.
                n_excluded_periodic += 1
                continue

            # primitive, mixed-letter hyperbolic word: full analysis
            M = word_matrix(w)
            tr = M[0][0] + M[1][1]
            disc = tr * tr - 4
            assert disc > 0, f"expected hyperbolic disc>0 for mixed word {w}, got {disc}"
            fac = factorize(disc)
            prime_conductor = is_prime_exact(disc)
            # cross-check primality test against independent factorization
            fac_says_prime = (len(fac) == 1 and list(fac.values()) == [1])
            assert prime_conductor == fac_says_prime, (
                f"primality mismatch for word {w} disc {disc}: "
                f"is_prime_exact={prime_conductor} factorization={fac}"
            )

            det_AminusI = 2 - tr
            unit_det = (abs(det_AminusI) == 1)

            rev = w[::-1]
            canon_rev = canonical(rev)

            swapped = w.translate(SWAP_TABLE)
            canon_swap = canonical(swapped)

            revswap_a = canonical(rev.translate(SWAP_TABLE))
            revswap_b = canonical(swapped[::-1])
            assert revswap_a == revswap_b, (
                f"reverse and swap should commute up to rotation for word {w}: "
                f"{revswap_a} vs {revswap_b}"
            )
            canon_revswap = revswap_a

            amphichiral = (canon_revswap == w)

            char_table = {}
            for p in sorted(fac.keys()):
                char_table[str(p)] = {
                    str(k): legendre_or_kronecker(k, p) for k in range(4, 16)
                }

            hyperbolic.append({
                "word": w,
                "length": n,
                "matrix": [list(M[0]), list(M[1])],
                "trace": tr,
                "disc": disc,
                "disc_factorization": {str(p): e for p, e in sorted(fac.items())},
                "prime_conductor": prime_conductor,
                "det_A_minus_I": det_AminusI,
                "unit_det": unit_det,
                "reversal_class": canon_rev,
                "swap_class": canon_swap,
                "reversal_swap_class": canon_revswap,
                "amphichiral": amphichiral,
                "character_table": char_table,
                "class": "hyperbolic",
            })
            n_hyper += 1

        counts_per_length[n] = {"hyperbolic": n_hyper, "parabolic": n_para}
        excluded_periodic_mixed_per_length[n] = n_excluded_periodic

    return hyperbolic, parabolic, counts_per_length, excluded_periodic_mixed_per_length


def compute_symmetry_orbits(hyperbolic):
    """For each class, the dihedral-4 orbit {w, rev(w), swap(w), revswap(w)}
    as canonical reps, deduplicated, plus orbit size."""
    by_word = {c["word"]: c for c in hyperbolic}
    orbits = {}
    for c in hyperbolic:
        w = c["word"]
        members = {w, c["reversal_class"], c["swap_class"], c["reversal_swap_class"]}
        orbits[w] = {
            "members": sorted(members),
            "orbit_size": len(members),
        }
    return orbits


def main():
    print(f"[W0a] enumerating primitive cyclic R/L words, length {MIN_LEN}..{MAX_LEN}", flush=True)

    hyperbolic, parabolic, counts_per_length, excluded_periodic = build_table()

    print(f"[W0a] hyperbolic primitive classes: {len(hyperbolic)}", flush=True)
    print(f"[W0a] parabolic classes (all-R / all-L): {len(parabolic)}", flush=True)
    total_excluded_periodic = sum(excluded_periodic.values())
    print(f"[W0a] excluded non-primitive mixed necklaces (periodic, e.g. (RL)^k): {total_excluded_periodic}", flush=True)

    for n in range(MIN_LEN, MAX_LEN + 1):
        c = counts_per_length[n]
        print(f"[W0a] length {n:2d}: hyperbolic={c['hyperbolic']:4d}  parabolic={c['parabolic']}  "
              f"excluded_periodic_mixed={excluded_periodic[n]}", flush=True)

    symmetry_orbits = compute_symmetry_orbits(hyperbolic)

    # identify the golden word RL/LR (length 2 hyperbolic class)
    golden_candidates = [c for c in hyperbolic if c["length"] == 2]
    assert len(golden_candidates) == 1, f"expected exactly one length-2 hyperbolic class, got {golden_candidates}"
    golden = golden_candidates[0]
    golden_word = golden["word"]
    print(f"[W0a] golden word (RL) canonical rep: '{golden_word}'  trace={golden['trace']}  disc={golden['disc']}", flush=True)
    assert golden["trace"] == 3 and golden["disc"] == 5, "golden word RL must have trace 3, disc 5"

    # -------------------- THE FALSIFIER --------------------
    violations = []
    near_misses = []
    for c in hyperbolic:
        a = c["amphichiral"]
        b = c["unit_det"]
        cc = c["prime_conductor"]
        n_true = sum([a, b, cc])
        if n_true == 3:
            if c["word"] != golden_word:
                violations.append(c["word"])
        elif n_true == 2:
            missing = []
            if not a:
                missing.append("amphichiral")
            if not b:
                missing.append("unit_det")
            if not cc:
                missing.append("prime_conductor")
            near_misses.append({
                "word": c["word"],
                "length": c["length"],
                "trace": c["trace"],
                "disc": c["disc"],
                "amphichiral": a,
                "unit_det": b,
                "prime_conductor": cc,
                "missing_property": missing[0] if missing else None,
            })

    falsifier_result = {
        "golden_word": golden_word,
        "golden_word_length": 2,
        "criteria_definition": "amphichiral AND unit_det(A-I) AND prime_conductor",
        "violations_other_than_golden": violations,
        "falsifier_status": "DIES" if violations else "SURVIVES",
        "near_miss_count": len(near_misses),
        "near_misses": near_misses,
    }

    print(f"[W0a] FALSIFIER STATUS: {falsifier_result['falsifier_status']}", flush=True)
    if violations:
        print(f"[W0a] !!!! FALSIFIER TRIGGERED !!!! other classes satisfying all three: {violations}", flush=True)
    print(f"[W0a] near-miss count (exactly 2 of 3 criteria): {len(near_misses)}", flush=True)

    # -------------------- summary stats --------------------
    classes_per_trace = {}
    for c in hyperbolic:
        t = c["trace"]
        classes_per_trace[t] = classes_per_trace.get(t, 0) + 1

    traces_with_amphichiral = sorted({c["trace"] for c in hyperbolic if c["amphichiral"]})
    prime_conductor_count = sum(1 for c in hyperbolic if c["prime_conductor"])
    unit_det_count = sum(1 for c in hyperbolic if c["unit_det"])
    amphichiral_count = sum(1 for c in hyperbolic if c["amphichiral"])

    # where amphichiral column differs from the naive unit-det assumption
    amphichiral_vs_unit_mismatches = [
        {"word": c["word"], "length": c["length"], "trace": c["trace"],
         "amphichiral": c["amphichiral"], "unit_det": c["unit_det"]}
        for c in hyperbolic if c["amphichiral"] != c["unit_det"]
    ]

    summary = {
        "total_hyperbolic_classes": len(hyperbolic),
        "total_parabolic_classes": len(parabolic),
        "counts_per_length": counts_per_length,
        "excluded_periodic_mixed_per_length": excluded_periodic,
        "total_excluded_periodic_mixed": total_excluded_periodic,
        "classes_per_trace": {str(k): v for k, v in sorted(classes_per_trace.items())},
        "distinct_trace_values": len(classes_per_trace),
        "traces_with_amphichiral_classes": traces_with_amphichiral,
        "amphichiral_class_count": amphichiral_count,
        "unit_det_class_count": unit_det_count,
        "prime_conductor_class_count": prime_conductor_count,
        "amphichiral_vs_unit_det_mismatch_count": len(amphichiral_vs_unit_mismatches),
        "amphichiral_vs_unit_det_mismatches": amphichiral_vs_unit_mismatches,
    }

    print(f"[W0a] distinct trace values among hyperbolic classes: {summary['distinct_trace_values']}", flush=True)
    print(f"[W0a] traces admitting amphichiral classes: {traces_with_amphichiral}", flush=True)
    print(f"[W0a] amphichiral class count: {amphichiral_count}", flush=True)
    print(f"[W0a] unit-det(A-I) class count: {unit_det_count}", flush=True)
    print(f"[W0a] prime-conductor class count: {prime_conductor_count}", flush=True)
    print(f"[W0a] amphichiral vs unit_det mismatch count: {len(amphichiral_vs_unit_mismatches)}", flush=True)

    output = {
        "meta": {
            "cell": "W0a",
            "campaign": "derivation_campaign",
            "seat": "cc3",
            "word_length_range": [MIN_LEN, MAX_LEN],
            "matrices": {"R": [[1, 1], [0, 1]], "L": [[1, 0], [1, 1]]},
            "convention": "word w1 w2 ... wn maps to matrix product M(w1)*M(w2)*...*M(wn); "
                          "canonical class rep = lexicographically minimal rotation ('L' < 'R'); "
                          "amphichiral iff canonical(swap(reverse(w))) == w.",
        },
        "hyperbolic_classes": hyperbolic,
        "parabolic_classes": parabolic,
        "symmetry_orbits": symmetry_orbits,
        "falsifier": falsifier_result,
        "summary": summary,
    }

    out_path = "w0a_table.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=1)
    print(f"[W0a] wrote {out_path}", flush=True)

    print("[W0a] EXIT_MARKER_W0A_DONE", flush=True)


if __name__ == "__main__":
    main()
