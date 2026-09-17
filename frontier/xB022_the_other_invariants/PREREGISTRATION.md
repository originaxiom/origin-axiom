# xB022 — PREREGISTRATION (sealed before the verification code exists)

**Seat `xb`, `sep16-branch`, 2026-09-17. Sealed, hashed and pushed before any cell runs.**

## P0

Group actions on topological invariants of a named family of hyperbolic 3-manifolds. Named
mathematics. No value, no generation count, no physics reading, nothing to `CLAIMS.md`. Gate 5
absolute.

## The owner's instruction

> *"do them properly and apply all the verifications u can think of, verify also banked data when u
> refer to them"*

— the first of the two continuations xB021 fenced inside its own verdict.

## WHAT WAS RUN BEFORE THIS SEAL (declared, not hidden)

Three things touched the bench before sealing, and all three are declared here so the seal is honest:

1. `snappy.Manifold('m004')` — `volume()`, `homology()`, `chern_simons()`. Textbook values, used only
   to confirm SnapPy 3.3.2 is present and functioning.
2. `snappy.Manifold('m004').symmetry_group()` and `dir()` on its `Isometry` objects — an **instrument
   scout** for xB023, establishing that `Isometry` exposes only
   `cusp_images, cusp_maps, extends_to_link, num_cusps`.
3. Reading of banked arcs (xB013 Addendum 1, xB021, B1239, B1235, L194's register entry).

**No cell of this arc has been run. No prediction below has been tested.**

## The question

xB021 computed the stabiliser of the object's Chern–Simons value and held **`CS` only**, naming that
as its principal limitation:

> *"Volume, `H₁` and the trace field are NOT analysed as group actions here, and the three arithmetic
> negatives fall outside."*

This arc removes that limitation. **For each of volume, `H₁` and the invariant trace field, is the
object a fixed point of the same stabiliser `{A6, A7}`, of a larger one, or of a smaller one?**

## THE CONFIGURATION AXES — declared first (xB017 Addendum 4's rule)

| axis | values | this arc |
|---|---|---|
| **the invariant acted on** | `CS` / volume / `H₁` / trace field | **volume, `H₁`, trace field.** `CS` is re-derived only as the control |
| **the bits** | A5 · A6 · A7 | **all three** |
| **the word corpus** | the minimal word `LR` / xB015 K6's 494 mixed words / B1186's 112-member family | **all three, and each named where used** |
| **the locus** | the object / the sister pair / the family | **all three** |
| **held fixed** | the ±-sign convention of SnapPy's bundle notation | **b++ / b+- as xB015 K6 used them, re-derived here, not cited** |

## The predictions — each falsifiable, each stated before the data

**V1 — volume under A5.** For every word `w` in the corpus, compare `vol(b++w)` with `vol(b+-w)`.
*Prediction:* **EQUAL for every word** — A5 lies in volume's stabiliser. Ground: `m003` and `m004`
are the two smallest cusped orientable hyperbolic 3-manifolds and share the volume `2v_tet`.
*Refutation:* one word with unequal volumes refutes the prediction, and the arc must report A5 as
moving volume.

**V2 — volume and `H₁` under A6 and A7.** Mirror images have equal volume and equal `H₁`.
*Prediction:* stabilised, by construction. *This cell must still be RUN, not asserted* — an assertion
next to a number that does not test it is **E69**, already in this record's ledger.

**V3 — `H₁` under A5.** *Prediction:* **MOVED.** At the minimal word, `H₁(m004) = ℤ` and
`H₁(m003) = ℤ ⊕ ℤ/5`. Across the corpus the prediction is that they differ for a **majority** of
words. *Refutation:* if they agree for a majority, `H₁` joins volume and the predicted table is wrong.

**V4 — the invariant trace field under A5.** *Prediction:* **EQUAL** at the minimal word (both
`ℚ(√−3)`); across the corpus, honestly unknown, and the arc must report the measured rate rather than
assert. *No prediction is made for the corpus and none may be read into the result.*

**V5 — the stabiliser table.** Assemble, from V1–V4 and xB021's `CS` result re-derived here as
control:

| invariant | predicted stabiliser | predicted orbit of the object's value |
|---|---|---|
| volume | **all three bits** | **trivial** |
| trace field | **all three bits** | **trivial** |
| `CS` | `{A6, A7}` | `{0, ¼}` |
| `H₁` | `{A6, A7}` | **two values** |

**V6 — THE CELL THAT CAN REFUTE THE UNIFICATION.** xB021 reported three banked negatives that did
**not** fit its hypothesis, and noted that every one is arithmetic: xB013 Addendum 1 (selection among
an infinite family), xB017 (the Bianchi base rate), xB017 Addenda 2/3 (orbifold covering theory).
*Prediction:* each of the three turns on an invariant whose orbit is **trivial** — so they are not
"the thing asked about is in the stabiliser" negatives but a **distinct species: invariants with no
orbit at all.**
*Kill condition, binding:* **if any one of the three turns on an invariant that A5 moves, the
unification fails and must be reported as refuted, not re-scoped.**

**V7 — a family-level index for `H₁`.** xB015 found `24·CS mod 12` surjective onto ℤ/12 on B1186's
112-member family. *Question, not prediction:* does `H₁` torsion carry a comparable index?
*Required honesty:* this cell is exploratory and **must report a null result as a null result.**

## Controls required before any cell counts

- **Re-derivation, not citation.** Every banked number this arc leans on — xB015 K6's 494-word
  corpus and its ¼-shift, xB018 C5's negation, B1186's 112 — is **recomputed here from SnapPy**.
  A number taken from a banked `FINDINGS.md` and not recomputed must be labelled **CITED** in the
  findings table.
- **A base rate for every "they differ" claim** (the E-class this session has hit twice).
- **A positive control**: a comparison known to differ must be shown to differ by the same code.
- **Exact arithmetic where the claim is exact**; tolerance declared where it is numerical.

## What this arc may NOT conclude

It may not conclude that any invariant supplies `σ`, `c`, or any value — xB016 closed that route and
nothing here reopens it. It may not promote a measured rate to a theorem. It re-poses, at most, the
same question xB021 re-posed, on three more invariants.
