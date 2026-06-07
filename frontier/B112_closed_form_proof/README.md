# B112 — PROOF of the opposition-involution closed form (the sign half of ρ_n)

The first piece of the `ρ_n` catalog proved **from first principles, engine-free, for all `n`**. B111 split the
prize into the **sign** half (bulk `θ=−w₀`) and the **degree=rank** promotion; this proves the sign half. NO
physics; no `CLAIMS.md`; the `ρ_n` proof stays the prize; P1–P16 untouched.

**Theorem (all `n`, all `h`):** `mult char(M^h) = ⌈(n−h)/2⌉`, `mult char(−M^h) = ⌊(n−h)/2⌋`.

**Proof** = an elementary **root-system lemma** + the banked **B64** parity assignment:
- **`opposition_action_matrix()` / `eigenspace_split()` / `is_reversal_involution()`** — `θ=−w₀` acts on the
  `(n−h)` positive height-`h` roots of `A_{n−1}` as the **reversal involution** `i ↦ (n−h+1)−i`; its `(+1,−1)`
  eigenspaces have dims `(⌈(n−h)/2⌉, ⌊(n−h)/2⌋)`. *(elementary; verified all n≤12, all h, two ways.)*
- **B64 assignment:** `+1` (symmetric) sector → `char(M^h)`, `−1` (antisymmetric) → `char(−M^h)`.
- **`lemma_holds()`** — the lemma `= ⌈⌉/⌊⌋` for all n≤12; matches B62 height-2 and B111 (n=3,4).

**Scope.** Proves the **bulk θ-decomposition** = the **sign half** of `ρ_n`. The full tower = this **+ the single
degree=rank promotion** `char(M)→char(Mⁿ)` (B111) — the **power half** (`speculations/S022`), still open.
Computer-assisted (the lemma is rigorous; the sector assignment leans on B64 + verification against the tower).

```bash
python frontier/B112_closed_form_proof/probe.py
python -m pytest tests/test_b112_closed_form_proof.py -q
```
No physics claim; the `ρ_n` catalog proof stays the central target; proven core P1–P16 untouched.
