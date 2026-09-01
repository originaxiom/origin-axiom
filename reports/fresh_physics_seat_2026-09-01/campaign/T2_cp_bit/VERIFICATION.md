# VERIFICATION — adversarial re-run of cell T2_cp_bit

**Verifier seat, 2026-09-01. Verdict on the cell's DESIGN-SEALED claim: CONFIRMED.**

All re-runs were performed on copies in the session scratchpad so that no file in this cell
directory was modified (the cell's `results.json` timestamp and content are untouched; this
file is the only addition).

## 1. Re-run of every script

- `compute_cp_bit.py` (copied, run under snappy 3.3.2): reproduces the claimed output exactly.
  All six amphichiral exhibits land on {0, 1/4}: m004/m136/m206 at 0.000000000 (CP-EVEN),
  m003/m135/m207 at 0.250000000 (CP-ODD). m208: CS mod 1/2 = 0, amphichiral=False, bit =
  UNDEFINED-CHIRAL. Twelve chiral controls give exactly the claimed mod-1/2 values (0.386,
  0.364, 0.479, 0.229, 0.308, 0.347, 0.263, 0.097, 0.352, 0.287, 0.037, 0.422); 0 of 12 within
  1e-6 of {0, 1/4}. HALF-1 VERDICT: PASS. Exit code 0.
- The regenerated `results.json` was diffed field-by-field against the banked one: **0 diffs**
  (floats compared at 1e-9). Notably `cs_raw_hp` is non-None for all 19 rows, so
  `precision_agreement_everywhere: True` is a real check, not vacuous via the exception path
  (I specifically attacked this: the script would report agreement if `high_precision()` threw;
  it did not throw for any manifold).
- `bite_control_design.py`: all 9 design checks True, DESIGN BITE VERDICT: PASS, exit 0.

## 2. MB12 attack — could the criterion have failed? Did the control bite?

- The bite control was **actually run** (re-run here) and **bites**: `object_bit(0.25)` returns
  CP-ODD, and non-hypothetically m003 reads CP-ODD in HALF 1 (`MB12_bite_m003_cp_odd: True`).
- The criterion can fail on all advertised paths: NOT-2-TORSION is reachable (object_bit(0.1)),
  UNDEFINED-CHIRAL is produced 13 times on real inputs, and the chiral control m010 at
  0.2291666... (= 11/48, only 0.021 from 1/4) correctly does NOT read as 2-torsion at
  TOL 1e-6 — the tolerance genuinely separates.
- Reader side reaches both bits and the abstain; MATCH and MISMATCH both expressible.
- Minor leniency noted, not verdict-affecting: `generic_chiral_not_2torsion` passes with up to
  1 of 12 controls in the torsion set; the actual count is 0.

## 3. Convention attack (E23) — restated, survives

- Conventions are stated in the script header, FINDINGS.md, and SEALED_DESIGN.md: SnapPy
  `chern_simons()` mod 1/2, value group R/(1/2)Z, representatives [0, 1/2), census
  orientation, `symmetry_group().is_amphicheiral()`, TOL 1e-6, no pi^2 factor.
- Independent restating run by this verifier: `reverse_orientation()` on m004, m003, m006,
  m015 — CS negates mod 1/2 in every case (orientation-odd, as claimed) and the **bit is
  invariant** (m004 CP-EVEN both ways, m003 CP-ODD both ways; -1/4 = 1/4 mod 1/2). The bit is
  orientation-free as claimed.
- Independent amphichirality re-check: m004, m003, m135, m136, m206, m207 all True; m208
  False. Matches the cell's table.
- The raw values are internally consistent with the mod-1/2 normalization (exact rationals
  such as -1/48 for m009 and 11/48 for m010 appear), confirming no stray unit factor.

## 4. Gate 5 — no measured value leaked

- Read both scripts, SEALED_DESIGN.md, FINDINGS.md, results.json in full. No measured Standard
  Model value is named, used, or implied. A grep for measured-value tokens (theta_QCD,
  Jarlskog, CKM/PMNS, delta_CP, characteristic magnitudes) hits only geometric CS values
  (m010's 0.229166...). Z* = 5 is a significance threshold, not a measured value.
- The sealed comparison is HELD: the reader-side inputs are three abstract labels; no label is
  assigned to any real channel anywhere in the cell.
- `git status`: only the untracked campaign directory exists; no tracked file modified.

## 5. Scope attack — FINDINGS.md vs what was computed

- The claims match the computation: one bit, contingent tier (ii), m208 guard, orientation
  independence, 19-manifold precision agreement — all verified above.
- One cosmetic overcount: "HALF-1 checks: 9/9 PASS" — the `checks` dict has 9 keys but two
  (`n_chiral_controls`, `n_chiral_in_torsion`) are integer data, not pass/fail checks; 7
  boolean checks pass and the script's own pass gate uses 6 of them. Does not affect any claim.
- Residual caveat (already disclosed by the cell, correctly): the primary-channel designation
  "on type grounds" cannot be proven free of the author's background knowledge; the cell
  flags this and freezes the choice, which is the correct mitigation short of a pre-registered
  third party. Since the comparison is HELD and the caveat is stated, this does not degrade
  the DESIGN-SEALED verdict.

## Verdict

**CONFIRMED.** Every script re-ran to identical outputs; the MB12 bite was run and bites; the
criterion has reachable failure paths; conventions are stated and survive orientation
restating; Gate 5 is clean; FINDINGS.md claims no more than the computation shows (modulo the
cosmetic 9/9-vs-7 boolean count noted above).
