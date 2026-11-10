# Review 77 — the reader's full read of B1849, B1852, B1853, B1854 and B1858 (seeded by the anchor 1eb535ecd)

*An independent reader, a fresh-context subagent spawned by main and told to read skeptically. It edited no tracked
file. Its report is reproduced below, after main's dispositions. Main verified every must-fix item at its source before
applying it. The reader computed and looked up no measured value, and did not read the agy lanes' branches.*

## The reader's verdicts

- **All five arcs HOLD WITH NOTES.**
- **All five test files pass:** B1849 4, B1852 3, B1853 2, B1854 2, B1858 5.
- **Eight must-fix findings:** two in B1854, one in B1853, five in B1858. Three of the five arcs are main's own of the
  last four days, and B1858 was written the day of the review, so the reader's independence is the point.

## Must-fix, and main's disposition

| # | the reader's finding | main's check at the source | applied |
|---|---|---|---|
| 1 | B1854: the stated cause of the k = 3 stop (the mesher's χ(T₂) condition, line 81) is contradicted by the logs, which show an assertion with no message | verified: `driver_k3.log` and `runs/k3_*` show `AssertionError()`; lines 80 and 81 of B1847's `stage_e_gamma.py` carry messages, lines 75 and 79 do not | FINDINGS § 2, the verdict line, P-739 and CHANGELOG corrected: the failing check is one of the two unlabelled translation checks |
| 2 | B1854: "± 0.010" on 6.070 is not derived, and the arc's own scatter is larger | verified: the mirror pairs differ by 0.006 at k = 2 and 0.023 at k = 1; the three-point fit uses one single-sided point | the value restated as 6.070 with an error of about 0.02; "confirmed to ± 0.01" restated as "consistent within main's scatter"; the title, § 2, § 3, the verdict line, the τ read-out rule, P-739 and CHANGELOG |
| 3 | B1858: T:RE graded DERIVED, while B1852 says the tube's identification rests on numerics | verified: B1852 § 3 and `fixed_fibre_classes.py` ("is not decided by this algebra") | regraded CONDITIONAL, the text says which part is exact and which numerical, a third pin added |
| 4 | B1858: nine edges make a DERIVED node require a postulate or a choice, so "12 proved" mixed outright theorems with premise-given ones | verified from EDGES.json | DERIVED now means proved outright; the builder refuses a DERIVED node that requires anything else, with a planted failing-path test; the nine edges are `applies-under` |
| 5 | B1858: MC:CS0's text omits its source's scope | verified: THE_CLAIM's "this is NOT a symmetry theorem"; FALSIFIER_REGISTER's "the mathematics CS = 0 stands" beside the withdrawn physics step | the text scoped to m004 and to mathematics; two pins added |
| 6 | B1858: the dated note's "13 proved and 35 open" is stale against the arc's own `build_run.txt` | verified: the live build had 15 and 36 | the note and the verdict's bracket no longer state a live count; the page points to the generated files |
| 7 | B1858: § 5a's weave, thread and list counts and its prose list are wrong | verified: "eight negatives" listed seven; thread was 24, not 25 | § 5a rewritten without counts, pointing to the generated table; the labels below corrected first |
| 8 | B1853: B1855's correction is a note at the end; § 1's ladder, § 2's charge law and the verdict line still read as before | verified | § 1's two rows, § 2's charge law and the verdict line now carry the correction where they stand |

## Optional, and main's disposition

- **Applied:**
  - B1858's labels, by THE WEAVE's own test (item 2, "defined by the joint action … not by one thread's own
    geometry"): the mirror-even index and "one end" are lists, not weave results; "nothing places Im τ" is a statement
    about the record.
  - B1858, SC:UNIT: a NEGATIVE read from two negative arcs, about any theory; no longer DERIVED, no longer labelled
    weave.
  - B1858, W:T: the text now says that the records' sitting at the quaternion point is the grammar's premise.
  - B1858, GR:ACTION: a pin for "one term", and "with Λ = −1 forced".
  - B1852: "thirteen words" corrected to twelve, the run files' count.
  - B1853: the test's "about two minutes" corrected to the reader's ten.
- **Recorded, not applied** (they do not change a conclusion):
  - B1849, p476: "slowly approaching about 20" is an unfitted extrapolation of a column still rising at 18.35.
  - B1849, p039: the covariance is by construction; the script is a sanity check of a known theorem.
  - B1852: its test's last assertion reads a printed constant; the addendum's "why it works" is an untested
    explanation.
  - B1853: "about 0.62" for gaps between 0.45 and 0.69 (the corrected line now gives the range); the apex-law check
    is an algebraic identity, not a maximum over shifts; one test is a string search of the committed output.
  - B1853: `reach: class` rests on a range-scoped enumeration and the seat's proof, not re-run (P-741).
  - B1854: the seat's table values are in no file of the arc (harvest row 1614 holds them); the extrapolation model is
    calibrated on k = 1 against the seat's number, as § 4 discloses.
  - B1858: W:DRAW is a negative about the weave's measure tested on six thread-level numbers; B1814 labels itself
    weave, and the map keeps the arc's own label.
  - B1858: GM4 stays a weave statement, as GENESIS § 0 says; PR:P10 stays a weave statement, as B1612 and B1613 label
    themselves.
  - B1858: CO:S12's DERIVED is the record's grade for B867's first two statements; the map checks the citation, not
    the proof, and its page says so.
- **The reader's own limits, as it states them:** the mesher was not re-run; B1849's ninety per-row dispositions were
  not opened one by one; the 78 debt nodes and the 27 framing-ledger nodes of the map were not reviewed; B1859's
  mathematics was not re-derived.

---

## The reader's report, as returned


## Verdicts
- B1849: HOLDS WITH NOTES. pytest 4 passed. p039 and p476 outputs reproduce or are consistent (p039 re-checked by the test; p476 needs SnapPy and was read, not re-run).
- B1852: HOLDS WITH NOTES. pytest 3 passed. Apex correction independently verified (own sympy: L^6RLR height^2 = 40/3, reduced Re 0; L^5RLR height^2 = 119/12, Re 1/2). No place in the arc still states the old claim without the correction beside it.
- B1853: HOLDS WITH NOTES. pytest 2 passed. Full explore_facts.py re-run (about 10 min niced, not the stated "about two minutes"): every line reproduces the committed run except the HV1 wall-clock ("5 s" now against "1 s" committed).
- B1854: HOLDS WITH NOTES. pytest 2 passed. The tests only re-read committed run files; the mesher was not re-run.
- B1858: HOLDS WITH NOTES. pytest 5 passed; build_map.py last line "ALL PINS CHECK". Grading and labelling have the problems below.

## Must-fix
| # | arc | finding | file | verbatim quote | why it matters |
|---|---|---|---|---|---|
| 1 | B1854 | The stated cause of the k = 3 failure is contradicted by the committed logs. The assertion carrying the "chi(T2)" message is line 81 of the mesher; the logs show an empty assertion. | frontier/B1854_the_tubes_tau_beyond_k1_on_main/FINDINGS.md; verification/driver_k3.log; B1847 verification/stage_e_gamma.py lines 76-81 | FINDINGS: "The likely cause is the mesher's lattice condition χ(T₂) ≠ 0 (its line 81)." Log: "FAILED: AssertionError()". Mesher: `assert lat.c2 != 0, "this mesher lifts sheets by T2: needs chi(T2) != 0"` | That assert would print `AssertionError('this mesher lifts...')`. The failing assert is one of the message-less ones (the trans_of check on line 79, or the T1/T2 tuple check on line 80), so the diagnosis as written is probably wrong. It is hedged ("likely", "not diagnosed") but it points the next worker at the wrong place. The line number 81 is right. |
| 2 | B1854 | The "±0.010" error on 6.070 is not derived from anything computed in the arc. The arc's own scatter is larger than the quoted error. | FINDINGS.md; verification/tube_extrapolation_run.txt | "**main's value: Im τ(Σ₀) = 6.070 ± 0.010,**" against "the mirror pairs at d = ±0.001 differ by 0.006 at k = 2 and 0.023 at k = 1" | The 3-point fit uses the single-sided d = +0.0005 point (6.0653) with no mirror, and the only mirror-pair tests give 0.006 and 0.023. The k = 1 agreement was called "partly luck" by the arc. So "confirmed ... to ±0.01" (§3) and "within 0.005 of the seat's sealed limit" rest on an unmeasured error bar. The verdict says "consistent ... at main's resolution", which is the strongest honest reading; "confirmed to ±0.01" is stronger. |
| 3 | B1858 | Node T:RE is graded DERIVED with text "Re τ = 0 exactly, by topology". B1852 says the tube/anti-apex identification rests on numerics, and B1858 itself makes DERIVED node T:RE require the CONDITIONAL node T:RULE. | frontier/B1858_the_closure_map/verification/map_source.py (T:RE); frontier/B1852_.../FINDINGS.md § 3 | Node text: "The tube's level surface has Re τ = 0 exactly, by topology; the Teichmüller apex of the same word also lies on Re 0." B1852 § 3: "The identification of the tube as the Re-0 fibre rests on B1847's anti-apex numerics, at 7 × 10⁻⁷ against the alternatives 0 and ½." | Grade overstates. The class split is exact; which fibre is the tube is numerical. This should be CONDITIONAL (on B1847's numerics and the framing T:RULE), or the text should say so. It counts as one of the "proved on main" results. |
| 4 | B1858 | The DERIVED/CONDITIONAL line is not applied consistently, so "proved on main" counts are not a clean category. Nine edges have a DERIVED node requiring a non-DERIVED node. | NODES.json / EDGES.json (computed from them) | Edges: G:T-ROOT->G:SE1 POSTULATED; G:XGEN->G:GM2, GM4 POSTULATED; G:XGEN->G:GM5b, GM5d CHOSEN; MC:CS0->G:SE2 CHOSEN; T:RE->T:RULE CONDITIONAL; W:Q8->G:GM1, GM2 POSTULATED. FINDINGS § 1: "Of them 12 are proved on main, 9 are banked negatives, and 17 are proved given named premises." | The grade table defines CONDITIONAL as "proved on main given named premises". W:Q8 (given two records, GM1) and MC:CS0 (given the orientable choice SE2) are exactly that, yet are DERIVED. The test checks only that DERIVED does not rest on LANE nodes. So "12 proved" mixes unconditional and premise-given results. |
| 5 | B1858 | Node MC:CS0 text omits what its pinned source says about its own scope. | map_source.py MC:CS0; docs/THE_CLAIM.md | Node: "No dimensionful quantity, by theorem: the object's Chern–Simons invariant is zero." Source: "Corrected B1226: this is NOT a symmetry theorem — m003 is amphichiral with CS = ¼, m208 is chiral with CS = 0. The conclusion stands for m004; the blindness is contingent on which element of the symmetry-given ℤ/2 the object occupies." | The map's text reads as a necessity. The source says it is contingent on the object's own choice and is about m004. A one-thread fact; labelled thread (right) but the text and DERIVED grade hide that it rests on SE2 (CHOSEN). docs/FALSIFIER_REGISTER.md separately says the physics step is "WITHDRAWN (the object→physics functor step refused — B1009; the mathematics CS = 0 stands)"; the node text "No dimensionful quantity" echoes the withdrawn physics sentence. |
| 6 | B1858 | The dated count note is itself stale against the generated files committed the same day. | frontier/B1858_the_closure_map/FINDINGS.md; verification/build_run.txt; arc_verdict.json | FINDINGS: "13 proved and 35 open on the spine"; verdict: "(after B1859: 13 proved, 35 open)". build_run.txt: "DERIVED": 15, "OPEN": 36. Computed over layers 0-12 (164 nodes): DERIVED 15, OPEN 36. | The verdict line carries numbers that the arc's own committed build_run.txt contradicts. The note says "the generated files hold the live ones", which excuses §1, but the verdict's bracket states 13/35 as the post-B1859 figure. They are not. |
| 7 | B1858 | The weave/thread/list counts in § 5a and the verdict do not match the nodes, and the prose breakdown of the 15 is wrong. | FINDINGS.md § 5a; arc_verdict.json; NODES.json | FINDINGS: "eight negatives (no hand, one end, no modulus, no value, no atom, no placement, the draw test)"; table "a thread | 25". Computed from NODES.json among DERIVED/CONDITIONAL/NEGATIVE nodes: weave 15 = 7 NEGATIVE + 7 DERIVED + 1 CONDITIONAL; thread 24; list 3. | Eight negatives are claimed but seven are listed, and seven exist. The 7th derived weave node is SC:UNIT (not named in the prose list). Thread is 24 live, not 25 (total 42 against 43 in the text). The headline "15 / 25 / 3" is copied into the verdict. |
| 8 | B1853 | The dated correction does not annotate the statement it corrects. § 2 still states the charge law unscoped. | frontier/B1853_the_departures_depth_premises_verified/FINDINGS.md § 2 and the verdict | § 2: "Under charge at S the selected departure is the single run lcm(S) + 1, with depth lcm(S)/2 + √5/2. This is a candidate scoped to R1 ∪ R2". Dated note: "So the charge law's depth lcm(S)/2 + √5/2 holds only where lcm(S) ≤ 10." Verdict: "the least-length ladder (2), (2,1,1,1,2), (6), (21), (61) over R1 u R2, each unique". | § 2 and the verdict's ladder still present (21) and (61) as the selected departures for S = {4,5} and {2,3,4,5}. The note says those two rows are not minima outside R1 ∪ R2 ({4,5}: 3.9224 against 4.5940; {2,3,4,5}: 3.8672 against 6.6524). "Scoped to R1 ∪ R2" is honest as far as it goes, but the verdict carries no pointer to B1855's correction, and the true minima are not (21)/(61). |

## Optional
- B1849, p476: FINDINGS says "the gap × a² slowly approaching about 20". The committed run (frontier/B1849_.../verification/p476_whitehead_volumes_run.txt) shows 1.63, 3.99, 6.07, 9.17, 12.01, 14.48, 16.28, 17.53, 18.35 for a = 1..55, still rising. "About 20" is an extrapolation with no fit in the arc. The verdict's "gap ~ 18/a^2 at a = 55" matches the last row. The e^(-Vol/π) bound "above 0.31" holds (e^(-3.6639/π) = 0.3116).
- B1849, p039: the check builds Y as a sum of conjugates, so covariance is by construction; the result is a known theorem, so the script is a sanity check, not a discriminating test. The link to B345's actual texture and to B1736's family group is not computed in the arc: "the texture is the order-3 cyclic structure (B1736's family group) seen in its eigenbasis" rests on the script's docstring, not on B345's matrices. I did not open B345.
- B1849, counts: the "6 superseded" in FINDINGS corresponds in apply_r76_1.py to P-046, P-267, P-329, P-402, P-474 (superseded) and P-526 (worded "lapsed at the seal"); P-494 is in the dict but counted as paid. The totals (29 in ANSWERED, 47 merged, 19 hosts, 11 kept, 2 retyped) match the script's dicts. The "234 open / 108 leads" register state cannot be checked now (the register has since moved: 247 QUEUED rows) and the test checks per-row dispositions, not those totals.
- B1852: "pattern ... observed in four words" in FINDINGS § 2 and the verdict versus the Addendum "it holds in thirteen words". The run files show 4 + 5 (k = 1..5, k = 1 duplicating L^6RLR) + 4 = about 12 distinct words (13 if L^5RLR, which is a both-≢I case, is counted). The addendum's number is not enumerated in any file. The verdict still says "observed in four words".
- B1852: § 3 withdraws a positional assignment of involutions ("the assignment depends on where the word is cut, so that claim is withdrawn"), but the later addendum's "Why it works" paragraph re-asserts a positional rule ("the cut lies in the middle of the product region"). The exact tests do pass for the 4 extra words, but the explanation is not tested.
- B1852: the claims "the pleated and tetrahedron readings are 2.87 and 2.58 in height" and "B1847's ... −0.016 and −0.048" are cited from B1847/B1845, not reproduced in this arc.
- B1852: the test for the original claim only asserts the committed output string "0 + 6.15(15) i" on the last line, which the script prints unconditionally (a text constant, not a computed value).
- B1853: "Each is unique, the next about 0.62 higher (0.45 under charge at 5)". The committed gaps are +0.5386 (none), +0.6852 (symmetry at 5), +0.4450, +0.6276, +0.6229. "About 0.62" is loose; all gaps are large relative to the k = 20 truncation, so the selections are not affected.
- B1853: "The apex law, exact" is asserted via `assert abs((xp - xm)/2 - ((n-1)/2 + sqrt5/2)) < 1e-30` for n = 2, 6, 21, 61. This checks an algebraic identity, not "the maximum over shifts" that the FINDINGS text claims. The max-over-shifts claim is not computed in this script. B1852's apex_real_part.py does compute max over shifts for other words.
- B1853: test_the_committed_run_holds_the_claims is a string search of the committed output; it can only fail if someone edits the file. Not a regression test of the code. The second test (centraliser mod 5, fixed point) is an independent recomputation and can fail.
- B1853: verdict "reach": "class" while the evidence is range-scoped enumeration (R1, R2). FINDINGS says "range-scoped" in § 2, and "PROVED" is applied to enumerations plus the seat's proof not re-run (P-741).
- B1853 FINDINGS says "Main's re-derivation shares no code with it" (the seat's); not checkable from the committed files.
- B1854: the title carries "0 + 6.070(10)i". The real part 0 is B1852's; this arc's own real-part evidence is that mirror pairs at d = ±0.001 are +0.380/-0.379 (k = 1) and +0.390/-0.404 (k = 2). The d-dependence of the reduced Re in the committed table is roughly linear in d (-0.18 at 0.0005, -0.38 at 0.001, +0.26 at 0.002, i.e. -0.76 mod 1), which is consistent with Re -> 0 but is not stated as such.
- B1854: the "seat's table" values ("match the seat's table to every printed digit", "the seat's 6.08186(42)") are not in any file in the arc; they are cited from harvest row 1614. The arc's own committed values (core length, s0, systole 0.18519963, 0.18521766) do agree with B1852's addendum run, which used SnapPy.
- B1854: the extrapolation model is selected by calibration on k = 1 against the seat's number, and then applied to k = 2 (disclosed in § 4). The comparison of main's k = 2 value with the seat's therefore is not fully independent of the seat for the method choice.
- B1858, labels. I judged these labels doubtful against docs/THE_WEAVE.md ("Defined by the joint action ... About all threads at once"):
  - W:MIRROR-EVEN (weave): its source is "a flat frame's count can tell a module from its dual ... the class index is mirror-even for every module (B1487, T1)". That is about a count in a flat frame, not about the weave's joint action. Reads as thread or list.
  - SC:UNIT (weave): "An ABSOLUTE energy cannot come from the object — topological invariants carry no units ... unreachable by any theory". It is a statement about any theory, so neither weave nor thread, and it is a register process note (P-719), graded DERIVED. It is counted in the 15 weave results.
  - T:NO-PLACE (weave, NEGATIVE): the text says "the object's action is linear". That comes from B1341's LR (one thread, m004), not from the pinned quote. Only "its one phase transition has no scale" is about PSL(2,Z). Mixed.
  - W:DRAW (weave, NEGATIVE): "The measured six read as a draw from the weave's own measure". The six are V:SIX, which the map labels thread. A negative that uses the six is not purely a weave statement.
  - G:GM4 (weave): "The carrier is the once-punctured torus." It is a carrier choice (not the joint action of moves).
  - PR:P10 (weave): the TM1 reading comes "from the root's double tick RL and RRL" (the root is a thread by THE_WEAVE's own definition).
  - The builder check (weave node requiring a thread node) only looks at "requires" edges whose source is DERIVED/CONDITIONAL/NEGATIVE; SC:UNIT and T:NO-PLACE have no such edges, so the check cannot catch a label like these.
- B1858, node texts I judged fair against their pins (no overstatement found): G:PF2, G:PF1-FORM, G:GM2, G:XGEN (758 states, 536 manifolds), G:T-ROOT, G:GAP5, G:FK8, G:FK13, A:A01, A:A10, T:CHARGE5, SC:PREMISE, SC:RATIO, GR:VECTORLIKE, CO:S3, PR:P2, MC:Z6 (pin: B1221 addendum, "|kernel| = 6 exactly when k = 1"), MC:UNIQ (pin: B1859 FINDINGS "The door set is {1, 4}, for every m" and the CORRECTED note in THE_CLAIM; I did not recheck B1859's mathematics).
- B1858, texts I judged slightly strong or under-qualified:
  - W:T: "a three-dimensional representation follows from the quaternion point" omits the pin's own condition, "two records follow from the input **the records have a non-trivial common character in SL(2, ℂ)**". W:T requires only W:Q8 (which requires GM1 and GM2) so the dependency is in the graph, but the node is DERIVED and unconditional in text.
  - MC:Y: text "its normalisation is underivable by homogeneity" is fair, but the source table grades it "DERIVED / CLOSED" while the node is CONDITIONAL (which is the conservative reading, and fine).
  - CO:S12: "Two of the three preconditions ... stand as structure, and as preconditions only" pins a table cell ("PROVED, structural | stands, as preconditions only") about B867 S1, S2 and is graded DERIVED. The builder checks that the cell exists; B867's proof is not read by the map ("Not verified beyond its pins"). Fair as a record statement; DERIVED reads stronger than a pinned status cell.
  - GR:ACTION: "a one-term action" is not in the pinned quotes (it is in THE_FRAMEWORK lines 554 and 616, "S = −Vol·σ, one term"). The "no free dimensionless constant" part is pinned. Fair, but the "Λ = −1 forced (B259)" convention is where the zero-constant claim sits; the map does not mention it.
- B1858, grades asked in item (iv): FK13 CHOSEN (not too strong, and the source says "Revisable by a better argument"); MC:CS0 DERIVED (see Must-fix 5); MC:UNIQ DERIVED (fair given B1859; the proof is not re-derived here); W:T DERIVED (conditional on GM1, see Optional above); W:MIRROR-EVEN DERIVED (grade fair, label doubtful); SC:UNIT DERIVED (too strong for a register process note; it is a dimensional-analysis remark); T:RE DERIVED (too strong, Must-fix 3); GR:ACTION DERIVED (fair for "a mathematical fact about this one construction"); CO:S12 DERIVED (see above).
- B1858 test strength: test_a_planted_error_is_caught only shows that a missing quote is reported. A pin shows that the record says a thing; FINDINGS admits this ("A pin shows that the record says a thing, not that the thing is true").
- B1858 FINDINGS states "241 pins on main ... All 280 check"; build_run.txt now has 250 on main + 39 = 289. The landing numbers are in the text and the live ones in the generated files (the dated note explains).

## What I ran
- `python3 -m pytest -q -p no:cacheprovider frontier/B1849_*/verification` -> 4 passed in 1.33s.
- `python3 -m pytest -q -p no:cacheprovider frontier/B1852_*/verification` -> 3 passed in 3.04s.
- `python3 -m pytest -q -p no:cacheprovider frontier/B1853_*/verification` -> 2 passed in 1.09s.
- `python3 -m pytest -q -p no:cacheprovider frontier/B1854_*/verification` -> 2 passed in 2.18s.
- `python3 -m pytest -q -p no:cacheprovider frontier/B1858_*/verification` -> 5 passed in 2.92s.
- `python3 -B frontier/B1858_the_closure_map/verification/build_map.py` -> last line "ALL PINS CHECK"; stats: pins_checked_on_main 250, pins_checked_on_seat_branches 39, seat_pins_unavailable_in_this_clone 0.
- Own sympy script (scratchpad, apex.py): L^6RLR -> (40/3, all reduced Re 0); L^5RLR -> (119/12, all reduced Re 1/2). Agrees with frontier/B1852_.../verification/apex_real_part_run.txt.
- `grep -rIl "(1/2|½) \+ 3\.65|real part as well as its height"` over the repo: hits in B1852 FINDINGS/verdict/apex_real_part.py (all inside the correction wording), and in CHANGELOG.md, docs/THE_TAU_READOUT_RULE.md, docs/POINT_REGISTER.md, docs/views/VERDICT_LEDGER.md and docs/handoffs/CC_TO_CHAT1_2026-11-10_THE_APEX_CORRECTED_AND_THE_FRAMING_RULED.md. I did not open those outside the arc, so I cannot say whether each carries the correction beside it.
- Full `explore_facts.py` (B1853), niced, OMP_NUM_THREADS=1: completed after about 10 minutes (the arc's own comment says about two minutes); output identical to explore_facts_run.txt except HV1's elapsed seconds.
- Own Python over the committed apply_r76_1.py dictionaries: ANSWERED 29, MERGED 47, PARTS 1, KEPT 11, RETYPE 2; 19 distinct merge hosts (including P-574).
- Own Python over NODES.json / EDGES.json for the grade and label counts above, and a context dump (pinned file text around each pin) of 29 nodes: 20 sampled at random across layers (seed 77; main-only pins; G:PF2, G:PF1-FORM, G:GM4, G:GM2, CO:S3, PR:P10, PR:P2, G:T-ROOT, G:XGEN, G:GAP5, G:FK8, MC:Y, MC:Z6, A:A01, A:A10, T:CHARGE5, T:NO-PLACE, SC:PREMISE, SC:RATIO, GR:VECTORLIKE) plus the nine listed in item (g)(iv).
- No tracked file was modified by any test or script run (`git status --short | grep -v '^??'` was empty after the runs). The runs wrote `__pycache__` only where pytest was used; I ran scripts with `-B`.

## What I did not check
- B1849 p476 (SnapPy volumes) was not re-run; the run file was read and its numbers were checked for internal consistency only. The register-state claims ("234 open, 108 leads, 311/186 before") were not re-derived: the register has changed since 2026-11-06.
- B1849's per-row "check at the pointer" dispositions (about 90 rows) were not opened one by one against the record; I checked only the script's dict sizes against the prose counts and the test's assertions.
- B345 and B1736 (to see whether p039's texture claim matches their actual matrices) were not opened.
- B1852/B1854 claims taken from B1847 and B1845 (the 7e-7 anti-apex figure, -0.016 / -0.048, the 6.15 ± 0.15) were not re-derived; the B1847 mesher (setup of tens of minutes and ~13 GB) and tube_driver.py were not run. B1854's run files under verification/runs/ were read for the cited rows only. tube_extrapolation.py ran inside the test only.
- The seat's own table (harvest row 1614), the web seat's numbers (6.14916, 6.08186, 6.06526) and the explore seat's modules were not read (no access needed, and the lane branches named in the constraints were not touched).
- B1858 nodes with seat-branch pins (39 pins) were not opened by me; only the builder's own internal check was run. B1859's mathematics was not re-derived.
- B1858: I did not check all 155-164 nodes; I checked 29 for text and pin, and 28 labels by reading node text (the fifteen-plus requirement). I did not review the 78 register-debt nodes, the 27 framing-ledger nodes, or MAP.md / CLOSURE_QUEUE.md beyond the test that they equal the builder's output.
- The file docs/closure/THE_TWO_TARGETS_2026-11-05.json and the two named seat branches were not touched. No measured physical value was looked up or compared. B1849's register rows mention particle-physics names but I did not read or reproduce any value.
