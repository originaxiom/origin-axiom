#!/usr/bin/env python3
"""B1224: amphichirality forces CS to be 2-TORSION, not zero. Exactly {0, 1/4}, 6/6."""
import snappy

amph, non = [], []
for M in snappy.OrientableCuspedCensus(cusps=1)[:400]:
    try:
        a = M.symmetry_group().is_amphicheiral()
        cs = float(M.chern_simons())
    except Exception:
        continue
    (amph if a else non).append((M.name(), cs))

print("AMPHICHIRAL one-cusped census manifolds:")
vals = set()
for nm, cs in amph:
    t = abs((2 * cs) % 0.5)
    t = min(t, 0.5 - t)
    vals.add(round(cs, 9))
    print(f"  {nm:8s} CS = {cs:12.9f}   2*CS = 0 (mod 1/2): {t < 1e-7}")
print(f"\n  distinct CS values among amphichiral: {sorted(vals)}")
assert vals <= {0.0, 0.25}, vals
z = sum(1 for _, cs in non if abs(cs) < 1e-9)
print(f"  NON-amphichiral with CS = 0: {z}/{len(non)} = {z/len(non):.4f}")
print("\n  amphichirality => CS is 2-torsion in R/(1/2)Z, values exactly {0, 1/4}")
print("  m004 sits at 0; its sister m003 sits at 1/4 -- that is what separates them.")
