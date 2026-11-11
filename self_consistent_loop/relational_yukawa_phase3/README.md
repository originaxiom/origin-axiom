# Phase 3: Relational Quotient, Spin-Flux Throat, 3D Hyperbolic Yukawa Overlaps & Topological Tadpole Engine

Clean-room Phase 3 verification suite enforcing `0 of 19` empirical inputs and all 6 `user_global` Mathematical-Physics Guardrails.

## Run Pipeline
```bash
PYTHONPATH=src python3 -m relational_loop.phase3_engine
python3 scripts/referee_relational_phase3.py
PYTHONPATH=src python3 -m unittest discover -s tests -v
```
