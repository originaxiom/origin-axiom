# W161 — the plan's stage 1, second part: the agy branch's ten Higgs recipes (B1762) on this seat's own code, the whole menu priced, and held out at the strip's 38 rows (the rule, committed before the script)

The SM-derivation seat, 2026-10-27. Committed and pushed before the script that reads it exists. Nothing here is a
result.

## Why

- **The plan** (`THE_NINETEEN_PLAN_2026-10-27.md`, adopted by the owner) asks, at stage 1, for B1762's recipes to be
  checked on own code with "the whole menu priced (the step above)". Its charter (iv) says a menu chosen after the fit
  is priced by a class-choosing null over the whole menu.
- **What B1762 claims** (the agy branch at 05e6caabf; its script and JSON read):
  - ten recipes for the two Higgs directions, built from the frame's Gram matrices and the record's DR with no
    continuous fit;
  - best χ²_nine 25.4–26.3 at B1757's four strip points, against the bar of 21.67.
- **Why it matters to the plan.** W159 found that the forced moves cannot supply the second Higgs's orientation.
  B1762's down Higgs, the inverse Gram H_d ∝ (Σ̄_down)⁻¹v, is a direction fixed by the frame, not by the moves. It is
  the lead the plan's stage 3 would derive.

## The recipes (B1762's definitions, rebuilt here)

At a point on a C1 line (W160), with the S reading for every sector, the leptons with H_d and c = 3 (B1757's nine2):
- **The Grams.** Σ^(s)_cd = tr(Y_c† Y_d)/tr, with Y_c the sector's coupling of the basis direction e_c (W158's basis
  couplings).
- **The record's Higgs.** dr = DR(τ) gauged so its second component is real and positive; dr̄ the same for conj(DR).
  v = (0, dr̄₁, dr̄₂).
- **The down Higgs.**
  - hd₁ = (Σ̄_down)⁻¹v;
  - hd_p = (Σ̄_down)^{−p}v, with p = 1 + Σ^(up)₀₀/2;
  - hd_dec, the decoupled-block version.
- **The up Higgs:** (z, dr̄₁, dr̄₂), with
  - z₀ = boost·(−dr₀), boost = Re(v†Σ_up v)/Σ^(up)₀₀;
  - z_L2 = z₀ e^{iδ}, δ = Σ^(up)₀₀/2;
  - z_L3 = Re z₀ + i∣e₁∣, with e₁ = −(Σ^(down)₀₁ dr₁ + Σ^(down)₀₂ dr₂)/Σ^(down)₀₀ conjugated;
  - z_L4 = z₀ e^{2i∣e₁∣}.
- **The ten:**
  - B0: (dr̄, dr̄);
  - B1: (dr̄, hd₁);
  - L1_decoupled: (z₀, hd_dec);
  - L1: (z₀, hd₁);
  - L1p: (z₀, hd_p);
  - L2: (z_L2, hd₁);
  - L2p: (z_L2, hd_p);
  - L3: (z_L3, hd₁);
  - L3p: (z_L3, hd_p);
  - L4p: (z_L4, hd_p).

## The objects

- **B1757's four points:** line (2/5, 1/10), horocycle L_max, τ ∈ {0.3145 + 3.0345i, 0.333333 + 3.055050i,
  0.3145 + 3.10i, 0.3145 + 2.95i}.
- **The menu:** 10 recipes × 4 points = 40 fixed model nines. Nothing is fitted.
- **The held-out rows:** W158's 38 strip rows (B1749's 12 and B1753's 26, lines (2/5, 1/10) and (2/5, 1/2), each at
  its own horocycle), where the ten are rebuilt from the same definitions.
- **The nine, the targets and σ:** W158's (the record's, with the 10% allowance). J is a read-out against
  3.08 × 10⁻⁵ ± 0.15 × 10⁻⁵, the value B1762 uses.
- **The nulls** (fresh seeds 1849–1868, 4 000 targets each, W138's own draws), as W158: (a) the data's six with a
  random mixing; (b) B1741's random nines. A target counts if its least χ² over the same 40 nines is at or below the
  data's.
- **B1757's fitted vectors** (the agy branch's JSON at 05e6caabf, read by its git blob) for read-outs only.

## Weave or thread

**A thread-and-frame result, post hoc on the nine.** One line class, four points and ten recipes, all chosen by their
author after fits. The held-out rows were found with the data's six. **A look for the ledger** (target: the nine),
counted for any later test it informs.

## Seen before the rule (disclosed)

- **B1762's stored values at the four points** (its JSON, read in full).
  - At the probe the menu reads, in order B0 … L4p:
    821.16, 325.27, 291.58, 43.91, 31.89, 34.42, 26.31, 33.54, 25.81, 25.43.
  - The least over the 40 is 25.43 (L4p at the probe).
  - At 0.3145 + 2.95i the J pulls run from −20.4 to +3.75.
  - B1762's structural checks: the up Gram's off-block 0.0, and ∣Σ_lep − PΣ_down P∣ ≤ 6.2 × 10⁻¹⁶.
- **B1761's reported angles** between hd₁ and B1757's H_d at L_max, at three of the points: 0.46°, 6.85° and 2.92°.
- **Not run:** no script exists.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| K0 | **The instrument.** (i) The pins hold, and W158's 38 rows are rebuilt. (ii) At the four points the up Gram is 1 ⊕ 2 (off-block below 10⁻¹² of its norm) and Σ_lep = P Σ_down P with P = diag(−1, 1, 1), to 10⁻¹² | 85% |
| K1 | **B1762 reproduced.** For all 40 (recipe, point) pairs, the own χ²_nine equals B1762's stored value to 10⁻⁵ relative, and ∣J∣ likewise | 70% |
| K2 | **The menu priced.** The data's least χ²_nine over the 40 is at most 1% likely under each null: null (a) ≤ 1% and null (b) ≤ 1% | 50% |
| K3 | **Held out.** At the 38 rows, no recipe reaches χ²_nine below 21.67 | 75% |
| R | **Read-outs** (no prediction): per recipe, the least and median χ²_nine over the 38 rows, and the range of J's pull; the Fubini–Study angle between hd₁ (and hd_p) and B1757's fitted H_d at the four points; the angle from hd₁, from B1757's H_d and from its H_u to the nearest of DR's 24 images under the forced group (W159's orbit) at the four points | — |

## What the outcomes mean (fixed now)

- **K1 fails:** the rebuild or the conventions differ. The parts that differ are listed, and nothing is priced until
  they are diagnosed.
- **K1 holds and K2 holds.** The menu is specific: its nines are not what random targets reach. But the best (about
  25.4) is above the bar. The recipes are a lead, not a law, and their numbers (the boost near 2, p, the Schur
  component) become targets for the plan's stage 3 to derive from the frame's action.
- **K2 fails:** the menu's best is what random nines reach as often. B1762's recipes carry no specificity.
- **K3 holds:** the recipes do not pass the bar anywhere on the strip. **K3 fails:** the rows and recipes that pass are
  read out, labelled post hoc; no claim, since both were chosen with data in view.
- **The read-outs** say whether the inverse Gram lies near the free fit's H_d, and how far both lie from DR's forced
  orbit. That is W159's gap, measured.

## What stays out

- Any new recipe; B1762's two-parameter floors (fits); its GUT-scale targets (hand-shifted); other lines and points.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read.
- A failed part is a failed launch of that part: kept, disclosed, fixed, and only that part relaunched.
- Any later check is labelled post hoc.

0 of 19.
