# B596 — the clock is NOT the naive cat-map period: null-with-structure

**Status: banked (frontier). Nothing to `CLAIMS.md`; no SM quantities.
Preregistered; the registered prediction FAILED on the full sweep and is
banked as such. Locks `tests/test_b596_cat_map.py`.**
Run: `python3 cat_map_clock.py` (pyenv, ~3 min).

## Q1 — the blind sweep: the registered claim fails

The prereg's hand-checks (κ = 5, 6, 7: clock = ord(A₁ mod κ)) were lucky
rows. Over κ = 4..15: clock = ord(κ) holds 5/12; clock = ord(2κ) 5/12;
clock | ord(2κ) only 8/12; at κ = 4 the clock (1) is SHORTER than the
classical order (3) — the θ-antisymmetrization can destroy order, so no
divisibility law in either direction survives. **The θ-odd block's clock is
not the quantum cat-map period in any of the registered simple forms.**

Post-hoc structure (data, not law): the clocks are PISANO-ANCHORED —
clock(κ)/π(κ) ∈ {1/6?, 1/2, 1, 3/2, 2} across the sweep (e.g. κ = 10:
clock 60 = π(10); κ = 13: 28 = π(13); κ = 5: 10 = π(5)/2; κ = 11: 20 =
2π(11); κ = 9: 36 = 3π(9)/2) — but the multiplier is not a uniform function
of κ in this range. Q2: silver is likewise non-uniform (κ = 6: clock 12 vs
ord 4; κ = 8: clock 4 vs ord 4).

## Q3 — what stands, precisely

B587's factorization identifies the FULL stage trace with the quantum cat
map's Weyl-twisted character — that is proven and unchanged. What B596 shows
is that the θ-odd BLOCK's dynamical order is not the naive cat-map period:
the antisymmetrization and the metaplectic phases contribute κ-dependent
corrections that can lengthen (×2, ×3) or destroy (κ = 4) the order. The
operator-level dictionary at golden therefore holds at the level of traces
and determinants (B587; B595's spectral bridge) but NOT at the level of
orders — L84 is sharpened: any functorial map must explain the clock
multipliers, and L81(b)/L77's clock question stays open with this table as
its data.

## Discipline note

The prereg's prediction is banked as failed (rule: an extrapolated
hand-check is not a law). The sweep was blind; all candidate laws were
tested on every row and reported with their miss counts.

## Anchors

B587 (the factorization — unchanged), B585 (the clock table, now extended
and still lawless), B595 (the bridge — trace/determinant level), AP3/B211
(the classical orders/Pisano), L84 (sharpened), L77/L81(b) (the open clock).
