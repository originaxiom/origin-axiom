# §4–§5 — DRAFT v1

*Registry rows G7–G17, D1a–D1c, D2. Terminology per `TERMINOLOGY_POLICY.md`.*

---

## §4. The object's own arithmetic

Everything in this section is a property of the manifold produced in §3. **Nothing
is imported and no choice is made**; the section is included because §5 uses it and
because it establishes the character of the construction — theorems, censuses and
exact identities, in that proportion.

### 4.1 Three quadratic faces, forming a Klein four-group

> **Theorem 4.1.** The manifold's intrinsic arithmetic forces exactly three
> quadratic subfields, and they close under composition into a single Klein
> four-group `V₄`:
> ```
>        ℚ(√−3)        ℚ(√5)        ℚ(√−15)      (fundamental discriminant −15)
> ```

The first is the Kleinian trace field of §3.4; the second is the fiber field of
the monodromy's eigenvalues; the third is their composite. That there are
**exactly three, and that they close**, is the content — not that any one of them
appears. *(Registry G7; `tests/test_b730_faces_cosmos.py`.)*

### 4.2 The `V₄` belongs to the open manifold

> **Census 4.2.** No closed hyperbolic Dehn filling in the surveyed slope grid
> carries any of the three fields.

The arithmetic of §4.1 is a property of the **cusped** object. Filling the cusp
destroys it. This matters twice later: it is why §5's structure is available at
all, and it is the same cusped-ness that obstructs a boundary construction in §9.
*(Registry G8; `tests/test_b747_b748_sweeps.py`.)*

### 4.3 Congruence, rigidity, and the exact identities

Three further facts are used downstream and stated here without proof.

> **Theorem 4.3 (congruence).** The manifold's group is a congruence subgroup.
> *(G9; `tests/test_b734_m004_congruence.py`.)*

> ## ⚠ **Theorem 4.4 — SUSPENDED 2026-08-15, do not carry into the paper as stated.**
> The intended claim was: the continuous spectrum is a single channel, with an exact
> scattering determinant. **Three defects, all found by the Wave-1 inventory:**
>
> **(i) The corpus banks TWO CONTRADICTORY FORMULAS at equal authority.** B739 and
> `THEOREM_LEDGER` C10 give `Λ_K(s−1)/Λ_K(s)`; B737's own verdict and `LAW_MAP` give
> `Λ_K(s)/Λ_K(s+1)`. They differ by `s ↦ s−1`, and **no arc states the convention**.
> This draft cited *both* arcs as locks for one sentence.
>
> **(ii) Neither lock covers the function-level identity.** The two tests assert the
> `ℤ/4` coset character sum, the residue triangle, the index 12, the level palette and
> the disc-`−48` cusp — the identity itself appears **only as a comment**. The arc's own
> status line reads *"proven modulo 3 NAMED classical inputs … cited, not re-proven"*,
> and multiplicity-one is source-verified rather than proved.
>
> **(iii) The result is GENERIC, and the corpus says so.** The programme's own audit:
> *"φ(s) = Λ_K(s−1)/Λ_K(s) for **every** one-cusped quotient of PSL(2,O₃)\H³. **Not
> m004-specific**"*, and *"the scattering IS generic … by the letter of the falsifier,
> the thesis takes a hit. I report this honestly."*
>
> **What survives and may be used:** a one-cusp exact-transfer lemma was proved
> directly, and the level-character escape was closed by an exact Fourier restriction —
> so **level-dependent factors are proved absent**, which is the honest sentence. It is
> a statement about the *field* and the cusp count, not about this manifold. The genuinely
> m004-specific spectral data are the residue through `vol(m004)` and the conductor-4,
> disc-`−48` cusp CM.
>
> **This is exactly the objection an external referee raised and I could not then
> answer.** The answer is that the corpus is inconsistent, not that the referee was wrong.
> *(G10; locks `tests/test_b737_candidate_zero.py`, `tests/test_b739_rigidity.py` — both
> green, neither covering the suspended clause.)*

> **Identity 4.5 (the mixing structure).** The θ-odd block of the weld is exactly
> unitary with eigenphases `±72°`, and its overlap matrix is unistochastic and
> golden-exact:
> ```
>        P = [[ φ/√5 ,  1/(φ√5) ],
>             [ 1/(φ√5),  φ/√5  ]].
> ```
> *(G13; `tests/test_b753_mixing.py`.)*

Two further identities — the θ-equivariant fixed line of the trace map, and the
pure-3 symmetrized series — are recorded in the registry (G12, G14) and used only
in passing.

**Character of the section.** Of the nine links C7–C15, **five are theorems, three
are exact identities, one is a census, and none is a choice.**

---

## §5. The entrance

This is the section the paper rests on. It answers the question §1.3 raised: if
arriving at an exceptional algebra is generic, what is *not* generic here?

### 5.1 The tone structure at congruence level 15

The manifold's fiber-field side factors through a group of order **360** at
congruence level 15, whose non-CM subgroup is `Q₈`.

> **Theorem 5.1.** The twist-frame tone is ear-independent across all **360**
> group elements (agreement to `2·10⁻⁶⁰`), with an exact **five-tone** pentagon
> census. *(D1a; B641; `tests/test_b641_b642.py`.)*

This is the last structure that is purely knot-theoretic.

### 5.2 The two sides do not separate

It is tempting — and we record that one of us attempted it — to read the
congruence level (15) as a product of its prime parts and to conclude that the
algebra factorizes accordingly. **That reading is false, and the corpus contains its
refutation.**

> **Theorem 5.2.** The congruence-level-15 handshake is a **unique irreducible**
> coupling of the Kleinian-trace-field side and the fiber-field side: `59` of `60`
> primes falsify the corresponding `L`-factorization. *(D1b; B695;
> `tests/test_b695_e3_close.py`.)*

The two arithmetic sides **interfere**; they do not decompose. Any argument that
proceeds by splitting them is wrong at this step.

### 5.3 The exceptional algebras arrive at the two geometric ends

**The deformation itself is classical, and we claim none of it.** The figure-eight
complement's cone-manifold family — hyperbolic for cone angle `α < 2π/3`, **Euclidean
exactly at `α = 2π/3`**, spherical beyond — is due to Thurston, with the figure-eight
cone manifolds worked out by Hilden–Lozano–Montesinos and the degenerations by
Hodgson and Porti. A reader who knows that literature should recognise every
geometric statement in this subsection as theirs.

What we add is **which arithmetic sits at each end**.

> **Theorem 5.3.** Along that transition, the **hyperbolic end** carries
> `(ℚ(√−3), 2T)` and the **spherical end** carries `(ℚ(√5), 2I)` — so the
> object's **dual McKay pair `E₆ + E₈`** is realized as the two stable geometries
> of a *single* object, separated by the Euclidean wall, rather than as two
> unrelated faces.
>
> Concretely at the spherical end: the double cover is the lens space
> `L(5,2) = S³/ℤ₅`, and its `|H₁| = det(4₁) = 5` — **the `5` of that end is the knot
> determinant.** The corresponding representation is a genuine non-abelian `SU(2)`
> rep, with all word-traces real in `[−2,2]` and `tr(ab) = φ`.
>
> *(D1c; B248, B981; `tests/test_b248_e6_e8_geometric_transition.py`,
> `tests/test_b981_two_ended.py`.)*

> ## **Scope 5.3′ — the two ends are NOT symmetric, and the asymmetry runs against
> the direction a reader will assume.** At the hyperbolic end the object really
> does surject onto the binary polyhedral group: `π₁(4₁) ↠ 2T` is a genuine
> **group** surjection, with exactly two such quotients. **At the spherical end
> there is no surjection at all** — `π₁(4₁)` does **not** surject onto `2I`, nor
> onto `A₅`. So the `E₈` end is **field-level only** (`det = 5`, `ℚ(√5)`), and the
> two ramified-prime reductions are symmetric **as fields but not as group
> surjections**.
>
> *(The statement about `π₁(4₁)` is established by direct computation — GAP
> `GQuotients` gives `2T → 2`, `A₅ → 0`, `2I → 0` — banked as the B266 correction.
> Stuebner, arXiv:2502.06488, is cited as **context**: it studies binary
> icosahedral and `A₅` representations of hyperbolic integral homology spheres,
> and does not treat this knot specifically.)*

**We state this beside the theorem rather than in a limitations section**, because
a reader who takes "the two ends carry `2T` and `2I`" to mean two group-level
presences has been misled by the symmetry of the phrasing, and would be right to
distrust what follows. The symmetry is real at the level of *fields*; it is false
at the level of *quotients*.

The two exceptional algebras are therefore not selected and not assumed: they are
the **McKay images of the two binary polyhedral groups sitting at the two ends of
one deformation of the object** — with the asymmetry above understood — one end
carrying the field bought in §2.2 (C4)
and the other the fiber field of §4.1. The prior reading had `ℚ(√−3)` from the
geometry and `ℚ(√5)` from the bundle monodromy — *different* objects; the content
here is that **both arise as geometries on `4₁` itself**, as two distinguished
points of one character-variety curve.

**A firewall, carried from the source arc rather than added here.** `E₆` and `E₈`
in this subsection are **Arnold-trinity / McKay labels**, not gauge groups, and
nothing in §§5–8 upgrades them. The construction that would have broken `E₆` by the
geometric holonomy **fails**, because the `E₆`-selecting connection (hyperbolic,
`SL(2,ℂ)`) and a breaking `SU(2)` connection are different points of the variety —
and that very distinctness is what makes the present statement clean. **The split
that kills the physics bridge is the mathematical content.**

### 5.4 The entrance is where the uniqueness lives

Arrival at `E₆` is generic (§1.3). The **entrance** is not.

> **Theorem 5.4.** Over the infinite metallic family of grammars `RᵐLᵐ`, the golden
> grammar is the **unique** one whose **shadow modulus** `m² + 4` reduces to a McKay
> group — proved **at the `E₈` end**. The siblings diverge **at the entry map
> itself**, by exact enumeration: they have no corresponding door at all.
>
> *(B997 — uniqueness over the infinite family, stated at the `E₈` end,
> `tests/test_b997_golden_conductor_uniqueness.py`; B1019 — the siblings' divergence
> at the entry map, `tests/test_b1019_l149.py`; B1002 — the identification
> `shadow modulus = m² + 4`, which B997 had flagged as inferred from two data points,
> discharged.)*

This is the discriminating fact of the construction, and we state it here — beside
the genericity caveat, not in a later discussion — so that the two are read
together. **Reaching the algebra proves nothing; entering it the way this object
does is what is unique.**

### 5.4.1 Why it is the McKay group — two independent reasons, not one

The uniqueness above is a counting statement. There is also a **mechanism**, and it
is independent of the count.

> **Theorem 5.4.1 (the quantization-index law).** The reduction of the object mod
> its shadow modulus is an **isomorphism** exactly when the **cusp conductor** is
> coprime to the shadow modulus, and acquires a **kernel line** exactly when it is
> ramified. For the golden, `gcd(4, 5) = 1` — an **isomorphism**. For the silver,
> `gcd(2, 8) = 2` — **ramified**.
>
> *(B675, the mechanism; B666, the fact; B1002, the reconciliation.)*

So the golden's shadow is the McKay group because **both** independent conditions
hold: `|SL(2,ℤ/5)| = 120 = |2I|` with `N ∈ {3,4,5}` the complete list, **and**
`gcd(4,5) = 1`, so the reduction is faithful. **The silver satisfies neither** — `8`
is not a McKay order, and its ramification is precisely why its group sits one
quotient down.

*(A terminology warning, since the corpus was itself confused here for a while and
Appendix C repeats it: the bare noun names **two different quantities in adjacent
laws** — the **cusp conductor**, golden `4`, and the **shadow modulus** `m² + 4`,
golden `5`. B997's check looked open for months because the answer was banked under
the other sense of the word. We use the two qualified names throughout and never the
bare noun.)*

**Three scope notes, stated with the theorem rather than after it.**

**First**, the uniqueness is proved *at the `E₈` end*; the corresponding statement at
the `E₆` end is **not** claimed — that arrival remains class-level. **And by Scope 5.3′
the `E₈`-end object is not a quotient of the knot group at all.** This is not a
weakness of the theorem but a statement of what it is about: B997 quantifies over
**grammars** `RᵐLᵐ` and over `SL(2,ℤ/N)`, *not* over manifolds and not over
`π₁(4₁)`. The shadow whose uniqueness is proved is the **grammar's**, and the
paper must not let the surrounding discussion of the manifold blur that. The two
statements are compatible precisely because they quantify over different things.

**Second**, the reader should not be told that the moduli `N ∈ {3,4,5}` realize *the
whole exceptional series*. They do not. `SL(2,ℤ/3) ≅ 2T` and `SL(2,ℤ/5) ≅ 2I` are the
classical isomorphisms and give `E₆` and `E₈` genuinely; but **`E₇ = 2O` never
occurs**. At prime level `|SL(2,𝔽_p)| = p(p²−1)` is never `48`; and although
`|SL(2,ℤ/4)| = 48 = |2O|`, that group has **seven** elements of order 2, whereas every
finite subgroup of `SU(2)` has exactly **one**, so it is not `2O` — the order is a
coincidence and `2O` appears only as a quotient. **The golden's landing is unaffected
and is in fact cleaner: it lands on a genuine group, not on a matching number.**

**Third**, B997 formerly carried **no dedicated lock**, and earlier drafts of this
paper named that its weakest verification link. That is now closed: the lock cited
above proves the completeness step in exact arithmetic, replacing the arc's
`∏(1−1/p²) ≥ 6/π²` — true but irrational, and therefore not checkable — with the
telescoping bound `∏_{p|N}(1−1/p²) ≥ (N+1)/(2N)`, whence `|SL(2,ℤ/N)| ≥ N²(N+1)/2`,
already `126 > 120` at `N = 6`.

### 5.5 The forcedness census

We close the section with the count that characterizes the whole chain.

> **Census 5.5.** Of the **43** links, **26** are theorems, **6** exact
> identities, **5** no-go results, **1** a corollary, **1** a census — and **4**
> are declared choices, at links `3`, `4`, `5`, and `18`.
>
> ## **Between link 6 (the manifold) and link 17, there is no declared choice.**

The three choices of §2 occur *before* the manifold exists; the fourth occurs
after the algebra is in hand. **The stretch that carries the construction from the
manifold to the exceptional algebra and the `27` contains none.**

*(D2. Regenerated, not recalled: `scripts/checks/forcedness_census.py` recomputes
the census from the ledger and fails on drift.)*
