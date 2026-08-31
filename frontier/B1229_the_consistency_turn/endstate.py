"""THE END-STATE under the consistency program -- what the input ledger looks like if the
bootstrap move is applied to every row. Honest grading per row: COMPUTED / CANDIDATE / TYPE.

Cardy's theorem: in a RATIONAL CFT the consistent conformal boundary states are in bijection
with the PRIMARIES -- a FINITE set. Any continuous family of boundary data is therefore cut to
finitely many consistent points. That is the instrument aimed at the last continuum.
"""
import json
from fractions import Fraction as F

NPRIM_E6 = 3   # (E6)_1: {1, 27, 27bar}

print("THE MAP'S OWN END-STATE (GRAND_COMPUTATION section 9, floor amendment):")
print("  ell + the relational c-bit + finite labels + sigma (one bridge) + the lambda-placement")
print("  + the P^3 adjudication\n")
print("UNDER THE CONSISTENCY PROGRAM:\n")

rows=[
 ("ell",            "ONE dimensionful unit", "unchanged -- a unit is a CALIBRATION, not a parameter", "TYPE"),
 ("sigma",          "was: ONE continuous dimensionless anchor (R+)",
                    "-> RATIONAL by Anderson-Moore/Vafa; -> 7 values by MMS; -> 2 by the object's Z/3. ONE BIT.", "COMPUTED"),
 ("the c-bit",      "was: an unexplained external Z/2",
                    "-> IS the modular-invariant choice (diagonal vs charge-conjugate). Still a bit, now EXPLAINED.", "STRUCTURAL"),
 ("the P^3 line",   "was: up to THREE continuous parameters (the floor amendment's contested row)",
                    f"-> IF it parametrises boundary data of the rational boundary theory, Cardy cuts it to the "
                    f"{NPRIM_E6} primaries. Continuum -> finite. THIS IS THE TEST TO RUN.", "CANDIDATE"),
 ("lambda",         "was: an uncollapsed continuous 'time' candidate",
                    "-> a KMS weight; for a rational boundary the modular flow is periodic => finite label.", "CANDIDATE"),
 ("r, gamma_5, labels","were: finite already", "unchanged -- finite menus", "TYPE"),
]
for n,before,after,grade in rows:
    print(f"  [{grade:10s}] {n}\n        {before}\n        {after}")

comp=[r for r in rows if r[3]=="COMPUTED"]; cand=[r for r in rows if r[3]=="CANDIDATE"]
print(f"\n  computed now : {len(comp)}    candidate (named test) : {len(cand)}")

print("""
IF the two candidates land, the end-state reads:

      ell  +  a handful of BITS AND FINITE LABELS

i.e. ZERO continuous dimensionless parameters, and ONE calibration -- which is exactly the
map's own sentence for the goal: "one measurement then predicts the rest."

WHAT MAKES THIS DIFFERENT FROM THE DELETION SCHEDULE: nothing above is DERIVED from the object.
The object is not asked. Consistency classifies the menu; the object's arithmetic (Z/3, Q(sqrt-3))
cuts the menu; the closer still picks the point. B1225 is untouched -- the object still cannot
select. It never had to: a classified finite menu plus a picker is a parameter-free theory with
a calibration, which is what a ToE is allowed to look like.

HONEST FENCES:
  * the 7-value list assumes two characters with vanishing Wronskian index; drop that and the
    menu grows, but RATIONALITY (hence discreteness) survives -- that is the robust core.
  * the P^3 row needs the Higgs line to BE boundary data of the rational theory; if it is not,
    Cardy does not apply and the row stays contested. Named, not assumed.
  * lambda's periodicity is a candidate, not a computation.
  * Gate 5 intact: no measured value anywhere in this cell.
""")
json.dump({"rows":[{"row":n,"before":b,"after":a,"grade":g} for n,b,a,g in rows],
           "computed":len(comp),"candidate":len(cand),
           "end_state_if_candidates_land":"ell + bits and finite labels; ZERO continuous dimensionless parameters",
           "method":"consistency classifies the menu; the object's arithmetic cuts it; the closer picks",
           "b1225_untouched":True},
          open(f"{__file__.rsplit('/',1)[0]}/endstate.json","w"),indent=1)
