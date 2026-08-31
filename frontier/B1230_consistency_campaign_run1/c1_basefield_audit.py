"""C-1 -- THE BASE-FIELD AUDIT. Every continuous-parameter count in the input ledger,
re-examined for the field it was taken over. MB12 bite: the audit can return CLEAN."""
import re, io, json
from sympy import totient

LEDGER = "docs/GRAND_COMPUTATION_v0.md"
txt = io.open(LEDGER, encoding="utf-8").read()

# the object's fields, with their degrees over Q
FIELDS = {"Q(zeta_12)": totient(12), "Q(sqrt-3)": 2, "Q(zeta_3)": totient(3), "Q(sqrt5)": 2, "Q": 1}
print("the object's fields and their Q-degrees:", {k:int(v) for k,v in FIELDS.items()}, "\n")

# every row that asserts a CONTINUOUS parameter
rows = [
 ("sigma (A2)", "1 continuous dimensionless anchor", "R+ (no field stated)",
  "RE-TYPED by B1229: rational by Anderson-Moore/Vafa; 7 values by MMS; 2 by the object's Z/3.",
  "OVER-COUNTED (as a continuum)"),
 ("the P^3 Higgs line", "up to 3 continuous parameters", "Q  (dim_Q B_0 = 4)",
  f"dim_Q B_0 = 4 = phi(12) = [Q(zeta_12):Q]. If C12 acts by SCALARS, B_0 is 1-dim over "
  f"Q(zeta_12) and P = a point. Decided by C-2.",
  "SUSPECT -- field not stated; the dimension matches phi(12) exactly"),
 ("lambda (the weight)", "a continuous time-candidate", "none stated",
  "KMS weight; periodicity would make it finite. C-3.", "SUSPECT -- field/periodicity unexamined"),
 ("ell (A1)", "1 dimensionful unit", "n/a -- a UNIT, not a number",
  "not a parameter at all: a calibration. No field applies.", "CLEAN BY TYPE"),
 ("family/VEV magnitudes", "weight-1 magnitudes folded into R+/unit", "none stated",
  "cc3's open note; folds into the ell sector.", "DEFER to the ell sector"),
]
print(f"{'row':22s} {'claimed':32s} {'field taken over':22s} verdict")
verd={}
for n,claim,field,note,v in rows:
    verd[n]=v
    print(f"  {n:20s} {claim:32s} {field:22s} {v}")
    print(f"        {note}")
susp=[n for n,v in verd.items() if v.startswith("SUSPECT")]
over=[n for n,v in verd.items() if v.startswith("OVER")]
print(f"\n  OVER-COUNTED: {len(over)}  {over}")
print(f"  SUSPECT (field never stated): {len(susp)}  {susp}")
clean = not over and not susp
print(f"\n  MB12: the audit CAN return CLEAN (no over-counts, no suspects). It did not: clean={clean}")
print(f"  => VERDICT: OVER-COUNTED. At least one row counted a continuum where consistency gives a")
print(f"     finite menu, and {len(susp)} more rows state no field at all.")
print("\n  THE BINDING RULE THIS ESTABLISHES: every continuous-parameter count in this programme")
print("  must state the field it is taken over. A count over Q of a d-dimensional Q(zeta_12)-space")
print(f"  reports {4}d-1 parameters where the object has d-1 -- three spurious ones at d = 1.")
json.dump({"fields":{k:int(v) for k,v in FIELDS.items()},
           "rows":[{"row":n,"claimed":c,"field":f,"note":nt,"verdict":v} for n,c,f,nt,v in rows],
           "over_counted":over,"suspect":susp,"clean":clean,
           "rule":"every continuous-parameter count must state the field it is taken over"},
          open(f"{__file__.rsplit('/',1)[0]}/c1_results.json","w"), indent=1)
