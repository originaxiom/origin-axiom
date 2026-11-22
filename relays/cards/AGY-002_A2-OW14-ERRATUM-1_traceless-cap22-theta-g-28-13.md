# Erratum 1 to Pre-Registration Card `AGY-002_A2-OW14` (`AGY-C25` Finding `S6`)

- **Seat / Branch:** `agy-002` on `agy-002/verify`
- **Date:** `2026-11-22`
- **Target Sealed Card (unmodified):**
  `relays/cards/AGY-002_A2-OW14_7d-hyperbolic-radion-acceleration-and-unimodular-sequestering.md`
- **Empirical Inputs:** `0 of 19`

## 1. Exact Arithmetic Typo in Sealed Card Line 58

Line 58 of the sealed `A2-OW14` pre-registration card wrote:

> `Traceless (cap = 22): 5/2 < N_gen < 31/8 -> unique integer N_gen = 3 (g_* = 6 pi / 7, theta_g = 14/6 = 7/3;`

In the unimodular traceless (`cap = 22`) Litim FRG formula at `M_g = 8` (`N_gen = 3`, `G_SM + 2H`):

- Exact numerator: `2 * (22 - M_g) = 2 * (22 - 8) = 28`.
- Exact denominator: `21 - M_g = 21 - 8 = 13`.
- Therefore the exact critical exponent is **`theta_g = 28 / 13`**, NOT `14 / 6 = 7 / 3`.

Both the producer (`relays/a2_ow14_v2/verify_a2_ow14_v2.py`) and the independent referee
(`relays/a2_ow14_referee/referee_a2_ow14.py`) already computed `28 / 13` directly from the
exact rational formula (`relays/AGY002_A2_OW14_RESULTS.md` line 10 noted the typo without a
card-level erratum). This dated erratum closes `AGY-C25` finding `S6` cleanly without
modifying the historical sealed card.

## 2. Check Label Disclosure (`docs/seats/README.md` Section 12)

For full transparency under section 12, this erratum also records that six earlier cards
(`A2-P879`, `A2-OW6`, `A2-OW7`, `A2-OW11`, `A2-OW12`, `A2-OW13`) updated quantitative
thresholds in dated post-`v1` errata prior to running their final versions; those updated
expectations are classified as **mended expectations** rather than unmended `v1` locks.

0 of 19.
