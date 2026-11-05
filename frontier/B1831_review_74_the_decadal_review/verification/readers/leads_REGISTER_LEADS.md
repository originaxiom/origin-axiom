# REVIEW 74 — THE OPEN LEADS READ (the register's [LEAD] rows)

*A reader's report for the decadal review, 2026-11-04. Report only: no tracked file edited, nothing committed. Main
verifies every pointer before any row moves.*

**Scope.** `docs/POINT_REGISTER.md`'s open rows whose disposition is QUEUED, LEAD or OWNER and whose *where* cell
starts with `[LEAD]`: **142 rows** (132 QUEUED, 10 LEAD, 0 OWNER), extracted mechanically from the register as it
stands on main's working tree this morning. The rule served: "Leads do not age; they are an index, read at the decadal
reviews." The owner's concern, served alongside it, is that open leads "could contain game-changing leads".

**Method.** Six readers each took about 24 rows in ID order. For each row they swept the record: the row's P-number
across FINDINGS, arc_verdict, addenda, LAW_MAP, OPEN_LEADS, the register, CAMPAIGN_STATUS, GENESIS and the ledgers (a
mechanical cross-reference index), its L-number, its key terms (`scripts/checks/topic_sweep.py`, `--full` where it
mattered), and the seats' branches where a row names seat work. The index of all 142 rows is Part III; the per-row blocks are Part IV, in ID order. The
assembling reader then (i) re-checked at source every pointer behind a proposed ANSWERED, DEBT or retype closure that
§D marks **V**, (ii) adjudicated the cross-chunk merges, and (iii) overrode one closure (P-032: B1723's check is more
numerics, not a proof; it stays a low lead). Pointers marked **R** are the row reader's and were not re-opened by the
assembler.

**Firewall.** No value, sign or bound computed by any seat or model for y_b/y_t (m_b/m_t), θ̄ or y_τ/y_b appears
here. Where such a computation exists, the report says only where: the register's own rows P-323 and P-569 and HARVEST
rows 1411 and 1414 (θ̄ at B1726's best six-row); the agy audit lane's unsealed computation of the two held-out targets
(HARVEST row 1539; `docs/LOOK_LEDGER.md:120`, counted as a prior look); the web seat's post-pin relay 8ed19bbd4 (the
strong angle's counterterm rule). Nothing is compared with measured data. Record comparisons that already exist (χ²
values, D's tension) are quoted as the record states them.

---

## PART I — THE VERDICT ON THE INDEX

### (a) Totals by proposed disposition

| disposition | rows | meaning |
|---|---|---|
| **STILL A LEAD** (its own row) | **57** | the idea is live and not carried elsewhere; 6 of these are low-potential decline candidates (P-032, P-257, P-279, P-405, P-491, P-493) |
| **MERGE** (fold into a named host row) | **41** | the idea survives in the host; the row closes as merged (§C lists the hosts) |
| **ANSWERED** (close DONE) | **22** | the work was done after the row was written and the row was left open (§D) |
| **SUPERSEDED** (close, naming the successor) | **17** | the question moved on: refuted, closed by a later arc, or re-posed as another row (§D) |
| **SHOULD BE A DEBT** | **2** | P-418 (into debt P-579) and P-476 (conditional on a minutes-long check) |
| **RETYPE [PROCESS]** | **2** | P-063 (a seat result to re-run), P-574 (host of one bar amendment) |
| **DECLINE** | **1** | P-039 (its own escalation offers "or decline then") |
| total | **142** | |

After the proposed closures and merges, **57 leads remain as their own rows**, about 25 of them hosts that carry
the merged rows. That is an index a review can actually read. **39 rows (22 answered + 17
superseded) are stale**: the work exists on the record and the row never moved. That is the failure mode the brief
named (L251/B1800 is the first of them, P-020), and it is the largest single finding of this reading.

### (b) THE TOP TEN LEADS, by potential

Ranked by how much the programme would change if the lead worked, given today's state: 0 of 19; THE SIX ON THE STRIP
a level-1 candidate on a groundless end formula and about 3σ off D; the quark mixing blocked by the Higgs construction;
τ not selected; three only by selection.

**1. P-566 with P-591's RI-1 — an object-forced sector-odd singlet (the CKM corners).**
*The idea.* A singlet Higgs component of natural size, *odd* between up and down, lifts the CKM corner inversion
generically, where an even one does nothing (B1827 § D; `docs/FRAMING_LEDGER.md:60–65`). S291 found that the
adjugate reading is exactly that odd family (B1827 FINDINGS:78–80). RI-1 (P-591; the SM seat's retrieval sweep, HARVEST
row 1543) points at a candidate: the kernel's signed Laurent constant a₀, with a₀(up) = −a₀(down) = −a₀(lepton). B1656
uses only |a₀|², so the sign is unused, and three seats point at it independently (the SM seat, the web seat's kernels
note § 5, the agy lane's Theorem 15 Result 3).
*Why it could change direction.* The wall behind B1825's "never together" is the Higgs construction (B1739/B1826:
one Higgs near the null cone drags both sectors' light states). An oddness the object already carries, at zero free
numbers, would remove the main obstacle to the mixing inside the frame the record already has.
*First computation.* On main's own kernel code, verify the sign identity a₀(up) = −a₀(down) (data-free, hours). Then
run the corner order alone at the frame's hierarchical points with the bare a₀ and no free number (a day). Harvest
W183 with its look counted.
*Known against it.* The odd singlet makes the corners *balanced*, not nature-like (FRAMING_LEDGER.md:62). The S289–S290
scans used functions of the graded four as success criteria, so those targets are touched for any card these scans
inform (E95, in today's working tree, B1831). The SM seat's post-pin W183 (886dc3a3c on its branch, unharvested) held the parity on its
own code but failed the corner-lift cells at τ = i, where no frame point is hierarchical, so P-566's regime is untested.

**2. P-568 — the relations the frame forces (FL-14, FL-15).**
*The idea.* The bar grades values and never relations. Count the relations the frame forces among its outputs (the
co-rank of their Jacobian in the frame's continuous data) and grade those.
*Why it could change direction.* A frame that forces relations can be tested without fitting a point. That is the
honest answer to the restated goal's "how many free numbers" (2026-10-08). It changes what "derived" can mean while τ
stays unselected, and it is data-free.
*First computation.* The web seat already computed the first half post-pin (fe2f972cd, `relays/CHAT1_TO_CC_2026-11-03_THE_RELATIONS_THE_FRAME_FORCES.md`;
unharvested). On each B1825-typed branch the only continuous input is τ, the output rank is 2 on the 1 536 branches
sampled, so the ten obey 8 relations per branch, listed explicitly. Main re-runs its two check scripts against main
(hours), then designs a card that grades relations, priced.
*Known against it.* Many of the 8 relations are already-known identities (B1728's law, exact zeros, half-period
coincidences), and some are what the record calls D = 9 by construction. A relation is only as good as its source.
The second half (rigid inter-sector ratios at the strip) is P-585's held-out target and must not be computed outside
that card. The row should say so now.

**3. P-585 — THE SIX ON THE STRIP at level 2 (the held-out confirmation).**
*The idea.* Freeze the level-1 candidate family (FR-FIB on the order-10 lines (2/5, b), Im τ ≈ 3, c = 3; B1749, B1753)
on a sealed card and predict held-out numbers. Two passes would give the first PREDICTED values (GENESIS v1.60/v1.61).
*Why it could change direction.* It is the only route on the record by which the scoreboard can leave 0 of 19.
*First computation.* Before any card: establish that two *clean* held-out targets exist (B1829 REGRADE.md:41–52 says one
of the listed targets is not clean). Rule on θ̄ (P-569/P-323 and the web seat's post-pin 8ed19bbd4, which proposes
dropping it, leaving one clean target where v1.60 needs two). Adopt P-574–P-576 (scale, theory error, searched bits).
Freeze the card with the small-cut end counted as an input. Days; sealed; no target computed before the freeze.
*Known against it.* About 0.5 false candidates expected by chance over 53 looks (B1829). The frame fails the mixing
(B1825), so at most a scoped mass dictionary is at stake. The family is ~3σ off its own in-sample D (P-355). At the
exact horoball norms the six fail (P-421; LOOK_LEDGER row 1459). Both held-out targets have a prior look (the agy
lane's, LOOK_LEDGER.md:120). Its four supporting debts (P-355, P-384, P-421, P-586) are ranked #1–#4. This is the most
important lead, but the least likely to pass as it stands.

**4. P-294's cluster — derive the lepton factor (P-460 first, then P-403).**
*The idea.* On the candidate's lines the leptons copy the down quarks, and c = 3 (Georgi–Jarlskog) is put in by hand
(B1827: "c = 3 is the Georgi-Jarlskog factor by hand"). Find the structure that separates L from d. The cheapest probe
on record is untouched: **P-460**, twist only the doublet legs (Q, L, H) by a half-period of one even spin structure.
B1728's swap law maps down's doublet leg to the leptons' singlet slot, so a doublet-only twist acts on different slots
in the two sectors (the reader's reasoning, not computed). The heavier route is **P-403**, L250's flux design: B1800
did its geometry step; the three sectors from (q_L − q_R)w = 5w, −w, −9w in closed form are next.
*Why it could change direction.* Debt #1 (P-355) and debt #5 (P-446) are both "c = 3 chosen". A structural split
would turn the strip candidate's worst defect, D, from a by-construction 9 into a computed function. It is the one
place where the candidate could get *better* rather than weaker.
*First computation.* P-460: add the twist to B1726's `compute()`; data-free, check whether Y_e = Y_d^T survives on the
order-5 lines, whether B1790's S ↔ S̃ map still preserves the readings, and D as a function on the order-10 lines with
no χ²; hours. Then P-403's closed form (a day), sealed before data.
*Known against it.* Every frame-internal route so far is closed: B1738, B1789, B1793, B1817 ("c stays one discrete
input" to order 30), and B1827's retracted 45. B1794: no rational hypercharge class on the frame. A spin-structure
choice is itself a counted discrete input. P-567's centre-line half was answered negatively at the seat (W182, HARVEST
row 1542, at the cusp ladder and τ = i only; not re-run on main).

**5. P-411 with P-422 — a rule that selects the line class (2/5, odd/10).**
*The idea.* Find a data-free consistency condition on the line itself that selects the class the six sit on. P-422 is
the one concrete rule on record: require each holonomy's square to be central with SU(5) broken. On slope 2/5 that
admits exactly the odd tenths, with b-holonomy = centre × diag(1,1,1,−1,−1), Kawamura's orbifold parity. It amounts to
gauging the fibre's elliptic involution −I, which the record's group contains (GM5d, P-049).
*Why it could change direction.* Debt #2 (P-384) is that the line class is "mostly a pick". A forced rule pays it
positively and turns the candidate's discrete choice into an output.
*First computation.* Data-free: is −I, lifted to the SU(5) line bundle with the matter rule, a gauge symmetry of
B1656's coupling, and does the frame's consistency *require* gauging it (an orbifold, not a choice)? About a day.
*Known against it.* Every condition tried points the other way: W176 K0/K1 (row 1458), the web seat's selector (row
1460 (iv), (v): no flat extending line on slope 2/5 breaks SU(5); the counted class has the highest V* of eleven), W171
(row 1446), and P-424's Fact 2. The agy lane's post-pin d9a04edd7 claims a "P-384 2/5 sign selection" (Theorems 19–20).
It is unharvested and unverified, and that lane is learn-don't-trust (P-390).

**6. P-555 — the masses and the mixing at two addresses (the towers meeting).**
*The idea.* The frame reaches the six alone and the four alone, never at one address (B1825). Read the CKM as the
relative rotation of the up and down diagonalisations at two loci, where P-415's towers meet. The second locus must be
fixed by a 0-bit rule, never left free.
*Why it could change direction.* It is the frame-level alternative to #1, and it is what THE_TOWERS is for: different
Higgs constructions per sector (up at an E₆ point, down at an SO(12) point) are exactly what B1827 traced the wall to.
*First computation.* Write out the candidate 0-bit rules that change r = |h·h|/|h|² between the sectors (the mirror
keeps r, so it cannot be one), count them against the ceiling, and test corner order alone, data-free. The design note
is `frontier/B1827_the_framing_ledger/verification/scans/DESIGN_NOTE.md` (budget § 1, S298 correction at :76).
*Known against it.* The budget is 3.63 bits for a rule plus the four's misfit, and a free second address is dead. The
S298 correction stands: the mirror rule is NOT FOUND to raise the rate, not closed. In every frame tested the object
fixes the total class, not the positions (B1805; B1812 as narrowed; `docs/THE_TOWERS.md:139–164`).

**7. P-487 — the support and exclusion test on the whole interaction.**
*The idea.* Ask (a) whether any allowed configuration reproduces our pattern and (b) which patterns *no* configuration
reaches, with c supplied by the interaction, never set.
*Why it could change direction.* Half (b), exclusion, is the only test on record that could make the framework
falsifiable on *structure* rather than on fit. B1825 ran a restriction, and its X1 reads "none claimed".
*First computation.* Data-free: the exclusion census of FR-FIB as it stands, computed from the sealed census's
aggregates. Which coarse patterns does no node reach? For example the corner order of |V|, the sign of D − 9 by line
class, or m₁/m₃ at the floor in one sector and not another. Days. The whole-interaction version waits on the lepton
factor (#4).
*Known against it.* What a frame excludes may be generic to any Froggatt–Nielsen-type texture. It needs the
object-and-rival nulls of P-578 to mean anything.

**8. P-373 — what fixes Im τ ≈ 3.03 (absorbing P-343, P-398, P-457).**
*The idea.* The six's specificity lives on one strip, Im τ 2.96–3.11, Re τ flat. What principle fixes the height?
*Why it could change direction.* τ is the candidate's sharpest continuous input. A forced height makes the level-2 card
cheaper and is one of the programme's three named gaps (τ not selected).
*First computation.* First settle P-421 (debt #4): re-fit on the strip's lines with the exact horoball norms and L free,
at its look-elsewhere cost. If "Im τ ≈ 3.03" does not survive the exact end, there is no height to explain. Then the
non-perturbative and flux potentials, each stated before its check.
*Known against it.* Every one-loop and special-point route is closed: B1791 NEGATIVE; W154/W155 (rows 1388, 1390);
B1784:32; W175; W150 (one chosen ratio, S260); and the ρ′ Petersson peak, set by the η-power convention (P-398). The
strip is defined through the small-cut end.

**9. P-572 with P-396 — the nine with no frame (and the misfiled gauge route).**
*The idea.* Six of the 19 have no frame at all (g₁, g₂, g₃, m_H, v, y_t); three are frame outputs never examined
(FL-05; the S291 recount).
*Why it could change direction.* A third of the target sits outside every frame. Anything here changes the
programme's reach more than any flavour result. The only computed route to two of the three gauge couplings is
**P-396**, the audit lane's relative gauge thresholds: the universal SU(5) end cancels in the differences, and the
splitting lives in Wilson-sensitive spectral data. P-396 is typed **[PROCESS]**, so a [LEAD] reading would not have
seen it (§E).
*First computation.* Read B1684, B1791 and B1823 against FL-05: the SM seat says "no action on record" overstates
(P-591). Retype P-396 [LEAD] and verify its first H_R(q) step in main's own code (days).
*Known against it.* P-396's own row states that absolute couplings are not fixed and that a common internal scale
cancels only when the weighted light kernel vanishes. Two authored proofs are stacked unreviewed on it (its S263
note).

**10. P-058 (with P-059, P-060) — the audit lane's charged three on a connected double cover.**
*The idea.* The physical-bridge lane reports three left-handed 10 + 5̄ *with gauge currents* on a connected double
cover of a 2D punctured elliptic object with a supplied E₈ parent. Is it B1606's ±3 in another dress, or new?
*Why it could change direction.* Three exists on the record only as an index by selection. The integration census
calls this "the only result anywhere on the record that yields three with gauge content"
(`docs/THE_INTEGRATION_CENSUS_2026-10-13.md:48–53`), and in three weeks it has **never been verified on main**. It is
exactly the kind of stored lead the owner fears.
*First computation.* Re-run the lane's `silver_cover_{families,currents,cubic}_2026_10_12` packages at its pin in a
worktree, then test whether the three equals n(|Λ₊| − 3) for the cover's Λ (B1641's formula). If so, it is the existing
±3. About a day; data-free.
*Known against it.* The lane self-grades it "CONDITIONAL … not a derivation of three physical generations". Its
boundary is unselected, so it is probably a selection again. B1689 (at most two complete generations per sub-tower in
the fibre's E₈ frames) and B1604 (no index in three on covers) stand on main's objects.

**Next five, close behind:** **P-036** (the located selections as independent coordinates or one datum, which is the
free-number count itself; first computation a dependency table over FRAMING_LEDGER's CHOSEN rows under B1733's thread
rule, a day). **P-531** (which typing forces the generations' metric H = I; on the candidate's own order-10 lines the
moves leave H two-dimensional, so P-585's card must declare or charge it). **P-022** (average τ instead of choosing it:
a Petersson or Rankin–Selberg triple overlap over W46's four-dimensional space would remove τ as an input; obstacle:
divergence at the cusp, P-134). **P-439** (THE CLOCK: a forced clock would make "deep hierarchies are typical" a
derivation; B1815/B1816 say it stays CHOSEN). **P-458** (the spin connection as L250's background: the object's one
canonical non-flat SU(2) connection, against FL-02's count that 107 of 173 value-kills rest on flat premises; blocked
by debt P-540, B940's instrument).

### (c) Leads that duplicate one another (merge candidates)

| host (keep open) | merge into it | the one question |
|---|---|---|
| **P-555** the CKM corners (umbrella) | P-566, P-583, P-591's RI-1 as live children; P-474, P-558 close into it; P-345, P-357, P-366, P-377 superseded into P-566 | how the quark mixing escapes the one-Higgs lock |
| **P-295** the reading rule | P-394 | which sector reads the conjugate Higgs (B1790: not derivable in the frame; the adjugate is the new route) |
| **P-294** the lepton factor | P-397; P-315 → debt P-355; P-567's remainder → P-593 item 2; P-403, P-460, P-453 as its routes | what separates L from d (c = 3) |
| **P-373** what fixes Im τ | P-343, P-398, P-457; P-327, P-371, P-380 answered (residues here) | the strip's height |
| **P-022** averaging τ | P-455, P-069 (c) | remove the point instead of selecting it |
| **P-287** C6 | P-069 (b) | a content holding τ in the band |
| **P-439** THE CLOCK | P-413, P-438, P-440, P-477, P-478, P-479 | move count or geodesic flow |
| **P-411** a line-class rule | P-422 (first sub-item), P-454, P-456 | what selects (2/5, odd/10) |
| **P-415** THE TOWERS | P-416, P-424, P-463; P-466 and P-555 its computable children | where the towers meet |
| **P-419** selection by inversion | P-425, P-449, P-450 (their fate is debt P-527); P-494 → P-527 | discrete data forcing moduli onto rigid loci |
| **P-139** the selection principle (FK9) | P-073 | every "which" is free |
| **P-323** θ̄ in the frame | P-569, P-461 (b) | a CP-even determinant (conflicts with P-585's held-out target) |
| **P-337** the zero law | P-404 (P-292 already merged) | every exact zero is isotropy plus a mirror |
| **P-289** C10 | P-330 (blocked by debt P-540) | an index on a physical spacetime |
| **P-210** the end's index | P-184, P-218 | ±1 or ±3 at the symmetric state (would pay debt P-156) |
| **P-033** L252, the McKay ladder | P-034, P-040, P-041, P-331 | levels 3/4/5 ↔ 2T/2O/2I ↔ E₆/E₇/E₈, re-aimed at P-384 |
| **P-036** L253 | P-038 | the selections' dependence |
| **P-058** the silver-cover dossier | P-059, P-060 | the audit lane's 2026-10-12/13 results |
| **P-487** the support test | P-485 | support and exclusion |
| **P-574** one bar amendment ([PROCESS]) | P-570, P-575, P-576, P-582 | scale, theory error, searched bits, existence before looks (P-578 stays a lead: its object null is a computation) |
| **P-257** C5 | P-023 | the near-ω regime (both decline candidates: C5 cannot act on the order-5/10 lines, P-327's note) |
| debt **P-321** | P-280 | the prime under GM5c |
| debt **P-579** | P-418 | the total-inputs vector |
| debt **P-025** | P-537 (candidate) | the normalisation of forms used as couplings |
| debt **P-492** | P-137, P-476 (candidates) | L154's bridge and the action weight |

### (d) Rows that should be closed, with pointers

**V** = re-checked at source by the assembling reader; **R** = the row reader's pointer, not re-opened.

*ANSWERED — close DONE (22):*

| row | pointer | |
|---|---|---|
| P-020 | B1800 (claim line: L251 computed as stated, bulk overlaps of flux modes); `docs/OPEN_LEADS.md:3853` already marks L251 DISCHARGED by B1800 in today's working tree | V |
| P-044 | B1795 FINDINGS:78 cites B1484's ½; B1801, B1802/B1803; the orphan is reconnected; the gauge question lives on P-396 | V |
| P-062 | W49: B1642 FINDINGS:55, P-087 DONE; W25: GENESIS.md:443 (FK11 v1.27); W48: B1652 FINDINGS:78. The re-runs of W36 and W48 on main → [PROCESS] | V (in part) |
| P-064 | B1641 FINDINGS:49 ("the Banking Seat's Gate 11 obstruction (Δ⁴ = −I₃) is this sign"); THE_WEAVE.md:391 | V |
| P-070 | B1677 FINDINGS:86–87 and B1682 FINDINGS:57–59 (read as a finite orbit, "nothing is selected"); GENESIS GM1 v1.50 | V |
| P-258 | B1726 PREREGISTRATION:43 (R6, ∣J∣); B1825 PREREGISTRATION:39 (∣J∣ the tenth target) | V |
| P-269 | B1719 (W122); B1796 FINDINGS:50, :133 (W123, "P-288's verification half is paid"); HARVEST row 1302 (W124 read) | V (:133) |
| P-327 | HARVEST row 1401 (the web seat's e17/e18, refereed); W154 row 1388; B1784 FINDINGS:32. Close after a minutes-long re-run on main or a dated acceptance note | V |
| P-371 | HARVEST row 1371 (W150 reproduced with corrections at S260, audit/verify_w150/); rows 1376 (W152), 1409 (W158 NEGATIVE), 1410 (W159 NEGATIVE) | V |
| P-380 | Stage A = W154 (row 1388); Stage B = W155 (row 1390, "the census over contents, Stage B"). W154's analytic form is debt P-117 | V |
| P-393 | umbrella plan: steps 1–4 paid by B1785–B1791, B1793, B1817; residues in P-384, P-294, P-394, P-373, P-421 | R |
| P-412 | the web seat sealed it (e56a311ce; both cells INTERMEDIATE); HARVEST row 1469 is **READ, not recomputed on main**; LOOK_LEDGER.md:82 ("not a look"). Close DONE only with that qualifier, or after main's re-run | V |
| P-437 | stages B1813 and B1814; B1814 FINDINGS:138 ("the clock question goes to the theory side (P-438, P-439)") | V |
| P-443 | `docs/THE_CLOCK_AND_THE_NEXT_ATTACK_2026-10-29.md` § 6 (headed "(P-443, the owner's question)", six assumptions); `docs/FRAMING_LEDGER.md` (B1827) the full inventory | V |
| P-462 | B708 FINDINGS:1–4 (B707's test #1, sealed 96ebff1d, MEET); B905; B1108, B1156. B707's own verdict line "none run" is stale (the debt P-334 class) | V (B708) |
| P-465 | THE_CLOCK doc:65 (row E: "No hierarchy from the principle followed literally") and § 4; the residue is P-439 | V |
| P-468 | form 2: HARVEST row 1475, VERIFIED at S259 with main's own Gauss-operator code; form 4: THE_CLOCK doc:66, :152; form 3 = P-475 | V (1475) |
| P-523 | B1825 PREREGISTRATION § 4 (lines 95–190; vacuity calibration NOT VOID at 154–158). The unpaid FN populations (:181) → P-578/P-585 | V |
| P-538 | B1825 PREREGISTRATION.md:108–113 ("The line's price (P-538, main's ruling)"); read-out → P-556 | V |
| P-543 | B1825 PREREGISTRATION.md:190–195 ("R and t = −5/288 are structurally dead for our world") | V |
| P-554 | B1825 PREREGISTRATION.md:176–178 (names P-554); FINDINGS.md:59–60; the lesson is carried by FL-13, P-574, P-575 | V |
| P-562 | the same question as P-324, DONE (register line 472: B1744, the twisted Higgs is even, H_u = H_d); FRAMING_LEDGER.md:60 (an even singlet does nothing) | V |

*SUPERSEDED — close, naming the successor (17):* P-023 (B1691, B1657; C5 → P-257) R · P-046 (B1800 FINDINGS:92–93)
R · P-069 ((a) B1723 PREREG:25–27 V; (b) → P-287; (c) → P-022) · P-177 (items 1, 3, 4 by its own escalation; item 2
by P-277 DONE, register line 425 V; item 5 small) · P-184 (→ P-210: B1672, B1678, B1787) R · P-267 (B1732 NEGATIVE
as sealed; P-307 DONE, register line 455 V; residue P-303 OWNER) · P-328 (the J rule follows from B1821's mirror map
with its period shift, the reader's derivation, so B1821 owes one dated line; ledger → MAINS_PLAN and P-418; anchor →
P-411, P-569) R · P-329 (→ P-574, P-585's card; negatives → P-590) R · P-345 ((a) B1740, (b) B1742; live form P-555,
P-566) R · P-357, P-366, P-377 (→ P-566: B1744's det Y factor makes the odd singlet P-357's invariant; W158/W159 rows
1409/1410 V; B1823, B1825) · P-402 (→ debt P-421; HARVEST rows 1455, 1459) R · P-474 (→ P-555; HARVEST row 1513
"NOT FOUND, as scoped"; P-555's row already reads it first) V · P-494 (→ debt P-527; never reached B1825 PREREG § 7
Disclosed, lines 256–270) R · P-526 (lapsed at the seal; B1825 FINDINGS:15–20; HARVEST row 1515) R · P-558 (→ P-566;
B1826 FINDINGS:45–52; B1827 § D) R.

*SHOULD BE A DEBT (2):* **P-418**: debt P-579 (register line 727, ranked #19) has as its next action "build P-418's
vector (an owner ruling of 2026-10-29)" V, so P-418 is debt work filed as a lead; merge into P-579. **P-476**: if a
minutes-long SnapPy check confirms that vol(LᵃR) tends to the Whitehead link's volume, then the action weight's
"concentrate on short threads" comes from B1720's cutoff, not the weight, and B1722's W2 headline, LAW_MAP row 319 and
THE_WEAVE.md:854 each owe a scope sentence (B1722 FINDINGS:21 already calls the weight "nearly flat") R.

*DECLINE (1):* **P-039**. Its 2026-10-28 escalation offers "or decline then". B345's anti-diagonal texture is generic
to any ℤ/3-covariant quadratic coupling, and the live frame's ℤ₃ is diagonalised R.

*Retype [PROCESS] (2, and parts of three more):* P-063 (a seat statistic to re-run); P-574 as the host of one bar
amendment, with P-570, P-575, P-576 and P-582 merged into it. Also: the asks half of P-591 (identification rows, a rule,
FL-05's wording) and P-062's remainder.

---

## PART II — WHAT THE READING FOUND BESIDE THE ROWS

### (E) A lead outside the [LEAD] typing

- **P-396** (the relative gauge thresholds: the audit lane's route to two of the three gauge couplings) is typed
  **[PROCESS]**, as one of "the lanes' unverified results". By the register's own definitions it is a lead: an idea
  and a computation not yet done, with nothing resting on it. Its potential is HIGH, since it is the *only* route on
  record to any gauge coupling (see #9). Retype it [LEAD], and read it with P-572. Two other PROCESS rows are also
  other lanes' unverified mathematics rather than housekeeping: P-061 (puncture_fredholm) and P-102 (the surface
  fermion dictionary). Both are lower potential.

### (F) Seat work after main's S298 pins that bears on these leads (unharvested)

All four commits exist, and each descends from the pin S298 recorded:

| commit | lane | what | bears on |
|---|---|---|---|
| fe2f972cd | web seat (descends from e40d0fb1) | THE RELATIONS THE FRAME FORCES: output rank 2, eight relations per branch | P-568 (top ten #2) |
| 8ed19bbd4 | web seat | THE STRONG ANGLE NEEDS A RULE (P-323's counterterm rule); proposes dropping θ̄ from P-585's targets | P-323, P-569, P-585, P-461 |
| 886dc3a3c | SM seat (descends from 254c09df) | W183: RI-1 tested at τ = i; parity held, corner-lift cells failed, D cell a look | P-566, P-591 (top ten #1) |
| d9a04edd7 | agy audit lane (descends from 9366d7c6) | Theorems 19–20: P-524 elliptic periodicity, P-384 2/5 sign selection, P-233 control, P-355 order-10 | P-411/P-422 (#5), debts P-384, P-355, P-524, P-233 |

### (G) Conflicts with the held-out targets (P-585)

- Using θ̄ as a selector (P-569), or computing the det-real curves through the strip, spends one of P-585's two held-out
  targets. So does computing P-568's second half (the rigid inter-sector ratios at the strip). Both rows should carry
  the conflict now.
- P-582's "unsealed existence scan" is itself a look at data and must enter LOOK_LEDGER (E95; PRACTICES item 3 in today's working tree,
  B1831).
- P-583's test can probe the mechanism only: our six cannot sit on the order-5 lines, which P-590's row excludes
  through D at any scale.

### (H) Stale statements found along the way (each a small correction for main)

- `docs/MAINS_PLAN.md:85`: the horocycle "named, not studied", despite HARVEST rows 1455 and 1459 and P-421.
- `frontier/B1791*/FINDINGS.md:67`: "Not examined: P-380's Stage B", but W155 ran it (row 1390). P-373's ESCALATED note
  lists the same item as open.
- B707's verdict line ("none run"), though B708 ran test #1 (the debt P-334 class).
- `docs/OPEN_LEADS.md:3925` (L254's Review-74 mark, working tree): C6 and C7 are misnamed. `docs/THE_COMPLETION_MAP.md:35–36`
  defines C6 as "a content that holds τ in the band, or W106" and C7 as "a potential minimum with J ≠ 0". The same loose
  mapping is in L254's 2026-10-22 note. Two readers found it independently.
- `docs/THE_COMPLETION_MAP.md:36`: C7's status cell still reads QUEUED, though P-277 is DONE (register line 425).
- B1821 owes a dated line for the J-vanishing rule on the CP lines (P-328), which follows from its mirror map and period
  shift (the reader's derivation, to verify).
- P-454's "never tried since B1600" misses B355 (the Weil representation at N = 3, 5, 15), B413, B214/B283 and
  B587/B588. Its Seen first is owed.
- P-038: the reader gives a classical argument that the lead collapses. Hyperbolic A, B in SL(2, ℤ) with
  tr[A, B] = −2 generate a finite-area punctured-torus group of index 6, conjugate to the commutator subgroup Γ′, so the
  torus is always the hexagonal one (ω) and the list is the infinite Markov tree. Main can verify by enumerating thread
  pairs to length about 10 (an hour); if it holds, P-038 closes as answered by a classical theorem.

### (I) Where the 57 remaining leads sit, by the programme's open questions

| open question | live hosts (potential) |
|---|---|
| the quark mixing (the Higgs construction) | P-555, P-566, P-583, P-591 RI-1, P-295 (HIGH); P-045, P-536, P-564 (MEDIUM) |
| the candidate's c = 3 and D | P-294, P-460, P-403 (HIGH/MED-HIGH); P-453 (LOW) |
| the candidate's line class | P-411 with P-422 (HIGH, conditional); P-033 (MEDIUM) |
| τ not selected | P-373, P-022 (HIGH/MED-HIGH); P-287, P-475, P-419, P-439 (MEDIUM); P-466 (MED-HIGH) |
| recognising an answer | P-568, P-487, P-578 (HIGH/MED-HIGH); P-585 the decisive card; P-574 as process |
| three generations | P-058 (HIGH if new), P-210, P-531, P-564, P-035 (MEDIUM); P-264, P-279 (LOW) |
| the nine with no frame (gauge, Higgs, scale) | P-572 with P-396 (HIGH prize); P-281, P-290 (MEDIUM); P-459 (LOW) |
| θ̄ (a held-out target: handle under P-585) | P-323, P-461 (MEDIUM) |
| foundations and the free-number count | P-036 (HIGH importance), P-139, P-130, P-041's angle via P-033 (MEDIUM) |
| gravity and spacetime read-outs | P-289, P-458 (MEDIUM); P-137, P-178, P-491, P-493 (LOW) |
| neutrinos | P-042 (MEDIUM, near debt P-157); P-326 (LOW) |
| pure mathematics, nothing for the 19 | P-032, P-337, P-405, P-257 (LOW–MEDIUM) |

---

## PART III — THE INDEX (every row, one line)

`cat` = the proposed disposition after adjudication; *pointer / host* names the arc, the row or the host it folds into.

| row | line | registered | title | potential | cat | pointer / host | cluster |
|---|---|---|---|---|---|---|---|
| P-020 | 168 | 2026-10-13 | the couplings as overlap integrals of the fibre's zero modes | LOW | **ANSWERED** | B1800 (claim line; FINDINGS 95-99); OPEN_LEADS.md:3853 already marks L251 DISCHARGED | field/L251 |
| P-022 | 170 | 2026-10-13 | τ has two roles: integrated in the index, evaluated in the couplings | MEDIUM–HIGH | **LEAD** | host: averaging tau instead of choosing it (absorbs P-455, P-069 (c)) | tau selection |
| P-023 | 171 | 2026-10-13 | the near-fixed-point mechanism on the ruled branch, fields at their ow | LOW | **SUPERSEDED** | B1691, B1657; C5 residue -> P-257 | C5 near-omega |
| P-032 | 180 | 2026-10-13 | the converse: F = 8 only on the discriminant-5 geodesics | LOW | **LEAD** | LOW; B1723 PREREG 25-27 is more numerics (Im tau <= 4), not a proof; decline candidate | golden identity |
| P-033 | 181 | 2026-10-13 | the McKay ladder | MEDIUM | **LEAD** | host L252 (absorbs P-034, P-040, P-041, P-331); re-aim at P-384 | McKay ladder |
| P-034 | 182 | 2026-10-13 | the July level-5 golden corpus is cited by no B1400+ arc | MEDIUM | **MERGE** | -> P-033 | McKay ladder |
| P-035 | 183 | 2026-10-13 | the crossing's spin-structure results | LOW–MEDIUM | **LEAD** |  | spin structures |
| P-036 | 184 | 2026-10-13 | the located selections: independent coordinates or one datum | HIGH | **LEAD** | host L253 (absorbs P-038) | free-number count |
| P-038 | 186 | 2026-10-13 | orphan B471: thread pairs with tr[W₁, W₂] = −2 and where their axes me | LOW | **MERGE** | -> P-036; reader's classical argument (tr[A,B] = -2 forces the hexagonal torus) to verify, ~1 h | free-number count |
| P-039 | 187 | 2026-10-13 | orphan B345: ℤ/3 charges force an anti-diagonal texture | LOW | **DECLINE** | its own ESCALATED note offers "or decline then"; generic Z/3 texture (B345 tier) | orphans |
| P-040 | 188 | 2026-10-13 | orphan B640: im ρ = 2I × ℤ/3, tr ρ | MEDIUM | **MERGE** | -> P-033 | McKay ladder |
| P-041 | 189 | 2026-10-13 | orphan B997: golden the unique metallic grammar whose own-conductor sh | MEDIUM | **MERGE** | -> P-033, keeping its foundations angle (GENESIS.md:251 E8 container not derived) | McKay ladder |
| P-042 | 190 | 2026-10-13 | orphan B1143: B−L a genuine fourth Cartan direction, anomaly-free, aga | MEDIUM | **LEAD** | cross-ref debt P-157 | neutrinos |
| P-043 | 191 | 2026-10-13 | orphan B1430: the SM unique in E₆ only when the 27 branches as one gen | MEDIUM | **LEAD** | could become DEBT if F-MC uses B1430's branching unstated; near P-233 | towers |
| P-044 | 192 | 2026-10-13 | orphan B1484: sin²θ_W's gate ratio, cited only by docs and L250 | MEDIUM | **ANSWERED** | B1795 FINDINGS:78, B1801, B1802/B1803 cite B1484; live gauge question is P-396 | gauge |
| P-045 | 193 | 2026-10-13 | orphan B1251: the E₆ cubic's 45 triples, D2-odd, against one-27_H coup | MEDIUM | **LEAD** | near P-415, P-566 | towers |
| P-046 | 194 | 2026-10-13 | orphan B1089: every matter datum interface-resident, the coupling boun | LOW | **SUPERSEDED** | B1800 FINDINGS:92-93 (with B1642, B1653) | field/L251 |
| P-058 | 206 | 2026-10-13 | the audit lane's charged three on a connected double cover, against T- | HIGH | **LEAD** | host: the audit lane's silver-cover dossier (absorbs P-059, P-060); never verified on main | three generations |
| P-059 | 207 | 2026-10-13 | the audit lane's non-zero inter-family cubic on the cover | LOW–MEDIUM | **MERGE** | -> P-058 | three generations |
| P-060 | 208 | 2026-10-13 | the audit lane's E₈ embedding of the puncture coefficient, its Yang–Mi | LOW | **MERGE** | -> P-058 | three generations |
| P-062 | 210 | 2026-10-13 | engaged too little: W49, W25, W36, W48 | LOW | **ANSWERED** | W49: B1642 FINDINGS:55, P-087 DONE; W25: GENESIS.md:443 (FK11 v1.27); W48: B1652 FINDINGS:78; W36/W48 re-runs -> PROCESS | seat results |
| P-063 | 211 | 2026-10-13 | the Banking Seat's Gate 9: C₂ | LOW | **PROCESS** | a seat result to re-run; nothing rests on it | seat results |
| P-064 | 212 | 2026-10-13 | the Banking Seat's Gate 11: the abelianisations; Δ⁴ = −I₃ obstructs th | LOW | **ANSWERED** | B1641 FINDINGS:49; THE_WEAVE.md:391 | seat results |
| P-069 | 217 | 2026-10-13 | τ as a dynamical field: a modular-invariant potential, the orbit-avera | HIGH | **SUPERSEDED** | (a) B1723; (b) -> P-287; (c) -> P-022 | tau selection |
| P-070 | 218 | 2026-10-13 | why matter sits at the common point | LOW | **ANSWERED** | B1677 FINDINGS:86-87, B1682 FINDINGS:57-59 (finite-orbit reading selects nothing); GENESIS GM1 v1.50 | foundations |
| P-073 | 221 | 2026-10-13 | "if the principle is the seed, we miss the field" | HIGH | **MERGE** | -> P-139 (umbrella) | selection |
| P-130 | 278 | 2026-10-14 | the field's genesis, "what exists is read" | MEDIUM | **LEAD** | home FK15; note B1796 | field genesis |
| P-137 | 285 | 2026-10-14 | L154 posed on the weave's quantised sector | LOW | **LEAD** | LOW; with P-492 (debt) and P-476 (L154's bridge) | gravity/L154 |
| P-139 | 287 | 2026-10-14 | the selection principle | HIGH | **LEAD** | host: the selection principle (FK9), absorbs P-073 | selection |
| P-177 | 325 | 2026-10-15 | the owner's "existence in time / push-back" table | LOW | **SUPERSEDED** | items 1,3,4 per its own ESCALATED note; item 2 by P-277 DONE (register l.425); item 5 small: keep or decline | owner view |
| P-178 | 326 | 2026-10-15 | the arena: SL | LOW | **LEAD** | N4 only (N1 GENESIS v1.48/B1662; N2 = W98 seat-only) | arena |
| P-184 | 332 | 2026-10-16 | the end law's last question: does the weave's symmetry force index ±3? | MEDIUM | **SUPERSEDED** | -> P-210 (B1672, B1678, B1787) | end index |
| P-210 | 358 | 2026-10-20 | which index the end takes at the symmetric state | MEDIUM | **LEAD** | host: the end's index (absorbs P-184, P-218); would pay debt P-156 | end index |
| P-218 | 366 | 2026-10-21 | three ±3 pointers connected nowhere | MEDIUM | **MERGE** | -> P-210, copying its question into P-210 (answers S296's objection) | end index |
| P-257 | 405 | 2026-10-22 | W118's seven rationals of the composite field near ω | LOW | **LEAD** | LOW; C5 host; decline with P-023 once C5 is ruled moot for the strip | C5 near-omega |
| P-258 | 406 | 2026-10-22 | the CP phase as a ninth observable in sealed fits | LOW | **ANSWERED** | B1726 PREREG:43 (R6 /J/); B1825 PREREG:39 (/J/ the tenth target) | cards |
| P-264 | 412 | 2026-10-22 | an ALG gravitational instanton as the triplet's carrier | LOW | **LEAD** | LOW | end index |
| P-267 | 415 | 2026-10-22 | PF1-W: holomorphic invariants have zeros only at the end | LOW | **SUPERSEDED** | B1732 NEGATIVE as sealed (P-307 DONE, register l.455); residue P-303 (OWNER) | readings |
| P-269 | 417 | 2026-10-22 | the SM seat's gravity line: W122, the hand reading, W123, W124 | LOW | **ANSWERED** | B1719 (W122), B1796 FINDINGS:50,:133 (W123), HARVEST row 1302 (W124 read) | gravity |
| P-279 | 427 | 2026-10-22 | the cusp's unit under the family of wordings | LOW | **LEAD** | LOW; decline candidate citing B1796 | end index |
| P-280 | 428 | 2026-10-22 | does any weave quantity separate p = 2 from p = 3 without the triplet? | MEDIUM | **MERGE** | -> P-321 (DEBT): same computation; audit/drafts/leads_reeval/LEADREG_10_18.md:307-308 unbanked | prime |
| P-281 | 429 | 2026-10-22 | the gauge echo: does U | MEDIUM | **LEAD** | record P-140/W83 as its N = 2 case | gauge |
| P-287 | 435 | 2026-10-22 | the completion map's C6: a content that holds τ in the band | HIGH | **LEAD** | C6; with P-327, P-380 answered negative at one loop, what remains is non-perturbative/flux content | tau selection |
| P-289 | 437 | 2026-10-22 | the completion map's C10: an index on a physical spacetime | MEDIUM-LOW | **LEAD** | host C10 (absorbs P-330); W126 unverified on main | C10 |
| P-290 | 438 | 2026-10-22 | the completion map's C11: which fields carry T | MEDIUM | **LEAD** | C11 | gauge |
| P-294 | 442 | 2026-10-22 | derive the lepton factor 3 | HIGH | **LEAD** | host: the lepton factor (absorbs P-397); debts P-355, P-446 carry the load | lepton factor |
| P-295 | 443 | 2026-10-22 | derive the reading rule | HIGH | **LEAD** | host: the reading rule (absorbs P-394); children P-566, P-583 | CKM corners |
| P-315 | 463 | 2026-10-23 | why only the Higgs's i-component splits down from leptons on 12 order- | MEDIUM–HIGH | **MERGE** | -> P-355 (DEBT #1): B1742 section 3; Theorem 18C unverified on main | lepton factor |
| P-323 | 471 | 2026-10-23 | θ̄ in the mass frame | MEDIUM | **LEAD** | host: theta-bar (absorbs P-569, P-461 (b)); conflict with P-585's held-out target | theta-bar |
| P-326 | 474 | 2026-10-23 | ν^c's Majorana mass as a modular form | LOW | **LEAD** | LOW; near debt P-157 | neutrinos |
| P-327 | 475 | 2026-10-23 | the one-loop potential on the fit's lines | LOW | **ANSWERED** | HARVEST row 1401 (refereed); W154 row 1388; B1784 FINDINGS:32; close after a minutes re-run on main or a dated acceptance | tau selection |
| P-328 | 476 | 2026-10-23 | the input ledger and the CP-line J-vanishing rule | LOW | **SUPERSEDED** | J rule from B1821's mirror map (needs a dated line in B1821); ledger -> MAINS_PLAN, P-418; anchor -> P-411, P-569 | tau selection |
| P-329 | 477 | 2026-10-23 | B1726 at the unification scale | LOW | **SUPERSEDED** | -> P-574 and P-585's card (positives), P-590 (negatives) | cards |
| P-330 | 478 | 2026-10-23 | C10 on m004: seal B940's open O2, then the ρ_T twist | MEDIUM | **MERGE** | -> P-289 (C10); blocked by debt P-540 | C10 |
| P-331 | 479 | 2026-10-23 | L161 Phase 1b: does B1656's coupling carry the θ-odd 2I doublet on an  | LOW | **MERGE** | -> P-033 (L252) | McKay ladder |
| P-337 | 485 | 2026-10-23 | the zero law: every exact zero is isotropy plus an involution or the r | MEDIUM | **LEAD** | host: the zero law (absorbs P-404); web seat kernels note (row 1516) to verify; helps debts P-262, P-268 | zero law |
| P-343 | 491 | 2026-10-23 | what places τ where the six are reached | ? | **MERGE** | -> P-373 (its own ESCALATED note) | tau selection |
| P-345 | 493 | 2026-10-23 | what gives the nine | ? | **SUPERSEDED** | (a) B1740, (b) B1742; live form P-555, P-566 | CKM corners |
| P-357 | 505 | 2026-10-23 | what fixes the Higgs's invariant | ? | **SUPERSEDED** | -> P-566 (B1744's det Y factor makes the odd singlet P-357's invariant) | CKM corners |
| P-366 | 514 | 2026-10-24 | the target lies outside every single holomorphic section | ? | **SUPERSEDED** | -> P-566 | CKM corners |
| P-371 | 519 | 2026-10-24 | W150/W151: τ's height from the heavy states, and the two-object bound | LOW | **ANSWERED** | HARVEST row 1371 (reproduced S260, audit/verify_w150/), rows 1376, 1409, 1410 (W152, W158, W159 NEGATIVE); mu/M~ -> P-373 | tau selection |
| P-373 | 521 | 2026-10-24 | what fixes Im τ ≈ 3.03 | HIGH | **LEAD** | host: what fixes Im tau (absorbs P-343, P-398, P-457); conditional on debt P-421 | tau selection |
| P-377 | 525 | 2026-10-24 | step 2 of the plan after B1749: the mixing at the six's strip | ? | **SUPERSEDED** | -> P-566/P-555 (W158/W159, B1823, B1825) | CKM corners |
| P-380 | 528 | 2026-10-24 | W154: the census over contents, Stage A; Stage B waits on the owner | LOW | **ANSWERED** | Stage A W154 (row 1388), Stage B W155 (row 1390); W154's analytic form is debt P-117 | tau selection |
| P-393 | 541 | 2026-10-27 | main's own plan beside the SM seat's | LOW | **ANSWERED** | umbrella: steps 1-4 paid by B1785-B1791, B1793, B1817; residues in P-384, P-294, P-394, P-373, P-421 | plans |
| P-394 | 542 | 2026-10-27 | the reading rule as an input to remove | MEDIUM | **MERGE** | -> P-295 (B1790: not derived in the frame); the adjugate (B1827) is the new route | CKM corners |
| P-397 | 545 | 2026-10-28 | the lepton factor's route left | MEDIUM | **MERGE** | -> P-294 | lepton factor |
| P-398 | 546 | 2026-10-28 | a frame-internal height: the ρ′ Higgs's Petersson peak | LOW | **MERGE** | -> P-373 | tau selection |
| P-402 | 550 | 2026-10-28 | the horocycle is a counted discrete input with no row | ? | **SUPERSEDED** | -> P-421 (DEBT #4); HARVEST rows 1455, 1459 | end/horocycle |
| P-403 | 551 | 2026-10-28 | L250's sealed design: the flux geometry first | MEDIUM–HIGH | **LEAD** | L250 flux design; B1800 did step 1 | lepton factor |
| P-404 | 552 | 2026-10-28 | the Weinberg pair's CP-line zeros | LOW–MEDIUM | **MERGE** | -> P-337 | zero law |
| P-405 | 553 | 2026-10-28 | G₂ membrane-instanton Yukawas | LOW | **LEAD** | LOW; decline candidate on its own S234 reason | towers |
| P-411 | 559 | 2026-10-28 | a class-selecting consistency condition on the line | HIGH | **LEAD** | host: a rule selecting the line class (absorbs P-422, P-454, P-456); positive route to debt P-384 | line class |
| P-412 | 560 | 2026-10-28 | the frame null | LOW | **ANSWERED** | web seat sealed e56a311ce, both cells INTERMEDIATE (HARVEST row 1469, READ not recomputed); LOOK_LEDGER.md:82; residue debt P-446 | cards |
| P-413 | 561 | 2026-10-28 | a forced weight for the sum over threads | LOW | **MERGE** | -> P-439 (B1813, B1815, B1816) | clock |
| P-415 | 563 | 2026-10-28 | THE TOWERS: the SM as the interaction of towers meeting at loci | HIGH | **LEAD** | host: THE TOWERS (absorbs P-416, P-424, P-463); P-466, P-555 its computable children | towers |
| P-416 | 564 | 2026-10-28 | local G₂ models with coincident multiplets | LOW | **MERGE** | -> P-415 | towers |
| P-418 | 566 | 2026-10-28 | ONE HONEST SCOREBOARD: the total-inputs vector | MEDIUM | **DEBT** | -> P-579 (DEBT #19 names "build P-418's vector", an owner ruling of 2026-10-29) | scoreboard |
| P-419 | 567 | 2026-10-28 | SELECTION BY INVERSION: discrete SM data forcing the moduli onto speci | MEDIUM | **LEAD** | host: selection by inversion (absorbs P-425, P-449, P-450); fate of the CM rows is debt P-527 | selection |
| P-422 | 570 | 2026-10-28 | gauge the fibre's involution on the lines? | HIGH | **MERGE** | -> P-411 as its first sub-item (the only rule on record that selects (2/5, odd/10)) | line class |
| P-424 | 572 | 2026-10-28 | THE TWO W's | MEDIUM | **MERGE** | -> P-415 | towers |
| P-425 | 573 | 2026-10-28 | CM by the object's own compositum ℚ | LOW | **MERGE** | -> P-419 | selection |
| P-437 | 585 | 2026-10-29 | the owner's whole-existence computation, unforced | MEDIUM | **ANSWERED** | stages B1813, B1814 (B1814 FINDINGS:138 hands the clock to P-438/P-439) | clock |
| P-438 | 586 | 2026-10-29 | FOLLOWED OR COUNTED | LOW | **MERGE** | -> P-439 (B1815; THE_CLOCK doc row C) | clock |
| P-439 | 587 | 2026-10-29 | THE CLOCK: move count or geodesic flow? | MEDIUM | **LEAD** | host: THE CLOCK (absorbs P-413, P-438, P-440, P-477, P-478, P-479) | clock |
| P-440 | 588 | 2026-10-29 | THE PURE MOVE CLOCK | LOW | **MERGE** | -> P-439 (computed only in audit/drafts/briefing_2026-10-29/) | clock |
| P-443 | 591 | 2026-10-29 | INHERITED ASSUMPTIONS | LOW | **ANSWERED** | THE_CLOCK_AND_THE_NEXT_ATTACK_2026-10-29.md section 6 (headed P-443); docs/FRAMING_LEDGER.md (B1827) | framing |
| P-449 | 597 | 2026-10-29 | values at the CM points | LOW-MEDIUM | **MERGE** | -> P-419 (table in audit/drafts/p449/, unbanked; fate P-527) | selection |
| P-450 | 598 | 2026-10-29 | the three-generation curve as T₁₅ | LOW | **MERGE** | -> P-419 | selection |
| P-453 | 601 | 2026-10-29 | flux as the puncture degree | LOW | **LEAD** |  | lepton factor |
| P-454 | 602 | 2026-10-29 | THE WEIL FILTER | MEDIUM-LOW | **MERGE** | -> P-411; its "never tried since B1600" misses B355, B413, B214/B283, B587/B588 | line class |
| P-455 | 603 | 2026-10-29 | THE PERIOD AVERAGE | MEDIUM-LOW | **MERGE** | -> P-022 | tau selection |
| P-456 | 604 | 2026-10-29 | a least-description line rule | LOW | **MERGE** | -> P-411 (orders 3,6,7,8,9 split before 10: a least-order rule needs a hierarchy clause sealed first) | line class |
| P-457 | 605 | 2026-10-29 | the 12 behind the convention that sets Im τ | LOW-MEDIUM | **MERGE** | -> P-373 (with P-398) | tau selection |
| P-458 | 606 | 2026-10-29 | the spin connection as L250's background | MEDIUM | **LEAD** | sibling of P-330 (B940's instrument, debt P-540); P-424 way (d) | C10 |
| P-459 | 607 | 2026-10-29 | Criticality as m_H | LOW | **LEAD** | LOW; blocked behind a Higgs potential (P-536) | Higgs sector |
| P-460 | 608 | 2026-10-29 | Doublet legs on a spin structure | MEDIUM-HIGH | **LEAD** | untouched; cheapest structural probe of D (debt P-355) | lepton factor |
| P-461 | 609 | 2026-10-29 | The Dabholkar–Hull valley and FPST | MEDIUM | **LEAD** | (a) DH valley; (b) FPST -> P-323 | theta-bar |
| P-462 | 610 | 2026-10-29 | B707's three bridge tests, arithmetic Chern–Simons | LOW | **ANSWERED** | B708 ran B707 test 1 (FINDINGS:1-4, MEET); B905; B1108, B1156 close the line; B707's verdict line stale (debt P-334 class) | arithmetic CS |
| P-463 | 611 | 2026-10-29 | Two E₈'s | LOW-MEDIUM | **MERGE** | -> P-415 | towers |
| P-465 | 613 | 2026-10-29 | The principle as the selection | LOW | **ANSWERED** | THE_CLOCK doc:65 (row E) and section 4: no hierarchy from the principle followed literally; residue -> P-439 | clock |
| P-466 | 614 | 2026-10-29 | The tower flow as the selection | MEDIUM-HIGH | **LEAD** | the selecting dynamics for the towers (child of P-415) | towers |
| P-468 | 616 | 2026-10-29 | Picked in combination | LOW | **ANSWERED** | form 2 HARVEST row 1475 VERIFIED (S259, main's own code); form 4 THE_CLOCK doc:66, :152; form 3 = P-475 | clock |
| P-474 | 622 | 2026-10-29 | Door D, a clock-free observable | LOW | **SUPERSEDED** | -> P-555 (HARVEST row 1513, NOT FOUND as scoped) | CKM corners |
| P-475 | 623 | 2026-10-29 | Door E, the rising factor | MEDIUM | **LEAD** | absorbs P-468 form 3 | tau selection |
| P-476 | 624 | 2026-10-29 | The action weight is a third clock | LOW | **DEBT** | low rank, once vol(L^aR) -> Whitehead volume is confirmed (minutes): B1722 W2 headline, LAW_MAP row 319, THE_WEAVE.md:854 owe a scope sentence | gravity/L154 |
| P-477 | 625 | 2026-10-29 | Thermal clocks | LOW | **MERGE** | -> P-439 (LOW; decline candidate if unread) | clock |
| P-478 | 626 | 2026-10-29 | The literature transfers | LOW-MEDIUM | **MERGE** | -> P-439 | clock |
| P-479 | 627 | 2026-10-29 | The likelihood design | LOW | **MERGE** | -> P-439 | clock |
| P-485 | 633 | 2026-10-29 | The plenitude reframing | HIGH | **MERGE** | -> P-487 (P-487 carries the unrun exclusion half whole; consistent with S296's decline) | support test |
| P-487 | 635 | 2026-10-29 | The support test on the whole interaction | HIGH | **LEAD** | host: the support and exclusion test (absorbs P-485) | support test |
| P-491 | 639 | 2026-10-29 | L1, the celestial reading of m004's Maass spectrum | LOW | **LEAD** | LOW; decline candidate (nothing for the 19 by the seat's own statement) | gravity |
| P-493 | 641 | 2026-10-29 | L3, the sign of space's curvature as a sealed look | LOW | **LEAD** | LOW; decline candidate | gravity |
| P-494 | 642 | 2026-10-29 | A CM sighting, disclosed | LOW | **SUPERSEDED** | -> P-527 (DEBT #61); it never reached B1825 PREREG section 7 Disclosed (256-270) | selection |
| P-523 | 671 | 2026-10-30 | The vacuity calibration and the controls | LOW | **ANSWERED** | B1825 PREREGISTRATION section 4 (lines 95-190, NOT VOID at 154-158); unpaid FN populations (:181) -> P-578/P-585 | cards |
| P-526 | 674 | 2026-10-30 | The web seat's second code as Step B's third opinion | LOW | **SUPERSEDED** | lapsed at the seal; B1825 FINDINGS:15-20 and HARVEST row 1515 | cards |
| P-531 | 679 | 2026-10-30 | Which typing fixes the generations' metric | MEDIUM | **LEAD** | flag to P-585/P-576: H not forced on the candidate's lines | normalisation |
| P-536 | 684 | 2026-10-30 | Step A's supersymmetric completion | LOW | **LEAD** | conditional on reviving B1823 | Higgs sector |
| P-537 | 685 | 2026-10-30 | What fixes the normalisation of modular forms used as couplings | LOW–MEDIUM | **LEAD** | merge candidate with debt P-025 (same normalisation ambiguity) | normalisation |
| P-538 | 686 | 2026-10-30 | The price of a principled line on Step B's card | LOW | **ANSWERED** | B1825 PREREGISTRATION.md:108-113 (main's S276 ruling); read-out -> P-556 | cards |
| P-543 | 691 | 2026-10-30 | Two declared directions structurally dead menu-wide | LOW | **ANSWERED** | B1825 PREREGISTRATION.md:190-195 ("R and t = -5/288 are structurally dead") | cards |
| P-554 | 702 | 2026-10-31 | The six do not compress, even at a frame address | LOW | **ANSWERED** | B1825 PREREGISTRATION.md:176-178; FINDINGS.md:59-60; lesson in FL-13, P-574, P-575 | cards |
| P-555 | 703 | 2026-10-31 | The masses and the mixing at different addresses: the two-locus hatch | HIGH | **LEAD** | host: the CKM corners (children P-566, P-583, P-591 RI-1; absorbs P-474, P-558) | CKM corners |
| P-556 | 704 | 2026-10-31 | B1825's post-run read-outs not yet computed | LOW | **LEAD** | LOW; post-run read-outs | cards |
| P-558 | 706 | 2026-11-03 | FR-COV | LOW | **SUPERSEDED** | -> P-566 (B1826 FINDINGS:45-52; B1827 section D) | CKM corners |
| P-562 | 710 | 2026-11-03 | The Higgs's own hypercharge twist | LOW | **ANSWERED** | = P-324 DONE (register l.472, B1744: the twisted Higgs is even); FRAMING_LEDGER.md:60 | CKM corners |
| P-564 | 712 | 2026-11-03 | The cover framing: generations as the three sheets of m004's 3-fold co | MEDIUM | **LEAD** |  | three generations |
| P-566 | 714 | 2026-11-03 | The sector-odd singlet | HIGH | **LEAD** | the one computed mechanism lifting the corner inversion; RI-1 (P-591) its candidate answer | CKM corners |
| P-567 | 715 | 2026-11-03 | The lines as centre Wilson lines: does any Z₅ × Z₃ line give the Georg | LOW–MEDIUM | **MERGE** | partly answered at the seat (W182, HARVEST row 1542, not re-run on main); remainder -> P-593 item 2 | lepton factor |
| P-568 | 716 | 2026-11-03 | Relations and rigid outputs | MEDIUM–HIGH | **LEAD** | first half computed post-pin by the web seat (fe2f972cd, unharvested); second half -> P-585 only | relations |
| P-569 | 717 | 2026-11-03 | θ̄ as a constraint | MEDIUM | **MERGE** | -> P-323; using it as a selector spends a P-585 held-out target | theta-bar |
| P-570 | 718 | 2026-11-03 | Running and the allowance | MEDIUM | **MERGE** | -> P-574 (same day, sharper); past negatives -> debt P-590 | recognition |
| P-572 | 720 | 2026-11-03 | The nine with no frame | HIGH | **LEAD** | with P-396 (typed PROCESS) and P-591's FL-05 item; scoreboard half -> P-579 | nine with no frame |
| P-574 | 722 | 2026-11-03 | The scale and the running | HIGH | **PROCESS** | host of one bar amendment (absorbs P-570, P-575, P-576, P-582); a precondition of P-585's card | recognition |
| P-575 | 723 | 2026-11-03 | A declared theory error | MEDIUM–HIGH | **MERGE** | -> P-574 | recognition |
| P-576 | 724 | 2026-11-03 | The frame's own length | MEDIUM–HIGH | **MERGE** | -> P-574 | recognition |
| P-578 | 726 | 2026-11-03 | Object and rival nulls | MEDIUM–HIGH | **LEAD** | the object and rival nulls (same frame on +-LLLR, m003); precondition of P-585 | recognition |
| P-582 | 730 | 2026-11-03 | Existence before sealed looks | MEDIUM | **MERGE** | -> P-574; an unsealed existence scan is itself a look (LOOK_LEDGER) | recognition |
| P-583 | 731 | 2026-11-03 | The leptons read the adjugate | MEDIUM | **LEAD** | child of P-555; our six cannot sit on order-5 lines (P-590 via D) | CKM corners |
| P-585 | 733 | 2026-11-03 | The candidate family's confirmation: THE SIX ON THE STRIP at level 2 | HIGH | **LEAD** | the decisive one; absorbs P-568's second half | strip candidate |
| P-591 | 739 | 2026-11-03 | The retrieval sweep's candidates and asks; RI-1, the signed Laurent co | HIGH | **LEAD** | split: RI-1 -> P-566; asks -> PROCESS; RI-2..RI-8 an index | CKM corners |
| P-593 | 741 | 2026-11-03 | The harvest's new questions | MEDIUM | **LEAD** | split: Theorem 18C item -> debt P-355 | harvest questions |

---

## PART IV — THE ROWS (the six readers' blocks, in ID order)

*Each block: the idea; its status on the record with pointers; potential; first computation and cost; the reader's proposed disposition. Where Part I's adjudication differs from a block (P-032; the merge hosts chosen across chunks), Part I governs.*

### P-020 — the couplings as overlap integrals of the fibre's zero modes (register line 168; LEAD; L251)
- **Idea:** compute the Yukawas as Kaluza–Klein overlaps of the fibre's flux zero modes, so the coefficients are computed and not free.
- **Status on the record:** **computed.** B1800 (PROVED, data-free) does L251 as stated: every allowed bulk overlap is CIM's theta closed form; Wilson-line conservation gives B1636's parity pattern, but Y_pq ∝ η^{3/2}θ_r^{−1/2}, not θ_r² (arc_verdict.json claim line; FINDINGS §3 (c), lines 95–99: "No coefficient. What remains is τ and five complex Higgs components"). The point and residue versions were computed earlier (B1642, B1644, B1653; the currency note at `docs/OPEN_LEADS.md:5`). L251's heading now reads "DISCHARGED by B1800" (`docs/OPEN_LEADS.md:3853`, main's working-tree mark) and its dated note of S233 (line 3872) records the stale status. The row was left open after the work: the known stale-row failure.
- **Potential:** LOW now. It was answered, and the overlaps are not B1656's flat-frame coupling (B1800 FINDINGS §4). Its live heir is P-403 (the flux design).
- **First computation:** none owed.
- **Proposed disposition:** **ANSWERED.** Close DONE with B1800 (`frontier/B1800_the_couplings_as_overlaps_of_the_fibres_zero_modes/`) and `docs/OPEN_LEADS.md:3853`/3872.

### P-022 — τ has two roles: integrated in the index, evaluated in the couplings (register line 170; LEAD; L251)
- **Idea:** the three are counted by an index over M₁,₂, where τ is integrated over (W45/W46, B1641), while the couplings evaluate forms at one τ. A consistent Kaluza–Klein reading would integrate the couplings over the same space and leave no τ to choose.
- **Status on the record:** **not answered.** L251 promised to "give τ one role" (`docs/OPEN_LEADS.md` L251 "Why it matters"). B1800 does the overlaps over the fibre E_τ at fixed τ, and τ remains a free input (B1800 FINDINGS lines 95–99). Nothing integrates a coupling over the base. Against it: the surface frame's Petersson norms diverge at the cusp (P-134, register line 282, closed as DONE by changing the frame, not by a regularised integral). The nearest open rows are P-455 (a Petersson-weighted period average of the couplings, "no free point"; register line 603) and P-069's orbit-average half.
- **Potential:** MEDIUM–HIGH. "τ is not selected" is one of the programme's top walls. If the couplings were overlaps over the four-dimensional space whose index gives the three, τ would stop being an input: one fewer free choice, with fixed numbers (triple Petersson / Rankin–Selberg-type integrals). Against it: divergence at the cusp (P-134), and Zagier-type renormalisation is itself a choice.
- **First computation:** write W46's four-dimensional zero modes as sections over the universal curve on M₁,₂ (θ-characteristic sections times weight-k forms in τ, B1641's lifts). Compute the triple overlap ∫_{M₁,₂} with the hyperbolic measure. Check convergence at the cusp first; only then (sealed) any ratio. Cost: 1–3 days; data-free up to the comparison.
- **Proposed disposition:** **STILL A LEAD**; **merge** with P-455 (the period average) and P-069's orbit-average half under one heading: "averaging τ instead of choosing it".

### P-023 — the near-fixed-point mechanism on the ruled branch, fields at their own weights (register line 171; QUEUED; —)
- **Idea:** near the fixed points (ω, i), with each field at its own representation and weight, the residual symmetry might produce a hierarchy as powers of the displacement.
- **Status on the record:** **largely superseded in the live frames; untouched on the ruled branch itself.** B1691 (PROVED) computed the near-ω exponents for covariant sections at every weight to 23/2: they follow the residual ℤ₃ charge, k mod 6 (arc_verdict claim line). B1657 (PROVED) computed the symmetric point at ω and two small-departure laws, with D a cone at ω under the canonical end (arc_verdict claim line). The completion map's C5 (the δ-power pattern at the canonical end) stays QUEUED (`docs/THE_COMPLETION_MAP.md:34`), and P-257 is escalated onto the same C5. The ruled branch is not retired, only τ = ω on it (`docs/RETRACTIONS.md:218`; `docs/LAW_MAP.md:282`), so its near-ω regime is formally uncomputed.
- **Potential:** LOW. The candidate six live on order-5 and order-10 lines at Im τ ≈ 3, far from ω. The near-ω mechanism cannot act on those lines (S fixes only orders 1, 2; ST only 1, 3: P-327's note, register line 475; P-023's own escalation).
- **First computation:** C5 as written, DR at B1667's canonical end with one displacement δ = |τ − ω|, reading the powers δ² : δ : 1. Cost: hours; data-free.
- **Proposed disposition:** **SUPERSEDED** in substance (B1691, B1657). **Merge** into P-257 (C5) and close this row, or keep a single C5 row.

### P-032 — the converse: F = 8 only on the discriminant-5 geodesics (register line 180; QUEUED; —)
- **Idea:** prove that Σ_p|θ_p/η|⁴ = 8 holds only on the discriminant-5 (golden) geodesics, not elsewhere.
- **Status on the record:** **numerically checked in a bounded region, not proved.** B1723's preregistration records: "On 41 vertical lines of the fundamental domain up to Im τ = 4, F − 8 changes sign exactly once, on the arcs, to 4 × 10⁻¹⁵. So in that region the valley is the arcs and nothing else" (`frontier/B1723_the_golden_valley/PREREGISTRATION.md:25–27`). No proof is on record. Above Im τ = 4 a cusp asymptotic (F grows like |q|^{−1/6}) would finish the job.
- **Potential:** LOW. The golden valley sits too low for the frame's hierarchy (B1723, NEGATIVE), and nothing current rests on the converse.
- **First computation:** a certified level-set argument: the cusp bound for Im τ > 4, plus interval arithmetic on the compact remainder. Cost: hours to a day; data-free.
- **Proposed disposition:** **ANSWERED as far as the record uses it.** Close DONE with B1723 PREREGISTRATION.md:25–27, graded "numerical, Im τ ≤ 4". A proof is a LOW pure-math item and can be declined. Related to the debt P-031 (discriminant-5 specialness).

### P-033 — the McKay ladder (levels 3/4/5 ↔ 2T/2O/2I ↔ E₆/E₇/E₈) never unified (register line 181; LEAD; L252)
- **Idea:** the same ladder appears in the July record (B997, B644, B248, B981) and in the October weave (W3/B1601 at level 3, the θ-squares of Γ(4), the degree-5 modular equation). Is the weave's golden structure the shadow of a level-5 (2I, A₅′) structure already on record?
- **Status on the record:** **partly answered at the level of a rule; the computation never ran.** GENESIS F-MC now carries the ladder's rule R1 (v1.56–v1.58; `GENESIS.md:251`): the rungs are Δ(2, 3, N), finite exactly for N = 2–5, with the end at 5 forced by the moves' orders (W153). The rungs' groups form no chain, so the single container E₈ is adopted by ruling (B1752, B1754; `frontier/B1752_genesis_v1_57/FINDINGS.md:9–15`). The level-5 rung was tested on the lines: the SM seat's prediction (P-387 DONE) became B1755, which found that it "holds only through the slope … not an order, a five-ality class or a level-5 rung as such" (`frontier/B1755_*/FINDINGS.md:32, 52`). B1733 found the level-5 deck involution X₁(5) → X₀(5) on the order-5 lines (v ↔ 2v, which no thread-built rule chooses). L252's own first computation (the weight-1 A₅′ triplet against B640's traces and the golden coupling) has never run (`docs/OPEN_LEADS.md:3888`, main's mark).
- **Potential:** MEDIUM. The candidate's carriers are the order-10 lines (2/5, odd/10), and what selects that class is debt #2 (P-384: "mostly a pick"). The July level-5 corpus has the tick's Γ(5) lift as an order-10 rotation with trace φ (B674) and the hearing representation factoring through SL(2, 𝔽₅) = 2I (B644, B640). That is the natural place for a principle selecting the slope 2/5 and the offset. Known against: B1755 (the rung as such does not select), B1733 (v ↔ 2v is unbreakable by thread rules), B685 (no 5-adic structure in the intrinsic realisations).
- **First computation:** reframe toward P-384. Compute the fixed and permuted sets, on the flat lines of order 10, of the tick's level-10 lift (B674's order-10 element) and of B644's SL(2, 𝔽₅) image, and ask whether (2/5, odd/10) is an orbit or fixed class there. Data-free, hours. L252's original computation (the A₅′ triplet on the ruled branch) is a day, and LOW, since the golden coupling is not the live frame (B1800).
- **Proposed disposition:** **STILL A LEAD**, re-aimed at P-384. **Merge** P-034, P-040 and P-041 into it (all four point at L252).

### P-034 — the July level-5 golden corpus is cited by no B1400+ arc (register line 182; LEAD; L252)
- **Idea:** the July arcs B640, B674, B685, B691, B694, B695, B699, B702, B705 hold level-5 golden results that the weave never reads.
- **Status on the record:** **still orphaned.** In a citation count over frontier/B14xx–B18xx FINDINGS, only B674 is cited (by B1697, the scan for misses, item 5). The others have zero citations. B702 is RETRACTED (its swap/weld law). B685 is NEGATIVE: no 5-adic structure, so "no framework-derivable generator produces the flavor streams".
- **Potential:** MEDIUM, through P-033 (see there). On its own, a citation gap.
- **First computation:** as P-033's reframed computation; B644 and B674 are the two corpus items with content for the lines.
- **Proposed disposition:** **DUPLICATE**; merge into P-033.

### P-035 — the crossing's spin-structure results (B1477–B1483) against the θ-characteristics (register line 183; QUEUED; —)
- **Idea:** the triplet's θ-characteristics are the fibre's even spin structures. The crossing's spin structures carry the chirality bit and the hand. Read the two as one datum.
- **Status on the record:** **half done.** The join was named (B1651's second addendum §2: v_r = R_r S_r with Szegő kernels, so B1649's R·R = 0, B1650's O6 and B1651's isotropy are one identity; `frontier/B1651_where_a_higgs_can_couple/ADDENDUM_2026-10-14_the_szego_reading.md:49`, "the join P-035 asks for"). The crossing arcs were later used: B1483's spin end curves as τ candidates (B1697 item 5; B1702, NEGATIVE), and B1479/B1481/B1482 re-read by B1662 (the pull-back generates the place where a hand can register). No arc does the row's remaining "reading arc against B1477–B1483".
- **Potential:** LOW–MEDIUM. It bears on the hand and chirality, which are already graded a convention (B1640), not on the six or the CKM. A data-free observation for the reading: the tick acts on the fibre's spin structures through SL(2, ℤ/2) ≅ S₃. LR is of order 3 mod 2, so it 3-cycles the three even spin structures and fixes only the odd one, the unique MCG-invariant spin sector (B366, verdict line). So the mapping torus's spin structures (the crossing's) and the triplet live on complementary characteristics. This is my reading, to verify.
- **First computation:** the restriction map from the − word states' spin structures (B1481's classes) to fibre characteristics, against the tick's 3-cycle on the triplet. Cost: hours; data-free.
- **Proposed disposition:** **STILL A LEAD** (LOW–MEDIUM).

### P-036 — the located selections: independent coordinates or one datum (register line 184; LEAD; L253)
- **Idea:** the record's located choices (sheet, τ, cusp unit, thread, frame, weights, hand) may be one datum, not several. That is the goal's own question, "how many free numbers".
- **Status on the record:** **partly answered.** B1733 (PROVED): a thread fixes τ (its apex) and its own lines up to one bit, so two selections collapse on the thread. B1809 (PROVED): each of four frames keeps a continuous datum or an infinite menu nothing selects. B1722 (C2): neither record measure selects the data's thread. B1827's FRAMING_LEDGER now inventories the choices (FL-04 τ, FL-07 one address, FL-11 normalisation, FL-18 cutoffs) but does not analyse their dependence. Main's mark: "partly answered" (`docs/OPEN_LEADS.md:3905`). The B1409-versus-B1635 reconciliation was DECLINED (P-037, register line 185).
- **Potential:** HIGH in importance, since it is the free-number count itself. It is a framing question, not one computation, and the record has already reduced it to "which thread + one bit + the CHOSEN ledger rows".
- **First computation:** a dependency table over FRAMING_LEDGER's CHOSEN/UNSTATED rows under C1's thread rule. For each choice, record whether it is fixed by the thread (B1733), by a symmetry (B1809's fixed configurations), or by nothing. Cost: a day; data-free.
- **Proposed disposition:** **STILL A LEAD**, merged with P-038 (one L253 row), with its first computation re-stated as the dependency table.

### P-038 — orphan B471: thread pairs with tr[W₁, W₂] = −2 and where their axes meet (register line 186; LEAD; L253)
- **Idea:** list all thread pairs with a parabolic commutator. Check whether the punctured tori they generate, and their axis crossings, sit where the couplings are golden or degenerate, collapsing several selections.
- **Status on the record:** **never run** (`docs/OPEN_LEADS.md:3905`). A classical answer is available. B471's content is Cohn/Markov (`docs/RETRACTIONS.md:28`; THEOREM_REGISTRY T-COHN, `docs/THEOREM_REGISTRY.md:27`). For A, B ∈ SL(2, ℤ) hyperbolic, tr[A, B] = −2 is the Markov–Fricke equation (x² + y² + z² = xyz). Such a pair generates a finite-area once-punctured-torus group, of index 6 in PSL(2, ℤ). Torsion-free one-cusped index-6 subgroups of PSL(2, ℤ) form a single conjugacy class (I counted the transitive Z/2 * Z/3 actions on six points: 120 actions, one class), namely the commutator subgroup Γ′. So every such pair generates a conjugate of Γ′. The generated torus is always the hexagonal modular torus (conformal class ω), and the list is infinite (the Markov tree: traces 3 × Markov numbers). This is a reading plus a small check, to be verified by main.
- **Potential:** LOW. If the reading stands, the test's premise "if the list is finite" fails. All tori coincide at the hexagonal one (ω), where the record finds no hierarchy (B1691; τ = ω retired as tested). The only remaining datum is which pair of Markov geodesics and their crossing point, and that is a menu (B1809).
- **First computation:** verify the reading: enumerate thread pairs to length ~10 with tr[W₁, W₂] = −2, check the Markov condition and the index of ⟨W₁, W₂⟩. Cost: an hour; data-free.
- **Proposed disposition:** **STILL A LEAD** until checked. If the reading holds, close it as answered by the classical theorem (P-036 keeps L253).

### P-039 — orphan B345: ℤ/3 charges force an anti-diagonal texture (register line 187; QUEUED; —)
- **Idea:** check whether B345's ℤ/3 charge-conservation texture is the order-3 cyclic structure of B1656's coupling Y (as re-pointed by the escalation, to B1736).
- **Status on the record:** **untouched** (B345 is cited by no B1400+ arc). B345 itself grades the rule "generic to any ℤ/3" (`frontier/B345_z3_deviation_texture/FINDINGS.md`, "Tier"). The order-3 structure of the live frame is already diagonalised: B1657's order-3 move at ω has eigenlines R, R̄, n; B1736 writes Y exactly and finds its channel triplet and the order-3 icosian.
- **Potential:** LOW. Any ℤ/3-covariant quadratic coupling has this texture in the charge basis. The check cannot select anything.
- **First computation:** a 10-minute reading. In B1657's eigenbasis, list which entries of Y are allowed at ω.
- **Proposed disposition:** **DECLINE** (the escalation of 2026-10-28 itself offers "or decline then"). Reason: generic (B345's own tier), and the live frame's ℤ₃ is already diagonalised (B1657, B1736).

### P-040 — orphan B640: im ρ = 2I × ℤ/3, tr ρ(RL) = −1/φ (register line 188; LEAD; L252)
- **Idea:** the "hearing group" image is 2I × ℤ/3, the level-5 (A₅′) group of modular flavour models.
- **Status on the record:** **orphaned** (zero B1400+ citations). B644 (PROVED) says the hearing representation factors through mod-5 reduction into SL(2, 𝔽₅).
- **Potential:** MEDIUM, through P-033.
- **First computation:** in P-033.
- **Proposed disposition:** **DUPLICATE**; merge into P-033.

### P-041 — orphan B997: golden the unique metallic grammar whose own-conductor shadow is a McKay group (register line 189; LEAD; L252)
- **Idea:** |SL(2, ℤ/N)| is a McKay order exactly for N ∈ {3, 4, 5}, and the golden grammar is the one whose conductor (5) lands on 2I → E₈.
- **Status on the record:** cited by B1402, B1405 and B1601 (B1601 ties level 3 to F-MC; `frontier/B1601_*/FINDINGS.md:16`), not by any arc from B1640 on. Its content overlaps GENESIS F-MC's ladder rule, which reaches "the end at 5" from the moves' orders (W153) and records E₈ as the container "adopted by the ruling, not derived" (`GENESIS.md:251`; B1752).
- **Potential:** MEDIUM for the foundations, LOW for the 19. B997 is a candidate to earn F-MC's container clause from the object's own conductor rather than by ruling. LR has discriminant 5 and det(LR + I) = 5, and B997's statement is that golden is the unique metallic grammar whose shadow SL(2, ℤ/5) = 2I is McKay, i.e. E₈. That would turn one ruling into a derivation.
- **First computation:** a reading of B997's hypotheses against v1.57/v1.58's container clause; hours; data-free. Main or the owner decides whether it amends F-MC (through adoption/amend.py).
- **Proposed disposition:** **STILL A LEAD**, merged into P-033 but with this foundations angle stated.

### P-042 — orphan B1143: B−L a genuine fourth Cartan direction, anomaly-free, against the neutrino sector (register line 190; QUEUED; —)
- **Idea:** if the object's B−L is a genuine, anomaly-free gauge direction, Majorana masses are forbidden unless B−L breaks. That bears directly on whether neutrinos are Dirac.
- **Status on the record:** **untouched as asked.** B1143 is cited by no B1400+ arc. B−L appears later only in B1805 (matter parity z₂ = (−1)^{3(B−L)}, `frontier/B1805_*/FINDINGS.md:28`), whose verdict also records that "only 1, 10, 16, 16bar, 45 localise (no 126)" in Witten's G₂ frame. No renormalisable Majorana mass appears in that frame, a hint, not a test.
- **Potential:** MEDIUM. The live prediction P10/P10′ reads neutrinos as Dirac, and the debt P-157 (#7) questions that reading. A structural B−L that the frame's Higgs content does not break would make the Dirac reading a consequence, not an assignment.
- **First computation:** on the banked 27 with B1143's family c, compute the B−L charges of the frame's Higgs content and of the Sym²T (Majorana) and T̄⊗T (Dirac) bilinears. Ask whether any flat line w on record breaks B−L. Cost: hours; data-free.
- **Proposed disposition:** **STILL A LEAD**, cross-referenced to P-157. It could inform the debt's closing.

### P-043 — orphan B1430: the SM unique in E₆ only when the 27 branches as one generation + 10 + 1 (register line 191; QUEUED; —)
- **Idea:** B1430 shows that SU(3) × SU(2) × U(1) sits in E₆ uniquely only if the 27 is required to branch as one SM generation + 10 + 1 (otherwise 8177 branchings). Check FK11's dictionary against that counted condition.
- **Status on the record:** **untouched.** B1430 is cited by no B1400+ arc. The branching condition does not appear in IDENTIFICATION_LEDGER, KIND_TABLE, THE_CLAIM or GENESIS (grep for B1430, B1366 and "one generation plus" is empty). FK11 is UNEARNED (`GENESIS.md:443`). The hypercharge-forcing theorems already carry a debt (P-233).
- **Potential:** MEDIUM. Under THE_TOWERS (SU(5) ⊂ SO(10) ⊂ E₆), the branching 27 = 16 + 10 + 1 is automatic from the SO(10) tower. So the tower chain could turn B1430's selection into a consequence, removing one counted input. Conversely, if F-MC's "hypercharge direction" silently uses this uniqueness, it is a debt.
- **First computation:** read F-MC's hypercharge clause and T-Y18/T-TWO-ORBITS (with P-233) for whether they assume the one-generation branching. Then state the condition as a counted input, or derive it from the tower. Cost: hours; data-free.
- **Proposed disposition:** **STILL A LEAD**. It **could become a DEBT** if the F-MC read finds the condition used unstated. Merge candidate with the towers rows (P-415, P-416).

### P-044 — orphan B1484: sin²θ_W's gate ratio, cited only by docs and L250 (register line 192; QUEUED; —)
- **Idea:** B1484's arithmetic (the gauge ratio B for the desert, SUSY with split Higgs, complete multiplets) should be read against the record's gauge sector.
- **Status on the record:** **no longer orphaned; engaged.** B1795 (NEGATIVE for a structural doublet–triplet split): "nothing here moves the one-loop gauge ratio from B1484's ½ for complete multiplets" (`frontier/B1795_*/FINDINGS.md:78`). B1801: the torsion leaves the one-loop sin²θ_W unchanged for any Q (verdict line). B1802 (PROVED): Witten's doublet–triplet topology on the even fillings. B1803: the first model cannot be built at distinct points (P-409 DONE, register line 557). B1484 is cited by B1643, B1795, B1801 and B1802. The row's premise "cited only by docs and L250" is stale.
- **Potential:** MEDIUM for the gauge couplings, but carried by P-396 (relative thresholds) and the Witten-split line, not by this row.
- **First computation:** none for this row; the gauge work is P-396's.
- **Proposed disposition:** **ANSWERED** (the orphan reconnected and its question engaged). Close DONE with B1795 FINDINGS:78, B1801, B1802/B1803; the live gauge question stays on P-396.

### P-045 — orphan B1251: the E₆ cubic's 45 triples, D2-odd, against one-27_H couplings (register line 193; QUEUED; —)
- **Idea:** the E₆ cubic is uniformly D2-odd on its 45 support triples (B1251 (2)). A single 27_H inherits that structure, which fixes which sector bilinears a one-Higgs coupling reaches.
- **Status on the record:** **untouched as asked** (B1251 is cited by no B1400+ arc). The cubic's SM-graded Yukawa-support table exists (B884). P-014 closed by scoping B1637 ("one 27_H relating the sectors is a different test"). The live diagnosis is that the CKM wall is the Higgs construction (B1826, B1827: one Higgs drags both quark types; the adjugate / singlet ingredient). FL-07 "one address" is CHOSEN (`docs/FRAMING_LEDGER.md:36`).
- **Potential:** MEDIUM. If the frame's Higgs is a 27_H of the tower's E₆, the cubic forces the coupling's sector structure, possibly the very singlet-plus-mirror (adjugate) pattern B1827 needs, or its exclusion. Either way it constrains the Higgs construction that blocks the CKM.
- **First computation:** from B884's support table, list the one-27_H couplings of the 16·16, 16·10 and 10·10 pieces. Check whether the D2-odd sign forbids or forces a relative sign between the up and down Yukawas (the "opposite signs for the two quark types" of S289). Cost: hours; data-free.
- **Proposed disposition:** **STILL A LEAD**; merge candidate with the towers rows (P-415/P-416) and with P-566 (the adjugate reading).

### P-046 — orphan B1089: every matter datum interface-resident, the coupling boundary-evaluated, against L251 (register line 194; QUEUED; —)
- **Idea:** B1089 says the coupling is boundary-evaluated. L251 asked for bulk overlaps. Which is it?
- **Status on the record:** **answered in substance.** Both versions are computed. Boundary (residue/point): B1642, B1644, B1653, a rank ≤ 2 point coupling with θ_r² but antisymmetric. Bulk: B1800, symmetric and ∝ θ_r^{−1/2}. B1800 FINDINGS lines 92–93 state the contrast. B1089 itself is not cited, but the question it raises is settled by the two computations.
- **Potential:** LOW.
- **First computation:** none.
- **Proposed disposition:** **SUPERSEDED** (B1800 FINDINGS:92–93; B1642, B1653). Close DONE.

### P-058 — the audit lane's charged three on a connected double cover, against T-NO-INDEX-IN-THREE (register line 206; QUEUED; —)
- **Idea:** the physical-bridge (audit) lane reports three left-handed 10 + 5̄ with gauge currents on a connected double cover of a 2D punctured elliptic object with a supplied E₈ parent. Is this B1606's ±3 in another dress, or new?
- **Status on the record:** **never verified on main** since registration. It is listed first among unverified lane results in `docs/THE_INTEGRATION_CENSUS_2026-10-13.md:48–53` ("the only result anywhere on the record that yields three with gauge content"). The scripts are on `origin/audit/physical-bridge-2026-09-05` under `reports/physical_bridge_2026_09_05/silver_cover_families_2026_10_12/` and `…/silver_cover_currents_2026_10_12/`. The lane self-grades it "CONDITIONAL physical action-level positive, not a derivation of three physical generations" (its `silver_cover_cubic_2026_10_12/FINDINGS.md`). B1689 (the fibre's E₈ frames give at most two complete generations per sub-tower) and B1604 (no index in three on covers) stand against it on main's objects.
- **Potential:** HIGH if new, likely LOW if it is the ±3 in another dress. Three generations exist on the record only as an index by selection. An independent three with gauge content would be the most consequential of this chunk, and the boundary is "unselected", so it is probably a selection again.
- **First computation:** re-run the families and currents packages at the lane's pin in a worktree. Then test whether the three equals n(|Λ₊| − 3) for the cover's Λ (B1641's formula); if so, it is the same ±3. Cost: a day; data-free.
- **Proposed disposition:** **STILL A LEAD** (verification owed). **Merge** P-059 and P-060 with it as "the audit lane's 2026-10-12/13 silver-cover dossier".

### P-059 — the audit lane's non-zero inter-family cubic on the cover (register line 207; QUEUED; —)
- **Idea:** on the same cover the charged cubic is non-zero, against a zero cubic on the earlier selective domain: the count depends on the boundary.
- **Status on the record:** **unverified on main.** The lane's FINDINGS (`silver_cover_cubic_2026_10_12/FINDINGS.md`, on the lane's branch) report Q d^c L non-zero, e L L and u d d exactly zero by cancellation of Stokes terms. These are the 10·5̄·5̄ (R-parity-violating type) trilinears, not Yukawas.
- **Potential:** LOW–MEDIUM. It bears on matter parity (P-414; B1805 found the tower route NEGATIVE in Witten's G₂ frame), not on masses or the CKM.
- **First computation:** with P-058's re-run, the lane's `execute.py`/`reference.py` in that folder; hours.
- **Proposed disposition:** **DUPLICATE** of P-058's dossier; merge.

### P-060 — the audit lane's E₈ embedding of the puncture coefficient, its Yang–Mills lift of the cusp unit, its zero Higgs-pair quartic (register line 208; QUEUED; —)
- **Idea:** three conditional lane results: a join of the puncture coefficient into E₈; a 4D YM lift of FK10's cusp unit (the lift duty, not a selection); a Higgs quartic that vanishes on its domain.
- **Status on the record:** **unverified on main** (`docs/THE_INTEGRATION_CENSUS_2026-10-13.md:63–68`; the quartic files `reports/physical_bridge_2026_09_05/MIRROR_QUARTIC*` on the lane's branch).
- **Potential:** LOW. The cusp unit stays a tagged postulate (FK10; the debt P-056 on W47). A zero quartic gives no Higgs mass, and m_H has no frame (FL-05).
- **First computation:** with P-058's dossier; the YM lift first, since it touches FK10. A day.
- **Proposed disposition:** **DUPLICATE**; merge into P-058's dossier.

### P-062 — engaged too little: W49, W25, W36, W48 (register line 210; QUEUED; —)
- **Idea:** four SM-seat results the weave under-read: W49 (one zero mode three times, T = ℓ ⊗ M), W25 (self-conjugate bundles, so no FK11 dictionary from them), W36 (no SU(5) chirality on a 2D object), W48 (three need 24 lattice-free chiral bosons).
- **Status on the record:** **largely engaged since.** W49 is built in: B1642 FINDINGS:55 (M the imaginary quaternions), B1800, B1822 FINDINGS:116 (W49 stated the generation bundles' isomorphism before B1654), and P-087 DONE. W48 is engaged in the frame tribunal's D2 cell (B1652 FINDINGS:78, "a c = 24 source would (W48)"). W25's conclusion is carried by GENESIS FK11 v1.27, on B1604's different argument (`GENESIS.md:443`). W36 is cited only as context (B1616 FINDINGS:12, 31).
- **Potential:** LOW.
- **First computation:** none, beyond noting that W48 and W36 are seat results not re-run on main (they sit in the tribunal cell as "[sealed + seat]").
- **Proposed disposition:** **ANSWERED** for W49 and W25 (pointers above). Close DONE, or retype [PROCESS] for the remaining "W36/W48 not re-run on main".

### P-063 — the Banking Seat's Gate 9: C₂(p) = [96p(1 − p) − 25]/432 < 0 (register line 211; QUEUED; —)
- **Idea:** in the Banking Seat's joint weave action, the two-step connected correlation of the ruled projection statistic is negative for every letter probability p.
- **Status on the record:** **not verified on main.** The source is in the gitignored intake: `audit/intake_2026_10_13/gate11/Origin_Axiom_Banking_Seat_2026_10_13/EXPANDED_POST_GATE3/09_JOINT_WEAVE_GATE_9/Gate9_Weave_Joint_Action/verify_exact.py:154–165`, which derives C₂(p) from E tr(P_g P_gh) = 2p(1 − p)/9 against the baseline 25/432. The inequality itself is elementary: 96p(1 − p) ≤ 24 < 25. HARVEST_LEDGER row 1089 (`docs/HARVEST_LEDGER.md:1137`) has it READ at headline level.
- **Potential:** LOW. A correlation sign in a seat's action statistic, with no route to any of the 19 or to the six.
- **First computation:** run the intake's `verify_exact.py` read-only (minutes), and check its definition of P_g against the record's ruled projection.
- **Proposed disposition:** **STILL A LEAD**, better retyped **[PROCESS]** (a seat result to verify, nothing resting on it). Close it once the re-run is recorded.

### P-064 — the Banking Seat's Gate 11: the abelianisations; Δ⁴ = −I₃ obstructs the sign's extension (register line 212; QUEUED; —)
- **Idea:** the central sign at Δ⁴ obstructs extending the parity sign from the moves to the fibre loops.
- **Status on the record:** **answered on main for the obstruction.** B1641 (sealed, PROVED) computed it: the geometric lift differs from the moves' by the central sign at Δ⁴, "and the Banking Seat's Gate 11 obstruction (Δ⁴ = −I₃) is this sign" (`frontier/B1641_w46_on_main_and_the_two_objects/FINDINGS.md:49`; `docs/THE_WEAVE.md:391`). The abelianisation half of the gate is the seat's (`…/11_JOINT_STATE_GATE_11/Gate11/PROOF_AND_SCOPE.md`, `verify_hilbert.py`) and has not been re-run.
- **Potential:** LOW. It is now part of B1641's parity selection rule.
- **First computation:** optionally run `verify_hilbert.py` from the intake (minutes).
- **Proposed disposition:** **ANSWERED.** Close DONE with B1641 FINDINGS:49 and THE_WEAVE.md:391, noting the abelianisation half as the seat's.

### P-069 — τ as a dynamical field: a modular-invariant potential, the orbit-averaged mixing, a Kähler valley (register line 217; LEAD; L254)
- **Idea:** let τ be a field whose potential's minimum selects it, instead of choosing it. Read the mixing as an average over the tick's orbit.
- **Status on the record:** **one third closed; the rest carried elsewhere.**
  - (a) The valley is closed in B1656's frame by B1723 (NEGATIVE as sealed; the valley sits too low).
  - (b) The potential's minimum: C6 is carried by P-287 (QUEUED). The SM seat's W154/W176 found that every record content runs to the cusp, with a necessary condition Σw ≥ 0 that the frame's content fails (register lines 435, 528). C7 (a minimum with J ≠ 0) is DONE as P-277: on mirror-free slope-2/5 classes the frame's own one-loop potential, minimised over Re τ, sits at J ≠ 0, but with no true minimum at finite height (register line 425).
  - (c) The orbit-averaged mixing of the golden coupling has never been computed (topic sweep: only B1673's unrelated orbit-averaged J). It also belongs to the older coupling, which B1800 shows is not the bulk overlap.
  - **A pointer defect for main:** L254's Review-74 mark (`docs/OPEN_LEADS.md:3925`, working tree) names C6 "the arclength average of the golden coupling's mixing" and C7 "the minimum of a modular-invariant potential". `docs/THE_COMPLETION_MAP.md:35–36` defines C6 as "a content that holds τ in the band, or W106" and C7 as "a potential minimum with J ≠ 0" (P-277, DONE). The mark mislabels both. Also stale: THE_COMPLETION_MAP's own C7 status cell still reads QUEUED (line 36), though P-277 was closed ANSWERED at S243 (register line 425).
- **Potential:** HIGH for (b), the selection of τ by dynamics, but (b) is P-287's. LOW for (c).
- **First computation:** for (b), P-287's next action (verify W154 and its 13% window on main, P-380 Stage B). For (c), P-455's period average on the live lines, not the golden coupling.
- **Proposed disposition:** **SUPERSEDED / MERGE.** (a) answered by B1723. (b) duplicates P-287 (with P-327 and P-380). (c) merges with P-455 and P-022. Close this row as merged, and fix the C6/C7 labels in L254's mark.

### P-070 — why matter sits at the common point (register line 218; QUEUED; no L)
- **Idea:** The record places the matter at the point of the character variety fixed by every move (the quaternion point); the row asks why a jointly fixed character, rather than a finite orbit of the braid group or one thread's holonomy.
- **Status on the record:** answered by pricing, not by argument. B1677 (sealed) and B1679 show a non-trivial common character exists only for two records and is the quaternion point; B1683 (GENESIS v1.50) makes "a non-trivial common character in SL(2, ℂ)" GM1's postulate in an equivalent form (GENESIS.md:111). The finite-orbit alternative the row names is answered explicitly: "Read as a finite orbit, every finite-image character persists at every n, and nothing is selected" (frontier/B1677_the_common_point_and_the_record_count/FINDINGS.md:86–87; frontier/B1682_the_word_side_of_the_record_count_verified/FINDINGS.md:57–59, "What the form assumes, named"). The holonomy alternative: B1601 (odd-trace threads reduce to the common point mod 3).
- **Potential:** LOW — the location is now a named postulate (GM1); an argument would re-derive GM1, not touch any of the 19.
- **First computation:** none owed; at most a one-paragraph scope line in GM1 naming the finite-orbit reading as the rejected alternative (already in B1682).
- **Proposed disposition:** ANSWERED — close DONE: B1677 FINDINGS:86–87, B1682 FINDINGS:57–59, GENESIS GM1 v1.50 (B1683, P-212).

### P-073 — "if the principle is the seed, we miss the field" (register line 221; LEAD; L251, L254)
- **Idea:** The owner's root diagnosis: the record has no action, kinetic or Kähler term, no dynamics for τ, and did not use the zero modes as fields; the field must come from the weave, not be added to obtain a wanted integer.
- **Status on the record:** partly worked, not answered. L251 (zero modes as couplings) is DISCHARGED by B1800 (bulk flux-mode overlaps; docs/OPEN_LEADS.md:3853, :3872); the field stage (B1642–B1658) used zero modes; a τ potential exists only as B1704's one-loop content potential (no content holds τ in the band without ~89–95 tuned net bosons) and W154/P-380 (the band costs one free number); B1823 (Step A, NEGATIVE) tried a heavy-sector vacuum for the Higgs direction. No action or Kähler term is derived; P-025 (DEBT #53) carries the Kähler import. L254's valley half closed (B1723); its remainder ESCALATED today (docs/OPEN_LEADS.md, L254 section, "ESCALATED(2026-11-04, Review 74)").
- **Potential:** HIGH as a direction (τ not selected; Higgs direction not selected), but as a row it is an umbrella — its computable content lives in P-139, P-287, P-327, P-380, P-419 and P-025.
- **First computation:** none of its own; route to P-419 (selection by inversion, the owner's main line) and P-327 (B1704's potential on the strip's lines).
- **Proposed disposition:** STILL A LEAD as the umbrella; merge candidate (fold into P-139 with P-287/P-327/P-380 named as its computable children).

### P-130 — the field's genesis, "what exists is read" (register line 278; QUEUED; no L)
- **Idea:** A derivation from the principle (PF1, PF2) that a field must exist, as the seed was derived; main's candidate fourth face of the principle, "what exists is read" (firewalled speculation).
- **Status on the record:** untouched as a derivation. It is GENESIS FK15 (OPEN; GENESIS.md:447); stated as a candidate in speculations/S_THE_FIELDS_GENESIS.md:107. New since registration: B1796 shows FK10's tagged cusp unit "reduces to the field's existence (FK15), a type identification, uniform end data and the least remainder, given Λ and the hand, none derived" (B1796 arc_verdict claim; GENESIS FK15's [v1.59] clause).
- **Potential:** MEDIUM — after B1796 the field's existence is one of four links between the principle and the generation count (three from O(δ)); a derivation would turn one of the four into a theorem, not produce a number.
- **First computation:** state, for the fibre's uniformizing Higgs (W130's typing End E ⊗ K), which of PF1–PF3 would have to force a non-zero section; data-free, days, philosophy-to-mathematics, firewalled.
- **Proposed disposition:** STILL A LEAD (its home is FK15; note B1796's link in the row).

### P-137 — L154 posed on the weave's quantised sector (register line 285; QUEUED; L154)
- **Idea:** The weave has a quantised sector (690 of 745 threads to length 12 have CS ≠ 0), which supplies B1064's missing piece for L154's gravity bridge; B1228's pin k = 1 becomes a choice; tension between c = 6 (Planckian threads) and c ≫ 1 (weave concentrates on its root).
- **Status on the record:** untouched since B1650 recorded it as a reading for main's decision (frontier/B1650_chat1s_field_and_scale_notes_verified/FINDINGS.md:45–47). Neighbours: P-476 (the action weight as a third clock, LEAD), P-492 (DEBT #60: B1088/B1034's boundary assumption, L154's AdS₃ arena); B1722 used the c = 6 action weight as a measure (NEGATIVE as sealed).
- **Potential:** LOW — bears on gravity and the scale, not on the 19; B1722 already showed the action weight at c = 6 does not select the data's thread.
- **First computation:** name L154's level and type (E₆ or A₁) on the weave's CS ≠ 0 sector and recompute B1064's obstruction (a) with it; data-free, a day.
- **Proposed disposition:** STILL A LEAD; merge candidate with P-492 (same bridge, L154) and P-476.

### P-139 — the selection principle (GENESIS FK9) (register line 287; QUEUED; no L)
- **Idea:** Every "which" on record (τ, Higgs direction, Higgs location, vacuum) comes out free, and invariant constructions pick only symmetric points with no hierarchy; the parent needs a dynamics that lands at a computable non-symmetric point.
- **Status on the record:** open, with every attempted mechanism negative: B1722 (which thread; NEGATIVE as sealed), B1723 (the valley), B1704 (contents), B1809 (four frames leave a datum free; FINDINGS:22, §7 at :235–237 lists "FK9 / P-139" as not excluded), B1804/B1808 (selection by inversion: curves, not points), B1812 (F-theory card), B1823 (Step A; FINDINGS:348, :359 cite P-139). The owner made selection by inversion (P-419) "the next main line" (P-419's 2026-10-29 note).
- **Potential:** HIGH — selection is the gap between the frame reaching the data's neighbourhood and producing it (docs/OPEN_LEADS.md:4245–4247 says exactly this); but this row is the umbrella, not a computation.
- **First computation:** none distinct from P-419's next card item (an E₆ meeting point with flux breaking, P-415) and P-287/P-380's τ-holding question.
- **Proposed disposition:** STILL A LEAD as the umbrella; merge candidate (P-073 folds in; P-419, P-287, P-380 as its computable lines).

### P-177 — the owner's "existence in time / push-back" table (register line 325; QUEUED; no L)
- **Idea:** Sizes may be set by motion, not rest; a five-item speculation-to-calculation table (H̃ for up; CP from the two isotropic vacua aS₀ + bS̄₀; the field pushes back; sizes from motion; both undecided moves allowed).
- **Status on the record:** items 1, 3, 4 answered (the row's own ESCALATED note: B1660, the 2026-10-16 note, B1720, B1722, B1734). Item 2 was to fold into P-277/C7; P-277 is DONE (S243: the SM seat's W175 re-run on main — the frame's own one-loop potential at fixed height on mirror-free slope-2/5 classes sits at J ≠ 0; register line 425). Item 2's specific construction (aS₀ + bS̄₀ at the symmetric point, B1657's two isotropic vacua) was never computed, but its regime (the symmetric point near ω) has no hierarchy (B1691) and the CP question it served is answered differently. Item 5 (the enlarged thread set: swap and sign allowed) has only main's unsealed exploration (the row's 2026-10-15 note: the triplet robust, A₄ stays A₄).
- **Potential:** LOW — what remains is item 5's sealed census, a robustness check of the triplet.
- **First computation:** seal and run W1–W4 on the enlarged thread set (odd-trace words to length 6 with and without one swap and the sign); data-free, hours.
- **Proposed disposition:** SUPERSEDED for items 1–4 (pointers above; item 2 by P-277 DONE); keep item 5 as a small LEAD or decline it with a dated reason, as the escalation itself offers.

### P-178 — the arena: SL(2,ℝ)/SL(2,ℤ) as the trefoil's complement (register line 326; QUEUED; no L)
- **Idea:** The space of placements is the trefoil complement; threads are its closed geodesics (Lorenz knots, Ghys), each linking the cusp by Rademacher's Ψ; four proposals N1–N4 (arena in GENESIS; invariants by discriminant; the field on the arena; the linking matrix read for the three, the hand and the electron's zero).
- **Status on the record:** N1 recorded in GENESIS v1.48 (B1662; frontier/B1662_the_pull_back_acts_on_the_records/FINDINGS.md:56, arc_verdict line 18). N2 done by the SM seat as W98 "W95 by trace" (docs/HARVEST_LEDGER.md:1294–1300, rows 1246, 1247, 1252: READ at headline level, the by-trace and by-discriminant groupings agree; not re-run on main). N3 rides on P-177 item 4 (answered). N4 — the linking matrix read for the three, the hand and the electron's zero — never computed (topic sweep "linking matrix|rademacher|lorenz knot": no arc).
- **Potential:** LOW — N4 is a reading of discrete invariants against facts already explained otherwise (the hand a convention; the electron's zero B1656/B1716).
- **First computation:** N4: tabulate Ψ = #R − #L and pairwise linking numbers on the strip's best classes (L⁵RLR² etc.) and check for a 3; data-free, hours.
- **Proposed disposition:** STILL A LEAD for N4 only; record N1 (B1662) and N2 (W98, seat-only) as done in the row.

### P-184 — the end law's last question: does the weave's symmetry force index ±3? (register line 332; QUEUED; no L)
- **Idea:** At the finite puncture the freedom is the domain Λ in six critical coefficients (index dim Λ − 3); if the symmetry must preserve Λ, the representation decides whether only ±3 survives.
- **Status on the record:** answered in part inside the row (B1641; B1609's E4: under 2T alone −3, −1, +1, +3; with the parity grading only ±3), then reopened by B1672 (NEGATIVE: L₆ reducible under the moves, 2O, commutant 2) and sharpened by B1678 ("the extreme domain stays chosen"; "a covariant rank-3 end family exists on an open set but not at the symmetric state"). Its executable successor is P-210 (the audit lane's package, accepted by B1787, run once S263). The load is P-156 (DEBT #40: B1606/B1652's ±3 rests on the end condition and dim Λ₊ − 3).
- **Potential:** MEDIUM — a forced ±3 would make the generation count a consequence of the end rather than a selection; the record says the grading that gives ±3 is chosen.
- **First computation:** as P-210.
- **Proposed disposition:** SUPERSEDED by P-210 (merge: P-184 and P-218 into P-210, cross-referenced to P-156).

### P-210 — which index the end takes at the symmetric state (a joining law) (register line 358; QUEUED; no L)
- **Idea:** A state-dependent rank-3 boundary family (index 0) is covariant where the Higgs breaks the symmetry but dies at the symmetric state, where Q₈ allows only even ranks (index ±1 or ±3); which one needs a joining law (boundary dynamics from an action).
- **Status on the record:** sharpened, not answered. B1787 accepted the audit lane's P210 package with caveats ("P-210 is sharpened not answered, several checks pass by construction, the orientation and dagger controls are missing, the Q8 stabiliser is full only at generic tau" — B1787 arc_verdict claim); the package ran once 2026-10-29, ten of ten bounded checks (the row's S263 note). No joining law exists on record.
- **Potential:** MEDIUM — the same prize as P-184 (the count from the end, not by selection); blocked by the absence of an action (P-073's root).
- **First computation:** write the boundary response of B1678's transported coupling at the symmetric state as a self-adjoint extension problem and ask which Λ it selects; add the missing orientation and dagger controls B1787 named; data-free, days.
- **Proposed disposition:** STILL A LEAD — the merge target for P-184 and P-218; it is the lead that would pay P-156 (DEBT).

### P-218 — three ±3 pointers connected nowhere (register line 366; QUEUED; no L)
- **Idea:** W28's naturality condition, the fork lane's single sign and the audit lane's regularity at d = 0 or 6 each point to ±3; are they one condition?
- **Status on the record:** untouched. S296 declined its merge because P-210's row does not carry its question (the row's own S296 note; frontier/B1830_the_register_triaged/verification/MAIN_VERIFICATION.md:21).
- **Potential:** MEDIUM — if the three are the parity grading (the condition B1609/S141 found gives ±3), that would be one named premise under the count instead of three; still a premise.
- **First computation:** state the three conditions in B1678's lifted-register language and test whether each is the parity grading of L₆ (commutant 1); data-free reading, hours.
- **Proposed disposition:** STILL A LEAD — merge into P-210 by copying its question into P-210's row (which answers S296's objection).

### P-257 — W118's seven rationals of the composite field near ω (register line 405; QUEUED; no L)
- **Idea:** Prove on main the SM seat's numerically identified rationals m₁m₃/m₂² of the composite field near ω, and whether B1691's k mod 6 rule places a product of two weight-3/2 sections on l_ω².
- **Status on the record:** untouched on main (W118 the seat's, unverified; ESCALATED to "decide C5 first"). C5 (docs/THE_COMPLETION_MAP.md:34) is QUEUED, but P-327 already records that C5's mechanism cannot act on the strip's order-5 and order-10 lines (S fixes only orders 1, 2; ST only 1, 3; register line 475), and B1691 has no hierarchy at ω.
- **Potential:** LOW — a pure-mathematics check in a regime the candidate's lines do not reach.
- **First computation:** the q-expansion of the composite at ω to fix the seven rationals exactly; data-free, hours.
- **Proposed disposition:** STILL A LEAD at low priority; better: decide C5 moot for the strip (P-327's note) and decline P-257 with P-023 together, as their escalation proposes.

### P-258 — the CP phase as a ninth observable in sealed fits (register line 406; QUEUED; no L)
- **Idea:** W66's eight observables carry no CP phase, so a CP-conserving point can pass; add J (or δ) as a sealed cell.
- **Status on the record:** done, twice, and the row was not closed. B1726 sealed ∣J∣ as cell R6 (frontier/B1726_the_two_ingredients_replicated/PREREGISTRATION.md:43); B1825 (Step B, the final attack) pinned J before the seal and graded "the ten … the six, |V_us|, |V_cb|, |V_ub| and |J|" (frontier/B1825_step_b_the_nine_from_one_address/PREREGISTRATION.md:39, :217; FINDINGS.md:4). B1821 adds that only ∣J∣, never its sign, can be predicted in the frame.
- **Potential:** LOW (as a lead; the rule is now practice).
- **First computation:** none.
- **Proposed disposition:** ANSWERED — close DONE: B1726 PREREGISTRATION:43 and B1825 PREREGISTRATION:39, :217.

### P-264 — an ALG gravitational instanton as the triplet's carrier (register line 412; QUEUED; no L)
- **Idea:** Use the non-compact torus-fibred 4d solution (rational elliptic surface minus a fibre) as the space whose end condition and index give the three; main's hand check gave −15 or −12, not 3.
- **Status on the record:** untouched (full-text sweep "\bALG\b|rational elliptic surface|gravitational instanton|minus a fibre": no arc).
- **Potential:** LOW — the only evidence (the hand count) is against; the record's 4d index (W45/W46 on M₁,₂) already gives ±3 under its end condition.
- **First computation:** the twisted Dirac index on the ALG space with the cusp's end condition (APS-type), reproducing the hand count first; data-free, days (specialist geometry).
- **Proposed disposition:** STILL A LEAD (low).

### P-267 — PF1-W: holomorphic invariants have zeros only at the end (register line 415; QUEUED; no L)
- **Idea:** A reading of the principle on the weave: the law's holomorphic invariants vanish or blow up only at the cusp; promoted only by a test whose outcome is not known in advance.
- **Status on the record:** tested. B1730 (the zero-free Higgs lines under PF1-W), B1731 (the Higgs whose invariant has no zero, F₆; the two readings of PF1-W conflict at the least datum, FINDINGS:67–73) and B1732 (sealed, NEGATIVE: with F₆ the six fit but not specifically — "the specificity is ∂R's"; register P-307 DONE, line 455). The web seat's ZERO_FREE_HOLOMORPHIC was read at S202 (P-316, line 464). What remains is P-303 (OWNER: which reading of PF1-W, each field or each determinant).
- **Potential:** LOW — the outcome-unknown test ran and did not promote it.
- **First computation:** none beyond P-303's owner ruling.
- **Proposed disposition:** SUPERSEDED — by B1732 (P-307 DONE) and P-303 (OWNER); close with those pointers.

### P-269 — the SM seat's gravity line: W122, the hand reading, W123, W124 (register line 417; QUEUED; no L)
- **Idea:** Verify W122 (Weeks from −LR as the least closed universe), read the gravity page's hand reading, and read W123 (the Higgs route to the cusp's unit) and W124 (graviton spectra) when they land.
- **Status on the record:** every item paid. W122 verified on main (B1719; the row). The hand reading read (the row). W123 verified on main by B1796 (frontier/B1796_the_cusp_unit_from_the_field_checked_on_main/FINDINGS.md:1, §2 at :50, ":133 P-288's verification half is paid"). W124 landed and was READ: "a thread result, recorded not banked by the seat; no claim for main to verify beyond the seat" (docs/HARVEST_LEDGER.md:1350, row 1302).
- **Potential:** LOW (done).
- **First computation:** none.
- **Proposed disposition:** ANSWERED — close DONE: B1719, B1796 (FINDINGS:50, :133), HARVEST_LEDGER row 1302.

### P-279 — the cusp's unit under the family of wordings (register line 427; QUEUED; no L)
- **Idea:** The golden thread's tick never reaches the cusp (B1629), but wordings with long letter runs go deep into it; does that bear on FK10's unit?
- **Status on the record:** untouched as asked. Since registration FK10's unit was reduced by B1796 to the field's existence plus three identifications on the end data, none of which involves depth along a wording.
- **Potential:** LOW — the unit is end data (B1796); depth is a property of a thread.
- **First computation:** check whether B1796's end-data count d(nδ) = 3n changes along a sequence of wordings with growing letter runs (it should not, being end data); data-free, hours.
- **Proposed disposition:** STILL A LEAD (low); a candidate for a dated decline citing B1796.

### P-280 — does any weave quantity separate p = 2 from p = 3 without the triplet? (register line 428; QUEUED; no L)
- **Idea:** B1680 leaves the prime p as the only datum a target supplies; is p = 2 forced by something other than its giving a triplet?
- **Status on the record:** answered in the audit room, unbanked, and the same content is a debt. The register's parked-items reader found that the swap and the tick fix the odd-p Heisenberg points only up to complex conjugation (432 of 432 on H(3), 12 000 of 12 000 on H(5), a one-line proof), so under GM5c "the remaining choice is the prime" becomes "the prime is 2" (audit/drafts/leads_reeval/LEADREG_10_18.md:136, :307–308, :329; QUEUE.md:691–692). That is P-321's second half (DEBT, line 469).
- **Potential:** MEDIUM — it would remove one choice (the prime) under GM5c, which itself is OPEN; it moves no number.
- **First computation:** bank the K3c check and its one-line proof as an arc (data-free, hours), conditional on GM5c.
- **Proposed disposition:** duplicate of P-321 (DEBT) — merge into P-321; the computation is P-321's.

### P-281 — the gauge echo: does U(1)_Y survive in any move-kept H(N) in E₈? (register line 429; QUEUED; no L)
- **Idea:** For each Heisenberg-type point H(N), N ∈ {2, 3, 5, 6}, embedded in E₈ and kept by the moves, does a hypercharge direction commute with everything kept?
- **Status on the record:** answered for one frame only. The audit lane's E₈ frame (P-140 DONE, line 288): the moves become symmetries but the trace-free hypercharge does not survive; the SM seat's W83 (in P-140's row): "a trace-free Y commuting with the holonomy and the moves has dimension 0 through O"; the 15 are g₂ ⊕ u(1) (HARVEST_LEDGER row 1203). Other N: never computed (full-text sweep: no arc).
- **Potential:** MEDIUM — a hypercharge surviving for one N would tie the towers (SU(5) ⊂ SO(10) ⊂ E₆ ⊂ E₈) to the moves and select N; a uniform no is a clean structural negative on the gauge group's origin.
- **First computation:** for N = 3, 5 (H(3), H(5) ⊂ E₈ as classified Heisenberg subgroups), the centraliser and whether a U(1) commuting with the move-images branches like Y; data-free, a day.
- **Proposed disposition:** STILL A LEAD; record P-140/W83 as its N = 2 (2O) case.

### P-287 — the completion map's C6: a content that holds τ in the band (register line 435; QUEUED; no L)
- **Idea:** Find a matter content whose one-loop potential holds Im τ in the hierarchy band, or the SM seat's W106 democratic dynamics with a minimum off ω, i and the cusp.
- **Status on the record:** open, with the record leaning against within the frame: B1704 (needs ~89–95 tuned net bosons); W154 Stage A (P-380: the band costs one free number, a 13% window); the web seat's e17/e18 (P-327: every record content runs to a cusp on every flat line, not re-run on main); the SM seat (S238): "P-287's C6 has no forced candidate from this seat", with a necessary condition Σ_q w_q ≥ 0 failed by the frame's content (Σw = −41) (the row's note).
- **Potential:** HIGH as a question (τ fixed by dynamics would remove two of the strip candidate's continuous inputs), LOW odds on the frame's own content.
- **First computation:** P-327's run — B1704's potential on the ten α = 2/5 lines on main (data-free, minutes), and W176's Σw ≥ 0 condition verified on main.
- **Proposed disposition:** STILL A LEAD; merge with P-327 and P-380 (same question: what holds τ in the band at one loop).

### P-289 — the completion map's C10: an index on a physical spacetime (register line 437; QUEUED; no L)
- **Idea:** The APS or L² index of the Dirac operator twisted by ρ_T on the Milne cone over a thread, with the cusp's end condition — the read-out on spacetime.
- **Status on the record:** first step done by the SM seat (W126: zero on Weeks and Meyerhoff; HARVEST_LEDGER:1355, row 1307; not verified on main — no FINDINGS cites W126). The web seat's I-31 study (row 1507, VERIFIED WITH CORRECTIONS) showed C10's index cannot tell T from T̄ under (H1)–(H3), so C10 is a count on I-26's side (the row's S274 note).
- **Potential:** MEDIUM-LOW — at best a spacetime re-derivation of the count the end data already give (B1796); it cannot decide the hand.
- **First computation:** re-run W126 on main (Dirac spectra on Weeks and Meyerhoff), then the APS index on the Milne cone over LR with B1796's end data; data-free, a day then days.
- **Proposed disposition:** STILL A LEAD (scope in the row: a count, not the hand).

### P-290 — the completion map's C11: which fields carry T (register line 438; QUEUED; no L)
- **Idea:** Combine B1674's anomaly conditions (s_u = s_d = −s_Q; a ν^c) with the frame datum K (which automorphisms of the flat bundle are gauge) to say which fields transform under T.
- **Status on the record:** priced, not answered: the web seat's I-31 study (HARVEST_LEDGER:1555, row 1507; the row's S274 note) — "C11 prices I-31 and neither earns nor excludes it"; gauged moves obstructed for every dictionary at the level of the character. It bears on θ̄ (whether it is a free constant or tied to τ — the row states the dichotomy; no value is recorded here).
- **Potential:** MEDIUM — it decides whether the moves are an exact symmetry with QCD, i.e. whether θ̄ is a free input or tied to τ; it does not by itself produce a number.
- **First computation:** enumerate dictionaries satisfying B1674's QCD condition with I-31's n ≡ 12 mod 24 and K ≡ 2 mod 4 (row 1507's brute force, 16 of 64) and name the counterterm each needs; data-free, hours.
- **Proposed disposition:** STILL A LEAD.

### P-294 — derive the lepton factor 3 (Georgi–Jarlskog) (register line 442; QUEUED; L250 via P-403)
- **Idea:** On the frame's best lines the leptons copy the down quarks; data need a factor ≈ 3 in the middle generation (and D needs ≈ 3.25 per generation); find the coupling that separates L from d, or show none exists.
- **Status on the record:** heavily worked, every frame-internal route closed: B1738 (27 vevs, D ≡ 1), B1729 (coarser line), the horocycle and Pati–Salam checks (audit/verify_lepton_factor/), B1789 (c not derived; net flux excluded), B1793 (zero-net curvature cannot supply it), B1817 (the twist-charge route closed on slopes to order 30: "c stays one discrete input"), B1827 (S291: the 45-like singlet does NOT give Georgi–Jarlskog's pattern; S290's claim retracted). B1827 also records "c = 3 is the Georgi-Jarlskog factor by hand". Left: P-397's 24-type vev, L250's non-abelian bundle (P-401), P-403's sealed flux design.
- **Potential:** HIGH — the strip candidate rests on c = 3 (P-355, DEBT #1; P-446, DEBT #5) and fails D by ~3σ; a data-free derivation is what B1798 says would restore a THE_BAR grade.
- **First computation:** P-403's design — fix the flux geometry, compute the overlaps, make R₂, R₁ and D functions of the flux ratio, failing if it is free; data-free design, days; the run needs a seal.
- **Proposed disposition:** STILL A LEAD (the derivation is an idea; the load sits on P-355/P-446, already debts); merge candidate as parent of P-397, P-401, P-403.

### P-295 — derive the reading rule (which Higgs each sector reads) (register line 443; QUEUED; no L)
- **Idea:** Main reads up with S̃ and the others with S; one rule for every sector misaligns the CKM; derive which object enters each sector.
- **Status on the record:** not derived. B1744 (the Higgs's own twist does not force it); B1790 (no derivation inside B1656's frame: the coupling is complex-bilinear in holomorphic fields, the eight assignments are physically distinct; needs an antiholomorphic or Hermitian Higgs slot); W174 (S236: equal down and lepton exponents forced on the 2/5 lines). New since its last move: B1827 (S289–S291) found an opposite-sign singlet — exactly the adjugate reading adj(S) — balances the CKM's corners (P-566), and on the 24 order-5 lines the leptons read the down sector through the adjugate (P-583).
- **Potential:** HIGH — the quark mixing is blocked by the Higgs construction (FL-06), and this row is the question of which Higgs each sector sees; the adjugate result is the first construction that lifts the corner inversion.
- **First computation:** test whether the adjugate reading for down is forced by the amphichiral involution or the hypercharge sign (P-566's own list), data-free on the order-5 lines; hours to a day.
- **Proposed disposition:** STILL A LEAD; duplicate of P-394 (the reading rule as an input to remove) — merge, with P-566 and P-583 as its live children.

### P-315 — why only the Higgs's i-component splits down from leptons on 12 order-10 lines (line 463; QUEUED; no L)
- **Idea:** The web seat saw that on the 12 order-10 lines with 5α ∈ ℤ and 5β ≡ ½ the lepton spectrum differs from the down spectrum only through one component of the Higgs. The row asks for the mechanism.
- **Status on the record:** Computed and mostly explained since. B1742 §3 (FINDINGS lines 41–56) gives the mechanism on α = 2/5: on w = (2/5)τ + k/10 the lepton twists are the down twists swapped and shifted by half-periods. For odd k the spectra coincide only for a Higgs with no QI component, and the departure is linear in that component. S297's recheck under P-355 (row line 503; frontier/B1830_the_register_triaged/verification/recheck/p355/) extends this from α = 2/5 to all 24 order-10 "β-half-lift" points (α ∈ ⅕ℤ, β ∈ odd/10, i.e. 12 lines up to sign), which are exactly row 1321's lines. That extension is computed, not proved. Two proofs exist on seat lanes and neither is verified on main: agy's Theorem 18C (HARVEST row 1539 [line 1587]), and agy:B1761, "the up sector's i-residue vanishes exactly when 5w ≡ ½", listed as "to be re-derived on main with P-384" in B1784 FINDINGS line 31. Row 1321 says "i-component" and B1742 says "QI component". I read these as the same component; main should confirm.
- **Potential:** MEDIUM–HIGH, because this is the mechanism that sets D on the candidate strip's own lines. P-355's S297 note says the strip rows' D ≈ 10.9 comes from their Higgs's QI admixture. A principle that fixed that admixture would predict D.
- **First computation:** Verify Theorem 18C, or derive the half-lift identity directly from the θ-characteristic shifts, on all 24 points (data-free, hours).
- **Proposed disposition:** SUPERSEDED, merge into P-355 (DEBT #1). Its "why" is P-355's half-lift statement, and its proof is P-355's owed verification of Theorem 18C.

### P-323 — θ̄ in the mass frame (line 471; QUEUED; L192)
- **Idea:** In the frame's six-row reading, is there a (reading, Higgs, line) for which arg det(Y_u Y_d) is identically CP-even while J ≠ 0? If so, θ̄ would be predicted rather than free.
- **Status on the record:** Computed by seats, not verified by main. The web seat showed:
  - the Higgs phase cancels in θ_Y;
  - θ_Y is not a function of the physical point, because the T-step and b → b ± 1 relabellings move it (HARVEST row 1414; the row's own notes).
  Its sealed test THE STRONG ANGLE IN THE MASS FRAME (rule f53115e19; result row 1443 [line 1491]) found θ_Y NOT HARMONIC on almost all combinations, and on every slope-2/5 combination in the SM reading. So θ̄ stays an input in the frame as built. The SM seat's W168 reproduces this on its own instrument (row 1439 [line 1487]). Main's rows are "READ (quotes checked, cited numbers spot-checked)"; the row itself still says "main's own check (a sample) owed". Since then θ̄ has become a held-out level-2 target of the candidate family: P-585 (line 733) counts P-323 as "one prior look". The agy lane computed θ̄ on the strip, unsealed, and that is counted as a second prior look (row 1539 [line 1587]); main has not read the values. FRAMING_LEDGER line 50 (FL-16) cites the row's number. I do not repeat it here.
- **Potential:** MEDIUM. A forced CP-even (det-real) locus would remove an input and might fix Re τ (P-569). The sealed harmonicity test argues against it in the frame as built. P-585 now fences any further computation as a look at a held-out target.
- **First computation:** Main's sample re-run of the web seat's harmonicity cells on its committed script (data-free, hours). Any new θ̄ evaluation at the strip must go through LOOK_LEDGER and the P-585 card's rules first.
- **Proposed disposition:** STILL A LEAD. Merge with P-569 (θ̄ as a constraint, the det-real curves) and P-461's FPST half (a CP-even determinant by modular invariance). All three ask one question. The sample check of the sealed test is a verification owed before P-585's card uses θ̄; note it there.

### P-326 — ν^c's Majorana mass as a modular form (line 474; QUEUED; L221 (d))
- **Idea:** B1674 requires a ν^c, and B1616 forbids a constant Majorana mass. A weight-3 form (unique up to scale in one hand) could be the Majorana mass. The seesaw's cusp exponents would follow.
- **Status on the record:** Untouched in substance. B1799 (data-free, PROVED) studied the self-pairing and the type-I seesaw for any invertible N, "e.g. P-326's weight-3 form" (FINDINGS line 62). It explicitly says "Not examined: the weight-3 Majorana form of P-326 (a different slot)" (line 81), and "the size of m₁ needs the neutrino sector's own inputs (P-326 …)" (line 73).
- **Potential:** LOW. Neutrino masses are not among the 19 (B1799 line 74). It would add structure to the neutrino sector but would not move the count.
- **First computation:** Write the weight-3 ρ-covariant form in B1656's ν^c slot and compute the seesaw's light-state cusp exponents on the census lines (data-free, a day). Any oscillation comparison is sealed.
- **Proposed disposition:** STILL A LEAD (low priority). It is related to P-157 (DEBT: P10 as Dirac neutrinos).

### P-327 — the one-loop potential on the fit's lines (line 475; QUEUED; L254 (d); C6, C7)
- **Idea:** Run B1704's one-loop potential on the order-5 and order-10 lines at Im τ 2.55–3.25. A minimum there would fix τ by dynamics.
- **Status on the record:** Answered NEGATIVE by seats, and in part on main.
  - The web seat's e17/e18 (row 1401 [line 1449]): on every flat line every record content runs to a cusp at one loop, the ten α = 2/5 lines included. Taken as input, not re-run on main.
  - The SM seat's W154 (row 1388 [line 1436]): the band needs a content tuned to a 13% window.
  - B1784 FINDINGS line 32: V = E₃ − tE₂ holds every Im τ at its own t, so it selects no Im τ.
  - W175, re-run on main at S243 (P-277's row, line 425): dV/dy > 0 and no minimum in τ at finite height on the slope-2/5 mirror-free classes. This covers orders 15–30, not the order-5/10 lines this row names.
  - B1791 FINDINGS line 67 lists "P-327 and P-343 (both queued, the same question)" as not examined.
- **Potential:** LOW at one loop, where the question is closed. The non-perturbative and flux residue is P-373's.
- **First computation:** Re-run e17/e18's cusp coefficients on the ten α = 2/5 lines on main with B1704's code (data-free, minutes). Or accept them with a dated note, as the row's own ESCALATED note allows.
- **Proposed disposition:** ANSWERED (row 1401; W154 row 1388; B1784:32; P-277's S243 note). Close DONE after the minutes-long re-run or a dated acceptance note. Merge P-343 here or into P-373.

### P-328 — the input ledger and the CP-line J-vanishing rule (line 476; QUEUED; L217 (d), L151)
- **Idea:** The ledger: the frame reaches at most 10 of the 19, with five inputs unruled. The rule: J vanishes exactly where the CP map fixes the line on Re τ = 0 or ½. So if the line carries the CP violation, Im τ could be the only licensed continuous input.
- **Status on the record:**
  - The ledger half lives in docs/MAINS_PLAN.md lines 66–85 (the ESCALATED note says so) and in P-418's adopted scoreboard.
  - The J half is, in my derivation, a corollary of B1821 (PROVED, data-free). B1821's mirror (−x + iy, (α, −b)) ≡ (x + iy, (α, b)) sends J → −J, and its period check shifts the line under τ → τ + 1 (B1821 FINDINGS lines 1–30). The fixed points at Re τ = 0 and ½ are exactly the seat's kα ≡ −2b (mod 1). W170 ("the mirror's fixed point conserves CP", row 1441) and W176's K1 (row 1458) say the same for (0, 1/N).
  - B1821 does not state the rule in the row's form. It needs one dated line.
  - The anchor half was overtaken by W175, verified on main (P-277, line 425). CP violation in the frame's dynamics sits off the mirror lines, so a CP line removes J rather than licensing it.
- **Potential:** LOW. It is bookkeeping plus a corollary. The live selector question is P-411's (a class condition) and P-569's (θ̄ locus).
- **First computation:** None new. Write B1821's fixed-point corollary as a dated note and check it against the seat's 96/96 rows (minutes).
- **Proposed disposition:** SUPERSEDED: the J rule by B1821 (needs a dated note), the ledger by MAINS_PLAN and P-418, the anchor question by P-411 and P-569. Close DONE with those pointers.

### P-329 — B1726 at the unification scale (line 477; QUEUED; the OPEN O4 reader)
- **Idea:** B1726's seal names no scale, and Georgi–Jarlskog's 3 belongs at the GUT scale. Re-run its comparison against GUT-scale ratios.
- **Status on the record:** Never run. The scale question has since been generalised:
  - P-574 (line 722; LEAD): "every future card declares its scale (or a menu priced in bits)".
  - P-585's card: "its scale forced or priced (P-574)".
  - P-590 (DEBT #33, line 738): the scale robustness of the sealed negatives.
  - B1829's REGRADE.md line 49: a held-out target "can confirm only if the frame forces its scale, fixed before".
  - B1726 itself is UNSETTLED in the re-grade (REGRADE.md line 16).
  Re-running B1726's census against GUT-scale data now would be a level-1 re-look on seen data. Under GENESIS v1.61 it cannot make a result.
- **Potential:** LOW as written, since a re-look cannot confirm. The scale issue itself is HIGH and lives in P-574/P-585.
- **First computation:** None under this row. Under P-574: state the frame's scale (or a priced menu) before the P-585 card is sealed (data-free).
- **Proposed disposition:** SUPERSEDED by P-574 and P-585's card (positives), and P-590 (negatives).

### P-330 — C10 on m004: seal B940's open O2, then the ρ_T twist (line 478; QUEUED; L177, L174)
- **Idea:** B940 saw a Dirac kernel candidate of dimension exactly 2 that its seal excluded. Seal it, then twist by ρ_T. A non-zero kernel would be the first count read on a physical 4d spacetime.
- **Status on the record:** Not run. It is blocked by P-540 (DEBT #38, line 688): B940's ± pairing rested on B933 §5a, which gives Kramers doubling, not λ ↔ −λ (S274 dated notes). Its scope is also limited by the web seat's I-31 study, verified with corrections (row 1507 [line 1555]): C10's index cannot tell T from T̄ under (H1)–(H3), so C10 is a count (I-26's side) and not the hand (P-289's S274 note, line 437).
- **Potential:** MEDIUM. A count on a physical spacetime bears on "three generations only by selection". It cannot settle the hand, and nothing on the 19 rests on it.
- **First computation:** Settle P-540 first (does m004's orientation-reversing isometry reverse the 3d Dirac operator with the spin structure and twist kept; data-free, hours). Then seal O2 with B940's instrument (about 50 minutes a run).
- **Proposed disposition:** STILL A LEAD, merge with P-289 (C10, the Milne-cone read-out), which is the same computation one level up.

### P-331 — L161 Phase 1b: does B1656's coupling carry the θ-odd 2I doublet on an order-5 line? (line 479; QUEUED; L161)
- **Idea:** Test whether the current frame's coupling, on one order-5 line, carries the binary-icosahedral θ-odd doublet that carries the golden "tones" (B665), with a silver line as control.
- **Status on the record:** Untouched since registration. The topic sweep for "2I doublet|θ-odd|L161|tones" finds no arc from B1600 on. B1736 found the coupling's symmetry is Γ₄ = PSL(2, ℤ/4) (1 + ρ′, the cube's rotations), a level-4 group. That makes the level-5 2I question non-trivial and unasked.
- **Potential:** LOW. It would join the July golden corpus to the current frame (a weave link). Order 5 is not golden-specific (B997), and it bears on none of the 19 directly.
- **First computation:** Decompose B1656's channel weights on one order-5 line under the level-5 congruence quotient and look for the θ-odd 2I doublet; a silver line as control (data-free, minutes to hours).
- **Proposed disposition:** STILL A LEAD, merge into the L252 cluster (P-033, P-034, P-040, P-041: the McKay ladder and the level-5 golden corpus).

### P-337 — the zero law: every exact zero is isotropy plus an involution or the rectangular mirror (line 485; QUEUED; L242; carries P-292)
- **Idea:** B1656's four channels are the fibre's four spin structures. The row asks for a proof, with B1716's instrument, that every exact zero of det M comes from isotropy plus the involution or the rectangular mirror. P-292's 16 order-12 zero lines (with "12β odd") are part of it.
- **Status on the record:** The web seat's kernels note (HARVEST row 1516 [line 1564]; S298) claims the Re τ = 0 zero law derived, on P-292's 16 lines and P-404's 8, with no others in its census. Main marked it "NOT YET VERIFIED". From the same note main did verify one item: σ_b ≠ 0 at finite τ on (1/4, odd/8). That corrects B1826 and B1788's note, not this law. B1830 kept P-337 LEAD (MAIN_VERIFICATION.md line 23). The debts P-262 and P-268 (#54, #55) carry the used zero laws (B1701/B1703 and B1712/B1716), and P-524 (#11) carries the kernel lemma.
- **Potential:** MEDIUM. Exact zeros are massless generations, so a proved zero law tells which lines and points give a massless first generation. It would pay part of P-262 and P-268. It produces no value.
- **First computation:** Verify the web seat's derivation, then reproduce its Re τ = 0 census on main with B1716's instrument over the lines of order ≤ 12 (data-free, hours).
- **Proposed disposition:** STILL A LEAD (verification owed), merge with P-404. A main verification should close P-337, P-404 and parts of P-262 and P-268 together.

### P-343 — what places τ where the six are reached (line 491; QUEUED)
- **Idea:** The six's χ² minimum sits at a fitted τ on (2/5, 1/10). A principle that placed τ there would turn the reading into a count.
- **Status on the record:** The row's own ESCALATED note (2026-10-28) says "merge into P-373 once P-327 is run; no principle on record places τ". B1791 (NEGATIVE: Im τ not found forced) names P-343 and P-327 as "the same question" (FINDINGS line 67). Its CKM remark ("the nine need more than τ") is overtaken by B1825 (NEGATIVE: no single address carries the ten).
- **Potential:** That of P-373, which carries the same question.
- **First computation:** None separate from P-373.
- **Proposed disposition:** SUPERSEDED by P-373 (merge, as its own escalation says).

### P-345 — what gives the nine (B1739's consequence) (line 493; QUEUED)
- **Idea:** The record's Higgs is nearly null at the hierarchy's τ, so the SM reading misaligns the light states. It names two routes: (a) a Higgs led by ρ(T)'s non-null eigenline e₁; (b) another reading rule.
- **Status on the record:**
  - Route (a) answered NEGATIVE by B1740 (sealed; the row's own S202 note): it aligns but loses the hierarchy.
  - Route (b) as two doublets is B1742's TWO_HIGGS, verified on main: the mixing is too small.
  - "∝ r^½" was corrected to "the median's slope only" (S242; LAW_MAP lines 334/336 per the index).
  - The question then moved to P-352, P-357, P-366 and P-377, then to THE FINAL ATTACK: B1823 (Step A NEGATIVE) and B1825 (Step B NEGATIVE: the six and the four never at one address).
  - It now sits with B1826 (the CKM corner inversion: one Higgs drags both lightest states) and B1827 (the wall is the Higgs construction; the ADJUGATE balances the corners).
  - Today's live rows: P-555 (two addresses) and P-566 (the sector-odd singlet / adjugate).
- **Potential:** The question is HIGH (the CKM is a third of the 19), but this row's routes are spent.
- **First computation:** None under this row. See P-566.
- **Proposed disposition:** SUPERSEDED (B1740, B1742, B1825, B1826 item 3, B1827; live form P-555, P-566).

### P-357 — what fixes the Higgs's invariant (line 505; QUEUED)
- **Idea:** Every Higgs form on record is nearly null, with |h·h|/|h|² falling like e^{−π Im τ}. The nine need a nearly constant departure from the null cone. B1744 §2: det Y = (h₀² + h·h)(…)(…), so that departure is the first generation's own number and it carries the Cabibbo angle. What fixes it?
- **Status on the record:** Worked extensively and closed route by route:
  - S204–S214 post hoc (audit/verify_p357/): the form route on main is exhausted (S213: from weight 12 every direction is a form direction with free constants); the parameter-free energy rule fails (S214).
  - B1746: Γ₄'s forms do not reach the target. B1747: no line under the one-Higgs SM reading.
  - B1807 gives the invariant of every single covariant section in closed form (S248 note).
  - W158 and W159 NEGATIVE (rows 1409, 1410 [lines 1457–1458]).
  - B1823 (Step A, NEGATIVE as a compression): fixing the Higgs direction through the heavy sector's one-loop vacuum needs a chosen normalisation (3n − 2 ratios).
  - B1827 §2 / P-566: a sector-odd singlet (the h₀ of B1744's four-dimensional norm), read through the adjugate, lifts the CKM corner inversion.
- **Potential:** The question is HIGH (the first generation and Cabibbo), but its live form is P-566, which names the same object: the singlet h₀ in (h₀² + h·h).
- **First computation:** Under P-566: one definition of the odd singlet, then the corner order, |V_ud| and the six at the frame's points (data-free).
- **Proposed disposition:** SUPERSEDED as a working row by P-566 (with P-555). Merge P-357, P-366 and P-377 into one row, keeping their audit trail, and point it at P-566.

### P-366 — the target lies outside every single holomorphic section (line 514; QUEUED)
- **Idea:** W146 and W149 show every single section is exactly null, tends to I = 1, or has I falling exponentially. The nine's target lies outside all of these. What remains: two objects, a sum of sections with different multipliers, or a non-holomorphic section.
- **Status on the record:**
  - B1807 (S248 note on P-357) explains the trichotomy in closed form and "does not open the route".
  - Two objects: W151's pair lemma (row 1372) and W158/W159 NEGATIVE for the forced and named pairs (rows 1409, 1410).
  - B1825's sealed one-address test NEGATIVE.
  - B1827's adjugate reading is a new route not on this row's list: a holomorphic reading invisible on the 3D Higgs.
  - No non-holomorphic section has been sealed.
- **Potential:** As P-357; live form P-566.
- **First computation:** As P-566.
- **Proposed disposition:** SUPERSEDED, merge with P-357 into P-566.

### P-371 — W150/W151: τ's height from the heavy states, and the two-object bound (line 519; QUEUED)
- **Idea:** The one-loop heavy-state holder fixes a level curve m_Q(τ) = μ, so Im τ becomes one free ratio μ/M̃. A constant-ratio pair of sections cannot reach the target. The seat named a squared spinor h = ψ ⊗ ψ as next.
- **Status on the record:** Both halves answered.
  - (i) W150 was REPRODUCED WITH CORRECTIONS on main at S260 (HARVEST row 1371 [line 1419]; audit/verify_w150/REPORT.md). The height stays one free ratio μ/M̃, CHOSEN, with a second, exactly degenerate vacuum. The web seat's design study (row 1470) adds that μ/M̃ is one RG invariant, chosen.
  - (ii) The squared spinor became W152, the Higgs as a qubit state, a dictionary (row 1376 [line 1424]). Its test W158 (the 26 special lines are pure states' squares, so det Y = 0) is NEGATIVE, and W159 is NEGATIVE (rows 1409, 1410 [lines 1457–1458]).
- **Potential:** LOW as a row. What fixes μ/M̃ is P-373's question.
- **First computation:** None.
- **Proposed disposition:** ANSWERED (row 1371 at S260; rows 1376, 1409, 1410). Close DONE and carry "what fixes μ/M̃" in P-373.

### P-373 — what fixes Im τ ≈ 3.03 (line 521; QUEUED)
- **Idea:** The six's specificity lives on one strip (Im τ 2.96–3.11, the T-orbit of (2/5, 1/10)), Re τ nearly flat and Im τ sharp. What principle fixes the height?
- **Status on the record:** Every examined route closes or trades the input:
  - B1791 (NEGATIVE: special points, cusp shapes, apexes, functionals, horocycle).
  - The one-loop potential: W154 row 1388, B1784 line 32, W175 verified on main (P-277), W176.
  - The heavy-state holder (W150 at S260: one chosen ratio).
  - The ρ′ Petersson peak, set by a convention (P-398).
  - No channel threshold (audit/verify_tau_threshold/).
  - The agy τ* is a data row, not a selection (B1784).
  The ESCALATED note lists the open routes: P-380 Stage B, P-327/P-343, P-398, non-perturbative and flux potentials. P-380's Stage B already ran as W155 (row 1390 [line 1438]) and is stale on this list; P-327 is answered (above). New since: the strip is defined through B1726's compute() with the small-cut end. At the exact norms the six fail (P-421, DEBT #4; S297), so the target height is itself conditional.
- **Potential:** HIGH. A forced height would remove the candidate's sharpest continuous input and make a level-2 card cheaper. Against it: every one-loop and special-point route on record, and the strip's dependence on a groundless end formula.
- **First computation:** Before any new τ principle, settle P-421: re-fit the six on the strip's lines with the exact horoball norms and with L free, at its look-elsewhere cost. That says whether "Im τ ≈ 3.03" survives as a target (data in hand, needs a seal per P-421). Then non-perturbative and flux potentials, each stated before its check (days).
- **Proposed disposition:** STILL A LEAD. Absorb P-343, P-327's residue, P-371's μ/M̃, P-380 and P-398. Strike "P-380 Stage B" from its open list (W155 ran). Make it explicitly conditional on P-421.

### P-377 — step 2 of the plan after B1749: the mixing at the six's strip (line 525; QUEUED)
- **Idea:** At the strip, one Higgs reaches only a poor nine. Two free doublets reach the bar (reachability, not evidence). A sealed mixing test waits for a principled second object.
- **Status on the record:**
  - The design input was consumed: B1757 committed the step-2 vectors.
  - W158 (special lines) and W159 (the forced 24-element group) are NEGATIVE (rows 1409, 1410).
  - THE FINAL ATTACK sealed the one-address mixing test, B1825 (NEGATIVE as sealed), after Step A's attempt to supply the Higgs direction failed (B1823).
  - The second object is now P-555 (two addresses, a budget computed) and P-566 (the sector-odd singlet / adjugate).
  - The row's own note says the mixing reachability is not specific (two free doublets reach 66% of random CKMs).
- **Potential:** The question is HIGH; its live form is P-555/P-566.
- **First computation:** None under this row.
- **Proposed disposition:** SUPERSEDED (B1757, W158/W159, B1823, B1825; live form P-555, P-566). Merge with P-357/P-366.

### P-380 — W154: the census over contents, Stage A; Stage B waits on the owner (line 528; QUEUED)
- **Idea:** At one loop every admissible content gives V = −(A E(τ,3) + B E(τ,2)). Holding τ in the band needs a content tuned to a 13% window. Stage B (the Higgs direction) was to follow.
- **Status on the record:** Stale. Stage B ran: the SM seat's W155, "the census over contents, Stage B, the Higgs direction … at the owner's 'lets do themall'" (HARVEST row 1390 [line 1438]; main: READ, "line (B) of the owner's fork closed at one loop"). Stage A is W154 (row 1388 [line 1436]). B1784 line 32 checks its consequence (V = E₃ − tE₂ selects no Im τ unless t is chosen). B1791 line 67 still calls "P-380's Stage B" not examined, and P-373's escalation lists it as open; both are stale. What is genuinely owed is main's verification of W154's analytic form. That is already a DEBT: P-117 (#50), "verify it on main under P-380 Stage B and then close this as DONE".
- **Potential:** LOW. It is answered negative at one loop.
- **First computation:** None under this row. Under P-117: re-derive W154's E(τ,3), E(τ,2) form on main (data-free, hours).
- **Proposed disposition:** ANSWERED (W154 row 1388, W155 row 1390, B1784:32). Close DONE and move the W154 verification wholly to P-117. Correct P-373's open list and add a dated note to B1791's "Not examined" line.

### P-393 — main's own plan beside the SM seat's (line 541; QUEUED; source OW)
- **Idea:** docs/MAINS_PLAN.md, framed as reductions. The six's inputs are removed in order: the slope and its offset, the lepton factor, the reading rule, Im τ, then the horocycle and the scale.
- **Status on the record:** Steps 1–4 ran, each NEGATIVE or "not derived":
  - Step 1: B1785/B1786/B1788.
  - Step 2: B1789, plus B1793 and B1817.
  - Step 3: B1790.
  - Step 4: B1791 (MAINS_PLAN lines 26–54).
  - Step 5 was "named, not yet planned". The web seat's sealed HOROCYCLE AND HEIGHT (row 1455 [line 1503]) and P-421 have since addressed it.
  - The ledger of inputs removed reads "none" (MAINS_PLAN line 68).
  MAINS_PLAN's own table is stale: the horocycle row says "named, not studied" (line 85; the Im τ row, line 80, says "no potential fixes it (B1784)") despite row 1455 and P-421. This is an umbrella row like P-309 and P-313, which were closed DONE as umbrellas.
- **Potential:** LOW as a lead. It is a plan; its residues are the substance.
- **First computation:** None. Refresh MAINS_PLAN's table (the horocycle row; "no potential fixes it" to cite W175/P-277).
- **Proposed disposition:** ANSWERED as an umbrella (steps 1–4 paid by B1785–B1791, B1793, B1817). Close DONE, with residues in P-384, P-294/P-397, P-394, P-373 and P-421. Alternatively retype [PROCESS] for the page's currency.

### P-394 — the reading rule as an input to remove (line 542; QUEUED)
- **Idea:** The six use S̃ for up and S for down and leptons. Derive which sector reads the conjugate Higgs from the frame's conjugation structure, or show it is a free discrete input.
- **Status on the record:**
  - B1790 (NEGATIVE, frame-scoped): not derived. The coupling is complex-bilinear and no moduli map conjugates. The hypercharge sign rule would reduce it to one bit but is UNEARNED (I-35).
  - The SM seat (row 1431): no Hermitian slot on its record assigns it.
  - S242 dated note (B1790 FINDINGS line 128 ff.): on the mirror lines a holomorphic section reproduces S̃ exactly, Γ⁰(2)-covariant only.
  - New since: B1827 §2 found a fourth reading, the ADJUGATE adj(S) = εSᵀεᵀ, "never considered (B1724, B1790)". P-583 adds that on order-5 lines the leptons read the down sector through the adjugate (B1728's swap law).
  The reading is still a counted 3-bit input of the candidate (MAINS_PLAN line 84; P-585's (S̃, S, S)).
- **Potential:** MEDIUM. Deriving it removes up to three searched bits from the P-585 card, and the adjugate gives a structural handle B1790 did not have. Against it: B1790's no-go in the frame as built.
- **First computation:** Ask B1790's question again with the adjugate included. Is there a frame map, such as the amphichiral involution (τ, a₀) → (−τ̄, −ā₀) named in P-566, under which the up sector's reading is forced to be the adjugate or conjugate of the down sector's? Data-free, hours.
- **Proposed disposition:** STILL A LEAD. Cross-link to P-566 and P-583; the adjugate is the new route.

### P-397 — the lepton factor's route left (line 545; QUEUED)
- **Idea:** Find an insertion that sees the integer hypercharge on one leg (a zero-net local curvature, a 24-type vev, a first-order term linear in the doublet leg's charge) so that c = 3 is derived rather than chosen.
- **Status on the record:** Routes closed one after another:
  - B1793 (NEGATIVE: zero-net curvature acts on the pair's total charge, the same for down and leptons).
  - The literature at source (S259; audit/drafts/strandA/LIT_ONE_LEG.md): exactly 3 exists only as the 45/126/351′ Clebsch, which is absent at tree level.
  - B1817 (NEGATIVE as scoped: the twist-charge route gives 1, 4 or 1/4 at every N_c).
  - S290's 45 candidate RETRACTED at S291 (B1827 FINDINGS lines 67 and 91: mislabelled factors).
  What remains, by B1817's FINDINGS lines 82–86: an entry linear in the doublet leg's charge, the B − L channels (absent at tree level), and L250's non-abelian bundle (P-401, P-403). Separately, the candidate's real problem is D: c = 3 gives D = 9 where the spectra coincide, and on the strip D is set by the QI admixture (P-355). So deriving exactly 3 does not by itself fix D.
- **Potential:** MEDIUM. It removes one discrete input (c), but D is the binding constraint, and most mechanisms are closed.
- **First computation:** Through P-403: compute R₂, R₁ and D in closed form in the flux frame from (q_L − q_R)w (data-free, a day).
- **Proposed disposition:** STILL A LEAD. Merge with P-294 (the same question, chunk 2), and note P-446 (DEBT #5: c = 3 chosen on data).

### P-398 — a frame-internal height: the ρ′ Higgs's Petersson peak (line 546; QUEUED)
- **Idea:** The Petersson norm of η⁶∂R peaks at Im τ = 2.8406 for every line, but the η-power m moves it. A principle fixing m and naming "the Higgs at its Petersson maximum" as the vacuum would make the height a prediction.
- **Status on the record:** Registered by B1791 (FINDINGS line 91 ff.), which says the peak "sits outside the strip" and so it was "registered, not sealed". Untouched since. The strip's own ground is now in question (P-421).
- **Potential:** LOW. The height is set by a convention, lies outside the strip, and has been seen post hoc. A principle for m would still have to precede any check.
- **First computation:** Look for a principle fixing m, for example the weight that makes η^m ∂R a form of the frame's family group at a canonical weight (data-free, hours). Only then a sealed prediction.
- **Proposed disposition:** STILL A LEAD (low), merge into P-373.

### P-402 — the horocycle is a counted discrete input with no row (line 550; QUEUED)
- **Idea:** The six use L_max and the nine's one-Higgs optimum uses L₂. Say what selects a horocycle, or record it as an input with its fitting work disclosed.
- **Status on the record:**
  - The web seat's sealed HOROCYCLE AND HEIGHT (row 1455 [line 1503]): H2 NOT ABSORBED, the six need L_max, the horocycle "one discrete input chosen by the data, counted".
  - THE EXACT END (row 1459 [line 1507]): L_max's small-cut norm lies 35–38% above the exact norm.
  - The row's own last note: "the end's scale is now P-421". P-421 was retyped DEBT at S297 because the candidate is graded through that end.
  - The counting half is in P-418's adopted scoreboard. MAINS_PLAN's ledger still reads "named, not studied", which is stale.
- **Potential:** That of P-421: HIGH for the candidate's standing.
- **First computation:** Under P-421.
- **Proposed disposition:** SUPERSEDED by P-421 (DEBT #4). Close with that pointer and refresh MAINS_PLAN's horocycle row.

### P-403 — L250's sealed design: the flux geometry first (line 551; QUEUED; L250)
- **Idea:** Fix the geometry, compute the actual overlaps, and test three things: (i) the conjugate flux-mode Higgs reproduces S̃; (ii) the coupling is odd in the charge sign; (iii) R₂, R₁ and D as functions of the flux ratio, failing if the ratio is free.
- **Status on the record:** The geometry-first step is done: B1800 (PROVED; FINDINGS lines 95–120). In the flux frame a sector's coupling depends on (q_L − q_R)w at level 2 and is not B1656's flat-frame coupling. B1800 names the next steps: name the U(1) with flux 1 and 2, compute the three sectors in closed form, read R₂, R₁ and D, then seal. Not done. Constraints since:
  - B1794 (NEGATIVE, family-wide): no rational hypercharge class on the frame; hypercharge reaches an index only through a non-abelian V.
  - The web seat's caution (S274, row 1507): the APS end term cannot tell T from T̄ under unitary twists; not reproduced on main.
  - B1817 FINDINGS line 86 and B1795 FINDINGS line 92 list it as the remaining route.
- **Potential:** MEDIUM–HIGH. It is the one route on record where a quantised geometric datum, a flux integer, could give the lepton/down split and D, the candidate's failing relation. Against it: P-401's step back (flux trades inputs for integers, the landscape), B1794, and the 3 needing an irrational flux ratio in the literature (P-397's S259 note).
- **First computation:** Name the U(1) carrying fluxes 1 and 2 on B1800's torus. Write the up, down and lepton couplings from (q_L − q_R)w = 5w, −w, −9w in CIM's closed form, and read R₂, R₁ and D as functions of the flux ratio (data-free, a day). Seal the design before any data.
- **Proposed disposition:** STILL A LEAD. It is the live continuation of L251/L250. P-020/P-022 (L251, computed by B1800) are the known stale rows for its first half.

### P-404 — the Weinberg pair's CP-line zeros (line 552; QUEUED)
- **Idea:** On Re τ = 0 the LL pair's det M vanishes exactly on 8 order-8 lines, and on Re τ = ½ on 18 lines of orders 4 and 12. State the full zero law for self-pairings with P-292's family, and ask whether a principle places τ on a CP line.
- **Status on the record:** Found by B1799's referee. LAW_MAP line 346 records "the Weinberg pair's does [vanish] on CP lines (P-404)", the converse numerical with CP-line exceptions. The web seat's kernels note (HARVEST row 1516 [line 1564]) claims the Re τ = 0 law derived on P-404's 8 lines; NOT YET VERIFIED on main. The "τ on a CP line" half is P-411's and P-569's question, and W175 (verified on main, P-277) puts the frame's CP violation off the mirror lines.
- **Potential:** LOW–MEDIUM. A structural zero law for the neutrino sector, not among the 19.
- **First computation:** As P-337, in the same run (data-free, hours).
- **Proposed disposition:** STILL A LEAD, merge into P-337.

### P-405 — G₂ membrane-instanton Yukawas (register line 553; QUEUED; no L)
- **Idea:** in M-theory on a G₂ manifold with Q = an m004 filling, Yukawas are exp(−calibrated volume) of associative
  3-cycles joining the matter points; ask whether those volumes are fixed multiples of the object's own volume, which
  would give parameter-free ratios.
- **Status on the record:** untouched since its own S234 bracket (Acharya hep-th/0212294 read; the row itself concludes
  the chain "trades Im τ for a free integer" because Acharya's validity needs c₂ ~ 10³, a large cover of free index).
  B1801 FINDINGS:117 only reframes it (calibrated, not hyperbolic, volumes). Sweep
  `membrane instanton|associative (3-)?cycle|calibrated volume --full`: 2 arcs (B1801, B1803), neither computes it.
  The G₂ frame's tower test is NEGATIVE (B1805; docs/THE_TOWERS.md:139–152).
- **Potential:** LOW — by the row's own reading it replaces τ with a free cover degree and needs G₂ moduli the object does
  not fix; neither the cycles nor the matter points are object-supplied.
- **First computation:** a design note only: list the free data (cover degree, moduli, flux G) against Vol(Q) for the
  even fillings (volumes 1.3–2); hours; data-free.
- **Proposed disposition:** STILL A LEAD (low; could be DECLINED with the row's own S234 reason if main wants the index
  shorter).

### P-411 — a class-selecting consistency condition on the line (register line 559; QUEUED; no L)
- **Idea:** find a data-free condition on the flat line itself (a bundle condition over the mapping torus, θ's
  monodromy, one Green–Schwarz-type counterterm) that selects the line class the six sit on.
- **Status on the record:** not found; the tries all point against the counted class: W176 (SM seat, row 1458, READ
  not recomputed) K0/K1 "no condition the weave forces on the line selects a class within an order"; the web seat's
  selector (row 1460) (iv) "on slope 2/5 no extending line breaks SU(5)", (v) the counted class has the *highest* V* of
  eleven classes; W171 (row 1446) removes (2/5, odd/10) in the surface frame; W175 prefers the order-5 CP-conserving
  class. B1809 FINDINGS:239–243 lists it as an open door. The one candidate rule is P-422's.
- **Potential:** HIGH if found — it is the positive way to pay debt #2 (P-384: "what selects the single line class
  (2/5, odd/10)"), turning the strip candidate's pick into a forced input; the record's tries so far all fail.
- **First computation:** a design study listing every consistency condition on record with its verdict on (2/5,
  odd/10) (W171, W175, W176, row 1460 (i)–(v)), then the one untried: an anomaly/Green–Schwarz condition on the
  line; days; data-free.
- **Proposed disposition:** STILL A LEAD (umbrella for P-422 and P-456; merge candidates).

### P-412 — the frame null (register line 560; QUEUED; no L)
- **Idea:** test whether B1656's frame is specific to the six beyond its exponents: permute the log-prefactors across
  the frame's rows (N1) and compare with Froggatt–Nielsen populations of fixed width (N2), sealed.
- **Status on the record:** COMPUTED, sealed, by the web seat on main's word: both cells INTERMEDIATE (1 in 270
  permuted frames; 1 in 430 FN populations) — row 1469 (sealed e56a311ce, status READ, not recomputed on main);
  docs/LOOK_LEDGER.md:82 ("not a look", ruled at S257 under P-445, register line 593); the post hoc findings (2/5 lines
  carry 94% of N1's first hits; the down–lepton relation is part of what fits) are P-446, register line 594, a
  ranked DEBT (#5).
- **Potential:** LOW now — its number exists; the live residue is P-446's.
- **First computation:** none for this row; if main wants REPRODUCED rather than READ, rerun the seat's script
  427a3220e on main (an hour).
- **Proposed disposition:** ANSWERED — close DONE (row 1469; LOOK_LEDGER:82; residue carried by P-446).

### P-413 — a forced weight for the sum over threads (register line 561; QUEUED; no L)
- **Idea:** any thread sum is mirror-even and the democratic one is flat; look for a forced convergent weight whose
  minimum could sit off the mirror lines.
- **Status on the record:** relocated and then subsumed by the clock: B1813 (arc_verdict: "the counting rule is
  CHOSEN"; the weight is e^(−s·ℓ), s = 0 move count, s = 1 area; FINDINGS:145 names P-413 as bearing); B1815 ("The
  clock stays CHOSEN"; discrete symmetry cannot decide; Dani's door CHOSEN); B1816 (Weil–Petersson a third
  frame-native weight; "nothing here ranks the clocks", "no clock studied picks a point"). No forced weight on record.
- **Potential:** LOW as its own row — a forced weight is exactly a forced clock, P-439's question.
- **First computation:** none separate from P-439.
- **Proposed disposition:** SUPERSEDED — merge into P-439 (B1813 verdict line; B1815; B1816).

### P-415 — THE TOWERS: the SM as the interaction of towers meeting at loci (register line 563; QUEUED; no L)
- **Idea:** the owner's question: reality as the interaction of what is allowed on all towers SU(5) ⊂ SO(10) ⊂ E₆
  (matter where the singularity enhances, up-type Yukawas at E₆ points, down-type at SO(12) points), each tower
  supplying what the others lack; a breakthrough only if the object fixes where and how they meet.
- **Status on the record:** tested in two frames, open in others. G₂ (Witten) frame: NEGATIVE (B1805;
  docs/THE_TOWERS.md:139–152: SU(5) keeps the mechanism and lacks the parity, Spin(10) the reverse). F-theory 7-brane
  frame: B1812 NEGATIVE as first written, narrowed at Review 73 (docs/THE_TOWERS.md:154–164): inside the object's class
  A⁹BCC the chain SU(5) ⊂ SO(10) ⊂ E₆ CAN meet at a point, but positions are moduli — "allows the meeting and does not
  select it … a bigger menu, not a breakthrough"; the selecting dynamics is P-466 (register line 614, LEAD). Two-W
  tension: P-424. B1825 FINDINGS:79 cites P-415 as the expectation its one-address NEGATIVE confirms; FRAMING_LEDGER
  FL-07 (docs/FRAMING_LEDGER.md:36) names "separate loci for up and down (the CKM as a relative rotation)" as what the
  one-address framing excludes; that hatch is P-555.
- **Potential:** HIGH — it is the structural home of the only live CKM hatch (P-555: up and down diagonalised at two
  addresses) and of different Higgs constructions per sector (up at an E₆ point, down at an SO(12) point), the wall
  B1827 traced to the Higgs construction; it would change direction if the object fixed the meeting loci. Known
  against: in every frame tested the object fixes the total class, not the positions.
- **First computation:** the frame × rung × verdict table the row adopted at S256 (B727, B1805, B1812 as narrowed),
  then one data-free question: in B1812's configuration, does the object's class fix the *relative* position of an E₆
  (up) and an SO(12)/D₆ (down) enhancement, i.e. the two-address offset P-555 needs? Days; data-free.
- **Proposed disposition:** STILL A LEAD (umbrella; P-416, P-424, P-466 and P-555 are its sub-rows).

### P-416 — local G₂ models with coincident multiplets (register line 564; QUEUED; no L)
- **Idea:** Witten's first model on m004's even fillings needs 4 or 7 of its 8 multiplets at one fixed point; ask
  whether a conical singularity (or cluster) carrying V with three 10's or three 5̄'s exists and what classical Yukawas
  coincidence gives.
- **Status on the record:** untouched beyond B1803 (FINDINGS:118–126 and 148–153: "realisation OPEN (P-416)"); sweep
  `coincident multiplet|Heckman.Tavanfar|codimension.7|conical singularit --full`: only B1803. Note B1805 (THE_TOWERS
  :139–152): Witten's first model in this frame lacks matter parity, so a realisation would still leave the proton
  problem.
- **Potential:** LOW — even if realised, the G₂ frame's own negative (B1805) stands, and the coincidence points are not
  object-fixed beyond B1803's four.
- **First computation:** literature at source (Acharya–Witten; Heckman–Tavanfar–Vafa) for the enhancement a point with
  V + 3×10 requires; days; data-free.
- **Proposed disposition:** STILL A LEAD (sub-row of P-415; merge candidate).

### P-418 — ONE HONEST SCOREBOARD: the total-inputs vector (register line 566; QUEUED; no L)
- **Idea:** print beside "0 of 19" a named, graded vector — the fitted continuous parameters, the discrete choices in
  bits, the unearned identifications — generated from the registers at every landing; progress = an item removed.
- **Status on the record:** adopted by the owner (S249, S254 rulings in the row); schema and first FR-FIB rows exist
  (rows 1478, 1479; docs/MAINS_PLAN.md:72); the generator is UNBUILT — B1827 FINDINGS:113 (A6: "the owner's total-inputs
  scoreboard (P-418, 2026-10-29) is unbuilt"); FRAMING_LEDGER FL-19 (docs/FRAMING_LEDGER.md:111) and §G item 0
  (:70, "P-418's input vector built as the headline (P-579)"); no script in scripts/ or tests/ generates it (grep
  `total.inputs|input vector|scoreboard`: only B1261/B1660 tests).
- **Potential:** MEDIUM — produces none of the 19, but it is the recognition instrument the S291 audit says the
  programme lacks (the board "cannot move under any outcome of any current test").
- **First computation:** the generator: read INPUT_COMPLETENESS_LEDGER, IDENTIFICATION_LEDGER (B1266's union-find),
  each arc's CHOSEN labels, print the vector, add a doc-facts gate; a day; data-free.
- **Proposed disposition:** SHOULD BE A DEBT — P-579 (ranked debt #19, register line 727) names "build P-418's vector"
  as its next action and the front-document headline rests on it; retype [DEBT] or merge into P-579 (one row, not two).

### P-419 — SELECTION BY INVERSION: discrete SM data forcing the moduli onto special loci (register line 567; QUEUED; no L)
- **Idea:** instead of potentials, ask whether the SM's discrete data (three, the hand, doublet–triplet, matter
  parity) force the continuous moduli onto a rigid locus (Donagi–Wijnholt's Noether–Lefschetz precedent).
- **Status on the record:** worked frame by frame, every frame NEGATIVE for a forced point: B1804 (split frame: curves
  only; holomorphic frame: isolated CM points chosen by free flux integers, no invariant Kähler class); B1808 NEGATIVE
  ("three generations cut a curve, not a point"; LAW_MAP:348); B1812 (7-brane card, NEGATIVE for loci); row 1473 (two
  three-generation fluxes leave a menu of five classes). Left on its card: "an E₆ meeting point with flux breaking"
  — sweep `E.?6 meeting point|flux breaking --full`: no arc. The owner made it the main line at S249; the final attack
  (B1823–B1825) went another way.
- **Potential:** MEDIUM — a forced locus would select τ (one of the programme's named walls); three frames fail and the
  remaining one is the E₆ point P-415 also needs.
- **First computation:** the E₆ meeting point with flux breaking, as a frame card with the free data counted first
  (WORKING_RULES 2026-10-29 rule); days; data-free.
- **Proposed disposition:** STILL A LEAD (umbrella of P-425, P-449, P-450; merge them under it).

### P-422 — gauge the fibre's involution on the lines? (register line 570; QUEUED; no L)
- **Idea:** requiring each holonomy's square to be central with SU(5) broken admits on slope 2/5 exactly the odd
  tenths (the counted class), b-holonomy = centre × diag(1,1,1,−1,−1) (Kawamura's orbifold parity); is there a reason in
  the object to gauge the elliptic involution on the lines?
- **Status on the record:** untouched since row 1460 ("gauging the fibre's involution on the lines is the one
  candidate rule that would select the class, and it is not in the record"); B1809 FINDINGS:242 lists it open. Against:
  W176 K0/K1 (row 1458); row 1460 (iv) (no flat extending line on slope 2/5 breaks SU(5)); P-424's Fact 2 (no flat
  SU(5) bundle on m004 gives the frame's SU(5)-breaking fibre line).
- **Potential:** HIGH conditional — the only rule on record that selects (2/5, odd/10); if the object forced it, debt
  #2 (P-384) is paid positively and the candidate's line is no longer a pick. The involution is −I, which the record's
  group contains (GM5d, P-049: "positivity excludes −I from the updates, not from the group").
- **First computation:** data-free: is −I's action on the fibre, lifted to the SU(5) line bundle, a gauge symmetry of
  the frame (B1656's coupling invariant under (a, b) ↦ −(a, b) with the matter rule)? If yes, ask whether the frame's
  consistency requires gauging it (an orbifold, not a choice); a day; data-free.
- **Proposed disposition:** STILL A LEAD (merge under P-411).

### P-424 — THE TWO W's (register line 572; QUEUED; no L)
- **Idea:** B1802's order-2 W runs along the base and leaves the fibre line trivial, and no flat SU(5) bundle on the
  figure-eight complement gives the frame's SU(5)-breaking fibre line; find which way out ((a) the line a counted
  choice, (b) breaking along the base, (c) a cyclic cover of input degree, (d) a non-flat connection) the record takes.
- **Status on the record:** untouched since row 1464 (Facts 1–3; READ, not recomputed on main); docs/THE_TOWERS.md
  :128–137 records it. No arc picks a way out.
- **Potential:** MEDIUM — Fact 2 says the strip candidate's lines are not the restriction of any flat SU(5) bundle on
  the object, so the line class is CHOSEN at the frame level (way (a)); ways (c) and (d) are the only routes to an
  object-supplied line. Way (d) has a natural candidate in P-458 (the canonical non-flat spin connection, curvature
  fixed by Mostow).
- **First computation:** reproduce Fact 2 on main (exact, in Fractions; the seat's bridge_check2.py); then record which
  of (a)–(d) the strip card (P-585) adopts; hours; data-free.
- **Proposed disposition:** STILL A LEAD (sub-row of P-415; P-458 is its way (d)).

### P-425 — CM by the object's own compositum ℚ(√5, √−3)? (register line 573; QUEUED; no L)
- **Idea:** in B1804's holomorphic frame, require CM by K = ℚ(√5, √−3) to cut the flux freedom to a finite set of
  points.
- **Status on the record:** first computation done and corrected in the row itself (S239): K has class number 1;
  requiring CM by K is itself a CHOICE (B334 banked the Hilbert class field; B336 NEGATIVE: √−15 unreachable by
  monodromy and commensurator). B1808's referee: the K point lies on the three-generation curves, "one of infinitely
  many such points, not a selection"; row 1473 (VERIFIED by main's recount): five NS classes in four CM fields
  ℚ(√5, √−d), d = 2, 3, 7, 11; "no condition on record forces d = 3". P-527 (ranked DEBT, register line 675) owes its
  re-disposition: the revised Step B dropped the forced-CM arm it rests on.
- **Potential:** LOW — the remaining question (does anything force d = 3) has no candidate, and P-494 shows CM points
  near the strip are expected by density.
- **First computation:** none new; P-527 decides whether a CM read-out returns to a card.
- **Proposed disposition:** STILL A LEAD, narrowed to "does any condition force d = 3"; merge under P-419; its fate is
  P-527's.

### P-437 — the owner's whole-existence computation, unforced (register line 585; QUEUED; no L)
- **Idea:** let the weave produce its own measure over worlds without forcing, count both ways (moves, length), and see
  whether the measured world is a typical draw.
- **Status on the record:** its stages are landed: stage 1 B1813 (PROVED: the measure depends on the counting rule);
  stage 2a in the audit room (audit/drafts/weave_measure/stage2a_typical_world.py, unrefereed); stage 3 B1814 (sealed
  86cb26b30, NEGATIVE as sealed for D2; "the clock question goes to the theory side (P-438, P-439)", B1814
  FINDINGS:138). The row's remaining open question ("why the weave would sit at its critical point") is P-439's.
- **Potential:** MEDIUM for the remainder (via P-439); none left in this row.
- **First computation:** none for this row.
- **Proposed disposition:** ANSWERED — close DONE (B1813, B1814; the remainder carried by P-439).

### P-438 — FOLLOWED OR COUNTED (register line 586; QUEUED; no L)
- **Idea:** counting closed threads word by word gives the thick phase (Minkowski), following one thread from a typical
  start gives area (the critical point); which is the weave's history: fair-coin letters or a generic number's digits?
- **Status on the record:** its data-free table is computed (audit room; recorded in the tracked
  docs/THE_CLOCK_AND_THE_NEXT_ATTACK_2026-10-29.md:65, row C); B1815 proved the record's walk has Minkowski's exit law
  exactly and "the clock stays CHOSEN" (nothing forces 'followed'); reader A's point (row text, S257) that 'followed'
  smuggles in the geometric clock. The question is now word for word P-439's.
- **Potential:** LOW as its own row.
- **First computation:** none separate from P-439.
- **Proposed disposition:** SUPERSEDED — merge into P-439 (B1815 verdict line; THE_CLOCK doc §2 row C).

### P-439 — THE CLOCK: move count or geodesic flow? (register line 587; QUEUED; no L)
- **Idea:** decide whether the weave's time is the move count (Minkowski, thick phase) or the geodesic flow (Liouville
  / area, critical phase, deep hierarchies typical); or a third (Weil–Petersson).
- **Status on the record:** worked hard, CHOSEN throughout: B1815 (T1–T4: the discrete symmetry cannot decide; FR-FIB
  never sees word length; Dani's door CHOSEN; "consistent with both clocks"); B1816 (WP a frame-native third clock;
  "nothing here ranks the clocks"); row 1505 (premise map, verified with corrections: for observables of τ alone the
  clock does not decide the premise; FR-FIB's outputs, several-point observables and other τ-dynamics OPEN); LAW_MAP
  :349; docs/THE_WEAVE.md:599. Untried: door D (a clock-free observable reading several letters of one history) and
  door E (the rising factor) of docs/THE_CLOCK_AND_THE_NEXT_ATTACK_2026-10-29.md:181–195.
- **Potential:** MEDIUM — a forced clock would make "deep hierarchies are typical" a derived structural fact (the doc's
  §7 recommendation), but it yields a measure, not a point, and B1814 shows the six cannot tell the clocks apart.
- **First computation:** door D's design note: which FR-FIB observables read more than one τ of one history (the
  mixings; generations as successive letters, cf. FL-10); days; data-free.
- **Proposed disposition:** STILL A LEAD (absorbs P-413, P-438, P-440).

### P-440 — THE PURE MOVE CLOCK (register line 588; QUEUED; no L)
- **Idea:** a clock that ticks once per Farey crossing puts every sampled τ on Re τ = 0, a third measure not run in
  B1814; then ask whether the CP-fixed line is forced rather than chosen.
- **Status on the record:** computed in the audit room only (audit/drafts/briefing_2026-10-29/G_pure_move_clock_J.py;
  recorded in docs/THE_CLOCK_AND_THE_NEXT_ATTACK_2026-10-29.md:67, row G: τ exactly on Re τ = 0, J ≠ 0 on 178 of 266
  lines); unrefereed, unbanked; its height law and the "CP line forced?" question not done.
- **Potential:** LOW — one more CHOSEN clock; it puts τ on the CP-symmetric axis but the lines break CP anyway, and
  P-373 records Re τ as nearly flat for the six.
- **First computation:** land the audit-room table as an arc after a referee (the height law under the pure clock);
  hours; data-free.
- **Proposed disposition:** STILL A LEAD (merge under P-439).

### P-443 — INHERITED ASSUMPTIONS (register line 591; QUEUED; no L)
- **Idea:** audit every assumption the programme inherits from the SM and spacetime picture (the 19 fixed constants;
  the world at one point; deriving = pinning the point), with where the record relaxed each and what an arc relaxing the
  rest would compute.
- **Status on the record:** DONE twice over: docs/THE_CLOCK_AND_THE_NEXT_ATTACK_2026-10-29.md §6 (lines 168–179,
  headed "The inherited assumptions (P-443, the owner's question)": six assumptions, each with what the record now
  suggests); and comprehensively B1827's FRAMING_LEDGER (docs/FRAMING_LEDGER.md, the owner's "what are we excluding by
  the way we frame the program?": every framing commitment with status, what it excludes, the evidence it costs, and
  the reframing rule).
- **Potential:** LOW as a row (the deliverable exists; its consequences are FRAMING_LEDGER's rows).
- **First computation:** none.
- **Proposed disposition:** ANSWERED — close DONE (THE_CLOCK doc §6; docs/FRAMING_LEDGER.md, B1827).

### P-449 — values at the CM points (register line 597; QUEUED; no L)
- **Idea:** a data-free table of FR-FIB's outputs at the CM points of B1804/B1808's flux menu and at the images of i and
  ω under the object's cyclic isogenies, before any sealed comparison.
- **Status on the record:** the data-free table is computed in the audit room (audit/drafts/p449/: cm_table.py,
  cm_zero_line.py, summary.json; 213 CM points, |D| ≤ 800), unrefereed and unbanked; the comparison was to be banked
  with THE RIGID WORLD's seal, and the revised Step B dropped the forced-CM arm — P-527 (ranked DEBT, register line 675)
  owes restoring a CM read-out or re-disposing this row.
- **Potential:** LOW-MEDIUM — the shortest route to an integer-fixed τ (THE_CLOCK doc §7 door G), but the menu is
  large and P-494 shows CM points in the strip occur by density.
- **First computation:** referee and land the audit-room table as a data-free arc (no comparison); hours.
- **Proposed disposition:** STILL A LEAD (under P-419; its fate is P-527's decision).

### P-450 — the three-generation curve as T₁₅ (register line 598; QUEUED; no L)
- **Idea:** B1808's referee read the three-generation curve, in van der Geer's normalisation, as the Hirzebruch–Zagier
  cycle T₁₅; if so the Noether–Lefschetz/Humbert literature gives its intersections with CM points.
- **Status on the record:** untouched; B1808 FINDINGS:111–112 "a lead to check at source, not a claim"; no other arc.
- **Potential:** LOW — an identification on a frame already NEGATIVE for selection (B1808).
- **First computation:** read van der Geer at source and check N = det M_w = 15 against B1808's lattice; hours.
- **Proposed disposition:** STILL A LEAD (merge under P-419/P-425).

### P-453 — flux as the puncture degree (register line 601; QUEUED; no L)
- **Idea:** if matter's flux-one bundle is O(p) and the Higgs's O(2p), with p the fibre's cusp, the flux quanta are the
  degree of the object's own marked point rather than free.
- **Status on the record:** untouched (only the triage mentions it). Context: B1800 computed the flux-one/flux-two
  overlaps (arc_verdict) and P-401's B1794 found the cusped m004's one relative class is end data "its integers free
  topologically" (register line 549).
- **Potential:** LOW — a marked point fixes which degree-one bundle (the base point, i.e. a Wilson-line datum), not the
  degree itself (O(np) is as allowed as O(p)); the 2-torsion even characteristics do not reach the order-10 lines.
- **First computation:** check B1800's flux-one sections against H⁰(O(p) ⊗ even spin) and state what translation
  freedom the cusp removes; hours; data-free.
- **Proposed disposition:** STILL A LEAD.

### P-454 — THE WEIL FILTER (register line 602; QUEUED; no L)
- **Idea:** the Weil representation of a thread at level N = 5, 10 (trace, fixed vectors, Gauss-sum phases) as an
  object-supplied weight that might single out slope 2/5 or v over 2v (B1733's bit).
- **Status on the record:** not run for this purpose, but the row's "never tried since B1600" misses a pre-B1600 corpus
  (Seen first owed): B355 rebuilt the Weil representation at N = 3, 5, 15 (all 605 triple products exactly real);
  B413 (the tower measure flat, |L(χ)| = 1/4, Gauss-sum phases); B214/B283 (the WRT period law, generic to all torus
  bundles, Jeffrey 1992); B587/B588 (Weil Gauss-sum terms; "identical √5 Gauss data even on one stage and odd on the
  other"). B1733: multiplication by 2 commutes with A, so no thread-built rule chooses v over 2v.
- **Potential:** MEDIUM-LOW — at N = 5 the Weil phases distinguish residues from non-residues (2 is a non-residue
  mod 5), so they could separate v from 2v, but only through the choice of additive character, which is likely B1733's
  deck involution relabelled; B413's flatness says magnitudes will not select.
- **First computation:** with B355's instrument, ρ₅(RL) and ρ₁₀(RL) on the characteristics of the order-5/10 lines,
  diagonal entries and fixed vectors, and whether the v/2v difference survives a change of additive character; hours;
  data-free; grade any selection with B1798's class-choosing null.
- **Proposed disposition:** STILL A LEAD (merge under P-411; add B355, B413, B588 to its Seen first).

### P-455 — THE PERIOD AVERAGE (register line 603; QUEUED; no L)
- **Idea:** read the six as a Petersson-weighted average of the couplings along a thread's period, which has no free
  point, instead of at one τ.
- **Status on the record:** never run on masses (sweep `period average|…|sizes from motion|time.average --full`: one
  arc, B1663, which averages one τ-function, not the couplings). Related: B1720 ("along each best geodesic the fit is
  best at the apex"); B1722 (no record measure selects the thread).
- **Potential:** MEDIUM-LOW — removes the point but leaves "which thread" (B1722 NEGATIVE); B1720's profile suggests
  averaging dilutes the apex fit, though averaged couplings are a different quantity.
- **First computation:** on B1749's strip threads and a matched random set, the period-averaged ratios on the
  (2/5, odd/10) lines, hierarchical or not, data-free; a day.
- **Proposed disposition:** STILL A LEAD.

### P-456 — a least-description line rule (register line 604; QUEUED; no L)
- **Idea:** seal a rule "the least line order, then the least offset denominator, that splits down from leptons and
  carries a hierarchy" before reading the six, and see which class it picks.
- **Status on the record:** untouched. Known against, from B1703 (arc_verdict: d = e iff N | 4 or 5, u = d iff N | 6,
  u = e iff N | 2 or 7; every order from 8 on splits all three): orders 3, 6, 7, 8 and 9 come before 10 and split down
  from leptons, so the rule picks the candidate's order-10 class only if "carries a hierarchy" excludes every lower
  order, a clause that must be data-free and sealed first. Any rule written now is written after the class is known
  (P-384's lesson; B1798's class-choosing null).
- **Potential:** LOW — a rule chosen knowing the answer is the pick P-384 warns about; useful mainly as the
  description-length charge for the class (P-576).
- **First computation:** read B1703's census for the least splitting orders and state, data-free, whether a
  "hierarchy" clause can exclude orders 3–9; an hour.
- **Proposed disposition:** STILL A LEAD (merge under P-411).

### P-457 — the 12 behind the convention that sets Im τ (register line 605; QUEUED; no L)
- **Idea:** tabulate where conventions enter the height (the η power m, the end-data weight shift 12n, the χ_η twists)
  and whether the ℤ/12 character and Rademacher's Ψ are constant on B1749's strip threads.
- **Status on the record:** untouched. Related: P-398 (register line 546, LEAD): the Higgs's Petersson peak moves with
  the η power m (2.31–3.82), "set by a discrete convention, not forced".
- **Potential:** LOW-MEDIUM — if one convention (m) both sets the height and is fixed by a ℤ/12 invariant of the strip
  threads, τ's height would be a forced convention; otherwise a bookkeeping table.
- **First computation:** the data-free table (where each 12 enters; Ψ on the strip threads with a run of five);
  hours.
- **Proposed disposition:** STILL A LEAD (merge with P-398).

### P-458 — the spin connection as L250's background (register line 606; QUEUED; L250)
- **Idea:** ω = Re A, the object's one canonical non-flat compact SU(2) connection with curvature fixed by Mostow, as a
  background for L250; compute the twisted Dirac spectrum on m004 coupled to ω.
- **Status on the record:** untouched. B1794 (P-401's row) found only flat or trivial canonical holomorphic bundles.
  The proposed instrument is B940's, whose ± check is now owed a source (P-540, ranked DEBT #38: B933 §5a's J gives
  Kramers doubling, not λ ↔ −λ); P-330 (chunk 3) plans C10 on m004 with the same instrument and the ρ_T twist.
- **Potential:** MEDIUM — FRAMING_LEDGER FL-02: 107 of the record's 173 value-kills sit on flat premises (GAP6); this
  is the one object-supplied non-flat background with no free data, and it is P-424's way out (d). Hard: a cusped
  manifold, continuous spectrum.
- **First computation:** settle P-540 first (it is the instrument's debt); then B940's run with the coefficient
  changed, both spin structures, m004 against m003; about an hour a run once the instrument is cleared; data-free.
- **Proposed disposition:** STILL A LEAD (sibling of P-330, same instrument; links P-424 (d)).

---

## Chunk 4 tally

| proposed | rows |
|---|---|
| STILL A LEAD | 18 — P-405, P-411, P-415, P-416, P-419, P-422, P-424, P-425, P-439, P-440, P-449, P-450, P-453, P-454, P-455, P-456, P-457, P-458 |
| ANSWERED (close DONE) | 3 — P-412, P-437, P-443 |
| SUPERSEDED | 2 — P-413 → P-439; P-438 → P-439 |
| SHOULD BE A DEBT | 1 — P-418 (or merge into P-579) |

**Merge groups.** (1) THE CLOCK: P-439 ← P-413, P-438, P-440. (2) WHAT SELECTS THE LINE CLASS (the positive side of
debt P-384): P-411 ← P-422, P-456, P-454. (3) SELECTION BY INVERSION: P-419 ← P-425, P-449, P-450 (fate via debt
P-527). (4) THE TOWERS: P-415 ← P-416, P-424, (P-466, P-555 outside this chunk). (5) P-418 = P-579's action.
(6) P-458 and P-330 share B940's instrument, under debt P-540. (7) P-457 with P-398 (the η power that sets the height).

### P-459 — Criticality as m_H (register line 607; QUEUED; no L-number)
- **Idea:** if the frame's own potential gave the Higgs quartic at its scale, λ ≈ 0 there (criticality) would fix m_H
  with no fitted number; run B1670's four-loop code up to the Planck mass.
- **Status on the record:** untouched as a frame computation. The SM side of criticality exists: B1670's cell T8
  (frontier/B1670_the_price_of_the_nineteen/FINDINGS.md:80) priced m_H by criticality using measured inputs (not
  quoted here). No frame on record supplies a Higgs quartic: B1704 and W154 are τ's potential, not the Higgs's
  (B1704 arc_verdict claim). B1823 §5 (frontier/B1823_step_a_the_tied_heavy_vacuum/FINDINGS.md:235–237) says that in a
  non-supersymmetric reading the tree quartics are CHOSEN (zero or tuned), and in the supersymmetric reading the quartic
  would come with the H_u completion (P-536). The row's premise ("if the frame's potential gives a quartic") is unmet.
- **Potential:** LOW — m_H is one of the 19, but only through an outside hypothesis (criticality), and the record has
  no frame-level Higgs potential to supply the boundary value.
- **First computation:** a reading first: does any frame on record fix the Higgs quartic at a scale (B1656/FR-FIB,
  B1823's heavy sector, the D-term of a supersymmetric completion)? Hours, data-free. Only if yes: the running, which
  needs a seal (it compares with m_H).
- **Proposed disposition:** STILL A LEAD, noted as blocked behind a Higgs potential in the frame (P-536's completion
  is the only route on record).

### P-460 — Doublet legs on a spin structure (register line 608; QUEUED)
- **Idea:** twist only the SU(2)-doublet legs (Q, L, H) by a half-period of one of the fibre's three even spin
  structures, and ask whether the down sector stops equalling the leptons on the (2/5, odd/10) lines and whether
  B1790's S ↔ S̃ symmetry breaks.
- **Status on the record:** untouched. Full-text sweep `doublet legs|half-period twist|antiholomorphic slot` finds
  only this row. Nearest work: B1790 (FINDINGS.md:33–35) shows a uniform half-period shift is not a symmetry of the
  readings, but does not twist the doublet legs alone. B1800 (FINDINGS.md:35–36) notes that in the bulk-overlap frame
  every fermion shares one spin structure. B1728's swap law (Y_e = Y_d^T on order-5 lines) is what such a twist would
  have to break. My reasoning, not computed: the swap maps down's doublet leg to the leptons' singlet slot, so a
  doublet-only twist acts on different slots in the two sectors.
- **Potential:** MEDIUM-HIGH — it bears directly on debt #1 (P-355: on the order-5 lines c = 3 / D = 9 is
  Georgi–Jarlskog's by construction, and the strip candidate sits ~3σ off P-094's D). It is a structural mechanism that
  could split down from leptons without a 45. It costs one discrete choice (which spin structure, which legs), counted
  as an input, and it breaks SU(5)-type leg relations, against the towers reading.
- **First computation:** add the twist to B1726's compute(). Then, data-free: (i) does Y_e = Y_d^T survive on the
  order-5 lines; (ii) does B1790's S ↔ S̃ map still preserve the readings; (iii) D as a structural function on the
  order-10 lines, with no χ². Hours. Any χ² needs a sealed rule.
- **Proposed disposition:** STILL A LEAD (rank it with P-355's debt; it is the cheapest structural probe of D on
  record).

### P-461 — The Dabholkar–Hull valley and FPST (register line 609; QUEUED)
- **Idea:** two literature walls. (a) The Dabholkar–Hull duality-twist potential V(τ) for B1720's thread classes: is
  its valley the thread's geodesic axis? (b) FPST's modular-invariance mechanism for strong CP: is det M_q
  τ-independent and real at the frame's weights?
- **Status on the record:** (a) untouched. The sweep `Dabholkar|Hull|FPST|2406.01689|det M_q` finds no arc on DH or
  FPST (its 8 hits are unrelated uses of "hull"). (b) overlaps P-323 (register line 471). P-323 and harvest rows
  1411/1414 (the web seat's e20–e20d) already record data-free structural facts about arg det(Y_u Y_d) in B1726's
  reading, including how the T-step and b-shifts move it. They are not quoted here (firewall). They bear on whether
  det M_q is τ-independent. P-585 lists θ̄ as a held-out level-2 target with one prior look (P-323), and the S298
  harvest counted the agy lane's unsealed θ̄ computation as a prior look (CHANGELOG S298).
- **Potential:** MEDIUM. (a): if V depends only on the displacement d(τ, Mτ), its minimum set is exactly the axis of M
  (the translation length is attained only there), a physical reason for τ on the thread's geodesic. That fixes one
  coordinate, not the height; my reasoning, to be checked. (b) decides whether θ̄ is a clean prediction of the
  candidate family at all (Re τ is nearly flat on the strip, P-373).
- **First computation:** (a) write DH's twist potential for a hyperbolic SL(2,ℤ) twist and check whether it is a
  function of d(τ, Mτ); evaluate it on LR and on L⁵RLR². A day, data-free. (b) only inside P-585's sealed level-2
  card, as its θ̄ design question: is the frame's θ̄ fixed by modular invariance, or a function of Re τ?
- **Proposed disposition:** STILL A LEAD for (a). (b) is a merge candidate with P-323, and a prerequisite of P-585's
  θ̄ target.

### P-462 — B707's three bridge tests, arithmetic Chern–Simons (register line 610; QUEUED)
- **Idea:** run the three meeting-point tests B707 named (Kim's arithmetic-CS torsor against the 𝔽₂ seam; Scholze's
  Habiro ring against the A-polynomial; Lee's CS = regulator identity), the first "cheap as written".
- **Status on the record:** STALE. The row's premise, "never run", is false for the first test. B708 is "B707's #1",
  sealed prereg 96ebff1d (frontier/B708_kim_seam/FINDINGS.md:1–4), verdict MEET: the seam is the multiquadratic
  subspace of H¹(G_ℚ, ℤ/2), and the two-hands coupling is the Hilbert-symbol linking number. B905 paid the literature
  gate: its Q2 anchors test 2's setting (GSWZ's founding example is the figure-eight over ℚ(√−3)). B1108 closed the
  archimedean question NEGATIVE: arithmetic CS is finite-group-valued and meets the object only on the vanishing CS
  term. B1156 sharpened this (the full/Arakelov version carries Vol as the Borel regulator of ξ ∈ K₃(ℚ(√−3))). Test 3's
  identity is B680's Vol(4₁) = (3√3/2) L(χ₋₃, 2) plus B1156's regulator. Only test 2, as literally worded, has no
  computation. B707's own arc_verdict line ("three bridge tests named, none run") is itself stale; it is a P-334-type
  stale OPEN verdict.
- **Potential:** LOW — B1108 shows the finite-place theory cannot reach the object's archimedean content. Nothing for
  the 19.
- **First computation:** none owed. If wanted, test 2 as a literature reading of GSWZ against the record's A-polynomial
  (a day).
- **Proposed disposition:** ANSWERED. Close DONE: test 1 by B708; the line closed by B1108 and B1156; test 3's
  identity by B680 and B1156; test 2 DECLINED (no bearing, per B1108). Add a dated note to B707's verdict (P-334).

### P-463 — Two E₈'s (register line 611; QUEUED)
- **Idea:** the record's E₈ (B1752's container of the McKay rungs), its E₆ cascade (B727), and DHIZ's 7-brane chain
  inside E₁₀ (B1812) share names. Is there a faithful map from the record's containers to the brane
  subconfigurations, or are they unrelated?
- **Status on the record:** untouched. B1812 §3 says it outright: "No map from those to these subconfigurations is
  shown" (frontier/B1812_the_towers_in_f_theorys_seven_brane_frame/FINDINGS.md:80–81). Nothing since. B1815 refuted
  the nearby reading that the letters count branes (B1815 claim: L is conjugate to no 7-brane monodromy).
- **Potential:** LOW-MEDIUM — an identification question (the Identification Rule). It would matter only if the
  record's level-5 E₈ and the brane E₈ were one structure, and that would not supply a value.
- **First computation:** a reading: the McKay route (level-5 quotient → 2I → E₈ du Val singularity) against the Kodaira
  II* fibre's monodromy (order 6) and DHIZ's A⁷BC. Ask whether the record's level-5 image of LR relates to the II*
  class. Hours to a day, data-free.
- **Proposed disposition:** STILL A LEAD (merge candidate with P-415/P-466's towers cluster).

### P-465 — The principle as the selection (register line 613; QUEUED; the owner's question)
- **Idea:** could the selection principle be the genesis rule a → ab, b → a itself? Followed literally it is the
  golden thread (runs 1 or 2, apex √5/2), so a world's hierarchy would measure its history's departure from that ground
  path.
- **Status on the record:** answered for its computable half. The S257 note in the row itself, and
  docs/THE_CLOCK_AND_THE_NEXT_ATTACK_2026-10-29.md:65 (table row E) and :78, record it. In B1636's frame the principle's
  path gives the golden spectrum exactly. In today's frame m₂/m₃ stays order one along the path. "No hierarchy from the
  principle followed literally." The briefing's §4 (line 145) concludes: "It sets the ground path; it does not select
  our world." The residue, what drives the departures, is the clock question (P-439; B1813's run statistics; B1815:
  "the clock stays CHOSEN"). The computation is audit-room only (gitignored); the tracked evidence is the dated briefing
  doc.
- **Potential:** LOW now — answered negatively; what remains is P-439.
- **First computation:** none owed. If main wants the audit-room table on a clone, commit it as a verification file.
- **Proposed disposition:** ANSWERED. Close DONE → docs/THE_CLOCK_AND_THE_NEXT_ATTACK_2026-10-29.md:65 and §4; the
  departure question is P-439's.

### P-466 — The tower flow as the selection (register line 614; QUEUED; the owner's question)
- **Idea:** one dynamics that drives τ and the 7-brane positions together, so that how deep the breaking goes
  (E₈ → E₆ → SO(10) → SU(5) → SM) and how deep the hierarchy goes are one excursion.
- **Status on the record:** open, and the row is current. The web seat's design study (harvest row 1477,
  docs/HARVEST_LEDGER.md:1525; speculation, no script) found depth positional in the base's semi-flat metric and no
  potential on brane positions on record. Review 73 narrowed B1812 (THE_TOWERS.md:158–164): SU(5) ⊂ SO(10) ⊂ E₆ can
  meet at a point; allowed, not selected; "A dynamics that would select it … is P-466". B1815 refuted letters-as-branes.
  Nothing since S264.
- **Potential:** MEDIUM-HIGH — it would join three open questions (τ not selected, the towers, the clock). No
  computable form is on record yet, so the potential is conceptual.
- **First computation:** state one candidate potential in the record's terms: τ's one-loop potential (B1704 / W154's
  V = −(A E(τ,3) + B E(τ,2))) pulled back through τ(z) of the brane positions. Ask whether it has an isolated minimum
  with branes coincident (an E₆ or SO(10) point) at finite Im τ. Days, data-free.
- **Proposed disposition:** STILL A LEAD (cluster with P-415, P-419, P-463, P-475).

### P-468 — Picked in combination (register line 616; QUEUED; the owner's question)
- **Idea:** a point (the strip, Im τ ≈ 3) needs a rising factor times a falling one. The row lists four forms: mixed
  clocks; the two-clock critical line's democratic point; a clock times a rising factor the programme supplies; the
  thread's coupling of line and height.
- **Status on the record:** STALE. Every form the row said to do first is done:
  - Form 1: answered in the row itself (no point).
  - Form 4: closed at S257 in the audit room (the briefing doc:66, table row F: "lines cannot pick a height"; :152).
  - Form 2: computed by the web seat and VERIFIED on main with main's own code (harvest row 1475,
    docs/HARVEST_LEDGER.md:1523, status VERIFIED S259; P-441 DONE). The democratic point's measure peaks at Im τ = 1
    and no point picks a height except through a chosen statistic. The A2 read-out was read, not recomputed.
  - Form 3 (the rising factor) is exactly P-475 / the briefing's T6.
- **Potential:** LOW for what remains here (carried by P-475).
- **First computation:** none.
- **Proposed disposition:** ANSWERED. Close DONE → harvest row 1475 (VERIFIED) and the briefing doc:66, :146–152; form
  3 carried whole by P-475.

### P-474 — Door D, a clock-free observable (register line 622; QUEUED)
- **Idea:** a clock test with power needs observables that read several letters of one history. The dimension of the
  endpoint law distinguishes the golden path, fair-coin letters and generic numbers.
- **Status on the record:** STALE. Main answered the design question at S261 (the row's note): inside FR-FIB no
  observable reads more than one letter. The web seat's item 5.2 design study landed: harvest row 1513
  (docs/HARVEST_LEDGER.md:1561), "NOT FOUND, as scoped", READ at S287. That row says it bears on P-555. P-555's own row
  (register line 703) carries it: "Read the web seat's door D (row 1513) first". The P-474 row was never updated past
  S276.
- **Potential:** LOW as its own row; whatever remains lives in P-555 (the mixing as two addresses).
- **First computation:** none here.
- **Proposed disposition:** SUPERSEDED by P-555 (harvest row 1513). Close DONE with that pointer.

### P-475 — Door E, the rising factor (register line 623; QUEUED)
- **Idea:** set τ's own one-loop potential (which runs to the cusp, B1686, B1704) against the threads' measure (which
  falls with depth). The product could peak, and so select a height.
- **Status on the record:** untouched. It is the briefing's T6 (docs/THE_CLOCK_AND_THE_NEXT_ATTACK_2026-10-29.md:214,
  "after the dial") and form 3 of P-468 (:149–150, "open"). The sweep `rising factor|door E` finds only the two rows.
- **Potential:** MEDIUM — a data-free height prediction would address "τ not selected". Known against it, my reading
  and not computed: W154's V ~ −A E(τ,3) grows like (Im τ)³ toward the cusp, so e^{−βV} swamps any exponential
  measure unless the relative weight β is small. That β is a free number, so at best one number buys one number. P-371
  (W150's μ/M̃) is the same shape.
- **First computation:** the density e^{−βV(τ)} · ρ_clock(Im τ) for both clocks on record: does any β give an interior
  maximum, and does it need tuning? The predicted height is sealed before any look at the strip. Hours, data-free.
- **Proposed disposition:** STILL A LEAD (absorbs P-468's form 3).

### P-476 — The action weight is a third clock (register line 624; QUEUED)
- **Idea:** the action weight e^{−Vol/π} of L154 and B1722 is "supercritical": vol(LᵃR) tends to the Whitehead link's
  volume as a grows, so the weight does not suppress deep runs, and its thread sum needs a cutoff.
- **Status on the record:** unverified (reader A) and untouched. B1722's W2 cell (FINDINGS.md:15–23) ran the action
  weight normalised over B1720's finite census. It already notes μ_A is "nearly flat" (LR only 2.7%). Yet its title,
  LAW_MAP row 319 and THE_WEAVE.md:854 state flatly that both measures "concentrate on short threads". If P-476 holds,
  that concentration is the census cutoff's, not the measure's. The critical line it would sit on is now located (P-441
  DONE, harvest row 1475).
- **Potential:** LOW for the 19. It matters for the record's accuracy: a sealed negative's headline may be a
  cutoff artefact.
- **First computation:** SnapPy volumes of the punctured-torus bundles LᵃR for a = 1…40 (and LᵃRᵇ). Check the limit
  and the divergence of Σ_a e^{−Vol/π}, then B1722's W2 read-out at two census cutoffs. Minutes to hours, data-free.
- **Proposed disposition:** SHOULD BE A DEBT (low rank), once the volume limit is confirmed (minutes). B1722's W2
  headline, LAW_MAP:319 and THE_WEAVE.md:854 state a concentration that holds only within B1720's length cutoff, and a
  scope sentence naming the cutoff is owed. Otherwise STILL A LEAD.

### P-477 — Thermal clocks (register line 625; QUEUED)
- **Idea:** each measure's own modular flow is its counting rule. Minkowski's measure would give a type III_½ flow,
  Lebesgue's a type III₁ flow. That would tie the clock to the thermal-time lineage (B716, B721, B723, B850).
- **Status on the record:** unverified, untouched. B1815 lists P-477 under "bearing on it" (FINDINGS.md:277) without
  addressing it. The lineage it would join is B721 (NEGATIVE): "the object's own clock is tracial type II₁ with trivial
  modular flow". Even if verified, each measure would carry its own flow, so this re-describes the clock choice rather
  than deciding it. B1815: "the clock stays CHOSEN".
- **Potential:** LOW.
- **First computation:** read Connes–Rovelli and the type classification of the boundary actions (the SL(2,ℤ) action on
  ℝP¹ with Lebesgue measure; the Radon–Nikodym cocycle of Minkowski's measure under the Farey maps). Hours, a reading.
- **Proposed disposition:** STILL A LEAD (low; a decline candidate at the next review if unread). Merge candidate with
  P-439.

### P-478 — The literature transfers (register line 626; QUEUED)
- **Idea:** read at source the outside literatures that met the same one-parameter measure problem: cosmology's
  measure problem (Garriga et al.), Bousso–Yang's counting-equals-following test, flux-vacuum counting (Ashok–Douglas;
  Ishiguro–Kobayashi–Otsuka on finite tadpoles at ω), and Mixmaster's clock-free invariants (Cornish–Levin).
- **Status on the record:** untouched. The full-text sweep of those names finds no arc. The briefing summarises reader
  B's claim, unread at source (docs/THE_CLOCK_AND_THE_NEXT_ATTACK_2026-10-29.md:35–37). B1815's literature list
  (FINDINGS.md:279–283) is a different set.
- **Potential:** LOW-MEDIUM — flux-vacuum τ-distributions are the one literature prior on where τ sits, and the
  tadpole result (clustering at ω) bears on τ selection.
- **First computation:** read the four items marked [A]/[B] at source and record what each actually proves. A day, a
  reading.
- **Proposed disposition:** STILL A LEAD. Merge candidate with P-439 (the clock) and P-477.

### P-479 — The likelihood design (register line 627; QUEUED)
- **Idea:** design any future clock test as a likelihood ratio between named clocks, and compute data-free how much
  evidence one world in the strip carries about the clock.
- **Status on the record:** untouched as a computation. The "about one nat" figure is reader B's, quoted in the
  briefing (doc:35, :139, :213 as T5), with no committed script. The sweep `Bayes factor|likelihood ratio|Sellke`
  finds no arc. Its purpose is undercut by S261 / B1815: FR-FIB has no observable reading more than one letter, so no
  clock test with power exists in this frame.
- **Potential:** LOW.
- **First computation:** the expected log-likelihood ratio per world between the move clock and the geometric clock,
  from their height densities on the strip (B1813/B1815 numbers). An hour, data-free.
- **Proposed disposition:** STILL A LEAD (low). Merge candidate with P-439 (the clock), as a design rule for its test.

### P-485 — The plenitude reframing (register line 633; QUEUED; the owner's)
- **Idea:** if every world the framework allows is realised, deriving the SM is three questions in order: (a) support
  (some configuration reproduces our world), (b) exclusion (what the framework forbids), (c) only then typicality.
- **Status on the record:** the B1830 triage declined a closure because (b) never ran (MAIN_VERIFICATION.md:19). B1825
  ran (a) for one restriction: FR-FIB, one rigid address, c = 3 set, graded NOT FOUND (B1825 FINDINGS.md:112, S298
  note). It claimed no exclusion (X1: none claimed). (c) is B1814's. The row's own where-cell already states that P-487
  carries (a) and (b) as one sealed test.
- **Potential:** HIGH conceptually, but its whole content is P-487's.
- **First computation:** as P-487.
- **Proposed disposition:** SUPERSEDED by P-487 — merge (DECLINED as a duplicate carried whole by P-487, citing the
  B1830 ruling so the unrun (b) stays visible in P-487).

### P-487 — The support test on the whole interaction (register line 635; QUEUED)
- **Idea:** one sealed test on the whole interaction (fibre frame × weave sums × towers), with c supplied by the
  interaction, never set. It asks whether any allowed configuration reproduces the measured pattern (support) and which
  patterns no configuration reaches (exclusion), against a specificity null that chooses as freely as the test.
- **Status on the record:** run only as a restriction. B1825 = FR-FIB, one address, c = 3 by hand, X1 "none claimed";
  NOT FOUND per B1825's S298 note (FINDINGS.md:112–115). The triage declined closure (MAIN_VERIFICATION.md:20). Its
  prerequisites are open: strand A (P-397, the lepton factor c from the interaction, register line 545) and strand B
  (P-371, W150's τ-holder, line 519). The bar's cells were adopted (S263).
- **Potential:** HIGH — the exclusion half is the only test on record that could make the framework falsifiable at the
  level of structure rather than fit. Supplying c from the interaction would address debt #1 (P-355, c = 3 by hand).
- **First computation:** data-free first: the exclusion census of FR-FIB as it stands. Which coarse patterns (corner
  order of |V|; sign structure of D − 9 on each line class; whether m₁/m₃ can be at the floor in one sector and not
  another) does no node of B1825's census reach? This is computable from the sealed census's aggregates without data.
  Days. The whole-interaction version waits on P-397.
- **Proposed disposition:** STILL A LEAD (absorbs P-485).

### P-491 — L1, the celestial reading of m004's Maass spectrum (register line 639; QUEUED)
- **Idea:** on the Milne cone over m004 (B1708), celestial holography's boost basis is L²(Γ\PSL(2,ℂ)), whose scalar
  part is m004's Maass spectrum, already computed (B739, B797, B922, B1021, …). The new content would be only the
  reading.
- **Status on the record:** untouched. The web seat's day ledger (harvest row 1483, docs/HARVEST_LEDGER.md:1531, READ)
  registered it with the seat's prior of 95% NEGATIVE for the 19. P-490 (the owner's evening questions) is DONE in chat.
- **Potential:** LOW — by the seat's own statement nothing for the 19 is expected.
- **First computation:** a reading of the celestial-holography literature against B1708's cone (hours). Controls m003
  and 5₂ only if a statement emerges.
- **Proposed disposition:** STILL A LEAD (low; a decline candidate). Merge candidate with the gravity line (P-289,
  P-492).

### P-493 — L3, the sign of space's curvature as a sealed look (register line 641; QUEUED)
- **Idea:** identifying open-FLRW spatial slices with a GM3 state (finite volume, a cusp) fixes k = −1. That is a sign
  prediction, testable only as a sealed, counted look.
- **Status on the record:** untouched (harvest row 1483; no rule sealed). The sign is not specific to m004: any
  hyperbolic 3-manifold gives it. The identification is CHOSEN.
- **Potential:** LOW — not one of the 19, a one-bit sign from an unearned identification. It would spend a look
  (P-445).
- **First computation:** write the sealed rule (the open-FLRW family, not the Milne cone; the cosmic-topology
  constraints on a cusped finite-volume space; the look's count). Hours. Needs a seal; no data read before it.
- **Proposed disposition:** STILL A LEAD (low).

### P-494 — A CM sighting, disclosed (register line 642; QUEUED)
- **Idea:** two CM points (τ = 3i and (1 + 7√3 i)/4) lie inside the fitted strip. By density such sightings are
  expected, so this is not evidence. The row is a disclosure owed to THE RIGID WORLD's null and its Disclosed section.
- **Status on the record:** the disclosure did not reach the sealed card. B1825's §7 Disclosed
  (frontier/B1825_step_b_the_nine_from_one_address/PREREGISTRATION.md:256–270) has no CM sighting, and the revised
  Step B dropped the CM arm. That drop is debt P-527 (register line 675, ranked #61): "restore a CM read-out on the
  card, or re-dispose P-425, P-449 and P-494 with the reason".
- **Potential:** LOW in itself. It matters as a disclosure if any later card (P-585's level 2, P-574's forced scale)
  fixes τ by a CM point.
- **First computation:** none; P-527 re-disposes it.
- **Proposed disposition:** SUPERSEDED by P-527 (a DEBT) — keep open until P-527 rules. Any card that uses a CM τ must
  carry this row in its Disclosed section.

### P-523 — The vacuity calibration and the controls (register line 671; QUEUED)
- **Idea:** before Step B's seal, show on the real census that every criterion can fail given support. Run planted
  worlds off the grid, the CKM leg's size on unrelated CKMs, E20's negative controls, the DR slice reproducing B1726,
  the c-choosing null's calibration, area against WP, and range sensitivity.
- **Status on the record:** STALE — paid in B1825's preregistration before the seal (fa25925fc), at
  frontier/B1825_step_b_the_nine_from_one_address/PREREGISTRATION.md:
  - :154–158 the vacuity calibration, "NOT VOID";
  - :159–165 the Markov check;
  - :166–179 the pass side on the box, planted worlds at χ² = 0 and with noise;
  - :180–185 the leg's size: unrelated CKMs and anarchy;
  - :186–189 the DR slice reproducing B1726, done;
  - :118–120 the certification's planted gate (0.21% missed).
  Disclosed as not done: FN-texture populations (:181). Listed as post-run, never grading: the box ×½/×2, WP for τ and
  P-538's mixture (:104). The row was never flipped.
- **Potential:** LOW now. The undone controls (FN populations, permuted frames) carry forward to P-585's level-2 card.
- **First computation:** none for B1825.
- **Proposed disposition:** ANSWERED. Close DONE → B1825 PREREGISTRATION.md §4 (lines 95–190). Name the unpaid
  controls in P-585's card.

### P-526 — The web seat's second code as Step B's third opinion (register line 674; QUEUED)
- **Idea:** an independent calculator from the web seat for the whole decisive conjunction, plus the seat's read of the
  card before the seal.
- **Status on the record:** lapsed. B1825 sealed (fa25925fc) and ran without it. No web-seat harvest row after 1504
  delivers a second code (rows 1505–1516 checked). The verification it was meant to provide was covered two other ways:
  B1825's post-run referee, "an independent referee with its own code" (FINDINGS.md:15–20: a brute-force scan of all
  50 612 352 node rows reproduces the minimum), and the web seat's own post-run review of B1825 (harvest row 1515, S298,
  which regraded it NOT FOUND).
- **Potential:** LOW.
- **First computation:** none. If an independent reproduction outside main's agents is wanted under "main is the final
  verifier", a re-request of the census scan from the seat.
- **Proposed disposition:** SUPERSEDED (lapsed at the seal; covered by B1825 FINDINGS.md:15–20 and harvest row
  1515). Close DONE/DECLINED with those pointers.

### P-531 — Which typing fixes the generations' metric (register line 679; QUEUED)
- **Idea:** derive the physical typing of the generation index. Three one-dimensional typings force H = I, and the
  frame's diagonal SU(2) leaves a 2-dimensional family. A derived typing would remove H = I as a CHOSEN input.
- **Status on the record:** open, its last note current. The web seat's design study (harvest row 1509), verified with
  corrections by main (S274), recorded in the row. The moves act on the generation index as the cube's rotation group.
  With W10's lifts and a flat H kept by L and R, H = I is FORCED on odd-order lines and the zero line. Lines of order 2,
  6 and 10 keep 2 real dimensions, and lines of order 4, 8 and 12 keep 3. No typing is derived (B1822 FINDINGS.md:73,
  96). B1825's S298 note adds H = I to B1825's scope (FINDINGS.md:114).
- **Potential:** MEDIUM — removes or exposes an input. Notably the six's order-10 lines keep a 2-dimensional H, so the
  candidate family (P-585) has an unforced metric on exactly its own lines. That must be declared or charged on its
  level-2 card (P-576).
- **First computation:** Shapiro's lemma on W10's space for the cover typing (a derivation, days). Before that,
  data-free: how far the six's spectra move across the 2-dimensional H family on the (2/5, odd/10) lines (hours).
- **Proposed disposition:** STILL A LEAD. Flag it to P-585/P-576: the candidate's H is not forced on its lines.

### P-536 — Step A's supersymmetric completion (register line 684; QUEUED)
- **Idea:** B1823's potential is a softly broken supersymmetric supertrace, and a lone Y = −½ Higgs triplet is
  anomalous. An H_u triplet is then required, with its own direction, tan β and phase, and using the vacuum for FR-FIB
  needs H_u ≡ H_d, UNEARNED.
- **Status on the record:** registered by B1823's referee (B1823 FINDINGS.md:227–238, :281). Conditional ("only if a
  construction like B1823's is revived"), and B1823 is NEGATIVE as a compression. Nearby, not the same: B1742 (two
  Higgs as different forms within FR-FIB, a READING) and FRAMING_LEDGER.md:66 (the frame's twisted residue quaternion
  is even, H_u = H_d).
- **Potential:** LOW while B1823 stays dead. It is the only route on record to a Higgs quartic (P-459) and to
  independent up/down Higgs directions, which the CKM wall (the Higgs construction, B1827) would need.
- **First computation:** only on revival: H_u's couplings and the modular weight of H_u L̄ E. A day, data-free.
- **Proposed disposition:** STILL A LEAD (conditional; cluster with P-459 and the Higgs-construction rows of B1827).

## Chunk-5 tallies
- STILL A LEAD: 14 — P-459, P-460, P-461, P-463, P-466, P-475, P-477, P-478, P-479, P-487, P-491, P-493, P-531, P-536
  (P-476 becomes a 15th if its volume check fails).
- ANSWERED (close DONE): 4 — P-462, P-465, P-468, P-523.
- SUPERSEDED: 4 — P-474 (→ P-555), P-485 (→ P-487), P-494 (→ P-527, a debt), P-526 (lapsed; B1825's own-code
  referee and harvest row 1515).
- SHOULD BE A DEBT: 1 — P-476 (after a minutes-long SnapPy check): B1722 W2 / LAW_MAP:319 / THE_WEAVE.md:854.

### P-537 — What fixes the normalisation of modular forms used as couplings (register line 685; QUEUED; no L)
- **Idea:** A "tie" between couplings built from different modular forms means something only once each form's
  normalisation is fixed. The convention is continuous data (3n − 2 ratios for n copies). If the object forced a canonical
  normalisation, B1823's heavy-sector vacuum could fix the Higgs direction without free numbers.
- **Status on the record:** untouched since registration. The source is B1823 FINDINGS.md:270–273 (§7: "a canonical
  normalisation the object forces … would have to beat the light-copy regime", P-537) and the referee's B2 at :280. A sweep
  (`canonical normali[sz]ation|Petersson norm|Kähler ambiguity`) finds no arc after B1823. Related: B1822 (H = I CHOSEN,
  the matter metric not forced; FRAMING_LEDGER.md:40, FL-11) and the open debt P-025 (non-minimal Kähler; debts list #57).
- **Potential:** LOW–MEDIUM. A forced normalisation would revive Step A (the Higgs direction from the interaction), which
  bears on the Higgs construction that blocks the CKM. But the two canonical conventions already computed (cusp, Petersson)
  put every n = 2–5 in the light-copy regime (the row), so the known evidence runs against it.
- **First computation:** decide whether the zero-free family's N(F_a) = iη⁹ (the row's one forced normalisation, which
  covers the triplets only) extends to the heavy sector's other forms. Then rerun B1823's n = 2–5 vacua under it. Data-free;
  about one day.
- **Proposed disposition:** STILL A LEAD. Merge candidate with P-025 [DEBT] (the same Kähler/normalisation ambiguity; one
  answer serves both).

### P-538 — The price of a principled line on Step B's card (register line 686; QUEUED; no L)
- **Idea:** If a "principle" picks a line (closure, move-invariance, the one-loop potential, W63's tie), that principle is
  itself a choice and must be priced. A zero-line world carries the line's 8.06 bits unless some principle is FORCED.
- **Status on the record:** ANSWERED for its purpose, which was fixing the line price on the card before the seal. Main's
  S276 ruling (in the row) went into B1825's card: PREREGISTRATION.md:108–113 ("§ 3. The line's price (P-538, main's
  ruling)": uniform over the 266 lines at 8.06 bits, the null sharing the code; read-out: the principled-line mixture
  code). B1825 ran sealed (fa25925fc). The one remaining item, the mixture-code read-out, is listed again in P-556 (B1825
  PREREGISTRATION.md:104) and has not been computed.
- **Potential:** LOW. The card it served has run; the read-out is never grading.
- **First computation:** none for this row. The mixture code is part of P-556's batch.
- **Proposed disposition:** ANSWERED. Close DONE with pointer B1825 PREREGISTRATION.md:108–113; its read-out is carried by
  P-556.

### P-543 — Two declared directions structurally dead menu-wide (register line 691; QUEUED; no L)
- **Idea:** On the line (2/5, 1/10), R and t = −5/288 give m1/m3 and J at roundoff (rank-2 coupling; real CKM). If that holds
  menu-wide, two of the twelve directions can never produce a CP-violating world with a massive first generation.
- **Status on the record:** ANSWERED. The census_structure.py count was run menu-wide before the seal and stated in B1825's
  card, PREREGISTRATION.md:190–195: "R and t = −5/288 are structurally dead for our world — every row of both has m1/m3 at
  the floor in all three sectors and J at the floor … the address code still charges them, and the null shares it." The
  row's "where" (the count before the seal) is met; the row was never flipped.
- **Potential:** LOW. It is a priced structural fact, and the menu is already twelve (B1824).
- **First computation:** none.
- **Proposed disposition:** ANSWERED. Close DONE with pointer B1825 PREREGISTRATION.md:190–195 (P-543 named there).

### P-554 — The six do not compress, even at a frame address (register line 702; QUEUED; no L)
- **Idea:** At B1741's box C_six is negative in every section. The address's bits, τ's mixture and the misfit outweigh the
  six's raw code, so K over the ten can pass only through the four's predictive bits, and K and the CKM leg are nearly one
  test.
- **Status on the record:** ANSWERED for B1825. Both of the row's items were done: the card states it (PREREGISTRATION.md:176–178)
  and the run confirms it (FINDINGS.md:59–60: C_six = −3.08, "as the pass side predicted, P-554"). The third item, "a later
  design prices the address against what the six can carry", became FRAMING_LEDGER FL-13 (docs/FRAMING_LEDGER.md:47, which
  cites P-554) and the recognition items P-570/P-574/P-575.
- **Potential:** LOW as a separate row. The lesson is real, but it is carried elsewhere.
- **First computation:** none for this row.
- **Proposed disposition:** ANSWERED. Close DONE with pointers B1825 PREREGISTRATION.md:176–178 and FINDINGS.md:59–60; the
  design lesson is carried by P-574/P-575 (FL-13, FL-21, FL-22).

### P-555 — The masses and the mixing at different addresses: the two-locus hatch (register line 703; QUEUED; no L)
- **Idea:** B1825 found the six reachable alone and the four reachable alone, never at one rigid address. The hatch reads
  the CKM as the relative rotation of the up and down diagonalisations at two loci (P-415's towers meeting), with the second
  locus fixed by a 0-bit rule, never free.
- **Status on the record:** OPEN, with a design note and a budget. The note is
  frontier/B1827_the_framing_ledger/verification/scans/DESIGN_NOTE.md, with a dated S298 correction at :76. Its § 1 budget:
  the four carry at most 19.08 bits, and a free second address is dead (C_ten ≤ 0.36). The note's mirror-rule "CLOSED for
  the CKM" was corrected at S298 to NOT FOUND to raise the rate, not closed: three witnesses reverse the corner order with
  the six kept (FRAMING_LEDGER.md:57; B1827 FINDINGS.md:135; the row's S298 note). No two-locus frame has been defined or
  computed beyond the mirror rule. The requirement it found is that the down sector's Higgs sits farther from the null cone
  than the up's by about the hierarchy ratio (DESIGN_NOTE § 3). FL-07 (FRAMING_LEDGER.md:36) and § E item 4 (:80) carry it.
- **Potential:** HIGH. It is the only named route around the wall that blocks the quark mixing, B1825's "never together",
  and the towers picture (P-415) motivates it. Against it: the budget is tight (3.63 bits for a rule plus the four's misfit),
  and the S289–S290 scans used functions of the graded four as success criteria, so the four are not untouched for any card
  these scans inform (row S298 note; P-566 row).
- **First computation:** write out the candidate 0-bit rules that change r = |h·h|/|h|² between the sectors (the mirror
  keeps r, so it cannot be one). Count them against the 12-rule ceiling. Test each rule data-free on the frame's points for
  corner order alone; |V_ud| is one of the graded four, so it is disclosed as seen. Cost: a day for the note, a day for the
  scan; a seal before any value look.
- **Proposed disposition:** STILL A LEAD. This is the umbrella row for a cluster with P-566, P-583 and P-591 (RI-1); merge
  their bookkeeping under one CKM-corners lead with sub-items.

### P-556 — B1825's post-run read-outs not yet computed (register line 704; QUEUED; no L)
- **Idea:** The card listed labelled read-outs that never grade: the box at ×½ and ×2; B1814's arm N for the CKM; P-538's
  mixture code; WP for τ; B1735's χ² on the DR slice; T1 under the clocks beyond the area clock.
- **Status on the record:** mostly untouched. B1825 FINDINGS.md:46 reports only the c = 1 arm and χ²_nine, and :43 T under
  the area clock only. The list itself is at PREREGISTRATION.md:100–105. Some items touch data (B1735's χ² on the DR slice,
  per PREREGISTRATION.md:189), so each one is a look to be counted, not a free read.
- **Potential:** LOW. B1825's grade is NOT FOUND (FINDINGS.md:112), the read-outs never grade, and the box variants could
  only show how robust NOT FOUND is to the reach.
- **First computation:** the box at ×½ and ×2 on the stored census (aggregate scripts already exist), then the mixture code.
  Hours each; each one that compares with data is entered in LOOK_LEDGER.
- **Proposed disposition:** STILL A LEAD (low). It absorbs P-538's read-out.

### P-558 — FR-COV (the agy lane's 4D Higgs with a free sector scalar a₀) as a candidate frame (register line 706; QUEUED; no L)
- **Idea:** The agy lane's FR-COV adds a free complex per-sector scalar to FR-FIB's Higgs. Its "pass" of B1825's gates was
  a post-hoc fit. As a frame it could be sealed, but only once τ, the characters, the cell and a₀ are all priced.
- **Status on the record:** subsumed. B1826 FINDINGS.md:45–52 records the pass as post hoc, the targets hard-coded, and a₀
  free (more freedom than FR-FIB). The row's own S288 note: the lane's referee finds that the natural-magnitude scalar with
  no chosen phase leaves the corner inverted at B1825's address, and that taken at face value the fit could not clear K.
  The class of frames it belongs to (FR-FIB plus a singlet in the Higgs's identity channel) was then scanned data-free in
  B1827 § D (FRAMING_LEDGER.md:60–65). There a same-sign singlet does nothing and an opposite-sign singlet, which is the
  adjugate reading, balances the corners. That class is P-566's.
- **Potential:** LOW as its own row, since FR-COV is P-566's class with the singlet left free. It is worse priced than any
  rule-fixed singlet (P-555's budget leaves no room for a free a₀).
- **First computation:** none separately. Any test runs as P-566 with a₀ fixed by a rule.
- **Proposed disposition:** SUPERSEDED by P-566 (the singlet class, B1827 § D) under P-555's budget. Merge.

### P-562 — The Higgs's own hypercharge twist (register line 710; QUEUED; no L)
- **Idea:** The agy lane argued that the Higgs section should carry its 6Y = 3 twist, which would give a nonzero identity
  channel with no free number and break B1739/B1826's lock.
- **Status on the record:** ANSWERED before it was raised, as the row's own S289 correction says. B1744 (THE HIGGS'S OWN
  TWIST, P-324) computed the twisted residue quaternion (arc_verdict: "the residue quaternion at the Higgs's hypercharge
  twist is even, T0(3w) = T0(−3w) … H_u = H_d"; as a Higgs χ²_nine ≥ 493; with the scalar channel, null in 4D, det Y = 0).
  P-324 is DONE (register line 472). The consequence for the corners is answered by class: an even (same-sign) singlet does
  nothing (B1827 § D, FRAMING_LEDGER.md:60; B1827 FINDINGS.md:43, P-562's correction). The residual, the twisted Serre
  derivative in the four-channel frame, is even by the row's own note and therefore in that dead class.
- **Potential:** LOW. Both branches of the decision are known: twisted gives even, which gives no corner lift.
- **First computation:** none. If wanted, the Serre-derivative check is minutes, inside P-566.
- **Proposed disposition:** ANSWERED. Close DONE with pointers B1744 (arc_verdict), P-324 (line 472) and FRAMING_LEDGER.md:60.
  It duplicates P-324.

### P-564 — The cover framing: generations as the three sheets of m004's 3-fold cover (register line 712; QUEUED; no L)
- **Idea:** Read the three generations as the three sheets of m004's 3-fold cover. The colour centre's Z₃ Wilson line
  (B1801) would then separate quarks from leptons where the fibre's 6Y cannot.
- **Status on the record:** untouched by main. As stated it is not a frame with outputs. On the cover the symmetric commutant
  is 2-dimensional (H = aI + bJ), so H = I is not forced, and the Wilson line's torsion enters no Yukawa yet (the row).
  FRAMING_LEDGER FL-10 (:39) lists it as the alternative to "three quaternion images of one doublet". The agy lane's Theorem
  15 relay names P-564 (harvest row 1539, HARVEST_LEDGER.md:1587: every value claim unverified).
- **Potential:** MEDIUM. A frame where three is the cover's degree would bear directly on "three generations only as an
  index by selection" (B1496) and on FL-10. Against it: the cover's commutant leaves the metric free (democratic mixing
  allowed), which adds free numbers rather than removing them, and there are no outputs yet.
- **First computation:** write where the sheets enter the point coupling (B1656's Y as a 3×3 over the sheets). Then count
  the forced inputs: is H forced by the deck group, and does the Z₃ torsion enter any channel weight? Data-free; one to two
  days.
- **Proposed disposition:** STILL A LEAD.

### P-566 — The sector-odd singlet (FL-06): what in the object makes it odd (register line 714; QUEUED; no L)
- **Idea:** A singlet Higgs component at natural magnitude with opposite signs in up and down (exactly the adjugate reading
  adj S = εSᵀεᵀ) lifts the CKM's corner inversion generically, where an even one does nothing. The question is what in the
  object forces the oddness.
- **Status on the record:** OPEN. Computed so far:
  - B1827 § D (FRAMING_LEDGER.md:60–65): odd lifts, even does nothing, over a factor 16 in size.
  - S290: the SM reading (S̃ up) over-flips the corners and scrambles |V_ud|.
  - S291: adjugate = the opposite-sign family exactly (B1827 FINDINGS.md:78–80); the 45 half RETRACTED (FINDINGS.md:91–97).
  - S298: B1744 had already listed the operation among the unforced choices, and P-084 has adj N = J Nᵀ J⁻¹. The scans
    touched seen data (row note).

  Candidate answers: the SM seat's RI-1, the kernel's signed Laurent constant (P-591), and the agy lane's Theorem 15
  Result 3 (row 1539). **Post-pin:** the SM seat's W183 (origin/<v>/standard-model-derivation-0qt6ao 886dc3a3c, NOTE.md
  §W183) tested RI-1 at τ = i. The parity held on its own code, but the corner-lift cells failed there, and τ = i has no
  hierarchical point, so it is not P-566's regime. It is unharvested and not verified on main.
- **Potential:** HIGH. It is the one computed mechanism that lifts the CKM corner inversion, which is the wall behind
  B1825's "never together". If an object-forced oddness (RI-1) works in the hierarchical regime, the Higgs-construction
  block on the mixing loses its main obstacle at no free number. Against it: the corner ratio becomes balanced, not
  nature-like (FRAMING_LEDGER.md:62); the scans used the graded four as criteria; RI-1 failed its corner cells at τ = i.
- **First computation:** verify RI-1's identity a₀(up) = −a₀(down) = −a₀(lepton) on main's code (the web seat's kernels note
  § 5: K_s(u; −S) = −K_s(−u; S)). Then run the corner order alone at hierarchical frame points with the bare a₀
  (no free number). Data-free apart from the disclosed coarse facts; hours for the identity, a day for the scan.
- **Proposed disposition:** STILL A LEAD. Cluster with P-555, P-583 and P-591; P-558 and P-562 fold into it.

### P-567 — The lines as centre Wilson lines: does any Z₅ × Z₃ line give the Georgi–Jarlskog factor? (register line 715; QUEUED; no L)
- **Idea:** On order-5 lines the frame is minimal SU(5) exactly, so c = 3 is the Georgi–Jarlskog Clebsch put in by hand. The
  lines (2/5 + j/3, k/30) of orders 15 and 30 lie outside the sealed reach and might give the factor at c = 1.
- **Status on the record:** PARTLY ANSWERED, and the row is stale. The SM seat's W182 (sealed by commit order, read by main
  at S298) computed the down–lepton factor on the 90 centre lines at c = 1, at the cusp ladder and τ = i: "no centre line
  gives the Georgi–Jarlskog shape" (harvest row 1542, HARVEST_LEDGER.md:1590; LOOK_LEDGER.md:113). Main's own reading of
  the scope: "P-567 Q1 answered at the cusp ladder and τ = i only, not at the strip's Im τ ≈ 3". W182's C4 compared D with
  the data window, so it is a counted look. The strip-height half is now P-593's item 2 ("the centre lines at the strip's
  height (would be a sealed look)"). The row's where cell does not mention W182. It was not re-run on main.
- **Potential:** LOW–MEDIUM now. The answer so far is negative at two τ points. Only the strip height could still matter,
  and there it is a sealed look at D.
- **First computation:** main's re-run of W182's two-point scope (data-free part). If pursued, the strip height goes under a
  seal (P-593).
- **Proposed disposition:** ANSWERED IN PART (harvest row 1542). Close DONE with that pointer once main has re-run W182, and
  merge the strip-height remainder into P-593's item. At minimum the row must record W182.

### P-568 — Relations and rigid outputs (FL-14, FL-15) (register line 716; QUEUED; no L)
- **Idea:** The bar grades values, never relations. Count the relations the frame forces (the Jacobian co-rank of its outputs
  in its continuous data), and compute its rigid inter-sector outputs at the strip.
- **Status on the record:** first half computed post-pin by the web seat, not harvested and not verified on main:
  origin/chat1/web-seat fe2f972cd, relays/CHAT1_TO_CC_2026-11-03_THE_RELATIONS_THE_FRAME_FORCES.md (refereed twice
  read-only). On each B1825-typed branch the only continuous input is τ. The output rank is 2 on all 1 536 branches sampled
  (1 on 32 branches of orders 1–2), so the ten obey 8 relations per branch, and the relation list is explicit (B1728's law,
  the exact zeros, the half-period coincidences). Second half: deliberately not computed. The relay states that the
  strip's inter-sector Yukawa ratio is P-585's held-out target. On main the sweep `co-?rank|rigid outputs|number of
  relations` finds no arc.
- **Potential:** MEDIUM–HIGH. The relational count is the honest "how many free numbers" answer the owner's restated goal
  asks for (2026-10-08; P-418's vector), and it is data-free. The rigid-output half is the held-out target of the only
  level-2 card, so it must not be computed outside that card.
- **First computation:** main re-runs the web seat's relations_check.py (796f02e2b) and halfperiod_check.py (2b515e748)
  against main and harvests the relay. Hours; data-free.
- **Proposed disposition:** STILL A LEAD (first half: verify the relay, then DONE). The second half is SUPERSEDED by P-585
  and is to be computed only inside P-585's sealed card. Mark the conflict in the row now, so nobody computes the rigid
  ratios ahead of the card.

### P-569 — θ̄ as a constraint (FL-16) (register line 717; QUEUED; no L)
- **Idea:** Use the locus arg det(Y_u Y_d) = 0 through the strip either as a selector (fix Re τ, predict |J|) or as a
  strong-CP kill of the J ≠ 0 addresses.
- **Status on the record:** OPEN; one prior look on record (P-323; FRAMING_LEDGER FL-16 at :50; value not reproduced).
  **Post-pin:** the web seat's origin/chat1/web-seat 8ed19bbd4,
  relays/CHAT1_TO_CC_2026-11-03_THE_STRONG_ANGLE_NEEDS_A_RULE.md (data-free, refereed twice) finds the frame has no θ term.
  θ_Y is not invariant under the frame's own relabellings, so it is defined only once a counterterm rule is chosen, and the
  seat proposes dropping θ̄ from P-585's held-out targets (its referee notes the card would then be one target short). This
  is unharvested and unverified on main. B1829 REGRADE.md:45 lists θ̄ (the det-real locus, P-569) as one of P-585's
  held-out targets.
- **Potential:** MEDIUM. A forced strong-CP condition would be a genuine relation the frame could be tested on. But the
  seat's relabelling result says the frame cannot state it without a chosen rule. Using it as a selector would also spend
  one of P-585's held-out targets.
- **First computation:** main verifies the seat's closed forms for θ_Y's shifts under b → b + 1 and the T step on a line off
  the family's slope (the seat's theta_rule_check.py, 2e545afc4). Then the owner or main rules on the counterterm rule
  before any θ̄ cell. Hours; data-free.
- **Proposed disposition:** STILL A LEAD. Duplicate of P-323 (θ̄ in the mass frame); merge. Flag the conflict with P-585: θ̄
  cannot be both the selector here and a held-out target there.

### P-570 — Running and the allowance (FL-13) (register line 718; QUEUED; no L)
- **Idea:** Every card compares tree-level outputs at M_Z with no running and a flat 10% allowance. That caps the information
  a card can carry.
- **Status on the record:** not acted on as a rule. The content was split and sharpened the same day into P-574 (the scale,
  FL-21, FRAMING_LEDGER.md:113) and P-575 (the theory error, FL-22, :114). FL-13 (:47) carries S298's correction:
  within-sector running is bounded by B1718, and the inter-sector running is what is unstated. The debt half for the past
  negatives is P-590 (DEBT #33).
- **Potential:** MEDIUM, as part of P-574/P-575.
- **First computation:** as P-574.
- **Proposed disposition:** SUPERSEDED by P-574 + P-575 (same subject, later and sharper). Merge.

### P-572 — The nine with no frame (FL-05) (register line 720; QUEUED; no L)
- **Idea:** The gauge couplings, the Higgs sector and the scale have no action, normalisation or dynamics on record, and
  need new structure rather than extraction. The S291 recount: six have no frame (g₁, g₂, g₃, m_H, v, y_t); three are frame
  outputs never examined.
- **Status on the record:** OPEN. FL-05 (FRAMING_LEDGER.md:29) states the recount. The scoreboard statement asked for is
  not made in a front document; that is the open debt P-579 (#19). The SM seat's retrieval sweep says FL-05's "no action on
  record" overstates (B1684, B1791, B1823), which is in P-591 and unread by main. The gauge-coupling route on record is
  P-396 (the relative gauge thresholds).
- **Potential:** HIGH in prize (six of 19 have no frame at all, a third of the target), LOW in tractability (the row is a gap
  statement, not a computation). Anything here would change the programme's reach more than any flavour result.
- **First computation:** read B1684, B1791 and B1823 against FL-05 (is any of them an action that outputs a gauge coupling
  or v?), and write the one-line scoreboard statement under P-579. Hours.
- **Proposed disposition:** STILL A LEAD. Merge candidate with P-396 (the gauge couplings' only route) and P-591's FL-05 item;
  the scoreboard half belongs to P-579.

### P-574 — The scale and the running (FL-21, R1) (register line 722; QUEUED; no L)
- **Idea:** A theory exact at the unification scale fails K when compared at M_Z: R1 shows it pays more bits than B1825's
  address leaves. So every future card must declare its scale (or a priced menu) and run its outputs at one loop at least.
- **Status on the record:** not adopted. THE_BAR.md and THE_FINAL_ACTS_BAR_2026-10-29.md carry no scale-declaration rule
  (grep for scale, running and P-574 in THE_BAR.md: none). FRAMING_LEDGER § E item 0 (:70) puts it first. B1829 REGRADE.md
  (:50–51) makes it a precondition of P-585's card. The tools are calibrated (P-502 DONE: PyR@TE 3, register line 650). The
  backward half, past negatives at M_Z, is P-590 (DEBT #33).
- **Potential:** HIGH for recognition. Without it the tests cannot recognise a correct GUT-scale answer (B1827 § G, R1), and
  the only level-2 card (P-585) depends on it.
- **First computation:** write the bar amendment (declared scale or priced menu; one-loop running with the pinned PyR@TE),
  then compute R1's table for the card's targets data-only. A day; data-free.
- **Proposed disposition:** STILL A LEAD, but better typed [PROCESS] (a bar amendment owed before the next card). Merge with
  P-570, P-575, P-576, P-578 and P-582 into one "recognition amendment" row; the debt half stays P-590.

### P-575 — A declared theory error (FL-22) (register line 723; QUEUED; no L)
- **Idea:** The flat 10% allowance discards about 30 bits of measured information against a 12.37-bit gate, and K's power for
  a correct frame one σ away is 1 in 10. A card should name the frame's theory error and pay for it.
- **Status on the record:** not adopted (no bar text). FRAMING_LEDGER.md:114 (FL-22); B1829 REGRADE.md:51; B1825
  PREREGISTRATION.md:176–178 (the calibration).
- **Potential:** MEDIUM–HIGH, the same recognition argument as P-574.
- **First computation:** define the theory error for FR-FIB (tree plus one loop plus thresholds) and recompute B1825's
  calibration at it. A day; data-free.
- **Proposed disposition:** STILL A LEAD, to retype [PROCESS]. Merge with P-574.

### P-576 — The frame's own length (FL-23) (register line 724; QUEUED; no L)
- **Idea:** K never charges the frame's description. FR-FIB's H-cov branch carries about 15 bits searched on the data, and a
  frame planted to contain our world passes 7 in 10.
- **Status on the record:** not adopted. THE_FINAL_ACTS_BAR_2026-10-29.md:193 (the H-cov branch's searched bits);
  FRAMING_LEDGER.md:115; B1829 REGRADE.md:51 (precondition of P-585).
- **Potential:** MEDIUM–HIGH. Without it a fitted frame can pass, which is the false-positive side of recognition.
- **First computation:** K1 (THE_FINAL_ACTS_BAR_2026-10-29.md:323–332) lists the framework's length but lets it cancel against the null; replace the cancellation with a charge for the bits searched on the data (FR-FIB's H-cov figure, :193) and recompute B1825's planted-frame calibration under it. Hours; data-free.
- **Proposed disposition:** STILL A LEAD, to retype [PROCESS]. Merge with P-574.

### P-578 — Object and rival nulls (FL-25) (register line 726; QUEUED; no L)
- **Idea:** The decisive nulls randomise the world, never the object or the frame. Run the same frame on ±LLLR, m003 and
  other threads, and on one rival population (flavon charges or modular flavour), before the next sealed value look.
- **Status on the record:** untouched. The sweep `rival population|comparable.object null|object null|flavon.charge`
  (full text) finds only B790, which is unrelated. FRAMING_LEDGER.md:117 (FL-25); B1825 PREREGISTRATION.md:181 (FN-texture
  populations not computed).
- **Potential:** MEDIUM–HIGH. It decides whether anything the frame reaches is object-specific, which is exactly what
  THE SIX ON THE STRIP needs before a level-2 pass could mean "the object". If m003 or ±LLLR reach the six as easily, the
  candidate is the frame's, not m004's.
- **First computation:** FR-FIB's output distribution (the six's reach, no data) on the m003 thread versus m004's,
  data-free; then a sealed comparison. Days (census-scale); the first half is data-free.
- **Proposed disposition:** STILL A LEAD (a prerequisite for P-585; merge into the recognition amendment as its null clause).

### P-582 — Existence before sealed looks (register line 730; QUEUED; no L)
- **Idea:** B1713 and B1720 had already shown masses and mixing apart before B1825 spent a look on the same obstruction. An
  unsealed existence scan (free τ, directions, readings, the 4D Higgs) should gate any sealed value look.
- **Status on the record:** not adopted. FRAMING_LEDGER.md:175 lists it among § G's owed items. No existence-scan rule is in
  THE_BAR.
- **Potential:** MEDIUM. It saves looks, since each look raises m and the joint bar. But an existence scan that reaches our
  numbers is itself a look at data, so it must be counted under GENESIS v1.61's ledger; that is a tension to be ruled.
- **First computation:** a rule text plus the LOOK_LEDGER accounting for unsealed existence scans; an owner or main ruling.
  Hours.
- **Proposed disposition:** STILL A LEAD, to retype [PROCESS]. Merge with P-574.

### P-583 — The leptons read the adjugate (register line 731; QUEUED; no L)
- **Idea:** On all 24 order-5 lines Y_e(S) = −λ Y_d(adj S)ᵀ. So the reading that balances the CKM's corners (down reads
  adj S) is, there, the frame's own down–lepton relation. Test the corner order and |V_ud| on order-5 lines under (up S,
  down adj S), and what the same choice fixes for the leptons.
- **Status on the record:** the identity is PROVED/COMPUTED (LAW_MAP.md:351; B1827 recheck lepton_reads_adjugate_out.txt);
  M_e = λM_dᵀ is B1728's (credited at S294). The row's test (corners and |V_ud| restricted to order-5 lines under the
  adjugate reading) is not computed. B1827's singlet scans sample random lines of the whole menu (singlet_higgs_scan2.py:32–38),
  and RECHECK.md has no corner cell on order-5 lines.
- **Potential:** MEDIUM. If it works, one structure ties the CKM corners to the down–lepton relation, a unification of two
  walls. Against it: the order-5 lines cannot host our six, because D there is the Georgi–Jarlskog value, excluded at any
  scale (P-590's row; P-355). The result would be a mechanism, not a candidate address.
- **First computation:** the corner order (and, disclosed, |V_ud|) on the 24 order-5 lines under (up S, down adj S) with the
  singlet at natural magnitude; the existing scans already contain the code. Hours; data-free apart from the disclosed
  coarse facts.
- **Proposed disposition:** STILL A LEAD (in the P-555/P-566 cluster).

### P-585 — The candidate family's confirmation: THE SIX ON THE STRIP at level 2 (register line 733; QUEUED; no L)
- **Idea:** Freeze the level-1 candidate family (FR-FIB on the order-10 lines (2/5, b), Im τ ≈ 3, c = 3; B1749, B1753) on a
  sealed card and test held-out quantities it never used. Two passes would make the first PREDICTED values under GENESIS
  v1.60/v1.61.
- **Status on the record:** OPEN by design. No card has been drafted. Weakened three times since it was written:
  - S295: in about 3σ tension with its own in-sample D (P-355, debts #1).
  - S297: it is the small-cut end's, and at the exact norms the six fail (P-421, debts #4; B1829 LOOK_LEDGER).
  - S298: the agy audit lane computed the two held-out targets unsealed and set one against data, which counts as a prior
    look in m_V (LOOK_LEDGER.md:120; harvest row 1539). Main has not read the values.

  Held-out list and cleanliness are in B1829 REGRADE.md:41–52: one target is not clean, and its reason is disclosed there,
  not reproduced here. **Post-pin:** the web seat proposes dropping θ̄ from the targets (8ed19bbd4, see P-569), which would
  leave one clean target, while GENESIS v1.60 needs two. The card's preconditions P-574/P-575/P-576 are not adopted.
- **Potential:** HIGH. It is the only route on the record by which the scoreboard can move off 0 of 19 (GENESIS v1.60/v1.61).
  Known against it: about 0.5 false candidates expected over 53 looks (B1829); the frame fails the mixing (B1825), so at most
  a scoped mass dictionary is at stake; D's tension; the exact-norm failure; prior looks at both targets; possibly too few
  clean targets.
- **First computation:** before any card, settle whether two clean held-out targets exist: rule on θ̄ (P-569 / the seat's
  counterterm relay) and name a second clean target if needed. Then adopt P-574–P-576 and freeze the card on the family's
  best sealed card with the small-cut end as a counted input. Days; it needs a seal, and no target is computed before the
  freeze.
- **Proposed disposition:** STILL A LEAD (the decisive one). The debts it creates (P-355, P-384, P-421, P-586) are already
  ranked #1–#4. Absorb P-568's second half into it.

### P-591 — The retrieval sweep's candidates and asks; RI-1, the signed Laurent constant as the sector-odd singlet (register line 739; QUEUED; no L)
- **Idea:** The kernel's signed Laurent constant a₀ is odd between up and down (a₀(up) = −a₀(down) = −a₀(lepton)). B1656
  uses only |a₀|², so the sign is unused, and it may be exactly the sector-odd singlet P-566 needs with no free number. Three
  seats point at it independently. The row also carries RI-2–RI-8 and three asks (UNEARNED identification rows, a
  WORKING_RULES rule, FL-05's overstatement).
- **Status on the record:** OPEN on main. Harvest row 1543 (HARVEST_LEDGER.md:1591) records the candidates and asks; no RI
  row is in IDENTIFICATION_LEDGER (grep RI-: none). Row 1539 notes the agy Theorem 15 Result 3's independent support.
  **Post-pin:** the SM seat's W183 (rule 2a1653df5 → script 1c2ce95b7 → output 874fdedfe → record 886dc3a3c, on
  origin/<v>/standard-model-derivation-0qt6ao) held the parity by two routes on its own code. At τ = i the corner-lift
  cells O4 and O6 failed, no frame point there is hierarchical, and its D cell was a look (O8). RI-1 is "TESTED at τ = i,
  not earned". This is unharvested and unverified on main.
- **Potential:** HIGH for RI-1, as the best-placed candidate for the object-forced oddness P-566 asks for at zero free
  numbers. LOW to MEDIUM for RI-2–RI-8 and the asks, which are mostly process.
- **First computation:** verify the sign identity on main's own kernel code (the web seat's kernels note § 5), data-free, in
  hours. Then the P-566 scan at hierarchical points with the bare a₀. Harvest W183 with its look counted.
- **Proposed disposition:** STILL A LEAD. Split: RI-1 merges into P-566 (it is P-566's candidate answer); the asks
  (identification rows, the rule, FL-05) retype [PROCESS]; RI-2–RI-8 stay an index.

### P-593 — The harvest's new questions (S298; rows 1517–1543) (register line 741; QUEUED; no L)
- **Idea:** A bundle of about eleven data-free questions from the S298 harvest:
  - derive W181's post-hoc cosine-ratio law for the cusp limits;
  - the centre lines at the strip's height (a sealed look);
  - the lemma "only Im((q_L − q_R)w) reaches the cusp exponents";
  - the agy Theorem 18C on the 40 half-lift points;
  - an invariant separating the agy lane's three 2O classes;
  - 15:5:3 versus W178's exponents;
  - B1141's m004 fibre-spin forcing and B1707's q = 1 as the odd spin;
  - the Wilson character χ as the line address w;
  - Theorem 10's orbit as the Fox 5-colouring;
  - Gurevich–Hadani as prior art;
  - the owner's three-lens proposal not on main.
- **Status on the record:** untouched by main since registration. Harvest rows 1523 (HARVEST_LEDGER.md:1571, the three-lens
  intake), 1534 (:1582), 1539 (:1587) and 1541 (:1589) are the sources. The "sha 03ed8cd9" is not a commit in this clone
  (`git log 03ed8cd9`: unknown revision), so it is probably a file hash; the proposal is at the physical lane's b77117f6b
  (row 1523). Post-pin, the web seat's relations relay (fe2f972cd) computes the half-period coincidences at two τ, "not
  derived", which bears on the Theorem 18C item and on P-355.
- **Potential:** MEDIUM overall. The Theorem 18C item would turn S297's computed half-lift statement into a proof bearing on
  debt P-355. The cosine-ratio law and the cusp-exponent lemma would unify W179–W182. The spin and prior-art items are LOW.
- **First computation:** the Theorem 18C check on main (it supports P-355, a debt), then the cusp-exponent lemma. Hours each;
  data-free.
- **Proposed disposition:** STILL A LEAD, but split. The Theorem 18C item should be moved under P-355 (a DEBT); the strip-height
  centre lines merge with P-567's remainder; the rest stay an index.

---

## Chunk summary

- Counts (24 rows): STILL A LEAD 16 (P-537, P-555, P-556, P-564, P-566, P-569, P-572, P-574, P-575, P-576, P-578, P-582,
  P-583, P-585, P-591, P-593 — of which P-574/P-575/P-576/P-582 better typed PROCESS); ANSWERED 4 (P-538, P-543, P-554,
  P-562); ANSWERED IN PART 1 (P-567); SUPERSEDED 2 (P-558 → P-566; P-570 → P-574 + P-575); P-568 split (half answered
  post-pin by a seat, half superseded by P-585). (P-593's 18C item belongs under the debt P-355.)
- Post-pin seat work bearing on this chunk, unharvested: chat1 fe2f972cd (P-568), chat1 8ed19bbd4 (P-569, P-585), sm
  W183 886dc3a3c (P-566, P-591), agy d9a04edd7 (P-355, P-384 — outside this chunk).
