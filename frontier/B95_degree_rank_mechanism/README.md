# B95 — the degree=rank mechanism (Task M)

Attacks the project's deepest open question (V75): *why* does degree = rank, and why do different
components give different degrees? CH is refuted; the exponent reads A's specific eigenvalue structure.

- **`probe.py`** — (1) the principal spectrum is **forced** by `tr A = tr A⁻¹ = 1` (mult-1 = n−2):
  `{1,i,−i}` (n=3), `{1,1,ω,ω²}` (n=4), `{1,1,1,−1,−1}` (n=5), **impossible at n≥6**; (2) the n=5 forced
  spectrum has `A²=I` ⟹ `A,B` involutions ⟹ `⟨A,B⟩` dihedral ⟹ **reducible** (no irreducible SL(5)
  principal rep).
- **`FINDINGS.md`** — the derivation, the degeneration, and the honest scope.

**Result.** "exponent = rank" (`Mⁿ=L` on the principal component) is an **n ∈ {3,4} phenomenon**: the
forced principal spectrum admits an irreducible bundle rep only at n=3,4, **degenerates** (dihedral) at
n=5, and is **impossible** at n≥6. This upgrades B78's numerical SL(5) "method-limit" to a structural
reason, and corrects the handoff's SL(5) spectrum guess (`{1,1,1,ω,ω²}` has trace 2). The mechanism reads
whether the cusp's forced finite-order spectrum admits an irreducible rep — explaining the n≥5 wall on
*both* the tower and degree=rank. A complete degree classification at every rank stays open.

```bash
python frontier/B95_degree_rank_mechanism/probe.py
python -m pytest tests/test_b95_degree_rank_mechanism.py -q
```
No Origin-core claim; proven core P1–P16 untouched.
