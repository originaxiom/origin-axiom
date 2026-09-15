#!/usr/bin/env python3
"""THE HYPERBOLIC Zhat, DERIVED -- not fitted.

Sources (Gukov-Manolescu arXiv:1904.06057v2, read on-bench):
  Thm 1.2   Zhat_a(Y_{p/r}) = eps q^d L^{(a)}_{p/r}[ (x^{1/2r} - x^{-1/2r}) F_K(x,q) ]
  eq (1)    L^{(a)}_{p/r}: x^u q^v -> q^{-(r/p)u^2} q^v   if  ru - a in pZ, else 0
  sec 6.8   Spin^c labels:  a in Z + (r+1)/2  (mod pZ)      <-- the convention that unlocks it
  eq (11)   F_{4_1} = 1/2(Xi(x,q) - Xi(1/x,q)),  Xi = sum_k Xi_k(q) x^{k-1/2}
  eq (13)   Zhat_0(S^3_{-1/2}(4_1)) -- the target, ten published coefficients

For p/r = -1/2:  p = -1, r = 2.  a in Z + 3/2, so a = 1/2 mod 1, and the selection rule
2u - a in Z forces u in Z/2 + 1/4 -- which is exactly what (x^{1/4} - x^{-1/4})*x^{k-1/2}
produces.  (Taking a = 0 kills every term; that was the earlier error.)

Gate 5: q-series arithmetic only.
"""
from fractions import Fraction as Fr
import math

XI = [[1], [2], [1,3,1], [2,2,5,2,2]]          # eq (11) coefficient lists, symmetric in q
GIVEN = {0:1, 1:-1, 3:2, 6:-2, 9:1, 10:3, 11:1, 14:-1, 15:-3, 16:-1}   # eq (13)
p, r = -1, 2

print("DERIVED PLACEMENT")
base = None; centres = []
for k in range(1, 8):
    u1, u2 = Fr(k) - Fr(1,4), Fr(k) - Fr(3,4)
    e1, e2 = -Fr(r,p)*u1*u1, -Fr(r,p)*u2*u2
    if base is None: base = min(e1, e2)
    centres.append((k, e2-base, e1-base, e1-e2))
    print(f"   k={k}:  centre {str(e2-base):>4}   negative centre {str(e1-base):>4}   separation {e1-e2} = 2k-1")
print(f"\n   C_k = (2k-1)(k-1) = {[(2*k-1)*(k-1) for k in range(1,8)]}")

pred = {}
for k in (1,2,3,4):
    C = (2*k-1)*(k-1); blk = XI[k-1]; w = len(blk)//2
    for i, c in enumerate(blk):
        off = i - w
        pred[C+off]        = pred.get(C+off, 0) + c
        pred[C+(2*k-1)+off] = pred.get(C+(2*k-1)+off, 0) - c

print("\nVERIFICATION against the ten published coefficients of eq (13)")
ok = True
for e in sorted(GIVEN):
    m = pred.get(e) == GIVEN[e]; ok &= m
    print(f"   q^{e:<3} published {GIVEN[e]:>3}   derived {pred.get(e,0):>3}   {'ok' if m else 'MISMATCH'}")
print(f"\n   ALL TEN REPRODUCED FROM THE DERIVATION: {ok}")
print(f"   (the earlier 'fit' s_k = 3k(k-1)/2 measured each block's LEFT EDGE;")
print(f"    the derivation gives its CENTRE -- 9 vs 10 was edge vs centre of a width-3 block)")
print(f"\n   PREDICTION, no data behind it: block 4 = {XI[3]} centred at 21 (q^19..q^23),")
print(f"   negated centred at 28 (q^26..q^30).")

phi = (1+5**0.5)/2; lp = math.log(phi)
c = 3*lp*lp/math.pi**2
print("\n" + "="*70)
print("GROWTH, from the DERIVED positions")
print("="*70)
print("   block k: mass F(2k-1) ~ phi^{2k}/sqrt5  at  C_k = (2k-1)(k-1) ~ 2k^2")
print("   n ~ 2k^2  =>  k ~ sqrt(n/2)  =>  log|a_n| ~ sqrt(2) log(phi) sqrt(n)")
print("   Cardy  log a_n ~ 2 pi sqrt(c_eff n/6)  gives")
print(f"\n      c_eff = 3 (log phi)^2 / pi^2 = {c:.9f}\n")
print(f"   SUPERSEDES memo 175's 4(log phi)^2/pi^2 = {4*lp*lp/math.pi**2:.9f},")
print(f"   which came from the mis-anchored (left-edge) fit.")
print(f"\n   target c((E6)_1) = 6.   Ratio: {6/c:.1f}x.")
