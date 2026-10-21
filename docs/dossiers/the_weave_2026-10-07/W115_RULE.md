# W115 — the leptons at the shared τ: does the modulus the quarks pin predict the charged leptons? (the rule, committed before the code)

The SM-derivation seat, 2026-10-21. Committed before the script that reads it exists. Nothing here is a result.

## Why

- **The owner's choice** (2026-10-21), after W114: the leptons at the shared τ.
- **What W114 left.** θ̄ = 0 at every τ and the observed quarks coexist in the record's frame only where the fit has no
  degree of freedom. Assignments 11, 13 and 16 fit exactly, and 14 is compatible (χ² = 2.55).
- **The idea.** τ is one modulus for every sector. A zero-dof quark fit pins it, up to its discrete solutions. The
  charged leptons, coupled at that same τ with fewer free numbers than ratios, then make a prediction the quarks
  cannot.
- **What would count.** One unfitted ratio confirmed, with the look-elsewhere count stated and a null that random
  targets fail. A fit alone would not count.

## Weave or thread

**WEAVE-type, given the frame.**
- Every compatible zero-dof quark assignment is taken, every quark solution the stated search finds, and every lepton
  coupling the record allows, with none hand-picked.
- The shared τ is the weave's one modulus, common to every sector.

## The frame

W114's, unchanged: W101's hypotheses, CP in the law (GENESIS GM5c, OPEN), the Dedekind counterterm, tree level, the
ruled branch's holomorphic couplings. The leptons are the charged leptons only. Neutrinos would need a choice of
their masses' origin, so they are out of scope.

## The lepton census, by hand (to be checked)

- **A charged-lepton sector** has hands (s_L, s_e) and a coupling weight k. Its space is one of W113's types, and its
  real coefficients modulo scale leave d − 1 free numbers for two ratios, m_e/m_μ and m_μ/m_τ.
- **A prediction needs d ≤ 2.**
  - **d = 1:** T⊗T at k = 1 (B1636's sum rule, m₂/m₁ ≥ ½, against m_μ/m_τ = 0.059); T̄⊗T̄ at k = 1 (det ≡ 0, so
    m_e = 0); mixed at k = 0 (the identity, so degenerate). All three are excluded by the data's qualitative facts.
  - **d = 2:** T⊗T at k = 3, and mixed at k = 2 in either order. The two orders are transposes, with the same masses,
    so they count as one. These two couplings carry one free number each, and so one prediction.
  - **d ≥ 3:** no prediction.
- **By the dimension tables** (B1635; W113 F1), T⊗T has 1, 2, 4, 5, … at k = 1, 3, 5, 7; mixed 1, 2, 4, 5, … at
  k = 0, 2, 4, 6; T̄⊗T̄ 1, 3, 4, 6. So the two predictive couplings are the only ones up to weight 7. The run checks the
  tables' growth there; beyond weight 7 it rests on the tables.
- **No constraint ties the lepton hands to the quark hands** in this frame. W101's gravity condition binds only if
  the moves are gauged, and the compatible quark assignments are not anomaly-free anyway.

## The quark solutions (fixed now)

- **The assignments.** 11, 13 and 14, with W114's parametrization and data. Assignment 16 has −2 dof, so its exact
  fits form a family along which τ moves. It pins nothing and is left out.
- **The search for every solution** (seed 115):
  - per assignment, 60 000 random points;
  - Nelder–Mead from the best 120 (at most 8000 evaluations each), plus one start at W114's best point.
- **A solution** is an endpoint with χ²_q ≤ 10⁻⁶ for 11 and 13, or ≤ 3.84 for 14 (compatible only). Solutions are
  distinct when their τ in F differ by more than 10⁻³.
- **Scope.** A zero-dof system can have more solutions than any search finds. The test covers the ones found, and
  the run reports how many.

## The tests (fixed now)

**The data.** HZ2021 at M_Z, as W66 reads it: m_e/m_μ = 0.004747 and m_μ/m_τ = 0.05887, with relative errors in
quadrature and W66's allowance a = 0.10. The pass mark is 3.84, the 95% point of χ² with one degree of freedom.

**T1, pinned.** At each quark solution's τ, and for each predictive lepton coupling, the free angle φ ∈ [0, π) is
scanned on 40 000 points and refined. The read-out is χ²_ℓ,min, together with the predicted m_e/m_μ wherever φ fits
m_μ/m_τ exactly.

**T2, joint.** For each assignment and lepton coupling, the quarks and leptons are fitted together, with τ free.
- There are 10 observables and 9 effective parameters, so 1 dof.
- The starts are every quark solution with the best φ of T1, each refined by Nelder–Mead (at most 12 000
  evaluations).
- The read-out is the joint χ²_min.

**T3, the null.** It is computed for every combination, whatever T1 and T2 give.
- 4000 synthetic lepton targets, each ratio drawn log-uniformly within a decade of the data, from seed 1150.
- For each target, the family's best pinned χ²_ℓ,min is taken over every combination.
- p is the fraction of targets whose family-best is at or below the data's family-best.
- So the look-elsewhere count is built in: the number of combinations is the number of quark solutions times two.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| V0 | the control: lepton data synthesised by mixed at 2, at one quark solution's τ and a random angle, is recovered by T1 to χ² ≤ 10⁻⁶ and by T2 to χ² ≤ 0.01 | 85% |
| V1 | the census: up to weight 7 the only couplings with d ≤ 2 are T⊗T at 1 and 3, T̄⊗T̄ at 1, and mixed at 0 and 2; at the quark solutions' τ the three with d = 1 fail as stated (m₂/m₁ ≥ ½; m_e = 0; degenerate) | 95% |
| V2 | W114's best point is recovered as a solution for 11 and 13; read-out: the number of distinct solutions per assignment and their τ | 95% |
| V3 | no combination passes T1 (pinned χ²_ℓ,min ≤ 3.84) | 80% |
| V4 | no combination passes T2 (joint χ²_min ≤ 3.84) | 75% |
| V5 | the null: p ≥ 0.05, so whatever T1 gives is not special | 85% |

## What the outcomes mean (fixed now)

- **V3 and V4 hold.** At the τ the quarks pin, no lepton coupling with a free number to spare reproduces the charged
  leptons. The shared modulus predicts nothing in this frame. A clean negative.
- **V4 fails, but V5 holds** (p ≥ 0.05). The leptons fit at one free number, but random targets are fitted as often.
  That is no evidence, as in W112.
- **V4 fails, and V5 fails** (p < 0.05). The modulus the quarks pin predicts the charged-lepton ratios better than
  chance, with one free number for two ratios.
  - That would be the frame's first unfitted, confirmed value: a candidate for the first of the nineteen.
  - It goes to main for an independent check. The count stays 0 until main banks it.
- **In every case the quark side carries the Standard Model's own count with θ̄ tuned** (W114). Only a lepton
  prediction could change that.

## Seen before the rule (disclosed)

- W114's whole record: the sixteen fits, the four compatible ones, their best points and τ, and their J.
- The lepton data was read from `received/HZ2021_running_masses_MZ.json` to write the ratios above.
- No lepton coupling has been evaluated at any τ by this seat in this project, and no lepton fit has been run.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read.
- A failed launch is disclosed, with its log kept. Any failed prediction is recorded as failed, and any later check is
  labelled post hoc.

0 of 19.
