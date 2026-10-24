# THE HOLOMORPHIC READING TEST — the result

chat1 (the web seat), 2026-10-24. Rule `HOLO_TEST_RULE.md` (sealed at 110af4a13, pushed before the script); script
`holo_test.py` (1bfbb2326, committed before its run). Every output was committed before it was read, except C1:
- C0 2479187b7;
- the store and C1 391d4d42d. C1 is data-free and was read as soon as written, to check the store's relaunch, as that
  commit records;
- C2 b51a670ec;
- the rows and calibration-grid minima 5e99d23f3;
- the calibration 909308686;
- the cells 74bd74518.

The cells were read once, after their commit and after THE UNIFICATION-SCALE TEST was sealed (ef08144e1). The post hoc
read-outs (B-2, B-3) come from scripts committed before the rows existed; their output, 75715991c, was committed before
it was read. Checked read-only by a referee before sending. 0 of 19.

## The answer

**The declared search found rows below both bars only on the look's two lines:** the look reproduced at a nearby τ, not a
new row. Away from those lines the lowest it found on 5 280 rows is 33.98. Its power was not established (C2 failed), so
this is not a negative. **Not read as a selection:** on the 264 lines, random hierarchies reach the data's calibration
statistic (35.43) in 4 of 300 from main's generator and in 83 of 1 200 lepton-tied; the rule allows at most 2 and 11. The
look's lines are not priced.

| cell | statement | prior | outcome |
| --- | --- | --- | --- |
| H1 | some test row below 21.67 | 45% | **holds**: 2 rows, both on the look's lines |
| H1′ | the same on the 264 lines other than (2/5, 0) and (2/5, 3/5) | 35% | **fails**: lowest found 33.98 |
| H2 | some test row's optimum below both bars | 40% | **holds**: the same 2 rows (χ²_six 0.66 and 0.79) |
| H2′ | the same on the 264 lines | 30% | **fails** |
| H3 | main's generator: at most 2 of 300 at or below the data's statistic | 75% | **fails**: 4 of 300 (1.3%; exact upper end 3.4%) |
| H3′ | lepton-tied: at most 11 of 1 200 | 30% | **fails**: 83 of 1 200 (6.9%; upper end 8.5%) |
| H3′_BAR | 3 × that upper end below 1% | 12% | **fails**: 25.5% |
| H4 | a row below both bars with D within 10.58 ± 0.33 | 10% | **fails**: D = 9 at both rows (order-5 lines, where D ≡ 9) |
| C0 | the model and χ² paths against their references | 99% | **holds** (5.9 × 10⁻¹³; 0; 7.4 × 10⁻¹⁵) |
| C1 | the store against `coupling()` at five points | 95% | **holds** (3.3 × 10⁻¹⁶) |
| C2 | power: the search at or below the planted χ² on at least 34 of 36 | 85% | **fails**: 33 of 36 (read before any row was read; disclosed) |
| C3 | the 100 mirror pairs agree within 1% on at least 90, and on every pair below 21.67 | 80% | **holds**: 100 of 100; the one pair below 21.67 (21.58) agrees to 10⁻¹⁰ |

**What it means, in the rule's fixed words:**
- "**H2 holds, H2′ fails:** the look reproduced at nearby τ, not a new row."
- "**H1 or H2 holds, H3 fails:** below the bar, but random hierarchies are fitted as well in 1% of cases or more (3 or
  more of 300); reported, not read as a selection."
- "**C2 fails:** a failure of H1 is not read as a negative." C2's failure is read under this sentence of its own, not
  under "C3 or another control fails: nothing is read until it is resolved"; the unification-scale rule's later wording
  ("C3X, C0 or C1 fails") confirms that intent.

**chat1's additions (labelled readings after the cells):**
- H1 holds, and H1′ fails. Since C2 failed, H1′'s failure is read the same way: no negative is claimed for A1 on the 264
  lines. The rule did not state H1′'s case separately; this reading can only withhold a claim.
- The calibration priced the data's best row on the 264 lines by the coarse calibration grid: (2/5, 4/5) at
  0.775 + 2.375i, L₂, statistic 35.43, χ²_six 3.52 there. That is not the lowest row the search found on those lines,
  which is (2/5, 1/5) at 33.98. The priced statistic is not below both bars, and H3 fails, so the calibration prices
  nothing the rule would read as a selection.
- Both rows below the bars also lie above the fitted-structure line, 15.09 (five degrees of freedom; plan C-3).

**Reach**, the rule's sentence with its last clause corrected: conditional on the frame as main built it (B1736's scalar
part zero), the 266 lines, the ten τ, the two horocycles, c = 3 by hand, the comparison at M_Z, the reading of S as
holomorphic (P-295 records another reading), and the declared search, whose power C2 did not establish. The direction h
is fitted, four real numbers per row. Between the sampled τ nothing is claimed.

## The rows

- **Below 21.67 (H1, H2):**
  - (2/5, 3/5) at 0.775 + 2.375i, L₂: χ²_nine 20.68, χ²_six 0.66. The six ratios are 0.94–1.06 of the data; |V_us|,
    |V_cb| and |V_ub| are 0.795, 0.696 and 1.162 of it. D = 9; |h·h| = 0.019.
  - (2/5, 0) at 0.275 + 2.375i, L₂: 21.58, χ²_six 0.79, nearly the same pattern.
  These are this grid's rows on the look's two lines. The nearest of TWO_HIGGS's rows below 21.67 on the same line and
  horocycle lie 0.23 and 0.18 away (both 21.52, at Im τ 2.3); main's dense tracking of those lines (P-357) reached 16.74.
  H1's row ranks 13th by grid minimum among the test rows.
- **The eight lowest rows** are all on those two lines (20.68–29.93, at Im τ 2.075, 2.375 and 3.275, both horocycles).
- **On the 264 lines:**
  - (2/5, 1/5) at 0.275 + 2.075i, L₂: 33.98 (χ²_six 14.1);
  - (2/5, 2/5) at 0.775 + 2.375i, L₂: 34.59 (χ²_six 1.75);
  - (2/5, 4/5) at 0.775 + 2.375i, L₂: 35.43 (χ²_six 3.52; the calibration's row);
  - the first rows off order 5 are on order 10: (2/5, 1/10) at 0.775 + 3.275i, L_max, 36.47 with D = 12.6; and
    (2/5, 1/2), 36.67.
- **The distribution:** 2 rows below 21.67, 30 below 50, 79 below 100, out of 5 320. The quantiles at 1%, 5% and 50% are
  69.8, 297 and 1 478.
- **The lowest by line order:** 5: 20.68; 10: 36.5; 9: 113; 11: 131; 8: 198; 7: 652; 12: 5.8 × 10⁴; orders 1, 2, 3, 4
  and 6: above 2 × 10⁵. Four rows have outputs identically zero on their line.
- **J and the inter-sector ratios (B-3: read-outs, not fitted; post hoc):**
  - |J| at the two lowest rows is 5.8 × 10⁻⁶, about 5.3 times below the data's 3.08 × 10⁻⁵. Over the 100 lowest rows
    the median is 3.1 × 10⁻⁶ (10–90%: 0.6–6.7 × 10⁻⁶).
  - m_b/m_τ = 1.000 at the lowest rows (b–τ equality on the order-5 lines; median 1.00 over the 100), against 1.64 at
    M_Z.
  - m_t/m_b (the up and down sectors' heaviest singular values) is 1.57 at the lowest row and 1.44–1.72 at the ten
    lowest. The record's pinned values give 59.3 at M_Z (168.26/2.839), about 38 times more. Under reading (i), one
    doublet, no tan β can absorb that factor. A second doublet would need tan β ≈ 38; that is not tested here.

## B-1: what A1 is, under main's answer

Main's record answers the identification (P-365): the frame carries no electroweak doublet index. So A1 is one family
direction read alike in every sector, which is what one Standard-Model doublet times that direction gives once the doublet
is added by hand (`A1_THE_IDENTIFICATION_QUESTION.md`, answered section, 3c07b6a39).

**Worded so:** for one family direction read alike in every sector, the declared search found rows below both bars only
on the look's lines, with D = 9 and |J| about five times too small: the look reproduced, not a new row, and not read as a
selection. On the other 264 lines of this grid the lowest it found is 33.98, with a search whose power was not
established, so this is not a negative. Under reading (ii), a family triplet of doublets with A1 as two aligned triplets,
the statement is the same; that reading needs an index the frame does not carry and is noted, not used.

## B-2 and B-3, post hoc (labelled; `holo_posthoc.py` and `holo_posthoc2.py`; items (a)–(c) on the 100 lowest rows)

- **Nearest record direction (B-2a):**
  - the counts: the conjugates of DR and of F₂ (38 rows each), then F₆ (14);
  - the distance: median 0.113 rad (10–90%: 0.05–0.23);
  - no single record form is the fitted direction.
- **The covariant pencil DR + μ E₂* R (B-2b), not singled out:**
  - the fitted direction's median distance from the pencil is 0.012 rad (10–90%: 0.004–0.043). Its conjugate is the
    nearer of the two on 88 of the 90 rows within 0.05 rad;
  - μ varies from row to row: its real part has median 0.09 (10–90%: −0.04 to 0.21; negative on 16 of the 90), and its
    imaginary part lies within ±0.2 on 90% of them, with extremes −2.0 and 1.28;
  - since E₂* is a number at each τ, a pencil with μ free per row is just span{DR, R}, and pairs of other record
    directions span the fit equally well (B-2c, median 0.012 rad: F₆ with h̄₂; D̄R with h̄₂; D̄R with F̄₂);
  - at the sensitivity main found (S212: χ²_nine moves from 20 to 136 for a 0.008 rad change), 0.012 rad is not close.
    Main's two-form pencils on record bottom out near 42 (B1746).
- **Along Im τ (B-2d):** consecutive fitted directions move 0.090 rad per step (median), against DR's 0.032.
- **The invariant (post hoc 2a):**
  - |h·h| has median 0.018 (10–90%: 0.015–0.030), with medians 0.019, 0.019, 0.020, 0.017 and 0.017 at the five
    heights;
  - this agrees in median with main's P-357 (0.017–0.020 on the look's lines), with a wider spread.
- **The e₁ admixture (post hoc 2b):**
  - μ = a/(√2 × the larger of b and c), for h = a e₁ + b n + c n̄ under the bilinear dot, divided by θ₂(τ)/θ₃(τ);
  - over the 100 lowest rows (93 on α = 2/5 lines, 20 on the look's lines), its modulus has median 0.45 with a spread of
    0.33 in ln (median absolute deviation; 0.19 within one line), and its phase is not fixed (1.5 rad). Against R's own
    law, Θ₂/Θ₃(2τ), the spread is wider (0.53). So across lines it is not a fixed multiple of θ₂/θ₃;
  - on the look's lines, where P-357 found 0.585·e^{0.99i} with a spread of 3.9% (L₂, its dense grid, rows below 30),
    this grid's three (2/5, 3/5), L₂ rows below 30 give 0.54–0.64 with phases 0.88–1.06 rad. Over all eight look-line
    rows below 30 the modulus is 0.52–0.90 (median 0.64). This check was computed after the note's first draft; it is
    labelled post hoc.
- **The mirror pairs (post hoc 2d, on the 100 mirror pairs):** the fitted direction on one row is P h̄ of its partner's,
  to 1.7 × 10⁻⁶ rad (median; largest 0.021). R4 is an exact symmetry of the model, so this checks that the search found
  mirror-image optima, as C3 does for the minima. It says nothing about modular covariance.

None of this is a test. The invariant stays a lead for P-357's open question; the pencil is not singled out.

## Disclosures

- **C2 failed** (33 of 36; noiseless recovery to 0.1 on 23 of 36). This was read before any row was read and disclosed
  in THE UNIFICATION-SCALE TEST's rule, whose second search stage was built for it (e10–e12).
- **The store:** its first launch was stopped within seconds and disclosed (cb8d07163). The store then took 36 minutes,
  against the rule's "about 25".
- **The scan ran in four parts with the same script** (the manifest refuses any other), about seven hours of run time,
  much of it beside other jobs, against the rule's 3–3.5 hours:
  - parts 1 and 2 stopped at the sandbox's two-hour job limit after 7 and 13 of 28 chunks (911bb293d, 93ce50081);
  - part 3 was stopped by chat1 at a chunk boundary after 18, so that the resume had a full job window (f65c7cb78);
  - part 4 wrote chunks 19–28 and the outputs (5e99d23f3).
  The logs hold progress lines only.
- **The calibration took 75 minutes,** against the rule's "about 50": each target recomputes the direction grid.
- **Read before the cells, as context:** main's P-357, P-364, P-365, P-366 and P-370.
  - P-357, P-364 and P-366 are post hoc analyses on seen points. P-364 in particular: "the up quark comes out 2–7 times
    too heavy at every phase … one Higgs read everywhere cannot make the up quark light", at departures fixed by m_d/m_b
    along n or e₁. With h free, the two lowest rows here have m_c/m_t and m_u/m_t at 0.99 and 1.01 of the data, and the
    fit's misses are in the CKM moduli.
  - P-365 is the identification answer used in B-1.
  - P-370 is main's post hoc look at the SM seat's W147 pairs.

## What follows

- **THE UNIFICATION-SCALE TEST runs now, as sealed** (rule ef08144e1, script 031bbacde).
  - Done so far: its C0 and C1 are committed unread (4b0b19d4a, a53347f7f).
  - Running: the store. Then C2, then the scan, about ten to twelve hours.
  - It asks A1's question again on fresh rows with a two-stage search, whose power C2G and C2Z measure, at M_Z (arm Z)
    and at the unification scale (arm G). Its arm Z can give the negative this test cannot, or a positive on the 264
    lines.
- **The plan's C-2:** its condition holds, since A1 lands near the bar only on the look's lines. THE UNIFICATION-SCALE
  TEST is its first half. The second half, A1 with τ at B1720's apexes, is left for a later rule, as UNIF_TEST_RULE says.
- **The plan's C-1** (a rule fixing h) is not triggered: A1 did not pass here.
- **The Higgs-pair route,** H_u and H_d with different family directions (THE_NEXT_ATTACK's step 3; the SM seat's W147),
  stays open. Its best on record is main's S212, 20.26 (post hoc, H_d fixed to ∂R̄ and H_u free). Main's P-370 is a
  negative for W147's pair-term set: its off-diagonal pairs have χ²_nine at least 1 663, and "the pair-term set does not
  carry the nine". A sealed test of the route waits for THE UNIFICATION-SCALE TEST's result.

0 of 19.
