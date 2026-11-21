# Self-Consistent Loop (`Phi(X*) = X*`): Phases 1–11 & Preprint Manuscript

Clean-room (`0 of 19` empirical inputs in Track A) pre-registered implementations, outputs, unit tests, AST-isolated zero-import referee suites, and publication manuscript testing the self-consistent geometric loop across Phases 1–11.

## Directory Layout

- `self_consistent_loop_phi/` — **Phase 1:** Self-consistent Sol/anisotropic torus & modular feedback fixed-point engine (`self_consistent_loop_phi/PREREGISTRATION_PLAN.md`, `self_consistent_loop_phi/SEAL_SHA256.txt`, solver, referee, and tests).
- `cusped_3d_loop_phase2/` — **Phase 2:** 3D cusped hyperbolic Mostow-rigidity, Margulis-throat Laplacian, and chiral-boundary index engine (`cusped_3d_loop_phase2/PREREGISTRATION_PHASE2.md`, `cusped_3d_loop_phase2/SEAL_SHA256.txt`, solver, referee, and tests).
- `relational_yukawa_phase3/` — **Phase 3:** Relational weak-compass quotient (`0.0` enantiomer collapse), 2-component coupled spin-flux Klein-four palindrome protection audit, 3D hyperbolic trilinear Yukawa & Jarlskog CP theorem (`(6)` vs. chiral irreversible `[5, 1, 2, 2]`), and unrigged $E_8$ instanton tadpole audit (`relational_yukawa_phase3/PREREGISTRATION_PHASE3.md`, `relational_yukawa_phase3/SEAL_SHA256.txt`, solver, referee, and tests).
- `unification_cap_lepton_phase4/` — **Phase 4:** Unrestricted $|W| \le 12$ necklace census, 1-loop Fox–Wada Reidemeister acyclicity theorem ($\tau_{\text{Reid}}(k=0)=0$ vs. $\prod_{q=1}^4 \tau_{\text{Reid}}(k\ne 0)=5$), 4D $dP_9$ cusp-cap lattice $\mathbf{I}_{1,9}$ & mod-5 ramification audit, and parameter-free $SU(5)_{\text{GUT}}$ lopsided quark-vs.-lepton CKM/PMNS acid test (`unification_cap_lepton_phase4/PREREGISTRATION_PHASE4.md`, `unification_cap_lepton_phase4/SEAL_SHA256.txt`, solver, referee, and tests).
- `m004_cl10_a4_phase5/` — **Phase 5:** `m004 × Cl(10) × A_4` flavour completion, `Spin(11)` `50`-digit Hosotani EW breaking & UV–IR collar mirror duality, $M^{(5)} = 8^3_4$ `1/5` covering-space systole lift, `7D → 4D` radion stabilization, benchmark-gated `76`-ODE `2`-loop SM + Weinberg RGEs, and `45` planted-fault zero-import referee (`m004_cl10_a4_phase5/PREREGISTRATION_PHASE5.md`, `m004_cl10_a4_phase5/SEAL_SHA256.txt`, solver, referee, and tests).
- `weave_toe_phase6/` — **Phase 6:** Chiral Whitehead parent link `m129` weave unification (`|J_q|` promoted to `Tier 2`), zero-anchor `Spin(11)` NDA gauge couplings & Planck/Weyl/EW hierarchy, `11D` Hořava–Witten parent $\mathbb{R}^{1,3} \times M_3 \times dP_9$ anomaly cancellation, Svrček–Witten $C_3$ axion & radion BBN audit, and `65` cumulative planted-fault zero-import referee (`weave_toe_phase6/PREREGISTRATION_PHASE6.md`, `weave_toe_phase6/SEAL_SHA256.txt`, solver, referee, and tests).
- `inflation_lepton_phase7/` — **Phase 7:** `7D` radion plateau inflation ($A_s$ `Tier 1`, $n_s, r$), `2`-field cylindrical Kähler Affleck–Dine baryogenesis ($\eta_B$ `Tier 2`), `50`-digit Schwinger & Adams $V_{\mathrm{horo}}=\sqrt{3}$ cusp theorem, `Pin_-` odd-systole solar promotion (`12` Tier-1 + `10` Tier-2 = `22` of `24`), symbolic `5/42` Radion–BBN vacuum-energy no-go & Bousso–Polchinski Betti audit, and `85` cumulative zero-import referee (`inflation_lepton_phase7/PREREGISTRATION_PHASE7.md`, `inflation_lepton_phase7/SEAL_SHA256.txt`, solver, referee, and tests).
- `fourfold_majorana_phase8/` — **Phase 8:** Axion isocurvature branch shootout (`Branch 1B-SD` UV self-dual Casimir plateau $\beta_{\mathrm{iso}} = 0.00784 < 0.038$, $A_s$ `Tier 1`), $E_8 \supset \mathrm{Spin}(10) \times \mathrm{SU}(4)$ singlet `(1, 15)` negative-torsion Shell-2 Linear Seesaw (`v10_e8_weave` achieving `12` Tier-1 + `12` Tier-2 = `24` of `24` SM observables), Weierstrass elliptic CY4 $X_8 \to \mathbb{P}^1 \times dP_r$ critical rank $r_{\mathrm{crit}} = 8$ ($\log_{10}(\Delta\Lambda_{\mathrm{BP}}/|V_{\mathrm{bulk}}|) = -192.42 \le -105$ under strict M2-tadpole positivity), and `105` cumulative zero-import referee (`fourfold_majorana_phase8/PREREGISTRATION_PHASE8.md`, `fourfold_majorana_phase8/SEAL_SHA256.txt`, solver, referee, and tests).
- `zero_input_precision_phase9/` — **Phase 9:** $dP_8$ single `(-1)`-curve $B-L$ flux & Georgi–Jarlskog $\mathrm{SU}(5) \subset \mathrm{Spin}(10)$ selection rule (`v11_dP8_gj` promoting `5` SM observables into `Tier 1` $\to$ `17` Tier-1 + `7` Tier-2 = `24` of `24`), `2`-wall Contino–Pilo $-\ln\pi$ threshold & zero-input gauge/hierarchy fixed point ($\alpha_{\mathrm{EM}}^{-1}(M_Z) = 128.138$, $\alpha_s(M_Z) = 0.1135$, $v_{\mathrm{EW}}/M_{\mathrm{Pl,red}}$ `Tier 1`), `'t Hooft`/Coleman zero-input axion misalignment ($\theta_{\mathrm{mis},0} = 0.04487\text{ rad}$, $\Omega_a h^2 = 0.0660$ `Tier 2`, $\beta_{\mathrm{iso}}^{(1\text{B-SD})} = 0.01418 < 0.038$), unified `36`-observable zero-continuous-input scorecard (`23` Tier-1 + `9` Tier-2 + `4` Bounds = `36` of `36`), and `125` cumulative zero-import referee (`zero_input_precision_phase9/PREREGISTRATION_PHASE9.md`, `zero_input_precision_phase9/SEAL_SHA256.txt`, solver, referee, and tests).
- `precision_falsifiability_phase10/` — **Phase 10:** Pati–Salam $\cos\theta_R = \sqrt{3/5}$ hypercharge projection (`v12_dP8_ps` promoting $m_t/m_b \to$ `Tier 1`, `18` of `24` SM Tier-1 hits), $M^{(5)}$ `5`-sheet axion kinetic norm ($\Omega_a h^2 = 0.1686$ `Tier 1`, $\beta_{\mathrm{iso}}^{(1\text{B-SD})} = 0.00287 < 0.038$), `3`-generation chiral anomaly multiplicity ($\eta_B = 7.992\times 10^{-10}$ `Tier 1`), `10`-item experimental falsifiability ledger ($\delta_{\mathrm{CP}} = 197.0^\circ$, $\sum m_\nu = 45.9\text{ meV}$, $m_{\beta\beta} = 4.39\text{ meV}$, $m_a = 22.95\text{ neV}$, $\tau(p \to e^+\pi^0) = 2.12\times 10^{35}\text{ yr}$), unified `26` Tier-1 + `6` Tier-2 + `4` Bounds = `36` of `36` scorecard, and `145` cumulative zero-import referee (`precision_falsifiability_phase10/PREREGISTRATION_PHASE10.md`, `precision_falsifiability_phase10/SEAL_SHA256.txt`, solver, referee, and tests).
- `selberg_determinant_phase11/` — **Phase 11:** `50`-digit $\mathbb{H}^3$ Huygens geodesic propagator exactness & `3`-point vs. `0`-point double-counting theorem (`Clause P11-C1`), `60`-digit Wada–Dubois–Yamaguchi–Porti adjoint $\mathfrak{sl}(2, \mathbb{C})$ Reidemeister torsion ($|\tau_{\mathrm{Ad}}(\mathrm{m004};\mu)| = 2\sqrt{3}$ and modular cusp invariance `< 1e-35` across all `9` `m129` surgeries = `m004` + `8` sibling overtones, `Clause P11-C2`), `4`-branch `1`-loop $M_{p,q}^{(5)}$ partition shootout (`Branch 11A` `11D` SUSY bulk preserving `26` Tier-1 + `6` Tier-2 + `4` Bounds = `36` of `36` vs. `Branch 11D` pure `3D` topological CS falsified by Planck $\beta_{\mathrm{iso}} = 0.82 > 0.038$), and `165` cumulative zero-import referee (`selberg_determinant_phase11/PREREGISTRATION_PHASE11.md`, `selberg_determinant_phase11/SEAL_SHA256.txt`, solver, referee, and tests).
- `manuscript/` — Publication-ready LaTeX manuscript (`manuscript/main.tex`, `manuscript/references.bib`, `manuscript/README.md`, non-destructive referee audit `manuscript/review-2026-11-21.md`) and `4` dimensionless vector/raster figures (`manuscript/figures/`).
- `reports/` — Phase 1–11 comprehensive reports (`reports/phase4_vacuum_cap_lepton_plan.md`, `reports/phase4_unification_cap_lepton_report.md`, `reports/phase5_m004_cl10_a4_report.md`, `reports/phase6_weave_toe_report.md`, `reports/phase7_inflation_lepton_toe_report.md`, `reports/phase8_fourfold_majorana_toe_report.md`, `reports/phase9_zero_input_precision_toe_report.md`, `reports/phase10_precision_falsifiability_toe_report.md`, and `reports/phase11_selberg_determinant_toe_report.md`).

## Reproducing All Suites & Zero-Import Referees

```bash
# Phase 1
cd self_consistent_loop/self_consistent_loop_phi
python3 -m unittest discover -s tests -v

# Phase 2
cd ../cusped_3d_loop_phase2
python3 -m unittest discover -s tests -v

# Phase 3
cd ../relational_yukawa_phase3
python3 -m unittest discover -s tests -v

# Phase 4
cd ../unification_cap_lepton_phase4
python3 -m unittest discover -s tests -v

# Phase 5
cd ../m004_cl10_a4_phase5
python3 -m unittest discover -s tests -v

# Phase 6
cd ../weave_toe_phase6
python3 -m unittest discover -s tests -v

# Phase 7
cd ../inflation_lepton_phase7
python3 -m unittest discover -s tests -v

# Phase 8
cd ../fourfold_majorana_phase8
python3 -m unittest discover -s tests -v

# Phase 9
cd ../zero_input_precision_phase9
python3 -m unittest discover -s tests -v

# Phase 10
cd ../precision_falsifiability_phase10
python3 -m unittest discover -s tests -v

# Phase 11
cd ../selberg_determinant_phase11
python3 -m unittest discover -s tests -v
```
