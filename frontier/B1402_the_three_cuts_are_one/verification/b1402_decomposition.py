#!/usr/bin/env python3
"""L208: are the three arithmetic cuts of the metallic family one structure?  They are.

  B996  : the mod-3 shadow <R^m, L^m> in SL(2,Z/3) is the full 2T (order 24) iff 3 does not
          divide m; when 3|m it degenerates to the identity.
  B997  : the SHADOW MODULUS m^2+4 is a McKay order only at m = 1 (it equals 5, and 5 is PRIME,
          so the shadow IS SL(2,Z/5) = 2I).  [B1002: "conductor" is two quantities; this is the
          shadow modulus, not B675's cusp-order conductor.]
  B1349 : the theta-even readout is EAR-INDEPENDENT iff gcd(m,15) > 1.
  B1349 addendum 6 : on that branch the forced value leaves Q iff 5 | (m^2+4), i.e. m = +-1 mod 5.

CLAIM TO TEST:  gcd(m,15) > 1  <=>  (3|m) OR (5|m)  <=>  (B996-degenerate) OR (5|m),
so B1349's cut DECOMPOSES into B996's cut and a 5-part -- and the two parts carry DIFFERENT
readouts.
"""
import math
import numpy as np

# --- B996's mod-3 shadow, recomputed independently -------------------------------------
R3 = np.array([[1, 1], [0, 1]], dtype=int)
L3 = np.array([[1, 0], [1, 1]], dtype=int)
def mp(M, k, n=3):
    P = np.eye(2, dtype=int)
    for _ in range(k):
        P = (P @ M) % n
    return P
def gen_order(gens, n=3):
    seen = {tuple(np.eye(2, dtype=int).flatten() % n)}
    frontier = [np.eye(2, dtype=int) % n]
    while frontier:
        nxt = []
        for X in frontier:
            for g in gens:
                Y = (X @ g) % n
                k = tuple(Y.flatten())
                if k not in seen:
                    seen.add(k); nxt.append(Y)
        frontier = nxt
    return len(seen)

print("=" * 90)
print("B996 RECOMPUTED: order of the mod-3 shadow <R^m, L^m>")
print("=" * 90)
b996 = {}
for m in range(1, 16):
    o = gen_order([mp(R3, m), mp(L3, m)])
    b996[m] = o
    tag = "FULL 2T" if o == 24 else ("degenerate" if o == 1 else f"order {o}")
    print(f"  m={m:2d}: |<R^m, L^m> mod 3| = {o:3d}   {tag}"
          f"   {'(3|m)' if m % 3 == 0 else ''}")
assert [m for m in range(1, 8) if b996[m] == 24] == [1, 2, 4, 5, 7], "B996's own list m=1..7"
assert all((b996[m] == 1) == (m % 3 == 0) for m in range(1, 16))
print("\n  B996's stated list for m=1..7 (24,24,1,24,24,1,24) REPRODUCES.")
print("  LAW: the mod-3 shadow degenerates exactly when 3 | m.")

print()
print("=" * 90)
print("THE DECOMPOSITION")
print("=" * 90)
LAM = {3: 0.5, 5: 0.0, 6: -1/(2*(1+5**0.5)/2), 9: -1/(2*(1+5**0.5)/2),
       10: 0.0, 12: 0.5, 15: 1.0}
print(f"  {'m':>3} {'gcd(m,15)':>10} {'3|m (B996)':>12} {'5|m':>6} {'ear-indep':>10} {'lambda':>12} {'m^2+4':>7} {'5|m^2+4':>8}")
ok = True
for m in range(1, 16):
    g = math.gcd(m, 15)
    ei = g > 1
    dec = (m % 3 == 0) or (m % 5 == 0)
    ok &= (ei == dec)
    lam = f"{LAM[m]:+.6f}" if m in LAM else "-- (branch B)"
    print(f"  {m:>3} {g:>10} {str(m%3==0):>12} {str(m%5==0):>6} {str(ei):>10} {lam:>12}"
          f" {m*m+4:>7} {str((m*m+4)%5==0):>8}")
print(f"\n  gcd(m,15) > 1  <=>  (3|m) OR (5|m)  :  {ok}")
assert ok

print()
print("=" * 90)
print("AND THE TWO PARTS CARRY DIFFERENT READOUTS")
print("=" * 90)
only3 = [m for m in LAM if m % 3 == 0 and m % 5 != 0]
only5 = [m for m in LAM if m % 5 == 0 and m % 3 != 0]
both = [m for m in LAM if m % 15 == 0]
print(f"  3|m only (B996-degenerate): m = {only3}  ->  lambda in {sorted({round(LAM[m],9) for m in only3})}")
print(f"  5|m only                  : m = {only5}  ->  lambda in {sorted({round(LAM[m],9) for m in only5})}")
print(f"  15|m (both)               : m = {both}  ->  lambda in {sorted({round(LAM[m],9) for m in both})}")
assert all(abs(LAM[m]) > 1e-9 for m in only3), "the 3-part must be non-silent"
assert all(abs(LAM[m]) < 1e-9 for m in only5), "the 5-part must be silent"
print()
print("  => THE 3-PART (B996's degenerate grammars) CARRIES THE NONTRIVIAL FORCED VALUES,")
print("     including the golden -1/(2phi).  THE 5-PART IS SILENT (lambda = 0).  BOTH -> 1.")
print("  => and within the 3-part, golden iff m = +-1 mod 5 (addendum 6 / B997's prime 5):")
for m in only3:
    print(f"       m={m:2d}: m mod 5 = {m%5}, 5|m^2+4 = {str((m*m+4)%5==0):5s} -> lambda = {LAM[m]:+.6f}")
