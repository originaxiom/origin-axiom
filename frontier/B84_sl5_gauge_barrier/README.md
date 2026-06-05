# B84 — the SL(5) tower barrier is non-convergence, not gauge (Phase B; I1 refuted)

Tests whether the SL(5) tower barrier (B81) is a fixable gauge/basis artifact (the I1 conjecture: a
gauge-fix / θ-split / seed-averaging recovers it).

- **`probe.py`** — (1) seed-averaging `char(DT_0(5))` over 40 seeds (no consensus); (2) the decisive
  test: the gauge-**invariant** power sums `tr(DT_0^k)` across seeds.
- **`FINDINGS.md`** — the refutation + the sharp characterization.

**Result: I1 REFUTED.** At SL(5) even the gauge-**invariant** power sums scatter across seeds (`tr(DT_0)`
itself differs every seed) — so the **eigenvalue spectrum itself is seed-dependent**: the ε→0 pinv-limit
produces genuinely *different operators* per seed (a **non-convergence**, not a basis ambiguity). No
numerical gauge-fix / θ-split / averaging can recover the tower. 22/24 eigenvalues are canonical; the 2
of the *second* `char(M²)` are genuinely undetermined by the limit. The SL(5)+ tower **from first
principles** needs the symbolic trace map `σ` (Phase C/D), where `Dσ` is canonical by construction — or
B62's structural answer. SL(4) is seed-canonical (why B80 works).

```bash
python frontier/B84_sl5_gauge_barrier/probe.py
python -m pytest tests/test_b84_sl5_gauge_barrier.py -q
```

No Origin-core claim; proven core P1–P16 untouched.
