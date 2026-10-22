"""B1720's geometry (no model values): every primitive positive class (both letters), its height = Lagrange(w)/2 from the
run lengths' two-sided continued fraction, a representative A in SL(2, Z) whose axis reaches that height, its apex tau,
and the flat lines A fixes up to sign (A^T v = +-v mod Z^2, the contragredient action of B1698's moves)."""
import itertools, math
from fractions import Fraction as Fr
import numpy as np
Lm = np.array([[1, 1], [0, 1]]); Rm = np.array([[1, 0], [1, 1]])
def mat(w):
    M = np.eye(2, dtype=np.int64)
    for ch in w: M = M @ (Lm if ch == "L" else Rm)
    return M
def necklaces(lo, hi):
    out = set()
    for k in range(lo, hi + 1):
        for t in itertools.product("LR", repeat=k):
            w = "".join(t)
            if "L" not in w or "R" not in w: continue
            if any(w == w[:d] * (k // d) for d in range(1, k) if k % d == 0): continue
            out.add(min(w[i:] + w[:i] for i in range(k)))
    return sorted(out, key=lambda s: (len(s), s))
def runs(w):
    i = min(range(len(w)), key=lambda j: (w[j] != "L" or w[j - 1] == "L", j))       # start at the beginning of an L-run
    s = w[i:] + w[:i]; out = []
    for ch, g in itertools.groupby(s): out.append(len(list(g)))
    return out                                                                          # cyclic, alternating L, R runs
def cf_value(seq):                                                                       # the periodic continued fraction [seq; seq; ...]
    x = float(seq[0])
    for _ in range(200):
        v = x
        for a in reversed(seq[1:]): v = a + 1.0 / v
        x = seq[0] + 1.0 / v
    return x
def lagrange(w):
    a = runs(w); n = len(a); best = 0.0
    for k in range(n):
        fwd = a[k:] + a[:k]; bwd = list(reversed(a[:k])) + list(reversed(a[k:]))     # a_{k-1}, a_{k-2}, ...
        x = cf_value(fwd); y = 1.0 / cf_value(bwd)
        best = max(best, x + y)
    return best
GENS = [Lm, Rm, np.array([[1, -1], [0, 1]]), np.array([[1, 0], [-1, 1]])]
def representative(w, h, depth=8):
    M = mat(w); seen = {}; frontier = [np.eye(2, dtype=np.int64)]; best = None
    for _ in range(depth):
        nxt = []
        for g in frontier:
            for G in GENS:
                g2 = g @ G; key = tuple(g2.flatten())
                if key in seen: continue
                seen[key] = 1; nxt.append(g2)
                gi = np.array([[g2[1, 1], -g2[0, 1]], [-g2[1, 0], g2[0, 0]]])
                A = g2 @ M @ gi; a, b, c, d = (int(z) for z in A.flatten())
                if c == 0: continue
                r = math.sqrt((a + d) ** 2 - 4) / (2 * abs(c))
                if best is None or r > best[0] + 1e-12: best = (r, (a, b, c, d))
        frontier = nxt
        if best and abs(best[0] - h) < 1e-9: break
    return best
def fixed_lines(A):
    a, b, c, d = A; AT = np.array([[a, c], [b, d]])
    t = a + d; N = abs(2 - t) * (2 + t)
    out = set()
    for s in (1, -1):
        D = int(round(np.linalg.det(AT - s * np.eye(2))))
        # solve (A^T - s I) v in Z^2 for v in (Q/Z)^2: v = (A^T - s I)^{-1} m, m over a fundamental set
        Minv = np.array([[AT[1, 1] - s, -AT[0, 1]], [-AT[1, 0], AT[0, 0] - s]])        # adjugate
        for m1 in range(abs(D)):
            for m2 in range(abs(D)):
                v = (Fr(int(Minv[0, 0] * m1 + Minv[0, 1] * m2), D) % 1, Fr(int(Minv[1, 0] * m1 + Minv[1, 1] * m2), D) % 1)
                if v == (0, 0): continue
                key = min(v, ((-v[0]) % 1, (-v[1]) % 1))
                out.add(key)
    return sorted(out)
def census(lo=2, hi=8, hmax=4.0):
    rows = []
    for w in necklaces(lo, hi):
        h = lagrange(w) / 2
        if h > hmax: continue
        r, A = representative(w, h)
        assert abs(r - h) < 1e-9, (w, r, h)
        a, b, c, d = A; xc = (a - d) / (2 * c)
        rows.append({"word": w, "height": h, "A": A, "tau": (xc, h), "lines": fixed_lines(A)})
    return rows
if __name__ == "__main__":
    import sys
    hi = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    rows = census(2, hi)
    print(len(rows), "classes with apex height <= 4; total lines", sum(len(r["lines"]) for r in rows))
    for r in rows[:8]: print(r["word"], "h %.4f" % r["height"], "tau (%.3f, %.3f)" % r["tau"], "A", r["A"], "lines", len(r["lines"]))
    print("mirror check LLR/LRR heights:", [round(x["height"], 6) for x in rows if x["word"] in ("LLR", "LRR")])
