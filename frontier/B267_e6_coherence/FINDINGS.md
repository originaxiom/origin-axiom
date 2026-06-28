# B267 — the coherence check: the arithmetic E₆ and the character-variety E₆ are ONE E₆

**Status: banked observation (frontier). FIREWALLED — Lie theory / arithmetic, NOT physics. Nothing to
`CLAIMS.md`.** Closes the loop between B264/B265 (geometric) and B266 (arithmetic). `e6_coherence.py` (pyenv,
sympy; self-contained — 2T character data hard-coded from B266/GAP).

## The question
Two E₆'s were attached to the figure-eight by **independent** routes:
- **Geometric (B264/B265):** the principal `sl(2)→e₆` (Kostant); the geometric rep composed with it has a rank-6
  character variety **graded by the E₆ exponents `{1,4,5,7,8,11}`**, with E₆-Zariski-dense reps.
- **Arithmetic (B266):** trace field `ℚ(√−3)` → ramified prime 3 → `SL(2,𝔽₃)=2T` → McKay → affine E₆.

Are they the **same** E₆ — on every Lie-theoretic invariant, not just the name? (A priori the character variety
could have been F₄, rank 4; the arithmetic could have produced another type. Neither happened — this verifies they
agree.)

## The checks (all pass)
1. **Exponent recovery — the decisive B264↔B266 bridge.** Remove the affine node from B266's McKay graph of `2T`
   → the E₆ Dynkin diagram; its adjacency eigenvalues are exactly `2cos(π·m/h)`, `h=12`, `m∈{1,4,5,7,8,11}`
   = B264's principal-`sl(2)` exponents. **The McKay graph literally reproduces the character-variety grading.**
2. **Coxeter number.** `Σ` McKay marks of `2T` `= 12 = h(E₆)` = the principal `sl(2)`'s Coxeter number.
3. **Root count / dimension.** `Σ` exponents `= 36 = #positive roots = ℓh/2`; `dim = ℓ(h+1) = 78` (Kostant) =
   B264/B265's adjoint dimension.
4. **Kostant invariant theory (depth).** The Molien series of `2T` (= Poincaré series of `ℂ[x,y]^{2T}`, the
   coordinate ring of the **E₆ Kleinian singularity** `ℂ²/2T`) is `(1+q¹²)/((1−q⁶)(1−q⁸))` — its numerator
   `1+q^h` carries `h=12`, tying the arithmetic side's invariant theory to the geometric side's Coxeter number.

## Conclusion
The arithmetically-selected E₆ and the character-variety E₆ **coincide as Lie-theoretic objects**, on five
independent invariants, with the McKay graph directly reproducing the character-variety's exponent grading.

> **The two E₆'s are one E₆.**

## Honest guardrail (verify-don't-trust)
Coherence of Lie invariants is **not** a proof that the 3d-3d **input** type must be this E₆ (still the sharp
conjecture from B266). What it *does* do: rule out an **incoherence** — the geometric and arithmetic E₆'s are not
two different exceptional groups sharing a label; they are the same object. This tightens wall #2's remaining gap to
a purely **physical** identification (does the 6d type-input equal the manifold's arithmetic type?), with **no
Lie-theoretic obstruction** in the way. Net effect on the wall map: wall #2's only remaining content is now a single
physics conjecture, fully de-risked on the mathematics side.

Anchors: B264 (tangent dim = rank, exponent grading), B265 (E₆-irreducible flat connections exist), B266 (arithmetic
selects E₆), B256 (E₇ homeless). Lit: Kostant 1959 (principal `sl(2)`, exponents, `dim = ℓ(h+1)`), Kostant 1984
(finite subgroups of SU(2), McKay, the Coxeter element); McKay 1980; Springer (regular elements, Coxeter
eigenvalues `2cos(πm/h)`).

## Correction (2026-06-28 adversarial audit / B272)
"**Five independent invariants** coincide ⟹ one E₆" **overstates the evidential weight**. The geometric side is E₆
**by construction** (B264 *chooses* the principal `sl(2)→e₆` and decomposes by E₆ exponents), so once the arithmetic
side is also E₆ (B266), agreement of Coxeter number, exponent *sum*, dimension, and Molien series is **automatic** —
these are invariants of the single Lie algebra E₆, not five independent confirmations. Also: `e6_coherence.py`'s
`e6_dynkin_adjacency()` **hard-codes the E₆ Dynkin diagram**; it does not read `2T`'s McKay graph (the genuine
`McKay(2T)=`affine E₆ derivation is in B266's `mckay_selection_sage.py`). **The genuine, non-tautological content
is exactly two facts:** (i) the arithmetic route *independently* lands on **E₆** (rather than F₄ or another type) —
B266; and (ii) the resulting **exponent set `{1,4,5,7,8,11}`** is the one grading B264's tangent space. That is a
**consistency check** (the two constructions are not in conflict; both are E₆), not five independent measurements.
The physics guardrail (wall #2 still open) is unaffected.
