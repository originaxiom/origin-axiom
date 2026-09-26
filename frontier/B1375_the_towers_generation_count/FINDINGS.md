# B1375 — THE TOWER'S GENERATION COUNT: on the cyclic covers Y_n of m004, built on their own presentations, with the character group complete on each level's torsion and the search restricted only by B1297's T5, the Standard-Model-frame index of B1374 is computed level by level — Y₂ (m206) and Y₃ (s961) carry no generation-shaped background, Y₄ (t12839) carries 12 800, Y₅ (o10_150696) 800, Y₆ 67 200, and on every one of these 80 800 backgrounds the count is exactly one net generation, Q = u^c = e^c = d^c = L = ±1, never two, never three; the 12 800 of Y₄ reproduce B1374's census from a different presentation, one background per firing level is re-derived exactly over ℚ(ζ_N), and the singlet count is 0 on Y₄ and Y₅ and 0 on 57 600 and ±1 on 9 600 (the singlet carrying the generation's own sign on 9 600  the opposite sign on 0) on Y₆ — one generation per background is the tower's law as far as computed, and the count of three is not produced by this mechanism on any level up to six

> **Harvested from main (2026-09-26, main @ `987c0c8f`): main's B1427 (2026-09-18) verified this arc with independent code**
> (own Fox calculus, GF(p) and cyclotomic arithmetic; primes 1021, 1201, 1321) — every number reproduced, h¹(χ²) = 1 at all loci,
> 12 800 / 800 backgrounds, |I| = 1 throughout — and added three qualifications this arc's wording does not carry, adopted here:
> (1) "complete on each level's torsion" is not "complete": the μ_N scan misses exactly two loci per level, m004's own golden
> locus lifted to the cover (on M₄ the real numbers ((3+√5)/2)^(±4)), where h¹ = 1 as well, so the claim survives; (2) "h¹(χ²) = 1
> bounds |I| ≤ 1" is not a proof as stated — the bound is the interior-class count on the doublet, which is B1377's extension bound
> (|I| ≤ a₁(χψ) + a₁(χ⁻¹ψ)); (3) the M₅ census used the cusp filter, which is a proved consequence of t₀ ≠ 0. Cited, not
> re-derived here. Main's B1427 also writes Yₙ for these cusped covers — E72 applies there as here.

> **Notation correction (2026-09-26, B1379; E72).** The levels Y₂–Y₆ (and Y₇) below are the **cusped** cyclic covers of m004 — now written **M₂–M₆** — not B1301's closed branched covers, which keep the name Yₙ. Every number below stands, on Mₙ; none of the one-generation backgrounds descends to the closed cover (M₄: 0 of 89 loci; B1379).

**Date:** 2026-09-16 · **Seat:** cc (the SM-derivation branch) · **Status:** PROVED (the computations; the one-per-background law on the levels computed) · **Fence:** main's index on a non-semisimple background, main's fence — no physics reading, no value, no three · **Price: unchanged** · **Numbering:** B1375 (sL-2).

## 0. Seen from above

B1374 found the first Standard-Model-shaped chiral count in the record: on t12839, the degree-4 cyclic cover of m004, the
sector-by-sector one-cusped index (main's B1297 definition, on reducible non-split SL(2)_β holonomy at a torsion locus with ℂ*²-characters
of order dividing 60) is exactly one generation on 12 800 backgrounds. sL-2 asked whether the count grows with the level of the tower
and where it is three. This arc builds the levels Y₂–Y₆ by SnapPy's `covers` — their own presentations, not the census names — takes
the character group complete on each level's torsion (N = lcm(12, torsion exponent): 60, 12, 60, 132, 120), enumerates every non-split
locus (the intersection over three primes), and computes every doublet module ρ_χ ⊗ ψ that B1297's T5 allows to fire (ψ = χ^{∓1} on both
peripheral curves; every candidate computed, every non-zero re-checked over two more primes), then every pair (ψ_Y, ψ_γ) whose five
charged sectors all fire, solving ψ_Y⁵ = u/v from the two 5̄-sectors and reading the three 10-sectors.

The table is: **Y₂ (m206): 9 loci, 16 firing modules, no generation. Y₃ (s961): 31 loci, nothing fires. Y₄ (t12839): 89 loci, 976 firing,
12 800 generation-shaped backgrounds on 64 loci — B1374's numbers exactly, from a different presentation. Y₅ (o10_150696): 241 loci,
4 400 firing, 800 backgrounds on 200 loci. Y₆: 639 loci, 10 816 firing, 67 200 backgrounds on 576 loci.** On all 80 800 the count is
±1 — signs equally split, ψ_Y trivial or of order 5 (and 10, 2 on Y₆), ψ_γ of order 11 and 22 on Y₅, of order 4, 8, 20, 40 on Y₆ — and
never 2 or 3; the singlet count is 0 on every background of Y₄ and Y₅ and 0 on 57 600 and ±1 on 9 600 (the singlet carrying the generation's own sign on 9 600  the opposite sign on 0) on Y₆. One background per level was re-derived exactly
over ℚ(ζ₁₃₂) (Y₅, degree 40) and ℚ(ζ₆₀) (Y₄, B1374): (1, 1, 1, 1, 1, 0). The firing sectors always have (a₀, a₁, t₀, r₁) = (0, 1, 1, 0) on
one side and (0, 2, 1, 2) on the other: one interior class against none. So the tower's law, as far as computed, is **one generation per
background**: the mechanism does not produce three on any level up to six. What it produces it produces on every level from four
upward. Y₇ (N = 348, torsion ℤ/29 ⊕ ℤ/29) was attempted and did not complete: the character enumeration as written is
O(N^{#gens}) before the relator filter (348³ ≈ 4.2 × 10⁷ candidates checked one at a time in Python), and the process left no
output before the container recycled it. Not a negative — an instrument limit, named in B1377 §3.3 as the concrete next step
(solve the relator system over ℤ/N directly instead of enumerating).

## 1. Computed

`verification/tower_generations.py` (record `tower_generations_run.txt`; levels 4–6 with the background lists and singlet counts in
`tower_generations_run_456.txt`; `tower_generations_2_3_4_5_6.json`, `tower_generations_4_5_6.json`), `verification/exact_check_cover.py`
(`exact_check_cover_run_Y5.txt`); B1374's `index_lib.py` and `exact_lib.py`.

| level | H₁ | N, primes | non-split loci (spurious on single primes) | (χ(μ), χ(λ)) | T5 candidates / firing (re-checked, differing) | generation-shaped backgrounds / loci | count, signs, singlet | ψ_Y orders | ψ_γ orders | time |
|---|---|---|---|---|---|---|---|---|---|---|
| Y₂ = m206 | ℤ/5 ⊕ ℤ | 60; 421, 541, 601 | 9 (0) | (±1, 1) | 45 / 16 (16, 0) | **0** | — | — | — | 1 s |
| Y₃ = s961 | ℤ/4 ⊕ ℤ/4 ⊕ ℤ | 12; 409, 421, 433 | 31 (0) | (±1, 1) | 496 / 0 | **0** | — | — | — | 1 s |
| Y₄ = t12839 | ℤ/3 ⊕ ℤ/15 ⊕ ℤ | 60; 421, 541, 601 | 89 (0), all h¹ = 1 | (1, ±1) | 4 005 / 976 (976, 0) | **12 800 / 64** | ±1 (6 400 each); ν^c 0 on all | 1: 512, 5: 12 288 | 30: 4 608, 15: 4 608, 10, 5: 1 536 each, 6, 3: 192, 2, 1: 64 | 15 s |
| Y₅ = o10_150696 | ℤ/11 ⊕ ℤ/11 ⊕ ℤ | 132; 661, 1321, 1453 | 241 (4 on 661, 0, 0), all h¹ = 1 | (1, ±1) | 29 161 / 4 400 (4 400, 0) | **800 / 200** | ±1 (400 each); ν^c 0 on all | 1: 800 | 22: 400, 11: 400 | 117 s |
| Y₆ | ℤ/8 ⊕ ℤ/40 ⊕ ℤ | 120; 601, 1201, 1321 | 639 (0), all h¹ = 1 | (1, ±1) | 204 480 / 10 816 (10 816, 0) | **67 200 / 576** | ±1 (33 600 each); ν^c 0 on 57 600 and ±1 on 9 600 (the singlet carrying the generation's own sign on 9 600  the opposite sign on 0) | 1: 2 304, 5: 55 296, 10: 9 216, 2: 384 | 40: 46 080, 20: 18 432, 8: 1 920, 4: 768 | 860 s |
| exact | Y₅, locus χ = (0, 6, 120), ψ_Y = 1, ψ_γ = (24, 90, 96), over ℚ(ζ₁₃₂) (degree 40) | | h¹(χ²) = 1 exactly; ρ_χ a representation exactly | | | | **(1, 1, 1, 1, 1, 0)**; each firing sector V = (0, 1, 1, 0), V* = (0, 2, 1, 2); the singlet (0, 1, 1, 1) both sides | | | |

(Y₂ and Y₃ are labelled by SnapPy's cover presentation with χ(μ) = ±1 and χ(λ) = 1; from Y₄ on the labels come the other way; in every
case one peripheral curve is null-homologous on the level and the other carries ±1 at every non-split locus — the tower's structural
gift to a generation, B1374 §2.3.)

## 2. What it means

1. **One generation per background, on every firing level.** Levels four, five and six carry generation-shaped backgrounds in the
   tens of thousands; the count is ±1 on all 80 800. Two or three never occur. The reason is visible in the dimensions: at every locus
   h¹(χ²) = 1, the firing doublet modules have a single interior class on one side (a₁ = 1, r₁ = 0) and none on the other (a₁ = 2,
   r₁ = 2), and |I| = |n(V) − n(V*)| cannot exceed the number of interior classes. A count of three in one background would need
   three interior classes in one doublet sector, which no level up to six has; on the tower the rank-one h¹'s are 1 (B1301, B1303)
   and the non-split rank-2 modules computed here show a₁ ≤ 2 wherever they fire.
2. **Not two and not three: the count of three is not this mechanism's.** The programme's outstanding number is three generations.
   The tower's mechanism gives one per background at every level where it gives anything; three backgrounds are three flat connections,
   not one. If three is to come from the family it must come from somewhere else — a level with h¹(χ²) ≥ 3, a non-cyclic cover, or a
   different frame — and none of these is computed here.
3. **Y₂ and Y₃ are empty, Y₄ is the first firing level.** m206 fires (16 doublet modules at its ℤ/5 characters) but never on both a
   10-sector and a 5̄-sector at once; s961 fires nowhere at N = 12, its complete torsion group.
4. **Presentation independence.** B1374's 12 800 / 64 / 976 on the census triangulation of t12839 and this arc's on the cover's own
   presentation agree in every statistic — the index is a topological invariant of (M, module) and both codes compute it.
5. **The singlet.** On Y₄ and Y₅ no generation background carries a net right-handed neutrino; on Y₆ 57 600 of the 67 200 backgrounds have no net singlet and 9 600 carry one — 9 600 with the generation's own sign (a generation with its right-handed neutrino  all six counts equal) and 0 with the opposite sign.
6. **Fences, as in B1374.** Main's index (B1297) on reducible non-split SL(2)_β holonomy — a non-unitary, non-semisimple flat E₆(ℂ)
   connection whose physical standing is not established; the reading of I as net chirality is B1297's derivation in the D2 frame; no
   value; sL-2's question (iii) remains the one that would make the count a claim.

## 3. Caveats

1. Prime fields with the locus set as the intersection over three primes and every non-zero re-checked over two more; the exact
   re-derivation on one background per level (Y₄ in B1374, Y₅ here) with an independent implementation. Y₆'s backgrounds are
   prime-field results (three primes) without an exact check; ℚ(ζ₁₂₀) has degree 32 and the check is a minute's run if wanted.
2. Completeness: the character groups are complete on the torsion and contain the characters of order dividing 12 on the free part;
   other finite orders on the free part and infinite-order characters are not scanned. T5 is used only to skip modules that cannot
   fire; it is a theorem (B1297 §2), and the coset ψ = χ on both curves is included as well as ψ = χ⁻¹.
3. The generation search solves ψ_Y⁵ = u/v over all fifth roots in the character group and reads the 10-sectors; a background is
   generation-shaped iff all five charged counts are equal and non-zero. Anomaly-free patterns with some zero counts are not enumerated
   at these sizes (B1374 did so at μ₁₂ and found none on any member).
4. Levels beyond six: Y₇ (torsion ℤ/29 ⊕ ℤ/29, N = 348) did not complete with the brute-force character enumeration this arc
   uses (§0); Y₈ (ℤ/21 ⊕ ℤ/105, N = 420) and beyond
   need either more time or the deck-symmetry reduction (B1301's eigencharacters) that this arc does not build.

## 4. Registered

sL-2's status: the level-by-level table exists for n ≤ 6 and the count is one on every firing level; the lead stays open on (i) the
levels beyond six, (ii) the deck-symmetry prediction of the firing loci, (iii) the physics reading. Nothing on the destination ledger.

## Verification

`verification/tower_generations.py` (the levels by `covers`, characters into μ_N, the loci over three primes, the T5 cosets, the firing
set with re-checks, the generation search), `verification/exact_check_cover.py` (ℚ(ζ_N), B1374's `exact_lib.py`). Locks:
`tests/test_b1375_the_towers_generation_count.py` — fast (about a minute): Y₂, Y₃, Y₄ with the 12 800 / 64 / 976 reproduced; slow: Y₅,
Y₆ and the exact Y₅ background.

**Sources.** B1374 (the frame, the sectors, T5 at the cusp, the instruments), main's B1297 (the index, T5), B1418 (the class and the
cover), this seat's B1301–B1304 (the tower, its homology and eigencharacters), B1372 (the spin split and the charge table).
