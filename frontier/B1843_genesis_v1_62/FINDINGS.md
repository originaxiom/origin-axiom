# B1843 — GENESIS v1.62: THE JOINT CONFIRMATION (the owner's ruling on the SM seat's §§ 351–352)

*cc (main), 2026-11-05. Adopted before B1839's look was read.*

## The ruling

**The ruling, quoted:** the owner, 2026-11-05: "if you also agree with sm about the rule, i aprove it". Main agreed with the
SM seat's recommendation (option B, with option D as a valve), under three conditions:
- the change is made through this amendment;
- main verifies the statistic first;
- the claim's wording is fixed now.

**Why the rule changes.** GENESIS v1.60 GAP1's conditions 3 and 4 graded each held-out target alone, at p_V < 0.01/m_V. At
the screen's own 10% theory allowance, a correct frame almost never meets that.

**The budget.** The SM seat's §351 budget and main's own arithmetic give the same figures, with I(B) = log₂(W ln 10 / 2B):
- y_b/y_t carries about 5.5 bits and r about 4.5;
- the need is log₂(100·m_V), 10.3 bits at m_V = 13.
- So a fail under v1.60 would carry almost no information, and it would spend y_b/y_t, which can be used once.

## The change (adoption/amend.py; received/GENESIS_v1_61_main.md pinned by sha256)

- **Condition 3, graded jointly.**
  - Each target's measured value lies inside its 68% band.
  - The joint p_V is below 0.01/m_V in its 97.5% upper end. It is the rank, among the matched null's worlds, of the product
    of the targets' marginal rank p-values. Null worlds use leave-one-out ranks, ties count against the frame, and the data
    is counted in the null.
  - m_V counts every prior look recorded in LOOK_LEDGER, sealed or unsealed, across seats. This is the stricter of the two
    readings and main's standing practice; it is fixed now so that it cannot be chosen later.
- **Condition 4:** the targets "pass jointly". The claim reads "jointly confirmed, each within its band".
- **Condition 7 (new), worth spending.** Before any measured value is opened, main computes the card's power from the
  matched null's predictions alone, their spread and never their location. Below 10% power for a frame whose true error is
  5%, the targets are held unspent.
- **Also updated:** FK9's v1.61 sentence, docs/THE_BAR.md's level 2, and THE_FINAL_ACTS_BAR's V (by an appended dated block).

## Verified by main

- **The calibration.** `verification/joint_pv_calibration.py` is main's own implementation, with its own seed and sizes.
  Under exchangeability the joint p's rate at α = 0.01 is:
  - 1.02% for two independent targets;
  - 0.97% at ρ = 0.9;
  - 0.83% for three targets.

  All are within sampling error of 1%. This agrees with the SM seat's 0.93% and 0.90%. The naive rectangle, both
  marginals at once, runs at 5.1–5.6%, which is why it is not used.
- **m_V for the y_b/y_t-and-r card, from LOOK_LEDGER (S305h):**
  - y_b/y_t: 7 prior looks (8 if B1129's 22 numbers include it);
  - r: 2–3;
  - so m_V ≈ 12–13.
- **The fit with THE_FINAL_ACTS_BAR.** KIND_TABLE's admission, CROSSING_REQUIREMENTS and each target's band stay per
  target. Only PASSED changes.
- **Feasibility.** B1839's channel norms are sector-blind, so each row's prediction is one precompute over all rows. Each
  null world then re-chooses its best row with the existing null machinery. It is not 10⁵ separate frame evaluations.

## Disclosed

- **Adopted before any confirmation card exists, and before B1839's look is read.** B1839's census is complete; its look
  ran and its output is committed unread.
- **At m_V ≈ 13 and the 10% allowance, even the joint form falls about 0.3 bits short.** Condition 7 will hold the
  targets unless the frame's computed theory error beats the allowance. A computed σ_th is the work that would make a
  confirmation decisive.

## Seen first

- **Read for this amendment:**
  - B1828 (v1.60, GAP1's rule);
  - B1829 (v1.61, the two-level bar);
  - B1798 (the matched null);
  - P-611 (the information budget);
  - P-597 (one target short);
  - the SM seat's §§ 349–352 on its branch;
  - LOOK_LEDGER.
- `VERDICT topic-sweep /joint p|joint test|per-target|Fisher|combined p/`: the record's prior combination is THE_BAR's per-cell
  Bonferroni; no joint p_V rule existed.
