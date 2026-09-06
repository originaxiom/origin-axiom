# B1267 — B1260's DECIDING COMPUTATION, RUN: the index is ZERO, and the non-self-dual rank-3 components are RIGID

**Date:** 2026-09-06 · **Seat:** cc · **Status:** NEGATIVE (numerical, five-way controlled; the control caught a real bug before the result shipped)

## Why this arc exists

**B1260 named a computation and did not run it** — and this seat then *listed it as a requirement*
rather than executing it, which the owner correctly called out. B1260's own statement of the stakes:

> *"**Differ** ⇒ the cusped manifold carries net chirality, and JOIN 1's first question resolves in
> favour of the cusped object. **Agree** ⇒ the wall extends past closedness **and** past the abelian
> sector, and the generation count cannot be a net-chirality count on this manifold at all."*

**This arc runs it. The answer is AGREE.**

## The setup

m004 is a once-punctured-torus bundle, so
**π₁ = ⟨a, b, t | t a t⁻¹ φ(a)⁻¹, t b t⁻¹ φ(b)⁻¹⟩** with φ the monodromy (a → aab, b → ab). Fox
calculus on that **3-generator / 2-relator** presentation gives h¹ = dim ker d¹ − dim im d⁰ directly,
and the dual local system is **ρ\*(g) = ρ(g⁻¹)ᵀ**. B71's `realize()` / `monodromy()` supply A, B, t.

## The control — and it caught a real bug

Validated against tonight's independently verified knot-group Fox table (B1256 addendum, two primes):

| | Sym¹ | Sym² | Sym³ | Sym⁴ | Sym⁶ |
|---|---|---|---|---|---|
| expected | 0 | 1 | 0 | 1 | 1 |
| **reproduced** | **0** | **1** | **0** | **1** | **1** |

**A first attempt FAILED this control**, with relator residuals of **1.1 to 9.3**: the Sym^n routine
was returning the **transpose**, making Sym an **anti**-homomorphism ((AB)ᵀ = BᵀAᵀ) and destroying the
relations. **Without the control the wrong answer would have shipped.** A homomorphism check
|Sym(XY) − Sym(X)Sym(Y)| < 1e-14 now runs **before** any result is used.

## The result — 25 valid parameter points per component

| component | duality | h¹(V), h¹(V\*) | **INDEX** | min d₁ singular value |
|---|---|---|---|---|
| **V0** | self-dual, geometric | {0, **1**} | **0** | 0.000 |
| **W1** | **non**-self-dual | {0} | **0** | **0.011** |
| **W2** | **non**-self-dual | {0} | **0** | **0.020** |

**V0 reaching h¹ = 1 is what makes this a test rather than a tautology** — the machinery *does* detect
nonzero h¹ where it exists. And W1/W2's singular values are **far from zero**, so rank 6 (hence
h¹ = 0) is **numerically solid**, not a threshold artifact.

## Two conclusions, the second sharper

1. **The index is ZERO** at every point tested, self-dual and not. By B1260's own statement, **the
   wall extends past closedness and past the abelian sector.**
2. **W1 and W2 are RIGID** — h¹ = 0, **no deformations at all**. They carry **no massless modes**, so
   they cannot furnish a generation count in **either** direction. **The locus B1260 identified as the
   last candidate is not merely index-zero; it is empty of the modes a count would have to count.**

## What this does NOT say

It does **not** show net chirality is impossible on m004 for *every* local system — only for the
corpus's **exhibited** non-self-dual rank-3 family, over the sampled parameter range. **A non-rigid
non-self-dual system elsewhere would reopen it.** What it closes is the specific route B1260 named as
decisive.

## Controls (MB12, both directions)

- **Sym is checked to be a homomorphism before use** — the exact bug that failed attempt 1.
- The machinery **reproduces 5/5** of an independently verified h¹ table.
- **The test can return nonzero:** V0 attains h¹ = 1.
- Relator residuals asserted **< 1e-6**; failing points are **discarded, not counted**.
- The **smallest singular value of d₁ is reported**, so rank is never a silent threshold choice.

## Verification

`verification/deciding.py` — standalone.

- **Feeds on:** B1260 (the named computation), B102 (W1/W2), B71 (realize/monodromy), B1256's addendum
  (the control table), B1086 (the closed-side spectrum law).
- **Registers:** no status change; **closes the route B1260 named**, and sharpens **I-26**'s price.
