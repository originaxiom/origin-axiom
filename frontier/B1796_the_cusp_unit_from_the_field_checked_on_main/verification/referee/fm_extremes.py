"""Referee B1796 -- the per-line formula d(m) = max(0, sum m) at unbalanced end data far outside {-1..2}^3.
    python3 -B fm_extremes.py"""
import itertools
import fm_route as fr

tests = set()
for K in range(1, 13):
    for base in [(K, -K, 0), (2 * K, -K, -K), (K, -K, 1), (K, -K - 1, 1), (K, 0, -K + 1), (-K, -K, 2 * K + 1), (K, K, -2 * K)]:
        for p in itertools.permutations(base):
            if max(p) <= 12 and min(p) >= -24: tests.add(p)
bad = []
for m in sorted(tests):
    d = fr.d_of(m)[0]
    if d != max(0, sum(m)): bad.append((m, d))
print("extreme vectors tested:", len(tests), "| d(m) != max(0, sum m):", bad)
