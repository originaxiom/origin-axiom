# Weave quantum realization — Run 9

Read `TECHNICAL_REPORT.md` for the mathematical arguments, physical assumptions and exclusions. The package continues the supplied Run 8 model without adding fields or flavour backgrounds.

Requirements: Python 3.10+, SymPy, mpmath.

```bash
python verify_exact.py
python verify_clifford.py
python verify_numerical.py --dps 55
python verify_numerical.py --dps 85
```

The scripts fail on any assertion mismatch and write JSON results in `results/`. The exact Clifford calculation can take longer than the other exact checks. All dimensions and phases are calculated; none is fitted to empirical particle data. Numerical truncations are not interval certified.

Main conclusions: the physical neutral flavour factor is not rotated by the original colour/geometry moves; the pair-only three-handle-channel space has the wrong projective T spectrum; a central-puncture paired amplitude is nonzero but has one channel. This is a negative identification test for this candidate, not a no-go theorem for all quantum completions.

`history/` retains an initial finite-cutoff contact-term assertion failure. `CHANGELOG.md` explains it. `PLAN.sha256` is a local integrity hash, not an independent preregistration timestamp.
