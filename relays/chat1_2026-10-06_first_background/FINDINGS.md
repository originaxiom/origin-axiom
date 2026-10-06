# The first level with a background is not a family law: level 3 is what the smallest roots do (chat1, 2026-10-06)

Two seals: `PREREGISTRATION.md` (sha f090ecd4, commit df6dfec5) and `PREREGISTRATION_2_ORBIT_LAW.md` (sha c3c9f330,
commit 6cd612d1, written after and because of the first seal's data). Instrument: B1432's census imported unchanged, the
levels built directly as bundles of φⁿ (construction 24/24 against SnapPy; golden+ levels named m004, m206, s961,
t12839, o10_150696, otet12_00013). Every cell agrees at three primes (56 + 20 cells, 0 differing).

## Scored

| | prediction | prior | outcome |
|---|---|---|---|
| C1 control | golden+ L1–5 = B1432 | 85% | **HOLDS** exactly: firing 0/8/72/488/2200, backgrounds 0/0/48/256/400, orbits 3/4/5, s961 none lifted |
| R | first background at ord(A mod 2): golden± 3, silver± 1, bronze± 3 | 20% | **KILLED** by silver− (first background at L3, 144, predicted 1) |
| R0 | same first level on all six roots | 25% | **KILLED** by silver+: first background at L4 (320, orbits of 4, all lifted); the other five at L3 |
| Q1 | no background at level 1 or 2 on any of 26 sample roots | 65% | **KILLED**: backgrounds at L1 on ILLRLR (8), ILLLRLR (16), ILLRLLR (16); at L2 on nine more roots |
| Q2 | every background in a deck orbit ≥ 3 | 60% | **KILLED**: orbits of 1 and 2 throughout (`orbit_law_run.txt`) |

## The six metallic roots, complete

| root | L1 | L2 | L3 | L4 | first |
|---|---|---|---|---|---|
| golden+ = m004 | 0 | 0 | 48 | 256 | **3** |
| golden− = m003 | 0 | 0 | 96 | 256 | **3** |
| silver+ | 0 | 0 | 0 | 320 | **4** |
| silver− | 0 | 0 | 144 | — | **3** |
| bronze+ | 0 | 0 | 1584 | — | **3** |
| bronze− | 0 | 0 | 720 | — | **3** |

In the three acts' own walks (the + roots; orientable tick 2n = level n): golden and bronze first carry a background at
tick 6, silver at tick 8. The silver act is the one that reduces to the bare mirror at 2 (listening log); whether that
is why it is late is not tested and not claimed.

**Run notes.** The first heavy runs died with a container restart (no output; nothing claimed from them). The reruns use
`fast_census.py` (one index per deck orbit where h¹ = 1 — exact, since the deck is a self-homeomorphism; validated 6/6
against full cells) and `short_cover.py` (the level as the root's cyclic cover with short relators; torsion 21/21,
census 6/6). bronze+ L3 at primes 5077/5113/5437: 960 rechecks disagree (a bad prime, B1432's p = 1721 kind); rerun at
20089/20161/20233: 0 disagree, firing 29 176 (vs 29 608), backgrounds 1584 in both. The agreeing set is the one reported.

## The table that replaces the rules (first level with a background, 21 distinct roots; powers LRLR, LLRLLR omitted)

| first level | roots |
|---|---|
| 1 | ILLRLR, ILLLRLR, ILLRLLR |
| 2 | ILRLR, LLLRR, ILLLRR, LLRLR, LLLLLR, ILLLLLR, LLLLRR, ILLLLRR, LLLRLR |
| **3** | **LR (m004), ILR (m003)**, LLR, LLLR, ILLLR, ILLRR (silver−) |
| **3** (heavy cells) | LLLRRR = bronze+ (1584, orbits of 3, 288 lifted), ILLLRRR = bronze− (720, orbits of 3, 408 lifted) |
| **4** | LLRR = silver+ (L1–3 none; L4 320, orbits of 4, all lifted) |
| > 3 or open | ILLR (none through 3); LLLLR, ILLLLR (none through 2; L3 not run) |

**Reading, at the level the data carry.** Level 3 is not forced by the family: long words get backgrounds at levels 1
and 2, in orbits of 1 and 2. Level 3 is what the *short* words do — every decided root of length ≤ 4 except ILLR has its
first background at 3, none earlier. Golden (LR, trace 3) is the smallest hyperbolic monodromy there is; its sign twin
behaves the same. So the m004 fact "first background at the three-fold cover" is a fact of the minimal root, shared with
its nearest neighbours, not a law of the space. Whether that is a reason (the rule's minimality forcing a late first
background) or a coincidence of small arithmetic is not decided here. The "first background" principle itself remains a
postulate; this test only shows what it would select on each root.

**Fence.** Frame F-CI; objects 26 once-punctured-torus bundle roots and their levels ≤ 3 (≤ 5 golden); reach *class*
(the sample). No generation count on a vacuum, no value, no physics. Errors: R was fitted to golden — the first seal
existed to catch exactly that, and did.
