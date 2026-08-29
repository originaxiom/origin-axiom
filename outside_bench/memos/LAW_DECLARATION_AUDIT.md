# R52-6 COLD PASS — the paper's claim base is drawn from a field that 89% of the corpus never filled in
## (outside bench memo 133, 2026-08-29; certificate `certificates/law_declaration_audit.py`, GREEN; R52-6, the item the owner assigned this seat)

**The lead.** B1211 corrected **one** arc's `creates_law` flag (B1196,
declared false, should be true) and recorded exactly why it matters:
*"the registry gate reads the DECLARED field, so an under-declaration
made this arc invisible to it **and to B1210's claim-pool sweep**."*
B1210 builds the paper's claim pool from that field. cc reports the spine
now carries ~55 claim candidates with an empty disposition column. **If
the field is wrong anywhere else, the paper is being assembled on an
incomplete base — and the defect is invisible because the sweep that
builds the base reads the same field that is wrong.** B1211 fixed one
instance by hand. This cell asks whether the instance was a class — the
move that already paid off twice here (the finished-but-forgotten class,
GC-29 / R52-1).

**The criterion, fixed first and deliberately NOT the declared field:** a
settled arc (PROVED/NEGATIVE) not declared law-creating, whose own
`claim_one_line` carries the corpus's own law vocabulary (theorem, law,
forced, no-go, impossible, unique, exactly, necessary and sufficient,
cannot, never, always, iff, permanent).

**The two-sided control, run before the finding:** declared-law arcs score
**2.20** on that vocabulary against **1.00** for the rest — **2.20×**. The
criterion discriminates, so it is not noise. *(Had it not, the cell exits
and reports itself void — that branch is in the code.)*

## THE FINDING

| | |
|---|---|
| settled arcs (PROVED/NEGATIVE) | **1031** |
| `creates_law` declared **true** | **55** |
| `creates_law` declared **false** | **56** |
| **`creates_law` ABSENT ENTIRELY** | **920** |

> **The field was only ever filled on ~11% of settled arcs. B1210's claim
> pool — and therefore the paper's claim base — is drawn from a field that
> 89% of the corpus never populated.**

**Two distinct failure modes, and B1211 fixed the rarer one.** A
*mis-declaration* (B1196 said false) is a wrong call; an *absent* field is
**no call ever made**. A sweep that reads the field treats both
identically — as "not a law". Of the credible candidates, **81 have the
field absent and 21 have it declared false.**

**Candidate under-declarations:** 118 raw hits at or above the
declared-law mean, **minus 16 declared `instrument = true`** (process, not
content — excluded before reporting, so the narrowing is visible rather
than silent) ⟹ **102 credible candidates, against 55 currently in the
pool.**

## ⚠ THE DECISIVE EXHIBIT — this is not a borderline editorial call

**B991** — verdict **PROVED**, `instrument: false`, `creates_law`
**absent**. Its own claim:

> *"THE HYPERCHARGE NORMALISATION IS NOT DERIVABLE IN PRINCIPLE, and that
> is a THEOREM ABOUT THE EQUATIONS rather than a limitation of the
> object."*

**An explicit no-go theorem, invisible to the paper's claim pool.** The
arc says *theorem* in its own words. One exhibit is enough to settle that
the class is real; the statistic only says how large it might be.

## WHAT THIS DOES AND DOES NOT SAY

**It does not say all 102 should be reclassified.** Law-shaped language is
**evidence**, not proof, and several hits are plainly audit or sweep arcs
that simply lack the `instrument` flag (which is itself under-used). This
cell **reclassifies nothing** — it reports and ranks.

**It does say** the paper's claim base was assembled by a sweep over a
field with a **demonstrated failure mode and 89% non-coverage**, so
**the base should be re-audited before the disposition column is filled**
— because filling dispositions over an incomplete pool bakes the omission
into the paper, permanently and invisibly.

**Recommended, and cheap:** run the ranked list past the same editorial
call B1211 made for B1196, then regenerate B1210's ledger. Start with the
21 declared-false hits (someone made a call there and may have made it
wrong) and the explicit-theorem absentees like B991.

**Fence.** Repository metadata only; no object claim. The vocabulary
heuristic is deliberately not the declared field — that is the point —
but it is not a proof of law-hood either. Gate 5 untouched.

## R52-6's OTHER COMPONENTS, dispositioned by this cold pass
- **D2's scope choice — DISCHARGED** (confirmed by the owner this session;
  see the relay note: main still carries it as PROVISIONAL and should lift).
- **The census's 31 category calls — VOID AS WORDED.** B1196 already
  established that "census-31-calls" is a **label collision** — an
  unrelated queued cc3 artifact sharing the tag D2. The review item
  survived the finding that killed it. If cc3's artifact carries real
  work it needs its **own row under a non-colliding tag**; under D2 there
  is nothing to audit.
- **The L173 mode-COUNT seal path** — not touched here; remains open.
- **The θ-even designed crossing and the specialist send-queue** — **HOLD
  by the owner's word**, untouched, and released only by the owner.
