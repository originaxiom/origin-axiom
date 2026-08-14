# B804 — the Dirac spectrum of m004: the structure is settled, the eigenvalues need machinery

cc banking seat, 2026-07-29. **Prereg `b955c637ae6a46ba`, sealed and committed at `9d298657`
BEFORE any computation.** Mathematics only — no physics reading, no Gate 5 surface, nothing to
`CLAIMS.md`. No spinor is read as a fermion.

## The result against the pre-stated expectation

The prereg predicted Cell 1 returns **bounding** (forced) and flagged Cell 2 as the honest risk,
naming *"the structure is settled; the eigenvalues need the numerical machinery"* as a **legitimate
terminal state provided it is reported as such and not dressed up.** That is the outcome.

## Cell 1 — the cobordism computation (COMPUTED, exact)

`Ω^spin₂ ≅ ℤ/2`, detected by the Arf invariant. On `T²` in the `(μ, λ)` basis:

| (a,b) | Arf | bounds? |
|---|---|---|
| (0,0) | 0 | yes |
| (0,1) | 0 | yes |
| (1,0) | 0 | yes |
| **(1,1)** | **1** | **no** — the Lie structure, the generator |

Exactly one non-bounding class, as `Ω^spin₂ = ℤ/2` requires — verified, not assumed.

**The bordism step:** the cusp cross-section of a one-cusped spin 3-manifold **bounds the compact
core**, so `[T², σ] = 0` in `Ω^spin₂`, so **Arf = 0**, so the induced cusp structure is the
**bounding** one — for **every** spin structure on the 3-manifold. Hence for **both** of m004's two
(B279), and **identically for m003's two**.

**Consequence:** the Dirac spectral *type* is determined, identical across both spin structures, and
identical for the sister ⟹ **CLASS-level by construction (E34)**. The m003 scope sub-cell is a
**corollary, not a check**.

**Cited, not derived:** the implication *bounding cusp structure → spectral type* (Bär, *J. Diff.
Geom.* **54** (2000) 439, restated via Martelli–Reid). This arc does **not** re-derive it and does
**not** assert its direction from memory.

## Cell 2 — the Weyl caveat, made concrete (COMPUTED)

The prereg declared **in advance** that leading-order agreement is not a result. Demonstrated rather
than asserted, with `vol(m003) = vol(m004) = 2.0298832128`:

| λ | N_m004(λ) | N_m003(λ) | difference |
|---|---|---|---|
| 10 | 68.556723 | 68.556723 | **0.0** |
| 40 | 4387.630289 | 4387.630289 | **0.0** |
| 80 | 35101.042309 | 35101.042309 | **0.0** |

Identically zero, because the only manifold-dependent input at leading order is the **volume**, and
the volumes coincide. **This is not a measurement; it is an identity.** Any real separation must be
**fluctuation-level** — exactly where B790 found the Laplacian one.

## Cell 3 — NOT PERFORMED, and why (the honest terminal state)

**No Dirac eigenvalue was computed in this arc.** A cusped-manifold Dirac eigenvalue computation
requires a spinor-valued Hejhal-type collocation solver — the Maass machinery's analogue, with
spinor-valued Fourier–Bessel expansions on the cusp and a spin-structure-dependent boundary
condition. That is a **major numerical undertaking on the scale of the Maass work**, not a session's
computation.

Claiming otherwise is explicitly listed in the prereg's §5 as a failure of this arc, so it is
reported plainly: **the structure is settled; the eigenvalues need machinery that does not exist in
this repository.**

## What this arc actually establishes

1. The Dirac **spectral type** for m004 is **determined and class-level** — it cannot separate the
   object from its commensurability class. That is a *structural* result and it is the one the
   campaign was designed to be able to return.
2. The **leading-order** Dirac data likewise cannot separate them — proved by identity, not tested.
3. Therefore **any** future Dirac separation must live in the **fluctuations**, and the campaign's
   real falsifier is that comparison — which is **expensive**, and was mis-advertised as cheap in
   the first draft.

## The methodological finding, which outlived the campaign

The first draft placed a bounded falsifier at Cell 2 and the literature gate **after** it. The kill
branch was **excluded by a theorem nobody had retrieved**, so the falsifier could never fire. The
flaw was **ordering**, not reasoning — the campaign correctly demanded a literature gate and then
put it downstream of the falsifier it governs.

> **A bounded falsifier declared before its governing theorem is retrieved is not yet known to be a
> falsifier.** A falsifier that cannot fire is decoration, and worse than none, because it
> advertises a rigour the design does not have.

Registered in `docs/PRACTICES.md`. This is the durable output of the arc.

## Residual, registered

- **The spinor-Hejhal solver** — the one thing standing between this arc and Cell 3. Bounded and
  specifiable, but a real build.
- If it is ever built, the comparison **must** be fluctuation-level; §3 of the prereg forbids
  reading leading-order agreement as a finding, in advance.

`dirac.py` · prereg `b955c637ae6a46ba` · lock `tests/test_b804_dirac.py`
