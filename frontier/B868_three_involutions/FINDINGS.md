# B868 — G6 closed: the cascade's gate is the LINEAR −w₀/θ involution at every level; c appears nowhere

cc banking seat, 2026-08-03. Mathematics scope; nothing to `CLAIMS.md`; Gate 5 untouched.

## The three involutions, separated

The θ/c conflation has killed this programme **three times** (B780 retracted; B784 refuted; C21
mechanism-corrected). The cascade's gate uses "conjugation of labels" — G6 asked *which* involution
that is, at every level. Answer, computed:

| involution | nature | where it acts in the cascade |
|---|---|---|
| **the gate's C** | **linear**, λ ↦ −w₀(λ) on each level's weight lattice | **everywhere** — it *is* the gate |
| **θ (matrix form)** | linear outer automorphism realizing C: X ↦ −Xᵀ on A-type; Ad(det = −1 reflection) on D-type | the same involution, in its matrix presentation |
| **c** | **antilinear** (complex conjugation of scalars) | **nowhere** — the real-structure / layer-8 coordinate |

## The checks

1. **Label maps = the gate's CONJ tables**: A₄'s −w₀ reverses Dynkin labels — (1,0,0,0) ↦
   (0,0,0,1), i.e. 5 ↦ 5̄; (0,1,0,0) ↦ (0,0,1,0), 10 ↦ 10̄ ✓. D₅ (n odd, −1 ∉ W): −w₀ swaps the
   spinor nodes — 16 ↦ 16̄ ✓. E₆'s flip: 27 ↦ 27̄ (the fold, banked).
2. **Fixed cores match B860 and Q3**: the involution's fixed algebra per level — so(5) = 10 in
   su(5), so(4) = 6, so(3)×so(2) = 4, so(3) = 3 (B860's computed even parts), and **so(9) = 36
   of 45 in so(10)** computed here directly via Ad(diag(1,…,1,−1)) — the handoff Q3's B₄ core ✓.
   Note the D-type subtlety that would have bitten a naive check: on so(n) in the vector
   realization, X ↦ −Xᵀ is the *identity*; the outer involution is conjugation by a det = −1
   orthogonal element. The uniform statement is the weight-lattice one (λ ↦ −w₀λ).
3. **Source-level**: the gate's CONJ tables in B861/B863/B865 are pure label maps; **no complex
   conjugation of scalars appears anywhere in the cascade's code** — verified by scan.

## Consequence

**The ledger line "the gate IS the framework's even/odd boundary" is now precise**: the gate is the
θ-class (linear, outer) involution, level by level; and **c — the antilinear chirality/sheet bit —
enters the story exactly once, at layer 8** (the real-form question), which is where the framework
already places it. The B780/B784/C21 conflation cannot recur at cascade level: the two involutions
now have computed, non-overlapping jurisdictions.

`tests/test_b868_involutions.py`
