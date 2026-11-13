# SM-C6 E2 (second half) — the three named bits have rank 2 on the record's observables: the hand and the pieces' order

*Step card `relays/cards/SM_C6_E2_the-rank-of-the-three-bits.md`, pushed before the run and before B1915 was read.
GENESIS FK12 (ii). Exact, from B1438's slopes (main at f503b1f38), on 23 levels of LR, LLR and LLLR, both signs, with
the mirror states RRL and RRRL. Data-free. Run: `relays/sm_c6/run_e2.py` → `relays/sm_c6/e2_results.json`; log
`relays/sm_c6/RUN_e2.txt`.*

## The outcome: rank 2, as predicted; the exchange is carried, so B1327's over-count holds

| bit | the state's slopes (i) | the based count (ii) and the class count (iii) |
|---|---|---|
| c, the mirror (the hand) | acts on every chiral level (LLR, LLLR: 14 of 14), as s → −s up to the meridian's shift; trivial on LR, which is its own mirror | never acts (0 of 23 levels) |
| X, the exchange (particle ↔ antiparticle) | does not act (it moves modules, not the state) | never acts (0 of 23): s(χ⁻¹) = s(χ) |
| O, the order of the pieces | does not act | acts on 21 of 23 levels, and always as the swap (n, n*) → (n*, n). The two levels without it (+LLR 1, +LLLR 1) have no module with n ≠ n* |

- **The joint rank is 2.**
  - c and O are independent: c acts on (i) and never on (ii); O acts on (ii) and never on (i).
  - X acts on nothing the slopes build, and duality D = O·X acts as O.
  - So of GENESIS FK12 (ii)'s three named bits, the hand and the pieces' order are independent, and the exchange is
    carried by them.
- **The controls failed as they had to:**
  - **P1:** the reverse in place of the mirror is trivial on the slopes on every level (E1's finding).
  - **P2:** inverting ℓ alone acts on the counts on 21 of 23 levels.

## Against main's B1915 (read after the card was pushed)

- **B1915 counts a different object:** the eight placements (positivity's side, the hand, the line's twin) of the
  golden bundle.
  - Positivity's side adds no bit.
  - Under every map there are two orbits; under the orientation-keeping maps, four.
  - Corrected 2026-11-13: in the whole, the hand is one bit, and the twin is a condition the weight must deliver.
- **Where the two counts meet, they agree.**
  - Both find the hand an independent bit.
  - Both find a named partner not independent: main, the line's twin, which every mirror exchanges (B1914); here, the
    exchange, which duality carries.
- **They differ only in what they count.** The second independent bit here, the pieces' order, lives on modules (the
  based count of E1). B1915's placements do not contain it. Neither count contradicts the other.

## What it does not do

- It does not decide whether the hand and the pieces' order are one register seen twice, or two. That is
  GENESIS FK12 (iii)'s question of a relation (SM-C5's E3), which waits on E6.
- It does not use B1750's convention test (P-374) on the order itself. That stays queued.
