#!/usr/bin/env python3
"""Spot checks by the advisor seat of the reader's recomputation in this folder: a few of its central facts, computed
again in the seat's own few lines, by other routes.  Exact integers and one square root.
    python3 -B spot_checks_by_the_seat.py"""
import math, itertools
from fractions import Fraction as Fr

ok = True
def check(label, cond):
    global ok; ok &= bool(cond); print("%-118s %s" % (label, "ok" if cond else "FAILS"))

# ---- 1. the two curves at level 5, from the action of the modular group on cosets (not from the classical formulas)
def cycles(perm):
    seen, out = set(), []
    for x in perm:
        if x in seen: continue
        n, y = 0, x
        while y not in seen: seen.add(y); y = perm[y]; n += 1
        out.append(n)
    return sorted(out)
def curve(points, act):
    """index, cusp widths, points fixed by S and by ST, genus: S = [[0,-1],[1,0]], T = [[1,1],[0,1]], acting on the right"""
    S = {p: act(p, (0, -1, 1, 0)) for p in points}; T = {p: act(p, (1, 1, 0, 1)) for p in points}; ST = {p: T[S[p]] for p in points}
    n = len(points); widths = cycles(T); e2 = sum(1 for p in points if S[p] == p); e3 = sum(1 for p in points if ST[p] == p)
    genus = Fr(1) + Fr(n, 12) - Fr(e2, 4) - Fr(e3, 3) - Fr(len(widths), 2)
    return n, widths, e2, e3, genus
N = 5
def norm_line(v):                       # a point of the projective line over Z/5
    a, b = v[0] % N, v[1] % N
    for k in range(1, N):
        if (k * a) % N == 1 or (a == 0 and (k * b) % N == 1): return ((k * a) % N, (k * b) % N)
def norm_pm(v):                         # a nonzero vector of (Z/5)^2 up to sign
    a, b = v[0] % N, v[1] % N; return min((a, b), ((-a) % N, (-b) % N))
right = lambda v, m: (v[0] * m[0] + v[1] * m[2], v[0] * m[1] + v[1] * m[3])
lines = sorted({norm_line((a, b)) for a in range(N) for b in range(N) if (a, b) != (0, 0)})
vecs = sorted({norm_pm((a, b)) for a in range(N) for b in range(N) if (a, b) != (0, 0)})
c0 = curve(lines, lambda p, m: norm_line(right(p, m))); c1 = curve(vecs, lambda p, m: norm_pm(right(p, m)))
print("the curve of lines:", c0, "| the curve of vectors up to sign:", c1)
check("the curve of lines: index 6, two cusps of widths 1 and 5, two points of order 2, none of order 3, genus 0", c0 == (6, [1, 5], 2, 0, 0))
check("the curve of vectors up to sign: index 12, four cusps of widths 1, 1, 5, 5, no elliptic point, genus 0", c1 == (12, [1, 1, 5, 5], 0, 0, 0))

# ---- 2. heights of a cyclic run sequence: the radius of the axis of the product of [[c,1],[1,0]], greatest over rotations
def mul(A, B): return (A[0]*B[0]+A[1]*B[2], A[0]*B[1]+A[1]*B[3], A[2]*B[0]+A[3]*B[2], A[2]*B[1]+A[3]*B[3])
def apex(runs):
    best = 0.0
    for r in range(len(runs)):
        M = (1, 0, 0, 1)
        for c in runs[r:] + runs[:r]: M = mul(M, (c, 1, 1, 0))
        if len(runs) % 2: M = mul(M, M)                       # an odd number of runs: the square is the orientable history
        a, b, c, d = M; best = max(best, math.sqrt((a + d) ** 2 - 4 * (a * d - b * c)) / (2 * abs(c)))
    return best
check("a run of 6 closed by three runs of 1 reads 3.651483717 (the reader's value; here %.9f)" % apex([6, 1, 1, 1]), abs(apex([6, 1, 1, 1]) - 3.651483717) < 5e-10)
check("the ground alone reads sqrt 5 / 2 (here %.11f)" % apex([1, 1]), abs(apex([1, 1]) - math.sqrt(5) / 2) < 1e-12)
lim = 2.5 + math.sqrt(5) / 2
check("a run of 6 in a long ground tends to 5/2 + sqrt 5 / 2 = %.9f (here, 41 runs of 1: %.9f)" % (lim, apex([6] + [1] * 41)), abs(apex([6] + [1] * 41) - lim) < 1e-9)

# ---- 3. the letters.  The foundation: L = [[1,1],[0,1]], R = [[1,0],[1,1]].  The web seat's notes: L and R exchanged.
def eigenlines(M):
    return sorted(norm_line(v) for v in lines if norm_line((M[0] * v[0] + M[1] * v[1], M[2] * v[0] + M[3] * v[1])) == v)
Lf, Rf = (1, 1, 0, 1), (1, 0, 1, 1)
LR_f, RL_f = mul(Lf, Rf), mul(Rf, Lf)
print("in the foundation's letters: LR =", LR_f, "keeps the lines", eigenlines(LR_f), "| RL =", RL_f, "keeps the lines", eigenlines(RL_f))
# The seat's first version of the next check expected LR to keep two lines, (1,2) and (1,4), and failed: at level 5 the
# ground has a repeated eigenvalue and keeps exactly one line.  The check now states what was computed.
check("in the foundation's letters LR keeps exactly one line, (1,2); the line (1,3) is RL's, and its only one", eigenlines(LR_f) == [(1, 2)] and eigenlines(RL_f) == [(1, 3)])
check("with L and R exchanged, as the notes write them, LR = [[1,1],[1,2]] and (1,3) is its one line", mul(Rf, Lf) == (1, 1, 1, 2) and eigenlines(mul(Rf, Lf)) == [(1, 3)])
print("spot checks: %s" % ("every one holds" if ok else "ONE FAILS"))
