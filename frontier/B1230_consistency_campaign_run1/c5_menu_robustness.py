"""C-5 -- IS THE sigma MENU ROBUST? An adversarial check on B1229's own headline.

B1229 used the MMS two-character (Wronskian index 0) classification -> 7 values. That is a
RESTRICTION. Drop it: allow ANY WZW boundary (any simply-laced G at any level k). Then
c = k*dim(G)/(k+h^v) and sigma = c/6. If MANY (G,k) give sigma = 1, the discrimination B1229
claimed is an artifact of the restriction and the headline weakens.

MB12: this cell is designed to be able to REFUTE B1229's discrimination claim.
"""
from fractions import Fraction as F
import json
G = {"A1":(3,2),"A2":(8,3),"A3":(15,4),"A4":(24,5),"A5":(35,6),"A6":(48,7),"A7":(63,8),
     "D4":(28,6),"D5":(45,8),"D6":(66,10),"D7":(91,12),"E6":(78,12),"E7":(133,18),"E8":(248,30)}
KMAX = 12
hits=[]; allc=set()
for g,(d,h) in G.items():
    for k in range(1,KMAX+1):
        c=F(k*d,k+h); allc.add(c)
        if c/6 == 1: hits.append((g,k,str(c)))
print(f"scanned {len(G)} simply-laced types x levels 1..{KMAX} = {len(G)*KMAX} boundary WZW models")
print(f"distinct central charges produced: {len(allc)}")
print(f"\n(G,k) with sigma = 1  (i.e. c = 6):")
for g,k,c in hits: print(f"   {g} at level {k}:  c = {c}")
print(f"\n  count: {len(hits)}")

if len(hits)==1:
    print("  -> B1229's discrimination SURVIVES the restriction being dropped:")
    print("     c = 6 is reached by exactly one (G,k) in this whole family.")
else:
    print("  -> B1229's discrimination is WEAKENED: c = 6 is reached by several (G,k).")
    print("     The two-character restriction was doing real work; say so.")

# and the robust core: is the menu still DISCRETE without any restriction?
print(f"\nROBUST CORE: every c above is RATIONAL (Anderson-Moore/Vafa holds for any RCFT).")
print(f"  the menu is COUNTABLE and DISCRETE regardless of the two-character restriction.")
print(f"  sigma is never a continuum. That part does not depend on MMS at all.")
json.dump({"scanned":len(G)*KMAX,"distinct_c":len(allc),
           "sigma_1_solutions":[{"G":g,"k":k,"c":c} for g,k,c in hits],
           "discrimination_survives":len(hits)==1,
           "robust_core":"c rational for any RCFT => sigma discrete, independent of MMS"},
          open(f"{__file__.rsplit('/',1)[0]}/c5_results.json","w"),indent=1)
