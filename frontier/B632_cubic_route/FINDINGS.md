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

---

## CELL 2 (2026-07-15, same day): C unique, the vev couples to all three slots, the solo texture is antisymmetric and FULL

**Prereg CELL2_PREREGISTRATION.md (sha dc2be090…, sealed before running) —
the corrected design, after the parallel audit seat caught that the
original "three diagonal values" object cannot exist on the solo
complement. The cell-1 registered prediction ("the texture is diagonal
in the block basis") is hereby resolved: DISSOLVED-BY-OBSTRUCTION — its
object does not exist at class level on M (O1: cd = 2 kills scalar
triples; O2: H²(M;ℂ) = 0 + graded-commutativity force antisymmetry and
zero diagonal). The audit seat is credited with the catch.**

### Results (`cell2_texture.py`, `cell2_output.txt`; exact over ℚ(ω))

1. **The cubic invariant C is EXACTLY unique in B575's basis** —
   support = 45 zero-weight-sum triples, invariance system of 180
   equations has a 1-dim solution space with ALL 45 coefficients
   nonzero: the Jordan-determinant cubic, now explicit in the local
   system's basis (B308's multiplicity-1, upgraded to a constructive
   in-basis object). Spot gate: C(A·u, A·v, A·w) = C(u,v,w) exactly.
2. **The forced vev couples to ALL THREE generation slots:**
   B_C = C(v₀,·,·) is exactly block-diagonal (the sl₂ prediction
   verified) with c₀, c₄, c₈ ALL NONZERO.
3. **The component census = exactly the triangle rules:** all seven
   allowed spin triples PRESENT ((8,8,8), (8,8,4), (8,8,0), (8,4,4),
   (4,4,4), (4,4,0), (0,0,0)); all three forbidden ABSENT ((8,4,0),
   (8,0,0), (4,0,0)).
4. **The O1/O2 obstruction gates GREEN** (after one honest instrument
   fix, below): both diagonal classes [z∪z] = (0,0) exactly;
   class-level antisymmetry on all three pairs; coboundary control —
   class invariant, raw cochain changed.
5. **Ω: Λ²H¹(27) → H²(M; 27*) is NONZERO ON ALL THREE PAIRS** (exact
   classes in ℚ(ω), the two H² channels): no generation-pair
   decouples. The solo object's class-level cubic structure is the
   FULL antisymmetric form — the maximal structure O1/O2 permit.
   (Entry magnitudes are representative/normalization-dependent by the
   prereg's declaration; the invariant content is the all-nonzero
   pattern and the gate structure.)

### The instrument fix (disclosed; caught by the O2 gates, first run)

The first run FAILED its own coboundary-invariance control: the naive
2-cell evaluation Σᵢ F(p₍ᵢ₋₁₎, xᵢ) of the bar cup-cocycle omits the
inverse-letter correction chains ([ℓ⁻¹] = −ℓ⁻¹[ℓ] only up to
∂[ℓ⁻¹|ℓ]), so bar-coboundaries did not land in the cellular Fox image
the H² functionals annihilate. The corrected chain subtracts
F-evaluations on p₍ᵢ₋₁₎[ℓ⁻¹|ℓ] at each inverse letter; all gates then
pass. The failed first output is superseded in place; the control
worked exactly as sealed. **Hygiene residual registered:** B575's
`cup_on_relator` uses the naive evaluation; its Q ≡ 0 result is safe
(independently corroborated by B352's dps-100 pipeline and the
constructive z₂ solutions), but the resolution subtlety deserves its
own check (OPEN_LEADS).

### The structural theorem this arc banks (the coupling thesis, cohomological form)

On the solo complement, a symmetric mass-matrix-shaped object does not
exist (O1 + O2, now verified); the maximal solo structure is the
antisymmetric Ω — and it is full. A symmetric texture becomes
well-defined exactly on a CLOSED 3-cycle, canonically the mirror-double
M ∪_∂ M̄ (H³ = ℂ) — the program's banked forced two-body coupling (B580
G1, the chord). **The Yukawa-shaped object structurally requires the
coupling; the solo object carries the antisymmetric half.** Cell 3
(registered, own prereg, not run): the symmetric texture on the double
via Mayer–Vietoris from banked pieces.

---

## CORRECTIONS (2026-07-15, the audit seat's findings integrated (internal; PROVENANCE.md §0); REPAIR_ADJUDICATION.md)

The read-only audit seat (internal; PROVENANCE.md §0) verified cell 2's corrected mathematics
exhaustively (162/162 coboundary descents, all diagonals/exchanges,
exact rank — verifier adopted as `verify_cell2_exhaustive.py`, now the
lock) and corrected this arc's LANGUAGE, binding henceforth:

- **Ω is rank 2 with 1-dim kernel** — a surjective alternating
  cohomology operation; the earlier "full antisymmetric form / maximal
  structure" wording OVERSTATED (the target is 2-dim; one pair-direction
  is killed). Block-adapted H² coordinates = registered residual.
- **v₀ = the invariant-section generator**, not a "forced vev" (an
  invariant line exists; nothing selects it dynamically).
- **The three H¹ summands = three inequivalent local-system modes**
  (one class in each of three INEQUIVALENT principal-SL(2) blocks), not
  "generation slots": three copies of one representation is exactly
  what this is NOT — the physics-type check is open, not implied.
- The failed runs are restored verbatim (FAILED_RUN_1/2.txt); the
  corrected code is hashed post-hoc with that label; the repair trail
  is adjudicated in REPAIR_ADJUDICATION.md.
- **The cell-3 sketch in the cell-2 section is SUPERSEDED:** on ANY
  closed oriented 3-manifold the triple through a symmetric coefficient
  cubic is FULLY ALTERNATING (Koszul); "the double restores a symmetric
  mass matrix" was false as typed. The corrected cell-3 statement and
  the twisted-M–V dimension facts live in the B637 prereg (the audit's
  own exact table — h¹(D;27) = 2 at the full-E₆ bends m = 4, 8, so
  Λ³H¹ = 0 there — is reproduced in-repo and registered as the
  prediction to confirm independently).
