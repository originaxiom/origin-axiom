#!/usr/bin/env python3
"""
W0b -- THE FIELD TABLE
Seat cc3, DERIVATION CAMPAIGN, cell W0b (sealed prereg: PREREG_DC.md).

Independently regenerates the W0a word family (does NOT read W0a's output):
  primitive cyclic {R,L}-words, length 2..12, up to rotation,
  hyperbolic classes only (trace != 2).

For each class computes:
  1. trace, disc D = tr^2 - 4, exact squarefree factorization D = f^2 * d
     (d = squarefree part -> eigenvalue field Q(sqrt d)).
  2. entanglement classification of d:
       - golden:  d == 5
       - silver:  d in {2,3,6}  (squarefree, prime factors subset of {2,3})
       - ramification character: d == 1 (mod 4)  =>  disc(Q(sqrt d)) = d
                                  else             =>  disc(Q(sqrt d)) = 4d
       - which primes ramify in Q(sqrt d)
       - whether Q(sqrt d) is one of Q(zeta_24)'s quadratic subfields
         (derived computationally below, not assumed)
  3. field-degeneracy grouping: which words collapse onto the same d.
  4. THE GOLDEN QUESTION: is d=5 the only d that is simultaneously
       (a) linearly disjoint from Q(zeta_24)'s quadratic subfields, and
       (b) has prime field discriminant?

Exact integer arithmetic throughout (Python's arbitrary-precision ints).
Run: python3 -u w0b_fields.py
"""

import json
import sys

# ---------------------------------------------------------------------------
# 0. matrix machinery (exact 2x2 integer matrices, det should always be 1)
# ---------------------------------------------------------------------------

R = ((1, 1), (0, 1))   # standard SL(2,Z) generator "R"
L = ((1, 0), (1, 1))   # standard SL(2,Z) generator "L"


def mat_mul(A, B):
    (a, b), (c, d) = A
    (e, f), (g, h) = B
    return ((a * e + b * g, a * f + b * h), (c * e + d * g, c * f + d * h))


def word_matrix(word):
    M = ((1, 0), (0, 1))
    for ch in word:
        M = mat_mul(M, R if ch == 'R' else L)
    return M


def trace(M):
    return M[0][0] + M[1][1]


def det(M):
    return M[0][0] * M[1][1] - M[0][1] * M[1][0]


# ---------------------------------------------------------------------------
# 1. primitive-necklace enumeration (binary alphabet {R,L}, up to rotation)
# ---------------------------------------------------------------------------

def divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]


def is_aperiodic(s):
    """True iff s has no proper period, i.e. minimal period == len(s)."""
    n = len(s)
    for d in divisors(n):
        if d == n:
            continue
        if all(s[i] == s[i % d] for i in range(n)):
            return False
    return True


def is_canonical(s):
    """True iff s is the lexicographically smallest rotation of itself
    (one canonical representative per necklace / rotation-class)."""
    n = len(s)
    rotations = [s[i:] + s[:i] for i in range(n)]
    return s == min(rotations)


def enumerate_primitive_necklaces(n):
    """All primitive (aperiodic) binary necklaces of length n, alphabet R<L,
    one lexicographically-canonical representative word per necklace."""
    reps = []
    # iterative bit generation avoids itertools.product overhead concerns;
    # itertools is fine here too but this keeps it fully self-contained.
    for mask in range(2 ** n):
        s = ''.join('R' if (mask >> (n - 1 - i)) & 1 == 0 else 'L' for i in range(n))
        if is_canonical(s) and is_aperiodic(s):
            reps.append(s)
    return reps


def mobius(n):
    if n == 1:
        return 1
    result = 1
    nn = n
    p = 2
    while p * p <= nn:
        if nn % p == 0:
            nn //= p
            if nn % p == 0:
                return 0
            result *= -1
        p += 1
    if nn > 1:
        result *= -1
    return result


def moreau_necklace_count(n, k=2):
    """Moreau's necklace-counting function: number of aperiodic
    (primitive) necklaces of length n over a k-letter alphabet.
    M(n,k) = (1/n) * sum_{d|n} mu(d) * k^(n/d).
    Used purely as an independent cross-check on the brute-force count."""
    total = sum(mobius(d) * k ** (n // d) for d in divisors(n))
    assert total % n == 0
    return total // n


# ---------------------------------------------------------------------------
# 2. exact squarefree factorization
# ---------------------------------------------------------------------------

def factorize(n):
    """Exact trial-division factorization of positive integer n."""
    assert n >= 1
    factors = {}
    nn = n
    p = 2
    while p * p <= nn:
        while nn % p == 0:
            factors[p] = factors.get(p, 0) + 1
            nn //= p
        p += 1
    if nn > 1:
        factors[nn] = factors.get(nn, 0) + 1
    return factors


def squarefree_split(D):
    """D = f*f*d with d squarefree. Returns (d, f, factors_of_D)."""
    factors = factorize(D)
    d = 1
    f = 1
    for p, e in factors.items():
        if e % 2 == 1:
            d *= p
        f *= p ** (e // 2)
    assert f * f * d == D
    return d, f, factors


def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True


# ---------------------------------------------------------------------------
# 3. quadratic subfields of Q(zeta_24) -- derived, not assumed
# ---------------------------------------------------------------------------
#
# Classical fact (conductor-discriminant correspondence for quadratic
# fields): for squarefree integer m != 1, let disc(m) be the discriminant
# of Q(sqrt m):
#       disc(m) = m       if m == 1 (mod 4)
#       disc(m) = 4*m     otherwise
# Then Q(sqrt m) is a subfield of the cyclotomic field Q(zeta_n) if and
# only if disc(m) divides n (equivalently: the quadratic character
# attached to Q(sqrt m) has conductor |disc(m)|, and a Dirichlet character
# mod c factors through (Z/nZ)^* iff c | n).
#
# We use this to *compute* (not assume) the full list of quadratic
# subfields of Q(zeta_24), scanning all squarefree m with |disc(m)| <= 24
# (any larger disc cannot divide 24).

def field_discriminant(m):
    """m squarefree (m != 0, m != 1). disc(Q(sqrt m))."""
    return m if (m % 4 == 1) else 4 * m


def is_squarefree(m):
    n = abs(m)
    if n == 0:
        return False
    factors = factorize(n) if n > 1 else {}
    return all(e == 1 for e in factors.values())


def quadratic_subfields_of_zeta_n(n):
    """Brute-force-derive every quadratic subfield Q(sqrt m) of Q(zeta_n)
    by scanning squarefree m in [-n, n] and testing disc(m) | n."""
    hits = []
    for m in range(-n, n + 1):
        if m in (0, 1):
            continue
        if not is_squarefree(m):
            continue
        D = field_discriminant(m)
        if n % abs(D) == 0:
            hits.append((m, D))
    return sorted(hits, key=lambda t: (abs(t[0]), t[0]))


# ===========================================================================
# MAIN
# ===========================================================================

def main():
    print("=== W0b THE FIELD TABLE -- seat cc3 derivation campaign ===")
    print()

    # -- 0. derive quadratic subfields of Q(zeta_24) -----------------------
    print("--- Step 0: quadratic subfields of Q(zeta_24) (derived) ---")
    subfields_24 = quadratic_subfields_of_zeta_n(24)
    for m, D in subfields_24:
        sign = "sqrt(%d)" % m
        print(f"  Q({sign})   [m={m:>3d}, disc={D:>4d}]")
    print(f"  total quadratic subfields of Q(zeta_24): {len(subfields_24)}")
    real_subfields_24 = sorted({m for m, D in subfields_24 if m > 0})
    imag_subfields_24 = sorted({m for m, D in subfields_24 if m < 0})
    print(f"  real  (d>0): {real_subfields_24}")
    print(f"  imag  (d<0): {imag_subfields_24}")
    print()
    assert len(subfields_24) == 7, "expected exactly 7 quadratic subfields of Q(zeta_24)"
    assert real_subfields_24 == [2, 3, 6], "expected real subfields to be exactly {2,3,6}"

    # -- 1. enumerate primitive necklaces / cross-check with Moreau formula -
    print("--- Step 1: primitive {R,L}-necklace enumeration, length 2..12 ---")
    per_length = {}
    total_count = 0
    all_words = []
    for n in range(2, 13):
        reps = enumerate_primitive_necklaces(n)
        expect = moreau_necklace_count(n, 2)
        assert len(reps) == expect, f"n={n}: brute force {len(reps)} != Moreau {expect}"
        per_length[n] = len(reps)
        total_count += len(reps)
        all_words.extend((n, w) for w in reps)
        print(f"  length {n:>2d}: {len(reps):>4d} primitive necklaces (Moreau check OK)")
    print(f"  TOTAL primitive cyclic {{R,L}}-words, length 2..12, up to rotation: {total_count}")
    print()

    # -- 2. per-class computation --------------------------------------------
    print("--- Step 2: per-class trace / disc / field computation ---")
    classes = []
    n_excluded_parabolic = 0
    for n, w in all_words:
        M = word_matrix(w)
        tr = trace(M)
        dt = det(M)
        assert dt == 1, f"word {w}: det={dt} != 1 (SL(2,Z) violated)"
        if tr == 2 or tr == -2:
            # parabolic; excluded by the "hyperbolic classes only" filter.
            n_excluded_parabolic += 1
            continue
        assert tr > 2, f"word {w}: trace {tr} not > 2 (not hyperbolic-positive as expected)"
        D = tr * tr - 4
        d, f, D_factors = squarefree_split(D)

        disc = field_discriminant(d)
        ramified_primes = sorted(factorize(disc).keys())

        is_golden = (d == 5)
        d_factors = factorize(d) if d > 1 else {}
        silver_primes_only = d > 1 and set(d_factors.keys()) <= {2, 3}
        is_silver = d in (2, 3, 6)
        assert is_silver == silver_primes_only, "silver-class definitions disagree"

        ram_char = "1 mod 4 (disc = d)" if d % 4 == 1 else "not 1 mod 4 (disc = 4d)"

        in_zeta24 = d in real_subfields_24  # linear (non)disjointness test
        disjoint_from_zeta24 = not in_zeta24

        disc_is_prime = is_prime(disc)

        classes.append({
            "word": w,
            "length": n,
            "trace": tr,
            "det": dt,
            "disc_D": D,
            "D_factorization": {str(k): v for k, v in D_factors.items()},
            "squarefree_d": d,
            "conductor_f": f,
            "field_discriminant": disc,
            "ramified_primes": ramified_primes,
            "ram_class_mod4": ram_char,
            "is_golden": is_golden,
            "is_silver": is_silver,
            "d_prime_factors": sorted(d_factors.keys()) if d > 1 else [],
            "in_Qzeta24_quadratic_subfields": in_zeta24,
            "linearly_disjoint_from_Qzeta24": disjoint_from_zeta24,
            "field_discriminant_is_prime": disc_is_prime,
        })

    assert n_excluded_parabolic == 0, (
        f"{n_excluded_parabolic} primitive words of length>=2 were parabolic "
        "-- unexpected, investigate"
    )
    print(f"  computed {len(classes)} classes; parabolic exclusions: {n_excluded_parabolic}")
    print()

    # -- 3. field degeneracy --------------------------------------------------
    print("--- Step 3: field degeneracy (grouping by squarefree d) ---")
    by_d = {}
    for c in classes:
        by_d.setdefault(c["squarefree_d"], []).append(c)
    print(f"  distinct eigenvalue fields (distinct d values): {len(by_d)}")

    degeneracy = []
    for d, members in sorted(by_d.items()):
        members_sorted = sorted(members, key=lambda c: (c["trace"], c["word"]))
        rep = min(members, key=lambda c: abs(c["trace"]))
        degeneracy.append({
            "d": d,
            "field": f"Q(sqrt {d})",
            "count": len(members),
            "words": [c["word"] for c in members_sorted],
            "smallest_trace_representative": {
                "word": rep["word"], "length": rep["length"], "trace": rep["trace"],
            },
        })
    # sort report by degeneracy count desc, then d asc, for readability
    degeneracy_report = sorted(degeneracy, key=lambda e: (-e["count"], e["d"]))

    print("  top degeneracies (d : count of words sharing that field):")
    for e in degeneracy_report[:15]:
        print(f"    d={e['d']:<6d} count={e['count']:<4d} smallest-trace rep: "
              f"{e['smallest_trace_representative']}")
    n_singletons = sum(1 for e in degeneracy if e["count"] == 1)
    print(f"  fields hit by exactly one word (no degeneracy): {n_singletons} / {len(by_d)}")
    print()

    # -- 4. THE GOLDEN QUESTION ------------------------------------------------
    print("--- Step 4: THE GOLDEN QUESTION ---")
    all_d = sorted(by_d.keys())
    set_A_disjoint = sorted(d for d in all_d if d not in real_subfields_24)
    set_B_prime_disc = sorted(d for d in all_d if is_prime(field_discriminant(d)))
    set_joint = sorted(set(set_A_disjoint) & set(set_B_prime_disc))

    print(f"  condition (a) linearly disjoint from Q(zeta_24) quad. subfields: "
          f"{len(set_A_disjoint)} / {len(all_d)} d-values satisfy this")
    print(f"    (i.e. all d NOT in {{2,3,6}})")
    print(f"  condition (b) prime field discriminant: {len(set_B_prime_disc)} d-values: "
          f"{set_B_prime_disc}")
    print(f"  condition (a) AND (b) jointly: {len(set_joint)} d-values: {set_joint}")
    print(f"  is d=5 the ONLY one satisfying both? "
          f"{'YES' if set_joint == [5] else 'NO -- FALSIFIED'}")
    print()

    golden_question = {
        "condition_a_disjoint_from_Qzeta24_ds": set_A_disjoint,
        "condition_a_count": len(set_A_disjoint),
        "condition_b_prime_discriminant_ds": set_B_prime_disc,
        "condition_b_count": len(set_B_prime_disc),
        "joint_ds": set_joint,
        "joint_count": len(set_joint),
        "is_5_the_only_one": set_joint == [5],
    }

    # -- assemble output ------------------------------------------------------
    output = {
        "meta": {
            "cell": "W0b",
            "seat": "cc3",
            "word_family": "primitive cyclic {R,L}-words, length 2..12, up to rotation, "
                            "hyperbolic (trace != 2)",
            "per_length_counts": per_length,
            "total_count": total_count,
            "moreau_cross_check": "passed for all lengths 2..12",
            "matrix_convention": {"R": R, "L": L},
        },
        "Qzeta24_quadratic_subfields": {
            "all": [{"m": m, "disc": D} for m, D in subfields_24],
            "real_ds": real_subfields_24,
            "imag_ds": imag_subfields_24,
            "total": len(subfields_24),
        },
        "classes": classes,
        "field_degeneracy": {
            "distinct_field_count": len(by_d),
            "groups": degeneracy_report,
            "singleton_field_count": n_singletons,
        },
        "golden_question": golden_question,
    }

    out_path = "/Users/dri/oa-seat-cc3/seat-work/derivation_campaign/w0b_fields/w0b_table.json"
    with open(out_path, "w") as fh:
        json.dump(output, fh, indent=2)
    print(f"wrote {out_path}")
    print()
    print("=== DONE ===")


if __name__ == "__main__":
    main()
