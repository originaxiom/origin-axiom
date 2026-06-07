# B113 — the proved closed form resolves the SL(5) sign sectors + localizes degree=rank

**Status: `computer-assisted`.** Applies the **B112-proved** opposition-involution closed form to `n=5` and
compares it to the repo's SL(5) tower (B61: 22/24 resolved by the eps-series; B62: the 2 unresolved completed
structurally). Two findings: a **win** (the proof resolves what the numerics could not) and a **localization** (it
confines degree=rank to one place). NO physics; no `CLAIMS.md`; the `ρ_n` proof stays the prize; P1–P16 untouched.
Script `probe.py`; test `tests/test_b113_sl5_resolution.py`.

## Finding 1 (WIN) — the closed form resolves the SL(5) sign sectors above height 1
Per-height comparison of the proved closed form (B112) against the SL(5) tower:

| height `h` | closed form `(char(M^h), char(−M^h))` | SL(5) tower | match |
|---|---|---|---|
| 1 | `(2, 2)` | `(2, 1)` | **differs** (the promotion) |
| 2 | `(2, 1)` | `(2, 1)` | ✅ — `char(M²)²·char(−M²)` |
| 3 | `(1, 1)` | `(1, 1)` | ✅ |
| 4 | `(1, 0)` | `(1, 0)` | ✅ |

At heights 2, 3, 4 the proved closed form **matches the SL(5) tower exactly** — including the height-2 sector
**`char(M²)² · char(−M²)`**, which is precisely **B62's two gauge-corrupted modes** (the 23rd/24th multipliers the
eps-series `pinv` could not resolve, and which B62 had to supply structurally *at height 2 only*). B112 now
supplies **all heights** by proof, so the **SL(5) sign sectors are determined by a theorem, not by the
gauge-fragile numerics**. This is the concrete payoff of B112: the structural resolution B62 pioneered for
height-2 now covers the whole tower.

## Finding 2 (LOCALIZATION) — degree=rank touches only height 1 + the top power
The *only* place the closed form differs from the SL(5) tower is **height 1** (`closed (2,2)` vs `tower (2,1)`)
plus the extra **`char(M⁵)`** (the longitude `L = c·Mⁿ`). So:

- **Heights `2 … n−1` are pure bulk-`θ`** (the proved closed form) — degree=rank does **not** touch them.
- **degree=rank is confined to the height-1 / top-power interface** (`char(±M¹)` ↔ `char(Mⁿ)`).

This localizes the open *power half* of the prize to one interface. **Honest caveat:** the degree=rank promotion
is **not** a uniform `char(M)→char(Mⁿ)` rule — at `n=5` it consumes a `char(−M¹)`, whereas at `n=3,4` it consumed
a `char(+M¹)`. So the promotion's exact form is **n-dependent**, and the power half stays the genuinely-hard open
piece (`speculations/S022`).

## Verdict
The proved closed form (B112) **determines the SL(5) sign sectors at heights 2–4 by proof** (resolving the
gauge-corrupted eps-series modes B62 only patched at height 2), and **localizes degree=rank to height-1 + the top
power `char(Mⁿ)`**. The promotion rule is n-dependent and remains open — the power half of the `ρ_n` prize.

```bash
python frontier/B113_sl5_resolution/probe.py
python -m pytest tests/test_b113_sl5_resolution.py -q
```
No physics claim; the `ρ_n` catalog proof stays the central target; proven core P1–P16 untouched.
