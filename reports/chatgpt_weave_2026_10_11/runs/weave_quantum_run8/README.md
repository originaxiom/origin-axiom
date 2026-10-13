# Weave quantum realization — Run 8

This package tests a physical junction to the SU(2)_2 candidate from Run 7.

**Result:** In the minimal co-propagating fundamental matter class, level matching requires two doublets. The full colour coset is SO(5)_1. A central-line endpoint yields a neutral triplet plus a charged pair, not an isolated triplet. The full source metaplectic triplet and its physical interpretation are not derived.

Read `TECHNICAL_REPORT.md` for the assumptions, proofs, gauge/framing boundaries and primary sources.

## Reproduce

```bash
python -m pip install -r requirements.txt
python verify_exact.py
python verify_numerical.py --dps 50
python verify_numerical.py --dps 80
```

Final outputs are under `results/`. Exact script: 52 named checks. Numerical script: 84 comparisons per precision. These numbers are inventories, not confidence scores. The calculations are independent of the prior run verification modules.

`PLAN.md` is a locally recorded working plan, not a blind preregistration. `CHANGELOG.md` and `history/` retain the correction history. The report does not claim a new topological phase, a simulation of a microscopic material, a 4D particle spectrum, or a TOE.
