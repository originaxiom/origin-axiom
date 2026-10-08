# B1621 — PREREGISTRATION: THE PRINCIPLE'S CLOCK AND TICK ON THE MATTER — of the two forced data outside the weave, which can break the parity grading the observed mixing needs, and what do their invariant means give under each mass tensor?

cc (main), 2026-10-08, after S99. B1620 showed that couplings in τ alone keep the inner automorphisms (the parity grading
K), so every mixing matrix is a permutation, and the observed mixing needs something that breaks the grading. The
principle supplies two forced data outside the weave: the **clock**, the parity class (A_n, B_n) mod 2 of the rule's
fixed-point word (B1620 part B), and the **tick**, σ² = LR, the rule's double step (B1083's arrow; the genesis theorem's
A = LR). This arc asks what each does to the weave's triplet T. **Sealed before `clock_and_tick.py` runs.** Only P2 reads
data, and only B1612's transcription. The couplings here are a READING ("given a coupling that reads the clock or the tick
by its invariant mean"), not an adopted postulate. 0 of 19.

## Seen first

`VERDICT topic-sweep /democratic|rank.one|invariant mean|Ces[aà]ro|trimaximal|parity grading|flavou?r democracy/: 12 of 1392 arcs on main match (NEGATIVE 3, OPEN 1, PROVED 8)`
- **B320 (NEGATIVE):** "the democratic Yukawa (3λ, 0, 0) is forced by ℤ/3" overclaims. A ℤ/3-invariant (circulant)
  matrix has rank 3 generically, and rank-one democracy needs S₃. This arc does not claim invariance forces rank one; T2's
  rank one comes from the operator MEAN of the tick, which is a reading.
- **B342:** the object's ℤ/3 is the standard trimaximal symmetry; TM2 is disfavoured relative to TM1.
- **B1612:** among the weave's fixed patterns is the all-⅓ matrix; one-column survivors (⅓, ⅓, ⅓) as U's second column
  (TM2) and (⅔, ⅙, ⅙) as its first (TM1).
- **B1617, B1618:** the inner lifts act as the parity signs, and U is a 3-cycle on the lines.
- **B1620:** τ-only residuals give permutations; the clock's 1 + 2 split.
- The SM seat's W38–W41: T is the cube's rotation group twisted by c, and the mass tensor is T ⊗ T given Λ.

**Literature:** flavour democracy (Harari–Haut–Weyers 1978; reviewed by Fritzsch and Xing 2000): a rank-one all-equal mass
matrix gives one heavy generation and, for two aligned sectors, no mixing at leading order. Burnside's theorem: the
matrices of an irreducible representation span End(T).

## Disclosed

- **Seen before the seal (an exploratory run, uncommitted):** T(LR) has eigenvalues {1, ω, ω²} on T, cycles the three
  parity lines, and its eigenvectors have moduli squared ⅓ in the parity basis. T1 and T2 therefore reproduce what was
  seen. K1–K3, T3, P1 and P2 were not run.
- **The reading is the arc's choice of coupling:** "reads by its invariant mean". The clock's mean is the average over the
  word's prefixes. The tick's means are the average of its operator powers (T2, canonical only in T̄ ⊗ T = End(T)) and
  the average of its action on the clock's forms (T3, all three tensors). Other weightings are not covered: by Burnside,
  free weights over the group's elements give any matrix, which is the count of free numbers restated.
- P2's quark line is a leading-order statement, not a fit. Any leading-order pattern sits many σ from precision data.

## Cells, predictions, priors

| | prediction | prior |
|---|---|---|
| **K1** | the inner lifts are diagonal in the parity basis, with real sign characters, and commute; along the word to F₂₆ the prefix product equals diag(χ_p(class)): **the clock acts within the grading** | 97% |
| **K2** | the clock's matrices span exactly the diagonal algebra (dimension 3): every clock-reading coupling, under every tensor, is diagonal in the parity lines — **it can split masses, never mix** | 95% |
| **K3** | the clock's invariant mean on T is zero (every line's character averages to 0; below 10⁻³ at F₃₀) | 97% |
| **T1** | T(LR) has eigenvalues {1, ω, ω²} (turns 0, ⅓, ⅔), order 3, is monomial and cyclic on the parity lines, and its eigenvectors have moduli squared ⅓ in the parity basis: **the tick breaks the grading** | 97% (seen) |
| **T2** | the tick's operator mean is rank one, with every entry of modulus ⅓ in the parity basis (the democratic matrix up to phases), and it does not commute with the clock | 95% (seen in part) |
| **T3** | the tick's mean acting on the clock's forms gives degenerate or zero spectra under all three tensors | 70% |
| **P1** | two tick-reading sectors have aligned heavy lines (leading-order mixing 1); the tick-against-clock heavy row is (⅓, ⅓, ⅓) | 95% |
| **P2** | (⅓, ⅓, ⅓) lies inside NuFIT 6.0's 3σ ranges only as U's second column, not as the τ row and not as the ν₃ column: **the leptons' sole heaviest state cannot be the tick's heavy line**; the quarks' leading order |V_tb| = 1 is recorded with its pull | 85% |

**The reading, written before the run (the cells can only lower it).** Of the principle's two forced data outside the
weave, the clock stays inside the parity grading: it can split masses but never mix, and its mean on the matter is zero.
The tick breaks the grading. Its operator mean is the rank-one democratic matrix, which gives one heavy generation per
sector and, for two sectors reading it, no mixing at leading order. That is the quark sector's leading-order shape, and
the canonical form exists only in T̄ ⊗ T. Its means on the clock's forms give no hierarchy under any tensor. For the leptons
the tick's heavy line cannot be the sole heaviest state. So the principle's own data, read by their means, fix no number.
At most they supply the quarks' leading-order shape under one tensor; the observed mixing still needs a chosen vacuum.

## Instruments

`verification/clock_and_tick.py`; hashes in `ARTIFACT_HASHES.txt`.
