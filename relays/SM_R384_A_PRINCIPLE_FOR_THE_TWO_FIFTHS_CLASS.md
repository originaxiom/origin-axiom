# SM-R384 — the class (2/5, odd/10) is one cusp; its offset is forced, and α = 2/5 over 1/5 is one Galois bit, CHOSEN

*The SM seat, 2026-11-26, for register row P-384 (main's M53). The card is
`relays/cards/SM_R384_a-principle-for-the-two-fifths-class.md`. It was committed with its script before the run, in
8a6f01fd6. The script is `relays/sm_r384/run.py`, SHA-256 d0c30fbf62479829, run once on the real case. Its output is
`relays/sm_r384/r384_run.txt` (SHA-256 3d8f8467b690ba26), with `relays/sm_r384/r384_results.json`
(SHA-256 f1b967c9f2134787). Data-free: an exact enumeration of lines; no measured number is read. No post hoc script.*

## Result against the sealed expectations

| | expectation (prior) | outcome |
|---|---|---|
| E0 | 266 lines; 12 of order 5, 36 of order 10; K and both carriers inside (95%) | **holds** |
| E1 | PLANT "divisible by 5" selects 48 ⊃ K; "divisible by 2" ⊃ K; neither exact (97%) | **holds**: 48 and 129 lines |
| E2 | the act's line: 8 lines (2 of order 5, 6 of order 10), one of K, (2/5, 3/10), no carrier (85%) | **holds** |
| E3 | ±mark: none of K; ±2·mark: one of K, (2/5, 3/10) (85%) | **holds** |
| E4 | K not unit-invariant; its unit closure is K ∪ (1/5, odd/10), 10 lines (90%) | **holds** |
| E5 | every rule without the sign or a named point is unit-invariant and not exactly K (90%) | **holds**: all 11 such |
| E6 | order 10 has 8 cusps; K is exactly one; 4 see the 5-part (85%) | **holds**: sizes 1, 1, 10, 5, 10, 5, 2, 2 |
| E7 | the least multiple of 5 at which B1934's lepton copy breaks is 10 (97%) | **holds** (copy only at 5) |
| E8 | Π exactly K; Π_inv 10 lines; the h = 1 plant gives the twin, none of K (90%) | **holds** |
| E9 | the unit twist at order 15 selects ±{1/15, 2/5, 11/15} (85%) | **holds** (printed as 1/15, 4/15, 2/5) |
| E10 | χ(5a₅) = −1 at order 10 selects the slopes ±1/10 and ±2/5, two cusps (80%) | **holds** |

All eleven held. The control behaved as designed: the bare description "order 10, a = ±2/5" selects exactly K, as Π
does. Selecting exactly K therefore shows nothing about whether a rule is a principle. That is decided by the sources
the card sealed (§ 2 there).

## The sealed decision rule, applied

E4, E5 and E8 hold, so the first branch applies.

- **b odd/10 is not an independent choice.** Given a = 2/5 and order 10, it is forced. The five lines of K are one
  ⟨T, −I⟩-orbit, one of the 8 cusps of the order-10 lines.
- **Order 10 has a candidate principle in B1934's terms:** the least level containing 5 at which the lepton–down copy
  breaks. It rests on a minimality postulate that is not derived. Nothing here says why the second prime is 2 rather
  than 3.
- **α = 2/5 over α = 1/5 is one Galois bit, declared an observer choice (CHOSEN, one bit).**
  - Every rule built from the order, the act's line (B1943), the cusp's view of the 5-part (SM-C24), the least level or
    the Galois-invariant twist is invariant under scaling by units. Each such rule selects K together with its twin
    (1/5, odd/10), or neither.
  - Only a non-invariant clause separates them: the unit twist 3a = ±1/5, equivalently the golden character's sign.
    No object on record fixes that sign. B1934's two Weil representations and B1923's twin exchange it.
  - The one discriminator on record, ‖3α‖ = 1/5, was read from data (B1786).
- **The act's line does not answer P-384** (the second branch did not occur). It holds one line of K, (2/5, 3/10), and
  neither carrier.

## Reading

- **P-384's open content is now smaller and named:**
  1. one bit, the square class of the Higgs's twist: CHOSEN;
  2. the minimality behind order 10: a postulate;
  3. which of K's five offsets carries.
- **The third item is an inference, for frame C only.** By SM-C23 the five offsets are one cusp read at τ, τ + 1, …,
  τ + 4, so item 3 becomes a condition on Re τ mod 5. This is consistent with W163. It does not carry over to B1753's
  instrument (B1741's) until that instrument's joint covariance is shown.
- **Post hoc, against the record and not a test.** The unit twist alone selects only the slope 2/5 at orders 20 and 25.
  At orders 15 and 30 it also selects 1/15 and 4/15, slopes that B1755 (at 15) and B1786 (at 30) found carry nothing.
  So the twist is not a cross-order rule, as the record already said. Π avoids this only by its minimality clause.

## Not checked

- No rate or row of any frame is computed, and no cusp is read.
- Joint covariance of B1741's instrument.
- A derivation of the minimality, or of the sign.
- No value of the 19 is computed or compared.
