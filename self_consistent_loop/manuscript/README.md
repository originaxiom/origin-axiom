# Hyperbolic Whitehead Dehn-Surgery Compactifications — Remediated Data-Free Manuscript (`REVTeX 4.2`)

Complete data-free (`0 of 19`), `46`–`60`-digit verified `REVTeX 4.2` (*Physical Review D* Regular
Article) manuscript, self-contained Technical Appendices (`A–B`), and four-figure vector suite
(`fig5`, `fig6`, `fig7`, `fig8`) uniting `Card X-REM12` (`relays/x_rem12_verify/verify_x_rem12_out.json`)
and `Card X-HARVEST-3S-1` (`relays/x_harvest_3s_1_v4/verify_x_harvest_3s_1_v4_out.json`) while
remediating all equation-to-code and bundle items (`X-F1a..e`, `X-F2`) flagged in peer review `AGY-C29`.

All phenomenological `36`-observable scorecard claims from earlier exploratory drafts remain formally
retracted in view of the structural consistency obstructions established in Section V (`Table III`),
while the five pure-mathematical and quantum-field-theoretic theorem suites are proved cleanly.

## Files

- `self_consistent_loop/manuscript/main.tex` — `REVTeX 4.2` data-free manuscript (`Secs. I–VII`,
  `Data Availability`, `4` figures, `4` tables, and `Appendices A–B`).
- `self_consistent_loop/manuscript/main.pdf` — Compiled two-column PDF (`0` overfull boxes,
  `0` BibTeX warnings, `0` unresolved citations).
- `self_consistent_loop/manuscript/references.bib` — Primary literature bibliography (`25` cited
  foundational references, `0` uncited keys, APS `apsrev4-2` clean).
- `self_consistent_loop/manuscript/SUBMISSION_GUIDE_PRD_ARXIV.md` — Turnkey `arXiv` (`hep-th` /
  `math.GT` / `hep-ph`) metadata, pre-flight checklist, and APS *Physical Review D* cover letter.
- `self_consistent_loop/manuscript/build_prd_arxiv_bundle.py` — Deterministic packager & standalone
  `AutoTeX` (`pdflatex`-only) verifier producing `main.tex` + `main.bbl` + `figures/fig5..8.pdf`.
- `self_consistent_loop/manuscript/figures/fig5_porti_torsions_and_covers.pdf` — `60`-digit Porti
  adjoint torsions across all `9` `m129(p, q)` surgeries & degree-`5` cover classification of `m004`.
- `self_consistent_loop/manuscript/figures/fig6_h3_green_and_zss_divergence.pdf` — Exact $d=3$ radial
  $\mathbb{H}^3$ Green function vs. Selberg return factor & $n=1$ Euler-product non-convergence.
- `self_consistent_loop/manuscript/figures/fig7_cy4_signature_and_bp.pdf` — Hirzebruch signature
  splitting $(b_4^+, b_4^-)$ & self-dual $H^4_+$ Bousso-Polchinski flux spacing across $X_r$.
- `self_consistent_loop/manuscript/figures/fig8_three_seat_bridges.pdf` — Punctured-torus duality
  $L_2(\tau) + b_c^*(\tau) = \pi$ (`Hurwitz Gamma(1/4) Fricke closed form`) & gauged $E_6$ brane-`2HDM`
  singlet-driven conformal EWSB.
- *(Historical figures `self_consistent_loop/manuscript/figures/fig1..4.pdf` and
  `self_consistent_loop/manuscript/review-2026-11-21.md` are retained unmoved in place per
  `origin/main:WORKING_RULES.md`.)*

## Compiling to PDF

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```
