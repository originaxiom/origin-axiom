# Phase 3 Reproducibility

## Levels
### Level A (Verification from repo snapshot)
- Build Phase 3 paper from `phase3/paper/`
- Verify artifacts using `phase3/outputs/paper_bundle/` manifests + hashes
- Run: `bash scripts/phase3_gate.sh --level A`

### Level B (Regenerate Phase 3 artifacts)
- Create a venv, install dependencies
- Run Snakemake to reproduce tables/figures and refresh paper_bundle
- Run: `bash scripts/phase3_gate.sh --level B`

### Level C (Full heavy runs)
- Optional developer mode; creates `phase3/outputs/runs/` (gitignored)
- Run: `bash scripts/phase3_gate.sh --level C`

## Environment
Recommended:
- Python 3.11+ (document exact in run meta)
- `pip install -r phase3/requirements.txt` (generated in Phase 3 by gate)

## One-command rebuild (Level B)
- `snakemake -s phase3/workflow/Snakefile -c 1 all`

All final artifacts intended for review are stored in:
- `phase3/outputs/paper_bundle/`
