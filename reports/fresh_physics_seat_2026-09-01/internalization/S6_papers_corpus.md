# S6 — THE PAPERS CORPUS (internalization sweep digest)

Seat: internalization sweep reader · Date: 2026-09-01 · Scope: everything under `papers/` not
already read in full by the evaluating seat (excluded as already-read: PORTFOLIO_2026-08-27.md,
P3_THE_PAPER/main.tex + SPEC.md + CLAIM_CANDIDATES.md, FALSIFIABILITY_MATRIX.md, flagship/README.md).
I digest and flag only; the evaluating seat adjudicates.

## COVERAGE MODULUS (exact)

**Read in full:** P4_markov_stage/{DRAFT_v8.md head+abstract+§1 opening+§6 tail+both appendices,
PANEL_v1_ADJUDICATION.md, PANEL_v2.md, PANEL_v2_FINAL.md, LIT_GATE.md (first 40 lines = both
completed hunts), CLAIMS.md, OUTLINE.md}; all ten flagship/sections/*.tex + main.tex preamble;
SCRUTINY_P1P3.md, SCRUTINY_P1P3_round2.md, SCRUTINY_P1P3_round3.md (complete);
REVIEW_VERDICT_2026-07-05.md (first 60 lines = verdict + all 8 fix items + start of novelty section);
THE_MAP_of_the_object.md (lines 1–75 incl. full layer table and "root"/descent diagram; the
"what the paper can honestly claim" tail partially, via preview); P3_THE_PAPER/
TERMINALITY_SECTION_CANDIDATE.md (status header); sl4_dehn_filling/README.md; papers/README.md;
PAPERS_CAMPAIGN.md, FLAGSHIP_CAMPAIGN.md, REPRODUCIBILITY_LEDGER.md, REVIEWABILITY_INDEX.md,
VALIDATION_WORKFLOW.md, ARTIFACT_MANIFEST.md, CANDIDATES.md, PAPER_PORTFOLIO_2026-07-12.md,
SPECIALIST_NOTE_R1_held_breath.md, SLN_FIGURE_EIGHT_SKELETON.md heads (~20 lines each, headers +
governing content).

**Read as header + abstract/intro only (~25–45 lines each):** P1_seam_form/DRAFT_v4.md + CLAIMS.md
(full); P1_value_theory/PAPER.md + ABSTRACT.md; P2_trinity/PAPER.md + ABSTRACT.md;
P2_inversion_law/DRAFT_v3.md; P3_forcing_chain_residue/DRAFT_v4.md; P5_monoid/DRAFT_v1.md +
PHASE3_VERDICT.md (first 40 lines incl. the decisive BGJ table); drafts/PC23–PC26 PAPER.md
abstracts + PC26/ABSTRACT.md; candidates PC02/PC04/PC06/PC07/PC11/PC12/PC27 PAPER_CARDs +
PC27 PAPER.md §1; dark_hyperbola_letter/ABSTRACT_DRAFT.md; metallic_one_object/{README, PAPER head,
SYNTHESIS head}; metallic_trace_map_note/README; omega_strict_full_note/README;
structure_paper/{ABSTRACT_DRAFT, SKELETON heads}.

**Sampled / skimmed:** VALIDATION_LEDGER.md (scope header + entries V1–V3 of ~238; the rest is a
uniform per-probe table through V238, NOT read row-by-row); PANEL_v1_findings.md (first 25 lines of
406 — raw pre-adjudication findings, superseded by PANEL_v1_ADJUDICATION which I read in full);
tex/*.tex (title + freeze-header grep only, to verify the FROZEN notices propagated to the renders);
preview/preview.tex (preamble only).

**NOT read (silently truncating nothing — declared):** superseded draft versions P4 DRAFT_v1–v7,
P1_seam_form v1–v3, P2_inversion_law v1–v2, P3_forcing_chain_residue v1–v3 (headers/first-5-lines
only — each header states what its successor changed); the middle 480 lines of P4 DRAFT_v8 body
(theorem statements; claim structure captured via CLAIMS.md + panels + appendices); bodies of
P1_value_theory/PAPER (355 lines), P2_trinity/PAPER (275), PC23–PC27 bodies past intro, PC26 §§3–9;
sl4_dehn_filling/sections/*.tex; P5_monoid OUTLINE/PHASE0/PHASE1; P2_trinity+P1_value_theory
OUTLINE/THEOREMS; candidates' REVIEW_PACKET/VALIDATION_BRIEF/CHECKLIST files (PC02/PC11/PC12);
metallic_one_object PAPER_PLAN/ARITHMETIC_SELECTION and bodies; NOTE.md bodies of the two note dirs;
figure-generation scripts; the four tex/ PDFs and flagship/sl4 PDFs (sources checked instead);
paper_p4.html; gen_tex.py/md2tex.py/render_paper.py bodies.

---

## PER-ARTIFACT DIGESTS

### P4_markov_stage/ (the July arXiv-candidate)
- **DRAFT_v8.md** — "The parabolic locus of the metallic family: Cohn's stage, principal breathers,
  and the commutators of quantized cat maps" (2026-07-08, "final"). Self-status: all gates closed
  (verified · lit-gated · two panel rounds · reproduced); "the arXiv-candidate draft"; awaiting only
  the owner's voice revision. Core results: tr[A_m,A_n] = 2 − (mn(m−n))² (a generic symmetric-pair
  identity, honestly demoted; the metallic content is M₁₂−M₂₁ = mn(m−n)); (1,2) the unique parabolic
  pair = Cohn's modular torus / Reutenauer's Markoff morphism; breathable traces = metallic traces
  with A_m the principal breather (class-number-one specialization of Latimer–MacDuffee/Sarnak);
  the level-15 Weil-shadow quantum tables (Q₈ × SL(2,5), order 960; closure address (2,3) minimal
  non-central; the 36-cell divisor-lattice master table). Appendix B is a full corrections ledger.
  Staleness vs board: **consistent** — PORTFOLIO_2026-08-27 line 53 confirms it as "THE ONE
  ARXIV-CANDIDATE in papers/", held owner-gated, remapped as a P3-satellite worked-instance.
- **PANEL_v1_ADJUDICATION.md / PANEL_v1_findings.md** — round-1 panel (5 seats): 2 banked errors
  (Theorem E′ false in generality; "family = breathability locus" false), Theorem A deflated to the
  symmetric-pair identity, the Hannay–Berry lit gap, PSLQ "certificate" overclaim. All verified
  before acceptance; findings file is the raw pre-adjudication record.
- **PANEL_v2.md / PANEL_v2_FINAL.md** — round 2 partial then complete. Structure seat caught two v4
  math errors ((2,3)-minimality false as printed — (1,6) closes via central A₂⁶; misprinted E″
  witness word). Final round: NO FATAL; the load-bearing lever is the **level-15 collision**
  ((A₁₆,A₁₇) ≡ (A₁,A₂) mod 15 → §4 blind to parabolicity, reframed as "Weil shadow"); "240 = 4·60"
  curiosity was manufactured (real image order 960); F(ii)'s Appleby step false but the theorem true
  via genuine-rep center faithfulness; OP-3 constants unreproducible at 18 printed digits (spurious
  PSLQ relation verified); several novelty demotions (h⁺-equivalence a tautology; Theorem G a worked
  N=15 instance). All fixed in v6.
- **LIT_GATE.md** — both rounds complete; Kurlberg–Rudnick Cor. 6 has the 'if' direction verbatim;
  Howe's |χ|² = #Fix explains all 25 magnitudes (gate-gifted upgrade); Cohen even functions + Serre
  ℚ-classes give the one-line divisor-lattice proof. Honest "ours" list scoped.
- **CLAIMS.md / OUTLINE.md** — 13-row claims inventory with bank/reproducer/lock columns; outline of
  v1 architecture. Consistent with v8.
- **DRAFT_v1–v7** — superseded chain; each header narrates its delta. Historical only.

### flagship/ (the integrative preprint, sections read in full)
Proof-status-badged whole-repo exposition (PROVED/SYMBOLIC-EXACT/NUMERICAL/STRUCTURAL/KNOWN/GATED/
POSTULATED). §1 firewall + "architecture, not furniture". §2 metallic bundles. §3 κ = Fricke–Vogt
identification. §4 Dickson tower proved n ≤ 4, sharp wall at n ≥ 5 (forced spectral degeneracy).
§5 the one GATED headline: SL(4) figure-eight L = −M⁴, complete on the irreducible locus (Burnside,
validated against the invalid Schur-commutant shortcut), family L = (−1)^{n−1}Mⁿ conjectural beyond
n = 4, novelty explicitly NOT closed ("AI-assisted read de-risks, does not close"). §6 cyclic-
palindrome amphichirality criterion (corollary of GHH 2008) + the refuted "arithmetic ⇒ amphichiral"
shortcut (ℚ(√−7) chiral arithmetic pair). §7 bridge (𝒩=2* class-S S-duality = the same trace-map
action; FORCED) and wall (complex volume dimensionless; scale-carrier CS = 0 for 4₁), plus the
"seam" reading (open object; closing is where symmetry breaks) marked POSTULATED. §8 proper name:
metallic-mean Schrödinger cocycle; six-wall obstruction map. §9 three open problems + method.
Status vs board: the flagship's wall/bridge/no-selector stance is **compatible with** B1225 (selector
impossibility proved) and B1226–B1228; note however §7's seam Proposition asserts "Every generic
filling is chiral (CS ∉ {0,½})" and leans on the CS/chirality nexus that **B1226 corrected at the
family level** (B1012's blind-to-k ⟺ CS=0 ⟺ amphichiral refuted; m003/m135/m207 amphichiral with
CS = ¼, m208 chiral with CS = 0) — see RED FLAGS. The flagship also still names "the E₆/ℚ(√−3)
arithmetic … lost on closing" in pre-B1228/B1232 terms.

### sl4_dehn_filling/ (PC13 narrow note)
README carries a binding **SUPERSEDED (2026-06-15)** header: the "component" framing is refuted —
{1,1,ω,ω²} is not rigid, the family is a codimension-1 **slice**; honest result is the
rank-stratified degeneration (B153); note "to be rewritten to the B153 thesis before any external
use". The flagship's §5 (later) still says "the principal Dehn-filling **component**" while its
completeness theorem is scoped to the fixed spectrum — a wording tension a referee would press
(see RED FLAGS).

### The frozen July trio + older generation
- **P1_seam_form/DRAFT_v4.md** (+CLAIMS.md, v1–v3) — the seam form (Galois projection of
  tr(Par·P_a·Q_b) @15; 30 values; broken subfield lattice with ℚ(√−15) deleted; 70-dark).
  **⚠ FROZEN 2026-07-09 as internal note** after three re-panel rounds; "do not circulate."
- **P2_inversion_law/DRAFT_v3.md** — Dehn-surgery collision laundering / "≤ one bit" residue.
  **FROZEN**; the "≤ one bit" law flagged partly tautological by round 3.
- **P3_forcing_chain_residue/DRAFT_v4.md** — the three orientation invariants (constant norm;
  level-alternating parity; three-valued −μ₃ word-determinant) + held-breath torsion fields
  (d=3 → ℚ(√−7); d=5 → degree-4 over ℚ with subfield ℚ(√5)). **FROZEN**; residual defects named.
- **SCRUTINY_P1P3.md / _round2 / _round3** — the three-round record: round 1 (two FATALs in P2:
  wrong trace field ℚ(√5) vs ℚ(√−3); false uniform orientation law); round 2 (14 defects incl. a
  **banked** error, B479's ℚ(√41) field, corrected in the registry; the "true fact one level too
  strong" pattern); round 3 (16 defects, ≥5 freshly manufactured by the fixes; verdict "solo
  iteration is not converging — freeze; I verify numbers reliably and prose statements
  unreliably"). Exemplary honesty artifact; all three consistent with the freeze headers.
- **P1_value_theory/ + P2_trinity/** — the OLDER (2026-07-05-era) "Paper 1 & 2". Both carry
  inline STATUS blocks: **NOT submittable** (P1: novelty largely unestablished — the seam is a
  discrete Wigner function, value theory is the KR matrix-element program; honest destination a
  short computational note conditional on Theorem 6 novelty. P2: no new theorem — expository
  survey or a short "two E₆ torsions" note if a specialist confirms the pairing; the "two
  discriminants 5 and −3" pairing is asymmetric). Matches REVIEW_VERDICT.
- **REVIEW_VERDICT_2026-07-05.md** — the four-reviewer verdict behind those statuses: all 8
  sampled claims recompute exactly, ~103 locks green, but one real arithmetic error found+fixed
  ("disc ℚ(√5) = −5"), conjecture-stated-as-theorem (P1 Thm 6), entropy 4logφ vs 2logφ conflation,
  "machine-verified" overstated (mostly regression guards, not live recomputes), physics vestiges
  to cut. Honest, still-accurate historical record.
- **P5_monoid/** — **WITHDRAWN 2026-08-01**: the core (End(F₂) monoid, transformation polynomial,
  classification) is Baake–Grimm–Joseph 1993 / Peyrière 1991, verified from the source PDF; BGJ's
  classification is finer; 7 fatals total incl. Q2's evidence cell reporting a null for a predicate
  the script never evaluates. PHASE3_VERDICT also names the gate-execution failure honestly ("the
  gate named the right person; I asked the wrong question"). Draft kept uncorrected for the record,
  clearly headed. Clean.

### Registry / process files
- **papers/README.md** — points to PORTFOLIO_2026-08-27 as canonical; registry rules ("paper
  candidate ≠ proven claim"). Current.
- **PAPERS_CAMPAIGN.md** (B475 charter) & **FLAGSHIP_CAMPAIGN.md** (2026-07-04) — the two campaign
  charters (readiness definition; F1–F6 phases). Historical; superseded operationally by the
  2026-08-27 portfolio but not contradicted by it.
- **CANDIDATES.md / REVIEWABILITY_INDEX.md / VALIDATION_WORKFLOW.md / ARTIFACT_MANIFEST.md** —
  registry scaffolding; REVIEWABILITY_INDEX's ranked scrutiny package (40a1 curve; SL(4) L=−M⁴ "as
  a single instance, NOT a family"; two E₆ torsions) is consistent with later dispositions.
- **VALIDATION_LEDGER.md** — per-probe validations through V238 (~B300, 2026-06-29); scope header
  explicitly declares it not backfilled past B300. Sampled entries (V1–V3, PC12 literature screen
  STANDARD_REPACKAGE etc.) match the PC12 card. Honest about its own staleness.
- **REPRODUCIBILITY_LEDGER.md** — 74/74 locks green (2026-07-04) for old Papers 1&2 theorems; note
  REVIEW_VERDICT's later caveat that most locks are regression guards, not live recomputes.
- **PAPER_PORTFOLIO_2026-07-12.md** — the earlier honest ranking (Tier 1: PC22 dark-hyperbola;
  gate resolved Prasad-adjacent). Superseded by the 2026-08-27 portfolio; consistent lineage.
- **THE_MAP_of_the_object.md** (2026-07-09) — the dictionary map (σ → everything), with the
  honest square/half subtlety and a 14-row layer table labeled CLASSICAL/ASSEMBLY/NOVEL-GATED/
  PROGRAM; row 12 records the SM/anyon readings **killed and firewalled (B483/B484)**. Good; the
  candidate spine for the synthesis paper, superseded in role by the portfolio's P3 blueprint.
- **SPECIALIST_NOTE_R1_held_breath.md** — a single precise question for a character-variety
  dynamicist on the held-breath field law (post-round-2-corrected form). Current as far as it goes.
- **SLN_FIGURE_EIGHT_SKELETON.md** — Phase-E internal skeleton of the SL(n) content; predecessor
  of the flagship/sl4 material. Historical.
- **P3_THE_PAPER/TERMINALITY_SECTION_CANDIDATE.md** — placed 2026-09-01 by the owner's T5/T4
  election; explicitly PENDING the G1 su(3)+g2 descent cell (part (ii) quantifier restricted to
  regular-maximal menus until G1 runs). Fresh, correctly fenced, adoption owner-only.

### candidates/ (PC cards)
- **PC02** (conditional uniqueness, A1–A7 ⇒ A=LR) — NEEDS_VALIDATION; card openly states "substrate
  and order are inserted, not derived". Early-era; the frame predates the B1168/B1225 typing.
- **PC04** (noncommutative residue), **PC06** (quantum selector bridge — card admits "the selector
  theorem is missing"; note B1225 has since PROVED no symmetry-read selector can exist, which
  supersedes PC06's hope in its original form — flag), **PC07** (Möbius-flow potential) — seeds.
- **PC11 / PC12** — computational-report candidates; PC12 marked STANDARD_REPACKAGE by its own
  literature screen with one elementary apparently-new bit. Honest.
- **PC27** ("One Arithmetic Knot", the honest capstone) — DRAFTABLE; methods/negative-result paper:
  the forced ℚ(√−3) core, the base-rate firewall, two computed closing negatives ("the framework
  reduces zero Standard-Model parameters"). Its observer-coupling thesis is the direct ancestor of
  the board's current typing discipline; broadly compatible with B1225/B1226, though its "V₄
  measurement torsor / Born-content ledger" wording predates the B1231 identification ledger and
  the B1232 three-column typing (would need a re-read before use).
- **dark_hyperbola_letter (PC22)** — CC header 2026-07-12: all three theorems PROVED in-repo; gate
  resolved APPEARS-NOVEL-as-explicit-congruence but Prasad-2009-adjacent; two mandatory framing
  corrections recorded ("proof of infinitude of primes" → "restatement of Euler"). Well-fenced.

### drafts/ (PC23–PC26)
- **PC23** (degree-4 gap labels, ℤ[τ], τ=√φ; photonic test) — per portfolio: gate CLEARED,
  checker 7/7, READY-minus. The strongest PC candidate. No board conflict seen at abstract level.
- **PC24** (the 3/2 law escalator tower) — lit-gate PASSED, READY-minus.
- **PC25** (E₆ → F₄ amphichiral fold; termination; no real form) — gate CLEARED (P11), READY-minus,
  target LMP. Pure math at the E₆-attachment; but see RED FLAGS on the E₆ chain's post-B1228/B1232
  context.
- **PC26** (chirality / θ-odd sector "and Its Listeners"; hearing law, closure theorem, listener
  amplitudes incl. 1/(2φ)+i·sin(2π/5)/√5) — v2, **HELD / GATED-ON-VERIFICATION** per portfolio
  (gate fired positive twice). Its listener framing is the item most exposed to B1231 (see flags).

### Other note dirs
- **metallic_one_object/** — SYNTHESIS (2026-06-24, no novelty claimed; credits Cantat 2009 for
  unifying three of the four faces — the novelty audit working) and PAPER.md (2026-06-28, "From a
  minimal self-referential object to a unique superconformal anyon chain") — the latter has **no
  supersession header** despite the SM/anyon readings having been killed/firewalled (B483/B484,
  recorded in THE_MAP row 12). See RED FLAGS.
- **metallic_trace_map_note/ (PC17)**, **omega_strict_full_note/ (PC18)** — specialist-facing
  consolidation notes, NEEDS_VALIDATION, honest risk statements. Dormant.
- **structure_paper/** — skeleton of "The measurement cascade of the figure-eight knot's E₆";
  portfolio: "superseded in spirit by the portfolio's P3 blueprint; keep as scaffold." Header does
  not itself say superseded (portfolio does). Minor.
- **tex/** — LaTeX/PDF renders of P1_seam_form, P2_inversion_law, P3_forcing_chain_residue,
  P4. Verified: the three frozen papers' renders DO carry the FROZEN titles/headers (regenerated
  Sep 1). Note SCRUTINY round 1 states errors "are in the LaTeX PDFs **already sent**" — an
  external-distribution fact the evaluating seat may want on record.
- **preview/** — a two-paper preview working draft (old Papers 1&2 era). Historical.
- **map_figures/, flagship/figures/, sl4_dehn_filling/figures/** — deterministic figure
  generators + outputs; not audited.

---

## RED FLAGS (for the evaluating seat to adjudicate — none graded here)

1. **[stale-vs-board, category (b)/(c)] PC26's listener frame vs B1231.** The live board (B1231)
   types the listener map `u` as "an identification map, performed for free for two years" and makes
   unearned identifications the named dominant error mode. PC26 (HELD, but still a live portfolio
   row "GATED-ON-VERIFICATION") presents the listener/hearing structure and closed listener
   amplitudes with no identification-ledger annotation. Its hold reason on record is a different
   named verification, not the B1231 discipline. Needs re-typing before any advancement.

2. **[stale-vs-board, (b)] Flagship §7 seam Proposition vs B1226.** The proposition asserts "Every
   generic filling is chiral (CS ∉ {0,½})" and the surrounding narrative leans on the CS/
   amphichirality nexus whose banked chain (B1012: blind-to-k ⟺ CS = 0 ⟺ amphichiral) B1226
   **refuted at the second link in both directions** (amphichiral m003/m135/m207 at CS = ¼; chiral
   m208 at CS = 0), correcting two THEOREM rows in THE_CLAIM.md. The flagship text predates this
   and carries no correction. The m004-scoped wall statement itself survives (B1226: "stands for
   m004 but the reason is corrected"), but the flagship's reason-giving is now the corrected-away
   symmetry-theorem version.

3. **[stale-vs-board, (b)] E₆-frame papers vs B1228/B1231/B1232.** structure_paper/ ("the
   measurement cascade of the figure-eight knot's E₆"), PC25, and PC27's E₆-adjacent content
   predate: the in-session retraction of σ = 1→E₆ via the geometric CS route (B1228: the boundary
   WZW of the geometric action is A₁, E₆ arrives only via McKay on 2T), the σ-rationality core
   retraction (B1232: "σ ∈ ℚ establishes nothing"), and the B1231 deflation ("MMS proved but
   ℓ = 0 only; Anderson–Moore/Vafa is a physics-argument, unread"). None of these papers claims the
   retracted steps *as such* (PC25 is pure fold-math), but any reader routed from them into the
   σ/E₆ story would land on retracted support with no pointer.

4. **[retracted-reading-as-live, (c)] metallic_one_object/PAPER.md has no supersession header.**
   Its title and §1 still headline "a unique superconformal anyon chain" and E₆/E₈/Fibonacci-anyon
   physics vocabulary, while THE_MAP row 12 records the SM/anyon readings as **killed and
   firewalled (B483/B484)** and the portfolio does not list this PAPER.md as live. Every other dead
   draft in papers/ (P5, sl4 note, frozen trio) carries a loud in-file warning; this one does not.

5. **[internal wording tension, (a)-adjacent] flagship §5 "component" vs sl4_dehn_filling
   supersession.** The sl4 note's binding 2026-06-15 header refutes the "component" framing
   ({1,1,ω,ω²} not rigid → slice). Flagship §5 keeps "the principal Dehn-filling component"
   phrasing while its formal theorems are scoped to the fixed spectrum. Substantively compatible;
   verbally exposed.

6. **[asserted-not-computed, (a) — small, disclosed] P4 DRAFT_v8 residual verified-not-proven
   items.** The paper itself discloses these (Theorem G's tier half "verified-not-proven"; F(iii)
   converse verified-on-240; the chain-breathability conjecture beyond rung 200; the OP-3 constants
   as height-bounded PSLQ exclusions living with the reproducer). Disclosed in-text, so not a
   hidden flag — listed for completeness because they are load-bearing for the §4 headline if the
   disclosure were ever trimmed in an owner voice pass.

7. **[stale hope vs proved impossibility, (b)] PC06's "selector theorem is missing".** B1225 has
   since **proved** the symmetry-read forcing/selector theorem impossible in the form sought. PC06's
   card still frames the missing selector as an open gap to fill rather than a closed route; if the
   card is ever revived it must route through B1225.

8. **[process note] The frozen P1–P3 LaTeX PDFs were "already sent"** (SCRUTINY round 1) before the
   FATALs were found; the renders now carry FROZEN headers, but whatever copies left the repo in
   early July predate them. Owner may already have handled this; recorded because the corpus itself
   records the send.

No contradiction found between the papers corpus and the batch-1..3 campaign reports' verdicts as I
know them from the live board; the TERMINALITY candidate placed in P3_THE_PAPER is correctly fenced
on the pending G1 cell. P4_markov_stage remains, per its own gates and the canonical portfolio, the
only paper in `papers/` that cleared the full internal gauntlet.
