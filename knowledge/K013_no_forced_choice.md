# K013 — No forced choice in the invariant ring: the structure is a moduli space, not a chooser

> **Explainer** (`GOVERNANCE.md`). Self-contained; standard material cited to the literature, the project's own use
> cited by `B`/`V` number (no re-proof). Nothing here promotes to `../CLAIMS.md`; never a premise in a proof. The
> bankable MATH of the no-forced-choice arc (B130/V119).

## The question, in its sharpest form

The project's firewall asks, ultimately, whether the structure can ever be *made to choose* a world. B130 makes that
decidable by naming the exact object a forced choice requires:

> A **forced choice** is an invariant `f` of the metallic trace map that is **(1) invariant** (fixed by the map — the
> structure must value it), **(2) discretely multivalued** (finitely many distinct values on the fixed locus —
> something to choose, not a continuum to slide along), and **(3) unsymmetrizable** (the structure's symmetry group
> does not relate those values).

Conditions (2) **and** (3) are the crux. `κ` is invariant but *determined* (single-valued — no choice). Chirality (CS,
`K011`/B128) is multivalued but condition (3) **fails** — the `Z₂` mirror relates `+CS ↔ −CS`. A forced choice needs an
invariant whose multiple values are a **discrete, non-orbit** set.

## The computation: κ is free on the fixed locus (B130)

In Fricke coordinates `(x,y,z) = (tr A, tr B, tr AB)`, with trace map `Ta:(x,y,z)→(x,z,xz−y)`,
`Tb:(x,y,z)→(z,y,yz−x)`, `φ_m = Ta^m∘Tb^m`, and the Fricke–Vogt invariant `κ = x²+y²+z²−xyz−2` (`K010`): adjoin `k=κ`
and eliminate `(x,y,z)` from the fixed-locus ideal `φ_m(x,y,z)=(x,y,z)`. **The elimination ideal in `k` is empty** —
`κ` is unconstrained on the fixed locus, varying **continuously** (no discrete value to select). Verified m=2,3,4
symbolically (lex Gröbner) and m=5 numerically (a 259-value continuum). So every trace-ring invariant is either
*determined* or *continuous*: the object a forced choice requires does **not** exist in the trace-ring /
character-variety invariants.

## The located fork — only "which seed," and it is external

If the continuous geometry has no fork, does the discrete combinatorics (the substitution word)? **L1:** within a fixed
`m`, the substitution `a→aᵐb, b→a` has a **unique deterministic fixed word** — no internal choice. **L2:** across `m`,
the substitutions are genuinely inequivalent — incidence `[[m,1],[1,0]]` has `trace=m` (distinct), `det=−1`, so
different `m` are **not** GL(2,ℤ)-conjugate, with distinct Perron fields ℚ(√(m²+4)). So "which `m`" **is** a discrete
unsymmetric fork — but `m` is the **seed parameter**: it labels *which structure exists*, not a fork a unit resolves
from inside. The discreteness lives entirely in the seed **label** (input), never in the unit's internal dynamics
(output).

## The reading: a moduli space does not choose

The structure is a **moduli space** — continuous `κ` × discrete seed-label — and *a moduli space parametrizes, it does
not choose*. This is the **root** of "permits but never forces" (`../philosophy/P008`, B128): internally a unit is
fork-free (deterministic word + continuous `κ`); the only discreteness is the external seed. Even viewing "the
structure" as the whole metallic family, it *contains* all `m` (a parameter space), it does not *select* one.

Together with `K012`/S031 (the SL(n) tower fixes only the `Sym^{n−1}` image — no new arithmetic up the ranks), this is
the **internal** companion to that **vertical** rigidity: *single-seed self-reference is rigid in every tested
direction — determined or continuous, never forced-discrete.* This is the seventh firewall direction
(`../philosophy/P007`); the only "this is physics" remains the emergent `K010` naming.

## Method (a banked tombstone and its lesson — `REPRODUCIBILITY.md` SCAN)

A killed false-positive (`K-G`, `../speculations/TOMBSTONES.md`) declared a forced choice from "isolated fixed points
with distinct κ" returned by `sp.solve`. Those were **degenerate points of the continuous fixed curve**, not
0-dimensional components (some branches still carried a free symbol, e.g. `κ = z²−2`), and the symmetry argument was
circular (only the κ-preserving sign subgroup). **To test discrete-vs-continuous fixed-locus value, use the
κ-elimination ideal (empty ⟹ continuous) and confirm 0-dimensionality by Jacobian rank — not `sp.solve`
branch-counting.** This is the *revival* failure mode (a too-eager "yes"), sibling of the B129 method-bug-#2 (the kill
failure mode).

## What is open

This is the trace-ring statement only. The **theorem-version** — that *no* invariant whatsoever (higher cohomology,
torsion, quantum/CS) is discretely-multivalued-and-unsymmetric — is the open MATH target `../speculations/S032`, which
also records the next forced-answer question: *is choice an emergent property of multiplicity (does combining two seeds
create an internal fork neither had alone)?*

**Anchors:** B130/V119 (the result, the located fork, `K-G`), B128 (`K011` chirality `Z₂` — condition (3) fails),
B129 (`K012`/S031 — the rigidity sibling), `K010` (`κ` = the Fricke–Vogt invariant), `../philosophy/P007`/`P008`,
`../speculations/S032` (the open program). External: Fricke trace coordinates; Markov/character-variety trace maps.
