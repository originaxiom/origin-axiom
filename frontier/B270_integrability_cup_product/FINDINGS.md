# B270 — integrability recomputed: the cup-product obstruction vanishes; deformations are cusp deformations

**Status: banked observation (frontier). FIREWALLED — deformation theory of flat connections, NOT physics.
Nothing to `CLAIMS.md`.** The rigor upgrade flagged in the B268 audit (Phase 3): B265 *cited* the smoothness of the
geometric rep for integrability; here it is **computed**. `integrability_cup_product.py` (pyenv, sympy + mpmath;
imports B264 for `Sym^n`).

## (A) The cup-product obstruction (SL(2,ℂ)/Sym² — the geometric / exponent-1 foundation)
Deform `ρ_ε(g) = exp(ε·ξ_g) ρ₀(g)`. The relator `ρ_ε(r)=I` expands as
- `ε¹`: `L(ξ) = 0` — `ξ` is a cocycle (`Z¹`);
- `ε²`: `Q(ξ) + L(η) = 0` — solvable for the 2nd-order `η` **iff** `Q(ξ) ∈ im(L) = im d¹`.

`Q(ξ)` is the quadratic obstruction (the cup product `ξ∪ξ` via the Lie bracket); its class `[Q(ξ)] ∈ H² =
coker(d¹)` is *the* obstruction to integrating `ξ`. Computed **exactly** at `t=e^{iπ/3}`:
`dim Z¹=4`, `dim B¹=3` → `dim H¹=1`; for the `H¹` representative `ξ`, `L(ξ)=0`, and **`Q(ξ)` is a coboundary**
(in `im d¹`), so `[Q(ξ)]=0`.

> The figure-eight `SL(2,ℂ)` character variety is **smooth at the geometric rep — re-derived, not cited.**

## (B) The mechanism for all exponents (why the `{4,8}` E₆ directions integrate)
`dim H¹(M, Sym^{2m}) = #cusps = 1` for all `m` (B264 / Menal-Ferrer–Porti). The cusp cohomology has
`dim H¹(∂M=T², Sym^{2m}) = 2·dim(Sym^{2m})^{peripheral} = 2·1 = 2` (the parabolic fixes one line, the highest
weight — verified for every exponent). **Half-lives-half-dies**: the restriction `H¹(M)→H¹(∂M)` has
half-dimensional (Lagrangian) image, `dim = 1 = dim H¹(M)`, so it is **injective** — every deformation is detected
on the cusp. Cusp (eigenvalue / cusp-shape) deformations are explicitly realizable, hence integrate.

> The `{4,8}` directions integrate because they **are** cusp deformations (`dim H¹ = #cusps`), with (A) the
> explicit confirmation in the foundational `SL(2)` block.

## Net effect, and honest scope
B265's integrability is now anchored by (A) an explicit vanishing cup product **plus** (B) the
`dim H¹ = #cusps` boundary-deformation mechanism — no longer a bare citation. **Honest scope:** (A) computes the
obstruction in the `SL(2)`/exponent-1 block; the higher blocks integrate by the cusp mechanism (B) — which is the
*actual reason* the MFP smoothness theorem holds — rather than by 78-dimensional `e₆` cup products computed
block-by-block. This closes the Phase-3 audit item.

Anchors: B264 (`dim H¹(Sym^{2m})=1=#cusps`), B265 (Zariski-density; the integrability that was cited),
B267 (the exponents). Lit: Goldman (symplectic/obstruction theory of character varieties); Thurston (deformation,
smoothness); Menal-Ferrer–Porti (twisted cohomology, `dim H¹=#cusps`); half-lives-half-dies (Poincaré–Lefschetz).
