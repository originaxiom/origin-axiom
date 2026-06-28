# B256 — the metallic Arnold trinity: E₇ is the silver bundle's discriminant field

**Status: banked observation (frontier). FIREWALLED — arithmetic / McKay (Arnold trinity), NOT physics. Nothing to
`CLAIMS.md`.** The headline lead from the 2026-06-28 deep-dive hunt. `metallic_arnold_trinity.py` (pyenv).

## The question the hunt sharpened
"Where is E₇?" The program repeatedly found E₇ *absent* — excluded from the figure-eight's orbifold trinity by
Niven (**B249**) and absent as any π₁-quotient `2O` across golden/silver/bronze (**B237**). But this conflated two
arithmetic levels.

## The result
The monodromy `φ = RᵐLᵐ` has trace `t=m²+2` and discriminant `t²−4 = m²(m²+4)`, so its eigenvalue/**discriminant
field** is `ℚ(√(m²+4))`. Its McKay-exceptional values:

| m | discriminant field | McKay | Arnold |
|---|---|---|---|
| 1 (golden) | `ℚ(√5)` | 2I | **E₈** |
| 2 (silver) | `ℚ(√2)` | 2O | **E₇** |
| 3 (bronze) | `ℚ(√13)` | — | — |
| 4 | `ℚ(√5)` | 2I | E₈ |

Together with the figure-eight's **imaginary trace field** `ℚ(√−3) → 2T → E₆`, the metallic family's arithmetic
realizes **all three Arnold-trinity groups**:

> **E₆** = figure-eight trace field `ℚ(√−3)` (hyperbolic end, 2T) · **E₈** = figure-eight discriminant `ℚ(√5)`
> (spherical end, 2I, cover `L(5,2)`) · **E₇** = **silver discriminant `ℚ(√2)`** (2O) — the missing third.

## Reconciliation (contradicts nothing banked; removes an apparent asymmetry)
- **B237** found silver has **no `2O` π₁-quotient** (`GQuotients=0`) — correct. *But golden has no `2I` π₁-quotient
  either* (B237: golden `2I:0`); golden's **E₈ is the discriminant/homological McKay, not a π₁-quotient.** So
  silver's E₇ sits at *exactly the same level* as golden's E₈. Neither E₇ nor E₈ is ever a π₁-quotient; both are
  discriminant-field McKay. B237's phrasing ("golden E₈ banked" vs "silver `ℚ(√2)` = field-only coincidence") is
  thereby made consistent — they are the same kind of object.
- **B249** (Niven) excludes E₇ from the figure-eight's *orbifold* trinity (`√2` is never a rational `2cos(π/n)`).
- **B251**: silver is **not a knot complement** → no orbifold, no double-branched-cover lens space.

⟹ **E₇ is arithmetically present (silver discriminant) but geometrically homeless.** Unlike golden's E₆ (hyperbolic
orbifold) and E₈ (spherical orbifold / lens cover `L(5,2)`), E₇ has *no* cone-manifold or covering realization. The
Arnold trinity is **arithmetically complete** across the metallic family but **geometrically partial** — only
golden's E₆/E₈ are realized as geometries. This is the precise, unified form of "E₇ is special-by-absence": it is
the one Arnold group that appears only in the discriminant arithmetic, never in the geometry or the fundamental
group.

## Why this is signal (not numerology)
- It is **object-specific and forced**: the discriminant field is `ℚ(√(m²+4))`, an exact invariant of the
  monodromy; `m=1,2` are *forced* to `√5, √2` (the E₈, E₇ fields), with `m=3+` falling off the McKay locus.
- It **unifies three prior results** (B237 π₁-absence, B249 Niven-exclusion, B251 not-a-knot) into one statement.
- It answers a standing program question (H14/"where is E₇", the E₈+E₆−E₇ selection) at the arithmetic level: E₇
  is not subtracted, it is *relocated* to silver — and it is the unique Arnold group with no geometric home.

## Open follow-ups (from the hunt)
- Does silver's `ℚ(√2)`/E₇ have *any* realization beyond the discriminant field — e.g. in the Seifert-dual
  cone structure (B227/B229) or a higher-rank flat connection? (B251 says no *knot*-type realization.)
- The **Euclidean transition point** (n=3, the ℤ/3 orbifold) of the figure-eight is the geometric companion still
  uncomputed (its volume is 0; its other invariants and the "three"-structure are open).

Anchors: B210 (dual McKay E₆+E₈), B237 (silver no-2O π₁-quotient; the geometric-vs-homological McKay distinction),
B248/B249 (the transition; Niven E₇-exclusion), B250 (the lens cover), B251 (silver not a knot), S023 (metallic
gap-label fields `ℚ(√5),ℚ(√2),ℚ(√13)`). Lit: McKay correspondence; Arnold's trinity; binary polyhedral character
fields.
