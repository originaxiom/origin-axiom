# B274 — ρ_prin is a smooth point of the E₆ character variety: existence is unconditional (all orders)

**Status: banked observation (frontier). FIREWALLED — deformation theory of flat connections, NOT physics. Nothing
to `CLAIMS.md`.** Upgrades B273 ("integration to second order") to all orders. `b274_smoothness_modp.py` (sage,
exact mod p) + `b274_smoothness.py` (pyenv verdict).

## What B273 left open
B273 proved the quadratic cup-product obstruction `H¹×H¹→H²(e₆)` vanishes identically → the E₆ deformations of
`ρ_prin` integrate **to second order**. The honest residual was all-orders smoothness (higher Massey products). This
closes it, two independent ways.

## Route (b) — the boundary/cusp closer (the actual all-orders argument)
The Heusener–Porti / Menal-Ferrer–Porti criterion (already cited in B265 for the analogous statement): for a
one-cusped hyperbolic `M`, if the restriction `H¹(M,Ad ρ)→H¹(∂M,Ad ρ)` is injective and the boundary character
variety is smooth at `ρ|_{∂M}`, then `ρ` is a **smooth point** of `X(M)` of dimension `½·dim H¹(∂M)`. Every
hypothesis is a finite integer certificate, computed exactly mod p (both primes agree):

| certificate | value | meaning |
|---|---|---|
| `dim H¹(M, e₆)` | **6** | tangent space (= B264) |
| `dim H²(M, e₆)` | **6** | obstruction space |
| `ker(ad e)` (meridian regular) | **6 = rank E₆** | the meridian holonomy `exp(ad e)` is a **regular** unipotent ⇒ boundary T²-variety smooth at `ρ|_{∂M}`, and `H⁰(∂M,e₆)=ker(Ad(μ)−I)=ker(ad e)=6` |
| `dim H¹(∂M=T², e₆)` | **12 = 2·rank** | `= 2·dim H⁰(∂M)` (Euler char 0 on T²) |
| restriction injective | yes | half-lives-half-dies: the image is a Lagrangian of dim `6 = dim H¹(M)` (B270, per exponent block) |

⟹ `ρ_prin` is a smooth point of dim `½·12 = 6 = rank(E₆)`. **All orders.** *Honest footnote:* the *implication* is
the cited MFP criterion, not re-derived in-sandbox — exactly the epistemic footing of the SL(2)/Thurston smoothness
statement already in the program.

## Route (a) — the cubic (3rd-order) obstruction, independent in-sandbox corroboration + falsification gate
Extend B273's relator ε-expansion to ε³ with the deformation `ρ_ε(g)=exp(ε·ad ξ_g + ε²·ad η_g)Ad(ρ(g))`: construct
the **actual** bounding cochain `η` with `d¹(η)=−q` (B273 only proved one exists), confirm the ε² coefficient
vanishes (`o2`), then the ε³ coefficient is `ad(q3)`; test `[q3]=0` in `H²`. Both primes: `[q3]=0` for **all six
exponent directions and a generic combination**, with `q3` a *nonzero* cochain (non-vacuous) and the verdict
**invariant under the η-indeterminacy** (`η → η + ker d¹`). A nonzero cubic would have **refuted** smoothness; it
does not.

## Conclusion
`ρ_prin` is a smooth point of the E₆ character variety of the figure-eight, of dimension `6 = rank(E₆)`. The
`{4,8}` E₆-irreducible flat connections (B265) therefore **exist unconditionally** — not merely to finite order.
B265's status: "expected" (B272) → "to second order" (B273) → **"unconditional (smooth point)"** (here). The one
remaining honesty note is shared with the whole program: the MFP smoothness *criterion* is cited, not re-proven.

Anchors: B264 (dim H¹=6=rank), B265 (existence/density), B270 (per-block cusp mechanism, half-lives), B273 (quadratic
obstruction = 0). Lit: Heusener–Porti; Menal-Ferrer–Porti (twisted cohomology / smoothness for hyperbolic
3-manifold reps); Thurston (SL(2) smoothness); Goldman (obstruction theory).

## Novelty (R6, 2026-06-28)
**KNOWN (framework).** The dim-`= rank` count is **Falbel–Guilloux 2015** (general reductive `G`, incl. E₆); the
smooth-point/cohomology mechanism is **Menal-Ferrer–Porti** (the criterion this result cites), applying termwise to
the Kostant exponents. B274 (and B264/B273/B275) is a **worked E₆ instance with explicit computation, not a new
theorem** — consistent with the honest footnote above (criterion cited, not re-derived). See
`frontier/B264_e6_character_variety/NOVELTY.md`, `docs/NOVELTY_AUDIT.md` R6.
