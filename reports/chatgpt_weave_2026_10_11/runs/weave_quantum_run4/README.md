# Weave quantum realization — Run 4

Start with TECHNICAL_REPORT.md. The report distinguishes new checks from inherited Run 3 formulas, and physical claims from mathematical controls.

Requires Python 3.10+ with sympy, numpy, and mpmath. A known-working environment is listed in ENVIRONMENT.txt.

Run these commands in this directory:

```
python verify_exact.py
python verify_cocycles.py
python verify_ward_and_bundles.py --dps 60
python verify_ward_and_bundles.py --dps 90
```

Each script writes its own JSON result file. The supplied logs are from these runs. The cochain calculation uses exact finite-field arithmetic. Numerical theta/source calculations are not interval-certified.

The initial .py.txt files are deliberately non-executable snapshots retained for integrity, not alternative recommended scripts.
