# Hyperbolic Whitehead Dehn-Surgery Compactifications — Remediated Data-Free Manuscript (`REVTeX 4.2`)

Complete data-free (`0 of 19`), `60`-digit verified `REVTeX 4.2` (*Physical Review D* Regular Article) manuscript, self-contained Technical Appendices (`A–B`), and vector figure suite (`fig5`, `fig6`, `fig7`) remediating all findings of peer audit `AGY002_PEER_AUDIT_AGY_EXP_45FE6E401` (`Card X-REM12`, sealed raw output `relays/x_rem12_verify/verify_x_rem12_out.json`).

All phenomenological `36`-observable scorecard claims from earlier exploratory drafts are formally retracted in view of the five structural consistency obstructions established in Section VI (`Table III`), while the exact pure-mathematical and quantum-field-theoretic theorems are proved and triple-verified cleanly.

## Files

- `self_consistent_loop/manuscript/main.tex` — `REVTeX 4.2` data-free manuscript (`Introduction`, `Adjoint Reidemeister Torsions and Modular Cusp Invariants`, `Degree-5 Cover Classification and Multi-Sheet Axion Scaling`, `Hyperbolic Propagators, Selberg Return Factors, and Critical-Exponent Divergence`, `Weierstrass Fourfold Signature Splitting and Self-Dual Flux Lattices`, `Effective-Action Obstructions and Repaired Two-Loop RGEs`, `Conclusions`, `Data Availability`, and `Appendices A–B`).
- `self_consistent_loop/manuscript/main.pdf` — Compiled two-column PDF (`0` overfull boxes, `0` BibTeX warnings, `0` unresolved citations).
- `self_consistent_loop/manuscript/references.bib` — Primary literature bibliography (`21` foundational references, APS `apsrev4-2` clean).
- `self_consistent_loop/manuscript/SUBMISSION_GUIDE_PRD_ARXIV.md` — Turnkey `arXiv` (`hep-th` / `math-ph`) metadata, pre-flight checklist, and APS *Physical Review D* cover letter.
- `self_consistent_loop/manuscript/build_prd_arxiv_bundle.py` — Deterministic packager & standalone `AutoTeX` (`pdflatex`-only) verifier producing the `main.tex` + `main.bbl` + `figures/fig5..7.pdf` upload tarball.
- `self_consistent_loop/manuscript/figures/fig5_porti_torsions_and_covers.pdf` — `60`-digit Porti adjoint torsions across all `9` `m129(p, q)` surgeries & degree-`5` cover classification of `m004`.
- `self_consistent_loop/manuscript/figures/fig6_h3_green_and_zss_divergence.pdf` — Exact $d=3$ radial $\mathbb{H}^3$ Green function vs. Selberg return factor & $n=1$ Scherk-Schwarz Euler-product non-convergence at $\delta(\Gamma) = 2$.
- `self_consistent_loop/manuscript/figures/fig7_cy4_signature_and_bp.pdf` — Hirzebruch signature splitting $(b_4^+, b_4^-)$ & self-dual $H^4_+$ Bousso-Polchinski flux spacing across $X_r \to \mathbb{P}^1 \times \mathrm{dP}_r$ ($r = 0,\dots,9$).
- *(Historical figures `self_consistent_loop/manuscript/figures/fig1..4.pdf` and `self_consistent_loop/manuscript/review-2026-11-21.md` are retained unmoved in place per `origin/main:WORKING_RULES.md` Rule 9.)*

## Compiling to PDF

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```
