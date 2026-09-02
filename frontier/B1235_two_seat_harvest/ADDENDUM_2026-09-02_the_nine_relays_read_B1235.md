# ADDENDUM (2026-09-02) — the nine recovered relays READ; E51 closes on content, not on files

**Status of E51 after this addendum: the nine files are recovered (B1235 main text) AND their
content is now accounted for on main, item by item.** The recovery was the easy half. This is the
read — every claim in the nine relays traced to where it lives on main today, or corrected, or
queued by name. Nothing is marked BANKED on a label match; each row names the file and line that
carries the content, and every correction below was re-derived on this bench before it was written.

## 1. The nine, disposed

| relay (all `CC3_TO_CC_2026-08-09_*` unless named) | disposition | where the content lives / what changed |
|---|---|---|
| `HARVEST_MANIFEST` (29 relays, 7 must-not-die + 1 open) | **READ — 6 banked, 2 corrections landed, 1 queued** | §2 below, item by item |
| `FRAMEWORK_DELTA` (six deltas to THE_FRAMEWORK) | **READ — 1 live fix landed, 2 cross-refs landed, 1 discharged, 1 partially adopted, 1 queued** | §3 below |
| `PROGRAMME_ASSEMBLY` (§3 misfiled-as-missing, §4 real gaps) | **READ** | §3 item 6 (the exotics) → fixed by B970/B978, THE_FRAMEWORK:771 now scopes L134 correctly; §3 item 3 (three generations "banked twice") is the reading the *same seat corrected one day later* in HARVEST_MANIFEST #7 — the later word wins, see §4; §4's real gaps are the standing frontier (transmission map = the crossing cell) |
| `L114_DISCHARGE` (the ι question) | **BANKED** | adjudicated on main by B1189 / GC-5 (`docs/OPEN_LEADS.md:754`) |
| `CORNERSTONE_PLAN` | **BANKED** | the plan behind B993; B993 executed it (32.8% base rate; Reid-uniqueness consumed at zero steps, `frontier/B993_cornerstone_verified/FINDINGS.md:49`) |
| `DAY_LOG` (sequence + six self-corrections) | **BANKED** | its one "still running" item, the parent eigenvalue r = 7.0720041858752050007371941867273, landed in B1021 |
| `PATH_BEYOND_THE_WALL` (five-stage bulk/boundary) | **TRIAGED (B1009 addendum, ledger row 57) — the ask to cc3 stands** | content summarized on main since 08-10; cc3 reactivated 08-28, the file is now readable again |
| `REVIVABLE_rationale` | **PARTIALLY ADOPTED — instrument queued** | the *data* exists (kill graph: 774 entries, `hatch` on 264, `revival_score ≥ 4` on 31, ≥ 3 on 84); the *practice* is standing (`docs/COMPUTE_THE_PROGRAM.md:92`: read the hatch before working a kill); a per-probe query exists (`scripts/atlas/query.py` mode 4 `revive`); the corpus-wide sealed listing cc3 proposed (a `REVIVABLE` index under docs/ (not yet written) + `--check`) was never built and B738's SHORTLIST (2026-07-21) indexes 217 of today's 774. Queued as **L195** |
| `README_ARC_PROPOSAL` ("The arc, end to end" README section; B988 step 7b) | **UNACTIONED — owner's** | README has no such section; README is outward-facing (RED by the delegation charter). Listed with the HELD main-lineage edits for the owner |

## 2. HARVEST_MANIFEST — the eight that must not die, traced

| # | item | where it lives on main | verdict |
|---|---|---|---|
| 1 | genesis F3 citation (Adams–Bergman–Ooguri–Vafa) | fixed by B998; lock `tests/test_b749_f2_f8_locks.py` | BANKED |
| 2 | B1–B5 (`frontier/B1_gluing_chern_simons` … `B5_wheeler_dewitt`) carry no `arc_verdict.json` | still true today — **verdict hole** (B2 matters most: it falsified the handoff's monodromy claim AND diagnosed why — fiber character variety vs meridian/longitude coordinates) | **QUEUED as L196** **Closed same day: L196 EXECUTED — five verdicts written, B2/B5 NEGATIVE routed into the kill graph.** |
| 3 | the weight ledger (g → k²g; 8 of 11 faces weight-0; "a shape has no size") | `frontier/B1022_functor_phase1/PHASE1_CORPUS.md:28–29` (C1) | BANKED |
| 4 | 2T base rate (~35% census / 36.4% knots) | B993 (32.8% one-cusped census), B1180 | BANKED |
| 5 | L73 falsified | `docs/OPEN_LEADS.md:1130` | BANKED |
| 6 | pin_phase | `frontier/B1007_arb_maass/_reference_double.py:565` | BANKED |
| 7 | **"three generations, structurally … banked (B897, B928)"** at `docs/THE_SM_VERDICT.md:45` and `docs/THE_FRAMEWORK.md:183` (both from B968, 2026-08-08) | **OVERCLAIM — corrected in place today (§4)** | CORRECTED |
| 7′ | charge quantisation t/3 + d/2 + Y ∈ ℤ | `docs/FALSIFIER_REGISTER.md:17` (P2) | BANKED |
| 8 | r = 7.0720041858752050007371941867273 | B1021 | BANKED |
| — | **B718 label**: `b718_probe4.py:95` calls the Neumann–Zagier constant "π²·(cusp longitude)" | it is π²·(cusp **area**) — `ADDENDUM_2026-09-02_cusp_area_not_longitude_B1235.md` in B718; check script + output in `verification/b718_cusp_area_check.{py,txt}` here | CORRECTED (label only; no value changes; line 148 is correct as written) |

## 3. FRAMEWORK_DELTA — the six, against today's `docs/THE_FRAMEWORK.md`

| Δ | the delta | state on main today | action |
|---|---|---|---|
| 1 | Layer 2 fuses two properties B727 keeps apart: "E₆-across-faces is forced (B727) — the atom being ℚ(√−3) as the unique arithmetic knot" | **still verbatim at :163**, 24 days after the fix was written | **FIXED** — dated correction beside the line: forced by the **field** (B727:54 "different objects … do not reinforce"), a commensurability-class invariant (B803:81), not by arithmetic-knot uniqueness, consumed at zero steps (B993:49) |
| 2 | Layer 3: registerability (DERIVED) forces the endpoint; maximal residual symmetry (ASSUMED) selects only the path — the confluence run, [3,2,1], six chains all → SM | **BANKED as B994** (`docs/LAW_MAP.md:330`; `frontier/B994_rule_variation/FINDINGS.md:20`); THE_FRAMEWORK:131 already cites it; the Layer 3 header at :173 still says "one principle (B861)" | dated cross-reference beside :173 |
| 3 | Layer 5: the weight argument as a second, cheaper scale mechanism | **BANKED as B1022 C1**; the Gukov mechanism has since been rebuilt three times (B1012, B1088) and "normalisation owed" is gone; C1 not cross-referenced in Layer 5 | dated cross-reference beside the Gukov paragraph |
| 4 | L134 "never addressed here" | **DISCHARGED** — :771 now reads "quantum numbers banked … the mass mechanism remains unaddressed" (B970/B978) | none |
| 5 | Layer 6: build a REVIVABLE index under docs/ (not yet written; L195 owns it) | partially adopted (§1) | L195 |
| 6 | B1–B5 verdict hole | **closed same day (L196 executed)** | L196 |

## 4. The three-generations correction (the one that changes a headline)

`docs/THE_SM_VERDICT.md:45` and `docs/THE_FRAMEWORK.md:183` say **"three generations, structurally;
D₂ carries the entire generation hierarchy | banked (B897, B928)"**. The arcs cited do not say that:

- **B897** (its own FINDINGS): *"generation-shaped … at the colour × flavour TILING level, not at the
  exact-quantum-numbers level"*; *"Mechanism-hood of generations … NOT decided"*. `docs/LAW_MAP.md:194`
  records it as **"THE SEALED GENERATION-SHAPE … mechanism-hood fenced"**; `CHANGELOG.md:6305`:
  *"Not decided: mechanism-hood (overlapping 16s ≠ replicated families) — the fence stands."*
- **B891** is the across-breakings reading itself: one 27, three SO(10) embeddings, three pairwise-
  distinguishable 16-sectors registered by a single observer. Three *sectors of one 27* — not three
  replicated families.
- **B298** PROVED the figure-eight cannot force three generations ("never 3"); **P13** (B562,
  `docs/OPEN_PROBLEMS.md:346`) tombstones the 9+9+9 reading as "the wrong 3".
- **B928** (D₂ = ±ρ₂₇(σ_{χ−})) characterizes the hierarchy's *carrier*; it does not decide
  generation mechanism-hood either.
- Swept today (THE ABSENCE RULE): nothing after B928 lifts the fence — LAW_MAP, OPEN_LEADS,
  OPEN_PROBLEMS, CAMPAIGN_STATUS. W6 in the masterplan ("becomes a mechanism or dies") closed the
  masterplan on 2026-08-18 without deciding it.

**Correction landed:** both lines now carry a dated note restating B897's own scope: *generation-
SHAPED at the tiling level; mechanism-hood fenced (B897, LAW_MAP:194); B298: the object does not
force three; B891: three sectors of one 27.* The row stays; the word "banked" is scoped to what was
banked. This is an **E53 instance** (#11): a banked *fence* never reached the two surfaces asserting
the opposite — cc3 flagged it on 2026-08-10 and the flag was lost with the file. The Layer 2
conflation (Δ1) is E53 #12 by the same shape: B727's own distinction, unpropagated for 24 days.

## 5. What this addendum does NOT do

- It does not weaken B897, B891 or B928 — it restores their scope lines to the surfaces.
- It does not build the revivable index (L195 — named, specced, queued). The B1–B5 verdicts (L196) WERE written the same day: B1/B3/B4 OPEN, B2/B5 NEGATIVE (kind-mismatch; B5 in B259-wall-#5's family, retracted B980).
- README_ARC_PROPOSAL remains the owner's (outward-facing).
- Gate 5 untouched; no measured value anywhere in this read.

## Locks

`tests/test_b1235_nine_relays_read.py` — the two flagship lines carry the dated scope note; THE_FRAMEWORK:163
carries the field/B803/B993 correction; the B718 addendum exists and names line 95 only; the
ERROR_LEDGER carries E53 #11–#12; L195/L196 exist in OPEN_LEADS.
