# N3 ON THE WEAVE — every Sturmian wording's clock and tick on the triplet (DRAFT preregistration, not sealed)

P-200 (the owner's question, 2026-10-20). The seats were asked for hostile reads by relay; this draft goes to them
before the seal.

## 0. Seen first (to be run at the seal)

`topic_sweep.py "clock|tick|Sturmian|substitution|democratic|fixed.point word"` — expected hits: B1607 (the principle's
tick at the common point), B1621 (the clock and tick of the golden rule), B1633 (the averaged word coupling), B1323
(the Sturmian morphisms abelianise onto exactly the non-negative GL(2, ℤ) matrices; C2a/C2b). Literature: Sturmian
morphisms are the positive automorphisms of F₂ (Mignosi–Séébold 1993; Wen–Wen 1994); flavour democracy (Harari–Haut–
Weyers 1978).

## 0b. Disclosed (seen before the seal)

- B1621's run (LR's tick: eigenvalues {1, ω, ω²}, mean rank one and democratic).
- A smoke test, 2026-10-20 (`before_the_seal/smoke.py`, `smoke_run.txt`): with the instrument's `T_of` on composed
  automorphisms, LR's tick mean is rank one and LLLR's is zero. **That lift is not multiplicative** (it picks a lift of
  each automorphism; Gate 12's conflicts), so this design fixes the lift as the product of the letters' lifts.
- The structural argument below, worked out before any census.

## 1. The objects

- **The wordings.** Every primitive positive word w in {L, R} with both letters, up to cyclic rotation, of length at
  most 12 (the record's 379 cyclic positive words). Each is a positive automorphism σ_w of F₂ (L: a ↦ a, b ↦ ab;
  R: a ↦ ab, b ↦ b), a Sturmian morphism.
- **The lift.** T(w) = the product of T(L) and T(R) along w, with T(L), T(R) the record's lifts of the moves on the
  triplet T (B1600, B1621's `T_of` on the single letters). This is a representation of the braid group ⟨L, R⟩, so a
  word's tick is well defined.
- **The clock of w.** The parity class (A_n, B_n) mod 2 of the prefixes of σ_w's fixed-point word (iterate σ_w on a;
  σ_w(a) begins with a), acting on T as diag(χ_p) (B1621 K1).
- **The tick of w.** T(w). Its operator mean is M(w) = lim (1/N) Σ_{n<N} T(w)ⁿ.

## 2. The structural argument (stated before the census)

For odd trace, w acts on the parity lines as a 3-cycle (the paper's Lemma 4), so T(w) is a phase times a signed
permutation matrix of a 3-cycle. Its eigenvalues are the three cube roots of det T(w). So M(w) ≠ 0 exactly when
det T(w) = 1, and then M(w) is the rank-one projector on the eigenvalue-1 line. With the multiplicative lift,
det T(w) = (det T(L))^{#L} (det T(R))^{#R}.

## 3. Predictions (to be sealed with thresholds)

- **Q1, the clock (every wording).** For every w, the clock's matrices along σ_w's fixed point (to N = 10⁵) span the
  diagonal algebra, and the clock's mean on T is below 10⁻² in every line.
- **Q2, the tick's mean.** For every odd-trace w, M(w) is rank one if det T(w) = 1 and zero otherwise, with the
  determinant as computed from the letters. The rank-one case occurs on a proper subset of the odd-trace words, and
  LR is in it. **A failure of either is a finding against §2.**
- **Q3, the lines.** Every rank-one M(w) is trimaximal (each entry of modulus ⅓). At least two distinct lines occur, so
  LR's democratic line is not the only one.
- **Q4, the interaction.** The average of M(w) over the odd-trace w of each length from 6 to 12 commutes with the clock
  to within 10% of its largest entry (the weave's tick mean keeps the grading), unlike LR's alone.
- **Controls.** LR reproduces B1621 (positive control). The golden rule σ = LP (det −1), whose square is LR, is
  recorded but outside the population.

## 4. What would change the paper

If Q2–Q4 hold, N3's tick statement is a statement about LR's class only: the democratic matrix is not the principle's,
and the weave's tick mean keeps the grading. If Q4 fails, the weave's ticks break the grading in a direction to be
named. Either way, N3's "fix no number" is re-tested on the weave.
