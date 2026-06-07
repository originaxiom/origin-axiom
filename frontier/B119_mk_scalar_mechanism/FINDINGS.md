# B119 — the Mᵏ-scalar (centrality) mechanism across components: a sharp negative on "prove `k=n`"

**Chat-2 Path 3 (the hard path; be brave).** B111 ADDITION 1 — the one surviving exponent lead — showed the cusp
eigenvalue arithmetic *controls* the degree=rank exponent: on the SL(4) secondary `M⁴=ζ⁴=−1` is **scalar**, so
`[A,B]=c·(−1)Id` is a **central** (trivial) commutator ⇒ `k=4` is algebraically impossible, `k=3=n−1` forced. This
probe extends the Mᵏ-centrality arithmetic to all `n` and the three component types, attempts the brave `k=n` proof
on the principal — and reports a **sharp negative** with the obstruction stated precisely, plus an emergent
correction to the cusp-order reading (B111 ADD2). No physics; nothing to `CLAIMS.md`; the `ρ_n` proof stays the
prize; P1–P16 untouched.

## Reframe (B117)

The **bulk** `char(Mⁿ)` is no longer a "promotion" to be explained — it is **`Sym^n` presence** (`μ_n=1`, B117). So
this is the **peripheral** `k=n` on the Dehn-filling component: the one open shot at a *positive* power-half
mechanism. **It does not close.**

## The arithmetic (pure eigenvalue, no walled tower)

The forced principal cusp spectrum (B95) is eigenvalue `1` at multiplicity `n−2` plus `{a, 1/a}` with
`a + 1/a = 3 − n`. The order of `a` (`2cos = 3−n`):

| n | a+1/a | order(a) |
|---|-------|----------|
| 3 | 0 | **4** |
| 4 | −1 | **3** |
| 5 | −2 | **2** |
| ≥6 | ≤−3 | **∞** (hyperbolic, not a root of unity) |

**`Mᵏ` is central on the principal iff `order(a) | k`.**

## The brave `k=n` attempt — and why it does NOT close

- **Where the principal exists (n=3,4):** the longitude `L=[A,B]` of an irreducible rep is **non-central**, so
  `Mᵏ` must be non-central ⇒ `k` is not a multiple of `order(a)`. That excludes `k∈{order(a),2·order(a),…}` (e.g.
  n=4 excludes `k=3,6`) but does **not** single out `k=n` — many `k` qualify (n=4: `k=1,2,4,5` all non-central). So
  centrality arithmetic is **necessary but not sufficient**; `k=n` is pinned by the **proved A-polynomial**
  `L=(−1)^{n−1}Mⁿ` (B83), not by scalar-ness. **The "scalar-ness + bundle relations" route is subsumed by B83**,
  not an independent proof.
- **For n≥5 there is nothing to prove:** the principal Dehn-filling rep does **not exist irreducibly** (B95 — at
  n=5 the forced spectrum `{1,1,1,−1,−1}` has `A²=I` → dihedral → reducible; at n≥6 no finite-order spectrum of the
  forced shape). So **"exponent = rank on the principal" is an `n ∈ {3,4}` phenomenon** (B95); the brave `k=n`
  proof **cannot be completed**.

> **Verdict (sharp negative).** `k=n` on the principal is **not forced by Mᵏ centrality**; where the object exists
> the A-poly (B83) pins it, and for `n≥5` the object does not exist. The positive peripheral power-half mechanism
> does not close — a first-class negative, the obstruction stated as sharply as B108's order-2-vs-4.

## The secondary (2n-type) — extends B111 to the type arithmetic

On the SL(4) secondary (odd 8th roots, order `2n=8`): `Mᵏ` central iff `n | k`, so `Mⁿ = −I` is **central** ⇒
`k=n` gives a central commutator ⇒ the observed **non-central** longitude is `M^{n−1}` ⇒ **exponent `n−1`**. This
generalizes B111's secondary result as the `2n`-type arithmetic (valid where the secondary exists: `n=4` computed;
`n=3` is W2).

## Emergent (chased inline) — a correction to B111 ADD2

The cusp order on the degree=rank **principal** is `order(a)` with `a+1/a=3−n`, i.e. the sequence
**`{4, 3, 2, ∞}`** for `n=3,4,5,≥6` — **not** a clean `{n−1, n+1, 2n}` law. B111 ADD2's reading conflated three
**different** components: the `n=3` W1 (order 4 = `n+1`), the `n=4` principal (order 3 = `n−1`), the `n=4`
secondary (order 8 = `2n`). There is **no single all-n cusp-order law**; the orders are the multiplicative orders
of each component's primitive cusp eigenvalue, and Mᵏ centrality is governed by exactly those orders
(`Mᵏ` central iff `order(a)|k` on the principal). This sharpens (does not overturn) B111 ADD2's `{n−1,n+1,2n}`
observation: those three values are real, but they belong to three components, not one law.

**Ledger:** V106. **Reuses:** `B95.forced_principal_spectrum` / `B95.n5_principal_is_reducible`,
`B111._CUSP_SPECTRA`.
