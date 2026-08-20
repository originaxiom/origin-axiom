# B1092 — THE PURITY SELECTOR, MAIN-BENCH PROVED (L168): the second VEV is a condition, not a point — with the stabilizer definitions disentangled

**Date:** 2026-08-20 · **Verdict: PROVED (own-code re-derivation, exact ℚ arithmetic throughout; two sharpenings beyond the source)**

## The build (independent; every convention verified before use)

so(10) on the 16-dim even half-spinor realized on Λ*(ℂ⁵) by fermionic bilinears — the
CAR relations verified on the full 32-dim Fock space BEFORE being trusted; the 45
generators close (990/990 commutator pairs, exact rank checks); the Cartan is
self-centralizing (rank 5 rigorous); the 40 nonzero roots are exactly D₅'s ±e_i±e_j;
**the parity control PASSES: all 16 weights in (±½)⁵ with CONSTANT parity — a single
chiral half.** (This is the control that catches the character-twisted wrong build the
original computation hit; here it was run as a precondition, not a postmortem.)

## The theorem, re-derived

1. **Pure spinor (|0⟩): literal stabilizer {X : Xv = 0} has dim 34 = sl(5) ⋉ Λ²(ℂ⁵),
   toral part 4** — the rank drop 5 → 4 happens AT purity. ✓ (the banked claim, exact)
2. **Generic spinor: literal stabilizer dim 29, toral part 0 — FATAL** (no rank
   survives): verified on two independent fully-random rational vectors (the agent also
   caught a plausible-looking test vector being secretly non-generic — toral 2 — the
   ≥2-vectors guard working as designed; recorded as the arc's own sobriety line).
3. **Transitivity: 45 − 34 = 11 = dim(pure cone)** — one orbit; and a second pure
   spinor (degree 4) has the same 34/4 — orbit homogeneity, with the bonus that
   attaining the maximal stabilizer dim IS the standard characterization of purity.

## The sharpenings (beyond both prior benches)

- **Literal vs projective disentangled**: the PROJECTIVE stabilizer (of the line ℂv) is
  35 = gl(5) ⋉ Λ² — the parabolic — and the cross-check lands exactly:
  **45 − 35 = 10 = dim 𝕊₁₀**, the projective pure-spinor variety, independently
  reproducing the textbook parabolic dimension from the Fock-space build. The banked
  "34" is the literal stabilizer; both numbers now stand with their definitions.
- **The genericity guard's catch** (above) — a named construction hazard for any future
  use: support-sparse spinors can carry accidental toral symmetry.

## What this banks for THE RANK WALL

**The second VEV ⟨ν^c⟩ must be a pure spinor — purity is the unique condition leaving
rank 4 standing** (generic is fatal, toral 0), **and Spin(10) is transitive on the pure
cone — the selector exists as a CONDITION, not a POINT.** B990's orbit-to-point gap
recurs verbatim on the 11-dim cone. Combined with Route A's cleared arithmetic (the
companion arc): the one-slot count is pinned to the PAIR space 27⊕27̄ — Kato–Yukie's
object — and the owed counter identification is the single remaining step of Route A.

**Locks:** the 34/4, 29/0, 11 = 10+1, and 35-parabolic numbers as fast exact
assertions on a compact re-run (the stabilizer dims from the 16×45 rank computations).
