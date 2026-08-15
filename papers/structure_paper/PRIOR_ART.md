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

## 3. What remains open

1. ## **The `T-TWOTEETH` caveat applied to `m²+4`** — the one that could bite. Does B997's
   own-shadow-modulus filter have the same discriminant-vs-antipalindromic-CF gap that the
   registry flags for the twisted Markov spectrum? **Not yet checked.**
2. **`T-GIES-FAM`, `T-COHN`'s metallic reading, `T-CHAIN`'s framing** — NEEDS-LIT.
3. **10 EMPTY rows** in the novelty sweep, `T-MAGIC` among them.
4. **Seven `STANDARD` entries in `refs.bib`** — bibliographic data from memory, blocking.
5. **B727's class-consuming step** — the third entrance claim, not yet searched.

**None of these is a reason to stop drafting. All of them are reasons not to submit.**
