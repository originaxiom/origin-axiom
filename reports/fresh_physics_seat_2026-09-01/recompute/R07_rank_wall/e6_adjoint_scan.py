#!/usr/bin/env python3
"""R07 blind recompute, part 4 — convention check (E23 discipline), STILL BLIND.

My simply-connected scan (e6_scan.py / e6_types.py) found that the centralizer
type A1+A2+u1^3 = su(3)+su(2)+u(1)^3 FIRST appears at element order n=7, i.e.
it does NOT occur among torus elements of order <= 6 of simply-connected E6.
B955 says "su(3)+su(2)+u(1)^3 appears in that table" where the table is the
order-<=6 scan. Before calling DISCREPANCY, check the other torus convention:

ADJOINT E6: T_ad = t / P^vee (coweight lattice). Order-n elements are
x = sum_i c_i omega_i^vee / n, c in (Z/n)^6, and a root alpha = sum m_i alpha_i
evaluates to (m . c)/n since <alpha_j, omega_i^vee> = delta_ij.
Root contributes to centralizer iff m . c == 0 mod n.
(The identity component of the centralizer is still full-rank; component group
may be nontrivial in the adjoint group, but rank of the Lie algebra centralizer
is what the claim is about.)

Scan all n in 1..7 and record type labels per n, plus the minimal n at which
A1+A2+u1^3 appears in the ADJOINT convention.
"""
import itertools, json
import numpy as np
from e6_scan import C, R, subsystem_type, rank_of_rootset

# adjoint evaluation matrix: just the coefficient vectors m themselves
EV = R.copy()   # 72 x 6, row = m

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
for n in range(1, 8):
    seen = {}
    it = itertools.product(range(n), repeat=6)
    while True:
        block = list(itertools.islice(it, CHUNK))
        if not block:
            break
        Cv = np.array(block, dtype=np.int64)
        Evn = (Cv @ EV.T) % n
        Z = (Evn == 0)
        bits = Z @ (1 << np.arange(72, dtype=object))
        for i, b in enumerate(bits):
            if b not in seen:
                seen[b] = (tuple(np.nonzero(Z[i])[0]), tuple(block[i]))
    labels = {}
    for b, (key, c) in seen.items():
        label, srk, nroots = classify(key)
        labels.setdefault(label, 0)
        labels[label] += 1
        if found_min_a2a1 is None and label == "A1+A2+u1^3":
            found_min_a2a1 = (n, c)
    types_by_n[n] = sorted(labels.keys())
    print(f"[adjoint] n={n}: {types_by_n[n]}")
    if found_min_a2a1 and found_min_a2a1[0] == n:
        print(f"   *** A1+A2+u1^3 FIRST appears (adjoint) at n={n}, c={found_min_a2a1[1]}")

print()
if found_min_a2a1:
    print(f"[adjoint] minimal order with su(3)+su(2)+u(1)^3 centralizer: {found_min_a2a1[0]}")
else:
    print("[adjoint] A1+A2+u1^3 NOT found for any order <= 7")

with open("e6_adjoint_out.json", "w") as f:
    json.dump({"types_by_n": {str(k): v for k, v in types_by_n.items()},
               "min_a2a1": {"n": found_min_a2a1[0], "c": list(found_min_a2a1[1])} if found_min_a2a1 else None},
              f, indent=1)
print("[done] wrote e6_adjoint_out.json")
