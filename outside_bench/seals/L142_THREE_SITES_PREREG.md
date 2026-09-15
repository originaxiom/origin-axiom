# PREREGISTRATION — L142: three sites, one field. One theorem or three facts?

**Sealed before any computation. Bench: the outside bench. Date 2026-09-11.**

## 0. The cell, in the record's own words

`docs/OPEN_LEADS.md` **L142** (registered 2026-08-08, from B969/solo §5), **never run**:

> *"**THREE SITES, ONE FIELD: one theorem or three facts?** K now appears at three constructions in
> two representations: μ's adjoint pencil, κ's adjoint pencil, and the cubic form on the compact
> kernel **in the 27**. **Not adjudicable by opinion.** The discriminating test, named: **exhibit a
> morphism carrying one pencil to another, or show the agreement is only of outputs.**"*

The record also corrected its own blocker label (2026-08-12): *"L142's 'blocked on L135' label
corrected … 'A separate cell' is a not-run, not an obstruction; the label propagated without its
reason."*

## 1. Corpus exhausted first, per question, terms stated (memos 153 / 199 / bench errors #23–#24)

`already_banked.py` on: *"three sites one field morphism between pencils or agreement of outputs"*,
*"joint kernel of x14 x22 on the 27 three dimensional subspace"*, *"restriction of x8 to a subspace
of the 27 generates the charge field K cubic"*, *"bridge between the D4 locus and the 77-bearing
charges disjoint loci"*. **And — the step this bench omitted twice today — the fetched-literature
JSONs** (`priorart_findings.json`, `prior_art_*.json`) were grepped directly, since
`already_banked.py` reads prose and skips them.

Read and credited: **B866** (the (x₈,x₁₆) adjoint pencil → μ), **B874** (the 15-subtorus census),
**B877**, **B898**, **B904**, **B969** (the vacuum 3-block → K by Kato–Yukie; *"only the COMPACT
charges have a kernel on the 27 (g14, g22 → dim 3; g8, g16 → dim 0)"*, recorded there as **not
verified** on that bench), **B939** (which touches the (14,22) pair only as a **rank check**, never
a charpoly), **B1077**, **W4 / NOVELTY_SWEEP_LEDGER row 6**.

**What this bench adds as a fourth site:** the **(x₁₄,x₂₂) pencil's branch locus on the 27** — built
for the first time in memo 201 — two cubics, neither equal to μ, both generating K, discriminants
carrying `19¹²` where μ carries `13¹²`.

## 2. The test, made computable — and the trap named first

**The naive form of the test is VACUOUS and is rejected before it is run.** Over ℚ, `PGL₂` is
3-transitive on `ℙ¹`, and the root-triple of an irreducible binary cubic is Galois-stable, so **any
two irreducible binary cubic forms over ℚ with isomorphic root fields are `PGL₂(ℚ)`-equivalent up to
scalar.** A `GL₂(ℚ)`-equivalence test therefore **cannot fail** — MB12. It is not used.

**And the integral refinement is rejected too, for a different reason.** `GL₂(ℤ)`-class
(Delone–Faddeev) *can* fail — but the sites' cubics are read off exact matrices **in a chosen
basis**, and rescaling the pencil parameter is a `GL₂(ℚ)` move that changes the integral class.
B866 records exactly such a rescaling between two constructions of μ (*"theirs(13t) = 2197·mine(t)"*).
**A `GL₂(ℤ)` test would be measuring basis conventions, not mathematics.** It is not used.

**What is used instead is the morphism question itself, in two layers.**

## 3. THE CELLS — two outcomes each, fixed now

**CELL 1 — across representations: can any equivariant morphism exist at all?**
μ's site is a pencil on the **adjoint 78**; the compact-kernel site and the new (x₁₄,x₂₂) site are on
the **matter 27**.
* **A** — the two representations are isomorphic, or admit a non-zero `e₆`-equivariant map. A
  morphism is then possible and must be looked for.
* **B** — they are **inequivalent irreducibles**, so `Hom_{e₆}(27, 78) = 0` by Schur and **no
  equivariant morphism carrying one pencil to the other exists**.

**CELL 2 — within one representation: are the two 27-side pencils conjugate?**
Both `(ρ(x₈), ρ(x₁₆))` and `(ρ(x₁₄), ρ(x₂₂))` act on the same 27. A morphism here would be a
`T ∈ GL(27)` simultaneously conjugating one ordered pair to the other.
* **A** — every conjugation invariant agrees (kernel dimensions, characteristic polynomials,
  rational canonical forms). A morphism is not excluded and must be constructed or excluded finer.
* **B** — some conjugation invariant **differs**, so no such `T` exists — **proved, not searched for**.

**CELL 3 — is the agreement real at output level?**
* **A** — the sites' cubics do **not** all generate `K`; then there is no agreement to explain and
  L142 dissolves.
* **B** — every site's cubic generates `K`, verified with positive and bite controls.

**The verdict rule, fixed now:** `B/B/B` answers L142 **THREE FACTS — the agreement is of outputs**.
`A` anywhere leaves the morphism question live and the cell says so.

## 4. CONTROLS, fixed now

* **C1 — the field test must be two-sided.** A positive control (μ found isomorphic to K) and a
  **bite** control (an unrelated cubic of the same resolvent `ℚ(√77)` found **not** K), or
  "generates K" is an instrument that cannot say no.
* **C2 — the conjugacy test must be able to say YES.** A matrix pair conjugated by a known random
  `T` must be reported **conjugate**, or CELL 2's negative is an artifact.
* **C3 — and able to say NO** on a pair that is genuinely non-conjugate.
* **C4 — every site's cubic is recomputed here from the build**, not copied from a memo, except
  where a banked polynomial is being reproduced *as* a check (B866's μ), which is labelled as such.
* **C5 — exact arithmetic throughout.** No discriminant or kernel dimension read numerically.

## 5. What this cannot deliver, stated before it is run

It cannot prove that **no** relation of any kind exists between the sites — only that **no morphism
of the two named kinds** does. A common *upstream cause* (all sites being determined by the same
four-dimensional charge space) is **not** excluded by a `B/B/B` result and must be stated as the
residue rather than buried. It cannot produce a value, a ratio or a prediction. It does not prove or
refute B882, and it does not decide whether the object's cubic is canonically K.

**Gate 5 untouched. No measured value is used as input anywhere.**
