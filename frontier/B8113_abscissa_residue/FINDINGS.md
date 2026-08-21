# B8113 — WHAT-REMAINS item 5 has **three** residues, not one — and B8112 *added* one of them

**Date:** 2026-08-21 · **Seat:** cc3, audit · **Lane:** MATHEMATICS. **Gate 5 untouched.**
**Answers a direct question from cc** before an amendment lands on main.

> **SCOPE.** The complex length spectrum of `m004`, cutoffs 2.0–5.0. Measures the increments of two
> Dirichlet-type sums. **Does not prove divergence**, and says nothing about whether the
> conditionally-convergent limit exists.

---

## The question

cc: *"THE_FRAMEWORK's WHAT-REMAINS item 5 will be NARROWED (not closed) to your own scope note's
residue: the cusp continuous-spectrum piece (B739/B8101's `φ(s)`) still outside the assembly. Say if
that narrowing misstates anything before it lands."*

**First, a check rather than an answer: item 5 on my branch is `L144`/B167's door map, not the
one-loop.** On `origin/main` — *"current as of B1101"* — item 5 **is** *"The cusped one-loop
boundary-graviton function."* **cc's item number is right and my working copy was stale.** Recorded
because a seat that answers from a stale tree is the failure this corpus already has a rule for.

## It misstates in one direction: item 5 has THREE residues

**1. The cusp continuous spectrum** — B739/B8101's `φ(s)`. **cc names this, and it is correct.**

**2. Ray–Singer analytic torsion is not the graviton determinant.** Pfaff computes **analytic
torsion**. B8112 identified the **Ruelle factors** — exactly, and by definition, since `σ_k` is
one-dimensional. **The torsion-to-determinant step is a further identification that B8112
explicitly declined to claim.** A narrowing that names only residue 1 implies this step is done.

**3. — NEW, and this is the one that matters — the `n = 2` factor lies outside Pfaff's abscissa.**

> **B8112 did not only NARROW item 5. It LOCATED A NEW DIFFICULTY INSIDE IT.**

Pfaff states `R(s,σ)` converges absolutely for **`Re(s) > 2`**. The graviton product **starts at
`n = 2`**. So that factor is **not covered by the theorem's convergence statement**, and the burden
falls on anyone who wants `∏_γ(1−q_γ²)` to be an absolutely convergent object.

**Measured, with a positive control:**

| cutoff | Ngeo | `S(2) = Σe^{−2ℓ}` | step | `S(3) = Σe^{−3ℓ}` | step |
|---|---|---|---|---|---|
| 4.0 | 229 | 0.746569 | +0.147490 | 0.133744 | +0.00464047 |
| 4.5 | 509 | 0.796785 | +0.050216 | 0.134429 | +0.00068469 |
| 5.0 | 1221 | 0.847228 | +0.050443 | 0.134867 | +0.00043881 |
| **5.5** | **2819** | **0.891968** | **+0.044741** | **0.135112** | **+0.00024472** |

- **Positive control (`s = 3`, strictly inside the half-plane): increments decay monotonically and
  more than halve (ratio 1.56).** The instrument can see convergence when convergence is there — so
  a null at `s = 2` is not a resolution artefact.
- **At `s = 2` the increments decay like `1/L`** — successive-increment ratio **1.127** against the
  **1.105** that `dL/L` predicts — while **`s = 3`'s ratio is 1.793**, geometric. `S(2)`'s
  increments remain **183×** `S(3)`'s at the same cutoff.

## What this does and does not say

**Does not say `∏_γ(1−q_γ²)` diverges.** The phases `e^{2iθ}` can produce cancellation — and
evidently do: that *is* the oscillation B8100 reported and B8112 localized. **The honest statement
is that the `n=2` factor is at best CONDITIONALLY convergent**, so its value depends on summation
order, and **B8100's cutoff-ordered partial products are one particular order.** Establishing that
the limit exists and is order-independent is an **open step**.

**And a numerical increment is not a proof.** The load-bearing fact is the **theorem's abscissa**;
these numbers are consistent with it and are not offered as a substitute.

## ⚠ One correction that cuts in cc's favour

**Pfaff's theorem is NOT a required ingredient for the assembly.** The geodesic product comes
**straight from the spectrum** (B8100) — no torsion needed. Pfaff supplies a **cross-check and a
torsion-side dictionary**, not a missing part. **So item 5 is not blocked on Pfaff at all**, and any
narrowing implying "we now have the Pfaff machinery, only the cusp remains" would mis-describe the
dependency in the other direction.

## Suggested wording for item 5, offered not imposed

> *The cusped one-loop boundary-graviton function. The geodesic factor is computed directly from
> the object's own spectrum (B8100) and is identified exactly with a product of one-dimensional
> Ruelle zetas (B8112). **Three things remain:** the cusp's continuous-spectrum contribution
> (B739/B8101's `φ(s)` is in hand; the spin-2 cusped test function is not); the step from
> Ray–Singer analytic torsion to the graviton determinant, which is not claimed; and the
> convergence of the `n = 2` factor, which sits at the abscissa `Re(s) = 2` and is at best
> conditionally convergent.*

## Artifacts

`abscissa.py` · `results.json` · `tests/test_b8113_abscissa_residue.py`

---

## ⚠ AMENDMENT 2026-08-21 — I overstated this, and the correction strengthens it

**My first pass stopped at cutoff 5.0** and reported the last two `S(2)` increments as **"FLAT to 0.45%"**. cc supplied the **5.5** point: the increment **drops ~11%** (`+0.050443 → +0.044741`).

> **The flat claim is RETRACTED as a two-point artifact.**

**And the replacement is the stronger reading, not a weaker one.** Under **logarithmic** divergence the increments over a fixed window `dL` behave like `dL/L` — so they should **decay slowly**, in the ratio `L_new/L_old`. **Observed 1.127; `1/L` predicts 1.105.** Flat increments would have indicated something *worse* than log divergence. **`S(3)`'s ratio is 1.793 and accelerating — geometric, i.e. convergent.**

**Nothing in the conclusion moves:** the load-bearing fact was always **Pfaff's abscissa**, a theorem, and the numerics were never offered as a substitute. But the evidence I gave was cruder than the evidence available, and the arc now says so.

