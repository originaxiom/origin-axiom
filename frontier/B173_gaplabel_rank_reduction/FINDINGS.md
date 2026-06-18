# B173 — the gap-labeling reduction (Phase 2): the rank-3 module is a theorem; L16 confirmed, the √(dᵢdⱼ) worry dispelled

**Date:** 2026-06-18. **Status:** **Phase 2** of the multi-seed-interaction plan
(`~/.claude/plans/multi-seed-heterogeneous-quasicrystal.md`), the L16 spectral lane — the **theorem-reduction**
step. Reduces B172's numerical combination gap to the **gap-labeling theorem** (a citable consequence, not a new
claim), **confirms the L16 rank formula**, and **dispels its one "possibly-false step."** Backed by two adversarial,
citation-checked research legs (the reduction; the novelty). **Firewall-side**: emergent quasicrystal math
(`K007`/`K010` boundary), **NOT fundamental**; no scale/Λ; **nothing to `../../CLAIMS.md`**; P1–P16 frozen. Ledger
V167. Reproducer `gaplabel_rank.py` (`ALL CHECKS PASS`).

## The reduction (KNOWN-THEOREM)

For the 1D operator `(Hψ)_n = ψ_{n+1}+ψ_{n−1}+V_n ψ_n` with a **superposition** potential
`V_n = f(α_g n+θ_g) + g(α_s n+θ_s)` (hull = T², a single ℤ-action by the vector rotation `(x,y)↦(x+α_g, y+α_s)`),
the **gap-labeling theorem** gives the IDS-on-gaps as the **frequency module**

> `gap-label group = ℤ + ℤα_g + ℤα_s` — **rank 3, product-free.**

This is a theorem, not our claim: Johnson–Moser 1982 (CMP 84, 403 — the rotation number/IDS lies in the integer
frequency module); Bellissard gap-labeling (K-theory of the hull crossed-product, IDS = trace image on `K₀`);
explicit modern form **Damanik–Fillman 2022** (arXiv:2203.03696, Thm 1.1 / Eq 1.10: `𝔄(T^d, R_α) = ℤ + αℤ^d`). So
B172's numerically-isolated combination gap at IDS ≈ 0.6114 is the **witnessed rank-3 element (3,−3)** of this module.

## What the probe locks (arithmetic backbone, PSLQ)

- **R1 [rank 3]:** `1, α_g=1/φ, α_s=√2−1` have **no integer relation** (PSLQ → None, maxcoeff 1e6) ⟹ the
  golden+silver frequency module is **rank 3**.
- **R2 [the full L16 formula, confirmed]:** golden ∈ ℚ(√5), silver ∈ ℚ(√2) are **distinct** fields ⟹ `1 + #distinct
  fields = 1 + 2 = 3` = the R1 rank. **Same-field control:** golden `m=1` and `m=4` are *both* ℚ(√5), and PSLQ finds
  the exact relation **`−1 + 2α₁ − α₄ = 0`** ⟹ rank stays **2** ("same field caps at 2"). The two together confirm
  the **whole** L16 formula `rank = 1 + #distinct quadratic fields`, not just one clause.
- **R3 [the √(dᵢdⱼ) worry dispelled]:** the product `α_g·α_s` is itself **ℚ-independent** of `{1,α_g,α_s}` (PSLQ →
  None) — so a product term, *if present*, would genuinely make the group **rank 4**. But the gap-labeling theorem
  says it is **absent** for a 1D single-shift operator: products (`α_g α_s` / area / `√(dᵢdⱼ)`) are a strict
  signature of **ℤ^d≥2 actions / 2D cut-and-project tilings** (first genuine product at d=4 in the NC-torus, Elliott
  1984; the area/Λ² class in 2D tilings, Forrest–Hunton–Kellendonk). So L16's "possibly-false step" (a coupling
  raising the rank above `1+k` via `√(dᵢdⱼ)`) is **misplaced for the 1D superposition** — that mechanism lives in
  2D, not here. Rank stays **3**.

## Novelty (adversarial, tiered)

- **The rank-3 / combination-gap MECHANISM is KNOWN** (Johnson–Moser 1982 / Bellissard) — *not* to be claimed.
- **The explicit construction APPEARS-NOVEL** as a worked example: a 1D *additive* superposition of two **distinct**
  metallic-mean Sturmian chains (golden+silver) with a combination gap numerically isolated does not appear in the
  literature (the metallic-mean quasicrystal literature is uniformly single-mean; bichromatic optical-lattice work
  frames the same potential via localization, not gap labeling). The dangerous near-miss **Damanik–Gorodetski
  "Square Fibonacci"** (arXiv:1601.01639) is a **different object** — separable, 2D, the Minkowski sum of two *same*
  golden spectra — *do not conflate*. Honest framing: **"first explicit construction/observation," not a new
  phenomenon** → NEEDS-SPECIALIST to confirm.

## Residual (NEEDS-SPECIALIST)

- **(a) Discontinuous sampling.** The clean rank-3 theorem is for **smooth** `f`. B171/B172 used the **Sturmian
  indicator** (discontinuous on T²); the *exact* group there may carry extra **additive** subshift-weight generators
  (Bellissard–Scoppola 1982; Damanik–Fillman subshift ring) — **still product-free**, but possibly larger than
  `ℤ+ℤα_g+ℤα_s`. The smooth-`f` reduction is the clean statement; the indicator case needs care.
- **(b) Module = menu, not realized gaps.** The frequency module is the *set of possible* labels; *which* labels open
  actual gaps (gap-filling / horseshoe) is the Damanik–Gorodetski-type question, still open off the real axis (B165).

## Scope / firewall

A literature/reduction finding (the computation is the arithmetic backbone; the reduction is cited). Emergent
quasicrystal spectral theory only (`K010` boundary). No scale, Λ, mass, or constant; the S035 link is a one-way
`[LEAP]` hook, value-matching forbidden. **Nothing to `../../CLAIMS.md`**; P1–P16 untouched.

## Anchors
`B171`/V165 (Phase 0 baseline + density trap), `B172`/V166 (Phase 1: the (3,−3) combination gap this reduces),
OPEN_LEADS **L16** (the rank conjecture this confirms), `K007`/`K010` (the object), `B165` (the realized-gaps /
off-axis open question), `../../speculations/S035` (the one-way hook). External: Johnson–Moser 1982 (CMP 84, 403);
Bellissard gap-labeling; Damanik–Fillman 2022 (arXiv:2203.03696); Elliott 1984 (NC-torus K-theory); Forrest–Hunton–
Kellendonk (2D tiling cohomology); Damanik–Gorodetski 2015 (arXiv:1601.01639, the near-miss); Bellissard–Scoppola 1982.

## Reproduction
`python frontier/B173_gaplabel_rank_reduction/gaplabel_rank.py` — R1 rank-3 (PSLQ); R2 the L16 formula
(distinct→3, same-field→2); R3 the product is a 4th direction (theorem-excluded); R4 the cited reduction + novelty +
residual. Prints `ALL CHECKS PASS`.
