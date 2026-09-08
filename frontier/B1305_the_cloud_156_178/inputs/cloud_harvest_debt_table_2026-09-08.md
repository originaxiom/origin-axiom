# HARVEST-DEBT TABLE — the cloud seat's `outside_bench` memos 1–178 against main

## 0. Method note and three corrections to the brief

**Scope correction (memos 1–29).** `outside_bench/INDEX.md`'s table starts at memo 30. Memos 1–29 belong to a *different* branch, `paper-hostile-review-alero0` of `originaxiom/golden_gate`, per the INDEX's own provenance note. That work is recorded there as already reconciled into main as **B1144** (audit) and **B1145** (memo 29, SP‑2, TWO‑BENCH). It is out of reach from the outside-bench branch itself and out of scope for a sweep of *this* branch. The exhaustive table below therefore covers the **149 memos (30–178) that actually exist in this branch's INDEX** — a complete set, no gaps, no duplicates (verified `seq 30 178` diff-clean against the table).

**Arc-number correction.** The brief's premise — "harvest arcs on main are B1235–B1241, B1247, B1293, B1294" — is **not this seat**. I grepped main for those exact IDs and traced every one: B1235–B1241 harvest **`fab5cloud`** (a *different* branch, `physics-seat-evaluation-8dkbrl`) plus **codex** and **fc**; B1293/B1294 are main's own re-runs of "every seat number." None touch `outside_bench`. Likewise `docs/CLOUD_ALIAS_TABLE.md`'s `qB…` numbers alias a *third*, unrelated branch (`qor5up`, the "cloud consolidation seat," forked at B1024) — also not this seat. **There are at least three differently-named "cloud" seats in this repo's history; only `origin/outside-bench` is the one this report is about.** The real, load-bearing evidence trail for *this* seat is `docs/RELAY_LEDGER.md`'s `outside_bench/…(cloud→cc, origin/outside-bench <sha>)` rows plus literal `memo N` citations across `CHANGELOG.md`, `PROGRESS_LOG.md`, `docs/`, and `frontier/*/FINDINGS.md` — that is what this table is built from (`git grep -w -E "memo (N|N|…)" main`, run in bands, plus full reads of every `RELAY_LEDGER.md` row naming `outside_bench`).

**Mark-detection caveat.** An automated keyword pass over the INDEX rows for RETRACTED/SUPERSEDED/NOT ADOPTED/etc. throws false positives — a memo often *narrates* another memo's or another era's retraction. I hand-verified every case material to a step‑3 exclusion; two are genuine self-retractions (173, 176 — both *partial*, sections only), two are genuine self-non-adoptions (164, 166), the rest (132, 135, 154, 158, 159, 167 flagged by the scan) are false positives referring to other subjects.

---

## 1. The compact table — memos 30–178

Legend: **H**=HARVESTED (main independently reproduced/verified/adopted it), **C**=CITED (main names it, does not re-run it), **A**=ABSENT (zero mention anywhere in main's tracked files).

| # | file | own mark | status | main pointer |
|---|---|---|---|---|
| 30 | FOUR_DISTINGUISHED_PARITIES | — | H | B1147 (4th-bench verified, codex R003 byte-identical) |
| 31 | CUSP_REFLECTION | — | H | B1147 |
| 32 | JORDAN_BEAT | — | H | B1147 ("no mass term" theorem) |
| 33 | THE_64_GLUED | — | H | B1147 |
| 34 | PARITY_LEMMA | — | H | B1147; also cross-checked as B1146 (SEAM-B) |
| 35 | YUKAWA_COUNT | — | H | B1147 |
| 36 | PIN_ABOVE_THE_FORK | — | H | B1147 |
| 37 | BLANKET_BLIND_SPOT | — | H | B1147 |
| 38 | WEYL_DERIVED | — | H | B1147 |
| 39 | HABIRO_TOWER | — | H | B1147 |
| 40 | OHTSUKI_BRIDGE | — | H | B1147 |
| 41 | KAPPA_MEETS_BEAT | — | H | B1148 |
| 42 | THE_FREEDOM_LEDGER | — | H | B1148 (synthesis, named explicitly in the bank) |
| 43 | FIXED_POINT_TWIN | — | H | B1148 |
| 44 | ONE_BIT | REFUTED (internal, re: a reading) | H | B1148 |
| 45 | ONLY_SPINOR | — | H | B1148; representation-side of B1146 |
| 46 | THE_CARRIER | — | H | B1148 (Ψ=C²⊗27) |
| 47 | YUKAWA_ON_CARRIER | — | H | B1148 |
| 48 | UNIQUENESS_CHAIN | — | H | B1148 |
| 49 | TRACE_THREE | — | H | B1149 |
| 50 | ODD_STEPS_ARE_MATTER | — | H | B1149 |
| 51 | LONGITUDE_IS_THE_LOCK | — | H | B1149 |
| 52 | YUKAWA_READS_THE_CLOCK | — | H | B1150 |
| 53 | FAMILY_YUKAWA | REFUTED (internal, re: E8-not-object-paid caveat) | H | B1150 |
| 54 | PERIPHERAL_IDENTITY | — | H | B1153 |
| 55 | SUPERPOSITION_SPEAKS | — | H | B1153 |
| 56 | DARK_LEDGER | — | **C** | B1158 (corroborates dark-ledger typing at anomaly level only) |
| 57 | FAMILY_ESCALATOR | — | **A** | — |
| 58 | ANOMALY_PAYMENT | — | H | B1158 (reproduced, QUARANTINED scope) |
| 59 | CENTER_IS_THE_LOCK | — | **A** | — |
| 60 | ONE_QUADRATIC_TWO_ENDS | — | **A** | — |
| 61 | VEV_LEDGER | — | **A** | — |
| 62 | FAMILY_PORTAL_FINE | — | **C** | B1158 row (CITED-ONLY, "not re-run") |
| 63 | EXCHANGE_LEDGER | — | **C** | B1158 row (CITED-ONLY) |
| 64 | MIRROR_DEEPEST | — | **C** | B1158 row (CITED-ONLY) |
| 65 | PERIPHERAL_DIMS | — | **A** | (WAVE-2 cell A4; not even cited) |
| 66 | MINIMAL_FACTOR | — | **C** | B1158 row (CITED-ONLY) |
| 67 | CENSUS_DIMENSIONS | — | **C** | B1158 row (CITED-ONLY) |
| 68 | GAUDIN_CLOSE | — | H | B1158 (reproduced, SCOPED) |
| 69 | HABIRO_AT_ZETA | — | H | B1158 (mechanism SOLVED; codex R016 sharpened the fence) |
| 70 | HYPERCHARGE_FALLS_OUT | — | H | **B1160** |
| 71 | SUSY_NO_GO | — | **C** | B1162 (cloud stack, cited not re-run) |
| 72 | UNIQUE_CHAIN | — | **C** | B1162 (cloud stack, cited not re-run) |
| 73 | RESIDUAL_CHARACTERIZED | — | H | B1158/B1162 (confirms B1158 scoping) |
| 74 | FAMILY_CENSUS | — | H | B1162 (= B1161 generation-NULL) |
| 75 | ALIGNMENT_AUDIT | — | H | B1162 (= B1160/B1161 discriminant) |
| 76 | Z2_CENSUS | — | **A** | — |
| 77 | PSI_SURVIVAL | — | **A** | — |
| 78 | GRAVITY_LOAD_BEARING | — | H | B1165 addendum + B1170 ("in-derivation STANDS") |
| 79 | ONE_BIT_WITNESS | — | **A** | — |
| 80 | THE_TEXTURE | — | H | B1171/B1185/B1206/B1208 (byte-identical, repeatedly cited) |
| 81 | GEODESIC_TONGUE | — | **C** | B1168 (FENCED, relayed to cc3, unanswered at cc3's retirement) |
| 82 | FAMILY_RANK | — | H | B1171/B1185 |
| 83 | COSMOGONY_LEDGER | — | **A** | — |
| 84 | ATOM_SHAPE | — | **A** | — |
| 85 | SCRIPT_CHAIN | — | **A** | — |
| 86 | ORDER_DIRECTION | — | **A** | — |
| 87 | DARK_LAW_PROVED | — | **A** | — |
| 88 | DARK_TOWER | — | **A** | — |
| 89 | DARK_TOWER_COUNTED | — | **A** | — |
| 90 | TWO_PULSES | — | **A** | — |
| 91 | OWN_METER | — | **A** | — |
| 92 | TWIST_PARITY | — | **C** | B1193 ("harvest-queued," never subsequently verified) |
| 93 | KLEIN_PARITY | — | **C** | B1193 (harvest-queued) |
| 94 | H_THEOREM | — | **C** | B1193 (harvest-queued, "clock-coherence") |
| 95 | STAGE2_UNSEALED | — | **C** | B1193 (harvest-queued, "Stage-2 closure") |
| 96 | DEGREE_LEDGER | — | **C** | B1193 (harvest-queued) |
| 97 | BRANCH_BIT | — | **A** | — |
| 98 | FOUNDING_TORSOR | — | **A** | — |
| 99 | UNIT_TRICHOTOMY | — | **A** | — |
| 100 | GRAMMAR_DISC48 | — | **A** | — |
| 101 | GAMMA5_REVERSER | — | **A** | — |
| 102 | CLASS_GROUP_953 | — | **A** | — |
| 103 | PRINCIPAL_WITNESSES | — | **A** | — |
| 104 | E6_BOUNDARY | — | **C** | B1195/B1200/B1201 (abstract Φ₃ identity rebuilt; own E₆/ℤ[ω] construction "still owed") |
| 105 | MENU_WIDTH | — | **A** | — |
| 106 | RELATIONAL_KAPPA | — | H* | **B1200, uncredited** — main independently verified this memo's own K2 cross-link (Φ₃(κ−2)=0) "exactly rather than adopted," without citing "memo 106" |
| 107 | QUINE_BUILT | — | H | B1201 (byte-identical re-run; was CITED-only in B1200) |
| 108 | AMPHICHIRAL_WORD | — | **C** | cited as background for memo 109's proof; never itself re-run |
| 109 | FENCE_INDEPENDENCE | — | H | B1201 |
| 110 | MIRROR_KERNEL | — | H | B1201 |
| 111 | BIT_LEDGER | — | H | B1201 |
| 112 | OCCUPANT_TYPE | — | H | B1201 (confirmed, but redundant with B1195/GC-24) |
| 113 | FIRST_BEAT_LAW | — | H | B1201 (byte-identical; but its *own* cross-link claim to GC-24 later ruled vacuous/tautological by B1201's own hostile-review cell) |
| 114 | PATTERN_LADDER | — | H | B1201 |
| 115 | SHADOW_PAIRING | — | **A** | — |
| 116 | UNIQUENESS_TEST | — | **A** | — |
| 117 | LAYER_TOWER | — | **A** | — |
| 118 | LAYER_FLOW | — | **A** | — |
| 119 | SECOND_CLIMB | — | **A** | — |
| 120 | CLOCKS_INVENTORY | — | **A** | — |
| 121 | B496_REDISCOVERY | — | **A** | (self-correction: 117/118 re-derived main's own B496 without citing it) |
| 122 | DM_STABILITY | — | **A** | — |
| 123 | DM_CENSUS | — | H | B1208 (confirmed entry-for-entry, stronger) |
| 124 | YIN_TRANSITION | — | **A** | — |
| 125 | CANCELLATION_RESIDUE | — | **A** | — |
| 126 | ANATOMY_RECONCILE | — | **A** | — |
| 127 | DUALITY_INDEX | — | H | B1208 (confirmed, identified with B1203) |
| 128 | LAMBDA_RANK | — | H | B1208 (confirmed, derivation corrected) |
| 129 | HD_EXHAUSTION | — | H | B1208 (ADOPTED) |
| 130 | D2_SCOPE | — | H | B1208 (confirmed stronger, 541× witness) |
| 131 | LEAP1_PROPAGATION | — | **A** | — |
| 132 | INFLATION_PROBE | — | **A** | — |
| 133 | THE_LADDER_RESULT | — | H | **B1213** (verified entry-for-entry) |
| 134 | LAW_DECLARATION_AUDIT | — | **A** | — |
| 135 | STRUCTURE_PROBE | — | **A** | — |
| 136 | THETA_EVEN_FIREABILITY | — | **C** | B1217 (read, not re-run) |
| 137 | KIND_ROW_ADJUDICATION | — | **A** | — |
| 138 | L173_SEAL_PATH | — | **A** | — |
| 139 | SEND_QUEUE_READINESS | — | **C** | B1217 (read, not re-run) |
| 140 | Q1_REWRITE (Q1) | — | **C** | B1217 (read, not re-run) |
| 141 | Q1_REWRITE (Q2) | — | **C** | B1217 (cross-seat lesson-propagation noted) |
| 142 | LANE_SELF_AUDIT | — | **A** | — |
| 143 | VOL_BASIS_PROBE | — | **C** | **B1217** — explicitly typed "CITED, with both checkable sub-claims CONFIRMED and the run unreproduced" |
| 144 | L173_GAP_DETECTOR | — | **A** | — |
| 145 | REVERSAL_FORCES_SYMMETRY | — | **A** | — |
| 146 | ODD_INDEX_ASYMMETRY | — | **A** | — |
| 147 | GOLDEN_EXCESS_ENSEMBLE | — | **A** | — |
| 148 | P3_HOSTILE_READ | — | H | RELAY_LEDGER row121 / `papers/P3_THE_PAPER/SPEC.md` (H3 independently re-derived+confirmed; 2 of 3 witnesses corrected) |
| 149 | P3_CLAIM_TRACE | — | **A** | — |
| 150 | THE_PAPER_CHAIN | — | **A** | — |
| 151 | THE_ROUTE_A_DISPOSITION | — | **A** | — |
| 152 | THE_CHAIN_GAP | — | **A** | — |
| 153 | GAP_DOCS_CURRENCY | — | **A** | — |
| 154 | LANE_INSTRUMENT_ADOPTION | — | **A** | — |
| 155 | MERGE_DIGEST_AND_VERIFY | — | **A** | — |
| 156 | GATE_D_FIRST_NUMERICS | — | **A** | **explicit**: "main never banked memos 156/157 (zero hits)" — preventive DO-NOT-BANK flag; main's own hostile read found its box-dimension result a pixel-resolution artifact |
| 157 | GATE_C_ADJUDICATION | — | **A** | same explicit zero-hits statement; content later landed on main independently (Gate C closed by refutation condition, `d7df9316`) without crediting this memo |
| 158 | GATE_C_CORRECTION | ADOPTED (internal, re: memo153's rule) | **A** | — |
| 159 | STATE_CLAIM_LINTER | SUPERSEDED (internal, re: its own linter's subject) | **A** | — |
| 160 | Q7_STRONG_APPROXIMATION | — | **A** | — |
| 161 | Q7_STABILIZER_ID | — | **A** | — |
| 162 | Q7_TRIALITY | — | **A** | — |
| 163 | THE_MIRROR_CLASS | — | **A** | — |
| 164 | THE_MIRROR_INSTRUMENT | **NOT ADOPTED** | **A** | *excluded from expansion by task rule* |
| 165 | CHAIN_GAP_CURRENCY | — | **A** | — |
| 166 | THE_PAIRED_SUMMARY_CHECK | **NOT ADOPTED** | **A** | *excluded from expansion by task rule* |
| 167 | Q7_LEDGER_AUDIT | — | **A** | — |
| 168 | THE_ESSENCE | — | **A** | — |
| 169 | THE_SIGMA_ASK | — | **A** | — |
| 170 | THE_ONE_WALL | — | **A** | (B1294 reaches the same 3rd-regime conclusion independently, "does not cite B1227 once") |
| 171 | THE_SIGMA_TYPE_ERROR | — | **A** | — |
| 172 | THE_SENSE_CENSUS | **ADOPTED** (own instrument) | **A** | — |
| 173 | THE_PAPER_ARRIVED | HEAD-NOTED; §2(a)/§3 **RETRACTED** | **A** | *excluded from full expansion (partial self-retraction)* |
| 174 | THE_FIRST_MEASUREMENT | — | **A** | — |
| 175 | THE_HYPERBOLIC_CEFF | — | **A** | — |
| 176 | THE_CEFF_LAW | §§5–7 **REFUTED/RETRACTED** | **A** | *excluded from full expansion (partial self-retraction, same day, by memo 177)* |
| 177 | THE_CEFF_SCALING_LAW | NEGATIVE (one sub-finding) | **A** | — |
| 178 | THE_SUBSTITUTE_WAS_THE_OBJECT | — | **A** | — |

---

## 2. The expanded section — unharvested positives (CITED/ABSENT, own mark clean)

### (a) Mathematical results

*Format: memo — claim (≤25-word quote) — cert — caveat — bears on.*

**56 DARK_LEDGER** — "no triple couples the 16 to the singlet… the vector-like 10 is the sole channel." `dark_ledger.py`. Caveat: SO(10)-inside-e6 choice is "OBSERVER-PAID." Bears on: SM group / dark sector.

**57 FAMILY_ESCALATOR** — the internal clock is "a family-charge escalator: each tick moves a state down the ladder 1→16→10." `dark_carrier.py`. Caveat: extends 56's frame fence. Bears on: dynamics / dark sector.

**59 CENTER_IS_THE_LOCK** — "Four independently computed structures are one operator: the center of the holonomy closure." `center_lock.py`. Caveat: "commuting involutions abound" — sharpens away an overclaim. Bears on: chirality/instrument unification.

**60 ONE_QUADRATIC_TWO_ENDS** — the conserved pair satisfies "X²−(x²−1)X+(x²−1)," reading Eisenstein at the cusp and golden at the 2I end. `one_quadratic.py`. Caveat: curvature reading "interpretive and fenced." Bears on: values / arithmetic structure.

**61 VEV_LEDGER** — "a singlet vev preserves the matter parity but breaks the lock" — object's one group-paid ℤ/2. `vev_ledger.py`. Caveat: "no potential, no vev asserted." Bears on: SM group / dynamics.

**62 FAMILY_PORTAL_FINE** — "in every internal triple, the distinguished leg carries each family exactly twice" — exact E8-channel democracy. `family_portal_fine.py`. Caveat: E8 not object-paid (memo 53 fence). Bears on: generation count.

**63 EXCHANGE_LEDGER** — "the three-family vertex is exactly symmetric under full exchange… (−1)×(−1)=+1." `exchange_class.py`. Caveat: "kinematic sign ledger, not a statistics claim." Bears on: generation count.

**64 MIRROR_DEEPEST** — "the beat induces exactly I₆ on gr₃" — the deepest 6 dims of matter are mirror-rigid. `mirror_deepest.py`. Caveat: none stated beyond corrected slot labeling. Bears on: chirality.

**65 PERIPHERAL_DIMS** — "the longitude-alone fixed space coincides with the joint cusp-fixed space" — the 12/15 coincidence resolved (half forced, half genuine). `peripheral_dims.py`. Caveat: two tautological asserts pre-removed. Bears on: gravity-cosmology/instruments.

**66 MINIMAL_FACTOR** — "every nontrivial e6 irrep… has dim ≥ 27, equality only for the 27 and its dual." `minimal_factor.py`. Caveat: "the requirement of a nontrivial internal factor remains a modelling choice." Bears on: SM group.

**67 CENSUS_DIMENSIONS** — orbit-dimension multiset for all 20 characteristics computed exactly; catches the bench's own memorized comparison list as wrong. `census_distinct.py`. Caveat: corroboration, not a completeness proof. Bears on: instruments/methodology.

**71 SUSY_NO_GO** — "no odd operator squaring to the meridian exists… the object's one square-root of the tick is even and semilinear." `susy_test.py`. Caveat: "cited (cloud stack single-homed)"; 4d field-theoretic SUSY untouched. Bears on: dynamics (SUSY).

**72 UNIQUE_CHAIN** — "the 27 offers exactly TWO SM-safe vev directions… the chain lands on exactly the SM torus." `breaking_chains.py`. Caveat: main types this CITED, not re-run — "the cloud stack, cited." Bears on: SM group / breaking chain.

**76 Z2_CENSUS** — "not one of the 15 [survivor ℤ/2s] is an R-parity substitute: every survivor is odd on exactly 8 of the 15 SM states." `z2_census.py`. Caveat: measured, "no mechanism claimed." Bears on: SM group / dark matter.

**77 PSI_SURVIVAL** — "the surviving torus IS the SM torus, not merely contains it… not even a discrete cyclic shadow survives" of u(1)_ψ. `psi_survival.py`. Caveat: dark-block stability conclusion is conditional. Bears on: SM group / dark sector.

**79 ONE_BIT_WITNESS** — "chirality is character-INVISIBLE… orientation is character-VISIBLE… gal(q)=q⁻¹ exactly." `one_bit.py`. Caveat: filed as a preregistration refusal, not a clean hit. Bears on: chirality/instruments (observer bit).

**81 GEODESIC_TONGUE** — mirror "negates every geodesic's torsion and preserves every length" on m004's exact complex-length spectrum. `geodesic_tongue.py`. Caveat: mirror-parity of analytic torsion "FENCED (WebSearch budget exhausted)," relayed to a now-retired seat, never answered. Bears on: chirality/gravity-cosmology.

**83 COSMOGONY_LEDGER** — "the object forces ZERO CP-odd phase" — every ingredient of the Big Bang typed SCRIPT/ARROW/SCHEDULE/WALL. `cp_column.py`. Caveat: interpretive mapping labeled throughout; two banked channels only. Bears on: gravity-cosmology.

**84 ATOM_SHAPE** — "Q(uud)+Q(e)=0 and Q(udd)=0, EXACTLY" — hydrogen/neutron neutrality forced by the same anomaly arithmetic as hypercharge. `atom_shape.py`. Caveat: existence only, "binding is dynamics, walled." Bears on: SM values / gravity-cosmology.

**85 SCRIPT_CHAIN** — "the record's coupling has NO diagonal entry — the neutrino sector is DIRAC-ONLY in-record." `script_chain.py`. Caveat: a seesaw "requires structure the object has not paid for." Bears on: dynamics (neutrino mass mechanism) — a genuine, still-open structural gap.

**86 ORDER_DIRECTION** — the owner's a/ab/ba conjecture "half-confirmed": order is forced (κ = tr[a,b]), but direction is free three independent ways. `order_direction.py`. Caveat: none. Bears on: chirality/gravity-cosmology (arrow of time).

**87 DARK_LAW_PROVED** — B534's dark hyperbola classifier for N=p² *proved* from three Gauss lemmas, closing a 6-week-buried owner register item (R5/H123). `dark_law_p2.py`. Caveat: none stated. Bears on: dark matter / number theory.

**88 DARK_TOWER** — generalizes 87 to arbitrary prime-power depth: one classifier, spectrum {0,1,√p,…,p^(e/2)}, "531,000+ points." `dark_tower.py`. Caveat: one clause preregistered conjectural, held at every tested point. Bears on: dark matter.

**89 DARK_TOWER_COUNTED** — closed-form shell counts for the dark tower, proved by induction, verified at 12 depths. `dark_tower_counts.py`. Caveat: none. Bears on: dark matter (completes 87–88).

**90 TWO_PULSES** — answers the owner directly: "the heartbeat is isometric: it CANNOT drive expansion" (theorem); the record's actual stretching pulse is the golden substitution. `two_pulses.py`. Caveat: "the unpaid weld named" — expansion mechanism still open. Bears on: gravity-cosmology.

**91 OWN_METER** — "the object's archimedean action equals a special value of its own finite/arithmetic shadow" — Vol computed as an L-value four independent ways, agreeing to 50 digits. `own_meter.py`. Caveat: none. Bears on: values / gravity-cosmology — a striking, hard-to-dismiss result.

**92 TWIST_PARITY** — "the hierarchy carrier is MIRROR-EVEN: the gauge choice is NOT an observer bit… belongs to the object's side." `twist_parity.py`. Caveat: main's own B1193 named this a "harvest-queued traveler" and never verified it. Bears on: chirality/values (generation hierarchy).

**93 KLEIN_PARITY** — B928's gauge Klein group "SPLITS under the mirror… the hierarchy line is exactly the mirror-even subgroup." `klein_parity.py`. Caveat: same queued-not-verified status. Bears on: chirality/values.

**94 H_THEOREM** — "the H-theorem as stated is REFUTED, and the refutation is a law — the arrow is BRANCH-CONDITIONAL." `h_theorem.py`. Caveat: preregistered NOT-MONOTONE, refined not simply confirmed. Bears on: gravity-cosmology (arrow of time).

**95 STAGE2_UNSEALED** — owner-authorized comparison of B928's shape sheet against measured mixing, under an exhaustive preregistered protocol. `stage2_unseal.py`. Caveat: strictly quarantined per Gate 5; prior TIER-2-MISS verdict stands. Bears on: values (Yukawa/mixing).

**96 DEGREE_LEDGER** — "the record's whole dimensionful content is a rank-1 lattice… 'seconds' costs exactly one external datum." `degree_ledger.py`. Caveat: none. Bears on: gravity-cosmology / instruments (dimensional audit).

**97 BRANCH_BIT** — "no tested symmetry commutes with the flow, fixes P₀, and reverses v_u" — the arrow's ℤ/2 is external and is NOT c. `branch_bit.py`. Caveat: exhaustive over a "natural" finite set, not a full no-go. Bears on: chirality/gravity-cosmology.

**98 FOUNDING_TORSOR** — independently verifies a result relayed from a retired seat (cc) and adds: "the object cannot even SEE the reading direction" (character-invisible). `founding_torsor.py`. Caveat: none. Bears on: chirality/instruments.

**99 UNIT_TRICHOTOMY** — three quadratic fields split observer-bit roles (silent/pulse/orienting) by unit-group arithmetic; independently verifies a cited result (GC-16). `unit_trichotomy.py`. Caveat: "exhibited pairs, not a general norm law." Bears on: values / gravity-cosmology.

**100 GRAMMAR_DISC48** — "the CM datum was a grammar word" — closes a named main-adjacent gap (GC-17) by exhibiting the longitude as an explicit grammar word. `grammar_disc48.py`. Caveat: "a realization-free derivation is a stronger claim, not made." Bears on: values / arithmetic.

**101 GAMMA5_REVERSER** — time reversal R "restricts to the γ₅ conjugation up to the unit φ∓⁶" and no banked involution induces the branch swap. `gamma5_reverser.py`. Caveat: identification with cc's r-bit "needs a level-crossing map." Bears on: chirality/gravity-cosmology.

**102 CLASS_GROUP_953** — h(K)=1 certified for the disc-6237 value field, with an explicit norm-953 generator, closing B931's terminal gap. `class_group_953.py`. Caveat: explicitly "relay to cc/codex for reproduction (a class-number claim deserves a second bench)" — never done. Bears on: values (a serious arithmetic result awaiting second-seat check).

**103 PRINCIPAL_WITNESSES** — re-proves h(K)=1 by a disjoint method (no relation matrix), self-verified generator for every prime under the Minkowski bound. `principal_witnesses.py`. Caveat: "true second-SEAT reproduction stays relayed" — same unanswered ask as 102. Bears on: values.

**104 E6_BOUNDARY** — "the E₆ root lattice carries M=(Coxeter)⁴ with M²+M+I=0 exactly… content {1,27,27̄} at level 1." `e6_boundary.py`. Caveat (main's own, B1201): "still owed" — the actual construction was never independently re-run; only the abstract polynomial identity was. Bears on: gravity-cosmology (the L154 boundary bridge) — the single most cited-but-unverified item in the whole set.

**105 MENU_WIDTH** — MENU-1 tier-1 run: W₁=11,720 distinct menu values, denominator rule fixed *before* any data contact. `menu_width.py`. Caveat: "Gate 5 untouched… tier-1 menu is DENSE" — a negative-leaning finding for the values program. Bears on: values / instruments (statistical-significance floor for any future hit).

**108 AMPHICHIRAL_WORD** — "the mirror is a word map… φ(a)=a, φ(b)=ba⁻¹b⁻¹" found by exhaustive search; the quine's one external bit "carries no object content." `amphichiral_word.py`. Caveat: cited only as background for memo 109; never itself re-run. Bears on: chirality.

**115 SHADOW_PAIRING** — tests the owner's "shadow" hypothesis (Occ(X):=[X,gal(X)]≠0) directly; a preregistered prediction (H2) fails informatively — the predicate is *not* a restatement of the mirror-odd column. `shadow_pairing.py`. Caveat: "FIREWALLED per H5." Bears on: instruments/chirality.

**116 UNIQUENESS_TEST** — deliberately hostile design finds "6 distinct admissible sets" pass the gates memo 115 used, downgrading 115's status from leading candidate to "one of several." `uniqueness_test.py`. Caveat: self-downgrading, methodologically honest. Bears on: instruments.

**117 LAYER_TOWER** — the owner's layering hypothesis L(A,B)↦(AB,BA) "does not collapse" through 8 levels but "adds STRUCTURE… provably NO INFORMATION." `layer_tower.py`. Caveat: independently re-derives a *pre-existing* main arc (B496) without citing it — corrected in memo 121. Bears on: dynamics/instruments.

**118 LAYER_FLOW** — closes the layering map to an exact 2-variable dynamical system in (z,κ); proves it is NOT the banked Fricke dynamics. `layer_flow.py`. Caveat: same B496-overlap issue (memo 121). Bears on: dynamics.

**119 SECOND_CLIMB** — "L is the ONLY κ-breaker" among 5 banked maps; commutation table shows genuine non-commutative structure at the level of maps. `second_climb.py`. Caveat: interpretive framing labeled. Bears on: dynamics.

**120 CLOCKS_INVENTORY** — self-correction ("bench error #10"): the record does NOT lack time — three flows/rate/order/arrow/beat are already banked; only "the second" and "the thermal arrow" are missing. `clocks_inventory.py`. Caveat: corrects the bench's own prior overstatement. Bears on: gravity-cosmology.

**122 DM_STABILITY** — runs COSMOLOGY_LEDGER row 4 verbatim: "the object's forced gauge 2-torsion supplies NO stabilizer" for either dark candidate. `dm_stability.py`. Caveat: basis-independent test, negative result. Bears on: dark matter — directly answers a row in **main's own** ledger, uncredited.

**124 YIN_TRANSITION** — the record's dynamics "passes from the being field to the hearing field exactly once, at the cusp," and the crossing is irreversible. `yin_transition.py`. Caveat: answers "the computable half" of the owner's yin/yang question only. Bears on: gravity-cosmology/chirality.

**125 CANCELLATION_RESIDUE** — advances a stalled paper card (PC04): "the residue := κ−2 = ω² exactly" — the founding Eisenstein unit itself. `cancellation_residue.py`. Caveat: values a pre-existing named gap, doesn't close it. Bears on: values/instruments.

**126 ANATOMY_RECONCILE** — resolves a standing CHANGELOG "blemish" (zero name-overlap between kill_graph's faces and the atlas's motifs) by building the actual contingency table: the schemes are ORTHOGONAL, not redundant. `anatomy_reconcile.py`. Caveat: reads main's own primary sources directly. Bears on: instruments/paper.

**131 LEAP1_PROPAGATION** — mechanical audit of a payment ("LEAP-1 PAID") through the corpus; catches two overstatements at the point of payment. `leap1_propagation.py`. Caveat: governance-adjacent but substantive (methodology). Bears on: instruments.

**132 INFLATION_PROBE** — runs COSMOLOGY_LEDGER row 2: "the object cannot inflate, and the obstruction is a determinant IDENTITY" (no tower map gives net volume growth). `inflation_probe.py`. Caveat: reframes tilt/e-folds as one Gate-5-clean question first. Bears on: gravity-cosmology — a clean negative on main's own open row.

**134 LAW_DECLARATION_AUDIT** — this is memo 133's actual content in the file (numbering shifted vs the INDEX row) — already HARVESTED as B1213; the compact table already credits it.

**135 STRUCTURE_PROBE** — runs COSMOLOGY_LEDGER rows 7/8: "the three blind rows are ONE obstruction seen three times" — row 8's growth is exponential-class so no exponent can even be compared. `structure_probe.py`. Caveat: explicitly avoids the S008 "iterations≈e-folds" trap. Bears on: gravity-cosmology.

**136 THETA_EVEN_FIREABILITY** — an owner-released irreversible "shot" found NOT fireable: 4 of its own 4 pre-work items are outstanding, so the last licensed contact row is left unspent. `theta_even_fireability.py`. Caveat: read, not re-run (B1217). Bears on: governance/instruments — but has real mathematical content (a no-go on firing).

**137 KIND_ROW_ADJUDICATION** — "the mirror row's independent content is exactly THREE values; 5 of its 8 are already spent" — reproduces a tensor mechanism (B1032) from character theory rather than citation. `kind_row_adjudication.py`. Caveat: typing, not a new shot. Bears on: values/instruments.

**138 L173_SEAL_PATH** — proves cross-hand isospectrality is "an IDENTITY, not a finding": J·H·J = H(reversed word) for ANY word. `l173_seal_path.py`. Caveat: a second B724-shaped defusal, caught pre-seal. Bears on: instruments (lab-prediction discipline).

**144 L173_GAP_DETECTOR** — built to fix a volatile diagnostic instrument, and "overturns the diagnosis it was built to fix": the volatility is real, not detector error. `l173_gap_detector.py`. Caveat: fires D-VOLATILE as preregistered. Bears on: instruments.

**145 REVERSAL_FORCES_SYMMETRY** — proves (not measures) that reversal-closed windows must tie: H_L=J·H_R·J is a theorem, closing L173's last surviving differential. `reversal_forces_symmetry.py`. Caveat: none. Bears on: instruments (kills a laboratory-prediction lead cleanly).

**146 ODD_INDEX_ASYMMETRY** — the theorem's one named exception is real but generic — every Sturmian slope shares it. `odd_index_asymmetry.py`. Caveat: took 3 iterations to control correctly, recorded honestly. Bears on: instruments.

**147 GOLDEN_EXCESS_ENSEMBLE** — closes 144's own open lead negatively: the apparent golden-slope excess was a Fibonacci-convergent-window confound, not real. `golden_excess_ensemble.py`. Caveat: "the failure is in this cell's own seal." Bears on: instruments — an honest negative closing an internal lead.

**160 Q7_STRONG_APPROXIMATION** — "zero arcs in the corpus mention strong approximation" — reopens Route A via Kneser–Platonov, finds 3 of 5 hypotheses hold. `q7_strong_approximation.py`. Caveat: "does not conclude that Route A crosses." Bears on: values (Route A / the "finite menu is terminal" claim).

**161 Q7_STABILIZER_ID** — computes the generic stabilizer of a (27,27̄) pair exactly: "𝔰𝔬(8) — type D₄. Identified, not guessed." `q7_stabilizer_id.py`. Caveat: "a Lie algebra is not a group scheme" — fenced by memo 161 itself. Bears on: values (Route A).

**162 Q7_TRIALITY** — "the group is Spin(8)": 27 = 1+1+1+8v+8s+8c, discharging 161's own fence; Q7 moves to "four of five." `q7_triality.py`. Caveat: orbit-count = class-set remains the one open ask. Bears on: values (Route A) — a substantial structural result feeding a still-unsent specialist question.

**167 Q7_LEDGER_AUDIT** — closes the "ℚ-simple" hypothesis by direct computation (centroid dim 1, Killing form nondegenerate) rather than by the substitution memo 160 used; "the number does not move," the proof does. `q7_ledger_audit.py`. Caveat: self-audit of its own prior chain (160–162). Bears on: values (Route A, now genuinely 4 of 5 proved).

**168 THE_ESSENCE** — re-reads the whole record's own stated floor ("ONE unit + TWO bits + acceptances… no continuous input except σ") with no new math but one new count. `essence_census.py`. Caveat: explicitly "not offered as a breakthrough." Bears on: paper/values synthesis.

**169 THE_SIGMA_ASK** — kills its own inference before drafting Q11: "no cover of m004 has six cusps up to degree 8," and every cover has CS≡0 — six cusps "are not available and would not help." `cusp_six_census.py`. Caveat: "nothing sent" at time of writing. Bears on: values (σ / L154 bridge) — directly informs Q11.

**170 THE_ONE_WALL** — unifies three apparently separate "walls" as one amphichirality theorem (B1227): 2·I(M)=0 in any abelian group A the mirror acts on by negation, with a third (ℤ, torsion-free) regime the corpus tracked separately. `partial_filling_joint.py`. Caveat: notes main's own B1294 reached the third regime independently, uncited both ways. Bears on: gravity-cosmology/chirality.

**171 THE_SIGMA_TYPE_ERROR** — identifies the literature this WHOLE 1122-arc corpus never once searched (Ẑ-invariants, GPPV, logarithmic VOA, F_K) as the exact missing tool for the σ bridge; corrects a category error (six cusps were never the requirement). `c_eff_calibration.py`. Caveat: "nothing here claims σ=1." Bears on: values (σ) — this is the memo that produced Q11, the *only* gate-send actually transmitted.

**174 THE_FIRST_MEASUREMENT** — runs GC-6's own c_eff estimator on the actual object for the first time (not on (E6)1 or η⁻¹): "coefficients all ±1… a false theta. c_eff=0" for Σ(2,3,7); the mock-theta measurement for the mirror surgery. `zhat_ceff.py`. Caveat: source paper read on-bench, not independently vetted. Bears on: gravity-cosmology (the L154 bridge, GC-6's charge).

**175 THE_HYPERBOLIC_CEFF** — derives c_eff = 3(log φ)²/π² = 0.070387 from the paper's own Theorem 1.2 + §6.8 spin-c convention (not a fit), superseding its own earlier mis-anchored 0.0938. `hyperbolic_ceff.py` + `hyperbolic_derived.py`. Caveat: superseded in turn (positively, its tangent point survives) by memo 177. Bears on: values/gravity-cosmology.

**177 THE_CEFF_SCALING_LAW** — refutes and replaces memo 176's law: c_eff(Q)=(6/π²)max_y[yh(y)−y²/Q], cross-validated to seven figures against 10 independently published GM series and against three exact Seifert values; proves c((E6)1)=6 is *unreachable* for the figure-eight. `ceff_scaling_law.py` + 5 more certs. Caveat: extensive, self-stated — "the law is a saddle-point statement, validated not proved"; a full literature fence naming three unread papers on the exact same subject. Bears on: gravity-cosmology (L154) — the single deepest, most cross-checked result in the whole 149-memo set.

**178 THE_SUBSTITUTE_WAS_THE_OBJECT** — discharges its own long-standing self-charge: GC-6's "1" (η⁻¹) *is* the object's own colored-Jones tail edge, measured not asserted; reshapes the 6-vs-1 gap from "nothing in between" to a named, priced open cell. No new cert (reads 177's). Caveat: "no bridge asserted, no lead closed." Bears on: gravity-cosmology (L154).

### (b) Instruments the cloud ADOPTED (as internal practice, own mark = ADOPTED)

**165 CHAIN_GAP_CURRENCY** — applies "**memo 153's adopted rule**" (`already_banked.py` run on each row's own stated terms before any MISSING/OPEN claim). Certificate: reuses `scripts/checks/already_banked.py`. **Important correction to the brief's framing**: this tool is not the cloud's invention — `already_banked.py` is **main's own B1202** (banked 2026‑08‑28, "the finished-but-forgotten class gets an INSTRUMENT"), and memo 153 (2026‑08‑30) is where the cloud first *imported* it into its own workflow. So the true direction of travel for this instrument is **main → cloud**, the opposite of a "cloud adoption main harvested." Bears on: governance/instruments.

**172 THE_SENSE_CENSUS** — own header: "**ADOPTED**, and it finds a collision at 3474 occurrences." First self-built instrument whose own control did NOT void it (contrast 164 and 166, both explicitly "NOT ADOPTED"). Detects "false comfort" — a term present in the corpus but never in its technical sense (e.g. "logarithmic" meaning log-of-a-number everywhere, never once "logarithmic CFT"). Certificate `sense_census.py`. Caveat: excludes `outside_bench/` itself from the scan to avoid self-contamination. Bears on: instruments/paper — genuinely useful methodology, unmentioned on main.

### (c) Governance/paper items

**139/140/141 SEND_QUEUE_READINESS / Q1_REWRITE** — audits the specialist send-queue for staleness (Q1 stale by 8 post-queue arcs) and narrows Q2. Main read these (B1217) but did not re-verify the readiness audit itself.

**142 LANE_SELF_AUDIT** — 112 certificate/output pairs re-run: 0 failures, 1 genuine drift, and the audit's own instrument produced false positives from a race condition. Absent from main.

**143 VOL_BASIS_PROBE** — see table; explicitly typed CITED by main's own B1217 with a named "evidence-contract gap" (the committed cert is the wrong file).

**149/150/151/152 P3_CLAIM_TRACE / THE_PAPER_CHAIN / THE_ROUTE_A_DISPOSITION / THE_CHAIN_GAP** — a chain of hostile-read paper audits: 18/50 claims mechanically mis-sourced (D1-NOISY), zero arc citations in two sections (D4-GAPS), and a self-correction ("the corpus did not lose Route A — I was wrong to say so"). Absent from main.

**153/154/155 GAP_DOCS_CURRENCY / LANE_INSTRUMENT_ADOPTION / MERGE_DIGEST_AND_VERIFY** — the cloud turning main's own 12 `scripts/checks/` instruments on itself; finds 12 dead path-citations, all its own; merges 99 commits with zero conflicts. Absent from main (this is the cloud auditing itself with main's tools).

**158 GATE_C_CORRECTION** — bench error #17, self-caught: "the live route is not unrun, it is run and sector-complete" (B632 cell 2 was actually run 2026‑07‑15). A genuine correction of the cloud's own prior misreading of main.

**159 STATE_CLAIM_LINTER** — builds an instrument for "a claim about the state of the record, asserted from prose rather than checked against the artifact" — the exact failure class that produced memo 158's error.

**163 THE_MIRROR_CLASS** — pure reading of main at a pinned commit; records that memo 157's content "landed on main" (Gate C closed) without crediting the cloud, and that a paper drift charge got *stronger* since it was filed, not weaker.

**168 THE_ESSENCE** — see (a); largely a synthesis/reading exercise for the owner.

**173 THE_PAPER_ARRIVED** *(excluded from full expansion — genuine partial self-retraction: §2(a) and §3 false, filed same day)* — worth a one-line flag anyway: the cloud read only 4 of 79 pages of the actual Gukov–Manolescu paper before declaring a refutation, and two of three headline claims were wrong. This directly seeded memos 174–178's more careful work.

**176 THE_CEFF_LAW** *(excluded — §§5–7 explicitly REFUTED/RETRACTED by memo 177 same day)* — sections 1–4 (block-4 confirmation, series exact to q³⁹⁵²⁴) explicitly stand per memo 177's own head-note and are folded into 177's harvest-worthy content above.

---

## 3. The seat's own open asks — Q1–Q12 (`THE_GATE_SENDS.md`, `docs/SPECIALIST_SEND_QUEUE.md`, `sends/`)

| # | subject | priority | status as of the branch head |
|---|---|---|---|
| Q1 | SEAM-A Gate 2 (Andersen–Hansen / Kim-style arithmetic-CS extension to cusped m004) | ★★★★ | Drafted, **HOLD** (owner, 2026‑08‑27); readiness audit (memo 139) later found it **stale by 8 post-queue arcs**. Not sent. |
| Q2 | J₃(𝕆) Beilinson regulators (Tier B) | ★★★ | HOLD → **narrowed** (addendum 7, 2026‑08‑31): the volume-regulator half is closed by Lee's theorem (verified on-bench); only the exceptional-domain half remains. Not sent. |
| Q3 | B491 seam form (ℚ(√5,√−3)-projection vanishing) | ★★★ | HOLD, ready as written. Not sent. |
| Q4 | Cappell–Miller order of vanishing (cusped Ruelle zeta) | ★★ | HOLD, ready as written. Not sent. |
| Q5 | B165 complexified hyperbolicity (metallic family off-axis) | ★★ | HOLD, ready as written. Not sent. |
| Q6 | The closed-form k (rider on Q3/Q5) | ★ | Not standalone; rides Q3/Q5. Not sent. |
| Q7 | Route A / trialitarian Spin(8) strong approximation | (rewritten 5×) | Rewritten through addenda 3–5 and memo 167: **4 of 5 hypotheses now proved** (simply connected, ℚ-simple, non-compact, stabilizer=D₄); only "orbit count = class set" remains. "Worth sending." **Not sent.** |
| Q8 | Gate B "the crux" (T[4₁;E₆] cascade as gauge dynamics) | — | Confirmed **NOT the cloud's own gap** (ownership was inherited, not tested). Stands as drafted. Not sent. |
| Q9 | Gate C (intrinsic ℤ/3 → three generations) | — | **WITHDRAWN** — its own answer (NO) was already banked on main (B323/B324), neither cited in the gate's own Settled list. Pending a rewrite around the *actual* live mechanism (B632 cell 2). |
| Q10 | Gate D (non-Hermitian Damanik–Gorodetski at complex κ) | — | **"WAS OURS and is now done"** — answered internally as memo 156. **Caveat the seat itself doesn't flag**: main's own hostile read (RELAY_LEDGER row 126) found memo 156's headline numbers were pixel-under-resolution artifacts and explicitly flagged it DO-NOT-BANK — so the gate the seat calls closed rests on a memo main found broken. |
| Q11 | The σ bridge (Brown–Henneaux c=6σ / boundary CFT identification) | ★★★★★ (higher than Q1) | **SENT** — 2026‑08‑31, to Tudor Dimofte (Edinburgh), signed "Dritëro M.," message id `1a05a10d88d4971a`. The **only actual transmission** in the queue's history. |
| Q12 | c_eff-from-surgery literature (the arXiv:2508.10087 authors) | — | **DRAFTED, DO NOT TRANSMIT.** Recipient list unverified (three candidates named, none confirmed); standing instruction is compose-only. |

---

## 4. Count table

| status | count | share |
|---|---|---|
| **HARVESTED** | 51 | 34% |
| **CITED** | 21 | 14% |
| **ABSENT** | 77 | 52% |
| **Total (30–178)** | 149 | 100% |

Excluded from expansion by their own mark (RETRACTED/SUPERSEDED/NOT ADOPTED): memos **164, 166** (self-built instruments explicitly NOT ADOPTED) and **173, 176** (partial same-day self-retractions).

---

## 5. Highest-value unharvested — top 10, one line each

1. **Memo 177 (THE_CEFF_SCALING_LAW)** — a saddle-point law cross-checked to seven figures against ten independently *published* Gukov–Manolescu coefficients; the deepest, most externally-validated result in the set, and main has zero record of it.
2. **Memos 161/162/167 (Q7: Spin(8) stabilizer)** — Route A ("the finite value menu is terminal") is now 4-of-5 proved by direct computation, one hypothesis from a real crossing test main's own paper language depends on.
3. **Memo 171 (THE_SIGMA_TYPE_ERROR)** — found the *entire* 1122-arc corpus never once searched for Ẑ-invariants/GPPV/logarithmic VOA, the literature that actually bears on σ; produced Q11, the one gate-send that got sent.
4. **Memo 91 (OWN_METER)** — Vol(m004) proved equal to a special L-value of the object's own field in four independent dressings to 50 digits; a striking, easily-reproducible arithmetic fact.
5. **Memo 104 (E6_BOUNDARY)** — the only serious attempt at the L154 boundary-object construction anyone has made; main independently re-verified its *abstract* polynomial identity but never the construction itself.
6. **Memos 87–89 (dark tower)** — a fully proved, closed-form prime-power classifier that closes a 6-week-buried owner question (R5/H123); zero main engagement.
7. **Memos 92/93 (TWIST_PARITY/KLEIN_PARITY)** — resolves whether the generation hierarchy is object-side or observer-side; main's own B1193 named it a "harvest-queued traveler" and then never came back.
8. **Memo 85 (SCRIPT_CHAIN)** — names a real, unclaimed structural gap (no Majorana term exists in the record's own coupling — Dirac-only neutrinos, seesaw unpaid), a negative main would likely want on its own ledger.
9. **Memo 143 (VOL_BASIS_PROBE / V-NEG)** — closes a value-crossing corner using the object's own canonical regulator; main confirmed every checkable sub-claim and stopped one commit short because the extended-run certificate is the wrong file.
10. **Memo 132/135 (INFLATION_PROBE/STRUCTURE_PROBE)** — clean negatives on rows 2/7/8 of **main's own** COSMOLOGY_LEDGER, run and typed exactly to the ledger's own specification, with zero credit back to main's document.