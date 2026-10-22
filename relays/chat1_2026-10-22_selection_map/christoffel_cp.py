#!/usr/bin/env python3
"""Lemma CP (computed, no data): are the principle's own threads, the Christoffel (Sturmian) words, reversal-symmetric
up to conjugacy?  A word and its reverse are CP images (B1456: M(reverse w) = D M(w)^-1 D^-1), so a reversal-symmetric
class has a closed geodesic invariant under tau -> -conj(tau).  Primitive positive classes of length 2..9 with both
letters.     python3 -B christoffel_cp.py      # writes christoffel_cp_run.txt"""
from math import gcd
from itertools import product
import pathlib

HERE = pathlib.Path(__file__).resolve().parent


def primitive(w):
    n = len(w)
    return all(w != w[d:] + w[:d] for d in range(1, n) if n % d == 0)


def canon(w):
    return min(w[i:] + w[:i] for i in range(len(w)))


def christoffel(p, q):
    """the lower Christoffel word of slope p/q in L (x-step) and R (y-step), length p + q"""
    n = p + q
    return ''.join('R' if (i * p) // n > ((i - 1) * p) // n else 'L' for i in range(1, n + 1))


classes = sorted({canon(''.join(t)) for n in range(2, 10) for t in product('LR', repeat=n)
                  if 'L' in t and 'R' in t and primitive(''.join(t))}, key=lambda s: (len(s), s))
rev_sym = [w for w in classes if canon(w[::-1]) == w]
chris = sorted({canon(christoffel(p, n - p)) for n in range(2, 10) for p in range(1, n) if gcd(p, n - p) == 1},
               key=lambda s: (len(s), s))
lines = [
    f"primitive positive classes, length 2..9: {len(classes)}",
    f"reversal-symmetric up to conjugacy: {len(rev_sym)}",
    f"Christoffel classes, length 2..9: {len(chris)}",
    f"Christoffel classes that are reversal-symmetric: {sum(1 for w in chris if canon(w[::-1]) == w)} of {len(chris)}",
    f"shortest classes that are not: {[w for w in classes if canon(w[::-1]) != w and len(w) <= 7]}",
    f"B1720's best thread L^5RLR^2 = LLLLLRLRR reversal-symmetric: {canon('LLLLLRLRR'[::-1]) == canon('LLLLLRLRR')}",
    f"L^5R^2 = LLLLLRR reversal-symmetric: {canon('LLLLLRR'[::-1]) == canon('LLLLLRR')}",
]
print("\n".join(lines))
(HERE / "christoffel_cp_run.txt").write_text("\n".join(lines) + "\n")
