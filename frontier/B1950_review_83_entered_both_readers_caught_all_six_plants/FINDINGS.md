# B1950 — Review 83 entered: both readers caught all six plants, and their findings include errors in main's mathematics

**Verdict: PROVED (a process arc).** Main, 2026-11-17. Register row P-858. 0 of 19.

## Seen first

- **Swept:** `VERDICT topic-sweep /Review 83|plant|reading copy|recused/: 47 of 1691 arcs on main match (NEGATIVE 1, OPEN 2, PROVED 43, RETRACTED 1); 62 register rows match (DECLINED 1, DONE 22, QUEUED 39)` — the earlier reviews' entries (B1898, B1916, B1931) and their planted readings.
- **The literature:** none applies; this is a review of the record's own window, read by sessions that built none of it.

## What was read

- **The window:** main's work from 73e71e277 to c8cece9be: B1904 as built, B1930 to B1944, the sweep, register rows P-849
  to P-858, and harvest rows 1799 to 1827.
- **The reading copy:** review-83/read at b35eac607, which is main's head of 2026-11-15 with six planted faults.
- **The readers:** agy-exp (harvest row 1844) and agy-002 (row 1843), sessions of the other model family. Each read the
  window in full, built none of it, and recused itself from its own lines.
- **Quotations** (`verification/quote_check.py`): every quotation main's check could parse is exact in the reading
  commit: agy-002's 28 of 28 and agy-exp's 20 of 20. *[Added 2026-11-18, Review 84: no output of this check was committed; it is now (`verification/quote_check_run.txt`, rerun today). "Exact" here means present, whitespace-normalised, somewhere in the window's text at the reading commit, not at the path the reader cited; and the check can be rerun only while that commit exists.]*

## The plants (`verification/plants.json`, sha256 as published at the opening, b3da3d92…)

**Both readers caught all six.**

| plant | where | what was planted |
|---|---|---|
| P1 | B1940 | the largest log shift, 0.068 → 0.086 |
| P2 | B1942 | "evenly" → "each hit six times" (it is eight) |
| P3 | B1943 | Smith(LR + I) = (1, 5) → (1, 3) |
| P4 | B1938 | the control's max ∣z∣, 6.4 → 2.4 |
| P5 | B1941 | the minimum difference, +1.38 → +1.83 |
| P6 | B1944 | W₊∣b's ∣V_cb∣ ratio, 17.6 → 7.6 |

## The findings

agy-002 reports 31 and agy-exp 20. Six of each are the plants, and several of the rest coincide.

### Mended in this entry, each recomputed by main

*[Corrected 2026-11-18, Review 84: this heading named `verification/main_checks.py` for all eight. That script holds four of them (C1 to C4: RL's line, m003, the signed residues, the two frames at height 12). The reversal near τ = i had no committed output; it has one now (B1941's `verification/near_i.py`: −0.392 and −0.120 at 1.05i). The other three mends are of wording, a lock and two verdict files, and are held by the files themselves.]*

| finding | what was wrong | the mend |
|---|---|---|
| R83-20, F-R83-05 | B1943 and the theorem registry put RL on LR's line. LR fixes {k(1, 2)/5}; RL fixes {k(1, 3)/5} | B1943's page and script (each act's own line is now printed and held) and the registry's row |
| F-R83-07 | the scoreboard's S03 said SE1 selects m003 beside m004. m003 = −LR has torsion of order 5 | the scoreboard |
| R83-17 | B1941's "at every point" and "no measure can reverse it". The four draws at height 0.9 were rejected, so the sample spans 1.2 to 9, and at τ = 1.05i the determinant's difference is −0.39 | B1941's title, page and verdict, narrowed |
| R83-18 | the rule's A13 misstated B1941 ("under every declared change but one") | a dated note in the rule |
| R83-19 | B1940 blamed double precision for the exchange of ∣V₂₃∣ and ∣V₁₃∣ at height 12. The double and extended frames agree there on the three mixing moduli at x = 0.13 (0.4282, 0.4169, 0.5832 against 0.42815, 0.41689, 0.58318), though the double frame fails its own symmetry check at that height (1.2e-1) *[scoped so 2026-11-18, Review 84]*; the exchange is the real approach to the cusp limits | B1940's page |
| F-R83-11 | B1935's "acts as S₃" holds for the channels' moduli. The complex residues carry signs: under T, (R_i, R_j, R_k)/R_1 goes to (R_i, R_k, −R_j) | B1935's page, scoped |
| R83-11, F-R83-14 | B1938's lock compared signed differences without an absolute value | the lock |
| R83-26, F-R83-16, F-R83-17 | B1940's verdict file said "second computation owed" with no seat cited; B1944's named SM-C15 without citing it | both verdict files |

### Carried as action item R83-1 (to build, each checked by main)

- **Numbers and statements off their source:** R83-07 (B1932's mirror figure, shift and spread), R83-08 (B1904's passage
  placement), R83-09 and F-R83-13 (B1937's description of its lock), R83-21 and F-R83-15 (B1939's contradiction on V and
  its remark on B1935's phases), R83-22 (B1939's 1 + 4 lines across all members), R83-23 (B1905's summary), R83-24
  (B1938's "no figure uses unreduced ones"), R83-27 (B1932's statement beside a committed output), F-R83-12 (B1936's
  degree rule on the singlet), F-R83-19 (the sweep's claims).
- **Locks that cannot fail or that omit claims:** R83-10 (B1939), R83-12 (test_b734), R83-13 and F-R83-09 (B1932), R83-14
  (B1935), R83-15 (B1940), R83-16 (B1927; a duplicate test file), F-R83-10 (B1934's Weil phase), F-R83-20 (the waiver's
  test).
- **Stale statuses and travel:** R83-25 (B1937 stale at OPEN; S10, S20), R83-28 and F-R83-08 (the scoreboard's generator),
  R83-29 (the scoreboard's changes did not travel), R83-30 (harvest pins), R83-31 (THE_CLAIM's unconditional DERIVED on
  the global form), F-R83-18 (B1933's verdict names).

## What it teaches

- **The readers found errors in main's mathematics, not only in its bookkeeping.** RL's line, the reversal near τ = i and
  the signed action on the residues are statements of results. Each was caught from the page and its script, and each is
  confirmed on main's own code.
- **Two of them were hidden by main's own instruments:** a print gated on one case (B1943), and a sample whose lowest
  draws were all rejected (B1941).

## Carried from Review 82

R82-1 to R82-5 and R81-1 to R81-10 are carried once more. The builder's session is paused at the author's word.
