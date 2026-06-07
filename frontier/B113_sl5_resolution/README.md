# B113 — the proved closed form resolves the SL(5) sign sectors + localizes degree=rank

Applies the **B112-proved** opposition-involution closed form to `n=5`, vs the repo's SL(5) tower (B61 22/24 +
B62 structural). NO physics; no `CLAIMS.md`; the `ρ_n` proof stays the prize; P1–P16 untouched.

- **`probe.py`**
  - **`closed_form_vs_sl5()`** — per-height: heights **2,3,4 match the SL(5) tower exactly**; height 1 differs (the
    degree=rank promotion).
  - **`b62_modes_resolved()`** — the closed form predicts **`char(M²)²·char(−M²)`** at height 2 = **B62's two
    gauge-corrupted modes** (the eps-series could only resolve 22/24; B112 supplies them by proof, all heights).
  - **`degree_rank_localization()`** — degree=rank is confined to **height 1 + the top power `char(Mⁿ)`**; heights
    `2..n−1` are pure bulk-θ. The promotion is **n-dependent** (consumes `−M¹` at n=5, `+M¹` at n=3,4) → the power
    half stays open (`speculations/S022`).
- **`FINDINGS.md`** — the table, the win, the honest caveat.

**Result.** The proof (B112) determines the SL(5) sign sectors at heights 2–4 — resolving the gauge-corrupted
eps-series modes B62 only patched at height 2 — and **localizes degree=rank to the height-1/top-power interface**.
The promotion rule (power half) is n-dependent and remains the open piece.

```bash
python frontier/B113_sl5_resolution/probe.py
python -m pytest tests/test_b113_sl5_resolution.py -q
```
No physics claim; the `ρ_n` catalog proof stays the central target; proven core P1–P16 untouched.
