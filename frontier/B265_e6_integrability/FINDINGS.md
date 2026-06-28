# B265 — integrability + Zariski-density: genuine E₆-irreducible flat connections on the figure-eight exist

**Status: banked observation (frontier). FIREWALLED — geometry / rep theory of flat connections, NOT physics.
Nothing to `CLAIMS.md`.** The integrability rung of chat-1's program, following B264. `e6_integrability.py` (pyenv;
imports B264's verified Fox machinery) + `t41_e6_generation_sage.py` (sage-python, the density computation).

## The question
B264 found the tangent space to the E₆ character variety at the principal-composed geometric rep is
`dim H¹(Ad ρ_prin) = 6 = rank(E₆)`, graded by the E₆ exponents `{1,4,5,7,8,11}`. This rung asks the two questions
that turn "the tangent space is big" into "actual E₆-irreducible reps exist":
1. do those infinitesimal deformations **integrate** to genuine representations?
2. is the generic deformation **E₆-Zariski-dense** — a true E₆-irreducible flat connection — or trapped in a
   subgroup (F₄, a Levi, …)?

## (1) Zariski-density — the decisive computation (Sage, exact over ℚ)
In `e₆`, build the principal `sl(2)` (`e=Σeᵢ`, principal nilpotent) and the highest-weight vector of each
exponent-graded module, then compute the dimension of the subalgebra they generate:

| deformation direction | `dim ⟨principal sl(2), v⟩` | verdict |
|---|---|---|
| exponent **4, 8** (E₆∖F₄) | **78 = dim e₆** | **E₆-Zariski-dense** |
| exponent **5, 7, 11** (F₄) | **52 = dim f₄** | trapped in F₄ |
| principal `sl(2)` alone (exp 1) | 3 | the SL(2) A-polynomial curve |

So the 6-dimensional tangent space splits **exactly** by the F₄/E₆ structure: the `{4,8}` directions (the
`e₆/f₄ = 26` coset) generate all of `e₆`; the F₄ directions stay in F₄. A deformation with a `{4,8}` component is
genuinely E₆-irreducible. (Underlying Lie fact: the only subalgebras of `e₆` containing the principal `sl(2)` are
`sl(2)`, `f₄`, `e₆` — Dynkin; the `{4,8}` directions leave `f₄`, forcing closure `= e₆`.)

## (2) Integrability — obstruction space + smoothness
The obstruction to integrating an `H¹` class lives in `H²`. Computed exactly (Fox complex, exact Riley rep):
`dim H²(π₁(4₁), Sym^{2k}) = 1` for all `k` — consistent with the knot complement's Euler characteristic
(`χ=0`, `H⁰=0` for `k≥1` ⟹ `H²=H¹`). So the obstruction space is **6-dimensional, nonzero** — integrability is *not*
automatic. But the discrete-faithful (geometric) holonomy is a **smooth point** of the G-character variety of a
1-cusped hyperbolic 3-manifold, of dimension `rank(G)·#cusps = 6` (Thurston for SL(2); the principal-composed
higher-rank version — Menal-Ferrer–Porti / higher-Teichmüller). Smoothness ⟹ the cup-product obstruction
`H¹×H¹→H²` **vanishes** at this rep despite `H²≠0`. Hence the rank-6 family consists of **actual** representations.

## Conclusion
Combining (1)+(2): the `{4,8}` deformations integrate to a positive-dimensional family of **E₆-Zariski-dense**
representations of `π₁(4₁)`.

> **Genuine E₆-irreducible flat connections on the figure-eight exist** (near `ρ_prin`).

This is the strongest pro-bridge result in the program: chat-1's hope confirmed at the **actual-representation**
level, not merely infinitesimal — `T[4₁;E₆]` has a substantive E₆-irreducible locus to be about, not a relabeling.

## Honest guardrails (verify-don't-trust)
1. **Local statement.** "Exist near `ρ_prin`" — a neighborhood of the geometric rep (the right place for the 3d-3d
   story). We do not classify the global E₆ character variety.
2. **Existence ≠ SM physics.** The input-E₆ (chosen 6d type) vs output-McKay-E₆ (trace field) selection is still a
   conjecture; the 4d-lift / chirality / scale walls (B259) stand untouched.
3. **Consistent with the SL(n) ladder** `dim = rank`: SL(2)→1, SL(3)→2 (B71), …, E₆→6. E₆ is the exceptional
   capstone; this and B264 establish its tangent dimension and the genuine E₆-density of the deformations.

Anchors: B264 (tangent dim = rank), B71/B89 (SL(3)/SL(4) char varieties), B260 (Coulomb branch = char variety),
B259 (the wall map). Lit: Thurston (`H¹(ad)=1`, smoothness); Menal-Ferrer–Porti 2012 (twisted cohomology / local
coordinates, cusped hyperbolic); Kostant (principal `sl(2)`, exponents); Dynkin (subalgebras containing the
principal `sl(2)`); Dimofte–Gaiotto–Gukov (3d-3d type G).

## Correction (2026-06-28 adversarial audit / B272)
The headline "genuine E₆-irreducible flat connections EXIST" is **stronger than what is proven here** and is
hereby softened. What is solid: (i) `dim H¹(Ad ρ_prin)=6=rank` (MFP, independently re-confirmed 3 ways); (ii) the
`{4,8}` directions are **E₆-Zariski-dense** (pure Lie theory, solid). What is **not** separately established: the
**integrability** of the `{4,8}` directions as E₆-reps. B270 computes the cup-product obstruction only for the
`SL(2)/Sym²` (exponent-1) block; for `{4,8}` the obstruction is the `e₆`-bracket-coupled cup product
`H¹×H¹→H²(e₆)`, which is **not computed**. The cusp mechanism (`dim H¹=#cusps`) and the general "geometric rep is a
smooth point" principle make existence **strongly expected**, but the cited Menal-Ferrer–Porti theorem is the
*dimension count* (`dim H¹(Sym^{2k})=#cusps`), not an E₆ *smoothness/integrability* theorem. **Honest status:**
E₆-irreducible flat connections are *expected to exist* (rank-dimensional tangent space + Zariski-dense + cusp
mechanism), **conditional on** integrability of the `{4,8}` directions — established for exponent 1, open for
`{4,8}` (the residual computation: the `e₆` bracket-coupled obstruction). The verdict "they EXIST" should read
"they are expected to exist; the tangent-level structure is established."
