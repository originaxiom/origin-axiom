# Self-Consistent Geometric Loop — Preprint Manuscript (`REVTeX 4.2`)

Complete referee-audited `REVTeX 4.2` (`APS PRD` primary, `1`-word toggle to `APS PRX`) 9-page manuscript, self-contained Technical Appendices (`A–C`), and vector figure suite synthesizing Phases 1–11 (`26` Tier-1 + `6` Tier-2 + `4` Bounds = `36` of `36` at `0` continuous fitted or calibrated parameters, `165` of `165` zero-import planted-fault controls).

## Files

- `self_consistent_loop/manuscript/main.tex` — `REVTeX 4.2` manuscript (`Introduction`, `Geometric Framework`, `Computational and Audit Methods`, `Results`, `One-Loop Hyperbolic Audit and Experimental Falsifiability`, `Conclusions`, `Data Availability`, and `Appendices A–C`).
- `self_consistent_loop/manuscript/main.pdf` — Compiled 9-page two-column PDF (`0` overfull boxes, `0` unresolved citations).
- `self_consistent_loop/manuscript/references.bib` — Publisher-verified primary literature bibliography (`26` foundational references).
- `self_consistent_loop/manuscript/review-2026-11-21.md` — Structured `review-paper` audit (`Guidelines 1–9`) and Phase-4 applied changelog.
- `self_consistent_loop/manuscript/SUBMISSION_GUIDE_PRD_ARXIV.md` — Turnkey `arXiv` (`hep-ph`) metadata, pre-flight checklist, and APS *Physical Review D* cover letter.
- `self_consistent_loop/manuscript/build_prd_arxiv_bundle.py` — Deterministic packager & standalone `AutoTeX` (`pdflatex`-only) verifier producing the `main.tex` + `main.bbl` + `figures/*.pdf` upload tarball.
- `self_consistent_loop/manuscript/figures/fig1_progression_and_36_scorecard.pdf` — Campaign progression & `32`-ratio zero-input scorecard.
- `self_consistent_loop/manuscript/figures/fig2_zero_input_unification_and_hierarchy.pdf` — `2`-loop zero-input gauge running & $M^{(5)}$ scale hierarchy.
- `self_consistent_loop/manuscript/figures/fig3_isocurvature_and_cy4_tadpole.pdf` — Axion isocurvature shootout & $\mathbb{P}^1 \times dP_r$ M2-tadpole step.
- `self_consistent_loop/manuscript/figures/fig4_falsifiability_landscape.pdf` — $0\nu\beta\beta$ ($m_{\beta\beta}$ vs. $m_{\mathrm{lightest}}$) & DMRadio-GUT axion ($|g_{a\gamma\gamma}|$ vs. $m_a$) targets.

## Compiling to PDF

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

## Optional APS `PRX` Popular Summary (`208` Words, $\le 250$-Word Limit)

If submitting to *Physical Review X* (by changing `prd` to `prx` on line 1 of `self_consistent_loop/manuscript/main.tex`), include the following non-technical Popular Summary in the APS submission portal:

> Particle physics and modern cosmology rely on roughly two dozen measured constants—governing force strengths, quark and lepton masses, neutrino mixing, dark matter, cosmic inflation, and the survival of matter over antimatter—whose numerical values are inserted from experiment rather than calculated from geometry. Attempts to unify these constants using extra spatial dimensions typically introduce flexible hidden shapes ("moduli") whose unknown sizes replace old free parameters with new ones.
>
> In three spatial dimensions, however, hyperbolic spaces around knots obey Mostow rigidity: their volumes, throat lengths, and closed-loop spectra are fixed mathematical constants that cannot flex continuously. Here we evaluate an eleven-dimensional geometric framework combining the five-sheeted cover of the minimal-volume figure-eight knot complement, its eight chiral Whitehead-link Dehn-surgery overtones, and an elliptic Calabi–Yau fourfold over a del Pezzo surface, audited under a strict code firewall containing zero experimental input numbers.
>
> Across 36 dimensionless particle and cosmological observables and bounds, the zero-parameter equations place 26 quantities within 41% of observation, place 6 renormalization-invariant flavour ratios within a factor of three, and pass all primordial radiation bounds while showing that satellite cosmic microwave background limits rule out purely topological three-dimensional gravity. Ten concrete predictions—led by normal neutrino ordering, a 5.55-MHz dark-matter axion, and a $2.1\times 10^{35}$-year proton lifetime—offer decisive experimental tests over the coming decade.
