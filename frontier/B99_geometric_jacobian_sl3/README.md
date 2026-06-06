# B99 — the SL(3) trace-map Jacobian at the GEOMETRIC representation (Probe 1c)

Strengthens B98 (Probe 1) to SL(3): does the geometric rep again give a torsion-type spectrum, not the
Dickson tower?

- **`probe.py`** — the SL(3) figure-eight trace-map Jacobian at the geometric `Sym²` point: 2 eigenvalue-1's
  (tangent to V0) + 3 transverse reciprocal pairs with sums `c∈{5, 4.5±4.664 i}`. The `c=5` pair is the
  SL(2) torsion pair (B98) carried by `Sym²`.
- **`FINDINGS.md`** — the result + the honest scope.

**Result (`computer-assisted`).** **Not the tower** (whose pair-sums are the real `{−1,3,4}`): the
geometric rep carries a **torsion-type (twisted-Alexander) spectrum** at SL(3) too — *consistent with*
Daly (arXiv:2411.04431) and the 3d-3d framework (cited, not claimed). With B98: the Dickson tower is a
trivial-rep phenomenon; the geometric rep is the torsion side. Different fixed points, different objects.

```bash
python frontier/B99_geometric_jacobian_sl3/probe.py
python -m pytest tests/test_b99_geometric_jacobian_sl3.py -q
```
No Origin-core claim; proven core P1–P16 untouched.
