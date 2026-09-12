"""Where is dim S > 0 ?  Half-lives-in-half-dies makes the peripheral image in H_1(M;Q) of rank c,
so dim S = b_1(M) - c.  The deformation proof (B1334) therefore applies exactly when b_1 > c --
a condition a ONE-CUSPED manifold can meet, by having b_1 >= 2.

Scan: every cover of m004 to degree 10 (one-cusped ones included), by (cusps, b_1).
"""
import sys, warnings; sys.path.insert(0,'/tmp/sweep'); warnings.filterwarnings("ignore")
import snappy
from collections import Counter
M0=snappy.Manifold('m004')
tally=Counter(); good=[]
for deg in range(2,11):
    for k,C in enumerate(M0.covers(deg)):
        c=C.num_cusps()
        h=C.homology()
        b=h.betti_number()
        try: amph=C.symmetry_group().is_amphicheiral()
        except Exception: amph=None
        tally[(c,b,b-c)]+=1
        if b>c: good.append((f"d{deg}_{k}",deg,c,b,b-c,amph,str(h)))
    print(f"deg {deg} done, running total with b_1 > cusps: {len(good)}", flush=True)
print("\n(cusps, b_1, dim S = b_1 - c) -> count")
for k in sorted(tally): print("   ",k,"->",tally[k])
print(f"\nCOVERS WITH dim S > 0 (the deformation proof applies): {len(good)}")
print("tag         deg cusps b_1 dimS chiral  H_1")
for g in good: print(f"  {g[0]:10s} {g[1]:3d} {g[2]:4d} {g[3]:4d} {g[4]:4d}  {str(not g[5] if g[5] is not None else '?'):6s} {g[6]}")
onecusp=[g for g in good if g[2]==1]
print(f"\nONE-CUSPED with dim S > 0: {len(onecusp)}")
for g in onecusp: print("   ",g)
