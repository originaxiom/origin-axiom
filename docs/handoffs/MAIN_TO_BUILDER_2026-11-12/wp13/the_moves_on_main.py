#!/usr/bin/env python3
"""WP-1.3, first step: what "no period" removes among the words of the grammar, exactly, and what it does not.

Exact integer matrices.  L = [[1, 1], [0, 1]], R = [[1, 0], [1, 1]].
  1. POSITIVE WORDS (GM2 alone).  No positive word has finite order.  A positive word is parabolic exactly when it uses
     one letter, and hyperbolic (trace at least 3) exactly when it uses both.
  2. WITH INVERSE LETTERS (GM5b).  Words of finite order appear: every trace in {-2, ..., 2} occurs.  "No period" removes
     the classes of finite order; it does not remove a single shear, whose powers are never the identity.
  3. THE FORMAL STATEMENT'S TEST (B1867): an act is cancelled when it is the identity or becomes it when repeated.  By
     that test a single shear is not cancelled, at any power checked; a word of trace -1, 0 or 1 is.
How it could fail: a planted elliptic matrix among the positive words; a wrong shear whose square is the identity.
"""
import itertools, json, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
L, R = ((1, 1), (0, 1)), ((1, 0), (1, 1))
Li, Ri = ((1, -1), (0, 1)), ((1, 0), (-1, 1))
I2 = ((1, 0), (0, 1))
def mul(x, y): return tuple(tuple(sum(x[i][k] * y[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def mat(word, table):
    m = I2
    for ch in word: m = mul(m, table[ch])
    return m
def tr(m): return m[0][0] + m[1][1]
def order(m, cap=24):
    """the least n with m^n = 1 (up to cap), or None"""
    p = I2
    for n in range(1, cap + 1):
        p = mul(p, m)
        if p == I2: return n
    return None
CHECKS, FAILS = [], []
def check(name, ok, detail=""):
    CHECKS.append({"check": name, "holds": bool(ok), "detail": detail}); print("%s  %s%s" % ("ok  " if ok else "FAIL", name, ("  [%s]" % detail) if detail else ""))
    if not ok: FAILS.append(name)

POS = {"L": L, "R": R}
pos = [("".join(w), mat(w, POS)) for n in range(1, 13) for w in itertools.product("LR", repeat=n)]
one = [(w, m) for w, m in pos if len(set(w)) == 1]; both = [(w, m) for w, m in pos if len(set(w)) == 2]
check("1: no positive word to length 12 has finite order", all(order(m) is None for w, m in pos), "%d words" % len(pos))
check("1: a positive word with one letter has trace 2 and is not the identity", all(tr(m) == 2 and m != I2 for w, m in one), "%d words" % len(one))
check("1: a positive word with both letters has trace at least 3", all(tr(m) >= 3 for w, m in both) and min(tr(m) for w, m in both) == 3, "%d words; least trace %d, at %s" % (len(both), min(tr(m) for w, m in both), sorted(w for w, m in both if tr(m) == 3)[:4]))
check("1: every entry of a positive word is non-negative and the diagonal is at least 1", all(min(m[0] + m[1]) >= 0 and m[0][0] >= 1 and m[1][1] >= 1 for w, m in pos))

ALL = {"L": L, "R": R, "l": Li, "r": Ri}
signed = [("".join(w), mat(w, ALL)) for n in range(1, 7) for w in itertools.product("LRlr", repeat=n)]
by_trace = {}
for w, m in signed:
    by_trace.setdefault(tr(m), []).append((w, m))
small = {t: sorted(by_trace[t], key=lambda x: (len(x[0]), x[0]))[0] for t in range(-2, 3) if t in by_trace}
check("2: with inverse letters every trace from -2 to 2 occurs among words to length 6", sorted(small) == [-2, -1, 0, 1, 2], "; ".join("%d at %s" % (t, small[t][0]) for t in sorted(small)))
fin = {t: sorted({order(m) for w, m in by_trace[t]}, key=lambda x: (x is None, x)) for t in (-1, 0, 1)}
check("2: the words of trace -1, 0 and 1 have orders 3, 4 and 6", fin == {-1: [3], 0: [4], 1: [6]}, str(fin))
par = [(w, m) for t in (-2, 2) for w, m in by_trace[t] if m not in (I2, ((-1, 0), (0, -1)))]
check("2: a word of trace 2 or -2 that is not plus or minus the identity never has finite order", all(order(m) is None for w, m in par), "%d words" % len(par))
check("3: a single shear is not the identity at any power to 24, so the formal statement does not cancel it", order(L) is None and order(R) is None)
check("3: the shortest word of trace 1 becomes the identity when repeated six times", order(small[1][1]) == 6, small[1][0])
# planted
check("planted: an elliptic matrix among the words would be seen", order(((0, -1), (1, 1))) == 6)
check("planted: a matrix whose square is the identity is seen as of finite order", order(((-1, 0), (0, -1))) == 2)
res = {"checks": CHECKS, "failing": FAILS, "count": len(CHECKS), "least words by trace": {str(t): small[t][0] for t in small}}
(HERE / "the_moves_on_main.json").write_text(json.dumps(res, indent=1) + "\n", encoding="utf-8")
print("\n%d checks, %d failing" % (len(CHECKS), len(FAILS)))
sys.exit(1 if FAILS else 0)
