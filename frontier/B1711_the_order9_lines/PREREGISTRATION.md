# B1711 — PREREGISTRATION: W59'S ORDER-9 LINES AT THE BAND τ (P-256) — with the flat line at one of the record's eighteen order-9 lines, the end-data Higgs ∂R and one continuous number (Im τ), do the six charged-fermion ratios come out, specifically?

cc (main), 2026-10-22, after S182. **Sealed before `verification/the_order9_lines.py` and `verification/compare.py` run.**
A test of a structure (B1637's checklist), not a value derived. 0 of 19.

## Why

B1698's order-5 lines (the tick's) brought all six ratios within a factor 2.33 with one continuous number, but failed on
a structural obstacle: on any order-5 line the down quarks and the leptons are identical (minimal SU(5)'s Y_e = Y_dᵀ).
B1703's census: on B1656's coupling two sectors coincide exactly when the line's order divides 4, 5, 6, 7 or 2; from order
8 on all three split, and the only order that splits all three and protects a first generation is 9 (the leptons). The
record carries a specific set of order-9 lines: W59's eighteen, (p₁, p₂) = (b + i/3, b + j/3) with b ∈ {1/9, 2/9} (B1656's
LINES18; W59 verified on main, B1684), selected by the one-loop potential at ω for the Higgs alone — an input, not the
potential's state once the matter is in (B1686). P-256 tests them where the hierarchy lives.

## The model and the cells

Each of the eighteen lines (w = p₁τ − p₂); the section ∂R (B1700: the unit's member with R's own end condition);
B1667's canonical end; B1656's four-channel coupling; Re τ ∈ {0, ½}, Im τ = 1.5–3.5 (step 0.02) — **one continuous
number** — and the discrete choices: 18 lines × 2 Re τ × 2 horocycles × 3 up readings = 216.

| cell | prediction | prior |
|---|---|---|
| **H1** | some point puts all six ratios within a factor of 3 | 35% |
| **H2, specific** | at most 1% of 4 000 random hierarchical target sets (B1695's prior) fit at least as well | 5% |
| **H3** | the minimum χ² is below 16.75 | 2% |

Read-outs: the best point; the best worst-factor per line; whether d and e are split at the best point (B1703 says they
must be); the electron's m₁/m₃ there (protected at leading order, lifted at the canonical end).

**The reading, written before the run.** If H2 holds: the record's own order-9 lines with the end-data Higgs reproduce
the six ratios better than random hierarchies with one continuous number — the strongest structural result on the
record, graded a READING (Λ, the unit, H-cov in R's module, W59's lines as an input, 216 discrete choices tagged, inside
the calibration), to be attacked first: by the other order-9 lines (the census's 72 of exact order 9), by β's role, by an
independent route. If H2 fails: W59's lines do not select the line in this frame, and with B1698 the record's selected
lines are exhausted for the masses in this frame.

## Seen first

`VERDICT topic-sweep /order.?9 lines?|lines? of order 9|eighteen lines|W59's (eighteen )?lines|LINES18/ (full text): 14 of 1482 arcs on main match (NEGATIVE 3, PROVED 11)` —
B1656 and B1660 (W59's lines at ω, with a free Higgs and a fitted end: B1660 NEGATIVE), B1668, B1673, B1684 (W59 on main),
B1686 (the potential's state is not W59's lines), B1692, B1693, B1695, B1703 (the census). None tests these lines with the
end-data Higgs at the band τ. **Literature:** none beyond the cited arcs.

## Disclosed

- **Known before the seal.** The six measured ratios; B1694–B1702's results (B1698's best 2.33 on order-5 lines; the
  up quarks' floor 0.0134 at Im τ = 2, B1702); B1703's laws (order 9 splits all three and protects the leptons).
- **Model values on order-9 lines exist on main, unread:** B1703's census JSON holds (m₂/m₃, m₁/m₃) for every line of
  order ≤ 16 at τ = 0.31 + 2.4 i and 0.13 + 1.9 i (and 0.41 + 2.9 i), at L_max, with the same Higgs. Main read only its
  coincidence and protection flags, never the ratios; those τ are off this test's CP lines.
- The instruments were import-tested before the seal (no computation). B1660 tested these lines at ω with a free Higgs;
  this test fixes the Higgs and frees Im τ.

## Instruments

`verification/the_order9_lines.py` (no data) → `the_order9_lines.json`; `verification/compare.py` (the comparison and the
calibration, as B1698's) → `comparison.json`; B1656's functions copied verbatim; hashes in `ARTIFACT_HASHES.txt`.
