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


## LAW_MAP rows carry their arc's scope — GATED (`lawmap-scope`)

**Rule (adopted 2026-08-08, from B965's audit).** A LAW_MAP row citing an arc whose
**verdict** carries four or more scope markers (*only for, scope, assumes, not established,
conditional, up to, one-prime, not certified, not claimed, post-hoc, inferred, cited not
re-derived, screened, necessary-not-sufficient, limits, does not*) must carry **at least one
scope marker of its own**.

**Why.** The B965 audit found 165 rows, 5 flagged, **all five written the same day** — and in
**every** fix the arc's own verdict was *correct and properly scoped*. **The loss happened in
the compression step**: turning a verdict into a one-line row drops qualifiers. This is the
first gate here aimed at claim **scope** rather than at numbers, hashes or file presence —
the class of error that, until now, only a human ever caught.

Calibrated on that audit: it flags all three rows the audit had to fix, and passes the row
the audit adjudicated as already correctly scoped.


## A retraction is not done until the sweep is clean — GATED (`retraction-sweep`)

**Rule (adopted 2026-08-08, L139 from B965).** **Retracting a claim does not retract its
instances.** When a claim is retracted: register its phrase in `docs/RETRACTED_PHRASES.md`,
then run the sweep until it is clean. A retraction is **not complete** until both are done.

**Why.** B964 retracted the bare use of "VEV" and wrote a rule. **One hour later** the LAW_MAP
audit found that exact error still live in a row written the same day — and when the sweeper
was first run over all **2,210** tracked `.md` files it found **B962's own FINDINGS still
asserting both retracted claims, in its title and body, with no banner at all.** The
retraction had never reached its source.

The sweep distinguishes **use** from **mention**: the phrase may appear inside a retraction
record, a correction banner, a quotation of what was formerly claimed, or a test enforcing
its absence. Incoming panel reports (`PRIOR_ART_*.md`, `O3_PRIOR_ART.md`, `DRAFT_FINDINGS.md`)
are **evidence, not our claims**, and are exempt on the same principle as another seat's
scripts.

**Limitation, stated:** a phrase registry can only police wording specific enough to be
unambiguous. Broad phrases (e.g. "the Standard Model algebra") need **correction banners**,
not greps — `docs/RETRACTED_PHRASES.md` records which retractions are handled which way, and
why.


## Render before banking — NOT GATED (a human obligation)

**Rule (adopted 2026-08-08, from cc3's render audit, B975).** For any arc whose product is a
**field**, a **spectrum**, or a **set of points**: **render it once before banking.** Not for
presentation — **as a check.**

**Why.** Two defects (a truncated move set documented as complete; a global phase never pinned,
leaving "Re f" an arbitrary rotation) sat latent in code that had **already produced banked
results** and had passed **three §16 review passes, a shakedown, and 58 hours of certified
computation**. Neither surfaced while computing — *a number off by a phase still looks like a
number, and a truncated-but-sufficient move set produces exactly the right answer*. **Both
surfaced within an hour of somebody trying to draw the output.**

This is the complement to `lawmap-scope` and `retraction-sweep`: those catch **claim drift in
prose**; rendering catches **structure drift in numbers** — the class certified numerics absorb
without complaint. The same audit also produced the day's one unlooked-for observation (the
horoball radii are 1/(2N) for N an Eisenstein norm — ℚ(√−3)'s arithmetic visible as sphere
sizes in the cusp packing).

**Not gateable.** "Did you render it" cannot be checked automatically. This is a human
obligation and is recorded as one.


## Every substantial arc is represented somewhere — GATED (`representation-sweep`)

**Rule (adopted 2026-08-08, L143 from B976).** Every **substantial** banked arc — non-instrument,
PROVED or NEGATIVE, `claim_one_line` ≥ 500 characters — that is cited on **no** synthesis surface
must carry a disposition in `docs/REPRESENTATION_TRIAGE.md`: **PENDING** (a debt), **PROCESS**
(correctly absent from an object atlas), or **SURFACE** (the arc *is* a surface).

**Why.** B976 measured it: of 60 arcs banked in B800–B880, **39 were cited on no synthesis
surface**, and **only 1 of the 12 cascade-closure arcs** appeared anywhere. Among the missing was
**B864, which derives hypercharge** — while a ledger row written five days later called
hypercharge *"OPEN — the sharpest available target"*, sending a lead, a literature panel and a
running workflow phase after a solved problem.

**The repo lost nothing. The summaries forgot.** This is the third of the day's three gates, and
the one the other two could not have caught: `lawmap-scope` and `retraction-sweep` police the
**content** of rows that exist; **neither notices a row that was never written.**

**Calibration note.** Substantiality is measured by **claim length, not file size**. On the block
that was actually lost, a 6 KB file-size floor catches **1 of 11**; a 500-character claim-length
floor catches **11 of 11**. B864's FINDINGS is 3.7 KB — short and dense. A seat writes a long
claim line when there is a lot to say.

**Limit.** The gate enforces that an unrepresented arc is *known*, not that it is *rowed*.
Thirteen arcs currently sit at PENDING — that is a recorded debt, not a discharged one.

## Every "forced" must name its warrant — GATED (`forcing-audit`)

**The campaign's acceptance test is one sentence: *every occurrence of "forced" must be backed
by a theorem or an exhaustive classification*.** This gate checks it by machine, in
`papers/structure_paper/arxiv/main.tex`:

1. the forcedness-audit table's status column uses a **closed vocabulary** —
   `forced` / `proved here` / `certificate` / `classical`, plus the two sharpening qualifiers
   `+ Levi` and `conditional`;
2. **hedges are banned outright** in a status cell (`essentially`, `morally`, `modulo`,
   `largely`, `effectively`, `arguably`, `broadly`, `nearly`, …), because a hedged *forced* is
   how a cost claim erodes without anyone deciding to weaken it;
3. every `\ref` in the table resolves to a real `\label`;
4. a row marked **forced** must cite a **theorem, proposition, lemma, corollary or census** —
   a *forced* whose only citation is a Scope is precisely the defect the acceptance test names;
5. any bolded **forced** elsewhere in the body must carry a `\ref` in its own paragraph.

**Why a gate and not care.** The acceptance test had been checked by reading three times, and
each time a drifted row was found **by eye**. The programme's own diagnosis is that its failure
mode is retrieval — a claim and its warrant drifting apart — so the repair is mechanical.

**Calibration, run as `python3 scripts/checks/forcing_audit.py --selftest`.** Four violations are
seeded into a copy of the source and all four must be caught: a hedged status, an unresolved
reference, a **forced** whose only citation is a Scope, and a stray bolded **forced** in the
body. Baseline is 0 problems, so the gate is not passing by accident — it passes because the
table is clean, and it fails the moment it is not.

## A paper claim must carry its source where it is stated — GATED (`paper-claim-registry`)

**Every headline claim in `papers/structure_paper/` must resolve to a registry row or a lock,
and every cited lock path must exist.** Blockquoted Theorem/Proposition/Census statements are
checked directly; §1 is scanned **by paragraph**, and a structural assertion is recognised by a
**named mathematical object in inline code**, not by styling.

> **That last clause was earned the hard way, and the correction is the point.** The gate
> shipped claiming the `ℤ₆` defect as its calibration case **and did not catch it** — proved by
> mutation test the same day. Two reasons, both instructive: the `ℤ₆` claim **was never bold**
> (it is inline code in ordinary prose), and the one bold near it **spanned two lines**, so a
> line-by-line bold scan missed that too. **A gate that advertises a calibration case it cannot
> catch is worse than no gate**, because the documentation launders the gap. Now mutation-tested
> in both directions: removing the citation makes it exit 1 and name the structure; restoring it
> exits 0.

**The calibration case, kept because a gate without one is a gate nobody trusts.** On
2026-08-15 the paper's **own headline sentence** asserted the global form
`[SU(3)×SU(2)×U(1)]/ℤ₆` with **no citation and no registry row, in either registry** —
while `frontier/B862_global_form` and a green lock had existed for weeks, and `SKELETON.md`
mentioned `B862`, `ℤ₆` and "global form" **zero times**.

**This is the B950 failure one level downstream.** B950 wrote that the global `ℤ₆` form was
*"not addressed"*; **B862 derives it**; B978 counted that as one of *"three instances in one day
of declaring absent what already existed."* The synthesis layer lost the arc, and the paper then
inherited the loss **in a new shape — not "declared absent" but "asserted without its source"**,
which is the more dangerous form: **a missing claim looks missing; an uncited one looks
confident.**

**Why it is a new gate and not a patch to an existing one.** `path-refs` verifies that a cited
path *resolves* — it cannot see a claim that cites **nothing**. `representation-sweep` runs
**arc → surface**; this runs **claim → row**, the other direction. `retraction-sweep` polices
phrases, not sourcing.

**Limit, stated rather than hidden.** The gate recognises claims by *form* (blockquote
theorem-lines, §1 bolded assertions with factual cues). A claim written as ordinary prose is
invisible to it. It narrows the surface; it does not close it.

## Read the code before rebuilding it — MANUAL (a discipline, nine instances in one session)

*(Count updated 2026-08-12: at least three further corpus-level instances this window — B632's walked-and-dissolved cubic re-asked as an open question; B961's frame.py nearly rebuilt; rep27.json nearly re-derived. All three arcs carry double-digit inbound citations: not obscure, unretrieved. Gate-candidate against the atlas.)*

**The rule.** Before building an instrument, **open the files that would already contain one** and
read them. Not `grep` for a claim about them — **read the source**. A claim line says what an arc
*concluded*; the source says what the repo *can do*, and those are different questions.

**Why it is written down.** On 2026-08-09 this failed **nine times in one session**, twice
expensively:

- **B1006 cell D** re-ran B922's parked-H4 axis. The protocol's P3 prior-art step *was* executed —
  and it grepped **claim lines**, so it missed the check sitting in B922's **FINDINGS body**.
- **B1007** rebuilt a Maass solver from scratch **while a working, sealed, arb-based 25-digit one
  sat on main** at `frontier/B878_maass_upper_window/branch_cell9_rung1_v2.py`, carrying **B922's
  own seal hash**. Worse, the new arc then claimed a **cost overturn against B798** that B798's own
  sentence refutes — *"a different numerical stack (arb/mpmath Bessel, mp linear algebra)"* — and
  that the working solver disproves by existing. **Every one of the four defects in the failed
  rewrite is fixed in the working source, with the reason written in a comment.**

**The shape, and it is always the same:** the seat forms a belief about what the programme *lacks*,
then builds against that belief without checking it. **The belief is the thing to check first**,
because it is the one input nothing downstream can correct.

**The check, which costs about two minutes.** Before writing an instrument:

1. `grep -rl` the **code**, not the docs, for the primitives it would use (`bessel`, `svd`,
   `mp.dps`, the object's name).
2. Read any hit's **docstring and comments** — this repo's working sources document their own
   traps, and both B792 and the cell-9 solver name the exact fix B1007 needed.
3. If an arc banked a number, find **the script that produced it**, not the arc that received it.
   `B922_lambda2_receipt` is a *receipt*; the computation lives in `B878_maass_upper_window`.

**Why it is not a gate.** No gate can know what a seat *intends* to build. What a gate can do is
assert an instrument **exists** once found — so `tests/test_b1007_arb_maass.py` locks the presence
of the working solver, turning "we have no high-precision solver" from a false belief into a **test
failure**. **That is the pattern to copy: when a false belief costs an arc, lock the fact that
refutes it.**

## The suite runs parallel; serial is the certificate of record — the ARBITER RULE (B1018)

**The rule.** `scripts/run_suite.sh` runs the lock suite under xdist (`-n 12`) by default —
qualified by B1018 (correctness clean; the one run-1 failure was a baseline-delta the
anti-file-drawer lock was *right* to raise). **Serial (`--serial`) remains the certificate of
record: any parallel-vs-serial disagreement is a FAILURE, investigated and never shipped.** The
qualification is bench-specific; a material environment change (python, xdist, core count)
re-qualifies before parallel certificates are trusted again.

**Why it is written down.** The suite grew 33 min (Review 11) → 60–87 min, and the growth is
corpus-linear. The measured dividend on this bench is **1.42×** (~18 min/merge) — honest and
modest: twelve sympy workers on eight physical cores are cache-bound, not embarrassingly parallel.
**The number to distrust is a parallel run that disagrees with serial by even one test** — that is
never noise; it is a shared-state lock, and it gets a name and a fix before anything ships.

## A concession is not made until it is propagated — same batch (the window handoff's procedural finding)

**The rule.** A defect conceded in an exchange (relay, protocol round, review) is **not conceded**
until the correction lands in the conceding seat's own banked record — the arc, the row, the
claim line — **in the same batch as the concession.** The worked failure: C6/C12's "licensed by
theorem" was conceded in the Phase-2 exchange and left standing in the published Phase-1 arc;
the relay corrected it, the record did not, **and no instrument catches that** — a relay is not
the record. Sealed files take the addendum-beside pattern; everything else takes the edit.

## Maintaining this file

This register is itself gated — `practices-register` checks **both directions**:

1. every row marked **GATED** names a gate that actually exists in `scripts/gates/gates.py`; and
2. every gate in `scripts/gates/gates.py` appears somewhere in this file.

Direction (2) is the one that matters for drift: **a gate added without a row here would make this
register quietly incomplete**, which is precisely how `knowledge/INDEX.md` lost four entries. The
same both-directions check that fixed that fixes this.

When a practice is agreed in conversation, it is **not** agreed until it has a row here.

## No living document misrepresents the current state — GATED (`doc-currency`)

**The rule.** A registered *living document* — one a reader forms their picture of the programme
from — must not lag the corpus. `doc-currency` (B984) measures, for each, the **newest arc it
cites** against the **newest arc that exists**, and fails past a per-document tolerance.

**Why it exists.** `ROADMAP_TOE.md` described the programme's position as *"the kinematic/symmetry
frame is forced arithmetic"* for a month after B862/B863/B864 made that false. `THE_SM_VERDICT.md`
shipped omitting **eleven of the twelve** cascade arcs and contradicting two banked results. Neither
was caught, because **every gate checked arcs, and no gate checked surfaces.**

**The measure is deliberately crude and honest.** Newest-citation lag is a proxy: a document can be
current and cite nothing recent, or stale while citing a fresh arc. It is a *prompt to read*, not a
proof of staleness — which is why the failure message says a stale surface is **owed a read**, not
that it is wrong.

**Two visible pass-throughs, and neither may be silent** — B982 found seven gate exemptions resting
on an audit that never named them:

- **`frozen`** — an in-file marker `<!-- doc-currency: frozen -->` for records, dated snapshots and
  superseded files kept for provenance. **Reported on every run.**
- **`DECLARED_DEBT`** — names *what* is owed and *when* it was declared. **Printed on every run**,
  and the lock fails if the set grows. **A debt is not an exemption.**

**Standing debts declared 2026-08-09:** `docs/TOOLBOX.md` (**613 arcs stale** — and the pre-compute
protocol says read the toolset before any important probe, so this is the highest-priority debt on
the board), `CLAIMS.md` (129), `docs/THEOREM_LEDGER.md` (63), `docs/GUT_REQUIREMENTS_LEDGER.md` (31).

**Where the rest of the obligation lives:** `docs/BANKING_PROTOCOL.md` — the full banking checklist,
the independent-verification requirement, and the decadal review's room-by-room currency reading.

## Never mutate the tree while the suite is running — MANUAL (a discipline, not a gate)

**The rule.** Once a full `pytest` run starts, the working tree is **frozen** until it returns. No
`atlas.py`, no `views/generate.py`, no edits — not even ones that "can't matter".

**Why it is written down.** On 2026-08-08/09 this was violated **three times by the same seat**, and
each time it produced the *identical* artefact: `test_atlas.py::test_render_regenerates_the_map`
failing at collection position ~18, because the atlas was regenerated mid-run and the test read a
half-updated tree. Each violation cost a **~57-minute** run.

**Why it is not a gate.** A gate would have to detect a running pytest and block writes, which means
either a lock file every tool must respect or a filesystem watcher — both heavier than the failure
they prevent, and both new machinery to maintain. **The honest treatment is a named discipline with
its symptom recorded**, so the next seat recognises the artefact in one glance instead of debugging
a phantom test failure.

**The symptom, so it is recognisable:** a suite failure in `test_atlas` or `views-generated` that
**passes when re-run standalone**. That combination means the tree moved under the run. The result
is not a failure — it is a **void run**. Re-run it; do not "fix" anything.

**The sequence that works:** do all the work → regenerate → gates green → *then* start the suite →
do nothing until it returns → commit.

## Every relay carries a disposition, or it is invisible work — GATED (`relay-debt`)

**The rule.** Every seat-to-seat relay has one row in `docs/RELAY_LEDGER.md`: **BANKED** (the row
**names the arc**, so the claim is grep-checkable), **DECLINED** (the row says **why**), or **OPEN**
(a debt, with an age, escalated by name past 21 days). **A relay with no row is the failure state:
invisible work.**

**Why it exists.** Branch protection preserves **files**. Nothing preserved **findings**.
`CC3_TO_CC_2026-07-28_rank4_response.md` answered the ι-status question in July, never reached main,
and **L114 was then promoted asking a question that relay had already answered** — costing a full
campaign to rediscover. The loss audit caught this class once and it was actioned three ways (B909,
B920, B921, branch protection); **it recurred anyway, because every one of those fixes preserved
files.**

**Design credit: cc3 (2026-08-09), re-implemented and verified on main rather than merged, per
integrate-don't-merge.**

**It caught invisible work on its first run:** `CC3_TO_CC_2026-07-22_p3_complete.md`, tracked in the
repo root with no row, carrying a P3 verdict (8 CLOSED / 6 HELD / 7 EXPOSED) with no trace on main.
**18 days old — the oldest live debt, and exactly the shape that lost L114.**

**Who may mark what.** A seat may seed its own relays **OPEN**. **A seat may not mark its own relay
BANKED** — that is marking your own homework. BANKED is the *receiving* seat's judgement and its row
must name the arc.

## The naming gate (proposed at B1033; the day's three same-symbol collisions)

2026-08-11 produced three instances of the corpus's dominant error class in one day —
"θ-even" naming both the F₄ exponents and B1011's mirror set; tone(5) conflated with
mirror(8); "flavor" sealed onto an algebra B1033 adjudicated as chiral. The class (B980:
*the algebra was always right; what failed is what the symbols denote*) is caught today by
TERMINOLOGY rows after the fact. **The generative fix, proposed as an instrument follow-up:
a naming gate at bank time** — any arc introducing a named group, value set, grading, or
index declares its referent against the TERMINOLOGY registry, and the gate fails on an
undeclared collision with an existing name. Until the gate exists, the practice is manual:
**name a new object by its defining equation in the same sentence as its label** (the
window handoff's L154 clause, generalized).

## Point-of-use citation (registered at B1033/B1038; the corpus's measured retrieval defect)

The record's defect is not lost work but work cited everywhere except where it is needed
(measured: a banked arc with 38 inbound citations went unconsulted by the adjacent
same-operator arc; the fourth crossing used "CP phases" six times citing zero arcs of the
object's own CP-phase body). **The practice: an arc's FINDINGS cites the corpus's own
body for every load-bearing term it uses** — before sealing, ask of each key term "where
does the record already speak about this?" and cite it or record the search. The
checkable gate-shape (a future instrument): key terms in a new FINDINGS resolve against
the TERMINOLOGY registry and the atlas's motif index.

## A "no match" is not a finding until a second source agrees — MANUAL (gate candidate)

(B1001, applied at the audit seat's cost this window: seven instances, three species.)
*A search that cannot run returns exactly what a search that finds nothing returns.*
Sub-clauses: run both φ and phi; verify the tool ran; `head`/`tail` is a window, never a
population; check the flag's unit (occurrences vs lines).

## Assert the ordering, not the threshold — MANUAL

(B1002.) *Re-fitting a floor to each new N is fitting, not testing.* A count dressed as
a defect rate is the same error one level up.

## Gate every export against a number you did not compute — MANUAL

(B961.) *A wrong-dimensional space is not obviously absurd; on an unbanked question the
wrong answer looks like a finding.* Every subspace/rank export reproduces a banked value
before any new number is read (applied end-to-end in B1036).

## Ask whether the quantity moves under the gauge — MANUAL

(B647 c3 · B884.) *Only what survives the rescaling is content; the rest is the
pipeline's pivot order.* The census (B1038-verified) shows the banked record already
passes; the practice exists so it stays true.


## claim_drop.py outputs are CANDIDATES, never verdicts — instrument status (2026-08-12)

Held-out validation (the audit seat, item 6, this bench's record of it): real precision
~11% held-out vs 57% tuned — E29's law on the instrument's own numbers; two FP modes
fixed (heading-as-fence; retraction-as-fence), 62 → 30 candidates; the subject-mismatch
mode is a human call by design. **Any figure from this instrument is a candidate rate;
the honest adjudication question is "does the claim line assert something the arc's own
body explicitly refuses" — never "is there a fence somewhere in the body."** The fresh
held-out slice (B101 B109 B111 B120 B125 B126 B139 B145 B148 B158) is reserved — named
by the instrument's author, who must not adjudicate it.

Instrument staleness (2026-08-12, from the Field Ladder's verification): an instrument
built on a branch — a ladder, census, or atlas — sees main only as of its last sync.
**Date-stamp the sync in the instrument's header, and read every absence it reports as
"absent as of that sync."** Species instance: B1034 (banked on main days earlier) was
invisible to the Field Ladder; the miss was structural, not a search failure.

The decoy control (2026-08-12, the odyssey's Task C — its methodological keeper):
premise-level attacks on a registered frame carry evidential weight only against a
sealed decoy null. The audit seat pre-committed a deliberately-wrong premise swap,
sealed the reading "≥ 2 decoy refuters ⇒ K0", and its own headline finding — the S034
modality strike — demoted itself to VACUOUS when the corpus handed the decoy the same
refuters ("found it the way a metal detector finds the beach"). **Pre-commit the decoy
BEFORE the sweep; an attack that fires on a frame built to be wrong says nothing about
the frame under test.**

The sweeper gets swept (2026-08-12, the odyssey's coda; the audit seat's adopted
phrasing): a claim from a trusted seat, amplified because it was well-put, is the
failure species no synonym set catches — **verify-don't-trust binds to the PREMISE
regardless of who supplied it.** Species instance, both directions in one thread: the
banking seat's two-field compositum line (dropped the √−7 leg; B704 banks three) was
amplified unchecked by the audit seat as "the most valuable single line"; caught only
when the B704 grep ran. Twin species: window-read-as-whole struck twice in the same
thread (both seats truncated B733 one line above its explicit B704 bridge citation).

Provenance of debts and blockers (2026-08-13, from species #13 and #14 — one rule,
two faces): **a debt row carries its COMMISSIONING SOURCE the way a law row carries
its arc** (the manual misattribution survived both benches' ledger discipline
because ledgers police shrinkage, not provenance); **a blocker row carries its
BLOCKING REASON, one of {theorem, missing datum, fence, not-run}** — a row that
cannot name which is a NOT-RUN until proven otherwise ("blocked" and "not-run" are
different words this corpus had been spending as synonyms; the scrutiny's score:
seven blockers examined, four were not blockers, and none of the three genuine ones
was a wall). Enforcement: MANUAL at write-time; a gate-shaped check is a digest-
window candidate.
