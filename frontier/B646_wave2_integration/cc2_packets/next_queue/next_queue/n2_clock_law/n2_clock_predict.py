"""N2 — THE CLOCK LAW: apply the sealed H-R2 kill rule (sha 0982d8e0, verbatim, zero
refit) to all 19 banked rungs: E6 k=1..7 and SU(3) k=1..12. Predictions print BEFORE
the banked comparison (PREREG_N2.md, seal 8393e404).

Rule: n = ord(T_k); CRT n = prod p^a; killed components = split primes (p = 1 mod 3)
and deep 3-powers (a >= 3); clock_pred = min{ d | ord(A1 mod n) : A1^d = I at every
surviving component and = +-I at every killed component }.
"""
import sys, math
from fractions import Fraction
from functools import reduce

sys.path.insert(0, '<cc2-seat>/seat-work/level_ladder_campaign/scripts')
sys.path.insert(0, '<cc2-seat>/seat-work/veins/v7_conduit')
import numpy as np
from engine import enumerate_level_weights, HVEE, Cinv3, C6
from engine_v7 import An_Level

A1 = [[2, 1], [1, 1]]

def mat_mod(M, m):
    return tuple(x % m for row in M for x in row)

def mat_mul_mod(X, Y, m):
    return [[(X[0][0]*Y[0][0]+X[0][1]*Y[1][0]) % m, (X[0][0]*Y[0][1]+X[0][1]*Y[1][1]) % m],
            [(X[1][0]*Y[0][0]+X[1][1]*Y[1][0]) % m, (X[1][0]*Y[0][1]+X[1][1]*Y[1][1]) % m]]

def mat_pow_mod(M, e, m):
    R = [[1 % m, 0], [0, 1 % m]]
    B = [[x % m for x in row] for row in M]
    while e:
        if e & 1:
            R = mat_mul_mod(R, B, m)
        B = mat_mul_mod(B, B, m)
        e >>= 1
    return R

def ord_mod(M, m, cap=10**6):
    if m == 1:
        return 1
    I = mat_mod([[1, 0], [0, 1]], m)
    P = [[x % m for x in row] for row in M]
    cur = [row[:] for row in P]
    for j in range(1, cap):
        if mat_mod(cur, m) == I:
            return j
        cur = mat_mul_mod(cur, P, m)
    raise RuntimeError(f"order cap exceeded mod {m}")

def factorize(n):
    f, d = {}, 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f

def divisors(n):
    ds = [1]
    for p, a in factorize(n).items():
        ds = [d * p**e for d in ds for e in range(a + 1)]
    return sorted(ds)

def e6_ordT(k):
    K = k + HVEE
    PRIM = enumerate_level_weights(k)
    lam3 = (Cinv3 @ np.array(PRIM, dtype=np.int64).T).T
    rho3 = Cinv3 @ np.ones(6, dtype=np.int64)
    r = np.array([int(la @ C6 @ (la + 2 * rho3)) for la in lam3])
    assert (r % 3 == 0).all()
    r = r // 3
    expo = (2 * r - 39 * k) % (12 * K)
    g = reduce(math.gcd, [int(e) for e in expo], 12 * K)
    return (12 * K) // g

def su3_ordT(k):
    L = An_Level(3, k, name=f"SU(3)_{k}")
    return reduce(lambda a, b: a * b // math.gcd(a, b),
                  [(h - L.c / 24).limit_denominator(10**9).denominator for h in L.h], 1)

def predict(n):
    fac = factorize(n)
    comps = sorted(p**a for p, a in fac.items())
    killed = [p**a for p, a in fac.items()
              if (p % 3 == 1 and p != 3) or (p == 3 and a >= 3)]
    N = ord_mod(A1, n)
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
            return N, comps, killed, d
    raise RuntimeError("no divisor found")

# k=4 entry verified from disk (outputs/level4_readouts.json: order 12; the seal's
# "faithful at k=3,4,5" concurs) — an earlier in-context transcription said 36, wrongly.
BANKED_E6 = {1: 1, 2: 4, 3: 60, 4: 12, 5: 36, 6: 18, 7: 36}
BANKED_ORDT_E6 = {1: 12, 2: 84, 3: 180, 4: 48, 5: 204, 6: 108, 7: 228}
BANKED_SU3 = {1: 1, 2: 10, 3: 12, 4: 8, 5: 12, 6: 36, 7: 60, 8: 20, 9: 12, 10: 28, 11: 24, 12: 60}

rows = []
print("=== PREDICTIONS (printed before any banked comparison) ===", flush=True)
for fam, ks, ordT_fn in (("E6", range(1, 8), e6_ordT), ("SU3", range(1, 13), su3_ordT)):
    for k in ks:
        n = ordT_fn(k)
        N, comps, killed, pred = predict(n)
        rows.append((fam, k, n, N, comps, killed, pred))
        print(f"{fam} k={k:2d}: ord(T)={n:4d} = {comps}  killed={killed or '-'}  "
              f"ord(A1 mod n)={N:4d}  ->  clock_pred={pred}", flush=True)

print("\n=== COMPARISON WITH BANKED ===", flush=True)
hits = 0
for fam, k, n, N, comps, killed, pred in rows:
    banked = (BANKED_E6 if fam == "E6" else BANKED_SU3)[k]
    if fam == "E6":
        gate = BANKED_ORDT_E6[k]
        assert n == gate, f"ord(T) gate FAILED at E6 k={k}: {n} != {gate}"
    mark = "MATCH" if pred == banked else f"** MISMATCH (banked {banked}) **"
    hits += pred == banked
    print(f"{fam} k={k:2d}: pred={pred:4d} banked={banked:4d}  {mark}", flush=True)
    if pred != banked:
        print(f"    diagnostics: A1^{banked} mod components:", flush=True)
        for q in comps:
            P = mat_pow_mod(A1, banked, q)
            tag = ("I" if mat_mod(P, q) == mat_mod([[1,0],[0,1]], q)
                   else "-I" if mat_mod(P, q) == mat_mod([[-1,0],[0,-1]], q) else f"{P}")
            print(f"      mod {q}: {tag}", flush=True)
print(f"\nTOTAL: {hits}/19 rule-derived (E6 ord(T) gates all passed)", flush=True)
