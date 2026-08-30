# B1218 — THE OPEN-CLAIM SWEEP: `already_banked` stops needing to be aimed, and finds two more locks called open

**Status: banked (frontier). Verdict INSTRUMENT+PROVED** (the instrument, with two-directional
bite control; two confirmed stale rows repaired; two candidates adjudicated as NON-findings).
Owner-directed: *"run it."* `verification/reproduce.sh` → `REPRODUCES`. Gate 5 n/a.

## Why this exists

`scripts/checks/already_banked.py` is mandatory before writing MISSING / OPEN / "never run",
and it works — its own docstring records four times the record was called open when it was
already proved. Its limit is that **it must be aimed**: it only ever checks the claim a seat
happened to think of.

On 2026-08-30 the owner asked *"are u sure theyre not lost, make sure."* Aiming it by hand at
five hand-picked rows found **five locks** (B1217-adjacent; see the Section IX and Section X
repairs at `5ec66cf0` and its successor). The question that follows is the one this instrument
answers: **how many more are there when nobody is aiming?**

## The instrument (`scripts/checks/open_claim_sweep.py`)

Extract every claim asserting **current** openness from the live normative surfaces; scan all
1122 arcs for a SETTLED arc that already decided it; rank by **shared-term IDF**, not raw count.

Three design decisions, each load-bearing:

1. **IDF, not term count.** An unweighted count just surfaces whichever arc says "the object"
   most often. Rare shared terms carry the signal.
2. **The tautology exclusion.** `docs/views/VERDICT_LEDGER.md` is a *generated index of arcs*;
   every row matches its own arc by construction, so including it measures nothing. Excluded.
   (Unfiltered, it dominated the top of the first run — 526 hits.)
3. **History lines are not open claims.** A unit carrying a resolution marker (CLOSED, PROVED,
   FALSIFIED, …) is a record, not a live assertion; and a unit that already cites the matching
   arc is by definition not lost. Both dropped. **526 → 46.**

## Bite control (MB12, both directions — the instrument must be able to report nothing)

- **POSITIVE, 5/5**: each of the five hand-found locks, described in the *surface's own words*,
  must retrieve its own resolving arc. All five rank **#1** (B1112, B1109 ×2, B1141, B1110).
- **NEGATIVE**: off-corpus text ("the quarterly beverage procurement schedule for the office
  kitchen refrigerator") scores **0.00** against every settled arc, versus a 25.0 threshold.

An instrument that could only fire is worth nothing; this one can be silent, and is.

## THE FINDINGS — 46 candidates, adjudicated by hand

### Confirmed stale, repaired (2)

**1. L175 — the h = 0 locus. CLOSED, and the row still read "typed OPEN."**
The row states its own success condition: *"If the vanishing locus is a property of the WORD,
independent of channel and listener, that is a fourth theorem in the gate's family — one run."*
**B1110 (PROVED), F5: "L175 CLOSES."** It **is** a word property — six channels spanning every
listener sector share the identical **28-word set over 1364 words**, separation 5×10⁹, no
borderline, odd-u3 matching B1103's exact 28 — **so the fourth theorem exists**. The mechanism
was found too, which the row never asked for: the 28 are exactly the **diagonal-free weld
matrices** (max|diag| 1.2e-15 vs ≥0.30 for every other word, fifteen orders of separation).
*This is the same lock as Section X's, on a second surface that the Section X repair did not
touch* — which is precisely the failure mode: one arc, N surfaces, one updated.

**2. L57 — the theta-characteristic. ANSWERED, negatively, and re-posed.**
The row asks *"does the pairing geometry force a characteristic? Forced ⇒ invariant; choice ⇒
decoration."* **B364 (NEGATIVE)** answers it: *"the square theta family is equally T-stable and
carries the canonical lift's multiplier, so T-stability forces NEITHER lift"* — the two lifts
are two polarizations, and L57 becomes a **spin-structure** question. Two further PROVED arcs
bear on the row (B359 pair-specific/parity-selective seam form; B363 the seam is two-sided,
all 225 one-sided twists dark). **The row cited none of the three.**

> **Explicitly NOT claimed**: that L57's re-posed spin-structure question is the same ℤ/2 that
> B1141 assigns. A boundary theta-characteristic and a 3-manifold spin structure are related
> but not identified, and that identification has not been computed. Recording the adjacency
> without the claim is the point.

### Adjudicated NON-findings (2) — the instrument's honesty, stated

**`THE_SPINE.md` B171 `OPEN` beside B172/B173 `PROVED`.** *Not* staleness. THE_SPINE is
**generated** from each arc's own verdict file; B171's cell genuinely was open and B172/B173
are its successors. Ordinary succession. A view that reports arcs faithfully is not a stale
surface, and the sweep must not be allowed to manufacture findings out of it.

**`B921-6` the Cell-3 spin fork.** B1141 selects *which* spin structure the beat picks; B921-6
asks whether **spinor-Hejhal is authorized** by the cusp-data distinction. Related, not the
same question. Enrichment (the run now has a canonical target), **not** a closure.

The remaining ~42 are same-topic co-occurrence: a live claim about a subject matching settled
arcs about that subject. Expected, and not evidence of anything.

## What this measures

B1188/B985 put a number on the burial: object-faces recover at 79–100%, **relation-faces at
6–19%**, with 132 PROVED on-theme arcs off every live surface. This instrument turns the
hand-aimed check into a sweeping one, so the next stale row is found without the owner having
to suspect it first. **Standing use: run before any review, and before writing "open" anywhere.**

Scope, honestly: it searches the surfaces named in `SURFACES` and ranks by lexical overlap. It
cannot find a lock whose resolving arc shares no vocabulary with the claim, and it does not
adjudicate — every hit above was read and decided by hand. It narrows the reading, it does not
replace it.

## The instrument tripped its own lock — the fifth instance of a known class

On first run of the banked arc, the negative control **FAILED at 43.40** against a 6.0 bar, and
B1110 dropped from rank #0 to #1. Cause: **this arc's own FINDINGS quotes its own test phrase**
(and every lock it reports), so the corpus scan matched B1218 against itself.

This is the **self-documenting-instrument class** — an arc documenting a lock trips that lock —
and the repo has met it four times before. The fix is the established one, already written into
`already_banked.py`'s own `exclude` parameter and quoted here verbatim from its source:

> *"a self-documenting instrument quotes its own test phrases, so its arc matches them --
> excluding it is honesty, not evasion."*

`SELF = "B1218_open_claim_sweep"` is dropped from the corpus. Bite control then passes both
directions (5/5 positive at rank #0; negative 0.00). Worth stating plainly: the failure was
**the control working**. Had the negative control been decorative, this would have shipped with
the instrument silently matching itself and inflating every score.
