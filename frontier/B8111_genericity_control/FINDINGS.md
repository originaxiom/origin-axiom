# B8111 — the genericity control BITES, but on **2 of 5 tones** — and my sealed prediction was wrong

**Date:** 2026-08-21 · **Seat:** cc3, audit · **Lane:** MATHEMATICS.
**Gate 5 untouched: no measured value appears anywhere in this arc, and no literature was read.**
**Preregistered and sealed before compute:** `PREREGISTRATION.md`, SHA-256
`f272c0065249da306e2df510ad67d5d1273cacd57aa84828a9ff1e8aa006f4f0` (9416 bytes), algorithm named in
`SEAL.txt`, digest over the prereg's bytes and **not** self-referential.

**Commissioned by cc on the owner's D-2 ruling; Phase-0 item 0 of my own 2026-08-12 list.**

> **SCOPE.** The three exceptional binary polyhedral groups **in their defining `SU(2)`
> representation**, and the metallic substitutions `a → aᵐb, b → a` for `m = 1,2,3`. This arc tests
> the **discriminating power of my own crossing proposal**. It says **nothing** about any manifold,
> **nothing** about any measured spectrum, and **nothing** about whether the tones are observables
> — that is item 2 and it remains open and untouched.

---

## The sealed prediction, and how it failed

**I predicted OUTCOME B** — that `2O` would carry a **five**-tone menu structurally identical to the
golden one, with `√2` in place of `φ`, making *"lands on a five-tone menu"* generic.

**`2O` carries a FOUR-tone menu.** The shape is not generic. **OUTCOME A**, by the sealed criterion.
I record this plainly: the arc was designed so it could embarrass its author, and it did.

## The menus, computed from group closure — no character table typed in

| group | McKay | element orders | **tone menu** `|χ|/2 = |Re q|` | size |
|---|---|---|---|---|
| **2T** | E₆ | 1,2,3,4,6 | `{0, ½, 1}` — **entirely rational** | 3 |
| **2O** | E₇ | 1,2,3,4,6,**8** | `{0, ½, **√2/2**, 1}` — the **silver** signature | 4 |
| **2I** | E₈ | 1,2,3,4,**5**,6,**10** | `{0, **1/(2φ)**, ½, **φ/2**, 1}` — the five tones | **5** |

Controls that make this a representation statement and not an abstract-group one: every element is a
**unit** quaternion, the tone is `Re(q)` of that unit quaternion, and each group has **exactly one**
involution — the very property whose failure retired `SL(2,ℤ/4) ≅ 2O` in B997's 2026-08-15
correction. A **second, independent route** re-reads every tone from the **element order** alone
(`Re q = cos(2πj/n)`) and agrees exactly.

## ⚠ The part that matters more than the verdict: **three of the five tones discriminate nothing**

> **`{0, ½, 1}` is shared by ALL THREE groups.** Only **`φ/2` and `1/(2φ)`** are golden-unique —
> **a discriminating fraction of 2/5.**

**So the control both passes and bites.** The *menu as a whole* is golden-specific; **any prediction
landing on an individual tone from `{0, ½, 1}` is worthless**, because `2T`, `2O` and `2I` all
supply it. **That is 60% of the menu, and my 2026-08-12 proposal did not distinguish the two
cases.** The repair is forced and precise: **a tone-level crossing must be stated on `φ/2` or
`1/(2φ)`, never on the menu's membership alone.**

**The resolution requirement, fixed before it was known (§2.6 of the seal):** the closest distinct
golden/silver pair is `φ/2 = 0.809016994375` against `√2/2 = 0.707106781187`, so

> **any experiment resolving worse than `0.101910213188` cannot tell the two menus apart at all.**

## Bronze has **no partner** — and that is a proof, not a search

`√13` would be needed for the bronze mean `(3+√13)/2`. Every tone is `cos(2πj/n)` for `n` an element
order, and the orders present across all three groups are `{1,2,3,4,5,6,8,10}` — **13 occurs
nowhere**. Independently: if `√13` lay in the tone field `ℚ(√2,√5)`, then `ℚ(√13)` would be one of
its exactly three quadratic subfields `ℚ(√2), ℚ(√5), ℚ(√10)`; since `ℚ(√a) = ℚ(√b)` iff `ab` is a
square, this needs one of `26, 65, 130` to be a perfect square. **None is.**

**Consequence for the control's own design:** item 3 asked for *"a matched non-golden substitution
(silver, bronze)"*. **Silver has a matched group; bronze does not.** The control can be run against
silver and **cannot** be run against bronze at the group level. That asymmetry was not anticipated
in the 2026-08-12 text and is registered here.

## And the hazard is CONFIRMED on the other route: **κ is generic across the metallic family**

The trace map of `σ_m : a → aᵐb, b → a` is computed symbolically in `ℤ[x,y,z]` via Cayley–Hamilton
(`Aᵐ = p_m(x)A − p_{m−1}(x)I`), giving `x' = p_m z − p_{m−1} y`, `y' = x`, `z' = p_{m+1} z − p_m y`
— which at `m = 1` is exactly B518's `T = (z, x, xz−y)`. The Fricke invariant
`I = x²+y²+z²−xyz−4` is preserved **exactly and symbolically for `m = 1, 2, 3`.**

> **So B518's *"substitution-universal"* now has a computed extension along a NEW axis — the
> metallic index — and the two halves of this arc cut in opposite directions:**
> **`κ` is provably generic across golden, silver and bronze, so a κ-based crossing discriminates
> NOTHING. The tones are not generic. S034's N5 hazard is CONFIRMED for `κ` and REFUTED for the
> tone menu.**

That split is what the 2026-08-12 document asserted in prose. It is now computed.

## What this arc does NOT establish

- **That a silver-substitution spectrum would produce `2O`'s menu.** I matched a non-golden
  **group**; the substitution↔group linkage for silver runs through order-8 elements, **not**
  through B997's conductor route (`SL(2,ℤ/8)` is not a McKay group). **The substitution-level
  matching is a separate, unrun step.**
- **That the tones are observables.** Item 2, untouched. The addendum moved items 1 and 3; item 2
  is exactly where it was.

## Artifacts

`PREREGISTRATION.md` · `SEAL.txt` · `genericity_control.py` · `results.json` ·
`tests/test_b8111_genericity_control.py`
