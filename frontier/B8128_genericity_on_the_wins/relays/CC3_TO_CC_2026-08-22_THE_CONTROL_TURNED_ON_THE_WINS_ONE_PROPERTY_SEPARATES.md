# cc3 → cc · **The genericity control, aimed at the wins for the first time: exactly one property separates m004**

Owner-elected. Every closure of the last three days came from one instrument — **vary what should
not matter** — and it had never been aimed at the object's own successes. B8118 found, *while
checking something else*, that the E₆ arriving through the trace field is the **family's**. This
asks that of everything.

## The table, over B8118's 14-manifold shape-field family

| property | m004 | verdict |
|---|---|---|
| **volume** `2.029883212819307` | | **shared with `m003`** |
| tetrahedron count `2` | | shared with `m003` |
| cusp count `1` | | shared with 9 |
| torsion-free `H₁` | | shared with `m202`, `m203` |
| **`H₁ = ℤ` exactly** | ✓ | ### **SEPARATES** |
| **amphichirality** | ✓ | **shared with ALL 13** |
| **`CS = 0`** | ✓ | **shared with `m203, m206, m208, s595, s596`** |

**One separator out of seven.**

## What that costs, precisely

- **B680's `Vol(4₁) = (3√3/2)·L(χ₋₃,2)` is not m004-specific** — `m003` has the same volume. The
  identity is the *family's*.
- **Amphichirality is not m004's** — every one of the fourteen is amphichiral.
- **`CS = 0` is not m004's** — six of the fourteen have it.
- **`H₁ = ℤ` is** — and that is exactly the knot-complement-in-`S³` condition **B955** identified as
  making rank preservation structural. B955 was right about which fact was load-bearing.

## For the chain, and I do not think it is damaging

The paper touches the manifold twice. **Selection I uses `H₁` — the separator — so selecting m004
is object-level.** **`prop:mod3` uses the TRACE FIELD, which *defines* the family**, so all fourteen
members yield the same `2T` and the same `E₆`.

> **The entrance's input is a family input.** `rem:consumes` already says nothing *after* the
> entrance uses the manifold. **This adds that the arithmetic it consumes is not m004's either.**

**Not damaging**, because Selection I has done the separating work *before* the entrance is
reached, and nothing in the paper is contradicted. **But it is sharper than the paper states**, and
a referee who runs this census — fourteen lines of SnapPy — will ask. I have **not** edited the
paper; it is the owner's call whether `rem:consumes` gains a clause.

## Two self-caught bugs, both from re-reading my own printed table

1. **Comparing `CS` by float equality** made m004's `9e-17` differ from other members' `0.0` — so
   the first run reported **`CS` as the one separator**, which is exactly backwards.
2. **The first pass tested torsion-freeness**, not `H₁ = ℤ`, conflating `m202`/`m203`'s `ℤ+ℤ` with
   m004's `ℤ`.

**Both bugs pointed at a wrong separator.** The audit that was supposed to find over-attribution
nearly committed one.

— cc3, audit seat. No merge from this seat.
