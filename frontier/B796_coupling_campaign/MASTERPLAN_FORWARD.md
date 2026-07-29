# B796 — THE COUPLING CAMPAIGN MASTERPLAN (forwardable edition)

*cc3 audit seat, 2026-07-29. Self-contained for forwarding. Repo copy:
`frontier/B796_coupling_campaign/MASTERPLAN.md`; harvest reports in
`frontier/B796_coupling_campaign/harvest/`. Gate 5-Q. No cell runs
before cc gate + per-cell sealed prereg (sha256 in SEAL_LEDGER).*

## Contents
- [1. Thesis and hypotheses](#1-thesis-and-honesty-clause)
- [1.5 The campaign falsifier](#15-the-campaign-falsifier-what-makes-this-a-test-not-a-lens)
- [2. How the plan was derived from the 12-agent harvest](#2-derivation-rationale)
- [3. Wave 0 — governance status](#3-wave-0--governance-status)
- [4. Wave 1 — cheap two-outcome forks](#4-wave-1--cheap-two-outcome-forks)
- [5. Wave 2 — calibration and interface rigidity](#5-wave-2--calibration-and-interface-rigidity)
- [6. Wave 3 — the control instrument](#6-wave-3--the-control-instrument)
- [7. Wave 4 — the only value-facing cell](#7-wave-4--the-only-value-facing-cell-owner-gated)
- [8. Dependency spine](#8-dependency-spine)
- [9. Excluded as untestable](#9-excluded-as-untestable)
- [10. Protocol wrapper](#10-protocol-wrapper)
- [10.5 Second-round harvest results](#105-second-round-harvest--first-results-landed-while-drafting)
- [10.7 Context-sweep addendum](#107-context-sweep-addendum-2026-07-29-after-the-five-sweep-repo-re-analysis)
- [11. Open asks](#11-open-asks)

---

## 1. Thesis and honesty clause

Two hypotheses, named per cc's gate:

- **H0**: the object supplies STRUCTURE — sectors, degeneracies,
  counting, congruence data; VALUES arise in the observer-object
  coupling (automorphy sector, cutoff scheme, coupling dial, boundary
  condition).
- **H2**: the object has nothing to do with the Standard Model.

The banked nulls — character variety (0 bits), rung-1 PSLQ, forced
limits, Maass spectrum (B792/B797: 17 eigenvalues, sealed base-rate
null; their existence independently verified 7/7 by cc's instrument,
B795 — a statement about the eigenvalues, not about the hypotheses) —
refute *values-in-the-object*. **They do not, by themselves,
distinguish H0 from H2: every one of those nulls is predicted
identically by both.** §1.5 states the campaign-level test that does
distinguish them.

## 1.5 The campaign falsifier (what makes this a test, not a lens)

The BC/CM route (§10.5) is the only dynamics-native mechanism the
harvest identified. Its beta=infinity/Galois half requires an
arithmetic subalgebra whose KMS values are algebraic — on the Bianchi
side this must come from m004's Maass spectrum, which is not known
(and mostly not believed) to carry the required algebraicity.
**CAMPAIGN FALSIFIER (restructured per chat1's review): PRIMARY =
the bounded mechanism-exclusion** — a negative from the deep-precision
algebraicity test (Cell 9, the keystone) within a SEALED POWER BOX
(degree/height bounds (d, H) + digit budget fixed at prereg per
N ≳ 1.43·d·log₁₀H; at 8 digits there is NO power) **closes the BC/CM
route.** Bounded, bankable, needs no survey of alternatives.
**SECONDARY (conditional):** the H2-favoring inference fires only
once the two in-house dynamics leads (the parked transfer-operator
campaign, L72) are separately dispositioned — this keeps the §10.7
rider from re-opening E32 through the honest door. The literature
prior is against algebraicity; neither side pre-committed. Fallback:
if the box proves unreachable, exploratory-interpretive relabel;
mechanism-exclusions only. Honest cost note: 8 → 50 digits is
10⁴–10⁵× the certified run on a different numerical stack — the §16
review is cheap; the computation is not.

**Honesty clause (the critic's G22, scope per cc's gate):** every
Wave 1-3 cell tests coupling **structure**. The second-round harvest
identified a dynamics CANDIDATE (BC/CMR) — candidate identified is
NOT gap filled: **the Bianchi instance the object needs is verified
EMPTY in the literature.** BC dynamics is imported from Spec O_K,
attachable only through the cooling functor, and the anabelian control
(T6) may bound it to "attaches to the arithmetic, not to this
object".

## 2. Derivation rationale

How 12 agent reports became 8 cells — the actual filter, so the
conclusions can be audited:

**(a) Triangulation requirement.** A cell entered the plan only if
three independent sources aligned: a *mechanism* from a literature
agent (how structure could yield numbers), an *asset match* from a
repo agent (we can actually compute it with banked objects: Riley
holonomy, 17 certified eigenvalues, length spectra, exact scattering,
level-4 congruence structure), and *survival of the adversarial
critic* (12th agent, instructed to attack completeness and
testability).

**(b) The falsifier filter.** The selection criterion was "can fail
cleanly": every cell is a two-outcome fork whose failure is itself a
bankable fact (solver indictment, family closure, normalization
failure). The literature agents' seductive proposals that failed this
filter were cut — KK phenomenology numbers, scattering-phase coupling
constants, Koide circulants — because their failure modes are
unbounded scans, not verdicts.

**(c) What each literature agent contributed after filtering:**
- *NCG/spectral action* → warned that constant curvature makes ALL
  perturbative heat coefficients proportional to volume → became the
  **volume firewall** (Cell 4): before any spectral-action claim, prove
  the object-specific residual exists and differs from the sister's.
- *3d-3d correspondence* → T[m004, E6] has no definition (type-A
  machinery only) → **excluded**, with the verified negative recorded;
  only the protected-quantity boundary is cited.
- *Quantum modularity/CS* → no point-selection theorem exists for a
  "physical coupling"; only set-level statements are falsifiable →
  became the **Habiro cage** (Cell 5): test whether the coupling dial
  can ADD arithmetic, not which value it picks.
- *BKL/WDW* → the 5d→4d descent has no mechanism → excluded; the
  usable residue is the **parity census** (inside Cells 1/6), which
  connects our parent forms to the billiard states without descent.
- *Prior-art graveyard* → the repeated failure mode across
  Bilson-Thompson/Furey/Atiyah is deriving structure and then
  DECLARING values → encoded as protocol: the chirality/anomaly audit
  (Cell 8 Stage A) runs before any numerics, per the Distler–Garibaldi
  precedent.
- *Value-generation mechanisms* → dimensional transmutation is the
  only mechanism yielding pure numbers from counting + ONE imported
  scale → Cell 8 Stage B, owner-gated.
- *Arithmetic QC/Maass data* → the GH ladder values and the Hecke
  machinery → Cells 1 and 2, with the ladder demoted to
  predictions-not-controls (the 51.014 provenance lesson applied
  forward).

**(d) The critic's structural contributions.** Its gap list became
Wave 0 (each item verified in-session by me, not trusted from the
digest — which caught the critic itself once: the "2/25 record not
findable" claim was wrong, the record is at `B784/FINDINGS.md:287`;
it had grepped only `docs/`). Its "untestable" list was adopted
verbatim as Section 9 so the campaign cannot drift back. Its biggest
finding — zero dynamics coverage — produced both the honesty clause
and the three second-round harvest agents.

**(e) chat1's composition principle** (assembly vs search are separate
instrument capabilities, validate each on the axis where evidence
exists) shaped the instrument framing throughout: Cell 1 validates
search against pre-stated external predictions; Cell 6 validates
sector assembly against a sealed invariance table; Cell 7 builds the
standing control that every value-facing model must pass. The
mult-2/sector episode (cc's 8.8634 prediction, decided by the
eigenspace projection test) is the worked example: σ-minima prove
existence, never sector — only invariance tests assign sectors.

**(f) Ordering logic.** Cells ranked by unblocking value, not glamour:
1–3 are days-cheap forks that fix bookkeeping every later cell
consumes; 4–6 build calibration and interface rigidity; 7 is the
expensive control instrument that gates all value-facing work; 8 is
the only cell that touches SM numbers and is double-gated (chirality
audit, then owner's Gate-5-SM).

## 3. Wave 0 — governance status

| item | status |
|---|---|
| B792 seal + certified re-run + scope wording | **DONE** (seal `c6954bfa`; max mode-count drift 5.4e−9; generic-spectrum null wording) |
| r = 8.8634 sector call | **DONE** — eigenspace projection: no parent direction; cc's prediction refuted with clean controls (E4 instance, banked). The absence of a second parent eigenvalue below r = 9.84 is an ordinary Weyl fluctuation (V1 budget expects 2.55 on [3.9, 9.84], found 1, z = -0.97) — a GH-ladder explanation briefly attached here is WITHDRAWN per cc (the GH table is per-symmetry-type; 122.19 is uncorroborated) |
| B773 re-baseline | **DONE** — W4-304's trace-level wall REFUTED (θ-odd sector carries tr_odd = 1/4); no B796 constraint may cite it |
| "2/25" proposal record | **DONE** — sourced at `B784/FINDINGS.md:287` |
| LAW_MAP staleness | ADOPTED — design against origin/main's copy |
| ι adjudication (rank-3 vs rank-4 observer menu) | **RULED by cc** — rank-3 scoping kept for all cells; rank-4 deferred (interpretive status unresolved; importing it would be invisible and load-bearing) |
| Gate-5-SM owner authorization | SCHEDULED — blocks Cell 8 Stage B only |
| Second-round harvest (dynamics G15, Born-content G14, novelty G13) | IN FLIGHT — 3 agents |

## 4. Wave 1 — cheap two-outcome forks

**Cell 1 — GH LADDER.** Extend the verified solver's scan to r = 13.5.
Pre-stated: SOME parent (S-invariant) eigenvalues appear near
r ≈ 11.0086, 12.5016, 13.2960 (transcription-grade; 122.19
uncorroborated). NO completeness claim between rungs — the GH table is
per-symmetry-type, so entries are consecutive within a type only;
completeness statements come solely from the Weyl budget. The
(7.3, 10) parent-free result stands as data (projection test); the
(10, 13.5) window is open, not predicted. Plus the parity census
(z → −z̄, semidirect-2) starting at 51.0132434, building the
GH/Then/DHY parity dictionary. *Falsifier:* absent rungs or extra old
forms indict solver or the GH transcription — either is bankable.
*Provenance rule:* the ladder values are transcription-grade —
predictions to test, never controls to tune against.

**Cell 2 — DOUBLET SURGERY.** Hecke discriminator inside the five
mult-2 eigenspaces. VALIDATION GATE FIRST (Hecke relations + Ramanujan
on mult-1 forms at level (4); abort = banked normalization fact).
Equal eigenvalues ⇒ geometric (D₄) degeneracy; distinct ⇒ arithmetic
(Steil-type). Decides what degeneracy structure a coupling could
break; kills or confirms B791's "generic multiplicity."

**Cell 3 — SPIN FORK.** Exact Z[ω] arithmetic on m004's two spin
structures: bounding vs Lie via signs of lifted cusp parabolics.
Lie ⇒ the conventional fermionic spectral-action family CLOSES;
bounding ⇒ authorizes a Dirac-Hejhal follow-up. No third outcome.

## 5. Wave 2 — calibration and interface rigidity

**Cell 4 — VOLUME FIREWALL.** Two-sided Selberg closure (17
eigenvalues + exact φ(s) = Λ_K(s−1)/Λ_K(s) + the exact parabolic term,
derived as a sub-deliverable, vs 370 geodesic traces), then the
spectral-action residual under 3 cutoffs and 2–3 cusp regularizations,
with the m003 control. *Falsifiers:* sides fail to close (instrument
indicted); residual scale ≠ systole; m004/m003 residuals
indistinguishable ⇒ the spectral-action family is volume numerology,
CLOSED.

**Cell 5 — HABIRO CAGE.** b = 1 Taylor coefficients of the 4₁ state
integral, PSLQ against the pre-named basis {Q(√−3)-algebraics ×
e^{±kV/2π}} under B743 caps + surrogate nulls. Any coefficient outside
the cage kills arithmetic closure; full closure banks "the coupling
dial cannot ADD numbers" — H0's sharpest interface statement.
Declared trap: b = 1 factorization degenerates; the closed-form route
is mandatory.

**Cell 6 — SECTOR LADDER.** Decompose L²(m004) under the
**SL(2,Z[ω]/4)/{±I}** coset action (12 = 1+5+6) — E21 guard (chat1):
the TRUE PSL(2,Z[ω]/4) has center order 4 and order 960, and its
coset action on the image has degree 6; the degree-12 action carrying
1+5+6 is the intermediate quotient SL/{±I}, order 1920. A seat
building PSL from the definition gets degree 6 and the cell fails for
the wrong reason. Assign all 17 eigenvalues;
sealed-in-advance table of which functionals are object-fixed vs
sector-moving. Cross-check against the projection-test labels —
disagreement indicts one method.

## 6. Wave 3 — the control instrument

**Cell 7 — SISTER SPECTRUM.** Adapt the solver to m003 (declared
engineering cost), compute to r = 10 at 8 digits. Pre-stated: parent
forms incl. 51.0132434 appear IDENTICALLY in both sisters; newform
spectra differ. Then the STANDING GATE, sealed now: **any coupling
model that fires equally on m003 and m004 is refuted as volume
numerology.** Side quest: the m003 "≡ 1 mod 4" congruence half.

## 7. Wave 4 — the only value-facing cell (owner-gated)

**Cell 8 — GRAMMAR TRANSMUTATION.** Stage A (ungated, structure only):
enumerate anomaly-free compact-slice + matter assignments the grammar
admits; chirality/anomaly audit BEFORE numerics. No survivors ⇒ the
E6-skeleton coupling family closes — a clean negative. Stage B (ONLY
with owner-sealed Gate-5-SM design): 1–2-loop Λ_i/Λ_j ratios under one
unification boundary condition vs SM ratios under the B743 harness,
selection entropy declared in bits; bits(selection) ≥ bits(match)
voids the cell.

## 8. Dependency spine

    Cell 1 ──► Cell 6 (parity rungs) and old/new labels everywhere
    Cell 2 gate ──► any Hecke-consuming cell
    Cell 4 cusp term ──► Cells 1/6 instruments
    Cell 7 ──► standing control for every value-facing model
    Cell 3 ──► gatekeeper for fermionic follow-ups

Sealed with the preregs: a failed upstream cell VISIBLY voids its
dependents.

## 9. Excluded as untestable

Verbatim from the adversarial critic; no drift back: T[m004, E6] (no
definition); unique-coupling selection from CS/quantum modularity (no
point-selection theorem); β=1 SSB at finite level (needs the infinite
tower); time arrow/Lorentzian from the object (contradicts banked
theorems; no falsifier); Born CONTENT this campaign (harvest first);
the T1 mover (spec only); absolute scales (theorem-grade no-go);
thermodynamic-N / ≥2-cusp dynamics (NEEDS-SPECIALIST); 5d→4d BKL
descent (no mechanism); non-BPS T[m004]; anthropic measures (no
derivable measure); spacing statistics at n = 17 (no power).

## 10. Protocol wrapper

Rung named first; sealed prereg + sha256 in SEAL_LEDGER before
compute; vacuity check both directions; B743 surrogate-null gates on
anything numeric; m003 comparator; digit budget stated per cell
(8-digit ceiling until mp-eigenfunctions exist); negatives computed
in-sandbox; distinct-vs-multiplicity counting explicit;
discard-reporting on every filter; structural coincidences face the
same base-rate knife as decimals.

## 10.5 Second-round harvest — first results (landed while drafting)

Two of the three gap agents have returned; both materially amend the
plan (full reports in `harvest/second_round_*.md`):

- **Adversarial novelty re-search: both our "nobody has done this"
  claims FAILED as written** — which is exactly why the agent existed.
  (1) The Müller school has regularized heat-trace asymptotics on
  cusped hyperbolic manifolds (Müller 1501.07851; Park math/0111175;
  Friedman math/0605288); surviving novelty is only the
  spectral-action *packaging* and m004 *specifically* — and Cell 4 now
  builds on Müller's published cusp terms instead of deriving blind.
  (2) **F_K(4₁) exists** (Gukov–Manolescu 1904.06057, figure-eight as
  flagship) — a new asset for Cell 5's cross-checks. The T[m004, E6]
  exclusion stands but its reason is corrected: defined by the ADE
  construction, never made explicit for any manifold.
- **Born-content harvest: the II₁→III interface framing is UNCLAIMED
  TERRITORY** — a verified negative with named near-misses (the
  gravitational crossed-product literature produces entropies/weights,
  not interference content; the QFT-measurement literature states the
  type-III probability problem as open). Both halves of the
  programme's bridge are theorem-backed (Gleason–Yeadon trace forcing
  on II₁; Connes–Størmer + Takesaki on III). Five finite-stage test
  cells (T1–T5, SL(2,p) stages p = 5..13) are drafted as candidate
  Wave 2.5, pending critic pass + gate.
- **CM Bost–Connes dynamics (G15) — landed, and it is the tightest
  mechanism match of the harvest.** BC-type systems carry dynamics
  intrinsically (flow from the arithmetic norm); the phase transition
  sits at exactly β = 1 = the pole of ζ_K, matching the programme's
  banked measurement-SSB claim verbatim; the III→II cooling arrow
  exists as a literature functor (CCM endomotives). The agent's
  in-session computation of the disc-−48 class polynomial
  independently reproduced the banked cusp j-invariant, and the BC
  symmetry budget visible at congruence level (4) is exactly Z/2.
  The Bianchi/H³ BC slot is **verified empty** (structural reason: no
  Shimura data for H³) — the second unclaimed territory of the day.
  Six candidate cells (T1–T6) drafted with falsifiers, including the
  sharpest kill-test in the campaign so far: BC attachment FORCES
  observer type III₁ specifically, so a III_λ or III₀ reading kills
  the whole family — and an anabelian specificity control that bounds
  whether the dynamics sees m004 at all or only its arithmetic.
  Together with the Born-content T1–T5 these form candidate
  **Wave 2.5 (dynamics & content)**, pending critic pass + gate.
  Scope per cc: this is a dynamics CANDIDATE, not a filled gap — the
  Bianchi instance is verified empty, and the Maass-algebraicity
  requirement of the BC route's cold phase is exactly what the
  campaign falsifier (§1.5) tests.

## 10.7 Context-sweep addendum (2026-07-29, after the five-sweep repo re-analysis)

A full re-analysis of the authoritative origin/main docs (progress
spine, leads/doors, error/protocol rulebook, changelog/history, and
cc's banked B793-B797 arcs; reports in `context_sweep/`) produced
four changes a reader of this plan should know:

- **PROPOSED RIDER to the campaign falsifier (cc-gated wording):**
  the falsifier's "no alternative modality writing an observer-object
  equation of motion" clause is HARVEST-scoped. The repo already
  registers two in-house dynamics leads the harvest missed: the
  parked **trace-map transfer-operator campaign** (the object's one
  analytic/dynamical face — "no laundering theorem covers its
  transfer-operator spectrum," B451 Ruelle data banked, flagged
  "strongest H1 candidate," parked 2026-07-10 on a naming collision)
  and **L72** (the CS-functional/dynamics program). Both are
  object-side dynamics with no observer coupling, so the falsifier is
  not voided — but its "no alternative" clause must not fire until
  each is developed toward an observer coupling or shown unable to
  host one. The asymmetry favors the campaign: BC is imported and
  possibly object-blind (T6); the transfer operator is object-NATIVE.
  Wave 2.5 gains candidate family TM-1..n.
- **Cell hardening from the registries:** Cell 6 declares B384-T3's
  banked triangular S-compression negative as a control; Cell 8 must
  cite three registered priors (H118 Baez-Schwahn F4->SM door,
  registered "expected NO"; B561 "the chain stops at F4"; B565/H121
  gauge-behavior verdicts) and fill all 12 INPUT_COMPLETENESS_LEDGER
  rows at prereg; the protocol wrapper regains the atlas +
  FAILURE_ATLAS consult; the m003 comparator is used ALONGSIDE the
  banked D2/B447 m-scan control; base-rate priors are cited with
  scope (main's 1-for-21 governs mechanism proposals; 2-for-25 is
  the audit seat's cumulative score).
- **Exclusion re-scope:** the "unique-coupling selection / dense
  dial" exclusion does not dispose of PD1.4/W2.11 (the +-1/48
  selection-rule theorem — finite exact arithmetic, the programme's
  single forced-coupling candidate, the gate on PD1 AND PD4);
  remanded to cc as candidate cell vs exclusion-on-its-own-reason.
- **Record corrections in flight both ways:** three corrections to
  cc's banked B794/B797 records relayed (locked-test figures:
  m004-only norm count, certification-margin units, dry-run-vs-
  certified artifact); two of cc's corrections accepted on the
  branch (A5/D5 scoped to HOOK; Weyl residual as consistency check,
  never an order-one adjudicator).

## 11. Open asks

1. **cc:** gate the masterplan (structure, cell list, exclusions,
   spine).
2. **cc:** ι sequencing RULED (2026-07-29): rank-3 scoping kept; rank-4
   deferred (ι's measurement status is interpretive and unresolved).
3. **anyone with library access:** the Grunewald–Huntebrinker primary
   (Experiment. Math. 5(1) 57–80, Table 3) upgrades Cell 1 from
   prediction-test to control-test and discharges the last external
   provenance dependency.
4. **owner:** Gate-5-SM authorization decision point arrives only at
   Cell 8 Stage B — nothing before it touches SM numbers.
