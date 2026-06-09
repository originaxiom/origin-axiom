# B134 — the chirality recursion PROVED (corollary of GHH 2008) + the novelty audit

Phase B (novelty audit) + Phase C (one proof) of the approved program.

**The theorem (proved).** For a metallic-block word `W = R^{m₁}L^{m₁}…R^{m_k}L^{m_k}`, the bundle is **amphichiral ⟺
the block-length sequence `(m₁,…,m_k)` is a cyclic palindrome.** Proof: GHH 2008 give amphichiral ⟺ `W` anti-palindromic
(`reverse(W)=swap_{L↔R}(W)` cyclically); for a metallic-block word both `reverse(W)` and `swap(W)` are `LᵃRᵃ`-block
words, matching cyclically iff the block-length sequences agree up to rotation = cyclic palindrome. **∎** This upgrades
B128 from computer-assisted (15/15) to **proved**.

**The novelty audit (cited; `../../docs/NOVELTY_AUDIT.md`):**
- R1 chirality recursion — **PARTIALLY-KNOWN**: mechanism = GHH 2008; the block-sequence lift is the novel kernel (proved here).
- R2 two-seed fork — **KNOWN** (Kitano–Nozaki 2020), with a framing qualification: discreteness is gluing-map-driven (splice/swap), not distinctness; B131's "heterogeneity" reading is identity-gluing-specific (reconciled).
- R3 SU(2)_k field content — **KNOWN/standard** (Jeffrey 1992; Dong–Lin–Ng 2015; Lawrence–Zagier 1999); the corrected B132 content is standard.

`probe.py` verifies: the lemma `anti_palindromic(W) ⟺ cyclic_palindrome(blockseq)` exhaustively (5460 sequences); the
SnapPy three-way agreement (GHH anti-pal == B128 cyc-pal == `is_amphicheiral`, 16/16); the R2 gluing-map reconciliation
(swap-glue same-seed fig8 → degree-16 finite → discrete).

```
python frontier/B134_chirality_recursion_proved/probe.py
python -m pytest tests/test_b134_chirality_recursion_proved.py -q
```

**Reconciliations banked:** `K011` upgraded to **PROVED** (cite GHH); `B131` annotated (gluing-map dependence,
Kitano–Nozaki); `K015`/`K010` get the R3 standard citations.

**Tier.** MATH (low-dim topology). Nothing to `CLAIMS.md`; P1–P16, B85, S031, B124–B133 untouched. See `FINDINGS.md`;
ledger **V123**. External: GHH 2008 (arXiv:0801.4815), Kitano–Nozaki 2020 (arXiv:1904.02559), Jeffrey 1992, Dong–Lin–Ng
2015, Lawrence–Zagier 1999.
