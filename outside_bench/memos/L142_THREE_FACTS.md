# 205 — L142 ANSWERED: THREE FACTS, THE AGREEMENT IS OF OUTPUTS — and the successor question now has an answer

**Date** 2026-09-12 · **Lane** outside bench · **Branch** `<seat>/outside-bench`
**Certificate** `certificates/l142_three_sites.py` · **Output** `outputs/l142_three_sites_out.txt`
**Seal** `seals/L142_THREE_SITES_PREREG.md`, sha256
`8226e745503a63b0115e612800c19ec14893e0d7adad4a9f1b3357f387d36d87` — **sealed before the certificate
was written**
**CELL 1/2/3 = B/B/B · all controls pass · Gate 5 untouched**

**The cell** is `docs/OPEN_LEADS.md` **L142**, registered 2026-08-08 (its occasion was B969's §5
question; **B969 itself is a fully executed arc and nothing here says otherwise**). **L142 — the
cell, not the arc — had not been executed before this certificate.** Evidence, since the standing
rule forbids an unrun claim without one: `already_banked.py` on *"three sites one field morphism
between pencils or agreement of outputs"*, *"joint kernel of x14 x22 on the 27 three dimensional
subspace"*, *"bridge between the D4 locus and the 77-bearing charges disjoint loci"* returns no arc
executing it; `OPEN_LEADS.md` still carries it as a lead with its test named; and its 2026-08-12
amendment reads *"'A separate cell' is a **not-run**, not an obstruction; the label propagated
without its reason."* Its text:

> *"**THREE SITES, ONE FIELD: one theorem or three facts?** … **Not adjudicable by opinion.** The
> discriminating test, named: **exhibit a morphism carrying one pencil to another, or show the
> agreement is only of outputs.**"*

---

## 1. The trap, rejected before the run rather than after

The seal names two tests and refuses both **before** computing:

* **`GL₂(ℚ)`-equivalence of the cubics is VACUOUS.** Over ℚ, `PGL₂` is 3-transitive on `ℙ¹` and an
  irreducible binary cubic's root-triple is Galois-stable, so any two irreducible binary cubics with
  isomorphic root fields are `PGL₂(ℚ)`-equivalent up to scalar. **The test cannot fail — MB12.**
* **`GL₂(ℤ)`-equivalence would measure basis conventions**, not mathematics: the cubics are read off
  matrices in a chosen basis, and rescaling the pencil parameter changes the integral class. B866
  records exactly such a rescaling between two constructions of μ (*"theirs(13t) = 2197·mine(t)"*).

So the morphism question is asked **directly**, in two layers.

## 2. CELL 1 — across representations, no morphism can exist

μ's site is a pencil on the **adjoint 78**; B969's compact-kernel site and this bench's
`(x₁₄,x₂₂)` site are on the **matter 27**. These are **inequivalent irreducible `e₆`-representations**,
so `Hom_{e₆}(27, 78) = 0` **by Schur**.

> **Closed by a theorem, not by a failed search.**

## 3. CELL 2 — within the 27, the two pencils are not conjugate

    kernel_0      measured-plane vs orphan-plane : (0, 3)
    charpoly_0                                   : differ
    kernel_1                                     : (0, 3)
    charpoly_1                                   : differ
    rank_product                                 : (27, 24)

A conjugation invariant **differs**, so **no `T ∈ GL(27)` carries one pencil to the other** —
proved, not searched for. With the positive control firing (a genuinely conjugated pair is reported
conjugate) and the bite control firing (a genuinely non-conjugate pair is reported not).

## 4. CELL 3 — and the agreement is real: six sites, one field

| site | cubic | generates K |
|---|---|---|
| `x₈` on the compact kernel (B969, recomputed) | `x³ − 10063872x − 9710862336` | **True** |
| `x₁₆` on the compact kernel (recomputed) | `2197x³ − 6963104474726400x + …` | **True** |
| `(x₁₄,x₂₂)` branch cubic 1 (memo 201, new site) | `2771822592000x³ + …` | **True** |
| `(x₁₄,x₂₂)` branch cubic 2 (new site) | `1686085632000x³ − …` | **True** |
| μ itself — **positive control** | `500716339200x³ − …` | **True** |
| B866's adjoint-pencil μ — **C4 reproduction** | `500716339200x³ − 159667200x² − 28224x + 1` | **True** |
| **BITE CONTROL** — unrelated resolvent-77 cubic | `x³ − 6x² − 14x + 18` | **False** |

Every cubic irreducible over ℚ with resolvent squarefree part **77**. The bite control fires, so
*"generates K"* is an instrument that can say no.

**C6, added during the run and verified rather than assumed:** K is presented by its **smallest**
model `x³ − 12x − 5`, and μ is shown to factor over it as `[1,2]` — a root there — so both models
generate **the same field**.

## 5. The answer

> **L142: THREE FACTS. THE AGREEMENT IS OF OUTPUTS.**

## 6. And the successor question, which the seal required be stated rather than buried, now has an answer

The seal fixed in advance that a `B/B/B` result does **not** exclude a **common upstream cause**,
and that the successor is *"not 'is there a morphism between the sites' (no) but **what property of
the charge space makes every construction on it return the same cubic field**."*

**Memo 204 answers it.** That cubic **is the object's trialitarian `L`** — the cubic étale algebra
attached to its `D₄` by `π∗ : H¹(F, G₀⋊S₃) → H¹(F, S₃)`, verified by exhibiting a degree-3 field in
the commutant of the 28 acting on the 48. `L` is an invariant of **the whole structure**, not of any
construction on it.

> **So "three facts" is exactly right about morphisms and would be misleading as a statement about
> cause. There is no map between the sites, and there is a common origin — and that origin is the
> thing that makes the object ⁶D₄.**

Every construction on the charge space returns K because **K is the charge space's own trialitarian
invariant**, and each site is a different way of reading it off.

## 7. What this does not do

It does not prove that **no** relation of any kind exists between the sites — only that **no morphism
of the two named kinds** does. It produces no value, ratio or prediction. It does not bear on B882
beyond what memo 204 already settled.

## 8. Three instrument failures, recorded because they were all in the CONTROLS

This certificate stalled **three times**, and not once in a cell:

1. **The field test** presented K as `ℚ[L]/(μ)`, whose coefficients run to ~5×10¹¹; factoring over
   that number field did not terminate. Fixed by the smallest model, **with the equality verified**.
2. **The C2 positive control** inverted a dense random 27×27 integer matrix — enormous rational
   entries.
3. **Its unimodular replacement** kept integer entries but they still grew enough to stall the exact
   charpolys.

Fixed by a **permutation** conjugator: genuinely changes the matrices, preserves every conjugation
invariant, and its entries **cannot grow** — with assertions that `T·Tᵀ = I` and that the permutation
actually moves something, so the cheaper control is not a weaker one.

> **The controls cost more than the cells, twice over.** That is a different failure mode from this
> session's reading errors (#21–#23): the mathematics was reachable throughout and the **encoding**
> was not. Cheap to fix once seen, and worth seeing.

*Gate 5 untouched — no measured value is used or named. Nothing promotes to `CLAIMS.md`. One
registered cell, open since 2026-08-08, is closed.*
