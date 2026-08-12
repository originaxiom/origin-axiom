# B1052 — the refresh exits through a manual, and the manual is checked against the corpus

**Status: banked (frontier). The consolidation refresh's exit. No mathematics asserted or disturbed;
Gate 5 untouched; nothing to `CLAIMS.md`.**

---

## The problem this solves

**28 arcs, two closed bands, two gates, 27 `LAW_MAP` rows and two dozen recorded corrections — and
none of it transferable if the lessons live in one session's transcript.**

A transcript is the wrong artefact. **Almost all of a session is process**: greps that returned
nothing, measurements re-run after a container rewind, drafts corrected before they were written.
**None of that is evidence.** What a seat needs is what was found, what was corrected, what not to
repeat, and how to re-derive any of it — and the arcs already carry the first and the fourth.

**What the arcs do NOT carry is the second and third**, and those are the expensive ones.

## What was written

**`docs/handoffs/CONSOLIDATION_REFRESH_HANDOFF_2026-08-12.md`**, in the `docs/handoffs/` convention
the repository already had and had used twice — addressed seat to seat, opening by telling the
reader not to read the transcript, and pointing at `ORIENTATION.md` for the *programme* rather than
replacing it.

Six sections: the findings (each citing its arc), **every correction the window made**, the standing
rules ordered by what they cost to learn, an honest assessment including what the author did not
cover, what remains in priority order, and the commands to check the author.

## Why it is VERIFIED rather than merely written

> **Prose is where overstatement lives.** This arc re-measures **every countable claim the handoff
> makes** against the tree: 28 arcs, 4 instruments, 28 gates, debt 245 → 175, 27 `LAW_MAP` rows, 12
> leads, L166's 14 contradictions, the 42/5 supersession graph, 6-of-154 coverage, the 48-minute
> suite. **If any drifts, this arc goes red and the handoff is WRONG rather than stale.**
>
> That is the difference between a manual and a summary.

**And it caught one immediately.** The handoff's first draft said **11 `LAW_MAP` rows added**; the
tree says **27** — it counted only the restorations and missed the audit rows B1030–B1036 each
wrote. **The miscount is recorded in the table itself rather than silently replaced.**

The **honesty clauses** are locked too, because they are precisely the part a later seat cannot
reconstruct: the correction table must exist and enumerate at least twenty entries; the **one
overstatement that actually reached a curated surface** (B141 Item 4, closed by B564) must be named
*separately from the near-misses*; and the author's limits — a third of the corpus read, `snappy`,
`sage`, `cypari`, `flint` all absent — must be stated.

## The fourth markdown-structure bug, and they are all one shape

Writing this arc's checks hit **a blockquote marker surviving whitespace-flattening**: a sentence
inside a `>` block flattens to *"… in > this window …"*, so the match failed on prose that was
perfectly correct.

**That is the fourth in this window, and they are one shape — a check matching TEXT while the
meaning lives in STRUCTURE:**

| # | the bug | cost |
|---|---|---|
| 1 | a per-line exclusion defeated by **line wrapping** | B1037's lock red for five arcs (B1049) |
| 2 | a row lookup defeated by one row **quoting another's headline** | three occurrences (B1047, B1050, B1051) |
| 3 | a **firewall header** read as a verdict | would have declined eleven rows (B1050) |
| 4 | a **blockquote marker** surviving flatten | this arc |

*Stated together here because the shape is more useful than any one instance.*

## And B1049's repair paid, on the arc that documents it

**`retraction-sweep` fired on this handoff while it was still uncommitted.** The draft quoted
B408's headline — *"the one scale lever stands"*, a registered retracted phrase — without a mention
cue on that line.

**B1048 shipped exactly that mistake** and could not have caught it: the sweep listed only
*committed* files, so an arc's own FINDINGS was invisible to the sweep that arc ran. **B1049
repaired it with `-co --exclude-standard`.** This is the first time that repair has paid, and it
paid on the arc whose subject is the window's corrections. *Locked, so the demonstration is not
anecdote.*

## Registered as the campaign's seventh step

**`THE_CAMPAIGN.md` now carries THE MANUAL as step 7:** every refresh window exits through a
handoff, **re-authored per window and naming the previous**, so a later seat reads a chain rather
than doing archaeology. The enforcement rule — *"a window is not closed until its handoff exists and
names its arc range"* — is the refresh's own meta-finding (**naming is not gating**) applied to
itself.

**Registered, NOT gated.** A third instrument in three phases is the **`E34` apparatus-inflation**
this refresh already recorded against itself; whether to gate it is priced for the owner alongside
`L166`.

**Provenance.** `verify.py` (45 checks, every countable claim re-measured) ·
`tests/test_b1052_handoff.py` (9 locks) · the handoff · `THE_CAMPAIGN.md` step 7.
