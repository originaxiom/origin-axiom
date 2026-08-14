# §6–§8 — DRAFT v1 (the algebra, compressed)

*These three sections compress `SKELETON.md`'s Theorems A–E. The full formal statements,
their per-clause locks, and the module-level precursors are cited rather than reproduced:
the algebra is the **consequence** in this paper, not the headline.*

---

## §6. The frame

The construction of §5 delivers an exceptional Lie algebra together with a
distinguished abelian subalgebra. Both are canonical.

Write `𝔢₆` for the Chevalley algebra of type `E₆` over `ℚ`. Inside it sits

```
        C = ⟨ x₈ , x₁₄ , x₁₆ , x₂₂ ⟩,
```

the span of the four **binary-tetrahedral invariants** under the principal
`sl(2)` — Klein forms of degrees `8, 14, 16, 22`, which are twice the exponents
`4, 7, 8, 11`.

> **Proposition 6.1.** `C` is abelian, and its `z`-closure is `u(1)⁴`. The four
> Klein forms are the **complete** list of `2T`-invariants in `𝔢₆` under the
> principal `sl(2)`. *(Theorem A(i); B854; `tests/test_b854_centralizer.py`.)*

`C` is therefore not a basis choice. It is what the entrance of §5 hands over.

### 6.1 The charge cubic

The pencil `ad(x₈ + t·x₁₆)` has a determinant that factors, and its cubic factor
`μ` governs everything in §7.

> **Proposition 6.2.** `μ` is irreducible over `ℚ` with `S₃` Galois group and
> three real roots, and the two pencil determinants are exact powers of it over
> `ℚ`, up to nonzero rational constants:
> ```
>        det₃₆  ≐  μ¹²,        det₁₂  ≐  μ⁴.
> ```
> Write `K = ℚ[ρ]/μ`.
> *(Theorem A(ii); B866; `tests/test_b866_charge_cubic.py`.)*

**`K` in reduced form.** `μ` arrives from a `48×48` minor with twelve-digit
coefficients. It is worth recording that the field it defines is small:

```
        K ≅ ℚ[x]/(x³ − 12x − 5),        disc K = 6237 = 3⁴·7·11,
        monogenic (index 1),            class number h = 1,
        totally real,                   unit rank 2.
```

The squarefree part of the discriminant is `7·11 = 77`, so the quadratic
resolvent of the `S₃` closure is `ℚ(√77)` — recovering, from the reduced model in
one line, the resolvent already banked at C28. Only `3, 7, 11` ramify;
`13, 17, 19` are inert; `2, 5` and the value primes `953, 1129, 421493` are
partially split with exactly one degree-one place each.

**A correction to the record, since the paper would otherwise inherit it.** The
corpus records the resolvent `77` alongside a companion clause — that the golden
`5` "enters by ramification". The first is a fact about `K`; **the second is
not**. `disc(μ) = 2³²·3¹⁰·5²·7³·11·13⁶` does contain a `5`, but a ramified prime
must divide the field discriminant, and `5 ∤ 6237`. In `K` the prime `5` is
**unramified**, with the same splitting shape `f = [1,2]` as the value primes; it
is unramified in `ℚ(√77)` and hence in the whole `S₃` closure. The `5` in
`disc(μ)` — like the `13⁶`, for `13` is inert — is carried by the **integral
model** `ℤ[t]/μ`, which is non-maximal there. It is a property of how the pencil
was normalised, not arithmetic of the field. *(The support-level statement of C28
is unaffected; only the word "ramification" is.)*

*(Every clause above — the reduced model, `h = 1`, the splitting census, and this
correction — is recomputed by `verify/check_charge_field.py`, which exhibits a
generator for **each** prime ideal of norm below the Minkowski bound. Note that
`h = 1` matters downstream only as a negative: no class-group obstruction can
arise, because there is no class group.)*

---

## §7. The cascade

Three theorems carry `𝔢₆` to `su(3) ⊕ su(2) ⊕ u(1)³`. Each is a statement about
**successive centralizers of the charges of §6** — no new object is introduced.

### 7.1 First measurement

> **Theorem 7.1 (FMT).** On the plane `⟨x₈, x₁₆⟩` the centralizer dimension
> stratifies as `12` (generic in the torus), `30` (generic in the plane), and
> **exactly three lines at `46`**. The three lines are the `S₃`-Galois orbit of
> the roots of `μ`. For each such line `Kᵢ`, `z(Kᵢ) ≅ so(10) ⊕ u(1)`, while
> `z(plane) = so(8) ⊕ u(1)²`.
>
> Moreover `𝔢₆ = (so(8)⊕u(1)²) ⊕ V₁ ⊕ V₂ ⊕ V₃` with `dim Vᵢ = 16`, obeying the
> cyclic law `[Vᵢ, Vⱼ] = V_k`; and each `𝔢₆/Kᵢ ≅ 16 ⊕ 16̄` as an
> `so(10)⊕u(1)`-module.
>
> *(Theorem A(ii)–(v); B866, B872, B875, B877.)*

The three `so(10)⊕u(1)` walls are **Galois conjugates of one another** — they are
one object seen three ways, not three coincidences.

### 7.2 The frame is the magic square

> **Theorem 7.2.** The algebra built from split octonions and split complexes by
> the Freudenthal–Tits construction satisfies the Jacobi identity on all `76,076`
> unordered basis triples exactly, has Cartan matrix `E₆`, and admits an explicit
> isomorphism `φ` onto the Chevalley `𝔢₆` verified on all **`3,003` basis pairs**
> — **zero discrepancies** — with `det φ = −2/3`.
>
> *(Theorem B; B904; `tests/test_b904_bs.py`.)*

So the tiling of §7.1 **is** the `(𝕆, ℂ)` magic-square algebra by explicit
structure constants, not merely by module-level signature. **This identification
is also the paper's own ceiling**, and §9 returns to it: everything derivable at
this layer is standard exceptional-algebra theory.

### 7.3 Second measurement

> **Theorem 7.3 (SMT).** Over `K`, on the block-12 matter pencil, the wall point
> `y*` satisfies `dim z(x₁, y*) = 14`, with derived algebra of dimension `11` and
> centre `≥ 3`, whence
> ```
>            z(x₁, y*)  =  su(3) ⊕ su(2) ⊕ u(1)³   exactly.
> ```
> The within-`C` centralizer ladder is `{78, 46, 30, 18, 14, 12}`: the dimension
> `26` of `su(5) ⊕ u(1)` **is not attained** — the second measurement skips it.
>
> *(Theorem C(i)–(iii); B892; `tests/test_b892_smt.py`.)*

Two features are worth isolating. **The landing is exact**, not approximate: the
dimension is bounded below by construction and above by a tower prime.
**The skip is a fact about the ladder**, not a modelling decision — `26` simply
does not occur among the centralizer dimensions these charges produce.

---

## §8. The real form and the involution

The cascade above is over `ℚ` and `K`. Which real form of `E₆` supports it is
determined, not chosen.

### 8.1 Sign-locking

> **Theorem 8.1 (sign-locking and selection).** Every `C`-stabilizing
> automorphism of `𝔢₆` acts `±`-diagonally on the four charges, carrying a
> pattern `(ε₈, ε₁₄, ε₁₆, ε₂₂) ∈ {±1}⁴`; no real `C`-stabilizing symmetry swaps
> the split and compact directions. Two exact rational trace moments of degree 6
> then force `ε₈ε₁₆ = +1` and `ε₁₄ε₂₂ = +1`, so **twelve of the sixteen patterns
> are impossible for every automorphism**. The wall-real pattern is **unique**:
> `ε = (−1, +1, −1, +1)`, with `ε₈` and `ε₂₂` **forced rather than observed**.
>
> *(Theorem D(i)–(iv); B901, B907; `tests/test_b901_stab.py`,
> `tests/test_b907_selector.py`.)*

The wall of §7.3 is **complex in the split frame** — `det₁₄ > 0` at the real root
with vanishing `γ`-part, so the wall point is not a real point of the split torus,
and this holds at **all three** Galois roots of `μ` (Theorem C(iv); B893). The
real form in which the second wall is real is the quaternionic form `e₆(2)`,
reached only through outer-twisted alignments.

### 8.2 The involution that carries the ratios

One further theorem closes the algebra half. It identifies a single involution
`D₂` — an eleven-flip diagonal acting on the `27` — and shows that the ratio
structure of the construction is carried entirely by it.

> **Theorem 8.2.** `D₂ = ±ρ₂₇(σ_{χ₋})` for the **affine** (shifted) character
> `a* = (1,0,1,0,1,1)` — the unique match in the `128`-member family, with **all
> `64` un-shifted characters failing**. The wall-conjugation equation
> `H₊D₂ = H(φ*)` holds for `φ* = φ₊ ∘ σ_{χ₋}`, an involution and an automorphism
> verified on all `78²` bracket pairs, and `φ*` is the **unique** census member
> whose invariant Hermitian structure is `H₊D₂`. The four elements
> `{I, D₂, D, D₂D}` form a Klein group, realizing the wall pair's full `2`-torsion
> on the `27`.
>
> Every **inner** twist admits no invariant pairing; every **outer** composite
> admits exactly one (all `64` verified), Hermitian exactly when the composite is
> an involution.
>
> *(Theorem E(i)–(iv); B928, B916, B923; `tests/test_b928_decode.py`,
> `tests/test_b916_bridge.py`, `tests/test_b923_exact.py`.)*

From the characterization alone follow exact `K`-arithmetic invariants: a norm law
`N_{K/ℚ}(d_S) = N_{K/ℚ}(d_A) = −(953/2304)²` that **cubes** on the three-dimensional
coloured atoms, and a sum rule `Tr_{K/ℚ}(m_S) + Tr_{K/ℚ}(t_oct) = 11` exactly.
Under the canonical gauge the banked ratio polynomial collapses to `(x+3)³`.

**Two things are declared about this, not claimed.** First, the primes `953` and
`2304 = 2⁸3²` enter through the atom-solve eigenline coordinates and **the
derivation stops exactly there** — we do not derive them further, and §10 lists
that as an open registry item rather than a result. Second, these invariants are
computed **blind**: no measured value is consulted anywhere in their derivation,
and the stage at which such a comparison would be made is deliberately **outside
this paper** (§1.1, §9). They are recorded here as abstract invariants of `K`,
and as nothing else.

*(Note that `953` reappears here having already been seen in §6.1 as one of the
primes with a single degree-one place in `K`; `verify/check_charge_field.py`
checks that splitting shape.)*

**Character of §§6–8.** Every statement in these three sections is a theorem or an
exact identity about centralizers, structure constants, or trace moments of an
algebra the construction was handed. **No choice is made anywhere in them** — the
next declared choice in the chain is the observer's closing, which lies beyond the
scope of this paper (§5.5).
