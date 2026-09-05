# Boundary-value audit: instrument corrected, scoped mismatch retained

2026-09-05, against original main `f06d3405`. The original PREREGISTRATION,
`crossing.py` and `results.json` remain unchanged. The original definitions
reproduce all 16 finite archived two-loop curve points exactly.

**Instrument defect, independently recomputed:** the sequential weak-angle
solve holds alpha_s=0.118, then changes alpha_s in the second solve without
resolving the first. At two loops the first equation depends on alpha_s.
The final UV residual reaches **0.02683971597**, versus an integrator-tightening
change below **3.10e-11**. Varying the hidden fixed value changes the curve.
The old JSON-input-key test did not check this dependency.

**Correction:** run down from a common UV coupling, fitting only the EM
normalization; independently solve both equations simultaneously running up.
Corrected UV residuals are below 1.04e-10 and up/down disagreement below
8.95e-12. New locks recompute the equations and the legacy defect.

The corrected 61-grid minimum of the historical distance is about 16.485;
61/181 grids plus local refinement find **16.11621136**. The `d<=3` criterion
still is not met by that search. The number is **not calibrated sigma**:
the loop difference is a truncation diagnostic, the gauge-only two-loop
matrix omits Yukawa terms, and the original comparison covers only the
intersection with its actual root brackets. Invalid/excluded points are now
recorded explicitly. No certified global minimum or universal no-go is claimed.

The NEGATIVE classification is retained for this **specified desert
configuration and historical test**, not as a theorem killing E6 or the
program. B1245's group-independence under the shared normalization/content
is preserved; its AST argument did not test the solver's coupled residuals.

New conditional threshold models use the banked exotic multiplets but change
the spectrum assumption. Their meeting is an **inverse fit using all three
archived couplings**, not a prediction. The common-UV-mass escape is tested
including gauge mass running, with its narrow assumptions stated.

Design, code, hashes, successful outputs, failures and physical interpretation:
`reports/physical_bridge_2026_09_05/`. Live locks:
`tests/test_physical_bridge_legacy_audit.py`,
`tests/test_physical_bridge_gauge_running.py`,
`tests/test_physical_bridge_mass_match.py`.
