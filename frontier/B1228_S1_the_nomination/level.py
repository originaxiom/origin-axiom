"""K1's last gap: WHY LEVEL 1? -- and the object answers it with its own blindness theorem.

A WZW chiral algebra needs TWO data: the Lie type J, and the LEVEL k.
  * the object supplies J        -- pi_1(m004) ->> 2T, McKay 2T <-> E6 (verified, cell 2)
  * the object supplies NO k     -- CS = 0 => dS/dk = -CS = 0 identically (B1012/B1088);
                                    'the object is provably blind to the quantized level k'
                                    and CS = 0 is forced 2-torsion + at-zero (B1224/B1227, today)

At level 1 a simply-laced WZW IS the lattice VOA of the root lattice: the algebra is determined
by the LATTICE ALONE, with no level datum. At k > 1 the level is extra input.
So k = 1 is the ONLY level the object can supply -- not a choice, an inventory fact.
"""
from fractions import Fraction as F
import json

DIM, HV, RANK = 78, 12, 6
def c_of(k): return F(k*DIM, k+HV)

print("what a WZW needs:   (J, k).   what the object has:\n")
print("  J = E6      : SUPPLIED   -- pi_1(m004) ->> 2T (48 surjections on-bench), McKay 2T <-> E6")
print("  k           : NOT SUPPLIED -- CS = 0 => dS/dk = -CS = 0 identically (B1012/B1088);")
print("                the object is blind to the level. CS = 0 itself is forced: amphichirality")
print("                gives 2-torsion {0, 1/4} and m004 sits at 0 (B1224 / B1227, today).\n")
print(f"{'k':>3s} {'c = k*78/(k+12)':>18s} {'sigma = c/6':>12s}  needs a level datum the object lacks?")
for k in range(1,7):
    c=c_of(k); print(f"{k:>3d} {str(c):>18s} {str(c/6):>12s}  {'NO -- lattice VOA, level is implicit' if k==1 else 'YES'}")
print(f"\n  only k = 1 needs no level input: the level-1 simply-laced WZW IS the E6 ROOT-LATTICE VOA,")
print(f"  determined by the lattice alone. The object supplies exactly a lattice and no level.")
print(f"  => k = 1 is forced by INVENTORY, not chosen.\n")

c1=c_of(1); sigma=c1/6
print("THE CHAIN, end to end:")
steps=[("m004 amphichiral => CS in {0,1/4}, and m004 sits at 0","B1224 / B1227 (today)"),
       ("CS = 0 => dS/dk = -CS = 0 => blind to the level k","B1012 / B1088"),
       ("no k available => the only supplyable level is k = 1 (lattice VOA)","this cell"),
       ("pi_1(m004) ->> 2T, McKay => J = E6","verified on-bench, 48 surjections"),
       ("(E6)_1 => c = rank(E6) = 6 exactly","simply-laced level-1 identity, 9/9"),
       ("Brown-Henneaux c = 6 sigma => sigma = 1","B1088 map section 2.3"),
       ("row 1 of the deletion schedule DELETES","GRAND_COMPUTATION_v0 section 6")]
for i,(s,src) in enumerate(steps,1): print(f"  {i}. {s}\n       [{src}]")
print(f"\n  c = {c1}   sigma = {sigma}   sigma == 1 ? {sigma==1}")

# MB12: if the object were NOT blind to k, sigma would not be pinned
print("\nMB12 BITE -- the blindness is load-bearing, not decorative:")
for k in [1,2,3]:
    print(f"   if the object could supply k = {k}: c = {c_of(k)}, sigma = {c_of(k)/6}  -> sigma {'=' if c_of(k)/6==1 else '!='} 1")
print("   so 'blind to k' is exactly what pins sigma. Remove it and sigma is unpinned again.")
json.dump({"J_supplied":"E6 via pi_1 ->> 2T + McKay","k_supplied":False,
           "why_k1":"level-1 simply-laced WZW = root-lattice VOA: determined by the lattice alone, no level datum",
           "blindness":"CS=0 => dS/dk = -CS = 0 (B1012/B1088); CS=0 forced by amphichirality (B1224/B1227)",
           "c":str(c1),"sigma":str(sigma),"sigma_is_1":sigma==1,
           "mb12":{str(k):str(c_of(k)/6) for k in [1,2,3]}},
          open(f"{__file__.rsplit('/',1)[0]}/level_results.json","w"), indent=1)
