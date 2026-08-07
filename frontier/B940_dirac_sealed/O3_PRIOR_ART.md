# O3 — PRIOR-ART SWEEP: has anyone numerically computed a Dirac eigenvalue
# on a hyperbolic 3-manifold?

**Date:** 2026-08-07 · **Seat:** literature agent (adversarial) · **Obligation:**
O3, binding on the banking seat per B940 PREREGISTRATION §"THE 'FIRST' GATE".
**Mandate:** try hard to FIND prior art; a found citation converts OUTCOME A from
a "first" into a "reproduction" and is the MORE valuable result.

---

## (a) VERDICT

**NO PRIOR ART FOUND — for a numerically computed *nonzero* Dirac eigenvalue on
any hyperbolic 3-manifold — at the depth achieved (see §c).**

**But the sweep did NOT come back empty, and the banking seat must read this
before writing any sentence containing "first".** One paper lands close enough
that an unqualified "first Dirac eigenvalue on a hyperbolic 3-manifold" would be
**contestable and should not be banked**:

### The near-miss that constrains the wording

> **Francesco Lin & Michael Lipnowski, "Dirac spectral flow and Floer theory of
> hyperbolic three-manifolds", arXiv:2506.07238 (2025).**

What they actually do (verified against the full text, not the abstract):

- They study a **1-parameter family of spin^c Dirac operators** `D_{B_τ}` on
  **closed** hyperbolic 3-manifolds from the Hodgson–Weeks census (#356, 357,
  381, 734, 735, 790, 882, 1155, 1280, 1284, 3250, 3673, 10867).
- They rigorously, with computer assistance, **certify that a Dirac eigenvalue
  equals exactly zero** at certified parameter values — e.g. for the unique
  self-conjugate spin^c structure on census #357 they prove `s₀(τ) = 0` for some
  **τ ∈ [0.1537, 0.1556]** (and a second crossing at τ ∈ [0.4467, …]).
- Method: the **odd Selberg trace formula** and its derivative, fed by the
  **complex length spectrum computed with SnapPy** up to cutoff R ∈ [7, 8.5]
  (hours to ten days of CPU each), plus Dirichlet-domain geodesic
  triangulations (150–200 tetrahedra).
- They further prove that on the relevant intervals there is a **unique small
  eigenvalue** `s₀(τ)`, and bound it away from zero at interval endpoints.

**Why this is nevertheless not prior art for B940's claim shape:**

1. **Every number they publish is a *parameter*, not an eigenvalue.** The
   quantities `0.1537`, `0.1556`, `0.4467` are values of τ. Tables 1 and 2 report
   volume, systole, `H₁` torsion, and `C_Y` bounds — **no eigenvalue values**.
   There is no "λ = 2.9745…"-shaped number anywhere in the paper.
2. **The only eigenvalue they pin is ZERO** — the kernel. B940's seal
   **explicitly EXCLUDES the kernel (λ = 0, dim 2)** from the claim. The
   exclusion and the prior art land on exactly the same object; this is fortunate
   but must be stated, not relied on silently.
3. **Their manifolds are closed; m004 is cusped.** Different spectral regime
   (Bär's discreteness dichotomy is the whole issue in the cusped case).
4. Their own "first" is claimed for *monopole Floer chain complexes*, not for
   Dirac eigenvalues.

**Consequence for the banked sentence — the safe forms:**

- ✅ SAFE: "first computed **nonzero** Dirac eigenvalue **value** on a hyperbolic
  3-manifold"; "first numerical Dirac **spectrum** on a **cusped** hyperbolic
  3-manifold".
- ❌ DO NOT BANK: "first Dirac eigenvalue on a hyperbolic 3-manifold"
  (unqualified) — Lin–Lipnowski demonstrably locate λ = 0 eigenvalues of Dirac
  operators on hyperbolic 3-manifolds by computer-assisted means.
- Recommended: cite Lin–Lipnowski **positively** in the banked FINDINGS as the
  nearest prior work, and state the distinction (zero-crossing localization on
  closed manifolds vs. a computed nonzero eigenvalue value on a cusped one).
  This is stronger science than an unqualified priority claim.

---

## (d) THE CONTROL — and it came back POSITIVE

The control matters: if the surface literature also contained no computed spinor
eigenvalues, a 3-manifold null would be a search artifact rather than a result.
**It does contain them.**

> **E. Gesteau, S. Pal, D. Simmons-Duffin, Y. Xu, "Bounds on spectral gaps of
> hyperbolic spin surfaces", arXiv:2311.13330 (2023); publ. 2025.**
> zbMATH-reviewed, MSC 53C27, 58J50, 20H10, 11F72.

They compute, numerically, the **first nonzero Dirac eigenvalue** on hyperbolic
spin **surfaces and orbifolds**, via the Selberg trace formula with the geodesic
length spectrum as input (their §4; method credited to Lin–Lipnowski JAMS 2022).

Convention (their §1, verbatim): `λ₁^(1/2) := 1/4 + t₁²`, where `|t₁|` is the
lowest nonzero positive eigenvalue of the Dirac operator.

| surface / orbifold | λ₁^(1/2) computed | ⟹ Dirac eigenvalue t₁ |
|---|---|---|
| `[0;3,3,5]` orbifold | `[19.62850299650, 19.70606979308]` (= 19.669 ± 0.03) | **t₁ ∈ [4.4021, 4.4109]** |
| `[1;3]_sym` | `(8.255, 8.298)` | **t₁ ∈ [2.8293, 2.8369]** |
| Bolza surface (odd spin structure) | Appendix B table | computed |

So: **computed spinor eigenvalues exist in 2D and are absent in 3D.** The null is
meaningful. It is also sharpened by this: the *method* (Selberg trace formula +
length spectrum) was already available and already applied to Dirac in 2D and to
hyperbolic 3-manifolds in the scalar/Floer setting — nobody carried it to a
nonzero Dirac eigenvalue value in 3D.

**The contrast case (also checked):** explicit Dirac spectra on 3-manifolds DO
exist — but only where closed forms exist, i.e. **flat and spherical** ones:
Pfäffle, "The Dirac spectrum of Bieberbach manifolds" (2000); Boldt, "Properties
of the Dirac spectrum on three dimensional lens spaces" (2017); Bär, "The Dirac
operator on space forms of positive curvature" (1996, Killing spinors). None
hyperbolic. This is the expected pattern: hyperbolic 3-manifolds admit no closed
form, so a number there requires numerics — and none was found.

---

## (b) THE SEARCH RECORD

### Databases actually reached

| source | reached? | how |
|---|---|---|
| **zbMATH Open** | ✅ YES | `api.zbmath.org/v1/document/_search`, incl. MSC-code (`cc:`) structured queries; **full reviewer texts retrieved** for many records |
| **MathSciNet** | ❌ **NO** | `mathscinet.ams.org` returns HTTP 302 → subscription auth wall. Not reachable from this environment. |
| OpenAlex | ✅ | ~full corpus; both `search` (**full-text** index) and `title_and_abstract.search`; citation graph via `cites:` |
| arXiv API | ✅ | `export.arxiv.org/api/query` |
| Semantic Scholar | ✅ | graph API |
| INSPIRE-HEP | ✅ | physics/lattice literature |
| DuckDuckGo (general web) | ✅ | saturation cross-check |
| OATD (theses) | ❌ | HTTP 403. Partly mitigated: zbMATH indexes dissertations (it returned Pfäffle's Hamburg PhD thesis). |

> Note: this session's WebSearch tool budget was exhausted (200/200) before this
> task began, so the sweep was run over **raw HTTP against bibliographic APIs**
> instead. This turned out to be *stronger* than keyword search: results are
> verbatim records rather than summaries, and it reached the named zbMATH
> standard plus full-text and citation-graph queries.

### Method 1 — citation-graph traversal (the highest-yield adversarial move)

Any paper numerically computing a Dirac eigenvalue on a hyperbolic 3-manifold
would almost certainly cite **Bär 2000** (the discreteness dichotomy that makes
the problem well-posed). So the **complete citing set was enumerated and read**:

- `cites:W2130197549` → **56 works**; `cites:W2951147165` → 3 works.
- **Result: every one is theoretical.** Spectral theory, index theorems, Weyl
  laws, eigenvalue estimates, degeneration asymptotics, L^p spectra, eta
  regularity. **No numerical eigenvalue computation of any kind.**
- Closest members, each individually checked:
  - **Pfäffle, "Eigenvalues of Dirac operators for hyperbolic degenerations"
    (Manuscripta Math. 2004)** + his Hamburg PhD thesis "Convergence of
    eigenvalues for Dirac operators" (2003). The full zbMATH review confirms:
    a **convergence theorem** (spec of `M_i` → spec of `M` with multiplicity, via
    a spinorial escaping-sets method). **No numbers.**
  - **Park, "Eta invariants and regularized determinants for odd dimensional
    hyperbolic manifolds with cusps" (Amer. J. Math. 2005 / math/0111175).**
    Analytic: regularity at s=0, Selberg zeta of odd type, functional equations.
    **No numerics.** (This closes the "eta invariants sometimes need eigenvalues"
    lead — this line is trace-formula-analytic, never numerical.)
  - **Monk & Stan, "Spectral convergence of the Dirac operator on typical
    hyperbolic surfaces of high genus" (2023/2024).** Random Weil–Petersson,
    spectral *density*, Weyl law. Asymptotic, 2D, **no individual eigenvalues.**

### Method 2 — zbMATH structured / MSC sweep (20 queries)

Notable outcomes (`ZERO_RESULTS` verified to mean zero via a nonsense-query
control returning the same 404):

| query | result |
|---|---|
| `any:Dirac & any:"knot complement"` | **ZERO RESULTS** |
| `any:Dirac & any:"Bianchi group"` | **ZERO RESULTS** |
| `cc:53C27 & any:hyperbolic & any:numerical` | **ZERO RESULTS** |
| `any:spinor & any:eigenvalue & any:hyperbolic & any:numerical` | 1 hit, irrelevant (nuclear pairing code) |
| `any:Dirac & any:"hyperbolic 3-manifold"` | 2 hits, neither spectral-numerical |
| `any:Dirac & any:"hyperbolic three-manifold"` | 1 hit = Lin–Lipnowski |
| `any:"Dirac spectrum" & any:hyperbolic` | 8 hits — Bär, Ginoux survey, Moroianu², Gesteau et al. (2D), Monk–Stan (2D), Pfäffle, Farinelli, Stan (2D) |
| `any:Dirac & any:cusp & any:spectrum` | 16 hits — Bär 2000, Martelli–Reid, Park, Loya–Moroianu–Park, Anghel (2D) … all theory |
| `cc:57M50 & any:Dirac`; `cc:11F72 & any:Dirac`; `ti:"Dirac operator" & any:numerical` | reviewed; nothing hyperbolic-3D-numerical |

Also queried: eta invariants + hyperbolic + numerical; spinor + trace formula +
hyperbolic; harmonic spinor + hyperbolic; `cc:65N25` + hyperbolic manifold.

### Method 3 — reverse direction (who computes spectra on hyperbolic 3-manifolds at all?)

Numerical hyperbolic-3-manifold spectroscopy **exists but is entirely scalar /
integer-spin**:

- Inoue, "Numerical study of length spectra and low-lying eigenvalue spectra of
  compact hyperbolic 3-manifolds" (2000/2001) — **scalar Laplacian**.
- Grunewald–Huntebrinker lineage (the scalar 51.014 anchor B933 cites) — scalar.
- **Bonifacio, Mazáč, Pal, "Spectral bounds on hyperbolic 3-manifolds:
  associativity and the trace formula" (arXiv:2308.11174).** Checked
  specifically: covers the Laplace–Beltrami operator on functions **and powers of
  the cotangent bundle** — **integer spin only, no Dirac.**
- Author-level check for spinor/Dirac crossover on Inoue, Then, Aurich,
  Grunewald, Strohmaier: **none** produced a hyperbolic Dirac numerical spectrum.
  (Strohmaier has Dirac-*type* theory — counting functions, frame flows — not
  hyperbolic numerics.)
- Citing set of the 2D spin bootstrap (arXiv:2311.13330): **1 work**, unrelated.
  **No one has extended the spin bootstrap to 3 dimensions.**

### Method 4 — adjacent literature where a number might hide

- **Eta invariants / spectral flow**: Park; Loya–Moroianu–Park; Millson;
  Hochs–Wang. All analytic/index-theoretic. The only computer-assisted spectral
  flow on hyperbolic 3-manifolds is Lin–Lipnowski (§a).
- **Analytic torsion / Cheeger–Müller for spinor Laplacians**: Park; Ruelle zeta
  for cusped hyperbolic manifolds. Analytic.
- **Quantum chaos / spinor billiards**: "neutrino billiards" are **flat** 2D
  Dirac billiards (graphene-like), not hyperbolic 3-manifolds.
- **Lattice / discretized Dirac**: lattice QCD Dirac spectra live on flat 4-tori;
  "hyperbolic band theory" (Maciejko–Rayan) is 2D hyperbolic lattices. Neither is
  a hyperbolic 3-manifold Dirac spectrum.
- **SnapPy / Regina / Snap tooling**: Snap/SnapPy compute geometry, arithmetic
  invariants and length spectra. **No spinor/Dirac spectral capability exists** in
  this tooling; Lin–Lipnowski and Gesteau et al. both use SnapPy only as a
  *length-spectrum* source feeding a hand-built trace formula.
- **Theses/proceedings**: covered via zbMATH's dissertation indexing (which did
  surface Pfäffle's thesis); OATD unreachable (403).
- **General web engine** (DuckDuckGo) returned the same small set already found
  — a saturation signal.

### Papers read in full text (not just abstract)

1. `arXiv:2506.07238` Lin–Lipnowski — full HTML, ~185k chars extracted, grepped
   for numerics, SnapPy, tables, eigenvalue statements.
2. `arXiv:2311.13330` Gesteau–Pal–Simmons-Duffin–Xu — full PDF via `pdftotext`,
   ~214k chars, §4 numerical method + §5 + Appendix B table read.
3. zbMATH full reviewer texts for Bär 2000, Pfäffle 2003, Martelli–Reid,
   Gesteau et al., Monk–Stan, Park, Lin–Lipnowski.

---

## (c) HONEST DEPTH STATEMENT — for the banked caveat, verbatim-ready

> **Prior-art depth (O3, 2026-08-07).** The sweep reached **zbMATH Open**
> (including MSC-classified structured queries and full reviewer texts),
> **OpenAlex** (full-text index and citation graph), **arXiv**, **Semantic
> Scholar**, **INSPIRE-HEP**, and a general web engine; it enumerated and read
> the **complete citing set of Bär 2000** (59 works) and read two decisive papers
> in full text. **MathSciNet was NOT reachable** (subscription auth wall,
> HTTP 302), so the standard named in the B933 seal is **half met: zbMATH-grade
> yes, MathSciNet-grade no.** Within that depth, **no numerically computed
> nonzero Dirac eigenvalue on any hyperbolic 3-manifold was found**, while the
> must-pass control returned computed first Dirac eigenvalues on hyperbolic
> *surfaces/orbifolds* (Gesteau–Pal–Simmons-Duffin–Xu 2023), confirming the null
> is not a search artifact. The nearest prior work on 3-manifolds is
> **Lin–Lipnowski (arXiv:2506.07238)**, which certifies **zero** eigenvalues
> (spectral-flow crossings) of spin^c Dirac operators on **closed** hyperbolic
> 3-manifolds without computing any eigenvalue value.

### Residual risk — what could still be out there

Stated plainly, because a negative is only as good as its stated limits:

1. **MathSciNet not consulted.** Its review corpus overlaps zbMATH heavily but is
   not identical.
2. **A number buried in a body/appendix** of a paper whose title, abstract and
   review never mention it would be missed by metadata search. *Partly mitigated*:
   OpenAlex's default `search` is a full-text index and was used in group A.
3. **Language and era bias.** English-dominant; older print proceedings and
   non-indexed lecture notes are thin. (Mitigated: zbMATH indexes German/French
   theses well, and did return German-language work.)
4. **Paywalled full text** could not be searched systematically.
5. **Physics-side obscurity**: a Dirac spectrum on a compact hyperbolic 3-space
   could hide in an old quantum-cosmology paper under different vocabulary
   ("fermionic eigenmodes of a compact hyperbolic universe"). INSPIRE queries on
   this returned nothing, but the vocabulary space is large.

None of these is a reason to withhold OUTCOME A; all are reasons to keep the
qualifier **"nonzero"** (and preferably **"cusped"**) in any sentence using
"first", and to cite Lin–Lipnowski explicitly.

---

## Bibliography of everything materially checked

**Theory, hyperbolic Dirac (no numerics):**
- C. Bär, *The Dirac operator on hyperbolic manifolds of finite volume*,
  J. Differential Geom. **54** (2000) 439–488. Zbl 1030.58021.
- F. Pfäffle, *Eigenvalues of Dirac operators for hyperbolic degenerations*,
  Manuscripta Math. (2004); and *Convergence of eigenvalues for Dirac operators*,
  PhD thesis, Hamburg (2003).
- B. Martelli, A. W. Reid, *The Dirac operator on cusped hyperbolic manifolds*
  (2022/2025) — spin structures on cusps, bounding vs Lie; applies Bär's
  dichotomy. **No eigenvalues.**
- J. Park, *Eta invariants and regularized determinants for odd dimensional
  hyperbolic manifolds with cusps*, Amer. J. Math. **127** (2005).
- P. Loya, S. Moroianu, J. Park, *Regularity of the eta function on manifolds
  with cusps*; *Adiabatic limit of the eta invariant over cofinite quotients of
  PSL(2,R)* (2008).
- N. Ginoux, *The Dirac spectrum*, Springer LNM 1976 (2009) — survey.
- A. Moroianu, S. Moroianu, *The Dirac spectrum on manifolds with gradient
  conformal vector fields* (2007); S. Moroianu, *Weyl laws on open manifolds*.
- R. Camporesi, E. Pedon, *Harmonic analysis for spinors on real hyperbolic
  spaces* (2001) — eigenfunctions on **H^n itself** (continuous spectrum), not a
  finite-volume quotient.

**2D Dirac numerics (the positive control):**
- E. Gesteau, S. Pal, D. Simmons-Duffin, Y. Xu, *Bounds on spectral gaps of
  hyperbolic spin surfaces*, arXiv:2311.13330 (2023); publ. 2025.
- J. Bolte, H.-M. Stiepan, *The Selberg trace formula for Dirac operators*,
  J. Geom. Phys. (2006) — trace formula for compact hyperbolic **surfaces**;
  symmetry/multiplicity; relation to Maass–Laplace spectra. **Theory, no computed
  spectra** (confirms B933's characterization).
- R. Stan, *The Selberg trace formula for spin Dirac operators on degenerating
  hyperbolic surfaces* (2022/2025); L. Monk, R. Stan (2023/2024);
  C. Anghel, *On the Dirac spectrum on degenerating Riemannian surfaces* (2024).

**3-manifold Dirac, computer-assisted (the near-miss):**
- F. Lin, M. Lipnowski, *Dirac spectral flow and Floer theory of hyperbolic
  three-manifolds*, arXiv:2506.07238 (2025).
- F. Lin, M. Lipnowski, *The Seiberg–Witten equations and the length spectrum of
  hyperbolic three-manifolds*, JAMS **35** (2022) 233 — λ₁* of the Hodge
  Laplacian on **coexact 1-forms**, lower bounds. Not Dirac eigenvalues.
- F. Lin, M. Lipnowski, *Closed geodesics and Frøyshov invariants of hyperbolic
  three-manifolds* (2025).

**Scalar / integer-spin 3-manifold numerics (reverse direction):**
- K. T. Inoue, *Numerical study of length spectra and low-lying eigenvalue
  spectra of compact hyperbolic 3-manifolds* (2000/2001).
- J. Bonifacio, D. Mazáč, S. Pal, *Spectral bounds on hyperbolic 3-manifolds*,
  arXiv:2308.11174. J. Bonifacio, *Bootstrap bounds on closed hyperbolic
  manifolds* (2022).
- Coulson, Goodman, Hodgson, Neumann, *Snap* (2000) — arithmetic invariants.

**Computed Dirac spectra on NON-hyperbolic 3-manifolds (the contrast):**
- F. Pfäffle, *The Dirac spectrum of Bieberbach manifolds* (2000) — flat.
- S. Boldt, *Properties of the Dirac spectrum on three dimensional lens spaces*
  (2017) — spherical.
- C. Bär, *The Dirac operator on space forms of positive curvature* (1996);
  *Dependence of the Dirac spectrum on the spin structure* (2000).
- R. Podestá, eta series / Z_2^k-manifolds (2005, 2006).

**Checked and excluded:** M. Dahl, *Dirac eigenvalues for generic metrics on
three-manifolds* (2003) — genericity/simplicity, no hyperbolic numerics; lattice
QCD Dirac spectra (flat tori); neutrino/Dirac billiards (flat 2D);
Maciejko–Rayan hyperbolic band theory (2D lattices).
