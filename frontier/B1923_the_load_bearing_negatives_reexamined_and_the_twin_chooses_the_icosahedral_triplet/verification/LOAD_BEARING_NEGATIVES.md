# Load-bearing negatives, B1820 to B1922 (read-only reading, 2026-11-13)

Scope: frontier/B1820..B1922 FINDINGS.md, docs/POINT_REGISTER.md rows P-700..P-842, docs/LAW_MAP.md rows citing the arcs.
Nothing was run. Files with "agy" in the path, "/received/", the two-targets json, and measured-data files were not opened.
Line numbers are those of the file as it stands on main today. "Frontier" paths are shortened: B1825 = frontier/B1825_step_b_the_nine_from_one_address/FINDINGS.md etc.

Already retracted (not a row): B1918 (the channel norm is not the L-function's Kronecker coefficient), replaced by B1919.
Lesson already on record: its fits tried forms that did not contain the true one (a fit over a family of forms).

Key to column "kind": EXACT = counts/identities/classification; SCAN = numerical scan with a range; FIT = fit/regression over a family of forms; CARD = sealed card outcome; ARG = argument.

Ranking note. Rows are grouped: A (closed a route to removing an input / dropped a candidate), B (read-out point negatives), C (exact-enumeration negatives), D (scope/other). Within each, the most load-bearing and least independently checked first. Section E lists my five picks.

---------------------------------------------------------------------------------------------------

## A. Routes closed, candidates dropped, inputs counted unremovable

### A1. B1839 (the end card), cell D
1. "THE SIX ON THE STRIP, at the small-cut end, stops being a candidate" (B1839:45). Cell D fails: 24 252 of 10^6 random hierarchies as low, r97.5 = 2.4555e-2 > 0.01 (B1839:21).
2. Rests: B1839:53-55 "the small-cut ansatz (A07, A09) is retired from the candidate"; "the end, if the six are to rest on one, is B1841's principled entry" (B1839:55-56 region). B1841:41 "A07 is CHOSEN at this row".
3. Independent: web seat's "third opinion of the census" agrees to 2.0e-14 (B1839:4) and C0 reproduces the web seat's sealed rows to 8.2e-12 (B1839:12). That is the census, not the D verdict. The D null (matched null over 23 levels, 10^6 draws) has one code path I could find. B1841's D (8 665 of 10^6, r97.5 8.85e-3) is the same card family, run on the same null machinery. Independent null: none found.
4. Cut against the candidate's expectation: yes. B1838:19 and B1838 § 3 item 2 ("if no geometric level passes the screen, the candidate's pass belongs to the ansatz end and the candidate dissolves"). Note the margin: D fails at r97.5 2.46 % against 1 %, but B1841 passes at 0.885 % (margin 0.115 points of a 1 % gate); B1841 D with {1,3} c "would fail" 1.053e-2 (B1841:17). The whole verdict flips on the K = 4 versus 23 levels look-elsewhere count.
5. CARD (sealed, one look) + random-null sampling.

### A2. B1838 § 1 and § 2b (the exact end fails; no single horocycle reproduces the weights)
1. "At the exact norms the down and lepton m2/m3 fall from about 0.019 to about 0.012" (B1838:18); chi2_six 2.409 -> 30.664 (B1838:13). "No single horocycle reproduces the candidate's weights" (B1838:35); "The end is an ANSATZ" (B1838:41ish).
2. Rests: B1839 (whole card), LAW_MAP row B1838 closed-form note (docs/LAW_MAP.md:362); scoreboard A07 re-typed ("totals unchanged").
3. Independent: the web seat's sealed look, rerun on main with the seat's own instrument, every row identical (B1838:8-9). Strong on the numbers; the "ansatz" conclusion is main's argument.
4. Against the expectation: yes (the candidate's six "pass" at small-cut end, B1726 compute).
5. EXACT finite computation (4 rows) plus a numerical spread (0.135 against quadrature error 2e-14).

### A3. B1825 (Step B, the nine from one address), cell S
1. "The decisive cell S fails ... least chi2_ten ... is 291.4, against the sealed threshold 23.21" (B1825:5-6; table B1825:39). Scope: "excludes nothing beyond the reach (lines of order above 12, Im tau above 4, other directions, radii or c)" (B1825:9-10).
2. Rests: B1833:97 ("towers' meeting the next frame on NO SUPPORT ... B1825 returned NO SUPPORT"); B1823:61 (Step B proceeds on declared directions). The input count treats ten numbers as not reachable from one address.
3. Independent: an independent referee with its own code brute-forced all 50 612 352 stored node rows: least 291.81 (B1825:15-21). Also fresh evaluation by B1821's evaluator 291.4867. Good. But the referee reads the same stored census nodes; the evaluator is the same family.
4. The card said before the seal that the conjunction could not pass (B1825:31) and that "each lead one to expect that one address is not enough" (B1825:80). So it did NOT cut against expectation. A disclosed hole: "The CM arm was dropped and not disclosed" (B1825:119).
5. CARD (sealed census scan with a range: order <= 12, Im tau in [1,4], 12 directions, 2 radii, 8 readings). Scoped negative, reach-limited.

### A4. B1823 (Step A, the tied heavy vacuum): NEGATIVE as a compression
1. "NO COMPRESSION REMAINS FROM THREE COPIES ON: THE VACUUM MOVES IN ALL SIX DIRECTIONS OFF THE MIRROR LINES (COMPUTED AT n = 5, 6, 8)" (B1823:1); "Step A, 'a Higgs direction fixed by the interaction', is not delivered by this construction" (B1823:~59-61).
2. Rests: B1823:61 "Step B proceeds on the declared directions, twelve distinct (B1824), with no Step A arm"; the Higgs direction stays an input.
3. Independent: hostile referee with its own code; main re-ran B2's Jacobian at 40 digits, reproduced the referee's singular values, and re-ran the whole vacuum grid with a cancellation-free potential plus 24 extra starts (B1823:9-14). Referee is independent of the builder, not of the plan. Only n = 2..8 and a "CHOSEN" model (minimal Kahler, H_d only, cross terms zero) were computed; a negative about THIS construction.
4. The draft's own headline said "Yes ... from two heavy copies on" (B1823 body); it was refuted by the referee. So the negative cut against the builder's draft expectation.
5. SCAN (numerical minimisation over starts, grids at chosen primary points) + EXACT rank counts.

### A5. B1822 (T-norm on the frame's matter)
1. "'no new freedom' is false for the flat structure; H = I is a CHOSEN input" (B1822:68-70).
2. Rests: B1823:~114 / B1825 scope ("the census stands, for FR-FIB with H = I"; B1825:114: "H = I ... a CHOSEN input on the card"). It adds 8 real parameters per field to the count unless a typing forces H.
3. Independent: referee's independent implementation confirms census coupling() = (C_a F_x)^T eps S (C_b F_y) to 1.6e-14 (B1822:~22). The "outputs move with H" half: computed in refine.py, one code. The web seat's local search at the address finds no near-identity metric that rescues the CKM corner (B1825:114, "not re-run on main").
4. Cut against B1654's expectation ("no new freedom"); P-146's dismissal "is refuted" (B1822:84).
5. ARG/EXACT (theorem plus 1 170 configurations).

### A6. B1859 (the door set is {1, 4})
1. "It is false at m = 4" (B1859:11): the golden is NOT the unique metallic grammar with a McKay own-conductor shadow; R4L4 gives SL(2,5) = 2I. Door set {1, 4} for every m (B1859:13).
2. Rests: front pages and LAW_MAP row "THE GOLDEN IS THE UNIQUE METALLIC GRAMMAR WHOSE OWN-CONDUCTOR SHADOW IS A McKAY GROUP (B997)" (docs/LAW_MAP.md:455); the "one grammar one door" row (docs/LAW_MAP.md:236) says siblings have NO SU(2) embedding. I did not check whether those two rows carry the correction; the main author should.
3. Independent: "stated also by the agy lane's Theorem A (harvest row 1621); verified here on main's own code" (B1859:3-5). Two sessions, exact integer arithmetic.
4. Cut against the record's printed claim (B997). Not a prediction.
5. EXACT (group order, integer arithmetic).

### A7. P-720 (register line 932): the record's Kahler weight does not supply the apex read-out
1. "the record's Kahler weights do not supply P-717's apex read-out" (docs/POINT_REGISTER.md:932); "modular weight exactly k = 1 ... k = 1.0000 for every singular value, sector and reading at three tau and three lines".
2. Rests: the row is DONE-NEGATIVE; it re-routes P-717's apex read-out "to a dynamics along the circle (FL-05)" (same row, the [was] text), and the apex read-out stays a chosen input.
3. Independent: none found. One script (audit/drafts/p720/weight.py, 22 lines), main's own.
4. Against expectation: the row's goal was a derivation of the apex read-out ("If that total is large enough, P-717's apex read-out is derived from P-259"); the preliminary guess in the row was already "likely FAILS".
5. SCAN: three tau, three lines. FLAG FOR THE RE-VERIFIER: weight.py calls yukawas_exact(..., delta = math.inf, ...), "no horoball norm, every channel weight 1" (its docstring lines 1-2). So k = 1 is the weight of the RAW coupling. B1920 and B1921 later found that the frame's channel norm carries a universal non-modular tau-term (pi log Im tau; L-tilde = L + (1/2) log Im tau - (gamma + log pi); B1921:17-19). The negative may not cover the frame as it uses the channel norm. Whether the Kahler weight (Im tau)^(w) with the end's tau-term changes the count is untested.

### A8. P-715 / P-719 (scale): no process in the object supplies an ABSOLUTE energy
1. "So no process in the object supplies an ABSOLUTE energy" (docs/POINT_REGISTER.md:927, citing B151, B660, B719, B811, B980); P-719 (line 931): "An ABSOLUTE energy cannot come from the object — topological invariants carry no units".
2. Rests: the goal's scale clause is restricted to a dimensionless ratio; "what is missing is a principle that fixes the level" (P-719).
3. Independent: none new; re-read of older arcs. Argument from the record (pre-window arcs).
4. Cut against the owner's goal wording ("a process in the object that places ... an energy scale", B1845 header).
5. ARG.

### A9. B1851 (scale card not sealable) and P-722/P-732
1. "Not sealable (P-732)" (B1851:48); the card "fails P-728's 'more independent precise numbers than choices' on either count" (B1851:44). Register P-722 (line 934): "R2's form is not the block's value at level 5 — the exact Kashaev invariant is 46 + 2 sqrt5 = 50.47 against R2's leading exponential exp(5 Vol/2 ...)".
2. Rests: no sealed scale card; the scale stays an unearned input. LAW_MAP none.
3. Independent: main's re-derivation of the web seat's relays (B1851 § 1, `relay_facts.py`). The count ruling is main's argument.
4. Against the web seat's request to seal.
5. EXACT (Kashaev value) + ARG (count).

---------------------------------------------------------------------------------------------------

## B. Read-out point negatives (no value of tau is singled out)

### B1. B1868 (move count: no value of tau holds weight)
1. "If every move is equally likely, no value of tau holds a share of the weight. The density only sharpens, holding no mass, at the point i" (B1868:15-16). LAW_MAP: "no point of the modulus has positive weight" (docs/LAW_MAP.md:517).
2. Rests: P-756 answered; B1872 "it fixes no value of the modulus" (B1872:19); LAW_MAP row B1815 scope clause "the placement of the modulus is chosen".
3. Independent: yes. Web seat's card (40 million random moves) and main's quadrature with no random numbers; exponents agree to three digits, level-5 numbers exactly (B1868:12-14). Not verified by main: the five tested points off the imaginary axis, that the law has a density at all (seat cites with a disclosed gap), one family of side exponents (B1868:20-22).
4. Against the programme's hope that the move count would place tau; the seat "says itself that this closes nothing" (B1868:18-19).
5. SCAN (quadrature at three depths) + exponent estimates.

### B2. B1846 (harmonic time): neither metric weight is a point; the "no atom" negative was over-stated and corrected
1. "So the metric's energy places no read-out point" (B1846:41; LAW_MAP rows docs/LAW_MAP.md:363-364). Original B1846:128-131 "A point read-out is not something the metric produces" was CORRECTED at Review 76: the systole's theta is a canonical point at the tube.
2. Rests: P-717's tube read-out; B1852/B1854/B1847 tube values; LAW_MAP "the atom part THEOREM (volume-type measures only)".
3. Independent: energy uniformity measured chi2 38.6/39 (m004) and 42.0/39 (excursion); hump max/mean 1.75 "two methods". Same author. Hump law "NEEDS-LIT" (LAW_MAP:364).
4. Not an expectation test; the correction at Review 76 shows the negative was stated wider than computed (a lesson for any "no point" claim).
5. EXACT theorem (coarea + Stokes) for the energy; SCAN for the hump on 3 members.

### B3. B1913 (flat area excluded) and B1885 (the agy lane's point is not the critical point)
1. "So the measure is not an ingredient to choose: invariance forces it, and the flat area is excluded because it is not on the curve" (B1913:23-24). The flat-density maximum moves 0.065 between charts (B1913:21).
2. Rests: P-776's condition R6 and P-831 (register:1043: "fails the sixth of the eight conditions"); the read-out candidate = invariant density's place z* (B1885:20).
3. Independent: B1885's z* was agreed to every digit by the web seat's own code and the advisor seat recomputed its state (B1885 header). B1913 itself is main's own run only.
4. Main's reading "written before the run" (B1913:12), and the run agreed.
5. EXACT/ARG (invariance) + numerical check at two charts.

### B4. B1912 (golden state is the lowest twin-odd state, simple)
1. "for 0.02 <= R <= 3.40, in all four classes, the only eigenvalue is R0 ... absent from the other three" (B1912:15-16).
2. Rests: P-776 condition R3 ("existence and uniqueness first, met within the range", B1912:17); the read-out's state is unique.
3. Independent: two heights in one code plus a positive control (B1912:3). The web seat's referee scan (double precision) "was not read for this arc" (B1912:25). Not covered: R < 0.02 and exceptional eigenvalues lambda < 1/4 (B1912:18). Independent: none found.
4. No expectation recorded.
5. SCAN (numerical Hejhal-type scan over a range). An absence claim by a scan: the kind where a missed eigenvalue goes unseen.

### B5. B1875 / B1881 / B1872 (selection of one place by the allowed set)
1. B1875:19 "'single' ... cannot be a rule about which histories are allowed"; B1881:16 "Symmetry says where a single place can be. It does not put one there."; B1872:18 "Read through what it fixes, it selects nothing" (corrected at Review 78: "keeps both twins, never one" is an identity, B1872:20-21).
2. Rests: B1875 closes the "admission form of the first back-edge" (register P-776 row, line 988: "after B1875 ruled out the admission form of the first back-edge"); P-776's open search for a read-out on the whole.
3. Independent: web seat's sealed cards, main's own code, ties in integers (B1875:5-8); 65 checks (B1881:11). Main did not run seat code. Rule over 36 composites only: "Of the 36 composites tested, 18 are single and 18 are not" (B1875:13-14) - an enumeration, not a proof.
4. Against the advisor seat's design (A-adm).
5. EXACT enumeration (finite family).

### B6. B1920 / B1922 (thread average, not at the apex; S* not periodic)
1. B1920:21 "Not at the apex: on all 1,476 closed entries the line part at the apex differs from its average"; B1922:39 "S* is not periodic" (table B1922:19-23: S* 2.7 and 1.5 against 3e-10 at the own line; (1/5,3/5) 2.3-3.4).
2. Rests: P-776 now routes to the thread average instead of a point; the apex read-out (P-717) loses its arithmetic support from B1920; "It removes no input yet" (B1922:~38).
3. Independent: B1920's population run is the SM seat's (sealed expectations first: seven held, two did not, B1920:9-10); main checked three load-bearing parts (identity of B1919 to 4.9e-7; shifted Hecke at s=2 to 1.4e-7..1.8e-6; golden average 8.906783 vs seat's 8.9068) (B1920:23-31). Main's lower window disagreed, explained as main's own series truncation (B1920:29-31). B1922: main only, golden thread only, three windows, one with 7.8e-5 precision loss (B1922:25).
4. B1922 "Written before the run" (B1922:11) that S, S-tilde should repeat at the own line and S* should not: confirmed; not against expectation.
5. SCAN (numerical deviations). Note the lineage: B1918 (retracted) was the preceding negative of this family.

---------------------------------------------------------------------------------------------------

## C. Exact-enumeration negatives on the selection of the departure and the hand

### C1. B1855 (charge law fails for lcm(S) >= 12; proved only for lcm(S) <= 10 by the seat)
1. "REFUTED for every S with lcm(S) >= 12, by explicit counterexamples" (B1855:22); register P-737 (line 949) "{4, 5}: 3.9224 < 4.5940".
2. Rests: P-737; the run of 6 as least departure holds only "under the level-5 charge" (title). "It is not built on until main re-runs its exhaustive search (P-741)" (B1855:4-5); LAW_MAP waits on P-741 (B1855:46). Charge-law selection for general S is dead; scope is S = {5}.
3. Independent: the explore seat's search and proof; main checked every counterexample in exact integers and 80 digits (B1855:28-29) and corroborated S = {5} by brute force on 296 + 3 220 gapped words (B1855:42). Lemma B and the Lemma E shortest-path search "not re-run on main" (B1855:45, 67-68). The negative (counterexamples) is independent; the positive half is not.
4. Cut against the candidate law set up in B1853:62 ("a candidate scoped to R1 union R2, to be proved in general").
5. EXACT (counterexamples, exact integers).

### C2. B1853 / B1857 (the action selects within a premise; HS6 false)
1. B1853:53 "The action selects within a premise; it does not remove the premise"; "Without a premise, length selects (2)" (B1853:55). B1857:16 "HS6 FALSE as pre-registered. By length, the cheapest line-invisible departure with a unique lightest state is (2,1,2,1,2), not (6)".
2. Rests: the run of 6's depth is conditional on a counted level-5 premise (B1853:56-57); B1869 later: "the run of 6 comes out because 5 goes in" (B1869:16-17).
3. Independent: explore seat's tests, main re-derived with own code (B1853:6-7, B1857 § 2). Ranges R1/R2 are finite (m <= 6 runs <= 6 etc.): the "least" is range-scoped; POST HOC range note at B1857:17-19.
4. Against the seat's pre-registration for HS6.
5. EXACT enumeration in a finite range.

### C3. B1869 (the principle as a selection rule picks 6 only with 5 put in)
1. "Change any one choice and the answer changes" (B1869:18-20): sense of "detect" -> ties with (2,2,2); more levels -> 17-18 letters; silver/bronze -> no single run.
2. Rests: B1876:23 "the draft is a foundation and not a selector"; LAW_MAP (docs/LAW_MAP.md:520) "the founding principle read as a selection rule picks the run of 6 only when the level is put in"; the run of 6 stays a chosen input (level).
3. Independent: advisor seat's sealed exhaustive run (262 144 / 589 824 / 802 816 departures), main re-enumerated with its own code on main's definitions; all seven hypotheses reproduce (B1869:11-12, 29-30).
4. The owner's "lets try that" hoped for a selection (B1869:3-4): cut against it.
5. EXACT (enumeration to 20 letters).

### C4. B1914 (decision 4's route is spent; the twin cannot be separated) and B1915 (positivity adds no bit)
1. B1914:39 "Decision 4's route is spent. The extension condition gives what the ground already gives ... and cannot give the last bit"; B1914:24 "P-718's Q1 ... has the answer no, for every history, by that identity"; B1915:30 "positivity's side adds no bit to the hand and the twin".
2. Rests: the input budget's decision 4 and decision 1 (B1914:9-13; B1915:11-12); "No input leaves the budget by this arc" (B1914:46, B1915:41). Main "takes the stricter count ... two bits" (B1915:40-41).
3. Independent: main's own code only. The twin "no" is an identity (kept); the symmetry group is checked against SnapPy (B1914:3-4); the 176 maps are entries up to 9 (B1915:24) and the 104 symmetries entries up to 12 plus families up to 300: finite ranges. Independent: none found.
4. B1914 had a "named route ... a condition that can fail" and it did fail to reduce the budget (B1914:9-13): against the plan.
5. EXACT (integer searches over bounded entries).

### C5. B1884 (what level a ground names)
1. "The rule of a history's own lines gives the tick no line at any level. The line of order 5 that this rule finds belongs to the tick's square" (B1884:19-20, 25: "It may not cite the own-line rule for the tick's level: that rule gives the tick none.").
2. Rests: the foundation's ground entry (SE3) must say which reading it uses; five places carried a correction (B1884:14-16); the level 5 is not "a further input" only by the discriminant reading.
3. Independent: web seat's sealed card; main's own code, "recomputed independently" not "reproduced" (B1884:10-13 after Review 79).
4. Predictions all held (B1884:85): not against expectation.
5. EXACT (integers to N = 60).

### C6. B1867 (no result of main's map returns to fix an input; three forcing arguments one clause short)
1. "None of its 286 edges is a result that returns to fix an input" (B1867:12-13); "Three rows need a clause that the formal statement does not contain" (B1867:85). Corrected at B1873: exits on 8, not 12 of 38 (B1867:19).
2. Rests: closure programme (B1861); P-765; LAW_MAP:520.
3. Independent: B1873 (the advisor seat's read) corrected the count; the three clauses were exhibited by main in integers (B1867:89-102). The first of the three rows' "removed" label was by the seat's own account.
4. Seat expected the principle to be short "who the ground is and at which level it looks" (B1867:104): confirmed.
5. EXACT + ARG.

---------------------------------------------------------------------------------------------------

## D. Other negatives of record

### D1. B1845 (the level-5 diamond is not a frame symmetry at fixed tau)
1. "The diamond <2> ... is not a frame symmetry at fixed tau. The sealed features at the two points differ by 2 to 6 in ln ratio" (B1845:20-21); "at a placed tau, the 266 lines become 4" (B1845:22).
2. Rests: P-718; B1914's twin analysis; the line's last bit counts as a sign (B1914:42-46). B1845:24 labelled POST HOC (the line (2/5,4/5) is RL's own fixed line, noticed after B1841's best row).
3. Independent: none found (diamond_run.txt, main's script, a handful of cases).
4. Not an expectation test.
5. SCAN (numerical features at sampled points).

### D2. B1879 (the exchange removes the hand: the chiral three has no sign left)
1. "The chiral three ... has no sign left at the level of the weave: that is argued from the joined piece, and the index was not recomputed" (B1879:21-25); corrected at Review 79 to say it is an argument.
2. Rests: foundation GM5c (B1891 corrections), B1915's count of decision 1; LAW_MAP:538-540 "the index of three is argued to lose its sign there and was not recomputed".
3. Independent: none found for the index; the group order (96 -> 192) and the 6-dim irrep are exact on main.
4. "One thing gets stronger, and main did not expect it" (B1879:26) refers to the tick's fixed characters, not this.
5. ARG on top of an EXACT representation computation.

### D3. B1836 (seats past S300): refutations and non-earned joints
1. "Its 'dynamical Re tau*' is REFUTED" (B1836:78, the lane's Theorem 29 potential has no stationary point once rebuilt with the fermion-loop sign, 2 120 grid points); "P-639, the mirror half: NEGATIVE ... cannot force FL-06's adjugate pairing" (B1836:74-75); "no borrowed joint is earned by any of them" (B1836:80); "B08 does NOT match" (B1836:68).
2. Rests: scoreboard 0 of 19; the mirror cannot supply the adjugate pairing, so FL-06 stays a chosen input.
3. Independent: web seat's readers "through the mask", "Main re-ran every check it banks, and each output was identical to the reader's" (B1836:15-16). The Theorem 29 refutation is a grid scan of one potential (2 120 points).
4. Against the lane's claim.
5. SCAN (grid) + ARG (mirror commutes with reading).

### D4. B1882 (window ends of the nulls: all three decisive cells read B, "two by a hair")
1. "All three decisive cells read B: an end of the window is like other rows" (B1882:12); "Two of the three read B by a hair. One is short of A by less than one target in a thousand, one by three" (B1882 § 1).
2. Rests: reduces audit finding V1 to one sentence for two nulls; the six's rarities are not re-read (B1882 header). LAW_MAP row of B1882 known incomplete under the first null's covariant menu (docs/LAW_MAP.md "CURRENCY READ 2026-11-12"; P-814).
3. Independent: the advisor seat sealed the card; main sealed its own note and ran stage 2 (B1882:3-6). Same random-target code lineage.
4. The audit expected a window problem; the card read B. Margin by "a hair": fragile.
5. CARD (sealed) with random-target counts.

### D5. B1907 (two sealed packets refused as sealed): process-with-math, borderline
1. "Neither packet is accepted for execution as sealed" (B1907:9). Findings: "packet 2, method 6: the holonomy block cannot fail"; "packet 1: the code never builds the bracket of E8" (B1907:55-64).
2. Rests: P-746 (register line 958), R80-6; P-747.
3. Independent: two read-only readers in their own code re-derived 64 rows, none failed (B1907:11-12); readers are "not independent of main" (B1907:28).
4. Main chose the stricter of two options (B1907:15-17).
5. ARG (check-design review).

### D6. B1909 (the paired pole: two charged species; a chirality claim must account for the whole pole)
1. "the charged vectors at the pole ... are two complex species, not one ... and |g_R| = |g_L| in this background" (B1909:11-15); "R80-5 cannot close before it" (B1909:38). Step 7 "rank two, positive".
2. Rests: P-749 (e) and Review 80's R80-5 (third carry), per memory; the physical lane's chirality claim.
3. Independent: steps 1, 2, 3 (arithmetic), 5 (roots), 7 computed on main's own E8 and algebra; the lane's proof was read through the mask. The analytic half (steps 3-6) is open: verdict OPEN.
4. Not an expectation test.
5. EXACT (algebra) for the stated steps; the rest is ARG.

### D7. B1910 (abelian carrier excluded; the prime 2 only under a one-sector premise)
1. "The quaternion point ... cannot be carried by the abelian carrier Z^2" (B1910:9-10); "'the prime is 2' holds under the premise of a single irreducible sector, and not without it" (B1910:19-22).
2. Rests: P-321, P-747's last part, GM4 reading; selects p = 2 only with a declared premise (B1910:23-25).
3. Independent: the lane's note, main recomputed; register P-829 line 1041 (71 checks none failing, the remainder "does not exclude the quaternion group or the Heisenberg group"). Computed for p = 2, 3, 5, 7 only.
4. Against the lane's note ("freeness" and one sector are premises).
5. EXACT (finite groups for four primes).

### D8. P-713 (register line 925): the Farey transition at s = 1 places nothing
1. "NEGATIVE for placing tau ... s = 1 is the critical exponent delta = 1 of PSL(2,Z) ... its critical measure is hyperbolic area ... whose cusp tail 3/(pi Y) has no scale — the transition exists but singles out no height, scale or thread class" (docs/POINT_REGISTER.md:925).
2. Rests: P-729 "SEEN FIRST ... P-713 (DONE NEGATIVE: the Farey transition places nothing)" (line 941); closes the bang-programme route for placing tau.
3. Independent: none ("from the record"; 0.315 versus 0.318 at trace <= 400 from B1813/B1816; Prellberg-Slawny "cited, not re-derived").
4. The row asked the question "by a criterion written before computing"; the programme hoped for a singled-out scale.
5. ARG from the record's earlier numbers.

### D9. P-712 (register line 924): B867's S3 rests on a potential with no double well
1. "B867's S3 ... rests on a potential B295 had shown unbounded below with one minimum and one maximum — no double well; the 'barrier' is the cubic's maximum".
2. Rests: COSMOLOGY_LEDGER row 6's dated note; B867 ADDENDUM_2026-11-05 (docs/THE_BANG_PROGRAMME.md).
3. Independent: none found (re-read of B295, B853, B1341).
4. Against B867's reading.
5. ARG (reading earlier arcs).

---------------------------------------------------------------------------------------------------

## E. My five picks: most load-bearing and least independently checked

1. A1 (B1839 cell D) with B1841's D: dropped the small-cut end and froze the candidate at B1841's row; verdict hinges on a null's look-elsewhere count (23 levels versus 4) around a 1 % gate; one code path for the null; B1841's D passes at 0.885 % and its {1,3}-c variant fails (1.053 %).
2. A7 (P-720 NEGATIVE, k = 1): one 22-line script, three tau, raw coupling with delta = inf (no channel norm). B1920/B1921's tau-term (pi log Im tau, L-tilde) is a non-modular tau dependence the script's setting excludes. A route closed on a scope narrower than the frame.
3. B4 (B1912 absence of any lower or other twin-odd state, 0.02 <= R <= 3.40): an absence by scan in one code; exceptional range lambda < 1/4 and R < 0.02 not covered; the web seat's double-precision scan not read. It carries P-776's condition R3.
4. C4 (B1914 + B1915: decision 4's route spent, positivity adds no bit): main's own integer searches over bounded entries (up to 9, 12, 300); no second computation; they shape what counts as one bit in the budget.
5. B1 (B1868, no tau holds weight) and B6 (B1920/B1922 not at the apex; S* not periodic): B1868 leaves unverified the off-axis points and the existence of a density; B1922 is main-only, the golden thread only, with one window at 7.8e-5 precision loss; B1920's "not at the apex" rests on the seat's population run with main checking only three parts. Same family as B1918 (retracted), whose fits did not contain the true form.

Runners-up: A3 (B1825: referee reads the same stored census; reach-limited), C1 (B1855: the proved side rests on the seat's search not re-run, P-741), B2 (B1846: its first statement was too wide and was corrected at Review 76).
