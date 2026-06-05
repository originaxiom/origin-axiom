# B76 — cusp-torsion × quantum group at roots of unity (Path F2/F3 closure)

Does the metallic-bundle **cusp `k`-set** `{3..m+2}` (cusps at `x=2cos(π/k)`, B69) connect to a
**quantum group at a root of unity** / anyonic TQFT?

- **`probe.py`** — verifies `2cos(π/k)=[2]_q` at `q=e^{iπ/k}` (cusp value = SU(2)\_{k−2} value),
  tabulates the cusp k-set → WZW level (`k−2`) → torsion-order (`2k`) map for `m=1..6`, and records the
  V28 categorification barrier.
- **`FINDINGS.md`** — the split verdict + F3's disposition.

**Result.** **Literal** at the level of the special numbers/torsion: the cusp `k`-set **is** the SU(2)
quantum-group root-of-unity level set (both are the cyclotomic `2cos(π/k)`, order-`2k` torsion) —
closing B69's open reconciliation item (STRUCTURAL). But **no categorical lift**: the metallic fusion
rule categorifies only at `m=1` (V28, Ostrik), so the "anyonic TQFT" reading of the *family* is
**SPECULATIVE-ANALOGY** — shared structure is just "roots of unity." **F3** (parity × CS) is **subsumed
by V56** — the B64 parity split is the W_N charge-conjugation grading.

```bash
python frontier/B76_cusp_quantum_group/probe.py
python -m pytest tests/test_b76_cusp_quantum_group.py -q
```

No Origin-core claim; proven core P1–P16 untouched.
