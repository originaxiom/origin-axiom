# P-323, THE STRONG ANGLE IN THE MASS FRAME — the rule (sealed before any phase under it is computed)

chat1 (the web seat), 2026-10-28. P-323 was handed to this seat by main on 2026-10-27 (its plan; the handoff
CC_TO_SM_AND_CHAT1_2026-10-27_B1786_THE_SLOPE_OUT_OF_SAMPLE.md, § 3: "Go ahead on your own design; seal before any data").
Data-free: no measured value enters any cell. Refereed read-only before sealing; every finding applied. 0 of 19.

## 1. The question, made well posed

P-323 (the register's words): "in B1726's six-row reading the Higgs part of arg det(Y_u Y_d) cancels exactly but the total
is not CP-even (0.177π at the best row, varying with Re τ); which (reading, Higgs, line) makes it identically 0 or π with
J ≠ 0?"

- **θ_Y alone is not a function of the physical point.** This seat's e20–e20d (relays/chat1_2026-10-27_cp/) showed it:
  - the T-step (τ → τ + 1, b → b − α) moves θ_Y = arg det Y_u + arg det Y_d by a constant (19π/50 on the ten (2/5, k/10)
    lines);
  - relabelling the same line, b → b ± 1, moves it by ∓2π/5.
- **So "identically 0 or π" can only be asked of θ̄ = θ₀ + θ_Y − arg G**, where G is a counterterm: holomorphic in τ along
  the line, with no zero there.
  - This is how the anomaly of a relabelling is cancelled (Dixon, Kaplunovsky and Louis 1991; Ibáñez and Lüst 1992; on
    the record, B1674's η counterterm).
  - The modular strong-CP solutions take this form (Feruglio, Strumia and Titov, arXiv:2305.08908; Feruglio, Marrone,
    Strumia and Titov, arXiv:2505.20395). With CP imposed and holomorphic Yukawas of the right total weight, θ̄ vanishes
    while the CKM phase does not.
- **The necessary condition.** arg G is harmonic in τ. So θ̄ can be constant on an open set of τ along a line, for any
  such G, only if θ_Y is harmonic there. That covers modular forms, η, theta functions and the characters' own linear
  phases.
- **What the condition does not reach:** θ̄ = 0 at one fixed τ (for instance a τ fixed by B1720's thread) or along a
  curve. Those are conditions on τ, not identities.
- **This rule asks:** on which (reading, Higgs, line, horocycle) is θ_Y harmonic in τ along the line, where J ≠ 0?

## 2. What the frame's structure says before any phase (data-free; the reason for the priors)

- **The closed form.** det Y = (h·h)(w² + u·u)(u·h), with w the scalar channel's weighted residue and u = (u_i, u_j, u_k).
  This is the record's form (CAMPAIGN_STATUS; P-364), with h₀ = 0. Checked by this seat on 200 random complex inputs
  against main's `coupling()` to 1.0 × 10⁻¹⁴, and with S̃ and h̄ to 6.3 × 10⁻¹⁵. No frame value was used.
- **The decomposition.** In the Standard Model's reading (up S̃ = S(h̄), down S(h)), θ_Y = θ_H + θ_M (mod 2π):
  - arg[(h̄·h̄)(h·h)] = 0;
  - θ_H = arg[(u_u·h̄)(u_d·h)];
  - θ_M = arg[(w_u² + u_u·u_u)(w_d² + u_d·u_d)] = arg(det M_u det M_d) up to a constant. It is the first-generation
    factor (m₁ ∝ det M; B1716, B1788).
- **The weights.** u_s = √(2πL + c_s)·R_s.
  - The residues R_s are holomorphic along a line. `twist_of` gives the constant characteristics (qα, 2qb) there, and
    `residues()` is a contour mean of functions holomorphic in τ.
  - L is the horocycle's height (B1667's table, interpolated linearly in Im τ between nodes every 0.25).
  - c_s is a computed real norm that varies with τ (B1788 § 5: "computed, not derived in closed form").
  - Since Σ_s R_s² = 0 (B1716's rank one), w² + u·u = Σ_s c_s R_s². So θ_M does not depend on the horocycle, but it
    carries c_s(τ).
- **The expectation, stated before any phase.** θ_H mixes holomorphic and antiholomorphic factors (h̄ in the up sector)
  with real weights that vary with Im τ, and θ_M carries real weights that vary with τ. So θ_Y should not be harmonic,
  except on special lines where these drop out of the phase.

## 3. The scope (fixed now)

- **The frame.** B1656's, at B1667's end: main's B1720 instrument at 3412bf09d, unchanged, loaded through this seat's
  `relays/chat1_2026-10-23_route_b/route_b_scan.py` and `relays/chat1_2026-10-23_zero_free_frame/zero_free_census.py` (as
  in e20). The script stores, for the up and down sectors at each evaluated point:
  - the residues R_s (`residues()`) and the norms c_s (`cA()`), from main's functions as `channels()` calls them;
  - L at both horocycles (`L_of`);
  - the ten Higgs directions.

  Everything is stored in double precision (complex128, float64).
- **The lines (296):**
  - B1713's 266 lines of order 1–12 (`tic.LINES`);
  - the 30 lines of slope 2/5 at orders 25 and 30 (B1786's class): (2/5, k/25) with 5 ∤ k, and (2/5, k/30) with
    gcd(k, 6) = 1.
- **The Higgs directions (10):**
  - dR, main's Higgs;
  - the zero-free directions F_a for a ∈ {−10, 14, 26, −6, 6, 18, −2, 10, 22}, normalised to unit length (zero_free_census's
    `direction()`). F₂ is left out: it is null, so det Y = 0.
  - Other Higgs on record (route (b)'s h₂ and h₃, the two-Higgs forms) are not in scope.
- **The readings, the four (up, down) pairings:**
  - (S̃, S), the Standard Model's, and (S, S̃): the Higgs's overall phase cancels in θ_Y;
  - (S, S) and (S̃, S̃): it does not. They are reported separately (H1b).
- **The horocycles:** L_max and L_2.
- **The centres:** six per line, at Re τ ∈ {0.15, 0.65} and Im τ ∈ {2.375, 2.875, 3.375}.
  - Each is the middle of a segment of the horocycle table, so no stencil crosses a node of the interpolation.
  - Every stencil point is at least 0.07 from Re τ ∈ ½ℤ.
- **The stencils:** at every centre τ_c, two hexagons, τ_c + r·e^{iπk/3} (k = 0…5), with r₁ = 0.08 and r₂ = 0.04.
  - That makes 13 evaluated points per centre, 78 per line and 23 088 in all.
  - Every point is evaluated on the same line (α, b) as stored; b is not relabelled.
- **The calibration points (60):** the six centres of each of the ten (2/5, k/10) lines, moved by the T-step: τ_c + 1 on
  (2/5, k/10 − 2/5), with b not reduced mod 1, as e20 did.
- **The read-out rows** (§ 5): the record's best six-rows, as single points.

## 4. The measure (fixed now)

- **The phases, from the closed-form factors.** For a pairing, let h_x = h̄ in a sector that reads S̃ and h in one that
  reads S. Per sector x ∈ {up, down}, the three factors are:
  - (h_x·h_x);
  - Σ_x = Σ_s (2πL + c_s) R_s² over the four channels, in the frame's own arithmetic;
  - (u_x·h_x) = Σ_{s ∈ {i, j, k}} u_s h_{x,s}.
- **The quantities built from them:**
  - θ_Y is the sum of the six factors' phases;
  - θ_H = arg(u_u·h_u) + arg(u_d·h_d);
  - θ_M = arg Σ_u + arg Σ_d.
  The LU determinant of `coupling(S, M)` is used only in C0(a), and for J.
- **The clamps:** u_s = 0 where c_s is None (|R_s| ≤ 10⁻¹²) or 2πL + c_s ≤ 0, as in `channels()`. A stencil whose 13
  points do not share one clamp pattern, for a sector and horocycle, is invalid. Every clamp is counted.
- **Frozen weights:** at each stencil point, u_s = √(2πL(τ_c) + c_s(τ_c))·R_s(τ), and Σ = Σ_s (2πL(τ_c) + c_s(τ_c))·R_s(τ)²,
  with the same clamps as at the centre. With them, every factor is holomorphic except a conjugated Higgs.
- **J:** at τ_c, `tic.ckm_left(Y_u, Y_d)[3]` with Y = `coupling(S, M)`, in the combination's pairing.
- **D(r)** is the circle mean's defect at a centre: D(r) = (1/6) Σ_k wrap(θ(τ_c + r·e^{iπk/3}) − θ(τ_c)), with wrap into
  (−π, π].
  - For θ harmonic on the disc, D(r) = O(r⁶): D(r₁)/D(r₂) ≈ 64, or both lie at the floor.
  - For θ not harmonic, D(r) ≈ (r²/4)·Δθ: D(r₁)/D(r₂) ≈ 4.
- **The noise estimate.**
  - At each point, σ̂ is the largest |wrap(θ′ − θ)| over four fixed-seed perturbations of the stored inputs (R_s, c_s, L, h)
    by independent relative amounts of 10⁻¹².
  - This scale is set by B1788's 40-digit check, which matches the instrument to 10⁻¹², and by e20c's T-law spreads,
    at most 1.4 × 10⁻¹⁰π.
  - σ_D is the largest σ̂ over a centre's 13 points. C0(f) checks the estimate against an exact shift.
- **A valid centre for a quantity** meets four conditions:
  - no factor of the quantity vanishes at any of the 13 points:
    - |Σ_x| > 10⁻¹⁴·Σ_s |(2πL + c_s)R_s²|;
    - |u_x·h_x| > 10⁻¹⁴·Σ_s |u_s h_{x,s}|;
    - |h_x·h_x| > 10⁻¹⁴·|h|²;
  - for each factor separately (the pair (h̄·h̄)(h·h), which cancels exactly, is skipped), the wrapped differences between
    neighbours around each hexagon sum to less than π in absolute value;
  - each factor's wrapped differences from the centre are less than π/2 in absolute value;
  - the clamp pattern is shared.

  For the cells that ask for J ≠ 0 (H1, H1b, H2, H3) there is a fifth condition: |J| > 10⁻⁹ at τ_c. Exclusions are
  labelled "|J| < 10⁻⁹ at τ_c" and counted, not called J ≡ 0.
- **A valid centre's class:**
  - **Un** (noise-limited): σ_D > 10⁻⁹;
  - **N** (non-harmonic): |D(r₁)| > 10⁻⁶ and D(r₁)/D(r₂) ∈ [3, 5];
  - **H** (harmonic): |D(r₁)| < 10⁻⁸ and σ_D ≤ 10⁻¹⁰;
  - **H′** (harmonic at the stencil's resolution: the r⁶ scaling of a nearby zero): D(r₁)/D(r₂) ∈ [30, 250] and
    |D(r₂)| ≥ 100·σ_D;
  - **U**: otherwise.
- **The verdict on a combination** (reading, Higgs, line, horocycle; for θ_M the line, at L_max):
  - **NOT HARMONIC:** at least one N centre;
  - **HARMONIC:** no N, at least three valid centres that are not Un, and all of those H or H′;
  - **UNDETERMINED:** otherwise, if some valid centre is not Un;
  - **NOISE-LIMITED:** every valid centre is Un;
  - **NO READING:** no valid centre, counted by reason (|J| below the cut, a vanishing factor, a winding, a difference past
    π/2, a clamp mismatch).
- **"With a reading"** means NOT HARMONIC, HARMONIC or UNDETERMINED.

## 5. The cells

| cell | statement | prior |
|---|---|---|
| **H1, THE DECISIVE CELL** | in the two Higgs-phase-free readings, (S̃, S) and (S, S̃), pooled (2 × 10 Higgs × 296 lines × 2 horocycles), no combination is HARMONIC, and at most 1% of those with a reading are UNDETERMINED | 85% |
| H1b | the same in the other two readings, (S, S) and (S̃, S̃), pooled | 85% |
| H2 | in the Standard Model's reading, the horocycle enters θ̄: in at least 95% of the (line, Higgs) pairs with a centre valid at both horocycles, θ_Y(L_max) and θ_Y(L_2) differ by more than max(10⁻⁶, 1000·σ̂) at some such centre; the exceptions are listed | 85% |
| H3 | the conjugate Higgs suffices to break harmonicity: with frozen weights, the Standard Model's reading is NOT HARMONIC on at least 90% of its combinations with a reading | 80% |
| H4 | the computed norms suffice to break it: θ_M (one per line, at L_max) is NOT HARMONIC on at least 90% of the lines with a reading | 70% |
| C0 | the controls (a)–(f) below | 90% |

**The controls.** Each runs only on the centres valid for its quantity.
- **(a)** The closed form against the LU determinant, at the centres valid for θ_Y in the Standard Model's reading with
  σ_D ≤ 10⁻⁹: |Δdet| ≤ 10⁻¹²·σ₁³, where σ₁ is Y's largest singular value.
- **(b)** Rank one on the frame's values: |Σ_s R_s²| ≤ 10⁻⁹·Σ_s |R_s|² at every evaluated point, both sectors (B1788
  found 5 × 10⁻¹¹).
- **(c)** The Higgs's overall phase, h → e^{iφ}h (φ = 0.3, 1.1, 2.0), at the first valid centre of each line (in the
  centres' fixed order), for each reading: |wrap(Δθ_Y − expected)| ≤ max(10⁻⁹, 10·σ̂). Expected: 0 in (S̃, S) and (S, S̃),
  6φ in (S, S), −6φ in (S̃, S̃).
- **(d)** The floor. With frozen weights in the reading (S, S), every factor is holomorphic. No valid case may be classed N
  there.
- **(e)** The power. At least 80% of the frozen (S, S) combinations with a reading are HARMONIC. If (e) fails, the first
  clause of H1 and of H1b ("no combination is HARMONIC") is reported as untested, for want of power. That alone stops no
  other cell.
- **(f)** The noise model. At the 60 calibration points, in the Standard Model's reading with dR, F₆ and F₂₂ at both
  horocycles: |wrap(θ_Y(τ_c + 1; b − α) − θ_Y(τ_c; b) − 19π/50)| ≤ 10·max(σ̂ at the two points) + 10⁻¹².

**The stop rule.** A failure of (a), (b), (c), (d) or (f) stops the reading of every cell until it is resolved post hoc,
labelled.

**Read-outs (no cell):**
- **The scaling, a diagnostic:** among the centres with σ_D ≤ 10⁻⁹ and |D(r₁)| > 10⁻⁶ (θ_Y, Standard Model's reading),
  the fraction with D(r₁)/D(r₂) ∈ [3, 5].
- **The record's best six-rows:** θ_Y, θ_H, θ_M and J, in the Standard Model's reading with dR at L_max, in the
  representative as stored (b as stored, Re τ as stored). These are the values a constant θ₀ would have to cancel there.
  The rows:
  - B1726's (0.55 + 3.05i on (2/5, ½), as e20 read it);
  - B1749's (its comparison.json, best_six seat: line 151 of B1726's list at 0.605263158 + 3.025858…i);
  - B1786's two tied rows ((2/5, 23/30) at 0.2692… + 3.0375…i and (2/5, 5/6) at 0.7308… + 3.0375…i, from its
    comparison.json at 54cfec661).
- **The size of the non-harmonicity:** per slope class, the median over N centres of 4|D(r₁)|/r₁² (≈ |Δθ|), for θ_Y, θ_H
  and θ_M (Standard Model's reading, dR, L_max).
- **The counts:** every verdict class, with the reasons for NO READING, and the clamps.
- **Every HARMONIC, UNDETERMINED or NOISE-LIMITED combination,** listed in full.

## 6. What each outcome means (written now)

- **H1 holds (with C0 and (e)).** On every NOT HARMONIC combination (n of the m with a reading, counted), no counterterm
  holomorphic in τ makes θ̄ constant on any open set of τ that contains a non-harmonic centre. So θ̄ is not identically
  0 or π along those lines in either Higgs-phase-free reading.
  - **What this does not cover:**
    - the UNDETERMINED, NOISE-LIMITED and NO READING combinations, which are listed;
    - Higgs directions outside the ten;
    - counterterms not holomorphic in τ;
    - θ̄ = 0 at a fixed τ or along a curve, which would be a condition on τ, not a derivation.
  - **What it means for θ̄:** the frame as built does not fix θ̄ on the covered combinations. θ̄ stays an input: θ₀, tuned
    against θ_Y at the physical point to the measured 10⁻¹⁰, or one real equation on (τ, line).
  - P-323's answer, on the covered combinations: none. It bears on P-267 (θ̄ a post hoc candidate only), I-18 and P-277.
  - No input removed. 0 of 19.
- **H1's first clause fails (some combination HARMONIC):** those combinations are listed and become P-323's next step,
  under a new sealed rule: the characters' counterterm, the zeros of det Y in the strip, constancy of θ̄, the CP points
  (P-328), then the six on those lines.
  - A HARMONIC verdict is necessary for a constant θ̄, not sufficient. Nothing is removed by it.
- **More than 1% UNDETERMINED:** H1 is not decided on them. They are listed, and no reading is drawn from them.
- **(e) fails:** "no HARMONIC" is untested for want of power, and only the NOT HARMONIC combinations are read.
- **H2 holds:** the hand-set horocycle enters θ̄, through θ_H only (θ_M's freedom from the horocycle is analytic given rank
  one, C0(b)). One more place where an input that main's plan names as hand-set reaches a value.
- **H3 and H4:** each tests whether one ingredient alone suffices to break harmonicity, the conjugate Higgs or the
  τ-dependent norms. Both can hold. Either can fail without changing H1's reading.
- **A control failing** (the stop rule): no cell is read until it is resolved post hoc, labelled.

## 7. Seen first, and disclosed

**Seen before this rule** (this seat's own work):
- e20 (3e05a0be6, b50efdab5):
  - the Higgs phase's cancellation;
  - θ_Y = +0.1774π at B1726's best six-row;
  - θ_Y at Re τ 0.35 and 0.85 on that line, and at 0.3145 + 3.0345i on (2/5, 1/10). The three values on (2/5, ½) give
    ∂²θ_Y/∂(Re τ)² ≈ 1.7π, half of a Laplacian, so the prior is informed by it;
  - the T-law's shifts;
  - J and θ_Y on the CP lines at Im τ 2.2, 2.6, 3.03 and 3.4.
- e20b–e20d (c4ed82945, dbdc1d958, 7f419bc47, 501a7e5d8, 377dc3238, f66883040):
  - the characters on the ten (2/5, k/10) lines and on (1/3, 1/5), with their spreads (at most 1.4 × 10⁻¹⁰π);
  - b → b ± 1;
  - J's zeros at half-integer Re τ (P-328's rule), where θ_Y is constant in Im τ.
- **Frame values stored near or inside some stencils, as moduli only** (ratios, |V| and J; no phase):
  - this seat's zero-free and two-ingredient censuses at 0.1 + {2.4, 2.9, 3.4}i, inside the r₁ hexagons of the
    Re τ = 0.15 centres;
  - the sealed zero_free_holomorphic census at 0.15 + {2.35, 2.85, 3.35}i, 0.025 from three centres and inside their r₂
    hexagons, and at 0.6 + {2.35, 2.85, 3.35}i, inside the r₁ hexagons of the Re τ = 0.65 centres;
  - e20's 1.2 + 3.4i, which the T-step maps to 0.2 + 3.4i, inside the r₁ hexagon of 0.15 + 3.375i.
  
  None of these decides a cell: every cell reads a phase's circle mean.
- **Other inputs to this rule:** the identity check of § 2 (random inputs only), one timing call of `channels()` at
  0.05 + 1.05i on the line (0, 0) (its values not printed), and this seat's mechanics tests of the draft script on
  synthetic random arrays (no frame value).
- **Never computed before this rule:** no circle mean, Laplacian or other harmonicity measure of any phase, and no phase
  of det Y at any stencil point.

**The record:**
`VERDICT topic-sweep /theta.?bar|θ̄|strong (CP|angle)|arg ?det|counterterm|CP.?even|anomal/: 50 of 1535 arcs on main match (NEGATIVE 5, OPEN 7, PROVED 38); 17 register rows match (DONE 9, QUEUED 8); 21 other lanes match`
(run on main at 54cfec661).
- Bearing on it: B1246 (I-18 reaches θ, not θ̄); B1662 and P-274 (θ̄ ∈ {0, π} by the side chosen on the ruled branch);
  B1671 (the Dedekind phase); B1674 (with the counterterm θ̄ is a free constant θ₀; without it θ − π Re τ); P-267 (zeros
  and poles only at the end; its prior art arXiv:2505.20395); P-277 and P-328 (CP from a potential; the CP lines); P-357
  and P-364 (the Higgs's invariant; the closed form of det Y).
- Since then main's B1790 (S226, ccc09ec7c): the coupling is complex-bilinear in a holomorphic Higgs and matter, and a
  derivation of the reading needs an antiholomorphic or Hermitian Higgs slot. That bears on H3's conjugate Higgs.
- None asks whether θ_Y is harmonic in the mass frame.

**Literature:** the papers cited in § 1. In them θ̄ = 0 needs holomorphic Yukawas, CP imposed, and no zeros or
singularities away from special points (2505.20395's assumption). No paper treats B1656's frame.

## 8. The order

This rule is committed and pushed before the script exists. The script (`p323_strong_angle.py`) is committed before its
run, in two stages:
1. **the census**, resumable in chunks: R_s and c_s for the up and down sectors, L at both horocycles and the ten Higgs
   directions, at the 23 088 stencil points, the 60 calibration points and the read-out rows;
2. **the cells**, from the census.

The census's output is committed before the cells are computed, and the cells' output before it is read. A failed launch
is kept and disclosed. A post hoc step is labelled.

0 of 19.
