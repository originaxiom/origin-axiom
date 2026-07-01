# B332 — the two arithmetic ends are the *product* and the *ratio* of the founding substitution's two letters

**Status: banked (frontier). Verify-don't-trust on the Chat-1 handoff (2026-07-01). Firewalled; nothing to
`CLAIMS.md`.** Chat-1 found a genuinely clean identity connecting the founding axiom to the commensurator, wrapped in an
inverted interpretation and two dead hooks. This probe banks the **verified** identity with the **corrected**
interpretation, and explicitly quarantines what did not check out.

## The verified identity (the real find)
The substitution `σ` builds two letters `R = [[1,1],[0,1]]`, `L = [[1,0],[1,1]]` (generators of `SL(2,ℤ)`). Exactly:
- **`g = −R·L⁻¹`** — the commensurator's order-3 element `g = [[0,−1],[1,−1]]` (the generation ℤ/3, B324/B326) **is the
  signed ratio** of the two letters.
- **`g⁻¹·a = −L`** (`a = R`).

And the two **simplest length-2 combinations** of the letters land on the **two arithmetic ends** of the whole program:

| combination | matrix | trace | disc | field | end |
|---|---|---|---|---|---|
| **product `R·L`** | `[[2,1],[1,1]]` | 3 | **5** | `ℚ(√5)` | golden → 2I → **E₈** (monodromy/ambient) |
| **ratio `−R·L⁻¹ = g`** | `[[0,−1],[1,−1]]` | −1 | **−3** | `ℚ(√−3)` | Eisenstein → 2T → **E₆** (gauge + generations) |

So **the two-ended object is the product and the ratio of `σ`'s own two letters** — a clean tie from the axiom (Level 0)
to the banked two-ended structure ([[two-ended-unification-and-wall-map]], B248) and the four levels (K020). The E₆ end
(the ratio `g`, `√−3`) internally carries *both* the gauge center ℤ/3 (Level 3) and the commensurator generation ℤ/3
(Level 4) — both Eisenstein.

## Correction (verify-don't-trust on Chat-1)
- **The labeling was inverted.** Chat-1 wrote "product `LR` → `ℚ(√−3)` → E₆ (gauge), ratio → generations." But the
  product has **disc 5** (`ℚ(√5)` → **E₈**, the golden/monodromy end), and the ratio `g` has **disc −3** (`ℚ(√−3)` →
  **E₆**). So *product = √5/E₈; ratio = √−3/E₆*. The E₆/gauge lives on the **ratio** side, alongside the generations.
- **The founding-chain conflation is wrong.** "golden ratio → `ℚ(√−3)` → `ω`" jumps between two *distinct* fields — the
  golden ratio is in `ℚ(√5)`, `ω` in `ℚ(√−3)`. They **coexist** in `Δ = x²−3x+1` (disc 5 / mod-4 → `Φ₃`, B326) but
  neither *produces* the other; they are two independent arithmetic inputs (the two ends).

## Not banked (honest quarantine)
- **Overlap index `[Γ : Γ∩gΓg⁻¹] = 3`** — *reported, not verified.* Here `g·a·g⁻¹ = L⁻¹` (a real `SL(2,ℤ)` element, not
  obviously in `⟨a,b⟩`), so `g` **commensurates** Γ (it is not a normalizer) and a finite index >1 is plausible — but
  `= 3`, and the identification with B326's 3-fold cyclic cover, need the actual Bianchi-group computation. Left for a
  dedicated probe; **not** asserted.
- **The `1/4` volume-suppression pattern** — **DEAD** (Chat-1's own null test: `1/5`, `1/e`, `1/φ` fit the SM ratios
  comparably; a single-number match survives no null test — MB8).
- **`16 = 4 + h(E₆)`** — a dead hook: internally inconsistent (`4+12` vs `(#orbits)² = 4² = 16` are different splits),
  and it fed the dead suppression.

## The firewall (held)
An exact algebraic fact about the axiom's two letters; it forces *structure* (which end, which group), no value. The
hierarchy stays Level 4 (B326/B331). Nothing to `CLAIMS.md`.

## The fence
Exact `SL(2,ℤ)` matrix algebra + charpoly discriminants (sympy). No physics values. Nothing to `CLAIMS.md`.

`two_letters_two_ends.py` (pyenv) · `tests/test_b332_two_letters_two_ends.py`. Related: **B324/B326** (the ω-circulant,
the congruence torsion), **B331** (the elliptic generation element), **B248** (the two ends), **K020** (four levels),
**S046** (value-at-the-seam). Lit: `SL(2,ℤ) = ⟨R,L⟩` is standard; the product/ratio → two-ends reading is the object's
own.
