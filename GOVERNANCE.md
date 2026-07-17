# Origin Axiom — Governance (Phase 0)

**Status:** Phase 0 — locked. Amendments require a logged entry in `PROGRESS_LOG.md`.
**Last updated:** 2026-07-03

This file is the **constitution** of the consolidated Origin Axiom repository. It exists for
one reason: the project has a documented history of generating a small, genuine mathematical
core and then over-narrating it as physics. Governance is the mechanism that keeps the two
apart. Every other file in this repo is subordinate to the rules here.

---

## 1. Purpose

To investigate the Origin Axiom — *existence as a frustrated cancellation* — as a
**claim-bounded, reproducible, falsifiable** research program, in which:

- what is proven is locked behind tests and cannot silently regress;
- what is speculative is quarantined and clearly labelled;
- what has been killed stays killed;
- and every claim is traceable to code, a test, and a document.

The goal is **not** a theory of everything. The goal is a body of work an external expert
could clone, run, audit, and trust.

---

## 2. The framing lock

The project produced two contemporaneous self-assessments on 2026-05-21 (see
`AUDIT_REPORT.md` §3): an optimistic one (`handoff.md`) and a disciplined one
(`ORIGIN_AXIOM_REALITY_CHECK_v1.md` + the V4 paper).

**This repository is bound to the disciplined framing.** The strongest label the project may
apply to itself is:

> a candidate classical/statistical transfer-matrix framework with topological and
> Lorentzian *mathematical* structure — **not** a theory of spacetime, gravity, matter,
> or cosmology.

The handoff document is retained in `legacy/` as a historical record of the exploration. It
is **not** a source of claims.

**The form / contents distinction (canonical phrasing of the firewall).** The object the
project studies is the *form* of physics — the scale-free, kinematic, Betti / flat-side
structure (the `K010` emergent-math boundary) — never its *contents*: a scale `Λ`, a mass, a
gauge group, a spacetime, an arrow of time. Those remain **postulated inputs, not outputs**.
"We have the form, not the contents" is the one-line statement of the firewall; any prose that
lets the object *produce* contents (rather than be a compatible form for them) has breached it.

---

## 3. Claim status labels

Every claim in `CLAIMS.md` carries exactly one label:

| Label | Meaning |
|---|---|
| `proven` | Exact, independently checkable, and backed by a passing test. Safe to build on. |
| `conditional` | True *given assumptions that were chosen, not forced*. The assumptions must be named. |
| `open` | A research target. Not a partial result. Lives in `frontier/`. |
| `dead` | Tested and falsified, or shown circular/numerological. Permanent. See `docs/ARCHIVE.md`. |

A claim with no label does not exist. Prose anywhere in the repo must not assert anything
stronger than the label of the claim it rests on.

---

## 4. What counts as a claim

A statement is a **claim** only if it is backed by all three of:

1. **Code** — a script or module in `src/` (or `frontier/` for open work) that computes it;
2. **A test** — an assertion in `tests/` that fails if the result changes;
3. **A document** — an entry in `CLAIMS.md` with an ID, the statement, the label, and the
   evidence pointer.

"Interesting patterns" without all three are not claims. They may be noted in
`PROGRESS_LOG.md` as observations, never asserted as results.

---

## 5. Promotion and demotion gates

Status changes are **gated** and must be logged in `PROGRESS_LOG.md`:

- **`open` → `conditional`** — a derivation exists, but rests on named assumptions.
  Requires: code + test + the assumptions written explicitly in `CLAIMS.md`.
- **`conditional` → `proven`** — the assumptions are eliminated or shown forced.
  Requires: a proof or an exhaustive check, plus a test, plus reviewer-style scrutiny
  recorded in the log.
- **anything → `dead`** — a falsification or a demonstration of circularity. Requires:
  the reproducing code/test and an entry in `docs/ARCHIVE.md` explaining *why* it died.
- **`dead` → anything** — **forbidden.** A dead claim is permanent. A genuinely new idea
  that resembles a dead one is a *new* claim with a new ID.

Nothing moves out of `frontier/` into the proven core without passing the
`conditional → proven` gate.

### 5.1 The mathematics lane and the promotion audit (2026-07-03)

The gates above apply to mathematical claims **on their own terms**: a statement whose proof is
exact (or computer-assisted-exact with a certificate), locked by a test, and scrutinized per §6
is eligible for the ledger regardless of any physics reading — the framing lock (§2) governs
*interpretation*, never *eligibility*. Phase B's long-standing zero-promotions posture was
practice, not law, and it left the ledger unrepresentative of the project's actual load-bearing
results (rationale logged in `PROGRESS_LOG.md`, 2026-07-03). Two additions, both additive:

- **Certified data.** `CLAIMS.md` gains a *Certified data* section (`E`-ids) for exact
  computational exhibits — tables, aggregates — that are reproducible and test-locked but are
  data, not statements. The §4 three-part backing (code + test + document) applies unchanged.
- **The promotion audit.** A periodic dedicated pass sweeps `frontier/` FINDINGS for entries
  meeting the §5 bars and processes candidates through the existing gates — never by fiat,
  every promotion logged. The metric the project celebrates is **not** "zero promotions" but
  **"promotions with zero unmarked retractions"**: the ledger must represent what the project
  actually knows, at the strength it actually knows it. Refutations already bank decisively;
  positives must be able to graduate on the same evidentiary standard.

---

## 6. The red-team lens

Before any claim is labelled `proven`, ask the skeptic's questions and record the answers:

1. Were the axioms/parameters chosen to produce this result? (If yes → at most `conditional`.)
2. Is this a definition presented as a discovery?
3. Does the result survive if a different but equally natural choice is made?
4. Is a number being matched to a "famous constant" after the fact? (If yes → `dead`.)
5. Does the wording claim physics where only mathematics was shown?

The project's credibility is the honesty of these answers, not the size of the claims.

### 6.1 Two standing posture guardrails (the C / K pair)

The red-team questions above gate individual claims. Two further guardrails govern the
**program's overall posture**. They are a complementary pair — each is the antidote to the
other's failure mode, and a healthy frontier sits *between* them:

- **(C) Racing to close.** Do not upgrade "no breach found by the probes actually run" to "the
  central question is answered, the answer is no, the product is done." Absence of a reachable
  breach is `open` (no breach *yet found*), **not** a proof of impossibility. Declaring
  victory-by-exhaustion is as much an overclaim as declaring physics — and it silently kills
  live leads. The honest statement is "no breach reachable by the current probes," with the
  residuals named.
- **(K) Building past closed evidence.** Do not keep elaborating structure on a foundation the
  evidence has already closed or refuted. When a result is retracted (e.g. a "law" that proved
  to be a cherry-picked artifact), the structure resting on it retracts *with* it — it is not
  re-narrated under a new heading.

C forbids construction-on-emptiness (calling an unfinished search a finished proof); K forbids
construction-on-sand (calling a refuted result a foundation). Both are overclaims about the
*state of the evidence*, which §6 governs for single claims and which (C)/(K) extend to the
program. *(Harvested from the 2026-06 cross-chat strategy review; (K) is the discipline behind
the B192 refutation, (C) the correction to that review's own "we're done" posture.)*

### 6.2 The staging principle (verification attaches at promotion, not at birth)

The red-team lens and the full verification battery are **promotion-stage** tools. They do **not** fire at the
birth of a hint. A *hint* — a pattern, coincidence, anomaly, or unasked question — is **recorded before it is
judged** (in `docs/HINT_LEDGER.md`), and is **not** subject to the red-team lens, the MB-guards at full strength,
or the HELD rule until it is promoted past the cheap CHECKED stage. **Recording a hint is not asserting it.**

- Running the heavy adversarial battery on an **un-promoted** hint is itself a protocol violation (it re-imports
  the false-negative reflex the staging exists to prevent). A cheap check may only set a diagnostic flag and route
  a hint to **DORMANT** (parked, revivable) — it may **not** kill. Only the full **promotion gate** produces a
  `TESTED-NEGATIVE` / `dead`.
- This is the generative twin of §6.1: (C)/(K) forbid unearned verdicts *about claims*; the staging principle
  forbids unearned verdicts *about hints*. "This hint is worthless," asserted without running the gate, is as much
  an overclaim about the state of the evidence as "we proved physics." Generativity is added strictly **under** the
  rigor floor — the promotion gate is never softened.

The full protocol (the staged pipeline, the attachment table, the seven anti-blindness rules, the WIDEN/QUESTION
cadences) lives in `METHOD.md`. *(Added 2026-06-27 — the fix for the structural asymmetry that left rigor
institutionalized and generativity ad hoc, so verification was silently blinding the program to hints.)*

---

## 7. Phase structure

| Phase | Scope | Status |
|---|---|---|
| **Phase 0** | Governance, specification, claim ledger, repo scaffolding. | locked |
| **Phase A** | The tested foundation: lock every `proven` result behind a test. | complete — suite green, P1–P16 locked |
| **Phase B** | The frontier: attempt `open` items in `frontier/`, quarantined, gated. | active — probes B1–B370+; physics-boundary rows firewalled throughout; the §5.1 promotion audit executed 2026-07-03 (P17–P55, C6–C12, E1–E15 promoted through the §5 gates) |
| **Phase C** | Exhaustive survey of emergence-paths (`paths/`). | in progress |

Phase B began only after Phase A's test suite was green. See `ROADMAP.md`.

---

## 8. Anti-overclaim glossary

Recurring wording corrections. The left column is **forbidden**; use the right.

| Do not write | Write instead |
|---|---|
| "the gluing creates causal structure / spacetime" | "the composition preserves a Lorentzian form in *phase space*" |
| "φ explains the cosmological constant" | (nothing — this is `dead`, see D1–D3) |
| "the universe is a figure-eight knot" | "`A` is the figure-eight knot monodromy" |
| "we derived Einstein's equations" | "the BKL connection identifies one Kasner solution among infinitely many" |
| "Fibonacci anyon physics" | "an exact Fibonacci *fusion-count* dictionary" |
| "proven" (for a chosen-axiom result) | "conditional, given axioms A1–A6" |

---

## 9. Process

- **`PROGRESS_LOG.md`** — append-only, chronological. Every working session adds a dated
  entry. Never edit past entries. When it grows large, roll older entries into
  `docs/progress/` by quarter.
- **`CHANGELOG.md`** — human-facing, versioned (Keep a Changelog format), updated at releases.
- **`CLAIMS.md`** — the living ledger. Updated in the same commit as any result it describes.
- **Freezes** — stable states are git-tagged (see `REPRODUCIBILITY.md`).
- **`legacy/`** — frozen prior history. Never edited, never a source of claims.
- **`docs/ARCHIVE.md`** — the register of dead ideas and why they died.

---

## 11. Automated gates and the decadal review (2026-07-03)

- **Gates.** `scripts/gates/gates.py` implements fast, deterministic checks of the invariants
  in this file: the framing lock (§2/§8 banned phrasings), claims-ledger integrity (§3/§4 —
  labels, evidence files exist), the one-way firewall (no speculative room cited as claim
  evidence), append-only `PROGRESS_LOG.md` (§9), atlas freshness (the recurrence atlas
  regenerates with the frontier), attribution hygiene, and the forbidden-artifacts list.
  `tests/test_repo_gates.py` runs them with the suite, so **every merge enforces them**.
  Whitelists are frozen constants in the gate file — auditable, versioned amendments only.
- **The decadal review.** Every ~20 merges on `main` (raised from ~10, 2026-07-14 — the merge cadence densified; the name stays), a whole-repo review fires (ledger and
  protocol: `docs/progress/REVIEWS.md`); the gates surface DUE status automatically. The
  review includes the §5.1 promotion-candidacy sweep — this is where "verification attaches
  at promotion" (§6.2) fires on a cadence instead of never.

---

## 12. The five jobs and the prime organizational rule (amendment, 2026-07-16)

This repository serves five functions with contradictory optimal layouts: the **lab bench**
(arcs; append-only, stable paths), the **bank** (verified claims; immutable, lock-backed),
**navigation** (current state), **communication** (external readers), and **history**
(including failures and retractions — itself a research product). No single tree serves all
five. Therefore the prime rule:

> **Freeze the substrate; generate the views; govern by metadata.** The physical tree is an
> append-only archive. Files are never moved or renamed to "reorganize" — locks, hashes, and
> the atlas depend on path stability. Everything a reader or reviewer navigates by is a
> *view*: generated or curated from metadata, cheap to rebuild, free to evolve at every
> review. A physical move is allowed only when a wall forces it, and then: batched, scripted
> (locks migrated in the same commit), and logged in a `REORGANIZATIONS.md` entry.

The boundary of the "object teaches us" transfer is fixed here: the transfer is licensed at
the level of *problem shape* (finite observers extracting invariant content stratifies into
observer-independent / structured / coupling-dependent tiers), never at the level of the
specific mathematics. No directory mimics the 27; no cadence follows a conductor.

## 13. The three layers (amendment, 2026-07-16)

Every artifact belongs to exactly one layer, and content moves UP only through the §5 gates:

| Layer | Content | Home | Rule |
|---|---|---|---|
| **1 — invariant** | proven claims, certified data, locks, walls | `CLAIMS.md` (+ per-claim files as they convert), `tests/`, THEOREM_REGISTRY | observer-independent; every statement lock-backed |
| **2 — structured** | exact-on-instances laws, mechanisms-in-progress, strength classes | `docs/LAW_MAP.md`, banked FINDINGS | exact but mechanism-open; strength class explicit per row |
| **3 — coupling** | adjudications, seat handoffs, hints, speculations, reviews | `docs/HINT_LEDGER.md`, the governed rooms, `docs/progress/REVIEWS.md` | observer-dependent; NEVER citable as solo evidence for a layer-1/2 statement (the firewall, restated) |

Forward metadata requirements (new arcs from this amendment on; backfill lazy, never
big-bang): every arc FINDINGS carries a **lifecycle** field
(`anomaly | sweep | law | mechanism | named | unified | negated`) and a **uses:** field
(the banked arcs/toolkits it depends on). Every PREREGISTRATION carries a **conventions
block**: every basis, sign, normalization, orientation, and stage choice, declared before
the run. Rationale: the program's single most recurrent error class is undeclared choice
drift (`docs/ERROR_LEDGER.md`).

## 14. Claims as units (amendment, 2026-07-16; forward rule)

New promotions to layer 1 create one file per claim under `core/claims/` with frontmatter
(`id`, `label` per §3, `strength`, `layer`, `locks`, `uses`, `provenance`, `superseded_by`),
alongside the `CLAIMS.md` row (which becomes a generated index once conversion is complete).
Existing claims convert opportunistically. This is file *creation*, never movement (§12).

## 15. Reviews: the template, the loop, the declared modulus (amendment, 2026-07-16)

Reviews follow `docs/progress/REVIEW_TEMPLATE.md`: a small REQUIRED core (close or carry
the previous review's action items; advancement measured against LAW_MAP strength classes;
error-class recurrence check against `docs/ERROR_LEDGER.md`; provenance spot-sweep; the §5.1
promotion sweep) and OPTIONAL enrichments. Schema/governance changes are proposed as
separate arcs — never review-blocking. Every review DECLARES ITS MODULUS: what it sampled,
what it can and cannot certify — silent truncation reads as full coverage and is forbidden.
Action items are recorded in a parseable block (`### Action items (Review N)`; `- [ ]` open,
`- [x]` resolved, `- [>]` carried) enforced by the `review-actions` gate: a non-final block
containing unresolved `- [ ]` items fails the suite.

## 16. The factual-review lane for instantiated designs (amendment, 2026-07-17; owner-approved L99)

An INSTANTIATED design — any sealed document whose premises name real-world facts
(a dataset's existence or version, a publication's status, an experiment's
timeline, an access condition) — carries risks the mathematical review cannot
see. Three binding rules, distilled from the C2 provenance erratum (E4's window
instance; the mechanics were flawless, the premise was false):

1. **Adversarial factual review before execution.** Every instantiated design
   receives, AFTER sealing and BEFORE execution, an adversarial review of its
   FACTUAL premises by a reviewer that did not author the design. The reviewer's
   brief is the STANDING PROMPT below — never per-design text written by the
   author. The review report is preserved verbatim in the arc.
2. **Live-verification stamps.** Every empirical predicate in a sealed design
   ("X is unpublished", "release V is current", "the value is not public")
   carries a source + access date from a LIVE lookup at design time. A model's
   memory or prior is never a source. A predicate that cannot be live-verified
   is declared UNVERIFIED in the design itself and treated as a risk, not a fact.
3. **The widened anomaly clause.** For every seat executing under a sealed
   design: "the design's premises look wrong" is a stop-condition with the
   same standing as a mathematical anomaly — halt, report, do not work around.

**Who may review (the seat question, decided by the owner 2026-07-17):** the
factual reviewer MAY be a spawned high-capability subagent (fresh context, no
shared session state) rather than an owner-relayed seat. For FACTUAL review the
functional requirements are adversarial stance, live lookup ability, and
non-authorship — a fresh subagent satisfies these, and removes the owner as a
message relay. Two safeguards are mandatory: the subagent receives the sealed
design VERBATIM (never the author's summary), and its mandate is the standing
prompt. This equivalence does NOT extend to BLINDED lanes: predictor/comparator
separation (the B648 pattern) still requires genuinely separated seats, because
an authoring seat cannot unsee what it relays — blinding rests on the ORDER of
seals across contexts the author cannot read.

**The standing prompt (fixed text):** "You are the adversarial factual reviewer
of a sealed design. Your only job: attempt to REFUTE every factual premise in
it. For each empirical predicate, perform a live lookup (search the current
literature/data landscape) and report: VERIFIED (source + date), REFUTED
(source + date), or UNVERIFIABLE. You do not evaluate the mathematics. You do
not suggest improvements. A single refuted premise = recommend HALT."

This amendment is additive (a new review lane; no rule weakened); rationale in
PROGRESS_LOG.md (2026-07-17, the L99 adoption).

## 10. Amending this constitution

Phase 0 is locked. Amendments are allowed only when they improve *legibility or discipline*
without weakening any rule, and must be recorded in `PROGRESS_LOG.md` with a rationale.
Loosening a rule to admit a claim that would otherwise fail is explicitly forbidden.
Amendment record: §12–§15 added 2026-07-16 (organizational stratification, metadata
requirements, claims-as-units forward rule, the review loop) — all additive; no rule
weakened; rationale in `PROGRESS_LOG.md` (2026-07-16, the governance amendment).
§16 added 2026-07-17 (the factual-review lane, owner-approved L99) — additive; no rule
weakened; rationale in `PROGRESS_LOG.md` (2026-07-17, the L99 adoption).
