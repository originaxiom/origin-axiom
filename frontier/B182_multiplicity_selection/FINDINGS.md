# B182 — the selection / multiplicity door: superposition proliferates, it does not select-to-unique

**Date:** 2026-06-19. **Status:** the second hunt of the search specification (`../speculations/S036`) — the
**SELECTION / multiplicity** door, the direct answer to *"2 / more / set / infinity of units — what does the
interaction give?"* for the **superposition (weaving) channel**. **Result: superposition PROLIFERATES** — weaving
`N` distinct-field metallic units gives a gap-label module of **rank `1+N`** (→ ∞ as `N→∞`); it does **not** converge
to a unique selection. Selection-to-unique is a **constraint** (gluing) phenomenon, not a superposition one — and that
side is multi-cusp **NEEDS-SPECIALIST**. **Firewall-side**: pure arithmetic of the gap-label module (`K010` boundary);
no scale/Λ; **nothing to `../../CLAIMS.md`**; P1–P16 frozen. Ledger V176. Reproducer `multiplicity_selection.py`
(`ALL CHECKS PASS`). Pure PSLQ/algebra — none of the saturation/contamination issues of the spectral-width work.

## The multiplicity scan

| N units (distinct fields) | gap-label module | rank |
|---|---|---|
| 1 (golden) | `ℤ + ℤα₁` | 2 |
| 2 (+silver) | `ℤ + ℤα₁ + ℤα₂` | 3 |
| 3 (+bronze) | `… + ℤα₃` | 4 |
| 4 (+ m=5) | `… + ℤα₅` | 5 |

- **C1 [rank grows with distinct-field multiplicity].** PSLQ (dps 50, maxcoeff 1e6): `{1, α₁, …, α_N}` are
  **ℚ-independent** for the distinct-field units `m=1,2,3,5` (fields `ℚ(√5),ℚ(√2),ℚ(√13),ℚ(√29)`) ⟹ module rank
  `= 1+N`, for `N=2,3,4`. Each distinct unit adds a frequency-layer.
- **C2 [proliferation, not selection-to-unique].** `rank = 1+N` strictly **increases** with `N` (→ ∞): superposition
  **enriches** the structure-menu without bound — the *opposite* of converging to a unique (rank-1) selection.
- **C3 [field, not count].** Same-*field* units add **no** rank: `m=1` & `m=4` (both `ℚ(√5)`) are **ℚ-dependent**
  (`−1 + 2α₁ − α₄ = 0`, exact). So it is the number of **distinct fields** that proliferates, not the unit count
  (refines L16 / `B179`).

## The fence (so SELECTION isn't over-read)

The register's **SELECTION** ingredient asks for a *unique / specially-structured* forced choice. This finding shows
**superposition does not provide it** — it proliferates. Selection-to-unique is a **constraint** phenomenon:
- *constraint* (gluing): two A-poly curves meet in a **finite** κ-fork (continuum → finite, `K014`/`B174`); iterating
  it (many constraints) is **over-determined** → a special/empty set — the genuine selection-to-unique route, but the
  once-cusp topology makes literal large-N gluing **multi-cusp NEEDS-SPECIALIST**;
- *superposition* (weaving): adds frequencies → **richer** module (rank ↑) — enrichment, not selection.

And the proliferating structure stays **dimensionless** (gap-labels live in `[0,1]`) and **scale-free** (the object is
permanently critical, `B181`). So the honest answer to **"infinity of units"** (in the superposition channel):
**infinitely rich structure (rank → ∞), still scale-free and dimensionless** — the SELECTION ingredient (uniqueness)
remains open, and only on the **constraint** side.

## Scope / honesty
- Tests the **superposition** channel of selection (clean, PSLQ). The **constraint** channel (iterated gluing →
  selection-to-unique) is the multi-cusp generalization, **NEEDS-SPECIALIST** (H5-a).
- "Rank `1+N`" is the gap-label *module* (the menu of possible labels); *which* labels open actual gaps is
  potential-dependent and high-order-saturation-limited (`B175`/`B178`) — not re-litigated here.
- Pure arithmetic of the object; nothing to `../../CLAIMS.md`; P1–P16 untouched.

## Anchors
`../speculations/S036` (the search register — the SELECTION ingredient this addresses), `B179` (the metallic numbers
unified; the `−1+2α₁−α₄=0` same-field relation), `B173`/L16 (the rank `= 1+#distinct fields` formula), `K013`/`K014`
(single = continuum / distinct = structure), `B174` (the cusp-gluing κ-fork — the constraint side), `B181` (scale-free
by criticality — the proliferating structure carries no scale). External: theory of metallic means / quadratic fields;
gap-labeling (the frequency module).

## Reproduction
`python frontier/B182_multiplicity_selection/multiplicity_selection.py` — C1 the rank-`1+N` multiplicity scan (PSLQ);
C2 proliferation; C3 field-not-count (same-field dependent); C4 the fence + verdict. Prints `ALL CHECKS PASS`.
