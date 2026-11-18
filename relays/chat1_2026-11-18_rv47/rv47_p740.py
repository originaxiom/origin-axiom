#!/usr/bin/env python3
"""The status page's section 9: an independent check of main's per-centre rule for the tube's even-run pattern (B1852's
dated note of 2026-11-18; P-740). Data-free, exact. Computed once, post hoc; written from B1852's statement of the rule,
without main's reverser formula: the reversing involutions are found by search.

    python3 -I -u rv47_p740.py

For every primitive cyclic word w in L = ((1,1),(0,1)) and R = ((1,0),(1,1)), of length 2 to 10 with both letters,
that reads the same backwards up to rotation:
  - its reflection axis gives two centres on the circle, each between two letters or on a letter;
  - the rule predicts, for the two fixed fibres, the classes "= 1 mod 2" (a centre between letters) and "!= 1 mod 2"
    (a centre on a letter);
  - the search: every X = ((a, b), (c, -a)) with a^2 + bc = 1 (an integer involution of determinant -1) and |a|, |b|,
    |c| <= 150 with X W X^-1 = W^-1, W = M(w); the set of their classes mod 2.
P1  the searched set of classes equals the predicted set, on every word.
P2  the control: the prediction with the two kinds of centre exchanged fails on some word.
"""
import itertools

L = ((1, 1), (0, 1)); R = ((1, 0), (1, 1))
mul = lambda X, Y: tuple(tuple(sum(X[i][k] * Y[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def M(w):
    X = ((1, 0), (0, 1))
    for ch in w:
        X = mul(X, L if ch == "L" else R)
    return X


def canon(w):
    return min(w[i:] + w[:i] for i in range(len(w)))


def primitive(w):
    n = len(w)
    return all(w != w[d:] + w[:d] for d in range(1, n) if n % d == 0)


def centres(w):
    """Centres of the reflection axes of the cyclic word: positions 0..2n-1 on a circle of 2n half-steps; even
    positions are gaps (before letter k = pos/2), odd positions are letters (letter (pos-1)/2)."""
    n = len(w); found = set()
    for s in range(0, 2 * n, 2):               # reflection pos -> s - pos (mod 2n); it maps letters to letters only for s even
        ok = all(w[k] == w[((s - (2 * k + 1)) % (2 * n) - 1) // 2] for k in range(n))
        if ok:
            fixed = sorted(p for p in range(2 * n) if (2 * p - s) % (2 * n) == 0)
            found.add(tuple(fixed))
    return found


B = 150
INV = []
for a in range(-B, B + 1):
    t = 1 - a * a
    for b in range(-B, B + 1):
        if b == 0:
            if t == 0:
                INV += [((a, 0), (c, -a)) for c in range(-B, B + 1)]
            continue
        if t % b == 0 and abs(t // b) <= B:
            INV.append(((a, b), (t // b, -a)))

words = sorted({canon("".join(p)) for n in range(2, 11) for p in itertools.product("LR", repeat=n)})
words = [w for w in words if "L" in w and "R" in w and primitive(w)]
checked = mismatch = control_fail = 0
for w in words:
    axes = centres(w)
    if not axes:
        continue
    assert len(axes) == 1, (w, axes)
    (c1, c2), = axes
    pred = {("=1" if c % 2 == 0 else "!=1") for c in (c1, c2)}
    ctrl = {("!=1" if c % 2 == 0 else "=1") for c in (c1, c2)}
    W = M(w); Wi = ((W[1][1], -W[0][1]), (-W[1][0], W[0][0]))
    found = set()
    for X in INV:
        if mul(mul(X, W), X) == Wi:            # X^-1 = X
            found.add("=1" if (X[0][1] % 2 == 0 and X[1][0] % 2 == 0 and X[0][0] % 2 == 1) else "!=1")
    checked += 1
    mismatch += found != pred
    control_fail += found != ctrl
print("P1: %d words with a reflection, length 2 to 10: the searched classes equal the rule's on %d, differ on %d"
      % (checked, checked - mismatch, mismatch))
print("P2: the control (the kinds exchanged) differs on %d of %d" % (control_fail, checked))
