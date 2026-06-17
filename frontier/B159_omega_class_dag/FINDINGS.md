# B159 — the Ω strict-full class-graded DAG (L4–L10), independently verified

**Date:** 2026-06-17. **Status:** the cross-session "Gate-2 class DAG export" (the charpoly-class–graded
transition graph of the Ω strict-full cone, depths L4–L10) is **independently verified** — both internally
(full L4–L10 conservation/structure) and by **from-scratch re-enumeration** (L4–L7 reproduced class-by-class
and edge-by-edge with our own counter, which never touched the export pipeline). It confirms and sharpens
B156/B158 at the **class level**: the whole cone grows from the single seed **Ω₄ = B155**, every one of the
**474 classes is reciprocal** (TC-2 holds across the entire enumeration, not just the `R_{a,m}` family), and
the metallic bundle-monodromy spectra (figure-eight, silver, **and now bronze**) appear as reciprocal
factors. Standalone character-variety / arithmetic combinatorics; **no Origin-core claim, no physics**;
proven core P1–P16 untouched. Nothing promotes to `../../CLAIMS.md`. Ledger V153. Reproducer
`verify_gate2_dag.py`.

**Provenance.** Cross-session handoff (`audit/omega_gate2/`, gitignored): a `gate2_class_DAG_export` bundle
(nodes CSV, edges CSV, a 1.16 MB transition-DAG JSON). De-risks, does not certify — every count below was
re-derived under our own governance before banking. Source artifact SHA256
`13953d3503a790da5e87c58884fb21b8cc1d3502bea1ea18a6fc46c9354121ff` (full JSON retained in `audit/`; the small
node/edge CSVs are banked here).

## The object

Take the Ω strict-full survivor tower (B156): start from the L4 seed (strongly-connected length-4 positive
row-shear histories whose 4×4 matrix is full-metric, charpoly `(4,5,4)`), extend by the 12 unit row-shears,
keep full-metric endpoints. **Grade each level by charpoly class** `abc = [a, mid, a]` (charpoly
`x⁴ − a x³ + mid x² − a x + 1`; note `mid = 2a − 2m − 4`, so each class is an Ω lattice point `(a,m)`). The
DAG nodes are (level, class); edges are class→class transitions weighted by history-extension multiplicity.

| L | histories | matrices | **classes** |
|---:|---:|---:|---:|
| 4 | 96 | 36 | 1 |
| 5 | 672 | 240 | 2 |
| 6 | 3840 | 960 | 6 |
| 7 | 20928 | 3240 | 18 |
| 8 | 105312 | 9396 | 49 |
| 9 | 521904 | 25536 | 115 |
| 10 | 2488080 | 65472 | 283 |

(History totals match B156's re-derived counts, incl. the L10 = 2 488 080 run; the **matrix** and **class**
columns are the new graded structure.)

## What was verified (verify-don't-trust)

**PART 1 — full L4–L10, from the class CSVs (exact):**
- level counts (classes / histories / matrices) all match the table above; **[exact]**
- **every class charpoly is palindromic** — TC-2 (strict-full ⟹ reciprocal) confirmed across **all 474
  classes**, an empirical re-confirmation independent of the `R_{a,m}` proof; **[exact]**
- the **L4 seed class** `(4,5,4)` has charpoly `(x²−3x+1)(x²−x+1)` = **Ω₄ = B155** (golden×phase) — the
  entire cone descends from the one canonical object; **[exact]**
- **conservation:** for every level, the incoming edge history-mass per class equals that class's
  `history_count`; per transition, retained mass = target mass and candidate mass = source × 12 (the 12
  shears); **[exact]**
- **metallic spectral image (B158):** the bundle-monodromy traces `T_M = M²+2` appear as reciprocal factors —
  `T₁=3` (figure-eight) in 9 classes incl. the seed, `T₂=6` (silver) in 12 classes, **`T₃=11` (bronze) at L10**
  (class `(12,13,12) = (x²−11x+1)(x²−x+1)`); `T₄=18`+ absent in this depth range. **[exact]**

**PART 2 — from-scratch re-enumeration, L4–L7 (exact):** our own counter (`frontier/B156`
`independent_recount.py`, exact `det`-based full-metric test, no shortcut, never touched the export) rebuilt
the class DAG and reproduced the class counts (1, 2, 6, 18), **per-class** `(history_count,
distinct_matrix_count)`, **and** every edge's history-multiplicity (2, 9, 36 edges) — **exact match**. Since
the class decomposition is thus a faithful charpoly-partition of the survivor set whose totals (through
L10) were already independently re-derived in B156, the L8–L10 class structure rests on verified ground.

## Reading (firewalled)

This is the **class-graded internal structure** of the Ω strict-full cone — a sharper picture of the
"abelianized spectral image" of B158: the cone is one tree rooted at B155, reciprocal at every node, carrying
the metallic monodromy spectra as factors. The export's own claim-boundary is honest and we preserve it
verbatim: *"This is a class-level graded DAG export, not a causal-set/manifold verdict … Gate-2
Myrheim–Meyer/fatness analysis must be run separately."* The **Myrheim–Meyer dimension / "fatness"**
(causal-set manifoldlikeness) reading is the **path-to-physics hook and is firewalled** — signature (1,3) =
algebraic inertia, NOT spacetime; a graded DAG is not a causal set without a declared, justified poset
relation. **No such relation is asserted here; no physics; nothing to `CLAIMS.md`.**

## Anchors
B155 (golden×phase seed = Ω₄), B156 (the strict-full cone + the L4–L10 counts + `independent_recount.py`),
B158 (the spectral-image relation `(p−2)(q−2)=−2(m+1)`). Ledger V153.

## Reproduction
`python frontier/B159_omega_class_dag/verify_gate2_dag.py` — PART 1 (full L4–L10 from the banked CSVs) +
PART 2 (re-enumerate L4–L7 from scratch, compare). Prints `ALL CHECKS PASS`.
