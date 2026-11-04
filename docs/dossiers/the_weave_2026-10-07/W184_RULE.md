# W184 — B1814's census rerun blind, from its sealed card, on this seat's own code: the measured world as a draw from the weave's own measure, with the power beside each verdict (the rule, committed before the script)

The SM-derivation seat, 2026-11-04, at the owner's word "do it when u can", relayed by main
(CC_TO_SM_2026-11-03_B1814_BLIND_RERUN_THE_OWNERS_WORD.md), and the owner's "go". Committed and pushed before the
script that reads it exists. Nothing here is a result.

## Why

- **What main asked** (the handoff, from its invitation of 2026-10-29): rerun B1814's census from the sealed card
  (86cb26b30) with this seat's own code, blind. Main's outputs and FINDINGS numbers stay unread until this seat's
  outputs are committed unread. The verdicts to recover or contradict:
  - D2, the clock: p_F under the geometric and the move clock, and the test's power;
  - the six's typicality among the geometric clock's resolved worlds: p_nn unforced (D1) and with B1726's two
    ingredients by hand (D1h), and the random-hierarchy pass rates;
  - D1 at the floor 10⁻⁸, with the nearest unforced world's distance;
  - the mixings: the by-hand world's p on the nine.
- **The power beside each verdict.** Main's recognition audit (B1827 § G) graded B1814's typicality cell a screen
  with about 19% power. So a second census's power is as informative as its p values.
- **It counts as a verification of a sealed result, not a new look** (main's LOOK_LEDGER rule, as the handoff states).

## The card, and this seat's implementation where the card is silent (fixed now)

| card item | the card | this seat's implementation |
|---|---|---|
| the frame | B1656's four-channel coupling at B1667's end, B1740's module with DR | W178's point machinery (W162's frame: DR, κ-scaled residues, W177's exact norms, the weighted M, W93's coupling), with the record's residue cut ∣R_s∣ ≤ 10⁻¹² as B1740's module applies it, at working precision p = 40 + ⌈8π Im τ/ln 10⌉; per draw both readings S and S̃ for every sector, both horocycles, and the CKM for each (up, down) reading pair |
| A0, by moves | every primitive positive class with both letters of word length 2–16 (8 798) | Duval's generator of Lyndon words in L < R |
| A1, by length | every such class of trace 3–400 (14 690) | Lyndon pre-necklaces extended by the FKM rule, pruned by the trace (strictly increasing once both letters occur) |
| a thread's mass | ℓ = 2 arccosh(t/2) | a class is drawn with probability ℓ/Σℓ |
| the point | uniform in arclength, reduced | s uniform in [0, ℓ) from the axis's top: z = m + r tanh s + i r sech s; reduced exactly (integer γ) at 60 digits |
| the line | one of the thread's own flat lines, uniformly among those of exact order 1–12 up to sign | every v ∈ (ℤ/N)², N ≤ 12, of exact order N with vA ≡ ±v, one per ± pair, by brute force; uniform over the class's list |
| the transport | (α, b) ↦ (α, b)γ⁻¹ | as stated; checked in C1c |
| the radii | B1667's L_max, L₂, interpolated in Im τ from the Re τ = ¼ column, held outside [1, 4] | the column read as W162 reads it (B1667's the_canonical_cusp.json at W58's pin), Im τ clamped to [1, 4] |
| the horocycle and the readings | unforced: horocycle and each sector's reading uniform per draw (one sequence for both arms), c = 1; by hand: (S̃, S, S), c = 3, horocycle from the same sequence | as stated, with this seat's seed |
| c | 3 by hand | ln(μ/τ) + ln 3 and ln(e/τ) − ln 3 (B1726's lepton factor as W141 and W142 apply it) |
| resolved | all six ratios > 10⁻¹²; references and targets resolved | the world's six after c; read-outs at 10⁻¹⁶ and 10⁻⁸ |
| the cap | Im τ > 60 not computed: unresolved | as stated |
| data and sigmas | B1741's compare.py data, s6 and s9 | this seat's W142 code on B1741's inputs (HZ2021 at M_Z, ratios within a sector; B1612's CKM): T6 and s6 with the 10% allowance in quadrature; s9 adds the three CKM sigmas |
| random hierarchies | B1741's draws(seed) | this seat's own_draws (compare.py's order, written again; W141, W145), seeds 1741–1760, 4 000 six-targets each |
| anarchy | complex Gaussian 3 × 3 Yukawas per sector | 1 000 draws, three sectors, singular values to the six |
| draws per arm | 4 000 (seeds 18140, 18141; configurations 18142) | 4 000, this seat's seeds 18440 (A0), 18441 (A1), 18442 (configurations), 18443 (anarchy), 18444 (held-out split), 18445 (precision sample) — an independent census, not a replay |

## The statistics (as the card defines them; the details fixed now)

- **The distance:** max over the numbers of ∣x − t∣/σ, with s6 (s9 for the nine).
- **p_nn** (leave one out, among the arm's resolved draws). Let d_t be the target's nearest distance to the n draws,
  and d_i draw i's nearest distance to the other n − 1. Then p_nn = #{i : d_i ≥ d_t}/n.
- **p_F.** For each number k:
  - F_k = (#{draws < x} + ½ #{draws = x} + ½)/(n + 1), and p_k = min(1, 2 min(F_k, 1 − F_k));
  - the statistic is X = −2 Σ_k log p_k;
  - each reference draw's X_i is computed against the other n − 1 draws;
  - p_F = #{i : X_i ≥ X_t}/n.
- **Specificity r per decisive cell:** the share of the random hierarchies that pass the same cell, as a mean over
  the 20 seeds.
- **D1h's free null.** Each of the first 1 000 hierarchies per seed takes its best p_nn over the 16 configurations
  (8 reading triples × c ∈ {1, 3}, the horocycle from the sequence). The fixed-configuration r is a read-out.
- **THE_BAR (the card's):**
  - PASSED needs r < 0.01/53 ≈ 1.9 × 10⁻⁴;
  - a typicality cell that holds with r ≥ 1.9 × 10⁻⁴ reads CONSISTENT, NOT SPECIFIC.
- **The power, beside each verdict.** For each decisive statistic, the share called atypical (p ≤ 0.05) of:
  - 500 resolved worlds of the other arm (A0 under A1, A1 under A0);
  - the 1 000 anarchy worlds;
  - the random hierarchies (one minus the pass rate).

  Held-out calibration per arm: half the resolved draws as the model, 500 of the other half as targets, giving the
  share at p ≤ 0.05 (it should be near 5%).

## Controls (the card's, on this seat's code)

- **C1a:** the class counts are 29, 60, 96, 151 and 14 690 at trace ≤ 12, 18, 24, 30 and 400; 2 536 move classes of
  length ≤ 14; 8 798 of length ≤ 16. (Checked data-free for this rule: all match.)
- **C1b:** the reduction is exact: ∣γz − z′∣ < 10⁻³⁰ relative, for every draw.
- **C1c:** the transport and the radius law.
  - At fixed radii transformed by L ↦ L + log∣cτ + d∣, with γ = R and γ = TS, on two lines, every key agrees: max
    ∣log∣ < 10⁻⁹.
  - The wrong transport (α, b)γ must deviate by more than 0.1.
  - Checked data-free for this rule on two lines: deviation 0 against 2.6–3.1.
- **C1d:** this seat's point reproduces B1726's stored census row at (0.35 + 3.05i, line 149) to 10⁻⁹ in every key.
- **C1e:** at Im τ = 60, Re τ ∈ {0.05, 0.3}, on all 266 lines, every ratio is below 10⁻¹². The card states it for
  B1740's double-precision module; this seat's frame is exact, so here it is a read-out of the cap. A failure is
  recorded, not a stop.
- **C2:** this seat's measure reproduces B1735's 3.0945633 on B1726's census (W142's seat menu), within 10⁻⁶.
- **C3, the precision sample (this seat's):** 2% of the draws, recomputed at p + 60, agree within 10⁻⁶ on every
  feature above 10⁻¹².

## The cells, with predictions and priors

| cell | prediction | the card's prior | this seat's prior |
|---|---|---|---|
| **D1** | A1, the unforced mixture, the six, resolved draws: p_nn > 0.05 | 70% | 70% |
| **D1h** | A1, by hand, the six, resolved draws: p_nn > 0.05 | 75% | 70% |
| **D2** | the unforced mixture, the six, resolved draws: p_F(A1) > 0.05 AND p_F(A0) ≤ 0.05 | 45% | 45% |
| **C** | C1a–C1d, C2 and C3 hold | 95% | 90% |
| **R** | Read-outs. These are the card's list: p_F for D1 and D1h, p_nn for D2, the unconditioned statistics, every cell in A0 and in anarchy, the nine, each number's marginal p, the nearest resolved draw, the floors 10⁻¹⁶ and 10⁻⁸ (with the nearest unforced world's distance at 10⁻⁸), held-out calibration, the power, the heights, the capped and the share outside [1, 4], and q95 of the draws' own nearest distances per arm and configuration. The by-hand world's p on the nine is the mixings' verdict | — | — |

## What the outcomes mean

- **The cells read as the card's "The reading, written before the run (every outcome)",** unchanged. That includes
  D1h's conditional on resolution (the q95 in s6 units against log 3/s6 for μ/τ and e/τ).
- **The comparison, after this seat's output is committed unread.**
  - Then main's B1814 FINDINGS and comparison.json are read, and the web seat's rerun relay.
  - Each verdict is recorded as RECOVERED (the same side of its threshold) or CONTRADICTED, with both p values and
    both powers.
  - D1 at 10⁻⁸ is compared as the census-dependence check the handoff names.
- **A difference is not settled by preference.** A contradicted verdict is read with the census sizes, the
  resolution and the two frames' floors (this seat's frame is exact; B1740's is double precision).

## Weave or thread

- **neither (a census of the weave's own unforced measure under two declared counting rules, through B1656's frame;
  a verification of a sealed card).** The threads are every class of each clock, none picked. The comparison with
  data is the card's; this rerun adds no look.

## Seen before the rule (disclosed)

- **B1814's sealed card** (PREREGISTRATION.md at 86cb26b30), read in full. It was committed once, at the seal, and
  never edited. That includes its review-sample table, the shares of random hierarchies under each statistic on 400
  draws per arm.
- **Main's handoff,** which states that the web seat's rerun "found the three verdicts again and D1 at the floor
  census-dependent". It also states main's audit grade of about 19% power. Neither names a verdict's direction or a
  value.
- **B1813's FINDINGS § 1–2 and its frame card** (the clocks and their height tables), and B1733's FINDINGS § 1 (the
  Smith rule for a thread's lines).
- **This seat's W141, W142 and W145 records** (B1726's and B1735's census, B1741's measure), read when recorded.
- **Computed for this rule, data-free:**
  - the class enumeration and its counts (C1a);
  - one covariance check at τ = 0.31 + 1.47i on (1/7, 2/7) and (2/5, 3/10), which printed only the residuals.
- **Not read:**
  - B1814's FINDINGS.md, arc_verdict.json, census.jsonl, control.json, comparison.json, census_run.txt and
    compare_run.txt;
  - its referee's outputs and its census.py and compare.py;
  - the web seat's rerun relay and scripts.
- **Not computed:** no draw, no census point, no comparison with data.

## Discipline

- This rule is committed and pushed before the script exists in the tree.
- One run. Its output is committed before it is read. The only checks before that are the exit, failures, NaN, paths
  and warnings.
- Any later check is labelled post hoc.

0 of 19.
