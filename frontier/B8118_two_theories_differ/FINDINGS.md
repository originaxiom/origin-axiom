# B8118 — the two theories **differ in KIND**: the ambiguity was a category error

**Date:** 2026-08-21 · **Seat:** cc3, audit · **Lane:** MATHEMATICS. **Gate 5 untouched.**
**Owner-elected:** *"Neither — first prove they differ."*

> **SCOPE.** Tetrahedron **shape fields** over the orientable cusped census, and the arithmetic
> chain `disc → conductor → SL(2,ℤ/N) → McKay`. It uses the **shape field**, which for these
> manifolds is the invariant trace field up to the standard relation; **this arc does not
> independently verify that identification and says so.** It does **not** evaluate either theory,
> and does **not** decide which one to complete.

---

## What was actually open

B8099 found the corpus attaches **two** theories to `m004` and **asserted** *"these are not the same
theory"* — on the strength of **B262's wall #2**, which is an **open question** (*"is E₆ ever
dynamical"*), **not a proof**. The owner elected to settle it before choosing.

## The instrument: a genericity control, the same one as B8111

**If E₆ attaches through the FIELD rather than the MANIFOLD, every manifold sharing that field
inherits the same E₆** — and a quantity constant on a family cannot distinguish a member of it.

**How E₆ actually reaches the object — every step arithmetic:**

```
shape field disc −3  →  conductor 3  →  SL(2,ℤ/3), order 24  ≅  2T  →  McKay  →  E₆
```

**No step mentions the triangulation, the volume, or the geodesics.** *(B997's own correction re-run
rather than cited: `SL(2,ℤ/3)` has **exactly one** involution — consistent with `2T`; `SL(2,ℤ/4)`
has **seven**, so it is **not** `2O`.)*

## ⚠ The control bites

| | |
|---|---|
| census manifolds scanned | **1200** |
| **sharing `m004`'s shape field `ℚ(√−3)`** | **14** |
| which are | `m003, m004, m202, m203, m206, m207, m208, m410, m412, s118, s119, s594` … |
| distinct volumes among them | **3** |
| **tetrahedron counts among them** | **[2, 4, 5, 6]** |

**`m003` — the figure-eight sister — is in the family, as are `m202`, `m410`, `s118`, and nine
others.**

> **E₆ is a function of the FIELD and is inherited by all 14. The DGG
> theory is a function of the TRIANGULATION and is not** — the tetrahedron count runs
> `[2, 4, 5, 6]` across the very same family, so those manifolds have
> **different** DGG theories while sharing **one** E₆.

## The verdict

**They differ, and they differ in kind.**

- **(A)** attaches at the **triangulation** and is a **QFT**: `U(1)`, 2 chirals, rank 1.
- **(B)** attaches at the **shape field** and is **arithmetic**.

> **So "the 3d theory of m004" was never ambiguous between two theories. It was a CATEGORY ERROR:
> one of the two is not a 3d theory of this manifold at all.**

**This upgrades B8099's assertion to a proof, and changes the statement:** not two candidate
theories, but **a 3d theory and an arithmetic structure**. **B990's shape recurs** — an invariant
constant on a family cannot pick a point in it.

## A hygiene hazard caught in passing, and its blast radius checked

While setting this up, `import snappy` from the scratchpad emitted stray output. Cause: a scratch
file **`grp.py` shadowing the Python standard library's `grp` module**. **Neutralised.**

**Blast radius: none banked.** Every arc that imports SnapPy — B8100, B8112, B8113 and this one —
lives in and runs from its own `frontier/` directory, so `sys.path[0]` is the arc directory, never
the scratchpad. **Checked rather than assumed.**

## Artifacts

`two_theories.py` · `results.json` · `tests/test_b8118_two_theories_differ.py`
