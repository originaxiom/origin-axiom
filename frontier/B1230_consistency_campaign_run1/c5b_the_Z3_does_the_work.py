"""C-5b -- C-5 refuted 'c=6 => E6'. Does the OBJECT'S OWN Z/3 still discriminate,
without leaning on the two-character restriction at all?  Number of primaries of (G)_k:
for level 1 simply-laced it is |P/Q| = |Z(G_simply-connected)|; for A_n level k it is C(n+k, n)."""
from fractions import Fraction as F
from math import comb
import json

CENTRE = {"A1":2,"A2":3,"A3":4,"A4":5,"A5":6,"A6":7,"A7":8,
          "D4":4,"D5":4,"D6":4,"D7":4,"E6":3,"E7":2,"E8":1}
G = {"A1":(3,2),"A2":(8,3),"A3":(15,4),"A4":(24,5),"A5":(35,6),"A6":(48,7),"A7":(63,8),
     "D4":(28,6),"D5":(45,8),"D6":(66,10),"D7":(91,12),"E6":(78,12),"E7":(133,18),"E8":(248,30)}

def nprim(g,k):
    if k == 1: return CENTRE[g]
    if g.startswith("A"): n=int(g[1:]); return comb(n+k, n)
    return None                                  # not needed below

sols=[]
for g,(d,h) in G.items():
    for k in range(1,13):
        if F(k*d,k+h) == 6: sols.append((g,k,nprim(g,k)))
print("the four (G,k) with c = 6, and their primary counts:\n")
print(f"{'G':4s} {'k':>3s} {'#primaries':>11s}   Z/3 (=3 primaries)?")
for g,k,n in sols:
    print(f"{g:4s} {k:>3d} {str(n):>11s}   {n==3}")
keep=[(g,k) for g,k,n in sols if n==3]
print(f"\n  c = 6 alone            -> {len(sols)} solutions: {[(g,k) for g,k,_ in sols]}")
print(f"  c = 6 AND 3 primaries  -> {len(keep)} solution : {keep}")
assert keep==[("E6",1)], keep
print("""
  => THE DISCRIMINATION SURVIVES, and on a BETTER footing than B1229 stated it.
     It was never the two-character restriction doing the work -- it is the OBJECT'S OWN Z/3
     (trace field Q(sqrt-3) = Q(zeta_3); the trinification, B727/B1161). That is exactly what
     K6 demanded: the object's own datum, not a modelling convenience.

  CORRECTION TO B1229 (this campaign refuting its own headline's stated support):
     "sigma = 1 selects E6 uniquely AMONG THE SEVEN TWO-CHARACTER THEORIES" was true but
     leaned on the restriction. The correct statement is stronger and restriction-free:
     among ALL simply-laced (G,k) scanned, c = 6 has FOUR solutions, and the object's Z/3
     cuts them to ONE.
""")
json.dump({"c6_solutions":[{"G":g,"k":k,"n_primaries":n} for g,k,n in sols],
           "after_Z3_cut":[{"G":g,"k":k} for g,k in keep],
           "correction":"the Z/3 does the discriminating, not the two-character restriction",
           "b1229_headline_support_restated":True},
          open(f"{__file__.rsplit('/',1)[0]}/c5b_results.json","w"),indent=1)
