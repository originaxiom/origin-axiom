# B793 literature scaffold — complex Chern–Simons + quantum modularity on 4₁ (m004)

**Task**: identify, in the complex-CS / quantum-modularity literature on the figure-eight knot, which numbers are *arithmetically structured functions of the coupling* rather than constants, and whether any known mechanism selects a *distinguished coupling value* — the missing piece of the repo's H0 (object = structure; values = coupling + dynamics).

**Verification discipline**: every citation below marked [V] was found via live search or opened as a PDF in this session. One remembered formula failed its numeric check and is excluded (§6). Repo references are file:line.

---

## 1. The phenomenon: which numbers attached to 4₁ are functions of the coupling

### 1.1 The Kashaev invariant is a function on Q/Z with algebraic values
J(α) = Σ_{m≥0} |(q;q)_m|², q = e^{2πiα}, α ∈ Q/Z — terminating, exact, Galois-equivariant [V: Zagier 2010, Ex. 5; Garoufalidis–Zagier 2111.06645]. Values are algebraic integers in real cyclotomic fields:

| q | 1 | −1 | ζ₃^{±1} | ±i | ζ₅^{±1} | ζ₅^{±2} | ζ₆^{±1} |
|---|---|----|---------|----|---------|---------|---------|
| J | 1 | 5 | 13 | 27 | 46+2√5 | 46−2√5 | 89 |

(reproduced exactly in-sandbox, see §3). The **coupling is the argument**; the **values are arithmetic**.

### 1.2 Volume conjecture: the classical value appears only in a coupling limit
J(1/N) ~ 3^{−1/4} N^{3/2} e^{NV/2π} (1 + (11/36√3)(π/N) + (697/7776)(π²/N²) + (724351/4199040√3)(π³/N³) + …), V = Vol(4₁) = 2 Im Li₂(e^{iπ/3}) = 2.0298832128… [V: Kashaev q-alg/9601025; Murakami–Murakami math/9905075; series from Zagier 2010 eq. (32), read from PDF]. Proved for 4₁ [V: survey 0802.0039]. The subleading series is a power series in π/(N√3) with **rational coefficients** — i.e. coefficients in the trace field Q(√−3) of m004. The repo's substrate field reappears as the *coefficient field of coupling dependence*.

### 1.3 Quantum modularity: the exact law relating values at different couplings
Zagier's QMC (2010, eq. (36)) [V, read from PDF]: for γ ∈ SL(2,Z), γ(∞) = α, X → ∞ through rationals with bounded denominators,

J(γX)/J(X) ~ (π/ħ)^{3/2} exp( Σ_{n≥0} S_n(α) ħ^{n−1} ),  ħ := (π/√3)/(X − γ^{−1}(∞)),

with:
- **S₀(α) = πC/√3, independent of α** (C = V/2π): the volume is coupling-blind;
- **S₁(α) ∈ Q·log K_α^×**: exp(S₁) is essentially an algebraic **unit-like number** in K_α;
- **S_n(α) ∈ K_α** (n ≥ 2), K_α = maximal real subfield of Q(√−3, e^{2πiα}).

Zagier's exact table (read from PDF): exp(S₁(0)) = 1/3; exp(S₁(1/2)) = (2³/3)^{1/2}; exp(S₁(1/3)) = 2·3^{2/3}; exp(S₁(2/3)) = 3^{4/3}; exp(S₁(1/6)) = 2^{7/2}·3^{5/6}; exp(S₁(±1/4)) = 2³(2√3±1)/(3(2±√3)^{1/4}); at denominator 5 the values involve real cyclotomic units ε_k and a prime π₂₉ of norm −29. **This is the cleanest known instance of "the observer's coupling channel α determines an arithmetic value through a cyclotomic extension of the object's trace field."**

Status: proved for 4₁ (essentially) by Bettin–Drappeau via an exact modularity relation for the q-Pochhammer symbol [V: 1905.02045, Math. Ann. 382 (2022)].

### 1.4 The matrix refinement (Garoufalidis–Zagier) [V: 2111.06645, pp. 2–6 read]
- J upgrades to a **matrix** J(X) indexed by the boundary-parabolic SL₂(C) representations of π₁(m004) (3×3 for 4₁ including the trivial rep; 6 nontrivial entries). Refined QMC: J(γX) ≈ j̃_γ(X) J(X) Φ̂_{a/c}(2πi/(c(cX+d))).
- The **cocycle** W_γ(x) = J(γx)^{−1} j̃_γ(x) J(x) is a *smooth matrix-valued function on R* — modularity failure is exactly quantified.
- **Arithmetic aspects** (their words): occurrence of algebraic **units**, Habiro-ring structure, universal denominator bounds; coefficients Φ_α^{(σ,σ')}(h) ∈ Q̄[[h]] in cyclotomic extensions of Q(√−3).
- **Lift of the complex volume**: the refined QMC canonically lifts the complexified volume from C/4π²Z to C. *Repo hook*: this is directly relevant to the B151 firewall note (`speculations/S026_3d3d_state_integral.md:6-11`) which used the mod-4π² ambiguity; the ambiguity is conjecturally resolved by quantum modularity.
- For 4₁ the α-period ("level") is 1 and modularity holds under the **full** SL(2,Z) — 4₁ is maximally symmetric in this sense.
- Perturbative construction of the series from Neumann–Zagier data of the 2-tetrahedron triangulation: [V: Dimofte–Garoufalidis 1202.6268 (all-order series; 1-loop = torsion); Dimofte–Garoufalidis 1511.05628 (series at each root of unity); DGLZ 0903.2472 (all-loop complex-CS perturbation theory)].

### 1.5 The state integral: values as a holomorphic function of the coupling
Andersen–Kashaev TQFT [V: 1109.6295, CMP 330 (2014)]; for 4₁ the partition function is the one-dimensional state integral (in Garoufalidis–Kashaev normalization, read from PDF of 1411.6062):

**I_{A,B}(b) = ∫_{R+iε} Φ_b(x)^B e^{−Aπix²} dx, with 4₁ = I_{1,2}**, Φ_b = Faddeev's quantum dilogarithm; holomorphic in b² ∈ C∖R_{≤0}; manifestly invariant under **b ↔ 1/b** (Faddeev's modular double [V: hep-th/9504111]). Three exact structures:
1. **Factorization** (holomorphic blocks): I_{1,2}(b) = finite sum of products of integer-coefficient Nahm-type q-series in q = e^{2πib²} and q̃ = e^{−2πi/b²} [V: 1304.2705, MRL 24 (2017)]. Values at coupling b are glued from a modular pair (q, q̃).
2. **Rational points** b² = M/N: closed-form evaluation via the Rogers dilogarithm R(z), the cyclic quantum dilogarithm D_N(x;q) = Π(1−q^k x)^{k/N}, and finite state-sums G_{M,N} at roots of unity [V: 1411.6062, Thm 1.1, read from PDF]. The evaluation is syntactically identical to (a) QMC constant terms, (b) 1-loop complex CS, (c) Kashaev's state sums — "not a coincidence" (their words).
3. **Self-dual point b = 1** (eq. (2), read from PDF): **I_{1,2}(1) = (e^{iπ/6}/√3)(e^{V/2π} − e^{−V/2π})** = 0.3287151663 + 0.1897837898i (computed in-sandbox). The two flat connections (geometric/antigeometric, e^{±V/2π}) appear *simultaneously, with an algebraic prefactor in Q(√−3, ζ₁₂)*, at the coupling fixed by b↔1/b.

The q-series matrix realization (a PSL(2,Z)-cocycle of holomorphic functions from the factorized state integral) is [V: Garoufalidis–Zagier 2304.09377].

### 1.6 Resurgence: nonperturbative structure of the coupling plane
- Complex-CS asymptotic series are factorially divergent; Borel/median resummation reconstructs exact values; contributions of other flat connections are encoded in Stokes jumps [V: Gukov–Mariño–Putrov 1605.07615].
- For 4₁ explicitly: the Stokes automorphism is given by **matrices of q-series with integer coefficients**, and a distinguished entry **equals the DGG 3d-index** (BPS state counts) [V: Garoufalidis–Gu–Mariño 2007.10190, abstract fetched; DGG index: 1112.5179, PDF opened]. Verified numerically for 4₁ and 5₂ by the authors.
- The Borel singularities form "**peacock patterns**" — vertical towers indexed by differences of complexified volumes translated by the 4π²Z lattice; trans-series need two nonperturbative variables; Stokes data are generated by a dual linear q-difference equation [V: 2012.00062].
- **Interpretation for H0**: the coupling plane is not homogeneous — it carries an intrinsic pattern of distinguished *rays* (Stokes lines) with integer invariants, but again no distinguished *point*.

### 1.7 The Habiro-ring rigidity (the global statement)
[V: Garoufalidis–Scholze–Wheeler–Zagier 2412.04241]: for a number field K (here Q(√−3)), collections of power series at *every* root of unity that glue arithmetically via a Frobenius, forming a Habiro ring graded by **K₃(K)**, with the gluing controlled by the Bloch-group element (for m004: the 2-tetrahedron Bloch element). The 4₁ Kashaev series is the motivating example. **Consequence**: the entire coupling-dependence of the object's quantum invariants is a single rigid arithmetic object; values at different couplings are not independent data.

---

## 2. Distinguished-coupling mechanisms (the direct answer to the H0 question)

What the literature actually offers:

| Mechanism | What is selected | Status |
|---|---|---|
| **Level quantization** (gauge invariance of CS) | the SET of roots of unity q = e^{2πiα}, α ∈ Q/Z (Habiro locus) | rigorous, foundational; selects a countable set, not a point |
| **Modular-double self-duality b ↔ 1/b** [V: Faddeev hep-th/9504111] | the unique fixed point **b = 1** (τ = b² = 1... boundary of the q, q̃ degeneration), where I_{1,2}(1) has the closed form of §1.5(3) | rigorous; the strongest *point*-selection available; physically it is the maximally symmetric slice of Teichmüller TQFT |
| **Rational points** b² = M/N | algebraic evaluations (Rogers + cyclic dilogarithms) | rigorous [V: 1411.6062]; again a countable set |
| **Stokes rays / peacock pattern** | distinguished RAYS in the coupling plane; integer Stokes constants = 3d-index | conjectural + strong numerics for 4₁ [V: 2007.10190, 2012.00062] |
| **CM / trace-field points** τ ∈ Q(√−3) (e.g. τ = e^{iπ/3}, the shape of m004's tetrahedra) | — | **NOT established as a selection mechanism anywhere in this literature**; the field Q(√−3) appears in *coefficients*, not as a selected coupling. Flagged as an open, repo-original question (test with care, §5) |

**Verdict (exact)**: the literature provides *distinguished coupling sets and rays with rigid arithmetic values on them*, and one genuinely distinguished *point* (b = 1, by symmetry, not by dynamics). **No mechanism selects a unique physical coupling value.** Zagier's S₀(α) being α-independent says the leading classical value (the volume) is *coupling-blind*; everything the coupling controls is subleading and arithmetic (units, torsions, dilogarithms). H0's selector must therefore come from the observer/dynamics side; this literature fixes the *object-side interface* completely: a Galois-equivariant, quantum-modular, Habiro-rigid function on Q/Z (plus its holomorphic b-plane extension).

---

## 3. In-sandbox computables (environment: mpmath 1.3.0, numpy 2.4.0, scipy 1.16.3, sympy 1.14.0, **snappy 3.3.2 installed**)

Demo script (run this session): `/private/tmp/claude-501/-Users-dri-oa-audit-seat/00f419c5-801b-4bbb-8d32-503cc9c44455/scratchpad/qmc_demo.py`. Results:
- J₁…J₆ = 1, 5, 13, 27, 89 — exact match to Zagier's table.
- Volume-conjecture ratio R_N at N = 400/800/1600; Richardson-extrapolated c₁ = 0.5542140 vs predicted 11π/(36√3) = 0.5542165.
- **PSLQ detection of trace-field structure**: mpmath.pslq([c₁/π, 1, 1/√3]) → [36, 0, −11], i.e. the machine recovers c₁ = 11π/(36√3) with no prior knowledge.
- I_{1,2}(1) = 0.328715166319487 + 0.189783789761268i from the closed form; V = 2 Im Li₂(e^{iπ/3}) = 2.02988321281931 (matches repo's vol).

Full computable list:
1. J(α) exactly at any root of unity; Galois orbits (sympy).
2. QMC ratios J(γX)/J(X); extraction of S₁(α) units for denominators ≤ 12; comparison to Zagier's table.
3. Φ_b(z) by quadrature (integral representation, GK 1411.6062 App. A) → direct numerics for I_{1,2}(b) anywhere in the cut b²-plane; b→0 volume-decay check (AK volume conjecture, known for 4₁).
4. Closed-form cross-checks at b² = M/N (GK Thm 1.1: finite sums + Rogers/cyclic dilogarithms) vs quadrature; Taylor coefficients at b = 1.
5. Nahm-type q-series G^±(1,q) and the q/q̃ factorization test.
6. DGG 3d-index of m004 (two-tetrahedron formula, convergent q-series); GGM integer Stokes-constant matching via Borel–Padé of the NZ-data series (`snappy.Manifold('m004')` supplies shapes/NZ data in-house).
7. Dehn-filling family m004(p,q): volumes, CS invariants, exceptional slopes (SnapPy) — a geometric Q-parametrized coupling knob.
8. Exact base rates for any value-matching claim (the candidate sets are enumerable by denominator).

*Repo correction*: `speculations/S027_metallic_quantum_modularity.md:44-45` gates the cocycle/state-integral computation on "SnapPy / Magma / custom state-integral code … beyond the present environment" — **outdated**: snappy 3.3.2 and mpmath are installed; items 1–5 above are bounded probes now.

---

## 4. Failure modes
See structured field; headline items: (i) no unique-coupling theorem — only sets/rays/one symmetric point; (ii) α ∈ Q/Z is an infinite numerology dial — pre-registration + enumerable base rates are mandatory; (iii) Habiro rigidity means pure-CS coupling dependence never leaves Q(√−3)-cyclotomic arithmetic + the single period e^{V/2π} — SM values still require out-of-object dynamics; (iv) conjectural load (matrix RQMC, resurgence, Stokes=index) vs proved (volume conjecture for 4₁, Bettin–Drappeau modularity for 4₁); (v) numerical traps: factorial divergence (optimal truncation), contour poles at ±c_b, factorization degenerating at b = 1; (vi) the Humbert-formula chain for Vol(m004) via ζ_{Q(√−3)}(2) as remembered is numerically false for d = −3 (ratio 1.0114; unit correction needed) — excluded.

## 5. Coupling-test designs for B793
Six pre-registerable tests (structured field for full text): T1 self-dual-point observable algebra at b = 1; T2 Galois-stability obstruction for any "value emerges at α" claim; T3 unit-ladder audit of exp(S₁(α)) vs Bloch-group prediction with base-rate-calibrated null; T4 Stokes-ray point-selection probe (document the expected negative); T5 discrete level-k tower (verify Dimofte 1409.0857 — cited at `speculations/S026_3d3d_state_integral.md:9`, UNVERIFIED this session — before use); T6 Dehn-filling slopes as the geometric coupling knob with a finite distinguished (exceptional-slope) set.

## 6. Negative results from this session (kept, per repo rules)
- CM-point selection (τ ∈ Q(√−3) as a *selected* coupling): **absent from the literature** — do not cite it as known; it is at most a repo-original hypothesis.
- Humbert normalization for d = −3: numerically refuted as remembered (Vol(m004)/(12·3^{3/2}ζ_K(2)/4π²) = 1.0114 ≠ 1). Only Vol(m004) = 2 Im Li₂(e^{iπ/3}) = 6Λ(π/3) = 2.0298832128 is asserted.
- ar5iv HTML of 2111.06645 is broken (fatal conversion error); use the PDF.

## 7. Key sources (all live-verified this session)
[Kashaev q-alg/9601025](https://arxiv.org/abs/q-alg/9601025v2) · [Murakami–Murakami math/9905075 via nLab/search](https://ncatlab.org/nlab/show/volume+conjecture) · [Zagier, Quantum modular forms (PDF, opened)](https://people.mpim-bonn.mpg.de/zagier/files/qmf/fulltext.pdf) · [H. Murakami survey 0802.0039](https://arxiv.org/pdf/0802.0039) · [DGLZ 0903.2472](https://arxiv.org/pdf/0903.2472) · [Andersen–Kashaev 1109.6295](https://arxiv.org/abs/1109.6295) · [DGG 1112.5179 (PDF opened)](https://arxiv.org/abs/1112.5179) · [Dimofte–Garoufalidis 1202.6268](https://arxiv.org/abs/1202.6268) · [GK 1304.2705](https://arxiv.org/pdf/1304.2705) · [GK 1411.6062 (PDF opened)](https://arxiv.org/abs/1411.6062) · [Dimofte–Garoufalidis 1511.05628](https://arxiv.org/abs/1511.05628) · [GMP 1605.07615](https://arxiv.org/abs/1605.07615) · [Bettin–Drappeau 1905.02045 / Math. Ann.](https://link.springer.com/article/10.1007/s00208-021-02288-2) · [GGM 2007.10190](https://arxiv.org/pdf/2007.10190) · [GGM 2012.00062](https://arxiv.org/abs/2012.00062) · [Garoufalidis–Zagier 2111.06645 (PDF opened)](https://arxiv.org/abs/2111.06645) · [Garoufalidis–Zagier 2304.09377](https://arxiv.org/abs/2304.09377) · [GSWZ 2412.04241](https://arxiv.org/abs/2412.04241) · [Faddeev hep-th/9504111](https://archive.org/details/arxiv-hep-th9504111)

## KEY PAPERS (structured)
- [VERIFIED] R. Kashaev (1997), "The hyperbolic volume of knots from quantum dilogarithm" — arXiv:q-alg/9601025 (Lett. Math. Phys. 39 (1997) 269-275)
  - Origin of the volume conjecture: |<4_1>_N| grows like e^{N·Vol/2π}; the first 'value emerges in a coupling limit' statement for m004.
- [VERIFIED] H. Murakami, J. Murakami (2001), "The colored Jones polynomials and the simplicial volume of a knot" — arXiv:math/9905075 (Acta Math. 186 (2001) 85-104)
  - Identifies Kashaev's invariant with the N-colored Jones at q=e^{2πi/N}; makes the coupling = root of unity explicit.
- [VERIFIED] H. Murakami (2008), "An introduction to the volume conjecture and its generalizations" — arXiv:0802.0039
  - Survey; records that the volume conjecture is proved for 4_1 (Ekholm et al.) — 4_1 is the fully rigorous case.
- [VERIFIED] D. Zagier (2010), "Quantum modular forms" — Clay Math. Proc. 11 (2010) 659-675; no arXiv; PDF at people.mpim-bonn.mpg.de/zagier/files/qmf/fulltext.pdf (preprint header says vol. 12)
  - Example 5 = 4_1 as THE prototype quantum modular form. Contains the exact QMC: J(γX)/J(X) ~ (π/ħ)^{3/2}exp(Σ S_n(α)ħ^{n-1}), ħ=(π/√3)/(X−γ^{-1}(∞)); S_1(α)∈Q·log K_α^×, S_n(α)∈K_α (max real subfield of Q(√−3,e^{2πiα})); table of unit values exp(S_1(α)). Opened and read (pp. 10-14).
- [VERIFIED] T. Dimofte, S. Gukov, J. Lenells, D. Zagier (2009), "Exact results for perturbative Chern-Simons theory with complex gauge group" — arXiv:0903.2472 (Commun. Number Theory Phys. 3 (2009) 363-443)
  - All-loop perturbative SL(2,C) CS partition functions on m004; the ħ-expansion whose coefficients are the arithmetically structured 'values'.
- [VERIFIED] J.E. Andersen, R. Kashaev (2011/2014), "A TQFT from quantum Teichmüller theory" — arXiv:1109.6295 (Commun. Math. Phys. 330 (2014) 887-934)
  - The Andersen-Kashaev/Teichmüller TQFT: partition function of 4_1 as a one-dimensional state integral in coupling b; AK volume conjecture (b→0 decay by e^{−Vol/2πb²}).
- [VERIFIED] T. Dimofte, D. Gaiotto, S. Gukov (2011), "3-manifolds and 3d indices" — arXiv:1112.5179
  - The DGG 3d-index: an integer q-series invariant of m004 (BPS counting), later identified as the Stokes data of the perturbative series. Opened PDF (title page verified).
- [VERIFIED] T. Dimofte, S. Garoufalidis (2012/2013), "The quantum content of the gluing equations" — arXiv:1202.6268 (Geom. Topol. 17 (2013) 1253-1316)
  - Defines the all-order formal power series from Neumann-Zagier data of a triangulation (m004 = 2 tetrahedra); 1-loop term = torsion; the algorithmic source of Φ(ħ) coefficients in Q(√−3).
- [VERIFIED] S. Garoufalidis, R. Kashaev (2013/2017), "From state integrals to q-series" — arXiv:1304.2705 (Math. Res. Lett. 24 (2017) 781-801)
  - Factorization of the 4_1 state integral into finite sums of products of Nahm-type q-series in q=e^{2πib²} and q̃=e^{−2πi/b²} — the holomorphic-block structure of coupling dependence.
- [VERIFIED] S. Garoufalidis, R. Kashaev (2014/2015), "Evaluation of state integrals at rational points" — arXiv:1411.6062 (Commun. Number Theory Phys. 9 (2015))
  - THE distinguished-coupling paper: at b²=M/N the 4_1 state integral I_{1,2} evaluates in closed arithmetic form (Rogers dilogarithm + cyclic dilogarithm + finite state sums), and eq. (2) gives the self-dual point value I_{1,2}(1)=(e^{iπ/6}/√3)(e^{V/2π}−e^{−V/2π}), V=Vol(4_1). Opened and read (pp. 1-4).
- [VERIFIED] T. Dimofte, S. Garoufalidis (2015/2018), "Quantum modularity and complex Chern-Simons theory" — arXiv:1511.05628 (Commun. Number Theory Phys. 12 (2018) 1-52)
  - Constructs the QMC power series Φ_α(ħ) at each root of unity from Neumann-Zagier data — the bridge from triangulation combinatorics of m004 to the coupling-dependent arithmetic series.
- [VERIFIED] S. Gukov, M. Mariño, P. Putrov (2016), "Resurgence in complex Chern-Simons theory" — arXiv:1605.07615
  - Founding resurgence analysis: Borel transforms of CS asymptotic series, recovery of nonperturbative (other-flat-connection) contributions from perturbative data via Stokes phenomena.
- [VERIFIED] S. Bettin, S. Drappeau (2019/2022), "Modularity and value distribution of quantum invariants of hyperbolic knots" — arXiv:1905.02045 (Math. Ann. 382 (2022) 1631-1679)
  - Proof side: exact modularity relation for the q-Pochhammer symbol; Zagier's modularity conjecture established for 4_1 (and small knots except 7_2), plus reciprocity/value-distribution laws for J at rational couplings.
- [VERIFIED] S. Garoufalidis, J. Gu, M. Mariño (2020/2021), "The resurgent structure of quantum knot invariants" — arXiv:2007.10190 (Commun. Math. Phys. 386 (2021))
  - For 4_1 explicitly: Stokes automorphism given by matrices of q-series with INTEGER coefficients; a distinguished entry equals the DGG 3d-index (BPS counting) — the nonperturbative side of coupling dependence, numerically matched for 4_1.
- [VERIFIED] S. Garoufalidis, J. Gu, M. Mariño (2020/2023), "Peacock patterns and resurgence in complex Chern-Simons theory" — arXiv:2012.00062 (Res. Math. Sci., 2023)
  - Borel-plane 'peacock' towers of singularities for state integrals on m004-type manifolds; trans-series in two nonperturbative variables; Stokes automorphism factorization via a dual linear q-difference equation — the coupling plane has intrinsic distinguished RAYS.
- [VERIFIED] S. Garoufalidis, D. Zagier (2021), "Knots, perturbative series and quantum modularity" — arXiv:2111.06645
  - The central modern reference; 4_1 is the running example. Matrix-valued invariant J(X) indexed by boundary-parabolic SL_2(C) reps; refined QMC J(γX) ≈ j̃_γ(X)J(X)Φ̂_{a/c}(2πi/(c(cX+d))); smooth matrix cocycle W_γ; occurrence of algebraic UNITS; canonical lift of the complex volume from C/4π²Z to C; level N=1 for 4_1 (full SL(2,Z) modularity). Opened and read (pp. 2-6).
- [VERIFIED] S. Garoufalidis, D. Zagier (2023), "Knots and their related q-series" — arXiv:2304.09377
  - The q-series (holomorphic-block) realization: matrix of periodic holomorphic functions from the factorized Andersen-Kashaev state integral of 4_1 defining a PSL(2,Z)-cocycle — the third realization of the same 'motive'.
- [VERIFIED] S. Garoufalidis, P. Scholze, C. Wheeler, D. Zagier (2024), "The Habiro ring of a number field" — arXiv:2412.04241
  - The deepest arithmetic statement: values at ALL roots of unity glue via Frobenius into one element of a Habiro ring graded by K_3(K) (K=Q(√−3) for 4_1); coupling dependence is globally rigid, controlled by the Bloch group element of m004.
- [VERIFIED] L. Faddeev (1995), "Discrete Heisenberg-Weyl group and modular group" — arXiv:hep-th/9504111 (Lett. Math. Phys. 34 (1995) 249-254)
  - Source of the modular double / b↔1/b duality of the quantum dilogarithm — the symmetry whose unique fixed point b=1 is the self-dual coupling, the strongest 'distinguished coupling value' candidate in this literature.

## COMPUTABLE QUANTITIES
- Kashaev invariant J(α) of 4_1 at any root of unity, exactly (algebraic integers) and in floats: J_N = Σ_{m=0}^{N-1}|(q;q)_m|², O(N) work. DEMO RUN (scratchpad/qmc_demo.py): J_1..J_6 = 1, 5, 13, 27, 89 match Zagier's table exactly; Galois orbits (46±2√5 at ζ_5^{±1}, ζ_5^{±2}) computable via sympy minimal polynomials.
- Volume-conjecture asymptotics and QMC series coefficients by Richardson extrapolation + PSLQ over the Q(√−3) basis. DEMO RUN: c_1 extrapolated 0.5542140 vs predicted 11π/(36√3)=0.5542165; mpmath.pslq([c1/π, 1, 1/√3]) returned [36, 0, −11], i.e. machine-detection that the coefficient lies in Q/√3 (trace-field structure).
- The unit ladder exp(S_1(α)) for α of small denominator (2,3,4,5,6,...): compute J(γX)/J(X) along X→∞ with bounded denominators, strip (π/ħ)^{3/2}e^{S_0/ħ}, extract S_1; compare against Zagier's exact table (1/3, (2³/3)^{1/2}, 2·3^{2/3}, 3^{4/3}, 2^{7/2}·3^{5/6}, 2³(2√3±1)/(3(2±√3)^{1/4}), cyclotomic units and the norm −29 prime at denominator 5).
- Faddeev's quantum dilogarithm Φ_b(z) by mpmath quadrature of its integral representation (properties in GK 1411.6062 Appendix A), hence the 4_1 state integral I_{1,2}(b)=∫_{R+iε}Φ_b(x)²e^{−πix²}dx directly for any b with b²∉R_{≤0} — including complex-coupling scans and the b→0 volume-decay check.
- Closed-form checks at distinguished couplings: (i) self-dual point b=1: I_{1,2}(1)=(e^{iπ/6}/√3)(e^{V/2π}−e^{−V/2π}) = 0.3287151663+0.1897837898i (computed; V=2 Im Li_2(e^{iπ/3})=2.0298832128 confirmed by mpmath.polylog); (ii) rational points b²=M/N via GK Thm 1.1 (Rogers dilogarithm + cyclic dilogarithm D_N + finite state-sums G_{M,N}) cross-checked against direct quadrature; (iii) Taylor coefficients of I_{1,2}(b) at b=1 (GK state eq. (2) extends to them).
- The Nahm-type q-series G^±(x,q) of GK 1304.2705 (integer-coefficient q-hypergeometric sums, fast convergence for |q|<1) and the numerical test of the q/q̃ holomorphic-block factorization of I_{1,2}(b).
- The DGG 3d-index of m004 as an integer q-series from the two-tetrahedron formula (tetrahedron index as a convergent q-series), and the GGM test that Stokes constants of the 4_1 asymptotic series are the corresponding integers (Borel-Padé of the Φ(ħ) series from Dimofte-Garoufalidis NZ data; singularity/peacock map of the Borel plane; m004's NZ data available from installed SnapPy 3.3.2).
- Dehn-filling coupling family m004(p/q) via installed SnapPy: volumes, Chern-Simons invariants, torsions, cusp shapes, and the finite exceptional-slope set — an in-house Q-parametrized 'coupling knob' geometrically realizing the α∈Q/Z structure.
- Base-rate/null calibration for any value search over this arithmetic: the candidate value sets (J(α), exp(S_1(α)), rational-point state-integral evaluations) are countable and enumerable by denominator/height, so exact base rates for 'accidental match to an SM constant' are computable in-sandbox — required by repo protocol before any comparison.

## COUPLING TEST IDEAS
- T1 self-dual-point interface: treat b=1 (the unique fixed point of Faddeev's b↔1/b modular-double duality) as the pre-registered 'observer coupling'. Compute the Taylor algebra of I_{1,2}(b) at b=1 (GK 1411.6062 say eq. (2) extends to Taylor coefficients): test in-sandbox whether every coefficient is (Q(√−3)-algebraic) × (polynomial in e^{±V/2π}), i.e. whether the full observable algebra at the distinguished point stays inside object arithmetic — a sharp, falsifiable H0 statement with no free dial.
- T2 Galois-stability gate for value claims: any 'measured constant emerges at coupling α' claim must come with its full Galois orbit (J and exp(S_1) are Galois-equivariant maps into K_α). Test: for candidate SM dimensionless ratios, determine whether they can even sit Galois-stably in some K_α (generically forces rationality). This converts the SM-value search from scanning to a structural obstruction test — computable with sympy number fields.
- T3 unit-ladder audit: numerically extract exp(S_1(α)) for all α with denominator ≤ 12 from QMC ratios (method demoed in qmc_demo.py), verify against Zagier's table and the Bloch-group/units prediction (Garoufalidis-Zagier 'arithmetic aspects', Calegari-Garoufalidis-Zagier line), then run the pre-registered base-rate-calibrated null: does ANY unit in the ladder match a SM ratio better than the enumerable-haystack base rate? Expected outcome per H0-so-far: clean null, but now on the coupling-interface side rather than the object side — new information either way.
- T4 Stokes-ray selection probe: compute the Borel/peacock singularity pattern of the 4_1 perturbative series (Borel-Padé in-sandbox from NZ-data coefficients) and the integer Stokes constants; verify GGM's Stokes=DGG-3d-index identification for m004. Then ask the H0 question: is there any intrinsic construction (median ray, first Stokes constant, radial ordering) that picks a POINT rather than a ray? Document the negative if not — that would close 'nonperturbative selection' as a mechanism.
- T5 discrete-level tower: complex CS has a quantized discrete coupling (level k∈Z) on top of the continuous one; the Teichmüller TQFT is the k=1 slice (repo already cites Dimofte 1409.0857 at speculations/S026_3d3d_state_integral.md:9 — UNVERIFIED here, verify before use). Model the observer channel as the pair (k, α) and test whether small-k towers (k=1,2,3) reproduce any of the repo's grammar counts (generations, rank data) rather than values — keeping the structure/value firewall explicit.
- T6 Dehn-filling as the geometric coupling knob: the QMC coupling lives on Q/Z, and m004 has an in-house Q-parametrized deformation family with the same shape — filling slopes p/q. SnapPy (installed, 3.3.2) computes vol(m004(p,q)), CS invariants, torsions, and the FINITE exceptional-slope set: a literature-adjacent but repo-original testbed where 'distinguished couplings' form a finite, pre-registerable set. Test whether any observable is singled out at exceptional slopes vs generic ones, with exact base rates. (Framing is ours, informed by the α∈Q/Z structure; not claimed from the literature.)

## FAILURE MODES
(1) No unique-coupling theorem exists: the literature distinguishes SETS of couplings (all roots of unity; the self-dual point b=1; Stokes rays; rational points), never a single physical value — Zagier's S_0(α)=πC/√3 is α-INDEPENDENT, i.e. the leading 'physics' (the volume) is coupling-blind, and everything α-dependent is subleading arithmetic. Any B793 model that needs one selected ħ must import the selector from outside this mathematics and say so explicitly. (2) Numerology hazard is maximal here: the coupling α∈Q/Z is an infinite scan dial, and the emitted values (units in cyclotomic extensions of Q(√−3), dilogarithm exponentials) form a dense, flexible target set; any SM constant can be approximated by scanning α. Protocol must pre-register the selection mechanism BEFORE looking at values, and compute the enumerable base rate (possible in-sandbox, see computables). (3) Habiro-ring rigidity cuts against H0's hope of 'new numbers from coupling': GSWZ show all root-of-unity values are Frobenius-glued into ONE arithmetic object graded by K_3(Q(√−3)) — pure CS coupling dependence never leaves the object's own arithmetic (trace-field cyclotomics + the single exponential period e^{V/2π+...}). Measured SM values would still require coupling to structure OUTSIDE m004 (dynamics, RG, scale), which this literature does not supply; it only constrains what the object-side interface looks like. (4) Conjectural load: the matrix/refined QMC, the resurgence trans-series and the Stokes=3d-index identification are conjectures with strong numerics (proved pieces: volume conjecture for 4_1; Bettin-Drappeau modularity for 4_1); treat higher-loop and Stokes structure as 'numerically established, unproven'. (5) Technical traps for the in-sandbox program: the perturbative series are factorially divergent (need optimal truncation / smoothed optimal truncation as in Garoufalidis-Zagier before any coefficient claims); state-integral quadrature contours pass near poles at ±c_b=±i(b+1/b)/2; at b=1 the q/q̃ factorization degenerates (double poles → derivative terms), so naive block formulas fail exactly at the most interesting point; QMC limits X→∞ must keep bounded denominators or convergence silently changes regime. (6) A remembered-formula failure caught during this task (negatives-first): the Humbert-formula chain 'Vol(m004)=12·|d|^{3/2}ζ_K(2)/(4π²)' is numerically FALSE as stated for d=−3 (ratio 1.0114, unit-correction factor needed for the extra units of Z[ω]); do not propagate it — only Vol(m004)=2 Im Li_2(e^{iπ/3})=6Λ(π/3)=2.0298832128 is verified here.
