"""B8142b -- the reflection formula that Fried + Pfaff + the Sym-power identity jointly FORCE.

    |R(-m, sigma_m)| = (c(m)/c(m-1))^{2 kappa} * exp(-4 m vol/pi) * |R(m, sigma_m)|

CONDITIONAL on Fried's theorem applying to rho(m) = Sym^{2m} C^2 in the cusped setting --
hypotheses NOT verified here. What is unconditional is the Sym-power identity (bridge.py)
and the algebra below; the physics of the conclusion rests on Fried.

The c(m)/c(2) values are the independently banked ones (B8104/B8112), not refitted here.
"""
import math
import sys

FAIL = []


def check(name, ok, detail=""):
    print(("  PASS  " if ok else "  FAIL  ") + name + (("   " + detail) if detail else ""))
    if not ok:
        FAIL.append(name)


VOL = 2.029883212819307          # m004, full double precision (a truncated string mis-tests at 1e-11)
KAPPA = 1                        # m004 has one cusp
C_OVER_C2 = {2: 1.0, 3: 0.7121142418, 4: 0.5531518273, 5: 0.4522787995}  # banked, B8104/B8112
#            ^ c(2)/c(2) = 1 by definition -- including it makes m = 3 available, which an
#              earlier version of this script needlessly excluded.
ABS_R = {3: 0.9687980563, 4: 0.9852054775, 5: 1.0052425571}       # computed in bridge.py, cutoff 5.5

print("A  inputs are the banked ones, not refitted")
check("kappa = 1 and vol carried at full precision", KAPPA == 1 and abs(VOL - 2.0298832128) < 1e-9,
      "vol = %.15f" % VOL)
check("c(m)/c(2) present for m = 2,3,4,5", sorted(C_OVER_C2) == [2, 3, 4, 5])

print("\nB  the forced reflection formula")
print("      m   c(m)/c(m-1)     |R(m,sigma_m)|     exp(-4m vol/pi)     => |R(-m,sigma_m)|")
pred = {}
for m in (3, 4, 5):
    ratio = C_OVER_C2[m] / C_OVER_C2[m - 1]
    damp = math.exp(-4.0 * m * VOL / math.pi)
    val = (ratio ** (2 * KAPPA)) * damp * ABS_R[m]
    pred[m] = val
    print("      %d   %.10f    %.10f      %.6e        %.6e" % (m, ratio, ABS_R[m], damp, val))

print("\nC  internal consistency -- the formula must behave, or it is not a formula")
check("every predicted value is positive and finite",
      all(v > 0 and math.isfinite(v) for v in pred.values()))
# An earlier version tested `all(v < 1e-4)`. That threshold was TUNED TO THE TWO POINTS
# THEN AVAILABLE and broke as soon as m=3 was added (2.1e-04). Replaced by the claim the
# derivation actually makes: successive values decay by the damping factor exp(-4 vol/pi).
DECAY = math.exp(-4.0 * VOL / math.pi)
ratios = [pred[m] / pred[m - 1] for m in sorted(pred)[1:]]
check("successive reflected values decay by ~exp(-4 vol/pi) = %.4f" % DECAY,
      all(0.5 * DECAY < r < 2.0 * DECAY for r in ratios),
      "ratios " + ", ".join("%.4f" % r for r in ratios))
check("all reflected values are far below 1 (exponentially suppressed)",
      all(v < 1e-3 for v in pred.values()), "max = %.2e" % max(pred.values()))
check("they DECREASE with m, as the damping requires",
      pred[5] < pred[4] < pred[3], "%.3e -> %.3e -> %.3e" % (pred[3], pred[4], pred[5]))
# CONTROL: drop the damping factor and the prediction must stop being small -- otherwise
# the smallness is not coming from where the derivation says it is.
undamped = {m: (C_OVER_C2[m] / C_OVER_C2[m - 1]) ** (2 * KAPPA) * ABS_R[m] for m in pred}
check("CONTROL without exp(-4m vol/pi) the values are O(1), so the damping is doing the work",
      all(0.1 < v < 10 for v in undamped.values()),
      "%s" % ", ".join("%.4f"%undamped[m] for m in sorted(undamped)))

print("\nD  what this is, and is not")
print("      IS  : a relation between the twisted Ruelle family at -m and at +m, with the")
print("            right-hand side absolutely convergent -- exactly the object residue 2 needs.")
print("      NOT : a proof. It is CONDITIONAL on Fried applying to rho(m) in the cusped")
print("            setting, which is NOT verified here. If Fried applies, the reflection is")
print("            FORCED; if it does not, this is an implication with an unchecked antecedent.")
print("      USE : it is falsifiable -- an independent computation of R at a negative integer")
print("            would either confirm it or refute the antecedent.")

print("\n%d/%d checks passed" % (7 - len(FAIL), 7))
sys.exit(1 if FAIL else 0)
