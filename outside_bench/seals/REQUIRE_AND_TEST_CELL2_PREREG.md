# PREREGISTRATION — CELL 2: requirement 1 (the gauge algebra), and the price of B1028's UNPRICED row

*Outside bench, 2026-09-14. Written and hashed BEFORE the sweep runs. Gate 5 untouched.*

## R — the requirement, verbatim (`docs/TOE_REQUIREMENTS_LEDGER.md` §A row 1)

> the SM's algebra, matter content, hypercharges, three generations

## P — the predicate

**P_2T = π₁(M) surjects onto 2T = SL(2, 𝔽₃).** This is chain link C6, *"the sole source of the McKay
E₆"* (B266), and `frontier/B282_e6_is_arithmetic_not_geometric/FINDINGS.md` states the stakes:

> The only thing the figure-eight has that nothing else does is that **it is the unique arithmetic
> knot** … If the bridge to physics works, it **must** run through the arithmetic atom.

## T — m004 against P

m004 HAS P. B282: 4₁ → 2, m003 → 2, and 5₂, 6₁, 6₂, 7₄ → 0 (GAP `GQuotients`, counting quotients up
to Aut(SL(2,3))).

## B — WHY THIS CELL EXISTS

**The base rate of P_2T over a census has never been measured.** Six knots is not a census, and
`frontier/B1028_freedom_ledger/ADDENDUM_2026-08-12.md` has carried the consequence since 2026-08-12:

> The row priced the family choice at 0 "because no live alternative family was ever on the table" —
> **a fact about the programme's history, not a measurement of the object.** … a flagged-but-unpriced
> freedom is not a measured zero.

## THE INSTRUMENT, and why it is not the record's

B282's instrument needs Sage + GAP. **Neither is installed in this container** (`which sage sage-python
gap` → empty). Since |SL(2,𝔽₃)| = 24, homomorphism enumeration is direct: assign each generator one of
24 matrices, check every relator, check the image generates. The instrument is validated against B282's
six published knots **before** any census manifold is touched, and the ÷|Aut(SL(2,3))| = ÷24 factor
relating a raw surjection count to `GQuotients` is asserted as a control, not assumed.

**Declared:** at the time of sealing, the enumeration has been run on B282's six knots only — values
already banked, so no information about the census has been obtained. Nothing else has been computed.

## THE SWEEP

`snappy.OrientableCuspedCensus`, one-cusped members, in census order, population **N = 5000**, fixed
now. For each: the 2-or-more-generator presentation from `fundamental_group()`, then the enumeration.
The population, not the hit count, is printed first.

## THE TWO OUTCOMES

- **OUTCOME A — the door is RARE** (P_2T holds for < 1 % of the population): requirement 1 does real
  selecting work, and the family row's price is genuinely low — **measured**, not assumed.
- **OUTCOME B — the door is COMMON** (≥ 1 %): B282's genericity collapse extends from the character
  variety to the McKay door itself, and C6 selects far less than the chain reads it as selecting.

## THE CONFOUND, AND ITS PREREGISTERED DISCRIMINATOR

If P_2T merely tracks arithmeticity then, by Reid's theorem (m004 is the unique arithmetic **knot**
complement), a tiny rate **re-measures Reid** rather than pricing the family choice. So the cell
compares two populations:

| predicate | base rate | source |
|---|---|---|
| **P_arith** — shape field is ℚ(√−3) | **112 / 212 641 = 0.053 %** | already banked: `frontier/B1186_family_is_112/verification/family_census.json` (`census_size = 212641`, `B_shape_field_in_Qsqrt3 = 112`), computed with a double-precision filter and an mpmath confirm — no Sage |
| **P_2T** | to be measured | this cell |

- **D = SAME** — the 2T population is (within the swept range) the ℚ(√−3) population. **P_2T is
  arithmeticity restated**; the cell has re-measured Reid and says so plainly, and the family row stays
  unpriced by this route.
- **D = DIFFERENT** — the populations diverge in either direction. P_2T is its own predicate and the
  difference is the finding.

The comparison is made on the swept range only; B1186's 112 are identified by name, and the overlap is
reported as a count of the swept population, never extrapolated to the full 212 641.

## CONTROLS

| # | control | catches |
|---|---|---|
| K1 | the enumeration reproduces B282 on all six knots — **the four zeros as load-bearing as the two hits** | an instrument that says yes to everything, or no to everything |
| K2 | raw count ÷ 24 equals B282's `GQuotients` value on the two hits | a miscounted automorphism factor |
| K3 | a positive control: some census manifold OTHER than m004/m003 must be found with P_2T, or the absence is reported as a possible instrument failure, not as a finding | the null that is really a broken instrument (#164) |
| K4 | population size asserted > 0 and printed before any rate | the B1197 vacuity trap |
| K5 | generator count per manifold recorded; if any presentation has > 4 generators the enumeration is skipped and **counted as skipped**, never as a zero | silent undercount masquerading as rarity |

## WHAT THIS CELL MAY NOT CONCLUDE

Nothing about E₆ beyond the 2T door: `frontier/B1258_2T_is_blind` proves the 27|2T branching character
is identical for both candidate embeddings, so the branching cannot discriminate objects and is not
invoked. No value. No claim that a rare door proves the object was correctly chosen — only that the
requirement does selecting work, which is the narrower thing measured.
