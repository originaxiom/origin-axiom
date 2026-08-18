# B8068 PREREGISTRATION — is the object's canonical cubic étale algebra the charge field?

**Date:** 2026-08-17 · **Seat:** cc3 · **Gate 5:** no physical identification anywhere in
this arc. Every statement is about `e₆`, `e₈`, `2T`, the exceptional Jordan algebra and a
cubic number field.

---

## THE SEAL, AND ITS HONEST WEAKNESS — READ THIS FIRST

The criterion below was written into the docstring of `build_j2t.py` **before any
structure constant was read**, and the conversation record shows it. **But it was not
committed and pushed before compute**, which is this repository's standard (B959's
`4c3c4775` is the pattern). **This is therefore a weaker seal than the house bar, and it
is labelled as such rather than dressed as the real thing.** A reader who discounts it
accordingly is reading correctly.

What partly compensates: **the criterion is two-sided and both sides were live.** The
"field" branch and the "split" branch had opposite consequences for the programme, and
the discriminant comparison could have come out anything.

---

## THE QUESTION

`2T ⊂ F₄ = Aut(J)` via the principal `sl₂`, so `J^{2T}` is a **Jordan subalgebra**. The
Molien series of `2T` fixes `dim J^{2T} = 3`, at principal degrees `{0, 8, 16}`. A
3-dimensional unital Jordan subalgebra with semisimple elements is a **cubic étale
algebra** — precisely the object by which Kato–Yukie classify rational orbits of pairs of
27s.

> **Which cubic étale algebra is `J^{2T}`?**

The programme owns a cubic: the charge field `K = ℚ[x]/(x³−12x−5)`, `disc K = 6237 =
3⁴·7·11`, totally real, class number one, computed on the **measurement** side of the
cascade. `J^{2T}` is computed on the **representation** side. There is no reason known to
this seat why they should agree.

## DECLARED IN ADVANCE

| outcome | reading |
|---|---|
| `J^{2T}` is a cubic **FIELD** | no primitive idempotents over ℚ ⟹ **no rational rank-1 VEV**; L138 does not fire rationally |
| `J^{2T}` is **SPLIT** (ℚ×ℚ×ℚ) | three rational primitive idempotents; two of them start `E₆ → SU(5)` |
| either way | compare `disc J^{2T}` with `disc K = 6237`. **Agreement is a result. Disagreement is a result. "Close to" is not a result.** |

**Additionally declared:** if `J^{2T}` is totally real it splits over ℝ regardless of what
it does over ℚ, and that must be reported with equal weight rather than buried.

## GATES, fixed before compute

1. the 27 is minuscule — Weyl orbit of `ω₁`, 27 weights, all multiplicity one
2. principal `h`-profile on the 27 matches `V(16) ⊕ V(8) ⊕ V(0)` — known independently
   from `height(ω₁) = 8`
3. the cubic form's support is **45** weight-triples summing to zero, each weight in 5
   (the classical 27-lines / 45-tritangent-planes count)
4. `dim (27)^{2T} = 3` at degrees `{0, 8, 16}` — known independently from Molien
5. **carrier gates:** `e₈` has 240 roots and dimension 248; the ℤ/3-grading by the
   coefficient of `α₇` gives `78 / 81 / 81`; deg-0 splits `72 (E₆) + 6 (A₂)`; deg-1
   splits into three 27-blocks by the coefficient of `α₈`
6. the principal `sl₂` satisfies `[e,f] = h`, `[h,e] = 2e`, `[h,f] = −2f`
7. the interpolated ternary cubic has **residual exactly 0**, and — an independent
   prediction, not an input — **no `a²b`, `a²c` or `abc` term**, because `v₈` and `v₁₆`
   are traceless and distinct `sl₂`-isotypic components are orthogonal

**No verdict line is to be read past a failed gate.**

## WHY e₈ AND NOT e₇

`e₇ ⊃ e₆ ⊕ ℂ` gives the 27 as a graded piece with signs for free, but its grading is
3-step (`−1, 0, +1`), so `[27, 27] = 0` there: **it supplies the module and kills the
cubic.** `e₈ ⊃ e₆ ⊕ sl₃` with `e₈ = (e₆⊕sl₃) ⊕ (27,3) ⊕ (27̄,3̄)` has
`[(27,3),(27,3)] ⊂ (27̄,3̄)`, which is the quadratic adjoint. This was checked, not
assumed — brackets inside a single 27-block vanish identically, exactly as `a ∧ a = 0`
in the `sl₃` factor requires.

## METHOD

`C(x) = ⟨[x, P·x], Q·x⟩` with `P, Q` the two `A₂` root vectors linking the three blocks.
`P` and `Q` commute with `e₆` and the Killing form is invariant, so `C` is an
`E₆`-invariant cubic on the 27; the `E₆`-invariant cubic is unique up to scale, so
`C ∝ det` and **the scale is irrelevant to every question asked here**. The scales of
`v₈` and `v₁₆` are likewise arbitrary — rescaling them is a change of basis in the
algebra and cannot move the field.

## SCOPE, stated in advance

The cubic **form** is computed; the multiplication table is **not**. The algebra is read
off the characteristic polynomial of a generic element. For a cubic étale algebra the
norm form together with the identity determines it — but that is an **inference**, and it
is recorded as one.
