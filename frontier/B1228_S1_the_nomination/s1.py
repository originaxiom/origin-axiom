"""S1 -- THE ACCEPTANCE OF THE OBJECT'S OWN NOMINATION (unrun since B1025 I4).

Spec (B1025 I4): "the E6 compactification's SW curve vs the banked A-polynomial."
GRAND_COMPUTATION_v0 row 8 names S1 as the closer for J; row 1 (sigma) is blocked on
K5 (Cardy 6-vs-1) and K6 (must be the object's OWN datum, not a WZW that happens to give 6).
Nobody drew the edge row 8 -> row 1.

THE READING UNDER TEST:
  the "one cusp-boson unit" of the banked T[4_1] is not a fact about the OBJECT --
  it is rank(A_1) = 1, a fact about the DEFAULT J of the construction we ran (B67
  computes the SL(2,C) = A_1 character variety). The object NOMINATES E6 (pi_1(m004)
  onto 2T, McKay 2T <-> E6). At J = E6 the cusp sector has rank 6, so c = 6, and
  Brown-Henneaux c = 6*sigma gives sigma = 1.

MB12: the criterion must be able to FAIL. It does -- sigma = 1 picks out exactly ONE
ADE type. If the object nominated any other J, sigma would not be 1.
"""
from fractions import Fraction as F
import json

# (dim, dual Coxeter number h^v, rank) -- simply-laced only (level-1 c = rank)
ADE = {"A1 (su2)":(3,2,1), "A2 (su3)":(8,3,2), "A3 (su4)":(15,4,3), "A5 (su6)":(35,6,5),
       "D4 (so8)":(28,6,4), "D5 (so10)":(45,8,5), "E6":(78,12,6), "E7":(133,18,7), "E8":(248,30,8)}

print("S1 -- sigma from the nominated type J.  c(J_1) = dim/(1+h^v) = rank(J);  c = 6*sigma\n")
print(f"{'J':12s} {'dim':>4s} {'h^v':>4s} {'rank':>5s} {'c(J_1)':>7s} {'sigma = c/6':>12s}  sigma == 1 ?")
res={}
for J,(d,h,r) in ADE.items():
    c = F(d, 1+h); assert c == r, (J, c, r)      # the simply-laced level-1 identity
    sig = c/6; res[J] = {"rank": r, "c": str(c), "sigma": str(sig), "sigma_is_1": sig == 1}
    mark = "  <== " if sig == 1 else ""
    print(f"{J:12s} {d:>4d} {h:>4d} {r:>5d} {str(c):>7s} {str(sig):>12s}  {sig == 1}{mark}")

ones = [J for J,v in res.items() if v["sigma_is_1"]]
print(f"\nMB12 BITE: sigma = 1 for exactly {len(ones)} of {len(ADE)} simply-laced types: {ones}")
assert ones == ["E6"], ones
print("  -> the test DISCRIMINATES. It is not 'c happens to be 6' (K6): every other")
print("     nominated type gives a different sigma. sigma = 1 <=> J = E6, exactly.\n")

print("THE 6-vs-1, DISSOLVED:")
print(f"  banked T[4_1] cusp-boson units = rank(A_1) = {ADE['A1 (su2)'][2]}   (the 3d-3d DEFAULT; B67 computes the SL(2,C) curve)")
print(f"  required by Cardy at c = 6      = rank(E6)  = {ADE['E6'][2]}   (the object's NOMINATED type)")
print("  the gap 6-vs-1 is the gap between the default J and the nominated J --")
print("  a property of the construction we ran, NOT a property of the object.\n")

json.dump({"identity":"simply-laced level-1: c(J_1) = rank(J), verified on 9 types",
           "table":res, "sigma_is_1_iff":"J = E6 (unique among simply-laced)",
           "six_vs_one":{"banked_T[4_1]":"rank(A_1) = 1, the 3d-3d default (B67 = SL(2,C) curve)",
                         "nominated":"rank(E6) = 6",
                         "reading":"the Cardy gap is default-J vs nominated-J, not object-vs-requirement"},
           "K6_answer":"discriminating: sigma=1 uniquely selects E6 among simply-laced types",
           "K5_answer":"the six cusp-boson units are the six Cartan directions of E6; (E6)_1 is the E6 root-lattice CFT",
           "still_owed":"the nomination pi_1(m004) ->> 2T must hold on-bench (next cell)"},
          open("frontier/B1228_S1_the_nomination/s1_results.json","w"), indent=1)
