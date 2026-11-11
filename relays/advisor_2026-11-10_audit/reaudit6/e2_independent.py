#!/usr/bin/env python3
"""Re-audit 6, the finding E2: the figure-eight knot group's congruence level, computed again in this seat's own code.

Main's mend (c61dc18e6) says: the image of the knot group has order 10, 320 and 20,480 at (2), (4) and (8); in
SL(2, O_3/I)/{+-1} its index is 6 at (2) and 12 at (4); 2 is inert; the level is (4); the old "(8)" is the reading in the
quotient by every central unit of square one (order 960 at (4)), where the image holds two of the four such units.

This script shares no code with main's lock.  O_3 = Z[w] is taken as 2x2 integer matrices (w -> [[0,-1],[1,-1]], which
satisfies w^2 + w + 1 = 0), so a matrix over O_3 is a 4x4 integer matrix and no formula for the ring's product is typed.

    python3 e2_independent.py          (standard library only; about a minute)

EXPECTATIONS, written before the first run.
  x1  main's generators, A = [[1,1],[0,1]] and B = [[1,0],[w^2,1]], satisfy a figure-eight relation  W A = +-B W  exactly in
      O_3, for at least one of the four words W = A B^-1 A^-1 B, A B A^-1 B^-1, A^-1 B A B^-1, A^-1 B^-1 A B; and with z = 1
      in place of w^2 (a different group) none of the four holds
  x2  the image in SL(2, O_3/I) has order 10, 320, 20480 at I = (2), (4), (8)
  x3  SL(2, O_3/I) has order 60, 3840, 245760; at (2) and (4) counted two ways (every matrix; and by products)
  x4  -1 is in the image at (4) and at (8)
  x5  the index of the image in SL(2, O_3/I)/{+-1} is 6, 12, 12
  x6  central units of square one: 1 at (2), 4 at (4), 8 at (8); the image holds 1, 2, 8 of them; the index in the quotient
      by all of them is 6, 6, 12 (the old reading)
  x7  x^2 + x + 1 has no root mod 2: 2 is inert in O_3, so the ideals that contain (4) are (1), (2), (4)
  x8  with Riley's own generator, z = -w, and with z = w and z = -w^2, the orders of x2 and the indices of x5 are the same
  x9  control: with z = 1 the index at (4) is not 12
"""
import itertools, sys

I2, W2, Z2 = ((1, 0), (0, 1)), ((0, -1), (1, -1)), ((0, 0), (0, 0))


def elt(x, y):                                   # x + y w as a 2x2 integer matrix
    return tuple(tuple(x * I2[i][j] + y * W2[i][j] for j in range(2)) for i in range(2))


def block(a, b, c, d):                           # [[a, b], [c, d]] over O_3, each entry a 2x2 block
    rows = []
    for top in ((a, b), (c, d)):
        for i in range(2):
            rows.append(tuple(top[0][i]) + tuple(top[1][i]))
    return tuple(rows)


def mul(X, Y, m):
    n = len(X)
    out = tuple(tuple(sum(X[i][k] * Y[k][j] for k in range(n)) for j in range(n)) for i in range(n))
    return tuple(tuple(v % m for v in r) for r in out) if m else out


def neg(X, m):
    return tuple(tuple((-v) % m if m else -v for v in r) for r in X)


ONE, ZERO = elt(1, 0), elt(0, 0)
ID4 = block(ONE, ZERO, ZERO, ONE)
Z_NAMES = {"w^2 (main's)": (-1, -1), "-w (Riley's)": (0, -1), "w": (0, 1), "-w^2": (1, 1), "1 (control)": (1, 0)}


def gens(z):
    x, y = z
    A, Ai = block(ONE, ONE, ZERO, ONE), block(ONE, elt(-1, 0), ZERO, ONE)
    B, Bi = block(ONE, ZERO, elt(x, y), ONE), block(ONE, ZERO, elt(-x, -y), ONE)
    return A, Ai, B, Bi


def relations(z):
    A, Ai, B, Bi = gens(z)
    words = {"A B^-1 A^-1 B": (A, Bi, Ai, B), "A B A^-1 B^-1": (A, B, Ai, Bi), "A^-1 B A B^-1": (Ai, B, A, Bi), "A^-1 B^-1 A B": (Ai, Bi, A, B)}
    held = []
    for name, word in words.items():
        Wd = ID4
        for g in word:
            Wd = mul(Wd, g, 0)
        left, right = mul(Wd, A, 0), mul(B, Wd, 0)
        if left == right or left == neg(right, 0):
            held.append(name)
    return held


def image(z, m):
    A, Ai, B, Bi = (tuple(tuple(v % m for v in r) for r in g) for g in gens(z))
    start = tuple(tuple(v % m for v in r) for r in ID4)
    seen, frontier = {start}, [start]
    while frontier:
        nxt = []
        for X in frontier:
            for g in (A, Ai, B, Bi):
                Y = mul(X, g, m)
                if Y not in seen:
                    seen.add(Y); nxt.append(Y)
        frontier = nxt
    return seen


def ring(m):
    return [elt(x, y) for x in range(m) for y in range(m)]


def rmul(p, q, m):
    return mul(p, q, m)


def rsub(p, q, m):
    return tuple(tuple((p[i][j] - q[i][j]) % m for j in range(2)) for i in range(2))


def sl_order_by_products(m):
    R = [tuple(tuple(v % m for v in r) for r in e) for e in ring(m)]
    one = tuple(tuple(v % m for v in r) for r in ONE)
    hist = {}
    for b in R:
        for c in R:
            p = rmul(b, c, m); hist[p] = hist.get(p, 0) + 1
    return sum(hist.get(rsub(rmul(a, d, m), one, m), 0) for a in R for d in R)


def sl_order_by_every_matrix(m):
    R = [tuple(tuple(v % m for v in r) for r in e) for e in ring(m)]
    one = tuple(tuple(v % m for v in r) for r in ONE)
    return sum(1 for a, b, c, d in itertools.product(R, repeat=4) if rsub(rmul(a, d, m), rmul(b, c, m), m) == one)


def central(m):
    one = tuple(tuple(v % m for v in r) for r in ONE)
    return [(x, y) for x in range(m) for y in range(m) if rmul(elt(x, y), elt(x, y), m) == one]


results = []


def line(tag, ok, text):
    results.append(bool(ok)); print("%-3s %-6s %s" % (tag, "HOLDS" if ok else "FAILS", text))


rel = {name: relations(z) for name, z in Z_NAMES.items()}
line("x1", rel["w^2 (main's)"] and not rel["1 (control)"],
     "the figure-eight relation W A = +-B W holds exactly for: " + "; ".join("z = %s: %s" % (n, ", ".join(h) if h else "none of the four") for n, h in rel.items()))

LEVELS = (2, 4, 8)
img = {name: {m: image(z, m) for m in LEVELS} for name, z in Z_NAMES.items()}
main_img = img["w^2 (main's)"]
orders = [len(main_img[m]) for m in LEVELS]
line("x2", orders == [10, 320, 20480], "the image's order at (2), (4), (8): %s" % orders)

sl = {m: sl_order_by_products(m) for m in LEVELS}
every = {m: sl_order_by_every_matrix(m) for m in (2, 4)}
line("x3", [sl[m] for m in LEVELS] == [60, 3840, 245760] and every == {2: 60, 4: 3840},
     "|SL(2, O_3/I)| by products: %s; by every matrix at (2), (4): %s" % ([sl[m] for m in LEVELS], [every[2], every[4]]))


def minus_in(image_set, m):
    return tuple(tuple(v % m for v in r) for r in neg(ID4, 0)) in image_set


line("x4", minus_in(main_img[4], 4) and minus_in(main_img[8], 8), "-1 in the image at (2), (4), (8): %s" % [minus_in(main_img[m], m) for m in LEVELS])


def standard_index(image_set, m):
    order = len(image_set) if (m == 2 or minus_in(image_set, m)) else 2 * len(image_set)     # at (2), -1 = 1
    return sl[m] / order


idx = [standard_index(main_img[m], m) for m in LEVELS]
line("x5", idx == [6, 12, 12], "the index in SL(2, O_3/I)/{+-1}: %s" % idx)

old = []
for m in LEVELS:
    cen = central(m)
    held = [c for c in cen if tuple(tuple(v % m for v in r) for r in block(elt(*c), ZERO, ZERO, elt(*c))) in main_img[m]]
    old.append((len(cen), len(held), (sl[m] / len(cen)) / (len(main_img[m]) / len(held))))
line("x6", old == [(1, 1, 6), (4, 2, 6), (8, 8, 12)], "central units of square one, how many the image holds, and the index in the quotient by all of them: %s" % old)
line("x7", all((x * x + x + 1) % 2 for x in (0, 1)), "x^2 + x + 1 mod 2 at x = 0, 1: %s" % [(x * x + x + 1) % 2 for x in (0, 1)])

same = {}
for name in ("-w (Riley's)", "w", "-w^2"):
    same[name] = ([len(img[name][m]) for m in LEVELS], [standard_index(img[name][m], m) for m in LEVELS])
line("x8", all(v == (orders, idx) for v in same.values()), "the other three roots: " + "; ".join("z = %s: orders %s, indices %s" % (n, v[0], v[1]) for n, v in same.items()))
ctl = (len(img["1 (control)"][4]), standard_index(img["1 (control)"][4], 4))
line("x9", ctl[1] != 12, "control z = 1 at (4): order %d, index %s" % ctl)
print()
print("expectations that hold: %d of %d" % (sum(results), len(results)))
sys.exit(0 if all(results) else 1)
