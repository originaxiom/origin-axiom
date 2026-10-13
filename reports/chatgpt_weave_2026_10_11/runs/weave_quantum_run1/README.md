# Weave quantum-realization run 1

Read `TECHNICAL_REPORT.md` for the derivations, hypotheses, findings and next test.

## Reproduce

Tested with Python 3.13.5, SymPy 1.14.0 and mpmath 1.3.0.

```bash
python -m pip install -r requirements.txt
python verify.py
python verify_cover.py
python verify_parity_conjugacy.py
python verify.py --dps 100 --output results_100dps.json
```

The scripts use no network, no experimental datasets and no project code. They write only their local JSON results. All final symbolic tests use exact arithmetic; numerical theta/eta checks are separately labelled.

## Principal outcomes

- Exact known-CFT block realization of the entire eta-theta expression, with explicit added Ising sectors.
- Exact obstruction to treating the three independent normalized functions as three complete simple sectors.
- Exact parity-twist conjugacy, obstructing the simplest vacuum-determinant reading under covariant-domain hypotheses.
- Exact eight-sheeted Q8 cover, compact genus three, preserved by both grammar generators.
- The faithful Q8-twisted puncture-state quantum blocks have NOT yet been calculated.

The main 34 test groups include intended negative controls. A check passing can mean that it correctly detected a forbidden candidate; it does not mean every proposed physical model passed.

`PLAN.md` and its hash document a local pre-execution plan, not an externally committed blind seal. The cover and parity additions were formulated after the initial run. `attempts/` preserves the initial instrumentation output; the final authoritative output is `results.json`. See `CHANGELOG.md`.

No claim of a complete TOE, physical gauge group, gravity, chiral generations or parameter prediction is made. No user's repository or source PDF was modified.
