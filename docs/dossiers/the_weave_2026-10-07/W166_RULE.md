# W166 — the plan's stage 3, the Higgs from the same action: each doublet is the response of the matter's induced quadratic form to the record's DR, H = K⁻¹·DR, frozen by hash before any score, then scored on the nine at W158's 38 strip rows (the rule, committed before the script)

The SM-derivation seat, 2026-10-28. Committed and pushed before the script that reads it exists. Nothing here is a
result.

## Why

- **The plan's stage 3** (`THE_NINETEEN_PLAN_2026-10-27.md`, adopted by the owner; the owner's "agreed continue do them
  all"). Derive the quadratic form and the source behind the inverse Gram from the frame's own action. Use no recipe
  menu. Freeze the vector by hash before any score. Run at the strip first, as a frame result labelled so.
- **What W161 left.** B1762's recipes reproduce exactly but pass nowhere (least 25.4). Two of its numbers carry the
  signal:
  - its down Higgs, an inverse Gram applied to the record's DR, lies within about 1° of DR's forced orbit;
  - its up Higgs is DR with the i-component boosted by about 2, the same at every point.
  Neither number was derived. This arc states one principle that would give both, and tests it once.

## The principle (fixed now)

- **The coupling.** A doublet h ∈ ℂ³ (components i, j, k, as the record writes DR) couples to sector s through the
  frame's Yukawa map Y_s(h). This is W158's basis coupling, in the reading the row's six were found with. The map is
  linear in h for the reading S and in h̄ for S̃.
- **The induced form.** Integrating the matter out at one loop gives each doublet the quadratic form
  K(h) = Σ_s N_s ‖Y_s(h)‖²_F, over the sectors s that the doublet couples to, times one common logarithm. Here
  ‖Y_s(h)‖²_F = h†K_s h, and K_s is the Hermitian form of the reading:
  - for S, K_s = G_s with G_cd = tr(B_c†B_d);
  - for S̃, K_s = conj(G̃_s), with G̃ built the same way from the S̃ basis.

  This is the standard fermion-loop (NJL and composite-Higgs) kinetic term. N_s is the colour multiplicity: 3 for up
  and down, 1 for leptons.
- **The source.** The record's own Higgs, DR at τ (W158's `higgs_DR`), with the unit metric: the doublet that the
  record writes when the matter is ignored.
- **Compositeness.** The doublet's bare form is dropped against the induced one. Stationarity of h†Kh − 2 Re(DR†h)
  gives **H = K⁻¹·DR**, with no free number.
  - The answer is covariant under conjugating the variable: it is the same whichever of h or h̄ the reading treats as
    linear.
  - Only H's direction enters the nine.
- **The doublets: type II, as in W158's two-object route.** H_u couples to the up sector, H_d to the down and lepton
  sectors.
  - **H_u = K_up⁻¹·DR**, with the colour factor dropping out of the direction.
  - **H_d = (3K_down + K_lep)⁻¹·DR.**
- **The couplings are the frame's raw ones:** the same M (W138's residues, norms and weighted M) that the six use, with
  no normalisation per sector. Each coefficient is either forced (the colour 3, the type II assignment of W158's
  route) or computed in the same frame (the sector scales).
- **The readings and c** are each row's own: those with which the row's six pass the bar with DR. Read from W156's and
  W157's committed outputs, all 38 rows use (S̃, S, S), c = 3, on L_max.
- **The score:** χ²_nine (W158's: the six ratios with c = 3 and log ∣V_us∣, ∣V_cb∣, ∣V_ub∣; the data's error bars) at
  each of W158's 38 strip rows. The bar is 21.67. J is a read-out.

## The objects

- **The rows:** the 38 strip rows (line, Re τ, Im τ, horocycle), read in part V from W156's and W157's committed
  outputs. No target file is read in part V.
- **The instrument:** W158's module (`the_two_special_higgs.py`) and W161's (`the_recipes_priced.py`), loaded
  unchanged, with W157's, W152's, W138's and W142's under them.
- **The four points** of B1757 (W161's POINTS), for read-outs. B1757's fitted doublets and χ²_nine come from the agy
  branch's committed JSON (W161's blob at 05e6caabf) and are read in part S only.

## Two parts, each run once

- **Part V, the vectors (blind).** It reads no target file: not the masses, not the CKM, not B1757's fits.
  - At each of the 38 rows: the forms K_up, K_down, K_lep; their condition numbers; the rule's (H_u, H_d); and every
    table entry's pair (below).
  - At the four points: the same, plus B1762's recipe pairs and boost (W161's `recipes`, which is target-free).
  - It writes the_higgs_from_the_action_vectors.json, with the sha256 of its canonical vector block.
  - That output is committed before part S runs.
- **Part S, the score.**
  - It reads the committed vectors file by its git blob, checks the bytes against the working file and the hash, and
    recomputes the vectors to 10⁻¹² (determinism).
  - It then loads the targets and scores. It computes nothing that feeds back into a vector.

## The sensitivity table (charter iii; every literal in the chain, one at a time; read-outs, never a pass)

| entry | change from the rule |
| --- | --- |
| T1–T3 | colour N_c = 1, 2, 4 in H_d's form (H_u's direction does not depend on it) |
| T4–T6 | lepton weight r = 0, 1/3, 3 in 3K_down + r K_lep |
| T7 | each sector's form normalised to unit trace before weighting |
| T8–T11 | partial compositeness: H = (1 + κK̂)⁻¹·DR, K̂ = 3K/tr K, for κ = 0, 0.1, 1, 10; κ = 0 is the record's own DR, as in W159's identity pair |
| T12 | one doublet: H_u = H_d = (3K_up + 3K_down + K_lep)⁻¹·DR |
| T13 | c = 1 in the score (the vectors unchanged) |

## Weave or thread

**A frame result on one line class, at 38 rows that the data's six chose.** The producer is a function of frame
quantities at a given τ and line; the rows are not. Charter (v) is not met, so nothing here is counted toward the 19.
It is labelled a thread-and-frame result. Stage 5 would evaluate the producer at a weave state.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| K0 | **The instrument.** The pins hold. The 38 rows rebuilt from the census with the data's six equal those read from W156's and W157's outputs, with their configuration. At every row, for three random h per sector and reading, ‖Y_s(h)‖²_F = h†K_s h to 10⁻¹² relative. The record's DR at (S̃, S, S), c = 3 gives each row's stored χ²_six to 10⁻⁶ relative | 95% |
| K1 | **The vectors, frozen and blind.** Part V reads no target file. Every K_up and 3K_down + K_lep is positive definite at every row, with condition number below 10¹⁰. The frozen hash matches in part S. Part S's recomputation agrees to 10⁻¹², before and after the targets are loaded and under three moved targets (three null draws in place of the data). This is the counterfactual, charter (ii); at fixed rows it holds by construction, since no target reaches the producer | 93% |
| K2 | **The score.** At some one of the 38 rows, the rule's (H_u, H_d) gives χ²_nine below 21.67 | 10% |
| K3 | **Specificity** (decisive only if K2 holds). The least χ²_nine over the 38 rows is reached by at most 1% of targets under each null, with seeds 1929–1948: (a) the data's six with random mixings, and (b) random nines (W161's nulls on own draws) | 50% given K2 |
| K4 | **B1762's boost is the inverse up form.** At each of the four points, β = (∣H_u,i∣/‖H_u,jk‖)/(∣DR_i∣/‖DR_jk‖) for the rule's H_u is within 10% of B1762's boost (W161's `recipes`, 1.977–1.983) | 45% |
| R | **Read-outs** (no predictions): per row χ²_nine, its six and CKM parts, and J's pull; the angles of H_u and H_d to DR and to each other; the 1 ⊕ 2 block of K_up; the raw trace ratio tr K_lep / tr K_down; the table's least and median per entry; the whole table priced by the same nulls; at the four points, χ²_nine against B1757's 19.08, 4.05, 29.17, 2.75, and the angles between the rule's coupling matrices and B1757's fitted ones and B1762's, per sector, taken as vectors in ℂ⁹ so that no reading convention enters | — |

## What the outcomes mean (fixed now)

- **K2 and K3 hold:** a Higgs pair from a stated principle, with no free number past the frame's, reaches the nine's
  bar at the strip and is specific. It is still a frame result at data-chosen rows and is not counted. It is carried
  to stage 5 as the stage-3 producer, unchanged.
- **K2 holds and K3 fails:** it reaches the bar but is not specific. This is a READING, and stage 5 runs with the
  failure stated.
- **K2 fails:** the principle as stated does not give the nine at the strip. The read-outs locate the miss.
  - No table entry is promoted. One below 21.67 is a priced read-out and a new look; it would need its own rule.
  - Stage 3 then reads "the Higgs's quadratic form is not the induced one alone", and the blocker stays open.
- **K4 holds:** B1762's fitted boost is the up sector's inverse form, so one of its numbers is explained. **K4 fails:**
  it is not.

## Pre-mortem

The likeliest failure is the mixing. Both doublets are deformations of the same DR, while B1757's fitted doublets sit
near two different images in DR's orbit (W161: H_u 2.6°–4.3°, H_d 1.0°–3.7° from the nearest images). If the
inverse forms move DR by less than the angle between those images, the CKM stays near the record's own, which W159
found at χ²_nine 315 or more.

## What stays out

- The three Yukawa scales, θ̄, the state (τ and the line), any other line or horocycle, and any fit.
- Any change of reading or c per row.
- Any refit of K, the source or the weights after part V.

## Looks (charter viii)

Fourteen looks at the nine at the strip (the rule and T1–T13), and four at B1757's points: eighteen, all targeting
the nine. They are entered in the look ledger with the record.

## Seen before the rule (disclosed)

- **This seat's own results:** W158, W159 and W161. They include B1762's recipes and numbers, B1757's χ²_nine at the
  four points, and its fitted doublets' angles to DR's orbit.
- **Read for this rule:** the 38 rows' configuration, from W156's and W157's committed outputs: all (S̃, S, S), c = 3,
  L_max.
- **Reasoning before the rule, not computation.** If the up form's 2-block acts as a scalar on DR's (j, k) part, the
  rule's H_u reproduces B1762's boost up to the factor ‖DR_jk‖²/‖DR‖². That is K4's prediction.
- **Not computed:** no K_s, no rule vector and no score. No script exists.

## Discipline

- This rule is committed and pushed before the script exists.
- The script is committed before part V runs.
- Each part runs once. Each output is committed before it is read. For part V the only checks are the exit, NaN, paths
  and the hash; part S runs only after part V's output is committed.
- A failed part is a failed launch, kept and disclosed. Only that part is relaunched.
- Any later check is labelled post hoc.

0 of 19.
