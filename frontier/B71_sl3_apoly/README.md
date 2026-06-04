# B71 — SL(3) figure-eight character variety from the trace map (Track B)

The SL(3) analogue of B67. The figure-eight monodromy `[[2,1],[1,1]]=M²` acts on the 8 SL(3) fiber
trace coordinates (B48) as `T_1²`; a fiber rep extends over the bundle iff its character is
`T_1²`-fixed, so `Fix(T_1²)` is the SL(3) character variety of the figure-eight bundle.

**B0–B1 result (this directory, exact):** `Fix(T_1²)` decomposes into **exactly three dimension-2
components** — `V0={x1=x4,x2=x5}` (geometric, contains `Sym²` of the figure-eight SL(2) holonomy),
`W1={x1=x4=1}`, `W2={x2=x5=1}` (Dehn-filling-type). This reproduces the **component structure** of
the published Heusener–Muñoz–Porti (arXiv:1505.04451) and Falbel et al. (arXiv:1412.4711) SL(3)
figure-eight character varieties. The `Sym²` ground truth lands on `V0` to `~1e-14` (offline, exact).

Honest scope: structural match (3 components, dim 2, geometric=Sym²), **not** a literal fiber↔knot
coordinate-ideal identity. The peripheral eigenvalue A-variety (monodromy `t`, longitude `[A,B]`;
literal Dehn-filling forms `L³=M`/`L³M=1`) is the B2–B3 continuation.

- `probe.py` — the trace map `T_1²`, `Fix(T_1²)` equations, the exact component decomposition, and
  the `Sym²` ground truth. `python probe.py` prints the verified summary.
- Tests: `tests/test_b71_sl3_apoly.py`. Ledger row **V43**.

Standalone character-variety mathematics; no physics, no Origin claim. Proven core P1–P16 untouched.
