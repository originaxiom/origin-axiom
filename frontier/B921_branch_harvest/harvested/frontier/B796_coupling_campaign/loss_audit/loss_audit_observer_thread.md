## Verdict summary

I read the FMT arc, the B848–B853 SSB sub-window, all 60+ arcs from B854→B917, the five registers, and Reviews 33–38 on `origin/main` @ `263234c4`. Findings below; all paths are absolute (read via `git show origin/main:<relative>`).

---

## (a) CONNECT-OR-PARALLEL: the new window runs **parallel**, with one 6-day bridge that was abandoned mid-span

**The First Measurement Theorem's "measurement" is a new, purely Lie-theoretic notion, and the B766 torsor is never cited.**

`[machine-path]/frontier/B877_fmt_review/REVIEWED_DOCUMENT.md` defines measurement as *centralizer-of-a-superselection-charge*: §5 reads "symmetry breaking = superselection-charge measurement; the first step of the world's cascade is the centralizer of any one of exactly three conjugate distinguished charges." Its §4 imports are I1–I5 (torality, reductivity of centralizers, the Cartan classification table, the one-prime lemma, D₅⊕u(1) branching). **No import, no clause, no dependency line mentions B700, B766, C20, C22, or the closing menu.** The S1 review (`frontier/B877_fmt_review/FINDINGS.md`) likewise cites only B854/B866/B872/B874/B875 and JOINT_NOTE_CC.

The hard count over every main-side arc from B854 onward:

| observer arc | files citing it in `frontier/B854+` |
|---|---|
| B700 (fiber functor), B733 (observer menu), B766 (measurement torsor), B782 (C22), B783 (C23), B786 (θ/ι), B725/B726/B728/B729 (Born ledger), B750 (lack ledger), B736 (A+B+C) | **0** |
| B701 | 1 — and it is `frontier/B887_gate_audit/audit_reports.json:656` noting that *the B701 directory no longer exists on disk* |
| B787 | 1 — inside cc3's imported branch text, `frontier/B878_maass_upper_window/branch_FINDINGS.md:255` |
| B723 | 3 — all in `frontier/B855_wrong_null_audit/` (a witness-list audit) |

`docs/LAW_MAP.md` now has a new **Section F** (21 rows, added in HEAD commit `263234c4`) titled "The measurement cascade and the value layer." Not one row cross-references Section D's observer laws (rows 147–158, B700–B736). Two disjoint "measurement" vocabularies now sit in the same file.

The collision is also live in `[machine-path]/TERMINOLOGY.md`: line 164 defines **"measurement = fiber functor"** (B700/B701 — "the object gives the torsor, never the point"), and line 218 defines **"the First/Second Measurement Theorems"** (charge stratification of e₆). No reconciling clause. This is exactly what Review 38's new protocol item 7 (terminology sweep, `docs/progress/REVIEWS.md:2982`) was minted to catch, and it did not catch it.

**Where the new window did re-root "torsor":** it uses B707 (arithmetic-CS meeting point / H¹-as-measurement), not B700/B766 — `frontier/B870_lift_obstruction/FINDINGS.md:40` ("the measurement-as-torsor motif, B707's arithmetic-CS meeting point") and `frontier/B905_kim_litgate/FINDINGS.md:21`. And the masterplan's W8 lane (`docs/STRUCTURE_TO_NATURE_MASTERPLAN.md:48`) names **"the three banked torsor levels (the S₃ charge orbit; the H¹ lift torsors; the B599 pairing)"** — B766's (ℤ/2)³ closing torsor, the one the programme actually proved rank-saturated against the observer menu, **is not one of the three.**

**The one real bridge — and it was cut.** B848–B853 (2026-08-02) is a genuine, high-quality assault on the observer thread's own foundation:

- `frontier/B849_order_parameter/FINDINGS.md` — the β=1 SSB (B723) has **no manifold-level order parameter** (CS(m004)=0, nine chiral positive controls), and the nominated order parameter (chirality = complex conjugation) is at the **wrong level**: it lies in Gal(K/ℚ), not Gal(K^ab/K).
- `frontier/B851_bc_litgate/FINDINGS.md` — the CMR citation confirmed verbatim in both directions; "complex conjugation" occurs zero times in `math/0501424`. §3: *"CMR's action on extremal KMS states is free and transitive — precisely the simply-transitive torsor B700 reports. The better the identification, the worse the level error."*
- `frontier/B850_length_spectrum_type/FINDINGS.md` — the III₁/foliation route is **GENERIC** (m004, m003 and a non-arithmetic control all DENSE): "the reframe keeps being right and keeps not being about this object."
- `frontier/B853_two_faces_ssb/FINDINGS.md` — the SSB ingredients sit on two different faces (order parameter on ℚ(√5), symmetry on ℚ(√−3)).

That thread has a single named load-bearing successor — B851 §3 / B849 "Carried forward" #1: **"Is the programme's β=1 system actually a BC/CMR-type system for K = ℚ(√−3)?" … "now the sole load-bearing assumption."** It was folded into a "six-task backlog campaign … running with adversarial verification pipelined per task" declared in `PROGRESS_LOG.md:9068` (B858, 2026-08-03). **There is no `frontier/B858_*` directory on main, and `BC/CMR-type` appears in no arc after B851.** The campaign was announced and vanished; B859 pivots to the SM handoff and the window never returns.

**Verdict: parallel.** One six-day bridge (B848→B853) was built into the observer thread's foundations, produced its sharpest negative result to date, named its own single decisive successor, and was abandoned at B854 when the SM-structure window opened. Everything after B854 develops "measurement" on independent Lie-theoretic ground and cites the observer formalism zero times.

---

## (b) ORPHAN TABLE

| item | registered where | last genuine touch | status on `main` now | verdict |
|---|---|---|---|---|
| **B787 open item 2** — ι's status as an *observer closing* vs char-variety-native symmetry (the rank-3/4 question) | `frontier/B787_interaction_programme/FINDINGS.md:§4` + `docs/HINT_LEDGER.md:540` (H-B787-IOTA) + `docs/THEOREM_LEDGER.md:153` (C20 strengthened note) | **B787, 2026-07-25** | HINT_LEDGER still reads "whose status AS an observer/measurement closing operation is **UNESTABLISHED**". The only `iota` hit in B854+ is `frontier/B882_magic_square_naming/arc_verdict.json` — Elduque's ι_i inclusion maps, an unrelated symbol | **LOST** (unregistered outside a hint row) |
| **B787 open items 1, 3, 4** (Phase-3 reversal-vs-inversion recompute; canonical-root re-run) | same §4 | item 3 (the lock) closed; **items 1 and 4 never run** | item 4 ("re-run the iota-id on the canonical primitive-6th-root Riley rep loaded from B71/B99/B101") — the arc's own admitted mislabelled rep — has no register row anywhere | **LOST** |
| **C18's priced sub-structure** — "the remaining unpriced frontier: the choice-mechanics of the coupling itself (the measurement torsor; the arithmetic-CS home), plus the c-into-θ crux's remaining routes" (`docs/THEOREM_LEDGER.md:124`) | THEOREM_LEDGER Part IV | **split**: arithmetic-CS home → B905 (2026-08-05) pays B707's lit-gate; c-into-θ → **alive** in B893/B901; measurement-torsor half → nothing | B901 explicitly chases "the B570 Lane-C crux" and delivers the sharpest no-go yet (`frontier/B901_c_stabilizers/FINDINGS.md`), but **cites neither C18 nor B750** — whose falsification edge it is | **HALF-ALIVE, UNWIRED** |
| **Born CONTENT open** (B725–B729: form + quadratic degree forced, amplitudes/phase imported, content OPEN) | `docs/LAW_MAP.md:148` upgrade-path column only ("Busch POVM-Gleason on III₁; Zurek envariance vs Haar; the full CMR/Hecke off-diagonal"); `TERMINOLOGY.md` "the Born ledger" gloss | **B729, 2026-07-20** | **No OPEN_LEADS row, no OPEN_PROBLEMS row, no masterplan lane.** Zero citations in B854+. The word "Born" in `frontier/B8*`/`B9*` appears only in cc3's imported selection-cochain packet | **LOST** — exists only as a LAW_MAP prose column |
| **B733 observer menu** (bounded discrete 𝔽₂ observer-space; the ≤8 menu; rank-saturation half of C20) | `docs/LAW_MAP.md:156`, C20, `tests/test_b733_observer_space.py` | **B766 (rank-saturation), 2026-07-22** | lock green, arc intact, **0 citations after B853** | **DORMANT-ALIVE** (not retracted; unreferenced) |
| **C23 / T1-mover spec** (`docs/THEOREM_LEDGER.md:205`, "a mover must lie outside the object's native symmetry group") | THEOREM_LEDGER, `tests/test_b783_c23.py` | **B783/B775-Wave-1, 2026-07-24** | lock green. Nothing since B848 touches T1 or the mover spec. Note `frontier/B887_gate_audit/audit_reports.json:545` demonstrates the CHAIN's lock-gate would swallow a new C24 block into C23's — the C23 link is structurally fragile | **DORMANT-ALIVE, gate-fragile** |
| **B736 PATH B** — "object-level observer non-existence theorem for the INFINITE non-abelian Bianchi case … both seats flag OPEN, no known route" (`docs/LAW_MAP.md:158` upgrade column; `frontier/B736_ABC_campaign/FINDINGS.md:31`) | LAW_MAP row 158 upgrade column only | **B736, 2026-07-21** — then *indirectly* pressured by B849/B851 (which attacks the β=1 SSB from the state side) | The B849/B851 result bears directly on it (the SSB's acting group excludes the very symmetry) and **no arc connects them**. No register row | **LOST** |
| **B849/B851's sole load-bearing successor** — "is B723's system BC/CMR-type for ℚ(√−3)?" | `frontier/B849_order_parameter/FINDINGS.md:§Carried forward`, `frontier/B851_bc_litgate/FINDINGS.md:95` | **announced 2026-08-03** in `PROGRESS_LOG.md:9068`'s six-task backlog campaign | **no B858 arc dir; zero hits for `BC/CMR-type` after B851** | **LOST mid-flight** |
| **B849 carried #2** — prior-art gate on the m003/m004 2-torsion CS separation (0 vs π²/2) | same | 2026-08-02 | never run; no register row | **LOST** |
| **B849 carried #3** — T2, the geodesic-length III₁ shadow; "the 370 geodesic lengths are NOT in main — the same phantom pattern as the 43 eigenvalues" | same | 2026-08-02 | the 43 eigenvalues *were* harvested (B878); the 370 lengths never were | **LOST** |
| **B750 lack ledger** (UNIFIED-3; falsification edge = c-into-θ) | THEOREM/SEAL ledgers, `tests/test_b750_lack_ledger.py` | **B750, 2026-07-21** | B893/B901 are actively working precisely B750's declared falsification edge; **B750 is cited by no arc after B770** | **ALIVE-BUT-UNWIRED** — its own falsifier is being tested by arcs that don't know it exists |

**Q3 items (relay-corpus adjacents):**

| item | status on main |
|---|---|
| **τ-parity V₅/V₆ prototype** | Registered as **L111, "OPEN, offered; prototype exists"** — `docs/OPEN_LEADS.md:639`. Registered 2026-07-29 (R32-8), **never run**, never referenced again. The τ-parity *content* survives only as hint `H-B787-D4-TAU` (`docs/HINT_LEDGER.md:~552`) and in `frontier/B787_interaction_programme/D4_e6_v4/`. The "1+2ω" grep resolves to an unrelated congruence-index item, `PROGRESS_LOG.md:8163`. **ALIVE-ON-PAPER, ORPHANED IN PRACTICE** |
| **m003-side congruence half** | **L109, OPEN, "in-sandbox, cheap"** — `docs/OPEN_LEADS.md:637`. Never run. **ORPHANED** |
| **GATE 8R2-A Stage A (option a/b)** | **Never decided.** `frontier/B793_gate8r2a_parent_localisation/FINDINGS.md` records (a)/(b)/(c) and takes (c) ("leave blocked"). The decision was re-registered as **L112, "OPEN, ready; cheap; both instruments exist"** (`docs/OPEN_LEADS.md:640`), which explicitly says "= B793's Stage-A options a/b". `8R2` appears in no arc after B793. B878 harvested cc3's mesh-scanning solver — i.e. option (b)'s instrument is now *on main* — and the harvest never notes that it discharges Stage A. **ORPHANED, and now cheaply closable** |
| **a_π census** (Cell-2's CM/lift discriminator, ~10 primes) | Exists **only** in the verbatim relay `frontier/B878_maass_upper_window/RELAY_AS_RECEIVED.md:87,110`. Not in B878's FINDINGS, not in its `arc_verdict.json`, not in any register. **LOST** |
| **the Steil read** (Steil 1999, IMA 109 617–641; "registered source for class labels — NOT yet read") | Single occurrence repo-wide: `RELAY_AS_RECEIVED.md:88`. **LOST** |
| **parity census / J-normalization check** | Single occurrence repo-wide: `RELAY_AS_RECEIVED.md:110`. **LOST** |

Note the pattern: B878's harvest (`frontier/B878_maass_upper_window/FINDINGS.md`) took the relay's **datasets and machinery** (§1–§3) and left the relay's **§4.5 open-item list** entirely in the preserved-verbatim file. Four items dropped in one banking pass.

---

## (c) Q4 — the registers: partially fixed, and the parked campaign is still parked

`[machine-path]/docs/LEAD_REGISTER.md`:

- **Fixed, structurally.** A `views-fresh` gate now fails the build if a review doesn't touch the file (§"VIEW REFRESH — 2026-07-29 (Review 32)"), and the file carries a Review-37 state header plus Review-33/34/35/36/38 notes and a post-crossing mid-window update. It has been touched at every review since.
- **Not fixed, substantively.** The reconciliation was *appended*, not applied. The ranked table still lists **`| 1 | B399 | e₃ exact … | YES | M | HIGH |`** with the caveat text "the reconstruction sentinel is already running" — while ~100 lines below, the refresh block says **"Its top-ranked HIGH items are already closed and must not be re-computed: B399/e₃ cleared (B578-D4)…"**. A reader entering at the table gets the stale answer. Same for B201/B202/B203 and B225.
- **The transfer-operator campaign is STILL PARKED, verbatim.** `docs/LEAD_REGISTER.md:127` "## Parked lead (2026-07-10)…" is byte-unchanged, still listing **UNRUN (a)–(d)** and still saying "Revisit as its own campaign." Meanwhile `frontier/B852_parabolic_pressure/FINDINGS.md` (2026-08-02) **demonstrated that B451's instrument was structurally incapable** of the answer — analytic hyperbolic pressure, exact doubling-map control to 1.3e-15, and the Gauss/Farey pair isolating the parabolic point. **B852 is cited nowhere in LEAD_REGISTER**, and `docs/OPEN_LEADS.md:331` still carries `D4 (B451) — trace-map transfer-operator resonances … **queued**`. The parked lead's items (a)/(c) are now known-dead and the register says otherwise.
- **L72** (`docs/OPEN_LEADS.md:512`, the CS-functional/dynamics programme) was swept into B775 Wave 5 (`docs/SEAL_LEDGER.md:444,447`) and has no disposition row in OPEN_LEADS; the row still reads as an open lead.

**Verdict:** the *mechanism* problem (stale registers going untouched) was fixed by the views-fresh gate at Review 32. The *content* problem was not — reconciliation notes accumulate at the bottom while the authoritative tables above keep their stale rows, which is the same failure in a new shape.

---

## (d) Q5 — Reviews 36/37/38 on the observer thread: **silently dropped**

- **Review 36** (`docs/progress/REVIEWS.md:2760`) — no observer/B7xx item anywhere in the section.
- **Review 37** (`:2861`) — the SM-structure/First-Measurement window. §5 explicitly scopes its stale check: *"Scoped stale-check on `OPEN_LEADS` rows **adjacent to this window's results** … The full-catalog audit remains a carried item."* The word "observer" does not appear. No item is marked deferred, parked, or closed.
- **Review 38** (`:2932`) — §5: *"Stale-leads check: no OPEN_LEADS row resolved-but-unmarked."* That is a check for the opposite failure mode (closed-but-still-open). Nothing detects an **open-but-abandoned** row, which is the whole B787/L109/L111/L112/Born-content class.
- The last review to name the thread at all is Review 26 (`:1797`, R26-5 the object-level observer door). Nothing since Review 32's addendum (`:2373`) mentions it.

**Verdict: silently dropped — neither deferred nor closed.** No review since 33 names the observer programme, and the two reviews spanning the pivot both ran stale-checks whose scope excluded it by construction.

---

## (e) THE FIVE MOST CONSEQUENTIAL LOSSES

**1. The B849/B851 successor — "is B723's system BC/CMR-type for ℚ(√−3)?" — announced as running and never landed.**
This is the single question on which the entire observer construction now rests. `frontier/B851_bc_litgate/FINDINGS.md:95`: *"Test whether B723's system is BC/CMR-type for ℚ(√−3) — in-repo, and now the only thing B849's verdict rests on."* If yes, the LEVEL MISMATCH becomes **unconditional** and B723's nominated order parameter is refuted at the level of group membership — i.e. the July observer construction's central identification fails. It was folded into a six-task backlog campaign declared running on 2026-08-03 (`PROGRESS_LOG.md:9068`); **there is no `frontier/B858_*` and no post-B851 occurrence of `BC/CMR-type` on main.** The programme's most consequential open question was lost inside a one-line log announcement.

**2. LAW_MAP row 147 still asserts "THE OBSERVER IS BUILT — as a PHASE TRANSITION (B723)" with no correction pointer.**
`docs/LAW_MAP.md:147` still reads, un-caveated, "CHIRALITY + VALUES = the broken type-I low-temperature extremal phase **carrying the Gal(K^ab/K) label**" — the exact clause B849/B851 showed cannot hold, since the nominated label (complex conjugation) is not in Gal(K^ab/K). **B849, B850, B851, B852, B853 appear nowhere in `docs/LAW_MAP.md` or `docs/THEOREM_LEDGER.md`.** The refutation lives in the arcs, `docs/CAMPAIGN_STATUS.md` blurbs, and `docs/views/VERDICT_LEDGER.md:480,802` — none of which is the authoritative law register. The programme's own most-catalogued defect class (right object, wrong level) is now recorded in a place its own law map doesn't read.

**3. The Born CONTENT gap has no register row at all.**
B725–B729 banked *form yes, content open* (interference and non-uniform |amp|² weights unexplained; amplitudes ℚ(√(2+φ)), phase ℚ(ζ₅) imported as golden-MTC overlays). The named next steps ("Busch POVM-Gleason on III₁; Zurek envariance vs Haar; the full CMR/Hecke off-diagonal") survive **only in a prose column of `docs/LAW_MAP.md:148`**. There is no OPEN_LEADS row, no OPEN_PROBLEMS row, no masterplan lane, and zero citations in B854+. The most physics-facing open door the programme ever opened is not in any executable queue.

**4. B787's ι question — the rank-3/rank-4 fork — is the joint between the two "measurements", and it is closed to nobody.**
`frontier/B787_interaction_programme/FINDINGS.md` proved ι = inversion is a 4th independent involution (F₂-rank 3→4, unconditional, de-welding time's arrow from the basepoint bit) and *deliberately left open* whether ι is an observer closing. That single unanswered question is what determines whether C20's rank-3 "full discrete closing menu" and its B733 rank-saturation are theorems or artifacts of a too-small generating set. It is registered only as `docs/HINT_LEDGER.md:540` (H-B787-IOTA), a hint — and by house rule (`METHOD.md`) **math never cites hints**. Meanwhile the new window has built a second, unrelated "measurement" formalism on top of the same word. Nobody can now say whether the two measurement structures are the same object, and the one computation that would tell you is parked in a non-citable ledger.

**5. Four relay open-items dropped in a single banking pass (B878), and the GATE-8R2-A decision that was already answerable.**
`frontier/B878_maass_upper_window/RELAY_AS_RECEIVED.md` §2 and §4.5 carried the a_π census (Cell-2's CM/lift discriminator), the **Steil 1999 read** (the registered source for class labels, explicitly "NOT yet read"), the parity census, and the J-normalization check. B878's own FINDINGS and `arc_verdict.json` carry the datasets and the solver and **none of the four items**; none reached OPEN_LEADS. Compounding it: B878 harvested cc3's **mesh-scanning** Hejhal solver — which is precisely option (b) of `frontier/B793_gate8r2a_parent_localisation/FINDINGS.md`'s Stage-A decision ("methodologically **stronger** on the axis at issue — it is a detection, not a refinement") — and never noticed. Stage A has sat BLOCKED since 2026-07-28 with `L112` marked "OPEN, ready; cheap; both instruments exist" while the instrument that unblocks it landed on main on 2026-08-03. That is a loss that costs nothing to reverse and has been sitting reversible for five days.

---

### One structural note for the caller

The corpus has a **verbatim-preservation-instead-of-registration** failure mode that shows up three times independently: the relay open-items (B878), the B849 carried list, and the B787 §4 open items. In each case the *artifact* was preserved with real discipline — sealed, hashed, committed, locked — and the *forward obligation inside it* reached no register. The register discipline the owner installed this window (Review 38 §5: "the register discipline … caught three would-have-been losses") demonstrably works when applied; it has simply never been applied backwards across the B854 pivot. A single sweep of `frontier/B7*/FINDINGS.md` §"Carried forward"/"Open items" sections into `docs/OPEN_LEADS.md` would recover most of the table in (b).