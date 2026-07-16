# HANDOFF — THE COMPARATOR LANE (to the web seat; campaign B648, seal a463c6aa)

**Your role in Phase C: extract the held-out target from the pinned
dataset, seal your extraction, then — and only then — receive the
prediction, verify its hash, compute the sealed statistic, and report
the outcome. You do NOT see the prediction's value or derivation
before your extraction is sealed. Your lane is deliberately
arithmetic-light: the sealed design carries all the weight.**

*(This handoff is self-contained — you do not need repo access. The
design document will arrive as a sealed file with its sha256.)*

## The state you inherit (one paragraph)

The calibration campaign you reviewed (your four amendments and the
other seat's fixes are all in the sealed text) has passed GATE B: the
object's interaction grammar has exactly ONE free constant — a
discrete binary choice (the Galois branch of the golden character).
The predictor seat calibrates that bit from a named calibration
observable and seals a zero-parameter prediction for a second, held-out
observable, hash-first. You grade it.

## Your task, in strict order

1. **Receive the sealed C2 design** (from the owner; verify its stated
   sha256 by recomputing on the file you received). It names: the
   channel; the held-out observable; the dataset NAME and RELEASE
   VERSION you must use (pinned — the NuFIT-flip lesson is why); the
   statistic; the success criterion with its pre-committed
   false-positive rate; the look-elsewhere multiplicity.
2. **Extract the target:** from EXACTLY the pinned dataset version
   (no substitutions — if that version is unavailable to you, STOP and
   report; do not use a newer release), record the held-out
   observable's value and uncertainty. Write your extraction note
   (value, uncertainty, the dataset citation string, access date) and
   give the owner its sha256 BEFORE receiving anything further. This
   is your seal.
3. **Receive the prediction hash** (from the owner), then the
   prediction file. Verify sha256(file) = the hash you were given
   FIRST; if mismatch, STOP and report — do not read further.
4. **Compute the sealed statistic** exactly as the design specifies —
   no alternative statistics, no re-binning, no "also interesting"
   side comparisons (the one-shot rule: this is the only comparison
   under this license).
5. **Report:** the statistic's value, the criterion's verdict
   (pass/fail at the pre-committed rate), and NOTHING interpretive —
   the adjudication seat writes the interpretation under the sealed
   two-outcome rules (a miss is banked with equal prominence as a hit;
   your report is identical in format either way).

## Binding rules

- Use only the pinned dataset version; record any anomaly rather than
  working around it.
- Your exposure line: state plainly what SM-value work you have done
  in prior sessions (the design already accounts for it — blinding
  here rests on the ORDER of seals, not on pretended ignorance).
- No reopening: whatever the outcome, no second channel, no second
  statistic, no "let me just check" — a fresh owner directive under
  the stopping rule is the only path to any further comparison.
- Format: one document — EXTRACTION.md (sealed first) + REPORT.md
  (after step 5), each with its own sha256 stated.

## Why you

Your lane needs protocol rigor and careful sourcing, not heavy
computation — the design was amended (partly by you) to make the
comparator's arithmetic simple and checkable by hand. Your prior
review caught the adrenaline-spike failure mode this order of
operations exists to prevent; you are grading under the rules you
helped write.
