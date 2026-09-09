#!/usr/bin/env python3
"""B1352 stage A''' -- IS THE LOCUS POINT AN Sp(8)-POINT?  The self-dual subgroup of E6 containing the subregular sl2 is
Sp(8) (the subregular sl2 of E6 is the principal sl2 of C4; 27 = Lambda^2_0(8) = 13 + 9 + 5 under it).  An element of
Sp(8) with eigenvalues y_i^{+-1} (i = 1..4) on the 8 acts on the 27 with eigenvalues {y_i^{+-1} y_j^{+-1} : i < j} (24 of
them) and three 1's: every Sp(8)-valued representation has exactly these three cusp-fixed weights.  Test on the banked
points: the 27 eigenvalue logs l_k of rho(a) must be {+-u_i +- u_j} u {0, 0, 0} for four numbers u_i.  The u_i are
recovered from the sums l + l' (2u_i = (u_i + u_j) + (u_i - u_j) occurs for three j's), then the pattern is verified.
Usage: python3 locus_point_is_sp8.py [points.json ...]"""
import sys, os, json, itertools
import mpmath as mp
mp.mp.dps = 100
HERE = os.path.dirname(os.path.abspath(__file__))
paths = sys.argv[1:] or [os.path.join(HERE, "fixed_locus_points.json"),
                         os.path.join(HERE, "..", "..", "B1350_the_v10_direction", "verification", "v10_direction_points.json")]
n = 27
TOL = mp.mpf('1e-30')
def load(path):
    d = json.load(open(path))
    for name, v in d.items():
        yield name, {int(g): mp.matrix([[mp.mpc(mp.mpf(re), mp.mpf(im)) for (re, im) in row] for row in v[g]]) for g in ("1", "2")}
def sp8_test(M, label):
    logs = [mp.log(z) for z in mp.eig(M, left=False, right=False)]
    ones = [l for l in logs if abs(l) < TOL]
    rest = [l for l in logs if abs(l) >= TOL]
    # candidates u = (l + l')/2; a true u_i is characterised by S containing both u_i + w and u_i - w for the six
    # values w = +-u_j (j != i): score(u) = #{s in S : 2u - s in S} >= 6, while a false candidate scores ~2 at most
    def close(a, b): return abs(a - b) < TOL * 1e6
    cands = []
    for a, b in itertools.combinations(range(len(rest)), 2):
        c = (rest[a] + rest[b]) / 2
        if abs(c) < TOL * 1e6: continue
        cands.append(c)
    def score(u): return sum(1 for s in rest if any(close(2 * u - s, s2) for s2 in rest))
    U = []
    for c in cands:
        if any(close(c, w) or close(c, -w) for w in U): continue
        if score(c) >= 6: U.append(c)
    ok = False; U4 = None
    def fits(U4):
        pattern = [s1 * U4[i] + s2 * U4[j] for i, j in itertools.combinations(range(4), 2) for s1 in (1, -1) for s2 in (1, -1)]
        used = [False] * len(rest)
        for pv in pattern:
            k = next((k for k in range(len(rest)) if not used[k] and close(rest[k], pv)), None)
            if k is None: return False
            used[k] = True
        return all(used)
    if len(rest) == 24:
        for quad in itertools.combinations(U, 4):
            if fits(quad): ok = True; U4 = quad; break
    print(f"      {label}: eigenvalues equal to 1: {len(ones)}; Sp(8) pattern {{+-u_i +- u_j}} on the other {len(rest)}: {'YES' if ok else 'NO'}" + (f"; u = {[mp.nstr(u, 6) for u in U4]}" if ok else f"; candidates with score >= 6: {len(U)}, no 4 of them fit"))
for path in paths:
    print(f"== {os.path.relpath(path, HERE)}")
    for name, mats in load(path):
        print(f"    {name}")
        sp8_test(mats[1], "rho(a)"); sp8_test(mats[2], "rho(b)")
