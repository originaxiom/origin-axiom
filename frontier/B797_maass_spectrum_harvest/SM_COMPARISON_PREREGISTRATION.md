# B792 SM-COMPARISON PREREGISTRATION (sealed before the certified run)

cc3 audit seat, 2026-07-28. This file extracts the protocol VERBATIM
from the docstring of `sm_comparison_tests.py` (which governed the
uncertified dry-run) and seals it, per cc's hold relay items (1)-(3),
BEFORE the certified re-run. Amendments A1-A3 below are the only
deltas from the dry-run protocol and are fixed before the re-run.

## THE PROTOCOL (verbatim from the dry-run docstring)

  SPECTRAL SET: all stable distinct eigenvalues of m004 from
  eigenvalues_final.json + scanD_refined.json; both r_n and
  lam_n = 1 + r_n^2. Eigenvalue precision: ~1e-9 relative; the
  spectral digit budget is capped at 8.

  TEST 1 (direct match): x in {r_n, lam_n} vs each of the 18 banked
  PDG targets v: candidate iff |x/v - 1| < tau_v,
  tau_v = max(2 * rel_unc_v, 1e-8). NULL: 500 surrogate spectra
  (Weyl-distributed: density ~ r^2 over the observed window, same
  count), same test => expected candidate count. A candidate is a HIT
  only if its per-target surrogate probability < 0.02 (B743 Gate 3).

  TEST 2 (ratios): all pairwise ratios r_m/r_n (m != n) and
  lam_m/lam_n vs each target, same rule, same surrogate null.

  TEST 3-lite (algebraicity at 8 digits): PSLQ of each r_n, lam_n
  against the six B743 bases (caps: 64 for deg-2, 16 for deg-4;
  dps = 14, tol = 1e-7, maxsteps 200000). NULL: 50 surrogates per
  basis; a relation is a HIT only if surrogate rate < 0.02. NOTE:
  8-digit PSLQ can only exclude LOW-HEIGHT relations; the deep
  algebraicity test (50+ digits, handoff Test 3) remains open and is
  NOT claimed here in either direction.

## AMENDMENTS (fixed before the certified run)

A1 (certified spectral set). The spectral set is the mode-count
CERTIFIED set: eigenvalues confirmed stable between truncation margins
21 and 27 at fixed Y = 0.75 (`mode_count_certification.json`). Any
eigenvalue moving more than 1e-6 in r between mode counts is EXCLUDED
from the set and reported.

A2 (tolerance floor from certification). The per-target tolerance
becomes tau_v = max(2 * rel_unc_v, 1e-8, 10 * max_rel_dr) where
max_rel_dr = max over the certified set of |dr|/r between mode counts,
read from mode_count_certification.json at runtime. The formula is
fixed here; the value is whatever certification produced.

A3 (verdict semantics, scope-corrected per cc). A clean-null outcome
is stated as: "no SM value is reachable from this spectral set at
8-digit precision under the stated base-rate control" — a
GENERIC-SPECTRUM null over a bounded window. It does NOT import the
B713-B716 H0 (a character-variety/torsor statement, different object),
does NOT claim the handoff's Tests 1-2 as posed (those require 20+
digits), and claims nothing about algebraicity in either direction.
A gated HIT goes to cc for adversarial re-derivation before any
write-up.

## SEAL

Algorithm: SHA-256 of this file's bytes; digest recorded in
docs/SEAL_LEDGER.md (never in this file).
