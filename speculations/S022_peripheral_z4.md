# S022 — the peripheral ℤ/4 for degree=rank's `c` (the successor to the closed θ→c route)

**Status: `ACTIVE (lead) — LOW-RANK n∈{3,4}`.** A conjecture/lead, **not** a result or an asserted route.
Firewalled; not a claim. The successor to S012 (`θ→c`, TESTED-NEGATIVE, B108).

> **⚠ SCOPE (B120/V107 — the degree=rank split).** This lead lives entirely on the **(II) geometric** side of
> degree=rank — longitude=meridianⁿ and the scalar `c` at the *irreducible Dehn-filling* rep — which exists only for
> **`n∈{3,4}`** (B119/B95: the forced principal `a+1/a=3−n` is a root of unity with order `{4,3,2,∞}`; absent
> irreducibly for `n≥5`). The **(I) spectral** statement (`char(Mⁿ)` is a tower factor ⟺ `μ_n=1`) is all-`n` and
> already settled (`Sym^n` presence, B117) — it is *not* what this lead is about. So the peripheral `ℤ/4` for `c`
> is a **low-rank** question, not a route to the all-`n` prize (which is the Sym two-sequence `μ_d`, B103).

**Why this lead exists (the B108 negative was constructive).** B108 proved the order-4 ingredient degree=rank's
`c` needs is **not** in the bulk opposition involution `θ=−w₀` (an involution, order 2, cannot produce the
order-4 secondary `c=i`). So the missing `ℤ/4` must live in the **peripheral / cusp-spectrum** data. Two banked
results point at it: **B95** (the forced cusp spectrum has `a=i`, order 4, at `n=3`) and **B76** (the cusp `k`-set
*is* the `SU(2)_k` quantum-group root-of-unity level set, `2cos(π/k)`).

**The B111 evidence the cusp arithmetic is the right place.** ADDITION 1 (B111) **proved** that the cusp
eigenvalue arithmetic *controls the exponent*: on the SL(4) secondary `M⁴ = ζ⁴ = −1` is **scalar** ⇒ `k=4` is
algebraically impossible ⇒ `k=3` forced. So the cusp spectrum is demonstrably where the degree=rank exponent (and,
plausibly, its scalar `c`) is decided.

**The constraints (what the ℤ/4 must explain).** A peripheral predictor must explain not just `c=i` (order 4) but
**why `Mⁿ` is the specific power that appears**. *Reframed (B117/V104):* the **bulk** `char(Mⁿ)` is no longer a
"promotion" — it is **`Sym^n` presence** (`μ_n=1` ∀n in the Sym two-sequence; the "promotion"/"two-halves" framing
is tombstoned). So the open peripheral question narrows to the **Dehn-filling `k=n`** (the exponent on the cusp
component) and the scalar `c` — *not* a bulk power-half. The cusp orders are **`{n−1, n+1, 2n}`** on the three
component types (B111 ADD2). Tested negatives so it does not soften:
- `k = ord−1` — **TESTED-NEGATIVE** (OK at SL3, FAIL at SL4 principal & secondary; B111 ADD2).
- `s_n = c` — **DEAD** (sign is order ≤2, can't reach order-4 `c=i`; `TOMBSTONES.md`).

**The candidate positive mechanism — DOWNGRADED (B114).** The **Weyl-orbit covering degree** of `(cusp
parameter) ↦ L = c·Mᵏ` was `k`-to-1 at the *single-eigenvalue* level (B111). But **B114 tested the full spectrum
and it is NOT `k`**: the full covering degree (meridian spectra, `det=1`, mod Weyl) is `~k^{n−1}` (SL3 W1 = 9, SL4
secondary = 27, principal = 40). So **the covering-degree-=-`k` mechanism is TESTED-NEGATIVE** — the exponent is
*not* a covering degree. The live exponent lead is instead the **`Mᵏ`-scalar arithmetic** (B111 ADDITION 1: `k` =
the smallest power where `Mᵏ` is non-scalar *and* bundle-compatible; the `M⁴=−1` impossibility forces `k=3` on the
secondary). The peripheral `ℤ/4` for the *scalar `c`* (not the exponent) stays the open lead.

**[HOOK] (the mandatory hinge, same discipline as B108).** Any proposed peripheral predictor must hit **all four**
`c = {1, 1, −1, i}`, not three — the secondary `c=i` is the whole test (a ℤ/2-flavoured predictor fails by
construction). Concrete first step: at the Dehn-filling reps compute the peripheral holonomy / cusp-shape and test
whether `c` is organized by the cusp `ℤ/4` (B76 level), the way the bulk parity was organized by `θ`.

**Status discipline.** This is the *right direction* (the cusp arithmetic is proven relevant by B111); the
*specific formula is open*. Do **not** let it soften into an asserted route. When derived, it leaves this folder
for a `B`/`V` number and supplies the degree=rank/peripheral half of the `ρ_n` prize (`TWO_SYMMETRY_FRAME.md`).

Related: `S012` (the bulk θ→c, TESTED-NEGATIVE), `TWO_SYMMETRY_FRAME.md`, `../frontier/B111_sign_structure/`,
`../frontier/B95_degree_rank_mechanism/`, `../frontier/B76_cusp_quantum_group/`, `../frontier/B117_interleaving/`
(the bulk `char(Mⁿ)` = `Sym^n` presence; the "promotion" tombstoned).
