# B806 — the instrument built to detect what recurs cannot see anything new, by construction

cc banking seat, 2026-07-29, digging into the owner's standing doubt: *"losing emerging branches,
forgetting context."* **Repository-instrument finding; no physics, nothing to `CLAIMS.md`.**

## The question

The owner has said repeatedly that campaigns designed to survey the whole object keep ending with
*"later we realized there's more in the object."* That is a subjective report. This arc asks whether
there is a **mechanism**, and finds one.

## The chain of measurements

**1. Face attachment is not mechanizable.** 88 % of unattached arcs *name* a face in their text —
but calibrated against the 166 human-classified arcs in `kill_graph`, a keyword classifier scores
**precision 0.45, recall 0.63, exact-set match 13 %**, over-predicting by 55 %. Same failure as the
verdict classifier (7/20, three wrong), same cause: **it reads vocabulary, not content.** *(This
falsifies the 88 % figure this seat had computed minutes earlier.)*

**2. The corpus looks extremely concentrated.** Over 734 probes: **18 distinct motifs; 3 cover
93.3 %; 11 cover 100 %.**

**3. That concentration is the instrument's, not the object's.** The atlas `LEXICON` is **18
hand-authored regex sets**, and its own header states its grounding: *"knowledge/K001..K022,
docs/atlas/GLOSSARY, the HINT recurrence-hints."*

| | |
|---|---|
| lexicon last authored | **2026-07-01** |
| arcs banked since | **409** |
| K-layer now | **25** explainers — **K023, K024, K025 are not in its grounding** |
| probes matching **zero** motifs | **19** |

## The mechanism, stated exactly

> **An arc whose content does not match one of 18 regex sets frozen on 2026-07-01 is invisible to
> the atlas by construction.**

And the instrument is **self-sealing**: a survey with 18 labels will always report the corpus
concentrated in 18 things, and can never report a nineteenth. *"Nothing new is recurring"* is its
output regardless of the input.

**The decisive instance:** `B798 — THE ALGEBRAICITY FALSIFIER'S POWER BOX` matches **zero** motifs.
That arc defines **the programme's own current falsifier** (the rung-1 algebraicity target, its
digit budget and basis list). The instrument built to detect what recurs cannot see the thing the
programme is currently betting on. Also invisible: **B537** (a PROVED result), **B770** (the closure
census), **B793** (blocked on an architectural finding about the solver), **B744**, **B679**.

The other 13 invisible probes are the early `B19–B51` block whose titles are bare *"Findings"* — the
same stratum Review 33 found carries an explicit `## Verdict` block instead. Two different blind
spots, one instrument.

## Why this answers the owner's report rather than merely restating it

The feeling *"there's more in the object, and our campaigns keep missing it"* has a cause that is
**not** entropy, carelessness, or attention. It is that **the survey instrument's vocabulary was
frozen 28 days and 409 arcs before the survey was run.** Campaigns designed with it were designed to
find what was already named.

This is **E34 (apparatus-inflation), method layer, one level deeper than recorded**: not the
*method's* recurrence read as the object's unity, but the **lexicon's granularity read as the
object's granularity.**

## What it does NOT show

The corpus may still be genuinely concentrated — 18 labels chosen well could track 18 real motifs.
This arc does **not** prove the object has more than 18 facets. It proves **the instrument could not
tell us either way**, and that at least 6 substantive recent arcs fall outside it. Distinguishing
those two requires a lexicon derived from the corpus rather than authored ahead of it.

## The fix, and it is cheap

A gate: **the count of zero-motif probes must not grow.** If new arcs stop matching the lexicon, the
lexicon is stale — mechanically checkable, unlike the semantic layers above it. Implemented as
`atlas-lexicon-current` with the current 19 as the ceiling.

That does not make the atlas able to discover new motifs. It makes its **going blind** detectable,
which is the property it lacked.

## Residual

- **Derive a lexicon from the corpus** (term extraction over 734 FINDINGS) and diff it against the
  18. The gap is the list of things the programme learned and never named.
- The 6 substantive invisible arcs want motifs of their own — starting with whatever names
  **B798**'s falsifier machinery.

`scripts/forcing/build.py` (B805) · lock `tests/test_b806_lexicon.py`

---

## POSTSCRIPT — the finding demonstrated itself within minutes

The `atlas-lexicon-current` gate was written, registered, and **fired on its first run — on B806**.

The count went **19 → 20** the moment this arc was banked, because **the arc documenting the
lexicon's blindness matches none of the lexicon's 18 motifs.** It is invisible to the instrument it
is about.

The ceiling is therefore recorded as **20**, as a **high-water mark requiring a deliberate act to
raise**, not a budget to spend. The alternative — widening the lexicon now — would change every
number in this arc while the arc was being written, so it is registered as the residual instead.

**The full invisible-and-recent set is now: B744, B770, B793, B798, B806.** Five substantive arcs
from the last weeks, including the programme's own falsifier definition and now its own instrument
audit, all outside the vocabulary of the instrument that surveys the corpus for what recurs.

## Residual, sharpened

**Widen the lexicon** — and do it by *deriving* terms from the corpus rather than authoring them
ahead of it, or the next freeze begins the day it is written. The gap between a corpus-derived
lexicon and the current 18 **is the list of things the programme learned and never named**, which is
the closest thing to a direct answer to the owner's question.

---

# THE RESIDUAL, DISCHARGED — the programme has TWO disjoint vocabularies, and neither names its centre

The residual asked: derive a lexicon *from* the corpus and diff it against the 18; the gap is what
the programme learned and never named. Done.

## Deriving it required fixing this seat's own instance of the same error

A first extractor ranked by document frequency and returned **process vocabulary**: *exactly* (69 %
of arcs), *verdict* (55 %), *frontier* (50 %), *independent*, *genuine*, *confirmed*. It was
measuring **how the programme writes**, not what it studies — the third instance of the vocabulary
trap in one session, this time in the tool built to detect it.

The fix is a different statistic. **A motif is bursty** — concentrated in a subset of arcs.
**Register is uniform** — one mention in nearly every arc. Scoring on *intensity* (mean occurrences
in the arcs that use a term) inside a *non-universal* document-frequency band collapses 722 noisy
candidates to **7**.

| candidate | arcs | intensity | in the 18? |
|---|---|---|---|
| **observer** | 48 | **4.1** | **absent** |
| **meeting** | 17 | 4.0 | **absent** |
| **cascade** | 16 | 3.6 | **absent** |
| **reducible** | 40 | 3.1 | **absent** |
| **principal** | 99 | 3.0 | **absent** |
| **hearing** | 81 | 3.0 | **absent** |
| handoff | 125 | 3.0 | *(process, not a motif — correctly rejected on reading)* |

## The finding, and it is sharper than "the lexicon is stale"

**The programme carries two disjoint anatomies of the same object.**

- `kill_graph`'s **11 faces** — being, hearing, meeting, children, congruence-tower, sln-tower,
  coupled-double, mtc-overlay, emittance-eigenvalues, emittance-lengths, infinite-hecke
- the atlas's **18 motifs** — figure_eight, trace_map, kappa, metallic, dickson_tower, eisenstein,
  golden, torsion, quasicrystal, symplectic, wrt_quantum, apolynomial, z3_generation, amphichiral_cp,
  five_web, hyperbolicity_split, lorentzian, firewall

> **Overlap: ZERO. Not one of the eleven faces is an atlas motif.**

The instrument that classifies the object's *negatives* by face, and the instrument that surveys the
object for *recurring motifs*, share **no vocabulary at all**. Each is internally coherent; together
they cannot be joined, which is why an arc can be attached in one and invisible in the other.

**And the centre is missing from both.** `observer` scores the **highest intensity of any derived
candidate (4.1 across 48 arcs)** and appears in neither vocabulary — while B733 proved the observer
menu **bounded and depth-independent** and B766 proved it **RANK-SATURATED at exactly 3**. That is
the programme's deepest late structural result, and **no survey instrument can see it.**

## The direct answer to the question that prompted this

*"What did the programme learn and never name?"*

**It learned that the object has an anatomy (11 faces) and an observer (saturated at 3 bits) — and
named neither in the instrument it uses to check whether anything is being lost.**

That is the mechanism behind *"later we realized there's more in the object"*, stated completely:
not that the work was missed, but that **the two things most recently learned are the two things the
survey cannot represent.**

## What follows (registered, not done here)

Unifying the vocabularies is a change to two shared instruments and would silently move every number
in this arc and in the atlas. It needs its own sealed prereg, not a patch appended to the arc that
found the problem. The **7 candidates and the zero-overlap measurement are the input to it.**
