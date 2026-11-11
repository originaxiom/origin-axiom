# Review 79 — the SM seat's reading (card SM-R79)

*Read at main 323f923278181ffbe69f8c3124182549ab0e3163, the commit the listener printed with M3. The rules are § 13
of the protocol. Card: `relays/cards/SM_R79_review-79-seven-arcs-five-locks.md`. The outputs this file relies on are in
relays/sm_r79/, committed before it. No other session's Review 79 file was opened before this one was pushed. No
measured value was read or compared, and no held-out target was computed. B1882's random targets are random only.*

## How the reading was done

- **Six arcs were read in full,** as git objects at the commit above: findings, verdict file, scripts, outputs, locks,
  and the sources they cite where a claim had to be held against its source.
  - Three readers within this session took two arcs each. Every finding below was then checked again before entry:
    each number by this seat's own code, each statement against the files.
  - The arcs' own scripts were also run from a scratch extraction. Each reproduces its committed output. That is not
    independent evidence, and no finding rests on it.
- **Every quotation was checked by machine** against its file at the commit: 63 quotations, 63 found
  (relays/sm_r79/quote_check.json). The check's control is the first quotation altered by one character, and it is
  reported missing.
- **Recomputations** are in relays/sm_r79/r79_checks.py and relays/sm_r79/b1885_euclid_max.py, with their outputs.
  Each number recomputed there is recomputed independently, for that number. B1885's maximum uses B1885's own f, so
  only the maximisation is independent.
- **Categories** are those of § 13: (1) a statement its outputs do not support; (2) a number that differs from its
  source; (3) a claim wider than what was computed; (4) a check that cannot fail, or a lock that pins a value; (5) a
  correction that did not travel; (6) something owed that no register row carries; (7) a label stronger than its
  evidence; (8) the owner quoted after 2026-11-11, a session as an authority, or a vendor's or model's name.
- **Minor** marks a finding that changes no conclusion of its arc.

## B1889 — left to another reader

B1889 (the seats digested) judges this seat's own record: its SM reading, verification/readers/reader_G1_sm.txt, and
the SM rows of SEATS.md. Under § 13 it is named here and left. It was not read.

## B1879 — the weave's theorems with the exchange (10 findings)

**R79-SM-01** (1). FINDINGS.md, § 8:
- `The square of the tick, which is the root, is one of the`
- **What is wrong:** the run counts only histories that are not a power, and lists them. FF is a power of F, so it is
  not among the thirteen and not among the eleven. The run's own heading says
  `histories (cyclic words in L and F with at least one F, not a power): 13`.
- **How known:** verification/only_the_tick_run.txt, read against the sentence.

**R79-SM-02** (3). FINDINGS.md, § 2, the walk's row:
- `**unchanged, exactly.** A run has length r with probability 2⁻ʳ in the grammar of L and the tick`
- **What is wrong:** what was computed is the law of run lengths, with no step back. The map's node W:WALK, which the
  row answers, holds the measure at every strength of the pull-back:
  - `singular to area, at every strength of the pull-back.`

  Pull-back strengths were not computed.
- **The two grammars also differ where the walk goes.** Rewrite a word in L and F = L·P as an L/R word times a power
  of P, using P·L·P = R. Then every one of the 4,096 words of length 12 begins with L, where L and R begin each way
  2,048 times. The run law is the same in both grammars.
- **So:** "unchanged" holds for run lengths. As the law of the walk's point it is not shown: every word of the new
  grammar begins with L, so its point lies on L's side, where L and R put half the weight on each side.
- **Travelled:** the same wording stands in GENESIS (see R79-SM-10) and in the claim line.
- **How known:** relays/sm_r79/r79_checks.json, block B1879. W:WALK's text is in
  frontier/B1858_the_closure_map/NODES.json.

**R79-SM-03** (4). FINDINGS.md, § 2:
- `each of the 22 histories of an odd number of runs to 7 letters has one end`
- **What is wrong:** a bundle over the once-punctured torus has one cusp by construction, whatever its monodromy. The
  check cannot fail, and it tests nothing that the exchange could change.
- **How known:** the construction (the fibre has one puncture, so the mapping torus has one cusp). The script checks it
  with SnapPy.

**R79-SM-04** (4). verification/test_b1879_the_weaves_theorems_with_the_exchange.py:
- `"the two acts: 96 elements, two pieces", "with the exchange: 192 elements, one piece",`
- **What is wrong:** the lock looks for these and other results as printed strings in the committed run. These are the
  group orders, the indicator, the end count and the tick's fixed set. Only the walk law and the short histories are
  recomputed in the lock.
- **Consequence:** a change of the script's computation that is not rerun passes the lock.
- **How known:** reading the lock. The B1879 reader planted a wrong group count in a scratch copy: the script failed
  and the lock passed (9 tests).

**R79-SM-05** (4, minor). verification/weave_with_the_exchange.py, part 5:
- `say("    %-22s fixes %s" % (name, want))`
- **What is wrong:** the fixed locus of each mirror is computed, and then the typed `want` is printed in its place.
  Nothing is asserted.
- **The same part also says:** `with i and the cube root of unity at their corners`. The corner of the modular triangle
  on Re τ = ½ is e^{iπ/3}, a primitive sixth root of unity, whose cube is −1.
- **How known:** reading the script.

**R79-SM-06** (7). FINDINGS.md, Seen first:
- `The expectations were written before computing,`
- **What is wrong:** the script's header carries the outcomes beside the expectations, e.g.:
  - `E1  the two characters the two moves fix (the trivial one and the quaternion point) are fixed by the exchange too  -- holds`

  Script, run and findings entered the record in one commit (660ade4f3).
- **So:** nothing on file shows the expectations came first. The label the evidence supports is "computed once", not
  "expectations committed first".
- **How known:** git log of the arc at 323f92327.

**R79-SM-07** (7, 8, 5). FINDINGS.md, § 8, the dated addition:
- `The advisor seat recomputed every statement of this arc that can be computed, with its own code`
- **What is wrong:**
  - A seat's check is stated as fact ("All of it agrees"), with its evidence on that seat's branch (`7726eeed`) and
    not on main.
  - "Checked by the advisor seat" is not a § 12 label. Main holds nothing that would earn "recomputed independently"
    for every statement.
  - The verdict file was not updated with the addition: `"cites_seat": [],`.
- **How known:** the arc's files at 323f92327. The cited commit is not in main's history.

**R79-SM-08** (5). FINDINGS.md, line 3:
- `The owner has ruled that the tick is an act`
- **What is wrong:** WORKING_RULES.md re-types that answer:
  - `the tick as an act is a supposition and was handled by computation`

  Its point 3 says such an item is never recorded as the owner's ruling.
  - The re-typing entered at bc18dd91a (10:46). The arc was edited after it, at 9b1c9d408 (11:27, the dated § 8).
  - Its opening still records a ruling, as does § 7.
- **How known:** git log -S on both files at 323f92327.

**R79-SM-09** (3). FINDINGS.md, § 1:
- `The chiral three, whose sign is the hand, has no sign left at the level of the weave.`
- **What is wrong:** the arc's own § 2 says of this row:
  - `argued from the two rows above; the index itself is not recomputed here`

  The answer-first line states as a result what the arc argued and did not compute.
- **How known:** the arc's § 2 table.

**R79-SM-10** (5, 3). GENESIS.md, GM5c, v1.65 (a), a page this arc fed:
- `every statement the record holds about the weave is unchanged except the hand`
- **What is wrong:** B1879 says `**Most of what the record holds about the weave is unchanged**`. It did not restate
  two negatives (W:NOVAL, W:DRAW), and the group's order changes as its own statement says. The foundation's
  sentence is wider than the arc. It also carries R79-SM-02's "the walk's measure" as standing.
- **How known:** GENESIS.md and B1879 at 323f92327.

**Could not check (B1879):**
- The advisor seat's code and the web seat's card are on their branches, not on main.
- The repo-sweep counts in "Seen first" record no query.
- The index ±3 under the exchange is computed neither by the arc nor here.
- The two negatives that compare with measurement are outside the firewall.
- The exchange's lift phase. The arc and this reading make no claim about it.

## B1881 — the whole and the value, verified (8 findings)

**R79-SM-11** (2). FINDINGS.md, § 5:
- `B1872 writes columns, the mark (1, 2) and the`
- **What is wrong:** the sentence goes on "ground [[2, 1], [1, 1]]". B1872's own run uses the ground LR mod 5 =
  ((1, 1), (1, 2)) and the mark ±(1, 3): `the line is +-(1, 3) and its twin +-(2, 1)`. The same attribution stands in
  the script's docstring.
  - B1881's conclusion, one allowed set in both conventions, is not touched by this. B1872's actual convention also
    agrees.
- **How known:** B1872's verification/together_facts.py and its run at 323f92327.

**R79-SM-12** (2, minor). FINDINGS.md, Disclosed:
- `Main read both relays about ten hours after the first was pushed`
- **What is wrong:** the source cited beside it, B1880 § 6, is `## 6. How a re-audit sat unread for eight hours`. It is
  about re-audit 3, not the two relays, and its figure is eight hours.
- **How known:** B1880's FINDINGS.md at 323f92327.

**R79-SM-13** (4). verification/whole_and_value_on_main.py:
- `the mirror normalises the group: [[a,b],[5c,d]] -> [[a,-b],[-5c,d]]", True, "an identity of matrices")`
- **What is wrong:** the check is passed the literal True. So is
  `increase without bound: 5m/2 + sqrt5/2 for the run of 5m + 1", True,`.
  Both are counted in "65 checks, none failing".
- **How known:** reading the script.

**R79-SM-14** (1, minor). verification/whole_and_value_on_main.py, the mended check E11:
- `The check now asks what the relay says.`
- **What is wrong:** the mended check asks that the offset print as "0.92", a figure main computed and typed. As the
  comment beside it says, the relay prints "nearly one percent". The check asks for main's number, not the relay's
  words.
- **How known:** reading the script.

**R79-SM-15** (4). verification/test_b1881_the_whole_and_the_value_verified.py:
- `index, cusp widths and elliptic points, by a count written apart from the script's: orbits of matrices mod 5`
- **What is wrong:** the lock recomputes the index (10 and 20 of 120). The cusp widths and the elliptic counts are
  compared with the committed JSON. The genus line is arithmetic on typed constants. The docstring promises a
  recomputation of all three.
- **How known:** reading the lock.

**R79-SM-16** (7). FINDINGS.md, Disclosed:
- `The expectations were written before the run,`
- **What is wrong:** script, run, JSON and findings entered together in one commit (bc18dd91a), with no earlier commit
  of the header. The label the evidence supports is "computed once".
- **How known:** git log of the arc at 323f92327.

**R79-SM-17** (3, minor). FINDINGS.md, § 4:
- `Over all 16,275 cyclic run sequences of even length to 6 with runs to 5, the least`
- **What is wrong:** 16,275 = 5² + 5⁴ + 5⁶ is the number of tuples. Up to rotation there are 2,815 cyclic sequences.
  The minimum is unaffected.
- **How known:** relays/sm_r79/r79_checks.json, block B1881 (necklace count).

**R79-SM-18** (5). docs/POINT_REGISTER.md, row P-776, Q1:
- `AGREED WITH THE WEB SEAT and to be carried onto the map's node T:NO-PLACE at the map's next change`
- **What is wrong:** the note entered at bc18dd91a (10:46). The map's NODES.json then changed at 9b1c9d408, 9ace774f4,
  78f6e829f and 57f604898. At 323f92327 the node T:NO-PLACE carries no note on the flat-fibre instrument and no
  mention of B1881.
- **How known:** git log of frontier/B1858_the_closure_map/NODES.json, and the node's JSON at 323f92327.

**Could not check (B1881):**
- The seats' digits, timings and sweep are on their branches.
- The literature facts the arc takes as given (§ 7) were not re-derived.
- Whether the state is the lowest and simple (P-783): neither the arc nor this reading computes it.

## B1882 — the V1 card, run on main (10 findings)

**R79-SM-19** (2, 7). FINDINGS.md, Seen first:
- `the finding itself was reproduced on main in B1870 before the card existed.`
- **What is wrong:** B1870 left V1 open: `| V1 | every specificity null has an unpriced window | OPEN, not checked |`.
  - The card's own PREREGISTRATION.md gives main's state as "OPEN, not checked".
  - The same page later calls B1870 "the finding as main reproduced it".
- **How known:** B1870's FINDINGS.md and the card at 323f92327.

**R79-SM-20** (2, minor). FINDINGS.md, § 2:
- `The threshold for A is 133.3 targets for the first null and 134.6`
- **What is wrong:** the second null's top layer holds 15/223 of the rows, so 2rn = 134.53, not 134.6. The figure
  comes from the rounded share 0.0673.
  - The margin beside it, less than one target, still holds: 134 against 134.53.
- **How known:** relays/sm_r79/r79_checks.json, B1882.threshold_2rn.

**R79-SM-21** (2, minor). FINDINGS.md, § 2, the 1% table:
- `| first null, worst factor, seat | 1.46 [1.37, 1.55] |`
- `| second null, χ², seat | 1.90 [1.80, 2.00] |`
- **What is wrong:** the exact intervals over r are [1.36901, 1.54453] and [1.80501, 2.00112]. To two places they
  are [1.37, 1.54] and [1.81, 2.00]. The third row is right. This seat's Clopper–Pearson agrees with the script's
  intervals.
- **How known:** r79_checks.json, B1882.intervals_at_1pct.

**R79-SM-22** (2, minor). PRE_RUN_NOTE.md:
- `Five interval endpoints differ in the sixteenth digit.`
- **What is wrong:** six interval endpoints differ between card/v1_controls.json and
  the_seats_stage_1/v1_controls.json. One of them (0.720878058462825 against 0.7208780584628247) already differs in
  the fifteenth significant digit. The note's point, that the two machines are not bit-for-bit the same, stands.
- **How known:** r79_checks.json, B1882.control_files_interval_endpoints_differing.

**R79-SM-23** (3). FINDINGS.md, § 1:
- `Those are targets that fit nothing.`
- **What is wrong:** the sentence is about the one random target in five whose best row is in the top layer. For the
  first null that is 205,881 of a million. Of these:
  - 5,925 are in the best 5%, 1,049 in the best 1% and 111 in the best 0.1%;
  - in each of those tails the top layer still holds 1.57 to 1.78 times its share of the rows.
- **What the outputs support:** the excess over that rate comes from less well fitted targets. They do not support
  that those targets fit nothing. The card prints no value of a fit statistic, so "fit nothing" is not measured.
- **Travelled:** the sentence also stands in the verdict file and in B1726's dated note.
- **How known:** r79_checks.json, B1882.N1_top_layer_hits_by_tail.

**R79-SM-24** (3). FINDINGS.md, § 1:
- `Among well-fitted targets the last layer is below its neighbour.`
- **What is wrong:** the sentence is unscoped. It holds at 5%, 1% and 0.1%. In the best 0.01%, the depth at which the
  card says the second null's decisive cell was read, the last layer is above its neighbour in two of three cells:
  - the first null: 17 hits against 10 (2.55 against 1.50 of their shares);
  - the second null under χ²: 17 against 18 (2.53 against 2.51).
- **Caveat:** these counts are small. They neither confirm nor refute the claim, and the sentence should name its
  depth.
- **How known:** r79_checks.json, B1882.last_two_layers.

**R79-SM-25** (7). FINDINGS.md, § 1:
- `The audit's figure is reproduced, and it is not about rarity.`
- **What is wrong:** the audit's 20% had no tracked source and named no null (B1870), so nothing of the audit's was run
  again. What was computed is a share falling in a window written beforehand:
  - 20.6% for the first null's top layer;
  - three of the six preregistered candidates in 17% to 23%.
- **So:** the evidence supports "computed once" with "expectations committed first", not "reproduced".
- **How known:** the card's § 6, B1870's V1 row, and r79_checks.json.

**R79-SM-26** (3, minor). FINDINGS.md, § 3:
- `| second null, worst factor, free | 2.36 | 2.00 | **A** |`
- **What is wrong:** at 1% this read-out reads A by 2.7 targets in 10,000 (1,348 against a line at 1,345.29; ratio
  2.004). The page gives the decisive B cells their margins and its own two-machine caveat. It states the A read-outs
  "at both depths" with neither.
- **How known:** r79_checks.json, B1882.free_menu_wf_at_1pct.

**R79-SM-27** (4). verification/test_b1882_the_v1_card_run_on_main.py:
- `def test_the_arc_says_what_the_cells_read_and_no_more():`
- **What is wrong:** the test asserts only that phrases are present, so it cannot fail when the arc says more.
- **The page's numbers are not read by any test.** The margins test compares the hash-pinned JSON with literals typed
  into the test. R79-SM-20 to 22 pass the lock.
- **How known:** reading the lock.

**R79-SM-28** (6, minor). FINDINGS.md, § 7:
- `are not measured: B1798's, B1839's and B1841's.`
- **What is wrong:** register row P-786 carries the count owed on B1841's null only. No row carries V1 for B1798's or
  B1839's nulls, which the card says the finding still covers, unmeasured. The card also says its seat does not press
  them, so this may be a choice. If so, it is a choice no row records.
- **How known:** docs/POINT_REGISTER.md at 323f92327.

**Could not check (B1882):**
- The seal commits named in the card are not in main's history. "Unchanged since the seal" rests on the hash list in
  the same folder.
- The million-target run was not rerun. The random-target generator was not opened.
- § 5's "a fraction, not an order of magnitude" for a quoted rarity would need a rarity read on measured targets. That
  is outside the firewall.

## B1884 — what level a ground names, verified (4 findings)

**R79-SM-29** (5). The old sentence, in docs/POINT_REGISTER.md (P-738, and in P-736) and elsewhere:
- `LR fixes a point of P¹(ℤ/N) only at N = 5, the ramified prime's double root`
- **What is wrong:** B1884's own table shows:
  - `Exactly one at N = 5 and at no other N. Two at 11, 19, 29, 31, 41, 55, 59, 61, 71, 79, 89, 95 and on; none elsewhere`

  So LR keeps points of P¹(ℤ/N) at other levels: at N = 11 it fixes (1, 4) and (1, 8), rows as vectors.
  - The old sentence was true of N = 2 to 5, the levels B1853 computed. It stands unscoped in P-736, P-738, B1853's
    verdict line and `  - **LR fixes a point of P¹(ℤ/N) only at N = 5.**` (CHANGELOG.md).
  - B1884 uses P-738 and adds no note to it.
- **How known:** r79_checks.json, B1884.LR_fixed_points_of_P1_ZN_to_30: N = 5, 11, 19, 29.

**R79-SM-30** (3). verification/ground_level_on_main_run.txt:
- `G2 rho is multiplicative on the N to 200 that are products of two coprime parts`
- **What is wrong:** the check tries both parts only up to 14. That covers 47 of the 139 levels to 200 that have a
  coprime factorisation, and the first missed is 34.
- **How known:** r79_checks.json, B1884.covered_by_parts_to_14.

**R79-SM-31** (4). verification/test_b1884_what_level_a_ground_names_verified.py:
- `assert len(checks) == 17 and all(checks.values())`
- **What is wrong:** the seventeen checks are read from the committed JSON, not rerun. A change to G5 that is not rerun
  passes. The B1884 reader planted one in a scratch copy: the script reported FAILING: 1 and the lock passed.
- **How known:** reading the lock.

**R79-SM-32** (7, minor). FINDINGS.md, § 1:
- `17 checks, none failing, on the first run.`
- **What is wrong:** the section opens "Every prediction of the card is reproduced". These are recomputations with
  main's own code, which § 12 calls "recomputed independently". The seventeen also include main's own G5, which is
  not one of the card's predictions.
- **How known:** the script's own labels.

**Could not check (B1884):**
- The web seat's card is on its branch.
- The repo-sweep counts record no query.

## B1885 — the golden state on the whole, verified (7 findings)

**R79-SM-33** (1, 2). FINDINGS.md, § 3.5:
- `and near the peak that is greatest 0.057 away, at ∣z∣² = 0.163, off the circle.`
- `Main's grid reproduces its figure of 0.056.`
- **What is wrong:** main's grid printed 0.0569 from the peak, at ∣z∣² = 0.163. The continuous maximum of f²/y² near
  the peak is 0.05585 from it, at ∣z∣² = 0.16432.
  - The value there is 1.00018 times the grid point's.
  - So the seat's 0.056 is right, and main's 0.057 and 0.163 belong to the grid point.
  - The grid's 0.0569 does not "reproduce" 0.056.
- **Travelled:** 0.057 and 0.163 also stand in register row P-776, the verdict file and the handoff to the web seat.
- **How known:** relays/sm_r79/b1885_euclid_max.py and its run. f is B1885's own; Newton on the gradient starts from
  the grid's point.

**R79-SM-34** (1, minor). FINDINGS.md, § 2:
- `Main's run prints exactly 0 there.`
- **What is wrong:** the run prints a value, 0.0, only for x = 0. On x = ½ the check is a threshold, f is very small
  but not exactly 0, and nothing is printed.
- **How known:** the script's H3 check and the run.

**R79-SM-35** (4). verification/golden_state_on_main.py:
- `so f vanishes at i/sqrt5 if s = -1; and it vanishes at 1/2 + i/(2 sqrt5), which lies on x = 1/2`
- **What is wrong:** i/√5 lies on x = 0, where every term of the sine series is exactly 0, so the check cannot fail.
  The second point is defined and never evaluated.
- **How known:** reading the script.

**R79-SM-36** (2, minor). FINDINGS.md, § 5:
- `Its last six printed digits are not the peak's.`
- **What is wrong:** that holds for the real part. For the imaginary part the number is seven.
- **How known:** the lane's point as quoted in B1885, against the arc's peak.

**R79-SM-37** (1). FINDINGS.md, § 5:
- `Main has not read the lane's files.`
- **What is wrong:** the harvest ledger records main reading some of them, in rows entered before B1885 (at 9b1c9d408):
  - row 1677: `READ AT NAME LEVEL, AND THE HEAD OF ONE SEALED PAGE THROUGH THE MASK`;
  - row 1676: the lane's relay, read in full through the mask.
- **How known:** docs/HARVEST_LEDGER.md at 323f92327, and git log -S.

**R79-SM-38** (7). arc_verdict.json:
- `"verdict": "PROVED"`
- **What is wrong:** part of what the arc states is, in its own words, `**Found, by a grid and not by a proof:**`: the
  greatest place is one pair and no more.
  - The verdict covers it without that distinction.
  - The script's header of expectations entered in the same commit as its run (f4ff1fa1f).
- **Caveat:** the PROVED vocabulary is older than § 12. Main may read it as it does "verdict".
- **How known:** the arc's files and git log at 323f92327.

**R79-SM-39** (2, minor). arc_verdict.json:
- `"domain": "30-digit arithmetic; a grid of 99 by 205 points of the strip`
- **What is wrong:** the grid, A4 and A5 run at 18 digits. The script sets mp.dps = 18 for them and returns to 30
  after.
- **How known:** reading the script.

**Could not check (B1885):**
- The seats' digits and the sweep commit's counts are on their branches.
- That the state is the lowest and simple (P-783).
- The literature facts the arc names: continuous spectrum, a ground state of one sign, Selberg's bound.

## B1887 — the loop check, verified (4 findings)

**R79-SM-40** (3, 1). FINDINGS.md, § 3:
- `Two even lattices of determinant 1 are left out by it: E₈ + E₈, because it is`
- **What is wrong:** the domain is the irreducible root systems of rank 1 to 24. Besides E₈ + E₈ and D₁₆⁺ in rank 16,
  it leaves out all 24 even unimodular lattices of rank 24 (Niemeier).
  - For example D₂₄⁺ is even, of determinant 1, and its glue coset's least norm is 6, so its roots are those of D₂₄
    only. That is the reason the page gives for D₁₆⁺.
  - E₈ + E₈ + E₈ and the Leech lattice are also left out.
  - The same "two" stands in the verdict file, in register row P-781 and in the script's docstring.
  - The arc's main result, that E₈ is the only one of the 95, is untouched.
- **How known:** r79_checks.json, block B1887 (D₂₄⁺). The count of 24 is Niemeier's classification, a standard result
  that was not recomputed here.

**R79-SM-41** (4). verification/loop_check_on_main.py, check "M4 by hand":
- `(3 * 1) % 5 == 3 and (3 % 5, (-1) % 5) == ((3 * 1) % 5, (3 * 3) % 5)`
- **What is wrong:** the expression is built from integer literals only and cannot fail. It is counted among "35
  checks, none failing". The mathematics behind it, J(1, 3) ≡ 3(1, 3) mod 5, is right.
- **How known:** reading the script.

**R79-SM-42** (7, 3). FINDINGS.md, § 1:
- `Every cell the web seat asked for reproduces on main's own code, by another route:`
- **What is wrong:** for the manifold cells, main's numbers come from SnapPy's own routines: the symmetry groups,
  amphicheirality, Chern–Simons and the isometries. The page's § 2 names SnapPy as the seat's referee's tool too. For
  those cells "another route" is not shown. The integer cells are computed by separate code, and the page's table
  does say how base reversal was read.
- **How known:** the script's calls and the § 2 table.

**R79-SM-43** (4, minor). verification/test_b1887_the_loop_check_verified.py:
- `assert [n for n, f in F.items() if f["amphicheiral"]] == ["the golden ground, twice"]`
- **What is wrong:** the manifold facts are read back from the committed JSON. The one SnapPy recomputation in the lock
  covers a single manifold and is skipped where SnapPy is absent.
- **How known:** reading the lock.

**Could not check (B1887):**
- The seat's relay and the lane's loop are on their branches.
- The twice-the-mark sector for k = 5 to 8 had no independent recomputation; the box was too large.
- The SnapPy facts could be checked only with the same library.

## The five locks, tested by planted errors

- **How the plants were run:**
  - Each lock was run unaltered in a scratch clone of main at 323f92327, and all passed.
  - Each plant was then applied there, only that lock's tests were run, and the clone was reset hard and cleaned
    before the next plant.
  - Main itself was not touched.
- **Evidence:** relays/sm_r79/plant_locks.py, with plant_locks.json and plant_locks_run.txt.

| lock | its tests | planted | caught | shapes missed |
|---|---|---|---|---|
| E13 | B1862 test_e13 | 9 | 4 | see below |
| E6 | B1862 test_e6 | 6 | 3 | see below |
| E10 | B1862 test_e10 | 7 | 3 | see below |
| E5 | tests/test_b892_walls_on_the_line.py (default lane) | 10 | 8 | see below |
| E3 | B1862 test_e3 and the old-form tripwire; B1877's carried-correction test | 12 | 7 | see below |

### E13 (twenty distinct eigenvalues at level 165)

- **Caught (4):**
  - the count reverted in place;
  - the dated bracket removed;
  - the quoted old count removed;
  - the count re-made by angle, which is the original mistake.
- **Missed (5):**
  - a wrong multiplicity list in the findings, sum kept at 165 (the list is computed but not compared with the page);
  - the bound "at most 20" restated as 21;
  - 21 written into B567's verdict line;
  - 21 on another tracked page. The lock reads only B567's findings, and the old-form tripwire has no entry for E13.
  - s = N // 2 in place of (N + 1) // 2 in the Weil matrix. That gives another element with the same counted spectrum
    (20, order 20, four at −1), so the corrected claim still holds and the lock is right to pass.

### E6 (the kernel computed from the map)

- **Caught (3):** the exponents swapped; half the grid scanned; the dated note removed.
- **Missed (3):**
  - the old hand condition restored in another spelling, exp(1j * 6 * a). The lock forbids one string, not the rule.
  - the kernel hard-coded as six triples without building the map. The lock tests the returned values.
  - results.json changed to Z3. The committed results are not compared with the computation.

### E10 (the arc lookup reads its argument)

- **Caught (3):** the argument ignored again; the status printed as the verdict; an unknown id printing the corpus card.
- **Missed (4):**
  - every arc's card built from B1812's verdict file;
  - the claim line dropped;
  - the status hard-coded as banked;
  - the verdict hard-coded as NEGATIVE.
- **Why:** the lock checks B1812's verdict, which is NEGATIVE, and only the header of B1859's card. So the stated
  behaviour, the named arc's status, verdict and claim line, is tested for one arc's verdict only.

### E5 (the walls purely imaginary; the scan's sentence carries its correction)

- **Caught (8):**
  - a wall given a real part;
  - one wall moved by 10⁻⁶;
  - a committed check set false;
  - the class pattern changed;
  - the findings' marker reworded;
  - B874's note reworded;
  - the skeleton's "all three" narrowed;
  - the old faulty script silently fixed.
- **Missed (2):**
  - the old exclusion restated on another tracked page. There is no tripwire entry for E5.
  - the instrument broken (its nullity returned as a rank) without rerunning the outputs. The default lane reads the
    committed outputs; with OA_SLOW=1 the recomputation caught it. This is the choice § 8 of the programme states for
    E5, reported here as the shape it leaves.

### E3 (the charge premise splits; no old form without its correction)

- **Caught (7):**
  - the exact old form on a new tracked page;
  - the correction placed 1,000 characters away;
  - the parity split miscounted;
  - the findings' count sentence reworded;
  - the verdict line's marker removed;
  - the carried-here markers on the read-out rule's page and in B1855 reworded.
- **Missed (5):**
  - the old form paraphrased as "invisible to every state". The tripwire matches only
    `(r"invisibility to every state\)", r"E = \+I|E ≡ \+I", "E3"),`, while the record itself writes
    "invisible to every state" in several places.
  - the exact form broken across a line;
  - an unrelated "E = +I" within 900 characters, which counts as the correction;
  - the form in a .txt file;
  - the form under docs/views/, excluded by design.
- **One real instance, found while testing:** the root CHANGELOG.md carries
  `only ±I act as scalars on both parity sectors (the charge is invisibility to every state);` with no correction
  within 900 characters on either side. The tripwire reads only frontier/ and docs/. § 8 of the programme says the lock
  fails "if the old form stands anywhere in the record". The changelog is a history and may be meant to stay as it
  was, but nothing exempts it in words.

## What was not done

- **B1889 was not read,** as § 13 asks for an arc that judges this seat's work.
- **Readings that would need a measured comparison** were not made. They are named under each arc.
- **Literature facts** the arcs take as given were not re-derived, and Niemeier's count of 24 was not recomputed.
- **Planted errors** were run against the five locks only, not against the six arcs' own locks. The findings on those
  locks (R79-SM-04, 15, 27, 31, 43) come from reading them. The B1879 and B1884 readers' own plants are described
  where used.
- **Fixes to this seat's own code before the final runs:**
  - The plant harness first reset the clone without clearing intent-to-add files. Those were left empty and could not
    affect a lock, and the whole run was repeated with a hard reset. The counts did not change.
  - The B1885 maximisation first used a mistyped peak. Its distance line was wrong and its ∣z∣² was not. It was rerun
    with the peak as B1885's run prints it.

0 of 19.
