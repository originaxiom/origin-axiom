# W90 — the rule, recorded before the code

The SM-derivation seat, 2026-10-15. Committed before the code that reads it exists. What the seat computed while
drafting is listed under "Seen before the rule", and the priors were set after that. Nothing here is a result.

## Why this arc

- **Main's B1657** (sealed d4dcd0d50, run ab392d4da) found two laws near τ = ω, each for one isotropic vacuum.
  - In the conjugate vacuum the light masses over the heavy are the two isotropy defects, |d_a| and |d_v|.
  - In the parallel vacuum they are |d_a + d_v|/4 and |d_a d_v|/4.
- **The reading "two defects, three masses" (relay §122)** found that one end condition shared by the Higgs and the
  matter is refuted in every sector. It left one number per sector.
- **But the Higgs is one field.** Its defect d_a is a property of its direction in M, so it is shared by every sector.
  The up quarks couple to its conjugate, whose defect is the complex conjugate, with the same modulus.
  - So |d_a| = A is one number for all three sectors, while the matter's defects d_s may differ by sector (the twist,
    B1656).
- **This arc asks whether any assignment of B1657's two vacua to the three sectors admits one A that fits the data.**
  It asks this whatever τ, L, the line, the matter's end conditions and every phase are. That is a relation with no
  free size, the kind W88 put against the data.

## Weave or thread?

- **Weave-type.** It takes every sector jointly under one rule, with none hand-picked. The quantity, the shared
  Higgs's defect, is defined by the joint coupling, and the claim is about all sectors at once. It is given Λ, the
  dictionary's sectors, and the premises below.

## The premises (stated, not derived)

- **P1.** Each sector s ∈ {up, down, leptons} sits near one of B1657's two vacua and obeys that vacuum's law at first
  order in the defects. B1657 derived the laws untwisted, so carrying them to the twisted sectors is a premise.
- **P2, one Higgs.** |d_a| = A is the same in every sector.
- **P3.** The matter's defect d_s and every relative phase are free, sector by sector.
- **The data.** HZ2021's running masses at M_Z (W53's `received/` file), with their printed uncertainties.

## Seen before the rule (disclosed)

- **The data's values were seen** (W53, W88 and the reading of relay §122).
- **The seat worked the central values by hand, in conversation, before this rule.** With x₂ = m₂/m₃ and x₁ = m₁/m₃:
  - **Conjugate:** A must equal x₂ or x₁.
  - **Parallel:** the feasible A satisfy |A − 4x₁/A| ≤ 4x₂ ≤ A + 4x₁/A. That gives:
    - up quarks: A in [0.0018, 0.0024] ∪ [0.0124, 0.0165];
    - down quarks: A in [0.034, 0.109];
    - leptons: A in [0.0047, 0.0049] ∪ [0.231, 0.240].
  - At central values no assignment shares an A across the three sectors.
  - The up quarks and the leptons share none in any assignment.
  - The down quarks and the leptons share A = m_μ/m_τ only with the down quarks parallel and the leptons conjugate.
  - At 2σ the up quarks and the down quarks share an A only with the up quarks parallel and the down quarks conjugate
    (about 0.015 to 0.018).
- So this arc is a scoreboard, not a blind test.

## The method (fixed here)

- **The bands.** For each sector and k ∈ {0, 2, 3}, x₂ and x₁ are taken over the box where each mass is within kσ of
  its value: the numerator raised and the denominator lowered for the upper end, and the reverse for the lower end.
- **The conjugate set** is the union of the x₂ band and the x₁ band.
- **The parallel set.** A is allowed if some S in 4·(x₂ band) and some P in 4·(x₁ band) satisfy
  |A − P/A| ≤ S ≤ A + P/A. For fixed A that holds exactly when the interval below is not empty:
  [max(P⁻, A(A − S⁺), A(S⁻ − A)), min(P⁺, A(A + S⁺))]
- **The grid.** A runs on 2 × 10⁶ log-spaced points from 10⁻⁸ to 1. The k = 0 sets are also given in closed form,
  from the roots of the quadratics.
- **The census.** All 2³ = 8 assignments of a vacuum to each sector for the three sectors jointly, and the 4
  assignments for each of the three pairs. For each, the common A set is reported as intervals.

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **H1, the sector sets** (k = 0, closed form) | the parallel sets are up [0.0018, 0.0024] ∪ [0.0124, 0.0165], down [0.034, 0.109], leptons [0.0047, 0.0049] ∪ [0.231, 0.240], each end to 2%; the grid agrees with the closed form to the grid's step | 96% |
| **H2, one Higgs, three sectors** | at k = 2 none of the 8 assignments has a common A | 92% |
| **H3, the decisive pair** | at k = 2 the up quarks and the leptons have no common A in any of their 4 assignments | 90% |
| **H4, down and leptons** (they couple to the same Higgs in the Standard Model) | at k = 2 exactly one assignment survives, down parallel and leptons conjugate, and its common set contains m_μ/m_τ | 80% |
| **H5, up and down** | at k = 2 exactly one assignment survives, up parallel and down conjugate | 70% |

**The read-outs (no prior).** Every sector's set at k = 0, 2 and 3; every assignment's common set; the k = 3
verdict.

## What it would say

- **If H2 holds,** B1657's two laws with one Higgs cannot reproduce the mass ratios of the three sectors, whatever τ, L,
  the line, the matter's end conditions or the phases. Then either the Higgs sits near neither symmetric vacuum, or the
  sectors see different Higgs defects. The second would mean the Higgs's direction is itself twisted by the sector (its
  hypercharge line, B1656's ū). That would be an exclusion, with the map's next step named.
- **If H2 fails,** the surviving assignment and its A are a candidate. A is then a number the frame must produce from
  the Higgs's section, and the matter's three defects follow from the data.
- A failure of H1 would mean a slip in the hand work, found post hoc and labelled.

## Limits

- One scale (M_Z); the ratios within a sector run slowly, but nothing here is computed at another scale.
- First order in the defects. The lepton parallel set's upper piece (A ≈ 0.23) sits where second-order terms are a
  few per cent.
- No CKM datum is used.

## After the run

- Record in the weave dossier's NOTE (section W90, the table), the state page, the relay to main, CHANGELOG and
  PROGRESS_LOG.
- A test in `tests/test_b1552_the_chiral_triplets_count.py` reads the JSON and recomputes the k = 0 sets in process.

0 of 19.
