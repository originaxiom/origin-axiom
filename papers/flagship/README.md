# Flagship preprint — the whole-repo integrative paper

A self-generating object: the metallic once-punctured-torus family, its trace-map tower,
and the boundary between structure and scale.

This is a **preprint / thesis-style artifact**, not a journal submission. It deliberately
draws the whole project into one narrative — the object, the tower, the figure-eight
A-polynomial family, chirality, and the class-S bridge / dimensional firewall — and is
held together by an explicit proof-status discipline rather than by uniform novelty.

## What it claims, and how to read it

Every result carries a proof-status badge:

| badge | meaning |
|---|---|
| PROVED | exact and machine-checkable |
| SYMBOLIC-EXACT | proved symbolically over a ring |
| NUMERICAL | high-precision numerics |
| STRUCTURAL | structurally forced, not fully symbolic |
| KNOWN | established in the literature (reproduced here) |
| GATED | appears new but awaits a specialist read |
| POSTULATED | proposed, not put through the verification gate |

**The one GATED headline** is the SL(4) figure-eight A-polynomial `L = -M^4` and the
family `L = (-1)^{n-1} M^n` it suggests (section 5). An adversarial literature read found
no prior art, but an AI-assisted read *de-risks* a novelty question without *closing* it,
and the family is established only at n=3,4. It is flagged GATED in the abstract, in the
introduction, and at the theorem. No external novelty claim is asserted as settled.

**The physics** (section 7) is a FORCED symmetry bridge (the metallic SL(2,Z) trace-map
action *is* the N=2* class-S S-duality action on the character variety, literature-
confirmed) plus a CONFIRMED dimensional wall (no κ/volume invariant carries a physical
scale). The structural sharpening of the wall stays POSTULATED. Nothing here crosses to
physical magnitude, and the firewall (philosophy/interpretation may cite mathematics, never
the reverse) is held throughout.

## Build

Requires a LaTeX toolchain (`latexmk`/`pdflatex`) and the project's Python environment
(matplotlib, numpy, sympy, scipy, snappy).

```
make figures   # regenerate the 12 plots into figures/out/
make pdf        # compile main.tex -> main.pdf
make all        # both
```

## Layout

- `main.tex` — preamble (proof-status badges, theorem environments) and section includes.
- `sections/` — one file per section (01 intro/philosophy … 09 open/methods, appendix).
- `figures/gen_figures.py` — deterministic figure harness; one function per figure;
  reuses committed probe data (`frontier/B80…`, `frontier/B149…`) where it exists.
- `figures/out/` — generated PDFs/PNGs (committed so the paper builds without re-running).
- `refs.bib` — bibliography (arXiv ids where applicable).

No AI-model attribution appears anywhere in this artifact; the work was AI-assisted under
the verification discipline described in section 9. Nothing here is promoted to
`CLAIMS.md`.
