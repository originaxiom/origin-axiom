# B1963 — In frame C, a charge-consistent Higgs reading aligns the cusp mixing only in the bulk, where the hierarchy is at most about two orders

**Verdict: PROVED** (computed on frame C's own code, on the grid stated below; data-free). Main, 2026-11-19. Register
row P-847. **0 of 19.**

> *Corrected 2026-11-19, the same day (Seen first was incomplete): the sweep used this campaign's words and missed the record's own. **B1739** (PROVED, October; B1656's frame) found the mechanism first: the frame's Higgs is nearly null, the cusp is led by ρ(T)'s null eigenlines (0, 1, ±i), each sector's lightest state sits on h̄ under S and on h under S̃, and under the Standard Model's reading (this arc's charge-consistent pair) the median |V_ud| on B1726's census is 0.28, following r^0.52. **B1740** (NEGATIVE as sealed, for F₋₂) found the other half: a non-null Higgs aligns the light generation and loses the hierarchy. B1742 adds the third regime. So this arc is a frame-C replication of B1739's census result on a wider grid (four columns, orders 2 to 10, heights 1 to 60), not a new exclusion. Its numbers stand.*

## Seen first

- **Swept:** `VERDICT topic-sweep /charge-consistent|charge rule|derange|cusp mixing|height window|S-tilde/: 2 of 1704 arcs on main match (NEGATIVE 1, PROVED 1); 7 register rows match (QUEUED 7)`.
  - **B1946:** at the 24 points of order 5, at heights 6 and 30, the charge-consistent readings (S̃ up with S down,
    or the mirror) derange frame C's cusp mixing. S → S̃ acts on the generations as a 3-cycle high in the cusp. At
    τ = i the two readings coincide.
  - **P-847:** the relative reading is fixed by hypercharge (main, the web seat's W-F13 and W-F14, agy-exp: four
    sources). One global bit remains.
  - **B1962:** frame D1, the Higgs's own twist, deranges the mixing for every reading.
- **The literature:** in the Standard Model the up quarks couple to H̃ = iσ₂H*, a conjugation hypercharge forces
  (standard). Frame C's charge rule copies it. No outside work bears on frame C's family.
- **Why now:** the session's goal is the final reading. A value-specific card needs the menu reduced by principle,
  and the charge rule is the one principle the record holds for the reading. This arc asks what the charge rule leaves
  of the mixing over the whole frame, not at order 5 alone.

## What was run

Frame C's own code throughout (B1945's split, B1946's unitary), unchanged. Each script states its expectations at its
top, and each was hashed before its run (`verification/EXPECTATIONS_HASHED.md`, with UTC times).

- **Part 1, `conjugation_cycle.py`.** Every point (i/n, j/n) ≠ (0, 0) for n = 2, 3, 4, 5, 6, 7, 8, 10 (295 points),
  at x = 0.13, heights 30 and 60.
  - **The first run is void,** and kept as `conjugation_cycle_run_VOID_threshold_bug.txt`. Its degeneracy screen
    (1e-30) set every point aside, order 5's included, because the frame's own hierarchy at height 30 crosses that
    floor.
  - **The screen was amended before the second run** to the working precision, 10^−(dps − 5) with dps = 30 + 2y as the
    frame sets it. The expectations were unchanged. The control held: order 5 has no degenerate point at height 30.
- **Part 2, `height_window.py`.** The 24 points of order 5 and the 48 of order 7, at x = 0.13, heights 1.0 to 10.
  The control is τ = i.
- **Part 3, `columns.py`.** The same points at x = 0, 0.25 and 0.5, heights 1.0 to 6.

**The measures.**
- m_cc is the smallest diagonal |V| over the two charge-consistent pairs, the worse of the two. Aligned means ≥ 0.9,
  deranged means < 0.1, and partial is between.
- h is the hierarchy: the smaller over the two sectors of s_min/s_max, with the record's reading per sector.

## The results

**High in the cusp, the charge-consistent mixing is deranged at every point** (part 1). At every non-degenerate point
of every order from 2 to 10 it is deranged:
- 271 points at height 30;
- 238 points at height 60.

**The conjugation becomes a permutation of the generations as the height grows.** At height 60 it is a 3-cycle at 20
of 20 points of order 5 and 80 of 90 of order 10. At height 30 many points are not yet a 0/1 pattern to 1e-6.

**(S, S), the pair the charge rule excludes, is aligned at most points but not at all.** The exceptions are 4 points
of order 8 at both heights, and 8 of order 10 at height 30.

**The height window** (parts 2 and 3; 72 points per row):

| x | height 1.0 | 1.5 | 2.0 | 3.0 | 4.0, 6.0 (and 10 at x = 0.13) |
|---|---|---|---|---|---|
| 0 | aligned 20, partial 52 | deranged 20, partial 52 | deranged 46 | deranged 72 | deranged 72 |
| 0.13 | aligned 16, partial 56 | (1.2: deranged 4) deranged 20 | deranged 46 | deranged 72 | deranged 72 |
| 0.25 | aligned 10, partial 62 | deranged 20, partial 52 | deranged 44 | deranged 72 | deranged 72 |
| 0.5 | aligned 6, deranged 4 | deranged 20, partial 52 | deranged 34 | deranged 72 | deranged 72 |

- **Aligned only at height 1.0.** No point at any column is aligned at height 1.2 or above. Every point is deranged
  from height 3.
- **Where it is aligned, the hierarchy is small.** The aligned cases at height 1.0 have h ≥ 3.9e-3. That is two
  points of order 7 at x = 0.13, (3/7, 4/7) and (4/7, 3/7), with m_cc = 0.927. At the other columns it is ≥ 1.1e-2.
- **No case anywhere has an aligned charge-consistent mixing with three orders of hierarchy** (h ≤ 1e-3).
- **The control:** at τ = i the charge-consistent pair equals (S, S) exactly, at all 72 points.

## The expectations, read

| | expectation | prior | result |
|---|---|---|---|
| X1 | at height 30 the conjugation is a 0/1 pattern at every point | 0.6 | fails: many points converge only by height 60 |
| X2 | 3-cycles are the majority at every order | 0.5 | fails at height 30 (orders 3 and 6); holds at 60 where any pattern is resolved |
| X3 | the charge-consistent pairs are deranged at every point at height 30 | 0.6 | holds, and at height 60 |
| X4 | (S, S) aligned at every point at height 30 | 0.5 | fails at 12 points |
| X5 | heights 30 and 60 classify alike | 0.8 | fails, 174 of 295, through degeneracy and convergence |
| Y1 | the control at τ = i | 0.95 | holds, exactly |
| Y2 | deranged everywhere from height 2 | 0.6 | fails at 2 and 2.5 (partial points); holds from 3 |
| Y3 | no aligned case with h ≤ 1e-2 | 0.7 | fails narrowly: 2 cases, h = 3.9e-3, m_cc = 0.927 |
| Y4 | where aligned, h > 0.1 | 0.5 | fails: h ≥ 3.9e-3 |
| Z1 | at the other columns, nothing aligned from height 1.5 | 0.6 | holds |
| Z2 | at the other columns, all deranged at heights 4 and 6 | 0.7 | holds |
| Z3 | no aligned case with h ≤ 1e-3 anywhere | 0.7 | holds |

## What it means

- **On frame C, the charge rule and a large hierarchy exclude an aligned cusp mixing.** Where the couplings carry
  three or more orders of hierarchy, a charge-consistent reading leaves the mixing partial or deranged at every point
  computed.
- **The aligned option needs the reading the charge rule excludes, (S, S).** So within this frame no principle the
  record holds for the reading leaves both an aligned mixing and a hierarchy. Frame D1 does not supply one (B1962).
- **For the goal:** a value-specific card cannot be built on frame C's mixing under its own charge rule. Either a
  principle that overrides the charge rule is found, or the frame changes, or this exclusion enters the write-up as a
  property of the record's frames.

## Scope and what is not established

- **A computation on a grid, not a theorem.** It covers orders 2 to 10 high in the cusp, orders 5 and 7 across height,
  and four columns. An analytic proof would derive the 3-cycle from the theta functions' leading terms. It is not
  attempted here.
- **Frame C's other declared choices are held fixed:** the Higgs direction, the end, the channel weights and the
  generations' metric. A different Higgs direction (P-873's ground plane) is not tested.
- **Data:** none. "Aligned" and the hierarchy thresholds were fixed in the scripts before each run. Neither is a fit.

## Files

`verification/conjugation_cycle.py`, `height_window.py` and `columns.py`, each with its run file, the void first run,
and `EXPECTATIONS_HASHED.md`. The lock is `verification/test_b1963_window.py`.

0 of 19.
