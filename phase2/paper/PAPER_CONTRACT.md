# Phase 2 Paper Contract (P2-S1)

## Purpose
Phase 2 is a *claims-first* paper whose only goal is to establish three auditable claims (C2.1–C2.3) with strict provenance. No new “Phase 3+” claims may enter Phase 2.

## Canonical spine (must match `paper/main.tex`)
1. 00_abstract
2. 01_introduction
3. 02_model_definition
4. 03_claim_C2_1_existence
5. 04_claim_C2_2_robustness
6. 05_claim_C2_3_frw_viability
7. 06_reproducibility_and_provenance
8. 07_limitations_and_scope
9. 08_conclusion
Appendix:
- appendix/A_run_manifest
- sections/A_provenance

## Naming + section invariants
- Section filenames are canonical and unique. No “ * 2.tex” duplicates. No alternate spines.
- Every section has an explicit `\label{...}` if referenced.
- `\appendix` occurs exactly once.
- `A_run_manifest` must provide `\label{app:run_manifest}`.

## Claims discipline
- Claim C2.1 / C2.2 / C2.3 must each contain:
  - One paragraph “Claim (C2.x).”
  - A bounded list of evidence artifacts (figures + run_ids)
  - A “Non-claims / limits” note (what is *not* asserted)

## Provenance rule
Every figure in `paper/figures/` must have:
- a run_id pointer in `outputs/figures/<fig>.run_id.txt`
- `outputs/runs/<run_id>/meta.json` including git commit hash + resolved params + environment snapshot
Appendix A_run_manifest is the human-readable map.

## Build rule
`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` must compile clean:
- no undefined references
- no undefined citations
- no empty journal warnings (bib hygiene)

