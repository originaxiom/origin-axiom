"""B247 (sage-python part) -- the authoritative E6 branchings behind the V1 adjudication. Requires sage-python.
Run: sage-python e6_branchings_sage.py

Outputs (verified 2026-06-28):
  78 of E6 -> A2 x G2      :  (8,1) + (8,7) + (1,14)            [(8,7)=56 resolves chat1's 64/78]
  7  of G2 -> A1 x A1      :  (1,1) + (2,0)
  14 of G2 -> A1 x A1      :  (2,0) + (3,1) + (0,2)
  78 of E6 -> A1 x A5      :  (2,20) + (3,1) + (1,35)           [A1 index 1 = LONG; centralizer A5 = SU(6)]
The pyenv adjudication.py consumes these (hardcoded) to compute embedding indices and centralizer dims.
"""
from sage.all import WeylCharacterRing, branching_rule

E6 = WeylCharacterRing("E6", style="coroots")
adj = E6(0, 1, 0, 0, 0, 0)           # the 78 (adjoint)
assert adj.degree() == 78

A2G2 = WeylCharacterRing("A2xG2", style="coroots")
print("78 -> A2xG2 :", adj.branch(A2G2, rule=branching_rule("E6", "A2xG2", "miscellaneous")))

G2 = WeylCharacterRing("G2", style="coroots")
A1A1 = WeylCharacterRing("A1xA1", style="coroots")
bG = branching_rule("G2", "A1xA1", "extended")
print("7  -> A1xA1 :", G2(1, 0).branch(A1A1, rule=bG))
print("14 -> A1xA1 :", G2(0, 1).branch(A1A1, rule=bG))

A1A5 = WeylCharacterRing("A1xA5", style="coroots")
print("78 -> A1xA5 :", adj.branch(A1A5, rule=branching_rule("E6", "A1xA5", "extended")),
      "  (A1 index 1 = long-root; centralizer A5 = SU(6))")
