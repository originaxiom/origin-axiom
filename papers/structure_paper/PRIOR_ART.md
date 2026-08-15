# PRIOR ART — what the paper must cite, and what it may claim

*Opened 2026-08-15, during the hardening run. **This file exists because P5 died of exactly
the gap it closes**: a lit-gate reported "no prior art found" while Baake–Grimm–Joseph 1993
contained P5's spine verbatim. The post-mortem — *"the gate named the right person; I asked the
wrong question of him"* — is the standard this file is held to.*

---

## 0. The finding that prompted it

**`docs/THEOREM_REGISTRY.md` is the programme's prior-art spine, and the paper had never been
written against it.** The registry carries a novelty-status column with **GATED /
PARTIALLY-KNOWN / DERIVABLE / KNOWN** dispositions and *named sources*, for claims §§2–5 of
this paper make. Nineteen further rows are bare **NEEDS-LIT**.

`docs/NOVELTY_SWEEP_LEDGER.md` — which the paper plan had treated as *the* novelty record — is
a **different and narrower instrument**: 19 algebra-layer `T-*` theorems, of which **only 9
carry a disposition; 10 rows are EMPTY**, including **`T-MAGIC`**, the magic-square
identification that is this paper's §7.2.

**And there is a third, older than both.** `docs/NOVELTY_AUDIT.md` (2026-06-09) is a deep
adversarial pass — fan-out search → fetch → three-vote verification → cited synthesis — with a
proper verdict enum and **65 graded verdicts: 22 KNOWN · 16 NEEDS-SPECIALIST · 14 APPEARS-NOVEL
· 13 PARTIALLY-KNOWN**. Its stance is the right one (*"assume known, try hard to find prior art
before concluding novel"*), and **its CLAIM 2 directly constrains §5.3** — see §2.4 below.

> **So the programme has THREE prior-art instruments, built at three different times, and no
> single document points at all three.** That is the retrieval failure in its purest form: the
> work exists, is good, and is not reachable from where a writer stands. **This file is the
> index that was missing**, and the paper is now written against all three.

> **Consequence for the paper, stated plainly: "the novelty sweep established that the
> algebra layer is standard" is true of the rows that were swept and NOT of the rows that were
> not.** §7 must cite Barton–Sudbery directly (it now does) rather than lean on a ledger row
> that is blank.

---

## 1. The genesis half — exposure the drafts did not carry

Every row below is from `THEOREM_REGISTRY.md` and was **not** referenced in any §-draft before
today.

| paper site | registry row | disposition and named prior art | what this costs the paper |
|---|---|---|---|
| **§3.2** self-selection via the Lagrange spectrum | `T-TWOTEETH` | ## **W0 GATE DONE — PARTIALLY-KNOWN**, "a one-corollary repackaging of **Andersen–Duke 2019** (Markov spectra for modular billiards) **+ Markov**" | §3.2 must not read as a new spectral theorem. The extremality of `√5` is Hurwitz/Markov; ours is the *application* to grammar selection |
| **§3.2**, and **§5.4**'s `m²+4` | `T-TWOTEETH` **caveat** | ## *"`2√2` is realized by BOTH det(−1) disc-8 AND non-det(−1) disc-32 forms ⟹ the proof must be about **antipalindromic-CF square-roots**, not disc `v²+4`"* | ## **A live caveat against a discriminant-only argument.** B997 evaluates each grammar at `m²+4`. Whether that filter has the same gap is **an open question this paper must not paper over** |
| **§2.2 (C5)**, the Gieseking price | `T-GIES-FAM` | **NEEDS-LIT** — "non-orientable punctured torus bundle orientation double cover"; Gieseking family literature | The C5 fork is stated as a *family* fact in the registry (every metallic bundle double-covers a non-orientable one). Un-lit-checked |
| **§3.3–3.4** the monodromy pair | `T-UNIQ` | **GATED, PARTIALLY-KNOWN** — mechanism classical (Sarnak; Gehring–Martin; Goldman/Fricke); ## **the `(1,2)` instance is VERBATIM in Reutenauer 2009/2019** (the Markoff morphism) | ## The sharpest single warning in the registry: one of the programme's statements already exists *verbatim* in print |
| trace-map background | `T-COHN` | **KNOWN core (Cohn 1955)**; the metallic reading NEEDS-LIT | cite Cohn |
| the Markov-cubic spine | `T-CHAIN` | Fricke/Markov **classical**; the body-tower framing NEEDS-LIT | cite Fricke/Markov |

---

## 2. The entrance (§5.3, §5.4) — the paper's only novelty claim

### 2.1 §5.3 — the geometry is **not ours**, and the draft now says so

The figure-eight cone-manifold family (hyperbolic below cone angle `2π/3`, **Euclidean exactly
at `2π/3`**, spherical beyond) is **Thurston**, with the figure-eight cone manifolds due to
**Hilden–Lozano–Montesinos** and the degenerations to **Hodgson** and **Porti**. B248's own
FINDINGS cited all of them; the §5.3 draft had dropped the line and has been corrected.

**Ours is only: which arithmetic sits at each end.**

### 2.2 §5.4 — a real prior-art neighbourhood, newly found

**The corpus did not know this literature.** `Dechant` returns zero hits corpus-wide; the only
`Baez` on record is an unrelated `F₄ → SM` paper.

| source | what it establishes |
|---|---|
| **Baez**, *From the Icosahedron to E₈*, arXiv:1712.06436 | the icosahedron → `2I` → `E₈` route, expository and explicit |
| **Dechant**, *The birth of E₈ out of the spinors of the icosahedron*, Proc. R. Soc. A **472** (2185) 20150504 (2016); arXiv:1602.05985 | the 240 `E₈` roots built from the 240 pinors doubly covering the icosahedral group |
| **Dechant**, *The E₈ geometry from a Clifford perspective*, arXiv:1603.04805 | same programme, Clifford-algebraic |
| **Dechant**, *From the Trinity (A₃,B₃,H₃) to an ADE correspondence*, arXiv:1812.02804 | Platonic trinity → `E₆,E₇,E₈` via spinors + McKay — **adjacent to B248's Arnold-trinity reading** |

> ## **Disposition: the DESTINATION is well-trodden.** "Golden ratio ↔ icosahedral ↔ `2I` ↔
> `E₈`" is an established cluster with a named literature, and `2I → E₈` by McKay is classical.
> **§5.4 must cite it and must not present arrival there as surprising** — which is consistent
> with §1.3, already conceding that arrival is generic.
>
> ## **What is NOT found in that literature: `SL(2,ℤ/N)`, congruence subgroups, the cusp conductor, or the shadow modulus.**
> Checked directly against arXiv:1812.02804 — absent. B997's statement is not "the golden is
> connected to `E₈`" (known) but **"over the family `RᵐLᵐ`, each grammar evaluated at *its own*
> shadow modulus `m²+4`, exactly one lands"** — a selection statement about a family and a
> modulus. **That is the claim to defend, and it is a different claim.**

### 2.4 The asymmetry of the two ends — `NOVELTY_AUDIT`'s CLAIM 2

Found 2026-08-15, carried into §5.3 as **Scope 5.3′**, and **it runs opposite to the direction
the phrasing invites.**

| end | field | group surjection from `π₁(4₁)` |
|---|---|---|
| hyperbolic / `E₆` | `ℚ(√−3)` | ## **YES — `π₁(4₁) ↠ 2T`, exactly two quotients** |
| spherical / `E₈` | `ℚ(√5)`, `det = 5` | ## **NO — `2I → 0`, and `A₅ → 0`** |

Established by direct computation (GAP `GQuotients`) on the programme's own bench, banked as
the B266 correction. **The two ramified-prime reductions are symmetric as fields and NOT as
group surjections.** Stuebner, arXiv:2502.06488, is cited as *context* — it treats binary
icosahedral and `A₅` representations of hyperbolic integral homology spheres, not this knot.

**Consequence carried in §5.4:** B997's `E₈`-end object is **not a quotient of the knot group at
all**. That is not a defect in the theorem — B997 quantifies over **grammars** `RᵐLᵐ` and
`SL(2,ℤ/N)`, never over manifolds — but the paper must not let the surrounding discussion of
`m004` blur it.

### 2.3 Corrections banked during this pass

- ## **`E₇ = 2O` never occurs.** `|SL(2,𝔽_p)| = p(p²−1)` is never `48` (**B207**, 2026-06-25;
  L105 refines `2O` to a *quotient*; CLAIMS E11's GAP census finds it absent). And though
  `|SL(2,ℤ/4)| = 48 = |2O|`, that group has **seven** involutions where a finite `SU(2)`
  subgroup has exactly **one** — an order coincidence, verified here, closing the composite-
  modulus case B207's prime-field argument does not reach. Registry row 10.
- **The golden's shadow is the McKay group for TWO independent reasons** (B1002): the order
  count, *and* B675's quantization-index law, `gcd(cusp conductor, shadow modulus) = gcd(4,5) = 1`
  ⟹ the reduction is an isomorphism. Recovered into §5.4.1; it had never reached the draft.

---

## 2.5 The adversarial read (2026-08-15) — and it moved the frame

Run against §5.4 and §3, with the registry's own `T-UNIQ` warning as the first item.
**It changed which literature the entrance claim has to be defended against.**

> ## **The nearest prior art is not the icosahedron/`E₈` literature. It is the
> Christoffel/Sturmian-morphism literature.**
>
> The metallic grammars `RᵐLᵐ` **are Sturmian morphisms**, hence positive
> automorphisms of `F₂` — and that is precisely the subject of Part II of Reutenauer,
> *From Christoffel Words to Markoff Numbers* (Oxford, 2019): finite Sturmian words,
> the free group on two generators, Christoffel bases, Nielsen's criterion, Sturmian
> morphisms, positive automorphisms. Part I is the classical Markoff theory, and the
> Christoffel↔Markoff link goes back to **Frobenius (1913)**.
>
> **§3's entire apparatus is the subject of a 2019 Oxford monograph**, and the drafts
> cited it nowhere. A referee in this area knows that book on sight. Now cited in
> §3 and in the built paper, with an explicit *"nothing in this section is offered
> as new."*

**The `T-UNIQ` warning, resolved for this paper.** The registry flags that the
`(1,2)` instance of `tr[A_m,A_n] = 2 − (mn(n−m))²` is **verbatim in Reutenauer**.
Checked: **this paper does not make that claim** — §3 uses `M = [[2,1],[1,1]]` and
Thurston/Riley, not the commutator-trace parametrization. **The warning bites a
different programme claim, not the paper.** Recorded so the next writer does not
re-import it.

**The residue, and it is deliberately left open rather than cleared:**

| source | status |
|---|---|
| Reutenauer 2019 (monograph) | **RESOLVED** and now cited |
| `Christoffel Matrices and Sturmian Determinants`, arXiv:2409.09824 (2024) | ## ✅ **OPENED IN FULL — CLEARED** |

**Read in full 2026-08-15, not judged from its abstract.** It is a different object
at every step:

| | arXiv:2409.09824 | B997 (§5.4) |
|---|---|---|
| the matrix | the **Burrows–Wheeler** matrix of a Christoffel word: `n × n`, rows = the word's conjugates in lex order, `n` = the **word length** | the word's **`2 × 2` `SL(2,ℤ)` monodromy** |
| the group | a commutative subgroup of `GL_n(K)`, `≅ K* × K* × G_n`, `G_n` the maps `x ↦ rx` on `ℤ/nℤ` | `SL(2, ℤ/N)` |
| the modulus | `n`, the **word length** (and `F_m` in the Fibonacci application) | `m² + 4`, the **discriminant of the metallic ratio** |
| the invariant | `det = ((n−r)a+rb)(b−a)^{n−1}\,\mathrm{sgn}(ω_r)`, the sign being the **Zolotareff symbol** (a Jacobi generalisation) | whether `\|SL(2,ℤ/(m²+4))\|` is a **McKay-group order** |

Verified absent from the full text: `SL(2,ℤ/N)`, congruence subgroups, congruence
images, binary polyhedral groups, McKay, `E₆/E₇/E₈`, metallic ratios, `m²+4`. **The
only thing shared is the shape** — *word → matrix → reduce mod something →
number-theoretic invariant* — **and the matrix, the modulus and the invariant are
each different.**

*(One near-coincidence, recorded so a later reader does not mistake it for an
overlap: their Fibonacci application reduces mod `F_m`, and `F₅ = 5 = 1²+4` is the
golden's shadow modulus. The indexings are unrelated — theirs by word generation,
B997's by the metallic discriminant.)*

> ## **Verdict on the entrance claim: NOT-FOUND, and now CLEARED against the nearest
> candidate.** Both bounding literatures have been searched — the icosahedron/`E₈`
> cluster and the Christoffel/Sturmian-morphism literature — and the nearest paper in
> the nearer one has been read end to end. The step *each grammar evaluated at its own
> shadow modulus* was not found in either. **This is a not-found at the standard the
> 19 rows were held to, not a search that stopped early.**

## 3. What remains open

1. ## ✅ **The `T-TWOTEETH` caveat applied to `m²+4` — CHECKED 2026-08-15, and it comes out in
   the paper's favour.** The conflation the registry warns about is **real at the field level**:
   `1²+4 = 5`, `4²+4 = 20 = 2²·5`, `11²+4 = 125 = 5³` all have squarefree kernel `5`, so
   **`m = 1, 4, 11` all give `ℚ(√5)`** — the exact analogue of "`2√2` from both disc 8 and disc
   32", and independently banked from the other side by B207 (*"only `E₈` (`ℚ(√5)`, m = 1, 4,
   11) is hit"*). **But the group-level filter separates them**, which a discriminant-level one
   cannot:
   ```
        |SL(2,ℤ/5)|   =     120 = |2I|   ← lands
        |SL(2,ℤ/20)|  =    5760          ← does not
        |SL(2,ℤ/125)| = 1875000          ← does not
   ```
   **B997 survives precisely because it is a statement about the group at the modulus, not
   about the field of the discriminant — which is also why B993's field-level genericity does
   not touch it.** Locked as
   `test_the_filter_is_finer_than_the_field_discharging_the_registry_caveat`.
2. **`T-GIES-FAM`, `T-COHN`'s metallic reading, `T-CHAIN`'s framing** — NEEDS-LIT.
3. **10 EMPTY rows** in the novelty sweep, `T-MAGIC` among them.
4. **Seven `STANDARD` entries in `refs.bib`** — bibliographic data from memory, blocking.
5. **B727's class-consuming step** — the third entrance claim, not yet searched.
6. ## ✅ **arXiv:2409.09824 — READ IN FULL 2026-08-15, CLEARED.** See §2.5.

**None of these is a reason to stop drafting. All of them are reasons not to submit.**
