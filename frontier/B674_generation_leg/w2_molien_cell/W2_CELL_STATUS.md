# W2 MOLIEN CELL (cc seat) — STATUS
# Governing document: PREREG_W2.md (sealed, sha b4c9a6bb). This cell ran ONLY
# the vacuity gate, step (i), and step (ii). Step (iii) is LOCKED.
# Script: w2_molien_cell.py ; full log: run_log.txt ; failed first attempt
# preserved byte-faithfully: run_log_attempt1_failed.txt (see "Corrections").

## Verdicts (two-outcome at every step)

- VACUITY GATE: **PROCEED** — W is NON-CENTRAL on every graded piece
  V_k, k = 0..40 (matrix-level exact witness at k = 0..3; distribution-level
  for all k; every piece has ≥ 2 occupied eigenvalue classes — k = 0 already:
  ζ₁₀ ≠ ζ₁₀⁻¹). No DESIGN-KILL. Table: vacuity_gate.md.
- STEP (i): **BANKED** — the exact eigenvalue distribution of W on the graded
  pieces of V, k = 0..40, over ℚ(√5) (ζ₁₀-classes + multiplicities).
  GATE ARTIFACT: eigen_distribution.json (cc2's independent derivation must
  match its GATE_PRIMARY block exactly). Human table: step_i_table.md.
- STEP (ii): **PASS** — the Molien doublet's dressed q-support classes mod 1
  land exactly in {2/5, 3/5}, and the component-swap map is reproduced by the
  two Galois conjugates (details: step_ii_support.md).
- STEP (iii): **LOCKED** — no coefficient was expanded beyond the two grade-0
  constants; no W33 target stream was loaded anywhere in this cell; nothing
  was compared against any target. Unlock condition: the cc2
  input-verification gate reports exact agreement with GATE_PRIMARY.

## The exact statements banked

1. σ(A₁) reconstructed exactly over ℚ(ζ₂₀): the commutator
   σ(T)σ(S)σ(T)⁻¹σ(S)⁻¹ with σ(T) = diag(1, ζ₅) and σ(S) the golden
   S-matrix. Verified: det = 1, σ(A₁)⁵ = −I, order exactly 10,
   char poly x² − φx + 1, eigenvalues ζ₁₀^{±1} (ζ₁₀ = e^{iπ/5}),
   **tr σ(A₁) = φ exactly** — the banked golden-rotation law reproduced as
   the base-grade self-check. Numerically pinned entrywise (2.5e-16) to the
   arc's stored 40-digit canonical matrix (an independent 70-dps route), and
   entrywise-EXACT against an independent sympy construction.
2. THE DISTRIBUTION LAW (verified k = 0..40; matrix-exact DFT recovery at
   k ≤ 3 and Sym^m, m ∈ {5,10,15,20}): on V_k (dim 2(5k+1)),
   m_k(t) = 2k+1 at t ≡ 5k±1 (mod 10); 2k at the other three classes of
   parity k+1 (mod 2); 0 at parity k (mod 2).
   tr(W|V_k) = (−1)^k·φ exactly (cyclotomic sum + ℤ[φ] Chebyshev, two routes).
   CONTROL (plain weight tower M_k): S_k(t) = k+1 at t ≡ 5k, k at the other
   same-parity classes; tr = (−1)^k — the arc's banked alternating law.
3. Grade-0 Molien factor: 1/det(1 − W|V₀) = 1/(2−φ) = 1+φ = **φ²** exactly;
   Galois conjugate (1−φ)² = 2−φ; doublet grade-0 gap = √5 (non-collapse
   witness). [Structural note, no stream loaded: φ² is the banked
   Galois-partner landscape value (W32).]
4. Support: the Molien product (weight-step grading) has INTEGER q-support —
   the REDUCED side of the Yang–Lee convention. The sealed per-component
   dressing (banked B672: comp_a = q^{ν_a}·η^{48/5}·reduced, ν = (0, 1/5)
   read from σ(T) = diag(1, ζ₅)) carries q^{2/5} (48/5·1/24 = 2/5 exact);
   dressed classes = {2/5, 3/5} — REQUIRED LANDING MET; both classes attained
   (grade-0 constants ≠ 0). The genuine coincidence: target class gap
   3/5 − 2/5 = 1/5 = the vvmf T-exponent gap (could have failed).
5. Swap map: Galois conjugation √5 ↦ −√5 (classes t ↦ 3t; lift-independent
   since m_k(t) = m_k(−t)) maps the distribution exactly onto the
   independently-enumerated conjugate-seed (ζ₁₀^{±3}, trace 1−φ = −1/φ)
   distribution, all k ≤ 40; involution; the doublet is genuinely
   two-element. This is the Yang–Lee ↔ Fibonacci convention swap
   (trace φ ↔ −1/φ), matching the banked comp1 ↔ comp2 structure; the
   ORIENTATION (which conjugate is comp1) is a step-(iii) question — locked.

## Declared choices (rule 4; for the cc2 gate to adjudicate)

- V-READING PIN: V_k = ℂ²_{(F₁,F₂)} ⊗ M_k(Γ(5)) (the vvmf system's FREE
  module over the ring, the pinned concrete formulation), with
  W|V_k = σ(A₁) ⊗ Sym^{5k}σ(A₁) [M_k = Sym^{5k}span(f₁,f₂), banked arc T3].
  FLAG: the alternative function-space reading (the W-closure of R·(F₁,F₂)
  inside scalar functions, per-grade ℂ² ⊗ Sym^{5k+1}, dim 2(5k+2)) gives a
  DIFFERENT distribution. If cc2's holonomy-side derivation lands on the
  alternative, the gate FAILS and both seats stop — that is the designed
  protection against a mis-reading; the disagreement would bank as-is.
- σ(S) representative: the real golden S-matrix. The arc's honest slash
  σ(S) carries a global phase (ζ₂₀⁻¹-type; its logged "golden S-matrix
  dev 0.27" is that phase, never asserted); every global phase cancels in
  the commutator — pinned by the entrywise numeric match to the arc's
  canonical σ(A₁).
- Galois lift: t ↦ 3t on ζ₁₀-classes; t ↦ 7t verified to give the same
  multisets (both restrict to √5 ↦ −√5 on the real subfield).

## Corrections (verify-don't-trust, own work)

- Attempt 1 FAILED at the (ii-a) grade-0 gate: a mistyped Cayley–Hamilton
  shortcut (2 + det − tr = 3−φ) instead of det(I − W₀) = 1 − tr + det = 2−φ.
  A scripting error in the CHECK expression, not in the banked data (the
  distribution and all step-(i) gates were identical). Corrected to a direct
  matrix determinant, re-run; failed log preserved byte-faithfully.

## What remains

- cc2 gate: independent holonomy/Fox-side derivation of GATE_PRIMARY; exact
  agreement unlocks step (iii) (≥ 100 coefficients, both Galois conjugates
  vs both banked doublet components). ANY disagreement = STOP both seats.
- Nothing in this cell asserts a MATCH: sealed outcomes remain
  MATCH / STRUCTURED NEAR-MISS / KILLED-AT-STEP-(k) / DESIGN-KILL, decided
  only after the locked step (iii) runs.
