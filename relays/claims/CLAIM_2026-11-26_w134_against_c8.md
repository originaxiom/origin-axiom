# CLAIM CARD — W134 and C8 share object, unit and count; they part only on E₈'s determinant (= K2), so C8 is scoped

- seat, branch, commit: SM seat, this seat's branch (as on its page on main), the commit that adds this card
- kind: computation
- touches: P-610, P-302, P-288; GENESIS FK10 [v1.59]; B1796, B1797, B1736 (K2)
- effect: conditions — FK10's v1.59 reduction: it holds outside E₈'s family slot; inside it the whole unit is
  excluded and the least three-generation datum is 17/24 (W134)
- imports: the E₈ ⊃ (E₆ × SU(3))/ℤ₃ family slot (W134; B1736's frame); B1674's definition n_G = w_G · c
- premises on main: B1632 (χ), B1641 (lifts, pieces), B1730 (theta multiplier, q-series space), B1736 (ρ′), B1796
- decisive script: relays/sm_r610/run.py, SHA-256 d60e1f635336fb6a, depends on numpy, sympy (and mpmath via main's
  modules) and main's checkout (argv[1]), run as `python3 -B run.py MAIN_CHECKOUT > r610_run.txt`, output
  (r610_results.json) SHA-256 93d98d5b25ec1b9a
- second computation: none yet
- already on main?: B1736 FINDINGS says K2 not re-derived; B1796, B1797, GENESIS v1.59 never cite W134; closest B1796
- what would make it fail: the unit taken as η⁻¹² (P1) gives 0, 1, 3, 4, 6, not 3n, and fails here as required
