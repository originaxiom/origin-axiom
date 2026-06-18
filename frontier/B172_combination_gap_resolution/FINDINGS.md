# B172 — the combination gap, resolved (Phase 1): interaction *does* generate a rank-3 gap, label ~(3,−3)

**Date:** 2026-06-18. **Status:** **Phase 1** of the multi-seed-interaction plan
(`~/.claude/plans/multi-seed-heterogeneous-quasicrystal.md`), the L16 spectral lane. Answers the question B171
opened — *does heterogeneous interaction generate a genuine rank-3 combination gap?* — **affirmatively, hedged**: the
woven metallic quasicrystal has a real, persistent spectral gap whose IDS is **not any single-frequency
(inherited-ladder) value**, so it requires **both** frequencies — a **combination gap present in neither pure chain**
(interaction-born). Its label is **consistent with the lowest-sum combination (3,−3)** to finite-size precision; a
**sharp many-digit certification is method-limited → NEEDS-SPECIALIST**. **Firewall-side**: emergent quasicrystal
math (`K007`/`K010` boundary), **NOT fundamental**; no scale/Λ; **nothing to `../../CLAIMS.md`**; P1–P16 frozen.
Ledger V166. Reproducer `combination_gap.py` (`ALL CHECKS PASS`).

## C1 — the 0.611 gap is a genuine combination gap (interaction-born)

The IDS on a true spectral gap is a fixed element of the gap-label module (gap-labeling theorem); the right
certification is its **value**, computed via the exact Sturm/negative-pivot count `count_below(E*)/N` (O(N),
validated against the dense solver). For the gap-center energy `E* = 2.389`:

| N | IDS | \|IDS−(3,−3)\| | dist to nearest single-freq label | in gap |
|---|---|---|---|---|
| 4 000 | 0.6110000 | 4.6e-4 | 4.2e-3 | ✓ |
| 8 000 | 0.6112500 | 2.1e-4 | 4.0e-3 | ✓ |
| 16 000 | 0.6111875 | 2.7e-4 | 4.0e-3 | ✓ |
| 32 000 | 0.6110313 | 4.3e-4 | 4.2e-3 | ✓ |
| 64 000 | 0.6112500 | 2.1e-4 | 4.0e-3 | ✓ |
| 128 000 | 0.6115000 | 3.9e-5 | 3.7e-3 | ✓ |

- **A real, persistent gap:** `E*` stays inside a spectral gap (no states in `[E*−0.02, E*+0.02]`) at every N up to
  128 000 (8× the reference) — energy width 0.114.
- **It is a combination gap, not an inherited ladder:** at every N the IDS (≈0.6114) is **≥8× closer (often far
  more) to the combination label (3,−3)=0.6114613 than to the nearest single-frequency label of any order** — the
  nearest single-freq value is the high-order silver (0,−13)=0.615 (≈3.8e-3 away); the prominent golden (1,0)=0.618
  ladder is 6.6e-3 away. Since 0.6114 is **not** any `(n,0)`/`(0,n)` value, the gap **requires both frequencies** —
  **absent from either pure chain** (interaction-born). This is the clean part of the answer: *interaction generates a
  spectral gap no single seed has.*
- **Honest limit:** the IDS does **not** sharpen below the finite-size floor (~2e-4) and the fixed-reference count
  drifts off the gap past N ~ 1e5. So the **specific** label is **consistent with (3,−3)** (the lowest-sum match) but
  a **sharp** certification (ruling out higher-sum module neighbours; θ-averaged / gap-edge-tracked IDS) is
  **method-limited → NEEDS-SPECIALIST**.

## C2 — seed-robustness (golden+silver, golden+bronze, silver+bronze, N=24 000)

- **Bilingual inheritance is seed-robust:** all three pairs carry both pure rank-2 `±1` ladders. The "spectrum speaks
  both languages" result (B171/B2) holds across the metallic family, not just golden+silver.
- **Genuine small-label combination gaps are essentially absent:** scanning the credible small-label window (sum ≤ 3,
  both coefficients nonzero, low null), only **one** non-robust hit appeared — golden+bronze `(1,−2)@0.013` (w 0.07),
  present in *neither* of the other two pairs. So the combination structure does **not** live at small labels at this
  resolution/coupling; it lives at **larger labels** (e.g. the (3,−3) gap of C1), each individually certifiable only
  by value/convergence, not by the single-N null (the density trap).

## Verify-don't-trust record

The probe's **first draft asserted "clean IDS-convergence to (3,−3)"** — and its own run **refuted** it (the residual
plateaus at ~2e-4, the fixed reference drifts at N=2e5). The checks were left to FAIL and the claim was **rewritten to
what the data supports**: a *combination gap* (certified: not a single-frequency value) with a label *consistent with*
(3,−3) (not sharply certified). This is the third self-correction in the multi-seed arc (after B171's two), and it
runs in the **opposite** direction from B171's — there the danger was under-claiming a real gap ("density artifact");
here it was over-claiming a sharp label. The honest middle: real combination gap, soft label.

## Scope / honesty (what this is NOT)

- It does **not** prove the gap's label is *exactly* (3,−3) (higher-sum module neighbours are not ruled out), and it
  does **not** give an all-orders or rigorous statement — those are NEEDS-SPECIALIST.
- "Combination gap" = a spectral gap whose IDS is not a single-frequency label (hence needs both seeds). That much is
  robust across N=4000–128000. The rank-3-ness of the gap-label *group* (vs the one gap) is the L16 conjecture, still
  open beyond this witness.
- Emergent quasicrystal spectral theory only (`K010` boundary). No scale, Λ, mass, or constant; the S035 link is a
  one-way `[LEAP]` hook, value-matching forbidden.

## Firewall
Emergent / condensed-matter mathematics on the metallic Schrödinger cocycle; no physical-magnitude claim; **nothing to
`../../CLAIMS.md`**; P1–P16 untouched.

## Anchors
`B171`/V165 (Phase 0: the bilingual baseline + the density trap + the (3,−3) candidate this resolves), OPEN_LEADS
**L16** (the gap-labeling-rank conjecture), `K007`/`K010` (the metallic Schrödinger cocycle — the object),
`../../speculations/S035` (the one-way interaction-born-structure hook). External: gap-labeling theorem (Bellissard;
Johnson–Moser); Forrest–Hunton–Kellendonk (coupled tiling cohomology).

## Reproduction
`python frontier/B172_combination_gap_resolution/combination_gap.py` — C1 the Sturm-count IDS sweep on the 0.611 gap
(combination-gap certification + the NEEDS-SPECIALIST limit); C2 the 3-pair seed-robust scan. Prints `ALL CHECKS PASS`.
