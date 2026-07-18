# G3 — BANKED: 1.785 IDENTIFIED EXACTLY + THE PERIOD LAW STAYS OPEN
# (cc2 seat + subagent, 2026-07-18; prereg 389b9af5; gates passed)

(a) THE VALUE CATALOGUE COMPLETES: the (n=10, kappa=8) cell is
  |tr_odd| = sqrt(5 + 2 sqrt3 - 2 sqrt2 - sqrt6), min poly
  x^8 - 20x^6 + 98x^4 - 172x^2 + 97 (irreducible, verified 250
  digits); Re = (1 - sqrt2)/2, Im = sqrt2 + sqrt6/2 - sqrt3/2. The
  field Q(sqrt2, sqrt3) matches the cell's arithmetic (disc 96 =
  2^5 x 3 at the 2-resonant stage kappa = 8). The D4 value menu is
  now fully identified.
(b) THE MINIMAL PERIOD: GOLDEN PROVEN — period exactly 20 =
  lcm(4,5), from the exact closed form tr_odd = [4|kappa] -
  [5|kappa]/phi, minimality verified against every proper divisor.
  For n = 4..10 the same Weyl-class mechanism yields only CANDIDATE
  periods (SNF-refined 30,42,112,360,90,770,528; table lcm 55440);
  the 12-level window is shorter than every candidate (repeat-check
  vacuous, stated); the resonance-consistency necessary condition
  holds only 72/96 — THE GOLDEN MECHANISM DOES NOT CLEANLY
  GENERALIZE; the non-golden period law stays HONESTLY OPEN (mirrors
  the g2_period precedent: generic proven, resonant open).
OPERATIONAL: engine_v7.py silently sets mp.dps = 60 at import —
callers must re-assert precision AFTER import (second engine_v7 trap
banked; the O(N^5) gate_report was the first).
Artifacts: g3_values.py, g3_results.json, g3_run.log.
