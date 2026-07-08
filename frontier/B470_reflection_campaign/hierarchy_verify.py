#!/usr/bin/env python3
"""B470 — the breath-hierarchy certification (see BREATH_HIERARCHY.md)."""
import sys
from itertools import product
from math import isqrt

import sympy as sp


def mat(w):
    a, b, c, d = 1, 0, 0, 1
    for ch in w:
        if ch == 'R': a, b, c, d = a, a + b, c, c + d
        else:         a, b, c, d = a + b, b, c + d, d
    return (a, b, c, d)


def revswap(w):
    return "".join('R' if c == 'L' else 'L' for c in reversed(w))


def cyc_eq(w1, w2):
    return len(w1) == len(w2) and w2 in (w1 + w1)


def canonical(w):
    dd = w + w
    return min(dd[i:i + len(w)] for i in range(len(w)))


def rooted_full(w):
    a, b, c, d = mat(w)
    tr = a + d
    if tr < 3: return False
    t = isqrt(tr - 2)
    return t > 0 and t * t == tr - 2 and all(x % t == 0 for x in (a - 1, b, c, d - 1))


def main():
    ok = True
    seen = set()
    full_not_mirror = []
    mirror_unbalanced = 0
    for L in range(2, 14):
        for bits in product('RL', repeat=L):
            w = ''.join(bits)
            if 'R' not in w or 'L' not in w: continue
            cw = canonical(w)
            if cw in seen: continue
            seen.add(cw)
            mirror = cyc_eq(cw, revswap(cw))
            if mirror and cw.count('R') != cw.count('L'): mirror_unbalanced += 1
            if rooted_full(cw) and not mirror: full_not_mirror.append(cw)
    ok &= mirror_unbalanced == 0
    ok &= sorted(full_not_mirror) == ['LLLRLLRRRLRR', 'LLLRRLRRRLLR']
    print(f"word-mirror => balanced: {mirror_unbalanced} violations (expect 0)")
    print(f"genuinely rooted-but-not-word-mirror (len<14): {full_not_mirror} (expect the pair)")
    # balanced strictness witness is manifold-chiral (CS != 0, session SnapPy: -0.0012159)
    w = "RRRLLRLL"
    ok &= w.count('R') == w.count('L') and not cyc_eq(w, revswap(w))
    print(f"{w}: balanced, not word-mirror (manifold CS = -0.0012159, session log) OK")
    # chain roots: exactly the two letters; rungs 2..200 rootless via mod-p QNR
    primes = list(sp.primerange(3, 3000))
    uncert = []
    for target in range(0, 201):
        if target in (0, 1): continue
        certified = False
        for p in primes:
            us = [6 % p, 3 % p, 15 % p]
            for k in range(3, target + 1):
                us.append((us[-1] * us[-2] - us[-3]) % p)
            val = (us[target] - 2) % p
            if val != 0 and sp.jacobi_symbol(val, p) == -1:
                certified = True
                break
        if not certified: uncert.append(target)
    ok &= uncert == []
    print(f"chain rungs 2..200 uncertified-rootless: {uncert} (expect []); "
          f"roots = the two letters (u0-2 = 4 = 2^2, u1-2 = 1 = 1^2)")
    print("ALL CHECKS PASS" if ok else "CHECK FAILURE")
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
