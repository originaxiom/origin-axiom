<!-- Review 66 (R65-7, P-124): the reliance census, run read-only by main at a157f0f74 and banked as the review's artefact. Its Table A drove the tags placed at Review 66 (THE_WEAVE, LAW_MAP, THEOREM_REGISTRY, ten arcs); its GENESIS rows go through GENESIS v1.51 (P-228); its verifications are queued by consequence (P-229); its ledger-currency rows (Table A2) and the audit lane's unrowed ids are P-230. Spot-checked by main against the cited lines. -->
# Reliance census — seat results relied on by main's surfaces (P-124, Review 66)

Read-only census, 2026-10-21, at main `a157f0f74` with the working tree as found. Statuses come from
`docs/HARVEST_LEDGER.md` as it stood (pins: sm `e1724317`). The rule audited: main does not RELY on a seat result unless
it is VERIFIED on main, or the reliance is tagged "the seat's, unverified". A citation that only attributes (credit,
who named or asked something, Seen-first lists, pointers to open questions, independent agreement with a main result)
is not reliance.

## Header

**Surfaces read: 4 documents and 66 arcs.**
- GENESIS.md: §0–§9 read in full; the version log (§10) skimmed. Its entries restate the body and add no reliance the
  body lacks.
- docs/THE_WEAVE.md: read in full.
- docs/LAW_MAP.md and docs/THEOREM_REGISTRY.md: every line carrying a seat id, found by regex and read in context.
- frontier/B1600–B1684: the 66 arcs whose verdict is PROVED. For each, the `rests_on_seat` and `depends_on` fields and
  every seat-id line of FINDINGS.md, read in context.

**Distinct seat items cited: 185.** These are W, sm:B, R/F01, xB, LP, memo and B8xxx ids. Excluded as not seat items:
- main's own labels: W0, the gate; W5 and W7 in B1601, THE_WEAVE and GENESIS, which are main's WM1 and WM2; W2, W3,
  W4 and W6 in LAW_MAP's B674/B1003/B1043/B1068 cells; THEOREM_REGISTRY's "W5 availability";
- the R1–R11 checklist;
- review items such as R23-4 and R65-3;
- sm:B1599, which appears only as the end of a range.

Every one of the 185 is classified below.
- **Relied upon: 146.** This is 64 VERIFIED (Table B), plus 73 not VERIFIED (Table A), plus 9 in Table A2.
- **Relied upon while not VERIFIED on main: 73** (Table A). Of these 73:
  - 23 carry a tag or disclosure in the citing text at at least one site ("registered", "read on main at headline
    level", "not re-derived", "a hypothesis here", "read, not re-run", a queue slot). These meet P-124's tagging rule
    at that site. W23, W24, W42 and W44 are tagged on LAW_MAP or in B1625 but not on GENESIS or THE_WEAVE.
  - 8 carry only B1652's "[seat]" source tag.
  - 42 are untagged at every site found.
  - 9 are partly verified: the part relied on is not the part checked. These are sm:B1515, sm:B1522, sm:B1527,
    sm:B1544, R41, W51, W53, W62 and W83.
- **Table A2, ledger currency: 9** (memos 13, 14, 15, 24, 25, 28, 29, R032, sm:B1518). The citing text says main
  verified the item, but the ledger records no verification.
- **Attribution only: 39** (Table C).

**Main findings**
1. `rests_on_seat` is unreliable. It is empty or partial on several PROVED arcs that use seat results:
   - B1656, B1653 and B1659 (W59);
   - B1606 (W23, W24 missing; W19–W22 declared);
   - B1625 (W44);
   - B1633 (W42);
   - B1652 (W83, W74, W76, W81, W55, W56 and others missing; W22, W79 and W82 declared).

   The gate `seat-positive-verified` (B1624) reads only this field, so it cannot see any of these.
2. The largest block of untagged reliance is GENESIS §5's table "Where each frame has been run, by object" (lines
   271–274). It states as facts the results of about 15 SM-seat arcs registered only (sm:B1368–B1388, B1501, B1503,
   B1515, B1522, B1523) and two audit-lane items (R40, F01). Only the v1.16 insertions carry the tag "read on main at
   headline level".
3. W23 and W24, the two negatives in the THE_BAR grade "the gauge three is a selection", are tagged unverified on
   LAW_MAP:271. They are untagged on GENESIS FK14 (424), THE_WEAVE (110, 112) and in B1606. They are queued as P-156.
4. W44's c-gauge frame carries the phrase "the 13 unreduced in every frame on record" on all four surfaces and in
   B1625. It is registered only (row 1061) and queued as P-053. It is tagged only inside B1625.
5. The motivating case is closed: W59 is VERIFIED (row 1105, B1684). The state it assumes now rests on W60 and W62,
   which are headline-level, queued as P-222. That use is in the conservative direction: it scopes claims down.

## Table A — relied upon, not VERIFIED on main

Judgement key:
- RELIANCE: used as a premise or a stated fact the text needs.
- LIKELY RELIANCE: supporting, explanatory, corroborating or inventory use.
- "(tagged)": the citing text marks it registered, unverified or not re-derived.

Order: GENESIS, THE_WEAVE, LAW_MAP, THEOREM_REGISTRY, then the arcs. Within each surface, roughly by item.

| seat item | where cited (file:line) | what the citing text uses it for | ledger status (row) | judgement |
|---|---|---|---|---|
| sm:B1380 | GENESIS.md:114 (GM4) | "sm:B1380 derives the puncture from faithful F₂ word data": the basis of "the puncture CONDITIONAL" | REGISTERED (655) | RELIANCE (tagged: "Main has not verified sm:B1380") |
| sm:B1384 | GENESIS.md:177 (X_gen claims) | status cell "DERIVED, at the level of definition (sm:B1384)" | REGISTERED (659); its 13 verifiers did not reproduce as shipped | LIKELY RELIANCE (tautological claim, unverified source) |
| sm:B1384 S0 | GENESIS.md:116 (GM5b) | the identity −I = (L²R⁻¹)² for the signed states | REGISTERED (659) | LIKELY RELIANCE (elementary, true by hand) |
| W30 | GENESIS.md:117 (GM5c v1.30); also 723 (log) | the records' orientation "carries the qutrit flux class" | REGISTERED (946) | LIKELY RELIANCE (convergence claim) |
| W28 | GENESIS.md:117 (GM5c v1.33, FK10 ruling) | "W28's naturality rules the record's flat counts (±3)" | REGISTERED (944) | LIKELY RELIANCE (overlaps verified W22's ±3) |
| W44 (c-gauge frame) | GENESIS.md:117 (v1.36); 711 (log) | "where c is gauge" TM1/TM2 allowed and Sym² T one relation; the basis of "13 unreduced in every frame" | TAKEN, c-gauge computation REGISTERED (1061); P-053 | RELIANCE |
| W24 | GENESIS.md:117 (v1.36) | "In W24's frame only c is flavour and nothing is constrained": part of "every frame on record" | REGISTERED, headline and verdict level (939) | RELIANCE |
| W24 (D4), W23 | GENESIS.md:424 (FK14 v1.28); 727 (log) | the grade's UNEARNED clause (D4: a Lagrangian half, a frame choice) and NEGATIVES (≤ 2 generations in E₈ frames; no six-dimensional object gives three) | REGISTERED (939); REGISTERED headline (937); P-156 | RELIANCE |
| W51 | GENESIS.md:117 (v1.41) | why τ stays open: the joint determinant is flat; the canonical functionals pick ω or the cusp | REGISTERED (1075); partly reproduced by B1684, row not updated | RELIANCE (tagged "registered") |
| W65 | GENESIS.md:420 (FK9 v1.45) | "τ = ω and the cusp (W65, W67)" give no hierarchy: a premise for "selection must be a dynamics" | REGISTERED headline (1125); W67 VERIFIED (1127) | RELIANCE |
| sm:B1385 | GENESIS.md:255, 271, 273 (§5) | "every word state is closed in F-FC (one cusp, b₁ = 1, no free cusp)" | REGISTERED (660) | LIKELY RELIANCE (elementary; main's B1487 has one cusp) |
| sm:B1368 | GENESIS.md:271 (§5 table, m004 F-FC) | m004 and its levels "closed" in F-FC | REGISTERED (645) | RELIANCE |
| sm:B1369 | GENESIS.md:272 (§5 table) | "B1186's 112: 108 closed" | REGISTERED (646) | RELIANCE |
| sm:B1370 | GENESIS.md:272 | "four cusps open on one Fourier coefficient each" | REGISTERED (647) | RELIANCE |
| sm:B1386, sm:B1388 | GENESIS.md:272 | cube~3.24 counts ±2, and the count moves with the cusp cut | REGISTERED (661, 663) | RELIANCE |
| sm:B1515 | GENESIS.md:271 (m004 F-HE) | "at q = 1 both halves on one background, with opposite signs" | PARTLY VERIFIED (690): item 4 only, the indices read | RELIANCE (the part used is the unverified part) |
| sm:B1522 | GENESIS.md:271 (v1.6); 420 (FK9) | the mirror breaks on M₅…M₁₂, up to 0.91 of M₁₂; all 196 firing members fixed | VERIFIED on M₁–M₆ only; M₇–M₁₂ and the 196 REGISTERED (827) | RELIANCE (partial) |
| sm:B1532 | GENESIS.md:271, 272 (v1.16 P5/P6) | no λ = 1 pulled-back member on finite abelian covers of M₂–M₆ carries a count | REGISTERED, sealed (837) | RELIANCE (tagged "read on main at headline level") |
| sm:B1501 | GENESIS.md:271, 272 (F-AP) | which cusps "sm:B1501's cones" complete | NOT RE-RUN TO COMPLETION, own check differs (676) | LIKELY RELIANCE |
| sm:B1503 | GENESIS.md:272 (F-AP) | "a cusp point is chiral only where its locus meets another fixed set" | REGISTERED (678) | RELIANCE |
| sm:B1536 | GENESIS.md:272 (v1.16 P6) | no three on connected covers of degree ≤ 12 of m004 and m003; room reaches two | REGISTERED headline (889) | RELIANCE (tagged) |
| sm:B1544, sm:B1546 | GENESIS.md:272 (v1.16 P6) | no three on N₄₅ at the trivial character | REGISTERED (897; step 2 verified for four covers, B1623); REGISTERED headline (903) | RELIANCE (tagged) |
| sm:B1544, sm:B1545 | GENESIS.md:326 (GAP2) | the seat's floor and ceiling bound every F-HE count by ends: the basis of "no state of X_gen carries three in either frame" | REGISTERED (897, 898): proofs followed on the page | RELIANCE (partly checked: "checked on main on 390 readings") |
| sm:B1523 | GENESIS.md:273 (v1.6); 420 (FK9); 430 | every word state to length 12 carries a projective family; on 262 manifolds no isometry dualises it | REGISTERED, verdict and §0 level (828) | RELIANCE |
| sm:B1534 | GENESIS.md:273 (v1.16 P7) | at most one generation on finite abelian covers of m135 and m136 | REGISTERED headline (887) | RELIANCE (tagged) |
| sm:B1535 (Theorem C) | GENESIS.md:252 (F-HE), 273 | the caps N(5̄′) ≤ n(ν³⊗ρ) and N(10′) ≤ b0 + n(ν⁴) | REGISTERED headline (888) | RELIANCE (tagged at 252 and 273) |
| sm:B1535 (Theorem C) | GENESIS.md:424 (FK14 v1.19, v1.23) | caps the count on both companions, so "no character of order ≤ 8 carries three, or two" (B1493's NEGATIVE); "Theorem C's cap is 2 at order four" | REGISTERED headline (888) | RELIANCE (untagged here) |
| sm:B1547 | GENESIS.md:424 (FK14 v1.19) | N₄₅ "has room 3 and reaches two" | REGISTERED (904–906) | RELIANCE |
| sm:B1529 | GENESIS.md:439 (frontier list, v1.16 P4) | Λ² carries no count near the hyperbolic point; the base condition fails on m135 | REGISTERED (834) | RELIANCE (tagged "read on main at headline level") |
| sm:B1527 (Part A) | GENESIS.md:420 (FK9 v1.16); 439 | no vacuum near the hyperbolic point has a non-zero index on any word state to length 12 | VERIFIED Part H only (832); Part A and Lemma C read | RELIANCE (partial) |
| sm:B1512 (Lemma I) | GENESIS.md:420 (FK9 v1.6) | B1297's P is the swap's class in Ballas' presentation (with sm:B1521 C1, verified) | REGISTERED (687) | LIKELY RELIANCE |
| sm:B1528 | GENESIS.md:423 (FK12 v1.10) | "Exact, from sm:B1528 (its own code)": P*V ≅ V* ⊗ (t ↦ λ²) | ADOPTED, "consistent with B1465" (833); not VERIFIED | RELIANCE |
| sm:B1533 (C3–C6) | GENESIS.md:382 (GAP6 v1.16) | the seat's M₄ at ν = (1/3, 0) reads +1, −1, 0 | SUPERSEDED-BY-SEAT (886) | LIKELY RELIANCE (main's B1466 and B1486 carry the claim) |
| sm:B1392 | GENESIS.md:323 (GAP2) | "sm:B1392 places the count at the ends" | REGISTERED (667) | LIKELY RELIANCE |
| R40 | GENESIS.md:274 (§5, m010 F-HE); 343 (GAP3) | m010: I(W) = I(Λ²W) = +1, an anomaly-free 10 + 5̄ | REGISTERED (711, 712) | RELIANCE |
| F01 | GENESIS.md:274; 331 (GAP3) | "on a block with no harmonic background"; chirality needs a source | REGISTERED headline (1048) | RELIANCE at 274; LIKELY at 331 (Corlette–Donaldson carries it) |
| R41 | GENESIS.md:331–336 (GAP3) | the source balance and flux through an end | PARTLY VERIFIED (741, 742): flag-pairing table re-derived | RELIANCE (tagged "read on main and not re-derived except where said") |
| R76 | GENESIS.md:336 (GAP3) | "the source may be supported in the compact core" | REGISTERED (745–747, 803) | RELIANCE (tagged) |
| R80 | GENESIS.md:336 (GAP3) | the balance paid by flux through an end | REGISTERED (804, 838) | RELIANCE (tagged) |
| R77 | GENESIS.md:338, 342 (GAP3) | an added source holds the configuration at the price of infinitely many flat directions | REGISTERED (801, 802) | RELIANCE (tagged) |
| R19, R24 | GENESIS.md:344 (GAP3) | "a conditional three on a two-ended exterior with sources between its ends" | REGISTERED with a main computation beside it (71); RUN, REGISTERED (539) | LIKELY RELIANCE (inventory, fenced) |
| R69 (audit lane) | GENESIS.md:345 (GAP3) | −3 on levels three and six for an induced rank-six coefficient | no audit-lane row (row 198 is the fc seat's R69) | LIKELY RELIANCE (inventory, fenced) |
| memo 122 | GENESIS.md:460 (frontier list) | "NEGATIVE for the root's forced gauge 2-torsion only" | SCHEDULED, "no main text names it" (371): stale | LIKELY RELIANCE |
| W23, W24 | THE_WEAVE.md:110, 112 (the B1606 grade) | the UNEARNED and NEGATIVES clauses of "the gauge three is a selection" | REGISTERED (937, 939); P-156 | RELIANCE |
| W30 | THE_WEAVE.md:149–150 | "the bit the seat's W30 finds carrying the qutrit flux class" | REGISTERED (946) | LIKELY RELIANCE |
| W44 | THE_WEAVE.md:262 | where c is gauge, TM1/TM2 return; one Sym² relation; leads to "13 unreduced in every frame" | c-gauge REGISTERED (1061) | RELIANCE |
| W24 | THE_WEAVE.md:263 | "In W24's frame nothing is constrained" | REGISTERED (939) | RELIANCE |
| W42 | THE_WEAVE.md:309 | "a thread's own H¹ reads the rule's word and breaks the parity grading" | READ in full, thread-H¹ census registered (1058) | RELIANCE (named in P-124) |
| W51 | THE_WEAVE.md:325 | "nothing forces τ (the seat's W51: the joint determinant is flat)" | REGISTERED (1075) | LIKELY RELIANCE (the flatness is Jacobi's identity) |
| W52 | THE_WEAVE.md:336 | "W52 counts 11 of the 13 at the geometry's weight" | REGISTERED (1081) | RELIANCE (tagged "registered") |
| W54, W53 (the 163) | THE_WEAVE.md:464–468 | "the union of their minima is the record's best"; "W54's sentence and W53's 163 stand" | REGISTERED headline (1091); W53 (1084): only the (3,3,3) exclusion verified | LIKELY RELIANCE (minor) |
| W83 | THE_WEAVE.md:524 | F3: "Y survives only if the family index is not the weave's three" | REGISTERED, not recomputed (1166); kernel 0 hand-checked in B1652 | RELIANCE |
| W60, W62 | THE_WEAVE.md:702, 704 | "a state the potential does not select" (scopes B1653, B1656, B1660, B1673) | REGISTERED headline (1109); PARTIAL on main (1115); P-222 | LIKELY RELIANCE (conservative; queued) |
| R76 | LAW_MAP.md:254 | the minima of the action are the reductive points (B1455's fence) | REGISTERED, "leaned on by B1455 as a hypothesis" (745) | RELIANCE (tagged "not re-derived") |
| W24 (D4), W23 | LAW_MAP.md:271 | the unearned clause; status cell "W23 and W24 registered, not verified on main" | REGISTERED (939, 937) | RELIANCE (tagged) |
| W44 | LAW_MAP.md:276 | "and in every frame on record (the SM seat's W44)" | c-gauge REGISTERED (1061) | RELIANCE |
| W42 | LAW_MAP.md:278 | the democratic matrix is "the zero-mode projector of LR's mapping torus, W42" | READ (1058) | LIKELY RELIANCE (named in P-124) |
| W54 | LAW_MAP.md:289 | "W54's sentence stands" (after main's refutation was withdrawn) | REGISTERED headline (1091) | LIKELY RELIANCE (minor) |
| W44, W43 | THEOREM_REGISTRY.md:320 (T-WEAVE-REDUCES-NONE) | "(iii) … in every frame on record (W44)"; "where c is gauge … (W43, W44)" | c-gauge REGISTERED (1061); W43 TAKEN, checked on stored fits (1059) | RELIANCE (W44's c-gauge part) |
| sm:B1545 | THEOREM_REGISTRY.md:315 (T-THREE-NEEDS-ENDS, B1487) | the seat's floor, "a hypothesis here, checked on 390 readings" | REGISTERED (898) | RELIANCE (tagged; B1487 "conditional on the seat's floor") |
| B8129, B8130 (cc3) | THEOREM_REGISTRY.md:258 (T-LANE-C, B1142) | "Graviton bridge DEAD (cc3 B8129/B8130)" | REGISTERED-EARLIER (302, 303) | LIKELY RELIANCE |
| B8078 (cc3) | THEOREM_REGISTRY.md:256 (T-64-ORGANIZED, B1140) | "cc3's 2nd grounding: 14 = B8078 rung → 64 forced" | REGISTERED-EARLIER (255) | LIKELY RELIANCE (supplementary grounding) |
| W23, W24 | frontier/B1606/FINDINGS.md:43, 47 | the grade's UNEARNED and NEGATIVES clauses; `rests_on_seat` omits them | REGISTERED (937, 939) | RELIANCE (disclosed afterwards by B1655's audit banner) |
| W44 (c-gauge) | frontier/B1625/FINDINGS.md:24, 35 | "the 13 unreduced in every frame on record" | c-gauge REGISTERED (1061) | RELIANCE (tagged: "read, not re-run on main") |
| W42 | frontier/B1625/FINDINGS.md:30 | a thread's H¹ breaks the grading democratically | READ (1058) | LIKELY RELIANCE (tagged as read) |
| W42 | frontier/B1633/FINDINGS.md:24 | "One thread reads the rule's word … (by the seat's W42)": the premise of "only through a choice of thread" | READ (1058) | LIKELY RELIANCE |
| W38, W40, W42, W44 | frontier/B1631/FINDINGS.md:29 | the "independent re-derivation" leg of the negatives audit for B1615–B1617 and B1620 | READ (1049, 1051, 1058); TAKEN (1061) | LIKELY RELIANCE |
| W38 | frontier/B1621/FINDINGS.md:23 | "LR carries the character c = 1 (the SM seat's W38)", explaining the equal masses | READ, not re-run (1049) | LIKELY RELIANCE |
| W30 | frontier/B1609/FINDINGS.md:41–42 | "three computations meet at GM5c" | REGISTERED (946) | LIKELY RELIANCE (not a premise of the verdict) |
| W62 | frontier/B1637/FINDINGS.md:62 | "in the fibre frame τ runs there (W62). Neither selects a τ" | REGISTERED headline, PARTIAL (1115) | LIKELY RELIANCE (aside) |
| W61 | frontier/B1643/FINDINGS.md:42, 76 | one of "three independent routes" for C6 | REGISTERED headline (1110) | LIKELY RELIANCE (corroboration) |
| W57 | frontier/B1643/FINDINGS.md:41, 95 | "the seed supplies the first step of hierarchy" in the census of contacts | REGISTERED headline (1099) | LIKELY RELIANCE (tagged "Registered") |
| W70 (script) | frontier/B1650/FINDINGS.md:59 | the condensate's E₈ claims "reproduced with the SM seat's W70 script" | REGISTERED (1131) | LIKELY RELIANCE (tagged: "An independent derivation … is owed") |
| W74, W76 | frontier/B1652/FINDINGS.md:83, 89 | F2 D7 FAILS: CP-invariant; mirror-symmetric threads carry bit 0 | REGISTERED (1147, 1149) | RELIANCE (cell tagged "[seat]") |
| W83 | frontier/B1652/FINDINGS.md:29, 90–98, 174 | F3's D3/D4 dichotomy; the parent's clause | REGISTERED (1166) | RELIANCE (partly hand-checked: kernel 0) |
| W81 | frontier/B1652/FINDINGS.md:80, 84 | F3 D5 FAILS; D8's "no free size" scoped | REGISTERED, not recomputed (1157) | RELIANCE (cell tagged "[seat]") |
| W55, W56 | frontier/B1652/FINDINGS.md:123–124, 181 | F4's D4 "fails on the data"; clause 7 (an E₆ cubic alone cannot split d from e) | REGISTERED headline (1093); W56 identity QUEUED, P-089 (1097) | LIKELY RELIANCE (F4 also falls on W22 and B1440) |
| W23 | frontier/B1652/FINDINGS.md:78, 117 | F3 D2 "three need rank six"; F4's D2 failure | REGISTERED headline (937) | LIKELY RELIANCE |
| W47, W48 | frontier/B1652/FINDINGS.md:78 | F2 D2: nothing supplies the unit; a c = 24 source would | REGISTERED (1068, 1070) | LIKELY RELIANCE (cell OPEN or CONDITIONAL, tagged "[seat]") |
| W65, W72, W73 | frontier/B1652/FINDINGS.md:77, 80–82 | D1 covariance and no hierarchy at ω or the cusp; F2's D1, D5, D6 cells | REGISTERED (1125, 1134, 1146) | LIKELY RELIANCE (tagged "[seat]") |
| W27, W70, W75 | frontier/B1652/FINDINGS.md:79, 84, 135 | D3 imported (W27 T1); F3's unalike Y; D8's scale | REGISTERED (943, 1131, 1148) | LIKELY RELIANCE |
| W80, W84 | frontier/B1652/FINDINGS.md:29, 77, 81, 110 | confirm B1637's artifacts; reproduce chat1's thread frame | REGISTERED (1165, 1167) | LIKELY RELIANCE (corroboration) |
| sm:B1270 | frontier/B1652/FINDINGS.md:121, 126 | the same holonomy type, net 27-count 0; the same commutant | SCHEDULED (126) | LIKELY RELIANCE (corroboration) |

## Table A2 — ledger currency: the citing text says main verified, the ledger does not record it

| seat item | where | what the text claims | ledger |
|---|---|---|---|
| memos 13, 14, 15, 24 (hostile-review seat) | THEOREM_REGISTRY.md:251–255 (B1138, B1139) | "verified two-bench", "re-derived in-lock with own … linear algebra" | SCHEDULED, "no main text names it" (342–347) |
| memos 25, 28, 29 | THEOREM_REGISTRY.md:257, 259, 260 (B1141, B1143, B1145) | "verified two-bench", "hostile-verified", "verified three independent ways" | no row |
| R032 (codex) | THEOREM_REGISTRY.md:288 (B1232) | "re-run and re-derived here" | no row (R031A/B also unrowed) |
| W50 §3 | THE_WEAVE.md:333; GENESIS.md:117 | "by main's own route the SM seat's W50 §3 holds" (B1635) | row 1073 still says §3 REGISTERED, not recomputed |
| W51 | GENESIS.md:117; THE_WEAVE.md:325 | (registered) | row 1075 REGISTERED; B1684 reproduced the parity product 4 and log(y∣η∣⁴)'s critical points (i a saddle, ω): partly verified, not noted |
| sm:B1518 | GENESIS.md:273 | "no criterion in the fibre torsion and the sign decides", "re-derived on main … B1458" | row 823 REGISTERED, "not verified on main" |
| W45, W46 | GENESIS.md:422 (FK11 cell) | the cell still says "registered, not re-run on main" | both since verified (rows 1063, 1064 later notes; B1634, B1641): the GENESIS text is stale |
| B8135, memo 122 | GENESIS.md:236, 460 | named on GENESIS | rows 308, 371 say "no main text names it" |

Audit-lane ids R57, R69, R89 and R92, as GENESIS uses them ("R-numbers and F01 are the audit lane's"), have no row by
id. Rows 189 and 198 are the retired fc seat's same-numbered items, a collision the ledger does not mark. B1457's relay
says main re-derived "R57's quotient".

## Table B — relied upon, VERIFIED (brief)

| seat item | where (examples) | ledger row |
|---|---|---|
| W1–W4 | THE_WEAVE 40–83; GENESIS 424; LAW_MAP 269; THEOREM_REGISTRY 318; B1600, B1601, B1604, B1662 | 911 |
| W6 (four cells; ±LR exclusivity by B1605) | THE_WEAVE 91; GENESIS 424 | 913 (922 REGISTERED for the rest) |
| W9 (in part), W10 | THEOREM_REGISTRY 320 ("W10's V"); B1600 | 919, 920 |
| W19 (in part) | GENESIS 421, 424; B1606, B1624 | 932 |
| W20, W21, W22 | THE_WEAVE 99–105; LAW_MAP 271; THEOREM_REGISTRY 322; GENESIS 117, 424 | 933, 935, 936/940 |
| W26 | GENESIS 117; THE_WEAVE 126 | 942 |
| W34, W101, W107, W108, W109, W110 | THE_WEAVE 634–684; THEOREM_REGISTRY 338–345; GENESIS 111; B1671, B1674–B1683 | 1267, 1263, 1271, 1275, 1276, 1278 |
| W39 (tensors computed by main), W43 (checked on stored fits) | GENESIS 117; THE_WEAVE 233; B1620, B1625 | 1050, 1059 (TAKEN) |
| W41 (the multiplier) | GENESIS 421; THE_WEAVE 299–305 | 1052 (S115 note, B1634) |
| W45 (core χ_{3/2} = 0), W46 | GENESIS 421–422; THE_WEAVE 267, 283, 295, 369, 377; LAW_MAP 283; THEOREM_REGISTRY 321; B1627, B1631, B1640, B1641 | 1063, 1064 (later notes) |
| W50 | GENESIS 117; THE_WEAVE 318; LAW_MAP 279; THEOREM_REGISTRY 347; B1634 | 1073 |
| W53 ((3,3,3) excluded on all 13) | THE_WEAVE 458; LAW_MAP 289; B1637 | 1084 (S123 grading) |
| W59 | THE_WEAVE 548, 697; LAW_MAP 294; THEOREM_REGISTRY 331; B1653, B1656–B1659, B1684 | 1105 (B1684) |
| W67 | GENESIS 420 | 1127 |
| W79, W82 | THE_WEAVE 466; LAW_MAP 289; B1652 | 1156, 1158 |
| W87, W88, W89, W90 | THE_WEAVE 574; LAW_MAP 295; THEOREM_REGISTRY 332; B1656–B1659 | 1190, 1191, 1192, 1206 |
| sm:B1516, B1517, B1519, B1526 | GENESIS §2–§4 (C1–C10, K1–K7) | 695, 822, 824, 831 |
| sm:B1509, B1374, B1375, B1390, B1530 (B1485), B1541, B1521 C1 | GENESIS §3, §5, FK9 | 684, 639, 640, 665, 835, 894, 826 |
| sm:B1283, B1304, B1279, B1355, B1365 (geometry), B1378 (already on main) | GENESIS 446/454, 271; THEOREM_REGISTRY 294, 299 | 28/29, 78/83, 135, 535, 619, 653 |
| R78 | GENESIS 145–153 | 795 |
| R72, R70 (fc) | THEOREM_REGISTRY 295 | 1, 2, 24, 7 |
| B8100, B8112, B8113, B8128, B8147, B8154 (cc3); R017 (codex); memo 80; memo 170 §3; memos 11, 27 (VERIFIED-DIFFERS) | THEOREM_REGISTRY 225, 246, 250, 265, 267, 284; LAW_MAP 326 | 274, 285, 286, 301, 320, 327, 218, 469, 40, 34 |
| xB031 | B1647 | 870 |

## Table C — attribution only (brief, grouped)

- **Credit, naming and Seen-first lists.** W25, W29, W31, W32, W33, W49, W63, W64, W71, W85, W86, W93, W94, W100;
  W27 on GENESIS 117 (it defines the tagged postulate Λ); W47 on GENESIS 421 ("W47's territory"); W56 in B1641 and on
  THE_WEAVE 391 (who owns the question); W59 on THE_WEAVE 404 (a candidate listed).
- **Location of frames and ranges.** sm:B1350–B1399, B1500, B1505, B1509–B1515 and R40–R76 on GENESIS 59 and
  249–253.
- **Pointers to settle open forks.** sm:B1382, B1383 (FK2); sm:B1506 (FK7); sm:B1508 and R57 (FK8); LP01 (FK14);
  sm:B1535 Corollary C3 and B1536 (GENESIS 444).
- **Conventions adopted as method, not results.** sm:B1384 as the X_gen definition and the moves table (GENESIS 124,
  156, 497); sm:B1518 and B1524 as THE_BAR and its null contract (GENESIS 348–349, 420). sm:B1518's census claim
  (GENESIS 273) is counted in Table A2.
- **Critique that only keeps a weaker status.** R57 on GENESIS 107, 114, 116, 118, 194, 419, 484 and 518–520 (a
  quotation, a convention, the rejection of sm:B1380 §3); sm:B1521 C2–C3 (FK12, B130 left open); W60 and W62 in B1684
  (disclosed headline-level, conservative).
- **Prompts and motivation.** R89 (GAP6 narrowed); R92 (LAW_MAP 258); R58-6 (LAW_MAP 255); R51 (LAW_MAP 326, who
  caught it); R48-F1 (THEOREM_REGISTRY 176, 182); B8111 (B1106's instrument control, LAW_MAP 434).
- **Independent agreement with a main result.**
  - sm:B1520 (B1455; GENESIS 271, 420; LAW_MAP 254); W42 as "verified by the SM seat" (LAW_MAP 276–277;
    THEOREM_REGISTRY 320); W52's sum rule (THEOREM_REGISTRY 349; THE_WEAVE 340); W78 (supports a withdrawal, W79
    verified).
  - W72 explained by main (LAW_MAP 292; THE_WEAVE 505, withdrawn); W71 (FK15's agreeing passages); W24's E₈ embedding
    naming B1620's frame (corrected by B1625).
- **Provenance, reporting another seat's own grade.** B8135 (GENESIS 236); sm:B1537 (P1, the GAP heading); sm:B1525,
  B1531 and B1533 in the version log.
- **Version-log history (GENESIS §10).** Restates the body; no separate reliance counted.

## Final list — PROVED arcs (B1600–B1684) that rest on an unverified seat item

Sure (the item is a premise of a stated result or grade):
1. **B1606** (three on the weave graded): W23 and W24 carry the grade's NEGATIVES and UNEARNED clauses. Disclosed
   afterwards by B1655 ("STANDS ONLY AS SCOPED"); queued as P-156. `rests_on_seat` lists only W19–W22.
2. **B1625** (the seat's corrections to B1620): W44's c-gauge frame carries "the 13 unreduced in every frame on record".
   Disclosed as "read, not re-run"; queued as P-053. `rests_on_seat` is empty.
3. **B1652** (the frame tribunal):
   - FAILS cells: W74 and W76 (F2 D7), W81 (F3 D5), W83 (F3's dichotomy, partly hand-checked).
   - Context cells: W55, W56, W23, W47, W48, W65, W72, W73, W27, W70, W75, W80, W84 and sm:B1270.
   - The cells are tagged "[seat]", but `rests_on_seat` lists only W22, W79 and W82. B1655 notes that outcome 2 needs
     no FAILS cell, so the verdict survives without them.

Likely (supporting, explanatory or corroborating use):
4. **B1633**: W42 (a single thread's H¹ breaks the grading; P-124 names W42).
5. **B1631**: W38, W40, W42 and W44 serve as the independent re-derivation of B1615–B1617 and B1620 in its negatives
   audit.
6. **B1650**: the W70 script reproduces the condensate's E₈ claims; the arc says an independent derivation is owed.
7. **B1621**: W38 (c(LR) = 1).
8. **B1609**: W30 (the GM5c convergence sentence).
9. **B1643**: W61 (corroborating route) and W57 (tagged "Registered").
10. **B1637**: W62 (an aside on where τ runs).

Resolved since: B1653, B1656, B1657, B1658 and B1659 rested on W59's lines, VERIFIED today (B1684). Their "state" is
scoped by P-214, and W60/W62 are queued as P-222.

Outside the B1600–B1684 window, seen through the surfaces:
- B1487 (T-THREE-NEEDS-ENDS): conditional on sm:B1545's floor (tagged).
- B1493 (GENESIS FK14 v1.19): its NEGATIVE uses sm:B1535's Theorem C, registered only.
- B1455: rests on R76 as a hypothesis (tagged on LAW_MAP).
- B1138, B1139, B1141, B1143, B1145: rest on hostile-review memos that the ledger does not record as verified (Table A2).
