# W15 — a prediction, recorded before the test

The SM-derivation seat, 2026-10-07, late. Committed before the runs it predicts. Nothing here is a result.

## What was seen before this was written

- **The weave's own extensions.** X = [[A, c B_p], [0, B_p]]: a parity line B_p extended by a twisted spin doublet A along
  a weave class c. Its class index is [c ∪ ℓ_p ≠ 0] (the B1297 identity, on the page of the weave dossier's W15).
  - At tick 3 it is +1 on every reading of ten odd-trace threads to length 6.
  - It is 0 on every reading of ±LLRLRR (traces ±15), at three primes.
  - In a partial run at length 8, it fired on ±LLLLLLLR (±9), ±LLLLLRLR (±19), −LLLLRLRR and −LLLLRRLR (−25), and was
    0 on ±LLLLLRRR (±17).
- **F-CI** at tick 3 (W14): generation-shaped backgrounds on the same ten threads to length 6, none on ±LLRLRR. It has not
  been run at length 8.

## The hypothesis

**H2: a thread is silent, in both instruments, exactly when its trace t satisfies t ≡ ±1 (mod 16)**, equivalently
t² ≡ 1 (mod 32). This fits every reading above: the silent traces are ±15 and ±17, and the firing ones 3, 5, 7, 9, 11,
13, 19 and 25 (up to sign).

## The predictions (the test is the next run; the trial budget is the states named)

1. **The weave's extensions, the rest of length 8.** ±LLLLRLRR and ±LLLLRRLR (±25), ±LLLRLLRR and ±LLLRRLLR (±29),
   ±LLLRLRRR (±27), ±LLRLLRLR (±37) and ±LLRLRLRR (±39) fire: index +1 on every reading. None of these traces is
   ±1 mod 16.
2. **F-CI at tick 3 on ±LLLLLRRR (±17): no generation-shaped background on either state.** The control, ±LLLLLLLR (±9),
   carries some. The instrument is the weave dossier's slope-law census, run unchanged.

**What each outcome would mean.**
- **If (2) holds,** the two instruments share their silent threads on fourteen of fourteen states, and H2 is the leading
  candidate for the common cause.
- **If F-CI carries on ±LLLLLRRR,** the shared silence on ±LLRLRR was a coincidence, and H2 describes the weave's
  extensions alone.
- **If any state in (1) is silent,** H2 is false as stated.

Either way the result is a thread criterion, not a weave law of content.
