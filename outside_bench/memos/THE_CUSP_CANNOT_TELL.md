# Memo 213 — L71: THE PERIPHERAL SLOPE IS THE SAME IN EVERY BLOCK, AND THAT IS A THEOREM ABOUT THE CUSP, NOT AN ANSWER

**Seal:** `outside_bench/seals/L71_CUSP_SLOPE_PREREG.md`, sha256
`788faf6fd92a0674109f38307cdf1725bb9f28c298e533956e181d47fc19ad31`, committed before the
certificate was written, **with the m = 1, 2 prototype disclosed inside it.**
**Certificate:** `outside_bench/certificates/l71_cusp_slope.py` ·
**Output:** `outside_bench/outputs/l71_cusp_slope.txt`
**Outcomes: CELL 1 = A · CELL 2 = B · CELL 3 = A.** Controls C1–C4 all pass.

---

## 0. The question, and why the instrument looked right

`docs/OPEN_LEADS.md` **L71 — what ARE the θ-odd deformations?** B270 banked that at the
SL(2,ℂ) foundation *"deformations are cusp deformations."* `P2W5-L72` computed the wall:
*"the θ-odd directions m = [4, 8] are **NOT** in the image of the SL(2,ℂ) deformation."*

So each block carries one deformation direction (`h¹ = 1`), and for m ≥ 2 it is **not**
induced from the geometric one. The obvious handle: **what does it do to the cusp?** Each
block has `dim H¹(T²; Sym^{2m}) = 2`, and the peripheral image is a line in a plane — a
slope. Define `slope_m := [ξ(λ)] / [ξ(a)]` in `V / im(ρ_V(a) − I) ≅ ℂ`.

## 1. CELL 1 — the slope is the same in every block. OUTCOME A.

Exactly, over ℚ(ζ₆), no floating point anywhere:

> **`slope_m = −2√−3` for every m from 1 to 12** — including both θ-odd exponents
> **m = 4 and m = 8**, all six E₆ exponents, and the six non-exponents.

`−2√−3` is the **cusp shape of the figure-eight**. Controls: the relator is the identity in
every block; `ρ(λ)` commutes with `ρ(a)` in every block; at the six E₆ exponents
`h⁰ = 0, h¹ = 1, periph_inv = 1` — matching `P2W5-L72`'s exact ℚ(ζ₆) table; and SnapPy's
cusp shape agrees in magnitude to **2.220e−15** (the sign differs, which the seal fenced in
advance as SnapPy's own orientation convention).

**Read alone, that is a headline.** It is also worthless, and the next cell is why.

## 2. CELL 2 — the cusp forces it. OUTCOME B.

The seal asked whether the cusp's own cocycle condition already pins the ratio, because if
it does, CELL 1 says nothing about the knot. **It does.** For every m from 1 to 12, the
solution space of `(ρ(a)−I)ξ(λ) = (ρ(λ)−I)ξ(a)` — dimension 4, 6, 8, …, 26 — contains **no
solution whose ratio differs from −2√−3.**

**Post-hoc mechanism, computed and not preregistered.** `ρ(a) = exp(N)` and
`ρ(λ) = exp(τN)` with the **same** nilpotent N. Write `exp(N) − I = N·φ(N)` with
`φ(N) = I + N/2 + N²/6 + …` unipotent. The cusp condition becomes

> `N·( φ(N)ξ(λ) − τ·φ(τN)ξ(a) ) = 0`,  so the bracket lies in `ker N`.

Apply `f`, the functional defining the coker. Two facts, checked exactly for m = 1…6:
**`f ∘ N = 0`**, so `f(φ(N)v) = f(v)` for every v; and **`f` vanishes on `ker N`**. Hence

> **`f(ξ(λ)) = τ·f(ξ(a))` identically — for any cocycle, on any manifold with this cusp.**

## 3. What this settles

> **The peripheral coker-slope is blind by construction.** It reads the cusp shape and
> nothing else. It cannot distinguish a θ-odd deformation from the geometric one at any m,
> and the constancy in CELL 1 is not a property of the figure-eight, of E₆, or of the
> θ-grading. **L71 is not answered, and this route cannot answer it.**

CELL 3 confirms the same thing from the other side. The statistic **does** move with the
representation — the complex-conjugate rep gives `+2√−3` at m = 1, 4, 8 — but it moves
*exactly as the cusp shape moves*. Passing MB12 shows the instrument is not constant; it
does not show the instrument is informative. **Memo 164 again: control passing is not
instrument working.**

## 4. The part worth keeping

> **INTERPRETIVE.** Had CELL 2 not been in the seal, this memo would have banked *"every
> Sym^{2m} deformation moves the cusp by the same shape — including the chiral ones"* as a
> theorem about the object. It is a theorem about ℤ² with a unipotent action, true for every
> knot and every block, and it would have been wrong in exactly the way this bench has been
> wrong before: **a real computation, correctly done, whose content was already in the
> hypotheses.**
>
> The seal's CELL 2 was written because the m = 1, 2 agreement looked *too* clean. That
> instinct is the reusable part, and it is now a rule.

**Rule added:** when a statistic comes out identical across every case, the next cell asks
whether the statistic *could* have differed — **before** the constancy is written down as a
finding.

## 5. What L71 still needs

The peripheral coker is the wrong invariant because it factors through the cusp. A
candidate that does not:

- **the full peripheral class**, not its coker shadow — `H¹(T²; Sym^{2m})` is 2-dimensional
  and the coker map crushes it to one number; the *second* coordinate is where the block
  dependence, if any, survives;
- **the cup-product / symplectic pairing** on the peripheral space — B270 computed the cup
  product at m = 1; its analogue on Sym^{2m} is not in the corpus by this bench's search;
- **the Zariski closure per block** — B576 did this for the E₆-valued deformation and got
  the answer at the level of the *algebra*; the geometric question L71 asks is about the
  *representation*, and those are not the same question.

**None of these is claimed to work.** They are named because this memo closed a route and
owes its successor.

## 6. Fences

The computation is exact over ℚ(ζ₆); the only floating-point number anywhere is SnapPy's
cusp shape in control C4, used for a magnitude comparison. The disclosure in the seal
stands: **m = 1 and m = 2 were computed in a scratch prototype before the seal was written,
and the CELL 1 prior was declared knowing them.** Nothing beyond m = 2 was known when the
seal was committed, and CELL 2's outcome — the one that decides the memo — had no prior
declared and went against the direction the author expected.
