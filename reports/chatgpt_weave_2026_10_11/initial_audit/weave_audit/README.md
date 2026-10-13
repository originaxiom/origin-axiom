# Reproducible audit package

This package accompanies an independent review of the uploaded *A Weave of Two Records* (October 2026).

## Files

- `mathematical_notes.md`: analytic golden-axis proof, exact omega counterexample, qualifications and references.
- `verify_weave.py`: standalone, independently written verification code; no project-repository imports.
- `results.json`: actual outputs of the included script.
- `run.log`: captured console output.
- `requirements.txt`: versions used for the run.

## Reproduce

Python 3.11 or newer is recommended. The included output was produced with Python 3.13.5.

```sh
python -m venv .venv
# Activate .venv using your platform's standard command.
python -m pip install -r requirements.txt
python verify_weave.py --dps 100 --points 120 --output results.json
```

## Main changes in claim status

1. Golden spectrum on the entire Fibonacci axis: analytic proof supplied, using Ramanujan's classical degree-five modular equation.
2. Coupling-dimension table: independently reproduced by exact polynomial linear algebra.
3. Universal degeneracy at omega: false for the allowed full weight-three coupling space; explicit 3:2:1 counterexample.
4. Exclusion of -I while using the full reversible group: inconsistent on homology as written; physical updates and symmetry/lift groups need separate definitions.
5. Unique common quaternion point: correct only after restoring the relevant relative-character-variety hypothesis.
6. Universal geometric reduction modulo 3: manuscript overstates its cited source, which explicitly leaves the general theorem open.
7. Standard Model derivation and empirical masses: not established. Physical dictionary, kinetic assumptions, modulus selection and fits remain separate tasks.

This package does not certify every claim in the original work or every computation in its repository. Numerical tests are not interval certificates. No claim of novelty is made for the classical modular identity underlying the golden-axis proof.
