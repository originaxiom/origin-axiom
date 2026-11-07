"""R76-4 / P-711 (data-free): the line stabilizers' images in PSL(2, Z/4) ~ S4 and their commutants on a 3-dim
irreducible of S4 (the generation block, as P-711 states it). Brute force in SL(2, Z/20) (onto both levels, by CRT).
An element's S4 cycle type from its order in PSL(2, Z/4) and whether it is +-I mod 2 (the Klein four = the kernel to
PSL(2, Z/2) ~ S3). Commutant dimension = (1/|K|) sum chi(k)^2, chi the standard 3-dim character (sign twist: same)."""
import itertools
from fractions import Fraction as F
M = 20
SL = [g for g in itertools.product(range(M), repeat=4) if (g[0] * g[3] - g[1] * g[2]) % M == 1]
assert len(SL) == 5760
def mul4(g, h):
    a, b, c, d = g; e, f, gg, hh = h
    return ((a * e + b * gg) % 4, (a * f + b * hh) % 4, (c * e + d * gg) % 4, (c * f + d * hh) % 4)
def pslkey(g):
    g = tuple(x % 4 for x in g); m = tuple((-x) % 4 for x in g); return min(g, m)
def order_psl(g):
    I = (1, 0, 0, 1); x = g; k = 1
    while pslkey(x) != pslkey(I):
        x = mul4(x, g); k += 1
    return k
def chi3(g):
    o = order_psl(g)
    if o == 1: return 3
    if o == 3: return 0
    if o == 4: return -1
    # order 2: double transposition iff +-I mod 2
    g2 = tuple(x % 2 for x in g)
    return -1 if g2 == (1, 0, 0, 1) else 1
def image(v):
    a, b = v; out = set()
    for g in SL:
        x = (a * g[0] + b * g[2]) % 1; y = (a * g[1] + b * g[3]) % 1
        if (x, y) == (a % 1, b % 1) or (x, y) == ((-a) % 1, (-b) % 1):
            out.add(pslkey(g))
    return out
full = set(pslkey(g) for g in SL)
assert len(full) == 24 and sum(chi3(g) ** 2 for g in full) == 24          # PSL(2, Z/4) has order 24; chi3 irreducible
for v, label in (((F(2, 5), F(4, 5)), "B1841's row line, order 5"), ((F(1, 5), F(2, 5)), "RL's other fixed line, order 5"),
                 ((F(1, 5), F(3, 5)), "LR's line, order 5"), ((F(1, 10), F(3, 10)), "an order-10 line"),
                 ((F(3, 10), F(1, 2)), "an order-10 line"), ((F(1, 10), F(1, 5)), "an order-10 line"), ((F(1, 2), F(0)), "an order-2 line")):
    K = image(v)
    dim = sum(chi3(k) ** 2 for k in K) / len(K)
    types = sorted(set(order_psl(k) for k in K))
    print(f"{label:32s} v = ({v[0]}, {v[1]}): image in PSL(2, Z/4) of order {len(K):2d} (element orders {types}); commutant on the 3 = {dim:g}")
