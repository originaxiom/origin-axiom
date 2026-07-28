# B793 Harvest: General Catalog of Mechanisms by which Structure + Consistency Yields Numbers

Literature agent report, 2026-07-28. All arXiv IDs / journal refs below were verified by live web search during this session unless explicitly marked UNVERIFIED. Repo assets cited by absolute path.

## 0. Scope

H0 (campaign target, frontier/B793_coupling_campaign/INFORMATION_PLAN.md): m004 supplies STRUCTURE only; VALUES arise from observer-object coupling + dynamics. This report catalogs every mechanism known to physics that converts structure + consistency into numbers, states what each requires as input, and ranks each by attachability to a fixed non-dynamical 3-manifold and testability with existing assets (character variety, A-polynomial in frontier/B67_figure_eight_apolynomial, Maass spectrum and length spectrum in frontier/B792_maass_m004_eigenvalues/, exact cusp scattering in weyl_scattering_check.py).

## 1. The catalog

### Mechanism 1: RG fixed points and the conformal bootstrap
- **Sharpest example:** 3d Ising critical point. From crossing symmetry + unitarity + minimal discrete assumptions, the mixed-correlator bootstrap isolates (Delta_sigma, Delta_epsilon) = (0.5181489(10), 1.412625(10)) — world-record precision numbers from consistency alone. Kos-Poland-Simmons-Duffin-Vichi, arXiv:1603.04436; methodology in El-Showk et al., arXiv:1403.4545.
- **Required input to start:** spacetime dimension d; global symmetry group; which operators exist (spectrum/gap assumptions, e.g. \"exactly one relevant Z2-odd scalar\"); crossing + unitarity. All inputs are DISCRETE/symbolic — no continuous parameter is fed in.
- **Output type:** isolated islands in dimension/OPE space; sharp numbers when the island shrinks.
- **UV variant:** fixed-point boundary conditions can also produce absolute numbers: Shaposhnikov-Wetterich (arXiv:0912.0208) predicted m_H = 126 GeV in 2009 from asymptotic safety of gravity + no new physics — a successful advance prediction.
- **Fit to m004:** conceptually the best fit in the catalog. The grammar supplies exactly the kind of input the bootstrap consumes (symmetry group, multiplicities/generation counting, gap data — e.g. Maass lambda_1). The manifold never needs to be dynamical; it only needs to dictate the discrete assumptions.

### Mechanism 2: Dimensional transmutation
- **Sharpest example:** Lambda_QCD. A classically scale-free theory generates a scale: Lambda = mu exp(-8 pi^2 / (b0 g^2(mu))) (one-loop), with b0 pure counting (11 - 2 n_f/3). The proton/Planck hierarchy is the classic \"huge number from modest input.\" Origin: Coleman-Weinberg, Phys. Rev. D 7, 1888 (1973), DOI 10.1103/PhysRevD.7.1888. Current empirical anchor: FLAG Review 2024, arXiv:2411.04268 (lattice alpha_s and Lambda_MSbar).
- **Required input:** gauge group + matter representation content (pure counting/structure) + ONE reference scale with its coupling value (observer-supplied).
- **Output type:** scale RATIOS as pure numbers; absolute scales only relative to the one supplied anchor.
- **Fit to m004:** immediate. If the grammar fixes candidate groups and matter counting, all beta coefficients and hence all inter-sector scale ratios under a unification boundary condition are parameter-free numbers. This is the cheapest genuinely dynamical mechanism available to the campaign.

### Mechanism 3: Moduli stabilization in string compactifications
- **Sharpest example:** KKLT (arXiv:hep-th/0301240): fluxes + nonperturbative effects stabilize moduli, and every coupling in the 4d theory becomes a number determined by WHERE dynamics parked the vacuum. Precursor: Bousso-Polchinski discretuum (arXiv:hep-th/0004134, JHEP 0006:006): many quantized fluxes make attainable values dense. Statistics: Denef-Douglas, arXiv:hep-th/0404116 (JHEP 05 (2004) 072).
- **Required input:** topology (cycles), integer flux choices, a potential from dynamics, and a vacuum-selection principle.
- **Why predictivity failed:** the integer inputs are unconstrained and the output set is dense — any target can be matched, so a match carries zero bits. The mechanism converts geometry to numbers but destroys falsifiability unless the selection entropy is bounded.
- **Fit to m004:** mostly a NEGATIVE lesson, plus one reusable method. Mostow rigidity means m004 has no metric moduli — nothing to stabilize on the geometric component. The discrete analog of the landscape is the set of Dehn fillings m004(p,q) / representation choices; Denef-Douglas-style density statistics over that set quantifies exactly how many bits any point-picking coupling model would consume (pre-registerable as a gate).

### Mechanism 4: Spectral action + unification boundary conditions (brief; depth covered by another agent)
- **Sharpest example:** Chamseddine-Connes spectral action Tr chi(D/Lambda) (arXiv:hep-th/9606001, Comm. Math. Phys. 186 (1997) 731); full spectral Standard Model with neutrino mixing in Chamseddine-Connes-Marcolli (arXiv:hep-th/0610241, ATMP 11 (2007) 991), which predicted m_H ~ 170 GeV from unification relations at Lambda plus RG running down. Falsified by m_H = 125 GeV — the cleanest historical demonstration that boundary-condition mechanisms make real, killable predictions.
- **Required input:** a spectral triple (the spectrum of an operator — for us, Dirac/Laplace data of m004), a cutoff function, one unification scale, and standard RG running below it.
- **Fit to m004:** direct attachment to banked assets: heat-kernel/Selberg coefficients from frontier/B792_maass_m004_eigenvalues/length_spectrum.json and the Maass eigenvalues in eigenvalues_final.json are precisely spectral-action inputs.

### Mechanism 5: Anthropic / environmental selection
- **Sharpest example:** Weinberg's bound on the cosmological constant (Phys. Rev. Lett. 59, 2607 (1987); standard APS DOI 10.1103/PhysRevLett.59.2607): structure formation bounds Lambda, predicting (pre-1998) a nonzero value of the observed order. Weak-scale version: Agrawal-Barr-Donoghue-Seckel (arXiv:hep-ph/9707380, Phys. Rev. D 57 (1998) 5480) — atomic-existence constraints on the Higgs vev.
- **Required input:** an ENSEMBLE of realized values, a measure over it, and a selection condition. Without all three it is unfalsifiable.
- **Output type:** exclusion windows and likelihood peaks — never sharp values.
- **Fit to m004:** weakest. The object is unique; the only available ensemble is the coupling-parameter space itself. Usable strictly as discipline: any continuous observer dial must declare its measure, and selection reasoning may only exclude, never select.

### Mechanism 6: Self-consistency bootstraps (Chew program, modern S-matrix bootstrap)
- **History:** Chew's 1960s hadronic bootstrap (\"nuclear democracy\") — the ancestor claim that consistency alone fixes the S-matrix. (Original refs from memory: UNVERIFIED; the program failed as a fundamental theory of hadrons but is the direct ancestor of the modern revival.)
- **Sharpest modern examples:** Paulos-Penedones-Toledo-van Rees-Vieira, \"The S-matrix bootstrap I: QFT in AdS\" (arXiv:1607.06109; II: 1607.06110, III: 1708.06765) — unitarity + crossing + analyticity carve out allowed regions numerically. Guerrieri-Penedones-Vieira (arXiv:1810.12849, PRL 122, 241604 (2019)): pion amplitudes sit near the BOUNDARY of the allowed region — real theories saturate consistency bounds. Also \"Where is string theory in the space of scattering amplitudes?\" (arXiv:2102.02847, found in search results).
- **Required input:** symmetries, masses/gaps of lightest states, unitarity + crossing + analyticity.
- **Output type:** bounds and islands; a theory is \"found\" when it saturates a bound.
- **Fit to m004:** we possess an EXACT S-matrix — the arithmetic cusp scattering matrix (Eisenstein phase; frontier/B792_maass_m004_eigenvalues/weyl_scattering_check.py). The bootstrap diagnostic transfers: does the arithmetic point saturate positivity/analyticity bounds where controls (m003) do not?

### Mechanism 7 (repo-specific, answers the key question directly): Quantization of a fixed 3-manifold — volume conjecture, complex Chern-Simons, 3d-3d
- **Sharpest examples:** (a) Volume conjecture: Kashaev's quantum-dilogarithm invariant (1995; original ID UNVERIFIED) = colored Jones at roots of unity (Murakami-Murakami, arXiv:math/9905075) grows as exp(Vol N/2pi); the figure-eight knot is THE canonical worked example, with Vol = 2.02988... (b) Gukov, arXiv:hep-th/0306165 (Comm. Math. Phys. 255 (2005) 577): complex SL(2,C) Chern-Simons on a knot complement is governed classically AND quantum-mechanically by the A-polynomial — the quantum operator A-hat annihilates the partition function. (c) Dimofte-Gaiotto-Gukov 3d-3d correspondence, arXiv:1108.4389 (Comm. Math. Phys. 325 (2014) 367): a triangulated 3-manifold LABELS a dynamical 3d N=2 gauge theory T[M] whose vacuum moduli space is the character variety; m004 is their flagship example. Computation route: Dimofte, arXiv:1102.4847 (state integrals Z(M; hbar)).
- **Required input:** the fixed manifold (all of it: triangulation, A-polynomial, character variety) + ONE quantization parameter (level k / hbar) supplied by the observer + a boundary condition at the cusp.
- **Output type:** exact numbers: partition functions, quantum invariants, recursion coefficients, asymptotic series (vol, CS invariant, torsion) — an infinite family of outputs from one dial.
- **Fit to m004:** this is the only mechanism in the catalog whose defining input is literally a fixed non-dynamical 3-manifold and whose output is a dynamical theory plus numbers. It consumes our best assets (A-polynomial, character variety) natively. Caveat: its natural outputs are geometric numbers already gated null against SM values (B792 discipline applies).

## 2. Answer to the key question

Which mechanisms attach to a FIXED non-dynamical 3-manifold supplying only symmetry/counting data, with the coupling/observer supplying scale?

- **Native attachment:** Mechanism 7 (quantization/3d-3d) — manifold in, dynamics out, hbar is the observer dial.
- **Clean attachment via discrete data:** Mechanism 1 (bootstrap: manifold dictates symmetry + multiplicities + gaps; consistency does the rest) and Mechanism 2 (transmutation: manifold dictates group + counting -> beta coefficients; observer supplies one anchor scale).
- **Attachment via spectrum:** Mechanism 4 (spectral action over the banked Maass/length spectrum, observer supplies cutoff Lambda).
- **Attachment via exact scattering:** Mechanism 6 (cusp S-matrix positivity).
- **Method-only attachment:** Mechanism 3 (selection-entropy accounting over the Dehn-filling discretuum — a gate, not a generator).
- **Discipline-only:** Mechanism 5 (measure honesty for any continuous dial).

## 3. Testability ranking with existing assets

| Rank | Mechanism | Asset used | In-sandbox cost | Falsifiability |
|---|---|---|---|---|
| 1 | TQFT quantization (7) | A-polynomial (B67), exact colored Jones, state integrals | Low (exact arithmetic + quadrature) | High: one dial, many outputs |
| 2 | Dimensional transmutation (2) | Grammar group/counting; B792 base-rate machinery | Trivial | High: parameter-free ratios |
| 3 | Spectral action (4) | length_spectrum.json, eigenvalues_final.json | Medium | High (170 GeV precedent) |
| 4 | Conformal bootstrap (1) | Grammar discrete data, Maass gap | Medium-high (toy truncations feasible; full SDPB heavy) | High if inputs pre-registered |
| 5 | S-matrix bootstrap (6) | weyl_scattering_check.py cusp S-matrix, m003 control | Medium | Medium (boundary-saturation diagnostic) |
| 6 | Moduli/landscape (3) | SnapPy Dehn-filling scans (B125 tooling) | Low | N/A — used as entropy gate |
| 7 | Anthropic (5) | none | — | Low — exclusion-only rule |

## 4. Failure modes (gate-design input)

1. **Input smuggling** (bootstrap): gap/spectrum assumptions chosen to hit a target reintroduce numerology. All discrete inputs must be derived from the grammar and pre-registered.
2. **Landscape degeneracy** (Bousso-Polchinski/Denef-Douglas): if selection entropy (bits of discrete choice) >= match information, the result is worthless. Pre-register a bits-accounting gate.
3. **Ratio/absolute confusion** (transmutation): the mechanism yields ratios; one observer scale is irreducible. Claiming absolutes is a category error.
4. **Falsification-then-rescue** (spectral SM's 170 GeV, then post-hoc sigma-field repair): allow pipelines to die visibly; forbid post-hoc immunization.
5. **Unfalsifiable selection** (anthropics without ensemble + declared measure).
6. **Rigidity mismatch**: m004 has no metric moduli (Mostow); moduli-stabilization intuitions transfer only to the discrete filling/representation set.
7. **Asymptotic charisma**: volume-conjecture outputs are exact and seductive but geometric; B792's clean-null discipline (base-rate calibration, no eyeball matches) applies to every new number channel.

## 5. Proposed coupling tests for B793 (ranked)

1. **Level-as-coupling:** one observer dial (k or hbar) against the full vector of exact m004 quantum outputs; overconstrained by construction.
2. **Transmutation-from-grammar:** grammar group + counting -> 2-loop RG ratios under one unification anchor; gate with B792's sm_comparison methodology (frontier/B792_maass_m004_eigenvalues/sm_comparison_tests.py).
3. **Spectral-boundary-condition:** Selberg/heat-kernel coefficients of m004 -> Chamseddine-Connes-type relations at observer Lambda -> RG down -> visible pass/fail.
4. **Bootstrap-with-grammar-input:** discrete data only; island location = prediction; audit inputs for smuggling.
5. **Cusp-S-matrix positivity:** does the arithmetic point saturate bootstrap-style bounds while m003 does not?
6. **Selection-entropy gate** (from mechanism 3) and **measure-honesty rule** (from mechanism 5) as standing campaign gates.

## 6. Sources (all opened/verified via live search this session)

- [arXiv:1603.04436 — Precision Islands in the Ising and O(N) Models](https://arxiv.org/abs/1603.04436)
- [arXiv:1403.4545 — Solving the 3d Ising Model with the Conformal Bootstrap II](https://arxiv.org/abs/1403.4545)
- [Coleman-Weinberg, Phys. Rev. D 7, 1888 (1973)](https://link.aps.org/doi/10.1103/PhysRevD.7.1888)
- [arXiv:2411.04268 — FLAG Review 2024](https://arxiv.org/pdf/2411.04268)
- [arXiv:hep-th/0301240 — KKLT, de Sitter Vacua in String Theory](https://arxiv.org/abs/hep-th/0301240)
- [arXiv:hep-th/0004134 — Bousso-Polchinski](https://arxiv.org/pdf/hep-th/0004134)
- [arXiv:hep-th/0404116 — Denef-Douglas, Distributions of flux vacua](https://arxiv.org/abs/hep-th/0404116)
- [arXiv:hep-th/9606001 — Chamseddine-Connes, The Spectral Action Principle](https://arxiv.org/pdf/hep-th/9606001)
- [arXiv:hep-th/0610241 — Chamseddine-Connes-Marcolli](https://arxiv.org/pdf/hep-th/0610241)
- [Weinberg, Phys. Rev. Lett. 59, 2607 (1987) — ADS record](https://ui.adsabs.harvard.edu/abs/1987PhRvL..59.2607W)
- [arXiv:hep-ph/9707380 — Agrawal-Barr-Donoghue-Seckel (journal: PRD 57, 5480)](https://arxiv.org/abs/hep-ph/9801253) (companion long paper hep-ph/9801253 also located)
- [arXiv:1607.06109 — S-matrix bootstrap I: QFT in AdS (JHEP 11 (2017) 133)](https://link.springer.com/article/10.1007/JHEP11(2017)133)
- [arXiv:1810.12849 — Bootstrapping QCD Using Pion Scattering Amplitudes](https://www.semanticscholar.org/paper/54de46bd4dd307fc43bdd13cdc9b6a94fc8a6d4c)
- [arXiv:0912.0208 — Shaposhnikov-Wetterich](https://archive.org/details/arxiv-0912.0208)
- [arXiv:hep-th/0306165 — Gukov, 3d Quantum Gravity, CS Theory, and the A-Polynomial](https://arxiv.org/pdf/hep-th/0306165)
- [arXiv:1108.4389 — Dimofte-Gaiotto-Gukov, Gauge Theories Labelled by Three-Manifolds](https://arxiv.org/abs/1108.4389)
- [arXiv:math/9905075 — Murakami-Murakami, colored Jones and simplicial volume](https://arxiv.org/abs/math/9905075)
- [arXiv:1102.4847 — Dimofte, Quantum Riemann Surfaces in Chern-Simons Theory](https://arxiv.org/pdf/1102.4847)

UNVERIFIED (from memory, flagged): Chew's original bootstrap texts; Kashaev's 1995 paper ID (q-alg/9601025); Chamseddine-Connes \"Resilience of the Spectral Standard Model\" (arXiv:1208.1030) as the post-Higgs repair.

## KEY PAPERS (structured)
- [VERIFIED] F. Kos, D. Poland, D. Simmons-Duffin, A. Vichi (2016), "Precision Islands in the Ising and O(N) Models" — arXiv:1603.04436
  - Sharpest existing example of numbers from consistency alone: Delta_sigma = 0.5181489(10) for the 3d Ising point from crossing + unitarity + discrete symmetry input only. Template for what a grammar-fed bootstrap could output.
- [VERIFIED] S. El-Showk, M. Paulos, D. Poland, S. Rychkov, D. Simmons-Duffin, A. Vichi (2014), "Solving the 3d Ising Model with the Conformal Bootstrap II. c-Minimization and Precise Critical Exponents" — arXiv:1403.4545
  - Establishes the bootstrap island methodology; documents exactly what inputs (d, symmetry, spectrum assumptions) are needed to start.
- [VERIFIED] S. Coleman, E. Weinberg (1973), "Radiative Corrections as the Origin of Spontaneous Symmetry Breaking" — 10.1103/PhysRevD.7.1888
  - Origin of dimensional transmutation: a dimensionless-coupling theory generating a scale; the mechanism by which counting data (beta coefficients) plus one reference scale yields pure-number scale ratios.
- [VERIFIED] Flavour Lattice Averaging Group (Y. Aoki et al.) (2024), "FLAG Review 2024" — arXiv:2411.04268
  - Authoritative current lattice determination of alpha_s and the Lambda_MSbar scale — the empirical anchor for the Lambda_QCD transmutation story.
- [VERIFIED] S. Kachru, R. Kallosh, A. Linde, S. Trivedi (2003), "de Sitter Vacua in String Theory (KKLT)" — arXiv:hep-th/0301240
  - Canonical moduli-stabilization construction: values from geometry only AFTER dynamics picks a point in moduli space.
- [VERIFIED] R. Bousso, J. Polchinski (2000), "Quantization of Four-form Fluxes and Dynamical Neutralization of the Cosmological Constant" — arXiv:hep-th/0004134
  - The discretuum: shows how integer flux choices make output values dense — the origin of landscape unpredictivity and the selection-entropy failure mode.
- [VERIFIED] F. Denef, M. R. Douglas (2004), "Distributions of flux vacua" — arXiv:hep-th/0404116
  - Statistical treatment of vacuum counting; the methodology to quantify how many bits of selection a point-picking mechanism consumes — directly reusable for Dehn-filling landscape statistics.
- [VERIFIED] A. H. Chamseddine, A. Connes (1996), "The Spectral Action Principle" — arXiv:hep-th/9606001
  - Numbers from a spectrum + cutoff function + unification boundary conditions; the mechanism that attaches most directly to our banked Maass/length spectrum assets.
- [VERIFIED] A. H. Chamseddine, A. Connes, M. Marcolli (2006), "Gravity and the standard model with neutrino mixing" — arXiv:hep-th/0610241
  - The full spectral-SM pipeline and its Higgs ~170 GeV prediction — the cleanest historical example of a boundary-condition mechanism making, and losing, a falsifiable bet.
- [VERIFIED] S. Weinberg (1987), "Anthropic Bound on the Cosmological Constant" — 10.1103/PhysRevLett.59.2607
  - The one anthropic argument that made a successful advance prediction (nonzero Lambda of the observed order); defines the exclusion-only standard for selection arguments. Journal ref verified via search; DOI is the standard APS form for PRL 59, 2607.
- [VERIFIED] V. Agrawal, S. M. Barr, J. F. Donoghue, D. Seckel (1998), "The anthropic principle and the mass scale of the Standard Model" — arXiv:hep-ph/9707380
  - Anthropic likelihood analysis of the Higgs vev — the template for environmental selection of a coupling-space parameter, and its measure-dependence problem.
- [VERIFIED] M. F. Paulos, J. Penedones, J. Toledo, B. C. van Rees, P. Vieira (2017), "The S-matrix bootstrap. Part I: QFT in AdS" — arXiv:1607.06109
  - Foundation of the modern S-matrix bootstrap (Parts II: 1607.06110, III: 1708.06765); numerical bounds carving allowed regions from unitarity + crossing + analyticity.
- [VERIFIED] A. L. Guerrieri, J. Penedones, P. Vieira (2019), "Bootstrapping QCD Using Pion Scattering Amplitudes" — arXiv:1810.12849
  - Real-world theory (QCD) found sitting near the boundary of the bootstrap-allowed region — the boundary-saturation diagnostic proposed for our cusp S-matrix test.
- [VERIFIED] M. Shaposhnikov, C. Wetterich (2009), "Asymptotic safety of gravity and the Higgs boson mass" — arXiv:0912.0208
  - RG fixed-point boundary condition producing a successful advance number (m_H = 126 GeV): the UV-consistency variant of mechanism 1.
- [VERIFIED] S. Gukov (2003), "Three-Dimensional Quantum Gravity, Chern-Simons Theory, and the A-Polynomial" — arXiv:hep-th/0306165
  - Directly on target: complex Chern-Simons on a fixed knot complement is governed by the A-polynomial; quantization (observer dial hbar) turns our banked A-polynomial into exact numbers. Comm. Math. Phys. 255 (2005) 577.
- [VERIFIED] T. Dimofte, D. Gaiotto, S. Gukov (2011), "Gauge Theories Labelled by Three-Manifolds" — arXiv:1108.4389
  - The 3d-3d correspondence: a fixed non-dynamical 3-manifold (m004 is their flagship example) DEFINES a dynamical QFT T[M] whose moduli space is the character variety — the only known mechanism whose input is literally our object.
- [VERIFIED] H. Murakami, J. Murakami (1999), "The colored Jones polynomials and the simplicial volume of a knot" — arXiv:math/9905075
  - Volume conjecture in Jones-polynomial form: exact quantum invariants of the figure-eight knot grow as exp(Vol N/2pi) — an exactly computable number-from-manifold channel with the level N as the coupling dial.
- [VERIFIED] T. Dimofte (2011), "Quantum Riemann Surfaces in Chern-Simons Theory" — arXiv:1102.4847
  - State-integral construction of Z(M; hbar) for knot complements including m004 — the concrete computation route for the level-as-coupling test.

## COMPUTABLE QUANTITIES
- Colored Jones polynomial of the figure-eight knot J_N(4_1; e^{2pi i/N}) evaluated exactly (integer arithmetic, Habiro-type sum) for N up to thousands: verify exp(Vol(m004) N/(2pi)) growth (volume conjecture, math/9905075), extract subleading torsion term; the observer dial is the root of unity N (= Chern-Simons level). Pure in-sandbox.
- Quantum A-polynomial annihilation check: confirm the known q-difference operator for 4_1 annihilates the colored Jones sequence, and that its q->1 limit reproduces the classical A-polynomial already banked in frontier/B67_figure_eight_apolynomial (Gukov hep-th/0306165 mechanism). In-sandbox symbolic algebra.
- Complex Chern-Simons state-integral partition function Z(m004; hbar) via quantum dilogarithm integrals (Dimofte arXiv:1102.4847) on a grid of hbar: one observer dial producing a continuum of exact numbers; check vol + i CS asymptotics. Numerical quadrature, in-sandbox.
- One- and two-loop beta-function coefficients and Lambda-scale ratios Lambda_i/Lambda_j for every candidate gauge-group/matter assignment the grammar produces, under a single unification boundary condition: parameter-free pure numbers from counting alone (dimensional transmutation); compare to SM ratios with the base-rate-calibration machinery of frontier/B792_maass_m004_eigenvalues/sm_comparison_tests.py. Trivial in-sandbox.
- Selberg-zeta / heat-kernel expansion coefficients and functional determinant of the m004 Laplacian from frontier/B792_maass_m004_eigenvalues/length_spectrum.json (+ m003 control in length_spectrum_m003.json): the ingredients of a spectral-action expansion Tr chi(D/Lambda) for m004, with the cutoff Lambda as the observer dial. In-sandbox.
- Cusp scattering phase / Eisenstein S-matrix and Weyl remainder (extending frontier/B792_maass_m004_eigenvalues/weyl_scattering_check.py): test unitarity/analyticity positivity constraints in S-matrix-bootstrap style on the exact arithmetic scattering data, m004 vs m003 control.
- Dehn-filling landscape statistics via SnapPy (already used in frontier/B125_snappy_arithmeticity): volumes and core-geodesic lengths of m004(p,q) for |p|,|q| <= N, density-of-states of the filling discretuum; quantifies the selection entropy (bits) any point-picking coupling model would consume, Denef-Douglas style (hep-th/0404116).
- Toy crossing-equation bootstrap (1d/small truncation) whose only inputs are grammar-supplied discrete data (symmetry group, generation count = 3 as an operator-multiplicity assumption, gap from Maass lambda_1 in eigenvalues_final.json): does an island form, and where.

## COUPLING TEST IDEAS
- LEVEL-AS-COUPLING (rank 1): posit the observer supplies exactly one quantization dial (CS level k or hbar) coupling to the fixed manifold; compute the full vector of exact outputs (Z(m004;k), colored Jones asymptotics, quantum-A recursion data) as functions of the single dial; a coupling model is falsifiable because one dial must explain many output ratios simultaneously (overconstrained by design).
- TRANSMUTATION-FROM-GRAMMAR (rank 2): take the grammar's candidate gauge group and generation counting as the ONLY manifold input; observer supplies one boundary scale + one unified coupling; run 2-loop RG; every scale RATIO (Lambda_QCD/v analog, hierarchy exponents) is then a pure number from counting; gate against SM ratios with B792-style base-rate calibration.
- SPECTRAL-BOUNDARY-CONDITION (rank 3): build the heat-kernel/Selberg spectral-action coefficients of m004 from the banked length spectrum, impose Chamseddine-Connes-type unification relations at observer-supplied Lambda, RG down, and accept the Higgs-170-GeV lesson: the pipeline must be allowed to fail visibly (falsifiability is the feature).
- BOOTSTRAP-WITH-GRAMMAR-INPUT (rank 4): feed only discrete data from the object (symmetry, multiplicities, a gap assumption from the Maass spectrum) into a small crossing+unitarity bootstrap; if an island forms, its location is a genuine number attributable to m004 structure + consistency, with zero continuous input from us; audit that no target value is smuggled in via the gap assumptions.
- CUSP-S-MATRIX POSITIVITY (rank 5): treat the exact arithmetic scattering matrix at the cusp as a physical S-matrix and impose Paulos-Penedones-style unitarity/analyticity carving; ask whether the arithmetic point (m004) sits on a boundary of the allowed region while controls (m003) sit inside — boundary-saturation is how QCD shows up in the pion bootstrap.
- SELECTION-ENTROPY ACCOUNTING (methodological, from the landscape failure): any coupling model that picks a point (a Dehn filling, a representation, a flux-like integer) must declare its selection entropy in bits BEFORE the match is scored; if bits(selection) >= bits(match), the model is a landscape, not a prediction — pre-register this as a campaign gate.
- MEASURE-HONESTY RULE (from anthropics): any continuous observer dial must come with a declared prior/measure; anthropic-style reasoning is admissible only as exclusion (Weinberg-bound logic), never as selection of a preferred value.

## FAILURE MODES
Seven documented ways these mechanisms fail, all relevant to B793 gate design. (1) Input smuggling: the bootstrap only outputs sharp numbers after discrete spectrum/gap assumptions are fixed; choosing those assumptions to hit a known target reintroduces numerology through the back door — every discrete input must be derived from the grammar and pre-registered. (2) Landscape degeneracy: Bousso-Polchinski/Denef-Douglas showed that a mechanism with enough unconstrained integer choices matches ANY target value and therefore predicts nothing; predictivity died in the flux landscape precisely because selection entropy exceeded match information — quantify bits of selection before scoring any match. (3) Ratio-only outputs mistaken for absolute predictions: dimensional transmutation yields Lambda/mu, never Lambda; one observer-supplied scale is always required, and forgetting this converts an honest ratio prediction into a fake absolute one. (4) Falsification history: the spectral action's sharpest number (Higgs at 170 GeV, hep-th/0610241) was falsified by the 125 GeV measurement — boundary-condition mechanisms produce real predictions that really die; the post-hoc rescue (adding a sigma field) illustrates the temptation to immunize a falsified model. (5) Anthropic unfalsifiability: without an independently motivated ensemble and measure, selection arguments explain everything and predict nothing; m004 is a single rigid object, so any ensemble must live in coupling space and its measure must be declared. (6) Rigidity mismatch: Mostow rigidity means m004 has no metric moduli — moduli-stabilization mechanisms have literally nothing to stabilize on the geometric component; the only landscape analog is the discrete Dehn-filling/representation set, which is where degeneracy risk (2) re-enters. (7) Asymptotic-charisma risk: volume-conjecture-type numbers (2.02988..., CS invariant, torsion) are seductive exact outputs, but B792 already established a clean null for SM values in object spectra; any TQFT-attachment test must gate its outputs with the same base-rate calibration, not eyeball resemblance.
