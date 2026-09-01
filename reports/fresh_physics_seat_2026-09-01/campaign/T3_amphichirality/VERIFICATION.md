# VERIFICATION — cell T3_amphichirality (adversarial re-run)

Adversarial verifier, 2026-09-01. Mandate: refute the cell's PASS. Method: full
re-run of both scripts from a scratchpad copy (cell files untouched), byte-level
comparison of outputs, plus independent checks the cell did not run. SnapPy 3.3.2.

## Verdict: CONFIRMED

## 1. Re-runs (exact reproduction)

Both scripts were copied to a scratchpad directory and re-run there
(`sweep_t3.py` writes `results.json` next to itself, so running in place would
have overwritten the cell's artifact; the copy avoids that).

- `sweep_t3.py`: re-run summary is **identical** to the claimed one —
  sweep 40/40 amphichiral, 40/40 in 2-torsion, max dist 1.193006682561921e-64,
  value distribution {0: 40, 1/4: 0}; control 15 manifolds, 0 on-lattice,
  min dist 0.013462533369514806 (m016), median 0.058163233620368876.
  `python3 -m json.tool` diff of the regenerated `results.json` against the
  checked-in one: **no differences** (all 40 sweep rows, all 15 control rows,
  both anchors).
- `scan_quarter.py`: re-run summary identical — 120 scanned, 120 at 0,
  0 at 1/4, 0 off-lattice, max dist 2.462981538192353e-64. Regenerated
  `scan_quarter_results.json` diffs clean against the checked-in one.
- Anchors reproduced: CS(m004) = -1.15e-65 (≡ 0), CS(m003) = 0.25 exactly.
- Determinism: two independent executions (the cell's and mine) agree to the
  last digit; the pipeline is randomness-free as claimed.

## 2. MB12 attack (could the criterion fail? did the control bite?)

- The control is **actually in the artifact and actually re-ran**: 15 rows
  (m006...m030), all with `is_full_group() = True` and no reversing element,
  0/15 on {0, 1/4} at 1e-9, min distance 1.346e-2 = 1.3e7 × tolerance. The
  criterion is falsifiable in both directions as stated in FINDINGS.md
  (cover off-lattice ⇒ counterexample; controls on-lattice ⇒ DEGRADED), and
  the FINDINGS control table matches the JSON row-for-row.
- Non-triviality of the amphichirality flag: the control loop itself skipped
  orientable-census manifolds because `is_amphicheiral()` returned True for
  them, so the flag demonstrably discriminates — the 40/40 True on covers is
  not an always-True artifact.
- Independent chirality certificate for the controls, not used by the cell:
  since CS is mirror-odd (verified numerically below), any manifold with CS
  off {0, 1/4} mod 1/2 *cannot* admit an orientation-reversing self-isometry.
  All 15 controls are off-lattice, so their chirality is confirmed by CS
  alone, independent of SnapPy's symmetry-group code. This removes the
  cell's own caveat for the control side (the caveat still stands, correctly,
  for the covers' certified amphichirality — though there Theorem A carries
  the claim regardless of the census code).
- One flawed check of mine, recorded for honesty: `M.is_isometric_to(mirror)`
  returns True even for certified-chiral m006 — SnapPy's isometry checker is
  orientation-blind, so that test is vacuous and was discarded; it does not
  contradict the chirality certifications.

## 3. Convention attack (E23)

- Conventions are stated (FINDINGS.md "Conventions", THEOREM.md §4): CS =
  SnapPy `chern_simons()` (normalized by 1/(2π²) per the docstring), mod 1/2,
  mirror-odd; no sheet of the cover chosen; distance = to nearest multiple
  of 1/4.
- Mirror-oddness verified numerically (not just asserted): for m006, m015,
  m019, CS(M) + CS(reverse(M)) ≡ 0 mod 1/2 to 1e-16.
- Mod-1/2 (not mod-1) consistency: SnapPy returns CS(-m003) = +0.25, i.e. it
  reduces -1/4 to +1/4 — only valid in R/(1/2)Z. Also, m003/m135/m207 are
  amphichiral with full groups (re-verified) and sit at 1/4, which would
  violate Corollary B if the value group were R/Z (2-torsion {0, 1/2}); the
  fact that the corollary's set is inhabited at 1/4 by amphichiral manifolds
  confirms the mod-1/2 reading is the operative one.
- Sheet-swap invariance holds by inspection: every reported quantity
  (|distance|, membership, the label 0 vs 1/4) is invariant under CS → -CS.
- The headline sweep result ("all covers at 0") survives any restatement of
  the modulus, since 0 is 2-torsion in every quotient of R.

## 4. Theorem check (read adversarially)

- Theorem A: Step 1 (deck maps are isometries of the pullback metric) is
  standard and correctly argued; Step 2 (descent: a deck-invariant
  orientation orients the base, contradiction) is complete and correct — the
  cell rightly flags that orientation-reversal of the deck involution is
  *not* definitional; Step 3 correctly confines Mostow-Prasad to
  metric-independence. Remark 2 (Steps 1-2 are dimension-free) is right.
- Corollary B: the two-line 2-torsion argument is correct; the 2-torsion
  subgroup of R/(1/2)Z is indeed {0, 1/4}.
- Gieseking sanity claim re-verified independently: the orientation cover of
  NonorientableCuspedCensus[0] (m000, Gieseking) `is_isometric_to(m004)` =
  True, `is_isometric_to(m003)` = False.
- Volume doubling: 0/40 violations of vol(cover) = 2·vol(base) at 1e-9 in the
  checked-in results.json (and in my identical re-run).
- Side-claim m009 = -1/48, m010 = 11/48: exact (48·CS = -1.0 and 11.0 to
  machine precision).

## 5. Gate 5

Both scripts and both documents contain only mathematical constants (0.25,
0.5, 1e-9) and census names. No measured Standard Model value appears in any
object-side computation. `git status` is clean — nothing outside the cell
directory was modified by the cell (this VERIFICATION.md is the verifier's
own addition to the cell directory, as mandated).

## 6. Scope attack

- FINDINGS.md claims match the data everywhere I checked (all summary
  numbers, the full control table, the anchor values, the 120-cover scan).
- The one place where over-claiming was possible — the degenerate {0: 40}
  distribution — is handled correctly: banked as Conjecture C, explicitly
  labeled "observed, NOT proved", with the correct observation that
  Corollary B cannot yield it and with a typed kill condition (one cover at
  1/4). The FINDINGS explicitly warns the record *not* to cite the cover
  census as evidence that 1/4 occurs for covers. No scope violation found.
- Caveats section honestly names the two real epistemic dependencies
  (SnapPy canonical-cell certification; quad-double numerics treated as
  exact). Both are acceptable and correctly typed.

## Residual (non-blocking) notes

- All numerics remain modulo SnapPy's canonical-decomposition and Zickert-CS
  code being correct; the cell says so. The controls' chirality is now
  additionally certified by CS mirror-oddness (item 2 above), which is
  independent of the symmetry-group code path.
- `is_full_group()` certifies the symmetry group of the *canonical
  triangulation*; the bridge to the isometry group is rigorous for these
  cusped census manifolds and is the community-standard certificate — noted,
  not held against the cell.

## What was attacked and survived

Re-ran both scripts (exact match, byte-level on JSON); attacked the bite
control (real, ran, bites at 7 orders of magnitude); attacked conventions
(mod-1/2 and mirror-oddness verified numerically, sheet-swap invariance
checked); attacked the theorem text (no gaps found); attacked scope (the one
dangerous datum is correctly conjecturized, not claimed); checked Gate 5 and
the no-outside-writes claim (git clean). Nothing was refuted; nothing
required degradation.
