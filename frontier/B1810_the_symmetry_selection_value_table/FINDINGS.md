# B1810 — THE SYMMETRY-SELECTION VALUE TABLE (P-432, FIRST HALF; DATA-FREE): THE FRAME'S OUTPUTS AT THE FOUR CONFIGURATIONS THE OBJECT'S SYMMETRY FIXES, FOR TABLE T's DIRECTIONS AND B1730's COMPLETE ONE-UNIT FAMILY (13 DIRECTIONS, 832 ROWS, 206 DISTINCT OUTPUTS). UP AND DOWN COINCIDE THERE UP TO PHASE (B1703: N ∣ 6). AT ω EVERY DIRECTION FALLS ON A STABILISER EIGENLINE AND THE OUTPUT IS (0, 1) OR RANK ONE. AT (i, 0) EVERY LISTED DIRECTION SHARES ONE LEFT EIGENBASIS, SO V IS A PERMUTATION. ON THE 2-TORSION LINE AT i THE FIRST GENERATION IS MASSLESS FOR EVERY LISTED DIRECTION BUT DR, AND A SPLIT READING GIVES ONE ANGLE OF ORDER 1/L, A PERMUTATION AS L → ∞. THE DIRECTIONS FORM AN INFINITE DISCRETE FAMILY, SO THESE "PARAMETER-FREE" OUTPUTS ARE A COMB INDEXED BY A DISCRETE CHOICE

**Verdict: PROVED** (a computed table and its structure). Data-free: no frame value was compared with any data. P-432's
first half; the second half is the sealed comparison. cc (main), 2026-10-29, the owner's ruling. Corrected before landing
at its hostile referee (§ 6): two blocking findings.

**0 of 19.**

## The frame card (WORKING_RULES, the rule of 2026-10-29)

| item | value | label |
|---|---|---|
| frame | B1656's flat fibre frame (FR-FIB, B1809): four-channel coupling, zero line or a flat line | CHOSEN (the frame) |
| configurations | (i, 0), (ω, 0), (i, (½, ½)), (ω, (⅓, ⅔)); lines up to sign; ω taken as e^{iπ/3} (B1667's point) | FORCED given the frame (B1809 § 2: exactly the configuration-fixed points; the frame's line convention verified, the referee's rf6b) |
| end radius | L = L_h(τ), B1667 (line-independent by construction) | FORCED (canonical construction) |
| horocycle h | max, 2 | CHOSEN |
| reading | each sector S or S̃ (eight), B1790 | CHOSEN (not derived, B1790) |
| direction | DR, a₀, R, t = −5/288 (B1809's Table T), and B1730's zero-free F_a at n = 1: a ∈ {−10, −6, −2, 2 (= R), 6, 10, 14, 18, 22, 26} | ADMITTED: an infinite family; n = 2 adds a from −22 to 50, not tabulated |
| sectors | up (1, −4), down (1, 2), leptons (−3, 6) (B1656) | FORCED given the hypercharges |
| outputs | per sector (m₁/m₃, m₂/m₃); the full 3×3 ∣V∣; J; a degeneracy flag (V undefined where a sector's singular values coincide to 10⁻⁸) | — |
| null | not here; the sealed half's (it must range over the direction family, the horocycle and the readings) | — |

## 1. The table (`verification/symmetry_selection_table.py` → `.json`; the record's machinery read-only)

- **The controls are asserted in the script**, and they reproduce B1809's Table T and the first referee's line values:
  - (i, 0) at L₂: DR (0, 1); a₀ (0.0753, 0.658); R (0, 0.01907).
  - (i, (½, ½)) with DR: (0.0381, 0.519).
- **The counts are computed in the script.** Values below 10⁻⁹ are set to 0 and the rest rounded to 5 significant
  figures.

| configuration | distinct outputs (masses) | (masses and V) |
|---|---|---|
| (i, 0) | 161 | 161 |
| (ω, 0) | 2 | 2 |
| (i, (½, ½)) | 16 | 44 |
| (ω, (⅓, ⅔)) | 2 | 2 |
| all | 178 | 206 |

- **V and J.**
  - V is defined in 400 of the 832 rows: every row at i except DR at (i, 0), which is the degenerate (0, 1).
  - It is a permutation in 320 of them, tested on the full 3 × 3.
  - J vanishes wherever V is defined (largest 1.6 × 10⁻³¹). That is implied: every V here has a vanishing entry. It is
    also B1809 FR-FIB's J = 0 on mirror-fixed configurations, and all four are mirror-fixed.

## 2. The structure (the referee's mechanisms, verified on main)

1. **Up and down coincide up to an overall phase at every configuration here.** This is B1703: u = d iff N ∣ 6, on every
   line of order dividing 6, at every τ. It is not new. The leptons coincide with up on the 2-torsion line and are
   untwisted on the 3-torsion line. So up and down differ only through the reading.
2. **At ω every listed direction lies on one of the order-3 stabiliser's three eigenlines.**
   - (1, −1, 1): DR and F₆ give (0, 1).
   - The two complex lines give rank one (B1618).
   - The reading swaps the two complex lines, so the ω rows carry two outputs.
   - The residual m₂/m₃ ≤ 1.2 × 10⁻¹³ is the quadrature's asymmetry, scaling as 1/(2πL + c) (the referee's rf8).
3. **At τ = i every listed direction except DR is a ∝ (1, 1, iκ) with κ real.**
   - κ = 2^{a/4} times F_a's sign; a₀ has κ = 2^{−1/2} (= F₋₂); R and t have κ = ∓√2.
     > *2026-10-30 (B1824, PROVED): a₀ = η⁴F₋₂/6 at every τ, not only at i, so a₀ and F₋₂ are one direction and the
     > thirteen listed directions are twelve distinct; on this table their 64 row pairs agree in every mass ratio to
     > 1.6 × 10⁻¹⁶ (and in ∣V∣ and J where V is defined).*
   - The menu at i is therefore a geometric ladder in κ, with a symmetry κ → 2/κ. That is why a₀ ≡ F₆ there, and also
     F₋₆ ≡ F₁₀ and F₋₁₀ ≡ F₁₄.
   - **(i, 0):** the coupling's left singular basis does not depend on κ (to 10⁻¹³ over 48 values, the referee's rf3).
     So V is a permutation for every pair of listed directions and every reading.
   - **(i, (½, ½)):** R_k = 0 and R_i = −R_j, and the I and J components of every (1, 1, iκ) are equal. So B1659's
     factor tr(εSMᵀ) in det Y vanishes, and **m₁ ≡ 0 for every listed direction but DR.**
     - The spectrum is even in κ, so the reading never changes the masses there.
     - The reading acts as κ → −κ. A split reading gives V = (a 2 ↔ 3 swap) × (one rotation by θ), with
       cos θ = ∣⟨n(κ), n(−κ)⟩∣, n being the massless left state.
     - **θ is a finite-radius effect.** For a₀'s class it is 0.101 at L₂(i), 0.00584 at L = 40 and 9.0 × 10⁻⁵ at
       L = 2560, about 0.23/L (computed in the script). In the L-free coupling, V is a permutation here too.
     - At L_max it is steep, because the 1-channel's weight 2πL + c₁ vanishes at L ≈ 0.617.
     - The 80 such rows carry 24 distinct ∣V∣ matrices.

## 3. What it means (data-free)

- **The table is restrictive before any comparison.** At the configurations the object's symmetry fixes:
  - up and down differ only through the reading;
  - J = 0;
  - V is a permutation, except one angle on the 2-torsion line at i. That angle is of order 1/L and comes with a massless
    first generation in every sector.
- **"Parameter-free" needs a qualifier.** The directions are an infinite discrete family (B1730: a ≡ 2 mod 4, without
  bound as the end data n grows). At i they form a ladder in κ, and the outputs are a comb indexed by it. A sealed
  comparison has to treat the direction as a discrete choice and range its null over the same family (the n = 1 window,
  stated in advance), not over hand-kept members.
- **For P-432's second half,** the menu is 206 distinct outputs at n = 1. Its look-elsewhere count follows from that, not
  from the row count.
- **0 of 19.**

## 4. Scope

- The four configuration-fixed points; B1667's radii; n = 1 for the F_a family.
- The F_a lie outside H-cov's proofs (B1730; the census referee).
- The table is numerical: the referee's independent route reproduces sampled rows to 5 × 10⁻⁷, the 6-figure rounding.

## 5. Disclosed

- **Before landing.**
  - The first two launches used 8 directions and stored only three ∣V∣ entries.
  - The draft's "distinct mass patterns" (114/128/110/128) counted floating-point noise.
  - The draft's "the record's eight parameter-free directions" omitted B1730's n = 1 members.
  - All three outputs are kept (`_first_launch`, `_second_launch`).
- **The list's provenance.** F₆ and F₂₂ entered the record through B1742's data-informed fit. Here the list is B1730's
  complete n = 1 basis, chosen by that rule.
- **Constants seen.** While reading the comparison script's interface for the second half, main saw two of its built-in
  constants (J_PDG and the P-094 target), both on record. Nothing in this table was compared with them.

## Seen first

**The sweeps.**
- `VERDICT topic-sweep /symmetry.selection|configuration.fixed|value table|permutation.{0,30}mixing/ (full text): 8 of
  1556 arcs, 2 register rows` (the referee's).
- The 2-torsion regex: 55 arcs.
- The sector-coincidence regex: 7 arcs, including B1703.

**Bearing on it:**
- B1703 (u = d iff N ∣ 6);
- B1659 and B1716 (the determinant's factors, the exact zeros);
- B1739 (a split reading misaligns the light states);
- B1730 (the F_a family);
- B1618 (ω's degeneracy);
- B1809 (the census, Table T);
- P-153, P-173, P-224, P-295, P-312, P-345.

**Literature:**
- the residual-symmetry argument for mixing at symmetric points (named on record as P-224's; Lam's papers not read on the
  bench);
- modular-flavour fixed points (Novichkov–Penedo–Petcov; Feruglio et al.).

## 6. The referee (hostile, read-only; `verification/referee/`)

- **Verdict:** BLOCK on two findings, both applied.
  - The pattern counts were noise; they are now computed in the script.
  - "Tabulated in full" and "the record's eight directions" were false against B1730; the family is now completed at
    n = 1 and its infinitude stated.
- **Corrections applied:**
  - fact 1 cited as B1703, "up to phase";
  - F₆ at ω gives (0, 1);
  - J restricted to rows where V is defined, and shown to be implied;
  - "the stabiliser no-go row by row" replaced by the mechanisms (the shared left basis at (i, 0); κ-evenness at
    (i, (½, ½)));
  - the angle's mechanism and its 1/L scope;
  - the full-V permutation test and the asserted controls in the script;
  - the 240 → 400 row description;
  - the frame card, labels, Disclosed and VERDICT lines.
- **Verified by the referee by an independent route:** sampled rows to 5 × 10⁻⁷; the four configurations exactly the
  fixed points; the frame's line convention; B1667's radii line-independent.
- **Main's verification:** the referee's rf1–rf9 regenerated on main; F₆ at ω, a₀ ≡ F₆ at (i, (½, ½)), B1703's statement
  and B1730's one-unit list checked against the table and the arcs.

## Dated note (2026-10-29, S252; B1811's referee, verified on main) — where κ → 2/κ holds

- § 2.3's "That is why a₀ ≡ F₆ there, and also F₋₆ ≡ F₁₀ and F₋₁₀ ≡ F₁₄" holds on the 2-torsion line (i, (½, ½)) (equal to
  6 × 10⁻⁴ relative), not at (i, 0), where a₀ and F₆ differ in the sector ratios by up to 2.35 relative (c/t 0.186 against
  0.148 under S̃). The left-eigenbasis statement at (i, 0) (V a permutation) stands.
