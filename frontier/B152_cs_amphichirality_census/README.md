# B152 — CS-as-parity-order-parameter, census test

**Question.** Across SnapPy's `OrientableCuspedCensus[:240]`, does amphichirality force the
Chern–Simons invariant to a 2-torsion value (`CS mod ½ ∈ {0,¼}`), and how does the converse fail?

**Answer (NUMERICAL / census, V141).** Yes — necessary, not sufficient. 7 amphichiral manifolds, 0
necessity violations, exactly one converse counterexample `m208` (chiral but `CS=0`). Extends B128 (CS
as a parity order parameter) and B136 (general amphichirality) with data. No physics; nothing to
`CLAIMS.md`.

**Method guard.** Amphichirality via `symmetry_group().is_amphicheiral()` gated on `is_full_group()`
(the documented orientation-blindness bug of `is_isometric_to`); CS 2-torsion via circular proximity to
`{0,¼}` mod ½ (negative near-zero CS wraps under `%`).

**Provenance.** Proposed in a cross-session review brief (Session B's F4); reproduced independently
in-session before banking, which also caught and fixed a modulo-sign bug in the converse detector.

```bash
python frontier/B152_cs_amphichirality_census/probe.py
python -m pytest tests/test_b152_cs_amphichirality_census.py -q
```

Files: `probe.py` (the scan), `census.json` (output), `FINDINGS.md`.
