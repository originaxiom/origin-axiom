# PREREGISTRATION — the subalgebra-stabiliser class (new item 1)

**Sealed 2026-08-17, committed BEFORE compute.** Rule 1.

## THE OPERATION CLASS WE NEVER SEARCHED

Baez & Schwahn, arXiv:2606.15235 (13 June 2026), **Theorem 1**, read (not inferred):

> Suppose `X, B` are Jordan subalgebras of `𝔥₃(𝕆)` with `X ≅ 𝔥₂(ℂ)`, `B ≅ 𝔥₃(ℂ)`, `X ⊂ B`.
> Then `Stab(X) ∩ Stab(B)₀ ≅ S(U(2)×U(3))`.

`S(U(2)×U(3)) ≅ (U(1)×SU(2)×SU(3))/ℤ₆` — the Standard Model gauge group. And the paper gives
`Stab(B)₀ ≅ (SU(3)×SU(3))/ℤ₃`, Lie algebra `su(3)⊕su(3)`, **dimension 16**.

**This stabilises SUBALGEBRAS.** Every sweep we ran stabilised **vectors** in the 27/27-bar,
or centralised **elements** of the Lie algebra, or fixed **finite groups**. Stabilising a
subalgebra is none of those. Our "su(3)⊕su(2)⊕u(1) appears in no exhausted class" named a
class and was at risk of being read as naming the question — exactly what `THE_RULE.md`
forbids.

## THE CONNECTION TO WHAT WE ALREADY HAVE

- Our `J^{2T} ≅ K` is a **3-dimensional Jordan subalgebra**. Over ℝ, `K ⊗ ℝ ≅ ℝ³` — which is
  precisely the shape of the **diagonal of `𝔥₃(ℂ)`**.
- Our charge-direction sweep already produced **dim 16, Killing rank 16** (18 of 10556
  directions) — recorded at the time as "su(3)⊕su(3), the trinification direction" and not
  pursued. That is the dimension of `Stab(B)₀`.
- Choosing `X ⊂ B` means choosing a 2×2 block inside the 3×3, i.e. **omitting one of the
  three diagonal idempotents** — a 3-way choice. Ours are a single **Galois orbit** under
  `S₃`, verified.

## DECLARED BEFORE COMPUTE — all outcomes live

| test | outcome and reading |
|---|---|
| **T1** Is `J^{2T}` the diagonal of a 9-dimensional Jordan subalgebra `B ≅ 𝔥₃(ℂ)` of `𝔥₃(𝕆)`? | **yes** → the object determines `B`. **no** → say which subalgebra it *is* the diagonal of, and whether that type appears in Theorem 1. |
| **T2** Is `Stab_{F₄}(B)₀` of dimension 16 with Killing rank 16? | must match the paper. **This is the CONTROL** — if we cannot reproduce `su(3)⊕su(3)`, nothing below is read. |
| **T3** Does the object determine an `X ≅ 𝔥₂(ℂ)` with `X ⊂ B`? | the 3-way choice of omitted idempotent is a **Galois orbit**, so if it works the choice is a *frame choice*, not a free parameter. |
| **T4** `Stab(X) ∩ Stab(B)₀` — dimension 12, Killing rank 11? | **that is the Standard Model algebra.** Our detector is already validated on it (`su(5)` as 5×5 matrices, `Y = diag(2,2,2,−3,−3)` → exactly `(12,11)`). |

## WHAT WOULD MAKE THIS A FALSE POSITIVE

Finding *some* `X ⊂ B` in `𝔥₃(𝕆)` proves nothing — Theorem 1 says **any** such pair works, so
their existence is the paper's result, not ours. **The object must DETERMINE the pair**
(rule 8). If `J^{2T}` merely *sits inside* some `B` among many, with no canonical choice, then
what we have is an import, and it must be booked as one.

## WHAT WOULD MAKE THIS A FALSE NEGATIVE

Concluding "the object does not determine `B`" from a search over the wrong kind of object —
e.g. searching vectors again instead of subalgebras. Rule 9.

## NOVELTY, settled in advance

**The SM-from-`𝔥₃(𝕆)` route is published (June 2026).** Nothing we do here is novel and
nothing may be claimed as such. What would be ours, if it holds, is only the narrower
statement that *this object's* canonical data determines the required pair.
