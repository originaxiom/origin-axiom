"""Q2 (a)+(b): odd-block conductors c_odd for all rungs; re-derive the clock law with
n = c_odd; verdicts on P-Q2-a (E6 k=2 conductor drop to 21) and P-Q2-b (consistency).
Prereg 287bfe86 sealed first."""
import sys, math
from fractions import Fraction
from functools import reduce

sys.path.insert(0, '/Users/dri/oa-seat-cc2/seat-work/level_ladder_campaign/scripts')
sys.path.insert(0, '/Users/dri/oa-seat-cc2/seat-work/veins/v7_conduit')
sys.path.insert(0, '/Users/dri/oa-seat-cc2/seat-work/next_queue/n2_clock_law')
import numpy as np
from engine import enumerate_level_weights, theta_split, HVEE, Cinv3, C6
from engine_v7 import An_Level
from n2_clock_predict import (A1, ord_mod, factorize, divisors, mat_pow_mod, mat_mod,
                              BANKED_E6, BANKED_SU3)

def lcmm(vals):
    return reduce(lambda a, b: a * b // math.gcd(a, b), vals, 1)

def e6_texpo(k):
    K = k + HVEE
    PRIM = enumerate_level_weights(k)
    lam3 = (Cinv3 @ np.array(PRIM, dtype=np.int64).T).T
    rho3 = Cinv3 @ np.ones(6, dtype=np.int64)
    r = np.array([int(la @ C6 @ (la + 2 * rho3)) for la in lam3])
    assert (r % 3 == 0).all()
    expo = (2 * (r // 3) - 39 * k) % (12 * K)
    fixed, pairs = theta_split(PRIM)
    return expo, fixed, pairs, 12 * K

def e6_conductors(k):
    expo, fixed, pairs, M = e6_texpo(k)
    full = M // reduce(math.gcd, [int(e) for e in expo], M)
    paired = [int(expo[a]) for a, b in pairs]
    for a, b in pairs:
        assert expo[a] == expo[b], "theta must preserve T"
    c_odd = lcmm([M // math.gcd(M, e if e else M) for e in paired]) if paired else 1
    return full, c_odd

def su3_conductors(k):
    L = An_Level(3, k, name=f"SU(3)_{k}")
    exps = [(h - L.c / 24) for h in L.h]
    full = lcmm([e.limit_denominator(10**9).denominator for e in exps])
    fixed, pairs = L.theta_split()
    for a, b in pairs:
        assert exps[a] == exps[b]
    c_odd = lcmm([exps[a].limit_denominator(10**9).denominator for a, b in pairs]) if pairs else 1
    return full, c_odd

def clock_with(n, stage):
    """Stage-typed law at conductor n: E-type kills split primes + deep 3-powers;
    A-type kills nothing (=> clock = ord(A1 mod n))."""
    N = ord_mod(A1, n) if n > 1 else 1
    if stage == 'A':
        return N
    fac = factorize(n)
    comps = sorted(p**a for p, a in fac.items())
    killed = [p**a for p, a in fac.items() if (p % 3 == 1 and p != 3) or (p == 3 and a >= 3)]
    for d in divisors(N):
        ok = True
        for q in comps:
            P = mat_pow_mod(A1, d, q)
            if mat_mod(P, q) == mat_mod([[1, 0], [0, 1]], q):
                continue
            if q in killed and mat_mod(P, q) == mat_mod([[-1, 0], [0, -1]], q):
                continue
            ok = False
            break
        if ok:
            return d
    raise RuntimeError

print("rung        ord(T)  c_odd   drop?  clock(c_odd-law)  banked  verdict")
breaks = 0
for k in range(1, 9):
    full, c_odd = e6_conductors(k)
    pred = clock_with(c_odd, 'E')
    banked = BANKED_E6.get(k)
    mark = "MATCH" if banked == pred else ("**BREAK**" if banked is not None else "PRED(Q1)")
    breaks += (banked is not None and banked != pred)
    print(f"E6  k={k:2d}:  {full:5d}  {c_odd:5d}   {'YES' if c_odd < full else 'no '}"
          f"    {pred:4d}             {banked if banked is not None else '--':>4}   {mark}")
for k in range(1, 14):
    full, c_odd = su3_conductors(k)
    pred = clock_with(c_odd, 'A')
    banked = BANKED_SU3.get(k, 12 if k == 13 else None)
    mark = "MATCH" if banked == pred else "**BREAK**"
    breaks += (banked != pred)
    print(f"SU3 k={k:2d}:  {full:5d}  {c_odd:5d}   {'YES' if c_odd < full else 'no '}"
          f"    {pred:4d}             {banked:>4}   {mark}")
print(f"\nP-Q2-a: c_odd(E6,2) — see row (sealed prediction 21)")
print(f"P-Q2-b: breaks = {breaks} (sealed: must be 0 at k>=3 rungs; "
      f"k<=2 rungs now carry the law's own verdicts)")
