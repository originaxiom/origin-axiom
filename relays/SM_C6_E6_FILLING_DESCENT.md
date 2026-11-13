# SM-C6 E6 steps 1 and 2 — the record's modules descend to Dehn fillings, and after filling they count both orders

*Step card `relays/cards/SM_C6_E6_filling-descent-and-count.md`, pushed before the run. GENESIS FK8. It uses B1434's
level presentation and B1438's exact slopes from main at f503b1f38, with Fox calculus in double precision. Data-free.
Run: `relays/sm_c6/run_e6.py` → `relays/sm_c6/e6_results.json`; log `relays/sm_c6/RUN_e6.txt`.*

## Step 1: descent

- **Rational slopes are common.** On 18 of B1438's 24 census levels some extension characters have a rational slope
  s(ℓ) = a/b. Exactly those modules descend, each to the one filling along γ = μ^b λ^(−a).
- **The derivation holds on every module.** All 46 618 such modules were checked: ρ(γ) = I on every one.
- **The fillings that receive modules** include μ itself (s = 0) and slopes such as ±1, ±1/2, 2/3, 3/4 and −5. The
  list for each level is in the results.
- **The checks:**
  - dim H¹(M; V) = 1 + [s(β) = s(ℓ)] on every module (B1438's exact sequence);
  - every ρ is a representation (each relator maps to I).

## Step 2: the count after filling

The census of (n(V), n(V*), dim H¹(M(γ); V)) over the 46 618 descended modules:

| (n, n*) | dim H¹ after filling | modules |
|---|---|---|
| (0, 0) | 0 | 39 424 |
| (1, 0) | 1 | 3 000 |
| (0, 1) | 1 | 3 000 |
| (1, 1) | 2 | 810 |
| (1, 1) | 1 | 384 |

- **After filling, the closed manifold counts both orders: dim H¹ = n(V) + n(V*).** This holds on 46 234 of 46 618
  modules. The exceptions are 384 of the 1 194 modules where both orders fire, which count 1.
- **So the filling turns the based count (n, n*) into its sum, and the class count I = n − n* does not carry.** A
  module that counts one way on M (+1 or −1) counts +1 after the filling, either way.

## The outcome

- **Outcome 1, as the card defined it, holds:**
  - the count n(V) carries on 42 808 modules: every (0, 0), every (1, 0), and the 384 exceptional (1, 1);
  - it does not carry on 3 810: every (0, 1), and the 810 (1, 1) that count 2.
- **Read plainly:**
  - filling descent is a map that carries the record's modules and their interior rank;
  - it forgets the pieces' order that the class count keeps: it reads both orders at once;
  - so it is a physical map for "how many", and not for the hand of the count.

## Controls and deviations

- **P2 held:** with the extension class set to zero, the rank changes on 42 424 modules.
- **P1 failed on exactly the 8 094 modules with slope 0.**
  - There the filling is along μ itself, ρ(μ) = I, and the planted wrong slope μ² descends as well. A plant on the
    other generator, μ^b λ^(−a+1), would have been needed.
  - On every module with a non-zero slope (38 524), P1 did not descend, as it had to.
- **Precision.** Ranks are numerical, by singular values in double precision, not exact. The built-in check passing
  on all 46 618 modules is the evidence that the ranks are right.
