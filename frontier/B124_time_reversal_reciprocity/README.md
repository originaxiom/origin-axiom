# B124 — reciprocal pairs + the time-reversal involution

`probe.py` verifies, in two **strictly separated** tiers:

- **§1 (generic symplectic):** at the SL(2) **void** fixed point the trace-map Jacobian has spectrum `{φ²,−1,φ⁻²}` —
  a reciprocal `(λ,1/λ)` pair + the self-reciprocal `−1`, `det=−1`; `(DT)⁻¹` carries the same spectrum with
  stable/unstable **roles swapped**. This is generic to area-preserving maps; the only metallic-specific datum is the
  **rate** `log φ²`.
- **§2 (metallic-specific):** the tower `ρ_n=⊕Sym^d(M)^{μ_d}` carries `det=−1`-specific **negative** modes
  (`char(−M^h)` sectors; `det=+1` has none) — a sign/**chirality** (P) imbalance, `O(n/2)`. But **expanding ==
  contracting exactly, every n, both det** → **no arrow** (T preserved). The exact constant is **open** (the raw `±1`
  excess is period-4, not `⌊n/2⌋`).

Run:

```
python frontier/B124_time_reversal_reciprocity/probe.py
python -m pytest tests/test_b124_time_reversal_reciprocity.py -q
```

**Reading is firewalled, not here.** The "two-headed time" interpretation lives in `philosophy/P006` (labeled
overlay) and the dynamics fork `speculations/S002`; this folder is the math only. No physics; nothing to
`CLAIMS.md`; the functorial `Sym(W)→trace-ring` wall is untouched. See `FINDINGS.md`; ledger **V113**.
