# B184 — the symmetry / gauge door: a gauge group is not forced; interaction breaks inflation, proliferates duality

**Date:** 2026-06-22. **Status:** the fourth hunt of the search specification (`../speculations/S036`) — the
**SYMMETRY / GAUGE** door: *does the interaction of multiple units force a symmetry (a gauge group), or is the
gauge content free input?* We **computed** it (per the standing directive: we calculate; NEEDS-SPECIALIST only when
exhausted). **Result: a gauge group is NOT forced — the same shape as every reachable door.** What *is* forced is
**per-unit**: each metallic unit carries (i) the modular **SL(2,ℤ)** duality on its character variety (`B150`/L14 —
a *real* symmetry, but a **duality / S-duality**, not the SM gauge group) and (ii) a **self-similarity / inflation**
symmetry (multiplication by `λ_m`). The **interaction** does the *opposite* of forcing a new gauge symmetry: of
distinct-field units it **breaks** the global inflation symmetry, and it only **multiplies** the per-unit dualities —
a product that **proliferates** with `N` (mirrors `B182`), not a selected Lie/gauge group. **Firewall-side**: emergent
quasicrystal / character-variety symmetry math (`K010` boundary); no scale/Λ; **nothing to `../../CLAIMS.md`**;
P1–P16 frozen. Ledger V178. Reproducer `symmetry_gauge.py` (`ALL CHECKS PASS`).

## The diagnostic and the result

A "gauge group is forced" would mean the collective's symmetry **selects** a specific group. The sharpest computable
symmetry of a metallic unit is its **inflation (renormalization) self-similarity** — and what the interaction does to
it is decisive.

- **C1 — each unit has a FORCED inflation symmetry.** Multiplication by `λ_m` is a **module automorphism** of the
  unit's gap-label module `ℤ + ℤα_m`: `λ·1 = m + α` and `λ·α = 1`, so in the basis `(1, α)` it is the metallic
  **companion** `[[m,1],[1,0]] ∈ GL(2,ℤ)` (det `−1`). This is the substitution / self-similarity symmetry of the
  metallic quasicrystal — a genuine forced symmetry of the *single* unit (verified exact for `m=1,2,3`).
- **C2 — interaction of DISTINCT units BREAKS the inflation symmetry.** The woven rank-3 module `ℤ+ℤα₁+ℤα₂` of two
  distinct-*field* units admits **no** nontrivial dilation automorphism: a single real inflation `×μ` would need
  `μ·α₁` in the module, but the **cross-product `α₁α₂` escapes** `span_ℚ{1,α₁,α₂}` (PSLQ → rank 4). So no single
  `λ` maps the woven structure to itself. **Control (field, not count):** same-field units `m=1, m=4` (both
  `ℚ(√5)`) keep `α₁α₄ ∈ span{1,α₁}` (`α₁α₄ = 2 − 3α₁`, exact) — a shared-field inflation **survives**. It is
  distinct-*field* interaction that breaks self-similarity (the same field-not-count mechanism as `B182`).
- **C3 — what survives PROLIFERATES, it does not select a gauge group.** The number of independent inflation
  directions = the number of **distinct fields** (distinct `λ_m` are multiplicatively independent: PSLQ on
  `{log λ₁, log λ₂}` → no relation), so the inflation symmetry **grows** with `N`; together with the per-unit
  SL(2,ℤ) dualities ⋊ permutations of same-field units it is a **product that grows** — not a single selected
  Lie/gauge group (mirrors `B182`'s rank `1+N`).
- **C4 — FIREWALL / the gauge verdict.** A gauge group is **not forced** by the collective. The forced symmetries
  are per-unit (modular SL(2,ℤ) duality, `B150` — real but a *duality*, not the SM gauge group; + companion
  inflation, real self-similarity); the interaction **breaks** the global inflation [C2] and only **multiplies**
  the duality [C3] (free input, proliferation). Symmetry here is **mathematics** (a duality / an automorphism), not
  **gauge-content selection** (MB9/MB10); nothing to `../../CLAIMS.md`.

## What this means for the search (S036)

The **SYMMETRY / GAUGE** ingredient stays **free input** — now *computed*, not asserted. The collective's forced
symmetry is per-unit (duality + inflation); the interaction of distinct units **breaks** the global self-similarity
and only **proliferates** the duality (a growing product, not a selected group). The genuine symmetry content
(SL(2,ℤ) = S-duality, `B150`/L14) is real, but it is a **duality**, not the SM gauge group; and `B150`/L15 already
showed the gauge group (SU(2)/N=2\*) is free input. So this door joins the pattern: every reachable door **relocates
the wall** — scale external (`B181`), selection proliferates not unique (`B182`), arrow externally-sourced &
scale-free (`B183`), and now **gauge not selected; interaction breaks inflation, proliferates duality** (`B184`).
A new, unifying structural fact across `B182`/`B184`: the **same distinct-field / cross-product-escape mechanism**
that grows the gap-label rank (`B182`) is what **breaks** the collective's inflation symmetry — proliferation and
symmetry-breaking are two faces of one arithmetic fact (distinct fields ⟹ cross-products escape the module).

## Scope / honesty
- Tests whether the collective **forces** a symmetry / gauge group, via the inflation-symmetry and duality-product
  structure (clean algebra + PSLQ). It does **not** claim to enumerate *all* symmetries of every gluing; it shows
  the two natural forced symmetries (duality, inflation) and what interaction does to them.
- "SL(2,ℤ) is a duality not a gauge group" is `B150`/L14's verdict, reused here; no new gauge claim.
- Emergent quasicrystal / character-variety symmetry mathematics (`K010` boundary); no physical-magnitude or
  gauge-content claim; nothing to `../../CLAIMS.md`; P1–P16 untouched.

## Anchors
`../speculations/S036` (the search register — the SYMMETRY/GAUGE ingredient this addresses), `B150`/L14–L15 (the
SL(2,ℤ) = N=2\* S-duality MCG action is real but a duality; the gauge group is free input — the firewall), `B182`
(the distinct-field / cross-product-escape mechanism — here it breaks inflation, there it grows the rank),
`B179`/`B180` (the metallic numbers / the do-not-conflate boundary; `λ_m` the one root), `B181`–`B183` (the prior
hunts — scale/selection/arrow), `K010` (the boundary). External: substitution / inflation self-similarity of
metallic quasicrystals (the companion matrix `[[m,1],[1,0]]`); units of `ℤ[λ_m]` / the metallic mean; gauge group
as free input vs forced (MB9/MB10).

## Reproduction
`python frontier/B184_symmetry_gauge_door/symmetry_gauge.py` — C1 each unit's forced inflation (companion
`[[m,1],[1,0]]`); C2 interaction of distinct fields breaks it (cross-product escapes; same-field control survives);
C3 the surviving symmetry proliferates (distinct `λ` multiplicatively independent); C4 the firewall/gauge verdict.
Prints `ALL CHECKS PASS`. Fast locks in `tests/test_b184_symmetry_gauge_door.py` (4 tests, ~0.2s).
