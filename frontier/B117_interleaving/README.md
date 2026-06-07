# B117 — the tower is the Sym two-sequence; the "promotion" is a Sym¹ absence

The **headline reframing** of the B111–B116 run (the Opus interleaving insight, verify-don't-trust). The (n²−1)-dim
trivial-point tower is **one object** — the Sym plethysm two-sequence (B103/B58) — not two separable halves (a
"sign half" + a "power half"). NO physics; no `CLAIMS.md`; the `ρ_n` proof stays the prize; P1–P16 untouched.

- **`probe.py`**
  - **`dimension_identity()`** — `(n+1)(n+2)/2 − (n²−1) = −(n−4)(n+1)/2` (roots `{−1,4}`); n=4 the unique perfect
    fit, n<4 surplus (omit modules), n>4 deficit (double modules).
  - **`sym_selection_equals_two_sequence()`** — the dimension-derived Sym-selection **= B103's
    `two_sequence_mult` μ_d** (n=2..8); μ_n=1 ∀n; the n≥6 doubling = the overlap `Sym²..Sym^{n−3}`.
  - **`n3_uniqueness()`** — the unique subset of {0,1,2,3} summing to 8 is `{0,2,3}` (**Sym¹ absent** — the
    "promotion" dissolved; char(−M) at height 1 is `Sym³`'s contribution).
  - **`sym_product_equals_b80_tower()`** — `Sym⁰..⁴` char-poly product = the **B80 proved n=4 tower** (deg 15).
  - **`sym_n_presence_status()`** — μ_n=1 ⇒ **char(Mⁿ) always a factor = degree=rank** at the char-poly level;
    with the precise status (dim-forced only n=3; rep-theory n=2,4; two-sequence form n≥5 — honors the DO-NOT).
  - **`n6_path4_crosscheck()`** — Path 4: the n=6 bulk prediction (|k|=3 total = 3 = max(n−d,1)) vs B66's
    gauge-under-counted 2 (consistency, not decisive).
- **`FINDINGS.md`** — the derivation tables + the reframe.

**Result.** The tower = the Sym two-sequence (one object). The "promotion"/"two-halves" framing is **superseded**;
degree=rank's `char(Mⁿ)` = **Sym^n presence** (μ_n=1). **The re-aimed prize: prove the two-sequence μ_d for all n**
(B103's standing open problem — the realization/trace-ring wall), not "close two halves."

```bash
python frontier/B117_interleaving/probe.py
python -m pytest tests/test_b117_interleaving.py -q
```
No physics claim; the `ρ_n` catalog proof stays the central target; proven core P1–P16 untouched.
