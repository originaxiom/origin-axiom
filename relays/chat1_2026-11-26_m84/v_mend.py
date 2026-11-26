#!/usr/bin/env python3
"""V-MEND (chat1, 2026-11-26; data-free): is main's mend of B1986's listen4.py (M84, harvest row 2018, main at 6f80ac0e5)
right and complete, and is the same output's W+- gap line right? Not blind: the seat has read, through the mask, the
old and new committed outputs, B1986's FINDINGS.md (lines 28 to 52 and its dated note) and row 2018. Nothing is
compared with data.

    python3 -B v_mend.py <checkout of main at 6f80ac0e5>     (under a minute)

The seat's own code builds the orbits (main's L, R and point sets as listen4.py states them: the cusp's leaf, near the
common point mod 9, 25, 49 with coordinates in 3Z/9, 5Z/25, 7Z/49; the whole leaf mod p). Main's listen4.py is only
run, not imported.

CONDITION, written before the run.
 M1 (exact, the seat's code) on every orbit of the three neighbourhoods: the nullity over Q of W+ - 2I is 1, and the
    period h of the move graph (u -> L u, u -> R u; strongly connected, the orbit being finite and the moves
    invertible) is read. By Perron-Frobenius (W+ nonnegative, irreducible, Perron root 2) the eigenvalues of modulus 2
    are 2 exp(2 pi i k / h), each simple, so the predicted label "non-constant W+ modes with |eigenvalue| = 2" is
    -2.0000 where h = 2 and none where h = 1 (another h is reported as such). Pass: nullity 1 on every orbit, and
    nullity(W+ + 2I) = 1 exactly where h = 2.
 M2 main's corrected listen4.py, rerun here: its label equals M1's prediction on every orbit line, in order.
 M3 main's new committed listen4_run.txt: its label equals M1's prediction on every orbit line, in order.
 M4 the old (18bb9e0da) and new (6f80ac0e5) committed outputs differ on exactly 14 lines, each an orbit of 24 points,
    and on each only the label changes, from 2.0000 to -2.0000.
 M5 (informational) the lines on which this rerun differs from the new committed output, and in which column.
 G  the whole leaf's big orbit mod p = 5, 7, 11, 13, 17, 19, read with numpy's eigvalsh (W+- is symmetric): lambda_2,
    the second eigenvalue by value; lambda_min; the one-sided gap 4 - lambda_2; the two-sided gap 4 - max(|lambda_2|,
    |lambda_min|).
    G1 at p = 5, 7, 11, 13 the committed output's "gap of W+-" equals 4 - lambda_2 to its four decimals. The seat
       expects a failure at p = 5, where the printed "second eigenvalue" is -3.7033, the second by modulus.
    G2 B1986's page (its post hoc line) gives the gap below the top as 0.52, 0.34, 0.13, 0.097, 0.052 and 0.13 at p =
       5 to 19: 4 - lambda_2 rounds to each at its printed digits, and the big orbit is the whole leaf without the
       common point (p^2 + 3 (-1/p) p points).
    G3 (informational) the two-sided gap at each p.
 Reading: M1 to M4 pass -> the mend is right and complete for the mode label. M5 says whether the output reproduces
 byte for byte here. G1 failing at p = 5 alone with G2 passing -> the run's mod-5 gap line is a second label of the
 same kind (a sort by modulus), the page's own numbers are right, and no claim rests on the printed 7.7033. Any other
 pattern is reported as found.
"""
import sys, re, math, pathlib, subprocess
from itertools import product
from functools import reduce
import numpy as np
import sympy

main_dir = pathlib.Path(sys.argv[1]).resolve()
head = subprocess.run(["git", "-C", str(main_dir), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
if not head.startswith("6f80ac0e5"):
    sys.exit("refused: checkout at %s" % head[:9])
card = next((main_dir / "frontier").glob("B1986_*")) / "verification"
REL = "frontier/%s/verification/listen4_run.txt" % card.parent.name

def setup(N, near):
    L = lambda v: (v[0], v[2], (v[0] * v[2] - v[1]) % N)
    R = lambda v: (v[2], v[1], (v[1] * v[2] - v[0]) % N)
    vals = range(0, N, near) if near else range(N)
    pts = [v for v in product(vals, repeat=3) if (v[0] ** 2 + v[1] ** 2 + v[2] ** 2 - v[0] * v[1] * v[2]) % N == 0]
    return pts, L, R

def orbits(pts, L, R):
    seen, out = set(), []
    for v in pts:
        if v in seen:
            continue
        s, st = {v}, [v]
        while st:
            u = st.pop()
            for f in (L, R):
                w = f(u)
                if w not in s:
                    s.add(w); st.append(w)
        seen |= s
        out.append(sorted(s))
    return sorted(out, key=len)        # stable: discovery order within a size, as listen4.py lists them

def wplus(o, L, R):
    idx = {v: i for i, v in enumerate(o)}
    M = [[0] * len(o) for _ in o]
    for v in o:
        M[idx[L(v)]][idx[v]] += 1
        M[idx[R(v)]][idx[v]] += 1
    return M

def period(o, L, R):
    lev, st, g = {o[0]: 0}, [o[0]], 0
    while st:
        u = st.pop(0)
        for f in (L, R):
            w = f(u)
            if w not in lev:
                lev[w] = lev[u] + 1; st.append(w)
    for u in o:
        for f in (L, R):
            g = math.gcd(g, lev[u] + 1 - lev[f(u)])
    return g

def nullity(M, c):
    A = sympy.Matrix(M) - c * sympy.eye(len(M))
    return len(M) - A.rank()

ORB = re.compile(r"orbit of\s+(\d+): W\+ top (.*?) \| W\+- top (.*?) \| non-constant W\+ modes with \|eigenvalue\| = 2: (.*)$")
BIG = re.compile(r"== mod (\d+), the cusp's leaf big orbit \((\d+) points\): W\+ second \|eigenvalue\| ([-\d.]+) \(top 2\); "
                 r"W\+- second eigenvalue ([-\d.]+) \(top 4\); gap of W\+- ([-\d.]+)")

def orbit_lines(text):
    return [m.groups() for m in map(ORB.search, text.splitlines()) if m]

if __name__ == "__main__":
    # M1
    pred, ok1 = [], True
    for N, near in ((9, 3), (25, 5), (49, 7)):
        pts, L, R = setup(N, near)
        for o in orbits(pts, L, R):
            W = wplus(o, L, R)
            h = period(o, L, R)
            n2, nm2 = nullity(W, 2), nullity(W, -2)
            lab = {1: "none", 2: "-2.0000"}.get(h, "h = %d" % h)
            ok1 &= (n2 == 1) and (nm2 == (1 if h == 2 else 0))
            pred.append((N, len(o), h, n2, nm2, lab))
    print("M1 exact: %d orbits; nullity(W+ - 2I) = 1 on all: %s; periods by size:" % (len(pred), all(p[3] == 1 for p in pred)))
    for N in (9, 25, 49):
        sizes = sorted({(p[1], p[2], p[4]) for p in pred if p[0] == N})
        print("   mod %d: %s" % (N, ", ".join("size %d: h = %d, nullity(W+ + 2I) = %d" % s for s in sizes)))
    print("M1 %s" % ("PASS" if ok1 else "FAIL"))

    # M2 and M5
    rerun = subprocess.run([sys.executable, "-B", "listen4.py"], cwd=card, capture_output=True, text=True).stdout
    new = (card / "listen4_run.txt").read_text()
    old = subprocess.run(["git", "-C", str(main_dir), "show", "18bb9e0da:" + REL], capture_output=True, text=True).stdout
    want = [p[5] for p in pred]
    sizes = [str(p[1]) for p in pred]
    def check(lines):
        return len(lines) == len(want) and all(l[3] == w and l[0] == s for l, w, s in zip(lines, want, sizes))
    print("M2 rerun's labels equal M1's prediction on all %d orbit lines: %s" % (len(want), "PASS" if check(orbit_lines(rerun)) else "FAIL"))
    print("M3 new committed labels equal M1's prediction: %s" % ("PASS" if check(orbit_lines(new)) else "FAIL"))

    # M4
    ol, nl = old.splitlines(), new.splitlines()
    diff = [(a, b) for a, b in zip(ol, nl) if a != b]
    ok4 = len(ol) == len(nl) and len(diff) == 14
    for a, b in diff:
        ma, mb = ORB.search(a), ORB.search(b)
        ok4 &= bool(ma and mb) and ma.group(1) == "24" and ma.groups()[:3] == mb.groups()[:3] \
            and ma.group(4) == "2.0000" and mb.group(4) == "-2.0000"
    print("M4 old -> new: %d lines differ; each a 24-point orbit with only the label 2.0000 -> -2.0000: %s"
          % (len(diff), "PASS" if ok4 else "FAIL"))

    rl = rerun.splitlines()
    d5 = [i for i, (a, b) in enumerate(zip(rl, nl)) if a != b]
    cols = {}
    for i in d5:
        ma, mb = ORB.search(rl[i]), ORB.search(nl[i])
        if ma and mb:
            for k, name in ((1, "W+ top"), (2, "W+- top"), (3, "label")):
                if ma.group(k + 1) != mb.group(k + 1):
                    cols[name] = cols.get(name, 0) + 1
        else:
            cols["other line"] = cols.get("other line", 0) + 1
    print("M5 rerun vs new committed: %d of %d lines differ (line counts %d, %d); differing columns: %s"
          % (len(d5), len(nl), len(rl), len(nl), cols or "none"))
    for i in d5:
        print("   line %d" % (i + 1))
        print("     here: %s" % rl[i].strip())
        print("     main: %s" % nl[i].strip())

    # G
    printed = {int(m.group(1)): m.groups() for m in map(BIG.search, nl) if m}
    page = {5: "0.52", 7: "0.34", 11: "0.13", 13: "0.097", 17: "0.052", 19: "0.13"}
    ok1g, ok2g = {}, True
    for p in (5, 7, 11, 13, 17, 19):
        pts, L, R = setup(p, 0)
        big = max(orbits(pts, L, R), key=len)
        leg = 1 if p % 4 == 1 else -1
        W = np.array(wplus(big, L, R), dtype=float)
        S = W + W.T
        ev = np.sort(np.linalg.eigvalsh(S))[::-1]
        top, l2, lmin = ev[0], ev[1], ev[-1]
        one, two = 4 - l2, 4 - max(abs(l2), abs(lmin))
        digits = len(page[p].split(".")[1])
        r2 = ("%." + str(digits) + "f") % one == page[p] and len(big) == p * p + 3 * leg * p
        ok2g &= r2
        line = "G  p = %2d: big orbit %3d points (p^2 + 3(-1/p)p = %d); top %.6f; lambda_2 %.6f; lambda_min %.6f; " \
               "one-sided gap %.4f; two-sided gap %.4f; page %s %s" % (p, len(big), p * p + 3 * leg * p, top, l2, lmin, one,
                                                                     two, page[p], "agrees" if r2 else "DISAGREES")
        if p in printed:
            g = printed[p][4]
            ok1g[p] = ("%.4f" % one) == g
            line += "; committed output: second %s, gap %s, %s" % (printed[p][3], g, "= 4 - lambda_2" if ok1g[p] else "NOT 4 - lambda_2")
        print(line)
    print("G1 committed gap = 4 - lambda_2 at %s; fails at %s" % ([p for p in ok1g if ok1g[p]] or "none",
                                                                 [p for p in ok1g if not ok1g[p]] or "none"))
    print("G2 page's gaps agree at every p: %s" % ("PASS" if ok2g else "FAIL"))
