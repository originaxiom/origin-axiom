# Weave quantum realization — Run 7

Read `TECHNICAL_REPORT.md` first. This is a new, conditional SU(2)_2
Chern–Simons/WZW center-puncture model, NOT the old level-one theory renamed.

Main result: a one-dimensional nonzero quantum puncture block has the same
metaplectic coefficient character as the geometric line in Run 6. Its explicit
Ramond inserted trace is eta^3, calculated including the oscillators.

Main limits: its puncture Hilbert space is one-dimensional, its ordinary torus
three-space is not the source triplet, and the old current theory has a different
quantized level. No Standard Model, 4d gravity, or physical scale was obtained.

Dependencies: Python >=3.10, sympy, mpmath.

Run in order:
```
python verify_exact.py
python verify_physical_controls.py
python verify_numerical.py --dps 60
python verify_numerical.py --dps 90
```

`results/` contains raw successful logs and JSON data. The scripts do not call
external services, read Standard Model measurements, or import earlier project
verification code. The full fusion-tree pentagon and hexagon tests use standard
SU(2)_2 F/R data cited in the report; those data are an input, not a discovery.
