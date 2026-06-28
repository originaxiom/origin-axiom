# B273 — the e₆ cup-product obstruction vanishes identically: the {4,8} deformations integrate to 2nd order

**Status: banked observation (frontier). FIREWALLED — deformation theory of flat connections, NOT physics. Nothing
to `CLAIMS.md`.** Resolves the residual computation flagged by the B272 audit. `e6_obstruction_modp.py`
(sage-python, exact mod `p`) + `e6_obstruction.py` (pyenv, the encoded verdict).

## The flagged residual (B272)
B272's audit found B265's headline "E₆-irreducible flat connections **exist**" rested on **integrability** of the
`{4,8}` directions, and that the decisive object — the `e₆`-bracket-coupled cup-product obstruction
`H¹×H¹→H²(e₆)` — was **uncomputed** (B270 had done only the `SL(2)`/exponent-1 block). This computes it.

## Setup
`ρ_prin = (principal sl(2)→e₆) ∘ ρ_geo : π₁(4₁) → E₆`, acting on `e₆` by `Ad`, built explicitly as
`Ad(ρ_prin(a)) = exp(ad e)`, `Ad(ρ_prin(b)) = exp(t·ad f)`, `t=e^{iπ/3}` — verified to **satisfy the figure-eight
relator** (the 78×78 product `= I`). The tangent space `H¹(π₁, e₆) = ⊕_m H¹(Sym^{2m})` is 6-dimensional (one
cocycle per E₆ exponent `m∈{1,4,5,7,8,11}`). The obstruction to integrating a tangent vector `ξ` is the cup product
`[ξ∪ξ] ∈ H²(e₆) = coker(d¹)` (dim 6), using the **`e₆` bracket** — which couples the exponent blocks (this is
exactly what makes it more than the per-block `SL(2)` computation B270 did).

## Method
Deform `ρ_ε(g) = exp(ε·ad ξ_g) Ad(ρ(g))`; expand the relator to `ε²`. The `ε¹` term is the cocycle condition
(`=0`); the `ε²` term is `ad(q)` with `q∈e₆` the obstruction element; `[q]=0` in `H²` iff `q∈im(d¹)`. Computed
**exactly mod two large primes** `p=99991, 100003` (`≡1 mod 3`, so `t²−t+1` splits) — no precision loss, no
coefficient blowup. (Double precision fails outright: `exp` of the principal nilpotent has `~10¹⁰` entries.)

## Result
Both primes agree: `rank d¹ = 72`, `dim H² = 6`, and the obstruction `q` is a **nonzero 2-cochain** (so the check is
non-vacuous) but `[q]=0` in `H²` — for **all six pure directions** *and* for a **generic random combination** of all
six. By **Schwartz–Zippel** (random point over `𝔽_p`, `p~10⁵`, two independent primes), the **full quadratic cup
product `H¹×H¹→H²(e₆)` is identically zero**. The quadratic cone equals all of `H¹` (dim 6 = rank).

> **No second-order obstruction in any direction.** The `{4,8}` E₆ deformations integrate to second order.

## Conclusion — and the honest residual
The leading (quadratic) obstruction vanishes **identically** at `ρ_prin` — *exactly* the witness that establishes
smoothness in the proven `SL(2)` case (Thurston / B270), now extended to the entire E₆ tangent space. So B265's
"expected to exist" is **upgraded**: the existence of E₆-irreducible flat connections is established **to second
order** (the leading obstruction is gone, for every direction). **Honest residual:** full all-orders smoothness
rests on the higher Massey products `⟨ξ,…,ξ⟩∈H²`, expected to vanish by the same cusp mechanism that gives
smoothness in the `SL(2)` case (`dim H¹=#cusps`, B270), but not separately computed here. The status moves from
"expected" → "established to second order; the leading obstruction vanishes identically."

Anchors: B264 (`dim H¹=6=rank`), B265 (Zariski-density; the existence claim), B270 (the `SL(2)`-block cup product +
cusp mechanism), B272 (the audit that flagged this), B267 (exponents). Lit: Goldman (cup product / obstruction
theory of character varieties); Heusener–Porti (deformations of 3-manifold reps); Thurston (`SL(2)` smoothness).

## Update (2026-06-28 / B274) — the all-orders residual is now closed
The "honest residual" above (all-orders smoothness / higher Massey products) is resolved in **B274**: `ρ_prin` is a
**smooth point** of the E₆ character variety (dim 6 = rank), shown two ways — the boundary/cusp MFP criterion
(certificates dim H¹(M)=6, meridian regular ker(ad e)=6, dim H¹(∂M)=12=2·rank) and the cubic 3rd-order obstruction
vanishing identically. So the existence of the {4,8} E₆-irreducible flat connections is **unconditional**, not
merely to finite order. B265 status: expected → 2nd-order (B273) → smooth point (B274).
