#!/usr/bin/env python3
"""e16 (data-free): the line facts chat1's step-back proposal cites, computed rather than recalled.  Run once in scratch
before it was committed (disclosed in the commit); the committed output is a second, identical run.
  L1  B1713's 266 lines, rebuilt with B1713's own enumeration (_lines copied from
      frontier/B1713_the_complement_and_the_mixing/verification/the_complement_and_mixing.py on main): the lines at the
      record's indices 88, 97, 149, 150 and 153, and how many lines have order 5 and order 10.
  L2  SL(2, Z/N) for N = 5, 10 acting linearly on the characters of exact order N, taken up to sign as B1713's lines are:
      the group's order, the number of classes, and the size of one orbit (transitive when the two are equal).
  L3  B1724's T-law on the lines, b -> b + 3 alpha (as B1741 uses it), on the ten alpha = 2/5 lines: its orbits.
    python3 -B e16_line_orbits_check.py        # writes e16_line_orbits_check_out.txt"""
import math, itertools, pathlib
from collections import Counter
from fractions import Fraction as Fr

HERE = pathlib.Path(__file__).resolve().parent
out = []


def _lines(lo, hi):
    seen, res = set(), []
    for N in range(lo, hi + 1):
        for j in range(N):
            for k in range(N):
                if math.gcd(math.gcd(j, k), N) != 1:
                    continue
                a, b = Fr(j, N), Fr(k, N); na, nb = (-a) % 1, (-b) % 1
                key = min((a, b), (na, nb))
                if key in seen:
                    continue
                seen.add(key); res.append(("N=%d" % N, key[0], key[1]))
    return res


LINES = _lines(1, 7) + _lines(8, 12)
out.append(f"L1 {len(LINES)} lines; " + "; ".join(f"index {i}: ({LINES[i][1]}, {LINES[i][2]}), {LINES[i][0]}" for i in (88, 97, 149, 150, 153)))
cnt = Counter(math.lcm(a.denominator, b.denominator) for _, a, b in LINES)
out.append(f"L1 lines of order 5: {cnt[5]}; of order 10: {cnt[10]}")

for N in (5, 10):
    G = [g for g in itertools.product(range(N), repeat=4) if (g[0] * g[3] - g[1] * g[2]) % N == 1]
    vecs = {(j, k) for j in range(N) for k in range(N) if math.gcd(math.gcd(j, k), N) == 1}
    cls = lambda v: min(v, ((-v[0]) % N, (-v[1]) % N))
    start = cls(min(vecs))
    orb = {cls(((a * start[0] + b * start[1]) % N, (c * start[0] + d * start[1]) % N)) for a, b, c, d in G}
    out.append(f"L2 SL(2, Z/{N}): order {len(G)}; classes of exact order {N} up to sign {len({cls(v) for v in vecs})}; orbit of {start}: {len(orb)}")

al = Fr(2, 5); left = {Fr(k, 10) for k in range(10)}; orbs = []
while left:
    b = min(left); o = []
    while b in left:
        left.remove(b); o.append(str(b)); b = (b + 3 * al) % 1
    orbs.append(o)
out.append(f"L3 T-orbits of the alpha = 2/5 lines under b -> b + 3 alpha: {orbs}")
(HERE / "e16_line_orbits_check_out.txt").write_text("\n".join(out) + "\n")
print("written")
