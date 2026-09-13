# PREREGISTRATION — KMRT ARRIVES: the trialitarian record verified against the source

**Sealed 2026-09-13, before the certificate was written.**
**Outcomes are stated as what will be OBSERVED. Consequences live in the memo's
interpretation sections, not here.**

## The source

*The Book of Involutions*, M.-A. Knus, A. Merkurjev, M. Rost, J.-P. Tignol — supplied by the
owner on 2026-09-13 as a **DRAFT** PDF (588 pp). **Stated up front because it changes what a
citation is worth:** in this draft **every internal cross-reference renders as `(??)`**, so a
numbered result can be quoted but the results it *cites* cannot be followed. Section and
theorem numbers, section titles, running heads and page numbers are intact and are what this
certificate anchors on. The relevant material is **Chapter X, "Trialitarian Central Simple
Algebras", §§43–44** (pp. 549–563) and **Chapter VIII, §36 "Twisted Compositions"** (pp. 487 ff).

**The bench's own standing ask named this as "KMRT Ch. VII §43 and §44.B."** Whether the
chapter number in that ask is right is CELL 5.

## What is being tested, and why it is not a formality

Memo 203 (`THE_LITERATURE_FLOOR`) reached its conclusions **from search-result summaries with
no full text obtained**, and said so in its own §5:

> *"the section-3 correction is THE MOST LOAD-BEARING AND THE LEAST VERIFIED ITEM and should be
> checked against KMRT or Knus–Tignol by a seat with document access BEFORE the record is edited."*

The record **was** then edited: memo 204 used that correction to type the object as **⁶D₄** and
to **REFUTE B882's ³D₄ naming**. So a banked refutation currently rests on an unverified
search summary. This preregistration exists to settle that, either way.

## Fixed inputs, taken from the record and not recomputed here

* `K = ℚ[x]/(x³ − 12x − 5)` — the object's cubic (B854/B1093, memos 204, 219).
* Memo 204 addendum 4's reduction: the commutant is a **quaternion algebra over `K`
  containing `K(√77)` as a maximal subfield**, **unramified at all three real places**, and
  `E` is split **iff** that quaternion algebra is split.

---

## CELL 1 — does KMRT's own definition type the object's cubic as ⁶D₄?

KMRT **§43.C** states the four types of trialitarian algebra in terms of the cubic étale
algebra `L`. The certificate quotes that sentence verbatim from the PDF text and computes, for
`K`, every quantity the sentence tests.

* **OUTCOME A** — the sentence is present verbatim, and `K`'s computed data satisfies **exactly
  the ⁶D₄ clause** and **none of the other three**.
* **OUTCOME B** — the sentence is absent, differs, or `K` satisfies a different clause.

## CELL 2 — is a cyclic composition available over `K`?

Memo 203 asserted, from summaries, that Springer's cyclic-composition construction needs an
order-3 automorphism `ρ` and that an S₃ cubic field has none. KMRT **§36.B** is the definition.

* **OUTCOME A** — §36.B's definition is quoted verbatim and requires `Gal(L/F) = A₃` with a
  **choice of generator ρ as part of the datum**, AND `#Aut(K/ℚ)` is computed to be `1`.
* **OUTCOME B** — the definition does not require this, or `#Aut(K/ℚ) = 3`.

## CELL 3 — is memo 204's pinned shape KMRT's normal form?

KMRT **§43.B** (Prop. 43.9, Prop. 43.11, Thm. 43.8) constrains which degree-8 algebras over a
cubic étale `L` carry a trialitarian structure.

* **OUTCOME A** — 43.9's normal form is `Q ≃ (a,b)_L` with **`b ∈ F×`** and `N_L(a) = 1`, and
  memo 204's pin (maximal subfield `K(√77)`, i.e. `b = 77 ∈ ℚ×`) **sits in that normal form**
  with `a ∈ K×`, `N_{K/ℚ}(a) = 1` as the single unknown.
* **OUTCOME B** — the normal form is different, or memo 204's pin does not fit it.

## CELL 4 — does the trialitarian classification DECIDE memo 204's open E-question?

This is the cell with something to lose. Memo 204 addendum 4 left `E` split-or-not **open** and
handed it to "a seat with a number-theory package". That seat now exists (memo 219). The
question this cell asks is whether KMRT's classification makes the object's own arithmetic
**unnecessary** — i.e. whether every quaternion algebra allowed by the ⁶D₄ typing is split.

The certificate searches an explicitly stated family of `a ∈ K×` with `N_{K/ℚ}(a) = 1`, and for
each computes the global Hilbert symbol `(a, 77)_K`.

* **OUTCOME A** — **at least one** such `a` is exhibited with `(a,77)_K` **NOT split** and
  **unramified at all three real places of `K`**: a non-split quaternion algebra satisfying
  every constraint the record has established about the object's commutant.
* **OUTCOME B** — **no** such `a` is found in the searched family; every one tested is split.
  **This is reported as a NOT-FOUND over a stated family, never as a proof of nonexistence.**

## CELL 5 — is the bench's own citation right?

* **OUTCOME A** — §43 and §44.B are found under a chapter number **different** from the
  "Ch. VII" the bench's standing ask has carried; the correct chapter is reported.
* **OUTCOME B** — they are in Chapter VII as the ask says.

---

## CONTROLS — every one must pass or the cell it guards is void

* **C1 (the instrument can say either thing).** `nfhilbert` must be shown returning **both**
  `+1` and `−1` on inputs whose answers are known independently, in this same run. A search
  that can only report "split" proves nothing. *(Memo 164: control passing is not instrument
  working; memo 213/R121: ask whether the statistic COULD have differed.)*
* **C2 (KMRT's own consequence, on the examples found).** For every non-split `(a,77)_K`
  exhibited in CELL 4, the certificate computes the ramified primes of `K` and checks that the
  number lying over each rational prime is **EVEN** — which is `N_{K/ℚ}([Q]) = 1`, the
  condition 43.8/43.9 require. If a CELL 4 example **violates** this, the example is
  **discarded and reported as discarded**, not quietly kept.
* **C3 (the field is the right field).** PARI's `K` must reproduce disc `6237`, signature
  `[3,0]` and `#Aut = 1` — B1093's hand-proved facts, re-validated as in memo 219.
* **C4 (the quotes are really in the book).** Every verbatim quotation this certificate makes
  is asserted as a substring of the extracted PDF text, with its page number. A quote that
  cannot be located **fails the run**.

## Fences, declared in advance

* This certificate **does not decide** whether the object's `E` is split. It can only decide
  whether the *classification* settles it. Any sentence claiming otherwise is out of scope.
* The PDF is a **draft**. No claim will be attached to a cross-reference that renders as `(??)`.
* **Gate 5 untouched. Nothing promotes. No arc is retracted by this certificate.**
* `docs/` and `frontier/` are not edited by this bench.
