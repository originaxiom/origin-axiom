# B179 — the metallic "numbers" unified: one object, several views (+ the do-not-conflate boundary)

**Date:** 2026-06-19. **Status:** the clean "understand-completely" consolidation (#3 of the menu) — pure symbolic
algebra, no resolution issues. Shows that the whole geometric/arithmetic tower of a metallic seed is **one algebraic
object** (the metallic mean `λ_m`), and draws the **honest boundary**: which same-named parameters are *distinct* and
must not be conflated. **Firewall-side**: pure arithmetic of the object; no scale/Λ; **nothing to `../../CLAIMS.md`**;
P1–P16 frozen. Ledger V173. Reproducer `metallic_unified.py` (`ALL CHECKS PASS`).

## One object: `λ_m`, the root of `x² − m x − 1 = 0`

Every geometric/arithmetic "number" we carry for a metallic seed `m` is an **exact function of the single algebraic
number** `λ_m = (m+√(m²+4))/2` (the metallic mean) — verified symbolically over `ℚ(m)`:

| our "number" | = (exact, in `λ_m`) | identity |
|---|---|---|
| gap-label frequency (Sturmian slope, B175) | `α_m = 1/λ_m = λ_m − m` | `λ_m·α_m = 1` |
| seed matrix `M_m=[[m,1],[1,0]]` | eigenvalues `{λ_m, −α_m}` | trace `m`, det `−1` |
| bundle monodromy `M_m²` (trace `m²+2`) | `m²+2 = λ_m² + α_m²` | det 1 |
| dynamical degree (Cantat–Loray, B169) | `λ_m²` | the larger `M_m²` eigenvalue |
| trace field | `ℚ(√(m²+4))` | `disc(x²−mx−1) = m²+4 = (λ_m+α_m)²` |
| Hurwitz constant (worst-approx, B176) | `1/√(m²+4) = 1/(λ_m+α_m)` | `√(m²+4) = λ_m+α_m` |
| Dickson/Sym tower eigenvalues | `±λ_m^k` | (golden `±φᵏ`) |

The key bridge identities: `λ_m + α_m = √(m²+4)` and `λ_m − α_m = m` — so the **discriminant root** (hence the field,
the Hurwitz constant, the bundle trace) is literally the **sum of the two reciprocal frequencies** `λ_m + 1/λ_m`, and
the **seed integer** `m` is their **difference**. Golden/silver/bronze: `λ = φ, 1+√2, (3+√13)/2`; trace `M²` =
`3, 6, 11`; Hurwitz `1/√5, 1/√8, 1/√13`.

## The honest boundary (MB12: what is NOT `λ_m`)

The unification is of the **geometric/arithmetic core**. Three *related-but-distinct* parameters share the names
"λ"/"κ" and must **not** be conflated with `λ_m` — conflating them would manufacture a false identity (the
"right object, wrong level" trap):
1. **The Schrödinger coupling `λ`** (B175/B178 — the potential strength `V=λcos(…)`) is a **free external parameter**,
   set by us, not derived from `m`. (It is the knob in the width law `width ∝ λ^{order}`.)
2. **The Fricke modular parameter `λ̃`** in `κ = tr[A,B] = λ̃ + 1/λ̃` (B148) is a **character-variety coordinate**
   that **varies** along the A-polynomial curve (`κ` is *free*, K013) — not the fixed `λ_m`.
3. **The gap-labeling IDS** `n₁α₁ + n₂α₂ mod 1` is a **derived combination** of the (inverse) metallic frequencies,
   living mod 1 — not a single "number."

So the map is: a **clean unification** of the seed's intrinsic arithmetic (all `= f(λ_m)`), **fenced** from the
external/coordinate/combination parameters that merely share a symbol.

## Why this completes understanding

It answers "how do all our tower-numbers fit together?" exactly: they are **one** number's shadows. The figure-eight's
`φ`, the silver `1+√2`, the gap frequencies, the trace fields, the dynamical degrees, the Hurwitz/irrationality
constants, the Dickson tower eigenvalues — **all of it is `λ_m`**, the root of `x²−mx−1`. And it draws the line that
keeps the picture honest: the Schrödinger coupling, the Fricke `κ`-modulus, and the IDS are *separate* objects. No new
claim; pure algebra of what we already have.

## Firewall
Pure arithmetic/algebra of the metallic object; no physical-magnitude claim; **nothing to `../../CLAIMS.md`**;
P1–P16 untouched.

## Anchors
`K002` (the metallic family / continued fractions), `K003` (the Dickson tower `±λ_m^k`), `K008` (`tower(n;trace,det)`),
`B169` (the dynamical degree `λ_m²`), `B175` (the gap-label frequency / the Schrödinger coupling — the distinct λ),
`B176` (the Hurwitz constant `1/√(m²+4)`), `B148` (`κ = λ̃+1/λ̃` — the distinct Fricke modulus), `K013` (`κ` free),
`K019` (the collective-spectrum synthesis). External: theory of metallic means / quadratic irrationals; Lagrange
spectrum (`√(m²+4)` for `[m;m,…]`).

## Reproduction
`python frontier/B179_metallic_numbers_unified/metallic_unified.py` — U1 the exact symbolic identities (all = `f(λ_m)`)
+ the golden/silver/bronze numeric table; U2 the do-not-conflate boundary; U3 the golden specialization. Prints
`ALL CHECKS PASS`.
