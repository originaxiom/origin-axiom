# B967 — L139 EXECUTED: the retraction sweep, and what it found on its first run

**Date:** 2026-08-08 · **Seat:** cc (banking) · **Lane:** INSTRUMENT / GOVERNANCE.
Gate 5 untouched. **Closes the other half** of the gap the owner named.

---

## 1. The rule

> **Retracting a claim does not retract its instances.** A retraction is **not complete**
> until its phrase is registered in `docs/RETRACTED_PHRASES.md` **and the sweep is clean.**

Machinery: `docs/RETRACTED_PHRASES.md` (the registry), `scripts/checks/retraction_sweep.py`
(the sweeper, over **all 2,210 tracked `.md` files**), gate `retraction-sweep`, and a
`docs/PRACTICES.md` row — registered both directions.

**Use vs mention** is the whole difficulty, and it is handled explicitly: a retracted phrase
**may** appear inside a retraction record, a correction banner, a quotation of a former
claim, or a test enforcing its absence. Incoming panel reports (`PRIOR_ART_*.md`,
`O3_PRIOR_ART.md`, `DRAFT_FINDINGS.md`) are **evidence, not our claims**, and are exempt on
the same principle as another seat's scripts.

## 2. WHAT THE FIRST RUN FOUND — and it justifies the whole exercise

**11 violations across 2,210 files**, and the important one was not a stray phrase:

> **B962's own FINDINGS still asserted BOTH claims B964 had retracted — in its TITLE and in
> two body sections — with no correction banner at all.**

I banked B964 as a separate arc and **never went back to mark its source.** A reader arriving
at B962 would have found *"nobody's object supplies a VEV, the route stops one step short"*
stated as findings, with nothing to warn them. **That is precisely the failure L139 was
registered to catch, and it existed in the corpus for four hours before the sweeper existed
to see it.**

Fixed properly rather than cosmetically:

- **the title retitled** (it asserted both retracted claims);
- **a banner added**, naming both retractions and listing what still stands;
- **both body sections marked inline** — heading warnings plus struck-through corrections at
  the exact sentences, because a banner at the top does not stop someone quoting §2.

The remaining hits were the correction machinery itself (mentions) and incoming panel
reports; the cue list and exemptions were widened to match, each widening justified by an
inspected case rather than to make the number go down.

## 3. Non-vacuity — demonstrated

Planting *"The object does not supply a VEV."* into `docs/OPEN_PROBLEMS.md` makes the sweep
**fire**; removing it makes it **clean**; the file was restored byte-identical.

## 4. What is registered, and what deliberately is not

**Registered (5):** the two B964 retractions; B943's priority sentence; B941's "golden
power"; B963's "no intermediate regime".

**Deliberately NOT registered**, with reasons recorded in the registry:
- *"chirality = the extremal-KMS / Galois label"* (B942) — registering it would fire on
  B723's own correction banner, which is the correct treatment.
- *"the Standard Model algebra"* (B950) — ordinary English used correctly in many places; a
  grep cannot distinguish those. **B892's banner and the amended LAW_MAP row are the correct
  treatment.**

> **This asymmetry is the registry's main limitation and is stated rather than hidden: it can
> only police wording specific enough to be unambiguous. Broad phrases need banners, not
> greps.**

## 5. Honest limits

1. **Phrase-exact and case-insensitive only.** A paraphrase of a retracted claim passes
   silently. This raises the floor; it does not certify the corpus.
2. **The mention-cue list is heuristic.** Each cue was added because an inspected case
   demanded it. A mention phrased without any cue would be a false positive; a *use* that
   happens to contain a cue would be a false negative.
3. **Registration is manual.** The gate enforces that registered phrases stay dead; nothing
   enforces that a new retraction gets registered — that is the practices row, i.e. a human
   obligation.
4. `.md` only. Code comments and JSON verdict lines are not swept.

---

**Verdict: INSTRUMENT.** L139 executed. The sweep exists, is gated, is proven able to fail,
and on its first run found a retraction that had never reached its own source — exactly the
failure it was built for. **Both halves of the gap the owner identified now have machinery:
`lawmap-scope` for the compression leak, `retraction-sweep` for the instance leak.** Neither
removes the need to read.
