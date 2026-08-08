# PRACTICES — the single register of agreed working practices

**Why this file exists.** On 2026-07-29 a full-day sweep found six practices had drifted and five
had held. The split was perfect and it was not about importance:

> **Every practice that drifted had no gate. Every practice that held had one.**

The clearest case: `GOVERNANCE.md` §12 clause two (*"generate the views"*) was adopted
**2026-07-16**, written into the constitution, and **not executed for thirteen days** — while every
navigation surface it governs quietly drifted. A written rule has a half-life. A gate does not.

The second finding was structural: **agreed practices had no single home.** They lived in
`WORKING_RULES.md` prose, in `scripts/gates/gates.py` code, and in conversation — and the
conversational ones reached neither of the other two. This file is the one place. **A practice that
is not in this table is not an agreed practice.**

## How to read the ENFORCEMENT column

| value | meaning | drift risk |
|---|---|---|
| **GATED** | a named gate in `scripts/gates/gates.py` fails the suite if it is violated | ~none |
| **TESTED** | a specific test locks it | ~none |
| **SCHEDULED** | carried as a review action item; enforced by the review cadence, not automatically | moderate |
| **MANUAL** | judgement; **cannot** be mechanically checked, and this file says so rather than pretending | high — see §Judgement below |

**The rule for adding a practice:** if it is mechanically checkable, it must be GATED or TESTED —
writing it here as MANUAL when it *could* be gated is how the last six drifted. If it genuinely
cannot be checked, mark MANUAL and name the mechanism that surfaces it at the decision moment.

---

## The register

### Substrate integrity

| practice | enforcement | mechanism |
|---|---|---|
| `PROGRESS_LOG.md` is append-only (one constitutional roll-up exception) | **GATED** | `append-only` |
| No forbidden artifacts tracked (archives, CI config, surname-bearing files, loose relays) | **GATED** | `tracked-forbidden` |
| No AI labels, seat labels, or the owner's surname in public docs | **TESTED** | `tests/test_public_surface_scan.py` |
| Commits as `originaxiom`; no AI trailer | **GATED** | `attribution` |
| No new frontier arc may reuse a B-number | **GATED** | `id-collisions` |

### Views and navigation — the class that drifted

| practice | enforcement | mechanism |
|---|---|---|
| Views are **generated**, never hand-maintained (§12 clause two) | **GATED** | `views-generated` |
| Every navigation view refreshed at each decadal review | **GATED** | `views-fresh` |
| Every `knowledge/K*.md` indexed, and every indexed K-number has a file | **GATED** | `knowledge-index` |
| Every backticked repo-path citation resolves | **GATED** | `path-refs` |
| The atlas is regenerated when arcs change | **GATED** | `atlas-fresh` |
| Every frontier arc with a FINDINGS.md carries a sibling `arc_verdict.json` (the B877 lesson: a banking retry resumed past the failed verdict step) | **GATED** | `arc-verdicts` |
| `PROGRESS_LOG` and `CHANGELOG` are updated together | **GATED** | `log-changelog-paired` |

### Claims and the firewall

| practice | enforcement | mechanism |
|---|---|---|
| `CLAIMS.md` rows well-formed; every PROVEN row cites an existing test | **GATED** | `claims` |
| Every link in THE CHAIN cites a **resolvable** test lock (the ledger's own admission rule) | **GATED** | `chain-locks` |
| `LAW_MAP.md` is an **unenforced index**: every row traceable to an arc, every cited lock resolving (R33-4) | **GATED** | `law-map-provenance` |
| The atlas lexicon must not **go blind**: zero-motif probes may not grow (B806) | **GATED** | `atlas-lexicon-current` |
| No speculative room (`speculations/`, `philosophy/`, `story/`) cited as claim evidence | **GATED** | `firewall-oneway` |
| Banned overclaim phrasings absent from the corpus | **GATED** | `framing` |
| No SM values to `CLAIMS.md` (Gate 5); physics readings wait on L91 | **MANUAL** | firewall review at banking |

### Verification

| practice | enforcement | mechanism |
|---|---|---|
| No test may pass unconditionally (no-assert / tautology) | **GATED** | `test-vacuity` |
| A gate must be **observed to fail** before it counts as a gate | **MANUAL** | mutation-test at the time of writing; recorded in the arc |
| A **complete** suite run is required before claiming green — a killed run is a *different, weaker* check | **MANUAL** | see §Judgement |
| Superseded review blocks carry no open action items | **GATED** | `review-actions` |
| Gates **fail closed** — a gate whose subject is missing must FAIL, never go quiet | **GATED** | verified by deletion in a fresh clone; see §Restart resistance |

### Cadence

| practice | enforcement | mechanism |
|---|---|---|
| Decadal review every ~10 merges | **SCHEDULED** | the `review-due` counter (`python3 scripts/gates/gates.py review-due`) reports it; it is advisory by design and does not fail the suite |
| Prereg sealed, hashed into `SEAL_LEDGER.md`, and **committed before** any computation | **MANUAL** | the seal itself is the evidence |
| Push to `origin` **and** `codeberg` after every banked advance | **MANUAL** | verified at review |
| cc3's branch is **never merged**; deliverables cherry-picked under a new number and verified independently | **MANUAL** | integrate-don't-merge |

---

## The arc-verdict vocabulary (W1) — four values, and the two boundary rules

Measured at **κ = 0.842** across two blind seats (B809), which passed the masterplan's sealed 0.75
gate. **Both disagreements were vocabulary boundaries, not reading errors**, and both are closed
here — the repairs would have taken that sample to κ = 1.0.

| verdict | meaning |
|---|---|
| **PROVED** | the arc's headline is a positive result that was established |
| **NEGATIVE** | the headline is that a claim, candidate or mechanism was killed, refuted, found null, or shown not to hold |
| **OPEN** | the arc advanced something but **settled nothing** |
| **RETRACTED** | the headline is the withdrawal of **this arc's own** previously banked result |

**MIXED ARCS — a verified core with an unsettled extension (B834, 2026-07-30).** Some arcs establish
something exactly *and* leave a labelled extension open. B556 says it in its own header: *"the
computational core is VERIFIED EXACTLY; the tower-as-physics-ladder reading is banked as a labelled
HYPOTHESIS."* The four-category vocabulary forces one label onto both halves.

> **Label a mixed arc by what it ESTABLISHED, and carry the unsettled half in the claim line** —
> prefixed `ESTABLISHED:` … `UNSETTLED:`. `OPEN` is for an arc that settled **nothing**.

**Measured, not asserted:** two independent 12-reader panels, judging blind, were **unanimous
(24/24, 24/24, 23/24)** against the corpus on exactly three arcs — B61, B556, B746 — **all three
mixed, all three drifting the same way.** κ = 0.93 was blind to it; only comparing the panel against
the corpus exposed it. **A panel can be perfectly self-consistent and uniformly drifted.**

**Disambiguation (B818, from the two errors wave 2's untested vocabulary let through).** `RETRACTED` applies only when the arc withdraws **its own** headline. An arc that *establishes* that **another** arc's claim fails is doing positive work: label it by what **it** established (`PROVED` / `NEGATIVE`), and the retraction lands on the **target** arc's record. This is what keeps the ledger usable — `RETRACTED` on X means "do not trust X's old claim", and that is the only thing the label is good for. Mislabelling an auditor as RETRACTED makes the ledger say the audit is untrustworthy, which is the opposite of the truth.


Plus `instrument: true` when the product is a tool/compiler/ledger/census rather than a result.

**Boundary rule 1 — a correction that also proves is PROVED.** `RETRACTED` applies only when the
withdrawal is the arc's **whole** content. If a new positive result supersedes an old one, the
verdict is `PROVED` and the withdrawal is recorded in `supersedes`. *(B809's B212 disagreement.)*

**Boundary rule 2 — the verdict labels what the arc ESTABLISHED, not whether the programme's target
was reached.** An exact result inside a firewalled arc is `PROVED` even when its destination bar is
explicitly not cleared. `OPEN` is reserved for arcs that settled **nothing**. *(B809's B420
disagreement.)*

**Known systematic effect — PREDICTED at n=2, then MEASURED at n=12 and found NOT to hold.** Both
B809 disagreements ran the same direction (one seat labelled PROVED where the other was more
cautious), so a **seat-to-seat conservatism offset** was predicted. B817 put all 12 readers on an
identical 15-arc block and measured it: **10 of 12 produced the exact same verdict mix (5:10)**,
the other two 7:8 and 6:9. **The offset is essentially nil** — so wave 1's 0.364 → 0.917 per-slice
spread reflects **genuine differences between the arc sets**, not who read them. Fleiss' κ = 0.9312.
A fan-out should still report its per-seat distribution; the point is that the prediction was
resolved by measurement rather than carried indefinitely as a caveat.

**But scope the measurement by what it actually exercised.** B817's calibration block used only
**two** of the four verdict categories, and licensed work that used four:

> **A calibration set must be checked, BEFORE the run, to exercise every category it will license.**
> A κ measured on a narrower distinction than the work it gates is a real number about the wrong
> question. This is the vacuity rule one level up: not *can the criterion fail?* but *was the
> criterion even exercised across the range it governs?*

## Judgement practices — the ones that cannot be gated

These are real and they are the most valuable, but **no gate can check them**. Pretending otherwise
is worse than admitting it, because a gate that cannot fail is exactly the defect `test-vacuity`
exists to catch.

- **Compute the discriminating fact.** A negative is only as sound as the in-sandbox computation of
  the fact that discriminates it — never asserted, cited, or proxied.
- **Verify in both directions.** A refutation gets the same scrutiny as a claim. (Error class E33
  was minted when a *correct* computation was discarded in deference to an unverified refutation.)
- **Calibrate a scanner before quoting its number.** A first count is a hypothesis. (103 → 65.)
- **Name the defect path before discarding your own result.** Suspicion that cannot name a route is
  not a reason.
- **An unearned negative is as bad as numerology.**
- **A sealed threshold inherits the seal-writer's bias (R36, measured).** Across ten sealed
  predictions, six failed **directionally**: over-confident about instruments this seat builds,
  **under-confident about reader panels four times consecutively**. The cost is concrete —
  **B842's gate was set at κ ≥ 0.60 because 0.55–0.75 was expected**, and κ came in at 0.8732.
  > **A bar set from a prior is a bar set at the prior's error. Derive thresholds from something
  > external — a pilot run, a published benchmark, a measured history — not from what you expect.**
  The κ history (0.9312 / 0.9305 / 0.9300 / 0.8732) is now that external source for panel gates.
  **Calibration on outcomes is not calibration on instruments:** the predictions that came out right
  were the ones whose answer was already implied by banked work.
- **A literal lock must NORMALISE before it matches (four instances this week).** Markdown defeated
  four locks in one week: a **bolded** value broke a table-row count (B845); `>` blockquote
  continuation markers interleaved mid-sentence and hid two phrases (P5 Phase 2); an exact-match on
  `authored_by` broke when provenance was **appended** (B835); a magic-word check flagged nine
  carried items that each gave a good reason **in different words** (B844).
  > **Strip emphasis, blockquote markers and whitespace before matching; match on the property, not
  > the rendering.** A lock that reads formatting is testing the typesetter.

  **And the normaliser must be IDEMPOTENT, not one-pass (fifth instance).** A single-level strip of
  `>` left a stray marker mid-sentence where the source nested them (`> >`). **A normaliser that
  handles one level of the thing it normalises is itself a literal lock.**
- **A gate that can only fail on ABSENCE cannot detect DRIFT (R36).** Four found this week:
  `log-changelog-paired` watched a file nobody wrote (frozen timestamp ⇒ could never fail);
  `review-actions` reported **0 open items when there were 13** (its regex stopped at the first
  continuation line); the lexicon ceiling was **self-referential**; and B840's `SEALED` was vacuous
  because the branch that could set it was unreachable. The 2026-07-29 restart-resistance audit
  missed all of them **because it only checked what happens when an input goes missing.**
  > **Any gate whose output is a COUNT or a MATCH must assert against an independently derived
  > total.** A count that only ever compares itself to its own source cannot notice that the source
  > moved.
- **A label-lock is not a lock (B828, 2026-07-30).** `test-vacuity` catches tests with *no*
  assertion. It does **not** catch a test that asserts over **literals the test itself defines** —
  e.g. `reasons = {...three strings...}; assert len(set(reasons.values())) == 3`, which verifies
  that three different strings were typed and can only fail if someone edits the dict to repeat one.
  **The question is not "does it assert?" but "what would have to be true in the WORLD for this to
  fail?"** If the answer is "nothing outside this file", it is documentation wearing a test's name.
- **A bounded falsifier declared before its governing theorem is retrieved is not yet known to be a
  falsifier (2026-07-29, the Dirac campaign).** The campaign designed the E34 trap in *advance* and
  caught the spin-count instance of it — then walked into a different instance of the same family:
  a falsifier whose terminating branch turned out to be **excluded by a theorem nobody had looked
  up**. The flaw was not in the reasoning; it was in the **ordering**. The campaign correctly
  insisted on a literature gate and then placed it *after* the falsifier it governs. **Retrieve the
  governing theorem first; only then is a kill branch known to be reachable.** A falsifier that
  cannot fire is decoration, and it is worse than none because it advertises a rigour the design
  does not have.
- **Apparatus-inflation (E34).** Before attributing a conclusion to the object, name the largest
  structure the derivation passes through and ask whether the conclusion is already a property of
  *that*. For an instrument, ask whether the pattern is the tool's own footprint.
- **An instrument that works but cannot be found has failed.** Review 33's sharpest finding was not
  a broken artifact but a correct one: the stagnation oracle (`scripts/atlas/query.py`) worked, was
  honest about its own selection effects, and was reachable from **zero** entry points at exactly the
  moment it was needed. **No gate catches this**, because nothing was wrong with the artifact. When
  you build an instrument, the same commit must put it in the path of the seat who will need it.
- **The commensurability rule (B803, adopted 2026-07-29; CORRECTED 2026-07-29 at review).**
  *A step that depends ONLY on the invariant trace field, the invariant quaternion algebra, or
  arithmeticity is a statement about the COMMENSURABILITY CLASS. A step that depends on the GROUP Γ
  itself is not.* The discriminator is **what the statement's input is**, not whether the field
  appears somewhere upstream.
  - **CLASS** — trace field, quaternion algebra, arithmeticity, and what follows from those alone:
    the ramified prime 3, `SL(2,𝔽₃) = 2T`, **the E₆ label**. m003 shares m004's field `ℚ(√−3)` at
    identical volume (verified), so these tie **by construction**.
  - **MANIFOLD** — anything whose input is Γ: **character varieties `Hom(Γ,G)//G`** (commensurable
    groups have *different* ones), cohomology, torsion at the E₆ exponents, homology, knottedness
    and hence **amphichirality**, congruence data, and the **spectra**.
  - **The first draft of this rule said "everything downstream of the field", which swept in the
    representation theory and was wrong.** Consequence: `CLAIMS` P49/P51 are **not** scope-inflated —
    P51's *"ρ_prin's deformation space in the figure-eight's E₆ character variety"* is correctly
    object-level, because a character variety is built from Γ₄₁, not from ℚ(√−3).
  - **Prior art the first draft missed** — the programme reached this two months earlier from the
    other side: **B302** (the generation ℤ/3 is in the *commensurator*, not the object — Neumann–Reid,
    since m004 is *the* arithmetic ℚ(√−3) knot), **B307** (no hyperbolic knot has a C₃ trace field —
    a theorem, closing the single-knot route), **B486** (hexagonal-cusp route refuted). B803 supplies
    *why* the chain is class-level; B302/B307 supply *what lives in the class* and *what provably
    cannot live in the object*.

- **Apparatus-inflation (E34).** Before attributing a conclusion to the object, name the largest
  structure the derivation passes through and ask whether the conclusion is already a property of
  *that*. For an instrument, ask whether the pattern is the tool's own footprint.
- **An instrument that works but cannot be found has failed.** Review 33's sharpest finding was not
  a broken artifact but a correct one: the stagnation oracle (`scripts/atlas/query.py`) worked, was
  honest about its own selection effects, and was reachable from **zero** entry points at exactly the
  moment it was needed. **No gate catches this**, because nothing was wrong with the artifact. When
  you build an instrument, the same commit must put it in the path of the seat who will need it.
- **The commensurability rule (B803, adopted 2026-07-29).** *Any derivation step routing through
  the invariant trace field, the invariant quaternion algebra, or arithmeticity is a statement about
  the COMMENSURABILITY CLASS, not about the object.* m003 and m004 share `ℚ(√−3)` and are
  commensurable (verified), so everything downstream of the field — the quaternion algebra, `2T`,
  **E₆ via McKay**, the three 27's, the cascade, the V₄ torsor — ties for the sister *by
  construction*. Only homology, knottedness (hence **amphichirality**), congruence data and the
  **spectra** are manifold-level. Decidable by inspection; it retroactively explains B727. No gate
  can check whether a *mathematical* derivation routes through a commensurability invariant.

**The mechanism that actually works for these is the PREREGISTRATION**, and this is not a slogan —
it was measured. B799's prereg declared in advance that an all-COMPUTED outcome would be a *warning
sign*, and when the result came back with five honest downgrades, that pre-commitment is what made
the outcome interpretable instead of self-congratulatory. A prereg forces the judgement **before**
the answer is visible, which is the only moment at which judgement is cheap.

So: **for anything judgement-shaped, seal a prereg with a two-outcome criterion.** That is the
closest thing to a gate that judgement admits.

---

## Restart resistance — verified, not assumed

The register is worth nothing if a fresh seat never finds it or a fresh clone silently loses it.
Both were **tested in a clean `git clone`**, and both were initially broken:

- **All 16 gates run in a fresh clone**, exit 0, no setup. ✔
- **Discoverability was BROKEN.** the gitignored session pointer file sends a new seat to `WORKING_RULES.md`, and that file
  mentioned **neither** the gates nor this register — zero hits. A seat could work indefinitely
  without learning the enforcement layer exists. `WORKING_RULES.md` now names both.
- **Three gates were FAIL-OPEN**, verified by deleting the very files they guard in a fresh clone:
  `knowledge-index` **passed** with `knowledge/INDEX.md` deleted; `review-actions` and
  `views-fresh` **both passed** with `REVIEWS.md` deleted. All are now **fail-closed** — a gate
  whose subject has vanished reports failure rather than silence. Re-verified by deletion.
- **`docs/PRACTICES.md` is now protected by a second, independent gate**: because
  `WORKING_RULES.md` and `CHANGELOG.md` cite it by path, deleting it trips `path-refs` as well as
  `practices-register`. Linking it from the entry point made discoverability and enforcement guard
  each other — an accident worth keeping.
- **Known and accepted soft-skip:** four gates that read git history report "git unavailable —
  skipped" outside a git checkout. That is an honest limitation, not a hole: a zip download
  genuinely cannot verify git facts, and a fabricated failure would be worse. It is recorded here
  so nobody rediscovers it as a surprise.

## A correction must be propagated to the document's companions (B848, 2026-08-02)

A multi-document delivery arrived where **the same failure occurred twice**: a claim was corrected
in one document, and the companions shipped in the *same bundle* still carried the withdrawn
version.

- the eigenvalue count was corrected to **17** in the final handoff's own error list, while
  **four of six documents still said 43**;
- the Riley polynomial was corrected in the master handoff, while the E6 probe still stated the
  form that correction withdrew.

**Both corrections were honestly recorded. Neither reached the documents that used them.** A
reader opening any single companion gets the withdrawn claim with no signal that it is withdrawn —
which is strictly worse than never having found the error, because the error now carries the
authority of a document that lists its own mistakes.

**Rule:** when a claim is corrected, the correction is not complete until every document in the
same delivery that *uses* that claim has been updated or explicitly marked. An error list is a
record, not a fix. Same shape as `RETRACTED` withdrawing only its **own** headline.

## A true identity can prove the wrong half (B848, 2026-08-02)

`S A S⁻¹ = adj(A)` for symmetric A is true, was verified symbolically, and was used to conclude
"no arrow". It cannot: `det S = +1`, so it supplies the **amphichirality** conjugator, while "no
arrow" needs the **det = −1** one. The counterexample was already inside the same document's own
table — a symmetric matrix with an arrow.

**Rule:** when an argument establishes an existence claim, check *which* of the case's two
branches the exhibited object lands in. A correct conclusion resting on a mechanism that proves a
neighbouring statement is the hardest defect class to see, because every individual step verifies.
This is the "hypothesis nobody listed" failure, and it survives symbolic verification.


## The seal carries its own provenance — GATED (`seal-provenance`)

**Rule (adopted 2026-08-08, from B946's adjudication of the solo seat's handoff 6).** Every
preregistration sealed on or after 2026-08-08 must name, *in the sealed text*, two things:

- **`BANKED IDENTITY:`** the banked identity this pipeline reproduces inside itself before any
  new number is read; and
- **`PRIOR ART:`** the bank grep / `query.resolutions_for()` run at **design** time.

**Why this and not a new gate.** The banked-identity gate already existed in `docs/TOOLBOX.md`
as a design pattern. A seat with full repo access proposed it mid-session, skipped it, and then
spent nine sections computing a quantity its own banked theorem forbade — and separately
duplicated a sealed arc for want of one grep. **A skipping problem is not fixed by adding
another gate.** It is fixed by making the existing requirement a field that must be present
before the seal hashes, which is the only moment where it can bite. Older seals are exempt by
construction: a rule cannot bind text sealed before it existed.

## Maintaining this file

This register is itself gated — `practices-register` checks **both directions**:

1. every row marked **GATED** names a gate that actually exists in `scripts/gates/gates.py`; and
2. every gate in `scripts/gates/gates.py` appears somewhere in this file.

Direction (2) is the one that matters for drift: **a gate added without a row here would make this
register quietly incomplete**, which is precisely how `knowledge/INDEX.md` lost four entries. The
same both-directions check that fixed that fixes this.

When a practice is agreed in conversation, it is **not** agreed until it has a row here.
