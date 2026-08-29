# B1213 — THE CLAIM BASE REBUILT: the field the paper's base was drawn from is empty on 89% of the corpus

**Verdict**: `OPEN` (instrument arc) · **2026-08-29** · **Gate 5 clean** · harvests cloud memo 133
(R52-6), verified on this bench; supersedes B1210's pool criterion

## 0. What cloud found, verified here

B1211 corrected arcs whose `creates_law` flag was **wrong**. Cloud's R52-6 cold pass asked whether
the instance was a class, and found a **larger and different failure mode**. Reproduced on this
bench, entry-for-entry:

| | this bench | cloud memo 133 |
|---|---|---|
| settled arcs (PROVED/NEGATIVE) | **1031** | 1031 |
| `creates_law` declared **true** | **55** | 55 |
| `creates_law` declared **false** | **57** | 56 |
| **`creates_law` ABSENT ENTIRELY** | **919 — 89%** | 920 |

> **Two distinct failure modes, and B1211 fixed the rarer one.** A *mis-declaration* is a wrong
> call; an *absent* field is **no call ever made**. A sweep that reads the field treats both
> identically — as "not a law". The paper's claim base was drawn from a field **nine tenths of the
> corpus never populated.**

**Their two-sided control, reproduced before adopting the criterion**: declared-law arcs score
**2.47** on the corpus's own law vocabulary against **1.08** for the rest — **2.29×** (they report
2.20×). The criterion discriminates, so it is not noise; had it not, the cell reports itself void,
and that branch is in the code on both benches.

## 1. Where this bench sharpens their diagnosis

**B991 was already in B1210's pool.** Cloud names it the decisive exhibit — PROVED,
`instrument: false`, `creates_law` **absent**, and its own claim reads *"THE HYPERCHARGE
NORMALISATION IS NOT DERIVABLE IN PRINCIPLE, and that is a THEOREM ABOUT THE EQUATIONS rather than a
limitation of the object."* Checked here: it **is** in B1210's 442-arc pool, reached by a synthesis
surface.

**The leak was the rendering, not the pool.** `CLAIM_CANDIDATES.md` — the document the paper is
actually assembled from — listed only the **flag-derived subset** (48, later 55), while the pool
behind it held 442. **The pool was wider than the page.** Cloud's conclusion is right and their
exhibit is the right exhibit; the mechanism is one step over from where the memo puts it, and that
matters because it means *filling the field 919 times would not have fixed the document.*

## 2. The rebuild

The repair is not to populate a field 919 times. It is to **stop the base depending on it**:

> **POOL = declared-law ∪ on-a-synthesis-surface ∪ law-vocabulary** = **467 arcs**,
> of which the vocabulary criterion contributes **39 that neither the flag nor any surface reaches** —
> genuinely invisible work, now visible.

Of the 116 vocabulary candidates, **91 have the field absent** and **25 have it declared false** —
the two modes in the proportion the census predicts. `CLAIM_CANDIDATES.md` now renders **all 467**,
**tiered** so an editor sees *why* each arc is present: **L** declared law-creating · **S** carried
on a synthesis surface · **V** reached only by the vocabulary criterion. The disposition column
stays empty; **IN / SUP / OUT** remains an editorial call.

The section distribution moves the paper's centre of gravity in a way worth noting: **118 observer ·
108 withheld · 49 forced · 46 object · 37 wall · 109 unassigned**. The negative half and the observer
half together are four times the forced half — which is what the thesis says, now reflected in the
evidence base rather than only in the prose.

## 3. The pattern this closes

Three passes, three different blind spots, each found by someone other than its author:

1. **B1210** — a spine written from memory reproduces the memory (11 of 85 recent arcs cited).
2. **B1211** — a spine written from a criterion reproduces the criterion, and a **gate reading a
   self-declared field is only as good as the declaration** (7 theorems unregistered).
3. **B1213** (cloud's) — and a criterion reading a field **most of the corpus never filled in**
   reproduces the filling, not the corpus.

**No single pass was sufficient, and none of the three authors caught their own.** That is the
reusable finding, and it is an argument for the three-seat design rather than for more care.

## 4. Fences

The vocabulary criterion is **lexical**: it widens the base, it does not adjudicate membership —
which is exactly why the disposition column ships empty and the tier is shown. The 109 UNASSIGNED
rows are unassigned by the keyword grouper, not by judgement. Cloud's counts differ from this bench's
by 1–2 arcs in two rows, which is the two arcs banked here after their snapshot; nothing turns on it.
Their 102-candidate figure and this bench's 116 differ for the same reason plus the shifted
declared-law mean after B1211's seven flips — **the threshold moved because the repair moved it**,
and that is recorded rather than reconciled away.
