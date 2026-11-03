# P-555 — THE MIXING AS THE MEETING OF TWO LOCI: A DESIGN NOTE (data-free first; exploration tier, labelled)

main, 2026-11-03. Not a result; it fixes what a two-locus frame must do and what it may cost before any sealed test.
**Seen (disclosed):** B1825's run (its K numbers, read after the run) enters § 1; two coarse qualitative facts about the
measured world enter §§ 3–4 — nature's CKM has |V_td| > |V_ub| (B1826), and the up quarks' hierarchy is steeper than the
down quarks' — and nothing else measured.

## 1. The budget (from B1825's run, a read-out)

- The four (|V_us|, |V_cb|, |V_ub|, |J|) can carry at most **19.08 bits** against the frame's own CKM marginal: a perfect
  prediction at σ has log₂ density 7.81 (k₄ = −7.81), the marginal at our four is 2^−11.27.
- With the six coded at their best address (C_six = −3.08, the address's 18.81 bits included), K over the ten can reach
  at most **16.00 bits** against the gate 12.37 (m = 53): **3.63 bits** of room for a rule's choice and the four's misfit
  (χ²₄ ≤ 5.03 at a 0-bit rule, or one of at most 12 rules at χ²₄ = 0).
- A **free** second address (its discrete code 15.64 bits before any τ price) leaves C_ten ≤ 0.36: dead before it runs.
  A second locus must be FIXED by the first through a rule stated before the data.

## 2. The mirror rule (down at A* = (−τ̄, (α, −b)); B1821's proven symmetry; 0 bits)

- **Data-free facts** (audit/drafts/p555/): the down spectrum at A* equals A's exactly (20 of 20; B1821), so the six are
  untouched; |U(A*)| = |U(A)| entry by entry in every sector (36 of 36), so the rule changes only phases; on lines where the
  frame's own V is the identity (the zero line, b ∈ {0, ½}) the rule gives small, CP-violating mixing.
- **The Higgs's distance from the null cone, r = |h·h|/‖h‖², is invariant under the mirror** (every direction, relative
  difference 0.0): the theta series have real coefficients, so the direction at −τ̄ is the conjugate of the one at τ.
- **So the mirror cannot undo the corner inversion** (§ 3): it keeps r and the six, and moves only phases. At 645 random
  hierarchical points the corner order is a coin flip before and after (|V_ub| < |V_td|: 0.468 and 0.465); the rule raises
  CP violation (median J ×10, sin δ 0.32 → 0.47). **Where up is steeper than down (as measured; 303 of 1 456 hierarchical
  points, mirror_rule_structure2): the frame alone has nature's corner order with |V_ud| > 0.9 at 1.7% of points (median
  |V_ub|/|V_td| 2.66), the mirror rule at 0 of 303 (median 2.64). The inversion is the frame's behaviour exactly where the
  hierarchy is nature-like, and the mirror rule cannot lift it: CLOSED for the CKM.**

## 3. What the corners ask for (the mechanism; B1739, extended by the agy lane, B1826)

- B1739 (main, P-344): each sector's lightest state overlaps conj(h) under S and h under S̃; equal readings keep the light
  generation unmixed (|V_ud| 0.995), the SM's mixed reading makes it nearly orthogonal (0.28). So the readings must be equal.
- The agy lane's extension (B1826 § 1.3): the 1–2 angle of each sector goes as θ₁₂ ∝ r/(m₂/m₃); one Higgs gives one r, so
  the steeper up sector carries the larger 1–2 angle and the Cabibbo rotation lands in the (1, 3) corner.
- **The requirement:** for the Cabibbo angle to come mostly from the down sector, r_d/(m₂/m₃)_d must exceed r_u/(m₂/m₃)_u,
  i.e. r_d/r_u larger than the hierarchy ratio (about 5): **the down sector's Higgs must sit farther from the null cone
  than the up sector's.** A rule that keeps r (the mirror; any τ-preserving symmetry) cannot do it.

## 4. Candidates that change r (speculation → calculation; none computed against data)

| speculation | what changes r | its price | the calculation that settles it, data-free first |
| --- | --- | --- | --- |
| each sector at its own depth (B1694: up Im τ ≈ 3.1, down ≈ 2.5) | r ∝ e^(−π Im τ) | a second τ: about 9 bits unless a rule fixes Im τ_d − Im τ_u — over budget | if r and m₂/m₃ both fall like e^(−π Im τ), r/(m₂/m₃) is depth-blind and the corners go to about 1, not nature's 0.43: half the inversion; compute θ₁₂^(s) against depth on the frame |
| a second Higgs direction for the down sector (B1742: H_u = F₆, H_d = F₂₂; the six fit, χ²_six 1.19; the mixing aligned but small) | r differs by direction (F₆ 0.0019 at Im τ 3; DR 0.0058) | log₂ 12 ≈ 3.58 bits for the second direction — at the budget's edge, and only if the four come out nearly exact | the corner ratio and |V_ud| over the 12 × 12 direction pairs at equal readings, on the frame's own points; then a card that names ONE pair before the data, or prices the choice |
| a singlet Higgs component at its natural magnitude, a0 = c·sqrt(h·h), one fixed phase c for both sectors (the agy lane's framing, P-562) | the lock itself (ΔY = a0(m1 I − [m⊥]×) is sector-dependent) | 0 bits for a forced c; log₂ 12 for one of twelve phases | singlet_higgs_scan.py: per phase, nature's corner order with |V_ud| > 0.9 where up is steeper |
| a rule tying the down direction to the up direction (an action of the object on the directions: the modular weight, the cover's deck group) | the directions' r at one τ | 0 bits if the rule is forced | name the rule from the object first; nothing on record forces one |

## 5. The order of work

1. Done: § 2 closed (the mirror rule cannot lift the inversion).
2. The 12 × 12 direction pairs at equal readings, data-free: does any pair put the corners in nature's order with |V_ud| near
   1 at the frame's own hierarchical points? If none, the two-Higgs route is closed in this frame.
3. Only then a card: one rule or one pair named before the data, its p₂ computed first (X2 sank Step B), m = 54.

## § 6. THE SECTOR-ODD SINGLET (2026-11-03, evening; exploration tier; two coarse facts disclosed)

singlet_higgs_scan2.py (seeds 900–1139; ~300 points per phase where both quark sectors are hierarchical and up is steeper;
equal readings): with a singlet Higgs component at natural magnitude, a0 = c·sqrt(h·h),
- **same sign in up and down** (a0_up = a0_down): nature's corner order with |V_ud| > 0.9 at 0.7–4.0% for every phase
  (the frame alone 2.1%); median |V_ub|/|V_td| 20–29 — no effect;
- **opposite signs** (a0_up = −a0_down): **33–47% at every one of the ten phases; median |V_ub|/|V_td| 0.91–1.0** — the
  inversion is lifted generically, independent of the phase.
Consistency: c = 0 identical in both families (331 points, 2.1%, median 27.1); the same-sign family reproduces
singlet_higgs_scan.py (2–6%, median 22–35).

**Reading.** The CKM's corner inversion is not structural once the singlet is ODD between the sectors; an even singlet does
nothing. B1744: the frame's own twisted Higgs is even (H_u = H_d), so oddness must come from elsewhere. Candidates (none
computed): the Higgs's hypercharge sign (the up and down sums q_L + q_R are −3 and +3); the amphichiral involution (the agy
lane's Theorem 11: (τ, c) → (−τ̄, −c̄)); a singlet imaginary relative to the triplet under the reading's conjugation (the
reading maps (a0, h) → (a0*, h*), computed by hand here). Robustness running: singlet_robustness.py (fresh seeds; |a0|² =
0.25, 1, 4 × |h·h|). The corner ratio becomes balanced (~0.9), not the measured 0.43: half the inversion's distance, not all.
