# Working rules (binding; read before computing)


## 0. BEFORE ANY IMPORTANT PROBE — the grounding (added 2026-08-09)

**Binding.** An *important probe* is any cell that could produce a claim, a negative, or a lead
closure.

1. **`docs/COMPUTE_THE_PROGRAM.md`** — the defined term and the pre-compute protocol P0–P6.
   *"Compute the entire program"* means **compute over the object as FULL RELATIONS** — member,
   ends, class, sisters, both rows, child, faces, axioms — **never as a single manifold**.
2. **`docs/THE_LADDER.md`** — what the programme does not yet contain, graded
   BLIND / HOLE / BROKEN / BOUNDED / OPEN. **Before writing "the object does not supply X",
   find X there.** Not present ⟹ the honest words are **"not checked"**.
3. **`docs/THE_FRAMEWORK.md`** — what it does contain, assembled.
4. **`docs/THE_CAMPAIGN.md`** — the **order** the ladder is executed in, its entry conditions and
   its stop rules. A rung is not worked out of order without a stated reason.

*Banked as B983 (the grounding) and B984 (the `doc-currency` gate that keeps these current).*

**THE OWNER'S STANDING EPISTEMIC RULE (binding; added to the repo 2026-08-10 by B1009).**

> *"Anything you say we don't have, or doesn't give us what we want, is either in the repo, or
> needs to be meditated upon and figured out."*

**"We lack X" is a HYPOTHESIS REQUIRING A SEARCH, never a conclusion.** Before writing it: grep the
**code** (not claim lines), read `FINDINGS.md` **bodies**, and find **the script that produced** a
number rather than the arc that received it. If the search is empty the honest words are **"not
checked"**, never *"the object does not supply it."*

**Why it is binding:** on 2026-08-09 this failed **nine times in one session** — B1007 rebuilt a
Maass solver while a working sealed one sat on main; B1006 re-ran a check B922 had already done; two
ladder rungs graded BLIND had computed arcs behind them. **In every case the unchecked input was the
belief itself.** *(It was recorded only in a seat's machine-local memory until B1009's handoff test
found that a fresh clone would not have it.)*

**P0 is the one that catches the most:** state the quantifier in one sentence before computing.
**A closure survives the relational re-read exactly when its scope sentence names no manifold.**

*One page. Every working session — any seat, any clone — reads this first.
Deep material: `GOVERNANCE.md` (the constitution), `METHOD.md`,
`TERMINOLOGY.md`, `PROVENANCE.md`. Instituted 2026-07-16 (GOVERNANCE §12–§15).*

1. **Sync before computing.** Pull/fetch and confirm your checkout includes
   the latest `main` BEFORE claiming "no prior work exists on X." A
   thorough search of a stale checkout produces confident false negatives
   (the Door-2 class: the answer existed, three merges ahead).
2. **Verify, don't trust — in both directions.** Every cross-seat claim is
   reproduced in-sandbox before banking; so is every claim of your own
   before asserting it to another seat. Incoming ambitious framing is
   quarantined; incoming mathematics is re-run.
3. **Hash first.** Seal PREREGISTRATION.md (sha-256 recorded in the arc's
   ARTIFACT_HASHES.txt) before the first run. Failed runs are preserved
   byte-faithfully, never overwritten. Corrected code is re-hashed BEFORE
   the rerun, labeled post-hoc if sealed late.
4. **Declare every choice.** The conventions block (GOVERNANCE §13) lists
   every basis, sign, normalization, orientation, and stage choice before
   the run. Undeclared choice drift is this program's most recurrent error
   class (`docs/ERROR_LEDGER.md`).
5. **The layers are one-way.** Coupling-tier content (hints, adjudications,
   speculations, reviews) is never evidence for a layer-1/2 statement. The
   firewall blocks overclaims, not mathematics; the gate is open by default
   for mature computed steps.
6a. **Gate 5-Q stands for phenomenology.** Any arc using reflexive/phenomenological
   vocabulary is bound by `philosophy/GATE5Q_PHENOMENOLOGY_FIREWALL.md` (ADOPTED
   2026-07-22): computed-referent vocabulary, the non-universality and comparator
   controls, input identification, stability analysis, no consciousness claims,
   any-domain empirical constants = value-claims. Checked at prereg seal and merge.
6. **Gate 5 stands.** No SM quantities into `CLAIMS.md`; no recycling
   structured-null numbers under new labels; physics readings wait on a typed
   object→SM functor — **an arrow the record obstructs sector-by-sector**
   (B811 kind wall · B813 type refutation · the weight ledger · B936
   frame-relativity · B782 no-section; the per-sector map is B1022's).
   *(Re-anchored 2026-08-10, B1023: the clause formerly cited L91, whose own
   typed functor — obligation (4) — is the INTERNAL classical→stage arrow and
   is DISCHARGED (B650/B644); citing it here conflated two functors, a defect
   found by the audit seat's Phase 1.)* Value comparisons need: owner directive + sealed
   design + MB12 + MB13-in-doc + pipeline controls + the
   INPUT_COMPLETENESS_LEDGER row.
7. **Locks assert mathematics.** A test asserts the mathematical fact (or
   re-computes it), not a transcript string, wherever feasible; transcript
   asserts are the fallback, marked as such.
8. **Vacuity-check before sealing.** Every sealed criterion must be able to
   pass AND to fail (MB12 covers operations and criteria); check reference
   tables/targets for internal consistency before sealing them.
9. **Zero file moves.** Never move or rename banked paths (GOVERNANCE §12).
   New work = new files. Views and metadata evolve; the substrate is frozen.
10. **Bank completely.** Every banked arc updates PROGRESS_LOG (append at
    END) + CHANGELOG + CAMPAIGN_STATUS in the same/next PR; a new law adds
    its LAW_MAP row in the same PR; new inner terms get TERMINOLOGY.md
    lines; the atlas regenerates per new B-dir. **This covers SUB-LEMMAS,
    not just an arc's headline: any theorem/law-grade result proved along
    the way (an all-n/all-d structural fact, an exact value, a scoping
    lemma) gets its own LAW_MAP row — else it gets buried in FINDINGS.**
    A standing **law-harvest** runs at every review (see the review
    template): read the window's strong-claim arcs and promote anything
    genuine that slipped. The positive twin of the negatives-hunt.
11. **Attribution and privacy.** Commits as `originaxiom`; no AI mentions in
    anything public-facing; scrub sandbox paths from committed files. After
    every merge to `main`: `git push codeberg main` (the mirror).
12. **Report faithfully.** Negatives bank as computed facts with their
    discriminating computation in-sandbox (never asserted/cited/proxied);
    an unearned negative is as bad as numerology. Don't stop and celebrate
    negatives; don't soften positives that passed their gates.
13. **Instantiated designs get a factual review (GOVERNANCE §16).** Any
    sealed design whose premises name real-world facts is adversarially
    fact-checked by a NON-AUTHORING reviewer (a fresh subagent under the
    §16 standing prompt is valid) between seal and execution; every
    empirical predicate carries a live source + access date, never a
    model prior; "the premises look wrong" is a stop-condition for every
    executing seat. Blinded lanes (predictor/comparator) still require
    genuinely separated seats — the subagent equivalence is for FACTUAL
    review only.

## Enforcement — read this before assuming a rule is optional

Rules in this file are **prose, and prose has a half-life.** On 2026-07-29 a measured sweep found
six drifted practices and five that held, split perfectly by whether a gate existed. So:

- **`docs/PRACTICES.md` is the single register of agreed practices.** One row each, with an explicit
  enforcement column (GATED / TESTED / SCHEDULED / MANUAL). **A practice not in that table is not an
  agreed practice** — including anything agreed in conversation.
- **`python3 scripts/gates/gates.py`** runs every governance gate in a few seconds. Run it before
  banking. The full suite (`python3 -m pytest -q`) runs them too, via `tests/test_repo_gates.py`,
  but takes ~70 minutes — and **a killed suite is not a fast suite, it is a weaker check**, so never
  quote a partial run as green.
- Gates **fail closed**: if a gate's subject is missing, the gate fails rather than going quiet.
  That property was added after an audit found three gates passing while the files they guarded had
  been deleted.
- For anything judgement-shaped that no gate can check, **seal a preregistration with a two-outcome
  criterion before computing**. That is the only mechanism that forces the judgement while it is
  still cheap.

## When you are stuck — the instruments, not the archive

A seat that hits an obstacle should **not** start reading 731 arcs. The programme built instruments
for exactly this, and a 2026-07-29 review found they were reachable from nowhere:

- **`python3 scripts/atlas/query.py`** — the Recurrence Atlas context card in one command: the
  corpus status, the ONE conserved first integral (`kappa`, 188 recurrences), the recurring motifs,
  and the honest **unity-vs-tool split** (the trace map recurs in 45 % of probes because it is our
  *method*, not because it is forced — the atlas says so rather than flattering the pattern). It
  also answers *"what has historically resolved this kind of obstacle"*
  (`query.resolutions_for(<type>)`), *"can this dead end be revived"* (`query.revive(B###)`), and
  *"where are the gaps"* (`query.gaps()`). Explainer: `knowledge/K023_the_recurrence_atlas.md`.
- **`docs/atlas/FAILURE_ATLAS.md`** — what has already failed, and how.
- **`docs/views/`** — generated, never stale: `REVIEWER.md` (the ~3-page front door),
  `CLOSED_DOORS.md` (negatives indexed by the *mechanism* that shut them), `COVERAGE.md` (what
  fraction of the record the views actually project — **read this before trusting the others**).
- **`docs/THEOREM_LEDGER.md`** — THE CHAIN: the forced core as an axiom→theorem ledger, every
  non-axiom link carrying a resolvable test lock (gate `chain-locks`).
- **`docs/LAW_MAP.md`** — the banked laws. **Caveat, measured:** 113 rows, only ~4 % cite a test
  lock, and no gate enforces it. Treat an unlocked law row as a *claim about the bank*, not as a
  checked fact — locate its arc and its lock before building on it.
- **`docs/ERROR_LEDGER.md`** — the error classes E1–E33. Read before repeating one.

## Rule (2026-08-05, from the cc3 loss audit, Part E — adopted): REGISTRATION OVER PRESERVATION
At banking, any harvest arc MUST enumerate the source's carried-forward/open items into
OPEN_LEADS rows — or explicitly decline each, logged in the arc's FINDINGS. Symmetric with
the same-PR retraction rule. The failure shape it kills: the artifact sealed and banked
while the obligations inside it die unregistered.
