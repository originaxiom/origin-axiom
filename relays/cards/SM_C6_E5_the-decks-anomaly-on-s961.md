# SM-C6 E5 part 1 — the deck's ℤ/3 anomaly on s961, the cover that carries the triplet

*Step card of SM-C6 (main's M13, M14, M18; SM-C5's entry E5 for GENESIS FK7). Pushed before the run. Data-free.*

## What is computed

- **The record's data** (B1432's census on main, census_M1_M5.json, level M3 = s961):
  - 48 generation backgrounds, in 16 orbits of three under the root's deck ℤ/3;
  - every orbit is closed, and the index is deck-invariant, so each orbit has one index vector;
  - every count is ±1, in all six sectors (Q, u^c, e^c, d^c, L, ν^c), with one sign per background.
- **The dictionary, which is chosen and not derived:**
  - the sectors carry their Standard-Model representations (Q (3, 2), u^c (3̄, 1), e^c (1, 1), d^c (3̄, 1), L (1, 2),
    ν^c (1, 1));
  - in the kept reading, an orbit's three members are three generations, which the deck permutes.
- **The charges.** A free orbit of three is the regular representation of ℤ/3. In the deck's eigenbasis the charges
  are q = 0, 1 and 2, each carrying one member's content.
- **The anomaly coefficients, per orbit and in total, mod 3:**
  - ℤ₃–SU(3)²: Σ q·T(R)·n;
  - ℤ₃–SU(2)²: Σ q·T(R)·n;
  - ℤ₃–gravity²: Σ q·dim·n;
  - ℤ₃³: Σ q³·dim·n.
  - ℤ₃–U(1)_Y² is computed for information only. It is not a robust condition, because of U(1) normalisation.

## The prediction, and the outcomes

- **Predicted:** every robust coefficient is 0 mod 3, on every orbit, because Σq = 3 and Σq³ = 9. Then gauging the
  deck is not forbidden by an anomaly, and GENESIS FK7 waits for part 2 (the minimum of an action).
- **Outcome "anomalous":** some robust coefficient is non-zero. The deck cannot be gauged on this spectrum: it is
  kept, or broken, and the count three stands.

## Controls, which must fail

- **P1:** the charges (0, 0, 1) in place of the regular (0, 1, 2). Some coefficient must be non-zero.
- **P2:** a planted fixed background, an orbit of size one with charge 1. Some coefficient must be non-zero.
