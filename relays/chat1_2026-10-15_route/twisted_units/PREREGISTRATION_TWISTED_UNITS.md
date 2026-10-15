# THE TWISTED UNITS ON THE LOW THREADS — preregistration (chat1; sealed before the run; one run)

chat1 (the web seat), 2026-10-15/16. **Pre-seal reviewed** by a read-only referee. Its blocker and fixes are taken;
they are listed in §1.
- **Committed together before the run:** this file, `twisted_units_seal.py`, `tlow2.py`, the two received data files,
  `null_draws.py` with the regenerated `null_draws.json` and `null_draws_run.txt`, and the validation scripts in
  `validation/` with their runs.
- **forms.pkl** (sha256 `64a40c036050c142…`, from `m003_exploration/instrument/build_forms.py`) is passed by path. Its
  sha256 is recorded in the output.
- The script runs once, and its output is committed before anyone reads it.
- **Nothing at N = 9, 11 or 12 has been computed before this seal.**

0 of 19.

## 1. Why this arc, and what changed since the design draft

- **The owner's rulings**, as chat1 reports them and as the SM seat reported them (§133):
  - the SM seat builds the twisted units, and chat1 seals both readings before any comparison;
  - the SM seat checks it blind after the seal, before reading chat1's run.
- **Main's answer to P-108** (S133, S134): the per-field reading is main's construction. The minimal reading is sealed
  too, as the alternative.
- **What changed since `DESIGN_DRAFT.md`, each with its reason.**
  1. **The primary claim moved from T-tower to T-low.**
     - The per-field cusp law (the 19:41 addendum) bounds m₂/m₃'s exponent below by ½ in every sector, in both
       readings. The bound holds in C1 and the E4 cells where Y is generic, at odd N, and is read at excluded orders.
     - That law was refined post hoc and confirmed out of sample, at excluded orders only.
     - So on the least-volume closing threads the six-ratio comparison fails for the Standard Model and for every null
       assignment alike, and it cannot discriminate.
     - T-tower stays as a read-out of the law's leading exponents (§7).
  2. **Closure uses the Higgs conjugated:** c(q_L² + q_R² − q_H²) ≡ 0 mod N (§133). The configuration set uses
     c ≡ 0, which closes for every charge and either sign.
     - At N = 12 the closure law is not established. The instrument tests closure on every configuration, and a
       configuration-cell that fails counts as not passing.
  3. **The null has M = 199,** drawn in a fixed order (seed 20261015) from gauge-invariant assignments with |q| ≤ 18.
     - **Eligibility.** Each draw must be eligible at N = 9, 11 and 12 on the Standard Model's terms:
       - the sectors split;
       - no sector is untwisted;
       - it is not ≡ k·SM;
       - **no field's charge is ≡ 0 mod N.**
     - **Why the last condition (the referee's blocker).** A matter field with charge ≡ 0 mod N has an exact zero in the
       per-field reading, since R = FM12[1], E4F[1] = E4·R and R·R = 0. A right field gives the zero in C2/E4 and
       C3/E4; a left field in C3/E4 and C3/ORTH. The Standard Model has no such field at these orders, so without the
       condition the null would be handicapped.
     - **The box.** The draft's box was |q| ≤ 12, which leaves only 132 such draws, too few to reach p ≤ 0.05/8.
       |q| ≤ 18 gives 224.
     - **Cost:** 109–123 s per configuration for 200 assignments in both readings, measured at N = 8 and 10.
  4. **r_calc is the change of the singular values** between Npts = 30·P and 37.5·P. Measured on the rank-three cells
     of closing configurations at N = 8 and 10, it is zero in double precision.
     - The 53-bit coefficient check is run for the Standard Model only. It is reported only and enters no acceptance
       rule.
  5. **THETA2's completion does not apply to dressed units** (W92 V7), so the per-field reading has five cells and the
     minimal reading seven.
  6. **W94's relation is a read-out, not a blind test.** The thread frame makes no prediction of it.
  7. **The configuration set is fixed by algebra.**
     - The draft admitted only threads that closed. Here closure failures count as not passing.
     - The draft's excluded-order coincidence control is replaced by the instrument's validation, run before this seal
       and filed in `validation/`. That validation is:
       - against `units_cells.py` to 10⁻⁵²;
       - against the stage-1 instrument;
       - the constant-phase identity;
       - convergence;
       - rotation invariance;
       - the dry runs.

## 2. The question

On the thread frame's low closing threads at N = 9, 11 and 12, do the cells' mass ratios with the Standard Model's
hypercharge charges meet the data under W66's predicate more often than other gauge-invariant charge assignments do?
- In the per-field reading: this is the primary claim.
- In the minimal reading: this is a read-out.

## 3. Premises

- **H-thread:** couplings are cycle integrals along the vacuum's closed geodesic (W72; chat1's thread frame).
- **The vacuum's thread is a T-low configuration:** a (word, line) pair with
  - a Lyndon word in L and R of length ≤ 12, at height ≤ 3;
  - a line of exact order N ∈ {9, 11, 12}, fixed up to sign by the closure law's action (a, b) → (aD + bB, aC + bA)
    in the word's own marking;
  - N² | Q_γ(w).
- **The configuration list** is `tlow_configurations.json`, made by pure algebra in `tlow_enum.py`:
  - N = 9: 18 configurations;
  - N = 11: 40;
  - N = 12: 32;
  - 90 in all, on 21 words.

  The instrument carries each line into the rotation it integrates over (`line_in_rotation`).
- **The units, Higgs modes and couplings:**
  - **Units:** W72's untwisted units, from the SM seat's code at `87cf7f55` via `forms.pkl`, sha256 in the output.
  - **Per-field reading:** W92's z-form dressing
    D_c(q) = [e^(iπ(α²τ + 2αβ))·θ_s(β + ατ)]²/θ_s(0)², with (α, β) = (q·lb/N, q·la/N), on every unit and Higgs mode, by
    its field's charge. R is neutral.
    - Taken per residue q mod N. D(q) and D(q mod N) differ by one constant phase on every component, which no singular
      value sees.
    - Verified: the raw Y differ from the tower instrument's by exactly that phase, uniformly to 10⁻¹⁶.
  - **Minimal reading:** B1656's coupling vector at the actual charges, W91's object, agreeing to 2.3 × 10⁻⁵⁰ at the
    excluded orders.
  - **The pairing per sector:**
    - up: (Q, u^c) with H (+3);
    - down: (Q, d^c) with H̄ (−3);
    - leptons: (L, e^c) with H̄.
- **The read-out convention (I-33):** singular values ascending are generations 1, 2, 3. V = U_upᴴ·U_down, from the left
  singular vectors in the cell.
- **The end condition is P4′.** The coupling vector is R (per-field) or B1656's vector (minimal), without P4's
  √(2πL + c_r). P4 changes the ratios at O(1/L).
- **Redundancy.** Up to word reversal and the L↔R mirror, the 21 words fall into 8 classes: 2 at N = 9, 2 at N = 11 and
  4 at N = 12.
  - Reversal gives conjugate couplings (W86), so orbit members repeat masses.
  - The pooled count weights each class by its orbit. The p-value is unaffected, since every assignment is counted on
    the same set.

## 4. What is computed (one run of `twisted_units_seal.py`)

- **Controls first, at excluded orders.** The configurations are LLRRRLRLRLRR (6, 3) at N = 10 and LLLRLLLRLR (1, 7) at
  N = 8.
  - Each must give closure below 10⁻²⁰ and r_calc below 10⁻⁶.
  - **Rotation invariance:** the masses from a second rotation, with the line carried into it, agree to 10⁻²⁰ in ln s,
    compared at the working precision.
  - **The negative control:** on a rotation that moves the line (the best one or the second), the uncarried line must
    fail closure (above 10⁻³).
  - **If any control fails, the run stops before any N = 9, 11 or 12 configuration.**
- **For each of the 90 configurations:**
  - ball arithmetic at bits = 2π·2.6·height/ln 2 + 140;
  - Npts = 30·P and 37.5·P, where P is the hyperbolic length of the period;
  - all 200 assignments (the Standard Model and 199 null);
  - both readings, all cells.
  - The Standard Model is also run with its coefficients rounded to 53 bits.
- **Acceptance per configuration-cell.** A configuration-cell is accepted when all three sectors meet every condition:
  - closure of every Y integrand below 10⁻²⁰;
  - r_calc at most 10⁻⁶;
  - no zero singular value (s₁ > 10⁻³⁰·s₃);
  - positive-definite norm matrices;
  - distinct singular values.

  A cell that is not accepted counts as not passing, by cause, and is never dropped. A configuration that raises an
  error counts as no pass for anyone, and is reported.

## 5. The scoring: W66's predicate as W88 used it (a = 0.10)

- **Data, at M_Z:**
  - masses: `received_HZ2021_running_masses_MZ.json`;
  - CKM: `received_B1612_data.json`.

  Both are copied unchanged from the SM seat's branch at `2d3ea1842`; their sha256 values are in the output.
- **Each equality is scored by W66's predicate:**
  z = (ln X_calc − ln X_data)/√(r_calc² + r_data² + a²), with r_data from the masses' σ.
- **S-mass:** R₁ = m₁/m₃ and R₂ = m₂/m₃ in three sectors. It passes if Σz² ≤ 12.592 (6 degrees of freedom, 95%).
- **S-shape:** ρ = ln R₁/ln R₂ per sector, with W88's r_ρ. It passes if Σz² ≤ 7.815.
- **S-ckm:** |V_us|, |V_cb| and |V_ub|. It passes if Σz² ≤ 7.815.
- **The count:** for each assignment, the accepted configuration-cells that pass.
- **The p-value:** p = (1 + #{null assignments with count ≥ the Standard Model's})/(M + 1), with M = 199.

## 6. The claims

- **PRIMARY.** S-mass, per-field reading, pooled over all 90 configurations and five cells (450 configuration-cells).
  - **Earned** if the Standard Model passes at least once and p ≤ 0.05.
- **Eight read-outs, each earned only at the Bonferroni level p ≤ 0.05/8.** With M = 199, a read-out reaches that level
  only if no null assignment equals or exceeds the Standard Model's count.

  The read-outs are:
  1. S-mass, minimal reading, pooled;
  2. S-shape, per-field, pooled;
  3. S-shape, minimal, pooled;
  4. S-ckm, per-field, pooled;
  5. S-ckm, minimal, pooled;
  6. S-mass, per-field, N = 9 alone;
  7. S-mass, per-field, N = 11 alone;
  8. S-mass, per-field, N = 12 alone.
- **Reported, not scored:**
  - the Standard Model's per configuration-cell values and z's;
  - **W94's ratio** (m_μ/m_τ)/(m_s/m_b) per configuration-cell, in both readings;
  - **T-tower** (§7);
  - the acceptance failures by cause;
  - **N = 12 split by W92's odd-structure feature.** At N = 12 a charge ≡ 6 mod 12 loses one component of every
    primitive line's dressing. The Standard Model's e^c has it. The nulls with and without it are reported apart.

## 7. T-tower: the law's read-out

For N = 9 and 11 (odd) and every line class lb, the per-field cusp law's leading exponents of m₂/m₃ and m₁/m₃ per sector,
and ρ, in C1 and the E4 cells. They are computed by the law, not by the instrument. There is no score: the law predicts
S-mass fails there (§1.1).

## 8. Priors (chat1's, stated before the run)

- **PRIMARY earned: 7%.** Every size-free relation on record has failed. Here the sizes come from the thread's height,
  and the null calibrates the look-elsewhere effect.
- **Read-out 1 (minimal) earned: 3%.**
- **At least one Standard Model pass of S-mass, per-field, anywhere: 30%.**
- **S-shape, per-field, earned: 10%.** The a = 0.10 allowance on ρ is generous.
- **S-ckm earned in either reading: 5%.**

## 9. What the outcomes would mean

- **PRIMARY earned.** The per-field thread frame, on a low closing thread, gives the Standard Model's mass ratios more
  often than other charge assignments do.
  - It would be a candidate fit with every discrete choice (N, word, line, cell) counted, sent to main as a candidate
    and not as a relation.
  - The SM seat's blind check comes first.
- **PRIMARY not earned with no Standard Model pass.** That excludes the per-field thread frame on T-low as enumerated,
  under H-thread, and nothing wider. "As enumerated" means:
  - Lyndon words to length 12, at height ≤ 3;
  - N = 9, 11 and 12;
  - five cells, under P4′;
  - W72's units dressed by W92.

  It does not exclude the fibre frame, other selections of the thread, or other units.
- **PRIMARY not earned with passes at the null's rate.** That is look-elsewhere, not evidence.
- **A read-out earned alone.** It is reported as such, and stays below the primary claim.

## 10. Seen before this seal (disclosed)

- The data's log-ratios, 2.11, 1.75 and 2.89 (§117), and the masses' sizes.
- At excluded orders only:
  - the minimal and per-field towers;
  - the per-field law, including its frozen prediction's partial failure and its post hoc refinement;
  - instrument checks at N = 3, 5, 7, 8 and 10, including cost and convergence on 200 assignments at N = 10 (masses,
    no score);
  - the scorer's code paths, on synthetic masses relabelled N = 9;
  - `tower_law()`, executed in the dry run with only its keys printed.
- **Not seen:** any N = 9, 11 or 12 mass, and any score on real masses.

## 11. After the run

1. The output is committed before the read-out.
2. Scored as sealed, then refereed read-only.
3. Relayed to the SM seat, whose blind check comes before it reads the output, and to main.

chat1. 0 of 19.
