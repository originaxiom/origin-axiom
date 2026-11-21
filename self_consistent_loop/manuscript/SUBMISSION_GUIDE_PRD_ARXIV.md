# Turnkey Submission Guide — `arXiv` (`hep-ph`) & APS *Physical Review D* (`PRD`)

This guide contains everything needed to upload `self_consistent_loop/manuscript/main.tex` to **arXiv** (`hep-ph` primary, cross-listed to `hep-th` and `astro-ph.CO`) and submit directly to **APS *Physical Review D* (`PRD` Regular Article)**.

---

## 1. Two-Minute Pre-Flight Checklist Before Uploading

1. **Author & Affiliation Line (`main.tex` lines 13–15):**
   Open `self_consistent_loop/manuscript/main.tex` and replace `\author{Origin Axiom Research}` and `\affiliation{Independent Theoretical Physics Collaboration}` with your exact legal author name(s), ORCID, and institutional or independent address.
2. **Public Replication URL (`main.tex` line 261, `\section*{Data Availability}`):**
   Once you push or archive your replication snapshot (`e.g.` Zenodo DOI or public GitHub release URL), paste that permanent URL/DOI into `\section*{Data Availability}` in `self_consistent_loop/manuscript/main.tex`.
3. **Build & AutoTeX-Verify the Upload Tarball (`main.tex` + `main.bbl` + `figures/*.pdf`):**
   arXiv's AutoTeX server runs `pdflatex` *without* `bibtex`, so `main.bbl` **must** be inside the `.tar.gz` archive. Run:
   ```bash
   python3 self_consistent_loop/manuscript/build_prd_arxiv_bundle.py --out ~/Desktop/arxiv_prd_submission_bundle.tar.gz
   ```
   This script compiles `main.bbl`, checks for `0` overfull boxes and `0` unresolved citations, packs the clean `.tar.gz` archive, and simulates arXiv's standalone `pdflatex`-only server in a fresh temporary directory to verify the 10-page PDF builds cleanly.

---

## 2. Copy-Paste Metadata for `arXiv.org` Submission Portal

- **Primary Category:** `hep-ph` (`High Energy Physics - Phenomenology`)
- **Cross-List Categories:** `hep-th` (`High Energy Physics - Theory`), `astro-ph.CO` (`Cosmology and Nongalactic Astrophysics`)
- **Title:**
  ```text
  Zero-Input Gauge-Yukawa-Cosmology Closure and Experimental Falsifiability on a Hyperbolic-Fano Fourfold Loop
  ```
- **Comments Field:**
  ```text
  10 pages, 4 figures, 4 tables, REVTeX 4.2 (Appendices A-D included)
  ```
- **Abstract (`1,801` characters — verified under arXiv's `1,920`-character hard limit and `PRD`'s `500`-word limit):**
  ```text
  Extra-dimensional grand unified models normally exchange four-dimensional Yukawa parameters for continuous bulk moduli, boundary thresholds, and initial cosmological angles. We evaluate a parameter-free geometric fixed-point framework that couples the five-sheeted cusped hyperbolic cover $M^{(5)} \to \mathrm{m004}$, chiral Whitehead surgery saddles on $\mathrm{m129}$, and an $E_8 \supset \mathrm{Spin}(10) \times \mathrm{SU}(4)$ Weierstrass elliptic fourfold $X_8 \to \mathbb{P}^1 \times dP_8$ under a two-track provenance firewall with zero empirical inputs in Track A. Across $36$ dimensionless Standard Model and cosmological observables and bounds, the zero-continuous-input solver places $26$ observables within $\pm 0.15\,\mathrm{dex}$ of experiment, places $6$ renormalization-group-quasi-invariant ratios within $\pm 0.50\,\mathrm{dex}$, and satisfies all $4$ vacuum and primordial bounds with zero misses, audited by $165$ zero-import planted-fault controls. Exact one-loop hyperbolic fluctuation analysis proves to $50$ digits that three-dimensional geodesic propagators receive zero subleading $1/\ell$ curvature corrections, reproduces Porti's adjoint Reidemeister torsion $|\tau_{\mathrm{Ad}}(\mathrm{m004};\mu)| = 2\sqrt{3}$ to $46$ digits, and shows that Planck's axion isocurvature bound excludes pure topological three-dimensional Chern-Simons weighting ($\beta_{\mathrm{iso}} = 0.825$) in favor of the eleven-dimensional supersymmetric bulk ($\beta_{\mathrm{iso}} = 0.00287$). The fixed point predicts normal neutrino ordering with $\sum m_\nu = 45.92\,\mathrm{meV}$, $m_{\beta\beta} = 4.39\,\mathrm{meV}$, $\delta_{\mathrm{CP}} = 197.0^\circ$, a $22.95\,\mathrm{neV}$ ($5.55\,\mathrm{MHz}$) QCD axion, and proton lifetime $\tau(p \to e^+\pi^0) = 2.12\times 10^{35}\,\mathrm{yr}$.
  ```

---

## 3. Ready-to-Send Cover Letter for APS *Physical Review D* (`Regular Article`)

```text
Dear Editors of Physical Review D,

Please consider our manuscript, "Zero-Input Gauge-Yukawa-Cosmology Closure and Experimental Falsifiability on a Hyperbolic-Fano Fourfold Loop," for publication as a Regular Article in Physical Review D.

Extra-dimensional grand unified theories and string/M-theory compactifications typically eliminate four-dimensional Yukawa couplings only at the cost of introducing continuous geometric moduli, adjustable Kaluza-Klein threshold corrections, or tuned pre-inflationary axion misalignment angles—or else run afoul of Planck bounds on cold-dark-matter axion isocurvature and Super-Kamiokande bounds on dimension-six proton decay.

In this work, we construct and audit a parameter-free geometric unification fixed point combining Mostow rigidity on the five-sheeted cover M^(5) of the minimal-volume cusped hyperbolic figure-eight complement m004, its eight chiral Whitehead-link Dehn-surgery overtones on m129, and an E_8 -> Spin(10) x SU(4) Weierstrass elliptic Calabi-Yau fourfold X_8 -> P^1 x dP_8. To guard rigorously against post-hoc parameter tuning, all theoretical solver modules (Track A) are enforced by static abstract-syntax-tree scanning to contain zero empirical float literals, and all calculations are independently verified by zero-import referee scripts across 165 planted-fault controls (with complete explicit 3x3 Yukawa and seesaw shell operators, UV boundary matching, and the 36-observable ledger provided in Appendices A-D).

Four technical results anchor the paper for the Physical Review D readership across particle phenomenology, early-universe cosmology, and quantum gravity:
1. Two-wall Contino-Pilo orbifold zeta thresholds (-ln pi) and Adams' maximal horoball cusp volume (sqrt(3)) fix the unified gauge coupling and Planck-to-weak hierarchy with zero continuous inputs, yielding alpha_EM^{-1}(M_Z) = 128.138 (+0.15%), alpha_s(M_Z) = 0.1135 (-3.70%), and v_EW / M_{Pl,red} = 1.17 x 10^{-16} (+15.3%).
2. Across 36 dimensionless Standard Model and cosmological observables and bounds integrated via the coupled 76-component two-loop RGEs, the zero-parameter fixed point places 26 observables within +-0.15 dex of experiment, places 6 RG-quasi-invariant flavour ratios within +-0.50 dex, and satisfies all 4 primordial and vacuum bounds with zero misses.
3. Exact one-loop hyperbolic fluctuation analysis proves to 50 digits that three-dimensional geodesic propagators receive zero subleading 1/ell curvature corrections, verifies Porti's adjoint Reidemeister torsion |tau_Ad(m004; mu)| = 2*sqrt(3) to 46 digits across presentations, and demonstrates that Planck's axion isocurvature bound (< 0.038) decisively rules out pure three-dimensional topological Chern-Simons saddle weighting (beta_iso = 0.825) in favor of the eleven-dimensional supersymmetric bulk (beta_iso = 0.00287).
4. Because there are zero continuous parameters to retune, the framework makes ten sharp, falsifiable predictions for near-term experiments: normal neutrino mass ordering with sum m_nu = 45.92 meV (DESI-II/CMB-S4), m_{beta beta} = 4.39 meV (LEGEND-1000/nEXO), delta_CP = 197.0 deg (DUNE/Hyper-Kamiokande), a 22.95 neV / 5.55 MHz QCD dark-matter axion (DMRadio-GUT), beta_iso = 0.00287 (CMB-S4), and proton lifetime tau(p -> e^+ pi^0) = 2.12 x 10^{35} yr via E_8 SU(4) split-multiplet orthogonality (Hyper-Kamiokande).

This manuscript is original, is not under consideration elsewhere, and comes with a complete open-source replication and verification suite as described in the Data Availability statement.

Sincerely,
[Author Name(s)]
```
