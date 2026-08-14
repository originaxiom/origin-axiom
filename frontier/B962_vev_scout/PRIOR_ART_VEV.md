# B962 — Prior-art scout: the 27 VEV, rank-1 elements of J₃(𝕆), and where a direction could come from

**Prepared by:** the scouting panel (adversarial prior-art seat)
**Date:** 2026-08-08
**Scope:** Q1–Q5 as posed. This document reports what the literature *shows*, separating
(a) statements verified against primary text in this sweep, (b) statements inferred from
standard theory and re-derived here, and (c) statements taken on abstract/metadata only.

**Headline for the seat, up front (details and caveats below):**

1. Q1 confirms the prior panel, **with one precision correction**: `Spin(10)` is the stabiliser
   of the rank-1 **vector**; the stabiliser of the rank-1 **line** (the point of the Cayley plane)
   is `(Spin(10) × U(1))/ℤ₄`. The difference is exactly whether you quotient by scale.
2. Q2: the VEV direction is **never derived** in any framework found. Group theory derives the
   *finite menu* of orbits; which orbit, and the potential that selects it, is always an input.
   **So "the object does not supply a VEV" is not a defect peculiar to this object.**
3. Q3: **certified null** — nobody has derived a GUT Higgs VEV direction from arithmetic.
4. Q4: **𝕆P² is F₄-homogeneous, and more strongly F₄ is transitive on Jordan frames.**
   Choosing a VEV is exactly and unavoidably a choice with no canonical answer — over ℝ or ℂ.
   **The single exception in principle is an arithmetic/integral structure**, which does stratify
   the rank-1 elements. That is the one live opening, and it is unworked.
5. Q5: a real no-go the prior panel did not flag — **two 27 VEVs reach SU(5), but 27 VEVs can
   never break SU(5) → the Standard Model.** Re-derived here from branching rules, and
   corroborated by an explicit statement in the E₆SSM literature.

---

## 0. Search record

### Databases reached

| Database | Endpoint | Status | Used for |
|---|---|---|---|
| zbMATH | `api.zbmath.org/v1/document/_search` | **reached**, HTTP 200 | Q1, Q4 — Jordan/Albert algebra, Cayley plane, Severi varieties |
| arXiv | `export.arxiv.org/api/query` (**HTTPS only**) | **reached** | Q1, Q3, Q4 — note: plain HTTP returns an empty body; HTTPS is required |
| arXiv e-print source | `arxiv.org/e-print/<id>` | **reached** | full LaTeX of Baez, Ferrara–Günaydin, Krutelevich |
| OpenAlex | `api.openalex.org/works` | **reached** | citation-graph closure (`filter=cites:`) |
| INSPIRE-HEP | `inspirehep.net/api/literature` | **reached** | Q2, Q5 — particle-physics literature |
| ar5iv | `ar5iv.labs.arxiv.org/html/<id>` | **partially reached** — issues a cross-host 307 redirect for some ids; worked for others | full text of E₆SSM / F-theory papers |
| Semantic Scholar | `api.semanticscholar.org/graph/v1` | **NOT reached** — HTTP 429 (rate-limited) throughout | — |
| MathSciNet | `mathscinet.ams.org` | **NOT reached** — HTTP 302 to an authentication wall, as expected | — |

**Stated plainly:** MathSciNet was unreachable (auth wall) and Semantic Scholar was rate-limited.
Neither gap is load-bearing: zbMATH covers the same mathematical literature and was reached,
and the Q1/Q4 conclusions rest on primary text (Baez's own LaTeX source), not on indexing.

One further disclosure: a sub-sweep exhausted its web-search quota partway through Q3 and
completed on the bibliographic APIs alone. All three APIs converged independently, so this is
disclosed for honesty rather than as a known weakness.

### Must-pass control — **PASSED**

The method was required to retrieve the standard Albert-algebra / Cayley-plane literature and
the standard E₆ GUT literature *before* any null is trusted. It did:

- **Freudenthal**, *Oktaven, Ausnahmegruppen und Oktavengeometrie* (1951; reprints 1960, 1985) — zbMATH ✅
- **Tits**, *Le plan projectif des octaves et les groupes de Lie exceptionnels* (1953) — zbMATH ✅
- **Rozenfeld**, *Die kompakte einfache Gruppe E₆ als Bewegungsgruppe der nichteuklidischen komplexen Oktavenebenen* (1954) — zbMATH ✅ (directly on point for Q1)
- **Jacobson**, *Structure and Representations of Jordan Algebras* (1968) — zbMATH ✅
- **Springer & Veldkamp**, *Octonions, Jordan Algebras and Exceptional Groups* (2000) — zbMATH + OpenAlex `W211457683` ✅
- **Baez**, *The Octonions* (2001/2002) — retrieved *and full LaTeX source obtained and read* ✅
- **Zak**, *Severi varieties* (1985) / *Tangents and Secants of Algebraic Varieties* (1993) — zbMATH ✅
- **Gürsey–Ramond–Sikivie**, *A Universal Gauge Theory Model Based on E₆* (1975, 871 citations) — INSPIRE ✅
- **Moore**, *Arithmetic and Attractors* (hep-th/9807087, 288 citations) — INSPIRE ✅ (control for the Q3 null)
- Standard flux-compactification literature (Donagi–Wijnholt 346 cites; Hebecker–March-Russell 276 cites) — INSPIRE ✅

The control retrieved every canonical item it was supposed to. **The nulls below are therefore
not artefacts of broken retrieval.**

### Citation-graph closure performed

The decisive closure was run on the sharpest arithmetic lead:

- **Elkies & Gross, *The exceptional cone and the Leech lattice*, IMRN 1996** — OpenAlex `W2995339545`
  (DOI `10.1155/s1073792896000426`; the OpenAlex record has a null title field, so title-search
  returns count 0 — it must be found by DOI/author, a retrieval trap worth recording).
  **Complete citing set enumerated: 39 papers, all titles read individually.**

  Result: the citing set is (i) lattice theory and modular forms (Leech/Niemeier, unimodular
  lattices, `G₂`/`E₈` modular forms), (ii) Jordan-algebra arithmetic (Elkies–Gross 2001,
  Garibaldi–Petersson–Racine, *Integral Embeddings of Cubic Norm Structures*), and
  (iii) **black-hole charge-orbit / U-duality physics** (*Observations on integral and continuous
  U-duality orbits in N=8 supergravity*; *Black Holes and Higher Composition Laws*; *Integral group
  actions on symmetric spaces and discrete duality symmetries of supergravity theories*;
  *Freudenthal dual* papers).

  **Zero of the 39 concern GUT symmetry breaking, Higgs fields, or VEVs.** This is the single
  cleanest piece of evidence for the Q3 null, and it is a *complete* enumeration, not a sample.

  The distinction that makes this citing set instructive: in the black-hole papers the 27 is a
  **charge vector**, where integrality is *physically forced* by Dirac quantisation, so the
  arithmetic structure is legitimate and used. In GUT model building the 27 is a **Higgs field**,
  whose VEV is a continuous parameter, and no one has proposed an integral structure on it.

---

## Q1 — Rank-1 elements of J₃(𝕆), the space of them, and the stabiliser

### Q1a. Characterisation of rank — **verified against primary text**

Let `J = h₃(𝕆)` be the Albert algebra, `dim = 27`. All of the following are from Baez,
*The Octonions*, §3.4 (read in the original LaTeX source, not paraphrased):

**Trace** is intrinsic to the Jordan structure, hence `F₄`-invariant:
`tr(a) = (1/9) tr(L_a)`, with `L_a` left Jordan multiplication.

**Determinant** (the cubic norm):

```
det(a) = (1/3) tr(a³) − (1/2) tr(a²) tr(a) + (1/6) tr(a)³
```

equivalently, in matrix entries,
`det = αβγ − (α‖x‖² + β‖y‖² + γ‖z‖²) + 2 Re(xyz)`.

**Sharp / adjoint map.** The determinant is a cubic form, so it polarises to a unique symmetric
trilinear form `(·,·,·)` with `(a,a,a) = det(a)`; dualising gives the **cross product**
`× : J × J → J*`, `(a × b)(c) = (a,b,c)`. The sharp map is `a# = a × a`.

**Rank, stated three equivalent ways:**

| rank | intrinsic characterisation | orbit-theoretic |
|---|---|---|
| 1 | `a ≠ 0` and `a# = a × a = 0` | closed (minimal) orbit; cone over the Cayley plane |
| ≤ 2 | `det(a) = 0` | the determinant hypersurface |
| 3 | `det(a) ≠ 0` | generic / open orbits |

The rank-1 condition `a × a = 0` is **Freudenthal's** characterisation; Baez attributes it
explicitly ("Freudenthal noticed that these are the same as elements `p` with `tr(p) = 1` and
`p × p = 0`"). Baez further notes one may **drop** `tr(p) = 1` provided one works with
equivalence classes of nonzero solutions of `p × p = 0` up to nonzero real scale — i.e. the
rank-1 condition is *projective*, and the trace-1 normalisation is a choice of scale, not part
of the geometry.

**Rank = trace for idempotents.** Baez proves that up to automorphism every projection in
`h₃(𝕆)` is one of `p₀, p₁, p₂, p₃` (0, 1, 2, or 3 ones on the diagonal), and that
`rank(p) = tr(p)` for every projection. Hence:

> **points of 𝕆P² = projections of trace 1 in h₃(𝕆) = the primitive idempotents.**
> (lines of 𝕆P² = projections of trace 2, giving the self-duality of the plane.)

**Explicit form.** Every trace-1 projection is

```
p = v v*,   v = (x, y, z) ∈ 𝕆³,   with   (xy)z = x(yz)   and   ‖x‖² + ‖y‖² + ‖z‖² = 1.
```

The associativity side-condition `(xy)z = x(yz)` is what makes this a genuine projective plane
despite non-associativity, and it is not optional.

**Confirmed:** rank-1 elements up to scale form **𝕆P², the octonionic projective plane, a smooth
manifold of dimension 16** (Baez §3.4, explicitly: "As a manifold, 𝕆P² is 16-dimensional"),
and they **are** the primitive idempotents of the Albert algebra. ✅ Prior panel correct.

**Complexified version (the GUT-relevant one).** For `J₃(𝕆_ℂ)` — the complex 27 — the rank-1
locus in `ℙ(27)` is the **complex Cayley plane** `E₆/P₁`, of complex dimension 16, the **unique
closed orbit** of `E₆` on `ℙ(27)` (the highest-weight-vector orbit). It is one of the four
**Severi varieties** in Zak's classification (`v₂(ℙ²)`, `ℙ²×ℙ²`, `G(1,5)`, `E₆/P₁`) — Zak,
*Severi varieties* (1985) / *Tangents and Secants* (1993), retrieved via zbMATH. Its status as
the *unique closed* orbit is the structurally important part: it is the smallest, most degenerate
stratum, of measure zero in the 27.

### Q1b. The stabiliser — **prior panel correct, with a precision correction**

This is the point most easily got wrong, because the answer differs depending on
(i) which real form of E₆, and (ii) **whether you stabilise the vector or the line**.
All dimension arithmetic below was re-derived and checked in-sandbox.

| Setting | Object stabilised | Stabiliser | dim | orbit dim | source |
|---|---|---|---|---|---|
| **compact E₆ on ℂ²⁷** | nonzero rank-1 **vector** | **`Spin(10)`** | 45 | 33 = 32+1 | Adams/Baez `e₆ ≅ so(10) ⊕ u(1) ⊕ S₁₀` |
| **compact E₆ on ℂ²⁷** | rank-1 **line** `[v]` | **`(Spin(10) × U(1))/ℤ₄`** | 46 | 32 (=16 ℂ) | Baez §4.4, verbatim |
| complex / split E₆ | rank-1 vector | `Spin(10) ⋉ ℂ¹⁶` | 61 | 17 | 78 − 61 = 17 ✓ |
| split `E₆₍₆₎` on real 27 | rank-1 vector | `O(5,5) ⋉ T₁₆` | 61 | **17** | Ferrara–Günaydin, verbatim |
| complex E₆ on `ℙ(27)` | rank-1 line | parabolic `P₁`, Levi `Spin(10)×GL(1)` | 62 | 16 | 78 − 62 = 16 ✓ |
| `E₆₍₋₂₆₎` on real `h₃(𝕆)` | point of 𝕆P² | Levi part `Spin(9,1)` | (45) | — | Baez §4.4 — **see caveat** |
| `F₄` on `h₃(𝕆)` | primitive idempotent | **`Spin(9)`** | 36 | 16 | Baez §4.2, `𝕆P² = F₄/Spin(9)` |

**Verdict on the prior panel's claim: CORRECT.** For the physically relevant case — compact E₆
acting on the complex 27, a single VEV along a rank-1 direction — the unbroken group is exactly
`Spin(10)`, dimension 45.

**Why `Spin(10)` and not `SO(10) × U(1)`:** the `U(1)_ψ` in `E₆ ⊃ SO(10) × U(1)_ψ` is *broken*,
because under that decomposition `27 = 1₄ + 10₋₂ + 16₁` and the rank-1 (highest-weight)
direction is the `1₄`, carrying `U(1)_ψ` charge **4 ≠ 0**. A VEV breaks every generator under
which it is charged. Dimension check: `78 − 45 = 33 = 32 + 1`, i.e. the 32 broken generators are
exactly the spinor `S₁₀`, plus the one broken `U(1)`. ✓

**Why `Spin(10)` and not `SO(10)`:** the unbroken group acts on the `16 ⊂ 27`, a genuine spinor
representation, which `SO(10)` does not represent. So the double cover is the correct group.

**The precision correction the seat should carry.** `SO(10) × U(1)` is not simply *wrong* — it is
the right answer to a *different* question. `(Spin(10) × U(1))/ℤ₄` is the stabiliser of the rank-1
**line**, i.e. of the VEV *direction considered projectively*, with the magnitude forgotten. Baez
gives this verbatim when defining the bioctonionic projective plane
`(ℂ⊗𝕆)ℙ² = E₆ / ((Spin(10) × U(1))/ℤ₄)`. Since a physical VEV has a magnitude, the vector
stabiliser `Spin(10)` is the physically correct one. **The distinction is exactly the quotient by
scale**, and any source quoting `SO(10)×U(1)` is almost certainly stabilising the line.

**A caveat on Baez, recorded because it is a live trap.** Baez writes that "the group of
collineations fixing a specific point is `Spin(9,1)`", paralleling `Spin(9)` for isometries. The
isometry statement is exact (`52 − 36 = 16` ✓). The collineation statement is **not** the full
isotropy group: `dim E₆₍₋₂₆₎ − dim 𝕆P² = 78 − 16 = 62`, whereas `dim Spin(9,1) = 45`. The full
point-stabiliser is the parabolic `(Spin(9,1) × ℝ⁺) ⋉ ℝ¹⁶`, dimension `45 + 1 + 16 = 62` ✓.
Baez is naming the semisimple part of the Levi, not the stabiliser. Do not quote it as the
stabiliser.

### Q1c. The full orbit stratification of the 27 — **verified against primary text**

From Ferrara & Günaydin, *Orbits of Exceptional Groups, Duality and BPS States in String Theory*
(hep-th/9708025), §2, read in the original LaTeX source. For the split form `E₆₍₆₎` acting on the
27 there are **exactly three nonzero orbits**, labelled by Jordan rank:

| Jordan rank | invariant condition | orbit | dim | stabiliser |
|---|---|---|---|---|
| 3 | `I₃ ≠ 0` | `E₆₍₆₎ / F₄₍₄₎` | 26 | `F₄₍₄₎` (dim 52) |
| 2 | `I₃ = 0`, `∂I₃ ≠ 0` | `E₆₍₆₎ / (O(5,4) ⋉ T₁₆)` | 26 | dim 36+16 = 52 |
| 1 | `∂I₃ = 0` | `E₆₍₆₎ / (O(5,5) ⋉ T₁₆)` | **17** | dim 45+16 = 61 |

All three dimension identities check (`26+52 = 78`, `17+61 = 78` ✓). The rank-1 orbit has
dimension 17 = 16 + 1, exactly the cone over the 16-dimensional Cayley plane. `O(5,5)` is the
split real form of `SO(10)` — **this is an independent confirmation of the `Spin(10)` answer**,
arrived at from the supergravity side with no reference to GUT model building.

**Structurally the most important line in this report:**

> The rank-3 (generic, open, full-measure) stratum has stabiliser **F₄**.
> The rank-1 (closed, minimal, measure-zero) stratum has stabiliser **Spin(10)**.

So the programme's already-proved F₄ obstruction — rank 4 but the 27 goes real, killing
chirality — is not a separate fact. **It is what the *generic* VEV does.** A VEV `∝ 1` (the Jordan
identity, rank 3) is stabilised by `Aut(J) = F₄` by definition. Chirality survives only on the
**closed, most degenerate, measure-zero** orbit. Whatever supplies a direction must land exactly
there, and "exactly there" is a codimension-10 condition in the 27.

---

## Q2 — What determines the VEV direction in E₆ model building?

**Answer: it is an input. Nothing found derives it. But the framing needs one refinement,
because part of it genuinely *is* derived.**

### The one thing that is genuinely derived: the menu

There is a real, first-principles result here, and it should not be dismissed. The **orbit space /
stratification** of the 27 under `E₆` is fixed by pure group theory — no potential, no parameters.
This is the Ferrara–Günaydin table above (three strata, rank-labelled), and on the physics side it
is the **Michel / Michel–Radicati** programme:

- **J. S. Kim**, *Orbit Spaces of Low Dimensional Representations of Simple Compact Connected Lie
  Groups and Extrema of a Group Invariant Scalar Potential*, J. Math. Phys. **25** (1984) 1694
  (INSPIRE 13825). Its abstract explicitly covers "the defining representations of `F₄` and `E₆`"
  and states that orbit spaces are "warped polyhedrons with (locally) more protrudent boundaries
  corresponding to **higher level little groups**", and that "the absolute minimum condition
  prompts the boundary conditions enough to determine the representation vector."
  *(abstract-level only — pre-arXiv, full text not reachable by this sweep.)*
- **Kim & Gell-Mann**, *General Methods for Analyzing Higgs Potentials* (INSPIRE 178410), invoking
  the **Michel–Radicati conjecture**: critical points of an invariant potential are geometrically
  forced to sit at points of enhanced symmetry. *(abstract-level only.)*

So: **group theory derives the finite menu of candidate directions and their little groups.
It does not order off the menu.** Which stratum is realised depends on the potential's free
parameters.

### Everything else is an input

- **The direction is assumed.** In the E₆SSM lineage (King, Moretti, Nevzorov, hep-ph/0510419 —
  *full text read*), the direction is stated as an assumption: "Without loss of generality we can
  assume that only the third family Higgs doublets and singlets ... gain VEVs", justified only
  post hoc ("the large third family coupling ... provides a radiative mechanism ... which defines
  the third family direction").
- **Flatness constrains but does not fix.** D-flatness and F-flatness cut down the space of
  admissible directions; they never single one out. In the F-theory realisation (Callaghan & King,
  arXiv:1210.6913 — *full text read*), flatness is imposed as a constraint while free integer
  choices remain ("we leave `ñ₃₁ > 0` unspecified for now", "we take the simplest case").
- **String/geometric breaking replaces the choice with a different choice.** Wilson-line /
  Hosotani / flux breaking fixes the unbroken group by *discrete topological data* rather than a
  potential — but which flux or automorphism is turned on is selected from a landscape to
  reproduce the Standard Model. Hebecker & March-Russell (hep-ph/0107039) prove orbifold breaking
  and Wilson-line breaking are in 1-to-1 correspondence; in both, the automorphism is hand-picked.
- **Composite-Higgs "vacuum alignment"** is the same paradigm, not an exception: alignment is
  fixed by minimising an effective potential generated by explicit-breaking terms.

### Why this matters for the seat (the load-bearing conclusion)

**No framework in the E₆ GUT literature derives the 27 VEV direction.** The direction is either
assumed outright, or constrained-but-not-fixed by flatness, or traded for an equally
hand-picked discrete choice of flux/automorphism.

Therefore: **"the object does not supply a VEV" is not a defect peculiar to this object.** It is
the universal situation. No E₆ model supplies one either; they *postulate* one. If the programme
wants to make something of this, the honest framing is not "our object is missing an ingredient
that others have" — it is "nobody has this ingredient, and here is a structure that might
eventually supply it," which is a much stronger and much riskier claim, and is unproven.

Note also a consequence of Q4 that sharpens Q2: **within a single orbit, all directions are
E₆-equivalent**, so "choosing a direction" *within* a stratum is physically vacuous — pure gauge.
The only meaningful content in "choosing a VEV" is **choosing which stratum (which rank)**. That
is a choice among three, not a choice in a 27-dimensional space.

---

## Q3 — Has anyone derived a VEV direction from arithmetic or geometry?

**Verdict: CERTIFIED NULL** for the question as posed — a GUT Higgs VEV direction *in a
representation space* derived from arithmetic rather than from potential minimisation.

The control passed (Moore's *Arithmetic and Attractors* and the standard flux literature were
both retrieved at high citation counts), and the complete 39-paper citing set of Elkies–Gross was
enumerated with zero GUT/Higgs hits. Roughly 30 targeted queries across INSPIRE, arXiv, and
OpenAlex converged on the same negative.

**Three near-misses, none of which satisfies the criterion:**

1. **Flux / Wilson-line / orbifold breaking** (Donagi–Wijnholt 0808.2223, 346 cites;
   Hebecker–March-Russell hep-ph/0107039, 276 cites; Marsano et al. 1206.6132;
   Anderson et al. 1411.0034). This is genuine *geometric* constraint on a symmetry-breaking
   direction — Donagi–Wijnholt show massless hypercharge is a **topological** constraint on the
   flux. **But it is categorically not a Higgs VEV:** no scalar acquires an expectation value in a
   representation; the breaking is a gauge-bundle/flux background, a class in `H^{1,1}` of a
   divisor. The "direction" fixed is *which Cartan generator carries the flux*, not a vector in a
   Higgs representation. **This is the closest real analogue in physics and it sidesteps the
   question rather than answering it.**

2. **Moore, *Arithmetic and Attractors* (hep-th/9807087).** Genuinely singles out arithmetically
   distinguished (CM) points — but in the **complex-structure moduli space of the Calabi–Yau**,
   not in a representation space where a Higgs lives. Its citing set was filtered for Higgs/VEV
   terms (20 inspected); none extend the attractor mechanism to a gauge-breaking direction.

3. **The integral Albert algebra** — Elkies–Gross (IMRN 1996; Duke 2001); Garibaldi–Petersson–Racine,
   *Albert algebras over ℤ and other rings* (arXiv:2205.09896); Krutelevich (math/0411104);
   Kato–Yukie (arXiv:1603.00739). Real, rich arithmetic structure on exactly the right object.
   **Zero physics content** — no GUT, no Higgs, no vacuum, no symmetry breaking.

**Nearest bridge, and why it fails.** Singh, *Fermion mass ratios from the exceptional Jordan
algebra* (arXiv:2508.10131, Aug 2025). Uses the arithmetic of the Jordan cubic form to get fermion
mass-ratio relations. But its own stated setup is "when `⟨X⟩` is Jordan-diagonalised to
`diag(a,b,c)`…" — **the diagonal basis, i.e. the VEV direction / choice of idempotent triple, is
an assumed starting condition, not a derived one.** The arithmetic fixes *ratios among
eigenvalues once a direction is chosen*; it does not explain why that point of the orbit is
singled out. This is precisely the necessary-not-sufficient trap.

Off-target but adjacent, recorded so the seat does not mistake them for prior art on this
question: Dubois-Violette (1604.01247) and Boyle (2006.16265) use `J₃(𝕆)` to encode fermion
*representation content* via triality — neither addresses a Higgs mechanism or a VEV direction.
Cayley-plane appearances in physics (0807.4899 `𝕆P²` bundles in M-theory; 1006.0728 Cayley plane
and the Witten genus; 2202.02050; 2309.00967) are target-space/index-theory objects, never
vacuum-selection spaces.

**Certified vs. not-found.** The null is *certified* for the specific claim "a GUT Higgs VEV
direction derived from arithmetic". It is *not* a certification that the broader idea is
impossible or unpublished in some adjacent form — a paper using different vocabulary entirely
could have been missed. The certification rests on: control passed, complete citation-graph
closure on the one paper such work would be obliged to cite, and convergence of ~30 queries
across three independent APIs.

---

## Q4 — Is there a canonical rank-1 element of J₃(𝕆)?

**Answer: NO, over ℝ or ℂ — and the statement is stronger and cleaner than the question assumed.**

### The transitivity statement, verified

**𝕆P² is F₄-homogeneous.** From Baez §4.2, verbatim: `Spin(9)` is *precisely* the subgroup of
`F₄ = Aut(h₃(𝕆))` fixing the trace-1 projection `diag(1,0,0)`; `F₄` acts transitively on `𝕆P²`;
hence

```
𝕆P² ≅ F₄ / Spin(9),     dim F₄ = dim Spin(9) + dim 𝕆P² = 36 + 16 = 52  ✓
```

Transitivity is not asserted — it is *constructed*. Baez's §3.4 argument uses `Spin(9) ⊂ F₄` to
make one octonion entry real, then `Spin(8)` to make the others real, then an `O(3)` conjugation
to diagonalise. This is an explicit algorithm carrying any element to diagonal form.

**Independently certified:** Miyasaka & Yokota, *Constructive diagonalization of an element X of
the Jordan algebra J(3,𝕆) by the exceptional group F₄* (arXiv:1011.0603), whose abstract states:
"any element `X` of the exceptional Jordan algebra `J` is transformed to a diagonal form by the
compact exceptional Lie group `F₄`" — and which supplies a **direct constructive proof**,
replacing the earlier proof by contradiction.

### The stronger statement the seat should actually use

Diagonalisability is transitivity on **Jordan frames**, not merely on single idempotents:

> **`F₄` acts transitively on ordered triples of pairwise-orthogonal primitive idempotents
> (Jordan frames) of `h₃(𝕆)`.**
> Equivalently: `E₆` acts transitively on the punctured rank-1 cone, and `F₄` acts transitively on
> complete orthogonal decompositions of the identity.

Consequently **no rank-1 element, no orthogonal *pair*, and no orthogonal *triple* is canonical.**
This matters because the route the prior panel identified needs **two** VEVs — and the two-VEV
configuration is *also* a single homogeneous orbit with no distinguished point. Closing off the
obvious escape ("maybe the *pair* is canonical even if neither element is") is worth having.

### The clean structural statement

> The set of possible VEV directions is a **homogeneous space** of the symmetry group.
> A canonical point of a homogeneous space exists only if the space is a point.
> `𝕆P²` has dimension 16. **Therefore choosing a VEV direction is exactly and unavoidably a
> choice, and no symmetry-based argument can ever make it canonical.**

This is worth its weight, and it is *not* a negative result about the object — it is a theorem
about `E₆` that applies to every E₆ model ever written. It converts "our object fails to supply a
VEV" into "no group-theoretic structure can supply one; the question is misposed."

Note the precise scope: it forbids deriving the direction **from the symmetry**. It does not
forbid deriving it from *extra structure that breaks the homogeneity*. Which is Q4's exception:

### The exception — arithmetic, and it is the one live opening

Homogeneity is a statement about `𝕆P²` over `ℝ` or `ℂ`. Over `ℤ` or a number field, the relevant
group is **arithmetic**, not the full real/complex group, and homogeneity fails: an arithmetic
group has *finitely many orbits*, and the strata are labelled by genuine arithmetic invariants.

- **Elkies & Gross, *The exceptional cone and the Leech lattice*, IMRN 1996** — constructs an
  integral structure `(J, E)` on the 27-dimensional exceptional Jordan algebra and ties the cone
  of rank-1 elements to the Leech/Niemeier lattices.
- **Elkies & Gross, *Cubic rings and the exceptional Jordan algebra*, Duke 2001** — embeddings of
  totally-real cubic rings into the integral Albert algebra.
- **Krutelevich, math/0411104** — an *integral* version of the Freudenthal construction, with an
  algorithmic approach to **orbit spaces** over ℤ, related to Bhargava's higher composition laws.
- **Kato & Yukie, arXiv:1603.00739** — for the prehomogeneous space `(GE₆ × GL(2), J ⊕ J)`, i.e.
  literally **pairs of 27s**, generic **rational** orbits are in bijection with isomorphism classes
  of pairs `(M, n)` with `M` an isotope of `J` and `n` a cubic étale subalgebra; for split `𝕆`,
  with separable extensions of `k` of degree ≤ 3.

That last one is the sharpest: **over a non-closed field the configuration space of two 27s is
*not* homogeneous — its orbits are classified by cubic étale algebras / degree-≤3 field
extensions.** So arithmetic genuinely does stratify exactly the object the two-VEV route needs.

**But state the honest limit.** Choosing the integral structure is itself a choice; nothing found
singles out one rank-1 element as canonical; and **no source connects any of this to a Higgs VEV**
(this is the Q3 null restated from the mathematics side). The opening is real and unworked, not a
result. It is also the one place where the programme's object could differ from a generic E₆
model, since it carries arithmetic (`ℚ(√−3)`) that a generic model does not. That observation is a
*motivation for a computation*, not a claim, and must not be banked as one.

---

## Q5 — Known no-gos for E₆ → SM with 27 VEVs

### Q5a. The decisive one: 27 VEVs cannot reach the Standard Model — **re-derived here**

This is the most important finding in the report and the prior panel did not flag it.

**Literature statement**, full text read, King–Moretti–Nevzorov hep-ph/0510419 §2.2, verbatim:

> "one cannot break E6 in a conventional manner as the required Higgs fields are in larger
> representations than the 27."

The authors accordingly resort to the **Hosotani mechanism** at the string scale for the primary
breaking, using 27 VEVs only for a secondary step.

**Independent re-derivation in-sandbox** (not taken on trust). Branching the 27 to `SU(5)` via
`E₆ ⊃ SO(10)×U(1)` then `SO(10) ⊃ SU(5)×U(1)`:

```
27 → 16 + 10 + 1                      (SO(10))
16 → 10 + 5̄ + 1,  10 → 5 + 5̄,  1 → 1   (SU(5))
⟹ 27 → 10 + 5 + 5̄ + 5̄ + 1 + 1        (dimension check: 10+5+5+5+1+1 = 27 ✓)
```

**The 24 (adjoint of SU(5)) does not appear.** Breaking `SU(5) → SU(3)×SU(2)×U(1)_Y` requires a
VEV along a hypercharge-neutral, `SU(3)×SU(2)`-singlet direction — i.e. `Y` itself, which lives in
the **24**. Sharper, and independent of representation bookkeeping:

> Every component of `5`, `5̄`, `10` carries nonzero hypercharge. The **only** `Y`-neutral
> directions available in any number of 27s are the `SU(5)` **singlets** — and those break
> nothing inside `SU(5)`. Hence **no combination of 27 VEVs can break `SU(5) → SU(3)×SU(2)×U(1)_Y`.**
> Any non-singlet direction that does break `SU(5)` necessarily also breaks `U(1)_Y`.

Worked example confirming this: a VEV along the `SU(3)×SU(2)`-singlet `(1,1)` of the `10` leaves
`SU(3)×SU(2)`, of rank 3 — hypercharge is destroyed, not preserved.

**What this means for the prior panel's route.** The route is **correct as far as it goes**:
`E₆ → SO(10) → SU(5)` via two rank-1 27 VEVs does achieve rank 6 → 4 with the 27 still complex
(verified: `1₄` gives `Spin(10)`, rank 5; the `SU(5)`-singlet of `16₁` gives `SU(5)`, rank 4;
`SU(5)` has complex `5`, `10`, so chirality survives). Both VEVs are Jordan rank 1 — the `1₄` is
the highest-weight vector, and the `SU(5)`-singlet of the `16` is a **pure spinor**, and the
`Spin(10)` pure-spinor variety is exactly the intersection of the Cayley plane with `ℙ(16)`.

**But `SU(5)` is not the Standard Model**, and the last step is blocked by the argument above.
The route delivers *rank 4 + a complex 27* and then stops one step short, and that step needs a
representation (the `78`, or a `351`) that the 27 route does not contain.

### Q5b. Supersymmetric D-flatness stalls the rank reduction at 5

Full text read, hep-ph/0510419. In SUSY the 27 VEVs come paired as `27_H + 27̄_H` along the
D-flat direction `⟨N_H^c⟩ = ⟨N̄_H^c⟩`, and this breaks only **one** unit of rank. The E₆SSM
therefore lands on a **rank-5** group (`SU(5)×U(1)_N` or `SO(10)×U(1)`-type), and the final `U(1)_N`
is broken separately at the **TeV** scale by an ordinary matter singlet `S`. This is partly a
model *choice* — the E₆SSM *wants* a TeV `Z′` — but the D-flatness constraint that forces the
`27/27̄` pairing is structural in SUSY, not optional.

**Recorded as a genuine tension:** the pure group theory (Q5a) says two rank-1 27 VEVs give
`SU(5)`, rank 4. The SUSY literature reports stalling at rank 5. These are consistent — the
SUSY models impose D-flatness and *choose* directions preserving a `U(1)` — but a seat that
quotes "two 27 VEVs give rank 4" inside a SUSY context will be contradicted by the literature and
should know why.

### Q5c. Exotics, proton decay, doublet–triplet

Full text read, hep-ph/0510419 and arXiv:2002.02788. Under `SU(5)×U(1)_N`:

```
27 → (10,1) + (5̄,2) + (5̄,−3) + (5,−2) + (1,5) + (1,0)
```

- `(10,1) + (5̄,2)`: one ordinary family.
- `(5̄,−3)` and `(5,−2)`: Higgs-doublet-like states **plus a vector-like colour-triplet pair
  `D, D̄`** of charge ∓1/3, with `B−L` twice that of ordinary quarks.
- `(1,5)`: extra singlet `S`. `(1,0)`: right-handed neutrino `N^c`.

This matches `27 = 16 + 10 + 1` exactly, and the exotics are unavoidable — they come with the
representation.

- **Proton decay / B,L violation:** the paper states plainly that "the gauge symmetry of the
  models under consideration does not forbid lepton and baryon number violating operators."
  Suppression requires an **ad hoc discrete symmetry** (`Z₂^L` → exotics are diquarks; `Z₂^B` →
  exotics are leptoquarks), with some parameter regions "basically ruled out".
- **Doublet–triplet splitting is not solved, it is routed around:** the `D, D̄` triplets are kept
  *light* (TeV, vector-like mass from `⟨S⟩`) rather than split to the GUT scale. In the F-theory
  version (1210.6913) proton decay is suppressed by "geometric coupling suppression ... peculiar
  to F-theory" — again a bypass, not a solution.

### Q5d. The orbit-theoretic no-go, stated cleanly

Combining Q1c with the above, the failure modes of a single 27 VEV are exhaustive and short:

| VEV Jordan rank | unbroken group | rank | 27 complex? | verdict |
|---|---|---|---|---|
| 3 (generic, `∝ 1`) | `F₄` | 4 | **no** — 27 → 26 + 1, real | rank 4 but **chirality dead** |
| 2 | `Spin(9)`-type | 4 | no | chirality dead |
| 1 (closed orbit) | `Spin(10)` | **5** | yes | chirality alive, **rank too high** |

**A single 27 VEV cannot give both rank 4 and a complex 27.** Rank 4 requires the generic strata,
which give real `F₄`/`Spin(9)`; the complex-preserving stratum is the closed orbit, which stops at
rank 5. **Two rank-1 VEVs are needed, and this is forced, not a modelling preference** — which is
why the prior panel's route requires exactly two. That is a genuine structural statement and it
now has an orbit-theoretic derivation rather than being a bookkeeping observation.

### Q5e. Not located — recorded honestly

Two items could not be confirmed to exist and **must not be cited** without further checking:

- "Buccella–Ruegg–Savoy, *Rank 5 and 6 subgroups of E₆*" — repeated author/title/full-text
  searches on INSPIRE returned nothing. The related Buccella–Ruegg *Group Theoretic Determination
  of Minima of Higgs Potentials* (Nuovo Cim. A 67 (1982) 61, INSPIRE 165933) exists but its own
  abstract restricts to `O(8+2n)`, `SU(3+n)`, `O(14)` — **not E₆**.
- Any "Babu–Bajc–Saad" E₆ paper — no matching INSPIRE record found under any search tried.

Also flagged: **Slansky**, Phys. Rept. 79 (1981) 1 (1466 citations) and **Hewett–Rizzo**,
Phys. Rept. 183 (1989) 193 (1524 citations) are certainly relevant and are cited from reputation;
their tables could **not** be accessed by this sweep (pre-arXiv, no full text via INSPIRE). Treat
their content as textbook-reputation, not verified here.

---

## Bibliography — what each source establishes, and under what assumptions

**Primary text read in full or in the relevant sections (highest confidence):**

| Source | Establishes | Assumptions / scope |
|---|---|---|
| **Baez, *The Octonions*, Bull. AMS 39 (2002) 145; arXiv:math/0105155** — LaTeX source read, §§3.4, 4.2, 4.4 | rank = trace for projections; `𝕆P²` = trace-1 projections = primitive idempotents; `dim 𝕆P² = 16`; explicit `p = vv*` form; Freudenthal's `p × p = 0`; `det` formula; `𝕆P² = F₄/Spin(9)`; `F₄ = Aut(h₃(𝕆))`; `E₆₍₋₂₆₎ = Coll(𝕆P²)`; `(ℂ⊗𝕆)ℙ² = E₆/((Spin(10)×U(1))/ℤ₄)`; `e₆ ≅ so(10) ⊕ u(1) ⊕ S₁₀` | Survey, but constructions are explicit and checkable. **Caveat: its "collineations fixing a point = `Spin(9,1)`" names the Levi's semisimple part, not the full 62-dim isotropy group** (see Q1b). |
| **Ferrara & Günaydin, hep-th/9708025** — LaTeX source read, §2 | the complete 3-orbit rank stratification of the 27 with dimensions and little groups; `E₆₍₆₎/F₄₍₄₎` generic; rank-1 orbit is 17-dim with stabiliser `O(5,5) ⋉ T₁₆` | Split real form `E₆₍₆₎` (supergravity context). Transfers to compact/complex by taking the corresponding real form; dimensions are form-independent. |
| **King, Moretti, Nevzorov, hep-ph/0510419** (+ review 2002.02788) — full text read | the VEV direction is *assumed*; D-flatness constrains only; **"one cannot break E6 in a conventional manner as the required Higgs fields are in larger representations than the 27"**; the `SU(5)×U(1)_N` decomposition; exotics `D,D̄`; B/L violation not gauge-forbidden | SUSY, E₆SSM-specific model choices (wants a TeV `Z′`). Its rank-5 stall is partly a design choice — see Q5b. |
| **Callaghan & King, arXiv:1210.6913** — full text read | F-theory E₆: flatness imposed as constraint with free integer choices remaining; breaking by flux, not by a Higgs potential; proton decay suppressed geometrically | F-theory construction; conclusions are about that framework. |

**Retrieved and used at abstract/metadata level (lower confidence, flagged in text):**

| Source | Establishes | Status |
|---|---|---|
| Miyasaka & Yokota, arXiv:1011.0603 | `F₄` diagonalises any element of `J₃(𝕆)`; constructive proof | abstract read; corroborates Baez's construction |
| Zak, *Severi varieties* (1985); *Tangents and Secants* (1993) | the complex Cayley plane `E₆/P₁` is one of exactly four Severi varieties | zbMATH; classification taken on reputation |
| J. S. Kim, J. Math. Phys. 25 (1984) 1694 | orbit-space stratification of the 27 of `E₆`; minima forced toward higher-little-group strata | abstract only, pre-arXiv |
| Kim & Gell-Mann, INSPIRE 178410 | Michel–Radicati: critical points sit at enhanced-symmetry orbits | abstract only |
| Elkies & Gross, IMRN 1996 (OpenAlex `W2995339545`) | integral structure on `J₃(𝕆)`; the "exceptional cone"; link to Leech/Niemeier | **complete 39-paper citing set enumerated**; full text not read |
| Elkies & Gross, Duke 2001 | cubic rings embedded in the integral Albert algebra | zbMATH |
| Garibaldi, Petersson, Racine, arXiv:2205.09896 | Albert algebras over ℤ and arbitrary base rings | abstract read |
| Krutelevich, math/0411104 | integral Freudenthal construction; algorithmic orbit spaces over ℤ; Bhargava link | abstract read |
| Kato & Yukie, arXiv:1603.00739 | **rational orbits of *pairs* of 27s classified by cubic étale algebras** | abstract read — sharpest arithmetic lead for the two-VEV configuration |
| Moore, hep-th/9807087 | arithmetic (CM) points distinguished in CY moduli space | Q3 control; does not concern representation-space directions |
| Donagi & Wijnholt, 0808.2223 | hypercharge flux breaking is a topological constraint | not a Higgs VEV (see Q3) |
| Hebecker & March-Russell, hep-ph/0107039 | orbifold breaking ≅ Wilson-line breaking; automorphism is an input | — |
| Singh, arXiv:2508.10131 | mass ratios from the Jordan cubic **after** assuming a diagonalised `⟨X⟩` | nearest bridge; direction assumed, not derived |
| Springer & Veldkamp (2000); Jacobson (1968); Freudenthal (1951); Tits (1953); Rozenfeld (1954) | the standard Albert-algebra / Cayley-plane theory | **control set** — retrieved, establishing the sweep works |

**Re-derived in-sandbox (independent of any source):** the branching `27 → 10+5+5̄+5̄+1+1` under
`SU(5)` and the absence of the `24`; the hypercharge-neutrality obstruction to `SU(5) → SM`;
all orbit/stabiliser dimension identities in the Q1b and Q1c tables.

---

## What the seat could honestly claim

**Safe — verified against primary text or re-derived here:**

1. Rank-1 elements of `J₃(𝕆)` are exactly the primitive idempotents (trace-1 projections);
   projectively they form `𝕆P²`, `dim 16`; intrinsically `a ≠ 0` with `a# = a × a = 0` (Freudenthal).
2. The stabiliser of a rank-1 **vector** in compact `E₆` is `Spin(10)` (dim 45, orbit 33).
   The stabiliser of the rank-1 **line** is `(Spin(10) × U(1))/ℤ₄`. Prior panel confirmed.
3. `E₆` has exactly **three** nonzero orbits on the 27, labelled by Jordan rank, with little
   groups `F₄` (rank 3), `Spin(9)`-type (rank 2), `Spin(10)`-type (rank 1).
4. **`𝕆P²` is `F₄`-homogeneous** (`= F₄/Spin(9)`), and `F₄` is transitive on Jordan frames.
   Hence no rank-1 element, orthogonal pair, or triple is canonical over ℝ or ℂ.
   **Choosing a VEV direction is exactly a choice with no canonical answer.**
5. The programme's F₄/chirality obstruction is the **generic** stratum; chirality survives only on
   the **closed, measure-zero** rank-1 orbit. A single 27 VEV can never give both rank 4 and a
   complex 27 — hence two VEVs are *forced*.
6. **27 VEVs cannot break `SU(5) → SM`**: the `24` is absent from the 27, and the only
   `Y`-neutral directions are `SU(5)` singlets, which break nothing.
7. In the E₆ GUT literature the VEV direction is **always an input**. So the object's failure to
   supply one is not peculiar to it.
8. Nobody has derived a GUT Higgs VEV direction from arithmetic (certified null, control passed,
   complete citation-graph closure on Elkies–Gross).

**Defensible but must carry its caveat:**

9. Two Jordan-rank-1 27 VEVs give `SU(5)` (rank 4, 27 complex) — **but** in a SUSY context
   D-flatness pairs `27/27̄` and the literature stalls at rank 5; and `SU(5)` is not the SM (see 6).
10. Over ℤ or a number field the rank-1 elements are **not** homogeneous — arithmetic stratifies
    them (Elkies–Gross; Krutelevich; Kato–Yukie's classification of *pairs* of 27s by cubic étale
    algebras). This is the **only** identified route to a distinguished direction, and it is
    unworked.

**Must NOT be claimed:**

- That the object's arithmetic *does* single out a rank-1 element. Nothing here shows that; item 10
  is a motivation for a computation, not a result.
- That deriving a VEV from arithmetic is "novel" in the strong sense. The null is certified for the
  precise question asked; it is not proof that no adjacent work exists under other vocabulary.
- That the two-27 route reaches the Standard Model. It reaches `SU(5)` and provably stops.
- Anything sourced to "Buccella–Ruegg–Savoy, *Rank 5 and 6 subgroups of E₆*" or to a
  Babu–Bajc–Saad E₆ paper — neither was located, and they may not exist as described.
- Baez's "collineations fixing a point = `Spin(9,1)`" as a statement about the full stabiliser.
