# PREREGISTRATION — is §8's chirality bit the manifold's mirror sign?

**Sealed before any cell is run. Bench: the outside bench. Date 2026-09-11.**

## 0. The question, and who asked it

`frontier/B1327_relation_not_observer/FINDINGS.md` (verdict **OPEN**), on the tree
`<seat>/paper-verification-ufp0zn` at `e829c02c`, raises one item and explicitly declines to
decide it:

> The genesis **swap** is booked in §2's pre-object assumptions; the **arrow** and the
> **chirality bit** are booked in §9. A relation among three bits spanning two tables is exactly
> where a double count would hide.
>
> **This is not a claim.** §8's chirality bit is a Fricke-`kappa` torsor class of a *pair*, and may
> not be the same object as the manifold's mirror sign. Whether they are the same bit is for the
> seat that owns §8 to adjudicate. If they are, one of the three rows is not an independent input.

This bench does not own §8. It adjudicates the **mathematical** half of the question — *are the two
quantities the same function?* — and leaves the **ledger** half (which row moves, if any) to the
seat that owns the table.

## 1. The two quantities, fixed now, in the words of the record

**Q1 — §8's chirality bit** (`papers/P3_THE_PAPER/main.tex`, §`sec:observer`):

> For a heterogeneous pair — the object together with a partner — the mirror is realisable over
> `GL_2(Z)` only with determinant −1. The resulting class is mirror-odd, dimensionless, and belongs
> to the **pair**: it is an invariant of neither relatum separately, and it is invisible to the
> traces. … The invariant deciding whether a pair carries the bit is the Fricke commutator-trace
> discriminant `kappa(A,M) = tr[A,M] − 2`.

Its decision procedure is **not** left to prose: B1248 (**PROVED**) supplies it as a law —
`eps = −1  <=>  2 − kappa = −g^2`, with `g` the entry-gcd of the additive commutator `AM − MA`, and
the four-branch trichotomy `D = (2 − kappa)/g^2`.

**Q2 — the manifold's mirror sign**, the third entry of B1327's own triple: for each isometry of
the object, the determinant of its induced map on the cusp, `mirror = det(cusp_map)`.

## 2. Corpus exhausted first, terms stated (memo 153)

`scripts/checks/already_banked.py` run on: *"chirality bit same as mirror sign"*, *"Fricke kappa
torsor pair double count"*, *"arrow swap mirror three bits one relation"*, *"freedom ledger
independent input over-count"*. The settled arcs returned and read: **B1248** (PROVED, the norm
classification), **B1192** (the relational bit exists), **B1200** (one polynomial, three faces),
**B1182**, **B1183**, **B1222**, **B1226**. **B1248 is the governing arc** and is read before the
cells are written; the corpus's own instrument
`frontier/B1248_norm_classification/verification/norm_classification.py` is run before any
bespoke code is written (memo 154).

## 3. THE CELLS — two outcomes each, fixed now

**CELL 1 — is Q1 a function of the object relatum alone?**
Hold the object relatum `A` fixed and sweep the partner `M`; read the B1248 class of each pair.
* **A** — the class is **constant** over the sweep. Then it is a function of `A` alone, and it
  **could** be the mirror sign; the over-count stays live.
* **B** — the class **takes more than one value** while `A` never changes. Then it is not a
  function of the object alone, and it is not any invariant of the object alone.

**CELL 2 — is Q2 a function of the object alone, and is it non-trivial?**
* **A** — computing it requires a partner, or it is constant on the object.
* **B** — it is computed from the object's own symmetry group with **no partner named anywhere**,
  and it **separates** the isometries into two non-empty classes.

**CELL 3 — on the object itself, do the two agree about PRESENCE?**
* **A** — both are present and non-trivial on the object. Identity remains possible; the
  over-count is not resolved here and the cell says so.
* **B** — one is present and non-trivial while the other is **absent**. Two quantities that
  disagree about their own existence on the same object are not the same quantity, and B1327's
  over-count resolves **NO**.

## 4. CONTROLS, fixed now

* **C1 — B1327 must reproduce.** Its script is re-run as written: eight isometries, four of the
  eight a priori sign triples, **zero** violations of `mirror = arrow x swap`. If it does not
  reproduce, nothing else in this certificate is read.
* **C2 — the kappa convention is PINNED, not assumed.** This bench has already made this error once
  in chat: the character-variety form `tr[A,B] − 4` was compared against B1200's statement and
  produced a spurious contradiction. The certificate prints **both** forms on `m004`'s holonomy and
  requires the `−2` form to reproduce B1200 exactly — `tr[A,B] − 2 = omega`, `|tr[A,B] − 2| = 1`
  (the unit obstruction), `Phi_3(tr[A,B] − 2) = 0` — and requires the `−4` form **not** to.
* **C3 — the corpus's instrument runs first and must PASS** its own selftest before any of its
  functions are used here (memo 154).
* **C4 — the classifier must be able to return every branch.** All four of
  `DIRECT+1 / DIRECT−1 / TORSOR / DEGENERATE` must be realised in the sweep, or CELL 1's "more than
  one value" is an artifact of an instrument that cannot say "same".
* **C5 — the mirror sign must be able to come out CONSTANT.** A **chiral** one-cusped control is
  run: its symmetry group has no orientation-reversing element, so `det = +1` on every isometry. If
  the detector reports a split there too, it is not reading orientation and CELL 2 is void.

## 5. What this cannot deliver, stated before it is run

It cannot move a row of the freedom ledger; that is the §8/§9 owner's call and this bench says so
in the verdict. It cannot decide whether **arrow** and **swap** are independent of each other — that
relation is internal to B1327's triple and is untouched here. It cannot make the §8 bit derivable:
*"which pair is used remains supplied"* is the paper's own withdrawn support and nothing here
recovers it. A **B/B/B** result answers exactly one question — *are Q1 and Q2 the same bit?* — and
nothing more.

**Gate 5 untouched. No measured value is used as input anywhere in the computation.**
