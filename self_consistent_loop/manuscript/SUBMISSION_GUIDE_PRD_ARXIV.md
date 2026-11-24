# Turnkey Submission Guide — `arXiv` (`hep-th` / `math-ph`) & APS *Physical Review D* (`PRD`)

This guide contains everything needed to upload the remediated data-free manuscript
`self_consistent_loop/manuscript/main.tex` to **arXiv** (`hep-th` primary, cross-listed to
`math.GT` and `hep-ph`) and submit to **APS *Physical Review D* (`PRD` Regular Article)**.

---

## 1. Pre-Flight Checklist Before Uploading

1. **Author & Affiliation Line (`main.tex` lines 12–13):**
   Replace `\author{originaxiom}` and `\affiliation{Origin Axiom Research Programme}` with
   your legal author name(s), ORCID, and institutional address prior to external submission.
2. **Build & AutoTeX-Verify the Upload Tarball (`main.tex` + `main.bbl` + `figures/fig5..14.pdf`):**
   arXiv's AutoTeX server runs `pdflatex` *without* `bibtex`, so `main.bbl` **must** be inside
   the `.tar.gz` archive. Run:
   ```bash
   python3 self_consistent_loop/manuscript/build_prd_arxiv_bundle.py
   ```
   This script compiles `main.bbl`, asserts `0` BibTeX warnings, `0` overfull boxes, and `0`
   unresolved citations, packs the clean `.tar.gz` archive (`main.tex`, `main.bbl`, and the `10`
   vector PDF figures `fig5..14`), and simulates arXiv's standalone `pdflatex`-only server.

---

## 2. Copy-Paste Metadata for `arXiv.org` Submission Portal

- **Primary Category:** `hep-th` (`High Energy Physics - Theory`)
- **Cross-List Categories:** `math.GT` (`Geometric Topology`), `hep-ph` (`High Energy Physics - Phenomenology`)
- **Title:**
  ```text
  Adjoint Reidemeister Torsions, Modular Cusp Invariants, and Consistency Obstructions on Hyperbolic Whitehead Dehn-Surgery Compactifications
  ```
- **Comments Field:**
  ```text
  REVTeX 4.2, 26 pages, 10 figures, 10 tables (Appendices A-B included)
  ```
- **Abstract (`under arXiv's 1,920-character hard limit and PRD's 500-word limit`):**
  ```text
  Mostow rigidity fixes the metric, volume, and geodesic spectrum of finite-volume hyperbolic three-manifolds without continuous moduli, making cusped hyperbolic spaces natural arenas for higher-dimensional consistency tests. We prove eleven exact theorem suites and an obstruction ledger across m000, m004, its degree-5 covers, m129(p,q) (p+3q = 0 mod 10), E_tau \ {0}, and Weierstrass fourfolds X_r -> P^1 x dP_r. (1) Adjoint torsions |tau_Ad| and Porti cusp constants agree across three sl_2(C) bases to 54-60 digits. (2) Among degree-5 covers of m004, 8^3_4 is the unique irregular D_5 three-cusp cover, with d-invariant f_a/M_{Pl,4}. (3) Radial H^d Liouville-Huygens reduction holds uniquely at d=3, while n=1 Euler products diverge at delta(Gamma)=2. (4) Signature splitting keeps log_10(Delta Lambda_BP / M_Pl^4) < 0 (r=0..9), while Townsend-Wohlfarth bounds exclude single-radius closure. (5) Punctured-torus duality L_2(tau)+b_c^*(tau)=pi yields Hurwitz Gamma(1/4) closed forms and conformal EWSB. (6) A 6D E_6 -> G_LR x Z_18^hol orbifold locks N_gen=3 and P_M=-1 dark matter at r_LR=2/5. (7) Holomorphic Lefschetz Yukawas lift Riemann's null quadric to rank 3 and split leptons from down quarks on K_6. (8) 6D Spin(10) supergravity cancels tr R^4 = tr F^4 = 0 and stabilizes (t_*,s_*,tau_*) at a dS minimum. (9) Hirzebruch F_k lifts give E/N=8/3 Strong-CP relaxation, spin-1/2 Liouville ordering, and 8^3_4 lopsided (2,0,3) seesaw mixing. (10) Green-Schwarz pairing f_vis=S+2T, f_hid=S+T locks t_*=2s_*, generates m_{3/2}/M_Pl = 3.48e-13 at alpha_GUT^{-1}=30.19, unifies |lambda_S|=|y_t| via E_6, and traps 60-e-fold inflation. (11) Minimal volume (m000 -> m004 -> 8^3_4), Spin(10)-D_5 centralizers, Gamma_0(2) equivariance, and constant-Polonyi Mirage Split-SUSY (tan beta=1.694) establish the countermodel-certified input floor.
  ```

---

## 3. Cover Letter for APS *Physical Review D* (`Regular Article`)

```text
Dear Editors of Physical Review D,

Please consider our manuscript, "Adjoint Reidemeister Torsions, Modular Cusp Invariants, and
Consistency Obstructions on Hyperbolic Whitehead Dehn-Surgery Compactifications," for publication
as a Regular Article in Physical Review D.

Because finite-volume hyperbolic three-manifolds possess rigid metrics, volumes, and closed-geodesic
length spectra by Mostow's theorem, they provide an exact arena for testing one-loop quantum gravity
determinants, Kaluza-Klein axion scaling laws, punctured-torus uniformization, and higher-dimensional
compactification consistency conditions without adjustable continuous geometric moduli.

In this work, we establish ten exact mathematical-physics theorem suites and a quantitative
effective-action obstruction ledger across m004, its degree-5 covers, the Whitehead surgery family
m129(p, q), punctured elliptic curves E_tau \ {0}, and Weierstrass Calabi-Yau fourfolds X_r -> P^1 x dP_r:
1. Multi-basis 54-60-digit computation of adjoint Reidemeister torsions and SL(2, Z)-invariant Porti
   cusp constants across all nine hyperbolic surgeries satisfying p + 3q = 0 (mod 10) across Chevalley,
   Sym^2(C^2), and step-free Cartesian Pauli-Killing SO(3, C) Laurent-DFT representations.
2. Complete classification of all four connected degree-5 covers of m004 (isolating 8^3_4 as the unique
   three-cusp torsion-free irregular D_5 cover) and exact cover-degree invariance of f_a / M_{Pl,4}.
3. Uniqueness of the d = 3 radial Liouville-Huygens H^d Green function, its +38.4% systolic separation
   from Selberg's return Jacobian, and n = 1 Euler-product non-convergence at delta(Gamma) = 2.
4. Hirzebruch signature splitting tau(X_r) = 32 + chi(X_r)/3 and F-theory vertical-orthogonal rank
   K_{F-th}^+(X_r) = b_4^+(X_r) - h^{1,1}(X_r) - 1 preserving dense negative flux spacing across r = 0..9,
   paired with scaling, curvature, and Townsend-Wohlfarth single-radius no-go theorems and exact two-loop
   Luo-Xiao/Buttazzo Standard Model RGE verification (rational benchmark 16142087 / 800000).
5. Punctured-torus Fuchsian-Liouville duality L_2(tau) + b_c^*(tau) = pi with closed-form Hurwitz
   identity L_2((+-2+i)/5) = pi - ln[8 sqrt(2 pi) / (sqrt(5) Gamma(1/4)^2)], spin-antiperiodic Lefschetz
   kernel bounds, and gauged E_6 brane-2HDM unification with singlet-driven conformal EWSB.
6. Anomaly-free 6D coroot orbifold E_6 -> G_LR x Z_18^hol multiplet splitting locking N_gen = 3 and
   P_M = -1 Majorana dark matter via mod-9 [Z_3]^3 cancellation and M_g < 31, achieving exact
   r_LR = 2/5 unification, full-rank seesaw M_R != 0, and s-wave pseudoscalar-portal annihilation.
7. Purely tau-holomorphic punctured-torus Lefschetz Yukawas on E_tau \ {0} canceling antipodal drift,
   lifting Riemann's single-point null quadric to rank 3 across all five fermion/seesaw sectors, breaking
   E[5] lepton-down degeneracy parameter-freely on K_6, and preserving I_3 spin-cover Kahler metricity.
8. Six-dimensional N=(1,0) Spin(10) supergravity on T^2 / (Z_2 x Z_2') canceling tr R^4 = tr F^4 = 0
   with factorized I_8, stabilizing all four real moduli (t_*, s_*, Re tau_*, Im tau_*) at a positive-definite
   dS minimum without embedded coordinates, protecting the Higgs mass via Scherk-Schwarz supersymmetry,
   and fixing bounded-from-below D/F-term 2HDM quartics with spontaneous CP violation J_CKM(tau_*) != 0.
9. Universal 11-member Morrison-Vafa Hirzebruch F_k Spin(10) Green-Schwarz factorization with F_6
   tensor-axion Strong-CP relaxation (E/N = 8/3), Gamma_0(2) generalized-CP geodesic semicircle lock,
   chiral spin-1/2 hyperbolic Liouville Kahler normalization restoring undressed CKM ordering, and
   zero-free-integer 8^3_4 cusp-ramified lopsided seesaw flavor n_10 = (2, 0, 3).
10. Parameter-free Hirzebruch Green-Schwarz pairing f_vis = S + 2T (n_16 = 0) and f_hid = S + T (n_16 = 2)
    locking t_* = 2 s_* with 13-decade racetrack transmutation (m_{3/2}/M_Pl = 3.48e-13, V_min = 1.52e-26
    at alpha_GUT^{-1} = 30.19), 78-generator E_6 Albert-Jordan cubic coupling unification |lambda_S| = |y_t|,
    bounded-from-below radiative U(1)_chi breaking (v_chi = 1.62 m_{3/2}), two-stage SUSY-to-2HDM RGEs,
    coupled 60-e-fold valley Starobinsky inflation, and Weierstrass CY_4 b_4^+ flux neutralization.

This manuscript is original, contains zero empirical parameter tuning, and is accompanied by a
standalone zero-float, zero-complex verification suite across ninety planted-fault controls.

Sincerely,
originaxiom
```
