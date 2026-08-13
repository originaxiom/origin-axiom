# Review 1 — the consolidation seat's own window (qB1024–qB1053, thirty arcs)

*Branch-local, on the consolidation-refresh seat's branch. **This branch never merges**; this review is
harvested at main's digest like everything else the seat produces. Commissioned 2026-08-12 by cc
(main's banking seat) with the owner's permission, under three conditions: the extended protocol
of `REVIEW_TEMPLATE.md`; **E37 discipline stated next to every number**; and **the review gets
reviewed** — main's digest re-grades its load-bearing claims, which is where the independence a
self-review structurally lacks arrives.*

**Why it is not in `REVIEWS.md`.** That file carries **main's** numbering, and a "Review 1"
heading inside it collides with main's own Review 1. This is the consolidation seat's first
review, on a branch that never merges, so it is a standalone document.

**Every number below is produced by `frontier/B1054_review_one/verify.py`** — no arguments, no
network required, re-runnable by the digest. 68/68 checks pass at this anchor. Where the review
quotes a figure, the instrument measured it; where the instrument only *records* a figure without
locking it, that is deliberate (**E38**: a review that pins an absolute count inside a programme
whose purpose is to move it breaks the moment the work succeeds — this window found two live
instances of exactly that and repaired both).

**E37, the standing scope.** This window both measures the corpus and is part of it. Every
denominator below that measures this window **excludes this window's thirty arcs**, and says so
in the same sentence. Eleven E37 instances inside thirty arcs say it will try to happen again.

**Grades used throughout, per cc3's digest protocol:**
**RUN** — the original script executed. **REBUILT** — produced from banked inputs without the
original code (a weaker grade; labelled). **NOT-REACHED** — examined by nobody this pass;
countable, and never an implied rejection.

---

## 1. The loop — what Review 1 inherits

**Nothing parseable, and the reason is not the one the commission assumed.**

The commission read this as *"a first review with no loop to inherit."* True in effect, wrong in
cause. **Review 42 exists on this branch.** What does not exist is a machine-readable loop: the
**last `### Action items` block on this branch is Review 37**; Reviews 38, 39, 40, 41 and 42 carry
none. Main resumed the practice at **R43 and R44** — *after this branch forked* — so the gap is
**branch-local**, not a gap in the programme. (REBUILT from `docs/progress/REVIEWS.md` on both
sides; `git show origin/main:` for the comparison.)

A related structural note, met inside item 1 itself: **Review 42's heading is a single `#`** where
38–41 are `##`. A `^## Review` sweep does not see it. That is the same defect species this window
spent thirty arcs naming — *a check matching TEXT while the meaning lives in STRUCTURE* — and it
appeared in the very first thing this review tried to measure.

### The one item that IS inherited, and it is escalated

**`TOOLBOX.md`.** Review 42 named it by name at lag 638, *"TWO reviews old,"* with the sentence
*"it does not survive a third review undeclared."* R43 carried it as R43-1; R44 carried it as
R44-1. **At this anchor the lag is 684** (RUN: `scripts/checks/doc_currency.py`), and it remains
the largest declared currency debt on the board, ahead of `THEOREM_LEDGER` (50),
`GUT_REQUIREMENTS_LEDGER` (101) and `CLAIMS.md` (17).

**This review is the third.** And it must be honest about what it can do: `TOOLBOX.md` is a
main-side document, this branch never merges, and a refresh written here would never reach the
reader it is for. **So this review does exactly what R42 said must not happen a third time — it
declares the debt and does not discharge it.** That is the correct disposition for a non-merging
seat and it is also an admission. Registered **R1-1, owner MAIN**, with the observation that the
item has now survived three reviews because each review that sees it is not the one that can fix
it — a routing defect, not a diligence defect.

## 1b. The branch inventory — and a defect in item 1b's own instrument

`git branch -r --no-merged` is the template's named instrument. **On this container it returns one
ref.** `git ls-remote --heads origin` returns **three**:

| ref | sha | state |
|---|---|---|
| `main` | `6d52d65` | the trunk |
| the consolidation-refresh seat (this branch) | `5b26e51` | this seat, LIVE — main's R44-5 (*"digest the cloud seat's branch on completion"*) |
| `audit/b775-braver-questions` | `d71732b` | the relay audit seat (cc3), LIVE |

**`git branch -r` answers from the refs the clone happens to hold, not from the remote.** This
clone had fetched two branches, so the audit seat's branch — a LIVE ref that main's R43/R44 both
inventory — was invisible to the command the protocol names. Nothing was concealed; the
instrument simply reports its own cache. **Registered R1-2, owner MAIN**: item 1b should specify
`git ls-remote --heads`, which reads the ground.

**NOT-REACHED:** the Codeberg mirror. R43 ran the inventory *"on both remotes"*; this container
has only `origin`. Not checked, not implied clean.

## 2. Declared modulus

**Window = qB1024 → qB1053, thirty arcs, no gaps** (instrument: `modulus_has_no_gaps`).
Opens at **B1024** — the fork seal, the one arc both sides carry, sealed `dc823e86` and the only
arc in the window with a `PREREGISTRATION.md`. Closes at **qB1053**.

**Citation convention** (binding, per the commission): this seat's arcs are cited **qB1024–qB1053**
and its leads **qL155–qL166**, because main independently banked **B1025–B1044** in the same range.
Main reserved **B1045–B1059** never-assigned; **B1054–B1059 are this branch's**, and this review
banks B1054. Main continues at B1060.

> **⚠ The resolver named in the commission is not on main.** A `CLOUD_ALIAS_TABLE.md` under `docs/` —
> stated as *"the permanent resolver, banked"* — **does not exist at `main@6d52d65`**, checked at
> both `docs/` and the repository root. The convention is followed here as instructed, but it
> currently travels on cc's word rather than on a banked artifact, which is precisely the failure
> mode this window has been cataloguing. **Registered R1-3, owner MAIN.**

Every arc was authored and banked by this seat in-session, read in full by construction. All
thirty carry an `arc_verdict.json` and a `FINDINGS.md`. **Anchor: `5b26e51`**, the window's last
bank (the known-green suite pin).

## 3. Advancement

**Twenty-seven `LAW_MAP` rows cite this window** (REBUILT from `docs/LAW_MAP.md`). Their kind
matters more than their number, and the instrument splits them:

| kind | rows |
|---|---|
| **RESTORE** a result the curated tier had lost | **12** |
| **RE-VERIFY / COLLECT** an existing result | **4** |
| **NEW** statement | **11** |

**Restorations are the largest class, and that is the correct reading of this window: it was a
consolidation, not a discovery run.** Twelve laws that the corpus had proved and then dropped are
back on a curated surface, each re-verified before restoration rather than cited from memory
(campaign step 5) — the metallic fixed line as Dickson over `ℤ[m]`, the two-block rank-1
obstruction, the seam field's conductor law, the projective wall found separately by six arcs, the
Painlevé-VI partner, the trivial-point tower's two Sym bands.

### The finding in this section: all twenty-seven rows are in one section, and seven do not belong there

`LAW_MAP` §A is **"The object's arithmetic (the solo laws)."** All 27 window rows landed there;
§§B, C, D, E and F took **zero**. But at least **seven** of them state nothing about the object's
arithmetic at all — *"naming a mechanism did not gate it," "naming is not registering," "the band
is the wrong unit," "the debt number counts rows; the debt is laws," "the knowledge room's rule is
prose-only," "the shadow library," "the representation gate cannot see two-thirds of the corpus."*
Those are findings about the **programme**.

**`LAW_MAP` has no section for them.** §D is titled "the meta-laws (the program's spine)" but its
43 rows are object/observer physics, not methodology. So this is a **structural gap, not a
filing slip**, and it is not a reviewer's call to invent a section. **Registered R1-4, owner
OWNER**: either §A's scope sentence widens, or a methodology section exists, or these rows belong
somewhere that is not `LAW_MAP` at all.

**Leads.** Twelve registered this window — **qL155 through qL166**, all open, **all the owner's
calls**. This review **registers** them and does not decide any of them, per the commission.
Stuck longest and named: **qL166** (below), and **qL157** (which five inputs), which is main's
question as much as this branch's.

**Debt.** 245 (the v3 baseline) → **175** as the metric counts it. §8 explains why that sentence
needs its qualifier.

## 4. Error-class recurrence

**Two classes registered this window**, both adopted at qB1042 and both live in
`docs/ERROR_LEDGER.md`:

- **E37 — self-measurement.** *An arc that both measures a gap and fills it invalidates its own
  metric.* Eleven instances inside thirty arcs.
- **E38 — progress-eroded threshold.** *A lock encoding a structural claim as an absolute count,
  inside a programme whose purpose is to change that count.* The window registered **three**
  instances, the third found because a repair had fixed one lock in a file and left its sibling —
  which produced the standing rule **"the repair is not complete until the FILE is swept."**
  **This review found ten more** (§6), including **two inside qB1042's own locks — the arc that
  registered E38** — one of which fired the moment this review added a class to the register E38
  was registered in. Running total: **thirteen**. It is the window's most recurrent class by a wide
  margin, and the recorded figure is deliberately *recorded* rather than locked.

A **third class is registered by this review**, because the §6 finding is neither of the above:

- **E39 — cached verification.** *A lock that asserts over an instrument's committed OUTPUT rather
  than re-running the instrument.* **E38 is a lock that fails when it should not; E39 is a lock
  that passes when it should not.** **Seven live instances**, measured (§6) — six inside this
  window, and **one outside it, qB946, dating to B963**, whose lock never matched its script at all.

**Twenty-four numbered corrections** are published in the window's handoff (§2), and the honest
summary of the taxonomy is that **the window's dominant recurrence is not a mathematical class at
all.** It is one methodological shape with two faces:

1. **Checks matching TEXT while the meaning lives in STRUCTURE** — now **five** instances: a
   per-line exclusion defeated by markdown line-wrapping (qB1049); a row lookup defeated by one row
   quoting another's headline (three occurrences); a `GOVERNANCE` §5 firewall *header* read as a
   verdict, which would have wrongly declined eleven of sixteen B0–B99 rows; blockquote markers
   surviving a whitespace flatten (qB1052); and **the single-`#` Review 42 heading, met in item 1
   of this review**.
2. **Naming is not gating** — a rule written in prose, a mechanism given a name, a register
   created, none of which constrains anything until something executes. This is Review 42's own
   governing finding, and this window **recurred it within two days** (qB1041) and then again
   structurally (qB1042: the error taxonomy had stopped 122 arcs earlier).

### The correction this review found in the window's own correction table

> The handoff's §2 opens: *"**Twelve** were caught by a check, **six** by a re-run, **four** by a
> measurement moving unexpectedly, and **one** was published wrong."*
>
> **12 + 6 + 4 + 1 = 23. The table enumerates 24.** And §2.2's eleven rows carry no
> catch-mechanism column at all, so the partition is **not derivable from the tables it claims to
> summarise** — it cannot be repaired by recounting, only by re-attributing eleven rows.
>
> **qB1052's instrument gated that section with `n_corr >= 20`** — a lower bound standing in for
> an exact four-way claim. The document made a precise statement; the check accepted any number
> above twenty. **This is finding-species (2) inside the instrument built to prevent species (2).**

**Registered R1-5, owner SEAT.** The fix is either an attribution column for §2.2 or the removal
of the partition sentence; the correction count itself (24) is right.

## 5. The 7d certification standard, asked of this window's own thirty arcs

> *"Can a reader arrive at the current state without being misled by any document in it?"*

**No — in one specific, measurable place, and it is this window's own named defect turned on
itself.**

**All thirty arcs carry `verdict: PROVED`.** Not twenty-eight. Thirty.

| | PROVED | NEGATIVE | OPEN | RETRACTED |
|---|---|---|---|---|
| **corpus, this window excluded** (n = 930) | 610 (**65.5 %**) | 279 | 31 | 10 |
| **this window** (n = 30) | **30 (100 %)** | 0 | 0 | 0 |

Against a 65.5 % base rate measured with this window excluded, **P(30/30) ≈ 3 × 10⁻⁶**. This is a
convention, not a coincidence. And the bodies do not agree with it: **eighteen of the thirty**
carry retraction, refutation, decline or non-finding language, and **two — qB1035 and qB1041 —
declare an outright NON-FINDING in the body while the metadata says PROVED.**

**This is qL166.** The window's own lead reads: *"fourteen arcs say PROVED in their metadata and
something else in their body,"* and its real cost, recorded there, is that the defect made those
arcs invisible to the owner-directed negatives hunt of 2026-07-21, **which selected on banked
negatives.** A future hunt run the same way **will not see one of this window's thirty arcs** —
including the two declared non-findings and the one overstatement this window published and
retracted.

**The control that makes this fair, and it cuts both ways.** The *same thirty arcs* carry an atlas
`status` field, and **that one discriminates**: **banked 18 · dead 9 · dormant 1 · open 2**. The
seat did make the judgement, arc by arc, and recorded it — **just not in the field the negatives
hunts select on.** So this is a **routing failure between two metadata fields**, not an absence of
judgement, and the repair is correspondingly cheaper than the finding first sounds. It is also,
exactly, the shape of everything else this window found: the information exists, and nothing
carries it to the place that reads it.

**On what the convention MEANT — cited, not re-adjudicated.** cc3 independently reproduced this
finding within an hour of reading it: **28 candidates corpus-wide, epoch-shaped — 13 below B100,
11 in the middle, 4 recent** — with the warning that **the early verdict convention must be
understood before old rows are read as errors**. Main's digest holds the metadata lane and this
review defers to it. **Two benches deriving the same finding separately is the evidence; a third
seat re-adjudicating it alone would be worth less than either.** The same convergence happened
with dispositions: cc3's *"NOT-REACHED is a first-class disposition"* and this seat's *"a decline
is a disposition"* were derived independently. **That convergence is marked as such** — it is the
strongest practice-level result either bench produced this cycle.

For this window specifically the reading is narrower and harder to excuse: these thirty arcs were
banked *after* qL166 was written. **The seat that named the defect kept instancing it for eleven
more arcs.** **Registered R1-6, owner OWNER** (the convention is the owner's to set) **with
R1-7, owner SEAT**: whatever the convention turns out to be, this window's thirty rows are
re-graded against bodies, not re-labelled by rule.

## 6. Provenance and protocol integrity

### The finding that outranks everything else in this review: six red instruments and a green suite

**At `5b26e51` — the branch tip this review anchors on, and the commit whose message is *"Pin the
known-green suite at be87a51 — 3996 passed, 0 failed"* — six of the thirty arcs were RED, and the
suite could not see it.**

Proven on two pristine worktrees of that exact commit:

| | result |
|---|---|
| `pytest` over those six arcs' locks, **caches untouched** | **46 passed, 0 failed** |
| re-running those six `verify.py` scripts | **all six RED** |

The six: **qB1042 · qB1043 · qB1046 · qB1047 · qB1049 · qB1052.** Every one ships a
`results.json` recording `all_pass: true`.

**The mechanism is structural, not sloppiness.** An arc's lock asserts over its arc's
`results.json`. That file is a **cache**, written once at banking time and committed. A
consolidation window's entire job is to edit the files those instruments measure — and nothing
re-runs the instrument. **So the lock validates the cache against itself, and cannot see the drift
by construction.**

**This is Review 42's governing finding — *"two locks were red at HEAD, and nobody knew"* — in its
third and worst form.** qB1041 found it recurring within two days of Review 42 and repaired the red
locks. It kept recurring because every repair fixed *the locks* rather than the fact that **a lock
cannot see its own instrument.**

**A first correction, against this review.** An earlier pass of this section reported *"29
reproducers re-executed, 29 pass, 0 fail"* and graded them **RUN**. That was wrong, and wrong in
this window's own catalogued way: the sweep read **exit codes**, and **28 of the 30 scripts never
exit non-zero** — they print `ALL PASS: False` and return 0. The sweep was measuring a harness that
cannot fail. It is corrected here rather than quietly dropped.

**What each of the six actually was** — and every one is **E37** or **E38**, the two classes this
window itself registered:

| arc | why it was red | class |
|---|---|---|
| qB1042 | its E37 exclusion read `git show **HEAD**:ERROR_LEDGER.md` — correct for one moment, and `HEAD` moves. Fifteen banks later it was reading the *post*-repair register | **E37** |
| qB1043 | its `SELF` filter drops any **line** naming B1043–B1049; a `LAW_MAP` row is one **3793-character line**, and B1040's row mentions B1045 — so the whole row left the measurement, taking B164 · B169 · B150's citations with it | **instrument bug #17, live** |
| qB1046 | asserted *"B408 has no RETRACTIONS row"* — **qB1048 added the row.** The lock failed because the defect it reported was fixed | **E38** |
| qB1047 | pinned `6 / 147` and `**55**`; the corpus grew to 154 rows and 62. *The ledger recorded the movement correctly — only the check froze* | **E38** |
| qB1049 | pinned *"TWO of the four consumers carry the defect"* — a third began to bite as curated prose grew | **E38** |
| qB1052 | pinned one suite sha and pass count, which `5b26e51` itself re-pinned; **and one conjunct asked the handoff for a sha the handoff has never carried, so it was false the day it was written** | **E38** |

**qB1043's is the sharpest.** Instrument bug #17 — *"the line-based fix nuked B117/B122/B121/B118's
citations"* — was found by qB1049, fixed in **four** consumers, and left live here, because this
arc spells the idiom `SELF` rather than as a consumer pattern and so was not in the sweep's list.
**The window's standing rule was "the repair is not complete until the FILE is swept." The rule
needed to be the CORPUS.**

**All six are repaired in this bank**, each to the structural claim rather than to a frozen
integer, with the reason written at the repair site.

### The oldest instance, found by the first full suite run — and it is outside this window

**qB946's lock has been asserting over data its own instrument cannot produce since B963.**

The full suite at `f1a185a` returned **exit code 1**, one failure:
`tests/test_b946_handoff6.py::test_the_residue_primes_are_class_sorted_and_the_base_rate_is_declared`,
`KeyError: 'frobenius_class_of_residue_primes'`. Traced:

- `frontier/B946_solo_handoff6/verify.py` is **unchanged since B963** (zero diff across this
  window) and contains **no occurrence** of `frobenius`, `mixed_class` or `base_rate`.
- Its committed `results.json` nonetheless carried **four such keys**, and the lock asserts over
  all four.
- They survived because **nobody ever re-ran the instrument.** The first regeneration — the
  freshness sweep above — dropped them, and the lock failed.

**This is E39 at its purest, and it is a corpus-wide instance rather than a window one.** The six
in this window drifted because later arcs edited what they measure; qB946's never matched its
script *at all*.

**The values were never wrong.** §8 of qB946's own `FINDINGS.md` states the symbol outright —
**`(6237 | p)`**, from B931/B937's √77 quadratic-resolvent class law — and all six primes
reproduce exactly under it (`6237 = 3⁴·7·11 = 81·77`, so it reduces to `(77 | p)`). **So the repair
is to compute them, not to restore them**, which is the whole content of E39: *a number a lock
asserts must be one the instrument can produce.* qB946's `verify.py` now derives all four from the
residual primes it already computes, and the results are **byte-identical to the cache**.

> **A defect this review introduced, and fixed.** The sweep's first pass **destroyed** those four
> values by regenerating over them; only git still had them. A tool built to expose stale caches
> must not eat the evidence. The sweep now **snapshots before re-running, restores the original
> whenever a re-run loses keys, and reports `KEY-LOSS`** — verified by injecting a canary key and
> confirming both that the guard fires and that the canary survives.

### The systemic fix, and what it costs

`scripts/checks/instrument_freshness.py` re-runs **every** arc instrument in the corpus and reports
any that does not come back green, distinguishing **STALE-GREEN** (the cache claimed green, the
live run is red — the failure above) from **RED**, **CRASH** and **NO-VERDICT**. It currently
returns **ok (28 instruments re-run, all green)**.

**Measured cost: ~5 m 20 s for 26 instruments.** That is **too slow for a per-push gate** — gates
run at every bank — and proportionate inside a suite that already runs ~48 minutes. **So it is
wired as a test (`tests/test_instrument_freshness.py`), not as a gate**, which also puts it exactly
where the blind spot was. **The per-push version is registered as R1-12, not pretended.**

**It earned its place on its first real use, against this review.** Run immediately before banking,
it caught **two more** that this review's own edits had just created — one **RED** (qB1042) and one
**STALE-GREEN** (qB1049), both **E38**, both invisible to the gates, which were 28/28 green at that
moment. The qB1042 one is the sharper: **this review had already repaired that exact count-lock in
`tests/test_b1042_error_ledger.py` and missed the identical lock inside the arc's own instrument.**
The window's rule was *"the repair is not complete until the FILE is swept."* The file *was* swept.
**The rule needs to be the ARC, and then the corpus** — which is what the sweep now does
mechanically, so it no longer depends on remembering.

### Reproducers

All **29** reproducer scripts in the window were re-executed at this anchor and, graded properly —
by re-reading each instrument's own recorded verdict rather than its exit code — **all are green**.

```
python3 scripts/checks/instrument_freshness.py     # the honest form of the sweep above
```

**qB1025 carries no reproducer** — it is the suite-collection repair, whose result lives in the
test infrastructure rather than in an arc script, and **it declares this in its own body**. That
is the correct handling and it is the only arc in the window without one.

**Seals — and the window's weakest showing.** **One arc of thirty is sealed** (qB1024,
`dc823e86`, hash-first, seal committed and pushed before compute). The other **twenty-nine are
unsealed, and only two of them say so.**

The *practice* is defensible: a consolidation arc that measures what a document says is not a
two-outcome prediction, and a prereg would be theatre. **The declaration is not optional, and it
is missing.** Main's R43 and R44 declare every unsealed arc in its header — *"B1035 and B1038
openly unsealed (a register and a verification arc — declared in their headers)."* This window
banked twenty-nine and declared two. **Registered R1-8, owner SEAT**: a one-line header on each,
or a single declared class rule for consolidation arcs, stated once and cited.

**Provenance sweep, REBUILT:** no external-verification pretense in the window's public-facing
files; every restored `LAW_MAP` row names the arc it restores and was re-verified before
restoration. The `B58` directory collision surfaced by the dedupe is **grandfathered by name** in
`gate_id_collisions` under §12's no-renaming rule — a governed exception, not a defect.

## 7. The §5.1 promotion sweep

**Zero promotions. The firewall held.** `CLAIMS.md` carries exactly **two** citations of this
window's arcs, and **neither is a promotion**: qB1036 re-labelled a line that had read "the
current theorem," and qB1034 added a name-collision warning about `κ`. Both are **corrections to
existing text**, which is what a consolidation window should be putting on that surface.

`CLAIMS.md` insertion stays deferred with the blocker named — it is itself a declared currency
debt (lag 17), unchanged from R43 and R44.

## 8. The headline finding — the window's own metric triages on the field its own lead forbids

The number this window published most often is the consolidation debt: **245 → 175**. Its
definition, in the instrument:

```python
if v.get("verdict") == "PROVED" and not v.get("instrument") and not cited(f"B{n}"):
    debt += 1
```

**It selects on `verdict:`.** That is the exact operation cc3's protocol makes forbidden and that
this window's own qL166 exists to warn against. Measured:

| | arcs |
|---|---|
| uncited, non-instrument, **counted** by the metric (`PROVED`) | **175** |
| uncited, non-instrument, **invisible** to it (`NEGATIVE` 171 · `OPEN` 16 · `RETRACTED` 4) | **191** |
| **the metric's share of its own subject** | **48 %** |

**The metric is blind to more arcs than it counts.** The 171 uncited `NEGATIVE` arcs are the
sharpest case: `LAW_MAP` §E — *"The walls (proved impossibilities — kept dead)"* — is the curated
home for exactly that material, and it holds **six rows**. The four uncited `RETRACTED` arcs are
unambiguous debt under any reading.

**This does not make 175 wrong.** It makes it an answer to a narrower question than the sentence
around it implies: *"how many arcs with a positive verdict are uncited"* — not *"how much of the
corpus a curated surface fails to carry."* **Registered R1-9, owner SEAT**, and flagged to
**MAIN/DIGEST** as the load-bearing claim of this window most worth independent re-grading.

## 9. Honest assessment, and what this review did not reach

**What the window did well.** It read bodies rather than claim lines, and that is where every real
finding came from. It published twenty-four corrections against itself, including one that
inverted its own plan and one that reached a curated surface. It discarded a green suite because
the run described no commit. It refused to decide twelve leads that were the owner's to decide,
after measuring each one. It recovered from three container rewinds, each caught because a number
moved and was not explained away.

**What it did badly, in one sentence:** it kept its own metadata to a lower standard than the
metadata it audited — thirty uniform verdicts, twenty-nine undeclared unsealed arcs, and a
headline metric selecting on the very field its own lead flagged.

**The deeper pattern, offered as opinion and marked as such.** Every finding in this window
reduces to the same shape: *a rule exists in prose, and nothing executes it.* The programme is
unusually good at writing rules and unusually good at building gates, and the gap between those
two activities is where all thirty arcs found their material. The rules are not the problem and
the gates are not the problem — **the routing between them is unowned**, and this review's item 1
is the same defect at governance level: a debt that three consecutive reviews have declared
because none of the reviewers that see it is the one that can fix it.

### NOT-REACHED — countable, and not an implied rejection

1. The **Codeberg mirror** branch inventory (§1b) — this container has only `origin`.
2. **Main's B1025–B1044**, banked since the fork, including the pattern-meditation campaign. Per
   the commission this review does not address them; they meet this window at the digest.
3. **The other 931 arcs.** This review's modulus is thirty. Nothing here grades the rest of the
   corpus, and the §5 and §8 base rates are measurements *of* it, not judgements *on* it.
4. **`TOOLBOX.md` content.** Declared at lag 684, not read, not refreshed (R1-1).
5. **The twelve leads qL155–qL166.** Registered, measured, **undecided by design**.
6. **The full serial suite at this review's own commit** — run and pinned at bank time (§ below),
   not at the time these words were written.

### Action items (Review 1)

- [ ] R1-1: `TOOLBOX.md` — lag 684, now **three** reviews declared and undischarged; the routing is the defect, not the diligence (owner: MAIN; source: R42 → R43-1 → R44-1, and this review)
- [ ] R1-2: template item 1b should name `git ls-remote --heads`, not `git branch -r` — the latter answers from the clone's cache and missed a live branch here (owner: MAIN)
- [ ] R1-3: the `CLOUD_ALIAS_TABLE.md` resolver is **not present under `docs/` at `main@6d52d65`** though the commission cites it as banked; the qB/qL convention currently has no artifact (owner: MAIN)
- [ ] R1-4: 27 window rows sit in `LAW_MAP` §A; at least 7 state programme methodology, and no section exists for them — widen §A's scope, add a section, or re-home the rows (owner: OWNER)
- [ ] R1-5: the handoff's catch-mechanism partition sums to 23 against 24 numbered corrections, and §2.2 carries no attribution column; qB1052 gated it with `>= 20` (owner: SEAT)
- [ ] R1-6: the `verdict:` convention — 30/30 `PROVED` against a 65.5 % corpus base rate (window excluded); qL166's disposition (owner: OWNER; cite cc3's 28-candidate reproduction, do not re-adjudicate alone)
- [ ] R1-7: re-grade this window's thirty verdicts **against bodies**, whatever convention R1-6 settles — never by relabelling rule (owner: SEAT; blocked by R1-6)
- [ ] R1-8: 29 unsealed arcs, 2 declaring — add the declaration, per R43/R44's standard (owner: SEAT)
- [ ] R1-9: the consolidation-debt metric selects on `verdict:` and shows 48 % of the uncited population; re-state the published figure with its qualifier, or widen the metric (owner: SEAT; **flagged to MAIN/DIGEST as this window's load-bearing claim most worth independent re-grading**)
- [ ] R1-10: the twelve leads qL155–qL166 remain open and are the **owner's** calls; this review registered and did not decide them (owner: OWNER)
- [ ] R1-11: main's R44-5 — *"digest the cloud seat's branch on completion"* — this review and its handoff are the input for it (owner: MAIN)
- [ ] R1-12: a **per-push** instrument-freshness check — the sweep costs ~5 m 20 s and so runs as a suite test, not a gate; a cheap staleness proxy (results.json older than any file its instrument reads) would close the window between banks (owner: SEAT)
- [ ] R1-13: **28 of 30 arc instruments never exit non-zero on failure** — they print `ALL PASS: False` and return 0, so any harness reading exit codes certifies nothing; give the arc-instrument template a `SystemExit` (owner: SEAT; this review's own first draft was wrong because of it)
- [ ] R1-15: `docs/RECURRENCE_ATLAS.md` is generated by `scripts/atlas/render.py` and has **no freshness gate** — `views-generated` covers only `docs/views/`. It went stale when B1054 banked and surfaced only because `tests/test_atlas.py` **writes that tracked file** during the suite, dirtying the tree on every run (owner: SEAT)
- [ ] R1-16: qB946's four Frobenius keys are now computed rather than cached — **sweep the corpus for the same shape**: locks asserting over `results.json` keys their instrument does not produce. The freshness sweep's `KEY-LOSS` disposition finds them (owner: SEAT)
- [ ] R1-14: the corpus-wide sweep of instrument bug #17 — qB1049 fixed four consumers by name; qB1043 carried the same idiom under a different variable name and stayed broken. Sweep by IDIOM, not by list (owner: SEAT)

**Next review due after 30 arcs banked from this anchor** — *not* after 20 merges. cc3's finding
that **the merge-counting trigger cannot see a non-merging seat** is the reason this window went
sixty-three merges without a review; a non-merging seat needs a unit it actually produces.

anchor-commit: `5b26e51` (the window's last bank, the known-green suite pin)
