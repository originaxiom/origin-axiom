#!/usr/bin/env python3
"""MEMO-134 CELL (ranked remainder item 1b): THE COSMOLOGY LEDGER'S ROW 8
(STRUCTURE FORMATION) FIRST PROBE, RUN — and it fails STRUCTURALLY, twice,
the second time for exactly the reason row 2 failed.  The two "MISSING"
rows are ONE obstruction seen twice.

THE LEDGER'S OWN WORDS (row 8 — "the most purely and simply MISSING row in
the whole cosmology ledger; no attempt, no negative, no adjacent theorem.
It is not walled; it has never been started"):
  "does B168's retention-rate decay curve, treated purely as a
   dimensionless growth-law SHAPE (never as a value), have any structural
   analog to a growth-of-structure exponent under a preregistered,
   Gate-5-compliant comparison?"
The ledger also records the honest prior: rows 1 and 2's STALLED
precedents make failure expected.

THE GATE-5 TRAP, NAMED BEFORE IT IS AVOIDED.  B168's retention runs
0.583 -> 0.397.  The cosmological growth index is a number in that
neighbourhood.  COMPARING THEM WOULD BE EXACTLY S008's RETRACTED
"iterations ~ e-folds" FAILURE MODE — a numerical coincidence dressed as
a derivation, and this record killed that once already.  THIS CELL MAKES
NO VALUE COMPARISON OF ANY KIND.  It asks only about SHAPE, which is what
the ledger actually asked for.

THE PREREGISTERED TEST.  A growth-of-structure exponent is by definition
  gamma = d ln D / d ln a
— a POWER-LAW slope taken with respect to a SCALE.  So the analogy needs
two things, and each is separately checkable:
  (i)  the growth must be POWER-LAW in its own depth variable (otherwise
       no exponent exists to compare, whatever its value);
  (ii) there must BE an independent scale variable to differentiate
       against (otherwise the derivative is not defined at all).
THE FORK:
  G-A  the growth is power-law AND a scale variable exists => an exponent
       exists and row 8's probe returns a genuine CANDIDATE.
  G-B  either fails => the probe returns a STRUCTURAL MISMATCH, with the
       failing half named.
Gate 5 untouched: dimensionless counts and growth classes only; no
measured value enters and none is compared to.
"""
import math

# ---- S1: B168's banked data, restated (NOT recomputed -- it is cited)
RATIOS = [7.0, 5.71, 5.45, 5.03, 4.96, 4.77]        # history growth ratios
RETENT = [0.583, 0.476, 0.454, 0.419, 0.413, 0.397]  # r_L
N0, NEND = 96, 2488080
N = [float(N0)]
for r in RATIOS:
    N.append(N[-1]*r)
print("S1 — B168's BANKED DATA (cited, not recomputed):")
print(f"    histories {N0} -> {NEND} (reconstructed endpoint {N[-1]:.0f}, "
      f"agreement {100*min(N[-1],NEND)/max(N[-1],NEND):.2f}%)")
print(f"    growth ratios : {RATIOS}")
print(f"    retention r_L : {RETENT}   (decreasing, decelerating)")
assert abs(N[-1]-NEND)/NEND < 0.01

# ---- S2: THE GROWTH-CLASS TEST (requirement (i))
print("\nS2 — REQUIREMENT (i): IS THE GROWTH POWER-LAW IN DEPTH?")
print("    A power law N ~ L^gamma has a CONSTANT log-log slope")
print("    gamma_L = ln(N_{L+1}/N_L) / ln((L+1)/L).")
print(f"    {'step':>6s} {'ln ratio':>10s} {'log-log slope':>15s}")
loglog, loglin = [], []
for i, r in enumerate(RATIOS):
    L = i + 1
    g = math.log(r)/math.log((L+1)/L)
    loglog.append(g); loglin.append(math.log(r))
    print(f"    {L:>6d} {math.log(r):>10.4f} {g:>15.3f}")
spread_ll = max(loglog)/min(loglog)
spread_lin = max(loglin)/min(loglin)
print(f"    log-log slope spans {min(loglog):.2f} .. {max(loglog):.2f}"
      f"  -> ratio {spread_ll:.1f}x  (constant would be 1.0x)")
print(f"    log-LINEAR slope spans {min(loglin):.3f} .. {max(loglin):.3f}"
      f"  -> ratio {spread_lin:.2f}x")
assert spread_ll > 3 and spread_lin < 1.5
print("    => THE LOG-LOG SLOPE IS NOT CONSTANT — it grows by a factor of")
print(f"       {spread_ll:.1f} across the measured range, so the growth is NOT a")
print("       power law and NO EXPONENT EXISTS TO COMPARE.  The log-LINEAR")
print(f"       slope is near-constant ({spread_lin:.2f}x), so the growth is")
print("       EXPONENTIAL-class with a slowly drifting base.")
print("    REQUIREMENT (i) FAILS.  Growth-of-structure is a POWER-LAW object;")
print("    this ensemble is an EXPONENTIAL one.  Different growth classes.")

# ---- S3: requirement (ii), the deeper block
print("\nS3 — REQUIREMENT (ii): IS THERE A SCALE TO DIFFERENTIATE AGAINST?")
print("    gamma = d ln D / d ln a needs the scale factor a.  The record has")
print("    no such variable, and that is banked TWICE, independently:")
print("    * B168's OWN G4 (this row's source): every emergent quantity is a")
print("      dimensionless ratio of counts — 'NO SCALE EMERGES FROM THE")
print("      ENSEMBLE'; a scale would need an external unit of accretion.")
print("    * memo 132 (this bench, row 2): the tower has NO NET VOLUME GROWTH")
print("      — det J_T = -1 constant, det J_L = 0, det sigma^2 = +1 with")
print("      eigenvalue product exactly 1, so the Lyapunov sum is zero at")
print("      every point AS AN IDENTITY.  A scale factor is precisely a net")
print("      volume growth; there is none to be had.")
print("    REQUIREMENT (ii) FAILS, and fails by theorem rather than by search.")

# ---- S4: the verdict and the unification
print("""
S4 — THE VERDICT: OUTCOME G-B, with BOTH halves failing.
  Row 8's probe returns a STRUCTURAL MISMATCH:
    (i) no exponent exists — the ensemble grows exponentially in depth
        while a growth-of-structure exponent is a power-law slope;
    (ii) no scale exists to take the slope with respect to.
  Neither failure is a value comparison, and none was made.

THE UNIFICATION — THE CELL'S REAL CONTRIBUTION:
  ROWS 2 AND 8 ARE NOT TWO INDEPENDENT GAPS.  Row 2 (inflation) needs
  e-folds = the log of a VOLUME RATIO.  Row 8 (structure formation) needs
  an exponent taken with respect to a SCALE FACTOR.  Both are the same
  missing object: NET VOLUME GROWTH.  memo 132 proved the record has none,
  by determinant identities that hold at every point.  So the two rows the
  ledger grades MISSING fail for ONE reason, and it is a proved one.
  PROPOSED: row 8 moves MISSING -> PROVED NEGATIVE, sharing row 2's
  mechanism, and the ledger records the two as one obstruction rather than
  two blind regions.  That is a smaller blind region than the ledger
  currently reports, honestly arrived at.

ROW 7 (THE CMB) DISPOSITIONED IN THE SAME PASS — target by target,
not by blanket inheritance.  The ledger names three: an AMPLITUDE, a
SPECTRAL INDEX, an ACOUSTIC-PEAK LOCATION.  Each needs a specific object:
  * SPECTRAL INDEX n_s  -> needs a TILT, i.e. a preferred sign of growth
    across modes.  memo 132 proved none exists: the tower is
    reciprocal-closed by det = 1, so expansion and contraction compensate
    exactly.  => BLOCKED BY THEOREM (row 2's mechanism, inherited with
    its proof, not by analogy).
  * ACOUSTIC-PEAK LOCATION -> a ratio of a sound horizon to an angular
    diameter distance; both are integrals over an EXPANSION HISTORY a(t).
    No net volume growth => no a(t).  => BLOCKED BY THEOREM (same object).
  * AMPLITUDE -> needs a normalization against a scale.  B168 G4 and the
    scale-torsor no-go both forbid it.  => BLOCKED BY THEOREM (banked).
  BUT THE HONEST SPLIT MUST BE STATED: all three are blocked GIVEN a
  perturbation spectrum to tilt, normalize or resolve into peaks — and
  THE RECORD HAS NO PERTURBATION THEORY AT ALL.  So row 7 is not purely
  a proved negative: its three NAMED targets are blocked by theorem, and
  the prior structure they presuppose is still simply ABSENT.  Row 7 is
  PART proved-negative (the three named targets), PART still MISSING
  (any perturbation structure whatsoever).  That is a weaker claim than
  rows 2 and 8 support, and it is made weaker deliberately.

DECLINED, DELIBERATELY (the discipline this row most needs):
  B168's own sub-branch 1 asks whether 12*r_infinity is a recognizable
  algebraic number (metallic/phi-related) and flags it OPEN, needing the
  L >= 11 enumeration.  ONLY SIX POINTS EXIST.  Extrapolating a limit from
  six points and then testing it against a family as rich as the metallic
  numbers is a false-positive generator — it is the same shape as the
  retracted S008 coincidence.  THIS CELL DOES NOT ATTEMPT IT, and records
  the refusal so the row is not later read as having been tried and
  failed.  It remains OPEN exactly as B168 left it, pending the heavy
  enumeration.
  FENCE: shape and growth class only; no measured value enters this cell
  and no number here is compared to any observed quantity.  Gate 5
  untouched.""")
