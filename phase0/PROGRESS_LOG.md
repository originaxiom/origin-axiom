# Phase 0 â PROGRESS_LOG
## 2026-01-01
- Updated repository hygiene: removed Snakemake cache directories and LaTeX build artifacts from version control; extended ignore rules to prevent re-introduction.
- Completed Phase 0 paper build plumbing: added `phase0/paper/main.tex`, `phase0/paper/macros.tex`, `phase0/paper/references.bib`, and a minimal `.latexmkrc` configuration enabling deterministic compilation with XeLaTeX.
- Generated `phase0/paper/main.pdf` from the Phase 0 LaTeX source.

Impact:
- Phase 0 can be cited as the governance and reproducibility contract for Phase 1+ artifacts.
- Subsequent phases may reference Phase 0 definitions and claim taxonomy directly.