#!/usr/bin/env python3
"""The Gang-Yonekura formula applied to m004, in the form of Celoria-Hodgson-Rubinstein (arXiv:2509.09886, eq. (32)
and the compact form used in their Theorem 13.2):

    I_{M(alpha)}(q) = sum_{k in Z} (-1)^k [ q^{k/2} I^{k alpha} - I^{2 alpha* + k alpha} ],   i(alpha, alpha*) = 1,

with their boundary classes  I^{2x mu + y lambda} = sum_j I_D(j - x, j) I_D(j + y, j - x + y)  (their p. 55), which is
B1428's index_xy(x, two_y = y).  Classes with an odd coefficient of mu have index zero.
Series are dicts {exponent of x = q^(1/2): coefficient}; all arithmetic is exact."""
import sys, json, math, functools, pathlib
REPO = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / "frontier" / "B1428_the_3d_index_computed" / "verification"))
from tet_index import I_delta, s_mul, s_add, s_shift, s_scal, s_trunc, s_str

def delta_x(m, e):
    p = lambda t: max(0, t)
    return p(m) * p(m + e) + p(-m) * p(e) + p(-e) * p(-e - m) + max(0, m, -e)

@functools.lru_cache(maxsize=None)
def IG(m, e, D):
    return I_delta(e, m, D)

def terms(x, y, D):
    """the j with a term of degree <= D, and the least degree bound."""
    J = 3 * (abs(x) + abs(y)) + D + 40
    low = [(delta_x(j - x, j) + delta_x(j + y, j - x + y), j) for j in range(-J, J + 1)]
    js = [j for d, j in low if d <= D]
    assert not js or (min(js) > -J + 5 and max(js) < J - 5), "j-range not safely bounded"
    return js, min(d for d, j in low)

def class_index(a, b, D):
    """I^{a mu + b lambda} to x-degree D (zero if a is odd)."""
    if a % 2: return {}
    x = a // 2; js, _ = terms(x, b, D); tot = {}
    for j in js:
        tot = s_add(tot, s_mul(IG(j - x, j, D), IG(j + b, j - x + b, D), D))
    return tot

def low_degree(a, b):
    return None if a % 2 else terms(a // 2, b, 0)[1]

def dual(p, q):
    """alpha* = r mu + s lambda with r q - s p = 1."""
    g, u, v = ext(q, -p); assert g == 1 and u * q - v * p == 1
    return u, v
def ext(a, b):
    if b == 0: return (abs(a), 1 if a > 0 else -1, 0)
    g, u, v = ext(b, a % b); return (g, v, u - (a // b) * v)

def filled(p, q, X, KMAX=600, TAIL=14):
    """the formula for alpha = p mu + q lambda to x-degree X. Returns (series, info) or (None, info) when the sum has
    infinitely many terms of bounded degree (not absolutely convergent)."""
    r, s = dual(p, q); tot = {}; used = 0; info = dict(dual=[r, s])
    for sign in (1, -1):
        quiet = 0; k = 0 if sign == 1 else -1
        while quiet < TAIL:
            if abs(k) > KMAX: info["divergent"] = True; return None, info
            hit = False
            a, b = k * p, k * q
            if a % 2 == 0:
                lo = low_degree(a, b)
                if lo + k <= X:
                    hit = True; used += 1
                    t = s_shift(class_index(a, b, X - k), k, X)
                    tot = s_add(tot, s_scal(t, 1 if k % 2 == 0 else -1))
                a2, b2 = 2 * r + k * p, 2 * s + k * q
                lo = low_degree(a2, b2)
                if lo <= X:
                    hit = True; used += 1
                    tot = s_add(tot, s_scal(class_index(a2, b2, X), -1 if k % 2 == 0 else 1))
            else:
                hit = None
            if hit is False: quiet += 1
            elif hit: quiet = 0
            k += sign
    info["terms"] = used
    return tot, info

