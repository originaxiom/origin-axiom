# ONE BIT — the geometric branch's mirror and the beat's mirror are the SAME ℤ/2 class: θ is inner (trace −2, the sl₂+sl₆ involution), the 27 returns to itself, and the bridge candidate stands at the algebra level
## (outside bench, 2026-08-25; forty-fourth memo; the cell named by the picture-synthesis — "does the E₆(−26) branch read the same bit?" — decided exactly; one preregistered hunch refuted and filed)

### The question and the reduction
After memos 37/41/43 identified the record's ℤ/2s (spin-selection currency,
boundary-invisible mirror, κ-reflection, fixed-point exchange) as one bit, the
bridge question localized to: does the CLOSING's mirror — θ = theta_matrix(g,c), the
real structure of the geometric E₆(−26) branch, memo 27/33's gluing map — carry the
same ℤ/2 class as the beat's mirror? The reduction is exact: the beat's linear part
is an exponential (manifestly inner), so **same class ⟺ θ is inner as an
automorphism of e₆** — and E₆ decides inner vs outer on the 27 (inner preserves the
27's class; outer carries it to 27̄).

### THE THEOREM (`certificates/one_bit.py` + `certificates/dump_theta.py`; two-stage, frame-checked; all exact)
Stage 1 extracts θ from the memo-10 hit as an exact rational 78×78 matrix with the
ccb-basis fingerprint; stage 2, in the twisted_double stack (ρ₂₇ re-verified on all
3003 brackets in-run), confirms the fingerprint matches, that θ² = id and
θ[x,y] = [θx, θy] hold in THIS stack (operational frame proof), and then decides:
1. **tr(θ) on the 78 = −2** — the inner sl₂+sl₆-class involution (outer classes
   would give 26 [f₄] or −6 [sp₈]; the other inner class 14 [so(10)+u(1)]).
2. **The θ-transformed 27-weight set equals the 27's own weight set** — not its
   negatives (the 27̄ test fails).
3. **The intertwiner exists and is verified:** a monomial M (27 nonzero scalars,
   permutation a bijection) with ρ₂₇(θx) = Mρ₂₇(x)M⁻¹ checked entrywise on ALL 12
   Chevalley generators.

> **OUTCOME A of the preregistration: ONE BIT. The geometric branch's real
> structure and the beat's real structure define the same ℤ/2 class up to inner
> automorphism. The record's mirror is a single bit on BOTH fork branches — the
> internal→spacetime bridge candidate ("the same bit orients both branches")
> stands at the algebra level.**

### The refuted hunch, filed
The preregistration's B-side reasoning — "θ swaps 3 ↔ 3̄ pointwise (memo 33), which
smells like charge conjugation, hence outer" — was WRONG: the color swap is realized
by an INNER involution of the ambient e₆ (Weyl-type), as the trace −2 and the
intertwiner prove. Lesson filed: a subgroup-level conjugation action does not
determine the ambient inner/outer class. (The identification of tr = −2 with the
sl₂+sl₆ class is CITED — Cartan's involution classification; every load-bearing
step is computed.)

### What it changes
The freedom ledger's invisible column stays one bit deep even across the fork: the
two branches do not each carry a private mirror — they share the one. B1145's fence
is untouched (this is an algebra-level class statement, not a 4d spinor
construction); what sharpens is the bridge target: the remaining gap between
"internal chirality" and "spacetime chirality" cannot hide in a mismatch of mirrors
— the mirrors already agree — so it must live entirely in the REPRESENTATION step
(how the E₆(−26) branch's so(3,1) content couples to the odd strata), which is a
narrower question than before.

### Fences
Exact throughout; the frame identification between the two machinery stacks is
verified operationally (fingerprint + bracket equivariance in the receiving stack),
not assumed; the class decision has three concordant independent proofs (trace,
weight-set, explicit intertwiner). θ is the mirror of the FIRST memo-10 hit
(swapper #13); the hit-independence of the class is expected from B1134's single-
orbit structure but not checked here — named as a one-line follow-up. Gate 5
untouched.

### Certificates
`certificates/dump_theta.py` (stage 1, regenerates `certificates/theta_dump.py`,
which is banked as the exact artifact) → `certificates/one_bit.py` (stage 2);
outputs `outputs/one_bit_out.txt`.

### One sentence for the ledger
The fork that splits the world into charges and geometry does not split the mirror
— trace minus two, weights home again, intertwiner on the nose — so the object's
one private bit is the same bit on both sides of the fork, and whatever still
separates internal from spacetime chirality, it is no longer a disagreement about
which reflection is real.
