"""Design-time facts about SL(n, F_2), n = 2, 3, 4 (finite-group facts, not census data; disclosed in the seal).
For each element g: does it act on some invariant line (a 2-dim subspace) as a 3-cycle of its three points -- i.e. is
x^2 + x + 1 a factor of its characteristic polynomial over F_2 -- and the cycle type of its action on the 2^n - 1 points."""
import itertools
from collections import Counter
import numpy as np

def charpoly_bits(M):
    c = np.rint(np.poly(M)).astype(np.int64) % 2           # integer char poly (exact for small 0/1 matrices), mod 2
    return int("".join(str(int(b)) for b in c), 2)          # bitmask, leading coefficient first

def gf2_rem(a, b):
    db = b.bit_length() - 1
    while a and a.bit_length() - 1 >= db:
        a ^= b << (a.bit_length() - 1 - db)
    return a

Q = 0b111                                                    # x^2 + x + 1
for n in (2, 3, 4):
    pts = [np.array(v) for v in itertools.product((0, 1), repeat=n) if any(v)]
    idx = {tuple(v): i for i, v in enumerate(pts)}
    total = tri = 0; longest = Counter(); tri_and_long = Counter()
    for bits in itertools.product((0, 1), repeat=n * n):
        M = np.array(bits, dtype=np.int64).reshape(n, n)
        if int(round(np.linalg.det(M))) % 2 == 0: continue
        total += 1
        t = gf2_rem(charpoly_bits(M), Q) == 0
        tri += t
        perm = [idx[tuple(int(x) for x in (v @ M) % 2)] for v in pts]
        seen, lens = set(), []
        for i in range(len(perm)):
            if i in seen: continue
            L, j = 0, i
            while j not in seen: seen.add(j); j = perm[j]; L += 1
            lens.append(L)
        longest[max(lens)] += 1
        if t: tri_and_long[max(lens)] += 1
    print(f"n={n}: |SL(n,2)| = {total}; with an invariant line cycled as a 3-cycle: {tri} ({tri/total:.4f}); "
          f"longest cycle on the {2**n - 1} points: {dict(sorted(longest.items()))}; among the triplet-cyclers: {dict(sorted(tri_and_long.items()))}")
