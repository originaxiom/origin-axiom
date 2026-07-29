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
| `PROGRESS_LOG` and `CHANGELOG` are updated together | **GATED** | `log-changelog-paired` |

### Claims and the firewall

| practice | enforcement | mechanism |
|---|---|---|
| `CLAIMS.md` rows well-formed; every PROVEN row cites an existing test | **GATED** | `claims` |
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

### Cadence

| practice | enforcement | mechanism |
|---|---|---|
| Decadal review every ~10 merges | **SCHEDULED** | the `review-due` counter (`python3 scripts/gates/gates.py review-due`) reports it; it is advisory by design and does not fail the suite |
| Prereg sealed, hashed into `SEAL_LEDGER.md`, and **committed before** any computation | **MANUAL** | the seal itself is the evidence |
| Push to `origin` **and** `codeberg` after every banked advance | **MANUAL** | verified at review |
| cc3's branch is **never merged**; deliverables cherry-picked under a new number and verified independently | **MANUAL** | integrate-don't-merge |

---

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

**The mechanism that actually works for these is the PREREGISTRATION**, and this is not a slogan —
it was measured. B799's prereg declared in advance that an all-COMPUTED outcome would be a *warning
sign*, and when the result came back with five honest downgrades, that pre-commitment is what made
the outcome interpretable instead of self-congratulatory. A prereg forces the judgement **before**
the answer is visible, which is the only moment at which judgement is cheap.

So: **for anything judgement-shaped, seal a prereg with a two-outcome criterion.** That is the
closest thing to a gate that judgement admits.

---

## Maintaining this file

This register is itself gated — `practices-register` checks **both directions**:

1. every row marked **GATED** names a gate that actually exists in `scripts/gates/gates.py`; and
2. every gate in `scripts/gates/gates.py` appears somewhere in this file.

Direction (2) is the one that matters for drift: **a gate added without a row here would make this
register quietly incomplete**, which is precisely how `knowledge/INDEX.md` lost four entries. The
same both-directions check that fixed that fixes this.

When a practice is agreed in conversation, it is **not** agreed until it has a row here.
