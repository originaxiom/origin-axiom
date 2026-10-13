# Weave Quantum Realization — Run 10

Read `TECHNICAL_REPORT.md` first. This packet tests a new nonlinear sigma model, not the previous SO(5) coset unchanged.

## Reproduce

Python 3.10 or later, with NumPy, SymPy, and mpmath:

```sh
python -m pip install numpy sympy mpmath
python verify_exact.py
python verify_numerical.py --dps 50
python verify_numerical.py --dps 80
python verify_global.py
```

Scripts write JSON results to `results/`. Existing run logs and JSON output are included. `PLAN.md` and its SHA-256 hash record a local pre-script plan, not a blind preregistration. `history/explore.py` is the retained initial direct-series check.

The analytic proof, not numerical tolerances, establishes the half-charge, minimum action, and classical Hessian positivity. The full quantum determinant, physical fermion spectrum, and a four-dimensional uplift have NOT been calculated.
