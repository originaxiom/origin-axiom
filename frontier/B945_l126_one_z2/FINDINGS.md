# B945 — L126: ONE ℤ/2 OR TWO? **OUTCOME INDEPENDENT.** The unification is withdrawn.

**Date:** 2026-08-07 · **Seat:** cc (banking) · **Lane:** MATHEMATICS. Gate 5 untouched.
**Preregistration sha-256:** `4873215851b1ea76adbf7997b6795ed502dad7597d15ddb3f55bacb109d1dfdf`
— sealed, ledgered and pushed (`57be2252`) **before any cell ran**.

---

## The verdict, against the sealed criterion

> **OUTCOME INDEPENDENT** — Stab_V(object) = V (both ρ and σ fix it separately). Then the
> two ℤ/2's are **independent symmetries**, the object is invariant under each on its own,
> a closing may break one without the other, and **L126's unification FAILS**: TIME and
> CHIRALITY stay two separate closings exactly as B717 has them, and B944's suggested
> collapse must be withdrawn.

**Stab_V(RL) = {1, ρ, σ, ρσ} — the full Klein group.** The unification is withdrawn, as
the seal requires. B717's spine stands unamended: TIME and CHIRALITY are two closings, not
one.

## 1. Cell 1 — the object

W = **RL**, cyclic rotations {RL, LR}.

| map | image | a rotation of W? |
|---|---|---|
| ρ (reverse — TIME) | LR | **yes** |
| σ (swap — CHIRALITY) | LR | **yes** |
| ρσ (GHH amphichirality) | RL | yes |

So the object is amphichiral (as banked), **and** it is separately invariant under
time-reversal alone and under the mirror alone. **Stabilizer = full V.**

## 2. Cell 2 — and it is NOT a degeneracy of the shortest word

The prereg flagged, before compute, that RL has only two cyclic rotations and might
therefore be too short to separate the involutions — and pre-committed cells 2–3 for
exactly that reason. The family answers it:

**Every metallic word R^m L^m, m = 1…8, has the full Klein stabilizer.** ρ alone always
fixes it; σ alone always fixes it. So the result is not an artifact of m = 1: **the whole
metallic locus decouples the two involutions.**

## 3. Cell 3 — the census, and the finding that is worth more than the verdict

All cyclic LR-words with both letters, length ≤ 10: **241 cyclic classes.**

| stabilizer | count | amphichiral? |
|---|---|---|
| {1, ρ, σ, ρσ} — full V | **13** | yes |
| {1, ρσ} — **diagonal only** | **18** | yes |
| {1, ρ} | 122 | no |
| {1} — trivial | 88 | no |

Of the **31 amphichiral** classes, **18 sit in the LOCKED class** — fixed by the product
but by *neither* involution alone — and only 13 have the full group.

> **So the locking is real, it is the MAJORITY behaviour among amphichiral bundles
> (18/31 ≈ 58 %), and our object is in the minority that escapes it.**

That is a sharper statement than either outcome the prereg anticipated. The hypothesis
B944 raised was not wrong about the *phenomenon* — bundles whose time-reversal and mirror
are inseparable exist, and are typical. It was wrong about **m004**, which together with
its entire metallic family sits in the exceptional class where the two come apart.

## 4. Cell 4 — the identity underneath, and its vacuity check

**Rᵀ = L** (verified). Hence word-reversal and swap are related by transposition:
ρ = σ ∘ transpose, verified on the object — reverse(W) = swap(W)ᵀ exactly.

Consequently GHH's criterion reads: **amphichiral ⟺ W is conjugate to Wᵀ**. And indeed
W = RL = [[2,1],[1,1]] is **symmetric on the nose**.

**Vacuity check, run because the statement is suspiciously clean:** every matrix is
conjugate to its transpose over a field, so "conjugate to its transpose" carries **no
content at the level of ℚ**. Whatever content the criterion has must be **integral** —
about the GL(2,ℤ)-conjugacy class, not the rational one. This cell therefore does *not*
license any reading of "the monodromy is symmetric" as a deep fact; it is recorded as the
mechanism behind the combinatorics and nothing more.

## 5. What this does to the programme

**Withdrawn:** B944 §3's suggestion that TIME and CHIRALITY are one unbroken ℤ/2 for this
object, and the corollary that "one closing supplies both". **A closing that chiralizes
the object (B432: all 31 sampled Dehn fillings do) does not thereby supply a time arrow** —
the two involutions are independent symmetries here, and breaking one says nothing about
the other. The three named gaps do **not** collapse to one choice. L126 is **CLOSED,
negative.**

**Kept, and newly registered:** the LOCKED class exists and is generic among amphichiral
once-punctured-torus bundles. That makes "which class does a given bundle sit in?" a real
structural question with a clean combinatorial answer, and it places m004 — with the whole
metallic locus — on the exceptional side of it. Registered as **L129**.

**Method note.** The seal did its job in the direction that matters. The prereg named
LOCKED as *"the convenient answer… therefore the one that must clear the higher bar"*, and
it did not clear it. It also named the m004-degeneracy worry **in advance** and
pre-committed the family and census cells — which is the only reason cell 3's census
exists at all, and the census is where the actual discovery is. Had cells 2–3 been added
after seeing cell 1, they would have been unfalsifiable follow-up rather than sealed
content.

## 6. Honest limits

1. **Length ≤ 10.** The census is complete to that length (241 classes), not beyond. The
   18/13 split is a finite-sample statement about short words; no asymptotic claim is
   made.
2. **Word-level, not isometry-level.** ρ and σ are computed as involutions on cyclic
   LR-words. That is the level GHH's criterion lives at and the level B944 named — but it
   is not the same as computing in Isom(m004) directly. A stabilizer at word level
   realizes symmetries of the bundle; the converse (that every symmetry is visible here)
   is not established by this cell.
3. **Cell 4 is deliberately defused** (§4): no depth is claimed for the symmetry of W.
4. The geometric identifications (ρ ↔ base/S¹ reversal ↔ time reversal; σ ↔ fiber
   orientation flip ↔ chirality) are the standard fibered-3-manifold readings and are
   used as such; they are not re-derived here.

## 7. Files

`PREREGISTRATION.md` (sealed, hash above) · `b945_cells.py` → `results.json` ·
locks `tests/test_b945_l126.py`.

---

**Verdict: OUTCOME INDEPENDENT. L126 closed, negative — the unification is withdrawn for
m004.** The compensation is a better question: the locking is real and generic, and this
object is the exception.
