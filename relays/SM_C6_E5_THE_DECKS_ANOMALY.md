# SM-C6 E5 part 1 — the deck's ℤ/3 anomaly on s961 vanishes: no anomaly forbids gauging the deck

*Step card `relays/cards/SM_C6_E5_the-decks-anomaly-on-s961.md`, pushed before the run. GENESIS FK7. It reads B1432's
census of s961 from main at f503b1f38. Data-free. Run: `relays/sm_c6/run_e5.py` → `relays/sm_c6/e5_results.json`.*

## The outcome: as predicted, every robust coefficient is zero mod 3

- **What the deck acts on.** On s961 the 48 generation backgrounds form 16 free orbits of three under the root's deck
  ℤ/3 (8 of each sign). Each orbit has one index vector, ±1 in all six sectors (B1432). So the deck acts on an orbit's
  content as the regular representation: charges 0, 1 and 2, each carrying one generation.
- **Per orbit,** with the chosen dictionary:

  | coefficient | value | mod 3 |
  |---|---|---|
  | ℤ₃–SU(3)² | 6 | 0 |
  | ℤ₃–SU(2)² | 6 | 0 |
  | ℤ₃–gravity² | 48 | 0 |
  | ℤ₃³ | 144 | 0 |
  | ℤ₃–U(1)_Y² (information only; not a robust condition) | 10 | 1 per orbit, 0 over the 16 orbits |

- **Why, in one line.** Every coefficient carries the factor Σq = 0 + 1 + 2 = 3, or Σq³ = 9, because the orbits
  are free.
  B1506's T5, that no firing background is fixed by the whole deck, is what makes them free.
- **The controls failed as they had to:** P1, the charges (0, 0, 1), and P2, a planted fixed background with charge 1,
  both give non-zero coefficients.

## What it means for GENESIS FK7

- **No anomaly forbids gauging the deck on this spectrum.** Its two readings, one background (gauged) or three
  (kept), are both consistent so far.
- **GENESIS FK7 now waits on part 2:** whether the minimum of an action breaks the deck. That needs an action verified
  on main (WP-2.1).
- **The dictionary is chosen, not derived:** the sectors' Standard-Model representations, and three members read as
  three generations.
