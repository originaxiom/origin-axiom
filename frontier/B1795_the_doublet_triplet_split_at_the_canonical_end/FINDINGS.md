# B1795 — THE DOUBLET–TRIPLET SPLIT AT THE CANONICAL END (P-325; L250 (ii)): NO STRUCTURAL SPLIT — det M VANISHES FOR NEITHER VECTOR-LIKE PAIR ON ANY OF 286 LINES AT THREE POINTS. ON THE SIX'S SLOPE-2/5 CARRIERS THE TWO PAIRS' LIGHT MEMBERS AGREE WITHIN A FACTOR 7 (THE SHARED TWIST −2·2/5 ≡ 3·2/5 MOD 1); OFF THAT SLOPE THEY DIFFER LINE BY LINE IN BOTH DIRECTIONS. AT THE STRIP EVERY PAIR, AND EVERY STANDARD-MODEL SECTOR, HAS A LIGHT MEMBER FROM THE HIGGS SECTION'S NEAR-DEGENERACY. WITH THE SINGLET TYPED AS THE FRAME'S HIGGS SECTION, THE FRAME DOES NOT SOLVE SU(5)'S DOUBLET–TRIPLET PROBLEM

**Verdict: NEGATIVE** for a structural doublet–triplet split: S2 fails as sealed, and S1 and S1′ hold. S3 fails as sealed,
but its statistic fails on every line at the strip and in reading S only (§ 2). Data-free; no grade sought. cc (main),
2026-10-28. Sealed 24b9e468d before any vector-like pair was computed by its instrument. Outputs committed unread at
195d74e2f, then read once. Corrected before landing at its hostile referee (§ 4). **0 of 19.**

## 1. The cells, as sealed (`verification/split_run.txt`, `split.json`, `split_rows.jsonl`)

| cell | prediction | outcome |
|---|---|---|
| C1, control | the Standard Model's sectors through split.py's path reproduce B1726's compute() | holds (0.0) — the same functions, so it checks the plumbing only |
| C2, control | on lines of order 1 or 5 the D and H pairs agree (−2 ≡ 3 mod 5) | **holds** (2.7 × 10⁻¹³; the spectra to 2.3 × 10⁻¹⁴) |
| **S1, decisive** | no line has an exact zero of det M for the H pair | **HOLDS**: none of 286 |
| S1′ | none for the D pair | **holds**: none |
| **S2, the split** | some line has an exact zero for the H pair and none for the D pair | **FAILS**: no line |
| **S3, decisive** | at the strip, on the six's six carrying lines, the H pair's lightest state is ≥ 10⁻³ of its heaviest | **FAILS**: 4.9 × 10⁻⁵ |

**Read-outs:**
- The least Dn is 7.44 × 10⁻⁵ for each pair. It falls on (0, 1/11) and (0, 4/11), which are images of each other (§ 2).
  It is below B1716's non-zero floor of 1.9 × 10⁻⁴, but 5.9 decades above the 10⁻¹⁰ threshold, and a genuine non-zero (the
  referee's independent recomputation).
- At the strip carriers, the least σ₃/σ₁ is 4.9 × 10⁻⁵ for H and 5.1 × 10⁻⁵ for D.
- The leading-order "1"-channel residue vanishes on every row (≤ 1.7 × 10⁻¹⁵), which reproduces the L250 reader's
  R-check 3.

## 2. Reading (as written before the run; then post hoc and labelled)

**S1, S1′ and S2: no structural split.** det M ≠ 0 on every line computed, for both pairs, so the canonical end lifts
every vector-like pair at the matter level. This half does not depend on the singlet's typing.

**S3, post hoc (the pre-written branch: "it names the coincidence and grades nothing; … the D pair's state examined").**
- **It fails on every line at the strip.** The largest lightest H member there is 6.3 × 10⁻⁴. On the same carriers the
  Standard Model's sectors are lighter still (σ₃/σ₁ 2.6 × 10⁻⁶ – 2.3 × 10⁻⁴). Its 90% prior was mis-set.
- **The light member comes from the singlet section's near-degeneracy at Im τ ≈ 3,** which every pair shares. By B1659's
  law det Y = 4 det S det M tr(εSMᵀ) (the referee's `r7`):
  - on the carriers det M is O(1), with ∣det M∣/(∣M∣²/2) ≈ 0.8;
  - ∣det S∣/(∣S∣²/2) is 5.2 × 10⁻³ at the strip, against 6.9 × 10⁻² and 0.30 at the generic τ;
  - the pair's alignment factor ∣tr(εSMᵀ)∣/(∣S∣∣M∣) is 1.4 × 10⁻² – 10⁻¹ in reading S, and about 0.4 in S̃.
  - **So it cannot split the pairs, and it is absent in reading S̃,** where the H pair's lightest is 1.5 – 3.4 × 10⁻³ on
    every carrier.

**On the six's carriers** (`verification/posthoc/pair_compare.py`):

| reading, horocycle | H pair's lightest | D pair's lightest |
|---|---|---|
| S, L_max | 4.9 × 10⁻⁵ – 3.6 × 10⁻⁴ | 5.1 × 10⁻⁵ – 3.6 × 10⁻⁴ |
| S, L₂ | 2.2 – 4.0 × 10⁻⁴ | 2.2 – 4.1 × 10⁻⁴ |
| S̃ | ≈ 1.5 – 3.4 × 10⁻³ | ≈ 1.5 – 3.4 × 10⁻³ |

- The two agree within a factor of 7.4 in S and 1.25 in S̃.
- The reason is the slope (the referee's `r5`): on slope 2/5, −2·(2/5) ≡ 3·(2/5) (mod 1). The two pairs' twists share their
  τ-component and differ only through the offset (10b), whose effect is suppressed at Im τ ≈ 3. This is SU(5)'s mod-5
  identity in one coordinate.

**Off that slope the pairs split, approximately and in both directions:**
- the median ∣log₁₀(light_H/light_D)∣ at the strip is 0.05 on slope 2/5, 0.11 where 5α ∈ ℤ, and 1.2 elsewhere (up to
  4.8);
- on (1/6, 1/12) at the strip the H pair's lightest is 7.3 × 10⁻⁸ against D's 1.5 × 10⁻⁴; on (1/4, 3/8) it is the reverse;
- at 0.37 + 2.2i, 57 lines have an H member below 10⁻³ with every D member above 10⁻² (same horocycle and reading), and 70
  lines the reverse.

These are approximate splits, not exact zeros, and neither pair is favoured over the census. The census's median ratio of
1 is a relabelling identity, not a dynamical result: on lines of order prime to 6 the D pair on λℓ (λ ≡ −3·2⁻¹ mod N) is
the H pair on ℓ (B1728's quotient; the referee checked 288 rows to 2.3 × 10⁻¹⁰). The range is −4.8 to +4.3 decades.

**The slot swap** leaves det M and the whole spectrum unchanged. This is B1728's identity: the swap is a transpose, and R₁ = 0
leaves the i, j, k channels symmetric. So the four orientations are two computations, and "either slot order" in S1 and S3
is redundant.

**So, with the singlet typed as the frame's Higgs section:**
- the frame does not split doublets from triplets structurally;
- where the six live, the two pairs are light together;
- off that slope they differ, by line, without a rule.
- A light doublet with heavy triplets would need either a singlet direction with tr(εSM_Hᵀ) = 0 (B1659's law; it splits any
  line not of order 1 or 5), which this typing does not select, or another partner. That is the μ-problem and SU(5)'s
  doublet–triplet problem as they stand, here at B1667's canonical end in B1656's frame.
- No split is found, so nothing here moves the one-loop gauge ratio from B1484's ½ for complete multiplets. No ratio is
  computed, and no value comparison is made.

**No input removed. 0 of 19.**

## 3. Scope

- **The frame:** B1656's coupling at B1667's canonical end, at three points:
  - B1716's two generic τ;
  - the six's strip point (B1792's best row, chosen from data; S3 reads all six carriers there, not at each carrier's own
    apex).
- **The lines:** B1713's 266 and the twenty slope-2/5 lines of order 60.
- **The partner:** the singlet typed as the frame's Higgs section (S and S̃), a hypothesis. S1, S1′ and S2 do not depend on
  it; S3 and every light-state statement do.
- **Not examined:** other typings, non-holomorphic or flux partners (L250's frame, P-403), and couplings to heavy states.

## 4. The referee (hostile, read-only; `audit/referee_b1795/`, scripts kept in `verification/referee/`)

**Custody clean:**
- every hash matches, and the instrument is unchanged from the seal;
- the order holds: seal 06:33, outputs 06:49, outputs commit 07:33, read after;
- 858 unique rows, no NaN;
- control_run.txt's hash was sealed and the file committed with the outputs.

**What git cannot show** — that the run began after the seal, and that the outputs stayed unread for the 44 minutes before
their commit — rests on main's word. The mtimes and the run's four minutes are consistent with it.

**An independent recomputation** (the referee's `r4`): its own theta sums, residues computed analytically from θ₁′, its own
quadrature and coupling, with only S taken from the repository. On 11 lines × 3 points × 4 orientations it reproduces
Dn to 1.2 × 10⁻¹¹ and the spectra to 1.3 × 10⁻⁹.

**One blocking finding, applied:** the draft's "the colour triplet is as light as the Higgs doublet; nothing in the frame
separates them" was true only on slope 2/5. It is now scoped (§ 2).

**Corrections, applied:**
- S3 fails everywhere at the strip, by the section's near-degeneracy, and only in reading S;
- the median of 1 is a relabelling identity;
- the slot swap is B1728's identity;
- the ½ sentence carries no ratio or comparison;
- the title is scoped;
- the S, L₂ row is added.

**The disclosure, corrected (dated 2026-10-28):** the PREREGISTRATION's "two lines' pair values seen before the seal"
understated the peek.
- Dn depends on a sector's twist class only, so the (0, 0) sector's values that were seen (1.05 × 10⁻² and 7.69 × 10⁻² at
  the two generic τ) were the H pair's Dn on all 10 lines with 3α ∈ ℤ and 6b ∈ ℤ, and the D pair's on all 6 lines with
  2α ∈ ℤ and 4b ∈ ℤ: 14 distinct lines.
- On (1/3, 1/2) all three explored sectors had integral twists.
- One explored spectrum (1.24 × 10⁻³) equals the H pair's on (0, 1/2) and the D pair's on (1/2, 1/4).
- The exploration (`audit/drafts/s232_p283/look.py`, kept in B1799) ran split.py's own `sector()` on (0, 0), (2/5, 1/10),
  (1/3, 1/2) and (2/5, 49/60). No sealed pair coincides on the last two.
- Every line it fixed is far from zero, so the outcome is unaffected.

## Seen first

As in the PREREGISTRATION:
`VERDICT topic-sweep /doublet.triplet|triplet split|colour triplet|color triplet|vector.like|mu.problem|μ-problem|5/7|unification ratio|P-325/ (full text): 77 of 1542 arcs on main match (NEGATIVE 11, OPEN 3, PROVED 63); 2 register rows match (QUEUED 2)`.
Also B1659 (the joint law) and B1728 (the quotient; the swap). **Literature:** SU(5)'s doublet–triplet splitting problem and the μ-problem (standard: the missing-partner and Dimopoulos–Wilczek mechanisms split the multiplets by representation content, which this frame's single coupling does not have); nothing in the literature bears on this frame's lines.

## Files

- **The seal:** `PREREGISTRATION.md`; `ARTIFACT_HASHES.txt` (the sealed hashes; the outputs' under a dated note).
- **The instrument:** `verification/split.py` →
  - `split_rows.jsonl`, `split.json`, `split_run.txt`, `split_log.txt`;
  - with `--control`: `control_run.txt`.
- **Post hoc:** `verification/posthoc/pair_compare.py` → `pair_compare_run.txt`.
- **`verification/referee/`:** r1–r7 and their runs.

The lock: `tests/test_b1795_the_doublet_triplet_split_at_the_canonical_end.py`.
