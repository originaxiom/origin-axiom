# `AGY-002` Card `A2-P879` Erratum `3` — `8`-Digit `v3` / `Referee v2` Match & `v4` / `Referee v3` Test-Grid Clarifications (`0 of 19`)

- **Date:** `2026-11-20`
- **Immutable Previous Records Preserved Untouched:** `relays/a2_p879/` (`de80a1eab`), `relays/a2_p879_v2/` (`0b537f08b`, `d48f34b17`), `relays/a2_p879_v3/` (`0babf1985`, `dd36935d7`), `relays/a2_p879_referee/` (`f5f3f968e`), and `relays/a2_p879_referee_v2/` (`3854a3f26`, `7601f72b5`) remain untouched in git history.
- **Confirmed `8`-Digit Producer `v3` vs Cold-Room Referee `v2` Agreement (`Erratum 2` `F_u` Cross-Check):**
  Across `24` order-`5` plus `4` order-`7` torsion points at columns `x in {0, 1/4}`, Producer `v3` (`dd36935d7`) and Referee `v2` (`7601f72b5`) match to **all `8` reported digits** of `max s_L`:
  - `y = 3/2`: `38755037 / 100000000` (`both`)
  - `y = 2`: `38806421 / 100000000` (`both`)
  - `y = 3`: `34114296 / 100000000` (`both`)
  - `y = 6`: `16651333 / 100000000` (`both`)
  - `y = 15`: `2428456 / 100000000` (`both`)
  - `y = 30`: `83974 / 100000000` (`both`)
  - Plus `8`–`10` digit agreement on `L_2(13/100 + y i)` (`dyadic Chebyshev vs RK4`).
- **Two Exact Test-Harness Clarifications (`Zero Changes to Theorems T1–T5`):**
  1. **`T3` `2D` Grid Parity (`for v4`):** On $t \in [0, \pi/2]$ and $\phi \in [0, 2\pi]$, `pv = np.linspace(0, 2*pi, N_phi)` must use odd `N_phi` (`N_phi = 33`, `32` intervals) so the analytical maximizer $\phi = \pi$ lies on the grid (`Producer v3 used even N_phi = 90`, missing $\phi = \pi$ by half a cell while exact $t_*$ passed to `< 2 * 10^{-16}`).
  2. **`T4(b)` Cusp Monotonicity Starting Height (`for referee_v3`):** Under the exact `B1940` $F_u$ formula, $s_L$ at $x = 0$ rises slightly from $y = 1$ (`33515/100000`) to its bulk peak at $y = 2$ (`38806/100000 < 2/5 \ll 17/19`) before decreasing strictly monotonically across the cusp sequence $y \in \{2, 3, 6, 15, 30\}$ (`Referee v2 checked 1 > 3 across that bulk peak`).
- **Sealed `A`-Only Final Companions:** `relays/a2_p879_v4/` (`adding T3 N_phi = 33, tau-level memoization, and unit-bidisk CP^2 filtering`) and `relays/a2_p879_referee_v3/` (`checking cusp monotonicity over y in {2, 3, 6, 15, 30}`).

0 of 19.
