# B136 — amphichirality for ALL once-punctured-torus bundles (general LR words)

Generalizes the proved metallic chirality recursion (B134) from `R^m L^m` blocks to **any** LR monodromy word.

**Theorem (proved, corollary of GHH 2008).** `W = R^{a₁}L^{b₁}…R^{a_k}L^{b_k}` is **amphichiral ⟺ the block-pair
sequence `((a_i,b_i))` is invariant under (reverse order + swap each `(a,b)→(b,a)`) up to cyclic rotation.** Proof:
GHH give amphichiral ⟺ `W` anti-palindromic; `reverse(W)` and `swap(W)` are both `LˣRʸ`-block words whose pair
sequences `((b_k,a_k),…)` and `((a_i,b_i))` match cyclically iff the criterion holds. **∎** Metallic `a_i=b_i` →
cyclic palindrome = **B134**.

`probe.py` verifies: the lemma `pair_criterion ⟺ anti_palindromic` exhaustively (7380 sequences); the reduction to
B134 on the metallic locus; SnapPy three-way agreement on metallic + non-metallic words (`(1,2),(2,1)` amphichiral;
`(1,2),(1,2)` chiral).

```
python frontier/B136_general_amphichirality/probe.py
python -m pytest tests/test_b136_general_amphichirality.py -q
```

**Honest novelty:** a clean block-pair restatement/generalization of GHH 2008's criterion (the mechanism is GHH's),
with the metallic-palindrome as a corollary. **Tier.** MATH. Nothing to `CLAIMS.md`; P1–P16, B85, S031, B124–B135
untouched. See `FINDINGS.md`; ledger **V125**.
