# B1441 — THE SEVERAL-CUSPED LEVELS: with two live cusps a rank-two background counts two — the first in the record to count more than one — and none counts three

cc, 2026-10-01. Sealed at 6085218c before the class index of any non-split module was computed on a manifold with
more than one cusp (`PREREGISTRATION.md`, sha-256 `a1b80a9e…`, SEAL_LEDGER). Main's lead L222 had carried the
computation as owed since 2026-09-16; a sweep of main and every lane found it run nowhere. **Verdict: PROVED** (the
run is complete; every identity of B1333's derivation held on every module; every index of two is exact).
**Predictions: M1, M3, M6, M7 YES; M2, M4, M5 NO.**

## The run

74 manifolds with two to six cusps — the multi-cusped covers of degree up to six of m004, m003, m009, m010, and
m202, s959, o10_150726, m129, m125 — and a second tier at N = 12 for the five named ones: 79 entries, 76 run, three
skipped for having more than 600 characters. Every character of order dividing N, no cusp condition imposed.
**564 742 rank-two non-split modules**, each through `mc_lib.check` with its five identities asserted.

- **63 of 76 entries fire:** 24 660 modules with I ≠ 0. These are the first values of main's class index on
  non-split modules over several cusps.
- **17 manifolds carry a module with |I| = 2; 344 such modules; none with |I| = 3.**

| cusps | entries run | carrying \|I\| = 2 | largest \|I\| |
|---|---|---|---|
| 2 | 56 | 11 | 2 |
| 3 | 15 | 3 | 2 |
| 4 | 3 | 3 | 2 |
| 5 | 1 | 0 | 1 |
| 6 | 1 | 0 | 1 |

| covers of | run | silent | largest \|I\| = 1 | largest \|I\| = 2 |
|---|---|---|---|---|
| m004 (the root) | 11 | 1 | 10 | **0** |
| m003 | 6 | 0 | 6 | **0** |
| m009 | 23 | 4 | 9 | **10** |
| m010 | 26 | 0 | 19 | **7** |

The two is on covers of degree four and six of the third and fourth word states. **No cover of the root or of its
sibling to degree six reaches it**, the five-cusped cover of m003 included.

## What an index of two looks like

- **Two live cusps.** Every module with |I| = 2 has at least two cusps live for it, and |I| never exceeds the
  number of live cusps counted with multiplicity (t₀ summed over cusps). 240 of the 344 sit on exactly two live
  cusps of a two-cusped manifold; the rest on two or three live cusps of a three- or four-cusped one.
- **A character with more than one class.** On several cusps H¹(M; χ) is no longer a line: over the population
  1 485 characters have one class, 463 two, 94 three, 15 four. Of the witnesses recorded, the extension character
  has two classes in 118, one in 18, three or four in 18. Where it has several, the index can depend on which
  class is used.
- **Small orders.** The carriers have N = 2 (nine), 4 (four), 6 (three), 8 (one): sign characters suffice.

## Exact (`verification/exact_mc.py`, record `exact_several.json`, `exact_run.txt`)

A second implementation of B1333's formulas over ℚ(ζ_N), own field and linear algebra, on up to four witnesses of
each of the 17 carriers (62 witnesses), over a basis of the extension classes and three random combinations:
**an index of exactly ±2 on every carrier.** Example, over ℚ: on the three-cusped cover m009 deg 6 #21, ℓ = [0,0,0,1],
α = [0,1,0,0], h¹(ℓ) = 2, I = 2 for every class tried. In the run itself every module with |I| = 2 was recomputed
at two further primes; where h¹(ℓ) = 1 all three agree (0 differing).

## The named manifolds

| manifold | N = torsion exponent (or 2) | N = 12 |
|---|---|---|
| m202 | no module (no character has a class) | 1 704 modules, all 0 |
| s959 | 350 modules, all 0 | 6 020, all 0 |
| o10_150726 | 168, all 0 | 65 436: I = ±1 on 192 each |
| m129 (the Whitehead link) | 4, all 0 | 3 124: I = ±1 on 16 each |
| m125 | no module | 1 704, all 0 |

The record's two-cusped carriers of the localized three, m202 and s959, carry **no** class index on any module
tried. That three is another count (B1414), and this arc is the first to put the class index beside it.

## The sealed predictions, read (`verification/read_several.py`, run twice; record `several_cusps_summary.json`)

| | prediction | prior | outcome |
|---|---|---|---|
| M1 | some manifold carries a rank-two module with \|I\| ≥ 2 | 50% | **YES** (17 manifolds) |
| M2 | some manifold carries one with \|I\| = 3 | 20% | **NO** |
| M3 | \|I\| at most the number of cusps, everywhere | 80% | **YES** |
| M4 | m202 and s959 each carry a module with I ≠ 0 | 50% | **NO** (neither does) |
| M5 | m202 or s959 carries \|I\| ≥ 2 | 25% | **NO** |
| M6 | every module with \|I\| ≥ 2 has at least two live cusps | 85% | **YES** |
| M7 | among the covers, the largest \|I\| is reached on a manifold with at least three cusps | 40% | **YES** (also on two-cusped ones) |

Four of seven came true where 3.5 were expected.

## What it means, and the fence

- **B1440's bound is one cusp's, and the cusp is what it counts.** With one cusp a rank-two background counts at
  most one; with two live cusps it can count two, and does, on seventeen manifolds near the architecture. The
  count per background is bounded by the live cusps, not by the frame.
- **Three in one rank-two background would need three live cusps and has not been found** to degree six. Modules
  with three live cusps exist here and count two. This is a search with a named target, not a negative.
- **The root's own covers never reach two.** Whether that is a law of the root or of degree six is not known.
- **A module is not a background.** A generation-shaped background needs five charged sectors with one index.
  That is the next sealed step, on these seventeen manifolds.
- **The fence is unchanged:** main's class index on modules outside the reductive domain; an index is not a
  generation count; no physics reading of a non-semisimple background. 0 of 19.

## Not in this arc

Generation-shaped backgrounds on several cusps; modules of rank above two; covers of degree above six; the three
manifolds skipped for size; a slope law for several cusps (the boundary data are now one vector per live cusp and
the firing condition an intersection of two Lagrangians; not worked out).

## Verification

`verification/several_cusps.py`, `read_several.py` (sealed), `exact_mc.py`; records `several_cusps_0..5.json`,
`slice_*_run.txt`, `control_run.txt`, `exact_run.txt`; `several_cusps_summary.json` and `exact_several.json` at the
arc's root. Lock: `tests/test_b1441_several_cusps.py`.
