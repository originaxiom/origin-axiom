# W96 — the rule, recorded before the code

The SM-derivation seat, 2026-10-15. Committed before the code that reads it exists. Nothing here is a result.

**Numbering.** W95 is held for the fresh look's N2, traces by discriminant
(`docs/A_FRESH_LOOK_FROM_THE_PRINCIPLE_2026-10-15.md`), if the owner rules it.

## Why this arc

- **Main sealed B1659, the joint law** (P-168; preregistration f4b12d788, sha256 8123044b). Main has not run it yet.
  It claims that in B1656's twisted, quaternionic frame the coupling Y(S, M) of B1658 satisfies, for every Higgs S and
  every matter M in M₂(ℂ):
  - **J1:** det Y = 4 det S det M tr(εSMᵀ);
  - **J2:** adj Y = det S·A(M) + det M·P A(S), with P = diag(1, −1, −1) and A main's explicit quadratic;
  - **J2b:** A(pqᵀ) = q̃p̃ᵀ on the null cone;
  - **J2c:** with M = Nε⁻¹, the coupling is symmetric in (S, N), and tr(εSMᵀ) = −polar(S, N);
  - **J4:** the corollaries, including geometric masses at the coincident point N = S.
- **This seat checks main's arcs on its own code,** as W89 did for B1656 and W93 for B1658. The law is P-175's first
  test: can the up quarks' own matter defect do a second Higgs's work?
- **Blind to main's output, not to its preregistration.** The preregistration (its cells and A's formula) was read
  before this rule. Main's run has not landed, and its draft numbers are not written anywhere this seat can read.

## Weave or thread?

- **Q1–Q5 and Q7 are identities of the frame over M₂(ℂ) × M₂(ℂ).** They hold at every τ, but within one frame. They
  are not a weave result.
- **Q6 is read at one τ (ω) on W59's eighteen lines: a frozen piece.**

## The objects (fixed here)

- **W93's implementation of B1656's frame, rebuilt in sympy for the identities:**
  - QI = diag(i, −i), QJ = [[0, 1], [−1, 0]], QK = QI·QJ, ε = QJ;
  - the generations' blocks are (QJ, QI, QK);
  - Y_ab(S, M) = ⟨C_aᵀ ε S C_b, M⟩, with ⟨A, B⟩ = Σ_mn A_mn B_mn.
- **Main's A(M)** for M = [[m₀, m₁], [m₂, m₃]], copied from its preregistration (§1):

  A(M) = [[m₀² + m₁² + m₂² + m₃², 2i(m₀m₂ + m₁m₃), −i(m₀² + m₁² − m₂² − m₃²)],
          [2i(m₀m₁ + m₂m₃), −4m₁m₂, 2(m₀m₁ − m₂m₃)],
          [−i(m₀² − m₁² + m₂² − m₃²), 2(m₀m₂ − m₁m₃), −m₀² + m₁² + m₂² − m₃²]]

  with p̃ = (p₀² + p₁², 2ip₀p₁, −i(p₀² − p₁²)) for p = (p₀, p₁).
- **polar(S, N)** = det(S + N) − det S − det N.
- **The masses** are the singular values m₁ ≤ m₂ ≤ m₃ of Y.
- **The sector matter for Q6** is W93's: M_s = Σ R_s E^s from the analytic theta sums at 40 digits, at τ = ω, on
  W59's eighteen lines and the three sectors. This is P4′, equal framed data. Main's J3 uses P4 with channel norms,
  which this seat has not built.

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **Q1, the determinant law** | sympy over eight complex symbols, on this seat's coupling: det Y − 4 det S det M tr(εSMᵀ) expands to 0 | 85% |
| **Q2, the adjugate law** | sympy: adj Y − det S·A(M) − det M·P A(S) expands to the zero matrix, with main's A as copied above | 80% |
| **Q3, the null cone** | sympy: A(pqᵀ) − q̃p̃ᵀ expands to 0, and A(pqᵀ) − p̃q̃ᵀ does not. At 200 random null M and complex S (double precision): ∥adj Y − det S·A(M)∥ ≤ 10⁻¹²∥Y∥², and ∣∥A(M)∥ − 2∥M∥²∣ ≤ 10⁻¹²∥M∥² | 85% |
| **Q4, the symmetric form** | sympy: Y(S, Nε⁻¹) − Y(N, Sε⁻¹) expands to the zero matrix; tr(εSMᵀ) + polar(S, N) expands to 0 at M = Nε⁻¹; det(Nε⁻¹) = det N | 85% |
| **Q5, the corollaries** | at 40 random complex draws each (double precision): null M gives m₁/m₃ < 10⁻¹²; null S gives the same; S = M exactly gives the same; at N = S (M = Sε⁻¹), ∣m₁m₃/m₂² − 1∣ < 10⁻¹⁰; and wherever m₂m₃ ≠ 0, m₁ = ∣det Y∣/(m₂m₃) to 10⁻¹⁰ relative | 85% |
| **Q6, on this seat's sector matter** | at τ = ω on W59's 18 lines, three sectors, with two random complex S per case (108 cases, 40 digits): J1 and J2 hold to 10⁻²⁵ relative to ∥Y∥³ and ∥Y∥²; every sector's ∣det M∣/∥M∥² ≤ 10⁻²⁵ (W93's K3), so m₁/m₃ ≤ 10⁻²⁰ for every case | 95% |
| **Q7, controls that can fail** | at 40 random draws: (a) Y plus a generic 10% perturbation violates J1 by more than 10⁻⁵∥Y∥³ in every draw; (b) A(S) in place of P A(S) violates J2 by more than 10⁻³∥Y∥² in every draw; (c) N ≠ S (independent draws) departs from the geometric law, with median ∣m₁m₃/m₂² − 1∣ > 0.05 | 90% |

**The read-outs (no prior).**
- **Q6:** the size of each sector's pairing tr(εSMᵀ)/(∥S∥∥M∥) on the random S. Under P4′ the first generation is
  massless for a reason other than the pairing: the matter is null.
- **Q5:** the smallest and largest m₁/m₃ off the null cone, as a scale for J4.

## What the outcomes would mean

- **Every cell as predicted:** main's joint law holds on a second instrument, before main's own run lands. That run
  can then be compared with this one.
- **Q1, Q2 or Q4 failing:** either this seat's frame and main's differ by a convention (a block order, a transpose or
  ε's sign), or main's law fails. The record says which, post hoc and labelled. A convention found that way is
  disclosed, and the cell stays failed as worded.
- **Q6:** this cell can only confirm that under P4′ every sector is on the null cone. The first generation's mass in
  this frame then needs P4's channel norms or another defect. That is main's J3, not this seat's.

## After the run

- Record in the weave dossier's NOTE (a section, the table, a header bullet and a files entry) and the state page.
- Send a relay section to main.
- Row main's f4b12d788 and chat1's a4cb90257 in the ledger.
- Update CHANGELOG and PROGRESS_LOG.
- Add a test that reads the JSON and recomputes J1 symbolically in process.

0 of 19.
