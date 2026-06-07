# B119 — the Mᵏ-scalar (centrality) mechanism (Chat-2 Path 3, the hard path)

The brave attempt to **prove `k=n` on the principal** from the cusp eigenvalue arithmetic (B111 ADD1's surviving
lead). It returns a **sharp negative** with the obstruction stated precisely, plus an emergent correction to the
cusp-order reading. NO physics; no `CLAIMS.md`; the `ρ_n` proof stays the prize; P1–P16 untouched.

- **`probe.py`**
  - **`principal_cusp_order()`** — the forced principal cusp order `= order(a)`, `a+1/a=3−n` = **`{4,3,2,∞}`**
    (n=3,4,5,≥6).
  - **`mpower_central_principal()` / `brave_kn_verdict()`** — `Mᵏ` central iff `order(a)|k`; `k=n` is non-central
    where the principal exists (n=3,4) but **not the unique** non-central `k` ⇒ centrality does **not** force
    `k=n` (the A-poly B83 pins it). For `n≥5` the principal does not exist irreducibly (B95). **`exponent=rank` is
    an `n∈{3,4}` phenomenon**; the brave proof cannot be completed.
  - **`secondary_exponent_arithmetic()`** — the 2n-type: `Mⁿ=−I` central ⇒ exponent `n−1` (extends B111).
  - **`cusp_order_correction()`** — the emergent: no clean `{n−1,n+1,2n}` law; B111 ADD2 conflated W1(n+1),
    principal(n−1), secondary(2n).
- **`FINDINGS.md`** — the arithmetic + the sharp negative + the obstruction.

**Result (sharp negative, first-class).** The positive peripheral power-half mechanism does **not** close: `k=n` on
the principal is not forced by Mᵏ centrality (only multiples of `order(a)` excluded; the A-poly B83 pins it), and
for `n≥5` the principal Dehn-filling rep does not exist (B95). The bulk `char(Mⁿ)` is `Sym^n` presence (B117); the
all-`n` prize stays the Sym two-sequence `μ_d` (B103).

```bash
python frontier/B119_mk_scalar_mechanism/probe.py
python -m pytest tests/test_b119_mk_scalar_mechanism.py -q
```
No physics claim; the `ρ_n` catalog proof stays the central target; proven core P1–P16 untouched.
