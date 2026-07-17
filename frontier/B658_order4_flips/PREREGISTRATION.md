# B658 — the order-4 orientation-reversing families through the flip
# pipeline (R21-6, owner-directed 2026-07-17; the B643 residual, run)

## The question

B643 proved both order-2 amphichiral flip classes break on the weld
double's 27 local system (wall 8); only the deck swap σ* survives. The
two remaining orientation-reversing families of Isom(4₁) = D₄ are the
ORDER-4 classes (B605's exact census over ℚ(√−3)):
- φ_A: a ↦ A, b ↦ bAB, U_A = [[−1, ζ̄₆], [0, 1]]  (τ² = the half-longitude)
- φ_B: a ↦ B, b ↦ aBA, U_B = [[0, 1], [−ζ₆, 1]]  (τ² = the half-longitude)
Do they admit a global invertible 27-companion on the double — the
last symmetry candidates of the object itself?

## The method (B643's pipeline, verbatim per its residual note)

For each family: (1) the peripheral conjugator search — exact SL(2)
breadth-first over reduced words to depth 9 for (w, s, t) with
φ(μ) = w μ^s w⁻¹ and φ(LONG) = w LONG^t w⁻¹ (±I projective equality);
record the signature (s, t). (2) ψ = Ad(w⁻¹)∘φ; the 27-companion
U_ψ = ρ(w)⁻¹ · lift₂₇(U_φ) (the lift is weight-even, so any det ≠ 0
lifts through PGL(2)). (3) The side-exchanging block-scalar system of
B643 step 3 (V₁ = U_W·conj(U_ψ), V₂ = U_ψ·U_W⁻¹; the block-scalar
correction d over Sym¹⁶⊕Sym⁸⊕Sym⁰; 27×27 off-diagonal conditions,
3 unknowns): report the solution dimension and d exactly.

## Sealed outcomes (two-outcome, no third reading)

- **ACTS(family):** the d-solution space contains an invertible member
  → the family survives at the companion level; a follow-up gates
  stage (the F1–F4 analogues of B643's prereg) is REQUIRED before any
  action claim — companion existence alone banks as "companion exists,
  gates pending."
- **BROKEN(family):** the solution space is singular (no invertible d)
  → the family breaks; inner corrections cannot rescue (B643's Ad(w)
  argument covers the full outer class).
- If BOTH families are BROKEN: wall 8 upgrades to the total statement
  — the chord breaks EVERY orientation-reversing family of the
  object's D₄ (two order-2 + two order-4); the double's 27-cohomology
  symmetry reduces to the deck swap σ* exactly.
- If a conjugator is not found to depth 9: banked as bounded-search
  negative for that family (stated as such, not as BROKEN).

## Controls

The a-family (known singular d = (0,0,1)) re-run through the same code
path as a positive-control of the machinery; the exact-arithmetic
environment (ℚ(√−3) Fraction pairs, zero floats) inherited from B637.

Artifacts: b658_order4.py, b658_output.txt, FINDINGS.md, locks in
tests/test_b658_order4.py. House rituals: hash-first (this file sealed
before compute), ledgers same-PR, Gate 5 untouched (pure mathematics).
