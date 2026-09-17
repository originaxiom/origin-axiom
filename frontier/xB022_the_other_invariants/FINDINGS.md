# xB022 — THE OTHER INVARIANTS: the object is a fixed point of MORE than xB021 could see

**Date:** 2026-09-17 · **Seat:** `xb` · **Branch:** `sep16-branch` · **Verdict: PROVED**

**PREREGISTRATION sealed `f153f67dcb0a27e8…`, committed and pushed at `cbfeec0` BEFORE
`verification/` existed**, with the predicted stabiliser table written down in advance and a binding
kill condition on V6.

---

## THE RESULT FIRST

xB021 computed the stabiliser of the object's Chern–Simons value and held **`CS` only**, naming that
as its principal limitation. This arc removes the limitation, and the picture it finds is **simpler
than the one predicted, not more complicated**: the invariants do not spread across four behaviours.
**They split into exactly two species.**

| invariant | stabiliser (measured) | orbit of the object's value | species |
|---|---|---|---|
| **volume** | **all three bits** | **trivial — one value** | no orbit |
| **shape field** | **all three bits** (at the object) | **trivial — one value** | no orbit |
| **`CS`** | `{A6, A7}` | `{0, ¼}` — two values | has an orbit |
| **`H₁`** | `{A6, A7}` | two values | has an orbit |

**All four sealed predictions were confirmed** (V5: 4 of 4), and **V3 came in stronger than
predicted** — the seal asked for a *majority*, the measurement gave **494 of 494, 100 %**.

---

## THE CELLS

**V0 — the banked inputs, re-derived and not cited.** The 494-word corpus was **rebuilt from
xB015 K6's rule**, not copied from its file, and checked against the closed form
`Σ_{n=2..8}(2ⁿ − 2) = 494`. On that rebuilt corpus both banked laws reproduce:

- **A5 shifts `CS` by ¼: 494 of 494** (xB015 K6)
- **A7 negates `CS`: 494 of 494** (xB018 C5)

**V1 — volume.** `vol(b++w) = vol(b+-w)` at `10⁻²⁵` for **494 of 494** words.
**Positive control:** the same comparator reports `vol(m004) ≠ vol(m006)`, so a null result here is
not a blind instrument. **A5 is in volume's stabiliser.**

**V2 — A6 and A7, run rather than asserted (E69).** Over 240 words, the mirror and the letter swap
each preserve **volume 240/240** and **`H₁` 240/240**. This cell exists because an assertion sitting
beside a number that does not test it is this record's own error class.

**V3 — `H₁` under A5.** `H₁(b++w) ≠ H₁(b+-w)` for **494 of 494 words — 100 %**.
At the minimal word `H₁(m004) = ℤ` against `H₁(m003) = ℤ ⊕ ℤ/5`.
**`H₁` behaves like `CS`, not like volume.**

**V4 — the field.** SnapPy's `invariant_trace_field_gens` requires Sage, which is **not on this
bench**, so the instrument was **built here** on PARI's `algdep` **under a guard**: detection at 30
digits, then the polynomial must be **irreducible** and must vanish at **60**. `m004` and `m003` both
give `x² − x + 1` — **ℚ(√−3), the same field**; 40 of 40 sampled word-pairs agree.
**Positive control** `m015` gives `x³ − x − 1`, so the instrument can see a difference.
**GRADE, stated and not blurred:** this is the **shape field**. Its identification with the
invariant trace field is a theorem this seat **has not read and does not cite** — E58's clause,
minted in this session for exactly that failure.
**Fence, stated not hedged:** equal polynomials prove the fields equal; unequal ones prove nothing
on their own, so the rate is a **lower bound**.

**V5 — the table.** 4 of 4 sealed predictions confirmed.

**V6 — the kill condition, which did not fire.** xB021 left **three** banked negatives unexplained
and observed that every one is arithmetic. Each turns on an invariant **whose orbit is trivial**:

| miss | turns on | orbit |
|---|---|---|
| xB013 Addendum 1 — selection among an infinite family | the field `ℚ(√−3)` against `ℚ(√5)` | **trivial** |
| xB017 — the Bianchi base rate | arithmeticity, a property of the field | **trivial** |
| xB017 Addenda 2/3 — orbifold covering theory | commensurability, an invariant of the field's class | **trivial** |

> **They were never stabiliser negatives. They are a THIRD SPECIES: questions asked of an invariant
> that has NO ORBIT — so xB021's remedy, "move to the orbit", cannot reach them even in principle.**

**V7 — the family index, and a law nobody asked for.** Over B1186's 112 members (re-read, count
confirmed): 33 distinct `H₁` signatures, 29 torsion-free, 51 with square torsion order. **`|Tor H₁|`
is NOT surjective onto ℤ/12** (9 of 12 residues) — so **`H₁` shares `CS`'s stabiliser but not
`CS`'s family index**, and that null is reported as a null. Every modulus is printed, not just the
first hit, because a first hit at `m = 2` is trivial and printing it beside a "null result" line
would itself be E69.

**Then, labelled EXPLORATORY and beyond the seal:**

> **`|Tor H₁(b+-w)| − |Tor H₁(b++w)| = 4` — exactly, for all 494 words.**

A constant shift. **A5 shifts `CS` by ¼ and shifts the torsion order by +4.**
**And the caution that goes with it, measured in the same cell:** across the corpus,
`(b++ square, b+- not)` occurs **70** times while the **reverse occurs 80** — so "square torsion
picks the `b++` branch" is **false in general** and true at the minimal word only. That limit is
carried into xB023 rather than left for a reader to discover.

---

## WHAT THIS DOES NOT DO

It supplies **no value** — not `σ`, not `c`, not any coupling; xB016 closed that route and nothing
here reopens it. It does not promote a measured rate to a theorem. It does not claim the shape
field **is** the invariant trace field. It sharpens xB021's diagnosis from *"the walls are the
stabiliser"* to something stricter and more useful:

> **Two of the four invariants have no orbit at all. For those, there is no mechanism to move to —
> which is exactly why the three arithmetic negatives never fitted.**

**Axes held fixed and named:** the shape field stands in for the trace field, graded · the ± sign
convention is SnapPy's bundle notation, re-derived not cited · the family-level cell covers B1186's
112 and no wider census · V4's corpus figure is a 40-word sample, not the full 494.

**Gate 5 absolute. Nothing to `CLAIMS.md`.**
