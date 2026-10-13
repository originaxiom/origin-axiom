# Weave Quantum Realization — Run 11

Read `TECHNICAL_REPORT.md` for the physics and its limits; read `REPOSITORY_MAP.md` before extending the research. This packet does not modify or replace the Origin Axiom repository.

Python 3.10+, `sympy` and `mpmath` are required. From this directory:

```sh
python verify_exact.py
python verify_numerical.py --dps 50
python verify_numerical.py --dps 80
```

Results are written to `results/`. There are 40 named exact checks and 61 numerical comparisons per precision. The latter separate 59 strict identities from two finite limits. These checks are not a complete quantum theory, a global nonlinear PDE solver, or an independent certification of the repository's authored analysis.

Key distinction: an exact equality of theta projective coordinates is obtained; equality of the round CP1 action and the reduced Yang–Mills theory is not. The periodic adjoint kernel contains six modes with index minus two.
