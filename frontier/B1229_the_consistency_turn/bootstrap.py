"""THE OTHER APPROACH: don't DERIVE sigma -- let modular consistency QUANTIZE it.

The whole GRAND_COMPUTATION is a DELETION schedule: kill a row by deriving it from nothing.
That is the hardest possible move (B1216: nine agents, zero deletions). Physics never reduced
its parameter count that way -- it found RELATIONS and CONSISTENCY conditions.

MMS (Mathur-Mukhi-Sen) completely classified two-character RCFTs with vanishing Wronskian
index: SEVEN unitary WZW models, 0 < c < 8, = the Deligne-Cvitanovic exceptional series.
A finite list. Brown-Henneaux (B1088) gives c = 6*sigma. So sigma cannot be any positive real.
"""
from fractions import Fraction as F
import json

# Deligne-Cvitanovic exceptional series at level 1: (dim, h^v)
DELIGNE = {"A1":(3,2),"A2":(8,3),"G2":(14,4),"D4":(28,6),"F4":(52,9),"E6":(78,12),"E7":(133,18)}
# number of primaries (= |P/Q| for simply-laced; G2,F4 are non-simply-laced with 2 primaries)
NPRIM  = {"A1":2,"A2":3,"G2":2,"D4":4,"F4":2,"E6":3,"E7":2}

print("MMS two-character RCFTs (Wronskian index 0) = the Deligne exceptional series:\n")
print(f"{'g':4s} {'dim':>4s} {'h^v':>4s} {'c = dim/(1+h^v)':>16s} {'sigma = c/6':>12s} {'#prim':>6s}")
menu=[]
for g,(d,h) in DELIGNE.items():
    c=F(d,1+h); s=c/6; menu.append((g,c,s,NPRIM[g]))
    print(f"{g:4s} {d:>4d} {h:>4d} {str(c):>16s} {str(s):>12s} {NPRIM[g]:>6d}")

print(f"\nSTEP 1 -- modular consistency alone:")
print(f"  sigma in {{{', '.join(str(s) for _,_,s,_ in menu)}}}")
print(f"  the ONE continuous dimensionless input becomes a FINITE MENU of {len(menu)} values.")
print(f"  R+ (uncountable)  ->  {len(menu)} values.   No derivation used; only consistency.\n")

# STEP 2 -- the object's own arithmetic cuts the menu: it carries Z/3 (trinification B1161,
# trace field Q(zeta_3) = Q(sqrt-3), the only object-specific atom B727).
z3=[(g,c,s) for g,c,s,n in menu if n==3]
print(f"STEP 2 -- the object's Z/3 (trace field Q(sqrt-3); trinification; B727/B1161) keeps only 3-primary theories:")
for g,c,s in z3: print(f"    {g}:  c = {c},  sigma = {s}")
print(f"  sigma in {{{', '.join(str(s) for _,_,s in z3)}}}  -- {len(z3)} values.  sigma is now ONE BIT.\n")

print("THE REDUCTION:  R+  ->  %d (modular consistency)  ->  %d (the object's Z/3)" % (len(menu), len(z3)))
print("  sigma stops being a continuum and becomes a LABEL -- the cheap kind of input the")
print("  map's own section 5 already treats separately ('FINITE menus only').")
print("\nWHAT THIS ASSUMES (stated, not hidden):")
print("  (a) the boundary CFT is a two-character RCFT with vanishing Wronskian index")
print("      -- a RATIONALITY/FINITENESS condition, far weaker than 'derive J';")
print("  (b) Brown-Henneaux c = 6 sigma (B1088, banked, derived twice);")
print("  (c) the Z/3 cut uses the object's arithmetic, not a fitted preference.")
print("  NOT assumed: any choice of the 6d type J. J never enters.")

json.dump({"method":"modular bootstrap / MMS two-character classification -- CONSISTENCY, not derivation",
           "menu":[{"g":g,"c":str(c),"sigma":str(s),"n_primaries":n} for g,c,s,n in menu],
           "step1":"R+ -> %d values by modular consistency alone"%len(menu),
           "step2_Z3_cut":[{"g":g,"sigma":str(s)} for g,c,s in z3],
           "reduction":"R+ -> %d -> %d ; sigma becomes ONE BIT"%(len(menu),len(z3)),
           "assumes":["two-character RCFT, Wronskian index 0","Brown-Henneaux c = 6 sigma (B1088)",
                      "the object's Z/3 (B727/B1161)"],
           "does_not_assume":"any choice of the 6d type J"},
          open(f"{SP if (SP:=__file__.rsplit('/',1)[0]) else '.'}/bootstrap_results.json","w"), indent=1)
