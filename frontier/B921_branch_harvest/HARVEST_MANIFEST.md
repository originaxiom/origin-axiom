# B921 STAGE 1 — BRANCH HARVEST MANIFEST (cc3 audit Part B)

Harvest of the load-bearing files from the cc3 audit-seat branch
`origin/audit/b775-braver-questions`, head `d8f95511` (2026-08-06,
"LAM_2 DELIVERED: 25 certified digits"). Copies live under
`frontier/B921_branch_harvest/harvested/`, preserving the branch-relative
paths. Every file below was extracted via `git show <branch>:<path>`,
verified non-empty, and sized (bytes). Four files carry SEAL_LEDGER
hashes; their verification is recorded in §2. Scrubs applied to written
copies are recorded in §3. The registration-over-preservation
enumeration (open/carried-forward items for OPEN_LEADS routing) is §4.

This is a harvest record. Nothing here is a claim; nothing to CLAIMS.md.

---

## 1. Harvested files (30), by task item

Status legend: OK = non-empty copy extracted; SEALED = sha256 verified
against docs/SEAL_LEDGER.md (§2); SCRUBBED = machine-path scrub applied
to the written copy (§3), copy no longer byte-identical to the branch
blob (deliberate, path-hygiene rule).

### (1) The loss audit — whole directory

| Branch path | Bytes | Status |
|---|---|---|
| frontier/B796_coupling_campaign/loss_audit/THE_LOSS_LEDGER.md | 7948 | OK |
| frontier/B796_coupling_campaign/loss_audit/loss_audit_branch_delta.md | 33126 | OK, SCRUBBED (2) |
| frontier/B796_coupling_campaign/loss_audit/loss_audit_general_register.md | 14551 | OK |
| frontier/B796_coupling_campaign/loss_audit/loss_audit_observer_thread.md | 20773 | OK, SCRUBBED (3) |

### (2) B796 campaign core — second-round reports, plans, context sweep

| Branch path | Bytes | Status |
|---|---|---|
| frontier/B796_coupling_campaign/harvest/second_round_cm_bost_connes.md | 18861 | OK |
| frontier/B796_coupling_campaign/harvest/second_round_born_content.md | 23989 | OK, SCRUBBED (1) |
| frontier/B796_coupling_campaign/harvest/second_round_novelty_research.md | 10875 | OK |
| frontier/B796_coupling_campaign/MASTERPLAN.md | 24977 | OK |
| frontier/B796_coupling_campaign/MASTERPLAN_FORWARD.md | 22967 | OK |
| frontier/B796_coupling_campaign/context_sweep/sweep_banked_arcs_B793_B797.md | 44121 | OK |
| frontier/B796_coupling_campaign/context_sweep/sweep_changelog_history.md | 26249 | OK |
| frontier/B796_coupling_campaign/context_sweep/sweep_error_protocol.md | 48910 | OK, SCRUBBED (8) |
| frontier/B796_coupling_campaign/context_sweep/sweep_leads_doors.md | 40434 | OK, SCRUBBED (8) |
| frontier/B796_coupling_campaign/context_sweep/sweep_status_spine.md | 26228 | OK, SCRUBBED (3) |

### (3) The Wave-1 negatives

| Branch path | Bytes | Status |
|---|---|---|
| frontier/B796_coupling_campaign/cell2_hecke_gate.py | 7114 | OK |
| frontier/B796_coupling_campaign/cell2_hecke_gate.txt | 2260 | OK |
| frontier/B796_coupling_campaign/cell3_spin_fork.py | 4159 | OK |
| frontier/B796_coupling_campaign/cell3_spin_fork.txt | 1652 | OK |

### (4) The sealed prereg chain (hash-verified, §2)

| Branch path | Bytes | Status |
|---|---|---|
| frontier/B796_coupling_campaign/WAVE1_PREREGISTRATION.md | 5034 | OK, SEALED 8424a335 |
| frontier/B796_coupling_campaign/CELL9_RUNG1_PREREGISTRATION.md | 3954 | OK, SEALED da516046 |
| frontier/B796_coupling_campaign/CELL9_RUNG1_PREREGISTRATION_v2.md | 5212 | OK, SEALED 3ba81779 |
| frontier/B796_coupling_campaign/CELL9_RUNG1_PREREGISTRATION_v3.md | 4754 | OK, SEALED 169e9042 |

### (5) The generators (outputs on main, generators branch-only)

| Branch path | Bytes | Status |
|---|---|---|
| frontier/B792_maass_m004_eigenvalues/sector_projection_test.py | 5773 | OK |
| frontier/B792_maass_m004_eigenvalues/certify_mode_count.py | 2377 | OK |
| frontier/B792_maass_m004_eigenvalues/weyl_scattering_check.py | 3530 | OK |
| frontier/B792_maass_m004_eigenvalues/length_spectrum_m003.json | 43277 | OK |

### (6) The certified-run SM header + the cell9 §16 verdicts

| Branch path | Bytes | Status |
|---|---|---|
| frontier/B792_maass_m004_eigenvalues/sm_comparison_certified.txt | 5937 | OK |
| frontier/B796_coupling_campaign/cell9_sec16_verdict.md | 8229 | OK |
| frontier/B796_coupling_campaign/cell9_sec16_verdict2.md | 12063 | OK, SCRUBBED (6) |
| frontier/B796_coupling_campaign/cell9_sec16_verdict3.md | 8898 | OK |

Note on (6): `sm_comparison_certified.txt` is the full certified-run
output; its header block (lines 1–4: "A1: certified set — 17 kept,
excluded []", the 6.90e-10 tolerance floor, the 17-eigenvalue spectral
set, the 18 B743 targets) is the certification header main lacks (main
stores the dry-run). Harvested whole to preserve the header in context.

---

## 2. Seal verification

main's docs/SEAL_LEDGER.md rows (lines 481–484, dated 2026-08-05) list
four prefix hashes for the cc3 branch prereg chain. Full sha256 digests
were computed from the branch blobs AND re-computed from the on-disk
harvested copies (identical — these four files received no scrub):

| SEAL_LEDGER prefix | File | Full sha256 | Verdict |
|---|---|---|---|
| 8424a335 | WAVE1_PREREGISTRATION.md | 8424a33545fb96c745856437d655b3df61172b3532f19a8e6355acbd41638f50 | MATCH |
| da516046 | CELL9_RUNG1_PREREGISTRATION.md | da5160461040c657708ec38fcddeff90df43199afa69e35ded4353df2b36e7fb | MATCH |
| 3ba81779 | CELL9_RUNG1_PREREGISTRATION_v2.md | 3ba817790db9c9666bf9e93cdb6bec785ea41005908984a4a1b8b00cf25e6902 | MATCH |
| 169e9042 | CELL9_RUNG1_PREREGISTRATION_v3.md | 169e90420d4fb75cc9907dd1ee6146c42a54003e33ee77e3d1db96526941f14e | MATCH |

4/4 verified. The chain's internal citations also close: verdict3
(third pass) verifies v3 = 169e9042 and v2 = 3ba81779 in its own text,
and its condition C6 (write the second-pass verdict to disk) is
satisfied on the branch by `cell9_sec16_verdict2.md` — now harvested.

---

## 3. Scrub log (written copies only)

Per the registration task's scrub rule and the repo path-hygiene rule
(no absolute machine paths in repo files), every occurrence of the
audit-seat clone's absolute filesystem prefix (the machine path of the
cc3 working tree) in the harvested copies was replaced with
`[machine-path]`, preserving the trailing repo-relative path. 31
occurrences in 7 files:

| File (harvested copy) | Occurrences scrubbed |
|---|---|
| frontier/B796_coupling_campaign/context_sweep/sweep_error_protocol.md | 8 |
| frontier/B796_coupling_campaign/context_sweep/sweep_leads_doors.md | 8 |
| frontier/B796_coupling_campaign/cell9_sec16_verdict2.md | 6 |
| frontier/B796_coupling_campaign/context_sweep/sweep_status_spine.md | 3 |
| frontier/B796_coupling_campaign/loss_audit/loss_audit_observer_thread.md | 3 |
| frontier/B796_coupling_campaign/loss_audit/loss_audit_branch_delta.md | 2 |
| frontier/B796_coupling_campaign/harvest/second_round_born_content.md | 1 |

Scrub notes:
- The four SEALED files contained no such paths and were NOT touched;
  their on-disk hashes still match the seals (§2).
- The 7 scrubbed copies are no longer byte-identical to their branch
  blobs; the branch remains the byte-exact reference until deletion.
- No name-form attribution token (assistant/vendor name, model names,
  co-author trailer, vendor e-mail) occurs anywhere in the harvested
  set — checked case-insensitively. The only case-insensitive near-hits
  are three occurrences of the physics term "anthropic measures"
  (MASTERPLAN.md:382, MASTERPLAN_FORWARD.md:266, sweep_leads_doors.md:222
  — the cosmological anthropic-measure concept in the "excluded as
  untestable" lists). These are scientific vocabulary, not attribution,
  and were left intact.
- No `[seat-tool]` replacements were needed (no tool-attribution
  strings found).

---

## 4. REGISTRATION OVER PRESERVATION — open/carried-forward items for OPEN_LEADS

Enumerated for the banking seat to route. NOT edited into OPEN_LEADS
here. Grouped by source document; each item is stated as a routable
lead. Items marked [MAIN-STATE] are register/state repairs rather than
computations.

### From THE_LOSS_LEDGER.md (Tier 1 — active damage on main)

1. [MAIN-STATE] L1: the sin²θ_W = 3/8 datum under the sealed B915
   crossing verdict is UNLOCKED — frontier/B909* does not exist. Build
   the B909 bank or re-derive + lock 3/8 standalone; until then annotate
   B915's FINDINGS.
2. [MAIN-STATE] L2: live contradiction on H-B788-NORMSPLIT (RETRACTED
   in HINT_LEDGER/B794/test_b794_congruence.py with wrong instance
   figures "12 vs 41" vs SURVIVES-at-norm-level in B878). Harvest
   trace_norm_split.* (branch: frontier/B792_maass_m004_eigenvalues/
   trace_norm_split.{py,json,txt} — NOT in this Stage-1 set) + the
   reconciliation paragraph (TRACE-level 139/37/one-odd vs NORM-level
   12/zero-odd); fix E28's instance figures + the lock.
3. [MAIN-STATE] L3: two unreconciled "measurement" definitions
   (TERMINOLOGY.md:164 fiber-functor vs :218 charge-stratification);
   LAW_MAP:147 still asserts "THE OBSERVER IS BUILT (B723)" though
   B849/B851 refuted the exact Galois-level clause. Terminology
   reconciling clause + LAW_MAP caveat; the ι adjudication is a real arc.
4. L4: the B851 §3 successor question — is B723's system BC/CMR-type
   for Q(√−3)? (announced under B858, no directory exists; the sole
   load-bearing assumption of the observer identification). The
   harvested CM/BC report carries the Q(√−3) groundwork; the test
   itself ~1–2 sessions.

### From THE_LOSS_LEDGER.md (Tier 2/3 — residue after this harvest)

5. Wave-1 Hecke follow-up (= L7, and cell2_hecke_gate.txt's own
   registered follow-up): construct the correct level-(4) Hecke
   operator for Γ₄₁ (congruence but not Γ₀-type; naive Bianchi
   double-coset normalization FAILED the sealed gate 0/10 at 5%).
   Stage 1 doublet surgery is BLOCKED until then. Bankable negative
   about main's own 43-eigenvalue dataset: level-1 lifts REFUTED via
   r_K = 2r_Q, first lift 19.067 > 13.5.
6. Cell 3 spin fork (= L7): the two spin structures of m004 are
   DISTINGUISHED by cusp data (ρ₁ trace pattern (2,−2), ρ₂ (−2,−2));
   ρ₁ is non-Lie under BOTH conventions ⇒ discrete Dirac spectrum ⇒
   spinor-Hejhal is AUTHORIZED — exactly the instrument B804 says it
   is missing. Route to the B804 lead.
7. [MAIN-STATE] L9 cheapest recovery: Gate 8R2-A closable — "both
   instruments exist" (L112 + B878's harvested mesh-scanning solver is
   option (b)); connect them.
8. [MAIN-STATE] L9 dropped forward obligations: B878 §4.5 items (a_π
   census, Steil read, parity census, J-normalization); B849's carried
   list (BC/CMR test, CS-torsion prior-art gate, the 370-geodesic
   phantom); B787 §4 items 1 and 4.
9. [MAIN-STATE] L10 ledger debts (route as one register-sweep lead):
   THEOREM_REGISTRY/LEDGER zero B8xx/B9xx rows; RETRACTIONS ≥5 missing
   rows; ROADMAP Tier-3 false; LAW_MAP five orphan rows; COMMS_PROTOCOL
   no legal name for cc3; B911 CMT draft without arc; B913 un-gated;
   8 sealed docs with post-banking commits; Born content no register
   row; transfer-operator lead parked though B852 killed its
   instrument; promotion gate 1/pass vs 8+ candidates/window.
10. L11 the paper void: named deliverables with zero drafts; the
    un-externalizable pile includes P69/P70, the sealed crossing
    negative, 21 §F laws, the 43-eigenvalue dataset (now + the branch's
    25-digit lam_2).
11. [PROCESS] The loss-audit pattern finding: nothing gates register
    COMPLETENESS against the carried-forward sections of banked
    FINDINGS; a standing sweep of "Carried forward"/"Open items"
    sections across frontier/ into OPEN_LEADS would recover most of
    Tier 3. (This Stage-1 manifest section is one instance of that rule.)

### From cell9_sec16_verdict3.md (execution-blocking conditions, rung i)

12. Conditions C2–C7 must be done before any cell9 rung-(i) run banked
    under the sealed chain: C2 non-convergence abort after itmax; C3
    self-labeling shakedown JSON; C4 correct the prereg stamp
    3ba81779→169e9042 + stale v2 docstring; C5 guard lam_1 / remove the
    --mult2 v2 pair protocol; C6 verdict2 on disk (SATISFIED on the
    branch, now harvested); C7 end-to-end shakedown log. C8 advisory
    (low-mode normalization or ‖a‖∞ bound; iteration-1 wall-clock
    checkpoint). NOTE: the branch head commit ("LAM_2 DELIVERED, 25
    certified digits, sealed PSLQ first pass CLEAN") post-dates the
    verdict; Stage 2 should audit whether C2–C7 were discharged before
    that run.
13. C1 (binding on any FUTURE rung (i-b) prereg): the D-1 clause "and
    it remains regular at multiplicity 2" is VOIDED (false at corank 2
    — any 2-dim null space contains a vector vanishing at the
    normalization coordinate); the corank-2 no-go BINDS the mult-2 pair
    protocol design.

### From MASTERPLAN_FORWARD.md (§10.8, §11)

14. The cell9 ladder as sealed: 25-digit rung → symmetrization/arb
    build → 50-digit rung; the (d,H) box seals per rung; feasibility
    MEASURED (pure-mpmath full system infeasible ~1685 h/ev; /8-
    symmetrized 3.3 h/ev; python-flint/arb installed).
15. Best case stated in advance (bank alongside any positive): a
    positive Cell 9 establishes only "the BC/CM route is not closed,"
    never an SM value — the Bianchi slot is verified empty and must
    first be built.
16. Cells 1–7 + 8A stand as standalone spectral geometry regardless of
    H0; the PAPER is a named deliverable (first computed discrete
    spectrum of m004, Hecke data, sister comparison).
17. Open ask 3: the Grunewald–Huntebrinker primary (Experiment. Math.
    5(1) 57–80, Table 3) upgrades Cell 1 from prediction-test to
    control-test and discharges the last external provenance dependency.
18. Open ask 4 (owner gate): Gate-5-SM authorization decision point
    arrives only at Cell 8 Stage B; nothing before it touches SM numbers.

### From second_round_cm_bost_connes.md

19. The verified open slot: NO Bost–Connes-type system exists on
    Bianchi groups / H³ / any hyperbolic 3-manifold (multiple targeted
    searches; structural reason: no Shimura data for GL(2) over
    imaginary quadratic on the H³ side; Maass forms lack the required
    algebraicity). A "Bianchi BC system" would be a new mathematical
    object. Nearest neighbors: Marcolli–Xu 1602.04890, LLN 0710.3452,
    Deninger's foliated systems.
20. Preregisterable in-sandbox tests T1–T6 with falsifiers: T1
    transition-count discriminant (ζ_K(β) one pole vs ζ(β)ζ(β−1) two);
    T2 level-(4) symmetry budget = ray class group mod (4) = Z/2 (same
    Z/2 as ι = θ mod-gauge and the two form classes (1,0,12),(3,0,4));
    T3 Galois action on the cusp singular modulus (j(2√−3) root of
    x² − 2835810000x + 6549518250000, splitting field Q(ζ₁₂)); T4 BC
    Hamiltonian degeneracies r(n) = Σ_{d|n}χ₋₃(d), Weyl slope π/(3√3),
    vs banked length-spectrum norm statistics; T5 the sharpest kill-
    test — Connes invariant S(M) of the observer must be III₁
    specifically (III_λ, λ<1, or III₀ excludes every known BC-type
    attachment); T6 anabelian specificity control (same-covolume
    control subgroup; bounds the claim to "attaches to its arithmetic").
21. Failure-mode registrations: no tracial KMS_β at finite β (the
    attachment can only be II₁-object = cooled dual of a type-III
    observer); BC dynamics is imported from Spec O_K, never derivable
    from m004's internal II₁ algebra; the μ₆ = 6-units regression test
    (what broke the 1997/1999 constructions) required of any in-cell
    presentation.

### From second_round_born_content.md

22. Born content is UNCLAIMED TERRITORY with four-to-five
    preregisterable finite-stage cells (SL(2,p), p = 5,7,11,13): T1
    I₂-block census (Gleason leak detector); T2 invariant-measure
    simplex vs the banked 1:φ² weights (localizes WHICH algebra the
    nativity claim is about); T3 envariance swap-availability; T4
    sub-effect-algebra Busch test (is Born content created by the
    completion?); T5 finite Takesaki interface test (does the KMS state
    restrict to the trace, with the programme's OWN automorphism —
    the θ-gauge action banked in B784).
23. One-check in-repo item: L(Γ₄₁) is a II₁ factor (knot groups icc —
    standard folklore, marked [UNVERIFIED] in the report; verify once).
24. Standing cautions to carry with any Born cell: type-I mirage
    (state finite results as "stable along the tower," never as II₁
    facts); name which additivity axiom carried any positive; Wright–
    Weigert GPT non-uniqueness; envariance circularity; 2026 arXiv
    contamination list (2602.09056, 2603.24619, 2603.06211, 2604.27125
    — abstracts only, do not bank against); priority risk if the
    interface gap is real (2604.27125 shows adjacent framings appearing).

### From second_round_novelty_research.md (corrections main is exposed to)

25. [MAIN-STATE] F_K/Ẑ for m004 EXISTS — Gukov–Manolescu 1904.06057
    computes F_K for the figure-eight as the flagship example (+ S. Park
    2004.02087, Willetts 2003.09854). Any main doc asserting "no Ẑ for
    m004" is one citation from wrong; the claim must be recast.
26. [MAIN-STATE] "No E6 T[M3]" must be recast as: T[M3,E6] exists by
    the ADE (2,0) construction but has never been made explicit or
    evaluated for ANY manifold; higher-rank Ẑ^G/F_K^G exist (Park
    1909.13002, torus knots; Murakami–Terashima 2308.04010, Seifert
    HS). The honest novelty is the INTERSECTION: exceptional gauge
    algebra AND cusped hyperbolic target.
27. [MAIN-STATE] Bianchi-IX name collision: Fan–Fathizadeh–Marcolli
    spectral-action papers (1506.06779, 1511.05321) concern the Bianchi
    classification of homogeneous cosmologies, NOT Bianchi groups
    PSL(2,O_K); citing them as prior art "on Bianchi groups" would be
    wrong.
28. Narrowed novelty statement (Claim 1) to carry: regularized
    heat-trace asymptotics on cusped hyperbolic 3-manifolds are
    established (Müller 1501.07851, Park math/0111175, Friedman
    math/0605288); the open novelty is assembling them into the
    Chamseddine–Connes spectral action for m004 — no Λ-expansion
    published for any cusped hyperbolic 3-manifold.

### From the generators + certified run (harvest items 5–6)

29. [MAIN-STATE] Main's "certified" B792 claims now have their
    generators in-repo (sector_projection_test.py,
    certify_mode_count.py, weyl_scattering_check.py — the only
    scattering-corrected completeness screen — and the m003 cutoff-6
    length spectrum). The certified-run SM header (17 kept, excluded
    [], tolerance floor 6.90e-09, 18 B743 targets, all candidates fail
    base rate) replaces main's dry-run-only record. Route: attach these
    to the B792/B743 provenance rows so "certified" is auditable on
    main.

### Not harvested in Stage 1 (registered residue for Stage 2)

30. The remaining branch-only corpus flagged by the loss audit but
    outside this stage's list: trace_norm_split.{py,json,txt} (the L2
    reconciliation instrument), the B792 scan corpus (scanA–G) that
    makes the 43 auditable, eigenvalues_final.*, the relay corpus
    (CC3_TO_CC_* / CC_TO_CC3_*, incl. the q-RETRACTION defense),
    INFORMATION_PLAN.md, CONTEXT_ENRICHMENT.md, WAVE1_FINDINGS.md,
    cell2_gate_results.json, the cell9 execution vehicle + logs
    (cell9_rung1*.py, *_v3_4.9001*.json, shakedown/rise logs,
    y080_rise_validation.txt, cell9_pslq.*), harvest/ remaining 13
    digests + critic.md, and the branch head's LAM_2 25-digit
    deliverable itself. The branch must not be deleted before Stage 2
    prices these.
