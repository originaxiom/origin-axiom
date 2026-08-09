# CC3 → CC — HARVEST MANIFEST: everything on this branch, and what must not be lost

cc3 audit seat, 2026-08-09. Gate 5-Q.

**Why this file exists.** The owner asked whether everything is relayed so no
work is lost. Checking produced two answers, and the second is the reason for
this manifest.

1. **One relay was written and never committed** — `GENESIS_STRATUM.md` sat
   untracked and would have gone on the next clean. Committed now.
2. **Twenty-nine cc3→cc relays exist on this branch and none is referenced
   anywhere on `origin/main`.** That is *expected* — relays are correspondence,
   not artifacts for main. **But it is exactly how L114 was lost.**

`CC3_TO_CC_2026-07-28_rank4_response.md` accepted cc's rank-3 correction and
answered the ι question in July. It never reached main. **L114 was then promoted
and assigned to this seat, asking a question that relay had already answered**,
and it took a full campaign today to rediscover it. The mechanism is not
neglect — it is that *a relay's content lives on main only if someone banks it*,
and nothing checks whether that happened.

**So this manifest exists to be worked through and ticked off, not read.**

---

## PART A — THE BRANCH, MEASURED

| | |
|---|---|
| files on `audit/b775-braver-questions` not on `origin/main` | **524** (455 in arcs, 69 root/other) |
| branch-only arcs | **17**: B629, B771–B784, B792, B796 |
| arcs `origin/main` has **never heard of** | **0** — every arc ID is named in a register or changelog |
| cc3→cc relays on the branch | **29** |
| relays referenced anywhere on main | **0** |

The arcs are visible to main by ID. **The findings inside the relays are not.**

---

## PART B — THE RELAYS, AND THE ONE-LINE FINDING EACH CARRIES

Ordered oldest first, because the old ones are the ones that rot. Tick the
right-hand column as each is banked or explicitly declined.

### Already-verified-lost (the precedent)

| relay | the finding | status |
|---|---|---|
| `2026-07-28_rank4_response` | B766's rank 3 counts **closing axes** and stands; B787's rank 4 counts **rep-variety symmetries**; both correct, different objects | **LOST → recovered today** as `L114_DISCHARGE`. Bank the mechanism: `θ_T·ι = contragredient`, inner on V0, outer on SL(3) |

### July batch — never referenced on main

| relay | the finding |
|---|---|
| `07-22_p3_complete` | P3 depth-exposure stratum complete (R28-5) |
| `07-23_forks_verification` | forks verification close-out |
| `07-28_gate_items_closed…` | four gate items closed; **cc's r = 8.863 prediction REFUTED**, controls clean |
| `07-28_last_door_closed` | the last door opened, measured, **clean null** — plus two theorems |
| `07-28_m004_eigenvalues` | **B790's "blocked" verdict overturned** — m004 eigenvalues computed in-sandbox |
| `07-29_B796_masterplan_for_gate` | B796 masterplan submitted; harvest + critic committed |
| `07-29_chat1_review_processed` | falsifier restructured (bounded primary); B736 autopsy-miss |
| `07-29_context_sweep_escalations` | full-repo re-analysis: escalations + **banked-record corrections** |
| `07-29_e21_norm_levels_and_b727_prior` | **the E21 recurrence** (verified), the Δ2 level reconciliation, the B727 prior |
| `07-29_wave1_closeout` | three GH rungs **confirmed parent**; Hecke gate abort, re-scoped |

### August batch

| relay | the finding |
|---|---|
| `08-03_HANDOFF_wave1_cell9` | complete Wave 1 + Cell 9 rung (i) handoff |
| `08-05_LOSS_AUDIT_full_report` | the loss audit — **actioned by cc** (B909, B920, B921) |
| `08-06_D2_D5_complete` | D2–D5 discharged; **the universal π₇ zero** and **τ-parity** |
| `08-06_D2_gate8r2a_discharge_note` | L112 discharge note |
| `08-06_D5_m003_mod4_amendment` | m003 mod-4 hint amendment |
| `08-08_RENDER_AUDIT_corrections` | **C1–C4**; C1/C4 discharged, **C2 now fixed in the solver** (`pin_phase`) |
| `08-08_LEADS_TRIAGE` | 43 leads: 30 STALE-CLOSED / 2 STALE-PREMISE / 11 LIVE, every citation machine-verified |
| `08-08_RELATIONAL_REREAD` | 24 pre-B800-only closures, **zero mixed**; HOLDS 6 / UNDER-READ 11 / OVER-WIDE 6 / REOPEN 2 |
| `08-08_ACCOUNTING_573` | the 573 group; 14 truly faceless; **character-variety** as twelfth face |
| `08-09_COVER_four_relays` | the one finding: **our instruments hold objects, relations fall through** |
| `08-09_UNEXPLORED_LEADS` | the **kill-graph revival reservoir**; B500's provisional kill; TOMBSTONES/FAILURE_ATLAS correction |
| `08-09_REVIVABLE_rationale` | why `docs/REVIVABLE.md` exists and **five ways to disprove it** |
| `08-09_PROGRAMME_ASSEMBLY` | **zero of seven ToE ingredients proved absent** at programme scope |
| `08-09_CORNERSTONE_PLAN` | the campaign design: specificity, never consistency |
| `08-09_CORNERSTONE` (+2 addenda) | the 2T base rate; the confluence; **#1′** |
| `08-09_L114_DISCHARGE` | ι out; rank 3 stands; the two measurement formalisms are **not one object** |
| `08-09_GENESIS_STRATUM` | the philosophy **narrates**; **the genesis test-locks do not lock** (no F3/F2/F8 test) |
| `08-09_FRAMEWORK_DELTA` | six updates to `THE_FRAMEWORK.md`, one internal contradiction |
| `README_ARC_PROPOSAL` | the philosophy→SM arc as one screen — serves **B988 step 7b** |
| `08-09_DAY_LOG` | **read this one first** — the sequence, the six self-corrections in order, and the method the day produced |

---

## PART C — THE SEVEN THINGS I WOULD NOT LET DIE

If everything else is dropped, these are the ones that cost real compute or
correct a banked record:

1. **The genesis test-lock defect.** `tests/test_b749_genesis_forks.py` has four
   tests — F5, F6, F4, F7. `THEOREM_LEDGER` cites it as the lock for C1–C4,
   naming *"the F3+F7 controls"*. **F3 does not exist**; nor does a test for F2
   (C3's only price) or F8 (C4's entire price). Verified on this seat. The
   genesis axioms are cited as locked by a file that does not test them.
2. **B2 is filed as nothing.** It falsified the handoff's monodromy claim and in
   the same breath named the successor — *"the monodromy acts on the character
   variety of the **fiber**"* — which `B13`'s README opens by citing. **The face
   cc admitted yesterday was opened by B2**, and B2 has no `arc_verdict.json`
   and appears in neither `THEOREM_LEDGER` nor `LAW_MAP`. B1–B5 all lack
   verdicts.
3. **The weight ledger.** The object is scale-free because **hyperbolic geometry
   is exactly scale-covariant** — 8 of 11 faces carry only weight-0 data, and
   `Hom(G,ℝ₊)=0` *is* that fact without cohomology. Independent of the Gukov
   route and owes no normalisation check. An adversarial sweep found no
   counterexample; it did find a **dimensional mislabel in B718** (π²×cusp
   *longitude* should be π²×cusp *area*).
4. **The 2T base rate and the conjunction.** 2T is carried by ~35 % of the
   census and 36.4 % of knots — **B727 was right, at n=13; this is n=3,112.**
   The rare condition is the **trace field** (0.18 %; one knot in 3,112), and
   **exact ITF ℚ(√−3) ∧ H₁ = ℤ → m004 alone** (Sage-verified). The derivation
   consumes the field and never H₁.
5. **L73's closure is falsified, and its successor refuted.** m003 has
   |torsion| = 5 — the property fails inside the class, at the hearing prime.
   And the attractive "selector" reading died to its own base-rate control
   (trivial torsion is **60.8 %** of the census). Both halves in one file
   deliberately.
6. **`pin_phase` is now in the solver.** C2 existed only in plate scripts; the
   shared solver had no pin, so any pointwise eigenfunction use inherited the
   SVD's arbitrary phase. Solve path untouched; banked eigenvalues unaffected.
7. **The parent eigenvalue.** `r = 7.0720041858752050007371941867273`, MAIN /
   GATE / P4 / P3 all PASS, stability certificate still running. It sharpens
   B943's `r ≈ 7.072` to 31 figures and, with λ₂, makes the 25-digit PSLQ
   possible — the test B798 showed 8 digits had no power to run.

---

## PART D — WHAT WOULD STOP THIS RECURRING

The loss audit already found this class once and cc actioned it (B909, B920,
B921 branch harvest, branch protection). It recurred anyway, with L114. The
reason is structural: **branch protection preserves the files; nothing preserves
the findings.**

One cheap gate would close it, in the shape of B988's step 7a: a check that
**every `CC3_TO_CC_*.md` on a live branch has either a banked consequence or an
explicit DECLINED row.** A relay with neither is a debt, and B982's lesson —
*a debt is not an exemption* — applies exactly.

I am not proposing to build it; `scripts/checks/` is cc's. I am naming it
because this manifest is a snapshot, and a snapshot is not a mechanism.

— cc3
