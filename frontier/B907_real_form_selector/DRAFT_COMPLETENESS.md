# B907-completeness (DRAFT) — the sweep is complete at the pattern level: the sign-locking theorem

**Date:** 2026-08-05 · **Seat:** computation agent (deliverable for the banking
seat; NOT banked by this draft) · **Register item:** B907-completeness (the
cell's registered follow-up, FINDINGS.md "Honest scope") · **Status:** exact
certificates + oblique-rule-compliant numerics; one honest gap, stated below.

## The question

B907 swept 128 representatives (64 inner sign-characters, 64 τ-composites) and
found exactly two C-compatible wall-real involutions, both naming e₆(2). Is the
sweep complete — or could a C-stabilizing involutive automorphism OUTSIDE the
swept family (up to conjugacy by C-stabilizing automorphisms) be wall-real and
realize a form other than e₆(2)?

By B901, every C-stabilizing automorphism acts ±1 on each of the four charges
(x₈, x₁₄, x₁₆, x₂₂), so it carries a pattern ε ∈ {±1}⁴, and the pattern is
invariant under conjugacy by C-stabilizing automorphisms (their own ±-actions
cancel in pairs). The completeness question therefore starts as: WHICH of the
16 patterns can any C-stabilizing automorphism realize?

## The exact kill mechanism (no eigenvectors, no floats)

If θ(x_n) = ε_n x_n then ad(θx_n) = θ ad(x_n) θ⁻¹ = ε_n ad(x_n), so for every
exponent tuple (a,b,c,d), invariance of the trace under conjugation gives

  (ε₈ᵃ ε₁₄ᵇ ε₁₆ᶜ ε₂₂ᵈ − 1) · tr(A₈ᵃ A₁₄ᵇ A₁₆ᶜ A₂₂ᵈ) = 0,   A_n := ad(x_n).

For CONJUGATE-LINEAR θ the conjugated trace is the complex conjugate — and
every mixed moment here is rational (the A_n are rational matrices), so the
same identity holds. One nonzero exact moment with ε-odd exponent parity kills
the pattern for EVERY C-stabilizing automorphism — involutive or not, linear
or antilinear.

## Theorem C1 (sign-locking; exact)

Every C-stabilizing automorphism of the built e₆ satisfies

  **ε₈ · ε₁₆ = +1  and  ε₁₄ · ε₂₂ = +1.**

Exactly the four patterns (a, b, a, b), a, b ∈ {±1}, survive; the other 12 are
dead. The measured pair (x₈, x₁₆) is sign-locked, and so is the unmeasured
pair (x₁₄, x₂₂).

**Certificates** (exact integer-matrix traces, re-verified through an
independent int64 mod-p code path at p = 1000003, 999983, 65537):

- tr(A₁₄ · A₂₂⁵) = −13172147840218514352082453085409194803200000000000 / 19⁵ ≠ 0
  — exponent parity (0,1,0,1), so ε₁₄ε₂₂ = −1 is impossible;
- tr(A₈ · A₁₆ · A₂₂⁴) = 4957259939867182820676192021390557184000000000 / (13·19⁴) ≠ 0
  — exponent parity (1,0,1,0), so ε₈ε₁₆ = −1 is impossible.

Every one of the 12 non-(a,b,a,b) patterns has ε₈ε₁₆ = −1 or ε₁₄ε₂₂ = −1, so
these two moments kill all 12 (per-pattern certificates in
`completeness_results.json`, stage 6).

A finding en route: the kill is INVISIBLE at low degree. The charge Gram is
exactly diagonal — B(x₈,x₁₆) = 0 and B(x₁₄,x₂₂) = 0, alongside every other
off-diagonal pairing — and ALL 65 mixed moments of total degree ≤ 4 vanish in
every odd parity class (only the all-even class is nonzero there). The
smallest killers found sit at total degree 6. The diagonal Gram entries are
B(x₈,x₈) = 241532928, B(x₁₄,x₁₄) = −317708697600, B(x₁₆,x₁₆) = 988843239014400/13,
B(x₂₂,x₂₂) = −889958915112960000/19 (split positive, compact negative — B898's
dichotomy seen by the Killing form).

## Corollary C2 (the wall pattern is unique)

The sealed wall-reality criterion is ε₁₄ = +1 ∧ ε₁₆ = −1. With C1 this forces

  **ε = (−1, +1, −1, +1)** — ε₈ = −1 and ε₂₂ = +1 are FORCED, not observed.

No C-stabilizing involution with any other pattern can be wall-real.

## Theorem C3 (realization: the sweep hits every feasible pattern)

The full 128-representative scan was re-run exactly and independently; the 8
C-compatible representatives were each re-verified as automorphisms on ALL
78² basis bracket pairs, as involutions (φ² = id as full matrices), with
exact patterns and fixed dimensions:

| kind  | χ signs               | pattern        | fix(φ) | fix(φ∘ω) | form of φ∘σ_split |
|-------|-----------------------|----------------|--------|----------|--------------------|
| inner | (1,1,1,1,1,1) = id    | (+,+,+,+)      | 78     | 36       | e₆(6)              |
| inner | (1,−1,−1,1,−1,1)      | (+,−,+,−)      | 38     | 36       | e₆(6)              |
| inner | (−1,1,1,−1,1,−1)      | (+,−,+,−)      | 38     | 36       | e₆(6)              |
| inner | (−1,−1,−1,−1,−1,−1)   | (+,+,+,+)      | 38     | 36       | e₆(6)              |
| outer | (1,1,−1,−1,−1,1)      | (−,−,−,−)      | 36     | 38       | e₆(2)              |
| outer | (1,−1,1,−1,1,1)       | (−,+,−,+) WALL | 36     | 38       | e₆(2)              |
| outer | (−1,1,−1,1,−1,−1)     | (−,+,−,+) WALL | 52     | 38       | e₆(2)              |
| outer | (−1,−1,1,1,1,−1)      | (−,−,−,−)      | 36     | 38       | e₆(2)              |

Every composite φ∘ω was verified to be an involution (a check the original
selector sampled; here it is exact and complete). All four feasible patterns
are realized; hence **the sweep is complete at the pattern level: feasible =
realized = {(a,b,a,b)}**. Two structural readings:

- ε₈ = +1 ⟺ inner ⟺ the conjugation realizes e₆(6); ε₈ = −1 ⟺ outer ⟺ e₆(2).
  C-compatible conjugations in the swept family reach exactly TWO real forms.
- The wall-pattern class already contains two DIFFERENT Aut-classes of φ
  (fix 36 = C₄-type and fix 52 = F₄-type — not conjugate in Aut(e₆) at all),
  and both composites name e₆(2): the φ-class is not a pattern invariant, but
  the named form was constant across everything realized.

## The corrected weight census (the oblique-readout-compliant layer)

The joint C-weight system of the 78-dim adjoint was recomputed with
COMPONENTWISE eigenvalue extraction — each joint eigenvector v of a generic
real combination of the four commuting A_n, each eigenvalue read from
A_n v = λ v at the largest component of v, never a Rayleigh quotient — at
45 digits, two independent generic combinations, with certified windows:
max residual ~5·10⁻²³ ≪ clustering tolerance 10⁻¹² ≪ minimum inter-weight
separation ≈ 1.06·10⁶ (absolute, sup-norm). Exact anchors all hit: zero-weight
multiplicity 12 = dim z(C); per-charge kernel counts 30/12/30/12 = B898's
exact census; λ₈, λ₁₆ real and λ₁₄, λ₂₂ imaginary; Σ λ_m λ_n equal to the
exact Gram (mixed power sums match exact traces to ≤ 10⁻²⁶ relative); the
multiset closed under conjugation. Both seeds give the SAME weight system:
31 distinct joint weights, multiplicity profile {0-weight ×12, eighteen
weights ×3, twelve weights ×1} (12 + 54 + 12 = 78). The 16-pattern multiset
census on BOTH seeds returned exactly the four (a,b,a,b) patterns — in full
agreement with the exact certificates, and correcting the retracted
Rayleigh-quotient census (which had contradicted the sweep's own exact
automorphisms).

Cautionary (logged): a first pass with the clustering tolerance BELOW the
residual scale (10⁻²⁵) split clusters seed-dependently (70 vs 72) and
mis-counted kernels — the window certificates above exist to rule exactly
that failure mode out.

## The reduction within the wall pattern (what constrains any unswept φ′)

Exact structure computed:

- z(C) is 12-dimensional with center exactly C (4-dim) and derived algebra
  8-dim: z(C) = C ⊕ [z(C), z(C)].
- ker(ad x₈) = ker(ad x₁₆) EXACTLY (each 30-dim, intersection 30-dim). The
  wall pattern's ε-fixed subalgebra is a := ker(ad x₈) ∩ ker(ad x₁₆), 30-dim.
- rank((ad x_n)²) = rank(ad x_n) for all four charges (48/66/48/66, exact) —
  the generalized 0-weight space equals the literal kernel (no Jordan blocks
  at 0), so the ε-fixed subspace IS a exactly and the pairing formula below
  is exact, not merely generic.
- Any C-stabilizing involution φ′ with the wall pattern maps the weight space
  W(λ) to W(ελ); the ε-swapped pairs contribute exactly (78 − 30)/2 = 24 to
  its fixed dimension, so fix(φ′) = 24 + fix(φ′|_a). Verified exactly on the
  two swept representatives: fix(φ₁) = 24 + 12 = 36, fix(φ₂) = 24 + 28 = 52.
- Any two C-stabilizing involutions with the same pattern differ by an element
  of Z_Aut(C), the ELEMENTWISE centralizer of the torus: φ′ = φ₁ ∘ g. The two
  swept wall representatives differ by g = φ₁φ₂ = the inner all-minus
  character exactly (a 2-torsion element of Z_Aut(C), fix 38).
- Identity-component rigidity: for g = exp(ad z) with z ∈ z(C), φ₁ z = −z
  (the −1 eigenspace of φ₁ on z(C) is 6-dim), the involution φ₁ ∘ exp(ad z)
  equals exp(−ad z/2) φ₁ exp(ad z/2) — conjugate to φ₁ BY a C-stabilizing
  automorphism (the identity uses only ad-equivariance of φ₁, verified
  exactly on z(C) samples). Such deformations change neither the pattern nor
  the named form.

## What is now a theorem, and the honest gap

**Theorem (completeness, pattern level).** Every C-stabilizing automorphism
of the built e₆ has pattern (a,b,a,b); all four patterns are realized by the
swept family; the unique wall-real-compatible pattern is (−1,+1,−1,+1); and
within everything realized — the swept 128 and their involutive
exp(z(C))-deformations (the φz = −z family of the rigidity bullet) —
wall-real conjugations name e₆(2) and only e₆(2). The e₆(−14) obstruction and
the B907 existence statement are unconditionally confirmed.

**The honest gap (form level).** The component group of Z_Aut(C) is not
enumerated. A wall-real involution realizing a form other than e₆(2) is not
fully excluded by this cell; what IS proved is that any such φ′ would need
(i) the exact pattern (−1,+1,−1,+1), (ii) to differ from φ₁ by an element of
Z_Aut(C) lying OUTSIDE the identity component and outside everything the
sweep reaches (the found 2-torsion included), and (iii) to satisfy
fix(φ′) = 24 + fix(φ′|_a) with φ′|_a an involution of the 30-dim subalgebra
a. No such element is exhibited; both known wall classes (C₄-type and
F₄-type) name e₆(2). Closing the gap = enumerating π₀(Z_Aut(C)) (equivalently
the φ₁-twisted H¹ over it) — a registered follow-up, not claimed here.

Note against the register's anticipated shape: the expectation "only the
trivial pattern and (−1,+1,−1,+1) survive" was WRONG in detail — (+,−,+,−)
and (−,−,−,−) also survive and were already realized inside the banked sweep
itself. The correct completeness statement is the sign-locking theorem C1.

## Independent re-verification (second pass, fresh code path)

Every load-bearing fact was re-verified through `completeness_verify.py`
(exit 0 = all assertions pass; `completeness_verify_results.json`):

- exact arithmetic redone over sympy DomainMatrix/ℚ (the original path was
  numpy object-int with manual denominator bookkeeping) — commutation of all
  6 charge pairs, both kill certificates recomputed exactly (values match to
  the digit), the full 65-moment low-degree census (all odd-parity moments 0,
  the diagonal Gram values match);
- the certificates re-verified a THIRD way, modulo the fresh primes
  101 / 2003 / 9973 (disjoint from stage 7's 1000003/999983/65537), rational
  entries mapped by modular inverse — residues match the exact values;
- the 8 C-compatible representatives re-verified as automorphisms on all 78²
  basis bracket pairs through the frame's own br() on full vectors (not the
  original's replicated coefficient bookkeeping), as involutions, with
  patterns, fixed dims (signed-cycle count AND DomainMatrix rank, agreeing),
  and ω-composite fixed dims 36 (inner) / 38 (outer); the 128-rescan again
  finds exactly these 8;
- structure ranks (48/48/48 ⟹ kernel equality; 4-stack 66 ⟹ dim z(C) = 12),
  the no-Jordan-block certificate, the wall-pair bookkeeping 36 = 24+12 and
  52 = 24+28, and φ₁∘φ₂ = the inner all-minus character, all exact;
- the pattern logic replayed independently: the two certificates kill exactly
  the 12 non-(a,b,a,b) patterns; survivors = realized; the unique wall-
  compatible survivor is (−1,+1,−1,+1).

A full re-run of `completeness.py` regenerated `completeness_results.json`
deterministically (byte-identical numeric content; the sole diff was one
whitespace character in a prose note edited after the first run).

## Files

- `completeness.py` (this cell; run from a scratch cwd — the B854 frame
  clobbers relative-path artifacts; the script now also redirects `__file__`
  before exec'ing the frame so the frame's own results.json lands in the
  scratch cwd, never the arc dir) → `completeness_results.json`
  (stages: 0 exact frame/commutation; 1 low-degree moment table + diagonal
  Gram; 2 the 128-rescan + deep exact verification of the 8 C-compatible
  representatives + ω; 3 z(C)/kernel structure; 4 wall-pair restriction
  bookkeeping; 5 the corrected componentwise weight census, 2 seeds;
  6 adaptive exact kill certificates for all 12 dead patterns;
  7 independent mod-p re-verification of the certificates).
- `completeness_verify.py` (the independent second pass, above) →
  `completeness_verify_results.json`.
- Provenance caution for the banking seat: the BANKED `results.json` in this
  arc contains the B854 frame's verdict, not the selector sweep — the frame's
  `__file__`-inherited write clobbered it pre-commit during the selector era.
  Nothing load-bearing is lost (the sweep lives in `sweep_results.json` /
  `results_complete.json`, and the lock test reads `sweep_results.json`),
  but `real_form_selector.py`'s intended output was overwritten; regenerate
  if wanted.

## Depends on

B854 (the frame), B898 (exact per-charge census — matched here), B901 (the
±-diagonal constraint — the premise), B907 (the sweep — re-verified here),
B893 (ω, the form-naming convention — inherited, not re-derived).
