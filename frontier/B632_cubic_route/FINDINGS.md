# B632 — THE CUBIC ROUTE: h¹(M; 27) = 3 (the generation count exists as cohomological multiplicity)

**Date: 2026-07-15. Status: cell 1 BANKED (prereg dab6948b… sealed in the
hash ledger before running; verdict by the locked table). Mathematics
only — no SM number appears in this arc.**

## Why this arc exists (the adjudication of chat-1's reframe)

Chat-1 proposed "the missing step is the cubic (the Yukawa)". The MB13
sweep (recorded in the prereg, per the standing rule) found the claim
half-wrong and the correction sharper than the proposal:

- **B308 already computed the cubic-invariant structure**: the E₆
  Yukawa is the UNIQUE cubic invariant 27×27×27 → 1 (multiplicity 1) —
  the coupling is forced; what is NOT forced is the TEXTURE, and B308
  explicitly queued the gate: "can the multiplicity route produce three
  generations with the right Yukawa texture?"
- **B307's theorem** closed the trace-field route to three generations
  (no hyperbolic knot has a C₃ trace field). Generations, if anywhere,
  come from a multiplicity mechanism.
- The genuinely new ingredient since B308: **B575's exact e₆ ⊂ gl(27)**
  build, which makes the 27 itself computable as a local system.

## Cell 1 results (exact, over ℚ(ω); `h1_27_generations.py`, `cell1_output.txt`)

1. **The principal decomposition of the 27:** h_pr eigenvalue
   multiplicities peel into strings exactly as
   **27 = V(16) ⊕ V(8) ⊕ V(0)** (dims 17 + 9 + 1). The 27's principal
   spins are {8, 4, 0} — the two θ-ODD EXPONENTS {4, 8} plus the
   trivial. Since ρ = principal ∘ ρ_geo, the 27-local-system is
   Sym¹⁶ ⊕ Sym⁸ ⊕ ℂ of the geometric SL(2) system.
2. **The cohomology (direct Fox calculus, 27-dim module, exact):**
   h⁰ = 1, **h¹ = 3**, h² = 2; Euler gate 1 − 3 + 2 = 0 PASS;
   rank(δ¹) = 25.
3. **The block cross-check AGREES**: h¹ = 1 (trivial block, = b₁) +
   1 (Sym⁸, banked B575-G4 at exponent 4) + 1 (Sym¹⁶, banked at
   exponent 8) = 3; h⁰ = 1 = the trivial block's invariant.

## What the verdict means (per the locked table)

**The object carries a THREE-slot cohomological generation structure:
H¹(M; 27_ρ) = ⟨the abelian class⟩ ⊕ ⟨the two θ-odd chiral classes⟩.**
This is a multiplicity mechanism DIFFERENT from B302's commensurator
ℤ/3 and NOT blocked by B307 (which kills symmetric trace-field triples,
not cohomology multiplicity) — it is the heterotic-style count
(generations = matter-valued H¹). B308's gate OPENS: the cup-product
cubic texture on H¹(27) is now a well-posed, canonical computation.

**Honesty (the "wrong three" caveat, one level deeper):** the three
slots are GRADED (spins 0, 4, 8), not three interchangeable copies —
one abelian + two chiral. Any generation reading must carry this
structure; it is suggestive (real generations are wildly hierarchical,
not symmetric) but it is a structural difference from "three copies of
one representation," stated at banking.

**The forced vev:** h⁰ = 1 — the ρ-invariant vector v₀ ∈ 27 (the V(0)
line) exists and is canonical. C(v₀, ·, ·) is then a ρ-invariant
symmetric bilinear form on the 27 — the forced, dial-free contraction
for the texture. By sl₂-invariance it is BLOCK-DIAGONAL, which
PREDICTS texture selection rules before cell 2 runs: the cup pairing
of classes from different blocks through C(v₀,·,·) vanishes
identically; the candidate texture is diagonal in the block basis.
Registered as cell 2's first gate (a computed prediction, falsifiable
by the cell-2 run).

## Cell 2 (queued, own prereg): the texture

Build C exactly (uniqueness gate = B308's multiplicity 1); verify the
block-diagonality prediction; compute the three diagonal values under
the house boundary normalization (the L85 campaign's banked
cross-domain normalization pattern; res is injective, banked). No SM
comparison anywhere — that would be a separate sealed round under the
owner's directive.

## Locks

tests/test_b632_h1_27.py: fast (prereg hash in ledger; the banked
output's verdict line; the decomposition arithmetic 17+9+1 = 27 with
spins {8,4,0} = {θ-odd exponents} ∪ {0}); OA_SLOW=1 (the full exact
rerun of cell 1, ~3 min).
