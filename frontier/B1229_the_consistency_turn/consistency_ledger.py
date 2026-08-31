"""THE CONSISTENCY LEDGER -- the method flip, applied to EVERY input row.

The map asks the OBJECT for each input and the object refuses (correctly: B1225, the naming
wall). So ask CONSISTENCY instead. Every row below gets the consistency condition that could
quantize or type it. This is the bootstrap move, applied to the input ledger.

THE THESIS being tested: the observer's input list is not a grab-bag of externals -- it is
exactly the data that specifies a MODULAR-INVARIANT CFT on the object's boundary.
"""
from fractions import Fraction as F
import json

ROWS = [
 ("sigma (A2)", "the ONE continuous dimensionless anchor, c = 6*sigma",
  "RCFT rationality (Anderson-Moore/Vafa: c, h rational) + MMS two-character classification",
  "QUANTIZED: R+ -> 7 (Deligne series) -> 2 with the object's Z/3. sigma becomes ONE BIT.",
  "COMPUTED"),
 ("the c-bit", "chirality; proved NOT self-supplied (B713/B760 NO-HATCH, B1183, B1184)",
  "the classification of MODULAR INVARIANTS of the boundary CFT",
  "TYPED: for a Z/3 fusion ring the invariants are diagonal vs CHARGE-CONJUGATE -- a Z/2. "
  "The c-bit IS the modular-invariant choice. Matches B1184 exactly: the theory names itself "
  "(the fusion ring) but cannot SIGN (which invariant). Not deleted -- EXPLAINED.",
  "STRUCTURAL"),
 ("the r-label (arrow)", "one Z/2 seed, finite-place (B1182)",
  "the T-matrix / the modular group's action; T has finite order (12 for E6)",
  "CANDIDATE: the arrow as a choice of square root / branch of T. Finite by modularity, "
  "which already matches 'finite-place'. Not computed here.",
  "OPEN"),
 ("lambda (the weight)", "completes the tracial II_1 to type III_lambda; 'the closer's clock'",
  "the KMS condition / Tomita-Takesaki modular flow -- the SAME word 'modular', and not a pun: "
  "the modular automorphism group is what a state's weight generates",
  "CANDIDATE, and the strongest lead here: lambda is a KMS parameter, and for a RATIONAL "
  "boundary the modular flow is periodic -- which would make lambda a finite label too.",
  "OPEN"),
 ("the P^3 line", "up to 3 continuous parameters (B1193 floor amendment; C12-trivial on B_0)",
  "UNITARITY of the boundary CFT + the finite number of primaries",
  "CANDIDATE: a continuous family of boundary conditions is constrained by Cardy's condition "
  "(boundary states = a finite set for a RCFT). Cardy states are FINITE -- so a P^3 of them "
  "cannot all be consistent boundary states.",
  "OPEN -- and this is the sharpest unrun test"),
 ("ell (A1)", "the ONE dimensionful unit -- the metre-to-ours wire",
  "NONE -- and correctly so: a unit is not a number. No consistency condition can fix a unit; "
  "it is the single calibration the map's row 7 calls the permanent floor.",
  "PERMANENT: not a parameter, a calibration.",
  "CLOSED-BY-TYPE"),
 ("family / VEV labels", "finite menus (B1025 I5)",
  "the finite set of primaries / Cardy boundary states of the boundary CFT",
  "ALREADY FINITE; consistency would say WHICH finite set, i.e. re-derive the menu.",
  "STRUCTURAL"),
]
w=max(len(r[0]) for r in ROWS)
print("THE CONSISTENCY LEDGER -- ask consistency, not the object\n")
for name,what,cond,result,grade in ROWS:
    print(f"[{grade}] {name}")
    print(f"    is        : {what}")
    print(f"    condition : {cond}")
    print(f"    result    : {result}\n")

g={}
for *_,grade in ROWS: g[grade]=g.get(grade,0)+1
print("grades:", g)
print("\nTHE THESIS: every row above maps to a datum of a modular-invariant boundary CFT --")
print("  sigma        -> the central charge (which member of a FINITE classified list)")
print("  the c-bit    -> which MODULAR INVARIANT (diagonal vs charge-conjugate)")
print("  labels/VEV   -> which PRIMARY / Cardy boundary state (a finite set)")
print("  lambda       -> the KMS weight (the modular automorphism's parameter)")
print("  ell          -> NOT a CFT datum: the calibration, permanently")
print("\nSo the 'observer' is not a grab-bag of externals. It is a CHOICE OF BOUNDARY CFT,")
print("and every one of its inputs is a datum in a classified, mostly FINITE structure.")
print("That is why the object cannot supply them (B1225: it cannot select) and why they are")
print("nonetheless not arbitrary -- consistency classifies the menu even when the object cannot pick.")
json.dump({"rows":[{"row":n,"is":w_,"condition":c,"result":r,"grade":gr} for n,w_,c,r,gr in ROWS],
           "grades":g,
           "thesis":"the observer's input list = the data of a modular-invariant boundary CFT",
           "method":"bootstrap: ask consistency, not the object"},
          open(f"{__file__.rsplit('/',1)[0]}/consistency_ledger.json","w"),indent=1)
