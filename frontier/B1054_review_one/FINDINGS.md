# B1054 — Review 1: the consolidation seat reviews its own window, and finds its own defect in it

**Status: banked (frontier). Firewalled; nothing to `CLAIMS.md`. The artifact is
`docs/progress/REVIEW_1_CONSOLIDATION_SEAT_2026-08-12.md`; this arc is its instrument.**

> **⚠ VERDICT CONVENTION, DECLARED — the first arc in this window to do so.**
> This arc's `verdict: PROVED` means **"the measurements below were computed and hold at this
> anchor."** It does **not** mean the window it reviews is in good order; §3 below says it is not.
> The declaration is here because **the review's own load-bearing finding is that this window
> banked thirty arcs with an undeclared verdict convention** (qL166), and a review that names that
> defect while committing it a thirty-first time would be worth nothing. **R1-6/R1-7 remain the
> owner's calls; this is a declaration, not a new convention.**

## Why this arc exists

The owner granted, and cc (main's banking seat) commissioned, the **decadal review of this seat's
own window — qB1024–qB1053, thirty arcs — run by this seat, on this branch**. The argument for
inverting the usual "a seat does not review itself" rule is structural: this branch forked before
main's Review 43, so **main's R43 and R44 could not see this window**, and no other seat holds the
context. The self-measurement hazard is this window's own **E37**, and the commission answers it
with **structure rather than prohibition**: main's digest re-grades the review one step later.

That only works if the digest can **re-run** the numbers instead of re-reading the prose. So every
countable claim in the artifact is produced here — no arguments, no network required, **53/53
checks pass**.

## What the review found, ordered by how badly it reflects on the window

### 1. All thirty arcs say `PROVED`. That is this window's own qL166, instanced thirty times.

| | PROVED | NEGATIVE | OPEN | RETRACTED |
|---|---|---|---|---|
| corpus, **this window excluded** (n = 930) | 610 (**65.5 %**) | 279 | 31 | 10 |
| **this window** (n = 30) | **30 (100 %)** | 0 | 0 | 0 |

**P(30/30) ≈ 3 × 10⁻⁶** against a base rate measured with the window excluded (**E37**). And the
bodies disagree: **eighteen of thirty** carry retraction, refutation, decline or non-finding
language, and **qB1035 and qB1041 declare an outright NON-FINDING in the body**.

qL166's recorded cost is that this defect made fourteen arcs **invisible to the owner-directed
negatives hunt of 2026-07-21**, which selected on banked negatives. A hunt run the same way today
**would not see one of these thirty arcs**. These arcs were banked *after* qL166 was written.

**THE CONTROL, and it is the fair reading:** the same thirty arcs carry an atlas `status` that
**does** discriminate — **banked 18 · dead 9 · dormant 1 · open 2**. The judgement was made and
recorded; it is not in the field the hunts read. **A routing failure between two metadata fields,
not an absence of judgement.**

### 2. The window's headline metric selects on the field its own lead forbids.

The consolidation debt — the number this window published most, **245 → 175** — is defined
`verdict == "PROVED" and not instrument and not cited`. Measured:

- **175** uncited arcs counted;
- **191** uncited arcs invisible to it (`NEGATIVE` 171 · `OPEN` 16 · `RETRACTED` 4);
- **the metric shows 48 % of its own subject.**

The 171 uncited `NEGATIVE` arcs are the sharp case: `LAW_MAP` §E is the curated home for proved
impossibilities and holds **six rows**. This does not make 175 wrong — it makes it the answer to a
narrower question than the sentence around it implied.

### 3. The handoff's correction tally does not sum, and its instrument gated a bound.

§2 of the handoff opens *"Twelve were caught by a check, six by a re-run, four by a measurement
moving unexpectedly, and one was published wrong."* **12 + 6 + 4 + 1 = 23; the table enumerates
24** — and §2.2's eleven rows carry **no catch-mechanism column**, so the partition is not
derivable from the tables it summarises. **qB1052 gated that section with `n_corr >= 20`**: a lower
bound standing in for an exact four-way claim.

### 4. Twenty-nine unsealed arcs; two declare it.

One arc of thirty is sealed (qB1024, `dc823e86`, hash-first). The *practice* is defensible — a
consolidation arc measuring what a document says is not a two-outcome prediction. **The
declaration is not optional**, and main's R43/R44 declare every unsealed arc in its header.

### 5. Template item 1b's own instrument under-reports.

`git branch -r --no-merged` returned **one** ref on this container; `git ls-remote --heads` returns
**three** — the missing one being the relay audit seat's LIVE branch. **The command answers from
the clone's cache, not from the remote.**

## What it found in the advancement, which is the window's better half

**Twenty-seven `LAW_MAP` rows**, split by the instrument: **12 restorations · 4
re-verifications/collections · 11 new**. Restorations are the largest class, which is the correct
reading — **this was a consolidation, not a discovery window** — and each was re-verified before
restoration rather than cited from memory (campaign step 5).

**But all twenty-seven landed in §A, "the object's arithmetic,"** and at least **seven** state
programme methodology rather than arithmetic. `LAW_MAP` has **no section for methodology** (§D's
"meta-laws" are object/observer physics), so this is a structural gap and an owner's call, not a
filing slip.

## The loop, and one item that is now three reviews old

The last parseable `### Action items` block **on this branch** is **Review 37**; R38–R42 carry
none. Main resumed at R43/R44, *after the fork* — so **the gap is branch-local**, correcting the
commission's reading that no prior review existed.

**`TOOLBOX.md` is the inherited item.** R42 named it at lag 638, *"TWO reviews old,"* with *"it
does not survive a third review undeclared."* **At this anchor the lag is 684**, still the largest
declared currency debt. **This review is the third, and it declares rather than discharges** — the
document is main's, this branch never merges, and a refresh written here reaches nobody. **The
routing is the defect, not the diligence.**

## Reproduce

```
python3 frontier/B1054_review_one/verify.py          # 53/53; writes results.json
pytest tests/test_b1054_review_one.py -q
for d in frontier/B10{2,3,4,5}*/; do for f in $d*.py; do python3 "$f"; done; done   # 1024–1053
```

The last line is the review's **RUN** grade: all **29** reproducers in the window were
re-executed at this anchor — **29 pass, 0 fail**. (qB1025 carries none; it is the suite-collection
repair and declares this in its own body.) Everything else in the review is graded **REBUILT** —
produced from banked inputs without the original code — and what nobody examined is marked
**NOT-REACHED** and counted, never implied rejected.
