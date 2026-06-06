# B102 — the W1/W2 dichotomy + the R4 (boundary-controlled cubic) continuation

Two follow-ons to B101 (a CC-web handoff, **verified before landing**). Higher-Teichmüller /
character-variety geometry; **no physics**.

- **`probe.py`**
  - **D1 — the dichotomy** (`STRUCTURAL`+`computer-assisted`): Cayley–Hamilton on `T₁²` forces every
    irreducible `Fix(T₁²)` SL(3) character into Case I (`trA=trA⁻¹`, self-dual) or the `trB=trB⁻¹=1` branch
    — **0 "neither"** (census + exact on B71's V0/W1/W2).
  - **D2/D3 — the ellipticity obstruction** (`computer-assisted`): realizing B71's components, **W1 → `ρ(a)`
    elliptic `{1,i,−i}`**, **W2 → `ρ(b)` elliptic `{1,i,−i}`** (order-4, not loxodromic ⇒ **not Hitchin**);
    the **geometric V0** point is self-dual with `tr(AB)` a root of `t²−t+7` (`Q(√−3)`). **V0 excluded by
    complexity, W1/W2 by ellipticity** — the cleaner obstruction.
  - **D4 — the Task-M link**: the `{1,i,−i}` spectrum **is** Task M's forced `n=3` spectrum (B95).
  - **D5 — the boundary-controlled cubic family**: the conditions `tr δC=0, tr C δC=0` cut the cubic
    directions to a **9-dim relative family** keeping the cusp real **to first order** — but **NOT** at
    finite `t` (generic second-order cube-root complexification). **The handoff's `(λ,1,1/λ)` geodesic
    boundary / `t*≈3.775` does not reproduce** (ray-dependent); the unipotent-preserving continuation is
    **`open`**.
- **`FINDINGS.md`** — the results, the honest corrections to the handoff, and citations.

**Result.** The genuine non-`Sym²` figure-eight components W1/W2 are excluded from the real Hitchin
component by an **order-4 elliptic generator** (`{1,i,−i}` = Task M's `n=3` spectrum); the distinguished V0
by complexity (`Q(√−3)`). The boundary-controlled cubic continuation works to first order only. Cite
Heusener–Muñoz–Porti, Labourie, Hitchin/Fock–Goncharov/Goldman/Marquis.

```bash
python frontier/B102_hitchin_continuation/probe.py
python -m pytest tests/test_b102_hitchin_continuation.py -q
```
No physics claim; no Origin-core claim; proven core P1–P16 untouched; physics chapter stays CLOSED.
