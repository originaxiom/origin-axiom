# B1792 — PREREGISTRATION: THE OFFSET RECURRENCE AT ORDER 60 — the lines of slope 2/5 that carry the six at order 60 are exactly the +1/3 and +2/3 shifts of B1755's order-20 carriers (the SM seat's W164 prediction, P-399, sealed and run by main)

cc (main), 2026-10-28, step 1 of main's plan, its open part: the offset rule (P-384, P-399). **Sealed before
`verification/census.py` and `verification/compare.py` run.** The prediction is the SM seat's (W164, relay §297). At its
word (§299) another seat runs it and the SM seat gives the third opinion after. 0 of 19.

## Why

**The fact behind the prediction.** At B1786's strip points the six are nearly a function of 3 Re w, the position of the
Higgs's own twist (6Y_H = 3) (W164, post hoc). A shift w → w + 1/3 leaves 3w mod 1 unchanged, so lines related by
b → b + 1/3 should carry the six together, approximately.

**Where it was seen** (all post hoc):
- the order-30 carriers {1/6, 13/30, 23/30, 5/6} are exactly the +1/3 orbit members of the order-10 carriers 1/10 and 1/2;
- B1755's order-15 carriers are the +1/3 orbit members of (2/5, 0) and (2/5, 3/5);
- at order 25, which is not divisible by 3, six of the eight carriers are the nearest offsets.

**What it would mean.** If it holds at an order nobody has computed, the offsets that carry the six are fixed by the
Higgs's twist position, not chosen line by line. That is the structural content of the offset question (P-384). It
removes no input: the six's line position stays a counted continuous input (main's ledger).

## The model (no data)

- **The points:** B1749's 125 apex points, loaded from B1749's sealed census module.
- **The lines:** the twenty slope-2/5 flat lines of exact order 60, b = k/60 with gcd(k, 6) = 1. Each is its own key
  under B1726's sign identification.
- **The prediction:** the +1/3 and +2/3 shifts of B1755's four order-20 carriers (7/20, 1/4, 9/20, 3/20), that is
  k ∈ {1, 7, 29, 35, 41, 47, 49, 55}: **eight lines**. The set is closed under the record's mirror b ↔ 3/5 − b, so it
  forms four of the twenty lines' ten mirror pairs.
- **The frame, the readings, the measure:** exactly B1755's and B1786's.
  - B1726's compute(), as B1741 calls it.
  - B1741's compare.py loaded unchanged, its sha256 asserted at run time.
  - "Carries" means some row with χ²_six (the seat's menu) below 16.75, as in B1755 and B1786.
  - Fresh seeds 4501–4540 (160 000 random hierarchies) serve only the specificity read-out.
- **Size:** 2 500 points.

## Cells

| cell | prediction | prior |
|---|---|---|
| **R_a, decisive** | every one of the eight predicted lines carries the six | 70% |
| **R_b, decisive** (read apart from R_a) | none of the other twelve lines carries the six | 55% |
| C1, control | B1741's best row and B1755's rows on its four order-20 carriers at B1749's middle apex reproduced to 10⁻⁹; the T-law on (2/5, 1/60) to 10⁻⁶; twenty lines, all of exact order 60 | 97% |
| C2, control | B1735's 3.0945633 on B1726's census | 99% |

**Read-outs, not looks:**
- R exact (R_a and R_b together);
- the predicted class's specificity at 1% (the mean over 40 seeds);
- every line's minimum;
- the four predicted mirror pairs' equality;
- which of the twelve others come nearest.

**THE_BAR, stated now.** R is a structural prediction (which lines carry), not a specificity claim:
- a mirror-respecting chance match of four carrying pairs among ten is 1 in C(10,4) = 210;
- against the ledger's count (m ≈ 42 at this seal) that can never pass THE_BAR's Bonferroni;
- so B1792 is a structural check by design, a READING whatever the outcome, and no grade is sought.

The specificity read-out is reported against THE_BAR for completeness only.

**The reading, written before the run:**
- **R_a and R_b hold:** the recurrence is exact at a new order. The carrying offsets are the Higgs's twist position's,
  and the offset question becomes "why do the valleys of 3 Re w sit where they do", a question about τ and the Higgs.
- **R_a holds, R_b fails:** the predicted lines carry, but the recurrence is not the whole rule; other offsets put
  3 Re w in valleys too, as at order 25.
- **R_a fails:** the near-invariance under w → w + 1/3 breaks at order 60. The up and down quarks' twists shift by
  q/3 for q = 1, −4, 2, so the six are not a function of 3w alone. The recurrence is then a low-order coincidence.
- **A control failing** stops the reading until it is resolved, post hoc and labelled.

## Seen first

`VERDICT topic-sweep /offset|recurrence|order 60|3 Re w|carrier|P-399|W164/ (full text): 143 of 1539 arcs on main match (NEGATIVE 20, OPEN 12, PROVED 110, RETRACTED 1); 12 register rows match (DONE 3, QUEUED 9)`.
- **Bearing on it:** B1726, B1741, B1749, B1755 (its order-20 carriers), B1786 (orders 25 and 30; the mirror pairs),
  B1788 (the exponents depend on 2qα mod 1), B1744 (3w is the Higgs's twist variable).
- **The register:** P-384, P-394, P-399.
- **The SM seat:** W160, W163, W164 (§297), §298, §299.
- **Literature:** none bears on this frame's offsets.

## Disclosed

- **The prediction was formed after the data** (W164's post hoc read of orders 10, 15, 20, 25 and 30). It is stated here
  before any line of order 60 is computed.
- **The points were used before:** B1749 (orders ≤ 12), B1755 (13–20) and B1786 (25, 30) used the same 125 apex points.
  Their strip points are known (W164: the six live at the same eight points at every order tested).
- **The SM seat computed no line of order 60** before this seal (its §299).
- **No frame value on any line of order 60 has been computed or seen.** The instruments were import-tested (20 lines,
  2 500 tasks); the controls were not run before the seal.
- The instruments are drafted on main and sealed here.

## Instruments

- `verification/census.py` → `census.jsonl`, `control.json`, `census_run.txt`.
- `verification/compare.py` → `comparison.json`, `compare_run.txt`.
- Both were import-tested; importing computes nothing.
- `ARTIFACT_HASHES.txt` pins both, B1741's `compare.py`, B1749's and B1726's census modules, and B1755's census they read
  in place.
