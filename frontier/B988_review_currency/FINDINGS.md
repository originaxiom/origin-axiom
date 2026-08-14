# B988 — the decadal review now certifies document currency, room by room

**Date:** 2026-08-09 · **Seat:** cc (banking) · **Lane:** repository governance. Gate 5 untouched.
**Owner directive:** *"every decadal review should make sure no single md document is outdated and
doesn't represent / reflect the current state — including claims, theorems, speculations,
philosophy, interpretations, logs, easy read. So whoever reads the repo, human reviewer or AI
agent, understands the complete chain of work, from philosophy to the aAbB principle … all the way
up to symmetry break gauge groups."*

---

## What the review protocol was, and what it missed

Six steps: suite green · gates green · atlas fresh · promotion-candidacy sweep · framing and
stale-leads sweep · dated report. **Every one of them checks arcs or gates. None checked whether
the documents a reader forms their picture from still describe the programme.**

That is why `ROADMAP_TOE.md` stated the position as *"the kinematic/symmetry frame is forced
arithmetic"* for a **month** after B862/B863/B864 falsified it, and why `THE_SM_VERDICT.md` shipped
omitting **eleven of twelve** cascade arcs. Both survived multiple reviews.

## Step 7 — four parts, and none of them optional

**7a — mechanically, first.** `scripts/checks/doc_currency.py` runs and **its output is pasted into
the review report**, including every `frozen` opt-out and every `DECLARED_DEBT` **with its age**.
**A debt older than two reviews is escalated by name.** *A debt is not an exemption* — the direct
lesson of **B982**, where seven gate exemptions rested on an audit that never mentioned them.

**7b — by reading, room by room.** Seven rooms, each with the one question the report must
**answer** rather than assume: **claims** (superseded, retracted, or scoped wider than proved?) ·
**the chain** (can a reader follow philosophy → aAbB → the object → faces, family, both rows → the
algebra → the cascade → symmetry breaking and gauge groups **without a gap**?) · **the negatives**
(is every *"we don't have X"* still a claim with a citation?) · **method** (does this describe how
we *actually* seal, verify and certify **today**?) · **speculation & philosophy** (is the firewall
still one-way, and does the motivation still match the mathematics?) · **interpretation & easy-read**
(can a new reader — human or agent — reconstruct the work from these alone?) · **logs**.

**7c — the named-chain check.** Every waypoint the owner named must be confirmed findable and
current, with the **thin** ones recorded rather than hidden. Today's check is written into the
protocol: eleven well covered; **Markov blanket = 0 arcs and in no document**, carrying a
**conflation hazard** (the corpus is saturated with Markov *triples*, a different object); **feedback
mechanism = 2 arcs**. Both are ladder rungs X31/X32.

**7d — the standard, and the clause that makes it real.**

> *Whoever opens this repository, human reviewer or AI seat, can follow the complete chain of work
> and arrive at the current state **without being misled by any document in it**.*
>
> **A review that cannot assert that names what blocks it.**

That last sentence is the operative one. It forbids a review from passing **silently** over a stale
room — which is exactly how a wrong roadmap survived a month of reviews.

## Scope

**Governance, not mathematics.** It proves nothing about the object. And it is a *reading*
obligation: 7a is mechanical, but 7b–7d are judgement, and their quality is the reviewer's. What
the protocol guarantees is that the judgement is **made and recorded**, not that it is correct.

The currency measure behind 7a is **deliberately crude** (newest-citation lag): a document can be
current while citing nothing recent, or stale while citing a fresh arc. It is **a prompt to read,
not a proof of staleness**.
