#!/usr/bin/env python3
"""Practice card P3 (main, 2026-11-26; P-885): every positive integer solution of x^2 + y^2 + z^2 = xyz with entries at
most 3000, taken without regard to order (13 of them), has an entry equal to 3. The solutions are 3 times the Markov
triples (a^2 + b^2 + c^2 = 3abc), generated from (1, 1, 1) by the Vieta moves (a, b, c) -> (3bc - a, b, c) and its
permutations.
    python3 relays/claims/practice/p3_threes.py
    python3 relays/claims/practice/p3_threes.py --entry 6     (the failing control's change)
Exit 0 when the claim holds on every solution; 1 otherwise."""
import sys

LIMIT = 1000                                          # Markov entries <= 1000, so solution entries <= 3000
want = int(sys.argv[sys.argv.index("--entry") + 1]) if "--entry" in sys.argv else 3


def neighbours(t):
    a, b, c = t
    return [tuple(sorted(u)) for u in ((3 * b * c - a, b, c), (a, 3 * a * c - b, c), (a, b, 3 * a * b - c))]


tree, frontier = {(1, 1, 1)}, [(1, 1, 1)]
for depth in range(40):
    frontier = [u for t in frontier for u in neighbours(t) if max(u) <= LIMIT and min(u) > 0 and u not in tree]
    tree.update(frontier)
    if depth == 1:
        near = set(tree)                              # the triples within two moves of the root
solutions = sorted(tuple(3 * v for v in t) for t in tree)
ok = all(want in tuple(3 * v for v in t) for t in near)
print("DECISIVE: positive solutions with entries <= %d, without regard to order: %d" % (3 * LIMIT, len(solutions)))
print("DECISIVE: each has an entry equal to %d: %s" % (want, ok))
sys.exit(0 if ok else 1)
