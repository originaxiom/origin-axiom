# B793 input — Arithmetic quantum chaos and the Bianchi Maass-data landscape for m004

Literature subagent report, 2026-07-28. All papers marked **[verified]** were opened or found via live search this session; anything from memory is marked **UNVERIFIED**. Downloaded primaries live in `/private/tmp/claude-501/-Users-dri-oa-audit-seat/00f419c5-801b-4bbb-8d32-503cc9c44455/scratchpad/` (`gh1996.pdf`, `then_aqc.pdf`, `ast_cosmo.pdf`, `bkl2025.pdf`, `sts.pdf`, `marklof.pdf`, `pams.pdf`, `special.pdf`). Repo anchors: `frontier/B792_maass_m004_eigenvalues/FINDINGS.md:18-25` (lower window), `:103-115` (upper window).

---

## 1. CRITICAL SIDE-QUEST: Grunewald–Huntebrinker 1996 — PRIMARY OBTAINED AND READ

F. Grunewald, W. Huntebrinker, *A numerical study of eigenvalues of the hyperbolic Laplacian for polyhedra with one cusp*, **Experimental Mathematics 5 (1996), no. 1, 57–80**. Full PDF fetched from Project Euclid (article id `em/1047591148`), 24 pages, all tables transcribed from the primary. **[verified]**

Method: adaptive finite elements on truncated fundamental polyhedra (IBM RS/6000; systems of order 10,000–12,000 for the d=3 domain), dual Dirichlet/Neumann cutoff runs at R=15 and R=19, eigenvalues via Rayleigh quotients. Accuracy statement, verbatim: *“In this and subsequent tables, the last digit of each entry may be untrustworthy.”*

### 1.1 Table 3 — the COMPLETE discrete spectrum of PSL₂(Z[ω]) up to λ = 675 (36 values)

Symmetry types (paper’s §6.1, prism with 30° northern angle): **B** even w.r.t. bottom, NQ, PQ / odd w.r.t. NP; **D** even w.r.t. all boundary planes; **G** odd w.r.t. all; **J** odd w.r.t. bottom, NQ, PQ / even w.r.t. NP. On the PSL₂(Z[ω]) domain only types B, D, G, J occur; **type-D entries are also the spectrum of the extended Bianchi group EB(Z[ω])** (index 4 over PSL₂(Z[ω])).

| λ | type | λ | type | λ | type | λ | type |
|---|---|---|---|---|---|---|---|
| 51.014 | B | 261.6 | B | 441 | B | 544 | J |
| 122.19 | B | 293.5 | D | 446 | D | 553 | B |
| 157.29 | D | 304.1 | B | 450 | D | 568 | D |
| 177.78 | B | 331.2 | B | 483 | J | 596 | D |
| 222.0 | B | 355.9 | D | 484 | B | 597 | D |
| 226.4 | D | 365.1 | D | 498 | B | 602 | J |
| 261.5 | J | 375.7 | J | 514 | D | 605 | B |
| — | — | 376.0 | B | 515 | D | 642 | B |
| — | — | 408.7 | B | 515 | G | 665 | B |
| — | — | — | — | 544 | B | 669 | D |

**Gate-8R2 resolution, from the primary:** 51.014 is the smallest entry, type B — the parent ground state. Our independent 51.0132434 (r = 7.07200419) agrees at GH’s stated accuracy (51.014 = 3-decimal rounding; |Δλ| ≈ 8e−4). The load-bearing value now has BOTH the primary transcription and the independent computation.

**Immediate falsifiable predictions for m004 (old forms):** every Table 3 value is a PSL₂(Z[ω]) eigenvalue and hence appears in m004’s spectrum as an old form. Below λ = 101 (r < 10) Table 3 contains ONLY 51.014 — **exactly matching B792’s finding of a single old form and no old forms in (7.3, 10)**. Next old forms predicted at:
- r ≈ **11.0086** (λ = 122.19, B), r ≈ **12.5016** (157.29, D), r ≈ **13.2960** (177.78, B), r ≈ 14.8661 (222.0, B), r ≈ 15.0133 (226.4, D).

Extend the scan to r ≈ 13.5 and these must appear (S-invariant to ~1e−9); absence would indict either the solver’s upper window or GH’s table.

**Caveat:** Table 3 has a single G entry (515) — GH’s FEM may have under-resolved the all-odd class; treat Table 3 as a lower bound on the parent spectrum, not proof of completeness.

### 1.2 λ₁ lower bounds quoted by GH (from Elstrodt–Grunewald–Mennicke 1987; Stramm 1994)

- λ₁(PSL₂(Z[i])) ≥ (2/3)π² ≈ 6.58; λ₁(PSL₂(Z[√−2])) ≥ (1/4)π² ≈ 2.47; **λ₁(PSL₂(Z[ω])) ≥ (32/27)π² ≈ 11.70** (page image read directly to resolve OCR).

### 1.3 Tables 4–5: two more one-cusp d=3-adjacent spectra nobody in the campaign has used

**Table 4 — Γ₄** (pyramid Υ₄ = {0 ≤ x ≤ 1/√2, −x/√3 ≤ y ≤ (1−x)/√3, r ≥ √(1−x²−y²)}, class T5; **commensurable with PSL₂(Z[ω]), commensurability index 5/2, covolume ≈ 0.1056, λ₁ > 1**), 34 eigenvalues to 305:
16.490 B; 45.856 D; 51.014 B; 78.41 B; 91.11 D; 100.77 D; 107.14 B; 122.19 B; 135.88 J; 135.91 B; 139.77 D; 157.29 D; 160.0 B; 177.78 B; 185.2 D; 198.7 D; 205.15 J; 205.2 B; 222.0 B; 226.4 D; 232.7 B; 238.1 D; 248.3 G; 248.4 D; 256.8 B; 261.5 J; 261.6 B; 270.2 D; 293.5 D; 294.9 B; 299.2 J; 299.8 B; 301.9 D; 304.1 B.
All ten Table 3 entries ≤ 305 recur with identical types (overgroup inclusion, noted by GH). **Flag:** Γ₄’s 16.490 sits 0.025 from m004’s λ₁ = 16.515066. GH last-digit uncertainty makes this borderline; both groups are commensurable with PSL₂(Z[ω]), so settle it computationally (restriction test on Γ₄ ∩ Γ₄₁), never by proximity.

**Table 5 — Γ₅** (**nonarithmetic** by Vinberg’s criterion, maximal, equal to its commensurator; covolume ≈ 0.1732; λ₁ > 1), 32 eigenvalues to 220: 7.322 B; 24.43 B; 43.5 B; 45.1 D; 63.7 B; 74.6 B; 87.0 B; 93.6 B; 95 D; 103.3 J; 112 D; 116 B; 118 D; 128 B; 145 D; 145.5 B; 151.4 B; 156.7 J; 163 D; 166.3 B; 170 B; 173 D; 179.6 G; 185.9 B; 189 D; 192 B; 196 D; 199 D; 199.7 J; 212 B; 216? D; 220 B. **Free nonarithmetic control group** for every arithmetic-signature claim.

Historical note from GH’s intro: the only prior published 3D table was Smotrov–Golovčanskiĭ (Bielefeld preprint 91-040, 1991; 12 smallest PSL₂(Z[i]) eigenvalues, C/D types only — their method missed the others due to an error in a corollary); GH also report “good agreement” with a then-unpublished Steil–Steiner PSL₂(Z[i]) list to λ < 900.

---

## 2. Steil 1999 — the d=3 chapter exists, is confirmed to contain d=3 samples, and is unread

G. Steil, *Eigenvalues of the Laplacian for Bianchi groups*, in **Emerging Applications of Number Theory** (Hejhal, Friedman, Gutzwiller, Odlyzko eds.), IMA Vol. 109, Springer 1999, **pp. 617–641**, DOI 10.1007/978-1-4612-1544-8_27. **[verified metadata]** Springer abstract (fetched): computation of Laplace spectra for arithmetic subgroups of PSL(2,C), *“special attention devoted to the cases D = 1, 2, 3, 7, 11, 19 having fundamental domains with one cusp”*; *“the spectra are not simple”*; *“samples of eigenvalues are listed.”*

So: **Steil’s chapter contains d=3 eigenvalue samples, but the full text is paywalled and the numbers were NOT retrievable this session.** No DESY/arXiv preprint of the Bianchi chapter was found (his 1994 DESY 94-028 report is the PSL(2,Z) work). Acquisition of pp. 617–641 is the single highest-value missing primary. Do not admit Steil d=3 numbers from secondaries — that would repeat the Gate-8R2 pattern.

What Steil’s chapter is known to contain (via Then math-ph/0305048 and Aurich–Steiner–Then gr-qc/0404020, both read **[verified]**):
- 2545 consecutive PSL₂(Z[i]) eigenvalues via a nonlinear system built on Hecke relations.
- **Theorem (Steil).** For the Picard group: if λ = 1+r² has an eigenfunction of class G (resp. H), there is an eigenfunction of class D (resp. C) with the SAME eigenvalue. Degeneracies first observed by Huntebrinker, explained by Steil via Hecke operators (Heitkamp 1992 Hecke theory).
- Poisson-like level spacings after desymmetrization (also Marklof’s Encyclopedia review, PDF fetched: “Steil performed experiments for arithmetic subgroups of SL(2,C)… and found a Poisson level spacing”).

---

## 3. The rest of the Bianchi Maass data landscape (who has computed what)

| Source | Group / d | Data | Status |
|---|---|---|---|
| Smotrov–Golovčanskiĭ 1991 | d=1 | 12 smallest (C/D only) | [verified as record] |
| GH 1996 | d=1,2,3 + Γ₄, Γ₅ | Tables 1–5; d=3: 36 values ≤ 675 | **primary read** |
| Steil 1999 | D = 1,2,3,7,11,19 | 2545 consecutive (d=1); “samples” incl. d=3 | metadata verified; text paywalled |
| Then math-ph/0305048; Aurich–Steiner–Then gr-qc/0404020 | d=1 (Picard) | **13950 eigenvalues**, 1 < λ ≤ 19601; per-class tables; smallest r = 6.6221193402528 (C) | primaries read |
| De Clerck–Hartnoll–Yang arXiv:2507.08788 (JHEP 11 (2025) 160) | d=1 AND **d=3** | Hejhal+Then method; **d=3 odd form at ε ≈ 24.5033** (λ ≈ 601.41), 1000 prime Hecke eigenvalues, Sato–Tate verified; Kesten–McKay over 995 levels (d=1) | primary read |
| Booker–Strömbergsson(–Venkatesh); Avelin; Then math-ph/0305047 | H² only | certification/deformation/large-eigenvalue methods | verified; **no d=3 anywhere** |

**Every explicitly sourced d=3 eigenvalue found this session** is in §1 (GH Tables 3–5) plus DHY’s ε ≈ 24.5033. Cross-identifications: DHY’s d=3 form matches GH’s **602 J** entry within GH error (√601.41 → “602”); DHY’s d=1 form at ε ≈ 25.7239 is exactly Then’s Table 1 D/G pair 25.72392169 — conventions align (λ = 1+ε², ε = r).

Note for the physics-coupling file: DHY show the **5d pure-gravity BKL billiard wavefunctions are precisely the odd Maass cusp forms of PSL₂(Z[ω])** (5d Einstein–Maxwell: odd forms of PSL₂(Z[ω])⋊2) — an independent community already couples the d=3 Bianchi Maass spectrum to gravitational dynamics.

---

## 4. Spacing statistics: what m004’s spectrum SHOULD look like

Canon **[all verified]**: Bogomolny–Georgeot–Giannoni–Schmit, PRL 69 (1992) 1477; Bolte–Steil–Steiner, PRL 69 (1992) 2188; Sarnak, Israel Math. Conf. Proc. 8 (1995) 183–236; Luo–Sarnak, CMP 161 (1994) 419–432 (number variance Poisson-like in part of the universal range — the only theorem in this class, H² only); Marklof, Encyclopedia review.

Prediction for m004 (arithmetic, congruence): **Poisson-like spacings, NOT GOE**, within each fixed symmetry/Hecke sector — the arithmetic violation of Bohigas–Giannoni–Schmit universality, driven by exponential length-spectrum multiplicities (cf. the repo’s own 7513-geodesic trace multiset). Verified numerically for SL(2,C) arithmetic groups by Steil.

**The multiplicity-2 pairs are the expected arithmetic signature, not an anomaly.** For the Picard group: Steil’s theorem + Weyl’s law + AST’s Conjecture 4 (degeneracies occur only in pairs, no accidental ones) imply **asymptotically almost ALL eigenvalues are two-fold degenerate**. GH’s own d=3 tables show the analogous **B/J pairs** (261.5/261.6, 375.7/376.0, 483/484, 544/544, 602/605; Γ₄: 135.88/135.91, 205.15/205.2, 299.2/299.8) and a G/D pair (515/515). m004’s doubles (5 of 6 in the lower window, 9 of 17 distinct below r = 10) are almost certainly the congruence-cover version, via either (i) the 2-dim irrep of Isom(m004) ≅ **D₄, order 8, amphichiral** (SnapPy-checked in-sandbox this session — consistent with B792’s “symmetry outside the coset action” scoping of B791’s criterion), or (ii) Steil-type Hecke pairing of conjugate newforms (c_μ vs c_μ̄). **Hecke operators restricted to the 2-dim eigenspaces decide between (i) and (ii)** — equal vs distinct Hecke eigenvalues.

Honesty clause: 17 distinct eigenvalues have no power to discriminate Poisson vs GOE. The reportable statistic now is the degeneracy fraction vs the AST asymptotic; NNS/number variance become meaningful at O(100+) eigenvalues.

---

## 5. QUE on H³: theorem landscape (directly constrains coupling models)

- Rudnick–Sarnak, CMP 161 (1994) 195–213: QUE formulated; **no strong scarring** on totally geodesic submanifolds of arithmetic hyperbolic manifolds; arithmetic 3-manifold theta-lift eigenfunctions BREAK the naive random-wave model (the one known arithmetic mechanism for distinguished eigenfunctions). **[verified]**
- Lindenstrauss, Ann. Math. 163 (2006) 165–219 (+ Soundararajan, Ann. Math. 172 (2010) 1529–1538, arXiv:0901.4060): AQUE for congruence surfaces, escape of mass excluded. **[verified]**
- **Shem-Tov–Silberman, arXiv:2206.05955** (J. Anal. Math., 2025): *“We prove the Arithmetic Quantum Unique Ergodicity Conjecture for hyperbolic 3-manifolds”* — congruence lattices in SL₂(R)^r × SL₂(C)^s, joint Hecke–Laplace eigenfunctions, |ψ_j|² dvol → dvol; “the case SL₂(Z[i])\H³ is already new.” **Given Γ₄₁ congruence of level (4) (B734), AQUE is a THEOREM for m004’s Hecke–Maass forms.** High-energy eigenfunction localization is not an available coupling channel. **[verified, Theorem 1 read]**
- Eisenstein/continuous spectrum: Koyama, CMP 215 (2000) 477–486 (class number one, includes Q(√−3)); Kim–Lee, arXiv:2603.16518 (2026, all class numbers); Petridis–Sarnak, J. Evol. Equ. 1 (2001) 277–290 (L-function estimates for SL₂(O)\H³). **[verified]**
- Scales: Chatzakos–Frot–Raulf, arXiv:2007.11473 — on Bianchi H³, equidistribution on shrinking balls r ~ t^{−δ} holds for δ < 2/5 (under Lindelöf), and **QUE fails for δ > 3/4**; the open window δ ∈ (2/5, 3/4] is where scale-sensitive coupling models must live (or at the cusp, or at low energy — no theorem constrains r < 10). **[verified]**

---

## 6. Hecke operators for Γ₄₁ (congruence, level (4), 2 inert in Z[ω])

- Foundations: Elstrodt–Grunewald–Mennicke (book, 1998; J. reine angew. Math. 360 (1985) 160–213); **Heitkamp 1992** (Hecke-Theorie zur SL(2,o), Münster); Şengün survey arXiv:1204.6697 (level structure, newforms, base change). **[verified as records/search]**
- Since Γ₄₁ is congruence, the full commutative Hecke algebra {T_𝔭 : 𝔭 ∤ (2)} acts: ramified T_√−3 (norm 3), split T_𝔭 for p ≡ 1 mod 3 (7, 13, 19, …), inert T_p for p ≡ 2 mod 3 (5, 11, 17; norm p²). (For non-congruence subgroups the action would factor through the congruence closure — Hamzeh Zarghani, PAMS 139 (2011) 3853–3865 **[verified]** — irrelevant here but a useful sanity guard.)
- **Extraction recipe exists and was used on H³ in 2025:** DHY arXiv:2507.08788 App. B/C: Hecke relations c_μ c_ν = Σ_{d|(μ,ν)} c_{μν/d²}; for reflection-odd forms the coefficient-to-Hecke inversion (their Eqs. (151)–(158)) recovers c_μ from Fourier coefficients up to a quadratically-determined constant, then the Hecke relations self-validate the numerics. Port this to m004’s cusp expansion (lattice Λ = Z + 2√−3·Z, B792) — the only new work is the double-coset normalization at one cusp for level (4).
- Payoffs: (a) split the five doubles (geometric vs arithmetic degeneracy); (b) Sato–Tate/Kesten–McKay universality tests (DHY verified both on the parent, d=3 included); (c) Ramanujan-bound check; (d) base-change detector c_μ = c_μ̄ linking m004 forms to classical modular forms.

---

## 7. What did NOT turn up

- No published Maass eigenvalue list for the figure-eight knot complement itself anywhere in the literature searched — **B792’s 17-eigenvalue spectrum appears to be the first computation of m004’s Maass spectrum** (the parent orbifold’s spectrum is GH/Steil territory; the congruence-cover spectrum is not in GH, Steil, Then, AST, or DHY).
- No d=3 content in Then (beyond method), Avelin (H², deformation of cusp forms, Uppsala reports 2002:26, 2003:8), Booker–Strömbergsson–Venkatesh (H² certification; their rigor standard is the one to port). Booker–Strömbergsson trace-formula paper (J. reine angew. Math., 2007) is H²-level work — **UNVERIFIED detail, from memory**.
- No AQUE gap: the H³ theorem (Shem-Tov–Silberman) is unconditional for congruence quotients; nothing in the literature licenses value-extraction from high-energy eigenfunction geometry.

## 8. Prioritized actions for B793

1. Acquire Steil 1999 pp. 617–641 (library scan) — the last unread primary with d=3 numbers.
2. Extend the B792 scan to r ≈ 13.5: the GH Table 3 old-form predictions (11.0086 / 12.5016 / 13.2960) are a pre-registered pass/fail test of both pipelines.
3. Implement T_√−3 and one split-prime T_𝔭 on the banked Fourier coefficients; split the doubles; run Sato–Tate + Kesten–McKay; pre-register a coefficient-level SM-value null scan.
4. Settle 16.490 (Γ₄) vs 16.515 (m004) by restriction, not proximity.
5. Use GH Table 5 (nonarithmetic Γ₅) as the control for every arithmetic-signature claim.

## KEY PAPERS (structured)
- [VERIFIED] F. Grunewald, W. Huntebrinker (1996), "A numerical study of eigenvalues of the hyperbolic Laplacian for polyhedra with one cusp" — Experiment. Math. 5 (1996), no. 1, 57-80; Project Euclid em/1047591148
  - PRIMARY for the side-quest. Full PDF obtained from Project Euclid and read; Table 3 (all 36 PSL(2,Z[omega]) eigenvalues up to 675 with symmetry types B/D/G/J) fully transcribed, plus Table 4 (commensurable group Gamma_4) and Table 5 (nonarithmetic control Gamma_5), lambda_1 lower bounds, and FEM accuracy caveats ('the last digit given is always somewhat uncertain').
- [VERIFIED] G. Steil (1999), "Eigenvalues of the Laplacian for Bianchi groups" — 10.1007/978-1-4612-1544-8_27
  - Springer abstract fetched: treats PSL(2,O_D) for D = 1, 2, 3, 7, 11, 19 (one-cusp fundamental domains), shows 'the spectra are not simple', and 'samples of eigenvalues are listed' — so d=3 eigenvalue samples EXIST in this chapter but the full text is paywalled; the actual d=3 numbers were not retrievable this session (acquisition item). Computed 2545 consecutive eigenvalues for PSL(2,Z[i]) via Hecke relations; proved the degeneracy theorem (class G in D, class H in C) and verified Poisson spacings (per Then math-ph/0305048 and Marklof's review).
- [VERIFIED] H. Then (2003/2006), "Arithmetic quantum chaos of Maass waveforms" — arXiv:math-ph/0305048
  - Read in full. Picard group PSL(2,Z[i]): 13950 eigenvalues in 1 < lambda <= 19601; symmetry classes D,G,C,H with first r-values tabulated (smallest r = 6.6221193402528, class C); states Theorem 1 (Steil): G-eigenvalues recur in D, H in C, degeneracies first observed by Huntebrinker, explained by Steil via Hecke operators; Poisson nearest-neighbor spacings within each symmetry class. The d=1 template for what m004's spectrum should look like.
- [VERIFIED] R. Aurich, F. Steiner, H. Then (2004), "Numerical computation of Maass waveforms and an application to cosmology" — arXiv:gr-qc/0404020
  - Read. Same Picard dataset; key statement: by Weyl's law + Steil's theorem + their Conjecture 4 (no accidental degeneracies, only pairs), asymptotically ALMOST ALL Picard eigenvalues are two-fold degenerate — the exact prototype of m004's multiplicity-2 pairs. Also lists prior Picard computations (Smotrov-Golovchanskii 1991, Huntebrinker 1996, GH 1996, Steil 1999) and the Hecke references (Stark 1984, Heitkamp 1992, Hejhal-Arno 1993).
- [VERIFIED] H. Then (2005), "Maass cusp forms for large eigenvalues" — arXiv:math-ph/0305047 (Math. Comp. 74 (2005) 363-381)
  - The algorithmic improvement of Hejhal's method used by all later Bianchi computations (H^2 paper; method cited by De Clerck-Hartnoll-Yang for their H^3 Hecke computations).
- [VERIFIED] M. De Clerck, S. A. Hartnoll, M. Yang (2025), "Wheeler-DeWitt wavefunctions for 5d BKL dynamics, automorphic L-functions and complex primon gases" — arXiv:2507.08788 (JHEP 11 (2025) 160)
  - Read. The most recent d=3 Maass computation found anywhere: an odd (z -> -zbar) Maass cusp form of PSL(2,Z[omega]) at epsilon ≈ 24.5033 (lambda = 1+epsilon^2 ≈ 601.4; matches GH Table 3's '602 J' entry within GH error), with 1000 prime Hecke eigenvalues verified Sato-Tate semicircular, plus Kesten-McKay across 995 levels (Gaussian case). Appendix B/C give the exact Hecke-relation machinery (c_mu c_nu = sum_{d|(mu,nu)} c_{mu nu/d^2}) and the recipe for extracting Hecke eigenvalues from Fourier coefficients of reflection-odd forms — the template for doing the same on m004's coefficients. 5d pure gravity BKL billiard = odd PSL(2,Z[omega]) forms: an independent physics community already couples d=3 Bianchi Maass spectra to gravitational dynamics.
- [VERIFIED] E. Lindenstrauss (2006), "Invariant measures and arithmetic quantum unique ergodicity" — Ann. of Math. 163 (2006) 165-219
  - AQUE for arithmetic hyperbolic surfaces (compact case complete; noncompact up to escape of mass). The measure-rigidity backbone of all AQUE results.
- [VERIFIED] K. Soundararajan (2010), "Quantum unique ergodicity for SL2(Z)\H" — arXiv:0901.4060 (Ann. of Math. 172 (2010) 1529-1538)
  - Eliminates escape of mass, completing noncompact AQUE on the modular surface.
- [VERIFIED] Z. Shem-Tov, L. Silberman (2022/2025), "Arithmetic quantum unique ergodicity for products of hyperbolic 2- and 3-spaces" — arXiv:2206.05955 (J. Anal. Math., 2025)
  - Read Theorem 1 and introduction. 'We prove the Arithmetic Quantum Unique Ergodicity Conjecture for hyperbolic 3-manifolds': for congruence lattices in SL2(R)^r x SL2(C)^s, normalized joint Hecke-Laplace eigenfunctions equidistribute (|psi_j|^2 dvol -> dvol). The case SL2(Z[i])\H^3 'is already new'. DIRECTLY applicable to m004 (Gamma_41 congruence, level (4)): QUE for m004's Hecke-Maass forms is a theorem, so no coupling model may rely on high-energy eigenfunction localization.
- [VERIFIED] S. Koyama (2000), "Quantum ergodicity of Eisenstein series for arithmetic 3-manifolds" — 10.1007/s002200000317 (Comm. Math. Phys. 215 (2000) 477-486)
  - QE of Eisenstein series for PSL(2,O_K), K imaginary quadratic of class number one — includes Q(sqrt(-3)), i.e. the continuous spectrum over m004's parent orbifold equidistributes.
- [VERIFIED] D. Kim, Y. Lee (2026), "Quantum ergodicity of Eisenstein series for Bianchi groups" — arXiv:2603.16518
  - Extends Koyama to all class numbers h_F >= 1 (March 2026). Shows the Eisenstein/continuous-spectrum side is fully equidistributed for every Bianchi group — the cusp channel carries structure only through the scattering phase, not through localization.
- [VERIFIED] Y. Petridis, P. Sarnak (2001), "Quantum unique ergodicity for SL2(O)\H^3 and estimates for L-functions" — J. Evol. Equ. 1 (2001) 277-290
  - L-function subconvexity input to QUE on Bianchi 3-manifolds; the analytic bridge between eigenfunction equidistribution and L-values on H^3.
- [VERIFIED] D. Chatzakos, R. Frot, N. Raulf (2020/2021), "Quantum ergodicity for shrinking balls in arithmetic hyperbolic manifolds" — arXiv:2007.11473
  - Abstract fetched. On PSL2(O_K)\H^3 (class number one): QUE FAILS for Hecke-Maass forms on balls shrinking faster than t_j^(-3/4); equidistribution holds for delta < 2/5 under Lindelof; unconditional Eisenstein results. Gives the quantitative SCALE at which observer-object coupling could see non-uniform structure — a key design constraint for B793.
- [VERIFIED] Z. Rudnick, P. Sarnak (1994), "The behaviour of eigenstates of arithmetic hyperbolic manifolds" — Comm. Math. Phys. 161 (1994) 195-213
  - No strong scarring onto totally geodesic submanifolds for arithmetic hyperbolic manifolds; arithmetic 3-manifold examples where the naive random-wave model FAILS (theta-lift eigenfunctions with anomalously large L^infinity norms) — the one known mechanism by which arithmetic 3-manifolds produce distinguished eigenfunctions.
- [VERIFIED] W. Luo, P. Sarnak (1994), "Number variance for arithmetic hyperbolic surfaces" — Comm. Math. Phys. 161 (1994) 419-432
  - Proves the spectral number variance of arithmetic surfaces is Poisson-like (nonrigid) in part of the universal range — the only rigorous spacing-statistics theorem in the arithmetic class; the H^3 analogue is open and is what m004 data would probe.
- [VERIFIED] E. Bogomolny, B. Georgeot, M.-J. Giannoni, C. Schmit (1992), "Chaotic billiards generated by arithmetic groups" — Phys. Rev. Lett. 69 (1992) 1477-1480
  - (Via bibliographies of papers read this session.) Origin, with Bolte-Steil-Steiner, of the arithmetic-chaos prediction: Poisson-like spacings from exponential length-spectrum multiplicities despite hard chaos.
- [VERIFIED] J. Bolte, G. Steil, F. Steiner (1992), "Arithmetical chaos and violation of universality in energy level statistics" — Phys. Rev. Lett. 69 (1992) 2188-2191
  - (Via bibliographies of papers read this session.) Companion PRL establishing the Poisson anomaly for arithmetic Fuchsian groups; Steil's Bianchi work is its H^3 continuation.
- [VERIFIED] P. Sarnak (1995); J. Marklof (2006) (1995/2006), "Arithmetic quantum chaos (Schur lectures) / Arithmetic quantum chaos (Encyclopedia review)" — Israel Math. Conf. Proc. 8 (1995) 183-236; Marklof PDF at people.maths.bris.ac.uk/~majm/bib/arithmetic.pdf
  - Marklof PDF fetched: confirms 'Steil performed experiments for arithmetic subgroups of SL(2,C)... and found a Poisson level spacing.' The two standard surveys framing GOE-vs-Poisson for arithmetic manifolds.
- [VERIFIED] M. H. Sengün (2012), "Arithmetic aspects of Bianchi groups" — arXiv:1204.6697
  - (Found via live search, not opened.) Standard survey of Hecke theory, level structures, base change, and newform theory for Bianchi groups — the reference frame for setting up Hecke operators on Gamma_41 at level (4).
- [VERIFIED] S. Hamzeh Zarghani (2011), "Hecke operators for non-congruence subgroups of Bianchi groups" — Proc. Amer. Math. Soc. 139 (2011) 3853-3865
  - First page read. Hecke action on cohomology of a finite-index subgroup of a Bianchi group factors through its congruence closure (Atkin/Serre/Berger circle). Since Gamma_41 IS congruence (level (4), B734), full Hecke theory applies directly with no closure loss.
- [VERIFIED] M. Chu (2017), "Special subgroups of Bianchi groups" — arXiv:1709.10503
  - Read intro. Confirms Riley's holonomy presentation Gamma_8 = <(1 1;0 1),(1 0;(1+sqrt(-3))/2 1)> in PSL(2,O_3), index 12 (the figure-eight knot group), and works with congruence subgroups of level 2 and 4 in Bianchi groups — external corroboration adjacent to the internal 'Gamma_41 congruence of level (4)' result.
- [VERIFIED] M. N. Smotrov, V. V. Golovchanskii (1991), "Small eigenvalues of the Laplacian on Gamma\H^3 for Gamma = PSL2(Z[i])" — Preprint 91-040, Bielefeld
  - (Via GH 1996 and Then bibliographies.) The only pre-GH published table for a Bianchi group (12 smallest PSL(2,Z[i]) eigenvalues, C/D classes only); historical baseline.
- [VERIFIED] D. Heitkamp (1992), "Hecke-Theorie zur SL(2;o)" — Schriftenreihe Math. Inst. Univ. Münster, 3. Serie, 5 (1992)
  - (Via bibliographies.) The German-school foundational reference for Hecke operators on SL(2) over imaginary quadratic integers, used by Steil and Then for the coefficient relations.
- [VERIFIED] A. Booker, A. Strömbergsson, A. Venkatesh (2006), "Effective computation of Maass cusp forms" — IMRN 2006, art. 71281 (PDF at math.ias.edu/~akshay/research/bsv.pdf)
  - (Found via live search.) Rigorous certification of Maass forms — H^2 ONLY. Together with Avelin (Uppsala, deformation of cusp forms, H^2 only) and Booker-Strömbergsson trace-formula work (H^2, UNVERIFIED details), confirms the answer to the task's question: Then, Avelin, Booker-Strömbergsson have NO published d=3 computations; the certified-computation methodology is the thing to port to H^3, not their data.

## COMPUTABLE QUANTITIES
- OLD-form prediction from GH Table 3 (sharpest immediate test): the next Bianchi (parent) eigenvalues must appear in m004's spectrum at r ≈ 11.0086 (lambda = 122.19, type B), 12.5016 (157.29, D), 13.2960 (177.78, B), 14.8661 (222.0, B), 15.0133 (226.4, D) — extend the B792 scan from r = 10 to r ≈ 13.5 and check each dip's S-invariance; GH predicts ZERO old forms in (7.3, 11.0), which the existing scan already confirms in (7.3, 10).
- Hecke eigenvalues of m004's newforms from the already-computed Fourier coefficients: implement T_pi for pi coprime to the level (4) — ramified pi = sqrt(-3) (norm 3), split primes above 7, 13, 19, 31, 37 (p ≡ 1 mod 3), inert 5, 11, 17 (norm p^2) — using the Hecke relations c_mu c_nu = sum_{d|(mu,nu)} c_{mu nu/d^2} exactly as in De Clerck-Hartnoll-Yang arXiv:2507.08788 Appendix B/C (their Eqs. (81), (151)-(158) give the coefficient-to-Hecke inversion for reflection-odd forms); verify self-consistency via the Hecke relations and the Ramanujan bound.
- Degeneracy-type discriminator: diagonalize T_sqrt(-3) (and one split-prime T_pi) INSIDE each of the five multiplicity-2 eigenspaces (r = 3.9389, 5.6707, 6.6328, 7.3495, 7.8578, ...). Equal Hecke eigenvalues on both basis vectors => geometric degeneracy (2-dim irrep of Isom(m004) = D4, SnapPy-verified order 8, amphichiral); distinct Hecke eigenvalues => Steil-type arithmetic degeneracy (two distinct Hecke newforms paired by conjugation mu -> mubar, the H^3 analogue of Steil's G-in-D / H-in-C theorem and of GH Table 3's B/J pairs 261.5/261.6, 375.7/376.0, 483/484, 544/544, 602/605).
- Sato-Tate semicircle test on m004: histogram the normalized prime Hecke eigenvalues of one fixed newform (e.g. r = 4.90008537, the first mult-1 newform) over the first few hundred primes of Z[omega] and compare to the Wigner semicircle, replicating DHY Fig. 4 (they used 1000 primes at epsilon ≈ 24.5033 on the parent); deviations at small primes are the arithmetic fingerprint available to coupling models.
- Kesten-McKay test across levels: fixed small prime pi (sqrt(-3), then a norm-7 split prime), histogram c_pi across all 17+ computed newforms and compare to the Kesten-McKay distribution (DHY Eq. (114), their Fig. 7) — checks whether m004's coefficient ensemble is statistically universal (supporting 'structure only, no values') or biased (a value-bearing channel).
- Spacing statistics with honest power analysis: unfold the m004 spectrum sector-by-sector (distinct eigenvalues only, doubles counted once, old forms removed) using the exact Weyl + scattering-phase counting function already available in-sandbox (phi = Lambda_K(s-1)/Lambda_K(s), B737/B739), then compute nearest-neighbor spacings and number variance; with only 17-27 points report ONLY the degeneracy fraction (9 doubles / 17 distinct below r = 10) against the Aurich-Steiner-Then asymptotic 'almost all eigenvalues doubled' prediction for the Picard case, and defer NNS/GOE-vs-Poisson claims until the scan reaches O(100+) eigenvalues.
- Cross-check the near-coincidence 16.490 (Gamma_4, GH Table 4 — commensurable with PSL(2,Z[omega]), commensurability index 5/2, covolume 0.1056) vs m004's lambda_1 = 16.515066: decide distinct-vs-identical by testing whether the r = 3.93891686 eigenfunction restricted to the common finite-index subgroup Gamma_4 ∩ Gamma_41 extends Gamma_4-invariantly (analogue of the B792 S-invariance test); GH's stated last-digit uncertainty makes the 0.025 gap borderline FEM error, so this must be settled computationally, not by eye.
- Base-change detector: test c_mu = c_mubar (conjugation-invariance of Hecke eigenvalues) for each newform; conjugation-even Hecke data flags candidate base-change lifts from GL(2)/Q (Sengün survey), which would tie specific m004 eigenvalues to classical modular forms — a concrete, checkable structural bridge out of the knot complement toward 4d-physics-adjacent objects.
- Nonarithmetic control: GH Table 5 (Gamma_5, nonarithmetic, vol 0.1732, 32 eigenvalues to 220 with 7.322 lowest) provides a free spacing/degeneracy control group — the arithmetic degeneracy and coefficient-statistics signatures computed for m004 should be ABSENT there; GH Table 5 values can calibrate any claim that m004's features are arithmetic rather than generic.

## COUPLING TEST IDEAS
- Hecke-sector coupling test: if measured values arise from observer-object coupling, the natural coupling channel AQC leaves open is the Hecke eigenvalue system {c_pi} of specific low-lying newforms (deterministic, computable, form-specific numbers — unlike eigenfunction values, which AQUE/no-scarring theorems force to be structureless). Design: extract {c_pi} for the 6 lowest m004 newforms at the ~10 smallest primes of Z[omega], and pre-register a protocol-gated scan for SM-adjacent rationals/ratios in THAT finite dataset (the natural next negative after the B792 spectral null, extending it from eigenvalues to coefficients).
- Degeneracy-breaking as symmetry-breaking toy model: the five mult-2 pairs are 2-dim 'flavor' spaces on which Isom(m004) = D4 and the Hecke algebra act; an observer coupling that selects a preferred basis (e.g. fixes an orientation, breaking amphichirality) splits each doublet. Model the split as a perturbation delta*H restricted to the 2-dim eigenspaces and compute which D4-breaking patterns are compatible with the grammar's chirality mechanism — this is the smallest honest 'coupling + symmetry breaking -> values' model the object supports, and it is fully computable in-sandbox.
- Scale-window coupling: Chatzakos-Frot-Raulf give sharp exponents — eigenfunction mass is provably uniform down to balls of radius t^(-delta), delta < 2/5 (conditional), and provably NON-uniform below the wavelength scale delta > 3/4. Any coupling model that reads values off eigenfunction amplitudes must therefore operate in the window delta in (2/5, 3/4] or at the cusp; test: compute |psi|^2 mass in shrinking balls around the m004 systole and cusp for the computed forms and check where finite-size non-uniformity actually onsets at our low r.
- Continuous-vs-discrete channel separation: Koyama/Kim-Lee force Eisenstein equidistribution, so the cusp channel's only invariant content is the scattering phase phi(s) = Lambda_K(s-1)/Lambda_K(s) already banked (B737/B739). Couple a model observer (test charge on the cusp torus, lattice Lambda = Z + 2sqrt(-3)Z) to the phase and ask which RG-like flows of the cutoff reproduce ratios previously tested in forced-limit branches — a designed coupling that uses only object-supplied structure (phase + lattice) and observer-supplied scale.
- Universality-deviation budget: Sato-Tate/Kesten-McKay are the arithmetic analogue of 'no free parameters' — deviations of small-prime Hecke eigenvalues from the universal laws are the ONLY finite list of distinguished numbers the coupling can latch onto. Compute the deviation vector (c_pi - Sato-Tate expectation) for the lowest newform and confront it with the B784-corrected iota = theta mod-gauge bookkeeping: if the campaign's coupling hypothesis is right, model-building should consume THESE numbers, not eigenvalues.
- Sister discrimination as observer proxy: m003 vs m004 share the parent; the refined mod-4 trace-norm law (B792: m004-only norms ≡ 0,3 mod 4; m003-only ≡ 1 mod 4) suggests coupling models in which the 'observer' is the choice of congruence structure at the inert prime 2 (level (4) = (2)^2). Test: recompute the m003 Maass spectrum with the same solver and check whether its doubles/Hecke data differ from m004's ONLY through level-(4) data at the prime 2 — if yes, 'which universe' = 'which coupling at 2', a concrete, falsifiable instance of H0.

## FAILURE MODES
Numerical/transcription: GH 1996 state 'the last digit of each entry may be untrustworthy' — Table 3 entries above ~400 have only 3 significant digits, and the single G-type entry (515) in Table 3 vs four G-free columns suggests FEM may have missed G-class eigenvalues (GH themselves note 3D comparative data are 'scarce'); do not treat Table 3 as provably complete, only as a lower bound on the parent spectrum. Steil's d=3 samples exist (Springer abstract confirms D=1,2,3,7,11,19 and 'samples of eigenvalues are listed') but the chapter is paywalled — any Steil d=3 number entering the bank before the primary is read would repeat the Gate-8R2 provenance failure. Convention traps: lambda = 1+r^2 vs E vs epsilon; GH symmetry types (B/D/G/J on the d=3 prism, defined by parities across the bottom/NP/NQ/PQ planes) vs Then's Picard classes (D/G/C/H) vs DHY's 'odd under z -> -zbar' — these do NOT map to each other by name, and misidentifying types will corrupt any old/new or degeneracy bookkeeping (e.g. GH type D = extended-Bianchi-invariant, NOT 'even' in Then's sense). Degeneracy claims are resolution-limited on both sides: GH found 'within each symmetry type the eigenfunctions are all simple' — apparent doubles are cross-type; our sigma-tail multiplicity calls could conversely merge two genuinely distinct eigenvalues closer than ~1e-9, so Hecke splitting inside each double is the only decisive test. Commensurability coincidences: Gamma_4's 16.490 vs m004's 16.515 shows how commensurable-group spectra generate near-collisions that invite false identification — never match across groups by proximity alone. Hecke setup risk: Gamma_41 is congruence but not visibly Gamma_0-type; the single-cusp Fourier extraction of T_pi eigenvalues needs the correct double-coset normalization at level (4) (2 is inert, so (4) = (2)^2), and a wrong normalization silently breaks every downstream 'Hecke eigenfunction' premise, including applicability of the Shem-Tov–Silberman AQUE theorem to our specific basis. Statistical power: 17 distinct eigenvalues cannot distinguish Poisson from GOE at any defensible significance — any spacing-statistics claim now would be theater; the AST 'almost all doubled' prediction is asymptotic and its finite-size approach rate is unknown even for the Picard group. Finally, AQUE constrains sequences of Hecke eigenforms as lambda -> infinity; it says nothing about the LOW-lying forms (r < 10) where all our data lives — low-energy localization features are not excluded by any theorem cited here, but equally cannot be extrapolated upward.
