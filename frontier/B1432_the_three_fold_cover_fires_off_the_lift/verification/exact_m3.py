#!/usr/bin/env python3
"""The complete candidate census of s961 = M_3 in EXACT arithmetic over Q(i): all 16 x 16 modules, compared entry by
entry with the prime-field census."""
import json, pathlib
from collections import Counter
import exact_lib as E
import cover_census as cc

n, N = 3, 4
ng, rels, mu, lam, tau = cc.cover(n)
chars = cc.characters(rels, mu, ng, N)
I = {}
for lc in chars:
    for al in chars:
        i = E.exact_index(n, N, lc, al)
        if i: I[(lc, al)] = i
squares = set(tuple((2 * x) % N for x in c) for c in chars)
out = dict(field="Q(i)", characters=len(chars), candidates=len(chars) ** 2, firing=len(I),
           firing_on_square_loci=sum(1 for (l, a) in I if l in squares), signs={str(k): v for k, v in Counter(I.values()).items()})
o, bgs, Ip, _, _ = cc.census(n, N, 5000, verbose=False)
out["identical_to_prime_field_census"] = (Ip == I)
print(json.dumps(out, indent=1))
json.dump(out, open(pathlib.Path(__file__).with_name("exact_m3.json"), "w"), indent=1)
