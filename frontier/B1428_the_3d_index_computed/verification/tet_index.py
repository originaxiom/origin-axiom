"""
Tetrahedron index I_Delta(m,e)(q) of Dimofte-Gaiotto-Gukov.

    I_Delta(m,e)(q) = sum_{n in Z} (-1)^n q^{ n(n+1)/2 - (n + m/2) e } / ( (q)_n (q)_{n+m} )

with (q)_n = (q;q)_n and 1/(q)_n := 0 for n < 0.

CONVENTION USED HERE
--------------------
Everything is carried in the variable

        x = q^{1/2}          (so q = x^2)

because the exponent  n(n+1)/2 - (n + m/2) e  is a half-integer when m*e is odd.
A series is a dict  { integer exponent of x : integer coefficient }.
All coefficients are exact python ints -- no floats anywhere.

In x the term exponent is
        E(n) = 2*( n(n+1)/2 - (n + m/2) e ) = n(n+1) - (2n + m) e
which is an integer for all m,e,n.
"""

from __future__ import annotations
import math


def sgn(k: int) -> int:
    """(-1)**k with an EXACT integer result (python's ** returns a float for k<0)."""
    return -1 if (k % 2) else 1


# ----------------------------------------------------------------- q-series helpers
def inv_pochhammer_table(nmax: int, D: int):
    """R[n] = 1/(q;q)_n as a coefficient list in q, truncated at degree D."""
    R = []
    cur = [0] * (D + 1)
    cur[0] = 1
    R.append(cur[:])
    for n in range(1, nmax + 1):
        new = cur[:]                       # multiply by 1/(1-q^n) = sum_j q^{jn}
        for d in range(n, D + 1):
            new[d] += new[d - n]
        cur = new
        R.append(cur[:])
    return R


def mul_trunc(a, b, D):
    """product of two coefficient lists in q, truncated at degree D."""
    out = [0] * (D + 1)
    for i, ai in enumerate(a):
        if ai == 0 or i > D:
            continue
        lim = D - i
        for j, bj in enumerate(b):
            if j > lim:
                break
            if bj:
                out[i + j] += ai * bj
    return out


# ----------------------------------------------------------------- the tetrahedron index
def I_delta(m: int, e: int, Xmax: int):
    """
    I_Delta(m,e) as a dict {exponent of x = q^{1/2} : int coefficient},
    correct for every exponent <= Xmax.  Exponents above Xmax are dropped.
    """
    res = {}
    nlo = max(0, -m)

    # E(n) = n^2 + n(1-2e) - m e  <= Xmax   ->  finitely many n, quadratic in n
    B = 1 - 2 * e
    C = -m * e - Xmax
    disc = B * B - 4 * C
    if disc < 0:
        return res
    r = math.isqrt(disc) + 2
    n_lo_q = (-B - r) // 2 - 2
    n_hi_q = (-B + r) // 2 + 2

    lo = max(nlo, n_lo_q)
    hi = n_hi_q
    if hi < lo:
        return res

    # biggest q-degree budget needed
    Emin = None
    for n in range(lo, hi + 1):
        E = n * (n + 1) - (2 * n + m) * e
        if E <= Xmax and (Emin is None or E < Emin):
            Emin = E
    if Emin is None:
        return res
    D = (Xmax - Emin) // 2
    R = inv_pochhammer_table(hi + max(m, 0) + 1, D)

    for n in range(lo, hi + 1):
        E = n * (n + 1) - (2 * n + m) * e
        if E > Xmax:
            continue
        d = (Xmax - E) // 2
        prod = mul_trunc(R[n], R[n + m], d)
        sgn = -1 if (n % 2) else 1
        for k, c in enumerate(prod):
            if c:
                res[E + 2 * k] = res.get(E + 2 * k, 0) + sgn * c

    return {k: v for k, v in res.items() if v != 0}


# ----------------------------------------------------------------- series arithmetic (in x)
def s_mul(a, b, Xmax):
    out = {}
    for i, ai in a.items():
        if i > Xmax:
            continue
        for j, bj in b.items():
            k = i + j
            if k <= Xmax:
                out[k] = out.get(k, 0) + ai * bj
    return {k: v for k, v in out.items() if v != 0}


def s_add(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, 0) + v
    return {k: v for k, v in out.items() if v != 0}


def s_shift(a, s, Xmax):
    return {k + s: v for k, v in a.items() if k + s <= Xmax}


def s_scal(a, c):
    return {k: c * v for k, v in a.items() if c * v != 0}


def s_trunc(a, Xmax):
    return {k: v for k, v in a.items() if k <= Xmax}


def s_eq(a, b, Xmax):
    A = s_trunc(a, Xmax)
    B = s_trunc(b, Xmax)
    return {k: v for k, v in A.items() if v} == {k: v for k, v in B.items() if v}


def s_str(a, Xmax=None, var="q"):
    """pretty print.  var='q' prints q^{k/2}; var='x' prints x^k."""
    if Xmax is not None:
        a = s_trunc(a, Xmax)
    items = sorted(a.items())
    if not items:
        return "0"
    parts = []
    for k, v in items:
        if v == 0:
            continue
        if var == "x":
            p = "" if k == 0 else ("*x" if k == 1 else f"*x^{k}")
        else:
            if k == 0:
                p = ""
            elif k % 2 == 0:
                p = "*q" if k == 2 else f"*q^{k//2}"
            else:
                p = f"*q^({k}/2)"
        parts.append(f"{v:+d}{p}")
    return " ".join(parts)
