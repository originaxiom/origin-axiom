> **CORRECTED 2026-11-13 (main's own, the same day; see the end):** § 2 called the relation of the tick to "even
> ticks observed" an open question. It was ruled on 2026-11-11 (P-771; GENESIS v1.65). The counts of § 1 stand.

# B1915 — The hand's rows counted: positivity's side adds no bit, and the hand with the line's twin is one bit or two, by the question of the tick (decision 1 of the input budget)

**Verdict: PROVED** (an exact count over integer maps). cc (main), 2026-11-13 (S306p). Main's own code. No data; no value
of the modulus on record is read, and nothing is compared with anything measured. **0 of 19.**

## 1. The answer first

- **The question.** The input budget's decision 1, the hand, was main's grouping of several rows: the orientation (SE2,
  FK2, S02, FL03), positivity's sign (GM5d), the chiral premise (the scale card's), and since B1914 the line's twin. Are
  they one bit? That is a computation, not a merge by reading.
- **Two of the rows are not a "which hand" bit, by their own words.** SE2 takes the orientable member m004 over the
  non-orientable m000: a choice of manifold. The chiral premise is that the scale card takes one block, not both (B1851;
  the scale card's design note of 2026-11-06): a choice of kind. Neither is a placement that a symmetry could move; both
  stay as they are.
- **Positivity, as the foundation now reads it** (GM5d at v1.48, B1662): step and pull-back are mirror images under
  D = diag(1, −1), and positivity is the choice of side: the forward word LR or the backward word D·LR·D = L⁻¹R⁻¹.
  (Main's report to the owner earlier today read GM5d by its v1.14 sentence, the exclusion of −I, and said it looked
  like a separate bit; that sentence holds of the forward semigroup only, and the v1.48 reading is the one in force.)
- **The count.** A placement is (the side, the orientation of that side's bundle, the line's twin on that side's
  eigenline modulo 5): eight placements. A map between bundles is an integer matrix X, determinant ±1, with
  X·A_s·X⁻¹ = A_s′^e; it sends (s, o, v) to (s′, o · det X · e, Xv). With entries up to 9 there are 176 such maps, 88 of
  them between the two sides, D among them.
  - **Under every map the eight placements fall into two orbits: one bit.**
  - **Under the maps that keep the orientation they fall into four**, and each of the four holds one forward and one
    backward placement: the side is always absorbed, and the hand and the twin are two bits.
  - The plant, the orientation read from the determinant alone, gives one orbit: the count depends on the rule.
- **So positivity's side adds no bit to the hand and the twin**: every placement on one side is a placement on the
  other, the orientation kept. And the hand with the line's twin is one bit if the mirror identifies placements, and two
  if only the maps that keep the orientation do.

## 2. Which count applies is one question, and it is already open on the record

- The mirror identifies placements exactly when an odd tick is a move of the whole. The owner has ruled the tick an act
  (P-771), and has asked for the question of how that stands with "even ticks observed" (2026-10-08) to be put again
  after the computation (P-769). Under even ticks only, the moves keep the orientation, and the count is two bits.
- B1913 left condition R6 of the read-out on the whole waiting on the same pair of rulings (the reading of the mark).
  **So the count of decision 1 and R6's remaining choice turn on one question.**
- Main takes the stricter count until that question is settled (P-805): two bits, the hand and the twin, with the side
  absorbed; SE2 and the chiral premise as separate choices of their own kinds. No input leaves the budget by this
  arc, and GM5d's grade in the foundation is not changed here: a grade changes only by the foundation's own adoption.

## 1a. Seen first

`VERDICT topic-sweep /choice of side|step and pull-back|even ticks|the hand.s rows|one bit/: 27 of 1654 arcs on main
match (NEGATIVE 5, OPEN 3, PROVED 19); 9 register rows match (DONE 6, QUEUED 3)`. Read for this arc: GENESIS GM5d and
FK6 (v1.14, v1.42, v1.48), B1662 (the pull-back; positivity the choice of side), B1914 (the twins and the bundle's
symmetries), B1851 and the scale card's design note (the chiral premise), P-769 and P-771 (the tick; even ticks),
B1913 (R6). **Literature:** none beyond B1914's.

## 3. What is not shown

- That the mirror is or is not a move of the whole: that is the open question named in § 2.
- SE2 and the chiral premise are separated from the hand by their own definitions, not by a computation; neither is a
  placement a map can move.
- The search for maps is bounded (entries up to 9); B1914's full search to 12 and its families to 300 found the same
  symmetry classes on one side.

## Files

- `verification/the_hand_rows.py` → `the_hand_rows.json`, `the_hand_rows_run.txt` (seconds).
- The lock: `verification/test_b1915_the_hands_rows.py`.

## Reproduce

```
cd frontier/B1915_the_hands_rows_counted_the_side_adds_no_bit/verification
python3 -B the_hand_rows.py && python3 -m pytest -q .
```

## Dated correction, 2026-11-13 (main's own, found the same day)

§ 2 said which count applies "is already open on the record" (P-769), that the owner had asked for the question to be
put again, and that main counts two bits until it is settled. Main had missed the later ruling of the same day: the owner ruled the relation on 2026-11-11, with B1879's computation in hand (P-771; GENESIS v1.65, GM5c and SE2): every tick is in the ledger, and 'only even ticks are observed' is no longer a ruling but a condition the weight must deliver, a named condition to derive, not counted as derived.
So, with the counts of § 1 unchanged:
- **In the whole every tick is a move,** the mirror identifies placements, and the eight placements are two orbits:
  positivity's side, the hand and the line's twin are **one bit, the hand**, which the tick does not supply (P-771).
- **The second bit** (the twin given the hand, which the orientation-keeping maps leave) is what "only even ticks are
  observed" would give. It is a condition the weight must deliver, typed as the orientation bit is typed, and not
  counted as derived.
- B1913's R6 does not wait on a ruling either (its own dated correction). The two items are still one: both are the
  weight's condition. The words of § 2 are kept as written above.
