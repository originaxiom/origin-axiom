# PREREGISTRATION — THE MIRROR AND THE BULK: where the rest of the object is

**Sealed 2026-09-14, before the certificate was written.**

## Occasion — the owner, two things "haunting my mind"

> *"the object is its own mirror … if the object is its own mirror, then where's the other part of
> the mirror?"*
> *"the object is a complement, it has no bulk … where is the rest whose complement it is, where's
> the bulk?"*
> *"why does it feel like we're computing only a part of something (complement, mirror, shadow), not
> the whole of it. where's the rest? what could be the rest?"*

**Both riddles are literal and both are computable.** This cell answers them from the object rather
than from metaphor, and then reports what the record has and has not examined.

---

## CELL 1 — THE BULK. What is the object the complement of, and what happens if you put it back?

`m004 = S³ ∖ 4₁`. The missing "bulk" is not mysterious: it is the **solid torus** glued back along a
slope — Dehn filling. C8 (B288/B740/B747/B748) is the banked census; this cell re-runs it.

* **OUTCOME A** — fillings **destroy** the object's arithmetic: the invariant trace fields of the
  closed fillings do **not** contain `√−3`, and the forced `V₄` is a property of the **open** object.
  **The bulk exists, has been looked at, and is arithmetically inert.**
* **OUTCOME B** — some filling preserves the trace field, and it is named.

## CELL 2 — THE MIRROR. Is the other half of the mirror a different object, or the same one?

* **OUTCOME A** — `m004` admits an **orientation-reversing self-isometry**: the mirror map is an
  **automorphism**, so there is no second object. *"The other half"* is the object itself, and the
  identification is what costs the bit.
* **OUTCOME B** — no such self-isometry; a distinct mirror partner exists and is named.

## CELL 3 — THE REST. Does the object's own covering tower break the mirror while keeping the atom?

The record's `FRESH_EYES` **Q15** asks: *is there a carrier that keeps the atom and remembers the
bit?* B1324 reports **YES, on the object's own tower**. This cell re-runs that census with its own
instrument.

* **OUTCOME A** — chiral covers of `m004` exist, and they **keep the invariant trace field
  `ℚ(√−3)`**: the "rest" is the tower, and it is **not arithmetically inert**, unlike the bulk.
* **OUTCOME B** — every cover is amphichiral, or the chiral ones lose the atom.

## CELL 4 — and does the rest supply what the object lacks?

* **OUTCOME A** — the record has already computed the chirality index on the chiral covers and it is
  **zero**, so the tower breaks the mirror **without** producing chirality; the honest frontier is
  named (what degree the census reaches, and what lies past it).
* **OUTCOME B** — a nonzero index exists on some cover, and it is named.

---

## CONTROLS — and one of them has already fired

* **C1 (THE NAIVE TEST IS WRONG, and this is recorded BEFORE the run).** `is_isometric_to(M, mirror)`
  **ignores orientation**: it returns `True` for `m015` (`5₂`), which is **chiral**. A first sweep
  using it reported **38 of 38 covers amphichiral to degree 8**, contradicting the banked census —
  **caught by comparison with B1324, not by the instrument.** The certificate must reproduce this
  failure explicitly so the wrong instrument is on the record.
* **C2 (two orientation-aware methods, as B1324 used).** (i) an isometry to the mirror with
  **cusp-map determinant +1**; (ii) the **Chern–Simons** sign test (`CS(M̄) = −CS(M)`, so `2·CS ≢ 0`
  ⟹ chiral). They must agree wherever both are decisive, on a control set containing a **known
  chiral** manifold and a **known amphichiral** one.
* **C3 (the CS test is ONE-SIDED, declared in advance).** `2·CS ≡ 0` does **not** prove
  amphichirality. It may only be used to prove chirality; the determinant test decides the rest.
* **C4 (the record is quoted, not recalled).** C8, Q15 and B1324's census are asserted as substrings
  of tracked files.

## FENCES

* **No physics reading is licensed.** This cell locates structure; it derives no value and touches no
  link past C4.
* **The multi-cusped index result lives on a branch** (`<remote>/paper-verification-ufp0zn`, B1333) and
  is **cited as branch work, labelled as such, not re-run here.**
* **Gate 5 untouched. Nothing promotes. No arc retracted.**
