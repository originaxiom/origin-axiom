#!/usr/bin/env python3
"""B550: verify chat-1's Promotion-Sign Conjecture against B111's locked data.

Conjecture: the degree=rank height-1 promotion has sign (-1)^n
(odd n -> consume char(-M^1); even n -> consume char(+M^1)).

Ground truth: B111's exact repo tower (n=3 Lawton Jacobian, n=4 B80
_Jm_n4_exact), height-1 (+M^1, -M^1) surviving multiplicities.
"""
import math

def closed_h1(n):
    return (math.ceil((n-1)/2), math.floor((n-1)/2))

TOWER_EXACT = {3: (0, 1), 4: (1, 1)}   # B111 locked

def conjecture(n):
    p, m = closed_h1(n)
    return (p, m-1) if n % 2 else (p-1, m)

def meridian(n):          # uniform: always consume char(+M^1) = the meridian
    p, m = closed_h1(n)
    return (p-1, m)

if __name__ == '__main__':
    for n in (3, 4):
        ex = TOWER_EXACT[n]
        assert meridian(n) == ex, (n, meridian(n), ex)
        print(f"n={n}: exact {ex} | conjecture {conjecture(n)} "
              f"{'ok' if conjecture(n)==ex else 'FAIL'} | meridian {meridian(n)} ok")
    assert conjecture(3) != TOWER_EXACT[3]      # the refutation
    print(f"\nCONJECTURE REFUTED at n=3: predicts {conjecture(3)}, exact {TOWER_EXACT[3]}")
    print(f"MERIDIAN RULE holds n=3,4; predicts n=5 = {meridian(5)}, n=6 = {meridian(6)}")
    print("n=6 does NOT discriminate (both rules give (2,2)); n=5 is the test.")
