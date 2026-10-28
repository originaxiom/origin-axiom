# W168 — the third opinion on chat1's P-323 (the strong angle in the mass frame): its structure and its slope-2/5 finding, on this seat's own instrument and by a different measure, a five-point Laplacian with step halving (the rule, committed before the script)

The SM-derivation seat, 2026-10-28. Committed and pushed before the script that reads it exists. Nothing here is a
result.

## Why

- **The owner's word:** "agreed continue do them all". That includes the third opinion on the web seat's P-323 when
  it reports. It reported at 51c25548c (relays/CHAT1_TO_CC_AND_SM_2026-10-28_P323_THE_STRONG_ANGLE_RESULT.md on the
  chat1 branch).
- **The plan** (`THE_NINETEEN_PLAN_2026-10-27.md`): every result gets another seat's third opinion before it is built
  on. P-323 bears on block E (θ̄) and on main's plan step 5 (the horocycle).
- **What a third opinion adds here.** Chat1 measured harmonicity with hexagon circle means and one noise model, on
  main's instrument through its own loaders. Its power control failed. This seat uses its own instrument (W138's, which
  reproduces main's census) and a different measure. Hexagon means scale as r² against r⁶. A five-point Laplacian
  instead is flat under step halving for a non-harmonic phase, and falls by four for a harmonic one.

## The objects

- **Chat1's definitions, taken as its rule states them** (P323_RULE.md at 51c25548c, read for this rule):
  - θ_Y = arg det Y_u + arg det Y_d, with θ_H, θ_M and the closed form det Y = (h·h)(w² + u·u)(u·h);
  - the Standard Model's reading (up S̃, down S);
  - the horocycles L_max and L₂;
  - the six centres per line, at Re τ ∈ {0.15, 0.65} and Im τ ∈ {2.375, 2.875, 3.375};
  - the cut |J| > 10⁻⁹ at the centre;
  - the 40 slope-2/5 lines in scope: (2/5, k/10) for k = 0…9, (2/5, k/25) with 5 ∤ k, and (2/5, k/30) with
    gcd(k, 6) = 1;
  - the twelve lines (1/6, b) and (1/3, b), b odd/12;
  - the ten Higgs directions: dR and F_a for a ∈ {−10, 14, 26, −6, 6, 18, −2, 10, 22}.
- **This seat's instrument:**
  - W138's residues, norms and weighted M, and W93's coupling (through W158's basis code);
  - the record's DR (`higgs_DR`);
  - W143's F_a through W146's `F_a`, whose phases ε = i^{(a+2)/2} equal chat1's ±1 for every a in scope. Both are
    normalised to unit length.
- **Chat1's numbers are not read by the script.** They are compared in the record afterwards. The four read-out rows
  come from this seat's own outputs:
  - B1726's best six-row (W138);
  - B1749's best row (W156: (2/5, 1/2), 0.666666667 + 3.0550505i);
  - B1786's best row (W164: (2/5, 5/6), 0.730769231 + 3.0374877i) and its mirror.

## The measure (fixed now)

- **At a centre τ_c:** θ is evaluated at τ_c ± h and τ_c ± ih, for h₁ = 0.04 and h₂ = 0.02, on the same line, with b
  not relabelled. Phase differences are wrapped about the centre's value.
  - Δ_h = [Σ θ(neighbours) − 4θ(τ_c)]/h².
  - The ratio is ρ = Δ_{h₁}/Δ_{h₂}.
  - No stencil crosses a node of the horocycle table, since the nodes are 0.25 apart.
- **A centre's class:**
  - **N** (non-harmonic): |Δ_{h₂}| > 10⁻⁵ and ρ ∈ [0.75, 1.35];
  - **H** (harmonic): |Δ_{h₁}| < 10⁻⁷, or ρ ∈ [3, 5] with |Δ_{h₁}| > 10⁻⁷;
  - **U** otherwise.
  - A centre where any factor of det Y vanishes (relative 10⁻¹⁴), or a wrapped difference exceeds π/2, is invalid.
- **A combination** (line, Higgs, horocycle) is NOT HARMONIC if some valid centre with |J| > 10⁻⁹ is N. It is
  HARMONIC if at least three such centres exist and all are H, and UNDETERMINED otherwise.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| P0 | **The closed form and rank one.** At 200 random complex (h, w, u), det coupling(S(h), M) over (h·h)(w² + u·u)(u·h) is one constant to 10⁻¹², and the same holds for S̃ with h̄. At every centre of the 40 lines, Σ_s R_s² = 0 to 10⁻¹² of Σ_s \|R_s\|², in both sectors | 90% |
| P1 | **The T-step and the relabelling** (chat1's e20). On each of the ten (2/5, k/10) lines, at every centre, with dR at L_max: θ_Y at (τ + 1, b − 2/5) minus θ_Y at (τ, b) is one constant, 19π/50 mod 2π, to 10⁻⁹. θ_Y at (τ, b + 1) minus θ_Y at (τ, b) is −2π/5 mod 2π, to 10⁻⁹ | 80% |
| P2 | **Chat1's Q6′ on own instrument.** In the Standard Model's reading, all 800 (line, Higgs, horocycle) combinations on the 40 slope-2/5 lines are NOT HARMONIC | 85% |
| P3 | **The twelve paired lines.** On each of the twelve, at every centre, in both sectors: c₁ = c_i and c_j = c_k to 10⁻¹⁰ relative, and w² + u·u = (c₁ − c_j)(R₁² + R_i²) to 10⁻¹⁰. θ_M is HARMONIC on each of the twelve | 80% |
| P4 | **The horocycle enters θ̄** (chat1's H2, on these lines). On each of the ten (2/5, k/10) lines, θ_H with dR differs between L_max and L₂ by more than 10⁻⁶ at some centre | 90% |
| R | **Read-outs** (no predictions): θ_Y/π at the four rows (SM reading, dR, L_max), and J's sign there; per Higgs, the count of N, H and U centres on the 40 lines; ρ's distribution at the N centres; the twelve lines' θ_M classes centre by centre; and, in the record only, the comparison with chat1's numbers | — |

## What the outcomes mean (fixed now)

- **P0–P4 hold:** chat1's structure and its slope-2/5 finding reproduce on a second instrument with a different
  measure. Its reading stands as written: θ̄ stays an input in the frame as built, with no structural zero on the
  six's slope. This seat agrees with chat1's grade, not decided as sealed.
- **P2 fails:** some slope-2/5 combination is HARMONIC or UNDETERMINED on this measure. It is listed. Chat1's
  post hoc claim is then qualified there, and the difference between the two measures is diagnosed before any reading.
- **P0 or P3 fails:** the closed form or the pairing does not hold on this seat's instrument. The two instruments are
  compared before anything else.
- **P1 fails:** the well-posedness argument (θ_Y is not a function of the physical point) is checked again by hand.
- **Whatever the outcome,** nothing is graded. P-323 is chat1's, and its cells stand as chat1 sealed them.

## Weave or thread

A third opinion on a census over every line of order up to 12 and every Higgs on record in one frame. On the
slope-2/5 lines it is a thread-and-frame result, and its claims are about the frame's θ_Y.

## What stays out

- Chat1's other cells: H1's full census, H1b, H3, H4 and C0(e)'s noise model.
- The readings (S, S), (S̃, S̃) and (S, S̃).
- Any target. No target file is read.

## Seen before the rule (disclosed)

- **Read on the chat1 branch:** chat1's result relay and result note in full; its rule's §1–§4; zero_free_census.py's
  direction(). Not run.
- **Read from own outputs for the rows:** W156's best row and W164's best row.
- **Checked by hand:** that W146's ε equals chat1's sign for every a in scope.
- **Not computed:** no θ_Y and no Laplacian. No script exists.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read. A failed part is a failed launch, kept and disclosed.
- Any later check is labelled post hoc.

0 of 19.
