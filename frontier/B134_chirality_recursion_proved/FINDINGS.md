# B134 — The chirality recursion PROVED (a corollary of Goodman–Heard–Hodgson 2008) + the novelty audit (V123)

Phase B (novelty/literature audit) + Phase C (one proof) of the approved program. A deep, adversarial literature pass
(fan-out search → fetch → 3-vote verify → cited synthesis) placed the project's three candidate-novel results against
prior art. This stage banks the audit's actionable outputs, **proves** the one genuinely-new kernel (the B128 chirality
recursion — upgrading it from computer-assisted 15/15 to **proved**), and reconciles B131/B132 with the located prior
art. MATH tier; nothing to `CLAIMS.md`; P1–P16, B85, S031, the merged B124–B133 untouched.

## The novelty audit (Phase B) — verdicts with citations (full report: `../../docs/NOVELTY_AUDIT.md`)

- **R1 — the chirality recursion (B128/K011): PARTIALLY-KNOWN, with a genuine novel kernel.** The
  amphichirality↔palindromic-monodromy *mechanism* is **published**: **Goodman–Heard–Hodgson 2008** (arXiv:0801.4815,
  *Commensurators of cusped hyperbolic manifolds*) classify the symmetries of a once-punctured-torus bundle by its L/R
  monodromy word — **anti-palindromic** word (reverse = L↔R swap, cyclically) ⟺ orientation-**reversing** symmetry ⟺
  amphichiral; **palindromic** word ⟺ orientation-preserving π-rotation. (Also long-established for rational/2-bridge
  knots: Kauffman–Lambropoulou, a "well-known result".) The residual **novel** kernel is the lift to the **integer
  block-length sequence** — proved below.
- **R2 — the two-seed fork (B131/K014): KNOWN, with a framing qualification.** **Kitano–Nozaki 2020**
  (arXiv:1904.02559, *Finiteness of the image of the Reidemeister torsion of a splice*) prove finiteness via the two
  pieces' A-polynomial curves intersecting in the boundary-torus character variety (gcd=1 ⟹ Bézout-finite) — exactly
  B131's mechanism. **Caveat (verified):** the discreteness is driven by the meridian↔longitude-**swapping splice**
  gluing, **not** by the pieces being distinct (a same-knot splice `Σ(K,K)` is already finite). So B131's "heterogeneity
  makes the choice" is correct **only for the identity gluing**; reconciled below.
- **R3 — the SU(2)_k field content (B132/K015, corrected): KNOWN / standard.** **Jeffrey 1992** (CMP 147: torus-bundle
  `Z=Tr ρ(U)` = explicit Gauss sum, cyclotomic), **Dong–Lin–Ng 2015** (modular rep ℚ(ζₙ)-rational, congruence kernel
  level `n=ord(T)`), **Lawrence–Zagier 1999** (WRT in ℚ(ζ), Galois-equivariant). The corrected B132 content is
  standard quantum topology; we cite, claim nothing novel.

## The theorem (Phase C) — the chirality recursion, PROVED

> **Theorem.** For a metallic-block word `W = R^{m₁}L^{m₁} R^{m₂}L^{m₂} … R^{m_k}L^{m_k}`, the once-punctured-torus
> bundle is **amphichiral ⟺ the block-length sequence `(m₁,…,m_k)` is a cyclic palindrome** (its reversal is a cyclic
> rotation of it).

**Proof.** By Goodman–Heard–Hodgson 2008, the bundle is amphichiral ⟺ `W` is **anti-palindromic** as a cyclic L/R
word, i.e. `reverse(W) = swap_{L↔R}(W)` cyclically. The elementary identity:
```
   reverse(R^{m₁}L^{m₁}…R^{m_k}L^{m_k}) = L^{m_k}R^{m_k} … L^{m₁}R^{m₁}     (block order reverses; each RᵃLᵃ → LᵃRᵃ)
   swap_{L↔R}(R^{m₁}L^{m₁}…R^{m_k}L^{m_k}) = L^{m₁}R^{m₁} … L^{m_k}R^{m_k}
```
Both are concatenations of `LᵃRᵃ` blocks, with block-length sequences `(m_k,…,m₁)` and `(m₁,…,m_k)`. Two such
block-words are equal as cyclic words **iff** their block-length sequences agree up to cyclic rotation. Hence `W` is
anti-palindromic ⟺ `(m_k,…,m₁)` is a cyclic rotation of `(m₁,…,m_k)` ⟺ `(m₁,…,m_k)` is a cyclic palindrome. (The word
has even length `2·Σmᵢ`, so GHH's even-length hypothesis for the orientation-reversing case is automatic.) **∎**

So B128's recursion is **the GHH anti-palindromic criterion specialized to metallic-block words**, with the
block-length-sequence palindrome as the clean restatement — the elementary lift is the project's novel contribution;
the chirality mechanism is GHH's.

**Verified three ways:** (1) the lemma `anti_palindromic(W) ⟺ cyclic_palindrome(blockseq)` holds for **all** block
sequences (exhaustive over length ≤6, entries ≤4 — 5460 cases — the combinatorial certificate of the string identity);
(2) SnapPy `is_amphicheiral` (the GHH input / ground truth) agrees on a 16-case sample; (3) consistent with B128's
15/15.

## Reconciliations (the audit's other actionable outputs)

- **B131 (R2): annotate with the gluing-map dependence.** B131's identity-gluing result (same seed → continuum,
  distinct → discrete) is correct, but the discreteness phenomenon is more fundamentally **gluing-map-driven**
  (Kitano–Nozaki): under the splice (swap) gluing the gluing map alone forks even a same-seed glue. Verified here:
  swap-gluing fig8-to-fig8 gives `P = f(f(P))` (`f(t)=t⁴−5t²+2`, B67), degree 16 → **finite/discrete**, whereas the
  identity-glued same-seed stays a continuum. So "heterogeneity makes the choice" is **identity-gluing-specific**; the
  general statement is "the gluing map determines continuum-vs-discrete" (Kitano–Nozaki), with distinctness sufficient
  under the identity gluing. B131's math stands; its framing is qualified.
- **K011 (R1): upgrade to PROVED** (was computer-assisted 15/15) — cite GHH 2008.
- **K015/K010 (R3): add the standard citations** (Jeffrey, Lawrence–Zagier, Dong–Lin–Ng) — the corrected B132 content
  is standard.

## Honest scope / residual

- The theorem rests on GHH 2008's word-classification (an established, peer-reviewed result); the lift is elementary.
  A specialist should confirm GHH's criterion is stated as an **iff** for all these bundles (the audit reads it as a
  classification — i.e. iff — but verifying GHH's exact hypotheses is the one outstanding check).
- Open (audit's residual): whether Bowditch / Hoste–Shanahan state any block-sequence palindrome criterion not
  surfaced; the per-word eigenvalue *subfield* (vs the ambient ℚ(ζₙ)) for R3 is a corollary-level refinement.

## Reproduce

```
python frontier/B134_chirality_recursion_proved/probe.py
python -m pytest tests/test_b134_chirality_recursion_proved.py -q
```

The lemma (exhaustive) and the gluing-map reconciliation run unconditionally; the SnapPy three-way check is guarded.

**Tier.** MATH (low-dim topology). The chirality recursion is now **proved** (`K011` upgraded); the novelty audit is
`docs/NOVELTY_AUDIT.md`; B131 annotated, K015/K010 cited. Nothing to `CLAIMS.md`; P1–P16, B85, S031, B124–B133
untouched. Ledger **V123**.

**Anchors:** B128/`K011` (the recursion — now proved), B131/`K014` (the fork — qualified), B132/`K015` (the quantum
layer — cited), `docs/NOVELTY_AUDIT.md`. External: **Goodman–Heard–Hodgson 2008** (arXiv:0801.4815); **Kitano–Nozaki
2020** (arXiv:1904.02559); **Jeffrey 1992**; **Dong–Lin–Ng 2015**; **Lawrence–Zagier 1999**; Kauffman–Lambropoulou;
Guéritaud–Futer (the LR-word/canonical-triangulation formalism).
