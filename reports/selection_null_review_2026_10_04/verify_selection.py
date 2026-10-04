#!/usr/bin/env python3
"""Exact probability-contract diagnostics, no foreign science imported."""
from fractions import Fraction
from itertools import combinations, product
from math import comb
import json


def sidak(p, n):
    assert 0 <= p <= 1 and n >= 1
    return 1-(1-p)**n


def independent_control():
    universe = tuple(product(range(10), repeat=2))
    A = {u for u in universe if u[0] == 0}
    B = {u for u in universe if u[1] == 0}
    p = Fraction(len(A), len(universe))
    union = Fraction(len(A | B), len(universe))
    assert p == Fraction(1, 10)
    assert Fraction(len(A & B), len(universe)) == p*p
    assert union == sidak(p, 2) == Fraction(19, 100)
    return {"marginal": str(p), "actual_union": str(union), "sidak": str(sidak(p, 2))}


def dependent_control():
    N, size = 100000, 501
    A, B = set(range(size)), set(range(size, 2*size))
    p = Fraction(size, N)
    actual, assumed = Fraction(len(A | B), N), sidak(p, 2)
    threshold = Fraction(1, 100)
    assert A.isdisjoint(B)
    assert assumed < threshold < actual
    assert actual == Fraction(1002, 100000)
    assert assumed == Fraction(99948999, 10000000000)
    for t in (Fraction(0), p/2, p, (p+1)/2, Fraction(1)):
        probability = Fraction(0) if t < p else (p if t < 1 else Fraction(1))
        assert probability <= t
    return {"valid_null_p_values": True, "marginal": str(p),
            "actual_union": str(actual), "sidak": str(assumed),
            "threshold": str(threshold), "decision_can_differ": True,
            "actual_foreign_grade_changed": False}


def finite_scan_control():
    population = tuple(range(5))
    distinct = tuple(combinations(population, 2))
    replacement = tuple(product(population, repeat=2))
    actual = Fraction(sum(0 in pair for pair in distinct), len(distinct))
    iid = Fraction(sum(0 in pair for pair in replacement), len(replacement))
    no_hit = Fraction(comb(4, 2), comb(5, 2))
    assert actual == 1-no_hit == Fraction(2, 5)
    assert iid == sidak(Fraction(1, 5), 2) == Fraction(9, 25)
    assert actual > iid
    return {"without_replacement": str(actual), "with_replacement": str(iid),
            "same_base_rate": "1/5", "physical_sampling_law_derived": False}


def arbitrary_dependence_bound():
    subsets = [set(i for i in range(5) if mask & (1 << i)) for mask in range(32)]
    checked = 0
    for A, B in product(subsets, repeat=2):
        actual = Fraction(len(A | B), 5)
        bound = min(Fraction(1), Fraction(len(A)+len(B), 5))
        assert actual <= bound
        checked += 1
    assert checked == 1024
    return {"pairs_checked": checked, "union_bound_valid": True}


def run():
    for label, control in (("INDEPENDENT", independent_control),
                           ("DEPENDENT", dependent_control),
                           ("FINITE_SCAN", finite_scan_control),
                           ("UNION_BOUND", arbitrary_dependence_bound)):
        print(label, json.dumps(control()), flush=True)
    print("SUMMARY", json.dumps({"probability_contract_gap_verified": True,
          "foreign_function_arithmetic_bug": False,
          "foreign_census_recomputed": False,
          "OA_physical_significance_derived": False}), flush=True)
    print("PASS: scoped dependence controls, not a foreign verdict reversal", flush=True)


if __name__ == "__main__":
    run()
