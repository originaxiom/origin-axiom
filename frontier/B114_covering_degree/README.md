# B114 — the covering-degree mechanism: TESTED-NEGATIVE

Is degree=rank's exponent `k` the **covering degree** of `M ↦ L = c·Mᵏ` (S022's candidate mechanism)? B111 found
`k`-to-1 at the single-eigenvalue level; this tests the full spectrum. NO physics; no `CLAIMS.md`; P1–P16 untouched.

- **`probe.py` (`full_covering_degree` / `covering_degree_negative`)** — the full covering degree (meridian
  spectra, `det=1`, mod permutation, → same `L`) is **`~k^{n−1}`** (SL3 W1 = 9 = 3²; SL4 secondary = 27 = 3³; SL4
  principal = 40), **not `k`** on any of the four.

**Result.** The **covering-degree-=-`k` mechanism is not supported** (the `=k` reading holds only at the
single-eigenvalue level, B111). The exponent is **not** a covering degree; the live lead stays the **`Mᵏ`-scalar
arithmetic** (B111 ADDITION 1 — the `M⁴=−1` impossibility forces `k=3` on the secondary). `S022`'s covering
candidate is downgraded; the power half of `ρ_n` stays open.

```bash
python frontier/B114_covering_degree/probe.py
python -m pytest tests/test_b114_covering_degree.py -q
```
No physics claim; the `ρ_n` catalog proof stays the central target; proven core P1–P16 untouched.
