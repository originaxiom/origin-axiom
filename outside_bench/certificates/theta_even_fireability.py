#!/usr/bin/env python3
"""MEMO-135 CELL (the owner released the standing HOLD: "do the theta-even
designed crossing"): THE FIREABILITY CHECK, RUN BEFORE THE ROW IS SPENT —
and the shot is NOT FIREABLE.  Its output is not a wrong number; it is NO
number.  The licensed row is left UNSPENT.

WHY A CHECK AND NOT A SHOT.  I3's own spec: "firing it consumes the last
licensed contact row (IRREVERSIBLE in the program's own accounting)".  An
irreversible one-shot must be shown to HAVE a determinate output before it
is fired.  Releasing the hold authorizes the shot; it does not make the
shot fireable.  This cell asks only the prior question, and the election
stays the owner's either way.

THE DESIGNED SHAPE (I3, quoted): Lambda -> u -> u-dagger T_m u for
m = 1, 2, 4 -> one shot, ZERO anchors.
PRE-WORK OWED FIRST (I3, quoted): the even-channel AC6 run; the
contact-quantity kind-row adjudication; R7's look-elsewhere ledger; the
T_m non-commuting frame problem.

THE PREREGISTERED FORK:
  F-A  all four pre-work items discharged AND the contact quantity has a
       determinate value => FIREABLE; hand the exact shape to the owner
       for the irreversible election.
  F-B  any pre-work item outstanding OR the contact quantity is
       indeterminate => NOT FIREABLE; the row must NOT be consumed, and
       the blocker is named exactly.
Gate 5 untouched: this cell computes the RANGE of a designed observable
from banked eigenvalues.  It contacts no measured value, and firing
nothing is precisely its point.
"""
import math

# ---- P1: the four pre-work items, each quoted from primary
PREWORK = [
 ("the even-channel AC6 run",
  "B1071 (the SEALED listener), its own scope line",
  "\"THE SCOPE HOLDS: not a completed listener map -- AC3 gates on the "
  "silver instrument (B1072, designed), AC6's TYPE-RUN UNATTEMPTED.\"",
  "OUTSTANDING"),
 ("the contact-quantity kind-row adjudication",
  "B1070 (the listener derivation)",
  "\"the crossing's contact quantity therefore NEEDS ITS OWN KIND-ROW "
  "ADJUDICATION, FLAGGED in the design facts\"",
  "OUTSTANDING (flagged, not performed)"),
 ("the T_m non-commuting frame problem",
  "B1070",
  "\"admits NO JOINT EIGENFRAME (the T_m pairwise non-commuting)\"",
  "OUTSTANDING (an exhibited obstruction, not a solved step)"),
 ("R7's look-elsewhere ledger",
  "I3's own pre-work list",
  "listed as owed; no discharging arc located on main",
  "OUTSTANDING (not located)"),
]
print("P1 — THE FOUR PRE-WORK ITEMS I3 OWES BEFORE THE SHOT:")
for name, src, quote, status in PREWORK:
    print(f"    [{status}]")
    print(f"      {name}")
    print(f"      source: {src}")
    print(f"      {quote}")
n_out = sum(1 for *_, s in PREWORK if s.startswith("OUTSTANDING"))
print(f"    ==> {n_out} of {len(PREWORK)} pre-work items OUTSTANDING.")
assert n_out == 4

# ---- P2: THE BLOCKING FACT — the shape's middle term does not exist
print("\nP2 — THE MIDDLE TERM OF THE DESIGNED SHAPE DOES NOT EXIST.")
print("    The shape is Lambda -> u -> u-dagger T_m u.  The spec's own I2:")
print("    \"u-as-apparatus (G9): MISSING BY DESIGN -- the physical-apparatus")
print("     layer is the spec's ONE UNCONSTRUCTED GAP, firewalled")
print("     (GATE 5 FORBIDS FITTING); the only builds on Lambda are two")
print("     calibration parameterizations, BOTH NULL (B1128, B1132).\"")
print("    So u cannot be supplied without violating Gate 5, and the two")
print("    attempts to supply it are banked NEGATIVES.")

# ---- P3: THE DECISIVE COMPUTATION — the output is a free interval
# B1070's banked even-sector spectra at the design's own m-values.
S5 = math.sin(2*math.pi/5)
SPEC = {1: S5, 2: math.sqrt(3)/2, 4: S5}          # T_m eigenvalues +-lam
ZERO_M = [3, 5]                                    # forced-zero, per B1070
print("\nP3 — THE CONTACT QUANTITY'S RANGE (the decisive computation).")
print("    B1070 banks the even sector's spectra: T_m has eigenvalues +-lam_m")
print("    at m = 1, 2, 4, and is FORCED-ZERO at m = 3, 5.")
print("    For a TRACELESS Hermitian T with eigenvalues +-lam, the Rayleigh")
print("    quotient u-dagger T u over unit u sweeps EXACTLY [-lam, +lam]")
print("    (min/max = extreme eigenvalues; the range is the full interval).")
print(f"    {'m':>3s} {'lam_m':>12s} {'u-dagger T_m u ranges over':>32s}")
box = 1.0
for m in (1, 2, 4):
    lam = SPEC[m]
    box *= 2*lam
    print(f"    {m:>3d} {lam:>12.9f} {'[%+.9f, %+.9f]' % (-lam, lam):>32s}")
for m in ZERO_M:
    print(f"    {m:>3d} {0.0:>12.9f} {'{0} (forced zero -- determinate)':>32s}")
print(f"    => the shot's output lives in a box of volume {box:.6f},")
print("       and NOTHING IN THE RECORD SELECTS A POINT IN IT.")
print("    THE DESIGN SELECTS EXACTLY THE u-CONTROLLED ENTRIES: m = 1, 2, 4")
print("    are precisely the m where B1070 says the even sector VARIES WITH u;")
print("    the two m that are determinate (3, 5) are forced to zero and carry")
print("    no information.  So the one-shot's three numbers are, in full, a")
print("    free point of a 3-box chosen by the one object the spec cannot")
print("    construct.  FIRING IT PRODUCES NOT A WRONG NUMBER BUT NO NUMBER.")
assert box > 0

# ---- P4: the verdict
print(f"""
P4 — THE VERDICT: OUTCOME F-B.  NOT FIREABLE.  THE ROW IS LEFT UNSPENT.
  Four independent blockers, any one of which is sufficient:
    (1) all four pre-work items I3 itself owes are OUTSTANDING;
    (2) the shape's middle term u is MISSING BY DESIGN and Gate 5 forbids
        supplying it -- the two attempts are banked NULLS;
    (3) the contact quantity is INDETERMINATE at exactly the three m the
        design uses -- a free point in a box of volume {box:.4f};
    (4) the T_m admit NO JOINT EIGENFRAME, so the three numbers do not
        even share a frame in which to be read together.
  CONSUMING THE LAST LICENSED CONTACT ROW ON THIS WOULD SPEND AN
  IRREVERSIBLE RESOURCE FOR NO OUTPUT.  The bench does not fire it, and
  records that the hold was RELEASED BY THE OWNER while the shot was
  BLOCKED BY THE RECORD -- two different things, both now on the page.

P5 — THE CONSTRUCTIVE HALF (what IS available, and it needs no u):
  B1070 also banks that B1011-C6's MIRROR VALUE SET is PROVEN
  u-INDEPENDENT ((1/4)tr).  That is a DETERMINATE quantity in the same
  even sector, and it does not route through the missing apparatus.
  IF a theta-even crossing is wanted, THAT is the quantity that can be
  specified without u -- but it is A DIFFERENT SHOT: it must not inherit
  I3's preregistration, and it needs its own kind-row adjudication (the
  very item I3 already flags as owed).  Whether a u-INDEPENDENT contact
  even consumes a licensed row is itself a kind-row question, and
  possibly the most valuable one here: a contact quantity that no
  apparatus choice can move may be a CHEAPER contact than the ledger
  assumes.  Named, not claimed, and not run.
  FENCE: the shot is not fired, no measured value is touched, and the
  licensed-row ledger is unchanged.  Gate 5 untouched.""")
