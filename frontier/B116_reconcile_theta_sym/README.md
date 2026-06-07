# B116 — reconcile the θ-split (B112) with the Sym two-sequence (B103)

The reconciliation run to *join* the two halves of the `ρ_n` prize. It instead **corrected** B112's all-`n`
claim (verify-don't-trust). NO physics; no `CLAIMS.md`; the `ρ_n` proof stays the prize; P1–P16 untouched.

- **`probe.py`**
  - **`sym_equals_sl5_tower()`** — the Sym two-sequence (B103/B58) **= the actual tower**: it matches the resolved
    SL(5) tower (B61+B62) exactly, including `char(M⁵)` (the degree=rank top, = `Sym⁵`'s top weight — no separate
    promotion needed).
  - **`differ_by_single_promotion()` / `divergence_at_n6()`** — through `n=5` the θ-split = the tower up to a
    single degree=rank promotion; at `n=6` the θ-split and Sym **DIVERGE** (a₁ 2vs3, a₂ 3vs2, b₂ 1vs2 — the
    banked **V26/V27**; they agree on `a₃(n=6)=2`).
  - **`b112_correction()`** — the explicit downgrade.
- **`FINDINGS.md`** — the tables + the correction.

**Result / correction to B112.** B112 proves the θ-split **combinatorics** for all `n` (a real `A_{n−1}` theorem —
this stands). But the **identification with the tower** (the V25 gap) holds only `n ≤ 5`; at `n ≥ 6` the θ-split
and the Sym two-sequence diverge. So **B112's "sign half proved for all n" → "θ-split combinatorics all n; = the
tower's sign half for n ≤ 5; all-n OPEN."** The **Sym two-sequence is the actual tower** (it equals the tower
wherever known + carries `char(Mⁿ)`), so **proving the Sym two-sequence for all n** (B103's open problem) is the
live route — not the θ-split.

```bash
python frontier/B116_reconcile_theta_sym/probe.py
python -m pytest tests/test_b116_reconcile_theta_sym.py -q
```
No physics claim; the `ρ_n` catalog proof stays the central target; proven core P1–P16 untouched.
