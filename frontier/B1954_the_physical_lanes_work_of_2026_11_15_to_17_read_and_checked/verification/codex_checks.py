"""B1954: main's checks of the physical lane's deliveries of 2026-11-15 to 17 (no data; neither lane's code is run).
1. Its X-APEX defects: every excerpt in its QUOTATIONS.json against agy-exp's files at the pinned head, line by line
   (needs both remote branches; run by hand, its output stored).
2. XA-07: the order of the permutation agy-exp calls a Weyl involution.
3. XA-08 and F05: the central scalar of the normalised Fourier square at p = 3 and 5.
4. Its X-ENDGAME countercheck: the homology of the fourth cyclic cover of m004 (SnapPy; run by hand) and the 45 points.
5. C7: the charges of E8's roots under Q = (2/3)(e1 + e2 + e3), the colour singlets among them, and the circle's periods.
6. F13: two masses of one dimension have dimensional rank one and one free ratio."""
import itertools, json, subprocess
from fractions import Fraction as Fr
import numpy as np
PH = "origin/audit/physical-bridge-2026-09-05"; LOOP = "5de6493f5f1a0300dca64c0fb90afd26925ef1c9"


def quotes():
    show = lambda ref, path: subprocess.run(["git", "show", "%s:%s" % (ref, path)], capture_output=True, text=True).stdout
    Q = json.loads(show(PH, "reports/physical_bridge_2026_09_05/x_apex_review_2026_11_17/QUOTATIONS.json"))
    assert Q["source_commit"] == LOOP
    cache = {}; ok = 0; miss = []; findings = set()
    for c in Q["checks"]:
        if c["path"] not in cache: cache[c["path"]] = show(LOOP, c["path"]).split("\n")
        L = cache[c["path"]]; hit = 1 <= int(c["line"]) <= len(L) and c["exact_excerpt"] in L[int(c["line"]) - 1]
        ok += hit; findings.add(c["finding"])
        if not hit: miss.append((c["finding"], c["path"], c["line"]))
    return ok, len(Q["checks"]), sorted(findings), miss


def order(perm):
    p = list(range(len(perm))); n = 0
    while True:
        p = [perm[x] for x in p]; n += 1
        if p == list(range(len(perm))): return n


def central_scalar(pr):
    """the sign s with S^2 = s * parity, for the S = c F and T = diag(psi(k x^2)) that satisfy (ST)^3 = S^2"""
    z = np.exp(2j * np.pi / pr); F = np.array([[z ** ((x * y) % pr) for y in range(pr)] for x in range(pr)]) / np.sqrt(pr)
    P = np.array([[1.0 if (x + y) % pr == 0 else 0.0 for y in range(pr)] for x in range(pr)]); found = set()
    for k in range(1, pr):
        T = np.diag([z ** ((k * x * x) % pr) for x in range(pr)])
        for c in (1, -1, 1j, -1j):
            S = c * F
            if np.abs(np.linalg.matrix_power(S @ T, 3) - S @ S).max() < 1e-12: found.add(int(round(((S @ S) @ P)[0, 0].real)))
    return sorted(found)


def e8_charges():
    R = set()
    for i, j in itertools.combinations(range(8), 2):
        for si in (2, -2):
            for sj in (2, -2):
                v = [0] * 8; v[i] = si; v[j] = sj; R.add(tuple(v))
    for s in itertools.product((1, -1), repeat=8):
        if s.count(-1) % 2 == 0: R.add(s)
    ch = {}
    for r in R:
        q = Fr(2, 3) * Fr(r[0] + r[1] + r[2], 2); ch.setdefault(q, [0, 0]); ch[q][0] += 1; ch[q][1] += (r[0] == r[1] == r[2])
    return {str(k): tuple(v) for k, v in sorted(ch.items())}


if __name__ == "__main__":
    ok, n, fs, miss = quotes()
    print("1. the physical lane's excerpts against agy-exp's source at %s: %d of %d found at their cited lines; findings covered: %s to %s (%d)" % (LOOP[:8], ok, n, fs[0], fs[-1], len(fs)))
    for m in miss: print("   MISS", m)
    print("2. XA-07: the permutation [4, 3, 5, 0, 1, 2, 6, 7] has order %d (an involution has order 2)" % order([4, 3, 5, 0, 1, 2, 6, 7]))
    print("3. with (ST)^3 = S^2, the square S^2 is the parity times %s at p = 3 and times %s at p = 5" % (central_scalar(3), central_scalar(5)))
    import snappy
    M = snappy.Manifold("m004"); cyc = [c for c in M.covers(4) if str(c.cover_info()["type"]) == "cyclic"][0]
    A = np.linalg.matrix_power(np.array([[2, 1], [1, 1]]), 4) - np.eye(2, dtype=int)
    print("4. the fourth cyclic cover of m004 has homology %s; |det(LR^4 - 1)| = %d" % (cyc.homology(), abs(round(np.linalg.det(A)))))
    ch = e8_charges()
    print("5. E8's roots under Q = (2/3)(e1 + e2 + e3), charge: (roots, colour singlets among them): %s" % ch)
    print("6. F13: the dimension matrix of two masses is [1, 1], of rank %d; their ratio is dimensionless and free" % np.linalg.matrix_rank(np.array([[1, 1]])))
