# B1621 — THE PRINCIPLE'S CLOCK AND TICK ON THE MATTER: the clock (the word's parity) stays inside the parity grading — it can split masses, never mix, and its mean on the matter is zero; the tick (σ² = LR) breaks the grading, and its operator mean is the rank-one democratic matrix, the quarks' leading-order shape in T̄ ⊗ T only; its means on the clock's forms give three equal masses under every tensor, and for the leptons its heavy line cannot be the heaviest state — the principle's own data, read by their means, fix no number

**Verdict: PROVED** (all eight sealed cells hold). cc (main), 2026-10-09. Sealed `bded4d62e` before the run. A READING:
"given a coupling that reads the clock or the tick by its invariant mean", not an adopted postulate. P2 reads only B1612's
transcription. Every statement concerns the weave's triplet T and the principle's own data, the rule's word and its tick,
not one thread's geometry. **0 of 19.**

## 0. Seen first

As sealed: `VERDICT topic-sweep /democratic|rank.one|invariant mean|Ces[aà]ro|trimaximal|parity grading|flavou?r democracy/: 12 of 1392 arcs on main match (NEGATIVE 3, OPEN 1, PROVED 8)`
— B320 (ℤ/3 does not force rank-one democracy), B342, B1612, B1617, B1618, B1620, and the SM seat's W38–W41.
**Literature:** flavour democracy (Harari–Haut–Weyers 1978; Fritzsch and Xing 2000); Burnside's theorem.

## 1. The computation (`clock_and_tick.py`, sealed, unchanged; `clock_and_tick.json`)

| | sealed prediction | prior | result |
|---|---|---|---|
| **K1** | the inner lifts diagonal in the parity basis with real sign characters, commuting; the prefix product equals diag(χ_p(class)) along the word | 97% | **HOLDS** — the lines carry (a, b) = (−, +), (+, −), (−, −); the prefix product matches to 3.5 × 10⁻¹¹ for every n ≤ F₂₆ = 121 393 |
| **K2** | the clock's matrices span exactly the diagonal algebra | 95% | **HOLDS** — dimension 3, largest off-diagonal entry 2 × 10⁻¹⁶ |
| **K3** | the clock's mean on T is zero (below 10⁻³ at F₃₀) | 97% | **HOLDS** — every line's character averages to ±7.4 × 10⁻⁷ at N = 1 346 269 |
| **T1** | T(LR): eigenvalues {1, ω, ω²}, order 3, monomial and cyclic on the lines, trimaximal eigenbasis | 97% (seen) | **HOLDS** — the lines go 0 → 1 → 2 → 0; every eigenvector has moduli squared ⅓ |
| **T2** | the tick's operator mean is rank one, democratic, and does not commute with the clock | 95% (seen in part) | **HOLDS** — singular values (1, 0, 0); every entry of modulus ⅓; it breaks the grading |
| **T3** | the tick's means on the clock's forms give degenerate or zero spectra under all three tensors | 70% | **HOLDS, sharper** — three EQUAL masses (1, 1, 1) under T̄ ⊗ T, T ⊗ T and Sym² T alike: LR carries the character c = 1 (the SM seat's W38), so its mean on a diagonal form is a scalar |
| **P1** | tick–tick heavy lines aligned; tick–clock heavy row (⅓, ⅓, ⅓) | 95% | **HOLDS** |
| **P2** | (⅓, ⅓, ⅓) only as U's second column, not as the τ row or the ν₃ column; the quarks' \|V_tb\| = 1 recorded | 85% | **HOLDS** — inside NuFIT 6.0's 3σ ranges only as column 2 (B1612's TM2 column); the τ row and the ν₃ column fail. \|V_tb\| = 1 at leading order sits 25.9σ from PDG's 0.999118 ± 0.000034, as any leading order does |

## 2. What it says

**The principle's two forced data act on the matter in opposite ways.**
- **The clock** is the word's parity class, the datum B1620 found splits the sectors 1 + 2. It acts on T through the
  parity grading itself: the prefix at time n acts as conjugation by the prefix, which on T is diag(χ_p). So every
  coupling that reads the clock is diagonal in the parity lines, under every tensor. It can give three different masses
  (the 1 + 2 split), but **it can never produce mixing**. Its invariant mean on the matter is zero, so the clock acts
  only through its fluctuations.
- **The tick** σ² = LR cycles the parity lines and **breaks the grading**, which is what B1620 said the observed mixing
  needs. Its operator mean, the coupling that pairs a state with its image one tick later averaged over the rule's time,
  is the **rank-one democratic matrix**. That gives one heavy generation in each sector reading it and, for two such
  sectors, no mixing at leading order: the quark sector's leading-order shape (m_t, m_b ≫ the rest; |V_tb| ≈ 1).
  - **Its scope is narrow.** The operator mean is canonical only for T̄ ⊗ T = End(T). Under the tensors the SM seat
    reads given Λ, the tick acts on forms, and its means on the clock's forms give **three equal masses**: no hierarchy.
  - For the leptons the tick's heavy line has overlaps (⅓, ⅓, ⅓) with the clock's lines. The data admit that only as
    the second column of U (TM2), never for the sole heaviest state. So the leptons' leading order is not the tick's.
- **So the principle's own data, read by their means, fix no number.** At most they supply the quarks' leading-order
  shape, under one tensor. With free weights (Burnside) the clock and tick together reach every matrix, which restates
  the free count rather than reducing it. The count stands at 0 of 19; the observed mixing still needs a vacuum chosen
  by a dynamics.

## 3. Disclosed

- T1 and T2 reproduce an exploratory run seen before the seal (disclosed there).
- The "invariant mean" is the arc's choice of reading (disclosed there); other weightings are not covered.
- B320's refutation stands untouched: no rank one is claimed from ℤ/3 invariance. T2's rank one is the mean of the tick's
  powers, not the commutant.

## 4. Files

`verification/clock_and_tick.py` (sealed, unchanged), `clock_and_tick.json`, `clock_run.txt`. Test:
`tests/test_b1621_the_principles_clock_and_tick.py`.
