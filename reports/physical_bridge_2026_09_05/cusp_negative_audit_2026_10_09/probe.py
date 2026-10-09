"""Exact divisor method; pinned source comparison is not producer replay."""
import hashlib
import json
import subprocess
from fractions import Fraction
from pathlib import Path

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[2]
MAIN = "87d769c7aa031cebc87da3e9fd292d55bcaa45b5"
ARC = "frontier/B1629_does_the_principle_reach_the_weaves_cusp"


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n):
    sign, p = 1, 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            sign = -sign
            if n % p == 0:
                return 0
        p += 1
    return -sign if n > 1 else sign


def population(n):
    return sum(mobius(d) * 2 ** (n // d) for d in divisors(n))


def event_count(period, k):
    return 2 if period <= k else (k + 1) * 2 ** (period - k)


def tail(n, k):
    if n < 2 or not 1 <= k <= n:
        raise ValueError("n>=2 and 1<=k<=n required")
    num = sum(mobius(d) * event_count(n // d, k) for d in divisors(n))
    return Fraction(num, population(n))


def pinned(path):
    return subprocess.check_output(["git", "show", MAIN + ":" + path], cwd=ROOT)


def source_table():
    inputs = json.loads((BASE / "INPUTS.json").read_text())
    for row in inputs["sources"]:
        data = pinned(row["path"])
        assert hashlib.sha256(data).hexdigest() == row["sha256"]
        assert len(data) == row["bytes"]
    return json.loads(pinned(ARC + "/verification/post_seal_cusp.json"))


def main():
    saved = source_table()
    counts = {str(n): population(n) for n in range(2, 19)}
    table = {str(n): {str(k): str(tail(n, k)) for k in range(1, n + 1)} for n in range(2, 19)}
    comparison = []
    for n, row in saved["P4_fraction_of_letters_in_runs_ge_k"].items():
        for k, val in row.items():
            comparison.append(round(float(tail(int(n), int(k))), 6) == val)
    bounds = []
    for n in range(2, 19):
        q = Fraction(2 ** n - population(n), 2 ** n)
        union = sum((Fraction(2 ** m, 2 ** n) for m in divisors(n) if m < n), Fraction())
        bounds.append(q <= union)
        for k in range(1, n):
            bounds.append(abs(tail(n, k) - Fraction(k + 1, 2 ** k)) <= q)
    facts = {
        "all_35_saved_run_fractions_recovered": len(comparison) == 35 and all(comparison),
        "finite_equality_control_fails_exactly": tail(10, 2) == Fraction(124, 165) != Fraction(3, 4),
        "all_finite_probability_error_bounds": bool(bounds) and all(bounds),
        "full_length_run_impossible_in_primitive_population": all(tail(n, n) == 0 for n in range(2, 19)),
        "every_primitive_site_has_a_run": all(tail(n, 1) == 1 for n in range(2, 19)),
        "necklace_population_is_integral": all(population(n) % n == 0 for n in range(2, 19)),
        "finite_height_population_recovered": sum(population(n) // n for n in range(2, 15)) == saved["P2"]["threads_len_le_14"],
        "bernoulli_block_avoidance_strictly_decays": all(Fraction(2 ** k - 1, 2 ** k) ** 10 < Fraction(2 ** k - 1, 2 ** k) ** 2 < 1 for k in range(1, 9)),
    }
    assert all(facts.values()), facts
    print(json.dumps({"facts": facts, "counts": counts, "tails": table,
                      "source_profile": saved, "exact_fraction_cells": sum(map(len, table.values())),
                      "physical_source_derived": False, "universal_dynamical_no_go": False}, indent=2))


if __name__ == "__main__":
    main()
