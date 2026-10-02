# B1518 — THE BAR: what a positive on a generated state must beat, fixed before the next match and run on main's class-index census. No criterion in the fibre torsion and the monodromy's sign decides which states carry a generation at their own level, though the fibre torsion predicts it strongly

cc (the SM-derivation seat), 2026-10-02. Sealed at `697217be` before any outcome was cross-tabulated (`PREREGISTRATION.md`,
sha-256 `76bd91e0…`, SEAL_LEDGER). The run took 17.6 s. **Verdict: PROVED.** The bar is fixed, and its null model was run as
sealed on main's B1439 census: **P1, P2 and P3 YES; P4 NO.** The priors expected 2.9 of 4 to come true, and 3 did.

P1 rests on main's records, so after the run every manifold of every mixed stratum (52 of them) was recomputed by an
independent route, which reproduces main's count on all 52 and on the three banked identities. **Prior work: EXTENDS** (§6).
**0 of 19 stays 0.**

## 0. What was found

- **The bar** (§2). A positive on a generated state is graded in five steps:
  1. a card;
  2. the frame's base rate in a named unit;
  3. its comparable objects, through the upper exact 95% limit of their rate;
  4. how the state was chosen, and every look;
  5. B614's gate at 0.01.

  The grades are WHAT_WOULD_COUNT's DERIVED, REPRODUCED and FITTED, plus UNJUDGED for a frame that has no population run.
- **No criterion in the fibre torsion with the monodromy's action decides own-level firing** (P1). Twenty-two (G, sign) strata
  each hold a firing and a silent manifold. The smallest witness pair is:
  - **m369 = −LLRLR**, which carries 8 generation-shaped backgrounds;
  - **o9_00001 = −LLLLLLLLR = −L⁸R**, which carries none.

  Both have H₁ = ℤ/12 ⊕ ℤ, the same sign and the same trace (10). Both are reversal-closed, have symmetry order 4 and are chiral.
  Two independent codes agree on both counts. So main's "no criterion found" (B1439) becomes **"none exists"** for any criterion
  that is a function of the fibre torsion group, the sign, the trace, the symmetry order or the reversal class. Fifteen strata
  stay mixed with the symmetry order added (P2).
- **The fibre torsion predicts own-level firing strongly** (P3). The leave-one-out AUC of the fibre-torsion strata is **0.858**,
  against a permutation null with median 0.498 and 99th percentile 0.602 (Šidák-corrected p = 0.001). It predicts the hit but
  does not decide it.
- **Reversal symmetry is not established beyond the fibre torsion and the sign** (P4 NO).
  - The unconditional split is 79 of 314 reversal-closed manifolds against 8 of 222 paired ones.
  - Inside the 32 strata that hold both classes, 6 of 36 closed manifolds fire and 0 of 34 paired ones do.
  - The conditional test gives a one-sided p = 0.011, or 0.022 after the trials factor. That is above B614's gate. With 70
    manifolds the test has little power: the reading is "not established", not "no effect".
- **The record's positives, graded** (§3.5). The root's tower is REPRODUCED at every level where it fires. m369, s639 and the
  census's other carriers were found by scanning, so each would be FITTED if presented as evidence; main presents none of them.
  The harmonic frame's counts are UNJUDGED.

## 1. The question

GENESIS GAP4 states that with hundreds of states, frames, levels and ends, a Standard-Model-like feature somewhere is expected by
chance. sL-9 item 1 asks for the bar first: a selection rule and a null model fixed before any further match counts. The record
held the pieces, but none said what a positive on one generated state must beat. Main's census (B1439) is the one frame with a
population. Its own question, L229 (i), "the own-level law", had "data and no law".

## 2. The bar (PREREGISTRATION §3, sealed)

A positive reads: frame F, on state s, shows feature X.
1. **The card.** F; X with its defining line; the population P; the unit (word state, manifold or level-manifold; B1517); and
   how s was chosen, by a rule fixed before computing or by scanning for X.
2. **The base rate.** X's rate in P, in the unit, with its exact 95% interval. If F has not been run on a population, the
   positive is **UNJUDGED**.
3. **The comparable objects.** r is the upper end of the exact 95% interval for X's rate among the other units of s's stratum.
   For the class-index frame the stratum is (d1, d2, sign, reversal class). A lone unit gets r = 1, and no size threshold is
   set.
4. **Selection and trials.** For a fixed rule, p = r. For a scan of n units, p = 1 − (1 − r_P)ⁿ. Then Šidák over every look.
5. **The gate.** p < 0.01 (B614 G3).

The grades are **DERIVED** (a fixed rule, and the gate passed), **REPRODUCED** (comparable objects make it unremarkable),
**FITTED** (found by scanning, and the gate failed) and **UNJUDGED**. The standing text is `docs/THE_BAR.md`.

## 3. The run (`verification/bar_run.py --write` → `bar_run.json`)

### 3.1 The banked identities and controls

All pass:
- **C1.** Main's 93 listed carriers plus B1434's two are exactly the 95 own-level records with a background.
- **C2a.** No own-level manifold is split (B1517 C5 reproduced).
- **C2b.** No level-manifold at k ≥ 2 is split. Main's counts do not depend on the deck labelling a level.
- **C3.** The instrument's ten planted controls.
- **C4.** The covariate controls.
- **C5.** The eight planted dry-run controls, re-run inside the sealed run.

### 3.2 Readings

| reading | value |
|---|---|
| R1 base rate, word states | 95 of 758 = 12.5 % (exact 95 %: 10.3–15.1 %) |
| R1 base rate, manifolds | **87 of 536 = 16.2 %** (13.2–19.6 %); no manifold split |
| R2 by word length, manifolds (2 … 12) | 0/2, 0/2, 0/4, 1/6, 1/10, 3/16, 5/28, 10/42, 15/78, 24/124, 28/224 |
| R2 smallest firing fibre torsion | 12; the 27 manifolds with smaller torsion are all silent |
| R3 level-manifolds by k (1 … 7) | 87/536, **50/79**, 25/32, 5/5, 3/4, 1/1, 2/2 (main's records: 95/758, 100/180, 25/32, 10/10, 3/4, 2/2, 2/2) |
| R4 a scan finds a carrier, at 16.2 % | 0.986 for B1434's 24 manifolds; 1.000 for the 536 |
| R5 amphichiral (descriptive) | 8 of 66 amphichiral against 79 of 470 chiral |
| R6 the bar's strata | 454 strata of (d1, d2, sign, reversal class), 70 of them with two or more manifolds |

### 3.3 Decided at design time, checked

- **D1** (main's B1442 lemma): three level-manifolds have exponent at most 2, and none carries a background.
- **D2:** the root's own level is silent.
- **D3** (the root's tower against the other level-manifolds at the same k):

| k | the root | the others firing |
|---|---|---|
| 2 | **silent** | 50 of 78 |
| 3 | 48 backgrounds | 24 of 31 |
| 4 | 256 | 4 of 4 |
| 5 | 400 | 2 of 3 |
| 6 | 2 160 | none in range |
| 7 | 3 136 | 1 of 1 |

D3 holds: wherever the root fires and two or more others exist, half or more of them fire. At k = 2 the root is silent where most
others fire. This is a reading, reported and not decided.

### 3.4 Tests and the sealed predictions

| | test | result | prediction | prior | outcome |
|---|---|---|---|---|---|
| T1 | mixed strata: S1 (G), S2 (G, sign), S3 (+ symmetry order) | 21 (72 manifolds), **22 (52)**, 15 (36) | P1: some S2 stratum mixed | 85% | **YES** |
| | | | P2: some S3 stratum mixed | 75% | **YES** |
| T2 | leave-one-out AUC under S1, S2, S3 | **0.858**, 0.554, 0.546; S1 against its null: median 0.498, q99 0.602, p = 1/2001 | P3: beyond chance, Šidák p < 0.01 | 85% | **YES** (0.001) |
| T3 | reversal class given S2 | unconditional 79/314 vs 8/222; Mantel–Haenszel OR = ∞ over 32 strata; permutation: 79 observed, 75.85 expected, p = 0.0108 | P4: OR > 1 and Šidák p < 0.01 | 45% | **NO** (0.0216) |

The AUC under S2 and S3 is low because most of their strata are single manifolds (F3), not because those covariates carry less
information.

### 3.5 The bar applied to the record's positives (post-run, `post_run_checks.py` Q5)

| positive | chosen by | p | grade |
|---|---|---|---|
| m369 and s639 carry a generation at their own level (main B1434) | a scan of 24 manifolds | 1 − (1 − 0.162)²⁴ = 0.986 | FITTED if presented as evidence; main does not ("nothing in this census selects m369 or s639") |
| the 87 own-level carriers and the fourteen complete states (main B1439) | the census | ≈ 1 | a base rate, not a positive ("nothing selects a state") |
| the root's level 3, 4, 5, 7 carries backgrounds | GENESIS T-ROOT (a fixed rule) | r = 0.904, 1.000, 0.992, 1.000 | **REPRODUCED** |
| the root's level 6 | GENESIS T-ROOT | r = 1 (no other level-manifold at k = 6 in range) | no credit |
| B1509–B1515's counts on m004's family; R40 on m010 | — | no population run in the harmonic frame | **UNJUDGED** |

## 4. Post-run checks (`verification/post_run_checks.py` → `post_run_checks.json`, 46 s)

These are not sealed. They were run after `bar_run.json` was written and change no prediction.
- **Q2, the independent route** (NO NEGATIVE FROM A BUG). P1 rests on main's records, so the own-level census was recomputed
  with code that shares only definitions with main's:
  - the characters by brute force;
  - the slope u(μ)/u(λ) by solving both relators' Fox-calculus cocycle system mod p, with the coboundaries removed. Main uses
    one relator in a fixed gauge;
  - two primes ≡ 1 mod N above 3·10⁹;
  - every (θ, ψ_Y, W) enumerated directly.

  It reproduces the banked identities (m004 0, m369 8, s639 16; B1434 (a)). It agrees with main's background count on all 52
  manifolds of the 22 mixed strata, with no slope coincidence at one prime only.
- **Q3, the witness pair,** identified with SnapPy 3.3.2: **m369** (−LLRLR, volume 4.7517) and **o9_00001** (−L⁸R, volume
  3.4762). Both have H₁ = ℤ/12 ⊕ ℤ and tr A = 10. Their counts are 8 and 0.
- **Q4.** Inside the 32 strata that hold both reversal classes, closed manifolds fire 6 of 36 times and paired ones 0 of 34.
- **Q5** is §3.5.

## 5. What it means, and what it does not

- **For the own-level law (main's L229 (i)).** The hit is not a function of (G, sign), so it is not a function of anything
  those determine: |G|, the exponent, 3 | |G|, non-cyclicity, or the trace (F2). Nor is it a function of the symmetry order or
  the reversal class, since the witness pair shares those too. A law must read the word beyond its trace: within a trace, the
  conjugacy class (by Latimer–MacDuffee, an ideal class). B1438's Theorem D, slopes summed letter by letter, is where such a law
  would live. G still predicts the hit strongly (AUC 0.86), and the exponent-two lemma and the 27 silent manifolds of torsion
  below 12 are part of that.
- **For the bar.** A positive in the class-index frame must now beat its stratum's rate. At the own level that rate is 16.2 %
  per manifold overall, and higher in the strata where G concentrates the hits. A carrier found by scanning has p ≈ 1. The root,
  the one state the genesis chooses (GENESIS T-ROOT), carries nothing at its own level or at level 2, and its higher levels fire like
  their neighbours.
- **For reversal symmetry.** The enrichment B1517 saw is mostly carried by the fibre torsion. What is left (6 against 0 inside
  the comparable strata) does not pass the gate. A longer census would have the power to decide it.
- **Not claimed:**
  - that any state is physical;
  - any physics;
  - that the bar is complete for frames without a population run;
  - anything beyond length 12 or main's frame (its trivial-character convention included).

  The bar is this seat's proposal; the owner may amend it.

## 6. Prior work

Standing **EXTENDS**; the record is in `arc_verdict.json`.
- **The repo,** 9 heads swept on 2026-10-02 (main @ 637561d3, the audit lane @ e4bb7f68). What this arc extends:
  - the emergence bar's CONTROLLED;
  - WHAT_WOULD_COUNT's grades;
  - B614's gate;
  - INPUT_COMPLETENESS rows 7–8;
  - E20 and E61, made one procedure for positives on generated states;
  - main's B1439, from "no criterion found" (two covariates looked at) to "none exists in (G, sign)", with a witness verified by
    two codes;
  - main's B1434 (b) comparable-object reading of the root's tower, reproduced by manifold;
  - main's B1442 lemma, checked on the census.

  "trials factor" was absent from every head. "Mantel" appeared only in this arc.
- **The literature:** PREREGISTRATION §5.2.
  - Gross–Vitells, for trial factors.
  - The landscape statistics. They impose three generations as a filter (the heterotic scans) or multiply suppression factors
    (Gmeiner et al.); Dienes–Lennek's floating correlations are the sampling-measure point that B1517's unit is.
  - Rivin, for H₁ of punctured-torus bundles.
  - Latimer–MacDuffee, for what a same-trace stratum holds.

  No source read runs a null model on a census of punctured-torus bundles for a frame's feature.

## 7. Errors caught, and registered

- **A design slip,** caught before the seal (ERROR_LEDGER rule slip). A draft prediction, "the root's tower is typical", was
  decided by main's published level table and had been argued by main's B1434 (b). It became D3, cited. Four cited line ranges
  were corrected before the hash.
- **A post-run slip, caught on first use.** The independent route used sympy's gcd, whose integer type `pow` refused. It was
  fixed (`math.gcd`) before any count was read.
- **A seal-time slip, found at the bank** (ERROR_LEDGER rule slip). The seal-time tests were chosen by the files they
  name, which missed `tests/test_b1516_genesis_v1.py`. That test scans every markdown file for GENESIS labels used without
  the word, and the sealed §6.1 wrote "(T-ROOT)" bare. The sealed file stays as hashed. The lock now exempts a
  preregistration whose current sha-256 is in SEAL_LEDGER, and FINDINGS names GENESIS beside the label.
- **Registered:**
  1. **GENESIS v1.2** (the next arc): GAP4 points to THE BAR; with R78's signed powers and B1517's miss there, the eighteen main
     records main's relay names, and main's same-day rule reconciled.
  2. **The own-level law,** asked of the word: does the slope spectrum (B1438 Theorem D) decide firing? m369 and o9_00001 are
     the first pair to explain.
  3. **The root at k = 2:** silent where 50 of 78 level-manifolds fire.
  4. **Reversal symmetry with power:** the census to length 14 or more.
  5. **The harmonic frame's population run,** without which its positives stay UNJUDGED (sL-9 item 2).

## 8. Verification

| file | role |
|---|---|
| `PREREGISTRATION.md`, `ARTIFACT_HASHES.txt` | the seal (sha-256 of the preregistration and of every sealed file) |
| `verification/covariates.py`, `level_covariates.py`, `design_checks.py` and their `.json` | design time, no outcome read |
| `verification/null_model.py` | the instrument (`--selftest`: ten planted controls) |
| `verification/bar_run.py` → `bar_run.json` | the sealed run (`--dry`: eight planted controls) |
| `verification/post_run_checks.py` → `post_run_checks.json` | the independent route and the post-run readings |
| `verification/main_B1439_firing_own_states.json`, `main_B1439_levels.json` | main's records, quoted with source and sha |

Lock: `tests/test_b1518_the_bar.py`.
