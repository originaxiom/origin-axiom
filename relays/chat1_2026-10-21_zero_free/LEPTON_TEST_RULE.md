# The leptons at the quark-fixed τ under PF1-W (the rule, committed before the code)

chat1, 2026-10-21. Committed and pushed before the script that reads it exists. Nothing here is a result. 0 of 19.

## Why

- **The reading** (`THE_ZERO_FREE_READING.md`). PF1-W says the law's holomorphic invariants vanish only at the end.
  In the record's frame it makes W114's tunings forced, and θ̄ is then derived in three compatible quark assignments.
  But θ̄ = 0 was known, so that is a postdiction.
- **The first place PF1-W can predict.** A zero-dof quark fit fixes τ. Under PF1-W every lepton sector must be
  zero-free too: only w ∈ {0, 12} is admissible, with w = 12 on its variety. The run's R2 found every admissible lepton
  pair over-determined at a fixed τ, with 1 to 5 predictions each.
- **The stakes.**
  - A pass that the random-target control (L5) also supports would be the record's first unfitted lepton prediction.
  - A clean negative would refute PF1-W in this frame, under this rule's Weinberg assumption, for the leptons. The
    quark reading would stand or fall separately.
  - Either way the count of the nineteen does not move: the charged-lepton ratios are fitted, and the neutrino data
    are not among the nineteen.

## The frame (fixed now)

- **The SM seat's construction, unchanged** (W113's and W114's code at c9f001d9d, hash-checked as in
  `zero_free_checks.py`):
  - the triplet hands T and T̄;
  - the coupling spaces of type (s_L, s_R) and weight k, with W = η^m Y;
  - CP in the law, so the coefficients are real in the seat's real basis;
  - tree level and holomorphic.
- **PF1-W on every sector.**
  - A sector is admissible only at w = 3k − a/2 ∈ {0, 12}.
  - At w = 12 its coefficients lie on the zero-free variety, by W114's `SectorParam` root along a fixed direction.
  - The same holds for the Weinberg coupling, with the cubic restricted to the symmetric part.
- **Assumption A-W (chat1's, stated and not derived):**
  - The Weinberg coupling LLHH lies in the symmetric part of the (s_L, s_L) space at weight k. The two Higgs legs'
    weights are absorbed in k, as the seat absorbs one Higgs's.
  - No seesaw, no right-handed neutrinos.
- **The charged-lepton coupling** is the (s_L, s_e) space at weight k.
- **Excluded by qualitative facts, fixed now** (as W113's viability rule):
  - mixed at k = 0, the identity: degenerate charged leptons;
  - T⊗T at k = 1, dimension 1: B1636's sum rule, m₂/m₁ ≥ ½, against m_μ/m_τ = 0.059.
  - That leaves the ten (charged, Weinberg) pairs of R2. For L in T: T⊗T 5t or mixed 4t, each with symmetric T⊗T 1
    or 5t. For L in T̄: T̄⊗T̄ 3, T̄⊗T̄ 7t or mixed 4t, each with symmetric T̄⊗T̄ 3 or 7t.

## The quark-fixed τ (stage Q)

- **The assignments.** W114's 11 and 13 (zero dof, exact) and 14 (zero dof, χ² 2.55). Assignment 16 (dof −2) does not
  fix τ and is left out.
- **The search, per assignment.** W114's machinery (`random_starts`, `stage1`, `nm`, `Model.chi2`, a = 0.10), with:
  - 40 000 random starts (seed 2110 + assignment number);
  - Nelder–Mead from the best 200 (at most 6000 evaluations each), then once more from each endpoint;
  - every endpoint with χ² ≤ 3.84 kept.
- **The distinct τ\*.** Endpoints are mapped to F and identified under τ ~ −τ̄, since the lepton observables below are
  invariant under it and J only changes sign. Two τ within 10⁻³ are one τ\*.

## The leptons at each τ\* (stage L)

- **The observables,** six:
  - m_e/m_μ and m_μ/m_τ;
  - sin²θ₁₂, sin²θ₁₃ and sin²θ₂₃;
  - r = Δm²₂₁/|Δm²₃ℓ|.
  The two overall scales (m_τ and |Δm²₃ℓ|) are free and not fitted.
- **The extraction.**
  - The charged-lepton and neutrino left singular vectors are taken in ascending order, with rows L.
  - The mixing is P = U_e†U_ν.
  - **The ordering.** With n₀ < n₁ < n₂ the neutrino singular values, the ordering is NO if n₁² − n₀² < n₂² − n₁², with
    (ν₁, ν₂, ν₃) = (n₀, n₁, n₂) and r = (n₁² − n₀²)/(n₂² − n₀²). Otherwise it is IO, with
    (ν₁, ν₂, ν₃) = (n₁, n₂, n₀) and r = (n₂² − n₁²)/(n₂² − n₀²).
  - **The angles.** s₁₃² = \|P_e3\|², s₁₂² = \|P_e2\|²/(1 − s₁₃²) and s₂₃² = \|P_μ3\|²/(1 − s₁₃²).
- **The data.**
  - The charged-lepton masses: HZ2021 at M_Z (the seat's `received/HZ2021_running_masses_MZ.json`), with relative
    errors combined as W66 does.
  - The neutrinos: NuFIT 6.0, IC24 with SK atmospheric data (arXiv:2410.05380v2, Table 1, fetched 2026-10-21), with
    1σ symmetrised.

| | NO | IO |
| --- | --- | --- |
| sin²θ₁₂ | 0.308 ± 0.0115 | 0.308 ± 0.0115 |
| sin²θ₁₃ | 0.02215 ± 0.00057 | 0.02231 ± 0.00056 |
| sin²θ₂₃ | 0.470 ± 0.015 | 0.550 ± 0.0135 |
| Δm²₂₁ (10⁻⁵ eV²) | 7.49 ± 0.19 | 7.49 ± 0.19 |
| Δm²₃ℓ (10⁻³ eV²) | +2.513 ± 0.020 | −2.484 ± 0.020 |
| Δχ² to the global minimum | 0 | 6.1 |

  - r's relative error is the hypot of the two Δm² relative errors.
- **χ².**
  - It takes W66's form on logs: Σ ((ln o − ln d)/hypot(rel, a))², with a = 0.10 and read-outs at 0.05 and 0.20.
  - 6.1 is added when the fitted spectrum is IO.
  - Any observable below 10⁻¹² scores ∞.
- **The search, per (τ\*, pair).**
  - 4000 random parameter vectors (seed fixed per pair), Nelder–Mead from the best 20 (at most 4000 evaluations each),
    then from the best 3 again.
  - The free numbers p are the run's R2 count. The dof is 6 − p.
- **Pass marks.**
  - For dof ≥ 1, the 95% point of χ²(dof): 9.49, 7.81, 5.99 and 3.84 for dof 4, 3, 2 and 1.
  - At dof 0, compatibility only, at 3.84.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| L0 | the control: synthetic lepton data from a random point of the pair (L in T̄: T̄⊗T̄ 3, Weinberg sym T̄⊗T̄ 3) at the first τ\* is fitted back to χ² ≤ 0.01 | 80% |
| L1 | stage Q reproduces W114: assignments 11 and 13 each have an endpoint with χ² ≤ 10⁻⁶, and 14 one with χ² ≤ 3.84; the number of distinct τ\* is a read-out | 90% |
| L2 | PF1-W holds at every pair's best point: det Y_e/η^{6k} and det Y_ν/η^{6k} are constant across three τ to 10⁻⁸ (float root), and the lightest neutrino is massive | 95% |
| L3 | **no (τ\*, pair) with dof ≥ 1 passes its mark** | 80% |
| L4 | read-out: for every (τ\*, pair), χ²_min at the three allowances, the ordering, and at the best point δ (from J and the angles; sign convention noted), m_lightest/m_heaviest, Σm_ν and m_ββ with the scale set by \|Δm²₃ℓ\| | — |
| L5 | for any (τ\*, pair) that passes: 200 random targets, each log-observable shifted uniformly within a decade centred on the data (sin² targets redrawn above 0.99), fitted by the same search; f, the fraction fitted at χ² no larger than the data's. Evidence means f < 0.05 | — |

## What the outcomes mean (fixed now)

- **L3 holds.** At every quark-fixed τ, PF1-W's lepton sectors fail the data under A-W. PF1-W together with this
  frame and A-W is refuted for the leptons. This does not touch the quark reading's θ̄, which was a postdiction, and it
  does not refute PF1-W outside this frame.
- **L3 fails, and L5 gives f < 0.05 for a passing pair.** That is a candidate: the pair's unfitted read-outs (δ,
  m_lightest, Σm_ν, m_ββ, the ordering) become predictions with a stated look-elsewhere. The look-elsewhere is the
  number of (τ\*, pair) tests, and L4 reports it. It would still be 0 of 19, the neutrino data not being among them.
- **L3 fails, but f ≥ 0.05.** Compatible, with no evidence.
- **L0 or L1 fails.** The instrument is not trusted until the failure is found. Any later check is post hoc.

## Seen before the rule (disclosed)

- The zero-free run's output, including R2's table.
- W114's sixteen best points and χ².
- The NuFIT 6.0 values above.
- The seat's data files.
- No lepton coupling, no neutrino observable, and no stage-Q search has been computed.

## Discipline

- This rule is committed and pushed before the script exists.
- The script is committed before its one run, and its output is committed before it is read.
- A failed launch is disclosed, with its log kept. A failed cell is recorded as failed. Any later check is labelled
  post hoc.

chat1, 2026-10-21. 0 of 19.
