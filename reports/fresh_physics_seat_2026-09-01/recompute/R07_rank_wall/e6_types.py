#!/usr/bin/env python3
"""R07 blind recompute, part 2 — which centralizer TYPES occur at each order.

Still blind: no arc scripts/tests opened. Deduplicate by contributing-root-set,
classify each distinct subsystem, report per order n (scanning all x = c/n,
c in (Z/n)^6, i.e. all elements of order dividing n) the set of centralizer
types (semisimple part + u(1)^k, k = 6 - semisimple rank).
Find the minimal n at which A2+A1 (su(3)+su(2)+u(1)^3) occurs.
Vectorized in chunks for speed; exact integer arithmetic.
"""
import itertools, json
import numpy as np
from e6_scan import C, R, RC, subsystem_type, rank_of_rootset

subset_cache = {}

def classify(key):
    if key not in subset_cache:
        sub = [tuple(int(x) for x in r) for r in R[list(key)]] if key else []
        srk = rank_of_rootset(sub)
        t = subsystem_type(sub) if sub else ""
        label = (t + f"+u1^{6-srk}") if srk < 6 else t
        subset_cache[key] = (label if label else "u1^6", srk, len(sub))
    return subset_cache[key]

types_by_n = {}
found_min_a2a1 = None
CHUNK = 200000
for n in range(1, 13):
    seen = {}
    it = itertools.product(range(n), repeat=6)
    while True:
        block = list(itertools.islice(it, CHUNK))
        if not block:
            break
        Cv = np.array(block, dtype=np.int64)          # m x 6
        Ev = (Cv @ RC.T) % n                           # m x 72
        Z = (Ev == 0)
        # dedupe by bitmask
        bits = Z @ (1 << np.arange(72, dtype=object))
        for i, b in enumerate(bits):
            if b not in seen:
                key = tuple(np.nonzero(Z[i])[0])
                seen[b] = (key, tuple(block[i]))
    labels = {}
    for b, (key, c) in seen.items():
        label, srk, nroots = classify(key)
        labels.setdefault(label, 0)
        labels[label] += 1
        if found_min_a2a1 is None and nroots == 8 and srk == 3 and label.startswith("A1+A2"):
            found_min_a2a1 = (n, c)
    types_by_n[n] = sorted(labels.keys())
    print(f"n={n} (orders dividing {n}): {len(labels)} distinct type-labels: {types_by_n[n]}")
    if found_min_a2a1 and found_min_a2a1[0] == n:
        print(f"   *** A2+A1 (su3+su2+u1^3) FIRST appears at n={n}, c={found_min_a2a1[1]}")

print()
if found_min_a2a1:
    n, c = found_min_a2a1
    print(f"MINIMAL n with centralizer su(3)+su(2)+u(1)^3: {n} (element x=c/{n}, c={c})")
else:
    print("A2+A1 centralizer NOT found for any order <= 12")

with open("e6_types_out.json", "w") as f:
    json.dump({str(k): v for k, v in types_by_n.items()},
              f, indent=1)
print("[done] wrote e6_types_out.json")
