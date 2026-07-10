# R1 — the divisor-indexed torsion field law (corrected), now a corollary of Cantat's method

**For:** a character-variety dynamicist (Cantat–Loray / Goldman / Markoff-dynamics). **Status:**
honest — the field law is verified exact and is now derived as a corollary; the remaining question
is a placement question about the completeness statement.

## Setup (self-contained)

Work on the SL(2,ℂ) relative character variety of the one-holed torus in Fricke coordinates
`x = tr A`, `y = tr B`, `z = tr AB`, with the boundary/commutator trace given by the Markoff cubic
`κ = x² + y² + z² − xyz − 2`. A mapping class of the one-holed torus acts on this surface by a
polynomial "trace map." For the metallic family (monodromy `RᵐLᵐ`, trace `m²+2` on homology; `m=1`
is the figure-eight) let `σ_m` be the finite-order mapping class acting by the involution `a ↔ b`.
On the cusp locus `κ = −2`, `σ_m` fixes certain torsion characters; internally this fixed-point
phenomenon is the "held-breath" law.

## The result — field statement CORRECTED (verified exact)

On `κ = −2`, the characters fixed by `σ_m` are exactly the order-`d` **torsion** characters for
divisors `d ≥ 3` of `m` with the order-`d` point non-degenerate (`2cos(2π/d) ≠ 0`, i.e. `d ≠ 4`);
the geometric (hyperbolic) character is never fixed. Writing `τ_d = 2cos(2π/d)`, the number field of
the order-`d` fixed character is

  `ℚ(τ_d, √( τ_d²(τ_d²−8) ))`,   of degree `2·[ℚ(τ_d):ℚ]` over ℚ.

The rational quantity `D_d = Norm_{ℚ(τ_d)/ℚ}( τ_d²(τ_d²−8) )` is a **norm/discriminant factor** of
that field, **not** in general its generator. Two rows carry corrections that must be respected
(the earlier drafts conflated a norm with the field, and are withdrawn):

- **d = 3:** `τ_3 = −1` is rational, the tower collapses, `D_3 = −7`, and the field **is** `ℚ(√−7)`
  (character minimal polynomial `z² − z + 2`).
- **d = 5 (CORRECTED):** the field is a **degree-4 extension of ℚ containing ℚ(√5)** — minimal
  polynomial `z⁴ − 3z³ + 7z² − 4z + 4`, field discriminant `5²·41`, Galois group `D₄` with unique
  quadratic subfield `ℚ(√5)`. `D_5 = Norm_{ℚ(√5)/ℚ}(Δ₅) = 41` appears only as a discriminant factor.
  It is **not** `ℚ(√41)` (that statement is withdrawn).
- **d = 7 (CORRECTED):** the field is a **degree-6 extension containing the cyclic cubic `ℚ(τ₇)`** —
  minimal polynomial `z⁶ − 5z⁵ + 16z⁴ − 25z³ + 30z² − 12z + 8`, irreducible over ℚ; Galois closure
  `C₂ ≀ C₃` (order 24); subfield degrees `[1, 3, 6]`, so **no quadratic subfield exists**.
  `D_7 = −239 = Norm(τ₇²(τ₇²−8))` is the norm of the discriminant, **not** a field generator. It is
  **not** `ℚ(√−239)` (that statement is withdrawn).
- Sample further rows: `d = 8` gives `ℚ(√−3)` (`τ₈² = 2`, eliminant `(z² − 2z + 4)²`); `d = 12`
  gives `ℚ(√−15)` (`(z² − 3z + 6)²`); `d = 11, 13` give irreducible fields of degree `φ(d)`.

## The result is now a COROLLARY (verified)

Cantat's (2009) fixed-locus pipeline — trace action → fixed locus → restrict `κ` → minimal
polynomial → field — transfers **verbatim** to the finite-order `σ_m` at `κ = −2` and yields the
full corrected law (divisor indexing, the `d ≠ 4` condition, the closed-form field), with **one**
supplement not in Cantat: an elementary Chebyshev transfer-matrix classification of the fixed locus,
at or below the difficulty of Cantat's own control computation. The control was reproduced exactly:
for the pseudo-Anosov `Ψ = [[2,1],[1,1]]` the fixed curve is `(x, x/(x−1), x)`, `κ` restricted is
`(x⁴ − 3x³ + x² + 4x − 2)/(x−1)²`, and the quartic `x⁴ − 3x³ + x² + 4x − 2` is irreducible over ℚ
and splits into two quadratics over **`ℚ(√17)`** (Galois `D₄`) — Cantat's own result. Notably this
control map **is** `T₁²`, i.e. `Ψ` is exactly the `m=1` metallic (figure-eight) monodromy `σ₁²`;
running the same pipeline at `κ = −2` instead of `κ = 0` returns `x² − 3x + 3` (discriminant `−3`,
the figure-eight trace field `ℚ(√−3)`).

**Completeness — proven for all `m`.** The fixed locus is
`Fix(T_m) = {(0,0,0)} ∪ {(2,2,2)} ∪ {(−2,−2,2) if 2|m} ∪ ⋃_{d|m, d≥3} {(τ_{d,k}, τ_{d,k}, z) : z ∈ ℂ}`.
The proof is an elementary transfer-matrix / eigenvalue-locus factorization (`2 − tr Mᵐ = −λ^{−m}(λᵐ−1)²`);
it is unconditional for all `m` (previously the statement was only Gröbner-verified for `m ≤ 16`;
now machine-checked to `m = 24` and cross-checked out-of-sample at `m = 17..20` as a belt).
Intersecting with `κ = −2` gives the cusp quadratic and the `d ≠ 4` collapse. Consequence: the
novelty of R1 narrows to a remark carried by a complete elementary proof rather than a computation.

## The single question (narrowed)

> Given that Cantat's fixed-curve method now yields the divisor-indexed field law as a corollary,
> is the **divisor-indexed completeness statement** — `Fix(T_m)` equal to the union of the order-`d`
> torsion lines over `d | m, d ≥ 3`, for *all* `m`, at `κ = −2` — genuinely new, or a
> known/immediate corollary documented somewhere in the later Cantat–Loray / Bowditch /
> Markoff-dynamics literature?

## Honest scope

This is a negative-existence verdict over the canonical references (Goldman 2003, Cantat 2009,
Biswas–Gupta–Mj–Whang 2022, Lisovyy–Tykhyy): the object, the modular action, and the
fixed-curve → field mechanism are all in the literature; no source we found states the divisor
indexing or the `τ²(τ²−8)` fields. Less-indexed literature (theses, proceedings, later preprints)
was not exhaustively mined. The result is posed for adjudication, not claimed as first.

**Provenance.** Rests on B479 (the law, as corrected 2026-07-09), B491 (the adversarial novelty
verdict and the corrected d=5 field), and B494 (the CL-1b duel: COROLLARY, the all-`m` completeness
proof, and the d=7 field/norm correction). Literature: Cantat, *Bers and Hénon, Painlevé and
Schrödinger*, Duke Math. J. 149 (2009); Goldman, *The modular group action on real SL(2)-characters
of a one-holed torus*, Geom. Topol. 7 (2003). Nothing promotes to `CLAIMS.md`.
