# Review 74 — the SCHEDULED rows of the four retired seats (cc3 paper seat, cc3 braver-questions, qor5up, codex)

Reader's report, 2026-11-04. REPORT ONLY: nothing on main edited, nothing committed, no branch checked out. Sources read with
`git show <tag>:<path>` at the pinned archive tags `archive/cc3-paper-lane@a31456d2`, `archive/braver-questions@53da05f6`,
`archive/qor5up@3851df2a`, `archive/codex-seat-r001@f7a49536`. No `prescreen.json` existed when this reader started (only
`prescreen.py`); the rows were extracted from `docs/HARVEST_LEDGER.md` directly (96 rows: cc3 42, braver 5, qor5up 30, codex 19).
The codex rows were read by a delegated reader under the same brief and are reported in §4 as that reader returned them,
with this reader's spot-checks marked.

**Firewall kept.** No value, sign or bound for y_b/y_t, θ̄ or y_τ/y_b is written here; nothing is compared with measured data.

## 0. Three facts that change how these rows should be read (found before the row-by-row)

1. **The qor5up rows are not unread. All 30 were dispositioned on main at B1060's DIGEST_LEDGER (2026-08-13/14), under
   the alias `qB10nn`.** Lane 1 rows 1.02–1.30 are the seat's B1025–B1053 one-to-one, row 4.8 is its B1054 (its Review 1);
   four are REBUILT on main's bench (qB1029 the seam's class field, qB1039 the B141 correction, qB1048 the contraction
   boundary — which spawned the landed `frontier/B426_scale_lever_closed_form/ADDENDUM_BOUNDARY_2026-08-14.md`), the rest
   ACCEPTED-WEAK/RUN. B1173 partial-closed the digest; the 13 NOT-REACHED rows (lanes 3–5, process instruments and the
   seat's 12 leads qL155–qL166) are the umbrella lead **L185**, PARKED in `docs/THE_REMAINING_MATH.md` row 8 ("bookkeeping-grade,
   no math blocked on it"). The prescreen's number-grep could not see this: the seat's numbers collide with main's own
   B1025–B1054 (`frontier/B1025_input_derivability` … on main are different arcs), and the digest cites them as `qB…`.
2. **B1416 (2026-09-16, THE RELAY RESIDUE CLOSED) already re-read about a dozen of these items against the archive tags**,
   writing new ledger rows 623–630 (B8087, B8143 verified-earlier; **B8148 REFUTED**; B8080, B8121, B8123/B8107 registered;
   codex R031D verified; codex wave-9 map registered) — but it marked only rows 261 and 316 and 237 superseded in words; the
   original SCHEDULED rows were left standing. Row 623 is itself in this reader's 96 only because its disposition contains
   the word "SCHEDULED" ("row 261's SCHEDULED is superseded").
3. **The P3 paper sweep `papers/P3_THE_PAPER/sweep_s10/w6.items.json` graded several of these items against the paper**
   (B8087 MUST, B8072 SHOULD, B8068 NO, B8148 NO-refuted, B8097's L1 NO-superseded, B792 NO, B784 NO). Its B8072 entry
   says, correctly, that the item was "never subsequently read into a main arc".

So most of the 96 are handled or bookkeeping. What is left that matters is small and is ranked in §6.

## 1. cc3 paper seat (42 rows) — `archive/cc3-paper-lane@a31456d2`

Every FINDINGS.md was read in full except B8075, B8076, B8148–B8150, B8153 (no FINDINGS; their `arc_verdict.json` /
`results.json` / CAMPAIGN.md read); B8108, B8114, B8131, B8134–B8137 read at verdict level. Note: the seat's B8068–B8080 were
first minted as B1068–B1080 and remapped (docs/CLOUD_ALIAS_TABLE.md lines 80–107: B8068 and B8069 "not yet ported").

| row | item (<25 words) | A load | B lead | C handled | disposition |
|---|---|---|---|---|---|
| 245 | B8068: J^{2T} (principal-2T-fixed Jordan subalgebra of the 27) ≅ the charge field K; cells 3/4/AXIS0/AXIS3/ITEM1: the object's rank-1 invariants reach so(10) and stop | no (alias table: not ported) | **LEAD** (§6 L3): cell 4 — every canonical rank-1 invariant has zero 16-component under all three so(10)s, so SO(10)→SU(5) cannot be taken from them; AXIS0 — an ω-twisted line in the 16 meets the pure-spinor cone in two points iff μ splits mod p (56 primes, exact quadric owed), i.e. a candidate finite point set over L = K(√77) where main says "a condition, not a point" (B1092); AXIS3/B8073 — su(5) not τ-stable in the swept families. Bears on X10/X19, THE_TOWERS P-415 and §8 (matter parity). Main never touched the spinor cells. **Re-run here with the seat's own scripts (REPRODUCED, not VERIFIED):** `cell4_spinor.py 1093` — all three so(10)s have Casimir multiplicities [1, 10, 16] and the 16-components of e₁, e₂, e₃ are zero in every case; `cell6_pure.py 1231` (μ splits) — the ω-line has span 2 in the 16 and exactly 2 of 1232 projective points are pure (stabiliser 34, Killing rank 24); `cell6_pure.py 1009` (μ has one root) — 0 pure points. | cell 1 ≈ main's L138/B969 (the canonical pair's Kato–Yukie invariant is K) and C28; cell 2 withdrawn by the seat | **LEAD** |
| 246 | B8069: Stein + affine isotropy fix B527's metric up to one scale; a (3,1) conformal structure; dimension count generic, PD∩Stein at 2.5 % base rate | no (not ported) | none for current questions (the B526/B527 transfer-operator metric lane) | extends main's B527 | CLOSED-NO-LOAD-NO-LEAD |
| 248 | B8071: in e₆(2), orbit A2 has compact su(3)⊕su(3) at 3 of 64 characters; the 2A1 centraliser is never compact there | no | minor: corroborates by compactness the A2 class main reached (B1098) without lowering its 1-of-20 price | B1098 (A2 → trinification su(3)⊕su(3) at rank 4; 2A1 excluded by a commutant argument) | CLOSED-HANDLED (B1098; a compactness addendum is optional) |
| 249 | B8072: the matching-capacity floor — a calibrated Poisson-placement model; most tested targets sit where a match carries no information | no — P3 sweep graded SHOULD, "never read into a main arc" | **LEAD** (§6 L1): a per-target information budget, computable before a level-2 confirmation is chosen (P-585, GAP1 v1.60) and directly on S291's "would we recognise the answer" (FRAMING_LEDGER §G) | none | **LEAD** |
| 250 | B8073: the object's su(5) (A = (34,24)) is not τ-stable: A∩τ(A) rank 3 over ~1557 characters per prime, intertwining gated | no (ERROR_LEDGER E48 names it only for a digest corruption) | part of the B8068 cluster (§6 L3): the reality step; scoped "no character in the swept family" | none | fold into L2; standalone CLOSED-NO-LOAD |
| 252 | B8075: the structure paper's 14-value rung spectrum is not attained (coordinate subsets give 12, 30, 78; 6, 8, 10 impossible) | no (cc3's structure paper; main's ladder is B874's {78,46,30,12}) | none | superseded within cc3 by B8078/B8079/B8149 | CLOSED-NO-LOAD-NO-LEAD |
| 253 | B8076: the paper-closure campaign, twelve items GREEN (item 6: π₁(4₁) has 48 surjections onto 2T, none onto 2I or A₅) | no | none | item 6's count is main's C6 (J(m004) = 1, 48 surjections; row 628) | CLOSED-NO-LOAD-NO-LEAD |
| 254 | B8077: the SM algebra is compact in e₆(2) (36/36); so(10)⊃su(5)⊃SM compact in e₆(−14); existence, not occupancy | no | none beyond §6 L3 | consistent with B1138's fork (E₆(−14) the charges) | CLOSED-NO-LOAD-NO-LEAD |
| 256 | B8079: the rung arrangement exact over ℚ (109 flats, eleven values) and the 64 Levi subsystems | no | none | cc3-internal (B8136, B8149) | CLOSED-NO-LOAD-NO-LEAD |
| 257 | B8080: the paper's assembly classification is false — all six candidate groups admit a 27-dim zero-radical assembly | no — "main's entrance never relied on it" | none | **B1416, row 626** | CLOSED-HANDLED (row 626) |
| 258 | B8084: cold audit of B1075 — no negative bias; the request counted B929's standing Tier-1 pass as a miss | no | none | RELAY_LEDGER (EVERYTHING_FROM_THE_AUDIT_SEAT: "COLD AUDIT VERDICT … CLEAN"); B929 counted as a shape hit in P-104's census | CLOSED-HANDLED |
| 259 | B8085: Route A's arithmetic obstruction is absent — h⁺(K) = 1, |Cl/Cl²| = |Cl/Cl³| = 1 | no | none | **B1093** (L169, h = h⁺ = 1 PROVED); B1099 (the counter is frontier mathematics) | CLOSED-HANDLED |
| 261 | B8087: ⟨ν^c⟩ purity — a condition, not a point | no | none | **row 623 / B1092** | CLOSED-HANDLED |
| 264 | B8090: B1076's "new exact character" mis-stated on summary surfaces (then the seat's own first diagnosis retracted) | no | none | RELAY_LEDGER (§4 character-kernel fix landed on B1076's summary layer) | CLOSED-HANDLED |
| 266 | B8092: design audit of the B1074/B1076 hunt prompts — three guards that can only remove candidates (incl. no grade for a partial positive) | questions an old closed crossing lane; nothing current rests on it | its finding 3 converges with main's CANDIDATE grade | finding 1 tested by cc3's B8096 (negative stronger); finding 3 ≈ **B1829 / GENESIS v1.61** | CLOSED-HANDLED |
| 269 | B8095: related-work armor, five differentiators (Lisi/Distler–Garibaldi …), each ending in a non-claim | no | none | paper positioning | CLOSED-NO-LOAD-NO-LEAD |
| 270 | B8096: the residue hunt re-run with the guard relaxed — no candidate; the 77 dies as a field property | no | none | answers B8092 f.1 inside cc3 | CLOSED-NO-LOAD-NO-LEAD |
| 271 | B8097: buried-results census — REPRESENTATION_TRIAGE's 12 PENDING rows and B985's six over-wide closures, L73 falsified | no | none new | **docs/OPEN_PROBLEMS.md §7** and THE_LADDER surface it (Review 47); L73 marked FALSIFIED in OPEN_LEADS | CLOSED-HANDLED (the PENDING synthesis rows are still bookkeeping debt) |
| 272 | B8098: L1 — volume and arithmeticity cannot tell m004 from m003 | no | none | superseded: the object is the family (owner, 2026-10-04); P3 sweep cites the Jørgensen-number selection | CLOSED-HANDLED |
| 276 | B8103: the specialist register re-dated; the E₆ character-variety novelty claim survives a re-search | no | none | OPEN_LEADS specialist register row (B264/B274/B347) | CLOSED-NO-LOAD-NO-LEAD |
| 278 | B8105: R48 phase 1 — THEOREM_REGISTRY violated its own same-PR rule | no | none | R48-F1 response (CHANGELOG 2026-08-21: backfill + `creates_law` gate) | CLOSED-HANDLED |
| 279 | B8106: R48-F2 — GUT_REQUIREMENTS_LEDGER said the object cannot reach rank 4 after B1098 | no | none | R48-F2 answered (CHANGELOG 2026-08-21) | CLOSED-HANDLED |
| 280 | B8107: R48 verification; R48-F4 (`creates_law` missing from BANKING_PROTOCOL) | no | none | **row 628**; BANKING_PROTOCOL | CLOSED-HANDLED |
| 281 | B8108: R48 phase 3 — 13 of 36 lagging surfaces carry supersession banners; the remedy is a banner | no | none | Review 48 doc wave | CLOSED-HANDLED (verdict level) |
| 287 | B8114: the related-work armor (duplicate of B8095) | no | none | — | CLOSED-NO-LOAD-NO-LEAD |
| 293 | B8120: P1 scrutiny triaged against cc3's own paper | no | none | the "ℚ(√−3) ⟹ 2T as a theorem" ask answered NEGATIVELY on main: 35 of 112 family members lack the door (**B1416, row 628**) | CLOSED-HANDLED |
| 294 | B8121: M4 — BMR cyclic commensurability, the sentence repaired | no | none | **row 627** | CLOSED-HANDLED |
| 295 | B8122: constructive items (det(A²−I) = −m², the m = 6 class threshold, A₂+A₁ has no 3A₁) | no | none | paper-internal | CLOSED-NO-LOAD-NO-LEAD |
| 296 | B8123: P1 scrutiny closed, one live defect fixed | no | none | **row 628** | CLOSED-HANDLED |
| 297 | B8124: the golden-meridian φ-law — its tone component is the identity φ·1/(2φ) = 1/2; the content is the (wx, wz) scaling | **yes, scope**: Review 48 registered exactly this as **R48-2** ("verify cc3's B8124/B8126 … and narrow T-GOLDEN-MERIDIAN to the off-tone components", OPEN_LEADS line 19); carried R49-5 → R50-6 → R51-5 → R52-5 and then dropped as "cc3's items CLOSED BY RETIREMENT" (REVIEWS.md l. 4515). LAW_MAP row 478 and THEOREM_REGISTRY T-GOLDEN-MERIDIAN still state the law unscoped; B1137 cites B1132. Not re-verified by this reader | none | none — closed by retirement, not by computation | **DEBT (low)**: verify with B1132's own script and scope LAW_MAP 478 (P-589 class) |
| 299 | B8126: the four Pauli components split against B8111's 2I tone menu transversely to the law; the golden-specific content sits in wy | as row 297 (same carry) | none | none | **DEBT (low)**, with row 297 |
| 304 | B8131: specialist-brief triage — two genuine gates, one struck | no | none | — | CLOSED-NO-LOAD-NO-LEAD |
| 306 | B8133: residue 2 is an evaluation-point gap (Fried at s = 0, the graviton at s = n) | no | none | B1157 (cusped Ruelle/torsion framework, Cappell–Miller) | CLOSED-NO-LOAD-NO-LEAD |
| 307 | B8134: a codex-branch "stale claim", withdrawn by the seat as an interrupted branch | no | none | B1144 | CLOSED-NO-LOAD-NO-LEAD |
| 308 | B8135: Paper I drafted (coker(A²−I) = ℤ/m ⊕ ℤ/m exactly) | no | none | the series' fate is the owner's (RELAY_LEDGER, ESCALATED at B1420) | CLOSED-NO-LOAD-NO-LEAD |
| 309 | B8136: Paper II drafted (finite rung spectrum; C forced) | no | none | as 308 | CLOSED-NO-LOAD-NO-LEAD |
| 310 | B8137: Paper III drafted, with a reproducer | no | none | as 308 | CLOSED-NO-LOAD-NO-LEAD |
| 321 | B8148: "m = 12 settled at 3" | no | none | **REFUTED on main, row 625 (B1416: 3 proper / 2 improper)** | CLOSED-HANDLED |
| 322 | B8149: Paper II's mod-p residue is one-sided; exposure {16, 20, 26, 28, 36} | no | none | paper-internal | CLOSED-NO-LOAD-NO-LEAD |
| 323 | B8150: Paper III's missing continuation fence | no | none | B1157 treats s = 0 directly | CLOSED-NO-LOAD-NO-LEAD |
| 326 | B8153: B500's depth-5 sweep unfinished (9 words never reached); the seat's mod-p obstruction vacuous | no | none | **B1187/ADDENDUM_b8153_nine_words.md** | CLOSED-HANDLED |
| 623 | B8087 (re-read) — already VERIFIED-EARLIER as B1092 | no | none | itself | CLOSED-HANDLED (matched only by the word "SCHEDULED" in its text) |

## 2. cc3 braver-questions branch (5 rows) — `archive/braver-questions@53da05f6`

| row | item | A | B | C | disposition |
|---|---|---|---|---|---|
| 489 | B775: the braver questions (32 agents): an interpretive consciousness bridge, 8 survivors in 4 families, the θ vacancy, a level audit (8.3 % suspect), the V₄-genericity falsifier | no (Gate 5-Q phenomenology) | none for the 19; its "V₄ genericity" falsifier is the family question main later answered by reframing (the object is the family) | CAMPAIGN_STATUS (E51 recovered; the nine relays at the branch root) | CLOSED-NO-LOAD-NO-LEAD (FINDINGS_FINAL read; PARALLEL/THREE_MOVES headline only) |
| 490 | B783: the observer ground-zero | no | none | **harvested as B802** (Review 32, R32-14) | CLOSED-HANDLED |
| 491 | B784: the trace-map intertwining — θ trivial on all SL(2) traces; C an inner automorphism | no | none | the θ-triviality scoping lemma (LAW_MAP row 70); E27 sweep; RELAY_LEDGER (θ-bridge VACUOUS) | CLOSED-HANDLED |
| 492 | B792: the first discrete Maass eigenvalues of m004 by a Hejhal solver, the parent ground state confirmed | no | none for the 19 | **B795** (main's independent re-derivation, 7/7) and B797; CHANGELOG notes a completeness gap (the seat's table may hold more eigenvalues than the 17 main harvested) | CLOSED-HANDLED (the completeness gap is process debt) |
| 493 | tierB_opening: B518 Tier B's mixed-chain gap-opening table tested; the MIXED row refuted for every directive under the pinned convention; under the other, a doubling decoy admits the dyadic gap too | **yes, weakly**: `docs/RETRACTIONS.md` row 13 still says the mixed-chain gap opening "is falsifiable; the discriminating fact was never computed in-sandbox" — the seat computed it on 2026-08-13 and main never received it (no main text names it). `layer0b_all_directives.py` re-run here: rc 0, output byte-identical to the committed `layer0b_output.txt` (the argument is at the gap-labelling level — a missing label already forbids the opening — so it reaches B525's distinction). The same directory also holds the seat's bronze-member checks of 2026-08-13 (a √−7 triple with elliptic generators; the geometric component degree 8, non-arithmetic), read at commit-message level only | none for the 19 | none | **DEBT (low)**: adjudicate the convention, re-word B518 Tier B, date-note RETRACTIONS row 13 |

## 3. consolidation seat qor5up (30 rows) — `archive/qor5up@3851df2a`

All 30 are **CLOSED-HANDLED at B1060's DIGEST_LEDGER** (rows as below; B1173 partial close; residue = L185, parked). This
reader read the mathematics-bearing arcs in full (B1026–B1032, B1038, B1047, B1048, B1050, B1051) and the rest at headline +
the digest's note. Two notes beyond the digest are given after the table.

| row | seat item | digest row (B1060) | grade there | anything beyond the digest |
|---|---|---|---|---|
| 494 | B1025 suite collection repair | 1.02 | ACCEPTED-WEAK | — |
| 495 | B1026 one involution, six names | 1.03 | ACCEPTED-WEAK, flag resolved | — |
| 496 | B1027 κ = 2 is the free chain | 1.04 | ACCEPTED-WEAK | — |
| 497 | B1028 κ absolutely conserved | 1.05 | ACCEPTED-WEAK | — |
| 498 | B1029 the seam's Hilbert class field is the two ends | 1.06 | **ACCEPTED, REBUILT** | — |
| 499 | B1030 one continuous dimensionless input; the two fives | 1.07 | ACCEPTED-WEAK | reconciled by THE_FRAMEWORK's count discipline |
| 500 | B1031 three generations structural, not derived | 1.08 | ACCEPTED-WEAK | — (consistent with B1496) |
| 501 | B1032 the across-breakings route (B885/B889/B890/B891) | 1.09 | ACCEPTED-WEAK | note (a) below |
| 502 | B1033 the second debt register | 1.10 | ACCEPTED-WEAK (scoped after its retraction) | — |
| 503 | B1034 two κ's | 1.11 | ACCEPTED, consumed (TERMINOLOGY; E72) | — |
| 504 | B1035 the shadow library | 1.12 | ACCEPTED-WEAK | L185 row 4.7 |
| 505 | B1036 the knowledge room | 1.13 | ACCEPTED-WEAK | — |
| 506 | B1037 the B100–B199 band | 1.14 | ACCEPTED-WEAK | — |
| 507 | B1038 the SL(n) tower cluster restored (unique fit at n = 4) | 1.15 | ACCEPTED-WEAK | the SL(n) tower, not THE_TOWERS' gauge towers |
| 508 | B1039 the B141 mechanism false | 1.16 | **CORRECTED, REBUILT** | addendum landed 2026-08-13 |
| 509 | B1040 isomonodromy cluster re-tiered | 1.17 | ACCEPTED-WEAK | — |
| 510 | B1041 three red locks | 1.18 | ACCEPTED-WEAK (3 of 10 checks environment-bound) | — |
| 511 | B1042 the error ledger stopped 122 arcs ago | 1.19 | ACCEPTED-WEAK (repaired) | — |
| 512 | B1043 the band is the wrong unit | 1.20 | ACCEPTED-WEAK | — |
| 513 | B1044 the topic search made mechanical | 1.21 | ACCEPTED-WEAK | L185 row 3.1 |
| 514 | B1045 the instrument's first miss | 1.22 | ACCEPTED-WEAK | — |
| 515 | B1046 the arc graph is one-way | 1.23 | ACCEPTED-WEAK | L185 row 3.2 |
| 516 | B1047 the seam cluster from the bodies | 1.24 | ACCEPTED-WEAK | — |
| 517 | B1048 the seam cluster closed; the contraction boundary | 1.25 | **ACCEPTED, REBUILT** | B426 boundary addendum landed (2026-08-14) |
| 518 | B1049 five red locks the targeted tests missed | 1.26 | ACCEPTED-WEAK | — |
| 519 | B1050 the projective quotient is natural and not a selector | 1.27 | ACCEPTED-WEAK | — |
| 520 | B1051 B0–B99 closed; the fixed line is Dickson | 1.28 | ACCEPTED-WEAK | — |
| 521 | B1052 the exit manual | 1.29 | ACCEPTED-WEAK (70/72 re-run) | lane 2 ported |
| 522 | B1053 the unread handoffs | 1.30 | ACCEPTED-WEAK | — |
| 523 | B1054 the seat's Review 1 | 4.8 | ACCEPTED-WEAK (70/72 green; its retraction re-verified) | — |

For every row: A no; B none, except note (a); disposition **CLOSED-HANDLED (B1060 DIGEST_LEDGER row as listed)**.

- **(a) B1032's "route (b)".** The seat points out that four MAIN arcs — B885, B889, and the sealed B890, B891 — show one
  observer registering three pairwise-distinguishable matter sectors (foreign vacuum lines, foreign 16s) on one 27 across the
  three measurement frames, and that B307's no-C₃ theorem does not touch this route. Main's B1496 (three generations,
  researched) did not include this cluster in its topic sweep. But B1496's own specification — the count is an index on
  closed cycles; overlapping, non-summand pieces do not count — likely dissolves it, and the cells' own fence says the same
  ("registerable distinctness is not mechanism-hood"). Listed as a weak lead (§6 L4), not a debt.
- **(b) L185's row 4.5** ("the 15 absent reproducers, 3 under CLAIMS promotions") is the only residue row that could bear on a
  promoted claim. L183 (the reproducer sweep) was executed as **B1177** (21 no-runner arcs recorded, REVIEWS.md l. 4511);
  crossing the seat's 15 against B1177's 21 is a two-list comparison, owed before L185 stays parked (process, not math).

## 4. codex seat (19 rows) — `archive/codex-seat-r001@f7a49536`

Read by the delegated reader: relays and memos in full for R001, R002, R004–R008, R013, R016, R018, R031, R031B–D (with
captured outputs); R022 relay + half the memo; R023 relay (22 asks) + its four certificate outputs (not the WAVE6 memo or its
485-line delta audit); R029, R029A, R031A relay only; the final question map `backbone.json` (201 rows) parsed for OPEN rows
and REFUTED rows naming main arcs. No certificate was run. **This reader's spot-checks:** OA-C1137's text on the tag
(`documents/PROGRAM_QUESTION_ANSWER_MAP.md` l. 220) and B1161's and B298's sentences on main (confirmed as quoted below);
B1195's `verification/batch5a_cells.json` (GC-21, 22, 23, 25 `survives: False`, GC-24 True; no addendum in the arc);
B1416's rows 629–630 and B1232's verdict ("CODEX R031A/R031B VERIFIED ON THIS BENCH"). One correction to this reader's own
brief: RELAY_LEDGER rows 521–523's "OPEN, no main arc" text predates B1416, which closed all three. The seat's subject — the
heterotic height-308 Yukawa evaluator — sits in a frame the record walled (OA-C1002, B1155) and retired (P-235 DECLINED).

| row | item | A | B | C | disposition |
|---|---|---|---|---|---|
| 202 | R001: the seat's self-summary (heterotic bridge, height-308 conditional MSSM witness, up-sector no-go, vacuum no-gos) | no | none current; its vacuum-selection no-gos (OA-C1017/1026/1035/1046/1049/1050/1052) were never on main and their evidence is in a local folder not on the branch — unverified | B1154, B1159, B1162, B1167, B1215 leg 4 | CLOSED-NO-LOAD-NO-LEAD |
| 203 | R002: Campaign II masterplan (gates C0–C7, the proof loop, anti-overclaim rules) | no | none (heterotic flavour fork) | — | CLOSED-NO-LOAD-NO-LEAD |
| 205 | R004: the wave-3 108-question map (superseded by R015) | no | none | its five live rows taken up: OA-C1067 → B1201/B1208; C1069 → B1208; C1074 → B1147 row 38; C1077 → B1153, B1171; C1083 → B1153 row 54 | CLOSED-HANDLED |
| 206 | R005: B1147's lock read an untracked `reproduce.log` | was a lock defect | none | B1147 `ADDENDUM_2026-09-02_B1240.md`; `tests/test_reproduce_runners_live.py`; ERROR_LEDGER E57 | CLOSED-HANDLED |
| 207 | R006: exact E₆/27 invariant census; fixed-linearisation cubic covariance | no | none | B1147 rows 32, 35 (the cloud seat's vendored certificate). Uncarried fence: the covariance scalar is 1 only for the named Ω lift (Ω → λΩ multiplies it by λ³); nothing current rests on it | CLOSED-HANDLED |
| 208 | R007: even labels ⇒ even ω₁ grades (det A = 3) | no | none | B1147 row 34 | CLOSED-HANDLED |
| 209 | R008: tr(ab⁻¹) + κ = x² − 1 on the whole Riley component | no | none | B1153 row 54 | CLOSED-HANDLED |
| 214 | R013: C = e₆^{2T} toral; one A₂ Weyl orbit; 109 flats and 11 centraliser values over ℚ and ℚ̄ (conditional on the principal 2T placement) | no | **LEAD** (folded into §6 L3): the flats are an enhancement-locus lattice of the object's charge torus that THE_TOWERS never used | the algebra is on main in B874's 2026-08-18 addendum (the no-moduli theorem), B892, B950; the 109-flat count itself is not | **LEAD** (pointer on P-415/P-416) |
| 217 | R016: the ζ₃ Habiro tables repaired at finitely many levels | no | none (OA-C1115 open, not current) | B1171 → `B1158/ADDENDUM_fence_note_R016.md` | CLOSED-HANDLED |
| 219 | R018: the wave-5 154-question map, never read on main | **yes**: its OA-C1137 refutes the implication "a degree-two trace field bounds multiplicity by two" (V ⊕ V ⊕ V is defined over the same field). B1161 l. 33 states it ("trace field … degree 2 … ⇒ multiplicities ∈ {1,2}, never 3") and B298's headline is "the degree-2 obstruction" ("a multiplicity of 3 needs a cubic structure"); B298 has no addendum, was outside B1655's negatives audit, and is cited as prior by B1496, `docs/views/CLOSED_DOORS.md`, `docs/GRAND_COMPUTATION_v0.md:150`, `docs/EARLY_RECORD_INDEX.md:612`, HINT_LEDGER H85; it is also in tension with main's own B1606/W20 (an index ±3 with no cubic field) | the rest of the map is consistent with main | none | **DEBT** |
| 223 | R022: the V₄ named-action audit | no | none | B1175, B1182 (C4′ convention fence), B1214/B1215 leg 1 | CLOSED-HANDLED |
| 224 | R023: the wave-6 185-question map, four certificates, 22 asks | **yes, low**: ask 9 never actioned — B1195's cells GC-21, -22, -23, -25 fail their own correctness lens (`survives: False`), yet B1195 stays PROVED with no addendum; GC-22 was promoted to "λ external by theorem" (CHANGELOG ~6298; P3 `main.tex` l. 56, 119); GC-25 is cited as proved by B1205 (FINDINGS l. 37), B1206, GRAND_COMPUTATION_LEDGER (~169–173), `views/CLOSED_DOORS.md:60`, `SM_SPECIFICATION_LEDGER.md:382`. Load low (that ledger retired, P-235/P-148; framing superseded by B1750/P-372) | ask 20 narrows B1208 leg 4's dark-matter-stability sentence to Cartan characters of order 2–6 (belongs with P-145); the seat's `outputs/r023_wave6_outside_hostile.txt` refutes cloud memo 100 (harvest row 349, still SCHEDULED): the opposite Riley sign fails the m004 relator | B1196 (16 is not a sum of the 9-blocks), B1197 (78 closings, 156/156), B1199 (745 classes, LR unique); the 𝒯-evaluator commission (B1185/B1205/B1206/B1212) never delivered, frame retired | **DEBT (low)** |
| 230 | R029: the wave-7 map; OA-C1169 (L173's five-vs-six differential not distinctive) | no | none | Review 53 §8 (corroborates B1095) | CLOSED-HANDLED |
| 231 | R029A: the wave-8 hostile read (B1218 reproduced; h¹ = 3 is V16 + V8 + V0, not three copies; Gate C; the {C, P} fence) | no | none | RELAY_LEDGER row 126; `OPEN_PROBLEMS.md:330`; B1339 l. 28. One stale sentence: `docs/PUBLICATION_CAMPAIGN.md:127` ("the live generation computation", dormant doc) | CLOSED-HANDLED |
| 233 | R031: minimum-support toric trace (4 triangles, 96-simplex product) | no | none (retired frame) | never verified on main | CLOSED-NO-LOAD-NO-LEAD |
| 234 | R031A: B₀ = 4χ₀ (the generator acts by I₄; ℙ³_ℂ) | no | none | **B1232** retraction 3 (certificate re-run) | CLOSED-HANDLED (the row should read VERIFIED) |
| 235 | R031B: the RCFT scope, six points | no | none; its residual OA-C1184 (a finite RCFT receiver for m004) lives only in the B1229 addendum | **B1232** (three points credited); `B1229/ADDENDUM_2026-09-16_fences.md` (Witten 1991, the I-7 fence); B1416 | CLOSED-HANDLED |
| 236 | R031C: the wave-9 map (OA-C1176–C1184) | no | none (OA-C1182, the CS bit as a CP-parity bit, is OPEN_LEADS L192) | **B1416, row 630** | CLOSED-HANDLED |
| 237 | R031D: "identify or descend" — an identification costs the image of its choice space in observables, not one row | no | **LEAD** (§6 L2): main adopted the lemma (B1232, THEOREM_REGISTRY T-COUNT-THE-IMAGE) but never applied it to the input count | B1232; **B1416, row 629** (certificate re-run) | **LEAD** (attach to P-418) |

## 5. Totals

| seat | rows | LEAD | DEBT | CLOSED-HANDLED | CLOSED-NO-LOAD-NO-LEAD |
|---|---|---|---|---|---|
| cc3 paper seat | 42 | 2 (245, 249) | 2 low (297, 299) | 19 | 19 |
| cc3 braver-questions | 5 | 0 | 1 low (493) | 3 | 1 |
| qor5up | 30 | 0 (one weak note, row 501) | 0 | 30 (B1060) | 0 |
| codex | 19 | 2 (214, 237) | 2 (219; 224 low) | 12 | 3 |
| **all** | **96** | **4** | **5** | **64** | **23** |

Read depth, honestly: cc3 — 36 FINDINGS read in full, 6 from `arc_verdict.json`/`results.json`/CAMPAIGN.md, 6 of the 36 at
verdict level; braver — B775's FINAL report, B792's head, tierB_opening's prereg, P0-0 notes and layer-0b in full, B783/B784
at headline plus main's harvest pointers; qor5up — 12 arcs in full, 18 at headline plus B1060's per-row note; codex — as
stated in §4 (delegated, spot-checked). Re-runs on this bench (seat code, scratchpad copies, REPRODUCED grade): B8068 cell 4
(p = 1093) and cell 6 (p = 1231, 1009); tierB_opening layer 0b (byte-identical); B8072 `capacity.py` (all controls pass).

## 6. The strongest leads, ranked

Nothing in the 96 rows is a hidden derivation of an SM parameter. Four items hold ideas main never followed up that bear on
today's open questions; the first two are data-free and cheap, the third is the largest if it holds.

**L1 — a per-target information budget before the level-2 card is sealed (cc3 B8072, row 249).** *The idea:* the seat modelled
a numerical match as Poisson placement — with candidate density ρ per unit ln near a target and measured relative precision δ,
a lucky hit has probability P = 1 − exp(−2ρδ) and a match carries −log₂P bits — and calibrated ρ from the record's own hit
counts (two independent windows agreeing to 1.3×, a third arc held out and predicted). Most of its twelve tested targets came
out in a band where no match, however close, carries information. *First computation:* calibrate ρ from the frame's own output
(B1825's census of about 55 million addresses gives the density of the frame's predictions near each target) and compute, from
each held-out target's measured relative uncertainty only — no central value read — the smallest p_V an exact hit could reach
under GENESIS v1.60 condition 3 (p_V < 0.01/m_V); the same for D at its measured precision. *What it would change:* it says,
before sealing, whether P-585's level-2 confirmation can succeed at all on each candidate target, so held-out numbers are not
spent where even a perfect prediction cannot count; and it gives S291's "would we recognise a correct answer" (FRAMING_LEDGER
§G) a number per target. *Why main has not:* the P3 sweep (`papers/P3_THE_PAPER/sweep_s10/w6.items.json`) graded it SHOULD and
recorded that it was never read into an arc; main's power controls (S284/S285's planted worlds for B1825) are the same idea for
one sealed test, and P-585's row charges theory error (P-575) and searched bits (P-576), but no capacity table for the level-2
targets exists (no "capacity" or "no-information" in B1828/B1829). *Re-run here:* `capacity.py` rc 0, all controls pass.

**L2 — count the image, not the rows: apply "identify or descend" to the input count (codex R031D, row 237).** *The idea:* an
unearned identification is not automatically one free number; its price is the image of its choice space in the invariant
observables — zero if every claimed observable descends through the choice, possibly more than one if it does not. *Where main
stopped:* B1232 re-derived the lemma (THEOREM_REGISTRY T-COUNT-THE-IMAGE) and applied it only to the retired ℙ³ case; no other
arc cites it; IDENTIFICATION_LEDGER has no "descends" status and calls its count "a lower bound" — an inference the lemma shows
can fail in both directions; P-418's scoreboard counts "the unearned identifications, each with its arc, counted apart"; B1809's
f(d) as a Jacobian rank is the discrete-choice half of the same idea, the identification half is missing. *First computation
(no data):* for each choice the candidate machinery uses (c = 3, the 2/5 line class, the end norm, τ, the Higgs direction) and
each unearned identification touching it, test whether the frozen map to the six ratios and D is constant under the choice — a
rank or orbit test with a planted control, as in B1232. P-355's "D = 9 for every Higgs on the d = e points" is already one such
fact. *What it would change:* the honest count of free inputs on the board (the goal restated 2026-10-08: SM structure and how
many free numbers), up or down. *Why main has not:* the lemma arrived in the September consolidation (B1232, B1416) and the
input count was rebuilt later (P-418, B1809) without reading it back.

**L3 — on the object's real data, both routes into E₆'s gauge chain reach SO(10) and skip SU(5); its ω-character data picks
two pure spinors over ℂ (cc3 B8068 cells 3, 4, AXIS0 with B8073, B8071, B8077; codex R013; main's own B874/B892; rows 245,
250, 248, 254, 214).** *The idea, from three sources that share no code:* (a) the adjoint route — main's B892: "the second
measurement skips SU(5) over ℝ" (the 26/A₄ stratum exists only at four non-real points, B874's 2026-08-18 addendum), while the
D₅ stratum 46 is in B874's real ladder; codex R013 gives the full lattice of 109 flats of the charge torus C = e₆^{2T}, i.e. the
enhancement loci (12 generic, 14 = B892's endpoint, 26 SU(5)-type, 46 SO(10)-type, 78). (b) The 27-VEV route — cc3's cell 3:
the object's six rank-1 invariants (2T-invariant idempotents of the 27 and 27̄) give so(10) in pairs (rank 5, chiral) and never
su(5); cell 4: each has zero 16-component, and SO(10) → SU(5) needs a 16. (c) cc3's AXIS0: a line in the 16 built from the 2T
forms of character ω meets the pure-spinor cone in exactly two points, over 𝔽_p exactly when μ = x³ − 12x − 5 splits — two
points over ℚ̄, apparently defined over L = K(√77), each with stabiliser sl(5)⋉Λ² (su(5)); but B8073 finds that su(5) not
τ-stable in the conjugations it swept. Read together: the object's real data fixes the SO(10) node, and SU(5) appears only over
ℂ or through a 16 that breaks Spin(10)'s order-2 central element (matter parity). THE_TOWERS cites none of B874, B892, B1092 or
B8068. *First computation:* (i) data-free and stdlib (R013's certificate already enumerates the flats): the incidence poset of
the 109 flats, which SU(5)-type flats contain an SO(10)-type flat, which are real; (ii) on main's own builders (B1102's vendored
Chevalley e₆, B883's 27, B1092's so(10) spinor build): the three so(10)s and their zero 16-components exactly; the ω-line's
pure-spinor quadric restricted and factored over ℚ(√−3)(θ) (the field of the two points); the joint stabiliser's behaviour
under the E₆(−14) conjugation of B1138's fork. *What it would change:* THE_TOWERS P-415 asks whether the object fixes where and
how the towers meet and calls it a breakthrough only if the object fixes the meeting; this would answer at the representation
level — SO(10) fixed and real, the SU(5) step either object-fixed at two points or absent over ℝ — and give P-414's matter
parity a frame-independent verdict (the twin of B1805's negative in Witten's frame). Main's B1092 ("a condition, not a point")
and THE_LADDER X10 ("unsourced") would be sharpened either way. *Why main has not:* cc3's cells were never relayed,
CLOUD_ALIAS_TABLE lists B8068 "not yet ported", the P3 sweep judged only cell 1; R013 was read for cc3's Paper II, not for the
towers, which were posed two months later. *Caveats:* cc3 re-scoped its own cells twice (cell 2 withdrawn; ITEM1's argument
wrong, conclusion kept by B8073); AXIS0 is mod-p evidence (56 primes; 2 more here), exact factorisation owed; everything rests
on the principal-2T placement (OA-C0006); algebra only, no value. *Re-run here (seat code, REPRODUCED):* cell 4 at p = 1093
(16-components 0, 0, 0 under all three so(10)s); cell 6 at p = 1231 (μ splits: 2 of 1232 points pure, stabiliser (34, 24)) and
p = 1009 (one root: 0).

**L4 — the across-breakings cluster as a generation route (qor5up B1032, row 501; weak).** Main's own sealed B890 and B891 (with
B885, B889) show three pairwise-distinguishable matter sectors on one 27 across the three measurement frames — a route B307's
no-C₃ theorem does not touch, absent from B1496's topic sweep. *First computation:* not distinguishability but an index: are the
three sectors direct summands carrying a closed-cycle index (B1496's E1)? The cells' own fence says they overlap, so the
expected answer is no; listed so the route is closed by a computation rather than by omission. (Its value rises slightly with
D1 below: the degree-2 "obstruction" that was read as forbidding a multiplicity 3 is not a theorem.)

## 7. DEBT candidates

| # | what | where it bites | owed | load |
|---|---|---|---|---|
| D1 | **B298's "degree-2 obstruction" overstated** (codex R018's OA-C1137, row 219) | B298's headline and B1161 l. 33 state "trace field of degree 2 ⇒ multiplicities in {1, 2}, never 3"; false as an implication (V ⊕ V ⊕ V over the same field). The seven computed routes stand. No addendum on B298; outside B1655's negatives audit; cited as prior by B1496, CLOSED_DOORS, GRAND_COMPUTATION_v0:150, EARLY_RECORD_INDEX:612, HINT_LEDGER H85; in tension with B1606/W20's ±3 index | dated addenda on B298 and B1161 scoping the claim to the seven routes; correct the B1496 and CLOSED_DOORS citations (P-589 class) | **moderate** — the highest of these: a closed door on the generation question that rests on a non-theorem |
| D2 | B1195's four cells that fail their own lens (codex R023 ask 9, row 224) | GC-21, -22, -23, -25 `survives: False` in `verification/batch5a_cells.json`, arc still PROVED, no addendum; GC-22 promoted to "λ external by theorem" (P3 `main.tex` l. 56, 119); GC-25 cited as proved by B1205, B1206, GRAND_COMPUTATION_LEDGER, CLOSED_DOORS:60, SM_SPECIFICATION_LEDGER:382 | an addendum on B1195; correct the citations | low (the ledger is retired, P-235/P-148; framing superseded by B1750/P-372) |
| D3 | R48-2 closed by retirement, not computation (cc3 B8124/B8126, rows 297, 299) | LAW_MAP row 478 and THEOREM_REGISTRY T-GOLDEN-MERIDIAN (B1132) state the golden-meridian law without the scope Review 48 registered (the tone third is the identity φ·1/(2φ) = 1/2; the golden content is off-tone); carried R49-5 → R52-5, then "CLOSED BY RETIREMENT"; B1137 cites B1132 | re-run B1132's script, scope the row (P-589 class) | low |
| D4 | B518 Tier B's mixed-chain prediction (braver tierB_opening, row 493) | RETRACTIONS row 13: "the discriminating fact was never computed in-sandbox" — it was (2026-08-13; byte-identical re-run here): the MIXED row fails for every directive under the pinned convention, and under the other a no-Thue–Morse decoy admits the dyadic label too | adjudicate the convention, re-word B518 Tier B, date-note RETRACTIONS row 13 | low |
| D5 | stale SCHEDULED dispositions (process) | 64 of the 96 rows are handled elsewhere (qor5up rows 494–523 at B1060; cc3 rows at B1416 rows 625–628, B1187, B1092/B1093; codex rows 205–209, 214, 217, 223, 230, 231, 234–237 per §4); the slice-D generator (B1306 `gen_rows.py`) matched case-sensitively and needed "codex" beside the id, so it missed B1232's "CODEX R031A", relay-only adoptions and the `qB` aliases; the harvest-debt gate still counts them | one bookkeeping pass re-pointing each row | process |
| D6 | small carries (process) | B792's eigenvalue table vs the 17 main harvested (CHANGELOG: "not investigated"); L185 row 4.5's 15 absent reproducers vs B1177's 21; codex's refutation of cloud memo 100 (row 349, still SCHEDULED: the opposite Riley sign fails the m004 relator) to attach before anyone banks memo 100; B1208 leg 4's dark-matter sentence narrowed to Cartan characters of order 2–6 (with P-145); `docs/PUBLICATION_CAMPAIGN.md:127`'s stale "live generation computation"; R006's Ω-lift fence (λ³) | list comparisons and one-line notes | process |
