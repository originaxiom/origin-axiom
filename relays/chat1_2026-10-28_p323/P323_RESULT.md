# P-323, THE STRONG ANGLE IN THE MASS FRAME — the result

chat1 (the web seat), 2026-10-28. The order of the work:
- **The rule**, `P323_RULE.md`, sealed and pushed at f53115e19 before the script was committed (a draft, tested on
  synthetic arrays only, is disclosed in the rule).
- **The script**, `p323_strong_angle.py`, committed before its run (3a9da0dab).
- **The census** ran in two parts, its logs committed as they ended. Part 1 stopped at its time limit after 1 322 of
  1 836 tasks (b4bb81844). Part 2's first launch failed before computing anything: it ran in the wrong directory and
  python could not open the script. That launch's log is kept, with the machine-specific path in it replaced by
  `<repo>` (the only change). Part 2 then finished the 514 tasks left. The census's outputs were committed unread before
  any cell existed (762784a71).
- **The cells** were committed unread, then read once (77a943950).
- **Post hoc read-outs, labelled.** Each script was committed before its run, and its output before it was read.
  - `p323_posthoc.py` (ca3609de3; output 0843b961c). Two of its read-outs classified without the cells' J cut.
  - `p323_posthoc2.py` (56f38e128; output d85a3d093) redoes them with the J cut and reproduces the cells' H1 counts
    exactly.
  - `p323_posthoc3.py` (2cffa96da; output 9c6265acd) and `p323_posthoc4.py` (02f576f9b; output c709b41f9) were written
    after this note's read-only referee. It found the note's account of the UNDETERMINED combinations wrong, and a
    parenthesis in post hoc 2's output to be fixed text, never computed. Every number its corrections needed is computed
    there before it is cited here. Post hoc 4's first launch failed before the script ran (the shell's timing utility is
    not installed). Its error log is kept.

Data-free. Refereed read-only before sending. 0 of 19.

## The answer

**The controls hold: C0(a), (b), (c), (d) and (f), so every cell is read. The power control C0(e) fails.**

**The decisive cell H1 does not hold as sealed.**
- Its second clause fails: 219 of the 11 078 combinations with a reading are UNDETERMINED, 1.98% against the sealed 1%.
  By § 6, H1 is not decided on them.
- Its first clause, "no combination is HARMONIC", is untested because C0(e) failed. None was classed HARMONIC.
- Its 85% prior is not met.

**What the rule allows to be read** (§ 6, "(e) fails: … only the NOT HARMONIC combinations are read"):
- In the two Higgs-phase-free readings, 10 859 of the 11 078 combinations with a reading (98.0%) are NOT HARMONIC.
- On each of them, no counterterm holomorphic in τ makes θ̄ constant on any open set of τ containing a non-harmonic
  centre. So θ̄ is not identically 0 or π there.
- **Not covered:** the 219 UNDETERMINED combinations, 318 NOISE-LIMITED and 444 NO READING. In the NO READING
  combinations, 1 224 centres fail the cut |J| > 10⁻⁹ and 1 440 have a vanishing factor.

**The six's slope** (post hoc, labelled; Q6′): in the Standard Model's reading the 40 lines of slope 2/5 in scope are
NOT HARMONIC for every Higgs direction at both horocycles, with the cells' J cut (400 of 400 at each). On each of them, no
counterterm holomorphic in τ makes θ̄ constant on an open set containing an N centre.

| cell | statement | prior | outcome |
| --- | --- | --- | --- |
| **H1, THE DECISIVE CELL** | Higgs-phase-free readings: no combination HARMONIC, and at most 1% of those with a reading UNDETERMINED | 85% | **does not hold as sealed**: second clause fails (UNDETERMINED 219 of 11 078, 1.98% > 1%); first clause untested (C0(e)); § 6: not decided on the UNDETERMINED; 0 HARMONIC; NOT HARMONIC 10 859 |
| H1b | the same in (S, S) and (S̃, S̃) | 85% | **does not hold as sealed**: second clause fails (UNDETERMINED 389 of 10 383, 3.7% > 1%); first clause reported untested (C0(e)), as sealed; 8 combinations classed HARMONIC, listed; NOT HARMONIC 9 986 |
| H2 | the horocycle enters θ̄ on at least 95% of the (line, Higgs) pairs | 85% | **holds**: 2 697 of 2 833 (95.2%; 2 692 needed) |
| H3 | the conjugate Higgs suffices: frozen weights, Standard Model's reading, NOT HARMONIC on at least 90% | 80% | **fails**: 4 642 of 5 527 (84.0%); 53 HARMONIC |
| H4 | the computed norms suffice: θ_M NOT HARMONIC on at least 90% of lines | 70% | **fails**: 242 of 290 (83.4%); 12 HARMONIC |
| C0 | the controls | 90% | **(a), (b), (c), (d), (f) hold; (e) fails** |

**The controls:**
- **(a)** The closed form against the LU determinant: 55 686 checked, none failing; the worst sits at 3.5 × 10⁻⁴ of the
  tolerance.
- **(b)** Rank one: |Σ_s R_s²| / Σ_s |R_s|² is at most 1.5 × 10⁻¹⁵ at every evaluated point.
- **(c)** The Higgs's overall phase: 34 800 checked, none failing (worst 1.4 × 10⁻¹³).
- **(d)** The floor: no valid frozen-(S, S) case is classed N.
- **(f)** The noise model: at the 60 calibration points (360 checks: three Higgs directions, two horocycles) the T-step
  deviates by at most 2.6 × 10⁻¹², and at most 0.0045 of its tolerance. The two maxima fall at different points.
- **(e)** The power **fails**: 189 of the 5 603 frozen-(S, S) combinations with a reading are HARMONIC (3.4%).

## What it means, in the rule's fixed words

- **H1 (§ 6):** "More than 1% UNDETERMINED: H1 is not decided on them. They are listed, and no reading is drawn from
  them." And: "(e) fails: 'no HARMONIC' is untested for want of power, and only the NOT HARMONIC combinations are read."
- **On those combinations, the reading the rule wrote for H1:**
  - no counterterm holomorphic in τ makes θ̄ constant on any open set of τ containing a non-harmonic centre;
  - the frame as built does not fix θ̄ there. θ̄ stays an input: θ₀, tuned against θ_Y at the physical point to the
    measured 10⁻¹⁰, or one real equation on (τ, line);
  - P-323's answer on the covered combinations: none. It bears on P-267 (θ̄ a post hoc candidate only), I-18 and P-277.
  - No input removed. 0 of 19.
- **H1b** has H1's status: its second clause fails, and its first is reported untested, as sealed. Its 8 HARMONIC
  combinations are listed below. "A HARMONIC verdict is necessary for a constant θ̄, not sufficient." They lie in a
  reading where θ_Y moves with the Higgs's overall phase.
- **H2 holds:** "the hand-set horocycle enters θ̄, through θ_H only." One more place where an input that main's plan names
  as hand-set reaches a value.
- **H3 and H4 fail.** Each tested whether one ingredient alone breaks harmonicity on at least 90%. Neither does. The
  post hoc read-outs below describe where harmonicity is not excluded.

## The post hoc read-outs (labelled; after the cells)

- **Why the power control failed (Q1; S1–S3).**
  - **The classes** of the frozen-(S, S) centres: 2 132 H, 1 842 H′, 15 590 U, 15 264 Un (noise-limited, σ_D > 10⁻⁹)
    and no N. In 15 585 of the U cases the ratio is in [30, 250] but |D(r₂)| < 100·σ_D.
  - **D's scaling:** wherever |D(r₁)| ≥ 10⁻⁸ the ratio D(r₁)/D(r₂) is 64 at the 10th, 50th and 90th percentiles, the r⁶
    scaling of a holomorphic phase (Q1). It stays 64.00 (63.94–64.05 from the 10th to the 90th percentile) where |D(r₂)|
    is only 1–10% of σ_D, and 64.01 (63.43–64.55) where it is 0.1–1% (S3).
  - **The noise bound against the T-step:** σ̂ is at least 22 times the T-step's deviation at all 360 of C0(f)'s checks
    (median 1 493; S1), and the 10⁻¹² floor never dominates the tolerance. C0(f) cannot see an error common to τ and
    τ + 1, so this bounds σ̂ against the T-step only.
  - **A factor of 20 does not explain the failure:** with σ̂ divided by 20, frozen (S, S) reaches 12.0% HARMONIC (697 of
    5 800 with a reading); divided by 100, 34.2%; only near a factor of 1 000 does it approach 80% (78.1% there; S2).
  - **So:** the power failed because σ̂ is conservative: the unclassed centres scale as r⁶ below the 100·σ_D margin.
    Holomorphy did not fail. The method certifies non-harmonicity (C0(d): no false N; of the 25 952 centres with
    |D(r₁)| > 10⁻⁶ and σ_D ≤ 10⁻⁹ in the Standard Model's reading, 25 752 scale as r²). Under this noise bound it cannot
    certify harmonicity.
- **The UNDETERMINED combinations (Q2′, R2, R3, S7; with the cells' J cut, whose counts Q2′ reproduces exactly).**
  - **Their largest |D(r₁)|:** between 10⁻⁸ and 10⁻⁶ in 201 of the 219, below 10⁻⁸ in 12, above 10⁻⁶ in 6 (Q2′).
    - Five of those six lie on (0, 5/11) at L_max. There the ratio is 4.33 at |D(r₁)| ≈ 0.05, at a centre that is
      noise-limited (σ_D 3.4–4.3 × 10⁻⁹, class Un). The rule's Un test looks at σ_D alone; here |D(r₁)| is about 10⁷ σ_D.
    - The sixth, (1/4, 7/12) with F₁₄ at L₂ in (S̃, S), has ratio 2.85 (class U; R3).
    - Q2′'s printed parenthesis, "(there the ratio lies outside [3, 5])", was fixed text in its print statement, not a
      computed result. R3 replaces it.
  - **Where they lie:** only on slopes 0, 1/12, 1/6, 1/4, 1/3, 5/12 and 1/2.
    - 165 of them are with F₋₁₀ (162) or F₋₆ (3).
    - 214 lie on lines whose four norms are equal in pairs (R1, below): 49 on the twelve lines where θ_M is HARMONIC
      (48 of them with F₋₁₀ or F₋₆), 165 on the 36 where θ_M is UNDETERMINED (R2, S7).
    - 5 lie elsewhere.
- **The Higgs directions (Q7).** At the centres:
  - F₋₁₀ puts essentially all its weight on one component: |h_max|² = 1.000000 at every centre, to six figures.
  - F₋₆ is nearly as close (down to 0.999998), and F₋₂ has median 0.996.
  - dR and the others split their weight about evenly between two components (|h_max|² ≈ 0.50).
  - For a direction on one channel, (u·h) is one term. So its phase is nearly holomorphic, or nearly antiholomorphic in a
    reading that conjugates h.
- **The lines whose norms are equal in pairs (R1, Q4, Q8, S4).**
  - **54 of the 296 lines** have c₁ = c_i and c_j = c_k, or one of the other two pairings, to 10⁻⁹ relative at every
    centre in both sectors: 18 in each pairing (R1). θ_M is HARMONIC on 12 of them, UNDETERMINED on 36 and NO READING on
    6. It is NOT HARMONIC on all 242 other lines.
  - **The 12 where θ_M is HARMONIC:** (1/6, b) and (1/3, b) with b ∈ {1, 3, 5, 7, 9, 11}/12. No channel is clamped there.
    At every stencil point, in both sectors, c₁ = c_i and c_j = c_k to 1.1 × 10⁻¹¹ (S4).
  - **Why θ_M is harmonic there:** with Σ_s R_s² = 0 the pairing makes w² + u·u = (c₁ − c_j)(R₁² + R_i²), to the pairing's
    precision. c₁ − c_j varies with τ, from 36.80 to 59.28 in magnitude over the stencil points, but its sign is fixed:
    negative on the (1/6, b) lines, positive on the (1/3, b) lines (S4). So θ_M is a constant plus the phase of a
    holomorphic function, harmonic to the pairing's precision.
  - For comparison, on (2/5, ½) |c_j − c_k| reaches 0.46 (Q8).
- **H1b's 8 HARMONIC combinations (Q3):**
  - which: the reading (S, S) with F₋₁₀, on the six lines (1/3, b) at L_max and on (1/6, 5/12) and (1/6, 11/12) at L₂.
    All eight lie on the twelve lines with F₋₁₀, the two features above together;
  - in the other three readings the same combinations are UNDETERMINED;
  - F₋₁₀'s other components are small but not zero, so these are near-harmonic, not structurally harmonic.
- **H2's exceptions (Q5, S6):** 136, holding H2 by 5 pairs. Their largest horocycle difference is 1.2 × 10⁻⁶.
  - F₋₁₀ on slopes 1/12, 2/9, 1/4, 3/11, 2/7 and 5/12;
  - F₁₄, F₁₈, F₂₂ and F₂₆ on slopes 1/6, 1/3 and 1/2;
  - F₁₄ and F₂₂ on slope 0.
- **A note on the rule's D (S5).** D wraps the total phase difference into (−π, π].
  - In the readings (S, S) and (S̃, S̃), and with frozen weights in (S, S), about 10% of the valid centres have a stencil
    point where the factors' own wrapped differences sum past π, up to 4.62 rad. There the total aliases.
  - Taking D from the per-factor sums instead changes 19 centre classes and no verdict. C0(d) still finds no N.
  - In the Higgs-phase-free readings and for θ_H and θ_M no sum passes π (largest 1.77 rad).
  - It does no harm here. A future rule should take D from the per-factor sums.

## Read-outs (no cell)

- **The record's best six-rows,** Standard Model's reading, dR, L_max, in the representative as stored:

| row | θ_Y / π | θ_H / π | θ_M / π | J |
| --- | --- | --- | --- | --- |
| B1726's (2/5, ½) at 0.5500 + 3.0500i | +0.1774 | +0.3391 | −0.1617 | −4.22 × 10⁻⁴ |
| B1749's (2/5, ½) at 0.6053 + 3.0259i | +0.1220 | +0.3024 | −0.1803 | −3.64 × 10⁻⁴ |
| B1786's (2/5, 23/30) at 0.2692 + 3.0375i | +0.6339 | +0.2123 | +0.4215 | −1.82 × 10⁻⁴ |
| its mirror (2/5, 5/6) at 0.7308 + 3.0375i | +0.9461 | −0.3523 | −0.7015 | +1.82 × 10⁻⁴ |

  - e20's 0.1774π reproduces. J ≠ 0 at every row, and the mirror flips its sign.
  - These are the values θ₀ would have to cancel, in this representative.
  - (Post hoc, Q6′:) all 40 slope-2/5 lines are NOT HARMONIC in this reading. So near their N centres no counterterm
    holomorphic in τ makes θ̄ constant. The rows themselves sit at Im τ ≈ 3.03–3.05, in the horocycle segment
    Im τ 3.0–3.25, which no stencil samples.
- **The size of the non-harmonicity** (median over N centres of 4|D(r₁)|/r₁² ≈ |Δθ|; Standard Model's reading, dR, L_max).
  On the slope 2/5: θ_Y 4.74, θ_H 1.23, θ_M 4.54.
- **The clamps.** 6 864 channel-points at each horocycle, all where c_s is None (|R_s| ≤ 10⁻¹²): the same count at both
  horocycles. At no point in scope is 2πL + c_s ≤ 0, at L_max or at L₂. No centre has a clamp mismatch.

## Reach

The reach is the rule's scope:
- B1656's frame at B1667's end, as main's instrument computes it (3412bf09d);
- the 296 lines, the 10 Higgs directions, the 4 readings and the 2 horocycles;
- six centres per line at Im τ 2.375–3.375 on Re τ 0.15 and 0.65;
- counterterms holomorphic in τ, and constancy on open sets.

Higgs directions outside the ten are not covered. Neither is θ̄ = 0 at one τ or along a curve, which would be a
condition, not a derivation.

## For main's registers (main's to enter)

- **P-323:** answered on the covered combinations: no (reading, Higgs, line) there makes θ̄ identically 0 or π.
  - That includes every slope-2/5 line in the Standard Model's reading (post hoc, Q6′).
  - H1 does not hold as sealed: its first clause is untested (C0(e) failed), and it is not decided on the 1.98%
    UNDETERMINED. The residue is listed.
  - The residue's structure (post hoc, labelled):
    - 214 of the 219 UNDETERMINED lie on the 54 lines whose norms are equal in pairs;
    - 165 involve F₋₁₀ or F₋₆, the two directions nearest one channel;
    - all 8 of H1b's HARMONIC combinations, and 48 of H1's 219 UNDETERMINED, lie on the twelve lines where θ_M is
      HARMONIC, with F₋₁₀ or F₋₆.
  - θ̄ stays an input on the covered combinations. No input removed.
- **The look ledger:** one sealed look (H1), its 85% prior not met; H1b–H4 as the rule counted them.
- **P-267, I-18 and P-277:** θ̄ gets no structural zero in the mass frame on the covered combinations.
- **Main's plan, the horocycle (step 5):** it enters θ̄ (H2). In scope neither horocycle makes a weight imaginary (no
  2πL + c_s ≤ 0).

0 of 19.

## Dated correction (2026-10-28, after the integrity audit in THE EXACT END, THE SELECTOR AND THE AUDIT)

A read-only audit found the negative earned and numerically robust, and if anything understated: 168 of the 219
UNDETERMINED and 317 of the 318 NOISE-LIMITED combinations have a valid centre scaling as r² above 100 σ_D. Three
statements are corrected; each was recomputed here (`relays/chat1_2026-10-28_audit/audit_checks_run.txt`, part B).
- **"near-harmonic, not structurally harmonic"** (H1b's 8 HARMONIC combinations): the one-channel limit IS structurally
  harmonic. That limit is off the census: F₋₁₀ is one-channel only up to terms of order 2¹⁰e^(−2.5π Im τ).
  - With the Higgs exactly e₀, e₁ or e₂, θ_Y is harmonic at all six centres of (1/3, 1/12) and (1/6, 5/12):
    |D(r₁)| ≤ 4.7 × 10⁻¹⁰, scaling as r⁶, with |J| = 1.3–3.1 × 10⁻².
  - On (2/5, ½) it is not (ratio 4.0).
  - At those harmonic points the up sector has no hierarchy (m₂/m₃ 0.43–0.93).
  - So on the twelve lines where θ_M is HARMONIC (two of them tested), a NOT HARMONIC verdict on F₋₁₀ measures its
    small off-channel components (about 2¹⁰e^(−2.5π Im τ)), not an obstruction of the frame.
- **"every slope-2/5 line"** (for main's registers): read "the 40 slope-2/5 lines in scope (orders 5, 10, 25 and 30)".
  In the other phase-free reading, (S, S̃), they are also NOT HARMONIC at 400 of 400 per horocycle. That makes 1 600 of
  1 600 in the two readings.
- **The 98.0%** counts the combinations with a reading. Over all 11 840 combinations it is 91.7%. With a stricter N
  (|D(r₁)| > 10⁻⁴, ratio 3.8–4.2, at least two centres) it is 9 288: 83.8% of those with a reading, 78.4% of all.
