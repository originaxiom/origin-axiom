# B1633 — PREREGISTRATION: THE WEAVE'S WORD COUPLING — the coupling that reads the rule's word (a thread's own H¹), averaged over all threads with the weave's uniform measure

cc (main), 2026-10-09, after S110, on the owner's "resume all" (the outline's 2c). **Sealed before
`weave_word_coupling.py` runs.** No data. 0 of 19.

**Why it matters.** B1620 showed that couplings in τ alone keep the parity grading, so their mixing is a permutation.
The SM seat's W42 found a coupling that reads the rule's word and breaks the grading: a thread's own H¹, whose T part is
the fixed space of the thread's monodromy on T. But it breaks it only democratically, and it is a thread result: a sector
that reads one thread is a choice. The weave-level question is what the coupling reads once it is averaged over every
thread with the weave's own measure, choosing none.

## Seen first

`VERDICT topic-sweep /word.reading|thread's own H|zero.mode projector|equidistribut|random walk on G/: 0 of 1404 arcs on main match (none)` — the SM seat's W42 (the threads' H¹ census, 237 of 745 with zero modes to length 12; the projectors spanned by
parity lines or body diagonals), B1620, B1621 (the tick's operator mean is the zero-mode projector of LR's mapping
torus, by W42), B1629 (the uniform measure on threads). **Literature:** random walks on finite groups (equidistribution
on a coset of the subgroup the steps generate; Diaconis); Schur's lemma.

## Disclosed

- The outcome is expected on general grounds. The uniform measure on words in L and R drives the lifts to the uniform
  distribution on a coset, and the average of fixed-space projectors over a conjugation-invariant set commutes with G,
  so by Schur it is a scalar on T. The arc computes the rate and what survives at finite length.
- All words of length n are counted, not only primitive cyclic ones; the difference is O(2^{n/2}). The seat's census
  counts primitive threads, so W4's fractions are compared with it loosely.
- Read back before the seal: the identity's index is now found rather than assumed, and an unused stub that claimed a
  parity-grading check was removed.

## Cells, predictions, priors

| | prediction | prior |
|---|---|---|
| **W1** | the lifts of words of length n fill a coset (support size constant on each parity of n), and their distance from uniform on it falls geometrically with n | 85% |
| **W2** | the averaged coupling's distance from a scalar falls geometrically with n | 85% |
| **W3** | on each coset the limit is a scalar on T (commutes with all of G) | 90% |
| **W4** | the fraction of words whose lift has zero modes tends to a constant between ¼ and ½ (the seat's 237/745 ≈ 0.32 at length 12 is close) | 60% |

**The reading, written before the run (the cells can only lower it).** A single thread reads the word and breaks the
parity grading, democratically. **The weave, reading all of its threads equally, restores the full symmetry:** the
averaged coupling is a scalar on the three generations up to corrections exponentially small in the thread length. So the
word reaches the masses and mixing only through a choice of thread, which is a selection. The weave's own measure gives
no non-permutation mixing, and 2c closes as a weave-level negative.

## Instruments

`verification/weave_word_coupling.py`; hashes in `ARTIFACT_HASHES.txt`.
