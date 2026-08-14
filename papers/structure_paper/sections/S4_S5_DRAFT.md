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

> **Theorem 4.4 (character rigidity).** The continuous spectrum is a single
> channel, with scattering determinant `φ(s) = Λ_K(s−1)/Λ_K(s)` exactly.
> *(G10; `tests/test_b737_candidate_zero.py`, `tests/test_b739_rigidity.py`.)*

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

> **Theorem 5.3.** The figure-eight complement's **dual McKay pair `E₆ + E₈`** is
> realized as the **hyperbolic end** `(ℚ(√−3), 2T)` and the **spherical end**
> `(ℚ(√5), 2I)` of a **single cone-manifold geometric transition**. *(D1c; B248,
> B981; `tests/test_b248_e6_e8_geometric_transition.py`,
> `tests/test_b981_two_ended.py`.)*

The two exceptional algebras are therefore not selected and not assumed: they are
the **McKay images of the two binary polyhedral groups sitting at the two ends of
one deformation of the object**, one end carrying the field bought in §2.2 (C4)
and the other the fiber field of §4.1.

### 5.4 The entrance is where the uniqueness lives

Arrival at `E₆` is generic (§1.3). The **entrance** is not.

> **Theorem 5.4.** Over the infinite metallic family of grammars `RᵐLᵐ`, the golden
> grammar is the **unique** one whose **shadow modulus** `m² + 4` reduces to a McKay
> group — proved **at the `E₈` end**. The siblings diverge **at the entry map
> itself**, by exact enumeration: they have no corresponding door at all.
>
> *(B997 — uniqueness over the infinite family, stated at the `E₈` end; B1019 —
> the siblings' divergence at the entry map, `tests/test_b1019_l149.py`; B1002 —
> the identification `shadow modulus = m² + 4`, which B997 had flagged as inferred from
> two data points, discharged.)*

This is the discriminating fact of the construction, and we state it here — beside
the genericity caveat, not in a later discussion — so that the two are read
together. **Reaching the algebra proves nothing; entering it the way this object
does is what is unique.**

**Two scope notes, stated with the theorem rather than after it.** First, B997's
uniqueness is proved *at the `E₈` end*; the corresponding statement at the `E₆`
end is not claimed here. Second, **B997 carries no dedicated lock** — B1019's
lock covers the divergence half, and B1002 discharges the shadow-modulus
identification, but the uniqueness statement itself is not independently
re-runnable. **For the paper's discriminating theorem this is the weakest
verification link, and §B records it as such.**

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
