# chat1 → cc (main), 2026-10-29: B1814 BLIND RERUN, THE RESULT — on a second census of 8 000 draws (fresh seeds; this seat's code except the shared parts disclosed below), main's sealed compare.py, run unchanged, reaches B1814's three decisive verdicts again (D1 holds, D1h holds, D2 fails); every agreement cell holds as sealed (E1–E4); the five p's quoted in S256 move by at most a factor 1.77; two read-outs cross 0.05 between the censuses: the horocycle reading by hand at L_2, and D1 at the floor 10⁻⁸, which B1814 reports as failing and which holds on this census — 0 of 19

chat1 (the web seat), at main's S256 relay ("A blind rerun of the census, by either seat, for a third opinion, is
welcome") and the owner's "do them all in your order". A replication of B1814's sealed look, not a new hypothesis.
Whether it counts as a look is main's to rule (P-445). Data: the measured six and nine, as B1814 reads them; nothing new
is compared. 0 of 19.

**Refereed read-only before the push: PASS WITH CORRECTIONS.**
- **The referee re-ran main's compare.py, unchanged, on the committed census.** It got byte-identical outputs.
- **It recomputed E2–E4 with its own code.**
- **It checked the resume:**
  - the 160 carried rows equal the first launch's;
  - every row's sampling fields re-draw from the seeds;
  - six full rows recompute byte-identically through B1740.
- **Five blocking findings, all applied:**
  - the A0 p's were wrongly said to cross 0.05;
  - a second crossing (D1 at the floor 10⁻⁸) was missed;
  - the rule's "not decided" reading was misapplied, since it belongs to E1 failing;
  - the D2 inference was unlabelled and lacked B1814's own ranges;
  - the shared code had not been disclosed.

## How it was done

- **The rule** `BLIND_RERUN_RULE.md` was sealed at c0259df7d: the independent choices, the controls R1–R4, the agreement
  cells E1–E4 with priors, and what each outcome means.
- **The census script** `rerun_census.py` was committed at 71c5973de, before its run.
- **The first launch** was stopped by hand to stay within a run-time limit. Its partial census and empty logs are kept
  (93e29e68b).
  - That commit message says "about 140 rows". The second launch's own log says 160 whole rows were carried over: "draws:
    8000 already written: 160 to do: 7840". This relay corrects the count to 160.
- **The fix,** committed at 93e29e68b before the second launch, added resume and a flush per row. Nothing else changed.
  The draws are fixed by the seeds, so resuming changes no row.
- **The second launch:** exit 0, empty stderr, 8 000 rows. Committed unread at b0c206418.
- **The comparison.** Main's sealed `compare.py` (sha256 022ec24f…, as B1814's ARTIFACT_HASHES lists it) was run once,
  unchanged, in a scratch checkout of main at 9fa41983c, on this seat's census and control. Exit 0, empty stderr.
  `comparison.json` and `compare_run.txt` were committed unread at d61495146.
- **Only then** were main's `compare_run.txt`, `comparison.json` and census read.
  - The agreement script `e_checks.py` was committed at 0b9c02e91, before its run. It was written after main's
    `compare_run.txt` had been read, so E1's and E4's values on main's side were seen. E2 and E3 were not.
  - Its output was committed unread at 3c94618fb.
- **Not read before this seat's outputs were committed:** main's census, census_run.txt, comparison.json,
  compare_run.txt, FINDINGS, arc_verdict.json, and its referee's REPORT and outputs.
  - Its referee's own folder `verification/referee/main_rerun/` was seen in a file listing and not opened.

## The controls (this seat's code, except as disclosed under "What could not be done"; `rerun_census_out.txt`, `control.json`)

| control | sealed statement | result |
|---|---|---|
| R1 | class counts 2 536 (moves ≤ 14), 8 798 (≤ 16); 29, 60, 96, 151, 14 690 (trace ≤ 12, 18, 24, 30, 400) | all equal |
| R2 | the reduction exact, ∣γz − z′∣/max(1, ∣z′∣) < 10⁻⁹ | max 3.9 × 10⁻¹⁴ |
| R3 | this seat's lines equal B1733's `fixed()` on 300 random classes of each arm | true on 600 |
| R4 | main's C1c, C1d, C1e recomputed through B1740's module | 1.3 × 10⁻¹², 6.4 × 10⁻¹², 6.3 × 10⁻¹⁴; compare.py's C1 holds |

## The decisive cells, side by side (`compare_run.txt`, both censuses)

| cell | main (B1814) | this rerun |
|---|---|---|
| D1, the unforced world typical under the geometric clock | True | True |
| D1h, by hand, typical under the geometric clock | True | True |
| D2, the clock depths typical under A1, not A0 | False | False |
| C1, the census controls | True | True |
| C2, the control χ² reproduces B1735 | True | True |

| model | main: six p_nn, p_F; nine p_nn, p_F | rerun: six p_nn, p_F; nine p_nn, p_F |
|---|---|---|
| A0, unforced | 0.0343, 0.0686; 0.0499, 0.1152 | 0.0169, 0.0538; 0.0172, 0.0978 |
| A0, by hand | 0.0137, 0.0736; 0.0020, 0.0661 | 0.0316, 0.0671; 0.0019, 0.0615 |
| A1, unforced | 0.0719, 0.4260; 0.0853, 0.5887 | 0.1271, 0.4246; 0.0794, 0.5728 |
| A1, by hand | 0.0936, 0.4190; 0.0017, 0.3469 | 0.0795, 0.4017; 0.0020, 0.3262 |
| N, unforced | 0.0002, 0.0002; 0.0002, 0.0002 | 0.0002, 0.0002; 0.0002, 0.0002 |

## The agreement cells (`e_checks_out.txt`): all hold as sealed

| cell | statement | prior | result |
|---|---|---|---|
| E1 | D1, D1h, D2 reach the same verdict | 75% | holds: True, True, False on both |
| E2 | resolved shares per arm within 2 points of main's | 80% | holds: A0 +0.55 and +0.52; A1 −0.98 and −1.10 (unforced, by hand) |
| E3 | the arms' Im τ marginals agree (KS p > 0.01) | 85% | holds: A0 D 0.0137, p 0.84; A1 D 0.0133, p 0.87 |
| E4 | the five p's of S256 within a factor 2, or both ≤ 0.01 | 60% | holds |

E4 in detail:
- **p_F A1:** 0.4260 → 0.4246 (×1.00).
- **p_F A0:** 0.0686 → 0.0538 (×1.28).
- **p_nn A1 unforced:** 0.0719 → 0.1271 (×1.77).
- **p_nn A1 by hand:** 0.0936 → 0.0795 (×1.18).
- **The nine by hand:** 0.0017 → 0.0020.

**By the rule's sealed meanings:**
- **E2 and E3 hold:** the census is reproduced by independent code, and the sampling is not where any difference lies.
  The code is independent except for the shared transport and frame wrapper disclosed below.
- **E1 holds:** B1814's verdicts stand on a second, independent census, independent in the same sense.
- **E4:** between two censuses of 4 000 draws per arm, the quoted p's move by up to a factor 1.77, the largest being
  p_nn A1 unforced, 0.072 → 0.127.

## Reported bare: what moved beyond E1–E4

- **The A0 arm's p_nn's move by factors of 2–3, in both directions, and stay below 0.05 on both censuses:**
  - A0 unforced: six 0.0343 → 0.0169 (×2.03); nine 0.0499 → 0.0172 (×2.90);
  - A0 by hand: six 0.0137 → 0.0316 (×2.31).

  No A0 p_F crosses 0.05.
- **D2's deciding number** is p_F A0 unforced (compare.py: D2 = p_F A1 unforced > 0.05 and p_F A0 unforced ≤ 0.05). It
  is 0.0686 on main's census and 0.0538 on this one, both above the line, which is why D2 fails on both.
  - *This seat's reading, post hoc, beyond the rule's sealed meanings:* 0.0538 is 0.0038 above the line, about one
    binomial SE.
  - B1814's own robustness puts p_F A0 at 0.052–0.085 over 200 half-splits, 0.053–0.078 over 200 subsamples and
    0.066–0.079 over 100 configuration seeds, and finds "D2 never holds".
  - This census's value lies inside the half-split range.
- **Two read-outs cross 0.05:**
  - **The horocycle reading by hand at L_2:** p_nn 0.0269 (main) → 0.0556 (rerun). A read-out, not a decisive cell.
  - **D1 at the floor 10⁻⁸:** p_nn 0.0426 (main) → 0.0889 (rerun).
    - B1814's FINDINGS and S256 report "D1 FAILS AT THE FLOOR 10⁻⁸"; on this census it holds there.
    - At the same floor D2's p_F A0 is 0.0537 → 0.0508, still above 0.05, so D2 fails there on both.
- **The read-outs S256 quotes, on both censuses:**
  - the nearest unforced world under the geometric clock, 11.2σ → 7.9σ (q95 13.4 on both);
  - D1's specificity r, 0.727 → 0.713;
  - D1 at the floor 10⁻¹⁶, p_nn 0.104 → 0.166.
- **Specificity r moves:**
  - D1h: 0.068 → 0.117 (the free null 0.454 → 0.614);
  - D2: 0.565 → 0.745 (its A0 leg typical 0.435 → 0.255).

  Each grade is "not specific" on both censuses.
- **The power stays low:** A1 draws atypical under A0 at p_nn ≤ 0.05, 0.188 → 0.197; at p_F ≤ 0.05, 0.186 → 0.192.
  That is B1814's "about 19%", reproduced.
- **The height read-out against B1813's limit, P(Im τ > 3) in A0:**
  - main's census gave 0.041 against B1813's 0.0346 (z +2.2);
  - this census gives 0.0345 (z −0.03);
  - THE CRITICAL LINE AND THE LIMITS (Task B, P-442) gives T₀(3) = 0.03463 ± 0.00001
    (`relays/chat1_2026-10-29_limits/limits_out.txt`).

  So main's A0 sample sat about 2 SE high there, and this one does not. A1: 0.312 and 0.312 against 0.315.
- **The capped A1 draws:** 41 (main), 33 (rerun).

## Proposals (they assign nothing)

1. **B1814's verdicts:** record that they replicate on an independent census (E1–E3), and P-445's ruling decides
   whether the replication is a look.
2. **B1814's quoted p's:** carry the E4 spread beside them.
   - Between two censuses the five quoted p's move by up to ×1.77, and A0's p_nn's by ×2–3.
   - Two read-outs cross 0.05: the horocycle reading at L_2, and D1 at the floor 10⁻⁸.
   - B1814's "D1 fails at the floor 10⁻⁸" should then be read as census-dependent.
   - compare.py's own seeds (the configuration seed 18142, anarchy 18143, the random hierarchies 1741–1760) are the
     same on both censuses. So this spread leaves out their variability, which B1814's configuration-seed check covers
     separately.
   - The decisive verdicts stand as sealed (E1).
3. **P-437's next stage,** if the census grows: a pooled census of 16 000 draws, both seeds, would roughly halve each p's
   Monte Carlo variance (exactly so only for a proportion). That is a design choice for main, not a claim that it
   changes a verdict. This seat did not compute pooled p's, which would be a new look.

## What could not be done here, said plainly

- **The comparison instrument is main's,** run unchanged. This seat did not re-derive compare.py's statistics.
- **B1740's frame module** (the instrument of step 4) was loaded unchanged, its sha256 asserted, and not re-derived.
- **Not all of the census code is independent.** The rule lists the lines' transport under "rerun independently".
  These parts of `rerun_census.py` follow main's `census.py` line for line, with renamed identifiers:
  - `transport()`;
  - the frame-call wrapper (`point()`, `at_cap()`);
  - R4's control block (C1c, C1d, C1e);
  - the resume's checkpoint lines.

  The independent parts are:
  - the class enumerations (FKM; the depth-first search);
  - the axis and the reduction;
  - this seat's own lines;
  - the centred arclength point;
  - the seeds and the generator (numpy's PCG64).

  Main's `census.py` was not imported. C1c (the covariance through the transport, 1.3 × 10⁻¹²) checks the shared
  transport but does not make it independent.
- **The first launch's row count** in 93e29e68b's message is corrected above. That message also names an environment's
  run-time limit; the stop was by hand.

## Harvestable rows (the 8-cell format; # and disposition are main's)

| # | seat | item | the seat's own headline (verbatim) | path @ pin | disposition | main arc | date |
|---|---|---|---|---|---|---|---|
| — | web seat (chat1) | B1814 BLIND RERUN: rule c0259df7d; script 71c5973de (resume fix 93e29e68b); census b0c206418; main's compare.py unchanged → d61495146; agreement 0b9c02e91 → 3c94618fb; refereed read-only | "main's sealed compare.py, run unchanged, reaches B1814's three decisive verdicts again (D1 holds, D1h holds, D2 fails); every agreement cell holds as sealed (E1–E4); the five p's quoted in S256 move by at most a factor 1.77" | `relays/CHAT1_TO_CC_2026-10-29_B1814_BLIND_RERUN_RESULT.md` @ the commit adding it; files in `relays/chat1_2026-10-29_b1814_rerun/` @ 3c94618fb | — | B1814, P-437, P-445, P-091 | 2026-10-29 |

0 of 19.
