"""Independent rooted-word enumeration and integer matrix radius check.

No import of the divisor producer or the author's producers. Constants
are excluded by the minimal-period test. No float decides populations,
fractions, ordering, equality of heights or the opposing control.
"""
import itertools
import json
from fractions import Fraction
from math import sqrt


def primitive(w):
    return all(w != w[:d] * (len(w) // d) for d in range(1, len(w)) if len(w) % d == 0)


def marked_run(w):
    n = len(w)
    if all(c == w[0] for c in w):
        return n
    forward = 1
    while forward < n and w[forward] == w[0]:
        forward += 1
    backward = 0
    while w[n - 1 - backward] == w[0]:
        backward += 1
    return forward + backward


def rows(n):
    hist = [0] * (n + 1)
    necklaces = []
    for bits in itertools.product("LR", repeat=n):
        w = "".join(bits)
        if not primitive(w):
            continue
        hist[marked_run(w)] += 1
        if n <= 14 and w == min(w[i:] + w[:i] for i in range(n)):
            necklaces.append(w)
    count = sum(hist)
    return count, {str(k): str(Fraction(sum(hist[k:]), count)) for k in range(1, n + 1)}, necklaces


def matrix(w):
    a, b, c, d = 1, 0, 0, 1
    for letter in w:
        if letter == "L":
            a, c = a + b, c + d
        elif letter == "R":
            b, d = a + b, c + d
        else:
            raise ValueError(letter)
    return a, b, c, d


def height_squared(w):
    radii = []
    for i in range(len(w)):
        a, b, c, d = matrix(w[i:] + w[:i])
        assert a * d - b * c == 1
        assert b > 0 and c > 0
        radii.append(Fraction((a + d) ** 2 - 4, 4 * min(b, c) ** 2))
    return max(radii)


def main():
    counts, table, necklaces = {}, {}, []
    for n in range(2, 19):
        count, row, words = rows(n)
        counts[str(n)], table[str(n)] = count, row
        necklaces.extend(words)
    heights = {w: height_squared(w) for w in necklaces}
    unique = sorted(set(heights.values()))
    unconditioned = []
    for n in range(2, 11):
        hist = [0] * (n + 1)
        for w in itertools.product("LR", repeat=n):
            hist[marked_run(w)] += 1
        for k in range(1, n):
            unconditioned.append(Fraction(sum(hist[k:]), 2 ** n) == Fraction(k + 1, 2 ** k))
    a, _, _, d = matrix("LLLR")
    e, _, _, h = matrix("LLRR")
    facts = {
        "unconditioned_positive_control": bool(unconditioned) and all(unconditioned),
        "primitive_condition_changes_fraction": Fraction(table["10"]["2"]) == Fraction(124, 165) != Fraction(3, 4),
        "tiny_populations": [counts[str(n)] for n in (2, 3, 4)] == [2, 6, 12],
        "corrected_finite_radius_minimum_preserved": unique[:2] == [Fraction(5, 4), Fraction(2)],
        "finite_minimum_argmin_preserved": [w for w in necklaces if heights[w] == unique[0]] == ["LR"],
        "same_word_length_different_translation_length": a + d == 5 and e + h == 6,
    }
    assert all(facts.values()), facts
    p2 = {"threads_len_le_14": len(necklaces), "min_top": round(sqrt(unique[0]), 6),
          "argmin": sorted(w for w in necklaces if heights[w] == unique[0]),
          "max_top": round(sqrt(unique[-1]), 4), "LR_top": round(sqrt(height_squared("LR")), 6),
          "LR_is_lowest": height_squared("LR") == unique[0], "second_lowest": round(sqrt(unique[1]), 6),
          "L^k R": {str(k): round(sqrt(height_squared("L" * k + "R")), 4) for k in range(1, 13)},
          "L^k R^k": {str(k): round(sqrt(height_squared("L" * k + "R" * k)), 4) for k in range(1, 9)}}
    print(json.dumps({"facts": facts, "counts": counts, "tails": table, "P2": p2,
                      "exact_fraction_cells": sum(map(len, table.values())),
                      "physical_source_derived": False, "universal_dynamical_no_go": False}, indent=2))


if __name__ == "__main__":
    main()
