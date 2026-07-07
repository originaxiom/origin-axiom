# B466 — the σ-equivariant locus: Chat-1's proposal adjudicated, the one open cell computed

**Status: banked (frontier). Firewalled. Incoming: Chat-1's "one place nobody looked"
(2026-07-07) — the substitution acting on the character variety, layers 0–4. Verdict: two
of the proposed cells are theorem-closed, one was banked all along under another name
(B448), and the one genuinely open cell is COMPUTED here exactly: the Dehn-filling pair
EXCHANGES under σ, the geometric component is preserved with a fixed line, and the whole
σ-story is the Gieseking double-cover deck action. No H1.**

## Two theorem-gates first (why "nobody looked" is inverted)

- **Gate A (σ² is inner):** the monodromy σ² equals conjugation by the meridian t in
  π₁(bundle); inner automorphisms act trivially on the character variety and on group
  cohomology (Brown, *Cohomology of Groups*, III.8). So "the σ²-fixed locus of X(M)" is
  all of X(M) — no selection.
- **Gate B (the fiber-level fixed locus is the banked object):** a fiber character extends
  to the bundle iff it is fixed by the monodromy — Fix(T₁²) IS the definition under
  B67/B71. The program's variety was the equivariant locus all along; Chat-1's Layer 3 is
  load-bearing, not unvisited. Likewise the bundle's H¹ is the Wang σ²-invariant part by
  construction.

## The genuinely live residual: σ itself — and it is the Gieseking deck symmetry

σ (a→ab, b→a) has abelianization [[1,1],[1,0]], **det = −1**: orientation-reversing, with
σ² = the fig-8 monodromy [[2,1],[1,1]]. Its mapping torus is the **Gieseking manifold**,
and the figure-eight complement is its orientation double cover (standard since Gieseking;
lit-gate, cited not claimed). So the σ-action on the character variety is the **deck
action of a 2-cover**, and σ-fixed characters = characters that descend to Gieseking.

## The computed cell (exact, `sigma_action.py`): the SL(3) σ-action on B71's components

| component | σ-image | consequence |
|---|---|---|
| V₀ (geometric, ⊃ Sym²) | **V₀**, via (p,q) ↦ (q,p) | preserved, with involution; **fixed line {p = q}** |
| W₁ (Dehn-filling) | **W₂(q,p)** | **the pair EXCHANGES** — Chat-1's central question, answered |
| W₂ | W₁(q,p) | (the σ-orbit structure pairs them) |

The σ-fixed locus is exactly the line {p = q} ⊂ V₀, passing through the **all-ones
character = V₀ ∩ W₁ ∩ W₂** (the triple point — the unique fixed point on the Dehn-filling
pair, and it is the point where all three components meet). Interpretation: these are the
SL(3) characters that extend to the Gieseking manifold; W₁/W₂ do NOT descend individually
— they are swapped by the deck symmetry.

## The geometric representation is NOT σ-fixed — and its σ-orbit is already banked

On the B67 SL(2) curve (y = z = x/(x−1)), the cusp condition κ = −2 restricts to
x²(x² − 3x + 3) = 0: the geometric fiber characters are **x = (3 ± √−3)/2 ∈ ℚ(√−3)**, and
σ (x ↦ x/(x−1)) **swaps the two roots** — exactly the banked **B448 period-2 ℚ(√−3)
orbit**. The only σ-fixed characters on the curve are the degenerate x ∈ {0, 2}. So:
- Chat-1's Layer 4 ("σ acts on the equivariant locus → ???") was computed in B448 without
  its name: **the heartbeat orbit IS the σ-orbit of the geometric structure** — the
  substitution exchanges the complete structure with its ℚ(√−3)-Galois conjugate (the
  deck action of the non-orientable quotient realizes the Galois flip).
- The hoped-for "physics lives where the static geometry meets the dynamic monodromy":
  the geometric point is NOT on the fixed line; what sits at the self-referential fixed
  point is the degenerate/triple-point locus, not the hyperbolic structure.

## The E₆ cell: closed a fortiori, with one named follow-up

The proposal "the Hessian restricted to the σ-equivariant subspace of H¹ might be
nonzero": the banked Hessian is **ZERO on ALL of H¹** (flat to third order, dps-100 —
B352/B370); zero on the whole space is zero on every subspace. Closed a fortiori, no
computation needed. The one new number that exists here: the **σ-signature** — σ acts on
the six 1-dimensional Sym-block directions of H¹ by ±1 each; the sign vector (±1)⁶ is a
well-defined new invariant (adjacent to, but distinct from, B347's banked hyperelliptic
θ-grading — different involution). Named follow-up; it cannot change the Hessian verdict.

## The dictionary essay (disposition)

Chat-1's frame — "arithmetic becomes physics through a dictionary; the dictionary is
DGG/L50; the left column is computed, the right column is not" — is filed with two
corrections:
1. **The rows already run through the dictionary gave class-shared or zero left-column
   values**: H¹ = 6 for BOTH 4₁ and 5₂ (B445 — the "particle content" row is universal,
   not a fingerprint); CS = 0 per component (B458); Hessian = 0 (B352/B370/B455). A
   dictionary translates values; it cannot make class-shared values object-specific. The
   Inversion Law survives any dictionary.
2. **Constructing T[M₃, E₆] is open research mathematics** (the DGG correspondence is
   established for A-type; the E₆ theory is not in the literature) — NEEDS-SPECIALIST,
   recorded as such, not as a repo-computable cell.
"It's a task, not a conclusion" is accepted for the genuinely new observables such a
correspondence would define — while the already-defined rows have already answered.

## Reproduce
```
python3 sigma_action.py     # exact; prints ALL CHECKS PASS
pytest ../../tests/test_b466.py
```
