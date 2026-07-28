# 3d-3d correspondence as the H0 coupling mechanism for m004 — literature report (B793 input)

**Scope.** What T[m004] is, which physical quantities are known for it exactly, higher-rank/exceptional status, Z-hat status, what \"values\" mean in this mechanism, failure modes, and what we can compute in-sandbox. All citations below were opened or found via live search this session unless explicitly marked UNVERIFIED. Two claims were **re-derived numerically in-sandbox** this session (scripts in scratchpad, listed in §7).

Repo anchors: `speculations/S026_3d3d_state_integral.md` (dormant fork on exactly this mechanism; its obstruction statement at lines 27–31 is now partially obsolete, see §7), `frontier/B151_firewall_confirmation/` (scale firewall, still intact under everything below).

---

## 1. The mechanism

Wrap N M5-branes (6d (2,0) theory of type A_{N-1}) on a 3-manifold M3 with a topological twist: the IR limit is a 3d N=2 SCFT **T[M3]** (Dimofte–Gaiotto–Gukov, arXiv:1108.4389). SUSY vacua of T[M3] on R^2×S^1 = flat SL(N,C) connections on M3; partition functions of T[M3] on curved backgrounds = complex Chern–Simons partition functions of M3. The figure-eight complement is *the* worked example in essentially every foundational paper.

**This is precisely the H0 shape**: the manifold enters as *structure* (which theory, which vacua, which q-series), and every measured *value* is a function of couplings the observer dials: squashing b, fugacities, background charges, rank N, background geometry. The manifold never emits a naked number.

## 2. What T[m004] IS (verified from primary sources)

- **DGG description** (from the 2-tetrahedron triangulation; DGG arXiv:1112.5179 §4.4, and stated with full Lagrangian in Gang–Yamazaki arXiv:1806.07714 eq. (23)–(24)):
  **T_DGG[m004; A=μ] = U(1) vector multiplet at vanishing CS level coupled to two chiral multiplets Φ1, Φ2 of charge +1** (plus specific background/mixed CS couplings to the U(1)_μ flavor symmetry). The theory depends on a choice of boundary 1-cycle A ∈ H1(T²,Z) = Z⟨μ,λ⟩; T_DGG[m004; A=λ] is obtained by gauging U(1)_μ. DGG themselves note the 2-tet description is \"a bit singular\" (missing the operator that breaks the internal-edge U(1)); the 6-tetrahedron refinement gives the faithful description.
- **Terashima–Yamazaki description** (arXiv:1103.5748; m004 = once-punctured-torus bundle with monodromy conjugate to ST³): **T_TY[m004; λ] = T[SU(2)] with diagonal SU(2) gauged at CS level 3**.
- **IR structure and SUSY enhancement** (Gang–Yamazaki arXiv:1806.07714, PDF read): duality **(T_{k=−3/2,Q=1})⊗² = T_TY[m004; λ]**, where T_{−3/2,1} = U(1) at CS level −3/2 with one chiral of charge +1, conjectured (3 pieces of evidence) to flow to the **minimal 3d N=4 rank-0 SCFT**. So T[m004;λ] factorizes in the IR into two decoupled copies of a minimal N=4 theory.
- **Twists**: topological twists of this rank-0 family give **nonunitary minimal-model TQFTs** (Lee-Yang-type modular data): Gang–Kim–Stubbs, PRL 132 (2024) 131601, arXiv:2310.09080.

## 3. Exactly known physical quantities for T[m004]

### 3.1 S³_b partition function — a ONE-dimensional integral (in-sandbox verified)
Garoufalidis–Kashaev arXiv:1411.6062 (PDF read), eq. (1) with (A,B)=(1,2):

    Z(b) = I_{1,2}(b) = ∫_{R+iε} Φ_b(x)² e^{−πi x²} dx,   0 < ε < Im c_b

Φ_b = Faddeev quantum dilogarithm; absolutely convergent; this is the Andersen–Kashaev/Teichmüller-TQFT invariant of 4_1 (Andersen–Kashaev arXiv:1109.6295) and the S³_b partition function of T[m004] up to a b-dependent phase convention. Saddle points = the two nonabelian parabolic PSL(2,C) representations; Rogers dilogarithm ↔ complex volume; g′(z) ↔ 1-loop invariant (GK Remark 1.6).

**Exact value at b=1** (GK eq. (2), proven in that paper):

    I_{1,2}(1) = (e^{iπ/6}/√3) · (e^{V/2π} − e^{−V/2π}),   V = 2 Im Li₂(e^{iπ/3}) = 2.0298832128193072...

**In-sandbox check (this session)**: numerical quadrature of the contour integral using the exact b=1 form Φ₁(x) = exp[(i/2π)(Li₂(e^{2πx}) + 2πx log(1−e^{2πx}))] (GK eq. 23) gives 0.3287151664 + 0.1897837898i vs exact 0.3287151663 + 0.1897837898i — **|diff| ≈ 1e-10**. The \"1-dim integral\" promise is real: ~1 second per b value.

**Rational couplings are arithmetic**: for b² = M/N, GK Theorem 1.1 evaluates Z exactly in terms of the Rogers dilogarithm and cyclic quantum dilogarithms at z = e(±1/6) — the coupling dial has special arithmetic points.

**Asymptotics**: b→0 growth governed by e^{V/(2πb²)} (volume conjecture regime); factorization into holomorphic blocks B^α(q)·B^α(q̃), q = e^{2πib²}, q̃ = e^{−2πi/b²}, α ∈ {geometric, conjugate} flat connection (Beem–Dimofte–Pasquetti arXiv:1211.1986, fig-8 worked example; complete resurgent/Stokes data for 4_1 in Garoufalidis–Gu–Mariño arXiv:2007.10190).

### 3.2 Superconformal / 3d index (in-sandbox re-derived)
DGG arXiv:1112.5179 (PDF read): tetrahedron index

    I_Δ(m,e;q) = Σ_{n≥max(0,−e)} (−1)^n q^{n(n+1)/2 −(n+e/2)m} / ((q)_n (q)_{n+e})     (3.5)

figure-eight gluing (4.18):  I_{4_1}(m,e) = Σ_{e₂∈Z} I_Δ(m−e₂, m+e−e₂) I_Δ(e−e₂, −e₂), with symmetry I(±m,±e) equal (amphichirality) and triality I_Δ(m,e) = (−q^{1/2})^{−e} I_Δ(e,−e−m).

**In-sandbox (this session)**: reproduced DGG (4.20) exactly — I_{4_1}(1,1) = −q −q² +2q³ +7q⁴ +11q⁵ +11q⁶ +3q⁷ −... — and computed new sectors: **I_{4_1}(0,0) = 1 −2q −3q² +2q³ +8q⁴ +18q⁵ +18q⁶ +14q⁷ −12q⁸ −52q⁹...**, I(1,0) = −2q^{3/2} +4q^{7/2} +10q^{9/2}+..., I(2,0) = q³+2q⁴+5q⁵+.... The quantum A-polynomial L̂_{4_1} (DGG eq. 4.43) annihilates the index — an implementable consistency gate.

### 3.3 Twisted indices, large N, black holes (values = couplings × volume)
- Gang–Kim–Lee arXiv:1401.3595 (PDF read): **F = N³ (b+b⁻¹)² vol(M)/(12π)** at large N (so N³·vol/3π at b=1); perturbative expansion terminates at two loops at large N; verified numerically to N≈10 for m004 (vol = 2.02988...).
- Gang–Kim arXiv:1808.02797: twisted partition functions on M_{g,p} backgrounds — universal large-N expressions from two Bethe vacua in terms of vol(M).
- Gang–Kim–Pando Zayas arXiv:1905.01559: N³ term = Bekenstein–Hawking entropy of dual AdS₄ black holes; **log N term matches 11d supergravity one-loop**; expansion terminates at finite order.
- Benini–Gang–Pando Zayas arXiv:1909.11612: large-N superconformal index gives the entropy function of *rotating* AdS₄ black holes.

### 3.4 Z-hat / homological blocks for m004
- GPPV arXiv:1701.06567 define homological blocks (labeled by **abelian** flat connections) for plumbed manifolds etc.; m004 is cusped and hyperbolic (not plumbed), so the applicable object is the knot-complement series.
- **F_{4_1}(x,q)** (Gukov–Manolescu arXiv:1904.06057): the two-variable Z-hat-analogue for the figure-eight is computed \"to any desired order\" via the quantum A-polynomial recursion; x is a boundary-holonomy fugacity — again a coupling. Closed manifolds obtained by surgery on 4_1 get Ẑ via surgery formulas from F_K.
- Resurgent completion for 4_1: Garoufalidis–Gu–Mariño arXiv:2007.10190 (explicit integer Stokes q-series matrices).

## 4. Higher rank and exceptional groups

- **SL(N)/SU(N)**: concrete machinery exists — K-decompositions (Dimofte–Gabella–Goncharov arXiv:1301.0192) build T_N[M3]; state-integral models evaluated numerically for m004 up to N≈10 (1401.3595); large-N controlled by vol with the principal-embedding factor (perturbative PSL(N,C) CS invariants; 1905.01559).
- **Higher-rank Ẑ/F_K**: Park arXiv:1909.13002 (SIGMA 16 (2020) 044) defines Ẑ^G (negative-definite plumbings) and F_K^G (computed for torus knots); higher-rank figure-eight series are frontier, not closed-form.
- **E6 / exceptional**: **no computations exist** in the searched literature for T[m004, E6] or any exceptional-group 3d-3d quantity. The 6d (2,0) theory of type E6 defines T[M3,E6] in principle; every explicit tool (ideal triangulations of flag-type moduli, K-decompositions, cluster coordinates, state integrals) is type-A. Also Ẑ^{E6}(m004) is not even *defined* today (m004 is not a plumbing). This is an honest absence, not an oversight of the search.

## 5. What \"values\" mean here — the H0 dictionary

Every exact quantity above is a function Z(couplings | structure):

| Observer coupling (dial) | Where it appears | Structural residue from m004 |
|---|---|---|
| squashing b | Z(b) = I_{1,2}(b) | vol 2.02988, CS=0 (saddle exponents), 1-loop torsion, arithmetic values at b²∈Q |
| fugacities q, u; charges (m,e) | 3d index I(m,e;q) | integer coefficients; lead(m,e) tentacles = A-polynomial Newton polygon |
| boundary cycle A = pμ+qλ | which SCFT T[M;A] | Z²-family from one object |
| rank N (number of M5s) | all large-N results | N³·vol/(3π), N(N²−1)/6 principal-embedding factor |
| background M_{g,p}, twist | twisted indices; TQFT modular data | Bethe vacua = flat connections; Lee-Yang-type S,T matrices |
| x (holonomy fugacity), q | F_{4_1}(x,q) | integer two-variable series; quantum A-polynomial |

The manifold fixes *functions and integers*; the observer's coupling choice turns them into *numbers*. This is exactly the surviving H0 shape — and the mechanism makes it quantitative and falsifiable (§7 test ideas in structured fields).

## 6. Failure modes (what T[M3] does NOT determine)

1. **Abelian/reducible flat connections are lost** by the DGG construction (Chung–Dimofte–Gukov–Sułkowski arXiv:1405.3663, PDF read: m004 has 3 flat SL(2,C) connections, 2 irreducible + 1 abelian; DGG keeps only the irreducible ones; the trefoil's unique abelian vacuum is lost entirely). Repair still active in 2026 (H.-J. Chung arXiv:2603.05236). T_DGG is therefore not a complete invariant.
2. **UV ambiguity**: 2-tet description singular (DGG §4.4); triangulation/polarization choices give different UV theories, equal only in the IR.
3. **No coupling-free numbers**: nothing dimensionful, no absolute values; only protected (localizable) observables are exact; non-BPS spectrum unknown.
4. **No scale**: dimensions enter only through the M5 embedding (11d Planck / AdS₄ radius) — consistent with the repo's B151 firewall; raising rank organizes dimensionless saddle data only (`speculations/S026_3d3d_state_integral.md:6-11`).
5. **Wrong dimension for the SM**: T[m004] is a 3d N=2 SCFT (IR: two copies of a minimal rank-0 N=4 SCFT) — not a 4d chiral gauge theory; no SM values have been extracted from it anywhere in the verified literature.
6. **Group-theory ceiling**: type-A only in practice; exceptional groups absent (§4).
7. **Non-injectivity surprises**: IR factorization into decoupled copies (§2) means \"one manifold → one interacting dynamics\" fails naively.

## 7. In-sandbox deliverables (demonstrated) and the S026 delta

Scripts (session scratchpad, `/private/tmp/claude-501/-Users-dri-oa-audit-seat/00f419c5-801b-4bbb-8d32-503cc9c44455/scratchpad/`):
- `dgg_fast3.py` — tetrahedron index + triality + gluing; reproduces DGG (4.20) exactly; computes any (m,e) sector to any order in seconds.
- `state_integral.py` — mpmath contour quadrature of I_{1,2}(1); matches the exact GK value to 1e-10.

**S026 delta**: S026's DORMANT-status obstruction (\"the state-integral needs the quantum dilogarithm machinery and a careful contour/saddle analysis — research-level, not a bounded probe\", `speculations/S026_3d3d_state_integral.md:27-31`) is now **demonstrably false at SL(2)**: both the quantum partition function and the full 3d index are bounded, seconds-scale, exactly cross-checked probes. The SL(3)+ state integral remains frontier, as S026 says. B793 can therefore build coupling-model tests directly on the SL(2) quantum objects (test ideas in the structured `coupling_test_ideas` field: b-scan with arithmetic-point protocol, A-cycle enumeration, twist-output modular data vs SM-number protocol, lead(m,e)-vs-A-variety cross-check, coupling-vector factorization test).

---
*Citation discipline: every arXiv ID above was live-verified this session (searched and/or PDF/abstract opened), except Dimofte arXiv:1409.0857, which is marked UNVERIFIED-live and is cited only via the repo's own S026 line 9.*

## KEY PAPERS (structured)
- [VERIFIED] T. Dimofte, D. Gaiotto, S. Gukov (2011 (Commun. Math. Phys. 325 (2014) 367)), "Gauge Theories Labelled by Three-Manifolds" — arXiv:1108.4389
  - Founding DGG paper: defines T[M3] from ideal triangulations; figure-eight is the primary worked example (2-tetrahedron gluing).
- [VERIFIED] T. Dimofte, D. Gaiotto, S. Gukov (2011 (Adv. Theor. Math. Phys. 17 (2013) 975)), "3-Manifolds and 3d Indices" — arXiv:1112.5179
  - PDF read this session. Tetrahedron index eq (3.5); figure-eight index eq (4.18) and series (4.20) [reproduced exactly in-sandbox]; triality (3.11); quantum A-polynomial annihilating the index; statement that the 2-tet T[4_1] (U(1) + 2 chirals charge +1) is singular and the 6-tet refinement is the good description.
- [VERIFIED] S. Garoufalidis, R. Kashaev (2015 (Commun. Num. Theor. Phys. 9)), "Evaluation of state integrals at rational points" — arXiv:1411.6062
  - PDF read this session. The 4_1 state integral I_{1,2}(b) = int_{R+i eps} Phi_b(x)^2 e^{-pi i x^2} dx; exact value at b=1 (eq 2) [matched numerically in-sandbox to 1e-10]; exact evaluations at all b^2 = M/N; saddles = nonabelian parabolic PSL(2,C) reps, Rogers dilog = complex volume (Remark 1.6).
- [VERIFIED] D. Gang, M. Yamazaki (2018 (Phys. Rev. D 98, 121701)), "Three-dimensional gauge theories with supersymmetry enhancement" — arXiv:1806.07714
  - PDF read this session. Precise T_DGG[m004; A=mu] = U(1)_0 + two chirals of charge +1 (eq 23-24); T_DGG[m004; lambda] by gauging U(1)_mu; T_TY[m004; lambda] = T[SU(2)]/SU(2)_diag at level 3 (eq 29); duality (T_{k=-3/2,Q=1})^{x2} = T[m004; lambda] with emergent N=4 SUSY.
- [VERIFIED] H.-J. Chung, T. Dimofte, S. Gukov, P. Sulkowski (2014 (JHEP 04 (2016) 140)), "3d-3d Correspondence Revisited" — arXiv:1405.3663
  - PDF read this session. The key failure mode: DGG theories lose abelian/reducible flat connections; figure-eight has 3 flat SL(2,C) connections (2 irreducible + 1 abelian) and the DGG theory keeps only the irreducible ones.
- [VERIFIED] D. Gang, N. Kim, S. Lee (2014 (Phys. Lett. B 733, 316)), "Holography of Wrapped M5-branes and Chern-Simons theory" — arXiv:1401.3595
  - PDF read this session. Large-N values from couplings x volume: F_gravity = N^3 (b+b^{-1})^2 vol(M)/(12 pi); perturbative expansion terminates at 2 loops at large N; numerics for m004 with vol(S^3\4_1) = 2 Im Li_2(e^{i pi/3}) = 2.02988...
- [VERIFIED] C. Beem, T. Dimofte, S. Pasquetti (2012 (JHEP 12 (2014) 177)), "Holomorphic Blocks in Three Dimensions" — arXiv:1211.1986
  - Abstract fetched + PDF grepped: figure-eight is a worked example; Z_b and index factorize into blocks B^alpha(q) x B^alpha(q~) labelled by massive vacua = flat connections — the precise sense in which 'values' split into object (blocks' q-series) x coupling (q, q~).
- [VERIFIED] S. Gukov, D. Pei, P. Putrov, C. Vafa (2017 (J. Knot Theor. Ramifications 29 (2020) 2040003)), "BPS spectra and 3-manifold invariants (Z-hat / homological blocks)" — arXiv:1701.06567
  - Abstract fetched. Defines homological blocks labeled by abelian flat connections for plumbed 3-manifolds etc.; D^2 x S^1 half-index of T[M3] refines WRT. m004 (cusped, non-plumbed) is covered via the knot-complement variant F_K, not directly.
- [VERIFIED] S. Gukov, C. Manolescu (2019 (Quantum Topol. 12 (2021) 1)), "A two-variable series for knot complements" — arXiv:1904.06057
  - Abstract fetched. F_K(x,q) = Z-hat analogue for knot complements; figure-eight F_K computed to any desired order via quantum-A-polynomial recursion — the answer to 'is Z-hat(m004) known': yes, as F_{4_1}(x,q), a series, not a closed form.
- [VERIFIED] S. Park (2020 (SIGMA 16, 044)), "Higher rank Z-hat and F_K" — arXiv:1909.13002
  - Confirmed via search: defines Z-hat^G (negative-definite plumbings) and F_K^G (computed for torus knots) for general gauge group — higher-rank fig-8 series not yet closed-form; nothing exceptional-group-explicit for m004.
- [VERIFIED] Y. Terashima, M. Yamazaki (2011 (JHEP 08 (2011) 135)), "SL(2,R) Chern-Simons, Liouville, and Gauge Theory on Duality Walls" — arXiv:1103.5748
  - Confirmed via search. The mapping-torus route to T[m004] (once-punctured torus bundle, monodromy conjugate to ST^3): duality-wall theory whose S^3 partition function equals SL(2,R) CS / quantum Teichmueller on the bundle.
- [VERIFIED] J. E. Andersen, R. Kashaev (2011 (Commun. Math. Phys. 330 (2014) 887)), "A TQFT from quantum Teichmueller theory" — arXiv:1109.6295
  - Confirmed via search. The Andersen-Kashaev TQFT whose 4_1 invariant is the state integral above; their volume conjecture framework for it.
- [VERIFIED] D. Gang, N. Kim (2018 (Phys. Rev. D 99, 021901)), "Large N twisted partition functions in 3d-3d correspondence and Holography" — arXiv:1808.02797
  - Confirmed via search: twisted partition functions on M_{g,p} backgrounds at large N — universal expressions from two Bethe vacua in terms of vol(M); couplings (g,p,N) dial the value, volume is the structural input.
- [VERIFIED] D. Gang, N. Kim, L. A. Pando Zayas (2019 (JHEP 03 (2020) 164)), "Precision Microstate Counting for the Entropy of Wrapped M5-branes" — arXiv:1905.01559
  - Abstract fetched. N^3 term = Bekenstein-Hawking entropy of dual AdS4 black holes; log N matches 11d supergravity one-loop; expansion terminates at finite order — the sharpest 'exact values from T[M3]' results, all coupling-dressed volume.
- [VERIFIED] F. Benini, D. Gang, L. A. Pando Zayas (2019 (JHEP 03 (2020) 057)), "Rotating Black Hole Entropy from M5-branes" — arXiv:1909.11612
  - Confirmed via search: superconformal index of T[M3] at large N gives the entropy function of rotating AdS4 black holes — the superconformal index's 'value' role.
- [VERIFIED] S. Garoufalidis, J. Gu, M. Marino (2020 (Commun. Math. Phys. 386 (2021) 469)), "The Resurgent Structure of Quantum Knot Invariants" — arXiv:2007.10190
  - Confirmed via search: 4_1 (and 5_2) worked out completely — Stokes matrices of integer q-series connecting the asymptotic series of the two flat connections; the modern form of the blocks/q-series data for m004.
- [VERIFIED] T. Dimofte, M. Gabella, A. B. Goncharov (2013 (JHEP 11 (2016) 151)), "K-Decompositions and 3d Gauge Theories" — arXiv:1301.0192
  - Surfaced in searches (title+id). The SL(N) generalization T_N[M3] via K-decompositions of ideal triangulations — the concrete higher-rank machinery (type A only).
- [VERIFIED] D. Gang, H. Kim, S. Stubbs (2024 (Phys. Rev. Lett. 132, 131601)), "Three-Dimensional Topological Field Theories and Nonunitary Minimal Models" — arXiv:2310.09080
  - Confirmed via search: topological twists of rank-0 N=4 SCFTs (the T_{-3/2,1} family tied to T[m004; lambda]) give nonunitary minimal-model TQFTs — discrete modular data as coupling-selected outputs.
- [VERIFIED] H.-J. Chung (2026), "3d-3d correspondence and abelian flat connection" — arXiv:2603.05236
  - Abstract fetched: realizes the abelian-flat-connection homological block of a knot complement as a half-index — current status of repairing failure mode (1).
- [UNVERIFIED] T. Dimofte (2014), "Complex Chern-Simons theory at level k via the 3d-3d correspondence" — arXiv:1409.0857
  - UNVERIFIED-live this session (not fetched); cited in repo at speculations/S026_3d3d_state_integral.md:9 as part of the B151 firewall chain (level k <-> dimensionful data). Included for continuity with repo anchors only.

## COMPUTABLE QUANTITIES
- DGG 3d superconformal index I_{4_1}(m,e;q) to arbitrary q-order from the tetrahedron index I_Delta(m,e;q) = sum_n (-1)^n q^{n(n+1)/2-(n+e/2)m}/((q)_n (q)_{n+e}) glued via I_{4_1}(m,e) = sum_{e2 in Z} I_Delta(m-e2, m+e-e2) I_Delta(e-e2, -e2) [DGG 1112.5179 eqs (3.5),(4.18)]. DEMONSTRATED this session: script /private/tmp/claude-501/-Users-dri-oa-audit-seat/00f419c5-801b-4bbb-8d32-503cc9c44455/scratchpad/dgg_fast3.py reproduces the published I(1,1) = -q - q^2 + 2q^3 + 7q^4 + 11q^5 + 11q^6 + 3q^7 exactly, and computes new sectors: I(0,0) = 1 - 2q - 3q^2 + 2q^3 + 8q^4 + 18q^5 + 18q^6 + 14q^7 - ..., I(1,0) = -2q^{3/2} + 4q^{7/2} + 10q^{9/2} + ..., I(2,0) = q^3 + 2q^4 + 5q^5 + .... Key trick: triality I(m,e) = (-q^{1/2})^{-e} I(e,-e-m) maps every charge to a region where the sum is termwise positive-exponent and monotone (runs in seconds).
- S^3_b partition function of T[m004] as a ONE-dimensional integral: Z(b) = I_{1,2}(b) = int_{R+i eps} Phi_b(x)^2 e^{-pi i x^2} dx (Faddeev quantum dilogarithm; contour just above R; absolutely convergent) [Garoufalidis-Kashaev 1411.6062 eq (1) with (A,B)=(1,2)]. DEMONSTRATED at b=1: script /private/tmp/claude-501/-Users-dri-oa-audit-seat/00f419c5-801b-4bbb-8d32-503cc9c44455/scratchpad/state_integral.py evaluates it with mpmath (using the exact b=1 closed form Phi_1(x) = exp[(i/2pi)(Li_2(e^{2pi x}) + 2pi x log(1-e^{2pi x}))], GK eq (23)) and matches the exact value I_{1,2}(1) = (e^{i pi/6}/sqrt3)(e^{V/2pi} - e^{-V/2pi}), V = 2 Im Li_2(e^{i pi/3}) = 2.02988321281930725..., to |diff| ~ 1e-10. Runtime ~1 s.
- Coupling-response scan Z(b) for b in (0,1]: same integrand at general b via the standard integral representation of Phi_b (valid for |Im x| < (b+b^{-1})/2); extract volume from the b->0 saddle growth log|Z| ~ V/(2 pi b^2) and locate the arithmetic points b^2 = M/N where GK Theorem 1.1 gives exact evaluations in terms of Rogers + cyclic dilogarithms at z = e(+-1/6) (the two nonabelian parabolic PSL(2,C) reps).
- Factorization into holomorphic blocks / q-series: write Z(b) as a finite sum of products of q-series (q = e^{2pi i b^2}) and q~-series (q~ = e^{-2pi i b^{-2}}), blocks indexed by the two irreducible flat connections (geometric + conjugate) [Beem-Dimofte-Pasquetti 1211.1986 secs on 4_1; Garoufalidis-Gu-Marino 2007.10190 give the explicit 4_1 q-series and Stokes matrices]. Numerically checkable in-sandbox by comparing block sums to the integral at several b.
- F_{4_1}(x,q) (the Gukov-Manolescu two-variable series = knot-complement analogue of Z-hat for m004) term by term from the quantum A-polynomial recursion; the operator L-hat_{4_1}(M-hat, l-hat; q) that annihilates both the 3d index and F_K is printed in DGG 1112.5179 eq (4.43)/(5.24) and can be implemented directly on the computed index series as an in-sandbox consistency test.
- Charge-lattice response map: lead(m,e) (leading q-power of I_{4_1}(m,e)) over the (m,e) lattice — DGG show its linear-growth 'tentacle' directions reproduce the amoeba/Newton polygon of the classical A-polynomial L_{4_1}: p + p^{-1} = m^2 - m - 2 - m^{-1} + m^{-2}; the repo already owns the SL(n) A-variety side (S026, B71/B83), so this is a direct object-vs-coupling cross-check.
- Rank tower at the classical/1-loop level: PSL(N,C) perturbative CS invariants of m004 around the principal-embedding geometric rep; large-N coefficients are proportional to vol(m004) with F ~ N^3 (b+b^{-1})^2 vol/(12 pi) [Gang-Kim-Lee 1401.3595, verified from PDF: 'F_gravity = N^3 (b+b^-1)^2 vol(M)/12pi'; they confirm numerically up to N ~ 10 via state-integral models]. The N-dependence factor is structural and computable in-sandbox from torsion/volume data.

## COUPLING TEST IDEAS
- Squashing dial b as the canonical H0 coupling: for the FIXED object m004, compute the full function Z(b) on a b-grid (1-dim integral, seconds per point). Protocol-gated test: does any SM-target ratio appear only at special b*, and is that b* itself structural (e.g. b^2 rational, where GK prove the value becomes arithmetic — Rogers dilog + cyclic dilog at e(1/6))? A hit at generic b is a coupling artifact by construction; the object only fixes the function, so the null is sharply defined.
- Discrete coupling = choice of boundary 1-cycle A = p*mu + q*lambda in H1(T^2,Z): the SAME m004 yields a Z^2-family of SCFTs T[m004; A] (Gang-Yamazaki 1806.07714 eqs (23)-(25): mu-theory = U(1)_0 + 2 chirals of charge +1; lambda-theory = gauged version, IR-equal to (T_{k=-3/2,Q=1})^{x2}). Enumerate small (p,q), compute each index in-sandbox, and classify which outputs vary with A (coupling-like) vs which are A-invariant (object-like). This is the cleanest worked example of 'observer choice enters at the level of defining the theory'.
- Topological twist as discrete coupling with DISCRETE output: the m004-adjacent minimal N=4 theory T_{-3/2,1} (two copies = T[m004;lambda]) has topological twists giving nonunitary TQFTs with Virasoro-minimal-model (Lee-Yang-type) modular data (Gang-Kim-Stubbs, PRL 132 (2024) 131601, arXiv:2310.09080). Mechanism-shape lesson for B793: discrete measured-value-like numbers (central charges, S/T matrices, quantum dimensions) emerge from object + discrete coupling choice, not from the object alone. Test: enumerate the twist outputs reachable from m004 and run the repo's base-rate-calibrated SM-number protocol on THAT discrete list (bounded, protocolizable).
- Charge/fugacity response: the index I_{4_1}(m,e;q) is a function on a background-charge lattice; only integer data (coefficients, lead(m,e) slopes) are object-structural, while (m,e,q) are observer dials. Fit the tentacle directions of lead(m,e) against the repo's A-variety tentacles (already in-house from B71/B83) as an explicit object(structure)-vs-coupling(value) decomposition.
- Rank tower as coupling: N (number of M5-branes) is an observer/embedding integer, not a property of m004; values scale as N^3 vol/(3pi) at b=1 with volume as the only object input (1401.3595, 1808.02797, 1905.01559). Test: treat (N, b, g, p in M_{g,p} backgrounds) as the full coupling vector and check that every known exact quantity factors as (structural invariant) x (function of couplings) — any counterexample would falsify the H0 factorized-coupling shape within this mechanism.
- Update S026 (speculations/S026_3d3d_state_integral.md): its stated obstruction ('the state-integral needs quantum-dilogarithm machinery... research-level, not a bounded probe', lines 27-31) is now partially obsolete at SL(2) — this session demonstrated the quantum computation is a bounded ~1 s probe with an exact cross-check to 1e-10. SL(3) state integrals remain frontier; the bounded B793 probe is the SL(2) coupling-response scan plus the discrete (A-cycle, twist) enumerations.

## FAILURE MODES
What T[M3] does NOT determine, verified from primary sources. (1) Missing flat connections: the DGG construction loses abelian/reducible SL(2,C) flat connections — m004 has three flat connections (two irreducible + one abelian) and T_DGG[m004] captures only the two irreducible ones; for the trefoil the DGG theory loses its unique abelian vacuum entirely (Chung-Dimofte-Gukov-Sulkowski 1405.3663, secs 1 and 4.3, read from PDF; still an active repair area — Hee-Joong Chung, arXiv:2603.05236, realizes the abelian homological block as a half-index). So T_DGG[M3] is NOT a complete invariant of M3. (2) UV-description ambiguity: the 2-tetrahedron T[4_1] is 'a bit singular' (DGG 1112.5179 sec 4.4, verbatim: U(1) + 2 chirals of charge +1 with no operator to break the internal-edge topological U(1)); a faithful description needs the 6-tetrahedron refinement; different triangulations/polarizations give different UV theories equal only in the IR. (3) No absolute numbers: every exact quantity is a FUNCTION of observer/background data — squashing b, fugacities q/u, background charges (m,e), boundary-cycle choice A, twist parameters (g,p), rank N. The manifold contributes only structural coefficients: vol (2.02988...), CS invariant (=0 for 4_1), torsions, integer q-series coefficients, modular data. This is exactly the H0 shape, and equally its limitation: T[M3] by itself predicts no dimensionful or coupling-free number. (4) No scale: all outputs are dimensionless; dimensions enter only via the M5-brane embedding (11d Planck scale / AdS4 radius) — consistent with the repo's B151 firewall (S026 lines 6-11). (5) Wrong spacetime dimension for the SM: T[M3] is a 3d N=2 SCFT, not a 4d chiral gauge theory; nothing in the verified literature extracts 4d SM-like values from T[m004]. (6) Only protected quantities are exact: localization gives SUSY-protected observables; the non-BPS spectrum of T[m004] is not known. (7) Rank/group limitations: explicit machinery (ideal triangulations, K-decompositions 1301.0192, cluster coordinates) is type-A; no E6 (or any exceptional) T[m004,G] computation exists in the searched literature — the 6d (2,0) E6 theory defines it only in principle; also Z-hat^G of Park 1909.13002 is defined for negative-definite plumbings, and m004 (hyperbolic, cusped) is not a plumbing, so there is no Z-hat^{E6}(m004) even as a definition today. (8) IR factorization surprises: T[m004; lambda] is IR-dual to TWO DECOUPLED copies of the minimal N=4 theory T_{-3/2,1} (Gang-Yamazaki 1806.07714, Evidence 3) — the map from manifold to interacting dynamics is not injective in the naive way one might hope.
