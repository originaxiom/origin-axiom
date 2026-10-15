# W97 — the rule, recorded before the code

The SM-derivation seat, 2026-10-15/16. Committed before the code that reads it exists. Nothing here is a result.

## Why this arc

- **chat1 sealed its comparison before running it** (0d83e6981, 2026-10-15 22:07 UTC): THE TWISTED UNITS ON THE LOW
  THREADS. It covers both readings of the hypercharge twist, on T-low's 90 configurations at N = 9, 11 and 12, for the
  Standard Model and 199 null assignments, scored by W66's predicate.
- **The owner's ruling (relay §133)** is that this seat checks it blind after the seal, before reading chat1's run. This
  seat promised that in relay §126 ("as W85 and W89 did for main"). Task 131.
- **Blind to chat1's output, not to its preregistration or instrument code.** This seat read three things, and no
  output:
  - the preregistration;
  - the configuration list's enumeration code;
  - the instrument's cell definitions.

  This seat will not read chat1's output before its own output is committed.

## Weave or thread?

- **A thread-frame result, read on each thread of a stated set (T-low), under H-thread.** Each configuration is one
  thread with one line. The set is a selection, not the weave.

## The scope (a declared subset of chat1's seal)

- **One reading:** per-field. This is chat1's primary reading: W92's z-form dressing on every unit and Higgs mode, R
  neutral.
- **One cell:** C1 = (3/2, 3/2) h5. The masses are the singular values of K_L^(−1/2) Y (K_R^(−1/2))ᵀ, ascending as
  generations 1, 2, 3 (I-33).
- **One assignment:** the Standard Model's 6Y charges. The sectors are:
  - up: (Q 1, u^c −4) with H (+3);
  - down: (Q 1, d^c 2) with H̄ (−3);
  - leptons: (L −3, e^c 6) with H̄.
- **All 90 configurations.**
- **Not reproduced:**
  - the minimal reading;
  - cells C2 and C3;
  - the null assignments;
  - the p-values;
  - the primary claim itself.

## The instrument (this seat's own, independent of chat1's)

- **The units.** W72's units F_i, F₊, F₋ (weight 3/2), R (weight −½) and h5 (weight 5/2) are rebuilt from this seat's
  code (`the_per_field_units.build_units`, section residuals about 10⁻⁴¹). They are evaluated by their series only in
  the standard fundamental domain.
- **The transport.** A point of the thread is reduced to the fundamental domain by τ ↦ τ − n and τ ↦ −1/τ. Each unit
  is carried back step by step with its own T and S matrices:
  - F(τ + 1) = M_T F(τ);
  - F(−1/τ) = (√τ)^(2k) M_S F(τ), with the principal square root.

  The matrices are fitted by least squares on the unit arc, where every series is valid.
  - This is not chat1's route. chat1 carries ratios to R by R's monomial map and evaluates R by explicit sums.
- **The dressing** is evaluated at the unreduced point by explicit theta sums with characteristics:
  D_c(q) = [θ[a_s + α, b_s + β](0 | τ) e^(−2πiα b_s)]² / θ[a_s, b_s](0 | τ)², with (α, β) = (q·lb/N, q·la/N) and
  s = (2, 4, 3) on (i, j, k).
- **The path is the axis of the word's own matrix** (rotation 0), with the line as listed and no carrying.
  - chat1 integrates on the rotation of least |C|, with the line carried. So agreement also tests rotation invariance.
- **The integrals:**
  - trapezoid in arclength over one period, with nodes at half steps;
  - Npts = ⌊30·P⌋ and ⌊37.5·P⌋, where P is the period's hyperbolic length;
  - 60 digits.
- **The configurations** come from this seat's own enumeration under chat1's stated definition:
  - Lyndon words in L and R of length at most 12 with both letters;
  - height √(t² − 4)/(2c) ≤ 3, with c = min(∣B∣, ∣C∣) over the rotations;
  - lines (la, lb) of exact order N, fixed up to sign by (la, lb) ↦ (la·D + lb·B, la·C + lb·A);
  - N² ∣ C·la² + (A − D)·la·lb − B·lb².

## Exploration before this rule (disclosed)

All of it was at excluded orders only, on chat1's two control configurations: LLRRRLRLRLRR (6, 3) at N = 10 and
LLLRLLLRLR (1, 7) at N = 8. It ran in scratch:
- the T and S fits, residuals about 10⁻⁴⁰ to 10⁻⁶⁰;
- the transport against direct series evaluation where both are valid, 4 × 10⁻⁴⁰;
- the closure of every integrand, in three sectors with the Standard Model's charges: 1.7 × 10⁻³⁸ and 1.1 × 10⁻³⁹;
- one full mass computation at N = 8, with a change between the two Npts of about 10⁻³⁹ and a cost of 0.09 s per
  point.

No quantity at N = 9, 11 or 12 was computed before this rule. This seat knows the data, as recorded since W88.

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **Q1, the configurations** | this seat's enumeration gives 18, 40 and 32 configurations on 3, 8 and 10 words at N = 9, 11 and 12, the same (word, line) set as chat1's `tlow_configurations.json` | 85% |
| **Q2, closure** | on every configuration, at one point and its image under the word's matrix, every integrand (K_L, K_R and Y in each of the three sectors) agrees to 10⁻²⁰ relative | 85% |
| **Q3, convergence** | ln(m₁/m₃) and ln(m₂/m₃) change by less than 10⁻⁶ between the two Npts, in every sector of every configuration | 90% |
| **Q4, no zero mass** | m₁ > 10⁻³⁰ m₃ in every sector of every configuration. W92's odd-structure zero touches the leptons' e^c (q = 6) at N = 12 on one component only | 70% |
| **Q5, agreement with chat1's sealed run** (evaluated after both outputs are committed) | for every configuration accepted in both runs: ∣Δ ln(m₁/m₃)∣ and ∣Δ ln(m₂/m₃)∣ ≤ 10⁻⁶ in every sector, Standard Model, per-field, C1 | 70% |

**The read-outs (no prior).**
- The Standard Model's S-mass under W66's predicate per configuration in C1, as chat1's §5 defines it:
  - z = (ln X_calc − ln X_data)/√(r_calc² + r_data² + a²), with a = 0.10;
  - the data are this seat's `received/HZ2021_running_masses_MZ.json`, the file chat1 copied;
  - pass if Σz² ≤ 12.592 over the six ratios.
- The number of passes.
- W94's ratio (m_μ/m_τ)/(m_s/m_b) per configuration.
- The masses by N.

These read-outs are seen-data numbers, not a test. chat1's primary claim needs its null and five cells, which are not
reproduced here.

## What the outcomes would mean

- **Q1–Q4 and Q5 as predicted:** chat1's sealed run, in its primary reading's first cell and for the Standard Model,
  holds on a second instrument with a different transport and a different rotation.
- **Q5 failing:** the two instruments differ.
  - The disagreement is diagnosed post hoc, labelled.
  - A convention found that way is disclosed, and the cell stays failed as worded.
  - chat1's scoring is not touched by this seat.
- **Q1 failing:** the configuration sets differ. The difference is listed, and Q5 is read on the common set.

## After the run

- Commit the output before any reading of chat1's output.
- Then read chat1's output, evaluate Q5, and record:
  - the weave dossier's NOTE (a section, a bullet, a table row and a files entry);
  - the state page;
  - a relay to chat1 and main;
  - the ledger;
  - CHANGELOG and PROGRESS_LOG;
  - a test.

0 of 19.
