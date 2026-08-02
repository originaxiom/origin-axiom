# B854 — the centralizer of 2T in 𝔢₆ is ABELIAN: u(1)⁴, computed exactly. The su(2)×u(1) claim does not survive.

cc banking seat, 2026-08-02. Mathematics scope; nothing to `CLAIMS.md`; Gate 5 untouched.
**Not preregistered** — this adjudicates an incoming claim by exact computation; its footing is the
verification battery in §2, not a seal.

## 0. What was at stake

An incoming relay called this *"the single most consequential open computation in the programme"*
and, after seven numerical attempts, reported **su(2) × u(1)** — *"the electroweak gauge algebra,
before symmetry breaking"* — from a numerically-obtained bracket table with Killing rank 3.

Reductivity leaves exactly two possibilities for a 4-dimensional centralizer: **u(1)⁴** or
**su(2)⊕u(1)**. This settles it exactly.

> **VERDICT: all six brackets vanish identically. The centralizer is ABELIAN — u(1)⁴.**
> **There is no non-abelian continuous symmetry commuting with the holonomy's finite image inside E₆.**

## 1. The computation

**Exact 𝔢₆ over ℚ**, Chevalley basis, structure constants from the standard bimultiplicative
cocycle. Built and **verified before use**, because a wrong sign silently yields a non-Lie algebra
— which is exactly the failure being diagnosed downstream:

| check | result |
|---|---|
| positive roots / total | **36 / 72** |
| dimension | **78** |
| **Jacobi on 4000 random basis triples** | **PASS** (zero failures) |
| principal triple | `[e,f] = h`, `[h,e] = 2e`, `[h,f] = −2f` all exact |
| hw multiplicities | **{1, 4, 5, 7, 8, 11}** — the E₆ exponents, recovered not assumed |

**The four 2T-invariants**, one each in V₈, V₁₄, V₁₆, V₂₂, built by exact averaging over the 24
unit quaternions of 2T in Sym^n, then mapped into 𝔢₆ by the sl(2)-equivariant identification
`x^{n−k}y^k ↔ ((n−k)!/n!)·ad(f)^k v_n`.

They come out as **Klein's classical forms**: `ΦΨ`, `t·ΦΨ`, `(ΦΨ)²`, `t·(ΦΨ)²` — reproducing 2T's
invariant ring (the E₆ singularity, generators in degrees 6, 8, 12).

## 2. The controls, which are what make the vanishing mean something

**A vanishing result is worthless without a control that could have made it nonzero.**

| control | result |
|---|---|
| **random elements of the same blocks** | **NONZERO 5/5 on every one of the six pairs** |
| rank of the four invariants | **4** — independent, none degenerate |
| block placement (`ad(e)`-annihilation depth) | 9, 14, 17, 22 — matching the y-degrees of the forms exactly |

The block depths are a real check, not a formality: `t` carries a factor of x, so x₁₄ and x₂₂ have
**no pure-y term**, which is precisely why they die one step early.

**And the isomorphism type is conjugation-invariant**, so the answer does not depend on which
conjugate of 2T ⊂ SL(2) the Klein forms correspond to.

## 3. Three independent confirmations of dim = 4

1. **Burnside average** over 2T of the trivial character across the blocks → 4.
2. **Full SL(2,3) character table**: `78 = 4·(triv) + 7·(ω) + 7·(ω̄) + 20·(3-dim)` = 4+7+7+60 = 78,
   with **all three 2-dimensional (spin) irreps at multiplicity zero** — as they must be, since −I
   acts trivially on the adjoint and the action factors through A₄. The arithmetic produces that on
   its own.
3. **Klein invariant theory**: true invariants of 2T occur in degrees 8, 14, 16, 22 within our
   blocks, one each — the invariant ring's own structure.

Cross-check: `dim Cent(ℤ/3) = 24` from the A₄ decomposition, and **1+3+3+5+5+7 = 24** from counting
weights ≡ 0 mod 3 across the blocks. Agreement.

## 4. A ℤ/2-grading, exact and E₆-free — and the reduction it buys

Computing all 24 transvectants of the explicit invariants: **odd order vanishes, even order does
not, without exception.** Hence

> **C₀ = ⟨x₈, x₁₆⟩, C₁ = ⟨x₁₄, x₂₂⟩**, with [C₀,C₀] ⊆ C₀, [C₁,C₁] ⊆ C₀, [C₀,C₁] ⊆ C₁.

For sl(2)⊕u(1) under this grading C₀ = ⟨h, z⟩ is abelian and C₁ = ⟨e, f⟩ with [e,f] = h ≠ 0. So the
whole question collapses to **one bracket, [x₁₄, x₂₂]** — not a 4×4×4 table. That reduction is why
seven numerical attempts were fighting a harder problem than the one they had.

**[x₁₄, x₂₂] = 0.** Exactly.

## 5. Why the competing computation reported su(2) × u(1)

**There are two different Killing forms and they answer different questions.**

| | value | meaning |
|---|---|---|
| **K_𝔢₆ restricted to C** | diagonal, **rank 4**, det ≈ 2.734×10⁵⁰ | nondegenerate — *exactly what a torus gives* |
| **K_C, the Killing form OF C** | **identically 0, rank 0** | **abelian** |

The form that distinguishes u(1)⁴ from su(2)⊕u(1) is **K_C**. A numerical rank-4 restriction with
one small eigenvalue reads as *"rank 3 plus a zero mode"* — precisely the signature su(2)⊕u(1)
requires. **The reported result is the restriction, misread as the intrinsic form.**

That diagnosis is corroborated by three independent defects in the reported table, each fatal alone:

- **centre = 0.** su(2)⊕u(1) requires a 1-dimensional centre, and **no 4-dimensional semisimple Lie
  algebra exists**, so a 4-dim reductive algebra must have one.
- **Jacobi violated at 3.5% relative** (4.99×10⁻³ against a largest constant of 0.141).
- **su(2) weight test**: a₁ should equal −a₂; the ratio is **0.175**, off by 5.7×.

And the relay's own reported residuals (0.06–0.98 against a 0.14 signal) had **already
disqualified** the numbers the verdict was read from. `[C,C] ⊆ C` is exact — invariants bracket to
invariants — so every residual outside C is pure error.

## 6. Consequence, stated without extension

**No non-abelian gauge algebra arises as the centralizer of the object's finite holonomy image
inside the E₆ its arithmetic selects.** No W bosons, no SU(2) to break, no electroweak reading from
this route.

**Related, checked, and separate:** the conformal-embedding route ((E₆)₁ ⊃ (A₂)₂ × (G₂)₁ ⊃
SU(3)₂ × SU(2)₃ × "U(1)", B254) has **every central charge exactly right** — 16/5 + 14/5 = 6 and
9/5 + 1 = 14/5. But **G₂'s maximal subalgebra is A₁ × A₁ at indices (1,3)**: the c = 1 factor is
**SU(2) at level 1**, the self-dual boson whose currents enhance U(1) to SU(2). Since
`c((A₁)₁) = c(U(1)) = 1` exactly, **central-charge matching cannot tell them apart** — so as groups
the chain delivers **SU(3) × SU(2) × SU(2)**, not SU(3) × SU(2) × U(1). Recorded here; not
adjudicated as an arc.

## 7. What this does NOT do

- **Does not close the E₆ chain.** It closes one route through it — the classical centralizer.
- **Does not refute the conformal embedding.** §6 flags a substitution in how it is *labelled*.
- **Does not test other embeddings.** 2T enters via the **principal** SL(2); a non-principal
  embedding has a different centralizer, and none was computed.
- **Nothing to `CLAIMS.md`.**

## Carried forward

1. **Non-principal embeddings of 2T in E₆** — the one honest way this route could still yield a
   non-abelian centralizer.
2. **The levels (2, 3) are forced by the conformal chain**, and in heterotic-type constructions
   affine levels fix tree-level coupling ratios (`k_i g_i²` constant), giving `α₃/α₂ = k₂/k₃ = 3/2`
   with no fitted input. **That is DOF-positive in shape** — but it requires the 2d CFT to be a
   heterotic worldsheet theory, which the programme has never claimed, and **k₁ is undetermined**;
   fitting it would be DOF-0.

`tests/test_b854_centralizer.py`
