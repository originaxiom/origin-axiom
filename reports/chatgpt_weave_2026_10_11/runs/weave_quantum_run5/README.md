# Weave Quantum Realization — Run 5

Start with `TECHNICAL_REPORT.md`. It separates invariant Q8 symmetry/defect data from the stronger requirement of keeping the particular free holomorphic fermion and puncture realization.

## Reproduce

Python 3.10+ with sympy, mpmath, and numpy:

```sh
python -m pip install -r requirements.txt
python verify_exact.py
python verify_lattice.py --dps 50
python verify_lattice.py --dps 80
```

Results are written beside the scripts. The supplied logs/results are the completed runs. `verify_lattice.initial.py.txt` and `initial_failure_50.log` retain the failed factor-two control described in the report.

No claims of full nonabelian sewing, a singular Dirac spectrum, Quillen connection, or a four-dimensional theory are made. Mathematical proofs are in the report; finite scans and numerical precision are not substitutes for those proofs.
