# B120 — the trivial-point tower as a fully-determined object: it depends only on `(n; trace, det)`

Banks the Chat-2 exploration interlude (Q2/Q3) and the computed Supplement (S1–S5), **verify-don't-trust**. Three
of the handoff's stated formulas were wrong and are **corrected** here. The surviving picture: the `(n²−1)`-dim
trivial-point tower (the Sym two-sequence, B117/B103) is **one object** fixed by two inputs — the unfolding depth
`n` and the abelianization seed `(trace, det)` — and nothing else enters. No physics; nothing to `CLAIMS.md`; the
`ρ_n` / Sym-`μ_d` proof stays the prize; P1–P16 untouched.

## Q3 — the tower char poly is a function of `(n; trace, det)` only

Distinct integer matrices with **equal `(trace, det)`** give **identical towers**: `[[2,1],[1,0]]` vs `[[1,2],[1,1]]`
(both `(2,−1)`, distinct) yield the same tower at `n=3,4,5` (8/15/24 roots match). Forced: the tower is
`⊕Sym^d(M)^{μ_d}` and `Sym^d` eigenvalues are degree-`d` monomials in `M`'s eigenvalues, fixed by the char poly =
`(trace, det)`. These are the two ingredients of the MCG interaction-word: **twist-count → trace** (the seed `m`,
the expansion rate), **swap-count mod 2 → det** (orientation, the parity sector). So the tower factors cleanly as
`tower(n ; trace, det)`.

## S2 — m-universality of the Sym content (the deep lead; a reframing, not a closure)

The `n=4` tower's `char(±Mᵏ)` **multiplicities are identical for `m=1,2,3`** — only the eigenvalue *values* `φ_m`
change. The Sym content `μ_d` depends only on `(n, det=−1)`, not on `trace=m`. (This is B103's `ℚ[m]`-iso at `n=4`,
made explicit.)

**The "why" (the user's dig):** the tower is a `GL(2,ℤ)`-representation `ρ_n` (B103); the `μ_d` are its **plethysm /
branching multiplicities** under the principal `SL(2)`, which see only the abstract rep (`n`) and the parity
(`det`), never the trace. So `m`-universality is *forced* by `ρ_n` being a representation.

**Honest scope (do not overclaim):** this **reframes the prize as a plethysm** and is proved only at `n=3,4`
(B103's `ℚ[m]`-iso). It does **not** lower the trace-ring wall — proving `m`-universality for all `n` is the *same*
wall as the two-sequence itself. **A reduction/reframing, not a closure.**

## S1 — the doubling range `{2..n−3}` is forced (CORRECTED formula)

The extra dimensions from doubling `Sym²..Sym^{n−3}` **equal** the dimension deficit
`|(n+1)(n+2)/2 − (n²−1)| = (n−4)(n+1)/2` (verified `n=4..10`), and `{2..n−3}` is the unique contiguous-from-`Sym²`
range that fills it. So the two-sequence's doubling band is **derived** from B117's dimension identity, not just
observed. **Correction:** the handoff's `(n²−3n)/2` is **off by exactly 2**; the correct value is `(n−4)(n+1)/2`.

## S3 + S5 — the height-count closed form (CORRECTED)

Eigenvalue heights run **`0..n`** (the top, `Sym^n`'s extremes `φ^{±n}`, is height `n` — initially missed). With
the top included, the profile has a **clean closed form**:
```
   count(n,0) = n−1;   count(n,h) = 2(n−2)  for h ∈ {1,2};   2(n−h)  for 3 ≤ h ≤ n−1;   2  for h = n,
```
and `Σ_h count(n,h) = n²−1` (verified `n=2..8`). **Corrections:** the handoff's guess `2·max(1,n−h−1)` is wrong,
and its "no closed form" claim is wrong — a closed form does exist, once the `h=n` height is counted.

## Q2 — degree=rank SPLITS into two statements

The promotion framing had fused two different statements:
- **(I) SPECTRAL — all `n`.** `char(Mⁿ)` is a tower factor ⟺ `Sym^n` is present ⟺ `μ_n=1`. Since `Sym^n` is the top
  of the `[2≤d≤n]` band, `μ_n=1` for all `n≥2`. (= B117's `Sym^n`-presence, restated.) **Survives, all `n`.**
- **(II) GEOMETRIC — `n∈{3,4}` only.** longitude eigenvalue `= meridianⁿ` at an irreducible boundary-unipotent rep.
  The forced principal spectrum `a+1/a=3−n` (B95) is a root of unity with order `{4,3,2,∞}` for `n=3,4,5,≥6`; `n=5`
  is the degenerate edge (`a=−1`, `A²=I`), `n≥6` absent. Proved `n=3` (B71), `n=4` (B89).

So "exponent=rank is `n∈{3,4}`" (B119) and "char(Mⁿ) always a factor" (B117) are *both right* — they are the two
halves (II) and (I) of one split statement.

## S4 — the θ/Sym comparison is factor-level; B116 stands

B116's θ-split vs Sym comparison is at the **factor level** (`char(±M^h)` multiplicity), and it agrees through
`n=5` and **diverges at `n=6`**. The Chat-2 interlude's "divergence at `n=3`" was an **eigenvalue-vs-factor units
error** (θ counts degree-2 factors; Sym counts individual eigenvalues), not a repo discrepancy. B116's `n=6`
divergence point stands.

## Net

The tower is **one internally-generated object** fixed by `(n ; trace, det)`: `n` = Sym unfolding depth (B117),
`(trace, det)` = the MCG-word seed (twists→trace, swaps mod 2→det). The prize is **unchanged and un-fused** — prove
the Sym two-sequence `μ_d` for all `n` (B103) — now seen as a **plethysm** computation (S2).

**Ledger:** V107. **Reuses:** `B103.two_sequence_mult` / `B103._Jm_n4_exact`, `B95.forced_principal_spectrum`,
`B116.differ_by_single_promotion`.
