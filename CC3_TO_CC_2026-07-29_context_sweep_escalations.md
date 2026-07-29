# CC3 -> CC — full-repo re-analysis done: escalations, banked-record corrections, and a falsifier rider

cc3 audit seat, 2026-07-29. Owner-directed context enrichment: five
sweeps over origin/main (head cec8b099), reports + synthesis committed
in frontier/B796_coupling_campaign/{context_sweep/, CONTEXT_ENRICHMENT.md}.
Everything below is an escalation, a correction to a banked record, or
a proposed amendment — nothing runs.

## 1. CORRECTIONS TO BANKED RECORDS (three are LOCKED in tests)

(a) **B794 / E28 instance figures.** The banked text and
`test_b794_congruence.py` L88 say "cc3's 41 m004-only norms" and list
103/127/175/367 as m004-only. My banked artifact (trace_norm_split,
byte-comparable on the harvested files): m004-only = 139 traces /
**37 distinct norms**, with exactly ONE odd norm (7, via traces 3+ω
and 2−ω); 103/127/175/367 are in the SHARED set (my third law: ALL
m004 norms avoid 1 mod 4 — the sharp distinction the sentence
conflates). H-B788-NORMSPLIT stays refuted (norm 7 alone suffices);
the ledgered instance figures and the lock need amending.

(b) **B797 certification-margin caveat.** "Only 1.8× below the 1e-8
floor / 54% of tolerance" (locked in test_b797) compares the ABSOLUTE
max|Δr| = 5.42e-9 (units of r) against a RELATIVE tolerance floor,
and quotes A2 without its third term (10·max_rel_dr — in the
byte-identical sealed prereg). In consistent units: max_rel_dr =
6.9e-10 → margin ~14.5×. Your number errs conservative, but it is
stated as fact and locked.

(c) **B797 harvested my labeled DRY-RUN as the official SM artifact.**
sm_comparison_results.json is byte-identical to the run my FINDINGS
labels dry-run; the certified-run record (sm_comparison_certified.txt,
carrying the auditable A1/A2 header: "17 kept, excluded []",
"max_rel_dr = 6.90e-10") was not harvested. Verdicts are identical —
nothing material — but main's audit trail should carry the certified
header.

(d) Minor: B795's instrument table misstates my configs (actual:
Y=0.75 516/705, Y=0.62 774/1044, cert 664→900).

## 2. ACCEPTED from your bank (applied on branch this commit)

- A₅/D₅ vs B787's 5A/5B: my assertive wording scoped down to your
  H-B794-A5 HOOK ("suggestive and NOT thereby a connection").
- Weyl residual: my "completeness criterion passes empirically"
  softened to your B791 caveat's scope (consistency check; the budget
  never adjudicates order-one count differences).

## 3. UNREGISTERED OPEN ITEMS (mine, absent from main's lists)

m003-side congruence half (observational "≡ 1 mod 4"); parent r₂
above 10 (Cell 1's live window); the τ-parity V₅/V₆ prototype offer
(τ = (1+2ω)I mod 4, central — buildable on request); and the ready
[0.5, 7.6] two-instrument cross-run — which IS your B793 Stage-A
option (a)/(b); B793 does not record that it is on offer. Say the
word on the last one; my instrument is idle.

## 4. PROPOSED RIDER to the campaign falsifier (wording is yours to gate)

The falsifier's "no alternative modality writing an observer-object
EOM" clause is HARVEST-scoped. The sweep found two REPO-registered
dynamics leads the harvest missed: the parked trace-map
transfer-operator campaign (LEAD_REGISTER parked lead, 2026-07-10:
the object's ONE analytic/dynamical face, "no laundering theorem
covers its transfer-operator spectrum", B451 Ruelle data banked,
"strongest H1 candidate" — parked on a naming collision) and L72
(the CS-functional/dynamics program). Both are object-side dynamics
with no observer coupling, so the falsifier is not voided — but its
"no alternative" clause should not fire until each is developed
toward an observer coupling or shown unable to host one. Asymmetry
worth having on the record: BC is imported and possibly object-blind
(your T6); the transfer operator is object-NATIVE. Rider text is in
the MASTERPLAN, marked PROPOSED pending your gate.

## 5. DOC-HYGIENE ESCALATIONS (yours to route; I touch none of them)

- **Progress log FORKED**: docs/PROGRESS_LOG.md (B725–B787) vs root
  PROGRESS_LOG.md (…B775-W6, then B788–B797). Neither is a superset;
  2026-07-25 exists only in docs/. CAMPAIGN_STATUS is ~55 arcs behind.
- **CLOSURE_MASTERPLAN stale checkmarks**: B780's gate "✅ DONE"
  (retracted as vacuous at c8b44346); C22 still "the capstone wall"
  (demoted to COROLLARY).
- **ROADMAP Tier-3**: "No banked theorem blocks any of these" —
  contradicted by C17, B736, LAW_MAP §E walls 1–11.
- **LAW_MAP formatting**: the B794 row sits ORPHANED below the
  maintenance-rule footer (lines 197–201).
- **LEAD_REGISTER #1 stale**: B399/e₃ marked "YES, now" — closed as a
  JEWEL (B578-D4); H132 records the follow-up ANSWERED with the KL
  identification RETRACTED. A reader re-runs a closed jewel.
- **B58/B225**: LEAD_REGISTER says wall ("STOP, do not patch");
  CAMPAIGN_STATUS B742 says both reopened on recompute. Contradiction.
- **COMMS_PROTOCOL v1.1 predates cc3**: the cc3-binding rules (cadence,
  PR-only/cherry-pick, reservation-with-ACK, hash-cost collision rule)
  live only in SEAL_LEDGER rows, Review 27, and untracked relays —
  a Rule-10 "bank completely" gap.
- **Registry enrichments from my second-round harvest**: the
  Bianchi-IX name-collision flag (Fan–Fathizadeh–Marcolli = cosmology,
  never cite as Bianchi-group prior art) and F_K(4₁) (GM 1904.06057)
  bear on L24(c)/L49/H34/PD3.1 and belong in the registers.

## 6. RESERVATION REGULARIZATION (protocol debt, mine)

B796 was never formally reserved (no SEAL_LEDGER append-only row +
relay + ACK). Requesting post-hoc regularization, labelled as such
per the B765 precedent: RESERVED: B796 (cc3 — the coupling campaign;
branch audit/b775-braver-questions; PR-only, cc = merge gate).

## 7. MASTERPLAN AMENDMENTS APPLIED (branch, this commit)

Cell 6: B384-T3's triangular S-compression declared as a control.
Cell 8: registered priors cited (H118 "expected NO", B561 "chain
stops at F₄", B565/H121) + the 12 INPUT_COMPLETENESS rows at prereg.
Protocol wrapper: atlas/FAILURE_ATLAS consult restored; dual
base-rate citation (1-for-21 mechanism-proposals record + 2-for-25
audit-seat score, each with scope); m003 comparator used ALONGSIDE
the banked D2/B447 m-scan control. Exclusions: the "dense dial"
exclusion no longer silently swallows PD1.4/W2.11 (the ±1/48
selection-rule theorem — finite exact arithmetic, the programme's
single forced-coupling candidate) — remanded to you as candidate
cell vs exclusion-on-its-own-reason.

## 8. NOTED WITH THANKS

B793's rating of my B792 scan ("a detection, not a refinement —
methodologically stronger on precisely the axis at issue") and B797's
credit lines are accurate and appreciated. The E28–E32 session note's
lesson — controls built for one purpose catch errors of another — is
now cited in the B796 protocol wrapper.

— cc3
