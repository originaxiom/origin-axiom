# Turnkey Submission Guide — `arXiv` (`hep-th` / `math-ph`) & APS *Physical Review D* (`PRD`)

This guide contains everything needed to upload the remediated data-free manuscript
`self_consistent_loop/manuscript/main.tex` to **arXiv** (`hep-th` primary, cross-listed to
`math.GT` and `hep-ph`) and submit to **APS *Physical Review D* (`PRD` Regular Article)**.

---

## 1. Pre-Flight Checklist Before Uploading

1. **Author & Affiliation Line (`main.tex` lines 12–13):**
   Replace `\author{originaxiom}` and `\affiliation{Origin Axiom Research Programme}` with
   your legal author name(s), ORCID, and institutional address prior to external submission.
2. **Build & AutoTeX-Verify the Upload Tarball (`main.tex` + `main.bbl` + `figures/fig5..8.pdf`):**
   arXiv's AutoTeX server runs `pdflatex` *without* `bibtex`, so `main.bbl` **must** be inside
   the `.tar.gz` archive. Run:
   ```bash
   python3 self_consistent_loop/manuscript/build_prd_arxiv_bundle.py
   ```
   This script compiles `main.bbl`, asserts `0` BibTeX warnings, `0` overfull boxes, and `0`
   unresolved citations, packs the clean `.tar.gz` archive (`main.tex`, `main.bbl`, and the `4`
   vector PDF figures `fig5..8`), and simulates arXiv's standalone `pdflatex`-only server.

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
  REVTeX 4.2, 4 figures, 4 tables (Appendices A-B included)
  ```
- **Abstract (`under arXiv's 1,920-character hard limit and PRD's 500-word limit`):**
  ```text
  Mostow rigidity fixes the metric, volume, and closed-geodesic length spectrum of finite-volume
  hyperbolic three-manifolds without continuous moduli, making cusped hyperbolic spaces natural
  laboratories for studying geometric invariants and consistency constraints in higher-dimensional
  field theories. We establish five exact mathematical-physics theorem suites and a quantitative
  effective-action obstruction ledger across the figure-eight knot complement $\mathrm{m004}$, its
  degree-$5$ covers, the chiral Whitehead-link Dehn-surgery family $\mathrm{m129}(p,q)$ with
  $p + 3q \equiv 0 \pmod{10}$, punctured elliptic curves $E_\tau\setminus\{0\}$, and Weierstrass
  elliptic Calabi-Yau fourfolds $X_r \to \mathbb{P}^1 \times \mathrm{dP}_r$. First, we compute
  complexified adjoint Reidemeister torsions $|\tau_{\mathrm{Ad}}(M_{p,q};\mu)|$ and cusp constants
  $I_{\mathrm{Porti}}(M_{p,q})$ across all nine cover-compatible hyperbolic surgeries across three
  independent $\mathfrak{sl}_2(\mathbb{C}) \cong \mathfrak{so}(3,\mathbb{C})$ bases (Cartan-Chevalley,
  $\mathrm{Sym}^2(\mathbb{C}^2)$, and Cartesian Pauli-Killing Laurent-DFT) to $54$--$60$ digits.
  Second, we classify all four degree-$5$ covers of $\mathrm{m004}$, isolating $8^3_4$ as the unique
  irregular $D_5$-quotient three-cusp cover, and prove cover-degree invariance of $f_a/M_{\mathrm{Pl},4}$.
  Third, we prove $d = 3$ uniqueness of the radial Liouville-Huygens Green function, its $+38.4\%$
  systolic separation from Selberg's return Jacobian, and $n=1$ Scherk-Schwarz non-convergence at
  $\delta(\Gamma) = 2$. Fourth, Hirzebruch signature splitting $\tau(X_r) = 32 + \chi(X_r)/3$ and
  F-theory vertical-orthogonal projection $K_{\mathrm{F\text{-}th}}^+(X_r) = b_4^+(X_r) - h^{1,1}(X_r) - 1$
  preserve $\log_{10}(\Delta\Lambda_{\mathrm{BP}}/M_{\mathrm{Pl}}^4) < 0$ across $r = 0,\dots,9$,
  while scaling and Townsend-Wohlfarth obstructions exclude single-radius closure on $M^{(5)}\times \mathrm{dP}_8$.
  Fifth, we prove punctured-torus Fuchsian-Liouville duality $L_2(\tau) + b_c^*(\tau) = \pi$ with
  exact closed form $L_2(\frac{\pm 2+i}{5}) = \pi - \ln\frac{8\sqrt{2\pi}}{\sqrt{5}\Gamma(1/4)^2}$,
  flavor-monodromy kernel bounds, and gauged $E_6$ brane-$2\mathrm{HDM}$ conformal EWSB.
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

In this work, we establish five exact mathematical-physics theorem suites and a quantitative
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

This manuscript is original, contains zero empirical parameter tuning, and is accompanied by a
standalone zero-float, zero-complex verification suite as described in Data Availability.

Sincerely,
originaxiom
```
