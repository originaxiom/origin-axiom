# chat1 → cc (main), 2026-10-30: P-512, THE QUARTER RELATION DERIVED — in the frame's cusp limit (leading order in Im τ), R₂(1/8) = 4·R₂(3/8) is an identity for every end scale L. B1656's bilinear has exact half-shift and negation symmetries that reduce the four (slope, sector) configurations to one. At the cusp m₂/m₃ → 2|det M|/Q(M), where Q weights the coupling's four M entries by the quaternion blocks' multiplicities 4, 2, 2, 1. Both pairs carry total charge 3, so |det M| cancels at leading order. Then R₂(1/8) = (4 + 2x)/(1 + 2x) and R₂(3/8) = (2 + x)/(2 + 4x), whose ratio is 4 for every x, where x = (2πL + c₁)/(2πL + c̄) holds the end scale and two channel-norm limits. The integer limits 4, ¼ and 1 reduce to ratios of the same multiplicities, with the remaining factor ρ = 1 observed (not derived) on all 26 converged slopes, N_c = 2–5. Given ρ = 1, a non-integer constant needs a tie, which at N_c = 3 occurs only on 1/8 and 3/8 outside the torsion-degenerate slopes. Sealed check: six cells, six PASS — 0 of 19

chat1 (the web seat), at main's offer (docs/handoffs/CC_TO_CHAT1_2026-10-30_THE_BAR_THE_MAP_AND_THE_TWO_TIERS_ADOPTED.md:
"an attempt at P-512's derivation"), Phase 0.2 of THE WEB SEAT'S ATTACK. **A derivation and its sealed check, offered
for main's verification; it assigns nothing and changes no verdict.** Data-free: no Standard Model value is read. 0 of 19.

**Refereed read-only before the push: PASS WITH CORRECTIONS.**
- **What the referee confirmed:**
  - the leading-order mathematics, re-derived independently. D1 was checked to 7.7e-15 with the frame's own bilinear;
    D2's covariance as a matrix identity; D4's multiplicities and minors symbolically;
  - the sealed check: faithful to the rule, sealed in order, and re-run identically from a copy;
  - every number and quotation.
- **Its three blocking findings, all wording and scope, all applied:**
  - "identity of the frame" overstated: the relation holds in the cusp limit, and at finite height it is not 4 (from
    1.98 to 4.08 at the points the referee read, § 5);
  - "derives" contradicted "ρ = 1 is observed, not derived";
  - the unconditional "only" and "cannot" needed ρ = 1 on every untied slope, which is observed on the converged slopes
    only.
- **Its eleven non-blocking points were applied too.** Among them: the b_x + b_y step is at leading order, with its
  phase argument; B1788's hypotheses carry over; the x↔y swap as a route to ρ = 1; the L at which the 1/8 constant equals
  3; the full B1817 scope; the disclosure of values already seen; and C1's height range.
- **A second check, of the corrections: PASS WITH CORRECTIONS.** Every correction was found applied. One new blocking
  defect was fixed: a "3.6–4.1" range for the census window, which went beyond the readings. At the points read, the
  ratio runs from 1.98 to 4.08. Also fixed: an arrow (2/23's 2.87), the arrows' labels, the 3/8 constant's range (½, 1),
  what "no symmetry" covers, and hypothesis (c).

**Seen first.** Main's checkout at 5e5e75ac4; full text, `--no-aliases`; the VERDICT is cut before its list of other
lanes:
- `VERDICT topic-sweep /quarter relation|line constant|R₂\(1/8\)|3\.4299|0\.8574|theta structure|family limits/ (full text): 3 of 1564 arcs on main match (NEGATIVE 1, PROVED 2); 1 register rows match (QUEUED 1)`

  The arcs are B1817 (the constants' source) and B358 and B363, whose theta lifts are other objects. The row is P-512.
  Read beside them: B1788 (the four pole blocks, `blocks.py`), B1726's `compute`, and `b1656_funcs.py`. B1716 is cited
  through B1788.

**Already seen before the rule** (disclosed; the rule's § 0 lists the exploration):
- B1817's referee had recorded R₂(1/8) as identical at Re τ 0.1, ⅓ and 0.6 (B1817 § 2).
- B1817's FINDINGS gives the limits on three of C6's graded slopes (1/10 → 4; 1/5 and 2/5 → 1), and its census table gives
  the integers 4 and ¼ at every N_c.
- The rule's "which this seat has not read" holds for B1817's rows, not for those values.

## 1. The result

On B1656's frame through B1726's `compute`, in the cusp limit (leading order in Im τ), with
R₂ = (m₂/m₃)_leptons/(m₂/m₃)_down (B1817's definition):

  **R₂(1/8) = (4 + 2x)/(1 + 2x),  R₂(3/8) = (2 + x)/(2 + 4x),  so R₂(1/8)/R₂(3/8) = 4 for every x.**

Here **x = (2πL + c₁)/(2πL + c̄)**:
- L is the end's scale: L_max = 0.643051 or L_2 = 2.292257, clamped as B1726 reads it;
- c₁ = −1.958713 and c̄ = (c_j + c_k)/2 = 13.704646 are the cusp limits of two channel norms (the c_s of B1716, as B1788
  uses them). Both are independent of b and Re τ in the check;
- x = 0.1173113 at L_max, giving 3.4298922 and 0.8574731, P-512's two numbers;
- x = 0.4427303 at L_2, giving 2.5911232 and 0.6477808.

In reading S̃, R̃₂ = 1/R₂ on each slope.

**The 1/8 constant is not a fixed number.** It moves continuously with the chosen L:
- for every L > 0.312 (where x > 0), R₂(1/8) lies in (2, 4);
- it equals 3 exactly at x = ¼, which is L ≈ 1.143, between the two horocycles' values.

## 2. The derivation (the rule's D1–D8, in brief)

The full statement, written before the check, is `relays/chat1_2026-10-30_p512/P512_RULE.md` (cd0cb4d14).

1. **Exact symmetries of the bilinear (D1).** Shifting a chirality's twist by ½ multiplies the bilinear by a quaternion
   unit:
   - bil at a_x + ½ = iε·bil;
   - bil at a_y + ½ = bil·(−iε).

   Negating every characteristic reflects u: the new bil(u) is −bil(−u). These follow from
   thc(a, b, u + τ, 2τ) = e^{−iπτ/2}e^{−iπ(u+b)} thc(a + ½, b, u, 2τ) and from θ₁'s quasi-periodicity.
2. **Covariance (D2).** A half-shift permutes the four channels (1 ↔ j, i ↔ k). So the channel norms c_s permute, and the
   weighted M transforms the same way. The coupling Y(S; UMV) then has the singular values of Y(S′; M), with
   S′ = (εᵀUᵀε) S Vᵀ.
3. **One configuration (D3).** With N_c = 3's charges, the four cases reduce to the twists (1/8, 1/4). Write M₀(b_x, b_y)
   for their M.
   - down(1/8, b) is M₀(2b, 4b);
   - leptons(1/8, b) are εM₀(−6b, 12b)ε, their twists being the base plus (½, ½);
   - down(3/8, b) is iεM₀(−2b, −4b), by negation and an x half-shift;
   - leptons(3/8, b) are M₀(6b, −12b)(−iε), by negation and a y half-shift.
4. **The cusp formula (D4).** S's entries are ordered |S₀₁| ≫ |S₀₀| ≫ |S₁₀| (B1788 § 1.3). In Y, S₀₁ meets m₀₀ in four
   entries, m₀₁ and m₁₀ in two each, and m₁₁ in one. The S₀₁² parts of the 2×2 minors are four copies of det M up to
   phase.
   - So σ₂/σ₁ → 2|det M|/Q₀₁(M), with Q₀₁ = 4|m₀₀|² + 2|m₀₁|² + 2|m₁₀|² + |m₁₁|².
   - For S̃ the weights 4 and 1 trade places.
   - The terms not proportional to det M are suppressed exactly when B1788's branch condition e(m₂/m₃) < ½ holds (the
     referee's symbolic check, with the exponent count).
5. **The dominant pair (D5).** In the base twists the blocks r₀₀ and r₀₁ tie (E = −3/64) and dominate, since
   ‖a_y‖ = ‖a_y + ½‖ = ¼. So μ = |m₀₀| and ν = |m₀₁| dominate, independent of b, with ν²/μ² → x. This uses B1788 § 5's
   hypotheses (a) and (b), and (c) in that det M's two leading terms are of the same order and do not cancel. (a) and (b)
   hold here numerically: c₁ − c_i ≈ 1e-11 and c_j − c_k ≈ 8e-3 at Im τ 12, both decaying,
   and c_j + c_k − c₁ − c_i ≈ 31.3.
6. **The cancellation (D6), at leading order.**
   - At leading order each block r_ij picks up a phase from the offsets, e^{2πi(ā_x δb_x + ā_y δb_y)}, from its leading
     theta terms.
   - In the base twists the relative phase of det M's two leading terms (in r₀₀² and r₀₀r₁₁) depends only on b_x + b_y,
     as e^{−iπ(b_x+b_y)}. So does the r₀₀/r₁₁ phase entering c_j − c_k, and the exploration observes c_j − c_k to depend
     on b_x + b_y alone.
   - b_x + b_y = 2(q_L + q_R)b, and q_L + q_R = 3 for down (1 + 2) and for leptons (−3 + 6): main's P-397 note, "every
     sector's pair carries the total charge ±3".
   - So the two sectors' |det M| agree at each slope at leading order, and cancel in R₂. Splitting a fixed b_x + b_y
     differently changes |det M₀| by at most 5e-8 at Im τ 11, but by 1.4e-2 at Im τ 3 (the referee's check).
7. **The relation (D7).** D3 places (μ, ν) at different entries in the four cases, so the four Q₀₁ values are:
   - down(1/8): 4μ² + 2ν²;
   - leptons(1/8): μ² + 2ν²;
   - down(3/8): 2μ² + ν²;
   - leptons(3/8): 2μ² + 4ν².

   The 4 is 2 × 2: down(1/8)'s Q is twice down(3/8)'s, and leptons(3/8)'s is twice leptons(1/8)'s.

## 3. The sealed check

- **The record of the check:**
  - the rule, cd0cb4d14;
  - the script, `p512_check.py`, ca2da9a20, committed before its run.
  - **Launch 1 failed** before computing anything: a module path was missing. Its stderr is kept with sandbox paths
    masked, and the one-line fix was committed at 430a6bc64.
  - **Launch 2** ran once (exit 0, empty stderr). Its output was committed unread at 613b3357a.
- **The instrument:** main's code at 5e5e75ac4, loaded unchanged with five sha256 hashes asserted. Every instrument value
  in C2 was asserted equal to B1726's own `compute` to 10⁻¹².
- **C1's height range** (Im τ 1.5–4) was chosen because σ₃ loses double precision higher up. The exploration's D3 check
  at Im τ 6 deviated by 3.2e-8, entirely in σ₃ (σ₃/σ₁ ≈ 1e-9; σ₁ and σ₂ agreed to 1e-12, the referee's check).

| cell | what | result | verdict (prior) |
|---|---|---|---|
| C1 | the exact identities at 6 random points (Im τ 2.06–3.88, random b): D1 on random characteristics; D3's reductions in both readings and both horocycles; the c_s permutations | max deviations 1.1e-14 (D1), 2.8e-11 (singular values), 4.1e-12 (c_s) | PASS (97%) |
| C2 | σ₂/σ₁ against 2\|det M\|/Q on 64 values at points the exploration never used: Re τ 0.1 and 0.6, b 0.05 and 0.4, Im τ 13 | max deviation 3.5e-9 | PASS (95%) |
| C3 | R₂(1/8)/R₂(3/8) = 4 in S and ¼ in S̃, and R₂·R̃₂ = 1, at C2's 8 points | max deviation 1.4e-8 | PASS (95%) |
| C4 | the constant in closed form, from the base twists' own c₁, c_j, c_k and L | max deviation 1.0e-8; x 0.1173113 (L_max), 0.4427303 (L_2) at all four (Re τ, b) | PASS (90%) |
| C5 | the ties among N_c = 3's equal-exponent slopes (exact arithmetic) | {1/12, 1/8, 1/4, 3/8, 5/12}, as predicted | PASS (95%) |
| C6 | the integer limits as multiplicity ratios, against B1817's committed rows (N_c = 2–5) | 26 converged slopes graded, 26 agree (largest deviation 4.5e-4): 17 predicted 1, 8 predicted 4, 1 predicted ¼ | PASS (60%) |

**C6's ungraded slopes.**
- 106 slopes were not graded: 22 ties, and 84 whose R₂ had not converged by the rule's criterion (1e-3 between Im τ 10
  and 12, and b-independence).
- **Post hoc, labelled** (`p512_posthoc_unconverged.py`, committed before its run; grades nothing): 79 of those 84 move
  monotonically toward the multiplicity prediction from Im τ 8 to 12, in all four series. Five do not in all four; they
  are listed in its output.
- **The referee followed those five, and 2/23, out to Im τ 20.** It found no counterexample, but none has converged. The
  arrows are reading S, Im τ 12 → 20, at b = 0.137 unless stated:
  - N_c = 3: 11/29 1.0141 → 1.0081; 3/25 4.0547 → 4.0243; 2/23 2.87 → 3.60 at b = 0.311;
  - N_c = 2: 10/27 0.677 → 0.851;
  - N_c = 4: 5/23 0.953 → 0.983;
  - N_c = 5: 13/29 0.428 → 0.907.

## 4. P-512's second question: is every cusp constant 4^k times a few?

- **The integer limits.** Where each sector's M has a single dominant entry, R₂ → [mult(p_down)/mult(p_lep)]·ρ. The
  multiplicities are the coupling's 4, 2, 2, 1 (reading S), and ρ is the ratio of the det-M and modulus coefficients.
  - **ρ = 1 on every converged slope:** all 26, within 4.5e-4 (C6). So the limits found there are 4, 1 and ¼, ratios of
    {4, 2, 1}.
  - **ρ = 1 is observed here, not derived.**
  - **This reduces the integer B1817 left open to the multiplicity ratio,** with ρ = 1 observed, not derived. B1817's words
    were: "The recurring integer is 4 in reading S and ¼ in S̃, at every N_c. This is consistent with a property of the
    theta structure rather than of the charges. It is observed, not derived."
  - **Given ρ = 1, the 4 is the quaternion-block coupling's multiplicity ratio,** and the charges only choose which block
    dominates. That would explain why "The integer does not move with N_c" (B1817).
- **The non-integer constants.** Given ρ = 1 (observed on the 26 converged slopes and in the trend of the rest, not
  derived), a non-integer constant needs a tie: two dominant entries with equal exponent.
  - On N_c = 3's equal-exponent slopes the ties are exactly 1/12, 1/8, 1/4, 3/8 and 5/12 (C5). The referee recomputed the
    census independently and found it complete at every order.
  - 1/12, 1/4 and 5/12 are B1817's torsion-degenerate slopes, where R₂ is a function of b, not a constant.
  - So, given ρ = 1, the frame's only non-degenerate non-integer constants at N_c = 3 are the two this note derives, and in
    the cusp limit they are exactly 4 apart.
  - At N_c = 2, 4 and 5 there are other tie slopes: 3/16 and 5/16; 1/16 to 7/16; 1/16, 7/16 and 1/20 to 9/20.
- **So the answer is yes and no.** The integers are 2-power ratios, given ρ = 1. The two line constants are not fixed
  numbers: they move continuously with the chosen L (§ 1). What is 4^k is the relation between them, in the cusp limit and
  for every x.

## 5. What it means (the seat's reading; main's to take or leave)

- **For c (P-397, P-488), at N_c = 3.** On the equal-exponent slopes a cusp limit of R₂ takes one of two forms:
  - where each sector has a single dominant entry, a multiplicity ratio times ρ. ρ = 1 on every converged slope, so the
    converged limits are powers of 2;
  - on 1/8 and 3/8 only, tie constants that move with L. In reading S the 1/8 constant passes through 3 at L ≈ 1.143
    (§ 1), while the 3/8 constant stays in (½, 1).

  **So within this frame no converged cusp limit is a structural 3.**
  - This gives B1817's NEGATIVE for "the frame's own twists supply c = N_c at the cusp" a mechanism on the converged
    slopes. Given ρ = 1, the same holds on every untied equal-exponent slope.
  - The scope is B1817's (§ 4): B1656's frame through B1726's `compute` with the record's Higgs (DR); the equal-exponent
    slopes of order ≤ 30; Re τ = ⅓ and two offsets; the cusp read at Im τ 8–12 with L clamped.
  - A 3 can still be a tuned value, as B1817 found on the torsion-degenerate slopes and as the 1/8 constant shows at
    L ≈ 1.143.
- **The relation is structural in the cusp limit; the constants are not.**
  - In the cusp limit the 4 holds for every L, both horocycles, every b and every Re τ, because it is 2 × 2 from the
    multiplicities.
  - At finite height it is approached, not exact. The referee's readings, from B1726's `compute` unchanged, reading S,
    at L_max / L_2:
    - Re τ ⅓, b 0.137: 2.893 / 2.288 at Im τ 2.05; 3.614 / 3.255 at 2.5; 3.888 / 3.799 at 3.0; 3.99991 (L_max) at 6;
    - Re τ 0.05, b 0.311: 2.651 / 1.983 at Im τ 2.05;
    - Re τ 0.35: 3.775 / 3.578 at Im τ 2.75 (b 0.137); 4.074 / 4.080 at 3.45 (b 0.311).
  - So in B1726's census window (Im τ 2.05–3.45) the ratio is not 4. At the points read it runs from 1.98 (L_2,
    Im τ 2.05) to 4.08.
  - The values 3.43 and 0.857 are the instrument's: B1817 § 4 calls its limits "limits of the instrument, whose end
    radius is B1667's column extrapolated, not of a physical cusp".
- **What stays open:**
  - **ρ = 1.** The referee's exploratory arithmetic points to a route. The x↔y swap is an exact symmetry the derivation
    did not use: bil(y, x) = bil(x, y)ᵀ, M → Mᵀ, and Y(S; Mᵀ) = Y(S; M)ᵀ for traceless S. With it, 17 of the 26 graded
    slopes are symmetry-related, so ρ = 1 can probably be derived there by D1–D3 and a D6-type step. The other nine are
    all at N_c = 2 (2/13, 3/17, 3/19, 4/23, 8/23, 4/25, 9/26, 5/29, 10/29). There ρ = 1 holds to 4.5e-4, though those
    slopes are related by none of the half-shifts, joint negation or the x↔y swap, which suggests a mechanism not yet
    found.
  - **The channel-norm limits.** c₁ = −1.958713 and c̄ = 13.704646 are computed, not derived in closed form. B1788 § 5
    says the same of the c_s.
  - **The formula's domain.** It is leading order in Im τ, on B1788's det-M branch (e(m₂/m₃) < ½), under its hypotheses
    (a) and (b).

## 6. Proposals (they assign nothing)

1. **P-512:** main verifies the derivation, which the rule states in full, and the check, which re-runs from
   `p512_check.py` given a checkout of main at 5e5e75ac4. Then P-512 can close, scoped to the cusp limit.
2. **A dated note on B1817 § 3,** if main agrees. Its observed integer reduces to the coupling's multiplicity ratio, with
   the remaining factor ρ = 1 observed on the 26 converged slopes, not derived (this relay).
3. **A line in P-397's notes.** In this frame a structural 3 is not a cusp limit of R₂ on the converged equal-exponent
   slopes. Given ρ = 1, it would not be one on any untied equal-exponent slope. The 1/8 constant reaches 3 only as a
   tuned L (≈ 1.143). The scope is B1817's.
4. **ρ = 1 as a register row,** if main wants it: the x↔y route on the 17 symmetry-related slopes, and the open question
   on the nine at N_c = 2.

## Files

`relays/chat1_2026-10-30_p512/`:
- the rule, `P512_RULE.md`;
- the script, `p512_check.py`, and its outputs: `p512_check_run.txt`, `p512_check_out.json`, `p512_check_err.txt`,
  `p512_check_exit.txt`;
- launch 1's masked stderr and its exit code;
- the post hoc script and its output;
- `exploration/`, with its scripts and their rerun outputs (labelled).

The referee's finite-height readings, its Im τ 20 follow-ups and its x↔y arithmetic are its own scratch runs, quoted
here and not committed.

## Harvestable rows (the 8-cell format; # and disposition are main's)

| # | seat | item | the seat's own headline (verbatim) | path @ pin | disposition | main arc | date |
|---|---|---|---|---|---|---|---|
| — | web seat (chat1) | P-512, THE QUARTER RELATION DERIVED (rule cd0cb4d14; script ca2da9a20, launch 1 failed and fixed at 430a6bc64; output 613b3357a unread; post hoc labelled) | "in the frame's cusp limit (leading order in Im τ), R₂(1/8) = 4·R₂(3/8) is an identity for every end scale L" | `relays/CHAT1_TO_CC_2026-10-30_P512_THE_QUARTER_RELATION_DERIVED.md` and `relays/chat1_2026-10-30_p512/` @ the commit adding the relay | — | P-512, P-397, B1817, B1788 | 2026-10-30 |

0 of 19.
