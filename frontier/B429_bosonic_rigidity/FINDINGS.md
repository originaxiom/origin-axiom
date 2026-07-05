# B429 — Phase I.2: the first-order Bosonic Rigidity Theorem (the E₆↔Lorentz coupling cannot be deformed into fermions)

**Status: banked. The registered B428 question answered, structurally. Firewalled.**

## The theorem (first order)

Along B347's 6-dim unobstructed E₆ moduli of π₁(4₁) at the principal point ρ₀ = principal∘ρ_geo:

**No first-order deformation of the object's E₆ structure produces spinorial matter.**

The moduli splits **6 = 1 geometric + 5 intrinsic**:
- the **geometric** direction (exponent m=1) is exactly the Sym²-block's H¹ — and the Sym² block
  (dim 3) **is the embedded principal sl2 itself** — so this direction deforms ρ_geo along the
  A-polynomial curve and *stays sl2-factored* with the same all-even Sym content: **bosonic**;
- the **five intrinsic** directions (exponents {4,5,7,8,11}) **leave the sl2-factoring locus at
  first order**: embeddings sl2→𝔢₆ are infinitesimally rigid (Whitehead: H¹(sl2,𝔢₆)=0 — verified
  per block: cocycles = coboundaries exactly, all six Sym^{2m}), so the tangent to "factors
  through SOME sl2" is precisely the m=1 line. Along the five intrinsic directions there is **no
  sl2 bridge at all** — no spin assignment of any kind.

With B428 (the coupling point itself is bosonic: 27=[17,9,1]), the Lorentz-coupled point is
**bosonic and 5-direction-isolated**: the unfolding map D cannot source fermions through E₆
deformations of the object.

## What this sharpens (the postulate's search map, updated)

The interface channels for chirality/spin are now narrowed by theorem: not the interior (B425/
Iwasawa rigidity), not the E₆ moduli (this bud) — the remaining live channels are the **boundary
filling** (external slope input), the **seam/gluing** (two-object coupling), and structures
*beyond first order / beyond E₆* (higher-order obstructions vanish to 3rd order by B370, so an
all-orders statement would need the full moduli, logged open).

## Verified legs
(a) 𝔢₆ = ⊕Sym^{2m}, dims [3,9,11,15,17,23], sum 78; the m=1 block has dim 3 = dim sl2.
(b) H¹(sl2, Sym^{2m}) = 0 for all six blocks (exact symbolic cocycle solve).
(c) dim H¹(π₁, Sym^{2m}) = 1 per exponent — banked (B347, lock test_b347).

**Provenance.** rigidity.py → rigidity.json; lock tests/test_b429_bosonic_rigidity.py.
Cross-refs: B428 (the registered question), B347 (moduli), B370 (3rd-order unobstructedness), S049.
