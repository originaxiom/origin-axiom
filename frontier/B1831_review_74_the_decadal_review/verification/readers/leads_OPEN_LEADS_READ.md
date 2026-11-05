# Review 74 — the open leads of docs/OPEN_LEADS.md, read one by one (2026-11-04)

*Report only: no tracked file edited, nothing committed, nothing banked. Main verifies every pointer. FIREWALL kept: no
value, sign or bound for y_b/y_t, θ̄ or y_τ/y_b is written anywhere in this report; where such computations exist only
their location is named. Nothing is compared with measured data.*

**Scope.** `lead_debt.py` counts 80 open leads; L252–L254 (handled by main today) are skipped, so 77 are read here (L251
is already marked DISCHARGED). Each lead's entry gives the idea, its status now with pointers, its potential against the
current open questions, its first computation and cost, and a disposition. The entries are in four parts, appended
below: A (L144–L166), B (L174–L200) and C (L201–L223) by three readers, and D (L229–L250) by the merging reader.

**Method.** For each lead:
- its text and dated notes;
- its 2026-10-23 report from the parked-items sweep (audit/drafts/leads_reeval/, merged in QUEUE.md). That sweep re-read
  every one of these leads, but its verdicts are a reader's, not banked;
- the register rows the sweep made (P-309, P-313 and their children P-311 to P-336, and later rows);
- every arc since, searched by L-number and by key terms.

**Caveat.** audit/review74/leads/_xref_index.txt's frontier column is unreliable on this machine: BSD grep returned
nothing for some leads, so readers A and C ran their own scans. Its register, LAW_MAP and CAMPAIGN_STATUS columns are
sound. The folder audit/review74/leads/parts/ belongs to a different Review 74 reader (the register's LEAD rows) and is
not part of this report.

## The answer first

- **Two of the 77 leads have HIGH potential.**
  - L241, the measurer: its "reading" is now the hinge of the quark-mixing wall.
  - L151, the anchor budget: a data-free rule that could turn Re τ into a CP bit.
  - **Neither is a stored lead any more.** Each already has a register row: L241 in P-295, P-566 and P-583; L151 in
    P-328. Neither row has been worked on main: P-328's rule is unverified since 2026-10-28, and P-583 is an untouched
    data-free cell.
- **Seventeen are MEDIUM and 58 LOW.**
- **73 of the 77 can leave the lead list:**
  - 41 are answered, superseded or retired, with pointers;
  - 32 are already carried in full by register rows.
- **Four stay open as leads:** L241 and L244 (both standing at the owner's word), L250 (as P-403 and P-458) and L195
  (the hatch index).
- **The dominant failure is the one named today, L251/B1800.** At least 21 leads were finished, or answered by the
  2026-10-23 sweep, and their headings were never marked, so the gate still counts them as open.
- **The sweep's own answers were mostly never written into the record:** P-334 and P-318 are still QUEUED, and none of
  B1400, B1401, B1406, B1408 or B1424 has received a dated note since.
- **Nine reader findings have no row at all**, and two are load-bearing:
  - W134's threshold against C8's whole unit (L222): the record's derived three may conflict with the E₈ family frame,
    while P-302 is closed DONE with that piece unverified.
  - The count of prior looks at θ̄ (L192): it may be undercounted against P-585's held-out-target rule.

## Totals

| | HIGH | MEDIUM | LOW | total |
|---|---|---|---|---|
| A (L144–L166) | 1 | 1 | 15 | 17 |
| B (L174–L200) | 0 | 5 | 16 | 21 |
| C (L201–L223) | 0 | 6 | 13 | 19 |
| D (L229–L250) | 1 | 5 | 14 | 20 |
| **all** | **2** | **17** | **58** | **77** |

| disposition | count | leads |
|---|---|---|
| STILL OPEN | 4 | L195, L241, L244, L250 |
| DISCHARGED / SUPERSEDED / RETIRED (close with pointer) | 41 | see the close list |
| MERGE into a register row (close as carried) | 32 | see the close list |

## One line per lead

| lead | potential | disposition | key pointer |
|---|---|---|---|
| L144 | LOW | DISCHARGED | B1096; body CLOSED since R57-3 (OPEN_LEADS.md:1083); banner into P-318, scope into P-138 |
| L145 | LOW | MERGE | L195 / P-322 (the revival view); L145a write-down into P-334 |
| L146 | LOW | DISCHARGED | B1600, B1601 (2T on every odd-trace thread); B1629, B1733; selection in P-139 |
| L147 | LOW | SUPERSEDED | B1006, B1021 nulls stand; the frame moved (B1656); retire the 50-digit run |
| L148 | LOW | MERGE | P-322 (query.py card ignores its argument, scripts/atlas/query.py:194), P-291 |
| L149 | LOW | DISCHARGED | B1019; m = 4 door correction on P-318 (GENESIS.md:262, LAW_MAP.md:236 unamended) |
| L151 | **HIGH** | MERGE into P-328 (escalate) | the CP-line J rule, unverified on main; MAINS_PLAN.md:81 "Re τ … no rule" |
| L152 | LOW | MERGE | P-291 (relay-content check) |
| L154 | LOW | MERGE | P-137, P-138, P-318 (B1228's σ = 1); B1034, B1064, B1722 |
| L157 | LOW | DISCHARGED | B1039, B1042, B1043, B1609 |
| L158 | LOW | DISCHARGED | B1040, B1041; TERMINOLOGY note into P-334 |
| L159 | LOW | DISCHARGED (after the Deligne–Milne gate is read) | B1248, B125 |
| L161 | LOW | MERGE | P-331 (Phase 1b), P-335 (owner's commissioning call) |
| L162 | LOW | MERGE | P-332 (debt #39); B1121 OPEN |
| L163 | LOW | DISCHARGED | B866, B978; residue P-301 → B1758 |
| L165 | LOW | MERGE | P-332 (duplicate of L176) |
| L166 | MEDIUM | DISCHARGED; remainder into P-303 / P-295 | B1070–B1073; value side B1075, B1128, B1132 |
| L174 | MEDIUM | DISCHARGED; remainder into P-330 / P-289 | C1–C4 B1088–B1091; C5 B1108 (not B1175) |
| L175 | LOW | DISCHARGED | B1110 (OPEN_LEADS.md:1960, :2012) |
| L176 | LOW | MERGE | P-332 |
| L177 | MEDIUM | DISCHARGED; remainder in P-330 + P-540 | B1104 (OPEN_LEADS.md:1995) |
| L178 | LOW | MERGE | P-335 (owner: retire by the math) |
| L182 | LOW | SUPERSEDED | B1146, B1154, B1156/B1159; B1736 (P-302); B1733/B1734 (P-312) |
| L183 | LOW | MERGE | P-322 (B1177's scanner never committed) |
| L184 | LOW | DISCHARGED | B1178; regression residue into P-322 |
| L185 | LOW | CLOSE by the reader's table | qL155 → P-317 (c); qL159 needs a row |
| L188 | LOW | DISCHARGED | B1199 GC-31 (FINDINGS.md:59); the 55 count into P-318 |
| L189 | LOW | CLOSE by the reader's table | U_e/PMNS needs its own row (P-283's DONE, B1799, does not cover it) |
| L190 | LOW | SUPERSEDED | SL(n) era; B1188 |
| L191 | LOW | MERGE | P-334 (B502 dead at depth 4, reader) |
| L192 | MEDIUM | MERGE | P-323; θ̄ is a P-585 held-out target (look-count flag below) |
| L193 | LOW | MERGE | P-334 |
| L194 | LOW | DISCHARGED | B1477 (Theorem A); proof obligation on T-QUARTER-IS-RHOMBIC; (b) into P-334 |
| L195 | MEDIUM | STILL OPEN | not built; ~214 unwalked hatches, 32 at score ≥ 4 (reader) |
| L196 | LOW | DISCHARGED | B1235 addendum + lock (OPEN_LEADS.md:2286) |
| L197 | MEDIUM (record) | MERGE | P-319 (debt #26), P-589's screen; lock_kind column into P-322 |
| L198 | LOW | MERGE | P-322 (CANNOT_RUN is 189 of 398, not 139; five GENESIS-cited arcs first) |
| L200 | LOW | RETIRE | identification note into P-318's B1295 item |
| L201 | LOW | SUPERSEDED | B1641, B1674 (the anomaly was a truncation artefact) |
| L202 | LOW | DISCHARGED / SUPERSEDED | B1324, B1413, B1418, B1441; B1604 (FK11) |
| L203 | LOW | SUPERSEDED | B1733, B1795 (order-16 lines not in its menu), B1722, B1723 |
| L204 | LOW | DISCHARGED | B1322 (status line CLOSED, OPEN_LEADS.md:2418) |
| L205 | MEDIUM | MERGE | P-333 (debt #24): o10_150729's three on five ends |
| L206 | LOW | DISCHARGED | the generating identity (re-checked by reader C); dated note on B1401 via P-334 |
| L207 | LOW | MERGE | P-334 |
| L211 | LOW | MERGE | P-318 (the strata are instrument outputs; B1424's two blocks both one-cusped, re-checked) |
| L212 | LOW | DISCHARGED | reader's argument; P-249 → B1702 |
| L213 | LOW | MERGE | P-322 |
| L214 | LOW | MERGE | P-322 (add the six live absence claims) |
| L215 | LOW | DISCHARGED (when P-334's note lands) | ε₃·f₅ (re-checked against the lead's table) |
| L217 | MEDIUM | DISCHARGED; remainder in P-328 | B1409 (banner CLOSED, OPEN_LEADS.md:2767); B1809 |
| L218 | MEDIUM | MERGE | P-318 (B1408's universal sentence), P-156 (the index's premises) |
| L219 | MEDIUM | DISCHARGED as posed | B1410; selection into P-139; Menal-Ferrer–Porti to be read |
| L220 | LOW | DISCHARGED | its body (OPEN_LEADS.md:2933), R57-3; instrument gaps into P-322 |
| L221 | MEDIUM | MERGE | P-326 (the Majorana form), P-294 (the 351′ note) |
| L222 | MEDIUM | DISCHARGED | B1438, B1444, B1470, B1441, FK13; **W134 residue needs a [DEBT] row** |
| L223 | LOW | SUPERSEDED | B1700, B1795, B1415/B1444/B1446 |
| L229 | LOW | DISCHARGED | P-309; (iv) via P-312 → B1733, B1734 |
| L231 | LOW | MERGE | P-427 (+ P-317 (b), P-318, P-330); "16σ" and the crossing count into P-426 |
| L232 | LOW | MERGE | P-426 (debt #27) |
| L233 | MEDIUM | DISCHARGED | B1438, B1440, B1737 (P-311); **B1737 §4's follow-on needs a row** |
| L234 | LOW | DISCHARGED | B1442; P-309; P-288 DONE |
| L235 | MEDIUM | SUPERSEDED | P-566, P-555, P-303 (the Higgs construction; B1739, B1827) |
| L236 | LOW | DISCHARGED | B1444, B1445; (f) into P-139; (e) unbanked |
| L237 | LOW | DISCHARGED | B1447, B1451, B1736 (P-302) |
| L239 | LOW | MERGE | P-321 (a), P-428 (c) |
| L240 | LOW | MERGE | P-092, P-320, P-428; **(g)+(h) need a row** |
| L241 | **HIGH** | STILL OPEN (standing) | B1744 (P-324); B1827 lines 61–86; P-295, P-566, P-583 |
| L242 | MEDIUM | MERGE | P-337 (the zero law; the web seat's derivation unverified on main), P-428 |
| L243 | LOW | MERGE | P-428 |
| L244 | MEDIUM | STILL OPEN (standing) | B1473; P-441 DONE; live cells P-465, P-468, P-475 |
| L245 | LOW | DISCHARGED | B1469–B1472; B207 note to P-318 (unrowed); (z) in P-322 |
| L246 | LOW | SUPERSEDED | B1474–B1481; remainder in P-035, P-289, P-337 |
| L247 | LOW | MERGE | P-571 (debt #62), P-589 (debt #15); member-scope baseline still 8 (gates.py:1601) |
| L248 | LOW | MERGE | P-335 (owner: §8 retire or later) |
| L249 | LOW | MERGE | P-429 |
| L250 | MEDIUM | STILL OPEN as P-403 / P-458 | B1483, B1484, B1794, B1795, B1800 |

## THE TOP TEN, by potential

**1. L241 — the measurer question, now the reading that decides the quark mixing (HIGH; standing).**
- **The idea.** The owner asked that the derivation stop dropping "the measurer" that tracks a → ab, b → a. The
  record's working translation is the *marking*: a base point, the letters' order, an orientation, and which of a
  module and its dual is read as the particle.
- **Where it stands today.** The 2026-10-23 reader located that fourth marking exactly in B1656's frame: *the reading*,
  which sector sees h and which h̄. Since then B1827 found that the reading which lifts the CKM's corner inversion is the
  adjugate, adj(S) = εSᵀεᵀ (the dual read holomorphically). On the order-5 lines that reading is the frame's own
  down–lepton relation (P-583).
- **Why it could change the direction.** The wall that blocks the quark mixing is then a per-sector binary choice of
  exactly the kind this lead names. A rule from the object that forces it would turn a free choice under the CKM wall
  into a consequence, and it would bear on the lepton–down relation at the same stroke.
- **The first computation.** P-583's data-free cell: the corner order and the first row's size on the 24 order-5 lines
  under (up S, down adj S). Then the forcing question: does any datum of the object fix which sector reads the dual —
  the orientation sheet, the record swap, or the twist's sign? One arc, data-free.
- **What is known against it.**
  - B1744: the Higgs's own twist is even, so it does not force the reading.
  - B1825: one address is NEGATIVE.
  - B1829: a reading chosen per sector is a counted input unless it is forced.
  - The S298 note on B1827 shows how easily a closure claimed in this area turns out to be unearned.

**2. L151 — the anchor budget: Re τ as a CP bit (HIGH; carried by P-328, with L217's remainder).**
- **The idea.** The owner's bridge principle says the typing of the inputs should predict how many continuous anchors
  are licensed: at most one dimensionless.
- **What was found.** The 2026-10-23 reader found a data-free rule on B1656's frame, checked in 96 of 96 cases: at
  Re τ = 0 or ½ the frame's J vanishes exactly when the CP image of the line is the line. The web seat reproduced it on
  the ten (2/5, k/10) lines (P-328's rows 1411 and 1414).
- **Why it could change the direction.** It is the only concrete route on the record to removing a continuous input:
  Re τ would be fixed discretely by CP, the line would carry the CP violation, and Im τ would be left as the single
  licensed anchor. That bears directly on "τ not selected" and on the free-number count. MAINS_PLAN.md:81 still lists
  "Re τ, and the line's position … no rule".
- **The first computation.** Re-derive the rule on main from B1724's covariance on every line of orders 5, 8 and 10 at
  Re τ ∈ {0, ½}. Data-free, minutes. P-328 has been escalated with exactly this action since 2026-10-28 and has not
  moved.
- **What is known against it.**
  - B1791: Im τ is not forced.
  - B1821: J's sign is never predicted.
  - P-323's note: on those loci the θ_Y phase depends on the line's representative.
  - Any test with Re τ fixed in advance is a counted look under B1829, and the best rows are already seen.

**3. L222's residue — W134's threshold against the whole cusp unit (MEDIUM in part C; ranked third here because it
bears on the one structural count the record calls derived).**
- **The two routes.** C8, banked in B1796 and B1797 (GENESIS v1.59), reaches three generations with one whole cusp
  unit. The SM seat's W134 says three chiral 27s in E₈'s family slot need 17/24 of the unit or more, "never the empty
  end or the whole unit", with m ≡ 5 − r mod 8.
- **Why it matters.** Both can stand only if the family symmetry is not E₈'s SU(3), or if m rather than n is the datum.
  Either way it moves where "three generations by selection" is priced.
- **Verified here.** P-302 is closed DONE by B1736, but B1736's FINDINGS line 33 says "W135's K2 (the anomaly of the
  full 27, m ≡ 5 − r mod 8) is not re-derived here". GENESIS, B1796 and B1797 never mention W134, and no open row
  carries it.
- **The first computation.** Derive K2 and the admissibility rule from B1674's det ρ = χ_η⁹ (minutes). Then W134's
  twelve |I| = 3 data from B1641's χ formula (exact, under an hour).
- **What is known against it.** W134 is a seat result, unverified, so the tension may dissolve on the first check.

**4. L166 (with L235) — a rule for the Higgs direction, "never a guessed vector, never a fit" (MEDIUM).**
- **Why it matters now.** The CKM wall is a choice in how the Higgs is built (B1826, B1827; FRAMING_LEDGER FL-06). In
  the old frame the listener map supplied a direction by a stabiliser-and-Galois rule (B1070, using A₅). The analogue
  here is S₄, the Higgs triplet's projective image (reader A's observation, not banked).
- **The first computation.** One data-free arc. Ask which rules stated in field data alone (stabilisers, holomorphy,
  being zero-free) select a direction on B1700's and B1730's spaces and on B1827's two-ingredient Higgs.
- **What is known against it.**
  - B1700: the unit does not select.
  - B1731: being zero-free is only a necessary condition.
  - B1744 and B1825 are NEGATIVE.
  - The work already belongs to P-303 (OWNER) and P-295.

**5. L250 — the frame of the right parity (MEDIUM; open as P-403 and P-458).**
- **The idea.** The record's only named route to matter counted by an index on a bundle with curvature. It is also the
  natural home of the towers' fluxes.
- **The untried angle (P-458).** The spin connection ω = Re A is the object's one canonical non-flat SU(2) background,
  its curvature fixed by Mostow rigidity. It would supply curvature without free flux integers, which is P-401's
  objection to the flux pivot.
- **The first computation.** The twisted Dirac spectrum coupled to ω on m004 against m003, on both spin structures,
  with B940's instrument (about 50 minutes a run). P-540 has to settle that instrument's ± check first.
- **What is known against it.**
  - B1794: rationally, no characteristic classes on any closed member's frame.
  - B1795: the doublet–triplet split, the gauge half, is NEGATIVE.
  - Cell (d), the literature read on the bench, is still owed.

**6. L233 — the channel norms as Kronecker-limit logs: a candidate rule for the line (MEDIUM; unrowed).**
- **The idea.** B1737 proved the slope is a twisted Shintani zeta value. Its §4 registers a follow-on: are B1656's
  channel norms c_s Kronecker-limit logs of the same L-function per (thread, line)? If so, "a candidate rule for the
  line" follows.
- **Why it matters.** The line is the strip candidate's weakest input (P-384, debt #2: "mostly a pick").
- **Its status.** No arc computed it, and it has no register row: P-311 is DONE with the follow-on inside its text.
- **The first computation.** Test c_s against −2π ln∣θ[v](0)∣² plus a τ-only term at a few (thread, line) points.
  Data-free, about an hour.
- **What is known against it.** B1800 already writes the flux-frame couplings as theta functions with characteristics,
  so the identity may be classical and select nothing.

**7. L244 — the symmetric phase: the principle's own path as the ground and the hierarchies as departures (MEDIUM;
standing).**
- **What is done.** The census (B1473), β_c (verified) and the critical line (P-441 DONE).
- **Live cells:**
  - P-465: the golden path never reaches the cusp, where the deep hierarchies live; what drives the departures?
  - P-468: picked in combination; its form 4 closed negative.
  - P-475: τ's one-loop potential as the factor that rises with depth.
- **Why it matters.** It is the record's one structured idea for selecting the strip's height.
- **The first computation.** Set B1704's potential against the threads' measure (data-free, hours), with any predicted
  height sealed.
- **What is known against it.** B1722 and B1813 show that neither measure selects on its own. Reader D2 found neither
  measure normalisable (not banked).

**8. L221 — ν^c's Majorana mass as a modular form (MEDIUM; P-326).**
- **The idea.** B1674 requires ν^c and B1616 forbids a constant mass. A reader's scratch check finds such forms only at
  odd weight, and in one hand the weight-3 form is unique up to scale.
- **Why it matters.** It is a cheap structural test of the frame. It bears on the reading of the live prediction P10 as
  Dirac neutrinos (P-157, debt #7). Its 351′ note names the one field, missing from the record's E₈ frames, that would
  carry both the Clebsch −3 and ν^c's mass, which touches the lepton–down relation D (P-294, P-355).
- **The first computation.** The existence-and-weight cell on main (minutes, data-free).
- **What is known against it.**
  - Neutrino masses are outside the 19.
  - B1799 computed the self-pairings, not this form.
  - S291's retraction of the "45" shows how easily this route mislabels.

**9. L205 — m003's companion carries F-CI's three on all five ends (MEDIUM; P-333, debt #24).**
- **The idea.** The companion o10_150729 (L10n113) carries F-CI's three on every end, with A₅ transitive on the ends, so
  no end is chosen. It is the only one of 16 thread companions computed, which makes it the record's only weave-level
  selection signal for a three.
- **The first computation.** A sealed F-CI read with B1492's instrument (minutes), then a companion census to word
  length 10 (one arc, data-free).
- **What is known against it.** FK14 and B1604 grade a three on a cover as a selection, never a count.

**10. L192 — does the object's ℤ/2 put θ̄ at a CP-even point? (MEDIUM; P-323).**
- **The idea.** Ask the bit-valued channel a bit-valued question: does the object place the strong-CP phase at a
  CP-even point?
- **Why it matters.** θ̄ is one of the 19 and one of P-585's level-2 held-out targets. A structural yes would settle one
  of the 19 without a free parameter.
- **What is known against it.** The web seat's sealed test "THE STRONG ANGLE IN THE MASS FRAME" (harvest rows 1439,
  1443) did not hold as sealed; its power control failed, so it is not decisive. The SM seat's W168 reproduces it. Main's
  own sample check is owed.
- **The first computation.** That check, designed so it is not a new look at P-585's target.
- **Runner-up for this slot: L174/L177's C10 count** on a physical spacetime (P-330, P-289, P-540). S274's note says it
  cannot tell T from T̄.

## Leads to close, with pointers (for main to verify)

**Answered, superseded or retired (41).**
- L144: B1096.
- L146: B1600, B1601, B1629, B1733.
- L147: B1006, B1021, B1656.
- L149: B1019.
- L157: B1039, B1042, B1043, B1609.
- L158: B1040, B1041.
- L159: B1248, B125, after the Deligne–Milne gate.
- L163: B866, B978, B1758.
- L166: B1070–B1073, B1075, B1128, B1132.
- L174: B1088–B1091, B1108.
- L175: B1110.
- L177: B1104.
- L182: B1146, B1154, B1156, B1159, B1736, B1733, B1734.
- L184: B1178.
- L185 and L189: by the 2026-10-23 tables, each with one new row.
- L188: B1199 GC-31.
- L190: SL(n) era; B1188.
- L194: B1477.
- L196: B1235 addendum.
- L200: retired into P-318.
- L201: B1641, B1674.
- L202: B1324, B1413, B1418, B1441, B1604.
- L203: B1733, B1795, B1722, B1723.
- L204: B1322.
- L206: the identity, with its note via P-334.
- L212: P-249 → B1702.
- L215: when P-334's note lands.
- L217: B1409, B1809, P-328.
- L219: B1410, P-139.
- L220: its body, R57-3.
- L222: B1438, B1444, B1470, B1441, FK13.
- L223: B1700, B1795, B1415, B1444, B1446.
- L229: P-309, P-312 → B1733, B1734.
- L233: B1438, B1440, B1737.
- L234: B1442, P-288.
- L235: P-566, P-555, P-303.
- L236: B1444, B1445.
- L237: B1447, B1451, B1736.
- L245: B1469–B1472.
- L246: B1474–B1481; remainder in P-035, P-289, P-337.

**Carried in full by register rows (32).**
- L145 → P-322
- L148 → P-322, P-291
- L151 → P-328
- L152 → P-291
- L154 → P-137, P-138, P-318
- L161 → P-331, P-335
- L162, L165, L176 → P-332
- L178 → P-335
- L183, L198, L213, L214 → P-322
- L191, L193, L207 → P-334
- L192 → P-323
- L197 → P-319, P-589
- L205 → P-333
- L211 → P-318
- L218 → P-318, P-156
- L221 → P-326, P-294
- L231 → P-427, P-317, P-318, P-330
- L232 → P-426
- L239 → P-321, P-428
- L240 → P-092, P-320, P-428
- L242 → P-337, P-428
- L243 → P-428
- L247 → P-571, P-589
- L248 → P-335
- L249 → P-429

## Process findings for main

1. **Work done, heading never marked: 21 leads.**
   - Done in body text or by an arc: L144 (B1096), L149 (B1019), L157, L158, L163 (B1758), L166, L174, L175 (B1110),
     L177 (B1104), L188 (B1199), L196, L204 (B1322), L217 (B1409), L220, L222.
   - Answered by the 2026-10-23 sweep or later arcs and never closed: L206, L229, L233, L234, L236, L237.
   - L220's Review 58 escalation re-carries stale task text (OPEN_LEADS.md:2938). L222's escalation to the owner is
     stale: FK13 ruled it.
2. **The 2026-10-23 sweep's answers were not written into the record.** P-334 and P-318 are still QUEUED. No dated
   note has reached B1400, B1401, B1406, B1408 or B1424 since 2026-10-23. Several pointers above rest on reader
   computations that were never banked: L145a, L149's m = 4 door, L151's CP rule, L154, L159, L162, L165, L176, L207,
   L212, L215 (reader C hand-checked it against the lead's table) and L236 (e).
3. **Reader findings with no register row (proposed):**
   - **W134's K2 and its 17/24 threshold** (L222): a [DEBT], since P-302 is DONE with it unverified.
   - **B1737 §4's channel-norm follow-on** (L233): a [LEAD].
   - **U_e / the PMNS in B1656's frame** (L189): a [LEAD].
   - **qL159**: the flow coupling κ in CLAIMS P15/P16 is undeclared against the bridge κ (L185; a second E72 instance).
   - **The HEARING LANDSCAPE proof sketch** (L188).
   - **B207's scope note** from xB014 (L245; add to P-318).
   - **GENESIS §6's Stage 6 page and the fresh-reader test of GENESIS and the README** (L240 (g), (h)).
   - **The withdrawn "16σ" on living surfaces and the inconsistent crossing count** (L231; add to P-426).
   - **B1795's menu omitted L203's order-16 lines** (a one-line note on B1795).
4. **P-585's prior-look count for θ̄ may be too low.** Reader B lists several separate frame computations of the θ̄-type
   phase on or near the strip's lines:
   - the 2026-10-23 reader's R6;
   - the web seat's e20–e20d and its sealed test (rows 1411, 1414, 1430, 1439, 1443);
   - W113 and W168;
   - the agy lane (row 1539).

   P-585 records "one prior look". Under B1829 a level-2 target must be untouched, so LOOK_LEDGER's count should be
   checked before θ̄ is used as a confirmation. No values are given here.
5. **Front statements still false or stale:**
   - GENESIS.md:262 and LAW_MAP.md:236 ("the siblings have no door"), against m = 4 (P-318, the reader's result,
     unbanked).
   - MAINS_PLAN.md:81 (Re τ "no rule"), pending P-328.
   - The member-scope gate is frozen at 8 since 2026-10-04 (scripts/gates/gates.py:1601), with none of L247's addenda
     landed (P-589).
6. **Tools:**
   - `query.py card <arg>` ignores its argument (scripts/atlas/query.py:194).
   - open_claim_sweep.py's surface list (lines 36–46) lacks GENESIS.md, POINT_REGISTER, THE_COMPLETION_MAP and
     THE_WEAVE, and REVIEW_TEMPLATE has no step to run it. That sweep is the instrument that catches this report's main
     failure.
   - The REVIVABLE hatch index (L195) has never been built.

---

# Per-lead entries


# Review 74, open leads, part A: L144–L166 (fork A, 2026-11-04)

Read-only. Nothing banked; main verifies every pointer. No data contact. The 2026-10-23 reader reports
(audit/drafts/leads_reeval/) are reader verdicts, not banked; where an entry relies on one it says so.

Method: lead text and dated notes (docs/OPEN_LEADS.md); the 2026-10-23 report; the sweep's rows P-314–P-336 and every
register row naming the lead; arcs citing the lead by number (Python scan of every frontier FINDINGS.md and
arc_verdict.json: none from B1723 on cites any of these seventeen leads by number) and by key terms in B17xx–B18xx.

Note for main: the parent's cross-reference index (_xref_index.txt) came out empty because BSD grep -rE with a
bracketed `(^|[^...])` prefix returns nothing silently; a Python scan works (scratchpad xrefA.py).

---

### L144 — is B167's door-map still standing after the cascade campaign? (docs/OPEN_LEADS.md:1081)
- **Idea.** Re-read B167's POSTULATED five-door "no internal door for a scale" taxonomy after the cascade gave the
  object SM gauge content; door 5 (a topological, RG-invariant ratio from the anomaly layer) was the proposed retry.
- **Status now.** Door 5 closed by B1096 (NEGATIVE: over the derived 16 every anomaly channel vanishes identically);
  the lead's own body has carried "CLOSED 2026-08-20 (B1096, L170a)" since R57-3 (OPEN_LEADS.md:1083), but the
  heading lacks the word, so lead_debt.py counts it open. The banner's "Doors 1–4 remain untouched" is stale in
  substance: the 10-23 reader (L144_to_L147.md §L144) read doors 1–4 against the weave (door 1 = τ's height, B1667;
  door 3 = what holds τ, B1684/B1704, now B1791 NEGATIVE "Im τ not found forced"; door 4 shut by B151/B666 cell S).
  The banner correction is already a listed item of P-318 ("L144's banner and THE_LADDER X30"; QUEUED [DEBT], #16 of
  the debts by load). The scope repair (B666 cell S covers algebraic outputs with finite stabiliser, not modular-form
  values at free τ) belongs to P-138 (debt #23).
- **Potential.** LOW — every door is shut or re-homed (τ's selection lives in P-139/FK9, B1791, B1813).
- **First computation and cost.** None; a heading mark and two dated notes (minutes).
- **Disposition.** DISCHARGED (B1096; heading to be marked CLOSED); remainder MERGE into P-318 (banner, X30) and
  P-138 (B666 cell S scope).

### L145 — THE REVIVAL RESERVOIR (kill_graph.json's hatch/revival_score fields unindexed) (docs/OPEN_LEADS.md:1193)
- **Idea.** B738's kill graph carries `hatch`, `revival_score`, `priority` that no register indexes; L145a: B500's
  child-hunt kill is provisional (35 words unchecked); L145b: six more high-revival kills; L145c: non-arc ids;
  L145d: LEAD_REGISTER.md never triaged.
- **Status now.** The index still does not exist (no docs/*reviv*; L195 owns it, and P-322 lists "a REVIVABLE view
  over the kill graph's ~214 unwalked hatches (L195)", QUEUED [PROCESS]). The 10-23 reader found scoring stopped at
  the weave (0 of 29 kills from B1600 on scored). L145a: the reader computed (SnapPy, audit room, not banked) that
  the child 4₁(5,1) is the slope-(5,1) point on the tick's own character curve and that two of B500's three verbs are
  not moves, so the 35-word reopen is moot; B500's revival score 6 should come down. L145b: B111 answered by GENESIS
  v1.30–v1.31 (B1609, B1610), B712 by C1/B1720, B706 by B1656's frame; B374, B394 retire (reader). L145d: LEAD_REGISTER
  rows were swept as LEADREG_1_9.md / LEADREG_10_18.md on 10-23 (QUEUE.md "LEAD_REGISTER rows 1–9 / 10–18"), so that
  half is done; the generated view is in P-322.
- **Potential.** LOW — an index and hygiene; no physics rests on it.
- **First computation and cost.** L195's generated index with a weave_or_thread column and a planted composite-id
  control: under one arc, data-free.
- **Disposition.** MERGE into L195 / P-322 (the REVIVABLE view); L145a write-down (B500/B986 dated note, score
  lowered) into P-334 after main re-runs the reader's one SnapPy script.

### L146 — IS m004 SPECIAL AMONG ONCE-PUNCTURED-TORUS BUNDLES? (docs/OPEN_LEADS.md:1259)
- **Idea.** On the common base Σ₁,₁/SL(2,ℤ), test whether m004 is distinguished among the bundles; runnable form:
  extend L105's conductor/McKay-shadow test across the metallic family (hypothesis: only m = 1 has the McKay shadow).
- **Status now.** (a) Answered, in the direction the lead pre-stated as FALSE: 2T arrives on every odd-trace thread
  (B1600 W3; B1601 PROVED, 16 of 16 to length eight), so the E₆ arrival is generic and "the two bases" are one on the
  weave (THE_WEAVE: "being universal on odd trace, it is not what singles out ±LR"). (b) What singles out a thread:
  lowest geodesic (B1629), smallest wording (GENESIS v1.49), fewest fixed lines — the line rule is banked as B1733
  (PROVED; P-312, P-336 DONE): a thread fixes lines of order N iff N divides the larger Smith invariant of A ∓ I; at
  order 5 one pair {v, 2v}. The selection question itself ("which thread / which τ") lives in P-139/FK9, B1722
  (NEGATIVE), B1791 (NEGATIVE), B1813. The reader's "t − 1 lines" count is not stated in B1733 (it states coker
  orders ∣2 ∓ t∣); a one-line corollary if wanted.
- **Potential.** LOW as a lead — fully absorbed into the selection problem (P-139), which is HIGH but not this lead's.
- **First computation and cost.** None owed by the lead.
- **Disposition.** DISCHARGED ((a) B1600, B1601; (b) B1629, B1733); selection SUPERSEDED by P-139/FK9.

### L147 — THE PRECISION BOTTLENECK (λ₂ of m004 beyond 25 digits) (docs/OPEN_LEADS.md:1349)
- **Idea.** m004's second Maass eigenvalue, the one "object-level real number", to 50 digits for a powered PSLQ.
- **Status now.** The nulls stand: B1006 (NEGATIVE, powered at 25 digits) and B1021 (the parent eigenvalue at 31
  figures, a two-eigenvalue null). The instrument is on main (B1007: frontier/B878_maass_upper_window/
  branch_cell9_rung1_v2.py). The 50-digit run was never done (priced ~100–500 core-hours by the reader). Under the
  weave rule λ₂ is one thread's number and no coupling, completion item or P-row reads a 3d Laplace eigenvalue
  (reader, L144_to_L147.md §L147); the value programme moved to modular forms of τ (B1656).
- **Potential.** LOW — neither PSLQ outcome can move any of the 19 or any completion item.
- **First computation and cost.** The 50-digit run, ~100–500 core-hours; not recommended.
- **Disposition.** SUPERSEDED (the weave frame, B1656; nulls B1006, B1021 stand); retire the extension by the math,
  keep the text as the instrument's record.

### L148 — RE-GROUND THE ATLAS LEXICON, OR STATE THAT IT IS HISTORICAL (docs/OPEN_LEADS.md:1425)
- **Idea.** The atlas's object vocabulary is frozen on the early corpus; widen it (and re-derive B806/B1008) or label
  the atlas historical.
- **Status now.** Half done: B1247 widened the question layer (seven motifs; top-3 coverage unmoved) and left the
  object layer frozen deliberately. The epoch gap persists into the weave era (reader K1: top-3 coverage 0.55–0.66 at
  B1601+). Review 43 marked L148 "resolved" by per-arc judgement (REVIEWS.md:3383), which the reader shows did not
  touch B1008's under-labelling finding. A defect: `query.py card <arg>` ignores its argument — still true on main
  (scripts/atlas/query.py:194, `if not argv or argv[0] == "card"`); listed in P-322 (QUEUED [PROCESS]).
- **Potential.** LOW — retrieval hygiene; it matters only for seen-first sweeps (topic_sweep.py is the working tool).
- **First computation and cost.** Fix `card <arg>` with a failing-path test (minutes); the WIDEN/DECLARE decision as
  one instrument arc (~2 h).
- **Disposition.** MERGE into P-322 (tooling) and P-291 (instrument-era drift); a dated correction of R43's "L148
  resolved".

### L149 — RUN THE CASCADE ON A NON-GOLDEN GRAMMAR (docs/OPEN_LEADS.md:1455)
- **Idea.** Does the silver (or bronze) grammar's cascade also land on the SM? If yes the endpoint has no confirming
  power; if no, the golden's specialness propagates.
- **Status now.** Answered for m = 2, 3 by B1019 (PROVED: the siblings' own-conductor shadows admit no SU(2)
  embedding, so no cascade begins); the lead's own 2026-08-19 stamp says "OVERTAKEN … by B1019", heading unmarked.
  New since: the 10-23 reader (L148_to_L152.md §L149(b), K4/K5, not banked) found B997's all-m uniqueness fails at
  m = 4 (⟨R⁴, L⁴⟩ mod 20 is SL(2,5) = 2I; door set {1, 4}); the true uniqueness is the conjunction "own-conductor door
  and π₁ ↠ 2T" = {1}. That correction is P-318's first item (QUEUED [DEBT], #16 of the debts by load) and is still
  unpaid: GENESIS.md:262 ("m004's siblings have no door (B1019)") and LAW_MAP.md:236 ("ONE GRAMMAR, ONE DOOR") stand
  unamended. The weave form (a two-door census over word states) was merged by the reader into L252/P-041 (L252
  escalated by main today).
- **Potential.** LOW for the open questions; the m = 4 correction is a foundation-statement debt (already ranked).
- **First computation and cost.** Re-derive K4/K5 on main with B1019's and B993's instruments (minutes), then the
  dated notes and a GENESIS amendment.
- **Disposition.** DISCHARGED (B1019; heading to be marked); the m = 4 correction stays on P-318; the census MERGE into
  P-041 / L252.

### L151 — THE ANCHOR BUDGET AS A STRUCTURAL PREDICTION (docs/OPEN_LEADS.md:1528)
- **Idea.** The owner's bridge principle: the input typing should predict its own anchor budget (one dimensionful plus
  at most one dimensionless continuous anchor, R11); MATCH or MISMATCH against what predictions actually need.
- **Status now.** Never run as a banked cell. Its premise moved (B1017, B1261, B1266, GENESIS v1.47's price line:
  the typed-input count is itself an undercount; P-374, [DEBT] #18, owes THE_CLAIM §1's recount). The 10-23 reader
  ran the budget as bookkeeping on B1656's frame: MISMATCH (τ is two reals against ≤ 1 licensed, plus ~10–13
  unlicensed bits), and found a data-free rule (K6): at Re τ = 0 or ½ the frame's J vanishes exactly when the CP image
  of the line equals the line (96/96), so Re τ could be fixed discretely by CP with the line carrying the CP violation,
  leaving Im τ the single licensed continuous anchor. The web seat reproduced the rule on the ten (2/5, k/10) lines
  (P-323 note, rows 1411/1414). Merged into P-328 (QUEUED [LEAD], ESCALATED 2026-10-28: "verify the web seat's e20c
  J-vanishing rule on main … then decide whether it makes Im τ a licensed anchor") — not verified on main (no B17xx/
  B18xx arc states it). docs/MAINS_PLAN.md:81 still lists "Re τ, and the line's position u: continuous (two) … no rule
  (P-384)"; B1791 (NEGATIVE) closed only Im τ.
- **Potential.** HIGH — the one concrete, data-free route on record to remove a continuous input (Re τ → a CP bit),
  bearing on "τ not selected" and on the free-number count, the restated goal.
- **First computation and cost.** Re-derive K6 on main from B1724's covariance (the CP image map) on every line of
  orders 5, 8, 10 at Re τ ∈ {0, ½}: data-free, minutes; then an R11-type column in the input ledger. A sealed
  R11-budget look (Re τ fixed to {0, ½} a priori) is a counted look under the two-level bar (B1829), after P-585.
- **Disposition.** MERGE into P-328 (escalate: the K6 re-derivation on main as its next action, before any look).

### L152 — RELAYS ARE NOT GATED FOR CONTENT (docs/OPEN_LEADS.md:1547)
- **Idea.** relay_debt.py checks dispositions, not whether a relay's content contradicts main (the θ_QCD = 0
  episode); design (a) claim-echo, (b) delivered-list rule, (c) accept.
- **Status now.** No content gate exists (grep of scripts/checks for delivered/claim-echo: none). The reader ran the
  design cell retroactively (K7): rule (b′) catches the θ instance and fires on 8 of 667 archived relays, so by the
  lead's own two-outcome rule the answer is "build". The class recurred (B1472's sep16 lane; P-184), caught by reading.
- **Potential.** LOW — process integrity.
- **First computation and cost.** One instrument arc (~1 h plus a failing-path test and a GATE_CONTROLS row).
- **Disposition.** MERGE into P-291 (the math-integrity check, QUEUED [PROCESS]) as its relay/harvest-content check.

### L154 — IS THE GRAVITATIONAL σ THE STAGE'S σ? (docs/OPEN_LEADS.md:1587)
- **Idea.** c((E₆)₁) = 6 and the AdS₃ closure c = 6σ: if the stage CFT is the boundary CFT, σ = 1 is forced and the one
  continuous dimensionless anchor becomes an output.
- **Status now.** UNDECIDED (B1034); the c = 6 route obstructed at the torus (B1064 NEGATIVE: amphichirality deletes
  the quantised sector); B1228 retracted σ = 1 in-arc (the geometric connection's boundary WZW is A₁, rank 1). On the
  weave the quantised sector is present (B1650; P-137, QUEUED [LEAD] Q7, unmoved since 2026-10-14). The action weight
  at c = 6 failed as a thread measure (B1722 NEGATIVE, W2 21.0%) and is supercritical (P-476, LEAD). The reader
  (L154_to_L159.md, C-1, not banked): every vector-valued form of the field stage on record is D-type (ρ_T ≅ so(4)₁ up
  to a phase; F₆ presents so(12)₁, c = 6 as D₆), never (E₆)₁-type; and a compact-image (2T) flat connection has volume
  0, so σ is invisible exactly where E₆ lives. B1228's "σ = 1 picks E₆ uniquely" also omits A₆, D₆ — in P-318's list.
  σ is outside the 19. P-492 ([DEBT] #60) questions B1088's boundary assumption under the same c = 6σ.
- **Potential.** LOW — outside the 19; the anchor A2 stands; the bridge would change an input outside the SM count.
- **First computation and cost.** P-137's lemma arc (C-1 extended to ρ̄_T and every F_a; the volume-zero lemma; the
  B1228 K6 sharpen): ~1 h writing, seconds of compute.
- **Disposition.** MERGE into P-137 (the bridge on the weave), P-138 (σ's wording), P-318 (B1228's K6).

### L157 — THE INTERACTION HOOKS (the seed–field frame's computables) (docs/OPEN_LEADS.md:1633)
- **Idea.** Four forward tests of the firewalled seed–field cosmogony: the V-valued residual on the double; FMT ↔ trit
  ↔ seam (one mechanism?); L154's bridge; the monotone-creation forbid on a three-copy weld.
- **Status now.** All run in August: L157-1 by B1039 (PROVED: existence NO; the seam-locality forbid UNTESTED, then
  unfalsifiable by MV exactness, X4); L157-2 by B1042 (PROVED: the trit is ω's ℤ/3, JOINED) and B1609 (the trit and
  the weave's three are exclusive); L157-3 is L154; L157-4 by B1043 (PROVED: the forbid holds strictly, h¹ = 10). The
  seed–field frame was replaced by the weave rule (THE_WEAVE.md). The heading never got its closure. B1043's "h⁰ = 1
  nobody had occasion to bank" was banked in B632/B670 — in P-318's list.
- **Potential.** LOW — tests of a superseded frame; the mathematics stays banked.
- **First computation and cost.** None.
- **Disposition.** DISCHARGED (B1039, B1042, B1043, B1609; L157-3 into L154/P-137).

### L158 — THE V-OWNER RECONCILIATION (FL-1, FL-5, FL-6) (docs/OPEN_LEADS.md:1670)
- **Idea.** Who owns the seam space V — the object or the field? Three textual collisions to reconcile.
- **Status now.** Answered in August: B1040 (PROVED: "FL-5 reconciled … FL-1 scoped (the field owns V's structure, the
  object its instantiation)") and B1041 (PROVED: the observer's operation bits are the ambient's Galois directions).
  B1040 asked for a one-line TERMINOLOGY note to close the lead; never written (reader's grep: none for "owns V",
  "instantiation"); the reader also flags an unrecorded three-way collision of "field" (arithmetic ambient; the field
  stage's physical fields; number field).
- **Potential.** LOW — terminology.
- **First computation and cost.** A TERMINOLOGY row (minutes).
- **Disposition.** DISCHARGED (B1040, B1041); the owed TERMINOLOGY note into P-334's write-down list.

### L159 — THE GERBE QUESTION (non-neutral Tannakian? the degree-2 class) (docs/OPEN_LEADS.md:1684)
- **Idea.** "Supplies the space, withholds the point" as a non-neutral Tannakian category; is the programme's H¹ the
  torsor layer inside a gerbe whose degree-2 class was never computed? Reading-gated (Deligne–Milne first).
- **Status now.** No arc cites L159; the gate (the Deligne–Milne reading) never ran. The 10-23 reader (L154_to_L159.md
  §L159, definitions only, not banked): the categories on record are either neutral (Rep_K of the binary groups) or not
  Tannakian (braided modular categories), so the identification retires; the genuine degree-2 object is the Brauer
  class of a representation's K-models, already computed without the name — B1248 (PROVED: (−1, −1) at the Q₈ pair,
  the Hurwitz quaternions), B125 (cusped ⇒ split invariant quaternion algebra); the reader's PARI check (C-2):
  non-split at the common point and at the golden irreps (icosian), split at every thread's geometric point.
- **Potential.** LOW — no completion item or count reads it; one firewalled reading touches FK14.
- **First computation and cost.** The gate: check the reader's definitions against Deligne–Milne §§1–3 (one sitting),
  re-run C-2 (one second).
- **Disposition.** DISCHARGED once the gate is read (B1248, B125); the write-down into P-334.

### L161 — THE APERIODIC CROSSING CAMPAIGN (owner-elected) (docs/OPEN_LEADS.md:1721)
- **Idea.** An SM value = class invariant × substrate scale; cross into aperiodic-order (Fibonacci-chain) spectra where
  a material supplies the scale; Phase 0: a sealed genericity control, the physical realisation, whether the five tones
  are observables.
- **Status now.** Phase 0 ran: P0-0 answered (B1062 V2 as corrected by B1237 — arithmeticity separates bronze only;
  silver rests on B997/B1019's door); P0-1 at seat grade (B8094, unverified on main) with the edge lane sealed (L173,
  B1106) and never commissioned; P0-2 negative on the material side (B1062 V1/V3; the reader's desk lemma: the KKT
  transfer-matrix group is never 2I). Phase 1b (does B1656's coupling on an order-5 line carry 2I's θ-odd doublet,
  which carries the tones, B665) is P-331 (QUEUED [LEAD], unmoved since 10-23; no later arc). Commissioning is the
  owner's (P-335, OWNER, open). Against: order-5 lines force D = 9 (B1728; P-094 excludes it), so the golden's own lines
  are not where the candidate lives; and the order-5 level is not golden-specific (B1733; m = 4, 5, 6 own order-5 lines).
- **Potential.** LOW — parallel to the 19 (a laboratory test of the grammar, not of the SM); Phase 1b is cheap.
- **First computation and cost.** P-331: decompose the SL(2,ℤ) action on one order-5 line's sector data (B1728's
  census module), silver order-4 line as control: data-free, under an hour.
- **Disposition.** MERGE into P-331 (Phase 1b) and P-335 (the owner's commissioning call); keep the election on record.

### L162 — THE F₄-TRANSITIVITY VERIFICATION (rank-1 idempotents, split integral Albert algebra) (docs/OPEN_LEADS.md:1774; updates 1826, 1849)
- **Idea.** Verify the web seat's claim that F₄(ℤ) is transitive on rank-1 idempotents of the split integral Albert
  algebra (the rank-closing VEV direction as one orbit: input #5 "proved irreducible").
- **Status now.** Krutelevich 2002 decides only the E₆-level (NP) orbit and cannot contain the F₄ refinement (gate
  update, :1849). B1121 (OPEN) reproduced the single-idempotent connection on main's code (evidence, not proof). The
  Yale thesis was never read. The 10-23 readers (L161_L162_L163.md; L165_L166_L174_L175.md) proposed a direct proof
  (strong approximation for Stab = B₄, two named steps) and found B1121's pair "inconclusive" was its {−1,0,1}⁸ box
  (an explicit integral rotation reaches the seed). All folded into P-332 (QUEUED [DEBT], #39 of the debts by load);
  no later arc (no B16xx–B18xx FINDINGS mentions F₄(ℤ), Eichler or Krutelevich).
- **Potential.** LOW — expected TRANSITIVE, which would confirm the VEV direction is a selection, not reduce a count;
  outside B1656's mass frame and the 19.
- **First computation and cost.** P-332's proof arc: the stabiliser's smoothness (dim 36 over ℚ, 𝔽₂, 𝔽₃ on B1121's
  machinery, minutes) plus desk work; one arc.
- **Disposition.** MERGE into P-332.

### L163 — THE μ-PENCIL INDEPENDENT DERIVATION (docs/OPEN_LEADS.md:1804)
- **Idea.** Derive the orthogonal charge frame from banked structure independently (B961 §5's route), then re-pose
  L142's three-sites question with the μ-pencil live.
- **Status now.** Answered before it was registered: B866 (PROVED: μ reproduced identically on an independent build),
  B973's rebuild in ~1.5 s, B978 (PROVED: L135 "DISCHARGED for the rebuild", blocked only on char-0 exactification over
  K). L142 closed at register grade (outside bench memo 205, hash verified B1414). The residue (exactness over
  K = ℚ[ρ]/μ) is P-301, now DONE by B1758 (PROVED: the block-12 pencil regenerated from scratch, C25's wall sign
  certified in exact rational arithmetic). So the lead is fully discharged and unmarked — an L251-type miss.
- **Potential.** LOW — gauge-skeleton side, closed.
- **First computation and cost.** None.
- **Disposition.** DISCHARGED (B866, B978; residue B1758 via P-301).

### L165 — F₄(ℤ) ON ORTHOGONAL PAIRS of rank-1 idempotents (docs/OPEN_LEADS.md:1812)
- **Idea.** Is F₄(ℤ) transitive on orthogonal pairs (the two VEVs taking rank 6 → 4), or does arithmetic stratify them
  and shrink the second acceptance's freedom?
- **Status now.** A duplicate of L176 (registered a week later, without citing L165); B1121 ran it under L176's name:
  "INCONCLUSIVE-AT-BOUND". The 10-23 reader (L165_L166_L174_L175.md §L165, B1121's code imported read-only, not banked):
  the hand seed is one integral rotation from the canonical pair, the "big exotic" pair two; a 120/120 census; a
  lattice proof sketch (Eichler's criterion on ⟨−2⟩ ⊥ U⁴) gives pair-transitivity given single-idempotent
  transitivity (L162) and one generation gate (G1). In P-332 (QUEUED [DEBT] #39). Also: a split frame generates
  ℚ × ℚ × ℚ, so the answer does not decide B1099's K-twisted Route A count.
- **Potential.** LOW — expected TRANSITIVE (the pair acceptance stays a selection); no count shrinks.
- **First computation and cost.** Inside P-332: re-derive the lattice argument and port the two-step recipe as a test
  on B1121's instrument (one arc, mostly desk).
- **Disposition.** MERGE into P-332 (with L162 and L176; L165 and L176 should cross-cite B1121).

### L166 — THE LISTENER MAP, posed (docs/OPEN_LEADS.md:1875)
- **Idea.** A rule Λ from field-side data to an admissible unit direction u — "never a guessed vector, never a fit" —
  the crossing cell's one unknown.
- **Status now.** Answered in the old frame: B1070 (PROVED: existence positive, uniqueness the pair u3/u6), B1071
  (sealed, three re-implementations), B1072 (AC3), B1073 (AC6); the value side closed (B1075 MISS, B1128
  INSTRUMENT-NULL, B1132 whole object; B1349 "do not spend the last row"). B1348's "neither outcome attempted / G5
  open" contradicts LISTENER_MAP_SPEC's 08-19 addendum (record hygiene; the reader reconciles them: the group alone
  leaves 12, with Galois the pair). The live analogue today is the Higgs direction and the reading rule: B1700 (end
  data selects DR's space), B1730/B1731 (PF1-W selects F₆), B1744 (NEGATIVE: the Higgs's own twist does not force the
  reading), B1826/B1827 (the CKM wall is the Higgs construction; a singlet part seen through the adjugate balances it);
  P-303 (OWNER) and P-295 (QUEUED [LEAD]).
- **Potential.** MEDIUM — the method (a stabiliser or field-data rule for a direction, as B1070 used A₅; here Γ₄ ≅ S₄,
  the triplet's projective image, reader) is exactly what the Higgs construction lacks, but the work is P-303/P-295's
  and four arcs have closed its old value channel.
- **First computation and cost.** State the Higgs-direction rule as a listener map on B1700's and B1730's spaces and on
  B1827's two-ingredient Higgs: which rules in field data alone (stabilisers of Γ₄, holomorphy, zero-freeness) select a
  direction; data-free, one arc.
- **Disposition.** DISCHARGED (B1070–B1073; value side B1075, B1128, B1132); the live remainder MERGE into P-303 /
  P-295; the LISTENER_MAP_SPEC status reconciliation into P-334.


# Review 74 — open leads, part B (L174–L200; 21 leads)

Reader's notes, not banked; main verifies every pointer. Sources read for each lead: its row and dated notes in
docs/OPEN_LEADS.md; its 2026-10-23 reader report in audit/drafts/leads_reeval/ (reader verdicts, NOT banked); the
P-rows the parked-items sweep (P-309/P-313) made from it in docs/POINT_REGISTER.md; later arcs by L-number and key
terms (frontier/B17*, B18*). FIREWALL kept: no value, sign or bound for y_b/y_t, θ̄ or y_τ/y_b is written below; where
such computations exist, only their location is given. Nothing is compared with data.

**Heading-mark failures found (the L251/B1800 class):** L174, L175, L177 and L196 carry a closure or supersession in
their own body text but not in their heading, so `lead_debt.py` counts them open; L188 is closed only in the Review 52
currency note at the head of OPEN_LEADS (and by B1199 GC-31), never in its own row.

---

### L174 — THE 3D COMPLETION CAMPAIGN (docs/OPEN_LEADS.md:1924)
- **Idea.** Assemble a parameter-free 2+1 quantum gravity with matter on the object: action card (C1), partition
  function (C2), matter sector (C3), boundary/observer card (C4), arithmetic-CS hole (C5).
- **Status now.** Its own row says SUPERSEDED: C1 B1088, C2 B1090, C3 B1089, C4 B1091 (all banked); C5 closed NEGATIVE
  by B1108 (verdict NEGATIVE). The row's second C5 citation ("B1175 records C5 SUPERSEDED BY THE LAW") is a different
  charter's C5 (the cloud gravity charter), per the 10-23 reader (L165_L166_L174_L175.md:188ff) — an unregistered
  citation error. Two scope debts on its cards are registered: P-138 (B1088's "no free dimensionless constant"; DEBT #23)
  and P-492 (B1088's Brown–Henneaux boundary assumption; DEBT #60). The reader also found C1's "zero free constants"
  holds only on amphichiral threads (31 of 482 bundles at CS ≡ 0 mod ½; reader's SnapPy check, not banked). The live
  remainder — the 3+1 Milne completion over the weave (B1708, B1719; W124–W126 seat, W126 unverified on main) and the
  C10 count — is P-330 and P-289 (both QUEUED [LEAD]); no arc after 10-23 computes it (C10 row in
  docs/THE_COMPLETION_MAP.md:60 still "never computed").
- **Potential.** MEDIUM — the remainder (C10) is the one place a generation count could be read on a physical 4d
  spacetime (FK14 "generations are ends"), but S274's verified note on P-289 makes C10 a count on I-26's side that
  cannot tell T from T̄.
- **First computation and cost.** Verify W126 on main (~30 min compute), then the data-free census of the triplet's
  lines on the cusped threads (minutes; reader found 16 of 241 thread classes in ±Γ(4), three equal lines).
- **Disposition.** DISCHARGED as written (C1–C4 B1088–B1091; C5 B1108); remainder MERGE into P-330/P-289. Fix the C5
  citation (B1108 alone).

### L175 — the h = 0 locus of the being gate (docs/OPEN_LEADS.md:1951)
- **Idea.** Is the vanishing locus of B1103's coupling a property of the word, independent of channel and listener?
- **Status now.** Answered: B1110 (PROVED), F5 "L175 CLOSES" — six channels share the identical 28-word set; mechanism
  = diagonal-free weld matrices. The row's own body carries "CLOSED 2026-08-30" (OPEN_LEADS.md:1960) and a second
  closure line at :2012; the heading was never marked. The 10-23 reader: ANSWERED; its method transfers to P-292 (now
  merged into P-337).
- **Potential.** LOW — old SU(3)₂ instrument, no counterpart in B1656's frame.
- **First computation and cost.** None.
- **Disposition.** DISCHARGED (B1110). Mark the heading.

### L176 — F₄(ℤ) on orthogonal PAIRS of rank-1 idempotents (docs/OPEN_LEADS.md:1971)
- **Idea.** Run the integral-Jordan machinery on the pair-orbit question (Route A's rank 6 → 4 needs a pair).
- **Status now.** B1121 (verdict OPEN) ran it: "inconclusive at bound". The 10-23 reader (L176_L177_L178.md:84–195,
  not banked) built explicit integral automorphisms sending both of B1121's non-canonical seeds to the canonical pair,
  and found the orthogonal pair is the wrong stratum for Route A (its pencil norm vanishes identically; the cascade's
  VEV pair too). Registered as P-332 (QUEUED [DEBT], ranked #39 of the debts: "B1121 banked 'inconclusive' … from a
  too-small search box"). Same question as L165 (part A) and L162.
- **Potential.** LOW — does not touch the 19; Route A's own pair is not this stratum.
- **First computation and cost.** Re-run the reader's `l176_seedD.py` construction on main, then Eichler's criterion
  on the 9-dim lattice; under one arc, data-free.
- **Disposition.** MERGE into P-332 (with L165, L162).

### L177 — the 4d suspension selection question (docs/OPEN_LEADS.md:1983)
- **Idea.** The owner's "is the dimension we lack nameable?": does the observer math embed one level up?
- **Status now.** Closed the same day by B1104 (PROVED, NO-SECTION); the row's own heading text says "RUN TO THE END
  SAME DAY → B1104" and its body ends "CLOSED (B1104)" (OPEN_LEADS.md:1995), yet the heading lacks the mark. The 10-23 reader re-placed it:
  the missing dimension is the Milne cone's time (B1708), B1104's suspensions are its conformal compactifications, and
  the selection question becomes C10; it also found C10 is not "never computed" — B940 §6 records a Dirac kernel
  candidate of dimension 2 on m004 excluded from its seal (obligation O2). Registered as P-330 (QUEUED [LEAD]), with
  P-540 (QUEUED [DEBT], what produces B940's ± pairing — must be settled before that seal).
- **Potential.** MEDIUM — see L174; a non-zero cusped count where the closed fillings read zero would be FK14 in
  physical form.
- **First computation and cost.** Settle P-540 (is the λ ↔ −λ pairing from the orientation-reversing isometry?), then
  seal O2 with B940's instrument (~50 min per battery), data-free.
- **Disposition.** DISCHARGED (B1104); remainder already in P-330 (+ P-540). Mark the heading.

### L178 — the tone crossing (docs/OPEN_LEADS.md:1997)
- **Idea.** Read the five-tone menu {0, 1/(2φ), ½, φ/2, 1} as measured spectral invariants with the scale divided out
  (gate 1: are tones observables in any catalogued realisation?).
- **Status now.** The 10-23 reader answered gate 1 negatively by the math (L176_L177_L178.md:296–372: no Hermitian
  substrate carries the menu — every non-commuting pair of 2T/2O/2I has Fricke level < 0, a Hermitian Fibonacci chain
  has ≥ 0); its golden-vs-silver content survives only as line order (5/10 vs 8), already inside the sealed mass tests
  (B1734). The retirement was put to the owner: P-335 (OWNER, "L178 — retire by the math?"), unanswered.
- **Potential.** LOW — gate 1 fails by group theory; the tones row is consumed (B1066, B1075).
- **First computation and cost.** None (a reading); the reader's `l178_tones.py` check, seconds, if main wants it.
- **Disposition.** MERGE into P-335 (owner's call); recommend retire by the math with an addendum-beside on
  docs/EDGE_PREREG_SPEC.md §6.

### L182 — THE THREE SEAMS (docs/OPEN_LEADS.md:2033)
- **Idea.** The three crossings the chain rests on: SEAM-B (2T = the object's −I), SEAM-Y (up-Yukawa = 0 ≡ the value
  wall), SEAM-A (heterotic = the archimedean place).
- **Status now.** SEAM-B DISCHARGED (B1146 PROVED); SEAM-Y MISMATCH (B1154 PROVED); SEAM-A sharpened to a FLOOR (B1156
  OPEN) and "does not pay link A" (B1159 OPEN); ∞-place dynamics structural rhyme (B1157). In today's frame the 10-23
  reader split SEAM-A: A1 (is E₈ ⊃ E₆ × SU(3) derived?) → P-302, now DONE by B1736 (PROVED: E₈ from 2I, the family
  group the frame's own; K2 not re-derived); A2 (finite datum fixes the archimedean one) → P-312, DONE by B1733/B1734;
  A3 (Andersen–Hansen finite-phase → Vol) retire, no consumer. The towers line (docs/THE_TOWERS.md, P-414–P-416) is
  where the heterotic question now lives.
- **Potential.** LOW — every part either answered or carried by P-302/P-312/the towers.
- **First computation and cost.** None owed by this row.
- **Disposition.** SUPERSEDED (B1146, B1154, B1156/B1159; A1 → B1736 via P-302; A2 → B1733/B1734 via P-312).

### L183 — THE REPRODUCER SWEEP (docs/OPEN_LEADS.md:2063)
- **Idea.** How many arcs are banked as results with no reproducer in the tree?
- **Status now.** Run as a sweep by B1177 (OPEN instrument): 21 true no-runner-no-lock arcs. The 10-23 reader
  (L182_to_L185.md:191–243): all 21 still have no code; 25 arcs have no code at all (incl. B1075, a sealed crossing);
  GENESIS F-MC cites B992/B994 which cannot be re-run; B1177's own scanner was never committed (its reproduce.sh greps
  its own markdown). Carried as part of P-322 (QUEUED [PROCESS]); no `reproducer_debt.py` exists in scripts/checks/.
- **Potential.** LOW — hygiene; touches GENESIS (B992, B994) only.
- **First computation and cost.** Commit the scanner with a touch gate (~1 h), then B992/B994 first.
- **Disposition.** MERGE into P-322 (with L198's walk).

### L184 — THE SUITE COLLECTION LAZY-FY (docs/OPEN_LEADS.md:2078)
- **Idea.** Move module-level compute in test files into fixtures so collection takes seconds.
- **Status now.** Done for its target by B1178 (178 s → 15 s). The 10-23 reader measured a regression to 28 s, 71% in
  four modules (test_b1249, test_atlas, test_b352, test_b353), with no collection-budget guard. Carried in P-322
  ("collection 28 s → ~8 s (L184)"); no guard in tests/conftest.py.
- **Potential.** LOW — program health; collection is < 2% of suite wall time.
- **First computation and cost.** Cached-runner move on the four + a 2 s/module guard with a failing-path test; ~1 h.
- **Disposition.** DISCHARGED for its target (B1178); residue MERGE into P-322.

### L185 — THE QOR5UP UNPORTED RESIDUE (umbrella) (docs/OPEN_LEADS.md:2145)
- **Idea.** One umbrella row for B1060's 13 NOT-REACHED digest rows on the frozen qor5up record.
- **Status now.** The 10-23 reader dispositioned every row (L182_to_L185.md:295–360): ANSWERED 3.2, 3.3, 3.4, qL158,
  qL164; MERGE the rest into L183/L195–L198/L217/L252; two live residues: (i) qL155 — B162's κ < 2 "thin" check is
  vacuous (passes on sets of area 1 and 8) while GENESIS §1 cites B162 — now P-317 (c) (QUEUED [DEBT], ranked #32);
  (ii) qL159 — the flow coupling κ ≈ 0.86 (CLAIMS P15/P16, `mobius.KAPPA`) undeclared against the bridge κ = tr[a, b]:
  **no register row found** (grep of POINT_REGISTER for P15/flow coupling/qL159 empty; ERROR_LEDGER E72 lists only the
  meridian/fibre pair).
- **Potential.** LOW — bookkeeping; one GENESIS sentence (B162).
- **First computation and cost.** qL159: a one-line E72 instance #2 and a CLAIMS P15 declaration (minutes).
- **Disposition.** CLOSE the umbrella by the reader's table; qL155 → P-317 (c); qL159 needs a new row (or MERGE into
  P-322).

### L188 — THE SELECTION-COCHAIN SIX-CLAIM VERIFICATION (docs/OPEN_LEADS.md:2132)
- **Idea.** Verify cc3's B879 selection-cochain claims C1–C6 per the packet's own addendum.
- **Status now.** Done: B1199 (PROVED) GC-31 "L188 CLOSED" (frontier/B1199_register_reads_and_L188/FINDINGS.md:59) —
  C1 on all 745 classes, C3's pointwise formula holds exactly. The Review 52 currency note at the head of OPEN_LEADS
  says "L188 CLOSED (B1199)"; the row itself never got the mark. Residues: the amphichiral count is 55, not 53 (10-23
  reader R1; now inside P-318, QUEUED [DEBT] #16); the LAW_MAP "HEARING LANDSCAPE" any-word tag CONJECTURE has a
  proof sketch by the congruence property (reader, L188_to_L192.md:134–182) — **no register row found**.
- **Potential.** LOW — genesis uniqueness is untouched; the residues are corrections.
- **First computation and cost.** Re-run the 55-count with SnapPy (seconds); check the four-step proof (one sitting).
- **Disposition.** DISCHARGED (B1199 GC-31); the 55 correction is P-318; the proof sketch needs a row.

### L189 — THE GENESIS-CHAT HARVEST CANDIDATES, OWNED (docs/OPEN_LEADS.md:2158)
- **Idea.** Eight candidate-unbanked topics from the genesis-era export: (1) U_e; (2) a quasinormal-mode channel;
  (3) Verlinde k = 5..7; (4) L(1, χ₅); (5) ζ₅ irrational basepoint; (6) the two-input framing; (7) the s = 1/48 pair;
  (8) one structural item.
- **Status now.** The 10-23 reader (L188_to_L192.md:183–299): (1) MERGE into P-283 — but P-283 is now DONE by B1799
  (the neutrino self-pairing), which does not build U_e or the PMNS; no arc on main builds U_e (B1713:94 lists "the
  PMNS (no neutrino sector)" as not done); (2) MERGE into C6 (P-287); (3) RETIRE (numerology); (4) ANSWERED
  classically, idea into P-311 (DONE, B1737); (5) RETIRE (B728's theorem); (6) RETIRE (B1168, input ledger);
  (7) ANSWERED (B382/B386, B775/B778, B1199 GC-29); (8) RETIRE (classical). **None of these dispositions became a
  register row.**
- **Potential.** LOW — U_e/PMNS is outside the 19; the rest is answered or retired.
- **First computation and cost.** U_e in B1656's frame at B1726's rows, data-free, under one arc (comparison sealed).
- **Disposition.** CLOSE by the reader's table; (1) U_e needs its own LEAD row (P-283's DONE does not cover it);
  (2) MERGE into P-287.

### L190 — THE Ω-DAG'S STRUCTURED NON-GENERICITY (docs/OPEN_LEADS.md:2172)
- **Idea.** Which combinatorial law makes the Ω class-poset's reach deficit, and does it carry object content?
- **Status now.** B1188 corrected only the direction word. The 10-23 reader (L188_to_L192.md:300–322, not banked):
  not a degree effect (degree-preserving null widens it); half of it is exact trace monotonicity under positive
  row-shears (B168's arrow); SL(4) era, superseded; no consumer. No register row.
- **Potential.** LOW — superseded cone, generic cause for half the effect.
- **First computation and cost.** None recommended.
- **Disposition.** SUPERSEDED (SL(n) era; reader R4 as a dated addendum to B189 if main re-runs it).

### L191 — THE B502 FIELD-LEVEL WITNESS (docs/OPEN_LEADS.md:2183)
- **Idea.** One odd-discriminant witness kills B502's "every interaction-born field has 2 | d_K".
- **Status now.** The 10-23 reader killed it at depth 4 from B500's own fields (word FFMD, S₉ nonic, odd d_K, 2 inert;
  L188_to_L192.md:324–345); in P-334 ("L191 (B502 dead at depth 4)", QUEUED [DEBT] #63); not yet re-run or banked on
  main (no later arc mentions B502).
- **Potential.** LOW — the child programme closed at B443; no live consumer.
- **First computation and cost.** Re-run FFMD's d_K in Sage (~30 s), bank one line.
- **Disposition.** MERGE into P-334.

### L192 — THE TYPE-MATCHED QUESTION IN THE β-ODD BOX (docs/OPEN_LEADS.md:2192)
- **Idea.** Ask the object's ℤ/2 the type-matched question — does it fix whether a CP phase sits at a CP-even point —
  instead of demanding a continuous value from a bit-valued channel.
- **Status now.** The CS bit is answered on the record (B1414; P-274 DONE, B1662's addendum and I-18). The Yukawa part
  became P-323 (QUEUED [LEAD]) from the 10-23 reader's R6; since then the web seat sealed "THE STRONG ANGLE IN THE MASS
  FRAME" (harvest rows 1439, 1443; P-323's 2026-10-28 note): its H1 does not hold as sealed (power control failed);
  the phase is not harmonic on nearly all combinations, so θ̄ stays an input in the frame as built; the SM seat's W168
  reproduces it; **main's own sample check is owed**. θ̄ is now one of P-585's level-2 held-out targets ("one prior
  look, P-323"). Frame computations of the θ̄-type phase exist at: P-323's row text, audit/drafts/leads_reeval/
  L188_to_L192.md (R6 and appendix), the web seat's e20–e20d and sealed test (rows 1411, 1414, 1430, 1439, 1443), W113,
  W168, and the agy audit lane (P-585 S298, row 1539). Values not reproduced here (firewall).
- **Potential.** MEDIUM — θ̄ is one of the 19 and a held-out target of the only candidate family; but the sealed
  structural test already says the frame as built does not make it CP-even, and every further computation spends the
  held-out target.
- **First computation and cost.** Main's sample re-run of the web seat's sealed test (data-free, under one arc) —
  designed so it does not become a new look at P-585's target.
- **Disposition.** MERGE into P-323 (already the successor); route any further θ̄ work through P-585's card.

### L193 — THE CS-SILENT CHIRAL HALF OF THE FAMILY (docs/OPEN_LEADS.md:2218)
- **Idea.** What distinguishes the 38 CS-silent chiral members of the 112 from the 38 amphichiral ones — a chirality
  invariant finer than CS?
- **Status now.** The 10-23 reader (L193_L194_L195.md:84–150): on the word states CS-silence ⇔ mirror symmetry,
  1490/1490 to length 12 (R1, not banked); the 112's counterexamples come from its 1/24 lattice (B1476 P6); the finer
  invariant exists on rank-one members (B1471's twisted Alexander realness); the paper story it served is not in P9.
  In P-334 ("L193 (CS-silent ⇔ amphichiral on 1490 word states)", QUEUED [DEBT] #63).
- **Potential.** LOW — a fact of B1186's 112, not of the object.
- **First computation and cost.** Re-run R1's census on main (seconds), dated note on B1235.
- **Disposition.** MERGE into P-334.

### L194 — does a free orientation-reversing deck force CS ≡ 0 (mod ½)? (docs/OPEN_LEADS.md:2227)
- **Idea.** A free orientation-reversing involution kills the ¼ Chern–Simons class.
- **Status now.** As a census question answered: B1239 (cusp-local), B1477 (PROVED, Theorem A; THEOREM_REGISTRY
  T-QUARTER-IS-RHOMBIC, docs/THEOREM_REGISTRY.md:308, "CENSUS LAW on 1,205 manifolds; CONJECTURAL beyond; no proof").
  The 10-23 reader: the original sentence is a theorem on the one-cusped census by joining B1476 §2 and B1477
  Theorem A/P2 (not banked; P-334 "L194 (b)"); the general proof remains, restated as F = cs − Re(z)/2 ≡ 0 (mod ½);
  Meyerhoff–Ouyang still "cited, not read".
- **Potential.** LOW — a proof would make I-18's input bit proved rather than measured; it moves none of the 19.
- **First computation and cost.** Read Meyerhoff–Ouyang's cusp term against F (a reading, then under one arc).
- **Disposition.** DISCHARGED as a question (B1477); (b) MERGE into P-334; the proof obligation lives on
  T-QUARTER-IS-RHOMBIC's status cell.

### L195 — THE REVIVABLE INDEX (docs/OPEN_LEADS.md:2262)
- **Idea.** A generated, input-hashed index of every unwalked hatch and high-score revival route in the kill graph, so
  new results can be queried against the reservoir of negatives.
- **Status now.** Not built (no REVIVABLE file in docs/ or docs/views/; no script references it). The 10-23 reader: kill
  graph at 837 rows, ~214 unwalked hatches, 32 at score ≥ 4; `query.py revive` is motif-based and does not read hatches;
  the atlas status column disagrees with verdicts on 578 of 1458 probes. Carried in P-322 (QUEUED [PROCESS]).
- **Potential.** MEDIUM — it is the instrument for exactly the owner's concern today (game-changing items stored, not
  read): it turns the record's negatives' named exits into a list.
- **First computation and cost.** ~80 lines over the existing loaders + an MB12 lock (planted unwalked hatch must
  appear); minutes to an hour.
- **Disposition.** STILL OPEN (next action: build it before the next decadal review and read its top 32) — or MERGE
  into P-322 with that priority stated.

### L196 — B1–B5 have no arc_verdict.json (docs/OPEN_LEADS.md:2274)
- **Idea.** Five early arcs invisible to every verdict-reading instrument.
- **Status now.** Executed the same day (B1235 addendum): five verdicts written, B2 and B5 routed into the kill graph;
  lock `tests/test_b1235_nine_relays_read.py::test_l196_b1_b5_carry_verdicts`. The row's body says "★★ → CLOSED
  (archival)" (OPEN_LEADS.md:2286); the heading was never marked. Residues (10-23 reader): 18 digest-read arcs still
  without a verdict, `gate_arc_verdicts` blind to them, the atlas reading keywords not verdicts — all in P-322.
- **Potential.** LOW — instrument trust.
- **First computation and cost.** Widen the gate (~5 lines + planted control); author 18 verdicts (2–3 h).
- **Disposition.** DISCHARGED (B1235 addendum); residues already in P-322. Mark the heading.

### L197 — THE SUPERSESSION SWEEP + the belt's two non-recomputing families (docs/OPEN_LEADS.md:2288)
- **Idea.** (a) A generator of supersession candidates (later arcs that refute/withdraw an earlier one whose verdict
  still says superseded_by: None); (b) a lock_kind column showing which locks recompute and which pin text.
- **Status now.** (b) largely done by B1240; the soft text pins hardened in S196 (P-317 (a) DONE); the lock_kind column
  is not in docs/views/REVIEWER.md (0 hits). (a): the 10-23 reader prototyped the generator (two hits on P9-cited arcs:
  B1479←B1662, B1656←B1658); now P-319 (QUEUED [DEBT], ranked #26: "Frozen paper P9 cites B1479 and B1656, superseded
  by B1662 and B1658"). S297's finding that 20 LAW_MAP rows were stale (P-589) is the same class this generator would
  catch.
- **Potential.** MEDIUM for the record (front documents and the frozen paper's errata), LOW for physics.
- **First computation and cost.** Commit the generator (~80 lines), run on the P9- and GENESIS-cited tier (~1–2 h
  reading).
- **Disposition.** MERGE (a) into P-319 (and P-589's screen); (b)'s lock_kind column into P-322.

### L198 — SHIP THE GENERATOR: the CANNOT_RUN class at corpus scale (docs/OPEN_LEADS.md:2310)
- **Idea.** Vendor the code behind every "reproduces" whose generator is not on main; walk the CANNOT_RUN claims.
- **Status now.** Not done on any of its three parts. Count correction: CANNOT_RUN is 189 of 398 (the 139 is a partial
  digest at 304 claims), on 135 arcs; the lead text and B1240 FINDINGS:99 carry the wrong figure (10-23 reader,
  L196_L197_L198.md:185–250). The reader ran codex R020–R022 from tag `archive/codex-seat-r001@f7a49536`:
  byte-identical, so vendoring will pass; not vendored (no VENDORED_FROM.txt under B1175). Five CANNOT_RUN arcs are
  GENESIS-cited (B92, B518, B957, B993, B996). In P-322 ("CANNOT_RUN is 189 of 398 … vendor R020–R022").
- **Potential.** LOW-MEDIUM — the "clone it and run it" claim and five GENESIS citations; no physics.
- **First computation and cost.** Vendor R020–R022 with VENDORED_FROM.txt (~1 h); then the five GENESIS arcs (~1 h).
- **Disposition.** MERGE into P-322 (state the GENESIS five first); correct 139 → 189 at its four sites.

### L200 — THE DIVISOR LAW OF THE HARMONIC GENERATOR (docs/OPEN_LEADS.md:2336)
- **Idea.** Prove B1295's conjectured divisor law for the θ-odd cusp coefficients as an Eisenstein expansion on
  m004's index-12 subgroup, and identify c₀.
- **Status now.** Not proved on main. The 10-23 reader (L252_L200.md, not banked): the law is, on every mode tested,
  the Eisenstein divisor sum of the Hecke character of ℚ(√−3) of conductor 2 and type z/z̄; on primes its coefficients
  are the CM newform η(2τ)³η(6τ)³ (weight 3, level 12); B1295's PSLQ for c₀ searched the wrong domain (the correction
  is in P-318, "B1295's PSLQ domain"). No consumer: B1295's sign partition is already decided with a 13× margin; P-311
  (B1737) is a different Eisenstein object (no merge). No later arc touches it (only B1704 cites B1295 in passing).
- **Potential.** LOW — an exact object where there was a number; nothing in the completion map consumes it.
- **First computation and cost.** Check the Hecke-character identification on main with B1295's divisor_law.py
  (minutes); derive c₀ from the L-value (one arc, low priority).
- **Disposition.** RETIRE as a route (MERGE the identification into P-318's B1295 note); keep the proof as pure math
  only if a consumer appears.


# Review 74 open-leads read, part C: L201–L223 (19 leads)

Reader: fork C, 2026-11-04. Read-only on tracked files; nothing banked. Sources for every lead: its text in
docs/OPEN_LEADS.md; its 2026-10-23 reader report in audit/drafts/leads_reeval/ (reader verdicts, NOT banked; merged in
QUEUE.md lines 120–195 and 455–475); the P-rows that sweep made (P-313's children, P-314–P-335); later arcs. Two of the
2026-10-23 readers' facts were re-checked here in-sandbox (L206's identity, L211's cusp counts; stated where used); the
rest is pointers for main to verify. No data were read or compared.

---

### L201 — can a closing absorb the SU(3) cubic anomaly of the F₄ chamber's chiral faces? (docs/OPEN_LEADS.md:2358)
- **Idea.** B1296's θ-equivariant charge locus lands the Higgs on the F₄ chamber, whose chiral faces carry a non-zero
  SU(3)³ anomaly in the charge-truncated (q > 0) left-handed content; is there a closing whose extra states cancel it,
  or one frame holding both the 78- and 27-sectors at the cancelling 1 : 3?
- **Status now.** Never computed; its premise is dead. The anomaly exists only in B1296's q > 0 truncation; every frame
  that now carries chiral matter counts whole multiplets (W46 on main, B1641; B1656's three families per SM field; E₈'s
  27s), and a complete multiplet carries no SU(3)³ (audit/drafts/leads_reeval/L201_L202_L203.md §L201 (a)). The live
  anomaly is the moves' mixed one, PROVED in B1674 (verdict PROVED). Y₉'s vacua are mirror-paired, net 0 (the lead's
  own first check). The reader's narrow restatement (per-field index of a hypercharge line on X₁(N)) has no P-row.
- **Potential.** LOW — a bookkeeping artefact of a frame no longer used; the restatement has a ~10% prior and no consumer.
- **First computation and cost.** None for the lead. The restatement: whether the line's twist enters W46's bundle on
  Γ₁(N), then per-field indices at N = 5, 10 (one arc, after P-302's K2 is verified; see L222).
- **Disposition.** SUPERSEDED (B1641, B1674; reader's argument L201_L202_L203.md §L201). Mark CLOSED; the restatement
  stays in the reader's file as a PROBE LATER, unrowed.

### L202 — where a spectral cover on m004 could still be chiral (docs/OPEN_LEADS.md:2375)
- **Idea.** After B1297 made every (2+1)-reducible E₆ spectral cover on m004's cyclic tower vector-like, three sectors
  could still be chiral: (a) non-extending irreducible SL(3) reps of π₁(C_n), (b) non-cyclic covers with 3-torsion and
  partial fillings, (c) whether I ≠ 0 occurs at all on a one-cusped manifold.
- **Status now.** (b) answered: B1324 (PROVED; no sector with identities intact has I ≠ 0), B1418, B1441 (PROVED; no
  cover to degree six reaches |I| = 2), B1304/B1305 (the partial filling priced at three discrete choices). (c) answered:
  B1413 (PROVED; Menal-Ferrer–Porti vanishing on the geometric class; a non-split positive on m010) and B1418. (a) never
  computed, but its physical role is removed by B1604 (PROVED: "the dictionary cannot be earned on a thread or any cover
  of one"; GENESIS FK11 [v1.27]). The weave's chiral count now lives on W46's surface (B1641), whose unit question was
  C8, paid by B1796/B1797 (P-288 DONE).
- **Potential.** LOW — a thread-level index that B1604 shows cannot be the dictionary.
- **First computation and cost.** None owed. (a) would be a polynomial-system enumeration (days) for a number with no reading.
- **Disposition.** DISCHARGED ((b), (c): B1324, B1413, B1418, B1441) and SUPERSEDED ((a): B1604, FK11). Mark CLOSED.

### L203 — selection among the closings: Y₉'s 19 624 vacua and Y₁₂'s 34 752 lines (docs/OPEN_LEADS.md:2431)
- **Idea.** Nothing selects among the tower's SM closings; (i) enumerate the closings to n = 24, (ii) the one-triplet
  lines' μ-matrix rank (doublet–triplet), (iii) look for a quantity extremal on exactly one closing.
- **Status now.** Recast and paid in today's frame. The tower's characters are the fibre's lines fixed by (LR)ⁿ, all at
  the tick's apex Im τ = √5/2, which B1723 shows sits too low for the frame's hierarchy. (i)'s arithmetic is B1733
  (PROVED: a thread fixes an order-N line iff N divides the larger Smith invariant of A ∓ I; H₁ of the thread's double
  branched cover, B1733 FINDINGS line 17). (ii) is P-325 → B1795 (NEGATIVE: no structural doublet–triplet split on
  B1713's 266 lines plus 20 order-60 lines at three points) — but the 2-adic order-16 lines L203 added were not in
  B1795's menu (B1795 FINDINGS line 89). (iii) merged into C2 (B1722 NEGATIVE as sealed) and C6/C7 (P-287 open, P-277).
  The reader's X₀ level-2 cell (a thread preserving an order-5/10 subgroup without fixing a line) is unrowed, prior ~5%.
- **Potential.** LOW — every closing sits at one τ that is too low; the selection problem lives on in P-139/P-373.
- **First computation and cost.** If wanted: B1795's det M on the order-16 lines (minutes, same script); the X₀
  level-2 cell only inside a sealed thread-rule test.
- **Disposition.** SUPERSEDED (B1733, B1795, B1722, B1723). Mark CLOSED; the order-16 residue is a one-line note on B1795.

### L204 — the subregular point's one unpaired direction (docs/OPEN_LEADS.md:2416)
- **Idea.** At the subregular sl₂ point the outer involution and the inversion disagree on exactly one tangent
  direction (the V₁₀ of the 42); compute N(27) there, the first symmetry-unprotected chiral direction.
- **Status now.** Done. Its own status line (docs/OPEN_LEADS.md:2418) reads "CLOSED — VERIFIED on two benches":
  B1322 (PROVED) re-read the SM seat's sm:B1350 with main's Fox calculus, N(27) = 0, h¹(27) = h¹(27̄) = 0. The heading
  never got the CLOSED marker, so lead_debt.py counts it open — the L251/B1800 failure. The weave extension is moot by
  B1604.
- **Potential.** LOW — answered zero; any rerun on threads is a flat-module count B1604 forbids from carrying the index.
- **First computation and cost.** None.
- **Disposition.** DISCHARGED (B1322). Add CLOSED to the heading.

### L205 — the sibling's localized count (docs/OPEN_LEADS.md:2450)
- **Idea.** Pantev–Wijnholt's localized count on m202 and a search of the three-line class for a member keeping the
  golden face (an owner-elected bounded arc of MASTERPLAN v3's D3).
- **Status now.** The m004-centric arc ran: B1321 (PROVED; count 3 on m202, signs forced; no member keeps the golden
  face), corrected to nine members by B1414 (E81), FAIL branch standing. The 2026-10-23 reader found the weave-level
  version the record never joined: m003's companion o10_150729 (= L10n113, identified in B1491, PROVED) carries F-CI's
  three on all five ends with A₅ on the ends (B1418's census row; reader's companion3.py), the only one of 16 thread
  companions computed (L204_to_L207.md §L205). Registered as P-333 ([DEBT] Q3, rank 24 of the debts by load): a sealed
  F-CI read and a companion census to word length 10. Not run. GENESIS's F-CI sentence and FK14's v1.18 entry
  (GENESIS.md:696, F-CI read only on L8a15) stay incomplete.
- **Potential.** MEDIUM — the only weave-level selection signal for a three on record (only the root's sign partner −LR
  has a companion with F-CI's three); graded as a selection, never a count (FK14, B1604).
- **First computation and cost.** Seal, then B1492's D5 instrument on o10_150729 (minutes); then the companion census to
  word length 10 including non-cyclic torsion (one arc, data-free).
- **Disposition.** MERGE into P-333 (already carries it). Mark L205 CLOSED as a thread arc (B1321, B1414).

### L206 — does a parabolic pair generate π₁(m003)? (docs/OPEN_LEADS.md:2467)
- **Idea.** B1401's upper bound J ≤ |κ − 2| needed a parabolic generating pair on m003; three search methods failed.
- **Status now.** Answered by the 2026-10-23 reader: b = mer⁻¹a⁻¹mer⁻¹a⁻³ with mer = ABABB, so (mer, a) generates;
  (lon, a), (lon, b) refuted by an S₅ quotient (L204_to_L207.md §L206). **Re-checked here:** SnapPy gives π₁(m003) =
  ⟨a, b | abAAbabbb⟩ with peripheral (ABABB, ABAbab); mer⁻¹a⁻¹mer⁻¹a⁻³ reduces freely to bbabbbabAA, and
  b⁻¹·bbabbbabAA = babbbabAA is the relator's rotation from its fifth letter, so the identity holds exactly. B1401's
  "no meeting point at Nielsen distance ~12" is explained by two Nielsen classes (κ vs κ̄). Queued as P-334 ([DEBT] Q3)
  for a dated note on B1401; not written (no dated line after 2026-10-23 in frontier/B1401_the_kappa_lower_bound/FINDINGS.md).
- **Potential.** LOW — mathematical hygiene; nothing in the completion map uses J.
- **First computation and cost.** None; the dated note on B1401 addendum 2 (minutes).
- **Disposition.** DISCHARGED (the identity, verified here; P-334 carries the note). Mark CLOSED with the identity.

### L207 — is κ constant over all generating pairs, or only the Nielsen class? (docs/OPEN_LEADS.md:2484)
- **Idea.** J ≥ |κ − 2| needs κ constant over every generating pair, proved only on the Nielsen class.
- **Status now.** Partly answered (reader, unbanked): κ itself is not a group invariant (m003: ∓2√−3 on two classes; the
  sign of Im κ is the hand), |κ − 2| is invariant on depth-one generating pairs of every two-generator punctured-torus
  bundle (a proof sketch), depth ≥ 2 classes exist on m009 with κ unchanged where computed (L204_to_L207.md §L207).
  Queued in P-334. A by-product bears on E72 and P-221: the knot-group κ exists only on the ±LⁿR column.
- **Potential.** LOW — clean mathematics; no live consumer.
- **First computation and cost.** Re-derive the depth-one lemma; Nielsen BFS on m009's depth-2 pairs (one arc, data-free).
- **Disposition.** MERGE into P-334 (its facts) and close the lead; the depth ≥ 2 lemma stays a LEAD inside P-334.

### L211 — the stratum law (docs/OPEN_LEADS.md:2653)
- **Idea.** Does B1400's split (the SL(2,3)-quotient rate's depth decline only in 2-generator groups) survive more than
  three census slices?
- **Status now.** Retired by the 2026-10-23 reader as ill-posed, with a correction to the banked record: the strata are
  outputs of SnapPy's simplifier (36 of 68 "3-generator" manifolds get 2-generator presentations on retriangulation), and
  B1424's "full census vs one-cusped census" contrast compares two windows of one-cusped manifolds
  (L211_to_L214.md §L211 2(a)). **Re-checked here:** OrientableCuspedCensus[20000:20800] and [80000:80800] are 800/800
  one-cusped (o9_02339–o9_03138; o10_018089–o10_018888), and the one-cusped census's [80000:80800] is a disjoint, deeper
  block (o10_021213–o10_022012). The correction is listed in P-318 ([DEBT] Q3, rank 16) with B1400's addendum, B1424 §2,
  L211's banner and P3's scope note; no dated note written yet.
- **Potential.** LOW — no consumer; an integrity correction to a paper sentence.
- **First computation and cost.** None to decide; the dated notes (minutes; the reader's l211_cusps.py run is under a minute).
- **Disposition.** MERGE into P-318 (the correction) and mark L211 CLOSED (retired: instrument-defined strata).

### L212 — where does the bronze's deafness live in Minsky's coordinates? (docs/OPEN_LEADS.md:2667)
- **Idea.** The end invariant treats every metallic rung alike while the cusp field is quadratic only at m = 1, 2; is the
  cusp field a function of the end invariant?
- **Status now.** Answered by argument (reader, unbanked): the bounded probe is vacuous (Serret: the rungs' slopes have
  different continued-fraction tails, so no two share an orbit); the cusp field is a commensurability invariant, hence a
  function of the end-invariant orbit, but not of the slope's arithmetic (m = 1 and m = 4 share ℚ(√5) and differ in cusp
  field, B1403) (L211_to_L214.md §L212). Its only live consumer, cusp shapes as τ, is P-249 DONE (B1702 NEGATIVE).
- **Potential.** LOW — no consumer; Schneider makes every non-CM rung's j transcendental.
- **First computation and cost.** None; main checks the two-line argument.
- **Disposition.** DISCHARGED (the argument; P-249/B1702 for the consumer). Mark CLOSED.

### L213 — which banked results assume canonicity, and which only use SnapPy's triangulation? (docs/OPEN_LEADS.md:2689)
- **Idea.** Classify every banked use of a triangulation as canonicity-assuming or instrument-only.
- **Status now.** Partly paid: the isometry class (E81, B1414), the 3D index class (B1428, B1431, B1450), the name
  (B1690 cites Epstein–Penner; B1405, B1413 cite Lackenby). The reader pre-filtered 28 arcs whose verdict names a
  triangulation-level object (B262, B528, B96, B598, B800, B1186, B100, B524, B705, B1479 first) and found no weave-era
  exposure (L211_to_L214.md §L213). Also: L211's strata are an instance. No P-row.
- **Potential.** LOW — integrity of the pre-weave record only.
- **First computation and cost.** Read the 28 arcs (~10 min each, half a day, no compute); a dated note on B1405 (b₁ = 1
  suffices for "the word is not a label").
- **Disposition.** MERGE into P-322 ([PROCESS]) as one more item; close the lead.

### L214 — re-run the literature audits with a homonym filter (docs/OPEN_LEADS.md:2705)
- **Idea.** Audits by name report presence for homonyms and absence for results under other names; re-run them through
  B1404's filter, reading every raw line.
- **Status now.** Not run. P-322 ([PROCESS] Q3) lists "a homonym table in topic_sweep (L214)"; no HOMONYM table exists
  (no match for "homonym" in scripts/checks/topic_sweep.py or absence_sweep.py). The reader narrowed the literature half
  to about six absence claims on live surfaces (P9 §7's parameter-reduction sentence, P9 §4's chain, P3 lines 1609–1615),
  which no row names (L211_to_L214.md §L214).
- **Potential.** LOW for physics; real process value — the Seen-first sweeps have missed prior work repeatedly (B1749
  missed P-350; S289–S292 missed B1728/B1742).
- **First computation and cost.** The HOMONYM table with a planted Epstein-zeta selftest (about an hour); the six claims
  read against the literature (web reading).
- **Disposition.** MERGE into P-322 (add the six absence claims to its text); close the lead.

### L215 — the closed form of the graded trace (docs/OPEN_LEADS.md:2722)
- **Idea.** Derive the observed map m ↦ j for str(m) = tr(C·RᵐLᵐ) = 2cos(jπ/15) on SU(3)₂ data.
- **Status now.** Derived by the reader (unbanked): SU(3)₂ = Z₃ ⊠ conjugate Fibonacci, so str(m) = ε₃(m)·f₅(m), the six
  values in bijection with the squares mod 15; the mirror invariance holds for every modular tensor category; tr_odd =
  f₅ and tr_even = 2f₅·[3 ∣ m] (L215_L218_L220_L223.md §L215). **Checked here by hand:** ε₃·f₅ reproduces all 15 entries
  of the lead's own table. Queued in P-334 for a dated note on B1406; not written.
- **Potential.** LOW — B1408 closed the mirror sector; nothing consumes str.
- **First computation and cost.** Main re-derives the factorisation on B1349's exact instrument (~30 lines, minutes).
- **Disposition.** DISCHARGED once P-334's note on B1406 lands; MERGE into P-334 meanwhile. Mark CLOSED.

### L217 — the parameter budget as a design constraint (docs/OPEN_LEADS.md:2765)
- **Idea.** For each place continuous room exists (tower, rank, filling), state its count, what selects in it, and
  whether the corpus computed on it — a filter on where the programme may look.
- **Status now.** The three rows are closed in the lead's own banner (docs/OPEN_LEADS.md:2767: "L217 IS CLOSED, all
  three rows"; B1409 PROVED, LAW_MAP:248), but the heading lacks CLOSED — the L251/B1800 failure. The remaining "design
  reading", recast for today's mass frame, is the input ledger: P-328 ([LEAD] Q3, escalated 2026-10-28; the frame
  addresses at most 10 of the 19, 8 with τ fitted; five inputs unruled), whose ledger part now lives in
  docs/MAINS_PLAN.md:66 ("The ledger of inputs … Today: none removed") and the scoreboard rows (harvest 1478–1479);
  B1809 (PROVED, a census) states what four frames leave free. Still open in P-328: the web seat's J-vanishing rule on
  CP lines (verify on main), and whether it makes Im τ a licensed anchor.
- **Potential.** MEDIUM — the ceiling (10 of 19) bounds every future claim from the frame, and P-328's CP-line rule is
  the one route on record to a licensed continuous anchor.
- **First computation and cost.** Verify e20c's J-vanishing on the (2/5, k/10) lines at half-integer Re τ on main
  (data-free, minutes); write the ceiling with its reasons into MAINS_PLAN.
- **Disposition.** DISCHARGED (B1409; MAINS_PLAN's ledger; B1809) with the remainder in P-328. Mark CLOSED.

### L218 — the index channel: build the contact row out of something discrete (docs/OPEN_LEADS.md:2788)
- **Idea.** At reachable precision only integers discriminate (B1408); enumerate the object's integer invariants, ask
  of each "anchor-free?" and "of a measured kind?", and build the next contact row from survivors.
- **Status now.** (a) The enumeration was drafted only in the reader's file (L215_L218_L220_L223.md §L218 table): the one
  integer of a measured kind with a mechanism is the chiral three = n(|Λ₊| − 3), anchored by n. Its anchor was C8 →
  P-288 DONE: B1796 (W123's exact route verified) and B1797 (GENESIS v1.59: FK10's unit reduced to the field's existence
  FK15, a type identification, uniform end data and the least remainder, "given Λ and the hand, none derived"). So the
  integer is conditional, not anchor-free. (b) B1408's universal "only discrete observables can discriminate" is refuted
  by joint readings (B1726); the sharpen note is in P-318, unwritten. The ledger was never written to a tracked surface.
- **Potential.** MEDIUM — the generations' index is the only integer output of a measured kind; making it anchor-free is
  FK15 plus the end datum (and the W134 tension, see L222).
- **First computation and cost.** Write the integer ledger (no compute) as a completion-map note; then the P-156
  premises (end condition, dim Λ₊ − 3, the M₁,₂ identification) verified on main (one arc).
- **Disposition.** MERGE into P-318 (the B1408 note) and P-156 (the index's premises); close the lead.

### L219 — what selects a point in the tower's room? (docs/OPEN_LEADS.md:2816)
- **Idea.** B1409's 20 real parameters are all boundary data with no selector; exhibit a principle that selects cusp data
  or price the selection.
- **Status now.** As posed, answered: B1410 reframed it ("nothing selects a departure" from the Mostow-canonical
  ρ_geo); the reader adds that Menal-Ferrer–Porti 2012 (arXiv:1111.4338; read at abstract level only, main must read the
  statement) make ρ_geo's lift isolated among boundary-unipotent representations, so the frame's own boundary condition
  (the run of B1444–B1447 noted in the lead) returns the origin in the tower's room (L219_L253.md §L219 (d)). The tower's
  room is in no current frame. The live question it names — what selects τ and the line — is B1733 (PROVED: a thread
  fixes τ at its apex and its line up to one real bit), B1734 (P-312 DONE), B1720/B1722/B1723 (NEGATIVE), and the open
  rows P-139 (FK9), P-287 (C6), P-373 (what fixes Im τ ≈ 3.03), P-437, P-465, P-468.
- **Potential.** MEDIUM — the question is the programme's top open one (τ not selected), but this lead's room is retired
  and its merge targets already carry it; the one idea worth carrying is a boundary condition as a selector.
- **First computation and cost.** None of its own; P-373's "a principle for Im τ stated before its check" is the live form.
- **Disposition.** DISCHARGED as posed (B1410; Menal-Ferrer–Porti, citation to be read by main); MERGE the selection
  question into P-139.

### L220 — finish the open-claim sweep's adjudication (docs/OPEN_LEADS.md:2859)
- **Idea.** Adjudicate the open-claim sweep's openness-asserting candidates one read per row.
- **Status now.** Done on 2026-09-14 in its own body: "12 of 12 adjudicated: 5 stale, 7 accurate" and "The lead, CLOSED"
  (docs/OPEN_LEADS.md:2933); R57-3 is [x] (docs/progress/REVIEWS.md:5508). The heading lacks CLOSED and the Review 58
  ESCALATED note (docs/OPEN_LEADS.md:2938, "ten candidates … remain unadjudicated") re-carried stale task text — the
  lead's own error class. The reader's re-run (74 candidates) found three new stale rows (L122, B1130's verdict file,
  GRAND_COMPUTATION_LEDGER D2) and two instrument gaps still unpaid: the review-cadence run was never wired into
  REVIEW_TEMPLATE.md, and SURFACES (scripts/checks/open_claim_sweep.py:36–46) lacks GENESIS.md, POINT_REGISTER,
  THE_COMPLETION_MAP and THE_WEAVE.
- **Potential.** LOW — bookkeeping; but this instrument finds exactly the unpropagated-closure class this review is chasing.
- **First computation and cost.** Add the four surfaces and a template step (under an hour).
- **Disposition.** DISCHARGED (its body, R57-3). Mark CLOSED; MERGE the two instrument gaps and three stale rows into P-322.

### L221 — the 27̄ sector and the seesaw (docs/OPEN_LEADS.md:2945)
- **Idea.** The Y₃ line's U(1)′ is the η direction; both E₆-charged singlets share its charge, forbidding a Majorana mass
  (no seesaw) in the three-apex design; remedy: a 27̄ sector whose pairing spectrum sets a Majorana scale.
- **Status now.** (a) the charges are root-system theorems (B1415, B1418 cell 4); (b), (c) retired by the reader: the E₆
  frame is refuted for the SM on main (B1652, PROVED) and no instrument for the pairing spectrum exists
  (L222_L221.md §L221). The reader's restatement (d), does ν^c (required by B1674) admit a Majorana mass in B1656's frame
  — scratch: only at odd weights; in one hand the weight-3 form is unique up to scale — is P-326 ([LEAD] Q3), unrun.
  B1799 (PROVED, P-283) computed the self-pairings' det M at the canonical end, not P-326's form (the lead's own S232
  note, docs/OPEN_LEADS.md:2950). (e), the 351′ note (E₈'s adjoint has no 351′; the Clebsch-−3 and ν^c's mass would sit
  in one field outside the record's E₈ frames), reached P-294.
- **Potential.** MEDIUM — P-326 is a cheap structural consistency test of the frame (no admissible form would force Dirac
  neutrinos); the 351′ reading names the one missing field that bears on the lepton–down relation D (P-294, P-355).
- **First computation and cost.** P-326's existence-and-weight cell on main (minutes, data-free); the seesaw's cusp
  exponents at B1667's end later (under one arc; any oscillation comparison sealed).
- **Disposition.** MERGE into P-326 (the Majorana form) and P-294 (already carries the 351′ note); close the lead.

### L222 — the family as the object (docs/OPEN_LEADS.md:2952)
- **Idea.** The chirality index fires on members of m004's commensurability class and its covers, not on m004; (i) the
  firing rule, (ii) admissibility of non-semisimple modules, (iii) the unrun modules, (iv) whether the class is the object.
- **Status now.** All four answered: (i) B1438 (the slope rule) and B1432; (ii) B1444 and B1604 (PROVED: the index lives
  only at the reducible end); (iii) B1470 (NEGATIVE, docs/OPEN_LEADS.md:2960), B1441; (iv) ruled by GENESIS FK13 [v1.13]
  (GENESIS.md:446: the family is the word states the principle generates), so the escalation to the owner is stale. Its
  thesis lives on as "the weave carries the three where no thread does" (B1600, B1604, B1641, B1700; C8 → B1796/B1797).
  **Unrowed residue:** the reader's tension between C8's whole unit (n = 1) and W134's "three chiral 27s need 17/24 of the
  cusp unit or more, never the empty end or the whole unit" (P-302's text). P-302 is DONE by B1736, but B1736 (FINDINGS
  line 33) and P-302's DONE cell say "K2 (the 27's anomaly) not re-derived", and harvest row 1314 still reads "to verify
  on main"; B1796/B1797 and GENESIS never mention W134. So W134's admissibility (m ≡ 5 − r mod 8, m odd) and its 17/24
  threshold sit unverified with their row closed.
- **Potential.** MEDIUM — the lead is answered; the residue bears directly on "three generations only by selection":
  either the family slot or the whole-unit route must give.
- **First computation and cost.** K2 and E2 from B1674's det ρ = χ_η⁹ (the reader's two-line derivation; minutes); W134's
  twelve |I| = 3 data from B1641's χ formula at weights 3/2 + m/2 (exact algebra, under an hour).
- **Disposition.** DISCHARGED (B1438, B1444, B1470, B1441, FK13). Register the W134 residue as a new [DEBT] row (or reopen
  P-302's K2).

### L223 — the level mismatch, harvested (docs/OPEN_LEADS.md:2940)
- **Idea.** Three chiral 27s exist only on Y₃ while the SM lines lived on Y₉, Y₁₂; the SM seat resolved it with a Q₈ ⊂
  SU(2)_β line on Y₃ and owed the 5 + 5̄ masses, the doublet–triplet splitting and the closing's existence.
- **Status now.** (i) dissolved: the three is ρ_T's weight-3/2 space with one unit (B1700, B1641), not a deck orbit;
  (ii) answered (B1415, B1444, B1446: the quaternion point); (iii) the doublet–triplet splitting is P-325 → B1795
  (NEGATIVE: the frame does not solve SU(5)'s doublet–triplet problem as typed); (iv) the closing's existence has no frame
  on main (L215_L218_L220_L223.md §L223).
- **Potential.** LOW — its live content was the doublet–triplet split, now a banked negative.
- **First computation and cost.** None.
- **Disposition.** SUPERSEDED (B1700, B1795; B1415/B1444/B1446). Mark CLOSED; the SM seat may close sm:L214 on its lane.


# Part D — L229 to L250 (main's own read; the fork for this block could not start)

Sources for every entry: the lead's text in docs/OPEN_LEADS.md; the 2026-10-23 reader report in
audit/drafts/leads_reeval/ (a reader's verdict, not banked); the register rows the sweep made (P-309, docs/POINT_REGISTER.md
line 457, is the umbrella for L229 and L233–L237; P-313 line 461 for the rest); later arcs by number. Every arc cited
below exists on main (checked by directory and arc_verdict.json).

### L229 — the architecture census's residue (docs/OPEN_LEADS.md:3002)
- **Idea.** Five questions left by the slope-frame census: which word states carry a generation at their own level and by
  what criterion (i); why two three-fold levels are silent (ii); whether the backgrounds survive in a frame built from a
  state's own arithmetic (iii); what singles out a state (iv); the Gieseking parent, non-cyclic covers, fillings (v).
- **Status now.** (i) data without a law (B1439: 95 of 758); (ii)–(iii), (v) answered or retired by the 2026-10-23 reader
  (audit/drafts/leads_reeval/L229.md:206–212) and adopted as such in P-309 (POINT_REGISTER.md:457). (iv) was turned into
  P-312 (POINT_REGISTER.md:460) and paid: B1733 (PROVED, the thread fixes an order-5 line iff its trace is ±2 mod 5) and
  B1734 (sealed, the thread rule with the two ingredients). What stays open of (iv) — "what selects" — is FK9 / P-139, not
  this lead. **The heading was never marked** (the L251 failure mode).
- **Potential.** LOW — the live residue is P-139 (selection), carried elsewhere; the slope-frame items are retired.
- **First computation and cost.** None owed here.
- **Disposition.** DISCHARGED (P-309 row 457; P-312 row 460 → B1733, B1734; residue in P-139).

### L231 — what the sweep of 2026-10-01 found buried or stale (docs/OPEN_LEADS.md:3051)
- **Idea.** A list of unharvested windows, buried results and stale sentences to pay as rows.
- **Status now.** Windows harvested (B1453, B1457, B1690; Review 70 note in the lead). Every remaining item has a row:
  B723, C-cal, paths/PATHS.md → P-427 (QUEUED [DEBT], POINT_REGISTER.md:575); B1137's PSLQ insensitivity → P-317 (b)
  ([DEBT], ranked #32); B1182 → P-318 (#16); B940's kernel → P-330 ([LEAD]). P-427's own text says "L231's other three
  are P-317 (b), P-318 and P-330". Not rowed: the withdrawn "16σ" phrase on living surfaces (the reader counted at least 13
  lines on 10 surfaces) and the inconsistent count of sealed crossings — both sit inside P-426's documents only in part.
- **Potential.** LOW — record hygiene; the B1137 item matters for the honesty of "the value door is closed" but is P-317's.
- **First computation and cost.** None; a grep for "16σ" over living docs (minutes).
- **Disposition.** MERGE into P-427 (with P-317 (b), P-318, P-330); add the "16σ" phrase and the crossing count to P-426.

### L232 — five living documents owed a read (docs/OPEN_LEADS.md:3071)
- **Idea.** COMPUTE_THE_PROGRAM, THE_FRAMEWORK, THE_LADDER, THE_SM_VERDICT and WORKING_RULES lag the record.
- **Status now.** Moved whole into P-426 (QUEUED [DEBT], ranked #27, POINT_REGISTER.md:574) by Review 72; P-417 holds the
  general currency machinery; COMPUTE_THE_PROGRAM waits on the owner (P-335).
- **Potential.** LOW — documents.
- **First computation and cost.** One read per document; hours each.
- **Disposition.** MERGE into P-426 (already carried there in full).

### L233 — the slope: what it is and what it does not yet say (docs/OPEN_LEADS.md:3086)
- **Idea.** Six questions about the slope s(χ): couplings between backgrounds (a), its arithmetic (b), one groupoid object
  (c), fillings (d), E₆'s Clebsch constants (e), larger modules (f).
- **Status now.** (a), (f) closed the same day (B1438 Theorem E; B1440). (b) answered on main by **B1737** (PROVED: the
  slope is the χ-twisted Shintani zeta value at s = 0; P-311 DONE, POINT_REGISTER.md:459; the lead carries the dated
  note). (c) "answered pending (b)" — B1737 §3 says writing the cocycle out in full is owed. (d) retired (B1604);
  (e) folded into P-294. **Buried follow-on:** B1737 §4 registers "whether B1656's channel norms c_s are Kronecker-limit
  logs of the same L-function per (thread, line) … a candidate rule for the line" — computed nowhere (no later FINDINGS
  mentions Kronecker) and it has **no register row** of its own; P-311 is DONE.
- **Potential.** MEDIUM — the follow-on is a data-free candidate rule for the line, and the line is the strip candidate's
  weakest input (P-384, debt #2: "mostly a pick"); against it, B1800 already writes the flux-frame couplings as theta
  functions with characteristics, so the identity may be classical and select nothing.
- **First computation and cost.** Test c_s against −2π ln|θ[v](0)|² plus a τ-only term on B1656's instrument at a few
  (thread, line) points; data-free, about an hour.
- **Disposition.** DISCHARGED for (a)–(f) (B1438, B1440, B1737, P-309); register B1737 §4's follow-on as a new [LEAD] row.

### L234 — three in one background: the several-cusped search (docs/OPEN_LEADS.md:3123)
- **Idea.** Whether rank-two backgrounds count three on manifolds with several cusps.
- **Status now.** (a) closed NEGATIVE (B1442); (e) answered (orbifold against smooth count, B1496/B1490); (b)–(d) retired by
  the reader (audit/drafts/leads_reeval/L234.md:178–195) and adopted in P-309. The reader's carrying probe, C8/P-288
  (W123: the weight-3/2 Higgs space is 3n), is DONE.
- **Potential.** LOW — a class-index-frame question; B1604 demoted that index.
- **First computation and cost.** None.
- **Disposition.** DISCHARGED (P-309; B1442; P-288 DONE).

### L235 — what fixes the Higgs values (docs/OPEN_LEADS.md:3144)
- **Idea.** In the slope frame a mass pattern is the pattern of an orbit's Higgs classes; what invariant fixes them.
- **Status now.** (a) closed (B1444: the cubic has no group to live in); (b) merged into P-294; (c) answered conditional on
  P-303; (d) dissolved into H-cov (audit/drafts/leads_reeval/L235_L236.md:45–60; P-309). The question itself is alive in
  today's frame as **the Higgs's construction**: B1739 (the Higgs is nearly null), B1826, B1827 (the CKM wall is a choice in
  how the Higgs is built; FRAMING_LEDGER FL-06), P-566 (the sector-odd singlet), P-555.
- **Potential.** MEDIUM — the question is the live CKM wall, but this lead's own form is the slope frame's.
- **First computation and cost.** Carried by P-566's data-free cell (one definition, then the corner order).
- **Disposition.** SUPERSEDED by P-566 / P-555 / P-303 (the Higgs construction in B1656's frame).

### L236 — what the periodic curve leaves open (docs/OPEN_LEADS.md:3169)
- **Idea.** Second-order coefficients, the Higgs character's direction, P4, the complete-cusp point, what selects a point.
- **Status now.** (b) B1445; (d) withdrawn; (g) answered (B1444 §9); (a), (c) retired; (f) merged into the completion
  map's selection items (C1–C7, P-139); (e) answered only in the audit room (complex volume Vol(4₁) with CS π²/30 mod π²/6,
  audit/drafts/leads_reeval/L235_L236.md:39–42), **never banked** (no FINDINGS carries it).
- **Potential.** LOW — slope-frame items; (f) lives in P-139.
- **First computation and cost.** Bank (e) with SnapPy (minutes) if wanted.
- **Disposition.** DISCHARGED (P-309; B1444, B1445); (e) to a one-line [LEAD] or retire.

### L237 — what tells the members of an orbit apart (docs/OPEN_LEADS.md:3198)
- **Idea.** The branch off one member's Higgs curve and its parabolic points.
- **Status now.** (a) B1447 and its addendum; (b) answered by **B1736** (P-302 DONE; the lead carries the dated note);
  (c), (d), (f), (g) retired, (e) run on sixteen levels (B1451), remainder retired (audit/drafts/leads_reeval/L237.md:18–29).
- **Potential.** LOW.
- **First computation and cost.** None.
- **Disposition.** DISCHARGED (B1447, B1451, B1736; P-302, P-309).

### L239 — the SM seat's "for main" items not settled on main (docs/OPEN_LEADS.md:3249)
- **Idea.** Seven seat statements main had not verified (the puncture from the carrier, Pin⁺/Kramers, the
  generated-state-space theorems, paper wording, a search under-count, reader notes, unrun scripts).
- **Status now.** (a) is P-321 ([DEBT], ranked #22: GM4 derived, GENESIS owes the update); (c)'s two theorems are open in
  P-428 ([PROCESS], POINT_REGISTER.md:576); (b) Pin⁺ answered (B1476 P4/P5), Kramers later; (d), (f) retired (paper frozen);
  (e) later; (g) partly answered (sm:B1374/B1375 verified by B1427). No live dependent (Review 70's note in the lead).
- **Potential.** LOW — foundation currency.
- **First computation and cost.** P-321's GENESIS amendment (hours).
- **Disposition.** MERGE into P-321 (a) and P-428 (c); the rest closed as the seat's, unverified, no dependent.

### L240 — the foundation lock's remainder (docs/OPEN_LEADS.md:3284)
- **Idea.** Scope tags on old negatives (a), THE_CLAIM restated (c), F-MC off the root (d), the forks FK2/FK3/FK5 (e),
  R58 (f), Stage 6's swept page (g), the fresh-reader test of the whole (h), FK1 (i).
- **Status now.** (b) paid (B1458). (c) → P-092 ([DEBT] #25). (d), (e) → P-320 ([DEBT] #21). (f) proposed ANSWERED in
  P-428. (i) answered at B1460 ("FK1 confirmed as written", L241's refinement 4). (a) is a standing campaign that
  overlaps P-589 (the member-scope addenda). **(g) and (h) have no row**; (h) — a fresh reader with only GENESIS and
  the README against sealed questions — has never run; B1827's blind outside reading (A5) is adjacent but is not that
  test.
- **Potential.** LOW for the 19; (h) bears on the owner's recognition question (B1827 § G).
- **First computation and cost.** (h): one agent session plus a seal.
- **Disposition.** MERGE into P-092, P-320, P-428; register (g)+(h) as one [PROCESS] row.

### L241 — the measurer question (docs/OPEN_LEADS.md:3309)
- **Idea.** The owner's standing question: the derivation keeps dropping the measurer that tracks a → ab, b → a; the
  working translation is the *marking* — base point, letter order, orientation, and **which of a module and its dual is
  read as the particle**. Not to be closed by a negative on one object.
- **Status now.** Standing at the owner's word. The 2026-10-23 reader located the fourth marking exactly in today's
  frame: **the reading** — which sector sees h and which h̄ (S or S̃ = εS*εᵀ; audit/drafts/leads_reeval/L244_L241.md:55–69;
  P-295). One route to force it is closed: B1744 (NEGATIVE; P-324 DONE) — the Higgs's own twist is even. **Today it is the
  hinge of the CKM wall:** B1827 (FINDINGS lines 61–86) finds the reading that lifts the corners is the **adjugate**,
  adj(S) = εSᵀεᵀ (the dual read holomorphically), and on order-5 lines that reading is the frame's own down–lepton
  relation (P-583); P-566 asks what makes the singlet sector-odd. The rising-factor angle is P-475 ([LEAD]).
- **Potential.** HIGH — the binary the record now needs (which sector reads the dual) is this lead's marking; a rule that
  forces it would turn a free choice under the CKM wall into a consequence.
- **First computation and cost.** P-583's data-free cell (the corner order and the first row's size on order-5 lines
  under up S, down adj S), then the forcing question: is the per-sector reading fixed by any object datum (the
  orientation sheet, the record swap, the twist's sign)? Data-free, one arc.
- **Disposition.** STILL OPEN (standing). Next action: add a dated note joining L241 (b)/(the reading) to P-295, P-566,
  P-583 and B1827; work P-583 first.

### L242 — do the three lines account for the zeros on the record (docs/OPEN_LEADS.md:3384)
- **Idea.** Whether B1455's self-duality criterion explains every class-index zero.
- **Status now.** (a) 188 points, (b), (c), (e) paid (B1459, B1462, B1465). Open: B1447's sixteen non-self-dual zeros and
  (d) m202's "12 up to Aut" — both proposed RETIRED in P-428 (B1604 demotes the class index). The live descendant is the
  frame's zero law, P-337 ([LEAD]): the web seat's kernels note of 2026-11-03 claims it derived; **not yet verified on
  main** (P-337's S298 line).
- **Potential.** MEDIUM — the zero law is a structural theorem about which lines protect a generation in B1656's frame and
  touches P-559 (B1788's exponents); the lead's own items are class-index bookkeeping.
- **First computation and cost.** Verify the web seat's zero-law derivation on main with B1716's instrument (under one arc).
- **Disposition.** MERGE into P-337 (live) and P-428 (retire the two counts).

### L243 — from the seats, not yet checked on main (docs/OPEN_LEADS.md:3432)
- **Idea.** Seven seat items (two early corrections, the bar, R79, the boundary table, R69, a law re-audit, a question).
- **Status now.** (a), (b), (g) paid (B1463, B1458). (d) proposed RETIRED as a route to three (P-428); (e) answered by B1440
  (reader); (c) R79 open in P-428; (f) answered (no status change on main).
- **Potential.** LOW.
- **First computation and cost.** Main's own read of R79 (an hour).
- **Disposition.** MERGE into P-428.

### L244 — the symmetric-phase reading (docs/OPEN_LEADS.md:3476)
- **Idea.** The owner's "treat it seriously": the programme as a theory of the symmetric phase and the SM a broken phase;
  three kinds of negative; β_c = 2 log φ as a Hagedorn point.
- **Status now.** (a) census done (B1473: the three kinds cover a third at most); (b) GAP6 named and narrowed (v1.9,
  v1.11–v1.12); (c) β_c verified; the critical line set beside it (P-441 DONE, delegated to the web seat); (d) B1466.
  Live descendants, all [LEAD]: P-465 (the principle as the selection: the golden path as the ground path, a world's
  hierarchies as departures), P-468 (picked in combination), P-475 (τ's one-loop potential as the rising factor). Reader:
  neither of the record's thread measures is normalisable (audit/drafts/leads_reeval/L244_L241.md:51–55; not banked).
- **Potential.** MEDIUM — it is the record's one structured idea for selecting τ (the strip), but B1722 and B1813 show the
  measures alone do not select, and form 4 of P-468 closed negative.
- **First computation and cost.** P-475: B1704's potential set against the thread measure (data-free, hours), any
  predicted height sealed.
- **Disposition.** STILL OPEN (standing at the owner's word). Next action: a dated note naming P-465, P-468, P-475 as its
  live cells.

### L245 — the sep16 lane's claims about main (docs/OPEN_LEADS.md:3519)
- **Idea.** Verify 31 frozen-lane arcs' statements about main's record.
- **Status now.** Reader: answered for 25 of 26 claims (B1469–B1472 and later; audit/drafts/leads_reeval/L240_L245_L247.md:241–330).
  Residue: xB014 — a scope note owed on B207 (not rowed: grep of the register for xB014/B207 is empty); (z) already_banked.py
  does not read the paper (in P-322); two rule proposals (the owner's).
- **Potential.** LOW.
- **First computation and cost.** One dated note on B207; the paper added to already_banked's corpus (15 minutes).
- **Disposition.** DISCHARGED except the B207 note → add to P-318's list; (z) in P-322.

### L246 — the spin swap: an execution plan (docs/OPEN_LEADS.md:3647)
- **Idea.** The owner-approved plan: does the orientation act non-trivially on the fermionic bit on family members A5
  excluded?
- **Status now.** Phase 1 paid (B1474, B1475, B1476, B1477: Theorem A, the ¼ law on 75 one-cusped members); the bit is the
  word state's sign (B1479); Phase 2's first cell paid (B1481, the hand is a phase). Remainder: phase → spectral asymmetry
  (C10, P-289) and the reading arc against B1477–B1483 (P-035, [LEAD]); Phase 3 retired by the reader (no route to the weave's
  count). In today's frame the four channels are the fibre's spin structures and the swap is P-337's zero-law cell
  (audit/drafts/leads_reeval/L242_L246.md:1–12). The lead also served as the running log to Review 63 (spent).
- **Potential.** LOW — the hand is a convention on the weave (B1610, B1640); its live parts are P-337 and C10.
- **First computation and cost.** None here.
- **Disposition.** SUPERSEDED (B1474–B1481; remainder in P-035, P-289, P-337).

### L247 — the wall is the frame, and the wall was a member's (docs/OPEN_LEADS.md:3770)
- **Idea.** The value negatives are theorems about flat frames (and about m004), not about physics.
- **Status now.** Absorbed into GENESIS (GAP6 v1.11–v1.12, FK13, B1610). **Not done:** the scope addenda on the twelve
  flat-premise continuous-value kills and on the 39 member-scope kills; the member-scope gate's baseline is still 8
  (scripts/gates/gates.py:1601, frozen 2026-10-04); no member-scope column in docs/views/CLOSED_DOORS.md. These are now
  P-571 ([DEBT] #62, FL-02/FL-03: 107 of 173 value-kills on flat premises) and P-589 ([DEBT] #15: "owed the eight
  member-scope addenda"). (f) merged into L248 §8.
- **Potential.** LOW — the reading has already changed the direction (B1827's framing ledger); what remains is bookkeeping.
- **First computation and cost.** The eight addenda (hours).
- **Disposition.** MERGE into P-571 and P-589.

### L248 — the arithmetic atom (docs/OPEN_LEADS.md:3785)
- **Idea.** The web seat's Kashaev series, CS ∈ (1/24)ℤ on the family, the Rogers atom.
- **Status now.** Every computed item answered on main (B598, B722, B1476 P6 and C2). Only §8 (the atom through the 3D
  index's asymptotics across the family) remains, and P-335 (OWNER, POINT_REGISTER.md:483) asks the owner "retire, or the
  L240 reader's probe later". Reader: the strip fit lives at the prime 5, not the atom's 3
  (audit/drafts/leads_reeval/L248_L249.md:7–25).
- **Potential.** LOW.
- **First computation and cost.** None until the owner rules.
- **Disposition.** MERGE into P-335 (the owner's call); otherwise DISCHARGED.

### L249 — the register at the door (docs/OPEN_LEADS.md:3797)
- **Idea.** Six cells the web seat left: m000's odd levels, the metallic base rate, the deck's role, a frame of the right
  parity, FK13, B1166's scalings.
- **Status now.** Moved whole into P-429 ([PROCESS], POINT_REGISTER.md:577) with the reader's dispositions to confirm:
  (a) B1607, (b) mod 5 via B1733, (c) into P-312/FK12, (d) into C10/P-403, (e) GENESIS v1.13, (f) B1708.
- **Potential.** LOW.
- **First computation and cost.** Confirm the six pointers (an hour).
- **Disposition.** MERGE into P-429.

### L250 — the frame of the right parity (docs/OPEN_LEADS.md:3813)
- **Idea.** The chirality count and the gauge-coupling gap need matter counted by an index on a bulk of dimension ≡ 2
  mod 4 with a non-flat bundle; candidate: the frame bundle Γ\PSL(2,ℂ); hypothesis: on a − state no mirror pairs a bundle
  with its conjugate, so a net index is allowed.
- **Status now.** Cells (a), (c) B1483; the gate stated B1484. (ii), the doublet–triplet split, NEGATIVE (B1795; P-325
  DONE). (b) on the + control and the closed members NEGATIVE (B1794: no rational hypercharge class on any closed frame;
  P-401 DONE). The couplings as flux-mode overlaps B1800. Live: **P-403** ([LEAD], the sealed flux design), **P-458**
  ([LEAD], the spin connection ω = Re A as the object's canonical non-flat SU(2) background — untried), C10 (P-289). The
  hypothesis on a − state (m003's X̃_s) is not killed; cell (d), the literature read on the bench, still owed.
- **Potential.** MEDIUM — the record's only named route to a count with curvature; against it, B1794 (rationally no
  classes on closed frames), P-401's caution (fluxes trade inputs for integers), B1795 (the gauge half).
- **First computation and cost.** P-458: the twisted Dirac spectrum coupled to ω on m004 against m003, both spin
  structures, with B940's instrument (about 50 minutes a run) — after P-540 settles that instrument's ± check.
- **Disposition.** STILL OPEN as P-403 / P-458 (next action: P-458's cell after P-540).

