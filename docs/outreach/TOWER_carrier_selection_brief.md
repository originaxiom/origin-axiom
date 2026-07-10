# Tower — the forced Sym⊗det block form, and the carrier-selection rule at n ≥ 5

**For:** an invariant theorist / geometric representation theorist (classical two-matrix invariant
theory; `GL(2)`-module structure of trace rings). **Status:** honest — the block *form* is proved at
probe-writeup strength for all `n`; the residual is a precisely located static invariant-theory
question.

## Setup (self-contained)

Let `X_n = Hom(F₂, SL_n(ℂ)) // SL_n` be the SL(n) character variety of the free group `F₂`, and let
`x₀` be the trivial character. An automorphism `φ ∈ Aut(F₂)` with abelianization `N ∈ GL(2, ℤ)`
induces a polynomial "trace map" `T_φ` on `X_n`, fixing `x₀`. Write `V` for the standard 2-dimensional
`GL(2)`-module and `D = det` for the determinant character. The internal "tower" is the sequence of
characters `char(ρ_n)` of these trace maps on the cotangent space; the standing prize is the identity
`char(ρ_n) = ∏_d char(Sym^d M)^{μ_d}` (a Witt/necklace-type product form).

## The filtration theorem (the new reduction — dynamics eliminated)

On the **intrinsic** cotangent space `𝔪/𝔪²` at `x₀`:

1. **(formal slice)** `Ô_{X, x₀}` is the completion of the graded invariant ring
   `R = ℂ[sl_n ⊕ sl_n]^{SL_n}` via `(A, B) = (eᵃ, eᵇ)`; completing does not change `𝔪/𝔪²`.
2. **(order is preserved)** `T_φ*` acts by `f ↦ f∘Φ` with `Φ = N ⊗ id_{sl_n} + O(deg 2)` (by BCH),
   and `N ⊗ id` is invertible, so `T_φ*` preserves the order filtration and its lowest term is
   `f_d ∘ (N ⊗ id)`.
3. **(graded = a static module)** hence `T_φ*` preserves the decreasing filtration with graded
   pieces `G_{n,d} := R_d / (\text{decomposables})_d` — the degree-`d` **indecomposable invariants
   of two traceless `n×n` matrices** (Procesi's first fundamental theorem: spanned by trace words) —
   and acts on `gr_d` by the natural `GL(2)`-action of `N`.

**Consequence:** `char(T_φ* | 𝔪/𝔪²) = ∏_d char(N | G_{n,d})`, and since each `G_{n,d}` is a rational
`GL(2)`-module `⊕_j (Sym^{d−2j}V ⊗ D^j)^{m_{d,j}}`,

> **the Sym-⊗-det-block FORM of the tower is FORCED, for every `n` and every monodromy `N`**
> (dependence on `N` alone is manifest); **only the static multiplicities `m^{(n)}_{d,j}` remain.**

The trace-map dynamics has been eliminated: the conjecture becomes classical two-matrix invariant
theory plus one splitting problem. Label: proved at probe-writeup strength (standard cited
ingredients — the formal Luna slice, Procesi's FFT, BCH — with the `N`-vs-`N⁻¹` convention pinned
empirically); a full formal writeup is deferred, and this is deliberately not promoted to the
catalog as PROVED.

## What is settled, and where it stalls

- **First arm, all `n` (proved intrinsically).** By Chevalley, `ℂ[sl_n]^{SL_n} = ℂ[tr a², …, tr aⁿ]`,
  so the untwisted-`Sym^d` multiplicity in `G_n` is `[2 ≤ d ≤ n]` for **all** `n` — the catalog's
  first arm, including its Cayley–Hamilton cutoff at `d = n`. The character-level bookkeeping is also
  closed for all `n`: the product form `≡` the two-sequence catalog is now an identity for every `n`
  (previously verified to `n = 8`), so proving the catalog for all `n` **is exactly** proving
  `char(ρ_n)` equals the product form.
- **Carriers vs extras, small `n` (computed, exact ranks).** For `n ≤ 4` the degree filtration
  **separates** carriers (degree ≤ 5) from extras (degree ≥ 6): the catalog is the canonical
  `T*`-stable quotient — no choices. (`n = 2` re-derives the free ring; `n = 3` matches Lawton's 9
  generators, with Lawton's `t9` = the `D³` generator; `n = 4` carries exactly the `n²−1 = 15`
  catalog carriers.)
- **The n = 5 wall.** From `n = 5` the second-arm carrier `Sym²⊗D²` at degree 6 and the first extra
  sit in the **same graded piece as a 2-dimensional isotypic multiplicity space**, which the
  filtration cannot split. Concretely `G_{5,6} = (Sym²⊗D²)² ⊕ D³`: the "doubled `Sym²`" carrier
  (multiplicity 2, an exact certificate) collides with the first extra in one graded piece. This is
  precisely the historically contested piece. For `n ≥ 5` the catalog is therefore not singled out by
  the degree filtration alone.

## The single question

> Is there a **canonical, filtration-independent rule** that selects the `(n²−1)`-dimensional carrier
> submodule inside the multiplicity space of `G_{n,d}` for `n ≥ 5` — equivalently, that identifies the
> banked `(n²−1)`-dimensional Jacobian as a canonical `T*`-subquotient of `𝔪/𝔪²`? Concretely: what
> canonically picks out the correct copy in the 2-dimensional isotypic space of
> `G_{5,6} = (Sym²⊗D²)² ⊕ D³`? A natural candidate is the **opposition-involution height grading**
> (`θ = −w₀` on the `A_{n−1}` root system) as a second grading on `G_{n,d}`, independent of the
> degree filtration — does it provide the splitting?

No trace map, no auxiliary series, and no Procesi symmetrization are needed for this: it is a purely
static question about the `GL(2)`-module structure of the indecomposable two-matrix invariants.

## Honest scope

The block form is proved for all `n` at writeup strength; the multiplicities `m^{(n)}_{d,j}` are the
hard part of classical two-matrix invariant theory, fully known only for small `n`, and were computed
here only to `n = 6`. A residual hint (not load-bearing): the extras look like a `D³`-twisted third
arm, suggesting `G_n` is a stack of det-twisted arms of which the catalog keeps exactly two — if that
closed form holds, the splitting rule may fall out of it.

**Provenance.** Rests on B503 (the filtration theorem, the all-`n` character-layer closure, the first
arm proved intrinsically, and the located n=5 wall), building on B103/B104 (the tower and its walls),
B117/B121/B122 (the two-sequence / product form), and B62/B112 (the opposition-involution grading, the
candidate splitting rule). Standard ingredients: Procesi (matrix-invariant FFT), Lawton (SL(3) trace
coordinates). Nothing promotes to `CLAIMS.md`.
