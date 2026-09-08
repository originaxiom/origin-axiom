#!/usr/bin/env python3
"""c_eff OF THE HYPERBOLIC CASE -- Zhat_0(S^3_{-1/2}(4_1)), eq (13) of Gukov-Manolescu.

The authors call these "the first computations of Zhat_a(q) for hyperbolic manifolds in the
literature."  Their coefficients have MIXED SIGNS, so a Cardy estimator cannot be run naively.
This decomposes the series instead, and gets the growth in closed form.

THE DECOMPOSITION (found here; reproduces all ten published coefficients exactly):
    Zhat_0(S^3_{-1/2}(4_1)) = sum_k [ Xi_k at q^{s_k} ]  -  [ Xi_k at q^{s_k + (2k-1)} ]
    where Xi_k is the k-th coefficient of Xi in eq (11) -- a symmetric Laurent polynomial in q --
    and s_k = 3k(k-1)/2.

Gate 5: q-series arithmetic only.
"""
import math

GIVEN = {0:1, 1:-1, 3:2, 6:-2, 9:1, 10:3, 11:1, 14:-1, 15:-3, 16:-1}   # eq (13), as printed
XI    = [[1], [2], [1,3,1], [2,2,5,2,2]]                                # eq (11), coefficient lists
s     = lambda k: 3*k*(k-1)//2

pred = {}
for k in (1,2,3,4):
    blk, st, sh = XI[k-1], s(k), 2*k-1
    for i,c in enumerate(blk):
        pred[st+i]    = pred.get(st+i, 0) + c
        pred[st+sh+i] = pred.get(st+sh+i, 0) - c
ok = all(pred.get(e) == c for e,c in GIVEN.items())
print("VERIFICATION against the ten published coefficients of eq (13)")
for e in sorted(GIVEN):
    print(f"   q^{e:<3} published {GIVEN[e]:>3}   decomposition {pred.get(e,0):>3}   "
          f"{'ok' if pred.get(e)==GIVEN[e] else 'MISMATCH'}")
print(f"   ALL TEN REPRODUCED: {ok}\n")
print(f"   s_k = 3k(k-1)/2 = {[s(k) for k in range(1,8)]}")
print(f"   shift  = 2k-1   = {[2*k-1 for k in range(1,8)]}")
print(f"   Xi_k sums       = {[sum(c) for c in XI]}  = F(2k-1), odd-indexed Fibonacci\n")

print("=" * 72)
print("THE GROWTH, IN CLOSED FORM")
print("=" * 72)
print("   Block k has total mass F(2k-1) ~ phi^{2k}/sqrt5 and sits at position s_k ~ 3k^2/2.")
print("   n ~ 3k^2/2  =>  k ~ sqrt(2n/3)  =>  log|a_n| ~ 2 log(phi) sqrt(2n/3).")
print("   Cardy form  log a_n ~ 2 pi sqrt(c_eff n / 6)  matches with")
phi = (1+5**0.5)/2; lp = math.log(phi)
c = 4*lp*lp/math.pi**2
print(f"\n      c_eff = 4 (log phi)^2 / pi^2 = {c:.9f}\n")
print(f"   log(phi) = {lp:.9f}   (transcendental: phi is algebraic, != 0,1)")
print(f"   The value is not a small rational: nearest tried is 3/32 = 0.09375, off by {abs(c-3/32):.6f},")
print(f"   and there is no reason to expect exact rationality. NOT claimed either way.")
print()
print("=" * 72)
print("EVERY MEASURED c_eff ON THE OBJECT'S SIDE, AND THE TARGET")
print("=" * 72)
print(f"   target      c((E6)_1) = 78/13                     =  6")
print(f"   HYPERBOLIC  S^3_{{-1/2}}(4_1), eq (13)   [this cell] =  {c:.6f}")
print(f"   Brieskorn   -Sigma(2,3,7), eq (12) mock theta      =  0.142410  (~ 1/7)")
print(f"   Brieskorn    Sigma(2,3,7), Prop 4.8 false theta    =  0")
print(f"   GC-6's substitute (eta^-1 free boson, NOT measured) =  1")
print()
print(f"   The hyperbolic case -- the one that matters -- is {6/c:.1f}x below the target,")
print("   and its growth rate is set by the GOLDEN RATIO, not by a rational level.")
print("   A rational CFT has rational c_eff. Nothing here looks rational.")
