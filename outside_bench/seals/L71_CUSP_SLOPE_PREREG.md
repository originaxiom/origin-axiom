# SEAL — L71: what the θ-odd deformations do to the cusp

**Sealed before the certificate was written.** Object: `docs/OPEN_LEADS.md` **L71 — what
ARE the θ-odd deformations?** (★★★, OPEN), whose row says: *"The deformed reps are not
discrete faithful. Their geometric meaning (Dehn-surgery-adjacent? complex-projective
structures? quasi-Fuchsian-like family?) … NOTE: B270 banked 'deformations are cusp
deformations' — start there."*

## DISCLOSURE — prior knowledge held when this seal was written

**A scratch prototype was run before this seal and computed the statistic below at m = 1
and m = 2. Both returned exactly `−2√−3`.** Nothing beyond m = 2 was computed. The priors
declared below are stated **knowing those two values**; a seal that hid them would be worse
than one that names them.

## Why the question is sharp, and what makes it non-trivial

B270 banked that at the SL(2,ℂ) foundation *"deformations are cusp deformations."*
`P2W5-L72` computed `dim H¹(M; Sym^{2m}ρ_geo) = 1` for every E₆ exponent, with peripheral
`dim H¹(T²; Sym^{2m}) = 2`. And `P2W5-L72` also computed the wall: *"the θ-odd directions
m = [4, 8] are **NOT** in the image of the SL(2,ℂ) deformation (they lie in Sym^8 / Sym^16,
not the adjoint block)."*

So for m ≥ 2 the one deformation direction in each block is **not** induced from the
geometric SL(2,ℂ) deformation. **What it does to the cusp is then a genuine question, and
it has a number.**

## The instrument

Presentation and geometric rep as validated in `B581`/`P2W5-L72`, rebuilt here:
`⟨a, b | a W b⁻¹ W⁻¹⟩`, `W = b a⁻¹ b⁻¹ a`; `ρ(a) = [[1,1],[0,1]]`,
`ρ(b) = [[1,0],[u,1]]`, `u = ζ₆`, `u² = u − 1`. Longitude `λ = W·W̃` (W̃ = W reversed),
which commutes with `ρ(a)` and has exponent sum 0.

For each m: `V = Sym^{2m}`, `N := ρ_V(a) − I`. Since `ρ_V(a)` and `ρ_V(λ)` are unipotent
with the same image, `V / im N` is 1-dimensional. Take the generator `ξ` of
`H¹(M; V)` (Fox calculus on the relator, modulo coboundaries) and define

> **`slope_m := [ξ(λ)] / [ξ(a)]` in `V / im N ≅ ℂ`.**

## CELL 1 — the slopes

**Observed:** `slope_m`, exactly, for **m = 1 … 12** (the six E₆ exponents flagged among
them).

- **Outcome A:** every `slope_m` equals `−2√−3` exactly.
- **Outcome B:** at least one differs.

**Declared prior: A**, on the disclosed m = 1 and m = 2 evidence.

## CELL 2 — is that value forced by the cusp, or is it global?

If the cusp's own cocycle condition `(ρ(a)−I)ξ(λ) = (ρ(λ)−I)ξ(a)` already pinned the
ratio, CELL 1 would be a triviality about ℤ² and would say nothing about the knot.

**Observed:** for each m, whether there **exists** a pair `(ξ(a), ξ(λ))` satisfying that
cusp condition whose coker-classes have ratio **different** from `−2√−3`.

- **Outcome A:** such a pair exists for every m — the ratio is **not** forced by the cusp,
  so CELL 1's value is global information about M.
- **Outcome B:** no such pair exists for some m — for that m the ratio is a cusp
  triviality.

**No prior declared.**

## CELL 3 — does the statistic read the representation? (MB12 transversality)

**Observed:** the same `slope_m` computed with `u` replaced by its complex conjugate
`ū = 1 − u` (the other geometric rep).

- **Outcome A:** the conjugate value, `+2√−3`.
- **Outcome B:** anything else, including the same value.

**Outcome B with "the same value" would mean the statistic cannot distinguish two different
representations, and CELL 1 may not then be read** (memo 164).

## Controls

- **C1** — `ρ_{2m}(r) = I` exactly, every m computed.
- **C2** — `h⁰ = 0`, `h¹ = 1`, `dim ker(ρ_{2m}(a) − I) = 1` for the six E₆ exponents,
  matching `P2W5-L72`'s exact ℚ(ζ₆) table.
- **C3** — `ρ_{2m}(λ)` commutes with `ρ_{2m}(a)` exactly, and `ρ_V(λ) = exp(τ·log ρ_V(a))`
  with the same `τ` in every block.
- **C4** — SnapPy's cusp shape of `4₁`. Its printed value is `3.4641016151i = +2√3 i`;
  the statistic here is expected to agree **in magnitude** and may differ in sign, because
  SnapPy's meridian/longitude orientation is its own. **A sign difference is a convention
  difference and is to be reported as such, not as a discrepancy** — and a magnitude
  difference would be a failure.

## Interpretation is not preregistered

Per bench rule #21 the outcomes state only what is **observed**. What a block-independent
slope would mean for L71 is written in the memo, after.
