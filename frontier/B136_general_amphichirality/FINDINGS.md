# B136 — The amphichirality criterion for ALL once-punctured-torus bundles (general LR words) (V125)

Extends the now-proved metallic chirality recursion (B134; metallic `R^m L^m` blocks, B128/`K011`) from the metallic
locus to **any** once-punctured-torus bundle (any LR monodromy word). Re-derived in-sandbox; provable the same way — it
is Goodman–Heard–Hodgson 2008's anti-palindromic criterion in **block-pair** form. The genuinely-novel thread the
audit identified, pushed to its general statement.

**One-line result.** A once-punctured-torus bundle with monodromy `W = R^{a₁}L^{b₁} R^{a₂}L^{b₂} … R^{a_k}L^{b_k}` is
**amphichiral ⟺ the block-pair sequence `((a₁,b₁),…,(a_k,b_k))` is invariant under (reverse the order **and** swap each
pair's components `(a,b)→(b,a)`) up to cyclic rotation.** The metallic case `a_i=b_i` reduces this to "the block-length
sequence is a cyclic palindrome" (B134), so B136 is the strict generalization.

## The theorem (proved, corollary of GHH 2008)

By GHH 2008 (arXiv:0801.4815), amphichiral ⟺ `W` anti-palindromic, i.e. `reverse(W) = swap_{L↔R}(W)` cyclically. Now
```
   reverse(R^{a₁}L^{b₁}…R^{a_k}L^{b_k}) = L^{b_k}R^{a_k} … L^{b₁}R^{a₁}      (order reverses; each RᵃLᵇ → LᵇRᵃ)
   swap_{L↔R}(R^{a₁}L^{b₁}…)            = L^{a₁}R^{b₁} … L^{a_k}R^{b_k}
```
Both are `LˣRʸ`-block words; reading their (L-exp, R-exp) pairs gives `((b_k,a_k),…,(b₁,a₁))` and `((a₁,b₁),…,(a_k,b_k))`.
These are equal as cyclic words ⟺ the pair sequence `((a_i,b_i))` is fixed (up to rotation) by "reverse order + swap
components". **∎** **Specialization:** `a_i=b_i=m_i` makes the swap trivial, so it reduces to `(m_k,…,m₁)` a cyclic
rotation of `(m₁,…,m_k)` = cyclic palindrome = **B134**.

**Verified:** the lemma `pair_criterion(pairs) ⟺ anti_palindromic(W)` holds exhaustively (all block-pair sequences,
≤4 blocks, exponents ≤3 — 7380 cases); the criterion reduces to B134 on the metallic locus (checked); and it agrees
with SnapPy `is_amphicheiral` on metallic **and genuinely non-metallic** words (`(1,2),(2,1)` amphichiral; `(1,3),(3,1)`
amphichiral; `(1,2),(1,2)` chiral).

## Significance

This is the full amphichirality criterion for once-punctured-torus bundles, in a clean combinatorial block-pair form —
the natural home of B128/B134's metallic recursion. As with B134, the **mechanism is GHH 2008**; the project's
contribution is the explicit block-pair restatement (and the metallic-palindrome corollary). Honest novelty: this is a
restatement/specialization of a published criterion, useful as a clean computational criterion, not a new theorem about
3-manifolds.

## Reproduce

```
python frontier/B136_general_amphichirality/probe.py
python -m pytest tests/test_b136_general_amphichirality.py -q
```

The lemma (exhaustive) and the B134-specialization run unconditionally; the SnapPy three-way check is guarded.

**Tier.** MATH (low-dim topology). Generalizes B134/`K011`. Nothing to `CLAIMS.md`; P1–P16, B85, S031, B124–B135
untouched. Ledger **V125**.

**Anchors:** B134/`K011` (the metallic case — proved), B128 (the original recursion), `docs/NOVELTY_AUDIT.md` (R1).
External: **Goodman–Heard–Hodgson 2008** (arXiv:0801.4815, the anti-palindromic word criterion); once-punctured-torus
bundles; SnapPy `is_amphicheiral`.
