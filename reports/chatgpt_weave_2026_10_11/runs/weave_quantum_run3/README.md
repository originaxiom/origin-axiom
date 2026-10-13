# Weave Quantum Realization — Run 3

Read `TECHNICAL_REPORT.md` first. The fixed faithful Gaussian puncture amplitude
exists explicitly, but its natural quadratic residue carries chi_eta5 rather
than the requested chi_eta3. This is a conditional mismatch, not a no-go for all
quantum completions and not a calculation of four-dimensional physics.

## Reproduce

Python 3.10 or later is recommended for the type syntax used by these scripts.
Install the versions recorded in `requirements.txt`, then run:

```sh
python verify_exact.py
python verify_amplitudes.py --dps 80
python verify_amplitudes.py --dps 100
```

The scripts write JSON results into this directory. Run from an extracted copy
if the originally supplied hashes/results should remain untouched. No network,
project repository, input PDF or other package from previous runs is required.
A failed assertion exits nonzero. The numerical script requires at least 40 digits.

## Contents

- `TECHNICAL_REPORT.md`: assumptions, analytic derivations, claims and limits.
- `verify_exact.py`: 28 named exact/finite verification groups.
- `verify_amplitudes.py`: 17 groups, 124 comparisons at each precision.
- `*_results*.json`, `*.log`: final successful outputs, including the deliberately
  rejected target-multiplier control.
- `PLAN.md`, `PLAN.sha256`: locally recorded plan; not blind preregistration.
- `CHANGELOG.md`: disclosed instrumentation corrections and scope notes.
- `exploratory/explore.py`: early float-input exploration; not precision evidence.
- `requirements.txt`: versions actually installed for this run.
- `SHA256SUMS`: package-file integrity hashes, not an external timestamp.

The two scripts and analytic proofs cross-check specific ingredients. They do
not amount to two independently constructed physical theories. No full Quillen
metric, singular-Dirac spectral zeta computation or all-genus sewing is claimed.
