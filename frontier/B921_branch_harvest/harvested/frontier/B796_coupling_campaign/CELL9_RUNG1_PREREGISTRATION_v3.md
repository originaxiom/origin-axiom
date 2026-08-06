# CELL 9, RUNG (i) — PREREGISTRATION v3 (re-sealed after the second §16 STOP)

cc3 audit seat, 2026-07-29. SUPERSEDES v2 (3ba81779, byte-frozen).
Second-pass verdict: cell9_sec16_verdict2.md. Deltas from v2 are
marked [D-n] and keyed to the reviewer's required changes 1–5;
everything on the reviewer's VERIFIED-CLEAN list is carried unchanged
(targets, certified values, gap midpoints, Y = 0.75 + artifact,
tolerance formula core, licensed-H machinery, gate, P4, cert
construction). Third §16 pass (delta review) required before
execution.

## [D-1] METHOD (replaces v2's joint Newton; fixes Defect A + the
shakedown-observed basin escape)

**Damped, bracketed scalar secant on the held-out-row residual:**
g(r) = row_n(r)·a(r), where a(r) solves the REGULAR n×n system
[rows 1..n−1; normalization row e_j0] = e_n. The n×n matrix stays
invertible AT the eigenvalue (the normalization row replaces the
deficient direction) — no bordered matrix, no arb-certification
failure at the root, and it remains regular at multiplicity 2.

Guards (all sealed):
- HARD BRACKET: iterates confined to [r_cert − 0.01, r_cert + 0.01];
  an iterate leaving the bracket ABORTS the run (logged) — the
  shakedown-observed failure mode (basin escape) becomes a clean
  abort, never a wrong converged value. (The gate would also catch
  it; the bracket catches it 10 iterations cheaper.)
- STEP DAMPING: |dr| per step capped at 1e-3 (cap logged when hit).
- P2 (strict, per the reviewer): |g| must strictly decrease from
  iteration 2 onward; a non-decreasing |g| aborts with iterate logged.
- Convergence: |dr| < 1e-27 or 14 iterations (abort if not converged).

P1 (unchanged, 10 decimal-string samples, mpmath dps-60 reference,
≤ 1e-27), P3 [D-2], P4, gate ≥ 7 digits, stability cert at +5 digits
(requirement |dr|_stab < 1e-26) all as v2 except as amended below.

## [D-2] P3 SEMANTICS (fixes the crash-instead-of-pass branch)

The displaced run (gap midpoints 4.42 / 5.29 / 7.21) executes inside
try/except: DIVERGENCE, bracket-exit, P2-abort, or singular-solve in
the displaced run are all CONTROL-PASSES (logged with the failure
mode). The control FAILS only if the displaced iteration converges to
within 1e-20 of the target. The displaced run uses its OWN bracket
[midpoint ± 0.01].

## [D-3] LAM_1 (mult 2) — deferred to its own sub-rung

Per the reviewer's Defect B: the pair protocol as sealed in v2 can
mis-bank under sheet-splitting. **Rung (i) executes lam_2 and the
parent ONLY** (both certified nullity 1 via sv_tail). lam_1 moves to
rung (i-b) with its own prereg, which must contain: a corank-2-capable
procedure (two normalization rows / deflation), a σ₂-grade nullity
assert, the pair-vs-single verdict CONDITIONED on split stability
across two truncations, and pre-declared cert-failure semantics.
Nothing about lam_1 banks from rung (i).

## [D-4] POWER BOX (text repairs; formula unchanged)

- The v2 sentence "a relation is detectable only where H × noise <
  tol_box headroom" is DELETED (raw-convention leftover; contradicted
  the formula).
- d is DEFINED: d = the NUMBER OF ENTRIES of the test vector (terms:
  3 for deg-2 boxes, 5 for deg-4/minpoly). The degree-convention
  H_max is also logged for any boundary case.
- CORRECTION of v2's note: under the max-normalized formula the
  parent λ-minpoly box is **POWERED** (noise ≈ 1.1e-26, tol ≈
  1.1e-25, N_eff = 18.17, H_max ≈ 348 with d = 5, capped 10³ with
  d = 4 convention). v2's "expected UNPOWERED" was wrong; the
  reviewer's recomputation governs. All six (box, target)
  combinations run; UNPOWERED declarations only where the runtime
  formula actually produces H_max < 10.

## [D-5] HONEST COST AND OPERATIONAL NOTES (before launch, per the
reviewer's finding)

- Runtime as coded: ~ONE DAY per eigenvalue serial (reviewer's
  measurement: ~70–99 μs per bessel_k; 6n² calls/iteration
  uncached). The k0 CACHE (the height-Y Bessel factor is
  row-independent) is implemented in v3 code and roughly halves
  this; the secant method needs 1 build/iteration (not 3), a further
  ~3× saving vs the reviewed joint-Newton — realistic estimate
  ~4–8 h per eigenvalue, LOGGED per iteration so the estimate is
  auditable from the first hour.
- Peak memory ~10 GB at the cert stage; runs from the repo root.
- y080_rise_validation.txt provenance: generated 2026-07-29 by the
  inline harness recorded in the session transcript (200-point grid,
  seed 3, reduce_pt from hejhal_m004.py); regenerable via
  cell9_rise_check.py (added in this commit).

## SEAL

Algorithm: SHA-256 of this file's bytes; digest in docs/SEAL_LEDGER.md
(never here). Third §16 pass (delta review of D-1..D-5 + code
conformance smoke test) required before execution.
