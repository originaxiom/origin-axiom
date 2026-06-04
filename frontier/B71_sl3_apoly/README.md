# B71 — SL(3) figure-eight character variety from the trace map (Track B)

The SL(3) analogue of B67. The figure-eight monodromy `[[2,1],[1,1]]=M²` acts on the 8 SL(3) fiber
trace coordinates (B48) as `T_1²`; a fiber rep extends over the bundle iff its character is
`T_1²`-fixed, so `Fix(T_1²)` is the SL(3) character variety of the figure-eight bundle.

**B0–B1 result (this directory, exact):** `Fix(T_1²)` decomposes into **exactly three dimension-2
components** — `V0={x1=x4,x2=x5}` (geometric, contains `Sym²` of the figure-eight SL(2) holonomy),
`W1={x1=x4=1}`, `W2={x2=x5=1}` (Dehn-filling-type). This reproduces the **component structure** of
the published Heusener–Muñoz–Porti (arXiv:1505.04451) and Falbel et al. (arXiv:1412.4711) SL(3)
figure-eight character varieties. The `Sym²` ground truth lands on `V0` to `~1e-14` (offline, exact).

**B2–B3 result (`peripheral.py`):** explicit SL(3) reps on each component (`realize`, round-trips
`<1e-7`) + the 18×9 Kronecker monodromy solve give the peripheral eigenvalue A-variety. The
Dehn-filling components **literally reproduce Falbel et al.'s published A-variety** (arXiv:1412.4711),
meridian↔longitude transposed: **W1=D2 → `M³=L`**, **W2=D3 → `M³L=1`** (`~1e-10`). The construction is
validated on the geometric branch by the Sym² shadow (`eig(t)={μ²,1,μ⁻²}`, `~1e-13`). The genuine
peripheral **meridian `μ=w⁻¹t` commutes with the longitude `[A,B]`** (the abelian cusp pair, `~1e-10`;
`w` from `φ([a,b])=w[a,b]w⁻¹`, verified by free-group reduction; `eig(μ)=eig(t)` so the relations are
unchanged). This is the SL(3) analogue of B67's exact Cooper–Long match, on the Dehn-filling
components. The geometric component (Falbel D1) has no tidy closed form (141-poly ideal) — no literal
match there.

Honest scope: B0–B1 is a structural character-variety match (3 components, dim 2, geometric=Sym²),
**not** a literal fiber↔knot coordinate-ideal identity; B2–B3 is a literal eigenvalue-A-variety match
on the Dehn-filling components (numerical, `~1e-10`).

- `probe.py` — the trace map `T_1²`, `Fix(T_1²)` equations, the exact component decomposition, the
  `Sym²` ground truth. `peripheral.py` — `realize`, `monodromy`, the Dehn-filling A-variety match.
- Tests: `tests/test_b71_sl3_apoly.py` (9 passing). Ledger rows **V43** (B0–B1), **V44** (B2–B3),
  **V46** (the genuine commuting meridian `μ=w⁻¹t`).

Standalone character-variety mathematics; no physics, no Origin claim. Proven core P1–P16 untouched.
