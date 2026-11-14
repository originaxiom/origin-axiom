# Metallic foundations — the rationale for "aim the theorem at the family"

> **SPECULATION / PHILOSOPHY — motivation only.** Nothing in this file is a claim. No content here
> promotes to `../CLAIMS.md` (GOVERNANCE §5), and none of it may appear as a premise, lemma, or step
> in any proof, `frontier/` FINDINGS, `papers/` note, ledger row, or commit message. This file *may* cite
> the mathematics; **the mathematics never cites this file.** The arrow is one-way: philosophy → why the
> mathematics is shaped this way, never philosophy → a mathematical conclusion.

This sits beside `PHILOSOPHICAL_PATHS.md` (P1–P5) and follows the same discipline: it exists to be
**exhaustive** (the original intuition is philosophical before it is mathematical), **governed** (kept
strictly out of the claim-bearing work), and **useful** (a precise statement of *why* the mathematics
takes the shape it does).

## The motivating question (why the family, not the seed)

The tower program studies the metallic substitutions `a → aᵐb, b → a`. Historically the seed `a→ab`
(`m=1`) was *chosen*. The motivating move of "Paper 0" is to stop choosing it and instead characterize
the whole family by a condition, with `m` free.

The informal driver: one cannot *define* "nothing" — to define it is to give it a determination, i.e. to
make it *something*. The only well-posed direction is the negative one, "what is **not**-nothing?", and
its minimal answers do not single out one object — they form a **self-generating family**. This is the
crucial expectation: a self-referential foundation that produced a *unique* seed would be the suspicious
outcome (fixed-point phenomena generically give *sets*, not points). So **"we end up with a family, `m`
free" is the intended shape, not a gap to be closed.** Any attempt to force a single seed relocates the
choice into a hidden metric rather than removing it.

**This paragraph is motivation. It is not, and must never be reported as, a result.**

## What the mathematics actually says (and where it lives)

The mathematics this motivates is entirely neutral and lives in the proof artifacts, not here:

- **The classification** (`frontier/B92_*`): among non-negative hyperbolic unimodular `2×2` matrices, the
  dominant eigenvalue has a purely-periodic period-1 continued fraction **iff `det = −1`**, which cuts out
  the metallic family `λ_m = [m; m, …]`, companion `M_m = [[m,1],[1,0]]`, up to `GL(2,ℤ)` conjugacy. This
  is a finite computer-assisted classification — no philosophy is used to obtain it.
- **The contingency boundary** (`MyCalc-5`): no conjugacy invariant distinguishes a single `m`; selecting
  `m=1` (golden) requires importing a metric — `m=1` is the systole (shortest closed geodesic on the
  modular surface). This is the *mathematical* form of "the family is determined, the member is
  contingent." It is a computed statement, not the philosophy above.
- **The bridge** (`frontier/B93_*`): `det = −1` is also exactly what gives the tower its sign/parity
  (the small eigenvalue `−1/λ ∈ (−1,0)` is negative), so the same condition that selects the family
  generates the tower's two-sheeted structure. Again: a theorem, proved without reference to this file.

## Interpretive lenses (each clearly SPECULATION)

These are *readings* of the mathematics, offered for orientation only:

- **Systole / Teichmüller (lens).** Each metallic `m` is a closed geodesic of length `2 log λ_m` on
  `H/GL(2,ℤ)`; `m=1` (golden) is the systole. A reading: "the member is the shortest distinction." The
  mathematics (the length computation, `MyCalc-5`) stands on its own; this sentence does not.
- **Galois (lens).** The contragredient `M_m → M_m⁻¹` is the Galois involution of `ℚ(√(m²+4))`
  (`λ_m ↔ −1/λ_m`). A reading: "the tower's discrete symmetry is the arithmetic of a real quadratic
  field." The identification (`MyCalc-4`) is a computation; the reading is not.
- **Renormalization / Lawvere (lens).** Lawvere's fixed-point theorem yields a fixed-point *set*, which is
  *why* the honest output is a family. Whether the metallic family is literally `Fix(R)` of a canonical
  renormalization endofunctor is an open mathematical question (`frontier/B95_*`); its honest status is
  recorded there, not here. The lens is only: "self-reference predicts a family, and the mathematics
  delivers one."

## The permanent boundary (stated as motivation, enforced as discipline)

The family is the result; the member is contingent. No principle selects a single `m` without
re-importing a metric. Treating the freedom in `m` as something to eliminate is the error this file
exists to forestall. The corresponding *mathematical* statements (classification, systole, parity) carry
their own proof-status in `frontier/` and `papers/`; this file carries none.

> If any sentence here ever needs to be cited to support a claim, that is the signal that the boundary has
> been crossed — stop and move the content into a neutral mathematical form, or it does not belong in the
> proof at all.
