"""Every hyperbolic class of SL(2,Z) is, up to sign, a cyclic word in L and R containing both letters (a check for the
paper's Section 2; the fact is classical, through continued fractions and cutting sequences).

A matrix of SL(2,Z) with non-negative entries other than the identity is a positive word in L = [[1,1],[0,1]] and
R = [[1,0],[1,1]] (peel off L or R by comparing columns); a hyperbolic one contains both letters, since L^n and R^n are
parabolic. So it suffices that every hyperbolic M with entries of absolute value at most 5 has a conjugate g M g^-1 or
-g M g^-1 with non-negative entries. The check finds such a g, with entries of absolute value at most 6, for every one.
It also checks that every matrix of trace +-3 among them is, up to sign, conjugate to LR (class number one for
discriminant 5).
"""
import itertools
import numpy as np

B = 5
mats = [np.array([[a, b], [c, d]]) for a, b, c, d in itertools.product(range(-B, B + 1), repeat=4)
        if a * d - b * c == 1 and abs(a + d) > 2]
G = [np.array([[a, b], [c, d]]) for a, b, c, d in itertools.product(range(-6, 7), repeat=4) if a * d - b * c == 1]
Ginv = [np.array([[g[1, 1], -g[0, 1]], [-g[1, 0], g[0, 0]]]) for g in G]
GA = np.array(G); GI = np.array(Ginv)


def peel(N):
    word = []
    while not (N == np.eye(2, dtype=int)).all():
        if (N[:, 0] >= N[:, 1]).all():           # N = N' R with N' = N R^-1 non-negative
            N = N @ np.array([[1, 0], [-1, 1]]); word.append("R")
        else:
            N = N @ np.array([[1, -1], [0, 1]]); word.append("L")
        assert (N >= 0).all()
    return "".join(reversed(word))


ok = 0; trace3 = 0
for M in mats:
    C = GA @ M @ GI                               # all conjugates g M g^-1 at once
    found = None
    for s in (1, -1):
        hit = np.where((s * C >= 0).all(axis=(1, 2)))[0]
        if len(hit):
            found = s * C[hit[0]]; break
    assert found is not None, M
    w = peel(found.copy())
    assert "L" in w and "R" in w
    if abs(M[0, 0] + M[1, 1]) == 3:
        assert w in ("LR", "RL"), (M, w)          # the trace-3 class is that of LR
        trace3 += 1
    ok += 1
print(f"{len(mats)} hyperbolic matrices with entries of absolute value at most {B}: every one is, up to sign, conjugate to a positive word in L and R containing both letters ({ok} of {len(mats)})")
assert ok == len(mats) == 168
print(f"every one of the {trace3} matrices of trace +-3 among them is, up to sign, conjugate to LR")
assert trace3 > 0
