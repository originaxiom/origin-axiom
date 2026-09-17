# xB013 — the product of both faces supplies 3.39 bits and stops at a PAIR: the object of the two faces is m004 *and its sign-twin*, and the last bit is A5's

**Status: banked (frontier, `sep16-branch`). Verdict PROVED.** Seat `xb`.
**PREREGISTRATION sealed and pushed BEFORE any cell ran** — sha256
`fd3568c38fbdec91e2749464be7e24e3c93d6fddad1ce0368e1384e65d1bc171`, commit `063e19f`.
Gate 5 untouched. Lock: `verification/reproduce.sh`, five cells.

## The thesis, and what it resolves to

> *"physics might be the product of both faces."* — the owner

**It is not a slogan, and it does not reach a manifold. It decomposes the selection.**

## X1 — κ re-derived, not cited

B309/B518/B1010's κ-unification reproduces exactly at `ρ_geo`:

> `κ = tr[a,b] = 3/2 − (√3/2)i` · **`κ − 2 = ω²` exactly** · `|κ − 2| = 1` — the **unit
> obstruction** · `κ = 2 ⟺ the cancellation completes ⟺ nothing`

So **κ already IS the product of both faces**: `2 + λ²` is the golden/Fricke–Vogt side,
`κ − 2 = ω²` the Eisenstein side. This arc does not re-claim it; it asks whether it **selects**.

## The faces, defined before computing, and measured

* **EISENSTEIN** = invariant trace field `ℚ(√−3)` — xB007's 21-member commensurability class.
* **GOLDEN** = fibres as a once-punctured-torus bundle with monodromy `|trace| = 3` (eigenvalues
  `φ^{±2}`).

| step | survivors |
|---|---|
| Eisenstein face alone | **21** |
| + fibres as a o-p-t bundle | **6** |
| + **GOLDEN** (`\|trace\| = 3`) | **2** — `m003`, `m004` |
| + **A5** (torsion-free, `H₁ = ℤ`) | **1** — `m004` |

> **The product of the two faces cuts 21 → 2: 3.39 bits.** The golden face is **thin** — 2 of 21,
> and 2 of the 6 that fibre at all.

## X4 — and it stops one bit short

The two minimal members of the intersection have **identical volume** `2.0298832128`, so the
product of the faces returns a **PAIR**, not a member. That was this seat's sealed prior, and the
reason is exact: **`m003 = b+-LR` and `m004 = b++LR` carry the SAME monodromy word**, differing only
by the sign `−I`.

> **The residue is exactly ONE BIT, and it is not a new bit.** It is precisely the bit xB007
> identified as knot-ness, `det(φ_*−I) = ±1` — and precisely the bit xB007 proved the **character
> variety cannot see**, because the trace map factors through `PSL(2,ℤ)`.

## A correction this arc made to itself before shipping

A first draft of X5 asserted *"the intersection is a TOWER, not a point."* **The table contradicts
it**: `(LR)ⁿ` for `n ≥ 2` has `|trace|` **7, 18** — Lucas `L₄, L₆` — **not 3**, so `m206` and `s961`
are **not** golden. The tower is golden only at its first step. Corrected to a measurement before
anything was banked.

## What this establishes

1. **κ really is the product of both faces** — re-derived exactly, not cited.
2. **The product is a strong selector**: `21 → 2`, **3.39 bits**, and the golden face is genuinely
   thin rather than a tower.
3. **It does not close.** The last bit is the monodromy sign, which is **A5's**, and the two faces
   together do not take that step.

> **The object of the two faces is the PAIR `{m003, m004}` — a manifold and its sign-twin — not
> either one alone.**

That is the owner's thesis, sharpened by measurement: *not that selection was wrong, and not that
the faces select — but that the faces supply 3.39 of the ~4.4 bits, and the axiom supplies the
last one.*

## What is NOT claimed

* **No physics.** That the faces "multiply" in any physical sense is **not** claimed; no
  identification is made and no link graph is asserted (**E82**).
* **Base rates reported, not assumed**: golden is 2/21 in the class and 2/6 among those that fibre.
* **No axiom amended.** A5 is the record's.
* The search for bundle structure reaches all four `b±±` prefixes at word length ≤ 9; a class
  member fibring with a longer word would be missed, and the 6/21 figure is a **lower bound**.

**Provenance.** `verification/both_faces.py` (X1–X5) → `reproduce.sh`. Re-derives B309/B518/B1010
(κ), and builds on xB007 (the 21-member class, the `−I` bit), xB012 (the faces on opposite sides of
A5), B425 (the two torsions).
