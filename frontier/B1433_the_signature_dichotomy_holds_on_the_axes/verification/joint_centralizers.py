#!/usr/bin/env python3
"""B1433 -- dimensions of joint centralisers of the four charges, from the exact matrices in ad_matrices.json.
dim z(S) = 78 - rank(stack of ad(x) for x in S).  Rank is computed modulo two large primes and the two agree.  A rank
mod p is a lower bound for the rational rank, so each dimension printed is an upper bound; for a single axis it equals
the exact multiplicity of the eigenvalue 0 (mixed_directions.json), which is the dimension for a semisimple element."""
import json, itertools, pathlib
from fractions import Fraction
HERE = pathlib.Path(__file__).resolve().parent
D = json.load(open(HERE / "ad_matrices.json")); AX = [8, 14, 16, 22]
M = {n: [[Fraction(x) for x in row] for row in D[str(n)]] for n in AX}
def rank_mod(rows, p):
    R = [[(x.numerator * pow(x.denominator, p - 2, p)) % p for x in r] for r in rows]; rk = 0; nc = len(R[0])
    for c in range(nc):
        k = next((i for i in range(rk, len(R)) if R[i][c]), None)
        if k is None: continue
        R[rk], R[k] = R[k], R[rk]; iv = pow(R[rk][c], p - 2, p); R[rk] = [x * iv % p for x in R[rk]]
        for i in range(len(R)):
            if i != rk and R[i][c]:
                f = R[i][c]; R[i] = [(x - f * y) % p for x, y in zip(R[i], R[rk])]
        rk += 1
    return rk
out = {}
for k in range(1, 5):
    for S in itertools.combinations(AX, k):
        rows = [r for n in S for r in M[n]]
        r1, r2 = rank_mod(rows, 1000003), rank_mod(rows, 998244353)
        assert r1 == r2, (S, r1, r2)
        out["z(" + ",".join(f"x{n}" for n in S) + ")"] = 78 - r1
for k, v in out.items(): print(v, k)
json.dump(out, open(HERE / "joint_centralizers.json", "w"), indent=1)
