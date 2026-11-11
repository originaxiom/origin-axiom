#!/usr/bin/env python3
"""Re-audit 6, the finding E2: a second check, written AFTER the first run of e2_independent.py and because of it.

The first run's expectation x1 FAILED: main's pair, A = [[1,1],[0,1]] and B = [[1,0],[w^2,1]], satisfies none of the four
relations  W A = +-B W  that were tried, while Riley's z = -w and z = -w^2 each satisfy two.  Every number of the lock held
all the same (x2 to x9), and held equally for all four z (x8).

Before this script ran, this seat's reading was: x1 was too narrow, not main's pair wrong.  D = diag(1, -1) lies in
PGL(2, O_3), carries A to A^-1 and [[1,0],[z,1]] to [[1,0],[-z,1]], and normalises PSL(2, O_3) and every principal
congruence subgroup.  So main's group is the D-conjugate of the group of the pair with z = -w^2, which does satisfy the
relation; main's own pair satisfies it once A is inverted.

EXPECTATIONS, written before this script's first run.
  y1  D A D^-1 = A^-1 and D B(z) D^-1 = B(-z), exactly, for z = w^2
  y2  for main's z = w^2, the relation  W(a, b) a = +-b W(a, b)  holds for the pair (a, b) = (A^-1, B) and for (A, B^-1),
      each with at least one of the four words; and for (A, B) and (A^-1, B^-1) with none
  y3  control, z = 1: with none of the four words for any of the four pairs
"""
import sys

I2, W2 = ((1, 0), (0, 1)), ((0, -1), (1, -1))


def elt(x, y):
    return tuple(tuple(x * I2[i][j] + y * W2[i][j] for j in range(2)) for i in range(2))


def block(a, b, c, d):
    rows = []
    for top in ((a, b), (c, d)):
        for i in range(2):
            rows.append(tuple(top[0][i]) + tuple(top[1][i]))
    return tuple(rows)


def mul(X, Y):
    return tuple(tuple(sum(X[i][k] * Y[k][j] for k in range(4)) for j in range(4)) for i in range(4))


def neg(X):
    return tuple(tuple(-v for v in r) for r in X)


ONE, ZERO = elt(1, 0), elt(0, 0)
ID4 = block(ONE, ZERO, ZERO, ONE)
D = block(ONE, ZERO, ZERO, elt(-1, 0))           # its own inverse


def pair(z):
    x, y = z
    return (block(ONE, ONE, ZERO, ONE), block(ONE, elt(-1, 0), ZERO, ONE), block(ONE, ZERO, elt(x, y), ONE), block(ONE, ZERO, elt(-x, -y), ONE))


def words_that_hold(a, ai, b, bi):
    words = {"a b^-1 a^-1 b": (a, bi, ai, b), "a b a^-1 b^-1": (a, b, ai, bi), "a^-1 b a b^-1": (ai, b, a, bi), "a^-1 b^-1 a b": (ai, bi, a, b)}
    held = []
    for name, word in words.items():
        Wd = ID4
        for g in word:
            Wd = mul(Wd, g)
        left, right = mul(Wd, a), mul(b, Wd)
        if left == right or left == neg(right):
            held.append(name)
    return held


results = []


def line(tag, ok, text):
    results.append(bool(ok)); print("%-3s %-6s %s" % (tag, "HOLDS" if ok else "FAILS", text))


A, Ai, B, Bi = pair((-1, -1))                    # z = w^2
conj = lambda X: mul(mul(D, X), D)
line("y1", conj(A) == Ai and conj(B) == Bi, "D A D^-1 = A^-1: %s;  D B(w^2) D^-1 = B(-w^2): %s" % (conj(A) == Ai, conj(B) == Bi))


def four_pairs(z):
    A, Ai, B, Bi = pair(z)
    return {"(A, B)": words_that_hold(A, Ai, B, Bi), "(A^-1, B)": words_that_hold(Ai, A, B, Bi),
            "(A, B^-1)": words_that_hold(A, Ai, Bi, B), "(A^-1, B^-1)": words_that_hold(Ai, A, Bi, B)}


def show(d):
    return "; ".join("%s: %s" % (k, ", ".join(v) if v else "none") for k, v in d.items())


m = four_pairs((-1, -1))
line("y2", m["(A^-1, B)"] and m["(A, B^-1)"] and not m["(A, B)"] and not m["(A^-1, B^-1)"], "z = w^2 -- " + show(m))
c = four_pairs((1, 0))
line("y3", not any(c.values()), "z = 1 -- " + show(c))
print()
print("expectations that hold: %d of %d" % (sum(results), len(results)))
sys.exit(0 if all(results) else 1)
