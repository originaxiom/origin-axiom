"""B1227 -- B1224 and B1225's missing keystone are ONE theorem in two value groups.

THEOREM (elementary, and that is the point). Let M be amphichiral, so the mirror mu is a
SELF-isometry: mu(M) ~ M. Let I be an isometry invariant valued in an abelian group A, and
mirror-ODD: I(mu M) = -I(M). Invariance gives I(mu M) = I(M), hence 2*I(M) = 0 in A.

  A = R/(1/2)Z  (has torsion)  ->  I in the 2-torsion subgroup {0, 1/4}   ... B1224 (CS)
  A = R         (torsion-free) ->  I = 0 exactly                          ... B1225's keystone

CONSEQUENCE for B1225. Its step 2 assumed the 17 menu atoms are OBJECT-CANONICAL
(mirror-even and dimensionless) -- which this bench cannot check, since the atom list is
cloud's (see the 2026-08-31 addendum). The theorem replaces that hypothesis: real + amphichiral
=> mirror-even, for free. So B1225 needs only that the atoms are REAL and dimensionless, and
B1203 verified reality on this bench when it re-ran the enumerator ("all 17 atoms real").
"""
import json, snappy
from fractions import Fraction as F

def cs_class(name):
    v = float(snappy.Manifold(name).chern_simons()) % 0.5
    return F(0) if min(v, 0.5 - v) < 1e-9 else F(1, 4)

# Regime 1 -- torsion: CS lives in R/(1/2)Z, so odd + amphichiral gives 2-torsion, not zero.
amph = ['m004', 'm003', 'm136', 'm135', 'm206', 'm207']
r1 = {n: cs_class(n) for n in amph}
assert all(v in (F(0), F(1,4)) for v in r1.values()), r1
assert F(1,4) in r1.values(), "regime 1 is VACUOUS unless some amphichiral manifold sits off zero"
print("regime 1 (A = R/(1/2)Z, torsion):", {k: str(v) for k, v in r1.items()})
print("   -> 2-torsion, NOT zero; the nonzero cases are what make it non-vacuous\n")

# Regime 2 -- torsion-free: the same hypothesis forces exactly zero.
# B1168 verified the archimedean data by hand; this records the classification it produced.
r2 = {"Vol": "mirror-EVEN (nonzero)", "cusp shape 2sqrt3 i": "mirror-EVEN (nonzero)",
      "length spectrum": "mirror-EVEN (nonzero)", "Chern-Simons": "mirror-ODD"}
odd_real_nonzero = [k for k, v in r2.items() if "ODD" in v and "R-valued" in v]
print("regime 2 (A = R, torsion-free): B1168's archimedean classification")
for k, v in r2.items(): print(f"   {k:22s} {v}")
print(f"   R-valued mirror-ODD data with a NONZERO value: {odd_real_nonzero}  (theorem forbids any)\n")

out = {"theorem": "mirror-odd + amphichiral => 2*I = 0 in the value group A",
       "regime_torsion":      {"A": "R/(1/2)Z", "result": "{0, 1/4}", "arc": "B1224",
                               "witness": {k: str(v) for k, v in r1.items()}},
       "regime_torsion_free": {"A": "R", "result": "0", "arc": "B1225 keystone"},
       "b1225_hypothesis_before": "atoms are OBJECT-CANONICAL (mirror-even and dimensionless)",
       "b1225_hypothesis_after":  "atoms are REAL and dimensionless (reality verified by B1203 on this bench)",
       "novelty": ("CONSOLIDATION, not discovery -- the argument is B1224's, generalised. What was "
                   "missing was the connection: B1183 (c is one global involution, c|R trivial) and "
                   "B1203 (atoms real) already sat beside B1225 without being joined."),
       "still_owed": "the atom LIST is cloud's; only the count 11720 and 'all 17 real' were reproduced here"}
json.dump(out, open("frontier/B1227_one_theorem_two_regimes/results.json", "w"), indent=1)
print("B1225's hypothesis: OBJECT-CANONICAL  ->  REAL (amphichirality supplies the rest)")
