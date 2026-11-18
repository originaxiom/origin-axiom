# SM-C22 — every Higgs vector in frame D1: none gives both an aligned cusp mixing and a hierarchy, and none makes the frame single-valued

*The SM seat, 2026-11-18. Card `relays/cards/SM_C22_every-higgs-vector-in-d1.md`, sealed and pushed before the run.
Main's closed form and gate-5 contraction imported unchanged. Frame-internal structure only. Nothing is set beside a
measured number, and no vector is offered as the Higgs.*

## The answer

- **T1, derived and checked: no Higgs vector makes D1 single-valued in the point.**
  - Moving w acts on the Higgs index as −Z³ and X³, which anticommute exactly (‖Z³X³ + X³Z³‖ = 0).
  - So no vector is an eigenvector of both, and the best of 2 000 random vectors still has a phase defect of 0.57.
- **S1: no vector in the scan has both** a top-aligned cusp mixing at half or more of the 24 points and a median
  exponent E(s₃/s₁) ≥ 0.1. The scan covered 5 021 vectors: single modes, U_M's eigenvectors, pair sums and differences,
  and 5 000 random vectors.
- **Where each property lives:**
  - **The hierarchy lives only on vectors concentrated on one or two modes.**
    - Single modes: median E(s₃/s₁) 0.93 to 1.07, with rational-looking exponents at the mark: (8/15, 4/5) or
      (2/15, 6/5), since 0.533, 0.8, 0.133 and 1.2 to three digits.
    - Pairs e_k ± e_(k+3): 0.233, with (1/10, 7/30) at the mark.
    - Their top alignment is at most 0.38.
  - **Generic vectors have no hierarchy:** the largest median E over 5 000 random vectors is 6.7e-5.
  - **The best-aligned vectors have no hierarchy.** The largest top-aligned share in the scan is 0.58: the random
    maximum, and also U_M's eigenvector at −π/3. Among random vectors with a share ≥ 0.5, the largest median E is
    −1.6e-4.
- **So in frame D1 the two properties are on opposite sides:** hierarchy needs the vector to avoid the unsuppressed
  modes, and alignment needs it to spread.

## The results against the sealed expectations

| | expectation (prior) | result |
|---|---|---|
| T1 | Z³ and X³ anticommute; no v makes M single-valued (95%) | **holds:** exactly 0, and the least defect is 0.57 |
| S1 | no vector has both (70%) | **holds:** 0 of 5 021 |
| S2 | hierarchy only for concentrated vectors, whose mixing is near a permutation (60%) | **half holds.** The hierarchy appears only on single modes and pairs. Their mixing is not shown to be near a permutation here: the card measured top alignment (≤ 0.38) and not the full permutation class. Single modes are permutations by B1957 |

## A reading, labelled as such

- High in the cusp, a coupling's leading behaviour is set by the least-suppressed Higgs mode in the vector's support.
  Any vector with weight on every mode inherits an unsuppressed component, and its exponents go to 0.
- A hierarchy therefore needs a vector supported on few modes. There the monomial structure of the overlap (B1957:
  one mode gives one entry per row) keeps the mixing from aligning.
- This explains the scan. It is not a proof over all vectors, and the scan is a sample, not a theorem.

## What it means

- **Frame D1 is closed at the cusp:**
  - for every Higgs vector in the scan, which together with the reading covers all of them, structurally;
  - not only at its tick-fixed vacuum (SM-C21);
  - and no choice makes it single-valued (T1).
- **The chain SM-C18 to SM-C22, in one line:** D1 is covariant on a double cover, its Higgs bit is the tick, and it
  cannot hold a cusp hierarchy with aligned mixing for any Higgs vector.
- **What this leaves for the programme:** frame C's cusp hierarchy (B1945) comes with a reading choice, and D1 removes
  the choice and loses the hierarchy. A frame that keeps both would need a different construction, not a different
  Higgs vector. That is main's question; no lead is claimed here.

## Files

`relays/sm_c22/run_c22.py`, `relays/sm_c22/c22_results.json`, `relays/sm_c22/RUN.txt`.
