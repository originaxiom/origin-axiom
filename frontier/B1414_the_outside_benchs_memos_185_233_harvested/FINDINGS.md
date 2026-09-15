# B1414 — THE OUTSIDE BENCH'S MEMOS 185–233 HARVESTED: its eight load-bearing items recomputed on main (five reproduced, one corrected, two already landed), the three-line class to nine tetrahedra has NINE members not six (three missed by an uncanonized isometry list — E81 minted, B1321 corrected, its FAIL branch unchanged), memo 233's forced escape clause re-derived and its v1 vacuity confirmed, the object's D₄ form re-typed ⁶D₄ over ℚ (B1077's label corrected, B882's conjecture split into its two readings), forty-nine memos rowed

**Date:** 2026-09-16 · **Seat:** cc (main) · **Lane:** HARVEST (MASTERPLAN v3.1 §1a; the consolidation). **Source:** the outside bench (cloud lane) at its frozen tip **8262c6ed**, merged into main 2026-09-15 (`merged/outside-bench@8262c6ed`); memos 185–233 under `outside_bench/memos/` (title-named; `outside_bench/INDEX.md` maps the numbers). **Verdict:** VERIFIED-WITH-CORRECTIONS (five of the bench's eight items reproduced on main's own code; one — the cell-3 base rate — corrected; two already on main; one correction to main's own B1321 found by the same instrument; one label correction to main's B1077). Nothing promotes to `CLAIMS.md`; Gate 5 untouched.

## 0. The rule applied
§1a: the seat speaks first; scripts are run, not read; no grade lower than the seat's without a computation here. The bench's last four memos (230–233) were read in full by main; memos 185–229 were fanned to eight bounded readers (`verification/readers/r0–r7/`, one file per memo, sections HEADLINE / CLAIMS / CERTIFICATE / ON MAIN ALREADY? / NEEDS COMPUTATION HERE / SUPERSESSION / GRADE PROPOSAL), who checked every seal hash, every certificate and output, and grepped main for each claim. Every number graded below was recomputed here; where the bench's own instrument was the right one it was run unmodified (B993's 2T counter, B1323's F9 enumerator, B1321's golden test, B1330's exact index); where it was not, the computation is main's own (`verification/*.py`). Populations: `snappy.OrientableCuspedCensus` here has 212 641 manifolds (203 123 one-cusped), i.e. through ten tetrahedra; the bench's populations are quoted with theirs.

## 1. The eight items, one by one

| # | the bench's item (SEAT_REGISTER row) | on main | computation here | grade |
|---|---|---|---|---|
| 1 | B1084 §3's isolation verdict right, derivation E70-class, B1353 did it first | **already on main** via the merge: `frontier/B1084_g2_cone/FINDINGS.md` ADDENDUM 2026-09-14 + its same-day CORRECTION (B1353 first, fourteen models); B1353 harvested in B1411 | documentary | ALREADY-ON-MAIN |
| 2 | TOE §C row 2's "2" (χ(Fix g) ∈ {0,2}) and B1321's "3" (\|det(A−I)\|) are different quantities; 89.88 % of 4 000 attain 4 | row framed 2026-09-15 (`docs/TOE_REQUIREMENTS_LEDGER.md` §C row 2 + addendum) | **the 89.88 % is an artefact** (§3 below): on canonical triangulations **3 996 of 4 000 = 99.90 %** attain 4, 4 attain nothing; the 0.050 % (m202, s959) stands; m004's multiset {0:2, 4:2} stands | REPRODUCED, one number CORRECTED |
| 3 | WHAT_WOULD_COUNT §4A lacks B1116's caveat | **already on main**: `docs/WHAT_WOULD_COUNT.md` ADDENDUM 2026-09-14 (memo 231 cell 9) | documentary | ALREADY-ON-MAIN |
| 4 | fork F9 FRAGILE at depth 4: m412 keeps the atom and is chiral | B749's addendum 2026-09-14 already on main (`frontier/B749_genesis_forks/FINDINGS.md`) | **B1323's own `u1_substrate_count.py --maxlen 5`, unmodified**: 9 324 + 1 360 = 10 684 words, 1 856 + 400 = 2 256 hyperbolic bundles, 21 + 14 = 35 classes, verdict FRAGILE, keepers `abbC` → m412 and `abAB` → L12n2208 — all as the bench; m412 recomputed on main's code: 2 cusps, vol 5.074708 = 2.5 × vol(m004), H₁ = ℤ/2 ⊕ ℤ², \|Sym\| = 8 with all 8 self-isometries orientation-preserving (chiral), all five shapes roots of x² − x + 1, **0** surjections onto SL(2,3), det multiset {0:4, 4:4}; L12n2208: 4 cusps, vol 6 × vol(m004), \|Sym\| = 48 with 24 reversing (amphichiral) | REPRODUCED |
| 5 | base rates: chirality 0.089 %, 2T door 33.92 % (7 of 1 696 in the ℚ(√−3) family), count-of-three 0.050 % | none | **chirality**: 181 of 203 123 one-cusped census manifolds amphichiral on canonical isometries (`chir_sweep_canon.json`; the uncanonized list gives 132 — the same E81 defect in the other direction); **2T door**: B993's own counter at N = 5 000 (main's code, unmodified): 1 696 of 5 000 = 33.92 %, distribution {0: 3 304, 2: 1 337, 4: 222, 6: 78, 8: 20, 10: 26, 12: 7, 14: 4, 16: 2}, and exactly 7 of the 1 696 lie in B1186's 112-member ℚ(√−3) family: m003, m004, m206, m207, s118, s958, v2873; **count of three**: 2 of 4 000 attain 3 (m202, s959) on canonical isometries, unchanged | REPRODUCED (three numbers), the companion 89.88 % CORRECTED (item 2) |
| 6 | the 185-arc gap: union over all heads 1 428, main 1 243 | none | recomputed today over all remaining heads and every `archive/*`, `merged/*` tag: union **1 453**, main **1 282**, absent **171** — every one accounted for by the harvest rule: 37 SM-seat arcs (own numbering, harvested B1411), 87 cc3 B8xxx (harvested, archived), 30 qor5up B1025–B10xx (the numbering collision, archived), 11 closure-phase-1 duels B493–B503, 5 braver-questions, 1 negatives-hunt. The gap is the rule at work, not unread work. The instrument is on main at `outside_bench/certificates/the_frontier_gap_all_heads.py`; main's standing check stays `scripts/checks/harvest_debt.py` (per-seat backlog) | REPRODUCED and explained |
| 7 | B1330's NOT DONE discharged; rank(H₁/⟨peripheral⟩) = 0 on the four best-case objects ⟹ B1334's S⁰ is a point | s958, t12833 were already computed in B1330's own `ADDENDUM_2026-09-11_all_targets_exact.md` (the bench found its own item stale; its cell ran t12835 alone); rank 0 spot-checked 2026-09-15 (SEAT_REGISTER) | **B1330's own `final_index.py t12835`, unmodified, re-run here**: **16 exact in-domain sectors, (t₀, I) = {(1,0): 4, (2,0): 6, (3,0): 4, (4,0): 2}, 12 at t₀ ≥ 2, NON-ZERO INDEX: 0** — identical to the bench's two runs, line for line (`verification/b1330_final_index_t12835.txt`; both relators evaluate to −I, so the even-power germs only, per B1330's own lesson) | REPRODUCED (t12835 added by addendum to B1330) |
| 8 | B1355's escape clause forced (the ℤ/3 is 2T/Q₈), memo 233 **v2 only**; v1 vacuous (bench error #36) | none (B1355 is the SM seat's arc, harvested B1411) | §4 below: v2 re-derived on main's own code, v1's vacuity confirmed by reading the certificate | REPRODUCED |

## 2. What the readers found in memos 185–229 (the table; the reports are in `verification/readers/`)

| memo | file | reader's grade | reader |
|---|---|---|---|
| 185 | `THE_CYCLOTOMIC_ROUTE_IS_CLOSED` | REPRODUCE-AND-BANK | r0 |
| 186 | `THE_TAILS_OF_A_FAMILY` | REPRODUCE-AND-BANK | r7 |
| 187 | `THE_ERRATUM_LOCALISED` | REPRODUCE-AND-BANK | r1 |
| 188 | `THE_VIEW_FROM_ABOVE` | REGISTER | r2 |
| 189 | `THE_ANTIBODY_RUSTED_TOO` | REPRODUCE-AND-BANK | r4 |
| 190 | `THE_BLOCKER_IS_BROKEN` | REPRODUCE-AND-BANK | r6 |
| 191 | `WHAT_WE_CAN_ANSWER_OURSELVES` | REGISTER | r5 |
| 192 | `THE_TWO_TIER_ONE_SOURCES` | REGISTER | r2 |
| 193 | `THE_GUARD_THAT_CAUSED_THE_DAMAGE` | ALREADY-ON-MAIN | r3 |
| 194 | `THE_BIT_ASKED` | REPRODUCE-AND-BANK | r6 |
| 195 | `THE_COMPLEMENTARITY_JOINED` | SUPERSEDED | r4 |
| 196 | `THE_CHAIN_IS_TWENTY_ONE` | REGISTER (body/pricing already cited on main via memo 215's supersession block); Addendum 1's word-identity finding is REPRODUCE-AND-BANK and NOT yet cited on main | r5 |
| 197 | `THE_CLOSURE_IS_GENERIC` | ALREADY-ON-MAIN | r3 |
| 198 | `THE_GATE_HAS_NO_PRODUCT_ROW` | REGISTER | r4 |
| 199 | `THE_SECTION8_BIT_IS_NOT_THE_MIRROR` | ALREADY-ON-MAIN for the math (B1248, PROVED 2026-09-05, predates B1327's question and this memo); REGISTER the adjudication act itself, which has not been written back into B1327's own file | r5 |
| 200 | `THE_Z2_SLOTS_ARE_FULL` | REGISTER | r1 |
| 201 | `THE_OBJECT_PARTITIONS_ITS_CHARGES` | REPRODUCE-AND-BANK | r7 |
| 202 | `THE_MAGIC_SQUARE_SPLITS_THE_CHARGES` | REGISTER (cells 2/3/4 = B874/B877/B898/W4, already on main per memo's own Addendum 1); REPRODUCE-AND-BANK for cell 1 and the Coxeter-duality framing (genuinely new, not yet on main) | r5 |
| 203 | `THE_LITERATURE_FLOOR` | DISPUTED | r3 |
| 204 | `THE_OBJECT_IS_6D4` | REPRODUCE-AND-BANK | r1 |
| 205 | `L142_THREE_FACTS` | REGISTER | r3 |
| 206 | `WHO_CAN_HEAR_CHIRALITY` | ALREADY-ON-MAIN | r7 |
| 207 | `THE_REGISTER_IS_BEHIND` | ALREADY-ON-MAIN | r3 |
| 208 | `THE_TRIAGE_WAS_ALREADY_DONE` | ALREADY-ON-MAIN | r0 |
| 209 | `THE_SWEEPS_FALSE_POSITIVES` | REGISTER | r7 |
| 210 | `THE_PRINCIPAL_TORSION` | REPRODUCE-AND-BANK | r7 |
| 211 | `THE_STALE_ARTIFACT` | ALREADY-ON-MAIN | r2 |
| 212 | `THE_ARTIFACT_PAIR_SWEEP` | ALREADY-ON-MAIN | r0 |
| 213 | `THE_CUSP_CANNOT_TELL` | REGISTER | r7 |
| 214 | `THE_PERIPHERAL_ROUTE_IS_EXHAUSTED` | REGISTER | r6 |
| 215 | `THE_SEAL_ALREADY_HAPPENED` | ALREADY-ON-MAIN | r5 |
| 216 | `THE_CORRECTIONS_APPLIED` | ALREADY-ON-MAIN | r4 |
| 217 | `THE_GATE_IS_INSTALLED` | ALREADY-ON-MAIN | r5 |
| 218 | `THE_INVARIANTS_ARE_EXACT` | SUPERSEDED | r2 |
| 219 | `PARI_ARRIVES_AND_THE_LITERATURE_WALL` | REGISTER | r3 |
| 220 | `THE_RESIDUAL_IS_DISCHARGED` | REGISTER | r1 |
| 221 | `MUELLER_ANSWERS_MEMO_210` | REPRODUCE-AND-BANK | r2 |
| 222 | `KMRT_ARRIVES` | DISPUTED | r6 |
| 223 | `THE_PRICE_IS_TWELVE` | ALREADY-ON-MAIN | r0 |
| 224 | `THE_FIRST_AXIOM` | REGISTER | r1 |
| 225 | `THE_JORGENSEN_NUMBER` | REPRODUCE-AND-BANK | r6 |
| 226 | `JORGENSEN_IS_IT_RIGHT` | REGISTER | r4 |
| 227 | `THE_CHAIN_RIGHT_NOW` | ALREADY-ON-MAIN | r6 |
| 228 | `DOOR_THREE` | DISPUTED | r0 |
| 229 | `THE_MIRROR_AND_THE_BULK` | DISPUTED | r2 |
| 230 | `THE_TOWER_PAST_TEN` | REGISTER (B1330 addendum: the last target t12835, own re-run) | cc |
| 231 | `REQUIRE_AND_TEST` | REPRODUCE-AND-BANK (cells 1-3, 5, 6 recomputed; cell 3 corrected) | cc |
| 232 | `THE_LIFT_AXIS` | REGISTER (the lift-axis map; its two addenda; the 185-arc gap recomputed as 171 and explained) | cc |
| 233 | `THE_TWO_THREES` | REPRODUCE-AND-BANK (v2 recomputed; v1 vacuity confirmed) | cc |
Dispositions used: **ALREADY-ON-MAIN** (landed via the merge or independently, cited at file:line in the report), **REGISTER** (documentary; a harvest row), **REPRODUCE-AND-BANK** (a computation worth re-running here — §7), **SUPERSEDED** (by a later memo, named), **DISPUTED** (main contradicts it — §5). Two write-back gaps the readers found that are not disputes: memo 196's addendum 1 (the three L173 edge clauses are exact word identities H_L ≡ J·H_R·J, not independent kill conditions) and memo 199 (B1327's question is answered by B1248) — both written back below (§8).

## 3. THE CORRECTION TO MAIN — the three-line class to nine tetrahedra has NINE members, not six (E81)

**The defect.** SnapPy's `M.isomorphisms_to(M)` enumerates the combinatorial automorphisms of the triangulation *as given*; the isometry group is the automorphism group of the *canonical* triangulation (`M.is_isometric_to(M, return_isometries=True)` canonizes; `symmetry_group()` does too). On the census triangulations the two lists differ on **853 of the first 4 000** manifolds (`canon_full.py`, `census_sweep_canon.py`), always by undercount. B1239 (2026-09-02) knew it and avoided it in a docstring (*"isomorphisms_to() is NOT used: it does not canonize (m006: 2 of 4)"*); B1302 saw 6 of 12 on m202 and read the missing six as "cusp-swapping"; **B1321 (2026-09-09) swept 61 911 manifolds with the uncanonized list**; the bench's memo 231 cell 3 swept 4 000 the same way, and its cell 6 scored m412 on 4 of its 8 isometries. The lesson lived in a docstring, not in the ledger. **Minted as E81, the UNCANONIZED-ISOMETRY-LIST class** (`docs/ERROR_LEDGER.md`).

**The recount** (`canon_full.py`, canonical isometries, orientation-preserving cusp-fixing, all 212 641 census manifolds, 93 s): the manifolds with a cusp-fixing rotation of \|det(A − I)\| = 3 are **twenty**, of which **nine** are within nine tetrahedra — B1321's six plus

| new member | tetrahedra | H₁ | \|Sym\| (uncanonized list found) | cusps carrying the 3 |
|---|---|---|---|---|
| **t10829** | 8 | ℤ ⊕ ℤ | 12 (2) | both |
| **t12582** | 8 | ℤ/3 ⊕ ℤ ⊕ ℤ | 6 (1) | both |
| **o9_42897** | 9 | ℤ/3 ⊕ ℤ ⊕ ℤ | 6 (1) | both |

and eleven at ten tetrahedra (o10_106653, o10_118186, o10_135235, o10_137270, o10_137271, o10_143602, o10_146953, o10_150704, o10_150725, o10_150726, o10_150729 — outside B1321's stated population and not golden-tested here).

**B1321's FAIL branch stands.** Its own golden test (`b1321_class_search.py`'s `alexander_two_var` + `golden_test`, executed from the script text; `golden_new_members.py`) on all nine: **0 of 48 primitive specialisations** divisible by t² − 3t + 1 for every member — t10829 is two-generator with a genuine 13-term Δ(t₁, t₂); t12582 and o9_42897 have Δ = 1 by the minors' gcd. So the sentence "none of the six members keeps the golden face" becomes "none of the **nine**": the count is corrected, the conclusion (the count of three costs the face) is unchanged. Addendum on B1321; `docs/OPEN_LEADS.md` L205, `docs/MAIN_GOAL.md`, `docs/THEOREM_LEDGER.md`, `docs/CAMPAIGN_STATUS.md` carry dated notes.

**What is NOT affected** (checked, not assumed): B1295's 87-cover count — canonical enumeration gives 984 isometries (968 uncanonized; one cover undercounted) with the orientation-preserving cusp-fixing multiset **{0: 502, 4: 494} identical** to B1295's, whose own count was made by cell propagation with `isomorphisms_to` only as a cross-check; B1324's 66 of 87 chiral — B1324 used the canonical call, and the two lists agree on chirality for all 87 covers; B1320's cover table — identical counts on every listed cover; m004, m003, m202, s959 — census triangulations already canonical (8, 8, 12, 12), multisets unchanged.

**The bench's cell 3, corrected** (item 2): on canonical isometries the maximal attained value is 4 on **3 996 of 4 000** (99.90 %, not 89.88 %) and 0 on 4 (not 405); the "attains 3" set is unchanged at {m202, s959}; 120 orientation-reversing cusp-fixing rows were rejected (the bench: 113). The bench's reading — m004 fails the count of three while carrying the value almost everyone carries — is *strengthened* by the correction.

## 4. Memo 233 (THE TWO THREES), re-derived; v1's vacuity confirmed

`two_threes_own.py` (main's code, exact): (i) 2T of order 24 in half-unit integer quaternions, Q₈ ◁ 2T of index 3, w = (1+i+j+k)/2 with w ∉ Q₈, w² ∉ Q₈, w³ = −1, and conjugation by w sends i → j → k → i; (ii) Fox calculus on SnapPy's own ⟨a, b | aaabABBAb⟩ (exponent sums (1, 0), so b ↦ t): ∂r/∂a = −t + 3 − t⁻¹, ∂r/∂b = 0, **Δ = t² − 3t + 1**; (iii) H₁(Y₃) = ℤ[t]/(t³ − 1, Δ): relation matrix [[1,1,−3],[−3,1,1],[1,−3,1]], **Smith form [1, 4, 4] ⟹ ℤ/4 ⊕ ℤ/4**; mod 2 the relations collapse to one, H₁/2H₁ = (ℤ/2)², and the deck (the cyclic shift) permutes its three non-zero classes in a **3-cycle**; the trivial deck returns TRIVIAL (V-FIRE); (iv) SnapPy's 3-fold cyclic cover, (1,0)-filled: H₁ = ℤ/4 ⊕ ℤ/4, volume 0 at working precision (the flat Hantzsche–Wendt manifold, B1273). All ten checks PASS (`two_threes_own.out`).

**v1 was vacuous, as the bench's addendum says**: in `the_two_threes.py`, side B is `conj_v(W, n) = modpm(qmul(qmul(W, n), qinv(W)))` — the same conjugation by w as side A, reduced mod ±1 — so its equivariance test compared an object with itself. v2 (`the_two_threes_v2.py`, re-run here, seven controls PASS) derives side B from the Alexander module only, and its V-INDEP control (no quaternion token in side-B code) is the right control for that defect. Bench error #36 is real and correctly filed.

**The consequence stands, at its stated strength**: a ℤ/3 acting on H²(X; ℝ) = ℝ^{b₂} with b₂ = 1 is trivial (GL(1, ℝ) has no element of order 3), so under B1355's sum rule a ℤ/3-symmetric triple of apexes carries equal charges 3q = 0 ⟹ q = 0 ⟹ no inflow; since the ℤ/3 that permutes the triple is the object's own 2T/Q₈ (the deck of Y₃, B1273), the clause "b₂ ≥ 2 with the ℤ/3 moving the harmonic forms" is a **necessary condition on every closing realising THE_ASSEMBLY item 1**, not a design option. Fences kept verbatim: X is not constructed; no b₂ of any 7-manifold is computed; I-26 is UNEARNED; this is not progress toward chirality. (Recorded here and in the harvest row; B1355 lives on the SM seat's branch and is harvested in B1411, which this arc points to.)

## 5. THE DISPUTE, adjudicated — the object's D₄ form is of type ⁶D₄ over ℚ, ³D₄ over ℚ(√77); B1077's label corrected; B882's conjecture has two readings

Four memos (203, 204, 222, 228) and the owner register (R110-2, R130-3) say ⁶D₄; main's B1077 (PROVED) says *"ℚ(√77) can only enter through the twisted ³D₄ form, where the cubic étale algebra is a field"*, and `docs/CAMPAIGN_STATUS.md` repeats "the ³D₄ twist of the split triple by K".

**Computed here** (sympy): K = ℚ[x]/(x³ − 12x − 5) — irreducible over ℚ (no root among ±1, ±5), discriminant **6237 = 3⁴ · 7 · 11**, not a square, **Galois group S₃** (`galois_group`); still irreducible over ℚ(√77), where the discriminant is a square, so there K is a **cyclic** cubic. **The type table** (Knus–Tignol, *Triality and algebraic groups of type ³D₄*, quoted verbatim by memo 204 from the owner-supplied source; the source is not on this bench and was not re-read here — that is stated, not hidden): ¹D₄ ⟺ L ≅ F³, ²D₄ ⟺ L ≅ F × Δ, ³D₄ ⟺ L a **cyclic** cubic field, ⁶D₄ ⟺ L a **non-cyclic** cubic field with Aut_F(L)(F) = 1. This is Tits' classification (the type is the image of Galois in Aut(Dynkin D₄) = S₃), and it is the standard fact. **So the object's twisted form is ⁶D₄ over ℚ and ³D₄ over ℚ(√77).** B1077's sentence conflated "a field" with "a cyclic field"; its intrinsic-split theorem (the bare datum is a split triple) is untouched. **Addendum on B1077** (label corrected, nothing struck).

**B882's conjecture** — *"the arithmetic S₃ IS the geometric S₃"* — is refuted or confirmed depending on what "geometric S₃" means, and the record must say which: (i) **triality automorphisms defined over ℚ** (an outer φ with φ³ inner): by the theorem memo 204 quotes, such a φ exists only in types ¹D₄ and ³D₄, so over ℚ there is none — under this reading the conjecture is **refuted as stated** (the register's R110-2); (ii) **the Galois action realising the full Dynkin symmetry S₃**: that is exactly what type ⁶D₄ *means* — under this reading the conjecture is the typing statement itself, true. Memo 228's "not proved, disproved or made harder" read (ii) through a stale novelty-sweep row; memo 204 read (i). **Addendum on B882** stating both readings; its verdict (the naming theorem M(𝕆, ℂ)) is unchanged. Neither reading yields a value or a physics claim.

## 6. Memos 230–232 (read in full by main)

- **230 THE TOWER PAST TEN** — 18 in-domain sectors on the covers of degrees 11–14, all I = 0; its own §3 caveat is the load-bearing content: *no live positive control in characteristic zero exists anywhere in the record* (B1297's own MB12; B1335's non-zero is over 𝔽_p and its char-0 half is NEGATIVE), so the null is evidence about the instrument, not the tower. Main already holds that position (B1297, B1335, B1413's E66). REGISTERED; a reader's claim that `docs/TOE_REQUIREMENTS_LEDGER.md` cites memo 229 without the caveat is **not confirmed** by grep (no citation of memo 229 or B1333's tower numbers there).
- **231 REQUIRE-AND-TEST** — cells 1–3, 5, 6 recomputed (§1 items 4, 5; §3); cell 1's lemma (a σ*-fixed finite-index class gives an amphichiral cover) and its prediction reproduced on main's code: **all 29 cyclic covers n = 2…30 amphichiral** (volumes n·vol(m004) to 1e−6, H₁ the Lucas–Fibonacci tower, last ℤ/832040 ⊕ ℤ/4160200 ⊕ ℤ), and to degree 7 the 28 covers split cyclic 6/0, irregular 4/18 (amphichiral/chiral), the 18 chiral ones in **9 mirror pairs, 0 unpaired** (`covers_and_m412.py`; canonical and uncanonized lists agree on all 87 covers to degree 10). Cell 4 (rows 3–8 object-free) documentary. The bench's interpretive §4 ("the selecting power sits where the object does not deliver") is a reading, not a result, and is not adopted.
- **232 THE LIFT AXIS** — the ten-route map with obstructions quoted verbatim; its ADDENDUM 1 (a) "WITHDRAWN" was an instrument error (the 7d/G₂ axis was right; two arcs advanced it on a head the bench had not diffed) and (b) §2 named the wrong object (Y₃'s H² is a 3-manifold's; B1355's sum rule runs over a 7-manifold's) — both self-corrections verified by reading and kept. REGISTERED; item 6 above.

## 7. The certificates re-run here (the REPRODUCE-AND-BANK memos)
Run in place under a 900 s alarm from `outside_bench/certificates/`, each committed output compared with `git status` afterwards and then restored (`verification/cert_reruns_summary.txt`):

| certificate (memo) | rc | seconds | committed outputs changed | note |
|---|---|---|---|---|
| `cyclotomic_vs_fk.py` (185) | 0 | 0 | none | C_K is not a q-series for 4₁ — reproduced |
| `park_eq32_localised.py` (187) | 0 | 242 | none | Park's eq. (32) fails at `rec.twist.knot.2.m` = 6₁ — reproduced |
| `zhat_unred_ceff.py` (191) | 0 | 135 | none | c_eff = 1 for Ẑ^unred shape-forced — reproduced |
| `edge_minimum_chain.py` (196) | 0 | 2 | none | the three sealed clauses are word identities — reproduced |
| `charges_and_the_magic_square.py` (202) | 0 | 404 | none | cell 1's semigroup-forcing rule — reproduced |
| `the_object_is_6d4.py` (204) | 0 | 101 | none | CELL 1 = B, 2 = B, 3 = B, controls ALL PASS: K non-cyclic, \|Aut(K/ℚ)\| = 1, type ⁶D₄ — reproduced (§5) |
| `l72_residual_discharged.py` (220) | 0 | 2 | none | reproduced |
| `kmrt_arrives.py` (222), `door_three.py` (228) | 2, 1 | 0, 1 | none | **not reproducible here**: both open the owner-supplied KMRT zip (`OA_UPLOADS`/`KMRT_PDF`), absent on this bench — the reading is the bench's, its typing consequence is verified independently in §5 |
| `cj_table_ingest.py`, `tail_tables.py` (186) | 0, 0 | 0, 1 | none | the exact 5-tails — reproduced |
| `six_planes_77.py` (201) | 0 | 341 | none | the six-plane resolvent, the Klein four-group {ℚ(√−3), ℚ(√77), ℚ(√−231)} — reproduced |
| `l72_phase1.py` (210) | 0 | 2 | none | τ_{E₆}: 87 digits, degree 78, order 6 — reproduced |
| `mueller_answers_memo210.py` (221) | 0 | 1 | none | reproduced; the closed-manifold caveat rides with it |
| `the_two_threes_v2.py` (233) | 1 | 2 | none | six of seven controls PASS; **V-CROSS fails on this bench only on its volume tolerance** (the (1,0)-filled 3-cover's volume prints as 1e−6 at working precision; H₁ = ℤ/4 ⊕ ℤ/4 matches) — main's own check in §4 passes at 1e−4 |
| `require_and_test_cell6.py` (231) | 0 | 1 | none | m412 vs m004 on the four predicates: OUTCOME B, controls ALL PASSED — reproduced (it imports cells 1–3) |
| `the_tower_past_ten.py` (230) | 0 | 3 | none | all in-domain sectors zero, C1–C5 PASS; the bookkeeping differs by one sector (17 in-domain here: degree 12 gives 16 and degree 14 gives 1; ±I discarded 19, identities discarded 10 — the memo: 18, 18, 12), the null unchanged |

The bench's outputs are reproducible on this bench for every certificate that does not need the owner-supplied book; no committed output changed under re-run.

## 8. Write-backs made on main in this arc
- `frontier/B1321_…/ADDENDUM_2026-09-16_nine_members.md`; `docs/ERROR_LEDGER.md` E81; `docs/TOE_REQUIREMENTS_LEDGER.md` (the 89.88 % → 99.90 % note, two of nine); `docs/OPEN_LEADS.md` L205 (nine), L142 (memo 205: three sites, one field — closed on the bench's B/B/B, registered), L71 (memos 213/214: the peripheral route exhausted, the cusp-coker slope forced), L72 (memo 220: the residual discharged via RSW), L173 (memo 196 addendum 1: the three clauses are word identities), L192 (memo 194: the CS-mod-½ bit lies below the commensurability class — m003 and m004 differ); `docs/MAIN_GOAL.md` D3; `docs/THEOREM_LEDGER.md`; `docs/FRESH_EYES_2026-09.md` Q15 (second YES on a three-record carrier, m412); `frontier/B1077_…/ADDENDUM_2026-09-16_6D4.md`; `frontier/B882_…/ADDENDUM_2026-09-16_two_readings.md`; `frontier/B1327_…/ADDENDUM_2026-09-16_memo199.md` (the question answered by B1248); `frontier/B1330_…/ADDENDUM_2026-09-16_t12835.md`; `docs/HARVEST_LEDGER.md` rows 561–609 and the cloud pin (8262c6ed, through memo 233); `docs/SEAT_REGISTER.md` (the row's currency note); `docs/CAMPAIGN_STATUS.md`.
- **Owed, not done here** (named so they are not lost): the exact-arithmetic results confined to `outside_bench/` that deserve their own arcs if the programme wants them on the frontier — memo 185 (C_K is not a q-series for 4₁), 186 (the exact 5-tails of a twist-knot family), 187 (Park's eq. (32) erratum localised to 6₁), 190 (f₀…f₅ of m(5₂) reproduced), 201 (the six-plane resolvent: a Klein four-group {ℚ(√−3), ℚ(√77), ℚ(√−231)}, both distinguished planes generate K), 210 (τ_{E₆}, an 87-digit integer, degree 78, order 6), 221 (Mueller's m(m+1) refinement, closed manifolds only — the caveat rides with it); memo 209's two stale `THE_SPINE.md` rows (B171, B1130 — the latter upgraded by B1133 without a `superseded_by`); memo 219's PARI (not installed on this bench; `docs/TOOLBOX_LIVE.md` unchanged); memo 188's `corpus_census.py` never promoted to `scripts/checks/`.

## 9. What is NOT claimed
No value, no generation count, no physics claim, no promotion. The type table (§5) is cited from the bench's verbatim quote of an owner-supplied source, not re-read here. The eleven ten-tetrahedra members of the three-line class are listed, not golden-tested. The 2T base rate is over the first 5 000 one-cusped census manifolds in census order, as the bench's was. Memo 231's interpretive §4 is not adopted.

## Reproduce
`verification/two_threes_own.py` · `verification/census_sweep_canon.py det 4000` and `chir` · `verification/canon_full.py` · `verification/golden_new_members.py` · `verification/covers_and_m412.py` · B993's `sl23_baserate.py 5000` and B1323's `u1_substrate_count.py --maxlen 5` (summaries in `verification/*_summary.json`) · B1330's `final_index.py t12835` · lock `tests/test_b1414_outside_bench_harvest.py`.
