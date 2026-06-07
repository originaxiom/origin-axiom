# B111 — the tower's sign structure + the degree=rank exponent

Banks the CC-web "sign findings" handoff + supplement. **Headline:** the tower's sign/multiplicity structure is
the **opposition-involution closed form**, *except* for a single **degree=rank promotion** `char(M) → char(Mⁿ)` —
naming both halves of the `ρ_n` prize. NO physics; no `CLAIMS.md`; the `ρ_n` proof stays the target; P1–P16
untouched.

- **`probe.py`**
  - **`sl3_sign_rule()` (PART 0)** — `char(J)` factorizations; the **corrected** parity `(t−1)(t−det N)` (the
    handoff's `(t+det N)` was wrong); det-determined, m-stable.
  - **`opposition_closed_form()` / `closed_form_matches_b62()`** — `⌈(n−h)/2⌉` / `⌊(n−h)/2⌋`; matches B62 height-2.
  - **`tower_vs_closed_form()` (PATH B/C, the key result)** — `Tower(n) = closed form with one char(M¹) promoted
    to char(Mⁿ)` (verified n=3,4); the single non-bulk piece is the degree=rank top power `L=c·Mⁿ`.
  - **`mpower_scalar_table()` (ADDITION 1)** — `M⁴=−1` scalar on the SL(4) **secondary** ⇒ `k=4` **impossible**;
    `M⁴` non-scalar on the **principal** ⇒ `k=4` allowed. *Proves the negative; does not prove `k=n`.*
  - **`cusp_order_pattern()` (ADDITION 2)** — cusp orders `{n−1, n+1, 2n}`; `ord−1` formula **TESTED-NEGATIVE**.
  - **`covering_degree_test()` (A1d)** — eigenvalue-level covering degree `= k` (partial-positive); full-component
    covering OPEN (a hypothesis).
  - **`s_n_to_c_bridge_dead()`** — `s_n∈{±1}` can't reach order-4 `c=i` (DEAD, same as B108).
- **`FINDINGS.md`** — the tables, the corrections, the honest scopes.

**Result.** Sign half of the tower = the `θ` closed form; the only non-bulk ingredient is `char(Mⁿ)` (degree=rank).
The exponent `k` is algebraically constrained (the `M⁴`-scalar impossibility forces `k=3` on the secondary). The
`ρ_n` prize splits into a closed-form bulk half (θ) and a degree=rank peripheral half (Path A).

```bash
python frontier/B111_sign_structure/probe.py
python -m pytest tests/test_b111_sign_structure.py -q
```
No physics claim; the `ρ_n` catalog proof stays the central target; proven core P1–P16 untouched.
