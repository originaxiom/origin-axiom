# Novelty / prior-art audit (2026-06-09, B134/V123; R4 appended 2026-06-11)

A deep, adversarial literature pass (fan-out web search → fetch → 3-vote verification → cited synthesis) on whether the
project's clean recent results are genuinely new or already in the literature. **Purpose:** stop re-deriving known
mathematics; locate where the real novelty is; cite prior art. Verdict enum: **KNOWN / PARTIALLY-KNOWN / APPEARS-NOVEL
/ NEEDS-SPECIALIST**. Adversarial stance: assume known, try hard to find prior art before concluding novel.

This is a reference note (motivation/provenance), not a claim. Nothing here promotes to `../CLAIMS.md`.

> **Section R4 (2026-06-11)** extends the audit to the one previously-unassessed result — the degree=rank / `Aₙ`
> A-polynomial family (`L=−M⁴`), the "main new result" the SLN paper skeleton flagged "the #1 thing to check." It is an
> **AI adversarial literature read** (WebFetch/WebSearch of the primary sources), and it **de-risks but does not close**:
> it finds the *findable* prior art and frames the residue with confidence levels, but a clean APPEARS-NOVEL here is
> still one same-kind-of-mind verdict — the final close needs a specialist (the Falbel / Heusener–Muñoz–Porti /
> Bergeron–Falbel–Guilloux circle) and/or the user's by-hand read (the H2 lead).

---

## R1 — the chirality recursion (B128 / `../knowledge/K011`) — **PARTIALLY-KNOWN** (mechanism known; block-lift novel)

**Claim audited:** a metallic-block bundle `R^{m₁}L^{m₁}…R^{m_k}L^{m_k}` is amphichiral ⟺ the block-length sequence
`(m₁,…,m_k)` is a cyclic palindrome.

- **Prior art (the mechanism):** **Goodman–Heard–Hodgson, "Commensurators of cusped hyperbolic manifolds,"
  Experimental Math. 17(3) (2008), arXiv:0801.4815** — classify the symmetries of a once-punctured-torus bundle by its
  L/R monodromy word: **anti-palindromic** word (reverse = L↔R swap, cyclically) ⟺ orientation-**reversing** symmetry
  (amphichiral); **palindromic** word ⟺ orientation-preserving π-rotation. The figure-eight `RL` is the canonical
  anti-palindromic/amphichiral example. **This is the exact engine** behind the recursion → the *principle* is not new.
- **Neighboring prior art:** **Kauffman–Lambropoulou (math/0212011, L'Enseignement Math. 2004)** — achiral rational
  knots ⟺ even-palindromic continued fractions (called a "well-known result"); palindrome↔amphichirality is
  long-established in the 2-bridge / continued-fraction setting.
- **The novel kernel:** the lift to the **integer block-length sequence** being a cyclic palindrome is **not stated**
  in the located literature (Guéritaud–Futer math/0406242 give the LR-word formalism but no amphichirality criterion;
  Lackenby math/0112221; full-text scans show no palindrome/chirality discussion). 
- **Status (B134):** now **PROVED** as an elementary corollary of GHH 2008 (see `../frontier/B134_chirality_recursion_proved/`).
  The lift is the project's contribution; the chirality mechanism is GHH's.
- **Open / needs-specialist:** confirm GHH state the criterion as an **iff** for all these bundles; check whether
  Bowditch (arithmetic punctured-torus bundles) or Hoste–Shanahan (twist knots) state a block-sequence/continued-fraction
  palindrome criterion not surfaced here.

## R2 — the two-seed fork (B131 / `../knowledge/K014`) — **KNOWN** (with a framing qualification)

**Claim audited:** gluing two distinct once-punctured-torus bundles along cusp tori discretizes `κ` (intersection of
two distinct A-polynomial curves); same-seed glue stays a continuum.

- **Prior art (the mechanism):** **Kitano–Nozaki, "Finiteness of the image of the Reidemeister torsion of a splice,"
  Ann. Math. Blaise Pascal 27(1) (2020), arXiv:1904.02559** — finiteness via the two pieces' A-polynomial curves
  intersecting in the boundary-torus character variety; `gcd(A_{K1}(L,M), A_{K2}(M,L)) = 1` ⟹ finite (Bézout). Exactly
  the posited transverse-intersection mechanism. Corollary extends to all 2-bridge pairs.
- **Qualification (verified in B134):** Kitano–Nozaki's discreteness is driven by the meridian↔longitude-**swapping
  splice** gluing, **not** by the pieces being distinct — a same-knot splice `Σ(K,K)` is already finite; only the
  identity-glued double stays a continuum. So B131's **"heterogeneity makes the choice" is correct only for the
  identity gluing**; the general statement is *the gluing map* determines continuum-vs-discrete. (Verified: swap-glue
  fig8-to-fig8 → `P=f(f(P))`, degree 16, discrete; identity-glue same-seed → continuum.) B131 annotated accordingly.
- **Status:** the phenomenon is KNOWN; B131's math stands; its framing is qualified (gluing-map-dependent).

## R3 — the SU(2)_k field content (B132 / `../knowledge/K015`, corrected) — **KNOWN / standard**

**Claim audited:** the cyclotomic field of `ρ_k(monodromy)` eigenvalues for torus bundles is controlled by the
T-matrix root of unity (word spin-content mod 4), not chirality.

- **Prior art:** **Jeffrey, Comm. Math. Phys. 147 (1992)** — torus-bundle invariant `Z = Tr ρ(U)` is an explicit
  finite Gauss sum, cyclotomic content governed by `Tr U ∓ 2` and level `k+2`. **Dong–Lin–Ng, Algebra & Number Theory
  9(9) (2015), arXiv:1201.6644** — the modular SL(2,ℤ) representation has kernel a congruence subgroup of level
  `n=ord(T)` and is ℚ(ζₙ)-rational (resolving Coste–Gannon; corroborated by Bantay 2003, Ng–Schauenburg).
  **Lawrence–Zagier, Asian J. Math. 3 (1999)** — WRT invariants lie in ℚ(ζ) and are Galois-equivariant.
- **Status:** the general fact (cyclotomic, T-matrix-governed, chirality-irrelevant) is **firmly KNOWN/standard**. The
  specific "ℚ(i) at spin-content 2 mod 4" is a corollary-level refinement (verify directly from the T-matrix
  conformal weights `h_j = j(j+1)/(k+2)`, not a verbatim citation). This *confirms* the B133 correction: the B132
  content is standard quantum topology, not a chirality property.

## R4 — the degree=rank / `Aₙ` A-polynomial family (B71 / B83 / B89) — **split: n≤3 KNOWN; SL(4) `L=−M⁴` + the family APPEARS-NOVEL / NEEDS-SPECIALIST**

**Claim audited:** on the figure-eight's principal Dehn-filling component, the longitude eigenvalue is a power of the
meridian eigenvalue — `L = (−1)ⁿ⁻¹ Mⁿ` (`degree = rank`), unifying SL(2) (Cooper–Long), SL(3) (Falbel), and SL(4)
(`L=−M⁴`, the claimed-new instance). Three sub-pieces, separately:

**(i) the `Aₙ` family `L=(−1)ⁿ⁻¹Mⁿ` / `L=−M⁴` (the lead).**
- **Prior art — n=2:** the classical figure-eight A-polynomial `L²M⁴ + L(−M⁸+M⁶+2M⁴+M²−1) + M⁴` (Cooper–Culler–Gillet–
  Long–Shalen). KNOWN. Note it is the full 2-variable polynomial, **not** of the form `L=±Mⁿ` — the `degree=rank`
  components are an `n≥3` phenomenon (the repo itself records SL(2) as degenerate here, A0/B73), which slightly weakens
  "unifies SL(2)".
- **Prior art — n=3:** the two exceptional-Dehn-filling components and the boundary-torus projection are
  **Heusener–Muñoz–Porti, "The SL(3,C)-character variety of the figure eight knot," arXiv:1505.04451** (five 2-dim
  components; "two are induced by exceptional Dehn fillings") and **Falbel–Guilloux–Koseleff–Rouillier–Thistlethwaite,
  arXiv:1412.4711** (the explicit boundary-torus projection). The repo's `L=M³` (D2) / `M³L=1` (D3) are the reading of
  these components — **KNOWN** (and correctly attributed to Falbel in the repo). *(The H2 lead's `φ(m³ℓ)=1` is the D3
  relation `M³L=1`, i.e. this n=3 known case.)*
- **Novel kernel — SL(4) `L=−M⁴` and the family for all `n≥3`:** an adversarial sweep (HMP, FGKRT, Tillmann
  math/0508295, "A-polynomials, Ptolemy equations and Dehn filling" 2002.10356, plus targeted searches for an SL(4) /
  higher-rank figure-eight A-polynomial and an `L=Mⁿ` Dehn-filling relation) surfaced **no prior art**; the literature
  states the SL(4) case is open ("a complete description of the geometry of SL₄ character varieties even for torus
  knots is still an open problem"; "complete results for SL(4,C) remain to be developed"). **APPEARS-NOVEL.**
- **NEEDS-SPECIALIST caveats (load-bearing):** (a) only `n=3,4` are actually established (numeric n=3,4; symbolic-exact
  `n=4` only, B89; the principal n=5 rep is not numerically locatable), so "a family for all `n≥3`" is a **conjecture
  with two data points + a prediction**, not an established family; (b) it could be **implicit** in the
  Bergeron–Falbel–Guilloux flag/gluing or Garoufalidis–Thurston–Zickert Ptolemy framework (PDFs not fully extractable
  by web read); (c) the right closer is a specialist in the Falbel / HMP / BFG circle, or the user's by-hand read.

**(ii) the CRT/F_p first-principles tower-proof *technique* (B80).** Reconstructing a symbolic-in-`m` result by
interpolating mod several primes + CRT + rational reconstruction is **standard computational-algebra** (textbook
modular/CRT reconstruction). **KNOWN as a technique**; its *application* to the fixed-line Jacobian is the project's
engineering, not a new method.

**(iii) the n≥5 forced-spectrum / degeneracy mechanism (B95).** That the principal Dehn-filling spectra are forced
(`{1,i,−i}`, `{1,1,ω,ω²}`, `{1,1,1,−1,−1}`) and degenerate at `n=5` (`A²=I` → dihedral → reducible) rests on the
exceptional-filling / finite-order-monodromy structure already in HMP (the SL(3) components "induced by exceptional
Dehn fillings"); the "exponent=rank is an `n∈{3,4}` phenomenon" framing is the project's. **PARTIALLY-KNOWN /
NEEDS-SPECIALIST.**

**Two corrections found while auditing (bank these):**
- The **H2 Tillmann citation is mis-specified:** `math/0508295` is Tillmann, *"Degenerations of ideal hyperbolic
  triangulations"* (deformation varieties / Culler–Morgan–Shalen), which contains **no "trace dictionary"** and no
  `L=Mⁿ` relation. The intended Tillmann reference for a trace/peripheral dictionary needs to be re-identified by the
  human (or dropped).
- The **H2 `φ(m³ℓ)=1` is the n=3 (known) Falbel D3 relation `M³L=1`**, not a separate novel item — so the H2 lead, as
  written, mostly points at already-known n=3 content; the genuinely-open novelty is the **SL(4)/`n≥4`** statement.

**Verdict (R4):** n≤3 **KNOWN** (Cooper–Long; HMP; Falbel/FGKRT); the SL(4) `L=−M⁴` and the unifying family
**APPEARS-NOVEL but NEEDS-SPECIALIST** (established only at n=3,4; possibly implicit in BFG/GTZ; a specialist read is the
real closer). The CRT/F_p method is a **KNOWN technique**; the n≥5 mechanism is **PARTIALLY-KNOWN**.

---

## Net assessment

Of R1–R3, two are **known** (R2 Kitano–Nozaki; R3 standard quantum topology) and one is **partially novel** with the
novel kernel now **proved** (R1, on GHH 2008). R4 (the degree=rank / `Aₙ` family) is **split**: its n≤3 content is
**KNOWN** (Cooper–Long; Heusener–Muñoz–Porti; Falbel/FGKRT), while the **SL(4) `L=−M⁴`** and the unifying family
**APPEAR-NOVEL but NEED-SPECIALIST** — no prior art was findable and the literature calls the SL(4) figure-eight
geometry open, but the result is established only at n=3,4 and could be implicit in the Bergeron–Falbel–Guilloux /
Garoufalidis–Thurston–Zickert frameworks. So the genuinely-new candidates are now **two, both narrow and both still
needing a human/specialist close:** *the block-length palindrome criterion (R1, a GHH corollary, proved)* and *the
SL(4)/`n≥4` `L=−Mⁿ` figure-eight A-polynomial (R4, the SLN-skeleton's main result, n=3,4 only)*.

The project's recurring strength is methodological (verify-don't-trust, firewall, first-class negatives). The honest
framing going forward: **cite GHH / Kitano–Nozaki / Jeffrey–Lawrence–Zagier–Dong–Lin–Ng / Cooper–Long / Heusener–
Muñoz–Porti / Falbel–FGKRT**; do not re-derive them; reserve any novelty claim for the block-lift (R1) and the SL(4)
A-polynomial (R4), **both pending a specialist read** (R1: GHH's exact hypotheses; R4: the Falbel/HMP/BFG circle, and
whether the family is implicit in their framework). An AI adversarial read can de-risk these — and did — but cannot
substitute for the specialist; that is the H2 lead, and it remains genuinely open.

**Method note (MB6, `../REPRODUCIBILITY.md`):** reproduction ≠ interpretation. **Method note (this audit):** "appears
novel" requires an adversarial prior-art search, not absence-of-memory — here it downgraded two of three.
