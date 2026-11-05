# Review 74 — the SCHEDULED rows of five seats: physics seat (fc), SM-derivation seat, hostile-review seat, chat1, audit seat

Reader's report, 2026-11-04. Read-only: nothing tracked was edited, nothing committed, no branch checked out. Sources read with
`git show` at the pins: `retired/fc-physics-seat@659487bbd`, the SM seat at `d722714f`, `golden_gate/<v>/paper-hostile-review-alero0`
at `6fc86147`, the audit lane at `6f862099` and `84f6b118`. chat1's rows were checked against main only. Main was searched at its
working tree (ripgrep over `frontier/`, `docs/`, `GENESIS.md`, `tests/`). `prescreen.json` was not there when I started; I used my own
searches and cross-checked against it at the end. Its token hits are noisy (R-numbers collide with review items and with the audit
lane's own R-numbers, as P-230 notes).

Firewall: no value, sign or bound for y_b/y_t, θ̄ or y_τ/y_b appears below. Nothing here is compared with data.

## 0. The headline: most of these rows are not unread — the label is a generator miss

**About 41 of the 79 rows were harvested by later main arcs, but the ledger still marks them SCHEDULED.** The rows were written
mechanically by `frontier/B1306_the_older_debt/verification/sliceD/gen_rows.py`, which counts an fc item as named only if the text
says `fc R44`, `fc's R44`, `physics seat R44`, or `R44_X`. For a hostile memo it needs `hostile` or `golden` within 60 characters of
`memo N`. The harvest arcs that took these items wrote them in other ways, so the generator missed them:

- **B1235** cites the R2/R3 rings by finding number (D5, D9–D12, V18, P2).
- **B1237, B1238 and B1240** name the cells as `**R44**`, `R39` and so on, in tables under an "fc harvest" heading.
- **B1134, B1135, B1139, B1142 and B1118** credit the golden_gate memos as "cloud memo N". These are the cloud seat's memos filed
  under the hostile seat's name (P-230).
- **B1303 / B1103, B1304, B1413, B1302 / B1321 / B1414, B1275 and B1290** took the chat1, audit, R72, SM-seat and literature-sweep
  items.

**What is truly unread on main.** Inside this set, only these were never read:

- fc's R1-ring defects other than the B994 and B1225-atom items;
- R53, R55 and R57–R60;
- R29's certificate;
- H1 and H2;
- sm:B1270, B1273, B1274 and B1275;
- the hostile PRIME_LANE ruling.

**What I found on the two axes.**
- **Load (A).** No row bears on the first tier of the debts list (the strip candidate, P10, B1825's machinery). Eight rows bear on
  older debts. Four of these give earlier, independent evidence for debts main registered a month or more later: P-317(b), P-318 with
  P-581, P-427 and P-492. Two would partly pay debts: P-233, and P-317's class (the B1225 lock). Three are new, small corrections that
  never reached main: B1221's table, B964's filing, and B1225's vacuous reproduction script.
- **Leads (B).** None is game-changing for today's open questions. The one untouched idea of real substance is fc's R55 locking
  dictionary, which is about discrete signs, not the 19 values. Four weak or supporting items are listed in §3.

Reading depth, stated honestly:
- **fc R01–R10, R20–R28, R29–R41, R53–R55, R57, R58, R60.** Read at the ring-synthesis level (`R1_REPORT.md`, `R2_REPORT.md`,
  `R3_REPORT.md` in full). R29–R41, R53–R55, R57 and R58 were also read at cell FINDINGS level.
- **fc R11–R19.** Read only through `R2_REPORT.md`'s per-cell diff tables. R18 has no FINDINGS file (the harness blocked it).
- **fc R59, R62.** Read at the `INDEX_R56-R72.md` line only.
- **SM-seat docs.** CHIRALITY_MAP and EXTERNAL_VERIFICATION were read at section level, LITERATURE_SWEEP at headline level.
- **sm:B1269, B1270, B1275.** Headline level plus main's own inventory (`frontier/B1306_the_older_debt/inputs/sm_seat_inventory.md`).
- **sm:B1271, B1273, B1274.** Read in part (first 60–90 lines).
- **Hostile memos.** Read through the seat's MANIFEST and main's arcs. VOICE_LADDER and PRIME_LANE were read directly.
- **Audit lane.** EXTENSION_1, R21 and FINDINGS were read in part.

## 1. Row by row

Key to columns: **A** = does something on main rest on it, or does it question something main cites. **B** = a lead. **C** = where it
was handled.

### chat1 (4)

| row | item | A | B | C | disposition |
|---|---|---|---|---|---|
| 12 | §0: re-adjudicate B1140 ("no hypercharge room") against fc R49 ("two spare Cartan directions") | B1140 = T-64-ORGANIZED; stands, scoped | none | B1303 §1 (`b1303_centraliser.py`): R49 is right for the regular A₁A₁A₂, B1140 for the principal sl₂'s; harvest row 33 VERIFIED-DIFFERS; E69 minted | CLOSED-HANDLED (B1303) |
| 13 | §1(a): χ from the odd-plane determinant in ℤ[ζ₃₀] | no | none | already VERIFIED in the row itself: B1103 THE BEING GATE, re-run in B1303 (1364/1364). "SCHEDULED" survives only in the row's "was:" text | CLOSED-HANDLED (B1103/B1303) |
| 15 | §1(c): the soft scale from sm:B1283's Z′ | no | the fork is registered | VERIFIED as one branch of a fork (B1303 §2–§3); FALSIFIER_REGISTER P9; OPEN_LEADS L203 | CLOSED-HANDLED (B1303) |
| 20 | §5: numbering, attribution, and the scope "SM group" vs SM × U(1)_Z′ | no | none | (iii) landed: MAIN_GOAL l.108, B1293 l.75, B1294 l.130 read "SM × U(1)_Z′, rank 5". The row is self-contradictory ("FIXED" and "SCHEDULED") | CLOSED-HANDLED |

### SM-derivation seat (9)

| row | item | A | B | C | disposition |
|---|---|---|---|---|---|
| 120 | CHIRALITY_MAP: a retrieval document for chirality around sm:B1280; "changes no value" | no | none | sm:B1280's two theorems VERIFIED (harvest rows 5, 8, 10); B1290/B1291 (index formula), B1294 (chirality bit) | CLOSED-HANDLED |
| 121 | EXTERNAL_VERIFICATION: a fresh seat re-derives the spine (18/18) and finds h¹(V)=h¹(V*) on the non-self-dual representations it tested | no | none current. Its §5 list (i)–(v) is the record's own priced input list. Its test-mutation observation (B1242's lock rewriting a tracked JSON) was fixed 2026-09-16 (`tests/test_b1242…py` l.65–68) | B1260/B1268/B1290 lineage | CLOSED-NO-LOAD-NO-LEAD (read at section level) |
| 122 | LITERATURE_SWEEP: the M-theory Higgs-bundle frame; net chirality = χ(M, ∂⁺M) | yes — B1290 applies it | none left | B1277 (harvest), B1290 (applied on main), L204/L205 | CLOSED-HANDLED |
| 125 | sm:B1269: I-26's surviving gauge group per holonomy; the SM algebra is not a centralizer in e₆ | no | none | main's B1275_e8_family_verified integrates it; B1336 | CLOSED-HANDLED |
| 126 | sm:B1270: E₆ as the orthogonal complement of the Eisenstein A₂ in the golden (icosian) E₈; one vector-like 27 pair, net 0 | weak: B1652 l.121/126 cites it as one of four sources withdrawing candidate F4 (Review 66 census: "LIKELY RELIANCE (corroboration)"); W22, B1440 and W23 carry the same conclusion | none (THE_TOWERS records B1736's family group in E₈) | lattice facts verified by main's B1275; fc R64/R67 (harvest rows 104, 107) | CLOSED-HANDLED. Tag the B1652 citation "the seat's, unverified", or drop it, since three other sources carry it |
| 127 | sm:B1271: three generations = the (27,3) of the golden E₈; E₈ forces the family tensor ε, so the tree Yukawa on the triplet is zero | no | none (the "symmetric family tensor" ask is superseded by the fibre frames) | main's B1275 (verified; the open step named), fc R64 (row 104: the object's order-3 element = the family rotation × an E₆ Weyl element, up to E₆ gauge); SM_SEAT_ALIAS_TABLE:49 | CLOSED-HANDLED |
| 129 | sm:B1273: the 3-fold branched cover Y₃ is Hantzsche–Wendt; 3_ρ descends as χ₁⊕χ₂⊕χ₃ (three flat directions); the single allowed cubic forces a zero-diagonal texture, refuted against data | no | weak (see §3, lead 4): the general zero-diagonal lemma. Main's current zero laws (B1701, B1703, B1712/B1716) are its present-frame instances | the Y₃ line superseded by later harvests: B1293/B1294, B1306 A, B1415 (sm:B1356/B1357 on Y₃ and the flat G₂ orbifold); never verified on main itself | CLOSED-NO-LOAD (weak lead) |
| 130 | sm:B1274: the cyclic closings carry one irreducible family class or three characters, never three classes, so no tree-level hierarchy on the object's tower (n ≤ 6, all 48 surjections) | no | supporting negative for B1667 ("the hierarchy is τ's"); never banked | main's L203 was re-registered for a different question (selection among closings) | CLOSED-NO-LOAD (optional: bank as a supporting negative) |
| 131 | sm:B1275: B308's cubic solved explicitly; Jordan ranks of lattice vectors; the mirror's triple has rank 3 | no | none | the cubic itself verified independently by fc R14; sm:B1276 cited (row 42) | CLOSED-NO-LOAD-NO-LEAD |

### Hostile-review seat (6) — memos 10–26 are the cloud seat's (P-230)

| row | item | A | B | C | disposition |
|---|---|---|---|---|---|
| 335 | PRIME_LANE: prime/zeta tools only where they meet open nodes; RH fenced as a boundary question; cells PR-1 to PR-5 | no | none | PR-3 → memo 22 → B1142; PR-2 (unit dictionary) re-derived in B1306 slice C; PR-4 = B1142's GUE test; PR-1/PR-5 parked | CLOSED-NO-LOAD-NO-LEAD |
| 340 | memo 10: one conjugation gives Lorentz signature and compact colour; every hit lands in E₆(−26) | T-SIMUL-CLOSING (low current load) | none | B1134 PROVED, two benches; fc R06 re-ran it with a stronger 3003-pair check; R06's V3: the so(3,1) clause cannot fail within the swapper family (§4, minor) | CLOSED-HANDLED (B1134) |
| 341 | memo 12: the EW slot closes as su(2,1); the gauge branch's host is E₆(−14) | T-row via B1135 | none | B1135 PROVED; fc R06 digit-for-digit | CLOSED-HANDLED (B1135) |
| 345 | memo 22: thirteen cusp resonances below t = 32; the first is a zero of L(χ₋₃) | no | none | B1142 Lane C (numbers reproduced; NEGATIVE for value content) | CLOSED-HANDLED (B1142) |
| 346 | memo 23: sin²θ_W = 3/8 at the symmetry point with the physical charge multiset | P-581 grades 3/8 as REPRODUCED against the GUT class | none | B1139 (memos 23/24, two benches). P-230 moved memo 24's row (347) to VERIFIED but not this one | CLOSED-HANDLED (B1139) |
| 348 | memo 26: frame audit; an unflagged mid-arc S₃ frame switch in B1118 | no | none | B1118 FINDINGS l.49, addendum-beside (2026-08-25) | CLOSED-HANDLED (B1118) |

### Audit seat (3)

| row | item | A | B | C | disposition |
|---|---|---|---|---|---|
| 524 | EXTENSION_1 (its R3): can a common UV mass plus one-loop gauge running supply R2's fitted triplet/doublet split? A bound over the whole threshold range | no | superseded on the gauge-coupling route by the lane's relative-threshold programme (P-396) | harvest row 55 (R1–R3, B1304: the B915 defect VERIFIED; the threshold/mass calculation REGISTERED as the seat's conditional model) | CLOSED-HANDLED (row 55 / P-396) |
| 525 | FINDINGS.md: the lane's pointer index R12–R20 | no | none | B1304 rows 54–76 | CLOSED-HANDLED (B1304) |
| 526 | R21 ANOMALY_COMPLETION: an H-representation 16₊₁+10₋₂+1₊₄ cancels the three-spinor anomaly by added fields; the parallel-Higgs shortcut fails | no | none | B1413 reads R22 against it: valid as an added-field theory; its fermions are not supplied by the source operator | CLOSED-HANDLED (B1413) |

### Physics seat (fc) (57)

| row | item | A | B | C | disposition |
|---|---|---|---|---|---|
| 4 | R72 §4–§6: on m202 the order-3 isometry fixes three lines, giving 3 × (16⊕10⊕1) of SO(10) | no | none left | B1302 (row 24: geometry VERIFIED); B1321 (L205 priced, FAIL: the three costs the golden face); B1414 (E81: nine class members); THE_TOWERS §3 | CLOSED-HANDLED |
| 136 | H1: B267's "the two E₆'s are one E₆" is a type coincidence, not an identification | low: B267 is not used today; its `claim_one_line` still says "are the same Lie object" (checked), so do THE_SPINE l.330 and HINT_LEDGER H64 | none | B272 appended "a consistency check" to FINDINGS in June; the verdict line was never touched | CLOSED-NO-LOAD-NO-LEAD (a one-line wording fix in the P-589 class; §4) |
| 137 | H2: B964 withdrew "the object does not supply a VEV"; B952/B959/B960 and the LAW_MAP rank-obstruction row never got the pointer; B964 is filed RETRACTED with `supersedes: null` | yes, modest: LAW_MAP row "THE RANK OBSTRUCTION (B952…)" (l.378) still ends "which the object does not supply (L133)", unscoped by B964 or by the Wilson-line closings (B1293/B1294); verified today | none | not handled | **DEBT** (P-589 class; §4) |
| 138 | Ring R1 synthesis: ten clusters, 9 MATCH, 1 PARTIAL; the defects are all in the verification layer | yes: B1225 (T-NO-CANONICAL-SELECTOR, T-IDENTIFICATION-IS-AN-INPUT, GENESIS FK12) has a reproduction script that only greps two arcs' claim lines (verified today); step 5's "√ is G-equivariant" is false without a nonnegativity premise the arc never checks | none | D3 (the 17 atoms) → B1225 addendum (B1235); P1/B994 → B1235 cell 4; B955's surjections → B1240 | **DEBT** (B1225's lock, P-317 class; §4). The rest are minor |
| 139 | R10: B1102/B1109's exact hypercharge recomputed blind (18 directions, two orbits of 9, 36/72 moves, an outer move fusing the orbits) | yes: P-233 (debt #36) says T-Y18, T-TWO-ORBITS and T-DEFLATION-P lack an independent reimplementation; R10 is a blind recount of all three in its own code (`r10_blind_solve.py`), though its frame came from B1098/B1100 | none | not used | **DEBT-support** (P-233; §4) |
| 140 | R11: B1183's one-class theorem, MATCH (41 checks); FINDINGS header metadata stale | no | none | — | CLOSED-NO-LOAD-NO-LEAD |
| 141 | R12: B1141's spin payment, MATCH; new leg: the beat derived from m000's own holonomy selects the same lift | no | none (it strengthens T-SPIN-PAYMENT; adoptable) | — | CLOSED-NO-LOAD-NO-LEAD |
| 142 | R13: B904's magic square rebuilt from scratch; full Jacobi 0/76,076 | no | none | — | CLOSED-NO-LOAD-NO-LEAD |
| 143 | R14: B884's cubic, two constructions, MATCH; prose slip (three {2,3,6} cells, not two) | no | none | — | CLOSED-NO-LOAD-NO-LEAD |
| 144 | R15: B892's Second Measurement Theorem, MATCH; the wall proved complex exactly; its lock is text-only | no | none | — | CLOSED-NO-LOAD-NO-LEAD |
| 145 | R16: the Kashaev tower's coefficients C0–C4, MATCH | no | none | deepened by R28 | CLOSED-NO-LOAD-NO-LEAD |
| 146 | R17: B1126 MATCH; B1137's PSLQ gate cannot pass any true relation at physical precision (planted 5V − 3L(1,χ₋₃) − 2π = 0 fails), so its true outcome type was FLOOR | **yes**: B1137's DISJOINT feeds the kill graph, T-VALUE-REGULATOR, THE_SM_VERDICT, B1179 and B1217 | none | P-317(b), found again by main's sweep on 2026-10-23, still QUEUED; fc saw it first (2026-09-01) and supplies a ready planted control; B1137 also has internal prose conflicts (384 vs 400 null cells) | **DEBT** (already carried as P-317(b)) |
| 147 | R18: B1003's genesis forks F2/F8, MATCH (no FINDINGS file; R2 report only) | no | none | — | CLOSED-NO-LOAD-NO-LEAD |
| 148 | R19: B725's Born form (scoped), MATCH; the lock's falsifier is vacuous | no | none | — | CLOSED-NO-LOAD-NO-LEAD |
| 149 | Ring R2 synthesis | via D5/V8 | none | B1235 (D5/D9: the family is 38/112 amphichiral; V18); V8 → P-317(b) | CLOSED-HANDLED (except V8 = row 146) |
| 150 | R20: the family separator H₁ = ℤ stands; amphichirality 38/112; "exactly 14" is a truncation (21) | no | none | B1235 cell 1; B1136 addendum (B1472) for amphichirality. Not propagated: B1136 l.23 still says "exactly 14", and `verify_genericity.py:29` breaks at i > 1200 | CLOSED-HANDLED (minor note, §4) |
| 151 | R21: B1234's residual checks (base rate 6/200; Gieseking cover), MATCH | no | none | — | CLOSED-NO-LOAD-NO-LEAD |
| 152 | R22: B1148's chain "6615 → 4 → 1" mixes conventions; with the full tensor it is 6615 → 9 → 1; the theorem is unchanged | no | none | B1235 cell 7: HELD (certificates off main) | CLOSED-NO-LOAD-NO-LEAD |
| 153 | R23: B1186's 2√3i carriers and quine, MATCH | no | none | — | CLOSED-NO-LOAD-NO-LEAD |
| 154 | R24: B1163's family-wide addenda fall (m202, s118, o10_150700 are chiral); the headline stands | no | none | B1235; B1163 ADDENDUM_2026-09-02; RETRACTIONS | CLOSED-HANDLED |
| 155 | R25: B1127's torsor, 4 of 48 compact-colour elements, MATCH | no | none | — | CLOSED-NO-LOAD-NO-LEAD |
| 156 | R26: B1080 residuals and B1011's C5/C6 (992/284), MATCH; B1011's lock was arithmetic on literals | no | none | B1235 cells 6 and 8 | CLOSED-HANDLED |
| 157 | R27: B994's exhibited chains are not subgroup chains; two menus never committed | no | none | B1235 cell 4; B994 addendum | CLOSED-HANDLED |
| 158 | R28: the Kashaev deep tail, 67–88 digits | no | none | — | CLOSED-NO-LOAD-NO-LEAD |
| 159 | R29: Krawczyk interval plus exact certificates: all 112 family members' shapes in ℚ(√−3), exactly; 183 cusp moduli exact | indirect: "the object is the family" (the owner's reframe), yet B1186's family is a double-precision prefilter | an adoptable instrument (§3, lead 5) | none on main (no Krawczyk anywhere in frontier/) | CLOSED-NO-LOAD (adoptable) |
| 160 | Ring R3 synthesis | via D9–D12, H1, H2 | none | B1235 (D9–D12, V18); H1/H2 = rows 136/137 | CLOSED-HANDLED (except H1/H2) |
| 161 | R30: Sym(m004) = D4 of order 8, amphichiral | no | none | — | CLOSED-NO-LOAD-NO-LEAD |
| 162 | R31: B208's radicand divides the period, swept to 300 000 | no | none | B1237 (listed as MATCH) | CLOSED-HANDLED |
| 163 | R32: B213's four misquotes; the curve is not 40a1 | no | none | B1237 row 9; B1238 (the character variety IS 40a3, EARNED) | CLOSED-HANDLED |
| 164 | R33: trace fields; bronze has degree 8 | no | none | B1237; B1238 (the bronze octic; E55, E56) | CLOSED-HANDLED |
| 165 | R34: E₆'s 27 is complex and the 78 real, from the Cartan matrix | no | none | B1237 (listed) | CLOSED-NO-LOAD-NO-LEAD |
| 166 | R35: ten census rows; B258 wrongly infers silver non-arithmetic | no | none | B1237 rows 1–2 (silver arithmetic; E55) | CLOSED-HANDLED |
| 167 | R36: batch 2; B333's discriminant-filter bug (16 of 122, not 14 of 123) | no | none | B1237 row 8 | CLOSED-HANDLED |
| 168 | R37: B850's multiplicity maxima are word-count artefacts | no | none | B1237 row 7 | CLOSED-HANDLED |
| 169 | R38: B854/B866 rerun; B919's runner cannot run from the repository | no | none | B1237 row 3 (C42's witness relocated) | CLOSED-HANDLED |
| 170 | R39: a deleted Z₁ ladder recovered and re-run | no | none | B1238: VERIFIED, nothing was lost | CLOSED-HANDLED |
| 171 | R04: B863 termination and B994 rule variation, MATCH; B994 provenance | no | none | B1235 cell 4 | CLOSED-HANDLED |
| 172 | R40: B516's Pisot quartics | no | none | B1238 VERIFIED | CLOSED-HANDLED |
| 173 | R41: four trace-map identities | no | none | B1238 VERIFIED | CLOSED-HANDLED |
| 176 | R44: B549's seven numbers are the Perron eigenvector of E₇'s adjacency matrix, not the Cartan spectrum | no | none | B1240 (B549 addendum) | CLOSED-HANDLED |
| 178 | R46: codex certificates rerun | no | none | B1240 → L198 | CLOSED-HANDLED |
| 179 | R47: outside-bench certificates; the up-Yukawa layering | no | none | B1240 (dated bracket at SM_SPECIFICATION_LEDGER:19) | CLOSED-HANDLED |
| 180 | R48: B511's script is numerically broken; its claim reproduces | no | none | B1240 (a 200-bit re-implementation) | CLOSED-HANDLED |
| 181 | R05: the ℤ₆ kernel, MATCH; B1221's primitivity addendum table is wrong: rescaling all charges by k gives a kernel of order 6k, not 6·gcd(k,12) | yes, modest: the ℤ₆ global form is graded in P-581 (debt #20) and stated in the paper; the addendum's "kernel = 6 exactly when gcd(k,6) = 1" is false (μ_k ⊂ U(1) acts trivially after rescaling) | none | not handled (checked today: `frontier/B1221_*/ADDENDUM_2026-08-31_the_Z6_needs_primitivity.md` l.16–25 unchanged) | **DEBT** (small; feed P-581; §4) |
| 182 | R50: B775's V4 table right, script broken | no | none | B1240 CONFIRMED | CLOSED-HANDLED |
| 185 | R53: the McKay route (conductor → SL(2,ℤ/N) → binary polyhedral) has image {A₀, E₆, E₈}; on hyperbolic manifolds it gives E₆ or nothing, so "carries E₆" means "shape field ℚ(√−3)"; B208's and B210's uniqueness depends on the convention | yes: P-318 (debt #16: B997's golden uniqueness fails at m = 4) — R53 had already listed m = 4 in the ℚ(√5) Lucas family (2026-09-02); and P-581 ("the route to E₆ is generic") | small, for THE_TOWERS: the object's arithmetic emits only the tower's top (E₆ geometric, E₈ monodromy), never SO(10) or SU(5) | P-318 and P-581 open; B993's base-rate addendum | **DEBT-support** (P-318, P-581; §4) |
| 186 | R54: every tracker is mirror-even or mirror-odd; the odd sign is one chosen bit | yes, through the cell's CHIRALITY_LEDGER (campaign/phaseF): **F4** is P-427(i) exactly (B723 still PROVED after its clause was refuted; LAW_MAP's B717 row; checked: B723 verdict still PROVED), seen 2026-09-02; **F5**: B783 types the letter swap as γ5, but it is the mirror c | none (the theorem is B1163/B1168/B1169/B766's) | P-427 open | **DEBT-support** (P-427; §4) |
| 187 | R55: THE LOCKING DICTIONARY — the object's closing bits {c, γ5, θ} mapped onto reality's discrete flips modulo CPT, with locking predictions | no | **LEAD** (§3, lead 1) | none: no CPT sign-locking anywhere on main (B709 is Turok's CPT, a different statement) | LEAD |
| 189 | R57: the rule is the 3-braid σ₁σ₂⁻¹; braid index of 4₁ is 3; M² cycles the fibre's three half-periods; proposes a fibre frame with matter at the three points | no | already realised: it anticipated by a month the fibre frame main built independently (B1651; THE_WEAVE's half-period lines; P-136). Fact (3) was retracted by R60 | B1651, THE_WEAVE l.483–488, 711–719 | CLOSED-NO-LOAD (a seen-first note owed; §5) |
| 190 | R58: ι-parity (the fibre's −I): the three classes on m004 are ι-even; the fibre carries ι-odd sectors of 6 and 10, sourced by the half-periods (Lefschetz checked) | no | weak (§3, lead 6) | none | CLOSED-NO-LOAD (weak lead) |
| 191 | R59: the ι-twisted closing is the sister m003; no cyclic cover keeps an ι-odd class | no | none | — | CLOSED-NO-LOAD-NO-LEAD |
| 192 | R06: B1134/B1135 recomputed, MATCH (a stronger 3003-pair check); the so(3,1) clause cannot fail within the swapper family | low: T-SIMUL-CLOSING's wording | none | — | CLOSED-NO-LOAD-NO-LEAD (V3 noted in §4) |
| 193 | R60: correction — the record's θ is the strong inversion; all three 27-classes are θ-odd; B347's (−1)^{m+1} reproduced | no (confirms B347) | none | — | CLOSED-NO-LOAD-NO-LEAD |
| 195 | R62: the cusp symmetry group; the mirror is broken by every filling, θ by none | weak: cited, unverified, in B1277 (bears on B432) and B1290 | none | the mirror half agrees with main's B1239 §3; the R69 correction was harvested (B1294, B1296) | CLOSED-HANDLED (cited with its caveat) |
| 199 | R07: B952/B955's rank wall, MATCH; the scan cannot fail by design; "order ≤ 6" is order 18 in simply-connected E₆ (prose) | no | none | B1240 (B955's surjections) | CLOSED-NO-LOAD-NO-LEAD |
| 200 | R08: the generation obstruction B298/B307/B1161, MATCH; locks hard-coded; a scope constant reads too strong | no | none | — | CLOSED-NO-LOAD-NO-LEAD |
| 201 | R09: the scale cluster, MATCH; c = 6σ checks only the algebra, and all its physics sits in the identification G_N = 1/(4σ) | yes: P-492 (debt #60: B1088's c = 6σ and B1034's bridge rest on an unread boundary assumption); R09 flagged the same gap on 2026-09-01 | none | P-492 open | **DEBT-support** (P-492) |

## 2. Totals (79 rows)

- **CLOSED-HANDLED: 41.** The SCHEDULED label is stale; the harvest arcs are named above.
- **CLOSED-NO-LOAD-NO-LEAD: 29**, of which four carry a weak or supporting lead: rows 129, 130, 159 and 190.
- **DEBT or DEBT-support: 8.**
  - Rows 137, 138 and 181 are new corrections not yet on the register.
  - Rows 139, 146, 185, 186 and 201 add evidence or a ready control to debts already open: P-233, P-317(b), P-318/P-581, P-427 and
    P-492.
- **LEAD: 1** (row 187).

By seat:

| seat | handled | no load, no lead | debt or support | lead |
|---|---|---|---|---|
| chat1 | 4 | 0 | 0 | 0 |
| SM | 5 | 4 | 0 | 0 |
| hostile | 5 | 1 | 0 | 0 |
| audit | 3 | 0 | 0 | 0 |
| fc | 24 | 24 | 8 | 1 |

## 3. The strongest leads, ranked (none is game-changing on today's numbers)

**1. R55, the locking dictionary (row 187). The only real idea in the set that main never touched.**
- **The idea.** B766's closing lattice has three bits {c, θ, γ5}. R54e re-derived c and γ5 from Sym(m004); θ and the identification
  T3 = T7 are taken from B766. Reality has three discrete flips (P, C, T), which reduce to two modulo CPT. A dictionary assigns c and
  γ5 to two of the three.
- **What R55 found.** Of the six assignments, three agree with what the object's axes mean. Only one (c = P, γ5 = T) has both rows
  populated by sign types that are already measured. Under it, signs that look independent are locked to one bit: a lepton-sector CP
  sign is not a free bit, and two combinations are excluded. One sign class touches EDM-type observables. The firewall applies there:
  I report no sign.
- **First computation (data-free).** Re-derive B766's θ column and the T3 = T7 identification on main; R55 did not. Then check that
  today's chirality bit (THE CROSSING: the bit is the word state's sign) is B766's c. The dictionary has to be rebuilt on the current
  bit before anything is sealed.
- **What it would change.** It would be the programme's first discrete, refusable statement about the CP/T sign sector. It moves
  nothing on the 19 values, except at most a relative sign.
- **Why main has not done it.** The row was never read (the generator missed it). Any sign comparison also needs the owner's
  directive and a sealed design.
- **Caveat.** R55 quotes measured signs from memory. F5 (B783's γ5 typing) does not affect it, because R55 uses R54e's γ5.

**2. R10 as the missing control for P-233 (row 139). Debt-paying rather than a lead, and the most immediately usable.**
- **The idea.** A blind, own-code recount of the 18 exact hypercharge directions, the two orbits of 9, the 36/72 set-preserving
  moves, and the outer move that fuses the orbits. Together these are exactly T-Y18, T-TWO-ORBITS and T-DEFLATION-P.
- **First computation.** Run `R10_exact_hypercharge/r10_blind_solve.py` from the retirement tag on this bench. Then replace the
  frame it took from B1098/B1100 with one built from the Cartan matrix alone. That would be P-233's "no shared code" control.
- **What it would change.** It pays part of debt #36 on registry theorems that the hypercharge line still cites.
- **Why not done.** Never read.

**3. R53, the image of the McKay route (row 185).**
- **The idea.** Over every conductor N ≤ 24 the route emits only {A₀, E₆, E₈}. On hyperbolic manifolds it emits E₆ or nothing. So
  "m004 carries E₆" says exactly "the shape field is ℚ(√−3)". The uniqueness in B208 and B210 depends on which convention is used:
  the field discriminant, or det(γ+I) = m²+4.
- **For THE_TOWERS (P-415).** The object's arithmetic emits only the top of each tower: E₆ on the geometric side, E₈ on the
  monodromy side. SO(10) and SU(5) can only appear through the cascade or the loci. This is consistent with sm:B1270's E₆ = the
  centralizer of the Eisenstein A₂ in the golden E₈.
- **First computation.** Restate B208's and B210's rows (LAW_MAP's two-ended theorem) with the convention named. Attach R53's
  enumeration to P-318's m = 4 correction and to P-581's genericity rule.
- **What it would change.** The scope of a load-bearing "object fact". No numbers.
- **Why not done.** Unread. Main reached part of it independently on 2026-10-23 (P-318).

**4. sm:B1273's texture lemma (row 129).**
- **The idea.** When generations are told apart only by abelian characters and the Yukawa is a single cubic invariant, the selection
  rule χ₁χ₂χ₃ = 1 forces a zero-diagonal mass matrix.
- **Bearing.** This is the same class of wall as today's "the CKM wall is the Higgs's construction". Stated across frames, it would
  say which Higgs characters are needed for non-aligned up/down supports.
- **First computation.** In B1656's frame, list the characters of the three zero modes and of each Higgs component, and read off the
  supports of Y_u, Y_d and Y_e. Then check whether S291's adjugate relation follows from the selection rule alone.
- **Why it is weak.** Main's zero laws (B1701's 0:1:1, B1703's N∣3 zero, B1712/B1716) are already the current-frame instances. B1273
  adds a precedent, not new content.

**5. R29, an exact certificate for the family (row 159).**
- **What it is.** Krawczyk interval certificates plus exact ℚ(√−3) gluing show that every one of the 112 members has its shapes in
  ℚ(√−3) and its complete structure. All 183 cusp moduli are exact. It has negative controls (torus knots refused, a perturbed m004
  refused, m015/m016 refused).
- **First computation.** Vendor `r29_krawczyk.py` and `r29_exact_shapes.py`. Re-run them on the family as main now defines it
  (B1186's 112, and the 99 shape-field members its 2026-10-02 addendum separates from the 13 non-arithmetic ones; OPEN_LEADS
  xB015).
- **What it would change.** The family is "the object" at the owner's word, yet its definition rests on a double-precision
  prefilter. This makes the positive half a theorem; the completeness half stays numerical.
- **Why not done.** Unread. Main's family checks use SnapPy without Sage, so no verified routine is available.

**6. R58's ι-odd sector of the fibre (row 190).**
- **The fact.** The fibre group carries ι-odd classes (6 and 10 for Sym⁸ and Sym¹⁶). They are sourced by the three half-periods, and
  the Lefschetz traces check this. The monodromy-fixed line is always ι-even.
- **Bearing.** Today's frame lives on that fibre, and z ↦ −z is a symmetry of it. Nobody has asked whether the frame's sector-odd
  structures (P-591's RI-1, the signed Laurent constant) are ι-parities.
- **First computation.** The ι-parity of the three zero modes and of each Higgs component in B1656's frame.
- **Prior.** Low. I could not tell from the record whether the frame's quaternion twists already fix this parity.

**7. sm:B1274's tower negative (row 130).**
- **What it is.** On every cyclic closing of the object up to n = 6, for all 48 surjections, there are never three irreducible
  family classes, so there is no tree-level hierarchy from closings.
- **First computation.** Re-run `tower_and_doubles.py` at d722714f, then extend it to n ≤ 12 by B1303 §5's deck-eigen law.
- **What it would change.** It closes the closing route to the hierarchy with an object-side theorem, supporting B1667. It is not new
  physics.

## 4. DEBT candidates

New, not on the register:

**D1. B1225's reproduction script is a citation grep (row 138).**
- **Where it is used.** B1225 underlies T-NO-CANONICAL-SELECTOR and T-IDENTIFICATION-IS-AN-INPUT, and GENESIS FK12 cites it.
- **What I checked today.** `frontier/B1225_no_canonical_selector/verification/reproduce.sh` checks only that B1203's and B1191's
  `claim_one_line` contain the strings "11720", "c-equivariance" and "GC-15". It then prints REPRODUCES.
- **fc's R01.**
  - It is the first machine check: 17/17 atoms fixed; 0/1173 moved in the single-operation stratum; a planted mirror-odd atom moves
    69/648.
  - It found that step 5's "√ is G-equivariant" is false without a nonnegativity premise. This is benign only because all 17 atoms
    are real, and the arc never checks that.
  - The theorem's one failable premise is the reality of the atoms; the rest is definitional.
- **Owed.** Vendor R01's check, add the one-line reality assertion, and file it under P-317's class.

**D2. B964's filing and the rank-obstruction row (row 137).**
- **What I checked today.**
  - B964's `arc_verdict.json` says RETRACTED with `supersedes: null`, although it withdraws other arcs' claims (B818's rule).
  - B952, B959 and B960 carry no pointer to B964.
  - LAW_MAP l.378 ends "a Higgs VEV, a Wilson line/Hosotani flux, or an orbifold projection — which the object does not supply
    (L133)". It is scoped neither by B964 (the cascade IS an adjoint Higgs mechanism) nor by the Wilson-line closings (B1293/B1294:
    the gauge algebra is reached, on an observer-selected vacuum).
- **Why it matters now.** The Higgs's construction is today's bottleneck. This is P-589's class: a correction that reached its arc
  but not the synthesis surface.

**D3. B1221's primitivity table (row 181).**
- **The error.** The addendum's table and its sentence "|kernel| = 6 exactly when gcd(k,6) = 1" are wrong. After rescaling every
  charge by k, μ_k ⊂ U(1) acts trivially, so the kernel has order 6k. The listed values equal 6·gcd(k,12), the trace of a search
  truncated at 12-torsion.
- **Direction.** The error strengthens the addendum's own conclusion: the ℤ₆ needs the primitive normalisation exactly.
- **Owed.** A dated correction, carried into P-581 (the ℤ₆ structural grade).

Existing debts, with earlier evidence or a ready control from this set:

- **D4. P-317(b), B1137 (row 146).**
  - fc's R17 found it on 2026-09-01, seven weeks before main's sweep.
  - R17 supplies a ready planted control, 5V − 3L(1,χ₋₃) − 2π = 0. At digits = 250 it is found, then rejected by the stability gate;
    at 60 and at 10 digits it is not found.
  - It also records B1137's two prose conflicts: 384 vs 400 null cells, and the "stable, height-legal" sentence.
- **D5. P-233 (row 139).** R10 as a partial independent control (§3, lead 2).
- **D6. P-318 and P-581 (row 185).** R53 (§3, lead 3).
- **D7. P-427 (row 186).** fc's CHIRALITY_LEDGER F4 is P-427(i) itself, seen 2026-09-02. F5 adds that B783's γ5 typing of the letter
  swap does not survive (the swap is the mirror c). I did not find a B783 arc directory, so I did not check where that typing still
  lives.
- **D8. P-492 (row 201).** R09 is the earlier flag that c = 6σ checks only the algebra and that the physics sits in G_N = 1/(4σ).

Minor, hygiene only (no load), for the next P-317 or P-589 sweep:
- B267's `claim_one_line` and HINT_LEDGER H64 (row 136).
- B1136 l.23 still says "exactly 14", and `verify_genericity.py:29` breaks at i > 1200, so the true count at ≤ 6 tetrahedra is 21
  (row 150).
- `tests/test_b1011_mckay_tensor.py:72` still ends `… or True`, which makes the assertion vacuous (fc R02's V2).
- T-SIMUL-CLOSING says "realizes so(3,1)", but that clause cannot fail inside the swept family; the falsifiable content is the
  E₆(−26) landing (row 192).
- B955's "order ≤ 6" is in the adjoint parameterisation (order 18 in simply-connected E₆) (row 199).
- B1225's W1 = 11,720 cannot be rebuilt from main's files. Its enumerator lives on the outside-bench branch.

## 5. Ledger and credit

- **Ledger.** The 41 handled rows should move from SCHEDULED to their arcs (§1). Rows 13 and 20 contradict themselves ("VERIFIED"
  or "FIXED" beside "SCHEDULED"). The slice-D grammar for fc and for the hostile seat is the cause; a re-run with
  `\bR\d+\b` inside fc-harvest arcs, and `cloud memo N` for the golden_gate memos, would reclassify most of them mechanically.
- **Seen-first credit owed in the record.**
  - fc R17 for P-317(b).
  - fc R09 for P-492.
  - fc R53 for P-318's m = 4 point.
  - fc's CHIRALITY_LEDGER F4 for P-427(i).
  - fc R57 for the fibre's three half-periods as matter points, a month before B1651. Note that THE_TOWERS' "not on record" sweep
    searched arcs only.
