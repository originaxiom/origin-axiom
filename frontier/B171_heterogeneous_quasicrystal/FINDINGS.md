# B171 — the heterogeneous metallic quasicrystal (Phase 0): baseline, density-trap null, cross-session verification

**Date:** 2026-06-18. **Status:** **Phase 0** of the multi-seed-interaction plan (`~/.claude/plans/multi-seed-heterogeneous-quasicrystal.md`),
the **substitution / gap-labeling lane** (OPEN_LEADS **L16**) — the *spectral* face of the κ↔spectrum bridge (`K010`),
chosen over the cusp-gluing/κ lane (H5) per owner direction. This establishes the **baseline + the density-trap null**
and **verifies a cross-session claim** before it shapes the plan. **Firewall-side**: emergent quasicrystal /
condensed-matter math (`K007`/`K010` boundary), **NOT fundamental**; no scale/Λ; **nothing to `../../CLAIMS.md`**;
P1–P16 frozen. Ledger V165. Reproducer `het_quasicrystal.py` (`ALL CHECKS PASS`).

## The object

A discrete Schrödinger operator `(Hψ)_n = ψ_{n+1}+ψ_{n−1}+V_n ψ_n` with a **metallic Sturmian** potential
`V_n = λ·χ_{[1−α,1)}(nα+θ mod 1)` (the Fibonacci-Hamiltonian construction, `K007`/`K010`), frequency `α = 1/λ_m`
(`λ_m` the metallic mean: golden `α_g = 1/φ = 0.618…`, silver `α_s = √2−1 = 0.414…`, bronze `α_b = 0.303…`). By the
**gap-labeling theorem** (Bellissard; Johnson–Moser), the integrated density of states (IDS) takes values on spectral
gaps in the **frequency module**: a single metallic chain → the **rank-2** module `ℤ+ℤα`. **Weaving** two distinct
chains, `V_n = λ_g·χ(…α_g…) + λ_s·χ(…α_s…)`, gives a two-frequency potential whose labels live in the **rank-3**
module `ℤ + ℤα_g + ℤα_s` (golden ∈ ℚ(√5), silver ∈ ℚ(√2), ℚ-independent). The **question** (L16): does a *genuine,
small-label* **combination gap** `n₁α_g+n₂α_s` (both nonzero) open above the density floor — interaction-born
spectral structure no single seed has?

## Phase-0 results (N = 8000, λ = 1.5)

- **B1 [control].** Single golden / single silver chains: every prominent gap matches a **single-frequency** label
  `(n,0)` resp. `(0,n)` (within finite-size tol ~1e-3) — the pure **rank-2 ladders**, as the theorem requires.
- **B2 [num] — bilingual.** The woven chain **inherits both pure ladders**: the golden `±1` gaps (IDS 0.382, 0.618,
  widths 0.31, 0.14) **and** the silver `±1` gaps (IDS 0.414, 0.586, widths 0.13, 0.30) all survive intact. The
  spectrum "speaks both languages." This is the **credible** part of the cross-session result — but note it is close
  to what gap-labeling *predicts* (each sub-chain's own frequency is in the combined module).
- **B3 [null] — the density trap, quantified.** The rank-3 label set is **dense**: the chance a random IDS lands
  within 1e-3 of *some* label rises with the label-sum — **1.0 % (≤1) → 2.9 % (≤2) → 5.8 % (≤3) → 9.6 % (≤4) →
  20.3 % (≤6)**; the min label spacing collapses past sum ~4. **So a large-label match is not evidence;** the credible
  window is **small labels (sum ≤ 3, null < ~6 %)**.
- **B4 [verification] — the cross-session "first combination gap" 0.611.** A **real, wide** gap *does* sit at IDS
  **0.6112** (width **0.114**, comparable to the inherited `±1` ladders) — it is **not noise**, and it is **resolvably
  distinct** from the adjacent golden `(1,0)=0.618` ladder gap (≈0.007 away, several × the finite-size resolution
  ~1e-3 — the woven spectrum carries *both*). Its best module match is the **large** label **(3,−3)** (sum 6, value
  0.611461, err 2e-4), ~30× better than its nearest small label. By gap-labeling its true label is well-defined, but
  at this resolution it is **UNIDENTIFIED**: the (3,−3) assignment is
  **plausible** (err ~2e-4 ≈ O(1/N)) **but not statistically credible** (sum-6 null ~20 % ≫ a small-label gap's ~3 %).
  **Honest status: a real gap with an unverified label** — *not* a density artifact (the gap exists), and *not* an
  established combination gap (the label is uncertified). The cross-session headline over-read a plausible-but-uncertified
  large-label match as a result.

## Verdict (Phase 0)

The woven metallic spectrum is **bilingual** (both rank-2 ladders survive) [B2, credible]; the **density trap** is real
and quantified [B3]; the cross-session 0.611 gap is **real but its combination-label (3,−3) is unverified** [B4]. The
genuine question — *does heterogeneous interaction generate a real rank-3 combination gap?* — is **OPEN**, with two
concrete Phase-1 tests now defined: **(i)** track the 0.6112 gap's IDS as `N` grows — does it **converge** to
0.611457 (confirming (3,−3))?; **(ii)** hunt the **small-label** witnesses `(1,1) 0.032, (1,−1) 0.204, (2,1) 0.650,
(1,2) 0.447, (2,−1) 0.822, (1,−2) 0.790` (sum ≤ 3, low null), **seed-robustly** across ≥2 metallic pairs.

## Scope / honesty (what this is NOT)

- Phase 0 is a **baseline + a null calibration + a verification**, not the combination-gap result. It does **not**
  establish a rank-3 combination gap (that is Phase 1) and does **not** refute one (the 0.611 gap is real).
- The **verify-don't-trust correction was applied twice**: once to the cross-session claim (the (3,−3) label is
  uncertified), and once to *this probe's own first draft*, whose verdict called the gap a "density artifact" — an
  over-claim in the opposite direction, since the gap is real; corrected to "real gap, unverified label."
- Emergent quasicrystal spectral theory only (`K010` boundary). No scale, no Λ, no mass, no constant. Nothing supports
  a physics claim; the S035 connection (interaction-born structure) is a **one-way `[LEAP]` hook**, value-matching forbidden.

## Firewall

Emergent / condensed-matter mathematics on the metallic Schrödinger cocycle; no physical-magnitude claim; **nothing to
`../../CLAIMS.md`**; P1–P16 untouched.

## Anchors
`K007`/`K010` (the metallic Schrödinger cocycle / Fibonacci Hamiltonian / Cantor spectrum — the object), OPEN_LEADS
**L16** (the field-multiplicity gap-labeling-rank conjecture this tests; "distinct from B131/K014 cusp-gluing"),
`K013`/`K014` (the character-variety companion: single seed = continuum, distinct seeds = discrete — the κ face),
`../../speculations/S035` (the one-way interaction-born-structure hook). External: gap-labeling theorem (Bellissard;
Johnson–Moser); Forrest–Hunton–Kellendonk (coupled/product tiling cohomology); cut-and-project quasicrystals.

## Reproduction
`python frontier/B171_heterogeneous_quasicrystal/het_quasicrystal.py` — B1 single-chain controls; B2 the bilingual
woven spectrum; B3 the density-trap null (chance-hit vs label-sum); B4 the 0.611-gap verification. Prints `ALL CHECKS PASS`.
