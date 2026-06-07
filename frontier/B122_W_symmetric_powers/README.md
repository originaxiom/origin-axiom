# B122 — the tower is symmetric powers of `W = V⊕1` (unifies B121)

`ρ_n = Sym^n(W) ⊕ (Sym^{n−3}(W) ⊖ W)`, `W = V⊕1` — a genuine GL(2)-module repackaging of the two-sequence, with
`W` canonically **B121's external monodromy fundamental**. Honest strength: a repackaging + a canonical
identification, **not** a proof route. No physics (the 3+1/spin-2 readings are firewalled in
`../../speculations/S028`); no `CLAIMS.md`; the `ρ_n`/Sym-`μ_d` proof stays the prize; P1–P16 untouched.

- **`probe.py`**
  - **`w_identity_character()`** — `ρ_n = Sym^n(W)+Sym^{n−3}(W)−1−V == μ_d`, n≤11; cleaner form `⊖W`.
  - **`w_identity_is_gl2_module_iso()`** — holds **symbolically in general `(x,y)`, det-independent**, n≤8 ⇒ a
    **genuine GL(2)-module iso** (not vacuous — the tower is a GL(2,ℤ)-rep, B103).
  - **`W_is_external_fundamental()`** — `det(W)=−1` (external, B121) vs `det(Fricke=Sym²V)=+1` (internal); the
    Fricke kill = external≠internal; the odd weights = `Sym^n(V⊕1)∋V`. **Unifies B121 + the W-identity.**
  - **`a7a_corollaries()`** — `Sym⁴(3)=15=sl(4)` unique saturation (n=4 fixed point); offset = dim W = 3.
  - **`not_a_wall_bypass()`** — module-iso-equivalent to the two-sequence; no functorial map; the re-aimed prize.
- **`FINDINGS.md`** — the identity, the GL(2)-module-iso upgrade, the B121 unification, and the honest verdict.

**Result.** The monodromy grading **is** `Sym(`external fundamental `W=V⊕1)` — a clean GL(2)-module repackaging that
identifies `W` canonically and unifies B121 with Chat-2's W-identity (one object, not two). But it is module-iso-
equivalent to the two-sequence and supplies no functorial `Sym(W)→trace-ring` map, so it re-aims the prize without
lowering the wall.

```bash
python frontier/B122_W_symmetric_powers/probe.py
python -m pytest tests/test_b122_w_symmetric_powers.py -q
```
No physics claim; the `ρ_n` catalog proof stays the central target; proven core P1–P16 untouched.
