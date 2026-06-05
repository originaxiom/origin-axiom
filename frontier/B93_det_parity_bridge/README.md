# B93 — det=−1 is exactly the tower's parity (Paper 0, Phase C)

The bridge from the foundation (B92) to the tower: why `det=−1` is structurally distinguished.

- **`probe.py`** — **MyCalc-1** (`det=−1 ⟺` a negative eigenvalue `−1/λ` `⟺` the `char(−Nᵏ)` parity
  sectors; `det=+1` ⟹ both positive ⟹ no sign sectors) and **MyCalc-4** (the parity `m→−m` and the field
  Galois `√→−√` are *distinct* ℤ/2 involutions — the CPT/parity is the contragredient, not Galois).
- **`FINDINGS.md`** — the two results + honest scope.

**Result (`proven`/`computer-assisted`).** `det=−1` is exactly what gives the tower its sign/parity
sectors (engine of the B94 universality result); and the parity involution is the contragredient `m→−m`,
distinct from the Galois action (which is the within-factor root swap).

```bash
python frontier/B93_det_parity_bridge/probe.py
python -m pytest tests/test_b93_det_parity_bridge.py -q
```
No Origin-core claim; proven core P1–P16 untouched.
