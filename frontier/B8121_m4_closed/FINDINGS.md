# B8121 — m4 closed

**Arc dated:** 2026-08-21 · **Seat:** cc3 (audit) · **Lane:** MATHEMATICS.
**Gate 5:** no physical identification claimed in this arc.

> **RECONSTRUCTED 2026-08-26 from this arc's own banked record** (`arc_verdict.json`
> and `results.json`). **This seat stopped writing `FINDINGS.md` at B8110 and the
> omission ran unbroken through B8134 — sixteen arcs.** It went uncaught because the
> lock that detects it lives in a suite too slow to finish inside a session. **This
> document is faithful to the banked record but is NOT contemporaneous, and is marked
> so rather than backdated.**

## Verdict

**PROVED**

M4 IS CLOSED, AND IT WAS REAL BUT SMALLER THAN STATED -- THE SCRUTINY'S OBJECTION OVERSHOT AND
OUR SENTENCE OVERSTATED. Fetched Bowditch's own abstract: BMR give A COMPLETE CLASSIFICATION for
once-punctured torus bundles, precisely three CYCLIC commensurability classes. So M3 is fully
discharged -- our attribution matches verbatim. The scrutiny's M4 objection was aimed at GENERAL
commensurability ('neither need cover the other') and therefore overshot, because BMR's classes
are CYCLIC. But our sentence still overstated what cyclic commensurability delivers: it yields
only that SOME power of one monodromy is conjugate to SOME power of the other, not conjugacy to
a power of a listed word. THE CONCLUSION IS UNAFFECTED, and this was verified rather than
argued: the block-sequence comparison is made between arbitrary powers on both sides, and
exhaustively over j,k <= 8, m=1 matches RL, m=2 matches RRLL, and every 3 <= m <= 12 matches
nothing at any pair of powers, with RLRL matching (RL)^2 as the bite control. REPAIRED: the
proof now states the cyclic strength and why it suffices, the comparison is written power-vs-
power, verify/check_arithmetic_tail.py is added with its bite control, App B gains a row for
thm:arith, and App C records the overstated strength. Suite 21/21 from the extracted tarball,
clean-room green, 51pp. THE SCRUTINY IS NOW FULLY TRIAGED ON ITS FATAL AND MAJOR FINDINGS: 13 of
13 closed. Settles one literature question by fetching the authors' own abstract, and verifies
the downstream argument exhaustively over powers to 8 and m to 12 -- a bounded check, not a
proof for all j,k,m. Does not re-derive BMR. Gate 5 untouched.

## What the arc recorded

### `verdict`

M4 IS CLOSED, AND IT WAS REAL BUT SMALLER THAN STATED -- THE SCRUTINY'S OBJECTION OVERSHOT AND
OUR SENTENCE OVERSTATED. Fetched Bowditch's own abstract: BMR give A COMPLETE CLASSIFICATION for
once-punctured torus bundles, precisely three CYCLIC commensurability classes. So M3 is fully
discharged -- our attribution matches verbatim. The scrutiny's M4 objection was aimed at GENERAL
commensurability ('neither need cover the other') and therefore overshot, because BMR's classes
are CYCLIC. But our sentence still overstated what cyclic commensurability delivers: it yields
only that SOME power of one monodromy is conjugate to SOME power of the other, not conjugacy to
a power of a listed word. THE CONCLUSION IS UNAFFECTED, and this was verified rather than
argued: the block-sequence comparison is made between arbitrary powers on both sides, and
exhaustively over j,k <= 8, m=1 matches RL, m=2 matches RRLL, and every 3 <= m <= 12 matches
nothing at any pair of powers, with RLRL matching (RL)^2 as the bite control. REPAIRED: the
proof now states the cyclic strength and why it suffices, the comparison is written power-vs-
power, verify/check_arithmetic_tail.py is added with its bite control, App B gains a row for
thm:arith, and App C records the overstated strength. Suite 21/21 from the extracted tarball,
clean-room green, 51pp. THE SCRUTINY IS NOW FULLY TRIAGED ON ITS FATAL AND MAJOR FINDINGS: 13 of
13 closed.

### `scope`

Settles one literature question by fetching the authors' own abstract, and verifies the
downstream argument exhaustively over powers to 8 and m to 12 -- a bounded check, not a proof
for all j,k,m. Does not re-derive BMR. Gate 5 untouched.

### `bite_control`

RLRL matches (RL)^2 -- so the instrument can see a match when one exists

### `M3_verdict`

FULLY DISCHARGED -- our attribution ('precisely three') matches the abstract verbatim, and it is
a COMPLETE CLASSIFICATION, not merely a count

### `the_objection`

commensurable manifolds share a common finite cover, neither need cover the other, so 'three
commensurability classes carried by RL, RRLL, RRL' does not entail 'every arithmetic monodromy
is a power of one of those three words'

### `the_precise_defect`

The load-bearing word is CYCLIC. Cyclic commensurability means a common finite CYCLIC cover,
which for surface bundles means: SOME power of one monodromy is conjugate to SOME power of the
other. Our text claimed the stronger 'exactly those conjugate to a power of one of the three
words'. The scrutiny's objection was aimed at general commensurability and so overshot; the
actual defect is that our sentence overstated what cyclic commensurability yields.

### `what_BMR_actually_proves`

Verbatim from the authors' own abstract page: 'We explore when a complete finite volume
hyperbolic 3-manifold fibring over the circle is arithmetic. In the non-compact case, we show
that there are only finitely many cyclic commensurability classes of arithmetic hyperbolic
surface bundles with any given fibre type. WE GIVE A COMPLETE CLASSIFICATION IN THE CASE OF
ONCE-PUNCTURED TORUS BUNDLES SHOWING THAT THERE ARE PRECISELY THREE CYCLIC COMMENSURABILITY
CLASSES. We give a partial result for compact manifolds.' Math. Ann. 302 (1995) 31-60.

### `why_the_conclusion_survives`

The downstream block-sequence argument compares ARBITRARY POWERS ON BOTH SIDES, so it is
insensitive to the weakening. Verified exhaustively: (R^m L^m)^j has 2j blocks all of length m;
matching against (RL)^k, (RRLL)^k and (RRL)^k over all j,k <= 8, m=1 matches RL, m=2 matches
RRLL, and every 3 <= m <= 12 matches NOTHING.

## Depends on

`B8120`

## Scope

As recorded above. Nothing in this reconstruction adds a claim the arc did not bank, and where
the arc recorded a limit, a flag or a self-caught error, that text is reproduced rather than
summarised away.
