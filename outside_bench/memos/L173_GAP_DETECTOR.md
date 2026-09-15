# THE PER-GAP OCCUPANCY DETECTOR — built, and it overturns the diagnosis it was built to fix: the "volatility" is a real discontinuity, and the 6−5 remainder is a one-ended-detector artefact
## (outside bench memo 142, 2026-08-29; certificate `certificates/l173_gap_detector.py`, GREEN; the instrument upgrade B1095 named and memo 137 made GATING)

**Why it was gating.** memo 137 conceded two of the three parts of L173's
differential and found that **the localization split alone survives**.
B1095 had already flagged its own detector as volatile and named the fix:
*"a per-gap occupancy detector (gap-interior energy + localization length)
is the named instrument upgrade before any window-measure claim."*
**A differential living entirely in localization cannot be measured by a
detector that flips on localization thresholds.** So it was built.

**Criterion fixed before running** (each clause in the state's *own* scale,
not an absolute window): **E1** localized — participation ratio
PR = 1/Σ|ψ|⁴ < N/10; **E2** at a boundary — centre of mass within **PR** of
an end; **E3** in a gap — smaller adjacent level spacing > 10× the median.

## THE PREREGISTERED OUTCOME FIRED **D-VOLATILE**

The old detector reads **(5,9)** below α and **(5,6)** at α and above.
The new one reads **(7,10)** below and **(7,7)** at and above. **It flips
too.** Reported as preregistered, **not re-tuned after seeing it.**

But both detectors hold the **right** hand fixed and move the **left** by
exactly **3** — which points at the chain, not the instrument.

## ⚠ FINDING 1 — B1095's DIAGNOSIS IS CORRECTED: there is no detector defect here

| | across ρ = α |
|---|---|
| right-hand **word** | **identical — 0 sites differ** |
| left-hand **word** | **differs at exactly 2 sites: {0, 1}** |

**The left chain is genuinely discontinuous at α**, at exactly the two
cut-adjacent letters. **The system is physically different on the two
sides**, and both detectors reported that correctly. **A detector that
read the same on both sides would be wrong.**

> **This is not "a detector volatile near transitions." The named
> instrument upgrade was aimed at a defect that is not there.**

## ⚠ FINDING 2 — THE 6−5 REMAINDER IS A ONE-ENDED-DETECTOR ARTEFACT

At ρ = α the new detector selects **7 states in each hand**, and their
energies are **identical sets**:

−1.158405, −0.916005, −0.503913, −0.306406, +0.470419, +2.030320, +2.298699

and **for every one of them the two hands bind it at OPPOSITE ENDS**:

| E | right com | left com |
|---|---|---|
| −1.158405 | 981.1 | 4.9 |
| −0.916005 | 17.5 | 968.5 |
| −0.503913 | 2.9 | 983.1 |
| −0.306406 | 983.4 | 2.6 |

> **The split is 7–7, EVEN.** Under the detector **B1095 itself
> prescribed**, the *"6 − 5 = 1 parity remainder"* **disappears.**

**The mechanism, exhibited rather than inferred:** B1095's detector sums
|ψ|² over the **first 20 sites only** — it examines **one** of the chain's
**two** ends and is **blind to states bound at the far end**. On a
reversal pair, a state bound *near* in one hand is bound *far* in the
other — **exactly the states it cannot see.** **A one-ended detector on a
reversal pair manufactures an asymmetry.**

## WHAT THIS DOES TO L173

B1095's *formulation* is **confirmed and strengthened**: *"the energies
are P-invariant (forced); the localization is P-equivariant (free)"* — the
new detector exhibits it perfectly, same seven energies, each bound at
opposite ends.

**But its NUMBER is not robust.** memo 137 identified the complementary
split as **the only surviving part** of L173's differential. That split's
**asymmetry is detector-dependent**: 6–5 on a one-ended detector, **7–7**
on a two-ended one.

> **So the last surviving part of L173's differential is now itself in
> question, and L173 remains unsealable — but for a different and better
> reason than memo 137 gave.** The gating question is no longer *"build
> the detector"*; it is **"which detector is correct, and is any
> asymmetry left once both ends are counted?"**

**Fences.** My thresholds (N/10, 10×median) are choices, preregistered but
not unique; a third detector could differ again, **which is precisely the
point — the asymmetry is not robust across defensible detectors.** N = 987
only; no laboratory datum touched, no experimental comparison made.
Gate 5 untouched.
