# B209 — the classical/quantum boundary: the tiling sees A₅, the spinorial E₈-completion is absent

**Date:** 2026-06-25. **Status:** the sharpest form of "where classical structure ends and quantum begins" —
the icosahedral tiling's exterior algebra `Λ*(ℝ⁶)` decomposes into exactly the **bosonic A₅ irreps**, and the
**4 spinorial irreps of the double cover `2I` — the ones that complete affine `E₈` — are absent.** Connects
B206 (A₅ vs 2I = the spin `ℤ/2`). Firewall-clean representation theory; **nothing to `CLAIMS.md`; P1–P16
untouched.** Ledger **V208**.

## The computation

The icosahedral quasicrystal lives in 6D (cut-and-project `ℤ⁶→ℝ³`); `A₅` (the icosahedral rotation group)
acts on `ℝ⁶ = 3 ⊕ 3'` (physical + perpendicular 3-spaces). The exterior algebra `Λ*(ℝ⁶)` (dim `2⁶=64`)
carries the tiling's topological invariants. Computed from characters (`χ_{Λ*}(g)=det(I+ρ₆(g))`):

| | result |
|---|---|
| `χ_{Λ*(ℝ⁶)}` on A₅ classes | `(64, 0, 4, 4, 4)` |
| decomposition | **every A₅ irrep (dims 1,3,3',4,5) at multiplicity exactly 4** → `4·16 = 64 = 2⁶` |
| spinorial `2I` irreps `{2,2',4',6}` (dims 2,2,4,6) | **ABSENT** |

`Λ*` of an honest A₅ representation (the center `−I` of `2I` acts trivially) contains **only** A₅ irreps. The
golden ratio in the A₅ character table (the two 3-dim irreps carry `φ` on the 5-cycles) **cancels** in every
multiplicity — the answer is the clean integer 4.

## What it means

`2I = A₅` (5 bosonic irreps, sum of dims² = 60) `⊔` `{spinorial}` (4 irreps, dims 2,2,4,6, sum of dims² = 60),
and the spinorial set is exactly the affine-`E₈` nodes beyond `A₅`. So:
- the **classical tiling** (its topological/K-theoretic invariants, built from `Λ*(ℝ⁶)`) sees **only `A₅`** —
  the bosonic half;
- the **4 spinorial irreps that complete `E₈`** are precisely what the classical structure **cannot** see;
  they require the **quantum/spin lift `2I`** (the `SL` level of B206, vs the classical `PSL=A₅` level).

This is the same `ℤ/2` as B206 (the spin double cover `SU(2)→SO(3)`, `SL(2,𝔽₅)→PSL(2,𝔽₅)`), now made concrete
as *which representations* are visible classically vs only quantumly: the boundary **is** those 4 spinorial
irreps.

## Firewall
Representation theory of `A₅`/`2I`. The "K-theory of the tiling" framing is a one-way hook — the actual K-groups
of a specific icosahedral tiling are a separate (known, involved) computation; here is the representation-
theoretic content. This is the McKay/representation-theoretic `E₈`, **not** physics' `E₈`. Nothing to `CLAIMS.md`.

## Reproduction
- `python lambda_decomposition.py` — `χ_{Λ*(ℝ⁶)}` from characters, the mult-4 decomposition, spinorial absence.
- `tests/test_b209_ktheory_classical_quantum_boundary.py` — 2 locks. 2 passed.
