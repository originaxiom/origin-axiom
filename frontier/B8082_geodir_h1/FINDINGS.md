# B8082 — the geodir dimension count is COMPUTED, and one adjective in it is not

**Date:** 2026-08-19 · **Seat:** cc3 (audit) · **Lane:** MATHEMATICS. **Gate 5:** untouched.
**Verdict: PROVED** for the `H¹` count; **the unobstructedness is registered as owed.**
Reproducer `geodir_h1.py`. **Not preregistered** — the targets are the paper's own.

## What the paper owed

`Scope (geodirscope)` says of Proposition (geodir), in its own words:

> *"We give neither a proof nor a citation for the dimension count, and it should be read as
> unverified. It is a deformation-cohomology statement — **which `H¹` is six-dimensional, and why
> it is unobstructed** — and this paper does not compute it."*

External review flagged it as load-bearing. **The first half is computed here. The second is not,
and saying which is which is the point.**

## The structure that makes it tractable

`ρ₀` factors through `SL(2)`, so as a `π₁`-module `𝔢₆` decomposes by principal-`𝔰𝔩₂` exponent:

```
  𝔢₆ = ⊕_{m ∈ {1,4,5,7,8,11}} Sym^{2m}(V₂),      3 + 9 + 11 + 15 + 17 + 23 = 78
```

and twisted cohomology follows the decomposition — six small problems instead of one 78-dimensional
one.

## The representation, and its control

`π₁(4₁) = ⟨a,b | a·w = w·b⟩` with `w = b⁻¹ab⁻¹a⁻¹`. The parabolic pair `A = [[1,1],[0,1]]`,
`B = [[1,0],[t,1]]` satisfies the relator **exactly when `t² − t + 1 = 0`** — so `t` is a primitive
sixth root of unity and the trace field is **ℚ(√−3)**, the figure-eight's. That is the control that
this is the geometric representation and not some other solution of the relator.

## The result

Fox calculus on the one-relator presentation, block by block, exact over `𝔽ₚ` at three primes with
`6 | p−1`:

| exponent `m` | `dim Sym^{2m}` | `H⁰` | `Z¹` | `B¹` | `H¹` |
|---|---|---|---|---|---|
| 1 | 3 | 0 | 4 | 3 | **1** |
| 4 | 9 | 0 | 10 | 9 | **1** |
| 5 | 11 | 0 | 12 | 11 | **1** |
| 7 | 15 | 0 | 16 | 15 | **1** |
| 8 | 17 | 0 | 18 | 17 | **1** |
| 11 | 23 | 0 | 24 | 23 | **1** |
| | **78** | | | | **6** |

**`dim H¹ = 6`**, the split is **1 + 5**, `H⁰ = 0` in every block so `B¹` is full and the count is
clean, and the exponent-1 block is `Sym²(V₂)` — **the adjoint of `𝔰𝔩₂`, i.e. the embedded principal
`𝔰𝔩₂` itself**, exactly as the proposition says. Three primes agree.

## One thing the paper does not say, and should

**`m = 2, 3, 6` are not exponents of `E₆`, and they give `dim H¹ = 1` too.** So the per-block
contribution of 1 is a property of *this manifold* and `Sym^{2m}`, **not** of which exponents `E₆`
happens to have. The six is therefore the **number** of exponents — `rank(E₆) = 6` — and the
*"1+5 split by exponent"* is a way of counting, not a discovery about `E₆`. The current phrasing
invites the stronger reading; it should not.

## What is NOT computed

**Unobstructedness.** The proposition says *"the **unobstructed** `E₆` moduli"*, and this arc
computes `H¹` only. The twisted Euler characteristic of a knot exterior is zero and
`H⁰ = H³ = 0`, so **`dim H² = dim H¹ = 6`**: the obstruction space is **not** zero, and
unobstructedness follows from **no** dimension count available here. It needs genuine obstruction
theory or a citation. **Registered as owed, not asserted.**

**And nothing about selection changes.** `ρ₀` is *defined* using the principal embedding, so a
statement computed at that point cannot distinguish it from other `𝔰𝔩₂`-subalgebras. **(C6) remains
a fully priced choice**, exactly as its own scope already records. This arc verifies a count; it
does not upgrade a choice.

## SCOPE

The member only — `m004`'s fundamental group and one representation of it. Nothing about the class,
the sisters or the rows; no physical identification.
