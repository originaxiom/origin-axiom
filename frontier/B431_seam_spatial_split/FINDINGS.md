# B431 — the seam's spatial split on the boundary torus: the CRT gating law CONFIRMED exactly; two value-level claims corrected

**Status: banked. Chat-1's GAP-2 data adjudicated (verify-don't-trust): the striking part
survives exactly; the two value-level readings were artifacts. Firewalled.**

## Confirmed exactly (the support / gating law — interface data)

Exact FT of the (1,2) seam's √−15 components (44 cells) to the dual torus (x,y) ∈ ℤ/20×ℤ/12:
- **ACTIVE 120 / DARK 120** — exactly half the boundary torus;
- **y ≡ 0 mod 3: all dark** (the Eisenstein character gates the spatial support completely);
- **x ≡ 0 mod 10: all dark**;
- CRT cells (x mod 5, y mod 3): the two x≡0-mod-5 cells carry 4/16 active, the eight others
  14/16 — so beyond the two gating lines there are exactly 2 extra dark points per generic cell;
- parity (x,y)→(−x,−y) preserves the active set with **0 fixed points** (60 free orbits).

## Corrected (value level)

- Parity partners are **conjugate, not equal**: S(−x,−y) = conj S(x,y) and S is genuinely
  complex — "the spatial seam is entirely parity-even" fails at the value level;
- the exact value-orbit structure is **34 orbits, sizes {2:24, 4:2, 8:8}** — not 18 = 4×16+14×4.

## Why it matters (the interface campaign)

This is the seam channel's **spatial support law**: where on the boundary torus the two-object
coupling is nonzero, gated exactly by the 3-side character. Together with B427 (the physical
√−15 channel is exchange-symmetric) this is the beginning of a concrete interface kinematics —
named as mathematics; the bar judges any physics reading later.

**Provenance.** spatial_split.py → spatial_split.json; lock tests/test_b431_spatial_split.py.
Machinery: B367 step0 + B358 cyclo_engine (all exact).
