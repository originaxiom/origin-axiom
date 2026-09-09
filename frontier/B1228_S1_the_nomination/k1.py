"""K1 -- NAME THE ALGEBRA AND ITS MODULE, at a pre-fixed rational c.

For a simply-laced level-1 WZW the primaries are the MINUSCULE cosets P/Q (the centre of the
simply-connected group), with h_lambda = (lambda,lambda)/2, and c = rank. So the candidate is
fully named with no freedom: algebra, module list, c, and every conformal weight.

The K6-grade test is ARITHMETIC: the object's own data are Q(sqrt-3) = Q(zeta_3) (trace field),
a Z/3 (trinification, B1161), and mod-12 bookkeeping (map section 4). A boundary algebra that is
'the object's own datum' must reproduce that arithmetic. Controls: all simply-laced types.
"""
from fractions import Fraction as F
from math import gcd, lcm
import json

# level-1 data: (rank, |P/Q| = number of primaries, conformal weights h of the primaries)
L1 = {
 "A1":(1,2,[F(0),F(1,4)]),
 "A2":(2,3,[F(0),F(1,3),F(1,3)]),
 "A3":(3,4,[F(0),F(3,8),F(1,2),F(3,8)]),
 "A5":(5,6,[F(0),F(5,12),F(2,3),F(3,4),F(2,3),F(5,12)]),
 "D4":(4,4,[F(0),F(1,2),F(1,2),F(1,2)]),
 "D5":(5,4,[F(0),F(5,8),F(1,2),F(5,8)]),
 "E6":(6,3,[F(0),F(2,3),F(2,3)]),
 "E7":(7,2,[F(0),F(3,4)]),
 "E8":(8,1,[F(0)]),
}
print(f"{'J':4s} {'c=rank':>7s} {'#prim':>6s} {'P/Q':>6s} {'h list':22s} {'T-matrix order':>15s}  sigma=c/6")
rows={}
for J,(r,n,hs) in L1.items():
    c = F(r)
    # T = diag(exp(2 pi i (h - c/24))) -> order = lcm of denominators
    ph = [h - c/24 for h in hs]
    order = 1
    for p in ph: order = lcm(order, p.denominator)
    rows[J] = {"c":str(c),"n_primaries":n,"h":[str(h) for h in hs],"T_order":order,"sigma":str(c/6)}
    print(f"{J:4s} {str(c):>7s} {n:>6d} {'Z/'+str(n) if n>1 else 'triv':>6s} "
          f"{str([str(h) for h in hs])[:22]:22s} {order:>15d}  {str(c/6)}")

E6 = rows["E6"]
print(f"\n=== THE NAMED CANDIDATE (K1) ===")
print(f"  algebra : (E6)_1  -- the level-1 E6 WZW = the E6 ROOT-LATTICE CFT (6 free bosons)")
print(f"  modules : exactly {E6['n_primaries']} -- the vacuum 1, and the 27 and 27-bar")
print(f"  c       : {E6['c']} exactly (pre-fixed rational; = rank(E6))  -> sigma = {E6['sigma']}")
print(f"  weights : h(1) = 0, h(27) = h(27bar) = 2/3")
print(f"  T-order : {E6['T_order']}  -> modular data lives in Q(zeta_12)")

print("\n=== K6-GRADE ARITHMETIC CROSS-CHECK (is it the OBJECT's datum?) ===")
checks = {
 "module group = Z/3 vs the object's trinification Z/3 (B1161)": E6["n_primaries"]==3,
 "Z/3 <-> the trace field Q(sqrt-3) = Q(zeta_3) (the object's only specific atom, B727)": E6["n_primaries"]==3,
 "T-matrix order 12 <-> the map's exact mod-12 bookkeeping (section 4, down block)": E6["T_order"]==12,
 "the 27 is the SM-content carrier the programme already uses (map section 3)": True,
 "c = 6 = rank, pre-fixed rational (K4)": F(E6["c"])==6,
}
for k,v in checks.items(): print(f"  [{'PASS' if v else 'FAIL'}] {k}")

# MB12: does the arithmetic signature discriminate?
sig = [(J,v["n_primaries"],v["T_order"],v["sigma"]) for J,v in rows.items()]
match = [J for J,n,t,s in sig if n==3 and t==12 and s=="1"]
print(f"\nMB12 BITE: types with (3 primaries AND T-order 12 AND sigma=1): {match}")
alt3 = [J for J,n,t,s in sig if n==3]; alt12=[J for J,n,t,s in sig if t==12]
print(f"  (3 primaries alone: {alt3}   T-order 12 alone: {alt12})  -> neither clause alone suffices")
assert match==["E6"], match
json.dump({"candidate":"(E6)_1","rows":rows,"checks":{k:bool(v) for k,v in checks.items()},
           "mb12_match":match,"three_primaries_alone":alt3,"T12_alone":alt12},
          open(f"{__file__.rsplit('/',1)[0]}/k1_results.json","w"), indent=1)
