# Self-Consistent Geometric Loop — Preprint Manuscript (`REVTeX 4.2`)

Complete referee-ready `REVTeX 4.2` (`APS PRX / PRD`) manuscript and vector figure suite synthesizing Phases 1–10 (`26` Tier-1 + `6` Tier-2 + `4` Bounds = `36` of `36` at `0` continuous fitted or calibrated parameters, `145` of `145` zero-import planted-fault controls).

## Files

- `main.tex` — Seven-section `REVTeX 4.2` manuscript (`Introduction`, `Geometric Framework`, `Computational and Audit Methods`, `Results`, `Analysis and Experimental Falsifiability`, `Conclusions`).
- `references.bib` — Primary literature bibliography (`20` foundational references).
- `figures/fig1_progression_and_36_scorecard.pdf` — Campaign progression & `32`-ratio zero-input scorecard.
- `figures/fig2_zero_input_unification_and_hierarchy.pdf` — `2`-loop zero-input gauge running & `11`-step $M^{(5)}$ hierarchy.
- `figures/fig3_isocurvature_and_cy4_tadpole.pdf` — Axion isocurvature shootout & $\mathbb{P}^1 \times dP_r$ M2-tadpole step.
- `figures/fig4_falsifiability_landscape.pdf` — $0\nu\beta\beta$ ($m_{\beta\beta}$ vs. $m_{\mathrm{lightest}}$) & DMRadio-GUT axion ($|g_{a\gamma\gamma}|$ vs. $m_a$) targets.

## Compiling to PDF

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```
