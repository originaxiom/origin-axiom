# B1633 — THE WEAVE'S WORD COUPLING: a thread's own H¹ reads the rule's word and breaks the parity grading, but averaged over all threads with the weave's uniform measure it is a scalar on the three generations, up to corrections exponentially small in the thread length — the weave restores the full symmetry; the word reaches masses and mixing only through a choice of thread

> *Audited 2026-10-15 by main (P-152, B1655): the computation HOLDS; the closing sentence is wider than computed. The grades, the corrected wording and the checks are in `frontier/B1655_main_audits_its_negatives/FINDINGS.md`.*

**Verdict: PROVED** (W1–W4 hold). cc (main), 2026-10-09. Sealed `a15da3840` before the run. No data; the owner's "resume all"
(the outline's 2c). **0 of 19.**

## 0. Seen first

As sealed: `VERDICT topic-sweep /word.reading|thread's own H|zero.mode projector|equidistribut|random walk on G/: 0 of 1404 arcs on main match (none)`
— the SM seat's W42, B1620, B1621, B1629. **Literature:** random walks on finite groups (Diaconis); Schur's lemma.

## 1. The computation (`weave_word_coupling.py`, sealed, unchanged; exact counts over G, order 96)

| | sealed prediction | prior | result |
|---|---|---|---|
| **W1** | the lifts fill a coset and equidistribute geometrically | 85% | **HOLDS** — the lifts of length-n words fill one of two cosets of an index-2 subgroup (48 elements each; odd and even n alternate). Their distance from uniform falls from 0.23 at n = 8 to 2.8 × 10⁻³ at n = 38 |
| **W2** | the averaged coupling tends to a scalar geometrically | 85% | **HOLDS** — the distance from a scalar is 0.236 at n = 2, 3.5 × 10⁻³ at n = 14 and 3.9 × 10⁻⁶ at n = 38 (geometric, about 0.6 per two steps, oscillating) |
| **W3** | each coset's limit commutes with all of G | 90% | **HOLDS** — both limits are scalars. Odd lengths have trace 0 (no zero modes at all, as the seat's W42 found); even lengths have a mean zero-mode dimension of 5/12 |
| **W4** | the zero-mode fraction tends to a constant between ¼ and ½ | 60% | **HOLDS** — 0.3125 (to 0.312 at n = 38). The seat's primitive census gives 237/745 ≈ 0.32 to length 12 |

> *Corrected 2026-10-29 (P-483; recounted on main, `verification/p483_recount/`): W4's comparison set two different quantities
> side by side. W4 is a per-length fraction over all words, with the record's single lift, at even n (odd lengths carry no
> zero modes). The seat's 237 of 745 is a census of primitive threads over lengths 2–12, counting a thread when either sign
> extension ±g of its lift has a fixed vector (its W42, Part B). Counted one per thread with this arc's single lift, the census
> gives 157 of 745 (0.211; 157 of the 477 even-length threads, 0.329); with either extension it gives exactly 237. W4's
> verdict (the per-length fraction tends to a constant in [¼, ½]) is unaffected.*

## 2. What it says

- **One thread reads the rule's word.** Its own H¹ breaks the parity grading (democratically, by the seat's W42).
- **The weave, reading all its threads equally, restores the full symmetry.** The averaged coupling commutes with the
  whole group, so by Schur it is a scalar on the three generations, and the corrections fall off geometrically with the
  thread length.
- **So the word reaches the masses and the mixing only through a choice of thread**, and a choice of thread is a
  selection. The weave's own measure gives no non-permutation mixing.
- This closes the outline's 2c as a weave-level negative. With B1620 (couplings in τ alone), B1621 (the clock and the
  tick), B1629 (the cusp) and B1630 (the tick's point), every datum the principle forces has been read for the flavour
  values. None fixes one: the values need a selection or a dynamics. 0 of 19.

## 3. Disclosed

- All words were counted, not only primitive cyclic ones (as sealed).
- Read back before the seal: the identity's index found rather than assumed; an unused stub removed.

## 4. Files

`verification/weave_word_coupling.py` (sealed, unchanged), `weave_word_coupling.json`, `word_run.txt`. Test:
`tests/test_b1633_the_weaves_word_coupling.py`.

## Seen late (2026-10-21, Review 66; P-123)

> *Seen late.* This arc's sweep, in its own words, missed older arcs on its subject (vocabulary drift; the topic sweep now expands aliases, R65-6). B415 (PROVED): the tower measure's continuum limit, a Gauss-sum-modulated Haar measure on ℤ₃ × ℤ/5 — the record's earlier measure over its threads.
> Whether B415's measure is this arc's uniform measure over threads is not checked here; no cell changes.

## Addendum (2026-10-21, Review 66; P-124, the reliance census)

> *Tagged 2026-10-21.* Review 66's reliance census found this arc relying on seat results that are not verified on main, and its `rests_on_seat` field does not declare them, so the gate seat-positive-verified could not see them. W42 (row 1058, read, its thread-H¹ census registered) is the premise of "only through a choice of thread". They are the seat's, unverified (harvest rows named); the verifications are queued by consequence (P-229). The cells and numbers are unchanged.
